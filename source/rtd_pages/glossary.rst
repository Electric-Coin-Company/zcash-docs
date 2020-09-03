:orphan:
.. _glossary:

Glossary
========

.. _address:
.. _addresses:

Address
    A Zcash address is similar to a physical address or an email address. It is the only information you need to provide for someone to send you `ZEC`_. There are two types of addresses in Zcash: a `shielded address`_ and a `transparent address`_.

.. _block:
.. _blocks:

Block
    A block is a record in the Zcash blockchain that contains a set of transactions sent on the network. Pending inclusion in a block, a transaction is kept in the `mempool`_ in an `unconfirmed`_ state. Roughly every 2.5 minutes, on average, a new block is appended to the `blockchain`_ through `mining`_ and the transactions included receive their first `confirmation`_.

.. _block reward:
.. _block rewards:

Block reward
    A block reward is new `ZEC`_ released into the network after the successful `mining`_ of a block. For the first four years, the block reward in Zcash is split into a `miners' reward` and a `founders' reward`. During this time, miners receive 80% (or 10 `ZEC`_) per block with the remaining 20% (or 2.5 ZEC) split between a range of beneficiaries including an `Electric Coin Company`_ strategic reserve, the `Zcash Foundation`_ and many stakeholders including Zcash founders, employees, investors and advisors. After 850,000 `blocks`_, the block reward halves for the first time and miners start to receive 100% of the block reward (6.25 ZEC). Each subsequent 840,000 blocks triggers a new block reward halving.
    
.. _blockchain:

Blockchain
    The blockchain is a public record of Zcash transactions in chronological order. The blockchain is shared between all Zcash users. It is used to verify the permanence of Zcash transactions and to prevent `double spending`_.

.. _confirmed:
.. _unconfirmed:
.. _confirmation:
.. _confirm:

Confirmation
    A transaction confirmation first occurs when that transaction has been included in a `block`_ and gains an additional confirmation for each subsequent block. The more confirmations a transaction has, the higher the security from a potential reversal (see: `rollback`_). Some may consider a single confirmation to be secure for low value transactions, although it is generally recommended to wait for 10+ confirmations. 

.. _cryptography:

Cryptography
    Cryptography is the branch of mathematics that lets us create mathematical proofs that provide high levels of security and privacy. Services like online commerce and banking already use cryptography and in many countries, are required by law to protect customers and their data. In the case of Zcash, cryptography is used to:
    
    #. protect user privacy (via `zk-SNARKs`_)
    #. make it impossible for anybody to spend funds from another user's wallet
    #. prevent corruption of the blockchain database

.. _Electric Coin Company:
   _Zcash Company:

Electric Coin Company
    This is the abbreviation for the Electric Coin Company, the team behind the `Zcash protocol`_, previously known as the Zcash Company.

.. _encrypted memo:

Encrypted memo
    The encrypted memo is an additional field for `transactions`_ sent to `shielded addresses`_ that is visible to the recipient of a payment. The encrypted memo is visible only the to the sender and recipient, unless the `viewing key`_ or `payment disclosure`_ gets shared with a third party. 
       
.. _equihash:

Equihash
    Equihash is a proof-of-work `mining`_ algorithm that is memory-oriented with very efficient verification.

.. _experimental feature:

Experimental feature
    An experimental feature is one that is available to users on the main `Zcash network`_ but should undergo further testing by users and developers. Users must explicitly opt into enabling an experimental feature until they become fully supported.
    
.. _double spend:
.. _double spent:
.. _double spending:

Double spend
    A double spend happens when a user sends the same `ZEC`_ to two different recipients. Zcash `miners`_, the Zcash `blockchain`_ and `zk-SNARKs`_ are integral for only allowing one transaction to `confirm`_ and be considered valid.       

.. _mempool:
.. _memory pool:    

Memory pool
    The memory pool (or `mempool` for short) is a temporary staging location for `transactions`_ which have been verified by nodes in the `Zcash network`_ but have not yet been included in a `block`_. Transactions in the memory pool are considered `unconfirmed`_.
    
.. _mining:
.. _miners:
.. _mined:

Mining
    Mining is the process where for each `block`_, nodes in the Zcash network compete by doing complex mathematical calculations to find a solution based on a self-adjusting difficulty. Zcash miners are rewarded with both the `transaction fees`_ of the `transactions`_ they confirm and `block rewards`_. Zcash uses a proof-of-work mining algorithm called `Equihash`_.

.. _multisig:

Multi-signature
    A multi-signature address (also referred to as `multisig`) is a type of `address`_ which requires multiple `private key`_  `signatures`_ in order to spend funds. This is a security mechanism to protect against theft or loss of a private key. Currently, multisig functionality is only supported by `transparent addresses`_. 
    
.. _network upgrade:
.. _network upgrades:

