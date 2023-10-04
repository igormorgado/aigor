.PHONY: clean

reinstall: clean uninstall install
	@echo "DONE"

install:
	pip install .

edit:
	pip install -e .

uninstall:
	pip uninstall -y aigor

upgrade:
	pip install --upgrade .

test: clean
	mypy src/aigor
	pylint src/aigor
	pytest -v -s

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@find . -type d -name "build" -exec rm -rf {} +
	@find . -type d -name "*.egg-info"  -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@echo "Done!"

