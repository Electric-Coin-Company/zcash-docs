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
        - *JSON format double-precision number with 1 ZEC expressed as 1.00000000.*
      * - memo
        - | *Metadata expressed in hexadecimal format.  Limited to 512 bytes, the*
          | *current size of the memo field of a private transaction.  Zero padding*
          | *is automatic.*

.. _Accounting:

Accounting
~~~~~~~~~~

.. _z_getbalance:

**Command:** ``z_getbalance``

**Parameters**

1. ``"address"``  *(string)* 
    The selected address. It may be a transparent or private address.
2. ``minconf``    *(numeric, optional, default=1)* 
    Only include transactions confirmed at least this many times.

**Output**

  amount *(numeric)* 
    The total amount in ZEC received for this address. 

**Description**

Returns the balance of a taddr or zaddr belonging to the node’s
wallet. Optionally set the minimum number of confirmations a
transaction must have in order to be included in the balance.
Use 0 to unconfirmed transactions.

**Examples**

The total amount received by address "myaddress"

.. code-block:: javascript 
   
   zcash-cli z_getbalance "myaddress"

   0.00000000

----

.. _z_gettotalbalance:   

**Command:** ``z_gettotalbalance``

**Parameters**

1. ``minconf``    *(numeric, optional, default=1)* 
    Only include transactions confirmed at least this many times.

**Output**

  "transparent" *(numeric)* 
    The total balance of transparent funds
  "private" *(numeric)*
    The total balance of private funds
  "total" *(numeric)*
    The total balance of both transparent and private funds

**Description**

Return the total value of funds stored in the node’s wallet.
Optionally set the minimum number of confirmations a private
or transparent transaction must have in order to be included
in the balance. Use 0 to count unconfirmed transactions.

**Examples**

The total amount in the wallet

.. code-block:: javascript

    zcash-cli z_gettotalbalance

    { 
        "transparent": "0.00",
        "private": "0.00",
        "total": "0.00"
    }     

----

.. _Addresses:

Addresses
~~~~~~~~~

.. _z_getnewaddress:

**Command:** ``z_getnewaddress``

**Parameters**

1. ``type``     *(string, optional, default="sprout")*
    The type of address (e.g. "sprout", "sapling").
    
**Output**

  "zcashaddress"    *(string)*
    The new shielded address

**Description**

Return a new zaddr for sending and receiving payments. The
spending key for this zaddr will be added to the node’s wallet.

**Examples**

Create a new shielded address (as of v2.0.2 Sapling is default; v2.0.0 and v2.0.1 Sprout is default )

.. code-block:: javascript

    zcash-cli z_getnewaddress

    zcU1Cd6zYyZCd2VJF8yKgmzjxdiiU1rgTTjEwoN1CGUWCziPkUTXUjXmX7TMqdMNsTfuiGN1jQoVN4kGxUR4sAPN4XZ7pxb

Create a new Sapling shielded address

.. code-block:: javascript

    zcash-cli z_getnewaddress sapling

    zs1z7rejlpsa98s2rrrfkwmaxu53e4ue0ulcrw0h4x5g8jl04tak0d3mm47vdtahatqrlkngh9sly

----    

.. _z_listaddresses:

**Command:** ``z_listaddresses``

**Parameters**

1. ``includeWatchonly``     *(bool, optional, default=false)*
    Also include watchonly addresses (see 'z_importviewingkey')

**Output**

  "zaddr"   *(string)*
  A zaddr belonging to the wallet

**Description**

Returns a list of all the zaddrs in this node’s wallet for
which you have a spending key.

**Examples**

List all the zaddrs in this node's wallet

.. code-block:: javascript

    zcash-cli z_listaddresses

    [
        "zcU1Cd6zYyZCd2VJ...",
        "zcddV3rosTRpWqNj..."
    ]       

----

.. _z_validateaddress:

**Command:** ``z_validateaddress``

**Parameters**

1. ``zaddr``     *(string, required)*
    The z address to validate

**Output**

  "isvalid" : true|false,      *(boolean)* 
    If the address is valid or not. If not, this is the only property returned.
  "address" : "zaddr",         *(string)*
    The z address validated
  "type" : "xxxx",             *(string)* 
    "sprout" or "sapling"
  "ismine" : true|false,       *(boolean)*
    If the address is yours or not
  "payingkey" : "hex",         *(string)*
    [sprout] The hex value of the paying key, a_pk
  "transmissionkey" : "hex",   *(string)* 
    [sprout] The hex value of the transmission key, pk_enc
  "diversifier" : "hex",       *(string)*
    [sapling] The hex value of the diversifier, d
  "diversifiedtransmissionkey" : "hex", *(string)* 
    [sapling] The hex value of pk_d

