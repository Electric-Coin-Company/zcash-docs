.. _payment_api:

Zcash Payment API
=================

Overview
--------

Zcash extends the Bitcoin Core API with new RPC calls to support private Zcash payments.

.. important::
 
   Zcash payments make use of **two** address formats:

   | ``taddr`` - address for transparent funds (just like a Bitcoin address, value stored in UTXOs)
   | ``zaddr`` - address for private funds (value stored in objects called notes)

   When transferring funds from one taddr to another taddr, you can use either the existing Bitcoin RPC calls or the new Zcash RPC calls.

   When a transfer involves zaddrs, you must use the Zcash RPC calls.


Compatibility with Bitcoin Core :fa:`bitcoin`
---------------------------------------------

Zcash supports all commands in the Bitcoin Core API (as of version ``0.11.2``).   Where applicable, Zcash will extend commands in a backwards-compatible way to enable additional functionality.

We do not recommend use of accounts which are now deprecated in Bitcoin Core.  Where the account parameter exists in the API, please use ``""`` as its value, otherwise an error will be returned.

To support multiple users in a single node’s wallet, consider using ``getnewaddress`` or ``z_getnewaddress`` to obtain a new address for each user.  Also consider mapping multiple addresses to each user.

List of Zcash API commands
--------------------------

.. note:: Optional parameters are denoted in ``[square brackets]``.


RPC Calls by Category
+++++++++++++++++++++

:fa:`university` Accounting_
    
z_getbalance_ , z_gettotalbalance_

:fa:`address-book` Addresses_

z_getnewaddress_ , z_listaddresses_ , z_validateaddress_ , z_exportviewingkey_ , z_importviewingkey_

:fa:`key` Key_Management_

z_exportkey_ , z_importkey_ , z_exportwallet_ , z_importwallet_

:fa:`calculator` Operations_

z_getoperationresult_ , z_getoperationstatus_ , z_listoperationids_

:fa:`barcode` Payment_

z_listreceivedbyaddress_ , z_listunspent_ , z_sendmany_ , z_shieldcoinbase_

.. admonition:: RPC Parameter Conventions

   .. list-table:: 

      * - **Parameter**
        - **Definition**
      * - taddr
        - *Transparent address*
      * - zaddr
        - *Private address*
      * - address
        - *Accepts both private and transparent addresses.*
      * - amount
        - *JSON format double-precision number with 1 ZC expressed as 1.00000000.*
      * - memo
        - | *Metadata expressed in hexadecimal format.  Limited to 512 bytes, the* 
          | *current size of the memo field of a private transaction.  Zero padding* 
          | *is automatic.*

.. _Accounting:

Accounting
~~~~~~~~~~

+----------------------+---------------------+-----------------------------------------------------------------------------------+
|**Command**           | **Parameters**      | **Description**                                                                   |
+----------------------+---------------------+-----------------------------------------------------------------------------------+
|.. _z_getbalance:     | | address           | | Returns the balance of a taddr or zaddr belonging to the node’s                 |
|                      | | [minconf=1]       | | wallet. Optionally set the minimum number of confirmations a                    |
|z_getbalance          |                     | | transaction must have in order to be included in the balance.                   |
|                      |                     | | Use 0 to unconfirmed transactions.                                              |
|                      |                     +-----------------------------------------------------------------------------------+ 
|                      |                     |``./zcash-cli z_getbalance ztKNzxa8uZ1f...``                                       |
|                      |                     |                                                                                   |
|                      |                     |.. code-block:: javascript                                                         |
|                      |                     |                                                                                   |
|                      |                     |   0.00000000                                                                      |
|                      |                     |                                                                                   |
+----------------------+---------------------+-----------------------------------------------------------------------------------+
|.. _z_gettotalbalance:| [minconf=1]         | | Return the total value of funds stored in the node’s wallet.                    |
|                      |                     | | Optionally set the minimum number of confirmations a private                    |
|z_gettotalbalance     |                     | | or transparent transaction must have in order to be included                    |
|                      |                     | | in the balance. Use 0 to count unconfirmed transactions.                        |
|                      |                     |                                                                                   |
|                      |                     +-----------------------------------------------------------------------------------+ 
|                      |                     |``./zcash-cli z_gettotalbalance``                                                  |
|                      |                     |                                                                                   |
|                      |                     |.. code-block:: javascript                                                         |
|                      |                     |                                                                                   |
|                      |                     |   {                                                                               |
|                      |                     |        "transparent": "0.00",                                                     |
|                      |                     |        "private": "0.00",                                                         |
|                      |                     |        "total": "0.00"                                                            |
|                      |                     |   }                                                                               |
|                      |                     |                                                                                   |
+----------------------+---------------------+-----------------------------------------------------------------------------------+

