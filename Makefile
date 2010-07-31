.PHONY: clean-tmp test

all: clean-tmp test

test:
	nosetests --with-doctest --doctest-extension=txt -v

clean-tmp:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.swp' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

release:
	python setyp.py release sdist upload