**Description**

Return information about the given z address.

**Examples**

List all the information about a given zaddr.

.. code-block:: javascript

    zcash-cli z_validateaddress "zcWsmqT4X2V4jgxbgiCzyrAfRT1vi1F4sn7M5Pkh66izzw8Uk7LBGAH3DtcSMJeUb2pi3W4SQF8LMKkU2cUuVP68yAGcomL"

    {
      "isvalid": true,
      "address": "zcbcb6XnP8hbV5y6ZwsY...",
      "payingkey": "b4ae837...",
      "ismine": true
    }   

----

.. _Key_Management:

Key Management
~~~~~~~~~~~~~~

.. _z_exportkey:

**Command:** ``z_exportkey``  

**Parameters**

1. ``zaddr``   *(string, required)* 
    The zaddr for the private key

**Output** 

    "key"      *(string)* 
      The private key

**Description**

Requires an unlocked wallet or an unencrypted wallet.
Return a zkey for a given zaddr belonging to the node’s
wallet. The key will be returned as a string formatted
using Base58Check as described in the Zcash protocol spec.

**Examples**

Export a key for a given zaddr.

.. code-block:: javascript

    ./zcash-cli z_exportkey "zcWsmqT4X2V4jgxbgiCzyrAfRT1vi1F4sn7M5Pkh66izzw8Uk7LBGAH3DtcSMJeUb2pi3W4SQF8LMKkU2cUuVP68yAGcomL"

    AKWUAkypwQjhZ6LLNa

----

.. _z_importkey: 

**Command:** ``z_importkey``

**Parameters**

1. "zkey"             *(string, required)*
    The zkey (see z_exportkey)
2. rescan             *(string, optional, default="whenkeyisnew")*
    Rescan the wallet for transactions - can be "yes", "no" or "whenkeyisnew"
3. startHeight        *(numeric, optional, default=0)* 
    Block height to start rescan from

**Output**

  NONE

**Description**

Wallet must be unlocked. Add a zkey as returned by
z_exportkey to a node's wallet. The key should be
formatted using Base58Check as described in the Zcash
protocol spec. Rescan can be "yes", "no" or the default
"whenkeyisnew" to rescan for transactions affecting any
address or pubkey script in the wallet (including transactions 
affecting the newly-added address for this spending key).
The startHeight parameter sets the block height to start
the rescan from (default is 0).

**Examples** 

Import the zkey with rescan

.. code-block:: javascript

    zcash-cli z_importkey "mykey"

Import the zkey with partial rescan

.. code-block:: javascript

    zcash-cli z_importkey "mykey" whenkeyisnew 30000

Re-import the zkey with longer partial rescan

.. code-block:: javascript

    zcash-cli z_importkey "mykey" whenkeyisnew 30000

----

.. _z_exportwallet:

**Command:** ``z_exportwallet``

**Parameters**

1. "filename"    *(string, required)* 
    The filename, saved in folder set by zcashd -exportdir option

**Output**

  "path"           (string) The full path of the destination file

**Description**

Requires an unlocked wallet or an unencrypted wallet.
Creates or overwrites a file with taddr private keys
and zaddr private keys in a human-readable format.
Filename is the file in which the wallet dump will be
placed. May be prefaced by an absolute file path. An
existing file with that name will be overwritten. No
value is returned but a JSON-RPC error will be reported
if a failure occurred.

As of Sapling activation, the shielded private keys in 
this file will be separated into legacy shielded private 
keys under the title Zkeys and Sapling shielded private 
keys. The export also includes (as of Sapling activation) 
a comment with an HD wallet seed and associated fingerprint, 
both as hex strings. This seed is only for the wallet’s 
Sapling shielded keys and addresses.

**Examples** 

Export a wallet 

.. code-block:: bash

    zcash-cli z_exportwallet "wallet_filename"

    <No output will appear if successful>

----

.. _z_importwallet:

**Command:** ``z_importwallet``

**Parameters**

1. "filename"    *(string, required)* 
    The wallet file

**Output**

  NONE

**Description**

