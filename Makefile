## Helpful make targets for coding.


## Clean up the project directory, and run tests.
all: clean test


## Clean the project directory.
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +


## Run the test suite.
test:
	python setup.py nosetests


## Distribute the latest release to PyPI.
release:
	python setup.py release sdist upload


## Build the documentation with Sphinx.
docs:
	$(MAKE) -C docs html dirhtml latex
	$(MAKE) -C docs/_build/latex all-pdf