.. _Addresses:

Addresses
~~~~~~~~~

+----------------------+---------------------+-----------------------------------------------------------------------------------+
|**Command**           | **Parameters**      | **Description**                                                                   |
+----------------------+---------------------+-----------------------------------------------------------------------------------+
|.. _z_getnewaddress:  |                     | | Return a new zaddr for sending and receiving payments. The                      | 
|                      |                     | | spending key for this zaddr will be added to the node’s wallet.                 |
|z_getnewaddress       |                     +-----------------------------------------------------------------------------------+
|                      |                     |``./zcash-cli z_getnewaddress``                                                    |
|                      |                     |                                                                                   |
|                      |                     |.. code-block:: javascript                                                         |
|                      |                     |                                                                                   |
|                      |                     |   zcU1Cd6zYyZCd2VJF8yKgmzjxdiiU1rgTTjEwoN1CGUWCziPkU                              |
|                      |                     |   TXUjXmX7TMqdMNsTfuiGN1jQoVN4kGxUR4sAPN4XZ7pxb                                   |                                                           
|                      |                     |                                                                                   |
+----------------------+---------------------+-----------------------------------------------------------------------------------+
|.. _z_listaddresses:  |                     | | Returns a list of all the zaddrs in this node’s wallet for                      |
|                      |                     | | which you have a spending key.                                                  |
|z_listaddresses       |                     |                                                                                   |
|                      |                     +-----------------------------------------------------------------------------------+
|                      |                     |``./zcash-cli z_listaddresses``                                                    |
|                      |                     |                                                                                   |
|                      |                     |.. code-block:: javascript                                                         |
|                      |                     |                                                                                   |
|                      |                     |   [                                                                               |
|                      |                     |      "zcU1Cd6zYyZCd2VJ...",                                                       |
|                      |                     |      "zcddV3rosTRpWqNj..."                                                        |                                                           
|                      |                     |   ]                                                                               |
+----------------------+---------------------+-----------------------------------------------------------------------------------+
|.. _z_validateaddress:| zaddr               | Return information about a given zaddr                                            |
|                      |                     |                                                                                   |
|z_validateaddress     |                     +-----------------------------------------------------------------------------------+
|                      |                     |``./zcash-cli z_validateaddress zcbcb6XnP8hbV5y6Z...``                             |
|                      |                     |                                                                                   |
|                      |                     |.. code-block:: javascript                                                         |
|                      |                     |                                                                                   |
|                      |                     |   {                                                                               |
|                      |                     |      "isvalid": true,                                                             |
|                      |                     |      "address": "zcbcb6XnP8hbV5y6ZwsY...",                                        |
|                      |                     |      "payingkey": "b4ae837...",                                                   |
|                      |                     |      "ismine": true                                                               |
|                      |                     |   }                                                                               |
+----------------------+---------------------+-----------------------------------------------------------------------------------+

.. _Key_Management:

Key Management
~~~~~~~~~~~~~~

