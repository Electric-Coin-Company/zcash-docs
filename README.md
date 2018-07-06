# ReadtheDocs Overview 
[![Documentation Status](https://readthedocs.org/projects/zcash/badge/?version=english-docs)](http://zcash.readthedocs.io/en/english-docs/?badge=english-docs)


This repo contains material, code, and resources for Zcash ReadtheDocs environment. It is intended as a staging area for existing
documentation to be updated during the ReadtheDocs migration. Additionally, it provides a local and non-local development environment using [Sphinx](http://www.sphinx-doc.org/en/master/)
and [ReadtheDocs](https://readthedocs.org/).

## Installation
If you are using Ubuntu 16.04, please install the required packages below:

```bash
sudo apt-get install python-pip
pip install sphinx_rtd_theme sphinx sphinx-autobuild sphinx_fontawesome
```

## Setup
To use the Zcash ReadtheDocs development environment, please issue the following command:

```bash
git clone ssh://git@github.com/mdr0id/zcash.git
git checkout zc_readthedocs
cd ./zcash/doc
```

Here you will notice some important directories and files:

:file_folder: bitcoin-release-notes

:file_folder: build

:page_facing_up: Doxyfile

:page_facing_up: make.bat

:page_facing_up: Makefile

:file_folder: man

:file_folder: release-notes

:file_folder: source

### Local Development
There are several options to create targets from the ReadtheDocs development environment. The core functionality 
is maintained in the below files, located in ```./doc/source/``` :

:page_facing_up: conf.py   (configuration file used to support local/non-local environment)

:page_facing_up: index.rst (root page for ReadtheDocs to generate sibling documents)

#### Build
If you are current in the ```doc``` dir issue the following command to generate a local html instance of ReadtheDocs:

```bash
make html
```
You can find the generated root html file in ```./doc/build/html/``` as ```index.html```

### Non-Local Development
This non-local implementation of Zcash ReadtheDocs found [here](http://zcash.readthedocs.io/en/latest/index.html)

The dashboard corresponding to this environment is located [here](https://readthedocs.org/projects/zcash/)


