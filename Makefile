# xscript/Makefile
# xscript makefile

SOURCE := xscript xscriptcore.py xscriptlib/

help: Makefile
	@echo "Help for xscript 0.5 Makefile"
	@echo ""
	@echo "demo            run xscript demo"
	@echo "deploy          commit source and push"
	@echo "deploy-docs     commit docs and push"
	@echo "docs            show xscript docs"
	@echo "help            show this help"
	@echo "install         install xscript"
	@echo "install-plugin  install plugin"
	@echo "restore-profile copy profile to HOME directory"
	@echo "upgrade         upgrade xscript from Github and install"

demo: Makefile $(SOURCE)
	@echo [Running demo...]
	@-./xscript examples/getver.xs
	@echo [Done]

deploy: Makefile LICENSE README.md setup.py docs/ examples/ $(SOURCE)
	@echo [Start deploying...]
	@echo [Committing changes...]
	@git add .
	@git commit -m `date +%Y-%m-%d`
	@sleep 1s
	@echo [Pushing changes...]
	@git push
	@echo [Deploying successfully]

deploy-docs: Makefile docs/ docs/mkdocs.yml
	@echo [Start deploying...]
	@cd docs/; mkdocs gh-deploy --message `date +%Y-%m-%d`
	@echo [Deploying successfully]

docs: Makefile docs/
	@echo [Running mkdocs...]
	@cd docs/; mkdocs serve
	@echo [Done]

install: Makefile setup.py
	@echo -n [Installing dependencies... 
	@pip install -r requirements.txt >> /dev/null
	@echo Done]
	@echo -n [Installing xscript... 
	@python3 setup.py install >> /dev/null
	@echo Done]
	@-cp xscript /usr/bin/xscript
	@-rm -rf build/
	@echo [Installing completely]

install-plugin: Makefile plugin/ plugin/ftdetect/xscript.vim plugin/syntax/xscript.vim
	@-cp plugin/ftdetect/xscript.vim ~/.vim/ftdetect/xscript.vim
	@-cp plugin/syntax/xscript.vim ~/.vim/syntax/xscript.vim

restore-profile: Makefile .xscriptrc
	@cp .xscriptrc $(HOME)/.xscriptrc

upgrade: Makefile setup.py $(SOURCE)
	@echo [Upgrading...]
	@git pull
	@echo -n [Installing xscript... 
	@python3 setup.py install >> /dev/null
	@echo Done]
	@-cp xscript /usr/bin/xscript
	@-rm -rf build/
	@echo [Testing xscript...]
	@-./xscript examples/getver.xs
	@echo [Upgrading completely]
