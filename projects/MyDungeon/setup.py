from distutils.core import setup

setup(
    name='MyDungeon',
    version='1.0',
    author='Lisa D Hewus Fresh',
    author_email='lhewusfresh@gmail.com',
    packages=['mydungeon', 'mydungeon.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/MyDungeon/',
    license='LICENSE.txt',
    description='Useless Dungeon Game',
    long_description=open('README.txt').read(),
    install_requires=[],
)
