# xscript/Makefile
# xscript makefile

COLOR_END := \033[0m"
COLOR_START := "\033[32m
SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.0 Makefile\n"
	@echo "demo        run xscript demo"
	@echo "deploy      commit source and push"
	@echo "deploy-docs commit docs and push"
	@echo "docs        show xscript docs"
	@echo "help        show this help"
	@echo "install     install xscript"
	@echo "upgrade     upgrade xscript from Github and install"

demo: Makefile script/hello.xs $(SOURCE)
	@echo $(COLOR_START)[Running demo...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_START)[Done]$(COLOR_END)

deploy: Makefile LICENSE README.md setup.py docs/ script/ $(SOURCE)
	@echo $(COLOR_START)[Start deploying...]$(COLOR_END)
	@echo $(COLOR_START)[Adding changes...]$(COLOR_END)
	@git add .
	@echo $(COLOR_START)[Committing changes...]$(COLOR_END)
	@git commit -m `date +%Y-%m-%d`
	@sleep 1s
	@echo $(COLOR_START)[Pushing changes...]$(COLOR_END)
	@git push -u origin master
	@echo $(COLOR_START)[Deploying successfully]$(COLOR_END)

deploy-docs: Makefile docs/ docs/mkdocs.yml docs/docs
	@echo $(COLOR_START)[Start deploying...]$(COLOR_END)
	@cd docs/; mkdocs gh-deploy --message `date +%Y-%m-%d`
	@echo $(COLOR_START)[Deploying successfully]$(COLOR_END)

docs: Makefile docs/ docs/mkdocs.yml docs/docs/
	@echo $(COLOR_START)[Running mkdocs...]$(COLOR_END)
	@cd docs/; mkdocs serve
	@echo $(COLOR_START)[Done]$(COLOR_END)

install: Makefile setup.py
	@echo -n $(COLOR_START)[Checking packages... $(COLOR_END)
	@-pip3 install -U colorama mkdocs prettytable >> /dev/null
	@echo $(COLOR_START)Done]$(COLOR_END)
	@echo -n $(COLOR_START)[Installing xscript... $(COLOR_END)
	@python3 setup.py install >> /dev/null
	@echo $(COLOR_START)Done]$(COLOR_END)
	@-rm -rf build/
	@echo $(COLOR_START)[Installing completely]$(COLOR_END)

upgrade: Makefile setup.py $(SOURCE)
	@echo $(COLOR_START)[Upgrading...]$(COLOR_END)
	@git pull
	@echo -n $(COLOR_START)[Checking packages... $(COLOR_END)
	@-pip3 install -U colorama mkdocs prettytable >> /dev/null
	@echo $(COLOR_START)Done]$(COLOR_END)
	@echo -n $(COLOR_START)[Installing xscript... $(COLOR_END)
	@python3 setup.py install >> /dev/null
	@echo $(COLOR_START)Done]$(COLOR_END)
	@-rm -rf build/
	@echo $(COLOR_START)[Testing xscript...]$(COLOR_END)
	@-./xscript script/getver.xs
	@echo $(COLOR_START)[Upgrading completely]$(COLOR_END)
