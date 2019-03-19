:orphan:

.. _sapling_turnstile:

Sprout to Sapling Turnstile Migration
=====================================

Overview
--------

The Sapling network upgrade requires a new type of shielded address to support the new usability and security improvements it brings to Zcash. Sapling shielded addresses start with "zs" whereas the legacy, Sprout shielded addresses start with "zc".

The Sprout to Sapling turnstile migration is an auditing mechanism for the number of ZEC in circulation. Shielded ZEC cannot be accounted for in the total monetary supply because balances remain private to the owners of shielded address private keys. This turnstile migration provides accounting for the ZEC held in Sprout shielded addresses as they are moved to the newer Sapling shielded addresses.

.. image:: images/turnstile.png
   :align: center

There are two levels to this mechanism: user and consensus. The user level mechanism refers to the `zcashd` RPC which prohibits any transaction from being sent directly from a Sprout address to a Sapling address (and vice versa). Users **must** use a transparent address as an intermediary which will obviously expose the balance being migrated. As described in :ref:`zcash_addresses`, all balance transfers from shielded addresses to transparent addresses reveal the value and become associated with those transparent addresses. Transfers from those transparent addresses back into shielded addresses reshield the value. This process is shown in the diagram below.

.. image:: images/turnstile2.png
   :align: center

The consensus level mechanism allows a direct Sprout to Sapling transaction to take place but requires the balance be *passed through* the transparent value pool (see: :ref:`value_pools`) before landing in a Sapling address, thus exposing the value without requiring the use of a transparent address. Because this may not be obvious to users (and therefore a privacy risk), a UX decision was made to limit availability in the RPC. A migration tool is under development to make use of this consensus level mechanism. See :ref:`migration_tool` below.

Checking the Value Pool Totals
------------------------------

It's possible to use your own node to check the total value in each shielded value pool  with a single RPC call to `getblockchaininfo`. One way to issue that is to call ``zcash-cli getblockchaininfo`` on a computer running a properly-functioning zcashd. The resulting JSON blob contains the perceived totals in the valuePool field. If the value corresponding with the "monitored" json key within the "Sprout" or "Sapling" entries are true, then your values for the pools are correct. If either of them are false, then your figures are wrong and you shouldn't rely on them, and you will need to reindex your node with ``zcashd -reindex`` to turn "monitored" to "true" at which point you can trust those figures.

The value pools are also monitored at the third-party website `zcha.in <https://zcha.in/statistics/network>`_.

.. _migration_tool:

Migration Tool
--------------

We plan to release a Sprout to Sapling migration tool to help users who have funds stored in older Sprout addresses migrate them to a newer Sapling address without accidentally leaking data which could publicly correlate them to their balances.

If you are a user who stores funds in older Sprout addresses, we recommend you wait for this new tool before migrating your funds. This tool is specified in a `Draft ZIP <https://github.com/zcash/zips/pull/197/files>`_.

The primary goal for development of this tool is protecting the users' privacy via automation to avoid human error or misunderstanding (yes, even advanced users). It makes use of the consensus level migration mechanism instead of manual migration which requires the use of transparent addresses described in the Overview section of this page. With that disclaimer, we are providing privacy recommendations below for users who still want to proceed with manual migration.

	   
Privacy Recommendations
------------------------------------------

There are several privacy recommendations that users should follow in order to retain privacy during a manual migration.

:fa:`arrow-circle-right` Use transparent addresses once for migrating shielded funds

  - Do not use transparent addresses which have already received funds.
  - Discard transparent addresses after migration is completed.
  - Use a unique transparent address for each balance migration.

:fa:`arrow-circle-right` Split balances into multiple migrations

  - Some users might prefer to not reveal the exact shielded balance in a single transfer.
  - Remember to use a unique, unused transparent addresses for splitting a balance across transfers.
  - A balance that is evenly divided across multiple migrations will have a higher chance of correlation..
  - Split balances will also have a higher chance of correlation the closer they are in block time. 

.. note::

   Splitting a shielded balance into multiple transfers is a matter of user preference and might not be the best approach for everyone. Using unused transparent addresses for the Sapling migration and discarding afterwards is **highly recommended for all users**.

   
Examples
--------

   Alice has a shielded balance of 14.6727 ZEC and doesn't want to reveal that a single address holds that exact value as she migrates to a new Sapling shielded address. She decides that paying six transaction fees to migrate is worth the cost to not reveal the total balance.

   To do this, Alice generates 3 new transparent addresses ``t1abc...``, ``t1def...`` and ``t1xyz..`` and picks 3 unequal values that add up to her total balance ``10``, ``4.0001`` and ``0.6756``.

   She initiates the first transaction, to the first fresh transparent address revealing 10 ZEC in address ``t1abc...``. This leaves 4.6726 ZEC in the legacy address accounting for the first transaction fee. Once confirmed, Alice sends 9.999 ZEC (accounting for the second transaction fee) from ``t1abc...`` to her new shielded Sapling address.

   She waits a couple of hours before initiating the second transfer, revealing 4.0001 ZEC in address ``t1def...``. This leaves 0.6724 ZEC in the legacy address accounting for the third transaction fee. Once confirmed, she finishes the second transfer by sending 4 ZEC (accounting for the fourth transaction fee) to the same Sapling address. The balance in the shielded Sapling address is now 13.999 ZEC.

   She waits for the next day to initiate the third and final transfer, revealing 0.6723 ZEC (accounting for the fifth transaction fee) in address ``t1xyz...``. Once the transaction is confirmed, the legacy Sprout address is now empty and a may be discarded. She finishes the final transfer by sending 0.6722 ZEC (accounting for the sixth transaction fee) to her Sapling address which now has a balance of 14.6721 ZEC (the original balance minus six transaction fees).

.. note::

   If fees are not a concern, users are advised to split balances transactions which send values in powers of ten (.001, .01, .1, 1, 10, 100, 1000, etc.). A user with a balance of 139.34 ZEC using this method would migrate 100 ZEC once,10 ZEC three times,1 ZEC nine times,.1 ZEC three times and .01 ZEC four times. This adds up to 20 migrations and 40 transactions. At the default fee rate (.0001 ZEC per transaction) this would cost .004 ZEC.

   If time is not a concern, users are advised to delay migrating their split balances over intervals of time that are sufficiently random (between 2 and 100+ hours). A user with 40 transactions to complete their migration of 20 balances using this method could pick 40 random hour intervals in which to send the transactions.
   
Additional Reading
------------------

:fa:`arrow-circle-right` `Sapling Addresses & Turnstile Migration <https://blog.z.cash/sapling-addresses-turnstile-migration/>`_

:fa:`arrow-circle-right` `Anatomy of a Zcash Transaction <https://blog.z.cash/anatomy-of-zcash/>`_

:fa:`arrow-circle-right` `Transaction Linkability <https://blog.z.cash/transaction-linkability/>`_
