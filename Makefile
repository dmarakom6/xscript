# xscript/Makefile
# xscript makefile

ECHO_END := \033[0m"
ECHO_COL := "\033[32m
SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.0 makefile\n"
	@echo "help     show this help"
	@echo "install  install xscript"
	@echo "test     run a xscript demo"
	@echo "upgrade  upgrade xscript from Github and install"

install: Makefile setup.py
	@echo $(ECHO_COL)[Installing...]$(ECHO_END)
	@-pip3 install -U prettytable mkdocs
	@python3 setup.py install
	@-rm -rf build/
	@echo $(ECHO_COL)[Installing completely]$(ECHO_END)

test: Makefile script/hello.xs $(SOURCE)
	@echo $(ECHO_COL)[Testing...]$(ECHO_END)
	@-./xscript script/getver.xs
	@echo $(ECHO_COL)[Testing completely]$(ECHO_END)

upgrade: Makefile setup.py $(SOURCE)
	@echo $(ECHO_COL)[Upgrading...]$(ECHO_END)
	@git pull
	@echo $(ECHO_COL)[Installing...]$(ECHO_END)
	@-pip3 install -U prettytable mkdocs
	@python3 setup.py install
	@-rm -rf build/
	@echo $(ECHO_COL)[Testing...]$(ECHO_END)
	@-./xscript script/getver.xs
	@echo $(ECHO_COL)[Upgrading completely]$(ECHO_END)
