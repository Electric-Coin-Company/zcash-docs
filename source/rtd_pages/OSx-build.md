# Building Zcashd & Zcash-cli on OSx


Zcashd & Zcash-cli are "best effort" supported for macOS.  It's ok to use it and develop on it--we sure do. The level of testing and integration is not up to par with our standards to call this [officially supported](https://zcash.readthedocs.io/en/latest/rtd_pages/supported_platform_policy.html#supported-platform-policy).

## Instructions

Currently, the only way to install Zcashd & Zcash-cli on OSx is to build from source. Instructions below. 

1. Get dependencies by running the command in Terminal. If already installed, skip that step.

      *  MacOS command line tools: 
          ```
          xcode-select --install
          ```
      * Homebrew: 
          ```
          /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
          ```
      * Packages: 
          ```
          brew install git pkgconfig automake autoconf libtool coreutils
          ```
      * Pip: 
          ```
          sudo easy_install pip
          ```
      * Python modules for rpc-tests: 
          ```
          sudo pip install pyblake2 pyzmq
          ```

1. Download the source code from the repository:
    ```
     git clone https://github.com/zcash/zcash.git
     cd zcash/
     git checkout v3.1.0
     ./zcutil/fetch-params.sh
     ```
     <!--The message printed by ``git checkout`` about a "detached head" is normal and does not indicate a problem. --> 
    This step includes fetching [zcash parameters](https://z.cash/technology/paramgen/), which are numerical dependecies for Zcash a result of the crypto inside. They are around 760 MB in size, so it will take time to download them.


1. Build Zcashd & Zcash-cli
    ```
    ./zcutil/build.sh -j$(nproc)
    ```

    If you don't have ``nproc``, then substitute the number of cores on your system. If the build runs out of memory, try again without the ``-j`` argument, i.e. just ``./zcutil/build.sh``
    
    *Note: There is an existing bug for macOS Mojave (10.14) that causes a failure in building Zcash. A work around for this includes one more step before the build: `open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg`*


## Next steps
Now that you've built Zcashd & Zcash-cli, we can move on to the next steps of: configuration, sync, and use. Refer back to the [Zcashd & Zcash-cli page](zcashd.html) for further instructions. 
