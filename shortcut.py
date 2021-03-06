#!/usr/bin/python

import argparse
from pathlib import Path
import os

HERE = os.path.dirname(os.path.realpath(__file__))
PAGE_DIR = f"{HERE}/pages"
PAGE_FILE_EXT = ".md"
VERSION = "0.3.0"
ARGS = None


class ListAction(argparse.Action):
    """
    An argparse action which lists every page then quits
    """
    def __call__(self, parser, namespace, values, option_string=None):
        list_pages()
        parser.exit()


def color_func(*colors):
    """
    Given a list of integers representing ANSI colors, returns a function which transforms text into those colors
    The resulting function takes one argument which is a string of text and returns the ANSI formatted text
    """
    if not ARGS.no_colors:
        prefix = ""
        for color in colors:
            prefix += f"\033[{color}m"
        return lambda text: f"{prefix}{text}\033[0m"
    else:
        return lambda text: text


def read_page(query):
    """
    Returns the raw page text from a given search query. (e.g. "c" -> text in "pages/c.md")
    """
    page_path = f"{PAGE_DIR}/{query}{PAGE_FILE_EXT}"
    with open(page_path, "r") as file:
        page_data = file.read()
    return page_data


def parse_md(raw_text):
    """
    Parses the raw markdown text, returning pretty output including ANSI colors (if desired)
    """
    formatted = ""
    lines = raw_text.split("\n")

    for line in lines:
        if line != "":
            formatted += parse_md_line(line)

    return formatted


def parse_md_line(line):
    """
    Parse and return one line of markdown formatted text
    """
    f_title = color_func("96", "1")
    f_subtitle = color_func("96", "4")
    f_shortcut = color_func("92")
    f_desc = color_func("32")
    f_meta = color_func("90", "3")

    if len(line) > 0:
        if line[0] == ">":
            return f_meta(line) if ARGS.meta else ""  # Parse comments starting with '> '
        elif line[0] == "#":
            return f"\n{f_title(line.lstrip('# '))}\n"  # Parse titles starting with '# '
        elif line[0] == "$":
            return f"\n{f_subtitle(line.lstrip('$ '))}\n"  # Parse subtitles starting with '$ '
        else:
            no_spacing = line.replace("  ", "")
            parts = no_spacing.split("{{")
            shortcut = f_shortcut(parts[0][1:])
            desc = f_desc("".join(parts[1:])[:-3])
            return f"\t{shortcut: <30}{desc}\n"
    return ""


def list_pages():
    """
    Print out a sorted list of all available pages excluding symlinked pages
    """
    pages = os.listdir(PAGE_DIR)
    pages.sort()
    for page in pages:
        symlink = os.path.islink(PAGE_DIR + "/" + page)
        if page[-len(PAGE_FILE_EXT):] == PAGE_FILE_EXT and not symlink: # Is it not a symlink and ends with .md?
            print(page)

def parse_arguments():
    """
    Parse the arguments provided to the program and return the resulting argparse Namespace
    """
    global ARGS
    no_color_env = "NO_COLOR" in os.environ
    parser = argparse.ArgumentParser(usage='%(prog)s [options] page', description="A python-based interface for "
                                                                                  "shortcut-pages on Github.\n")
    parser.add_argument("-V", "--version", help="Displays the current version", action="version", version=VERSION)
    parser.add_argument("-m", "--meta", help="Includes the metadata/comments included on a page", action="store_true")
    parser.add_argument("-l", "--list", help="Lists all pages accessible", action=ListAction, metavar="")
    parser.add_argument("--no-colors", help="Disables colored output", action="store_true", default=no_color_env)
    parser.add_argument("--raw", help="Show the raw, unformatted output", action="store_true")
    parser.add_argument("page", help="Name of the page to lookup")
    ARGS = parser.parse_args()


def main():
    """
    The main function which is called on start
    """
    parse_arguments()
    result = read_page(ARGS.page)
    print(result if ARGS.raw else parse_md(result))
    return 0


if __name__ == "__main__":
    main()