+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|**Command**            | **Parameters**         | **Description**                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_exportkey:       | zaddr                  | | Requires an unlocked wallet or an unencrypted wallet.                           |
|                       |                        | | Return a zkey for a given zaddr belonging to the node’s                         |
|z_exportkey            |                        | | wallet.  The key will be returned as a string formatted                         |
|                       |                        | | using Base58Check as described in the Zcash protocol spec.                      |
|                       |                        |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_exportkey zcbcb6XnP8hbV5y6Z...``                                   |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   AKWUAkypwQjhZ6LLNa...                                                           |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_importkey:       | | zkey                 | | Wallet must be unlocked. Add a zkey as returned by                              |
|                       | | [rescan=             | | z_exportkey to a node's wallet. The key should be                               |
|z_importkey            | | whenkeyisnew]        | | formatted using Base58Check as described in the Zcash                           |
|                       | | [startHeight=0]      | | protocol spec. Rescan can be "yes", "no" or the default                         |
|                       |                        | | "whenkeyisnew" to rescan for transactions affecting any                         |
|                       |                        | | address or pubkey script in the wallet (including transactions                  |
|                       |                        | | affecting the newly-added address for this spending key).                       |
|                       |                        | | The startHeight parameter sets the block height to start                        |
|                       |                        | | the rescan from (default is 0).                                                 |
|                       |                        |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_importkey AKWUAkypwQjhZ6LLNa...``                                  |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   <No output will appear if successful>                                           |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_exportwallet:    | filename               | | Requires an unlocked wallet or an unencrypted wallet.                           |
|                       |                        | | Creates or overwrites a file with taddr private keys                            |
|z_exportwallet         |                        | | and zaddr private keys in a human-readable format.                              |
|                       |                        | | Filename is the file in which the wallet dump will be                           |
|                       |                        | | placed. May be prefaced by an absolute file path. An                            |
|                       |                        | | existing file with that name will be overwritten. No                            |
|                       |                        | | value is returned but a JSON-RPC error will be reported                         |
|                       |                        | | if a failure occurred.                                                          |
|                       |                        | .. note::                                                                         |
|                       |                        |    | Please ensure you have specified the                                         |
|                       |                        |    | directory to export to in zcash.conf                                         |
|                       |                        |                                                                                   |
|                       |                        |    .. code-block:: javascript                                                     |
|                       |                        |                                                                                   |
|                       |                        |       exportdir=/home/user1/zcash                                                 |
|                       |                        |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_exportwallet wfile``                                               |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   <No output will appear if successful>                                           |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_importwallet:    | filename               | | Requires an unlocked wallet or an unencrypted wallet.                           |
|                       |                        | | Imports private keys from a file in wallet export file                          |
|z_importwallet         |                        | | format (see z_exportwallet). These keys will be added                           |
|                       |                        | | to the keys currently in the wallet. This call may need                         |
|                       |                        | | to rescan all or parts of the block chain for transactions                      |
|                       |                        | | affecting the newly-added keys, which may take several                          |
|                       |                        | | minutes. Filename is the file to import. The path is                            |
|                       |                        | | relative to zcashd’s working directory. No value is                             |
|                       |                        | | returned but a JSON-RPC error will be reported if a                             |
|                       |                        | | failure occurred.                                                               |
|                       |                        |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_importwallet /home/user1/zcash/wfile``                             |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   <No output will appear if successful>                                           |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_exportviewingkey:| zaddr                  | | Reveals the viewing key corresponding to 'zaddr'. Then                          |
|                       |                        | | the z_importviewingkey can be used with this output.                            |
|z_exportviewingkey     |                        |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_exportviewingkey ztKNzxa8uZ...``                                   |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   ZiVtJjUXq5...                                                                   |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+
|.. _z_importviewingkey:| | vkey                 | | Adds a viewing key (as returned by ``z_exportviewingkey``)                      |
|                       | | [rescan=             | | to your wallet.                                                                 |
|z_importviewingkey     | | whenkeyisnew]        |                                                                                   |
|                       | | [startHeight=0]      |                                                                                   |
|                       |                        +-----------------------------------------------------------------------------------+
|                       |                        |``./zcash-cli z_importviewingkey ZiVtJjUXq5...``                                   |
|                       |                        |                                                                                   |
|                       |                        |.. code-block:: javascript                                                         |
|                       |                        |                                                                                   |
|                       |                        |   <No output will appear if successful>                                           |
|                       |                        |                                                                                   |
+-----------------------+------------------------+-----------------------------------------------------------------------------------+

.. _Payment:

Payment
~~~~~~~

