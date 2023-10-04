SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build

.PHONY: clean help Makefile

reinstall: clean uninstall install
	@echo "DONE"

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	pip install .

edit: uninstall
	pip install -e .

uninstall:
	pip uninstall -y aigor

upgrade:
	pip install --upgrade .

test: 
	mypy src/aigor
	pylint src/aigor
	pytest -v -s
	
PHONY: doc
doc:
	# sphinx-build -b html docs/source docs/build
	sphinx-apidoc -f -o  docs/source src/aigor

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name "build" -exec rm -rf {} +
	@find . -type d -name "*.egg-info"  -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@echo "Done!"

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
