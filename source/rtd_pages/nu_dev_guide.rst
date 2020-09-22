:orphan:
.. _nu_dev_guide:

Network Upgrade Guide
=====================

We recommend all wallets, exchanges, and clients that accept/support Zcash to follow 
these guidelines to prepare for the upcoming network upgrade. Network upgrades on 
a bi-annual basis to maintain the Zcash network.

Below is general advice that applies to all network upgrades:

:fa:`arrow-circle-right` Keep your zcashd node updated
    Check that you are running the latest stable version of `zcashd <https://z.cash/download.html>`_

:fa:`arrow-circle-right` Version verifiability
    Clearly state the version of Zcash in a place users can find it.
    Somewhere inside the client’s user interface, state the protocol
    name and version number (available from the getblockchaininfo method). 
    This allows users to check what version of Zcash their client is running.

:fa:`arrow-circle-right` Pre-upgrade notification
    Inform users that a network upgrade is happening 
    before it happens. 4000 blocks (approximately a week) in advance, tell 
    users a network upgrade is happening soon, and that transactions will be 
    unavailable for about an hour at the activation block height.

:fa:`arrow-circle-right` Defensive transition
    Disable the initiation of new transactions starting 48 blocks (approximately
    one hour) before the activation block-height. If a user sends a transaction 
    right before the upgrade, it is likely to not make it onto the chain. 
    This can cause user confusion and frustration.

:fa:`arrow-circle-right` Post-upgrade notification
    Tell users when the upgrade has finished and re-enable initiation of 
    transactions. Notify users with a message or at their next login after 
    the network transition. 

:fa:`bullseye` Heartwood
------------------------

Heartwood is the fourth network upgrade for Zcash and enables more third-party integrations and better privacy through shielded coinbase.

:fa:`arrow-circle-right` Consensus Branch ID change
    See `ZIP 250 <https://zips.z.cash/zip-0250>`_

:fa:`arrow-circle-right` Flyclient Support
    Flyclient, specified through `ZIP 221 <https://zips.z.cash/zip-0221>`_, enables efficient proofs of Proof-of-Work for light clients. In addition to enabling improved light-client wallets, this improves many cross-chain protocols. This ZIP specifies modifications to be made to the Zcash block header format to include Merkle Mountain Range (MMR) commitments.

:fa:`arrow-circle-right` Shielded Coinbase
    `ZIP 213 <https://zips.z.cash/zip-0213>`_ defines modifications to the Zcash consensus rules that enable coinbase funds to be mined to shielded Sapling addresses. It does not disable the use of transparent addresses in coinbase transactions.

:fa:`certificate` Blossom
-------------------------

Blossom is the third network upgrade for Zcash.

`Shorter Block Target Spacing <https://github.com/zcash/zips/blob/master/zip-0208.rst>`_

This feature increases the frequency of blocks, allowing transactions to resolve faster. This will 
improve Zcash’s usability and increase how many transactions per hour the 
network can sustain while keeping transaction fees low. This feature has undergone
a specification audit. It is currently being tested on testnet as part of
the Blossom Network Upgrade Pipeline, before version 2.1.0 of zcashd
supporting mainnet activation is released in September.


:fa:`arrow-circle-right` Consensus Branch ID change
    See `ZIP 206 <https://github.com/zcash/zips/blob/master/zip-0206.rst>`_

:fa:`arrow-circle-right` Amount of FR to be paid in coinbase transaction
    See `ZIP 208 <https://github.com/zcash/zips/blob/master/zip-0208.rst>`_ and `Protocol Section 7.7 <https://github.com/zcash/zips/blob/master/protocol/protocol.pdf>`_

:fa:`arrow-circle-right` Function from block height to FR has changed 
    See `ZIP 208 <https://github.com/zcash/zips/blob/master/zip-0208.rst>`_ and `Protocol Section 7.8 <https://github.com/zcash/zips/blob/master/protocol/protocol.pdf>`_



:fa:`leaf` Sapling
------------------

Sapling is a network upgrade that introduces significant efficiency improvements for shielded transactions that will pave the way for broad mobile, exchange and vendor adoption of Zcash shielded addresses.

:fa:`arrow-circle-right` Transaction formatting
    All transactions must use the new transaction format from Sapling onwards. Make sure that you can parse these `v4` transactions. Previous formats will not be valid after the Sapling upgrade, so if you create transactions, the `v4` format must be used after the upgrade has activated (but not until then). Hardware wallets and SPV clients are particularly affected here.

   See `ZIP 243 <https://github.com/zcash/zips/blob/master/zip-0243.rst>`_. Test vectors for ZIP 243 have been pushed and are being reviewed.