+----------------------------+--------------------------+-----------------------------------------------------------------------------------+
|**Command**                 | **Parameters**           | **Description**                                                                   |
+----------------------------+--------------------------+-----------------------------------------------------------------------------------+
|.. _z_listreceivedbyaddress:|| zaddr                   | | Return a list of amounts received by a zaddr belonging to                       |
|                            || [minconf=1]             | | the node’s wallet. Optionally set the minimum                                   |
|z_listreceivedbyaddress     |                          | | number of confirmations which a received amount must have                       |
|                            |                          | | in order to be included in the result.  Use 0 to count                          |
|                            |                          | | unconfirmed transactions.                                                       |
|                            |                          |                                                                                   |
|                            |                          +-----------------------------------------------------------------------------------+
|                            |                          |``./zcash-cli z_listreceivedbyaddress ztKNzxa8uZ...``                              |
|                            |                          |                                                                                   |
|                            |                          |.. code-block:: javascript                                                         |
|                            |                          |                                                                                   |
|                            |                          |   [                                                                               |
|                            |                          |    {                                                                              |
|                            |                          |     "txid": "34d19c681...",                                                       |
|                            |                          |     "amount": 1.00000000,                                                         |
|                            |                          |     "memo": "5468616e...",                                                        |
|                            |                          |     "jsindex": 0,                                                                 |
|                            |                          |     "jsoutindex": 1                                                               |
|                            |                          |    }                                                                              |
|                            |                          |   ]                                                                               |
|                            |                          |                                                                                   |
+----------------------------+--------------------------+-----------------------------------------------------------------------------------+
|.. _z_listunspent:          || [minconf=1]             | | Returns array of unspent shielded notes with between minconf                    |
|                            || [maxconf=9999999]       | | and maxconf (inclusive) confirmations. Optionally filter to                     |
|z_listunspent               || [includeWatchonly=      | | only include notes sent to specified addresses. When minconf                    |
|                            || false]                  | | is 0, unspent notes with zero confirmations are returned                        |
|                            || [zaddrs]                | | even though they are not immediately spendable.                                 |
|                            |                          |                                                                                   |
|                            |                          +-----------------------------------------------------------------------------------+
|                            |                          |``./zcash-cli z_listunspent``                                                      |
|                            |                          |                                                                                   |
|                            |                          |.. code-block:: javascript                                                         |
|                            |                          |                                                                                   |
|                            |                          |   [                                                                               |
|                            |                          |    {                                                                              |
|                            |                          |     "txid": "34d19c681b9a0672...",                                                |
|                            |                          |     "jsindex": 0,                                                                 |
|                            |                          |     "jsoutindex": 1,                                                              |
|                            |                          |     "confirmations": 4,                                                           |
|                            |                          |     "spendable": true,                                                            |
|                            |                          |     "address": "ztKNzxa8uZ1fL...",                                                |
|                            |                          |     "amount": 1.00000000,                                                         |
|                            |                          |     "memo": "5468616e6b73206..."                                                  |
|                            |                          |    }                                                                              |
|                            |                          |   ]                                                                               |
|                            |                          |                                                                                   |
+----------------------------+--------------------------+-----------------------------------------------------------------------------------+
|.. _z_sendmany:             || fromaddress             | | This is an Asynchronous RPC call. Send funds from an                            |
|                            || toadress                | | address to multiple outputs. The address can be a                               |
|z_sendmany                  || amount                  | | taddr or a zaddr. Amounts is a list containing key/value                        |
|                            || [minconf=1]             | | pairs corresponding to the addresses and amount to pay.                         |
|                            || [fee=0.0001]            | | Each output address can be in taddr or zaddr format.                            |
|                            |                          | | When sending to a zaddr, you also have the option of                            |
|                            |                          | | of attaching a memo in hexadecimal format.                                      |
|                            |                          |                                                                                   |
|                            |                          | | When sending coinbase funds to a zaddr, the                                     |
|                            |                          | | node's wallet does not allow any change. Put another way,                       |
|                            |                          | | spending a partial amount of a coinbase utxo is not allowed.                    | 
|                            |                          | | This is not a consensus rule but a local wallet rule due to                     |
|                            |                          | | the current implementation of z_sendmany. In future, this                       |
|                            |                          | | may be removed.                                                                 |
|                            |                          |                                                                                   |
|                            |                          +-----------------------------------------------------------------------------------+
|                            |                          || ``./zcash-cli z_sendmany ztKNzxa8u...``                                          | 
|                            |                          || ``'[{"address": "ztWcr4...", "amount": 0.001},``                                 |
|                            |                          || ``{"address": "ztXGs...", "amount": 0.002}]'``                                   |
|                            |                          |                                                                                   |
|                            |                          |.. code-block:: javascript                                                         |
|                            |                          |                                                                                   |
|                            |                          |   opid-58a078dc-a5d8-48de-bf8b-3d1...                                             |                                                                                   
|                            |                          |                                                                                   |  
|                            |                          || Optionally set the minimum number of confirmations which a                       |
|                            |                          || private or transparent transaction must have in order to be                      |
|                            |                          || used as an input. When sending from a zaddr, minconf must                        | 
|                            |                          || must be greater than zero. Optionally set a transaction fee,                     |
|                            |                          || which by default is 0.0001 ZEC. Any transparent change will                      |
|                            |                          || be sent to a new transparent address. Any private change will                    |
|                            |                          || be sent back to the zaddr being used as the source of funds                      |
|                            |                          || Returns an operationid.  You use the operationid value with                      |
|                            |                          || z_getoperationstatus and z_getoperationresult to obtain the                      |
|                            |                          || result of sending funds, which if successful, will be a txid.                    |
|                            |                          |                                                                                   |
+----------------------------+--------------------------+-----------------------------------------------------------------------------------+
|.. _z_shieldcoinbase:       | | fromaddress            | | This is an Asynchronous RPC call. Shield transparent coinbase                   |
|                            | | toaddress              | | funds by sending to a shielded z address. Utxos selected for                    |
|z_shieldcoinbase            | | [fee=0.0001]           | | shielding will be locked. If there is an error, they are                        |
|                            | | [limit=50]             | | unlocked. The RPC call ``listlockunspent`` can be used                          |
|                            |                          | | to return a list of locked utxos. The number of coinbase utxos                  |
|                            |                          | | selected for shielding can be set with the limit parameter,                     |
|                            |                          | | which has a default value of 50. If the parameter is set to 0,                  |
|                            |                          | | the number of utxos selected is limited by the                                  |
|                            |                          | | `-mempooltxinputlimit` option. Any limit is constrained by a                    |
|                            |                          | | consensus rule defining a maximum transaction size of 10000                     |
|                            |                          | | bytes. The from address is a taddr or "*" for all taddrs                        |
|                            |                          | | belonging to the wallet. The to address is a zaddr. The                         |
|                            |                          | | default fee is 0.0001. Returns an object containing an                          |
|                            |                          | | operationid which can be used with z_getoperationstatus                         |
|                            |                          | | and z_getoperationresult, along with key-value pairs                            |
|                            |                          | | regarding how many utxos are being shielded in this                             |
|                            |                          | | transaction and what remains to be shielded.                                    |
|                            |                          |                                                                                   |
|                            |                          +-----------------------------------------------------------------------------------+
|                            |                          |``./zcash-cli z_shieldcoinbase tmFViN6... ztKNzx...``                              |
|                            |                          |                                                                                   |
|                            |                          |.. code-block:: javascript                                                         |
|                            |                          |                                                                                   |
|                            |                          |   {                                                                               |
|                            |                          |    "remainingUTXOs": 0,                                                           |       
|                            |                          |    "remainingValue": 0.00000000,                                                  |
|                            |                          |    "shieldingUTXOs": 1,                                                           |
|                            |                          |    "shieldingValue": 10.00000000,                                                 |
|                            |                          |    "opid": "opid-d6573e4e-4c44-4d3f-b351-d719ed..."                               |
|                            |                          |   }                                                                               |
|                            |                          |                                                                                   |
+----------------------------+--------------------------+-----------------------------------------------------------------------------------+



