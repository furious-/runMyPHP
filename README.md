# runMyPHP
Run your PHP code directly on SublimeText 3 and see the results into output panel

## Installation
See bellow how to install this plugin

### Install using git
To install this Plugin via git, simply browse to your 'Packages' folder like this:

**for Windows**
> cd %APPDATA%/Sublime Text 3/Packages

**for OS X**
> cd ~/Library/Application Support/Sublime Text 3/Packages

**for Linux**
> cd ~/.Sublime Text 3/Packages

**for Portable Installations**
> cd PATH_TO_PORTABLE_INSTALLATION/Sublime Text 3/Data/Packages

**and clone this repository**
> git clone https://github.com/furious-/runmyphp


### Install manually
* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to 'runMyPHP'
* Copy the folder to your Sublime Text 3 'Packages' directory

## Settings
The following settings are available and are optional, but the default settings should be changed
	
	{
		"runmyphp_binary_path": "",
		"runmyphp_with_tmp_file": true
	}

**runmyphp_binary_path**: The FULL path to your PHP binary, for portable installations use the root path without the drive letter, like: "/root/full_path/to/php"

**runmyphp_with_tmp_file**: If you want to always use a temporary file to execute partial/full (not saved) code, that way you can debug errors and find the correct line of the problem. (Syntax check always use temp files)

## Usage
This plugin only works when the PHP syntax is active, check bellow the shortcuts, or use the context menu with rightclick:

> **Ctrl+Shift+X** - Execute the selected piece of code or the entire code.

> **Ctrl+Shift+Alt+X** - Same above, but execute the entire code instead.

> **Ctrl+Shift+C** - Execute the current opened file. (It will warn you to save the file if it was changed before execute)

> **Ctrl+Shift+L** - Check the for Syntax errors in the selected or entire code.

> **Ctrl+Shift+Alt+L** - Same above, but ignores selection and uses the entire code instead.

> **Ctrl+Shift+Alt+C** - Same thing above, but this time uses the current opened file for Syntax-check

## Release Notes
#### 1.3
* Added more shortcuts
* Added "Syntax-Check" (lint) option
* Added "Run PHP file" option
* Added default sublime-settings
* Better thread PHP execution
* Better output real-time

#### 1.2
* Improved output real-time
* Improved thread PHP execution

#### 1.1
* Added threading-mode
* Improved plugin code

#### 1.0 (beta)
This is an initial version, so can have some bugs. And it's my first time making a plugin for ST3, and my second day programming python :P

### Contact
If you liked this plugin, let me know:

* Twitter: [@furious_](http://twitter.com/furious_)
* Website: <http://furious.cc>