:fa:`arrow-circle-right` Shielded HD Wallets
    All Sapling addresses will use hierarchical deterministic key generation according to `ZIP 32 <https://github.com/zcash/zips/blob/master/zip-0032.rst>`_ (``keypath m/32'/133'/k' on mainnet``). Transparent and Sprout addresses will still use traditional key generation.
    
    See `ZIP 32 <https://github.com/zcash/zips/blob/master/zip-0032.rst>`_.

Also see `Sapling Protocol Specification <https://github.com/zcash/zips/blob/master/protocol/protocol.pdf>`_.


General Guidelines
++++++++++++++++++

Using zcashd unmodified
^^^^^^^^^^^^^^^^^^^^^^^

If you use the RPC as provided in the zcashd client, which is true for *most* exchanges and general users of Zcash, you must update your zcashd node to at least version 2.0.1.

For an updated list of specific parameter changes for Sapling in the zcashd wallet RPC, please see: :download:`Sapling RPC Updates v2.0.1 <pdfs/Sapling-RPC-Updates-v2.0.1.pdf>` (PDF).

Additionally, Sapling introduces new parameters which must be downloaded by running the ``fetch-params.sh`` script. These new parameters are placed in the same directory as the older Sprout parameters.

Using custom code to create/sign/send transactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you manually create transactions, the following changes are `critical`. Reference section 7.1 of the `Sapling specification <https://github.com/zcash/zips/blob/master/protocol/protocol.pdf>`_ for complete details:

- The transactions version number **MUST** be 4.
- The version group ID **MUST** be 0x892F2085.
- At least one of tx_in_count, nShieldedSpend, and nJoinSplit **MUST** be nonzero.
- If version ≥ 4 and nShieldedSpend + nShieldedOutput > 0 then:

  - Let bvk and SigHash be as defined in §4.12 **‘Balance and Binding Signature (Sapling)’**;
  - bindingSig **MUST** represent a valid signature under the *transaction binding verification key* bvk of SigHash - i.e. BindingSig.Verify\ :sub:`bvk`\ (SigHash, bindingSig) = 1.
- If version ≥ 4 and nShieldedSpend + nShieldedOutput = 0, then valueBalance **MUST** be 0.
- A coinbase transaction  **MUST NOT** have any *JoinSplit descriptions, Spend description, or Output descriptions*. 
- valueBalance **MUST** be in the range {-MAX_MONEY .. MAX_MONEY}.

In addition, consensus rules associated with each JoinSplit description (§7.2 **‘Encoding of JoinSplit Descriptions’**) each Spend description (§7.3 **‘Encoding of Spend Descriptions’**) and each Output description (§7.4 **‘Encoding of Output Descriptions’**) **MUST** be followed.

Mining Pools
^^^^^^^^^^^^

Mining pools running the Stratum protocol will have to make some changes as well.

The ``hashReserved`` field in the Stratum Protocol will have to be replaced by the ``hashFinalSaplingRoot`` field from the block header (§7.5 **‘Block Header’**).

Testing
+++++++

Sapling is currently activated on testnet. To test transactions you’ll want to follow the :ref:`testnet_guide`. Alternatively, developers can use these features in regtest mode.

    
:fa:`snowflake-o` Overwinter
----------------------------

Overwinter is the first network upgrade for Zcash. Its purpose is strengthening 
the protocol for future network upgrades. It includes versioning, replay 
protection for network upgrades, performance improvements for transparent 
transactions, a new feature of transaction expiry, and more.

Overwinter activated successfully at block ``347500``,  mined at ``June 25``, 
``2018 20:42 UTC-04:00``

:fa:`arrow-circle-right` Transaction formatting
    All transactions must use the new transaction format from Overwinter and onwards. 
    Make sure that you can parse these “v3” transactions (write a parser for them if 
    you aren’t using our code). Previous formats will not be valid after the Overwinter 
    upgrade, so if you create transactions, the “v3” format must be used after the 
    upgrade has activated (but not until then). Hardware wallets and SPV clients 
    are particularly affected here. See ZIPs `202 <https://github.com/zcash/zips/blob/master/zip-0202.rst>`_
    and `203 <https://github.com/zcash/zips/blob/master/zip-0203.rst>`_ .

:fa:`arrow-circle-right` Transaction version number
     The 4-byte transaction version will have its most significant bit set from 
     Overwinter and onwards, for two-way replay protection of Overwinter and 
     unambiguous transaction parsing of all current and future formats. For 
     example, existing “v1” and “v2” transactions use version numbers “1” 
     and “2”, but “v3” Overwinter transactions will use the unsigned version
     number “(1 << 31) | 3” in the transaction serialization format. See ZIP 
     `202 <https://github.com/zcash/zips/blob/master/zip-0202.rst>`_ .

:fa:`arrow-circle-right` Version group IDs
    A transaction version will be uniquely paired with a version group ID to 
    ensure unambiguous transaction parsing. For example, a “v3” transaction 
    will always have the version group ID "0x03C48270" in its serialization 
    format, even after future network upgrades. See ZIP `202
    <https://github.com/zcash/zips/blob/master/zip-0202.rst>`_ .

:fa:`arrow-circle-right` Branch IDs
    Each network upgrade has an associated branch ID that identifies its 
    consensus rules. For two-way replay protection, creating transactions
    will require the branch ID of the current chain tip when signing a 
    transaction (in the BLAKE2b personalization field.) You can obtain 
    the branch ID of any block height from the getblock API. See ZIP 
    `200 <https://github.com/zcash/zips/blob/master/zip-0200.rst>`_ .

:fa:`arrow-circle-right` Signature hashing
    There are new SegWit-like features in this upgrade, such as transaction 
    signatures committing to values of the inputs. We suggest reusing code 
    from SegWit (e.g. for hashing transparent outputs) when implementing the 
    new SignatureHash function. See ZIP `143 <https://github.com/zcash/zips/blob/master/zip-0143.rst>`_ .

:fa:`arrow-circle-right` Transaction expiry
    We recommend that you do use the default expiry height (20 blocks/~1 hours) 
    and follow these UX guidelines so that Zcash users can develop a consistent 
    expectation of when Zcash transactions expire and what happens. Zee ZIP 
    `203 <https://github.com/zcash/zips/blob/master/zip-0203.rst>`_ .


This isn't an exhaustive list of the changes. Look at the Overwinter Zcash 
Improvement Proposals (ZIPs) below for complete details on the changes that 
will be made. The five ZIPs cover network handshaking, transaction format, 
transaction expiry, signature hashing, and network upgrade mechanisms.

    - ``ZIP 143`` `Transaction Signature Verification for Overwinter <https://github.com/zcash/zips/blob/master/zip-0143.rst>`_
    - ``ZIP 200`` `Network Upgrade Mechanism <https://github.com/zcash/zips/blob/master/zip-0200.rst>`_
    - ``ZIP 201`` `Network Peer Management for Overwinter <https://github.com/zcash/zips/blob/master/zip-0201.rst>`_
    - ``ZIP 202`` `Version 3 Transaction Format for Overwinter <https://github.com/zcash/zips/blob/master/zip-0202.rst>`_
    - ``ZIP 203`` `Transaction Expiry <https://github.com/zcash/zips/blob/master/zip-0203.rst>`_

The network upgrade is coordinated via an on-chain activation mechanism.

Zcashd v1.1.0 (and future releases) running protocol version ``170005`` will 
activate Overwinter at block 347500 at which point only v3 transactions 
are processed. Older versions of Zcashd <= 1.0.14, running protocol 
versions <= 170004, will partition themselves away from the main network 
into a legacy chain.

Wipeout protection is provided by the new transaction format and signature 
hashing scheme. Blocks from the legacy chain will not be accepted by the 
upgraded network. That is, the upgraded network is permanent, and
Zcashd v1.1.0 (and future releases) can not reorganize back to the 
older non-upgraded chain.


Common Issues
+++++++++++++

tx-overwinter-active
    This error is simply saying that Overwinter has been activated and 
    your client must be upgraded to the latest version. Upgrade your 
    client and try again. If the issue persists try restarting the 
    client. If this error is appearing on a third party app like a 
    mobile wallet, please file a support request with the developer 
    of the product and let us know in the 
    `#user-support <https://discord.gg/8t4zXje>`_ 
    channel on the community chat - https://discord.gg/PhJY6Pm

mandatory-script-verify-flag-failed
    (Script evaluated without error but finished with a false/empty top stack element)
    
    This error has been most commonly seen when using `sendrawtransaction`. 
    This can be caused by a few things.

        1. When creating raw transactions, the `signrawtransaction` step must be 
        completed correctly. There is a field in `signrawtransaction` called `prevtxs` 
        which can be seen here (https://zcash-rpc.github.io/signrawtransaction.html). 
        The `prevtxs` parameter is optional, but if it is specified, the `amount` 
        parameter must also be specified. This amount is the total amount of the 
        previous output. Prior to Overwinter the `amount` parameter was not required, 
        this is a change between Overwinter and the previous version.

        2. This issue can also arise in an edge case where a user is signing the 
        transaction from an offline node. If this is the case the offline node must 
        be synced to above the Overwinter activation height, block ``347500``.

Node sync is stuck before Overwinter activation height
    This bug occurs when you are starting a fresh node or restarting a node that 
    is not synced to above the Overwinter activation height (block 347500) and 
    causes the node to sync very slowly. The bug has to do with your node incorrectly 
    banning peer nodes. The end result is your node will sync very slowly as 
    it will not be able to maintain as many connections to other nodes as usual. 

    This issue has been fixed in 2.0.0. Please `update your client <https://z.cash/download.html>`_  to 2.0.0 or above.