.. _Operations:

Operations
~~~~~~~~~~

Asynchronous calls return an OperationStatus object which is a JSON object with the following defined key-value pairs:


+-------------------------+--------------------------------------------------------------------------------------------------------+
|**Item**                 |   **Description**                                                                                      |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| operationid             | | Unique identifier for the async operation.  Use this value with ``z_getoperationstatus`` or          |
|                         | | ``z_getoperationresult`` to poll and query the operation and obtain its result.                      |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| status                  | | Current status of operation:                                                                         |
|                         | |                                                                                                      |
|                         | | **queued :** operation is pending execution                                                          |
|                         | | **executing :** operation is currently being executed                                                |
|                         | | **cancelled:** operation is cancelled                                                                |
|                         | | **failed :** operation has failed                                                                    |
|                         | | **success :** operation has succeeded                                                                |
|                         |                                                                                                        |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| result                  | | Result object if the status is *‘success’*.  The exact form of the result object is                  |
|                         | | dependent on the call itself.                                                                        |
+-------------------------+--------------------------------------------------------------------------------------------------------+
| error                   | | Error object if the status is *‘failed’*. The error object has the following key-value pairs:        |
|                         | |                                                                                                      |
|                         | | **code :** number                                                                                    |
|                         | | **message:** error message                                                                           |
+-------------------------+--------------------------------------------------------------------------------------------------------+

