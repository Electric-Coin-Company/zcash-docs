# Installing Zcashd & Zcash-cli on OSx


Zcashd & Zcash-cli are "best effort" suppoerted for macOS.  It's ok to use it and develop on it--we sure do. The level of testing and integration is not up to par with our standards to call this [officially supported](https://zcash.readthedocs.io/en/latest/rtd_pages/supported_platform_policy.html#supported-platform-policy).

Currently, the only way to install Zcashd & Zcash-cli on OSx is to build from source. 

Installation
------------

Before we begin installing Zcash, we need to get some dependencies for your system.

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

Dependency Version Check
------------------------
	  
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


Build
-----

Ensure you have successfully installed all system package dependencies as described above. Then run the build, e.g.:


Troubleshooting
---------------
