.. _user_guide:

User Guide
==========

About
-----

The Zcash repository is a fork of `Bitcoin Core <https://github.com/bitcoin/bitcoin>`_ which contains protocol
changes to support the `Zerocash protocol <https://z.cash/technology/index.html>`_. This implements the Zcash
cryptocurrency, which maintains a separate ledger from the Bitcoin
network, for several reasons, the most immediate of which is that the
consensus protocol is different.

Getting Started
---------------

Welcome! This guide is intended to get you running on the official Zcash network. To ensure your Zcash client behaves gracefully throughout the setup process, please check your system meets the following requirements:

	| :fa:`linux` ``64-bit`` Linux OS
	| :fa:`microchip` ``64-bit`` Processor
	| :fa:`database` ``3GB`` of free RAM
	| :fa:`hdd-o` ``10GB`` of free Disk (*the size of the block chain increases over time*)


.. note:: Currently we only officially support Linux (Debian), but we are actively investigating development for other operating systems and platforms(e.g. OSX, Ubuntu, Windows, Fedora). 


Please let us know if you run into snags. We plan to make it less memory/CPU intensive and support more architectures and operating systems in the future.

If you are installing Zcash for the first time, please skip to the :ref:`Installation` section. Otherwise, the below upgrading section will provide information to update your current Zcash environment.

Upgrading?
----------

If you're on a Debian-based distribution, you can follow the :ref:`install-debian-bin-packages-guide` to install zcash on your system. Otherwise, you can update your local snapshot of our code:

.. code-block:: bash

   git fetch origin

| Ensure you check the current release version from :fa:`github` `here <https://github.com/zcash/zcash>`_ .
| If ``v1.1.2`` was current, issue the following commands:

.. code-block:: bash

   git checkout v1.1.2
   ./zcutil/fetch-params.sh
   ./zcutil/build.sh -j$(nproc)

.. note:: If you don't have ``nproc``, then substitute the number of cores on your system. 
   If the build runs out of memory, try again without the ``-j`` argument, i.e. just ``./zcutil/build.sh``. 
   If you are upgrading from testnet, make sure that your ``~/.zcash`` directory contains only ``zcash.conf`` to start with, and that your ``~/.zcash/zcash.conf`` does not contain ``testnet=1`` or ``addnode=testnet.z.cash``. 
   If the build fails, move aside your ``zcash`` directory and try again by following the instructions in the :ref:`installation` section below.


Setup
-----

There are a couple options to setup Zcash for the first time.

    1. If you would like to install binary packages for Debian-based operating systems, see :ref:`install-debian-bin-packages-guide`
    2. If you would like to compile Zcash from source, please continue to the :ref:`Installation` section.

.. _installation:

Installation
------------

Before we begin installing Zcash, we need to get some dependencies for your system.

UBUNTU/DEBIAN
	.. code-block:: bash
	     
	   sudo apt-get install \
	   build-essential pkg-config libc6-dev m4 g++-multilib \
	   autoconf libtool ncurses-dev unzip git python python-zmq \
	   zlib1g-dev wget curl bsdmainutils automake

FEDORA
	.. code-block:: bash

	   sudo dnf install \
	   git pkgconfig automake autoconf ncurses-devel python \
	   python-zmq wget curl gtest-devel gcc gcc-c++ libtool patch

RHEL (including Scientific Linux)
    - Install devtoolset-3 and autotools-latest (if not previously installed).
    - Run ``scl enable devtoolset-3 'scl enable autotools-latest bash'`` and do the remainder of the build in the shell that this starts.

WINDOWS (cross-compile)
    .. note:: 
    
       As of 5/1/2018 this platform is not fully supported. However, we are actively working to complete the components to support this.

       To view active work on this platform, see: :fa:`github` `#3172 <https://github.com/zcash/zcash/pull/3172>`_
       
    
MAC
    .. note:: 
    
       As of 5/1/2018 this platform is not fully supported. However, we are actively working to complete the components to support this.

       To view active work on this platform, see: :fa:`github` `#2820 <https://github.com/zcash/zcash/pull/2820>`_
    
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
    

Please see our :ref:`supported_platform_policy` for additional details.

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

Now we need to get the Zcash software from the repository:

