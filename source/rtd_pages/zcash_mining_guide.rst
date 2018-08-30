:orphan:

.. _zcash_mining_guide:

Zcash Mining Guide
==================

Welcome! This guide is intended to get you mining Zcash, a.k.a. "ZEC", on the Zcash mainnet. The unit for mining is Sol/s (Solutions per second).

If you run into snags, please let us know. There's plenty of work needed to make this usable and your input will help us
prioritize the worst sharpest edges earlier. For user help, we recommend using our forum:

https://forum.z.cash/

Setup
-----

First, you need to set up your local Zcash node. Follow the :ref:`user_guide` up to the end of the section :ref:`ugBuild` , then come back here. 

Configuration
-------------

Configure your node as per :ref:`ugConfiguration` , including the section 
:ref:`Enable_CPU_Mining` .

Mining
------

Now, start Mining!
``./src/zcashd``

To run it in the background (without the node metrics screen that is normally displayed):

``./src/zcashd -daemon``

You should see the following output in the debug log (`~/.zcash/debug.log`):

.. code-block:: bash

   Zcash Miner started

Congratulations! You are now mining on the mainnet.

To stop the Zcash daemon, enter the command:

``./src/zcash-cli stop``

Spending Mining Rewards
~~~~~~~~~~~~~~~~~~~~~~~

Coins are mined into a t-addr (transparent address), but can only be spent to a z-addr (shielded address), 
and must be swept out of the t-addr in one transaction with no change.
Refer to our :ref:`payment_api` for instructions
on how to use the ``z_sendmany`` command to send coins from a **t-addr** to a **z-addr**. 
You will need at least 4GB of RAM for this operation.


Mining Pools
~~~~~~~~~~~~

If you're mining by yourself or at home, you're most likely to succeed if you join an existing 
mining pool. See this community-maintained `list of mining pools <https://www.zcashcommunity.com/mining/mining-pools/>`_ for further instructions.


P2PKH transactions
~~~~~~~~~~~~~~~~~~

The internal `zcashd` miner inherited from Bitcoin used P2PK for coinbase transactions, 
but Zcash 1.0.6 and later `use P2PKH by default <https://github.com/zcash/zcash/issues/945>`_ , 
following the trend for Bitcoin.


Configuration Options
---------------------

Mine to a single address
~~~~~~~~~~~~~~~~~~~~~~~~

The internal `zcashd` miner uses a new transparent address for each mined block. 
If you want to instead use the same address for every mined block, use the ``-mineraddress=`` 
option available in Zcash 1.0.6 and later.