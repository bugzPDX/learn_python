try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Lisa Hewus',
	'url': 'My url',
	'download_url': 'My download url',
	'author_email': 'lhewus@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['FIRST_PROJECT'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)		