Network upgrade
    A network upgrade is a `software-updates-required` release of the Zcash software. After `activation`_ of a network upgrade, network nodes running older versions that are not compatible with the upgrade will be forked onto an outdated `blockchain`_ and will require a software upgrade to rejoin the main network. This is sometimes referred to as a `hard fork` upgrade. 

.. _Overwinter:

Overwinter
    Overwinter is the first `network upgrade`_ for Zcash. Its purpose is strengthening the protocol for future network upgrades. It includes versioning, replay protection for network upgrades, performance improvements for transparent transactions and the `transaction expiry`_ feature. Overwinter `activated`_ at `block`_ height 347500.
    
.. _payment disclosure:

Payment disclosure
  A payment disclosure is a method of proving that a payment was sent to a `shielded address`_ by revealing the value, receiving address and optional `encrypted memo`_. The current implementation of this is as an `experimental feature`_.
    
.. _private key:
.. _private key(s):

Private Key
    A private key is a secret string of data that gives access to spend the `ZEC`_ balance of an associated `address`_ through a cryptographic `signature`_. Your private key(s) may be stored directly in your computer or smartphone, with a custodian such as an exchange or a combination of both using `multisig`_. Private keys are important to keep safe as they are the only access to spending the funds you may own. For securing your private keys with the zcashd client, review the :ref:`wallet_backup`.

.. _public parameters:

Public parameters
    The Zcash public parameters are a set of global constraints required for constructing and verifying the `zk-SNARKs`_ used for `shielded addresses`_. 

.. _rollback:

Rollback
    A rollback is when a blockchain is rewound to a previous state and a set of the most recent `blocks`_ and the `transactions`_ they contain are discarded. Zcash has a rollback limit of 100 blocks.

.. _sapling:

Sapling
    Sapling is a `network upgrade`_ that introduces significant efficiency improvements for shielded transactions that will pave the way for broad mobile, exchange and vendor adoption of Zcash shielded addresses. Sapling is scheduled to `activate`_ at `block`_ height 419200. 
    
.. _selective disclosure:    
    
Selective disclosure
    Selective disclosure refers to the features of `shielded addresses`_ where the owner may `selectively disclose` shielded transaction data. A user may share a `viewing key`_ or `payment disclosure`_ with any third party, allowing them to access shielded data while maintaining privacy from others. 
    
.. _zaddr:
.. _shielded address:    
.. _shielded addresses:

Shielded address
    A shielded `address`_ (also referred to as a `zaddr`) sends or receives `transactions`_ such that the address, associated value and `encrypted memo`_ are not visible on the Zcash `blockchain`_. These addresses start with the letter `z`.  A shielded address uses `zk-SNARKs`_ to protect transaction data for value sent or received to it. A transaction consisting of only shielded addresses is called a `shielded transaction`_. A transaction consisting of both shielded addresses and `transparent addresses`_ only protects the data associated with the shielded address. Each shielded address has a `spending key`_ and `viewing key`_.

.. _shielded transaction:

Shielded transaction
    A shielded transaction is a transaction exclusively between `shielded addresses`_. The addresses, value and optional `encrypted memo`_ are shielded using `zk-SNARK`_  `cryptography`_ before the transaction is recorded in the `blockchain`_. 

.. _signature:
.. _signatures:

Signature
    A cryptographic signature is a mathematical scheme that allows someone to authenticate digital information. When your Zcash `wallet`_ signs a transaction with the appropriate `private key`_, the network can confirm that the signature matches the `ZEC`_ being spent. This signing is confirmed publicly for `transparent addresses`_ and through the use of `zk-SNARKs`_ for `shielded addresses`_. 
    
.. _hash rate:
.. _solution rate:
.. _Sol/s:

Sol/s
    Sol/s refers to solutions per second and measures the rate at which `Equihash`_ solutions are found. Each one of those solutions is tested against the current target (after adding to the block header and hashing), in the same way that in Bitcoin each nonce variation is tested against the target.

.. _spending key:

Spending key
    A spending key is a type of `private key`_ that allows any user in possession of it to spend the balance of the associated `address`_. For `shielded addresses`_, possessing the spending key also allows the user to view the address' balance and `transaction`_ data.

.. _Sprout:

Sprout
    Sprout is the first version of Zcash, launched on October 28, 2016. 
    
.. _TAZ:

TAZ
    TAZ is the three letter code for the valueless Zcash `testnet`_ currency.

.. _testnet:

Testnet
    The Zcash testnet is an alternative `blockchain`_ that attempts to mimic the main `Zcash network`_ for testing purposes. Testnet coins (sometimes referred to as `TAZ`_) are distinct from actual `ZEC`_ and do not have value. Developers and users can experiment with the testnet without having to use valuable currency. The testnet is also used to test `network upgrades`_ and their `activation`_ before committing to the upgrade on the main `Zcash network`_.

.. _transaction:
.. _transactions:

Transaction
    A transaction is a payment between users. They are locally created by the user or service then submitted to the `Zcash network`_ for verification by nodes and eventual `confirmation`_ into a `block`_.

