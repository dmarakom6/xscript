# xscript/Makefile
# xscript makefile

SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.5 Makefile\n"
	@echo "demo        run xscript demo"
	@echo "deploy      commit source and push"
	@echo "deploy-docs commit docs and push"
	@echo "docs        show xscript docs"
	@echo "help        show this help"
	@echo "install     install xscript"
	@echo "upgrade     upgrade xscript from Github and install"

demo: Makefile $(SOURCE)
	@echo [Running demo...]
	@-./xscript examples/getver.xs
	@echo [Done]

deploy: Makefile LICENSE README.md setup.py docs/ examples/ $(SOURCE)
	@echo [Start deploying...]
	@echo [Adding changes...]
	@git add .
	@echo [Committing changes...]
	@git commit -m `date +%Y-%m-%d`
	@sleep 1s
	@echo [Pushing changes...]
	@git push -u origin master
	@echo [Deploying successfully]

deploy-docs: Makefile docs/ docs/mkdocs.yml docs/docs
	@echo Start deploying...]
	@cd docs/; mkdocs gh-deploy --message `date +%Y-%m-%d`
	@echo [Deploying successfully]

docs: Makefile docs/ docs/mkdocs.yml docs/docs/
	@echo [Running mkdocs...]
	@cd docs/; mkdocs serve
	@echo [Done]

install: Makefile setup.py
	@echo -n [Checking packages... 
	@-pip3 install -U colorama mkdocs prettytable >> /dev/null
	@echo Done]
	@echo -n [Installing xscript... 
	@python3 setup.py install >> /dev/null
	@echo Done]
	@cp xscript /usr/bin/xscript
	@-rm -rf build/
	@echo [Installing completely]

upgrade: Makefile setup.py $(SOURCE)
	@echo [Upgrading...]
	@git pull
	@echo -n [Checking packages... 
	@-pip3 install -U colorama mkdocs prettytable >> /dev/null
	@echo Done]
	@echo -n [Installing xscript... 
	@python3 setup.py install >> /dev/null
	@echo Done]
	@-rm -rf build/
	@cp xscript /usr/bin/xscript
	@echo [Testing xscript...]
	@-./xscript examples/getver.xs
	@echo [Upgrading completely]