Requires an unlocked wallet or an unencrypted wallet.
Imports private keys from a file in wallet export file 
format (see z_exportwallet). These keys will be added
to the keys currently in the wallet. This call may need
to rescan all or parts of the block chain for transactions
affecting the newly-added keys, which may take several
minutes. Filename is the file to import. The path is
relative to zcashd’s working directory. No value is
returned but a JSON-RPC error will be reported if a
failure occurred. This command does not yet support importing HD 
seeds and will import Sapling addresses in a standard form 
(non-HD). To backup and restore the full wallet inclusive of 
the Sapling HD seed, use the backupwallet command.

**Examples** 

Import a wallet 

.. code-block:: bash

    zcash-cli z_importwallet "path/to/exportdir/nameofbackup"

    <No output will appear if successful>

----

.. _z_exportviewingkey:

**Command:** ``z_exportviewingkey``

**Parameters**

1. "zaddr"   *(string, required)* 
    The zaddr for the viewing key

**Output**

  "vkey"                  (string) The viewing key

**Description**

Reveals the viewing key corresponding to 'zaddr'. Then
the z_importviewingkey can be used with this output.

**Examples** 

Export a viewing key for a given address

.. code-block:: javascript 

    zcash-cli z_exportviewingkey "myaddress"

    ZiVtJjUXq5...

----

.. _z_importviewingkey:

**Command:** ``z_importviewingkey``

**Parameters**

1. "vkey"             *(string, required)* 
    The viewing key (see z_exportviewingkey)
2. rescan             *(string, optional, default="whenkeyisnew")* 
    Rescan the wallet for transactions - can be "yes", "no" or "whenkeyisnew"
3. startHeight        *(numeric, optional, default=0)* 
    Block height to start rescan from

**Output**

  NONE

**Description** 

Adds a viewing key (as returned by z_exportviewingkey) to your wallet.

**Examples**

Import a viewing key 

.. code-block:: javascript

    zcash-cli z_importviewingkey "vkey"

Import the viewing key without rescan

.. code-block:: javascript

    zcash-cli z_importviewingkey "vkey", no

Import the viewing key with partial rescan

.. code-block:: javascript

    zcash-cli z_importviewingkey "vkey" whenkeyisnew 30000

Re-import the viewing key with longer partial rescan

.. code-block:: javascript

    zcash-cli z_importviewingkey "vkey" yes 20000

----

.. _Payment:

Payment
~~~~~~~

.. _z_listreceivedbyaddress:

**Command:** ``z_listreceivedbyaddress``

**Parameters**

1. "address"      *(string)* 
    The private address.
2. minconf        *(numeric, optional, default=1)* 
    Only include transactions confirmed at least this many times.

**Output**
  
  "txid": xxxxx,           *(string)* 
    The transaction id
  "amount": xxxxx,         *(numeric)* 
    The amount of value in the note
  "memo": xxxxx,           *(string)*
    Hexademical string representation of memo field
  "change": true|false,    *(boolean)* 
    True if the address that received the note is also one of the sending addresses

**Description**

Return a list of amounts received by a zaddr belonging to
the node’s wallet. Optionally set the minimum
number of confirmations which a received amount must have
in order to be included in the result.  Use 0 to count
unconfirmed transactions.

**Examples**

Return a list of amounts recieved by a zaddr belonging to the node's wallet.

.. code-block:: javascript

    zcash-cli z_listreceivedbyaddress "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"

----

.. _z_listunspent:  

**Command:** ``z_listunspent``

**Parameters**

  1. minconf         *(numeric, optional, default=1)* 
      The minimum confirmations to filter*
  2. maxconf          *(numeric, optional, default=9999999)* 
      The maximum confirmations to filter
  3. "includeWatchonly" *(bool, optional, default=false)* 
      Also include watchonly addresses (see 'z_importviewingkey')
  4. "addresses"      *(string)*
      A json array of zaddrs to filter on.  Duplicate addresses not allowed.
    
    .. code-block:: javascript

        [
          "address"     (string) zaddr
          ,...
        ]

**Output**

    "txid" : "txid",          *(string)* 
      The transaction id 
    "jsindex" : n             *(numeric)* 
      The joinsplit index
    "jsoutindex" : n          *(numeric)* 
      [sprout] The output index of the joinsplit
    "outindex" : n          *(numeric)* 
      [sapling] The output index
    "confirmations" : n       *(numeric)* 
      The number of confirmations
    "spendable" : true|false  *(boolean)* 
      True if note can be spent by wallet, false if note has zero confirmations, false if address is watchonly
    "address" : "address",    *(string)*
      The shielded address
    "amount": xxxxx,          *(numeric)* 
      The amount of value in the note
    "memo": xxxxx,            *(string)* 
      Hexademical string representation of memo field
    "change": true|false,     *(boolean)* 
      True if the address that received the note is also one of the sending addresses