.. important::
   Depending on the type of asynchronous call, there may be other key-value pairs.  For example, a ``z_sendmany``
   operation will also include the following in an OperationStatus object:
   
    | **method** : name of operation ( e.g. ``z_sendmany``)
    | **params** : an object containing the parameters to ``z_sendmany``

Currently, as soon as you retrieve the operation status for an operation which has finished, that is it has either succeeded, failed, or been cancelled, the operation and any associated information is removed.

It is currently not possible to cancel operations.

+-------------------------+---------------------+------------------------------------------------------------------------------------+
|**Command**              | **Parameters**      | **Description**                                                                    |
+-------------------------+---------------------+------------------------------------------------------------------------------------+
|.. _z_getoperationresult:| [operationids]      | | Return OperationStatus JSON objects for all completed                            |
|                         |                     | | operations the node is currently aware of, and then                              |
|z_getoperationresult     |                     | | remove the operation from memory. Operationids                                   |
|                         |                     | | is an optional array to filter which operations you want                         |
|                         |                     | | to receive status objects for. Output is a list of                               |
|                         |                     | | operation status objects, where the status is either                             |
|                         |                     | | "failed", "cancelled" or "success".                                              |
|                         |                     |                                                                                    |
|                         |                     +------------------------------------------------------------------------------------+
|                         |                     |``./zcash-cli z_getoperationresult``                                                |
|                         |                     |                                                                                    |
|                         |                     |.. code-block:: javascript                                                          |
|                         |                     |                                                                                    |
|                         |                     |   [                                                                                |
|                         |                     |    {                                                                               |
|                         |                     |     "id": "opid-58a078dc-a5d8-48de-bf8b-3d1f71...",                                |
|                         |                     |     "status": "success",                                                           |
|                         |                     |     "creation_time": 1527886498,                                                   |
|                         |                     |     "result": {                                                                    |
|                         |                     |       "txid": "9f8d61d9454e0ef2b7ac525a55eefa2..."                                 |
|                         |                     |     },                                                                             |
|                         |                     |     "execution_secs": 141.212681193,                                               |
|                         |                     |     "method": "z_sendmany",                                                        |
|                         |                     |     "params": {                                                                    |
|                         |                     |       "fromaddress": "ztKNzxa8uZ1fLvwMLNikk2J...",                                 |
|                         |                     |       "amounts": [                                                                 |
|                         |                     |         {                                                                          |
|                         |                     |           "address": "ztWcr45gw32s1j6...",                                         |
|                         |                     |           "amount": 0.001                                                          |
|                         |                     |         },                                                                         |
|                         |                     |         {                                                                          |
|                         |                     |           "address": "ztXGsmLQ1sS8SMd5ZDBB...",                                    |
|                         |                     |           "amount": 0.002                                                          |
|                         |                     |         }                                                                          |
|                         |                     |       ],                                                                           |
|                         |                     |       "minconf": 1,                                                                |
|                         |                     |       "fee": 0.0001                                                                |
|                         |                     |    }                                                                               |
|                         |                     |   }                                                                                |
|                         |                     |  ]                                                                                 |
+-------------------------+---------------------+------------------------------------------------------------------------------------+
|.. _z_getoperationstatus:| [operationids]      | | Return OperationStatus JSON objects for all operations                           |
|                         |                     | | the node is currently aware of. Operationids is an optional                      |
|z_getoperationstatus     |                     | | array to filter which operations you want to receive status                      |
|                         |                     | | objects for. Output is a list of operation status objects.                       |                                                                    
|                         |                     |                                                                                    |
|                         |                     +------------------------------------------------------------------------------------+
|                         |                     |``./zcash-cli z_getoperationstatus``                                                |
|                         |                     |                                                                                    |
|                         |                     |.. code-block:: javascript                                                          |
|                         |                     |                                                                                    |
|                         |                     |   [                                                                                |
|                         |                     |    {                                                                               |
|                         |                     |     "id": "opid-58a078dc-a5d8-48de-bf8b-3d1f71...",                                |
|                         |                     |     "status": "success",                                                           |
|                         |                     |     "creation_time": 1527886498,                                                   |
|                         |                     |     "result": {                                                                    |
|                         |                     |       "txid": "9f8d61d9454e0ef2b7ac525a55eefa2..."                                 |
|                         |                     |     },                                                                             |
|                         |                     |     "execution_secs": 141.212681193,                                               |
|                         |                     |     "method": "z_sendmany",                                                        |
|                         |                     |     "params": {                                                                    |
|                         |                     |       "fromaddress": "ztKNzxa8uZ1fLvwMLNikk2J...",                                 |
|                         |                     |       "amounts": [                                                                 |
|                         |                     |         {                                                                          |
|                         |                     |           "address": "ztWcr45gw32s1j6...",                                         |
|                         |                     |           "amount": 0.001                                                          |
|                         |                     |         },                                                                         |
|                         |                     |         {                                                                          |
|                         |                     |           "address": "ztXGsmLQ1sS8SMd5ZDBB...",                                    |
|                         |                     |           "amount": 0.002                                                          |
|                         |                     |         }                                                                          |
|                         |                     |       ],                                                                           |
|                         |                     |       "minconf": 1,                                                                |
|                         |                     |       "fee": 0.0001                                                                |
|                         |                     |    }                                                                               |
|                         |                     |   }                                                                                |
|                         |                     |  ]                                                                                 |
+-------------------------+---------------------+------------------------------------------------------------------------------------+
|.. _z_listoperationids:  | [state]             || Return a list of operationids for all operations which                            |
|                         |                     || the node is currently aware of. State is an optional                              |
|z_listoperationids       |                     || string parameter to filter the operations you want                                |
|                         |                     || listed by their state.  Acceptable parameter values                               |
|                         |                     || values are ‘queued’, ‘executing’, ‘success’, ‘failed’,                            |
|                         |                     |                                                                                    |
|                         |                     +------------------------------------------------------------------------------------+
|                         |                     |``./zcash-cli z_listoperationids``                                                  |
|                         |                     |                                                                                    |
|                         |                     |.. code-block:: javascript                                                          |
|                         |                     |                                                                                    |
|                         |                     |   [                                                                                |                                        
|                         |                     |    "opid-58a078dc-a5d8-48de-bf8b-3d1f71...",                                       |
|                         |                     |    "opid-59a078dc-a5d8-48de-bf8b-3d1f71...",                                       |
|                         |                     |    "opid-58a078dc-a5d8-48de-bf8b-3d1f71..."                                        |
|                         |                     |   ]                                                                                |
|                         |                     |                                                                                    | 
+-------------------------+---------------------+------------------------------------------------------------------------------------+

