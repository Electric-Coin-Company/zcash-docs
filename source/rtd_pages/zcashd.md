# Zcash Full Node and CLI

Zcashd & Zcash-cli allow you to run a full node and interact with it via a command-line interface.  The zcashd full node downloads a copy of the Zcash blockchain,  enforces rules of the Zcash network, and can execute all functionalities. The zcash-cli allows interactions with the node (i.e. tell it to send a transaction).

![zcashdandzcashcli](./images/zcashd_and_zcashcli.png)

Zcashd & Zcash-cli are the maintained by Electric Coin Company (the founding team for Zcash).


## Installation

* [Debian/Ubuntu](Debian-Ubuntu-installation.md) ([officially](https://zcash.readthedocs.io/en/latest/rtd_pages/supported_platform_policy.html#supported-platform-policy) supported)

* **Other Linux Systems**: try the [Binary Tarball Download and Setup](install_binary_tarball.html) to install Zcashd & Zcash-cli. The .tar file unzips into a directory and does not involve a package manager, so it is agnostic of whether that system uses an OS package manager or which one it uses. Alternatively, you can [build from source](user_guide.html).

<!--Note that Debian packages usually “just work” on Ubuntu et al

yeah there’s a whole category of distributions that are based on Debian, Ubuntu being the big one
https://en.wikipedia.org/wiki/Category:Debian-based_distributions
for a system in that category, try the debian package source
for a system outside that category (e.g. red hat), try the tar file
if neither of those work, try build-from-source (edited) --> 

* [OSx](OSx-installation.md) ("best-effort" supported)

* [Windows](windows-installation.md) (unsupported)
<!--
## Configuration

The Zcash *configuration file* is a text file that specifies options that affect how your instance of the Zcash client operates.
The ``zcashd`` executable reads this file only when it starts.
You may edit the configuration file with any text editor, but performing the steps below does not require using an editor.
The order of the lines is not important. Lines beginning with a semicolon (``;``) are treated as comments and ignored.

Following these steps will create your zcashd configuration file which can be edited to either connect to ``mainnet`` or ``testnet`` as well as applying settings to safely access the RPC interface.

.. tip:: For a complete list of parameters used in ``zcash.conf``, please check out :ref:`zcash_conf_guide`

Linux
    Create the data directory:

    .. code-block:: bash
   
       mkdir -p ~/.zcash

macOS
    Your data directory is already generated at ``~/Library/Application Support/Zcash``.

Mainnet
*******

Place a configuration file inside your data directory using the following commands:

.. warning:: Note that this will overwrite any ``zcash.conf`` settings you may have added from testnet. (If you want to run on testnet, you can retain a `zcash.conf` from testnet.)

Linux     
    .. code-block:: bash

       echo "addnode=mainnet.z.cash" >~/.zcash/zcash.conf

macOS
    .. code-block:: bash

       echo "addnode=mainnet.z.cash" >~/Library/Application Support/Zcash/zcash.conf
       
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


## Use


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
    
   Notice ``319430``, in the above output, after the ``Block height`` field, this means your zcashd is fully synced.
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
   
   To ensure you have properly backed up your wallet, we **strongly** encourage you to review the :ref:`wallet_backup` .


Generating a t-addr
+++++++++++++++++++

Let's generate a t-addr first. If you are running zcashd for the first time, you 
can issue ``zcash-cli getaddressesbyaccount ""`` to view existing addresses. 

.. code-block:: bash

   $ ./src/zcash-cli getnewaddress
   t1example4vfmdgQ3v3SNuQga8JKHTNi2a1

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
   zs1examplea4lqxrtmlpkayj0hxpfdd3ve62xhd7jds8c2a8tqz5kekplt469eza5wu8djdvpauezv

This creates a private address and stores its key in your local wallet file. Give this address to the sender!

A z-addr is pretty large, so it's easy to make mistakes with them. Let's put it in an environment variable to avoid mistakes:

.. code-block:: bash

   $ ZADDR='zs1examplea4lqxrtmlpkayj0hxpfdd3ve62xhd7jds8c2a8tqz5kekplt469eza5wu8djdvpauezv'

Listing z-addr
++++++++++++++

To get a list of all addresses in your wallet for which you have a spending key, run this command:

.. code-block:: bash

   $ ./src/zcash-cli z_listaddresses

You should see something like:

.. code-block:: json

   [
      "zs1examplea4lqxrtmlpkayj0hxpfdd3ve62xhd7jds8c2a8tqz5kekplt469eza5wu8djdvpauezv"
   ]

Sending coins with your z-addr
++++++++++++++++++++++++++++++

If someone gives you their z-addr...

.. code-block:: bash

   $ FRIEND='zs1exampleakux6zswvlvsrcuku6540kw3l8jcft8n8hwnq6ma57canydsn3r05nxylrmcew82ja59'

You can send 0.8 ZEC by doing...

.. code-block:: bash
   
   $ ./src/zcash-cli z_sendmany "$ZADDR" "[{\"amount\": 0.8, \"address\": \"$FRIEND\"}]"

After waiting a few seconds, you can check to see if the operation has finished and produced a result:

.. code-block:: bash

   $ ./src/zcash-cli z_getoperationresult

.. code-block:: json

   [
    {
        "id" : "opid-bc8f822c-68df-419e-ae8f-b14b7aca29fd",
        "status" : "success",
        "creation_time" : 1554693337,
        "result" : {
            "txid" : "2979318b051a63281caa23e181ac02d367f1611374981ccd812708d13c3ed550"
        },
        "execution_secs" : 2.25543096
    }
   ]


Additional operations for zcash-cli
+++++++++++++++++++++++++++++++++++

As Zcash is an extension of bitcoin, zcash-cli supports all commands that are part of the Bitcoin Core API (as of version 0.11.2), https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list

For a full list of new commands that are not part of bitcoin API (mostly addressing operations on z-addrs) see :ref:`payment_api`

To list all Zcash commands:

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


## Upgrading 

If you're on a Debian-based distribution, you can follow the :ref:`install-debian-bin-packages-guide` to install Zcash on your system. Otherwise, you can update your local snapshot of our code:

.. code-block:: bash

   git fetch origin

| Ensure you check the current release version from :fa:`github` `here <https://github.com/zcash/zcash>`_ .
| If ``v3.1.0`` was current, issue the following commands:

.. code-block:: bash

   git checkout v3.1.0
   ./zcutil/fetch-params.sh
   ./zcutil/build.sh -j$(nproc)

.. note:: If you don't have ``nproc``, then substitute the number of cores on your system. 
   If the build runs out of memory, try again without the ``-j`` argument, i.e. just ``./zcutil/build.sh``. 
   If you are upgrading from testnet, make sure that your ``~/.zcash`` directory contains only ``zcash.conf`` to start with, and that your ``~/.zcash/zcash.conf`` does not contain ``testnet=1`` or ``addnode=testnet.z.cash``. 
   If the build fails, move aside your ``zcash`` directory and try again by following the instructions in the :ref:`installation` section below.

.. important:: Running ``make clean`` before building the update can eliminate random known link errors. If you ran into any other issues upgrading to Overwinter or Sapling, please see the :ref:`nu_dev_guide`

-->

## References
* [User Guide](user_guide.html)
* [Troubleshooting Guide](troubleshooting_guide.html)
* [Zcash Payment API](payment_api.html)
* [Wallet Backup Instructions](wallet_backup.html)
* [Sending Memos with Zcashd](memos.html)
* [Zcash.conf guide](zcash_conf_guide.html)
* [Zcash Mining guide](zcash_mining_guide.html)
* [Security Warnings](security_warnings.html)
* [Data Directory Files](files.html)
* [Tor Support in zcashd](tor.html)