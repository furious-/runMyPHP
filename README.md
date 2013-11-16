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
> cd ~/.Sublime Text 2/Packages

**for Portable Installations**
> cd PATH_TO_PORTABLE_INSTALLATION/Sublime Text 3/Data/Packages

**and clone this repository**
> git clone https://github.com/furious-/runmyphp


### Install manually
* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to 'runMyPHP'
* Copy the folder to your Sublime Text 3 'Packages' directory

## Settings
The following settings are available and optional, but the default settings should be mostly what you want if you install this plugin
	
	{
		"php_path": "YOUR_PHP_BINARY_PATH",
	}

**php_path**: The path to your PHP binary (fallback: "php"-call)

## Usage
If the PHP syntax is active, select the piece of code you want to get an output from, or if you want the whole file be used left the selection blank, and press this shortcut:

	Ctrl+Shift+X

Rightclick in the document and you can do the same above

## Release Notes
This is an initial version, so can have some bugs. And it's my first time making a plugin for ST3, and my second day programming python :P

### Contact
If you liked this plugin, let me know:

* Twitter: [@furious_](http://twitter.com/furious_)
* Website: <http://furious.cc>