Asynchronous RPC Call Error Codes
---------------------------------

Zcash error codes are defined in :fa:`github` `rpcprotocol.h <https://github.com/zcash/zcash/blob/master/src/rpcprotocol.h>`_

.. list-table:: z_sendmany
   :widths: 10 40

   * - **Value**
     - **Meaning**
   * - ``-8``
     - RPC_INVALID_PARAMETER_ 
   * - ``-5``
     - RPC_INVALID_ADDRESS_OR_KEY_
   * - ``-4``
     - RPC_WALLET_ERROR_ 
   * - ``-6``
     - RPC_WALLET_INSUFFICIENT_FUNDS_  
   * - ``-16`` 
     - RPC_WALLET_ENCRYPTION_FAILED_ 
   * - ``-12`` 
     - RPC_WALLET_KEYPOOL_RAN_OUT_ 

RPC_INVALID_PARAMETER
+++++++++++++++++++++

.. list-table::

   * - ``RPC_INVALID_PARAMETER``
     - **Invalid, missing or duplicate parameter**
   * - Minconf cannot be zero when sending from zaddr
     - | *Cannot accept minimum confirmation value of* 
       | *zero when sending from zaddr*
   * - Minconf cannot be negative
     - | Cannot accept negative minimum confirmation
       | number.
   * - | Minimum number of confirmations cannot be less
       | than 0
     - | Cannot accept negative minimum confirmation
       | number.
   * - From address parameter missing
     - Missing an address to send funds from.
   * - No recipients
     - Missing recipient addresses.
   * - Memo must be in hexadecimal format
     - | Encrypted memo field data must be in hexadecimal 
       | format.
   * - Memo size of __ is too big, maximum allowed is __ 
     - | Encrypted memo field data exceeds maximum size  
       | of 512 bytes.
   * - | From address does not belong to this node, zaddr 
       | spending key not found.
     - Sender address spending key not found.
   * - Invalid parameter, expected object 
     - Expected object.
   * - Invalid parameter, unknown key: __
     - Unknown key. 
   * - Invalid parameter, expected valid size
     - Invalid size.
   * - Invalid parameter, expected hex txid
     - Invalid txid.
   * - Invalid parameter, vout must be positive
     - Invalid vout.
   * - Invalid parameter, duplicated address
     - Address is duplicated.
   * - Invalid parameter, amounts array is empty
     - Amounts array is empty.
   * - Invalid parameter, unknown key
     - Key not found.
   * - Invalid parameter, unknown address format
     - Unknown address format.
   * - Invalid parameter, size of memo
     - Invalid memo field size.
   * - Invalid parameter, amount must be positive
     - Invalid or negative amount.
   * - Invalid parameter, too many zaddr outputs
     - z_address outputs exceed maximum allowed.
   * - | Invalid parameter, expected memo data in  
       | hexadecimal format
     - Encrypted memo field is not in hexadecimal format.
   * - | Invalid parameter, size of memo is larger than 
       | maximum allowed __ 
     - | Encrypted memo field data exceeds maximum size 
       | of 512 bytes.


