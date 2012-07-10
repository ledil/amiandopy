from setuptools import setup

readme = open('README.rst').read()

# Loading the version with ``from facepy import __version__`` will
# cause setuptools to attempt to import dependencies that we have no
# guarantee exist on the system yet, so we'll have to use ``execfile`` to
# import the file that contains the version specifically.
execfile('amiandopy/version.py')

setup(
    name = 'amiandopy',
    version = __version__,
    description = 'amiandoPy makes it really easy to interact with amiando\'s API',
    long_description = readme + '\n\n',
    author = 'Leonardo Di Lella',
    author_email = 'leonardo.dilella@mobileapart.com',
    url = 'http://github.com/ledil/amiandopy',
    packages = ['amiandopy'],
    install_requires = ['requests >=0.8'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    zip_safe=False
)
