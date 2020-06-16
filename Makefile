# xscript/Makefile
# xscript makefile

COLOR_END := \033[0m"
COLOR_START := "\033[32m
SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.0 Makefile\n"
	@echo "commit  commit changes and push"
	@echo "help    show this help"
	@echo "install install xscript"
	@echo "test    run a xscript demo"
	@echo "up      upgrade xscript from Github and install"

commit: Makefile LICENSE README.md setup.py docs/ script/ $(SOURCE)
	@echo $(COLOR_START)[Start committing...]$(COLOR_END)
	@echo $(COLOR_START)[Adding changes...]$(COLOR_END)
	@git add .
	@echo $(COLOR_START)[Committing changes...]$(COLOR_END)
	@git commit -m `date +%Y-%m-%d`
	@sleep 3s
	@echo $(COLOR_START)[Pushing changes...]$(COLOR_END)
	@git push -u origin master
	@echo $(COLOR_START)[Committing successfully]$(COLOR_END)

install: Makefile setup.py
	@echo -n $(COLOR_START)[Checking packages... $(COLOR_END)
	@-pip3 install -U colorama mkdocs prettytable >> .output
	@echo $(COLOR_START)Done]$(COLOR_END)
	@echo -n $(COLOR_START)[Installing xscript... $(COLOR_END)
	@python3 setup.py install >> .output
	@echo $(COLOR_START)Done]$(COLOR_END)
	@-rm -rf .output build/
	@echo $(COLOR_START)[Installing completely]$(COLOR_END)

test: Makefile script/hello.xs $(SOURCE)
	@echo $(COLOR_START)[Testing xscript...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_START)[Testing completely]$(COLOR_END)

up: Makefile setup.py $(SOURCE)
	@echo $(COLOR_START)[Upgrading...]$(COLOR_END)
	@git pull
	@echo -n $(COLOR_START)[Checking packages... $(COLOR_END)
	@-pip3 install -U colorama mkdocs prettytable >> .output
	@echo $(COLOR_START)Done]$(COLOR_END)
	@echo -n $(COLOR_START)[Installing xscript... $(COLOR_END)
	@python3 setup.py install >> .output
	@echo $(COLOR_START)Done]$(COLOR_END)
	@-rm -rf .output build/
	@echo $(COLOR_START)[Testing xscript...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_START)[Upgrading completely]$(COLOR_END)
