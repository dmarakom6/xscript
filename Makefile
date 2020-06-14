# xscript/Makefile
# xscript makefile

COLOR_END := \033[0m"
COLOR_COL := "\033[32m
SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.0 Makefile\n"
	@echo "commit  commit changes and push"
	@echo "help    show this help"
	@echo "install install xscript"
	@echo "test    run a xscript demo"
	@echo "up      upgrade xscript from Github and install"

commit: Makefile LICENSE README.md setup.py docs/ script/ $(SOURCE)
	@echo $(COLOR_COL)[Start committing...]$(COLOR_END)
	@echo $(COLOR_COL)[Adding changes...]$(COLOR_END)
	@git add .
	@echo $(COLOR_COL)[Committing changes...]$(COLOR_END)
	@git commit -m `date +%Y-%m-%d`
	@sleep 3s
	@echo $(COLOR_COL)[Pushing changes...]$(COLOR_END)
	@git push -u origin master
	@echo $(COLOR_COL)[Committing successfully]$(COLOR_END)

install: Makefile setup.py
	@echo $(COLOR_COL)[Installing packages...]$(COLOR_END)
	@-pip3 install -U prettytable mkdocs
	@echo $(COLOR_COL)[Installing xscript...]$(COLOR_END)
	@python3 setup.py install
	@-rm -rf build/
	@echo $(COLOR_COL)[Installing completely]$(COLOR_END)

test: Makefile script/hello.xs $(SOURCE)
	@echo $(COLOR_COL)[Testing xscript...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_COL)[Testing completely]$(COLOR_END)

up: Makefile setup.py $(SOURCE)
	@echo $(COLOR_COL)[Upgrading...]$(COLOR_END)
	@git pull
	@echo $(COLOR_COL)[Installing packages...]$(COLOR_END)
	@-pip3 install -U prettytable mkdocs
	@echo $(COLOR_COL)[Installing xscript...]$(COLOR_END)
	@python3 setup.py install
	@-rm -rf build/
	@echo $(COLOR_COL)[Testing xscript...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_COL)[Upgrading completely]$(COLOR_END)
