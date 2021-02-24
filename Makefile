TARGET := /opt/shortcut-py
SYM := /usr/local/bin/shortcut

.PHONY: install uninstall

install:
	mkdir -p $(TARGET)
	mkdir -p pages/
	cp -r pages/ $(TARGET)
	cp shortcut.py $(TARGET)
	cp README.md LICENSE $(TARGET)
	mkdir -p /usr/local/bin
	ln -s $(TARGET)/shortcut.py $(SYM)
	@echo "Installed."

uninstall:
	rm -f $(SYM)
	rm -fr $(TARGET)
	@echo "Uninstalled."