RPC_INVALID_ADDRESS_OR_KEY
++++++++++++++++++++++++++

.. list-table::

  * - ``RPC_INVALID_ADDRESS_OR_KEY``
    - **Invalid address or key**
  * - Invalid from address, no spending key found for zaddr
    - z_address spending key not found.
  * - Invalid output address, not a valid taddr.
    - Transparent output address is invalid.
  * - Invalid from address, should be a taddr or zaddr. 
    - Sender address is invalid.
  * - | From address does not belong to this node, zaddr 
      | spending key not found.
    - Sender address spending key not found.


RPC_WALLET_INSUFFICIENT_FUNDS
+++++++++++++++++++++++++++++ 

.. list-table::

  * - ``RPC_WALLET_INSUFFICIENT_FUNDS``
    - **Not enough funds in wallet or account**
  * - | Insufficient funds, no UTXOs found for taddr from 
      | address.
    - Insufficient funds for sending address.
  * - | Could not find any non-coinbase UTXOs to spend. 
      | Coinbase UTXOs can only be sent to a single zaddr 
      | recipient.
    - Must send Coinbase UTXO to a single z_address.
  * - Could not find any non-coinbase UTXOs to spend.
    - No available non-coinbase UTXOs.
  * - | Insufficient funds, no unspent notes found for zaddr
      | from address.
    - Insufficient funds for sending address. 
  * - | Insufficient transparent funds, have __, need __ 
      | plus fee __
    - Insufficient funds from transparent address.
  * - | Insufficient protected funds, have __, need __ 
      | plus fee __ 
    - Insufficient funds from shielded address.

RPC_WALLET_ERROR
++++++++++++++++

.. list-table::

  * - ``RPC_WALLET_ERROR``
    - **Unspecified problem with wallet**
  * - Could not find previous JoinSplit anchor
    - Try restarting node with `-reindex`.
  * - | Error decrypting output note of previous 
      | JoinSplit: __
    - 
  * - Could not find witness for note commitment
    - Try restarting node with `-rescan`.
  * - Witness for note commitment is null
    - Missing witness for note commitment.
  * - | Witness for spendable note does not have same 
      | anchor as change input
    - Invalid anchor for spendable note witness.
  * - Not enough funds to pay miners fee
    - Retry with sufficient funds.
  * - Missing hex data for raw transaction
    -  Raw transaction data is null.
  * - Missing hex data for signed transaction
    - Hex value for signed transaction is null.
  * - | Send raw transaction did not return an error 
      | or a txid.
    - 

RPC_WALLET_ENCRYPTION_FAILED
++++++++++++++++++++++++++++

.. list-table::

  * - ``RPC_WALLET_ENCRYPTION_FAILED``
    - **Failed to encrypt the wallet**
  * - Failed to sign transaction     
    - | Transaction was not signed, sign transaction 
      | and retry.

RPC_WALLET_KEYPOOL_RAN_OUT
++++++++++++++++++++++++++

.. list-table::

  * - ``RPC_WALLET_KEYPOOL_RAN_OUT``
    - **Keypool ran out, call keypoolrefill first**
  * - | Could not generate a taddr to use as a change 
      | address
    - Call keypoolrefill and retry.
