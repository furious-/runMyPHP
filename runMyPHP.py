##
# runMyPHP - SublimeText 3 plugin
# Coder: furious (github.com/furious-)
##

import sublime, sublime_plugin, threading, subprocess, os, base64

class runMyPHP(threading.Thread):
	def __init__(self, code):
		self.code = code
		self.view = sublime.active_window().active_view()
		threading.Thread.__init__(self)

	def run(self):
		self.execute(self.code)

	# process and return encoded code
	def process(self, rawcode):
		return "eval(base64_decode('" + base64.encodestring(bytes(rawcode.replace('<?', '').replace('?>', ''), 'ascii')).decode('ascii').replace("\n", '') + "'));"

	# execute code, print output
	def execute(self, code):
		if self.view.settings().has('php_path'):
			path = os.path.realpath(self.view.settings().get('php_path')) + os.sep
		else: path = ''

		command = '"%(path)sphp" -r "%(code)s"' % {'path': path, 'code': self.process(code)}

		sublime.status_message('Processing your code...')
		#self.output({"output": "Processing...", "title": "runMyPHP"})
		php = subprocess.Popen(command, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
		#result, err = php.communicate()
		#result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
		result = ""
		for line in iter(php.stdout.readline, ''):
			result += str(line)
			self.output({"output": result})
		sublime.status_message('Done.')

	# output workaround, thanks ST3 ¬¬'
	def output(self, args):
		self.view.window().run_command("runmyphpoutput", args)

class RunmyphpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		
		selection = ""
		for sel in self.view.sel():
			selection += self.view.substr(sel)

		if len(selection) == 0:
			selection = self.view.substr(sublime.Region(0, self.view.size()))
		
		if self.show():
			thread = runMyPHP(selection)
			thread.start()
		else:
			sublime.status_message('PHP code not detected.')

	def show(self):
		view = sublime.active_window().active_view()
		if view:
			return view.settings().get('syntax') == 'Packages/PHP/PHP.tmLanguage'

# output workaround, thanks ST3 ¬¬'
class RunmyphpoutputCommand(sublime_plugin.TextCommand):
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
		