.. code-block:: bash

   git clone https://github.com/zcash/zcash.git
   cd zcash/
   git checkout v1.1.2
   ./zcutil/fetch-params.sh

This will fetch our Sprout proving and verifying keys (the final ones created in the `Parameter Generation Ceremony <https://github.com/zcash/mpc>`_ , and place them into ``~/.zcash-params/``. These keys are just under 911MB in size, so it may take some time to download them.

The message printed by ``git checkout`` about a "detached head" is normal and does not indicate a problem.

.. _ugBuild:

Build
-----

Ensure you have successfully installed all system package dependencies as described above. Then run the build, e.g.:

.. code-block:: bash
   
   ./zcutil/build.sh -j$(nproc)

.. attention:: If you recieved any errors, from the above command, please check out our :ref:`troubleshooting-guide`

.. note:: This should compile our dependencies and build ``zcashd``. (Note: if you don't have ``nproc``, then substitute the number of cores on your system. If the build runs out of memory, try again without the ``-j`` argument, i.e. just ``./zcutil/build.sh``.

.. _ugConfiguration:

Configuration
-------------

Following the steps below will create your zcashd configuration file which can be edited to either connect to ``mainnet`` or ``testnet`` as well as applying settings to safely access the RPC interface.

.. tip:: For a complete list of parameters used in ``zcash.conf``, please check out :ref:`zcash_conf_guide`

Create the `~/.zcash` directory:

.. code-block:: bash
   
   mkdir -p ~/.zcash


Mainnet
*******

Place a configuration file at `~/.zcash/zcash.conf` using the following commands:

.. warning:: Note that this will overwrite any ``zcash.conf`` settings you may have added from testnet. (If you want to run on testnet, you can retain a `zcash.conf` from testnet.)


.. code-block:: bash

   echo "addnode=mainnet.z.cash" >~/.zcash/zcash.conf


Example configured for ``mainnet`` :

:fa:`file` ``zcash.conf`` 

.. code-block:: bash

    addnode=mainnet.z.cash


Testnet
*******

After running the above commands to create the `zcash.conf` file, edit the following parameters in your `zcash.conf` file to indicate network and node discovery for `testnet`:

	- add the line **testnet=1**
	- **addnode=testnet.z.cash** instead of **addnode=mainnet.z.cash**

Example configured for ``testnet``:

:fa:`file` ``zcash.conf`` 

.. code-block:: bash

    testnet=1
    addnode=testnet.z.cash

.. _Enable_CPU_Mining:

Enabling CPU Mining
*******************

If you want to enable CPU mining, run these commands:

.. code-block:: bash

   echo 'gen=1' >> ~/.zcash/zcash.conf
   echo "genproclimit=-1" >> ~/.zcash/zcash.conf

Setting ``genproclimit=-1`` mines on the maximum number of threads possible on your CPU. If you want to mine with a lower number of threads, set ``genproclimit`` equal to the number of threads you would like to mine on.

The default miner is not efficient, but has been well reviewed. To use a much more efficient but unreviewed solver, you can run this command:

.. code-block:: bash

   echo 'equihashsolver=tromp' >> ~/.zcash/zcash.conf

Note, you probably want to read the :ref:`zcash_mining_guide` to learn more mining details.

Usage
-----

Now, run zcashd!

.. code-block:: bash
   
   ./src/zcashd

To run it in the background (without the node metrics screen that is normally displayed) use ``./src/zcashd --daemon``.

.. important:: If you are running Zcash for the first time you will need to allow your node to fully sync:
    
   .. code-block:: console
    :emphasize-lines: 24
                                                                                                                                                        
             :88SX@888@@X8:                    8;     %X        X%     ;8       
          %%Xt%tt%SSSSS:XXXt@@              X            ::  ::            X    
        @S;;tt%%%t    ;;::XXXXSX           %               SS               %   
      .t:::;;%8888    88888tXXXX8;        S                                  S  
     .%...:::8             8::XXX%;       X                                  X  
     8888...:t888888X     8t;;::XX8       8                                  8  
    %888888...:::;:8    :Xttt;;;::X@                                            
    888888888...:St    8:%%tttt;;;:X       X                                X   
    88888888888S8    :%;ttt%%tttt;;X        8                              8    
    %888888888%t    8S:;;;tt%%%ttt;8          :                          :      
     8t8888888     S8888888Stt%%%t@            ::                      ::       
     .@tt888@              8;;ttt@;               t                  t          
      .8ttt8@SSSSS    SXXXX%:;;;X;                  8              8            
        X8ttt8888%    %88...::X8                      X.        .X              
          %8@tt88;8888%8888%8X                          :;    ;:                
             :@888@XXX@888:                                tt                   
                                                                                
    Thank you for running a Zcash node!
    You're helping to strengthen the network and contributing to a social good :)

    In order to ensure you are adequately protecting your privacy when using Zcash,
    please see <https://z.cash/support/security/>.

            Block height | 319430
                Connections | 8
    Network solution rate | 508319381 Sol/s

    You are currently not mining.
    To enable mining, add 'gen=1' to your zcash.conf and restart.

    Since starting this node 9 minutes, 1 seconds ago:
    - You have validated 7815 transactions!

    [Press Ctrl+C to exit] [Set 'showmetrics=0' to hide]
    
   Notice ``319430``, in the above output, after the ``Block height`` field, this means your Zcashd is fully sync.
   Alternatively, if you were *NOT* fully synced your output would look similar to below:

   .. code-block:: console
    :emphasize-lines: 24
                                                                                 
             :88SX@888@@X8:                    8;     %X        X%     ;8       
          %%Xt%tt%SSSSS:XXXt@@              X            ::  ::            X    
        @S;;tt%%%t    ;;::XXXXSX           %               SS               %   
      .t:::;;%8888    88888tXXXX8;        S                                  S  
     .%...:::8             8::XXX%;       X                                  X  
     8888...:t888888X     8t;;::XX8       8                                  8  
    %888888...:::;:8    :Xttt;;;::X@                                            
    888888888...:St    8:%%tttt;;;:X       X                                X   
    88888888888S8    :%;ttt%%tttt;;X        8                              8    
    %888888888%t    8S:;;;tt%%%ttt;8          :                          :      
     8t8888888     S8888888Stt%%%t@            ::                      ::       
     .@tt888@              8;;ttt@;               t                  t          
      .8ttt8@SSSSS    SXXXX%:;;;X;                  8              8            
        X8ttt8888%    %88...::X8                      X.        .X              
          %8@tt88;8888%8888%8X                          :;    ;:                
             :@888@XXX@888:                                tt                   

    Thank you for running a Zcash node!
    You're helping to strengthen the network and contributing to a social good :)

    In order to ensure you are adequately protecting your privacy when using Zcash,
    please see <https://z.cash/support/security/>.

        Downloading blocks | 319610 / ~320290 (99%)
                Connections | 6
    Network solution rate | 389211802 Sol/s

    You are currently not mining.
    To enable mining, add 'gen=1' to your zcash.conf and restart.

    Since starting this node 59 seconds ago:
    - You have validated 7144 transactions!

    [Press Ctrl+C to exit] [Set 'showmetrics=0' to hide]

   Notice now how the ``Block height`` field has changed to ``Downloading blocks`` with value ``319610 / ~320290 (99%)``.
   This indicates that your node is attempting to sync with the current block height.


You should be able to use the RPC after it finishes syncing. If you are running ``zcashd`` in the background, issue the below command to test:

*( If you did not run zcashd in the background, you will need to open a new terminal)*

.. code-block:: bash
   
   ./src/zcash-cli getinfo

.. note:: If you are familiar with bitcoind's RPC interface, you can use many of those calls to send ZEC between `t-addr` addresses. We do not support the 'Accounts' feature (which has also been deprecated in ``bitcoind``) — only the empty string ``""`` can be used as an account name. The main network node at mainnet.z.cash is also accessible via Tor hidden service at zcmaintvsivr7pcn.onion.

Using Zcash
***********

First, you want to obtain Zcash. You can purchase them from an exchange, from other users, or sell goods and services for them! Exactly how to obtain Zcash (safely) is not in scope for this document, but you should be careful. Avoid scams!

.. important:: **Terminology**

   Zcash supports two different kinds of addresses, a ``z-addr`` (which begins with a ``z``) is an address that uses zero-knowledge proofs and other cryptography to protect user privacy. There are also ``t-addrs`` (which begin with a ``t``) that are similar to Bitcoin's addresses.

   The interfaces are a commandline client (`zcash-cli`) and a Remote Procedure Call (RPC) interface, which is documented here:

   :ref:`payment_api`

.. attention:: **Wallet Backup**
   
   To ensure you have properly backedup your wallet, we **strongly** encourage you to review the :ref:`wallet_backup` .


Generating a t-addr
+++++++++++++++++++

Let's generate a t-addr first.

.. code-block:: bash

   $ ./src/zcash-cli getnewaddress
   t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1

Listing t-addr
++++++++++++++

.. code-block:: bash

   $ ./src/zcash-cli getaddressesbyaccount ""

This should show the address that was just created.

Receiving Zcash with a z-addr
+++++++++++++++++++++++++++++

Now let's generate a z-addr.

.. code-block:: bash
   
   $ ./src/zcash-cli z_getnewaddress
   zcBqWB8VDjVER7uLKb4oHp2v54v2a1jKd9o4FY7mdgQ3gDfG8MiZLvdQga8JK3t58yjXGjQHzMzkGUxSguSs6ZzqpgTNiZG

This creates a private address and stores its key in your local wallet file. Give this address to the sender!

A z-addr is pretty large, so it's easy to make mistakes with them. Let's put it in an environment variable to avoid mistakes:

.. code-block:: bash

   $ ZADDR='zcBqWB8VDjVER7uLKb4oHp2v54v2a1jKd9o4FY7mdgQ3gDfG8MiZLvdQga8JK3t58yjXGjQHzMzkGUxSguSs6ZzqpgTNiZG'

Listing z-addr
++++++++++++++

To get a list of all addresses in your wallet for which you have a spending key, run this command:

.. code-block:: bash

   $ ./src/zcash-cli z_listaddresses

You should see something like:

.. code-block:: json

   [
    {
        "txid" : "af1665b317abe538148114a45322f28151925501c081949cc7a5207ef21cb750",
        "amount" : 1.23,
        "memo" : "48656c6c6f20ceb2210000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    }
   ]

Sending coins with your z-addr
++++++++++++++++++++++++++++++

If someone gives you their z-addr...

.. code-block:: bash

   $ FRIEND='zcCDe8krwEt1ozWmGZhBDWrcUfmK3Ue5D5z1f6u2EZLLCjQq7mBRkaAPb45FUH4Tca91rF4R1vf983ukR71kHyXeED4quGV'

You can send 0.8 ZEC by doing...

.. code-block:: bash
   
   $ ./src/zcash-cli z_sendmany "$ZADDR" "[{\"amount\": 0.8, \"address\": \"$FRIEND\"}]"

After waiting about a minute, you can check to see if the operation has finished and produced a result:

.. code-block:: bash

   $ ./src/zcash-cli z_getoperationresult

.. code-block:: json

   [
    {
        "id" : "opid-4eafcaf3-b028-40e0-9c29-137da5612f63",
        "status" : "success",
        "creation_time" : 1473439760,
        "result" : {
            "txid" : "3b85cab48629713cc0caae99a49557d7b906c52a4ade97b944f57b81d9b0852d"
        },
        "execution_secs" : 51.64785629
    }
   ]


Additional operations for zcash-cli
+++++++++++++++++++++++++++++++++++

As Zcash is an extension of bitcoin, zcash-cli supports all commands that are part of the Bitcoin Core API (as of version 0.11.2), https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list

For a full list of new commands that are not part of bitcoin API (mostly addressing operations on z-addrs) see :ref:`payment_api`

To list all zcash commands:

.. code-block:: bash
    
    ./src/zcash-cli help

To get help with a particular command:

.. code-block:: bash

    ./src/zcash-cli help <command>

.. attention:: 
   Known Security Issues

   Each release contains a `./doc/security-warnings.md` document describing
   security issues known to affect that release. You can find the most
   recent version of this document here:

   :ref:`security_warnings`

   Please also see our security page for recent notifications and other
   resources:

   https://z.cash/support/security.html
