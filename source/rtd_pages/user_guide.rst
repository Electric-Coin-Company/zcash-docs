.. _user_guide:

User Guide
==========

Welcome! This guide is intended to get you running on the official Zcash network. To ensure your Zcash client behaves gracefully throughout the setup process, please check your system meets the following requirements:

	| :fa:`linux` ``64-bit`` Linux OS
	| :fa:`microchip` ``64-bit`` Processor
	| :fa:`database` ``5GB`` of free RAM
	| :fa:`hdd-o` ``25GB`` of free Disk (*the size of the block chain increases over time*)


.. note:: Currently we only officially support Linux (Debian), but we are actively investigating development for other operating systems and platforms(e.g. macOS, Ubuntu, Windows, Fedora). 


Please let us know if you run into snags. We plan to make it less memory/CPU intensive and support more architectures and operating systems in the future.

If you are installing Zcash for the first time, please skip to the :ref:`Installation` section. Otherwise, the below upgrading section will provide information to update your current Zcash environment.


Setup
-----

There are a couple options to setup Zcash for the first time.

    1. If you would like to install binary packages for Debian-based operating systems, see :ref:`install-debian-bin-packages-guide`
    2. If you would like to compile Zcash from source, please continue to the :ref:`Installation` section.
    3. If you would like to install via a binary tarball download, see :ref:`install-binary-tarball-guide`.

.. _installation:

Installation
------------

Before we begin installing Zcash, we need to get some dependencies for your system.

UBUNTU/DEBIAN
	.. code-block:: bash
	     
	   sudo apt-get install \
	   build-essential pkg-config libc6-dev m4 g++-multilib \
	   autoconf libtool ncurses-dev unzip git python3 python3-zmq \
	   zlib1g-dev curl bsdmainutils automake

    .. note::

        If you plan to cross-compile for Windows (that is, use your Linux system to build a Windows binary), there are a few additional setup steps. As of 2018-10-16 we have tested this using Ubuntu 18.04 (“Bionic Beaver”).

        Install the mingw-w64 package:

    	.. code-block:: bash

    	   sudo apt-get install mingw-w64

        The following two commands will display a current selection and prompt you for a new selection. Make sure the 'posix' compiler variants are selected for gcc and g++.

    	.. code-block:: bash

    	   sudo update-alternatives --config x86_64-w64-mingw32-gcc
    	   sudo update-alternatives --config x86_64-w64-mingw32-g++


    .. note::

        If you wish to run the test suite, you will need additional dependencies:

        .. code-block:: bash

            sudo apt-get install python-pip
            sudo pip install pyblake2

FEDORA
	.. code-block:: bash

	   sudo dnf install \
	   git pkgconfig automake autoconf ncurses-devel python \
	   python-zmq curl gtest-devel gcc gcc-c++ libtool \
	   patch glibc-static libstdc++-static

RHEL (including Scientific Linux)
    - Install devtoolset-3 and autotools-latest (if not previously installed).
    - Run ``scl enable devtoolset-3 'scl enable autotools-latest bash'`` and do the remainder of the build in the shell that this starts.

MACOS 10.12+ (Using the Terminal application)
    1. Install macOS command line tools:
        .. code-block:: bash

	    xcode-select --install

    2. Install Homebrew: 
        .. code-block:: bash
       
            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    3. Install packages:
        .. code-block:: bash

            brew install git pkgconfig automake autoconf libtool coreutils
    
    4. Install ``pip`` :
        .. code-block:: bash

            sudo easy_install pip
    
    5. Install python modules for rpc-tests
        .. code-block:: bash

            sudo pip install pyblake2 pyzmq

    .. note::

       There is an existing bug for macOS Mojave (10.14) that causes a failure in building Zcash. A work around for this includes one more step:

       .. code-block:: bash

	   open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg

CENTOS 7+
    .. code-block:: bash

       sudo yum install \
       autoconf libtool unzip git python \
       wget curl  automake gcc gcc-c++ patch \
       glibc-static libstdc++-static

    Please execute the below commands in order.

    .. code-block:: bash

       sudo yum install centos-release-scl-rh
       sudo yum install devtoolset-3-gcc devtoolset-3-gcc-c++
       sudo update-alternatives --install /usr/bin/gcc-4.9 gcc-4.9 /opt/rh/devtoolset-3/root/usr/bin/gcc 10
       sudo update-alternatives --install /usr/bin/g++-4.9 g++-4.9 /opt/rh/devtoolset-3/root/usr/bin/g++ 10
       scl enable devtoolset-3 bash
    

.. note:: Please see our :ref:`supported_platform_policy` for additional details.

Dependency Version Check
************************
	  
Next, we need to ensure we have the correct version of ``gcc`` , ``g++`` , and ``binutils``

    1. **gcc/g++ 4.9 or later is required.** 
        
        Zcash has been successfully built using gcc/g++ versions 4.9 to 7.x inclusive. 

        Use ``g++ --version`` or ``gcc --version`` to check which version you have.

        On Ubuntu Trusty, if your version is too old then you can install gcc/g++ 4.9 as follows:

	    .. code-block:: bash

   		  $ sudo add-apt-repository ppa:ubuntu-toolchain-r/test
   	 	  $ sudo apt-get update
   		  $ sudo apt-get install g++-4.9

    2. **binutils 2.22 or later is required.**

        Use ``as --version`` to check which version you have, and upgrade if necessary.

Downloading Zcash source
************************

Now we need to get the Zcash software from the repository:

.. code-block:: bash

   git clone https://github.com/zcash/zcash.git
   cd zcash/
   git checkout v3.1.0
   ./zcutil/fetch-params.sh

This will fetch the parameters generated in the Sapling MPC, and place them into ``~/.zcash-params/ ``. These parameters are around 760 MB in size, so it may take some time to download them.
The message printed by ``git checkout`` about a "detached head" is normal and does not indicate a problem.

.. _ugBuild:

Build
-----

Ensure you have successfully installed all system package dependencies as described above. Then run the build, e.g.:

.. code-block:: bash
   
   ./zcutil/build.sh -j$(nproc)

.. note::

    To build a Windows binary on another platform (as described in the Ubuntu/Debian section above), add a ``HOST`` environment variable setting with value ``x86_64-w64-mingw32`` to the build command, like this:

    .. code-block:: bash

       HOST=x86_64-w64-mingw32 ./zcutil/build.sh -j$(nproc)

.. note::

    To build an ARMv8 binary (using `g++-aarch64-linux-gnu`) on another platform (as described in the Ubuntu/Debian section above), add a ``HOST`` environment variable setting with value ``aarch64-linux-gnu`` to the build command, like this:

    .. code-block:: bash

       HOST=aarch64-linux-gnu ./zcutil/build.sh -j$(nproc)

.. note::

   If you wish to build ``zcashd`` with the Qpid Proton interface enabled, you
   will need an additional dependency:

   .. code-block:: bash

      sudo apt-get install cmake

   Then, Proton must be enabled during the build as follows:

   .. code-block:: bash

      ./zcutil/build.sh --enable-proton -j$(nproc)


.. attention:: If you recieved any errors, from the above command, please check out our :ref:`troubleshooting-guide`

.. note:: This should compile our dependencies and build ``zcashd``. (Note: if you don't have ``nproc``, then substitute the number of cores on your system. If the build runs out of memory, try again without the ``-j`` argument, i.e. just ``./zcutil/build.sh``.