.. _transaction expiry:
.. _transaction expires:

Transaction expiry
    A transaction expires after staying `unconfirmed`_ in the `mempool`_ for too long and is discarded. Once a transaction expires, it may be resubmitted to the network or a new transaction may be submitted in its place. The default expiry in Zcash is 20 `blocks`_.
    
.. _transaction fee:
.. _transaction fees:

Transaction fee
    A transaction fee is an additional value added to a `transaction`_ used to incentivize `miners`_ to include the transaction into a `block`_. Transactions with low or no fee may still be mined but transactions with the default fee or higher will be preferred. If a transaction has too low of a fee, it may stay in the `mempool`_ until the `transaction expires`_. The fee value is not protected for transactions containing `shielded addresses`_ and therefore it is recommended to always use the default fee of `.0001 ZEC`. Unique fees may result in loss of privacy in some cases.

.. _taddr:
.. _transparent address:    
.. _transparent addresses:

Transparent address
    A transparent `address`_ (also referred to as a `taddr`) sends or receives `transactions`_ such that the address and associated value are publicly recorded on the Zcash `blockchain`_. These addresses start with the letter `t`.  A transparent address does not use `zk-SNARKs`_ to protect transaction data for value sent or received to it. A transaction consisting of only transparent addresses reveals the entire transaction. A transaction consisting of both transparent addresses and `shielded addresses`_ only reveals the data associated with the transparent address.

.. _transparent transaction:

Transparent transaction
    A transparent transaction is a transaction exclusively between `transparent addresses`_. The addresses and value are recorded publicly on the `blockchain`_.

.. _upgrade activation:
.. _activation:
.. _activate:
.. _activated:

Upgrade activation
    An upgrade activation is a specific `block`_ height that triggers a `network upgrade`_. 
    
.. _viewing key:

Viewing key
    A viewing key is a type of `private key`_ that allows any user in possession of it to view the balance and transaction data of the associated `shielded address`_.
    
.. _wallet:

Wallet
    A Zcash wallet contains `private key(s)`_ which allow the owner to spend the `ZEC`_ balance it contains. Each Zcash wallet can show you the total balance of all `ZEC`_ it controls and lets you pay a specific amount to a specific `address`_, just like a real wallet you keep in your pocket or purse. This is different to credit cards where customers are charged by the merchant.

.. _Zcash network:

Zcash network
    The Zcash network is a `peer-to-peer` network of nodes where each node may interact directly with the others for broadcasting newly submitted `transactions`_, `mined`_ `blocks`_ and various other messages that regulate behavior. This type of structure removes the need for a trusted regulating central party.
    
.. _Zcash protocol:

Zcash
    Zcash is an in-production cryptocurrency implementation of the Zerocash protocol, with security fixes and improvements to performance and functionality. It bridges the existing transparent payment scheme used by Bitcoin with a `shielded` payment scheme secured by `zk-SNARKs`_. It implements the `Equihash`_ proof-of-work `mining`_ algorithm. Both the network and the associated currency are referred to as `Zcash` with `ZEC`_ referring specifically to the currency.

.. _Zcash Foundation:

Zcash Foundation
    The Zcash Foundation is a 501(c)3 non-profit dedicated to building Internet payment and privacy infrastructure for the public good, primarily serving the users of the Zcash protocol and blockchain.

.. _ZEC:

ZEC
    ZEC is the three letter currency code for the Zcash cryptocurrency. It is also used to help distinguish the `Zcash network`_ from the currency. Note that some exchanges use `XZC` as the Zcash currency code to conform with the `ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217#X_currencies>`_ standard for currencies and similar assets not associated with a nation.

.. _Zerocash:

Zerocash
    Zerocash is a cryptographic protocol invented by Eli Ben-Sasson, Alessandro Chiesa, Christina Garman, Matthew Green, Ian Miers, Eran Tromer, and Madars Virza in 2014. It improves on the earlier `Zerocoin`_ protocol developed by some of the same authors both in functionality and efficiency. 
    
.. _Zerocoin:

Zerocoin
    Zerocoin is a cryptographic protocol invented by Ian Miers, Christina Garman, Matthew Green, and Aviel D. Rubin in 2013. It is a less efficient predecessor of `Zerocash`_.

.. _zk-SNARKs:
.. _zk-SNARK:

zk-SNARKs
    A zk-SNARK is a particular form of zero-knowledge proof used in the `Zcash protocol`_ which allows `shielded addresses`_ to prove the validity of associated `transactions`_ without revealing the `address`_ or value transacted. For Bitcoin and `transparent addresses`_, `miners`_ can verify that a transaction has not been `double spent`_ because the addresses and their balances are publicly visible within transactions. zk-SNARKs allow this same double spend protection for shielded addresses. The term, which stands for `zero-knowledge Succinct Non-interactive ARguments of Knowledge`,  was first used in the `Zerocash`_ whitepaper. 



    




    
