:orphan:
.. _troubleshooting-guide:

Troubleshooting Guide
=====================

The following is a list of questions for troubleshooting zcashd, the core Zcash client software. For general FAQ, see https://z.cash/support/faq.html. 

System Requirements
-------------------

    | :fa:`linux` 64-bit Linux (easiest with a Debian-based distribution)
    | :fa:`th-list` A compiler for C++11 if building from source. Gcc 6.x and above has full C++11 support, and gcc 4.8 and above supports some but not all features. Zcash will not compile with versions of gcc lower than 4.8.
    | :fa:`database` At least 4GB of RAM to generate shielded transactions.
    | :fa:`database` At least 8GB of RAM to successfully run all of the tests.

Zcash runs on port numbers that are 100 less than the corresponding Bitcoin port number. They are:

    | :fa:`plug`  ``8232`` for mainnet RPC
    | :fa:`plug` ``8233`` for mainnet peer-to-peer network
    | :fa:`plug` ``18232`` for testnet RPC
    | :fa:`plug` ``18233`` for testnet peer-to-peer network

Building from source
--------------------

If you did not build by running `build.sh`, you will encounter errors. Be sure to build with:

``$ ./zcutil/build.sh -j$(nproc)``

.. note:: If you don't have nproc, then substitute the number of your processors.

.. code-block:: bash
  
   Error message: g++: internal compiler error: Killed (program cc1plus) 

This means your system does not have enough memory for the building process and has failed. Please allocate at least 4GB of computer memory for this process and try again.

.. code-block:: bash

   Error message: 'runtime_error' (or other variable) is not a member of 'std'. compilation terminated due to -Wfatal-errors. ``

Check your compiler version and ensure that it support C++11. If you're using a version of gcc below 4.8.x, you will need to upgrade.

.. code-block:: bash

   Error message: gtest failing with undefined reference ``

If you are developing on different branches of Zcash, there may be an issue with different versions of linked libraries. Try ``make clean`` and build again.

Running zcashd
--------------

| Trying to start zcashd for the first time, it fails with:

.. code-block:: bash

   could not load param file at /home/rebroad/.zcash-params/sprout-verifying.key

You didn't fetch the parameters necessary for zk-SNARK proofs. If you installed the Debian package, run `zcash-fetch-params`. If you built from source, run `./zcutil/fetch-params.sh`.

zcashd crashes with the message:

.. code-block:: bash
   
   ``std::bad_alloc`` or ``St13runtime_exception``

These messages indicate that your computer has run out of memory for running zcashd. This will most likely happen with mining nodes which require more resources than a full node without running a miner. This can also happen while creating a transaction involving a z-address. You'll need to allocate at least 4GB memory for these transactions.

Zcashd commands
---------------

To get help with the RPC interface from the command line, use: 

* ``zcash-cli help``, which lists all zcash-cli commands.  
* ``zcash-cli help $COMMAND``, which lists details of a specific command.

There is also additional documentation under :ref:`payment_api` . 


Restoring from backup
----------------------

`zcash-cli` stops responding after using the command `z_importkey`

The command has added the key, but your node is currently scanning the blockchain for any transactions related to that key, causing there to be a delay before it returns. This immediate rescan is the default setting for `z_importkey`, which you can override by adding `false` to the command if you simply want to import the key, i.e. `zcash-cli z_importkey $KEY false`


Custom transactions
----------------------

If, when attempting to execute the ``sendrawtransaction`` RPC method, you receive the error:

.. code-block:: bash

   AcceptToMemoryPool: absurdly high fees

This is most likely caused by not specifying an output address to receive the change when creating the transaction (``createrawtransaction``). This RPC call, unlike ``sendmany`` and ``z_sendmany``, does not do this automatically.

With ``createrawtransaction``, the fee is simply the sum of the inputs minus the sum of the outputs. If this difference is larger than 0.0021 ZEC (210000 zatoshis), the assumption is that this is unintentional, and the transaction is not sent. If you really do wish to send a transaction with a large fee, add ``true`` to the end of the ``sendrawtransaction`` command line. This will allow an arbitrarily high fee.

#### 

.. admonition:: What if my question isn't answered here?

  Hop on the `Zcash Dischord <https://discord.gg/GGtsUzyp>`_ to chat with ECC, maintainers of zcashd, and community members. 

  Search the issues section (https://github.com/zcash/zcash/issues) to see if someone else has posted a similar issue and if not, feel free to report your problem there. Please provide as much information about what you've tried and what failed so others can properly assess your situation to help.

.. important:: If you have issues with a network upgrade, please see the :ref:`nu_dev_guide`