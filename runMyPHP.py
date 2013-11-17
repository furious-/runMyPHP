##
# runMyPHP - SublimeText 3 plugin
# Version: 1.3
# Coder: furious (github.com/furious-)
##

import sublime, sublime_plugin, threading, subprocess, os, base64, tempfile

class runMyPHP(threading.Thread):
	def __init__(self, code, lint = False, filename = None):
		self.code = code
		self.lint = lint
		self.filename = filename
		self.view = sublime.active_window().active_view()
		self.tmpfile = ''
		self.settings = sublime.load_settings("runMyPHP.sublime-settings")
		self.path = os.path.realpath(self.settings.get('runmyphp_binary_path')) + os.sep
		threading.Thread.__init__(self)

	def run(self):
		self.execute(self.code)

	# process and return encoded code
	def process(self, rawcode, base64_encode = True):
		if base64_encode:
			return "eval(base64_decode('" + base64.encodestring(bytes(rawcode.replace('<?', '').replace('?>', ''), 'ascii')).decode('ascii').replace("\n", '') + "'));"
		elif '<?' in rawcode:
			return rawcode
		else: 
			return "<?\n" + rawcode

	# execute code, print output
	def execute(self, code):

		if self.settings.get('runmyphp_with_tmp_file') or self.lint or self.filename != None:
			if self.filename == None:
				f = tempfile.NamedTemporaryFile('w', suffix = '-runMy.php', delete = False)
				f.write(self.process(code, False))
				self.tmpfile = f.name
				self.filename = f.name
				f.close()
			command = '"%(path)sphp" -%(mode)s "%(file)s"' % {'path': self.path, 'mode': 'l' if self.lint else 'f', 'file': self.filename}
		else:
			command = '"%(path)sphp" -r "%(code)s"' % {'path': self.path, 'code': self.process(code)}

		sublime.status_message('Processing your code...')
		php = subprocess.Popen(command, cwd=self.path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

		result = ""
		for line in iter(php.stdout.readline, ''):
			sublime.status_message('Still processing your code...')
			result += str(line).replace(self.tmpfile, 'your code') if len(self.tmpfile) > 0 else str(line)
			self.output({"output": result})
		sublime.status_message('Done.')
		
		if len(self.tmpfile) > 0:
			os.unlink(self.tmpfile)

	# output workaround, thanks ST3 ¬¬'
	def output(self, args):
		self.view.window().run_command("runmyphpoutput", args)

class runMyPHPCommand(sublime_plugin.TextCommand):
	def run(self, edit, lint = False, currentfile = False, entirecode = False):
		self.edit = edit
		
		selection = ""
		for sel in self.view.sel():
			selection += self.view.substr(sel)

		if len(selection) == 0 or entirecode:
			selection = self.view.substr(sublime.Region(0, self.view.size()))
		
		if self.show():
			filename = self.view.file_name() if currentfile else None
			
			if currentfile and filename != None and self.view.is_dirty():
				sublime.error_message('You must save your PHP file before anything')
			else:
				thread = runMyPHP(selection, lint, filename)
				thread.start()
		else:
			sublime.status_message('PHP code not detected.')

	def show(self):
		view = sublime.active_window().active_view()
		if view:
			return view.settings().get('syntax') == 'Packages/PHP/PHP.tmLanguage'

# output workaround, thanks ST3 ¬¬'
class runMyPHPOutputCommand(sublime_plugin.TextCommand):
	def run(self, edit, output, multiline = False, title = 'Results:', panel_name = 'runMyPHP'):
		self.edit = edit
		if multiline or "\n" in output:
			panel = self.view.window().create_output_panel(panel_name)
			panel.set_read_only(False)
			panel.set_syntax_file('Packages/Text/Plain text.tmLanguage')
			panel.insert(self.edit, panel.size(), title + "\n" + output)
			panel.set_read_only(True)
			panel.show(panel.size())
			self.view.window().run_command("show_panel", {"panel": "output." + panel_name})
		else:
			self.view.window().show_input_panel(title, output, None, None, None)