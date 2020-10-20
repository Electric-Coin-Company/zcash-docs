# ReadtheDocs Overview
[![Documentation Status](https://readthedocs.org/projects/zcash/badge/?version=latest)](https://zcash.readthedocs.io/en/latest/?badge=latest)

This repo contains material, code, and resources for Zcash ReadtheDocs environment. It is intended as a staging area for existing
documentation to be updated during the ReadtheDocs migration. Additionally, it provides a local and non-local development environment using [Sphinx](http://www.sphinx-doc.org/en/master/),
[ReadtheDocs](https://readthedocs.org/), and [Python3+](https://www.python.org/)

## Installation
Below you will find setup instructions for a few common platforms. Please follow the procedure specific to your respective platform.

### Linux
Install PIP:

```bash
sudo apt-get install python3-pip
```

Get required packages for ReadtheDocs build:

```bash
pip3 install sphinx_rtd_theme sphinx sphinx-autobuild sphinx_fontawesome recommonmark sphinx-sitemap sphinx-copybutton
```

### macOS

If you are using `brew`, please issue the following:

```bash
brew install python3
pip3 install sphinx_rtd_theme sphinx sphinx-autobuild sphinx_fontawesome recommonmark sphinx-sitemap sphinx-copybutton
```

If you are **not** using `brew`, please verify version of OS:

```bash
sw_vers -productVersion
```
Using the version output from ``sw_vers -productVersion``, download the according package or follow the install from source instructions here:

https://www.macports.org/install.php

Once you have successfully installed macports, configure sphinx using the below commands:

```bash
sudo port install py36-sphinx
sudo port select --set python python36
sudo port select --set sphinx py36-sphinx
```

### Windows
Install PIP:

```bash
easy_install pip3
```

Get required packages for ReadtheDocs build:

```bash
pip3 install sphinx_rtd_theme sphinx sphinx-autobuild sphinx_fontawesome recommonmark sphinx-sitemap sphinx-copybutton
```

If you are unable to build the above packages, please compile them from source:

[sphinx_rtd_theme] (https://github.com/rtfd/sphinx_rtd_theme)

[sphinx_fontawesome] (https://github.com/fraoustin/sphinx_fontawesome)

## Setup
To use the Zcash ReadtheDocs development environment, please issue the following command:

```bash
git clone https://gitlab.com/zcash-docs/zcash-docs.git
cd zcash-docs
```

Here you will notice some important directories and files:

:page_facing_up: make.bat

:page_facing_up: Makefile

:file_folder: source

### Local Development
There are several options to create targets from the ReadtheDocs development environment. The core functionality
is maintained in the below files, located in ```./source/``` :

:page_facing_up: conf.py   (configuration file used to support local/non-local environment)

:page_facing_up: index.rst (root page for ReadtheDocs to generate sibling documents)

#### Build
If you are current in the project root directory issue the following command to generate a local html instance of ReadtheDocs:

```bash
make html
```
You can find the generated root html file in ```./build/html/``` as ```index.html```

### Non-Local Development
This non-local implementation of Zcash ReadtheDocs found [here](http://zcash.readthedocs.io/en/latest/index.html)

The dashboard corresponding to this environment is located [here](https://readthedocs.org/projects/zcash/)
