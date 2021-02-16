#!/usr/bin/python

import sys

PAGE_DIR = "./pages"
COLORS = True
SHOW_META = False
VERSION = "0.1.0"


def color_func(*colors):
    if COLORS:
        prefix = ""
        for color in colors:
            prefix += f"\033[{color}m"
        return lambda text: f"{prefix}{text}\033[0m"
    else:
        return lambda text: text


def read_page(query):
    page_path = f"{PAGE_DIR}/{query}.md"
    with open(page_path, "r") as file:
        page_data = file.read()
    return page_data


def parse_md(raw_text):
    formatted = ""
    lines = raw_text.split("\n")

    for line in lines:
        if line != "":
            formatted += parse_md_line(line)

    return formatted

def parse_md_line(line):
    global SHOW_META
    f_title = color_func("96", "1")
    f_subtitle = color_func("96", "4")
    f_shortcut = color_func("92")
    f_desc = color_func("32")
    f_meta = color_func("90", "3")

    if len(line) > 0:
        if line[0] == ">":
            return f_meta(line) if SHOW_META else ""
        elif line[0] == "#":
            return f"\n{f_title(line.lstrip('# '))}\n"
        elif line[0] == "$":
            return f"\n{f_subtitle(line.lstrip('$ '))}\n"
        else:
            no_spacing = line.replace("  ", "")
            parts = no_spacing.split("{{")
            shortcut = f_shortcut(parts[0][1:])
            desc = f_desc("".join(parts[1:])[:-3])
            return f"\t{shortcut: <30}{desc}\n"
    return ""


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        print(parse_md(read_page(arg)))
    else:
        show_help()

def show_help():
    global VERSION
    print(f"shortcut.py\t{VERSION}")
    print("Usage: shortcut.py [PAGE_NAME]\n")
    print("A python-based interface for shortcut-pages on Github.")

if __name__ == "__main__":
    main()