**Description**

Returns array of unspent shielded notes with between minconf
and maxconf (inclusive) confirmations. Optionally filter to
only include notes sent to specified addresses. When minconf
is 0, unspent notes with zero confirmations are returned
even though they are not immediately spendable

**Examples**

Return an array of unspent shielded notes

.. code-block:: javascript

    zcash-cli z_listunspent

Returns array of unspent shielded notes with between minconf
and maxconf (inclusive) confirmations. Optionally filter to
only include notes sent to specified addresses.

.. code-block:: javascript
    
    zcash-cli z_listunspent 6 9999999 false "[\"ztbx5DLDxa5ZLFTchHhoPNkKs57QzSyib6UqXpEdy76T1aUdFxJt1w9318Z8DJ73XzbnWHKEZP9Yjg712N5kMmP4QzS9iC9\",\"ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf\"]"

----

.. _z_sendmany: 

**Command:** z_sendmany

**Parameters**

  1. "fromaddress"         *(string, required)*
      The taddr or zaddr to send the funds from.
  2. "amounts"             (array, required) An array of json objects representing the amounts to send.
      
        "address":address  (string, required) The address is a taddr or zaddr
        "amount":amount    (numeric, required) The numeric amount in ZEC is the value
        "memo":memo        (string, optional) If the address is a zaddr, raw data represented in hexadecimal string format
  3. minconf               *(numeric, optional, default=1)* 
      Only use funds confirmed at least this many times.
  4. fee                   *(numeric, optional, default=0.0001)* 
      The fee amount to attach to this transaction.

**Output**

    "operationid"          *(string)* 
      An operationid to pass to z_getoperationstatus to get the result of the operation.

**Description**

This is an Asynchronous RPC call. Send funds from an
address to multiple outputs. The address can be a
taddr or a zaddr. Amounts is a list containing key/value
pairs corresponding to the addresses and amount to pay.
Each output address can be in taddr or zaddr format.
When sending to a zaddr, you also have the option of
of attaching a memo in hexadecimal format.

When sending coinbase funds to a zaddr, the
node’s wallet does not allow any change. Put another way,
spending a partial amount of a coinbase utxo is not allowed.
This is not a consensus rule but a local wallet rule due to
the current implementation of z_sendmany. In future, this
may be removed.

Optionally set the minimum number of confirmations which a
private or transparent transaction must have in order to be
used as an input. When sending from a zaddr, minconf must
must be greater than zero. Optionally set a transaction fee,
which by default is 0.0001 ZEC. Any transparent change will
be sent to a new transparent address. Any private change will
be sent back to the zaddr being used as the source of funds
Returns an operationid. You use the operationid value with
z_getoperationstatus and z_getoperationresult to obtain the
result of sending funds, which if successful, will be a txid.

**Examples**

Send funds from a t-address to z-address output

  .. code-block:: javascript

      zcash-cli z_sendmany "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" '[{"address": "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf" ,"amount": 5.0}]'

----

.. _z_shieldcoinbase:

**Command:** ``z_shieldcoinbase``

**Parameters**

  1. "fromaddress"         *(string, required)* 
      The address is a taddr or "*" for all taddrs belonging to the wallet.
  2. "toaddress"           *(string, required)* 
      The address is a zaddr.
  3. fee                   *(numeric, optional, default=0.0001)* 
      The fee amount to attach to this transaction.
  4. limit                 *(numeric, optional, default=50)* 
      Limit on the maximum number of utxos to shield.  
      Set to 0 to use node option -mempooltxinputlimit (before Overwinter), 
      or as many as will fit in the transaction (after Overwinter).

**Output**

  "remainingUTXOs": xxx       *(numeric)* 
    Number of coinbase utxos still available for shielding.
  "remainingValue": xxx       *(numeric)* 
    Value of coinbase utxos still available for shielding.
  "shieldingUTXOs": xxx        *(numeric)* 
    Number of coinbase utxos being shielded.
  "shieldingValue": xxx        *(numeric)* 
    Value of coinbase utxos being shielded.
  "opid": xxx          *(string)* 
    An operationid to pass to z_getoperationstatus to get the result of the operation.

**Description**

