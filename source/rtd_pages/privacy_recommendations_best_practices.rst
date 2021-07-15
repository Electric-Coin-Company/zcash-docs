.. _Privacy Recommendations and Best Practices:

Privacy Recommendations and Best Practices
==========================================

There are simple best practices to follow to minimize data leakage and protect your financial privacy. This post outlines important considerations for users who want to maintain optimal transaction privacy, no matter which supporting software (wallets, exchanges, web browsers) is being used.

Shielding Funds
----------------

One of the most important ways to maintain financial privacy with Zcash is by holding a certain amount or all of your funds in a shielded address. The more funds held in shielded pools, the greater the overall privacy of the network.

**Privacy Protection Best Practices for Shielded Zcash**

1. Store more Zcash on a shielded address than is need for any single transaction
2. Do not leak metadata such as the tx id, tx amount, or counterparty information as they can be used to create linkages.
3. Do not share viewing keys without understanding privacy implications

Pass-through Linkability
------------------------

`Transaction linkability <https://electriccoin.co/blog/transaction-linkability/>`_ is the ability to connect unique transactions to an individual address or group of addresses through monitoring activity on-chain. Partial and fully shielded transactions help mitigate and greatly reduce transaction linkability but people should still be mindful of meta-data leakages. 

Pass-through operations are when a given amount of ZEC is “passed-through” addresses, most commonly to break linkability.

Network Graph Analysis
----------------------

A unique IP address can allow network observers to correlate your Zcash transactions with each other and with your other traffic. Zcash is a global network using IP addresses over TCP for maintaining connections between nodes and does not obfuscate users’ IP addresses.

Users should be aware that when an adversary knows a person’s IP address, other private details can easily be discovered (names, locations, business interests, etc). For example, in Zcash, correlations can be made between transactions sent from shielded addresses and those sent from transparent addresses.

Additional Recommendations
--------------------------

- The transaction fees are publicly visible for all transactions, so when using a shielded address it’s best for privacy to rely on a privacy-focused wallet to select a fee rather than to select them manually.
- While it is safe to reuse one shielded address for receiving payments for a single purpose (e.g. donations to a non-profit), using one shielded address to receive payments for multiple purposes (e.g. a business service and donations to a non-profit), makes it possible for someone to compare the contexts where the address is used and build an identity profile.
- Be aware of IP linkability between transactions sent from shielded addresses and your other network traffic.
- Advanced users :ref:`may use Tor<tor>` to obfuscate the IP address of their Zcash node.

Security Considerations for zcashd
----------------------------------
> Warnings & Recommendations (applicable on any platform)

- Wallet encryption is disabled, use full-disk encryption (or encryption of your home directory) to protect your wallet at rest. 
- Ensure no other users have the ability to execute code (even unprivileged) on the hardware your zcashd process runs on unless you have fully analysed your operational security.
- Make regular backups of your wallet.
- Do not change the default setting that only allows RPC connections from localhost.
- Use a minconf of 15 (minimum number of confirmations) to defend against potential blockchain reorganizations (note: we may increase this number if ongoing research reveals notable risks).
- Setting ``the-debug=zrpcunsafe`` configuration is helpful for diagnosing issues but the log will contain private information, so be careful when sharing the contents of it with others. If this is too much liability, use ``-debug=zrpc`` instead.

When you send a transaction, your node sends the transaction to other nodes that are part of the Zcash peer-to-peer network. By observing that your node was the first to broadcast the transaction, those nodes may learn that your node created the transaction. To prevent this, configure zcashd to use Tor.

References
----------

:fa:`arrow-circle-right` `Transaction Linkability <https://electriccoin.co/blog/transaction-linkability/>`_

:fa:`arrow-circle-right` `A Shielded Ecosystem <https://electriccoin.co/blog/shielded-ecosystem/>`_ 

:fa:`arrow-circle-right` `Anatomy of A Zcash Transaction <https://electriccoin.co/blog/anatomy-of-zcash/>`_ 

:fa:`arrow-circle-right` `Payment Contexts & Reusing Shielded Addresses <https://electriccoin.co/blog/shielded-address-contexts/>`_

:fa:`arrow-circle-right` `The Encrypted Memo Field <https://electriccoin.co/blog/encrypted-memo-field/>`_
