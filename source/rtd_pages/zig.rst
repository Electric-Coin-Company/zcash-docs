:orphan:

.. _zig:

Zcash Integration Guide
=======================

Zcash is based on Bitcoin, and has a superset of functionality, both in the protocol and the RPC interface. This document describes Zcash integration into services and products. For help building and testing Zcash, see the :ref:`user_guide`.

Address Types
-------------

Zcash transparent addresses (aka t-addrs), begin with a “t” prefix and are very similar to Bitcoin addresses.

Zcash shielded addresses (z-addrs) which begin with a “z” prefix, are used for sending and receiving shielded funds, with transactions cryptographically protected with zero-knowledge proofs. The `Sapling network upgrade <https://z.cash/upgrade/sapling/>`_ added an improved type of shielded addresses which are much more efficient and user friendly. The new Sapling addresses begin with “zs” whereas the legacy, Sprout addresses begin with “zc”. 

For more information, see the guide to :ref:`zcash_addresses`.


Bitcoin API
------------

The zcash daemon, `zcashd`, presents the same kind of RPC interface as Bitcoin Core, and this interface (see `Bitcoin RPC reference <https://bitcoin.org/en/developer-reference#remote-procedure-calls-rpcs>`_) provides a very similar set of `Bitcoin API calls <https://bitcoin.org/en/developer-reference#rpc-quick-reference>`_, which we call the `Bitcoin API`. Transactions which only involve transparent addresses can be created with this API just as for Bitcoin.

This API can be used for advanced Bitcoin transactions, just as in Bitcoin Core, such as those involving multisig addresses. Multisig addresses begin with "t3" whereas standard transparent addresses begin with "t1".


Zcash Payment API
-----------------

In addition, `zcashd` adds the `Payment API` (see :ref:`payment_api` reference). This is a high-level API that simplifies the common use cases of transfers. This API can send from or to both z-addrs and t-addrs through the ``z_sendmany`` call.

Example of using curl to make a ``z_sendmany`` call::
  
  curl --user "$USER:$PASSWORD" \
    -X POST \
    --data-binary "{ \"jsonrpc\": \"1.0\", \"id\":\"curltest\", \"method\": \"z_sendmany\", \"params\": [\"$FROM_ADDR\", [{\"address\": \"$TO_ADDR\" ,\"amount\": $AMOUNT}]] }" \
    -H "Content-Type: text/plain;" \
    http://127.0.0.1:8232

This API does not yet support advanced Bitcoin transaction types, such as those involving multisig addresses.


Integration Path
----------------

There are two approaches to integrating a service or product with Zcash: the `Bitcoin-compatible` approach, and the `Zcash API` approach. The Bitcoin-compatible approach is convenient for deployments that already use Bitcoin Core, because the API is (almost) identical. Alternatively, if new integrations are being developed, using the Zcash API may be simpler for most use-cases.

Services that use the Zcash API can send to and receive from both z-addrs and t-addrs. One current drawback is that this API does not support multisig transactions. Services that use the Bitcoin-compatibility approach can only send or receive to/from t-addrs which do not provide the privacy features Zcash is known for.

A service that supports both z-addrs and multisig will use the Zcash API for all transactions except multisig, in which case it will use the Bitcoin API.

======= =========== ============ =========== ============ ===========
  Designation         Features to Support
------------------- -------------------------------------------------
 Level  Description Transparent  Transparent Private      Encrypted
                    Transactions Multisig    Transactions Memo
======= =========== ============ =========== ============ ===========
1       Bitcoin-    Bitcoin API  Bitcoin API ..           ..
        compatible
2       Zcash API   Zcash        Bitcoin API Zcash        Zcash
                    Payment API              Payment API  Payment API
======= =========== ============ =========== ============ ===========

Bitcoin API (JSON-RPC)
----------------------

- Backwards compatible with Bitcoin-Core 0.11.2 with minor modifications to JSON output.
- Recommended for: time to market for existing Bitcoin applications, familiarity with Bitcoin and multi-sig.


Zcash Payment API
-----------------

- For sending both transparent and private payments. Extends the existing Bitcoin API with new commands.
- Recommended for: new applications looking to add private transactions and encrypted memo field support which do not need multisig.

Contact Us
----------

For assistance with integrating Zcash into your product, send us a message at ecosystem@z.cash.

Resources
---------

:fa:`arrow-circle-right` :ref:`user_guide`

:fa:`arrow-circle-right` :ref:`payment_api`

:fa:`arrow-circle-right` `Bitcoin RPC reference <https://bitcoin.org/en/developer-reference#remote-procedure-calls-rpcs>`_ and `Bitcoin API calls <https://bitcoin.org/en/developer-reference#rpc-quick-reference>`_

:fa:`arrow-circle-right` `Zcash benchmarking site <https://speed.z.cash/>`_
