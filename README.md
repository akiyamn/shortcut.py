# shortcut.py
A python-based interface for [shortcut-pages](https://github.com/mt-empty/shortcut-pages) on Github.

## Usage
To see the shortcuts for a given program, type:
```bash
shortcuts.py [options] program-name-here
```

### Options
```
  -h, --help     show this help message and exit
  -V, --version  Displays the current version
  -m, --meta     Includes the metadata/comments included on a page
  -l , --list    Lists all pages accessible
  --no-colors    Disables colored output
  --raw          Show the raw, unformatted output
```

## Requirements
This program is written in Python 3.9+ however, versions as early as Python 3.6 are likely to function properly.

`make` is needed for optional installation.

## Setup
- Firstly, clone the repository to your computer
- Download the page directories `GUI` and/or `nonGUI` from the [shortcut-pages](https://github.com/mt-empty/shortcut-pages) repo
- Move the individual pages into a directory called `pages` in the shortcuts.py root folder.
An automated process is in the pipeline.
  
### Optional Install
If you would like to install shortcut.py (i.e. move to a `$PATH` directory) 
rather than use a script you can:

`make install` to install the program

`make uninstall` to uninstall the program


## To do
- Automated initial installation setup
- Automated way of updating pages on command
- ~~List all available pages~~
- Config file for settings (maybe)
- ~~Fix absolute vs relative path issues~~
