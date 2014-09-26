from setuptools import setup, find_packages

from djplatter import __version__, __author__

# TODO: Description, classifiers
setup(
    name="djplatter",
    version=__version__,
    url='https://github.com/thomasw/djplatter',
    download_url='https://github.com/thomasw/djplatter/releases',
    author=__author__,
    author_email='thomas.welfley+djplatter@gmail.com',
    description='',
    packages=find_packages(),
    tests_require=[
        'mock==1.0.1', 'nose==1.3.4', 'pinocchio==0.4.1', 'unittest2==0.5.1',
        'django==1.7'],
    install_requires=['django>=1.4'],
    classifiers=[],
    test_suite='nose.collector'
)