This is an Asynchronous RPC call. Shield transparent coinbase
funds by sending to a shielded z address. Utxos selected for
shielding will be locked. If there is an error, they are
unlocked. The RPC call listlockunspent can be used
to return a list of locked utxos. The number of coinbase utxos
selected for shielding can be set with the limit parameter,
which has a default value of 50. If the parameter is set to 0,
the number of utxos selected is limited by the
-mempooltxinputlimit option. Any limit is constrained by a
consensus rule defining a maximum transaction size of 10000
bytes. The from address is a taddr or “*” for all taddrs
belonging to the wallet. The to address is a zaddr. The
default fee is 0.0001. Returns an object containing an
operationid which can be used with z_getoperationstatus
and z_getoperationresult, along with key-value pairs
regarding how many utxos are being shielded in this
transaction and what remains to be shielded.


**Examples**

Shield transparent coinbase funds by sending to a shielded z-address.

  .. code-block:: javascript

      zcash-cli z_shieldcoinbase "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"

----

.. _Operations:

Operations
~~~~~~~~~~

Asynchronous calls return an OperationStatus object which is a JSON object with the following defined key-value pairs:

**Item** operationid

**Description**
  Unique identifier for the async operation.  Use this value with ``z_getoperationstatus`` or
  ``z_getoperationresult`` to poll and query the operation and obtain its result.

**Item**  status 

**Description**

Current status of operation:

  **queued :** operation is pending execution
  **executing :** operation is currently being executed
  **cancelled:** operation is cancelled
  **failed :** operation has failed
  **success :** operation has succeeded 

**Item** result

**Description**
  Result object if the status is *‘success’*.  The exact form of the result object is
  dependent on the call itself.

**Item** error

**Description**
  Error object if the status is *‘failed’*. The error object has the following key-value pairs:

  **code :** number
  **message:** error message  


.. important::
   Depending on the type of asynchronous call, there may be other key-value pairs.  For example, a ``z_sendmany``
   operation will also include the following in an OperationStatus object:

    | **method** : name of operation ( e.g. ``z_sendmany``)
    | **params** : an object containing the parameters to ``z_sendmany``

Currently, as soon as you retrieve the operation status for an operation which has finished, that is it has either succeeded, failed, or been cancelled, the operation and any associated information is removed.

It is currently not possible to cancel operations.


.. _z_getoperationresult:

**Command** ``z_getoperationresult``

**Parameters**

  1. "operationid"         *(array, optional)* 
      A list of operation ids we are interested in.  If not provided, examine all operations known to the node.

**Output**

"    [object, ...]"      (array) A list of JSON objects

 **Description**

Return OperationStatus JSON objects for all completed
operations the node is currently aware of, and then
remove the operation from memory. Operationids
is an optional array to filter which operations you want
to receive status objects for. Output is a list of
operation status objects, where the status is either
“failed”, “cancelled” or “success”.

**Example**

Return OperationStatus JSON objects for all completed operations the node is currently aware of

.. code-block:: javascript

    zcash-cli z_getoperationresult '["operationid", ... ]'

----

.. _z_getoperationstatus:

**Command:** ``z_getoperationstatus``

**Parameters**

  1. "operationid"         *(array, optional)* 
      A list of operation ids we are interested in.  If not provided, examine all operations known to the node.

**Output**

    "    [object, ...]"      *(array)* 
      A list of JSON objects

**Description**

Return OperationStatus JSON objects for all operations
the node is currently aware of. Operationids is an optional
array to filter which operations you want to receive status
objects for. Output is a list of operation status objects.

**Example**

Return OperationStatus JSON objects for all completed operations the node is currently aware of

.. code-block:: javascript

    zcash-cli z_getoperationstatus '["operationid", ... ]'

----

.. _z_listoperationids: 

**Command:** ``z_listoperationids``

**Parameters**

  1. "status"         *(string, optional)* 
      Filter result by the operation's state e.g. "success".

**Output**
 
    "operationid"       *(string)* 
      An operation id belonging to the wallet

**Description**

Return a list of operationids for all operations which
the node is currently aware of. State is an optional
string parameter to filter the operations you want
listed by their state. Acceptable parameter values
values are ‘queued’, ‘executing’, ‘success’, ‘failed’,

**Examples**

Return a list of operationids for all operations which the node is currently aware of

.. code-block:: javascript

    zcash-cli z_listoperationids 


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


.. important:: To view a community maintained list of the API, please click `here <https://zcash-rpc.github.io/>`_ 