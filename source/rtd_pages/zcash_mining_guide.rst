:orphan:

.. _zcash_mining_guide:

Zcash Mining Guide
==================

Welcome! In this guide, we'll cover how much you can make by mining Zcash and the various ways to mine Zcash. A win-win: Miners get Zcash, and mining strengthens the Zcash network by adding additional hash power. 

If you need help, talk to us on |discord| or post on the |forum|. 

.. |discord| raw:: html

   <a href="https://discord.gg/PhJY6Pm" target="_blank">discord</a> 

.. |forum| raw:: html

   <a href="https://forum.zcashcommunity.com/" target="_blank">forum</a> 


Calculating mining rewards
--------------------------

We highly recommend you use a |mining-calc| to find out what your expected return is depending on your hash rate and electricity cost. In other words, find out if it's profitable for you, specifically, to mine Zcash before proceeding.  


.. |mining-calc| raw:: html

   <a href="https://www.cryptocompare.com/mining/calculator/zec" target="_blank">Zcash mining calculator</a> 

CPU mining
-----------

Our core platform, zcashd, can be configured to mine blocks in addition to acting as a wallet and verifying network transactions. This is the most accessible way to mine, and can be done on your personal computer. 

1. Set up your local Zcash node. Follow the :ref:`user_guide` up to the end of the section :ref:`ugBuild` , then come back here. 

2. Configure your node as per :ref:`ugConfiguration` , including the section :ref:`Enable_CPU_Mining` .

3. Now, start mining by running zcashd: ``./src/zcashd``. To run it in the background, try: ``./src/zcashd -daemon``. 

  
  Congratulations! You are now mining Zcash.

4. If you wish to verify that you are mining, look in the debug log (`~/.zcash/debug.log`), you should see:

  .. code-block:: bash

   Zcash Miner started

5. To stop, enter the command: ``./src/zcash-cli stop``

Note: The internal `zcashd` miner uses a new transparent address for each mined block. If you want to instead use the same address for every mined block, use the ``-mineraddress=`` option available in Zcash 1.0.6 and later.

ASIC mining
-----------

Another way to mine Zcash is to with specialized devices. An application-specific integrated circuit (ASIC) miner is a device that is designed for the sole purpose of mining—not coal, but rather digital currency. 

Zcash is not ASIC-resistant, and you can purchase Zcash-specific or generalist ASICs that mine Zcash along with various other cryptocurrencies. We advise that you consider the tradeoffs of the cost or purchasing and running an ASIC versus the potential profit before making a purchase.

We do not have any specific recommendations, or provide instructions, for ASIC mining devices. Check with the specific manufacturer and model for details.  

Spending Mining Rewards
-----------------------

Starting with the Heartwood network upgrade (activating Q3 2020), mining rewards can be sent to a shielded address. We recommend this for practical and privacy reasons. 

If coins are mined into a t-addr (transparent address), they can only be spent to a z-addr (shielded address), and must be swept out of the t-addr in one transaction with no change. Refer to our :ref:`payment_api` for instructions
on how to use the ``z_sendmany`` command to send coins from a **t-addr** to a **z-addr**.  You will need at least 4GB of RAM for this operation.


Mining Pools
------------

If you're mining by yourself or at home, you're unlikely to mine any Zcash unless you join a mining pool. A mining pool allows miners to pool resources together and share the hashing power while splitting the reward equally according to the amount of shares they contributed to solving a block. See this community-maintained |pools| for further instructions.

.. |pools| raw:: html

   <a href="https://www.zcashcommunity.com/mining/mining-pools/" target="_blank">list of mining pools</a> 
