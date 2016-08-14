"""Handles packaging, distribution, and testing."""


from sys import exit
from subprocess import call

from setuptools import Command, find_packages, setup


class BaseCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class TestCommand(BaseCommand):
    description = 'run tests'

    def run(self):
        exit(call(['py.test', '--quiet', '--cov-report=term-missing', '--cov', 'pycall']))


class ReleaseCommand(BaseCommand):

    description = 'cut a new PyPI release'

    def run(self):
        call(['rm', '-rf', 'build', 'dist'])
        ret = call(['python', 'setup.py', 'sdist', 'bdist_wheel', '--universal', 'upload'])
        exit(ret)


setup(

    # Basic package information.
    name = 'pycall',
    version = '2.3.0',
    packages = find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),

    # Packaging options.
    zip_safe = False,
    include_package_data = True,

    # Package dependencies.
    install_requires = ['path.py>=2.2.2'],
    extras_require = {
        'test': ['codacy-coverage', 'python-coveralls', 'pytest', 'pytest-cov', 'sphinx'],
    },
    cmdclass = {
        'test': TestCommand,
        'release': ReleaseCommand,
    },

    # Metadata for PyPI.
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'http://pycall.org/',
    keywords = 'asterisk callfile call file telephony voip',
    description = 'A flexible python library for creating and using Asterisk call files.',
    long_description = open('README.rst').read()

)
