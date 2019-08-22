:orphan:

.. _insight_explorer:

Insight Block Explorer Guide
============================

You can run the ``zcashd`` client with additional features enabled that allow it to support
the Insight block explorer.
These features are not enabled by default because they increase the disk space used by the
data directory ``~/.zcash`` and will also reduce performance.
A block-explorer-enabled ``zcashd`` can perform all the functions of a normal ``zcashd``
but typically will not be used as a wallet (will contain no private keys).

There are three areas of change, which are described below:

* Configuration (additional ``~/.zcash/zcash.conf`` lines)
* New fields added to the existing ``getrawtransaction`` RPC
* A set of new RPC (cli) methods

The examples show actual (though in some cases, truncated for simplicity)
testnet results, and can be reproduced on testnet by copying and
pasting the command line (after starting an explorer-enabled ``zcashd``).
Since the blockchain state will have changed since this writing,
the results may no longer be the same as shown here. Also, for brevity, this document
doesn't show some of the example command results, when the purpose is to
illustrate how parameters can be specified.

You can search for the transactions and addresses used in these examples
using an existing testnet block explorer such as https://explorer.testnet.z.cash
so you can see the correspondence between the RPC results and the block
explorer results.

Configuration changes
---------------------

The ``zcashd`` process must be started with the following options, either on the command line or
in the ``zcash.conf`` file (see :ref:`zcash_conf_guide`):

.. code::

  txindex=1
  experimentalfeatures=1
  insightexplorer=1

After enabling these configuration options, it will be necessary to reindex the
database by starting ``zcashd`` one time with the ``--reindex`` command-line option (this will
take some time) and waiting for it to fully sync with the blockchain.
The ``txindex=1`` option causes ``zcashd`` to store all blockchain transactions
locally, which requires more storage.

Additional ``getrawtransaction`` fields
---------------------------------------

If the ``insightexplorer`` configuration option is enabled, the ``getrawtransaction`` RPC
verbose result will include new fields whose values are derived (of course, transactions
themselves include no additional information). None of the existing fields is modified, so these
additions should be backward compatible; existing consumers of the result will continue
to work unchanged, and they will be unaware of the additional fields.

Here is an example result, edited for clarity here by showing **only** the added
fields (this is a real testnet transaction, so you may try this yourself, or search
a block explorer for this transaction and see the correspondence):

.. code-block:: javascript

    $ zcash-cli getrawtransaction 91cbdf382fc7244fab745a2322e336444cb23ba4aec149574dc9b5c77dea7005 1
    {
      [...]
      "vin": [
        {
          [...]
          "value": 654.99971929,
          "valueSat": 65499971929,
          "address": "tmV5PUniaX9NMUfe76kTRWd7B8pAXhkq3Sf"
        }
      ],
      [...]
      "vout": [
        {
          [...]
          "spentTxId": "ed202d138c7103fbd2271d577644f4500c68daaccfb7b008995a06e501256cf7",
          "spentIndex": 0,
          "spentHeight": 458561
        },
        {
          [...]
          "spentTxId": "2c6896af644c29481b1682f3da00d2f218f340293c6c7f009d6f21a19ea7310f",
          "spentIndex": 3,
          "spentHeight": 493577
        }
      ],
      [...]
      "height": 458218
      [...]
    }

(Note that there may be multiple entries in the ``vin`` array; this transaction
happens to have only one.) The ``spent`` fields in a particular ``vout`` array
element will only be populated if a later transaction that (whose ID is shown)
has spent that output.

Additional API commands (RPCs)
------------------------------

.. _getaddressbalance:

**Command:** ``getaddressbalance``

**Parameters**

  1. a JSON object  *(required)*

    "addresses"     *(required)*
      A JSON list of zero or more taddrs

or

  1. A single taddr *(quoted string, required)*

**Output**

  A JSON object

  "balance"     *(numeric)* 
    The total balance in zatoshis of transparent funds held by the given addresses
  "received"    *(numeric)*
    The total amount in zatoshis of transparent funds received by the given addresses

**Description**

This RPC returns the total balance and total amount ever received (even if already spent),
by the given transparent addresses.

**Examples**

.. code-block:: javascript

    $ zcash-cli getaddressbalance '{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ", "tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"]}'
    {
      "balance": 58000347656,
      "received": 77000361504
    }
    $ zcash-cli getaddressbalance '{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"]}'
    $ zcash-cli getaddressbalance '"tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"'

----

.. _getaddressdeltas:

**Command:** ``getaddressdeltas``

**Parameters**

  1. a JSON object *(required)*

    "addresses" *(required)*
      A JSON list of taddrs
    "chainInfo" *(boolean, optional, default=false)*
      Include additional information about the current chain in the results
    "start"     *(numeric, optional, default=0)*
      Restrict results to blocks starting at this height
    "end"       *(numeric, optional, default=9999999)*
      Restrict results to blocks less than or equal to this height

or

  1. A single taddr *(quoted string, required)*

**Output**

  If `chainInfo` is `false`, or `start` or `end` are zero:

  A JSON object with the following key/value pairs:

  "address"     *(string)* 
    The taddr that information is being requested for
  "blockindex"  *(numeric)*
    The zero-based index of the transaction within the block
  "height"      *(numeric)*
    The height of the block in which the transaction was mined
  "index"       *(numeric)*
    The offset within the transaction's ``vin`` or ``vout`` array
  "satoshis"    *(numeric)* 
    The value (zatoshis) transferred to (if positive) or from (if negative) the taddr
  "txid"        *(string)* 
    The transaction ID

  **or (if "chainInfo" is true, and "start" and "end" are nonzero):**

  A JSON object with the following key/value pairs:

  "deltas"      *(JSON object)* (same as above)
    "address"     *(string)* 
      The taddr that information is being requested for
    "blockindex"  *(numeric)*
      The zero-based index of the transaction within the block
    "height"      *(numeric)*
      The height of the block in which the transaction was mined
    "index"       *(numeric)*
      The offset within the transaction's ``vin`` or ``vout`` array
    "satoshis"    *(numeric)* 
      The value (zatoshis) transferred to (if positive) or from (if negative) the taddr
    "txid"        *(string)* 
      The transaction ID
  "start"       *(JSON object)* 
    "hash"        *(hex string)*
      The block hash of the first block in the range
    "height"      *(numeric)*
      The height of the first block in the range
  "end"       *(JSON object)* 
    "hash"        *(hex string)*
      The block hash of the last block in the range
    "height"      *(numeric)*
      The height of the last block in the range

**Description**

This RPC returns a JSON list in which each entry contains information
about a transaction that includes the given transparent address or
addresses as either an input or an output.
You may restrict the output to transactions contained within a specified
range of blocks. Duplicate addresses are ignored.

**Examples**

.. code-block:: javascript

    $ zcash-cli getaddressdeltas '"tmEGycwsvcEhEfR43Dj7w6jYGY6JfqqYsAR"'
    [
      {
        "satoshis": 66399972661,
        "txid": "71a7ea74f071f0cad221b79c17e1455f19e0c4cb292385d564a232b75b2f634b",
        "index": 1,
        "blockindex": 1,
        "height": 457166,
        "address": "tmEGycwsvcEhEfR43Dj7w6jYGY6JfqqYsAR"
      },
      {
        "satoshis": -66399972661,
        "txid": "4b7de59de8f9e2e976f9b11e30382bec417be3dd0a66b3b173dfd07c44efde83",
        "index": 0,
        "blockindex": 1,
        "height": 457703,
        "address": "tmEGycwsvcEhEfR43Dj7w6jYGY6JfqqYsAR"
      }
    ]
    $ zcash-cli getaddressdeltas '{"addresses": ["tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"], "start":492191, "end":492191, "chainInfo":true}'
    {
      "deltas": [
        {
          "satoshis": -1000000000,
          "txid": "77e5f1f6326a5e11d80b87e2b29ab61df5d8c2722cbc1113c0d1710d05538c05",
          "index": 1,
          "blockindex": 1,
          "height": 492191,
          "address": "tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"
        },
        {
          "satoshis": -1000000000,
          "txid": "77e5f1f6326a5e11d80b87e2b29ab61df5d8c2722cbc1113c0d1710d05538c05",
          "index": 2,
          "blockindex": 1,
          "height": 492191,
          "address": "tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"
        },
      ],
      "start": {
        "hash": "001d6eff5fa2c9f0e1024f185ce9f2787143bfe993ba9e14144d8875cbfe4295",
        "height": 492191
      },
      "end": {
        "hash": "001d6eff5fa2c9f0e1024f185ce9f2787143bfe993ba9e14144d8875cbfe4295",
        "height": 492191
      }
    }

----

.. _getaddresstxids:

**Command:** ``getaddresstxids``

**Parameters**

  1. a JSON object *(required)*

    "addresses" *(required)*
      A JSON list of taddr strings
    "start"     *(numeric, optional, default=0)*
      Restrict results to blocks starting at this height
    "end"       *(numeric, optional, default=9999999)*
      Restrict results to blocks less than or equal to this height

or

  1. A single taddr *(quoted string, required)*

**Output**

  A JSON array containing transaction ID strings

**Description**

This RPC returns a list of transactions IDs associated with a given
list of transparent addresses (transactions for which the addresses
are either an input or an output).
You may restrict the output to transactions contained within a specified
range of blocks. Duplicate addresses are ignored.
See getaddressdeltas_ for an extended version of this RPC.

**Examples**

.. code-block:: javascript

    $ zcash-cli getaddresstxids '"tmEGycwsvcEhEfR43Dj7w6jYGY6JfqqYsAR"'
    [
      "71a7ea74f071f0cad221b79c17e1455f19e0c4cb292385d564a232b75b2f634b",
      "4b7de59de8f9e2e976f9b11e30382bec417be3dd0a66b3b173dfd07c44efde83"
    ]
    $ zcash-cli getaddresstxids '{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ", "tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"]}'
    $ zcash-cli getaddresstxids '{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"], "start": 400000, "end": 500000}'

----

.. _getaddressutxos:

**Command:** ``getaddressutxos``

**Parameters**

  1. a JSON object *(required)*

    "addresses" *(required)*
      A JSON list of taddrs
    "chainInfo" *(boolean, optional, default=false)*
      Include additional information about the current chain in the results

**Output**

If ``chainInfo`` is false:

  An array of JSON objects with the following key/value pairs:

  "address"     *(string)* 
    The taddr that information is being requested for
  "txid"        *(hex string)*
    The transaction ID (hash) of the utxo
  "outputIndex" *(numeric)*
    the index into the transaction's ``vout`` array
  "script"      *(hex string)*
    The utxo's locking script
  "height"      *(numeric)*
    The height of the block in which the transaction was mined
  "satoshis"    *(numeric)* 
    The value (zatoshis) that is available to transfer

If ``chainInfo`` is true:

  A JSON object with the following key/value pairs:

  "utxos"   *(array of JSON objects)*
    As described above (same as result when ``chainInfo`` is false)
  "hash"    *(hex string)*
    Current block hash
  "height"  *(numeric)*
    Current block height

**Description**

This RPC returns a list of per-transaction JSON objects for transactions
that include the given addresses an input or an output. If ``chainInfo`` is
given as true, the current, the hash and height of the best blockchain tip
is included in the output.

**Examples**

.. code-block:: javascript

    $ zcash-cli getaddressutxos '"tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"'
    [
      {
        "address": "tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ",
        "txid": "5d9341bd629fb8decb58e562bc07730c5640a7339f2b0b962e820817201c6df3",
        "outputIndex": 0,
        "script": "76a914fa2e24ff03abfa96945275307d7c8cb3bbbf927588ac",
        "satoshis": 1000010000,
        "height": 481688
      },
      {
        "address": "tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ",
        "txid": "15e12955413c777f8f75f27b57ce594e6d3558afa3c7b360d233812b366eff8b",
        "outputIndex": 0,
        "script": "76a914fa2e24ff03abfa96945275307d7c8cb3bbbf927588ac",
        "satoshis": 1000000000,
        "height": 481698
      },
    ]
    $ zcash-cli getaddressutxos '{"addresses": ["tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ"], "chainInfo": true}'
    {
      "utxos": [
        {
          "address": "tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ",
          "txid": "5d9341bd629fb8decb58e562bc07730c5640a7339f2b0b962e820817201c6df3",
          "outputIndex": 0,
          "script": "76a914fa2e24ff03abfa96945275307d7c8cb3bbbf927588ac",
          "satoshis": 1000010000,
          "height": 481688
        },
        {
          "address": "tmYXBYJj1K7vhejSec5osXK2QsGa5MTisUQ",
          "txid": "15e12955413c777f8f75f27b57ce594e6d3558afa3c7b360d233812b366eff8b",
          "outputIndex": 0,
          "script": "76a914fa2e24ff03abfa96945275307d7c8cb3bbbf927588ac",
          "satoshis": 1000000000,
          "height": 481698
        },
      ],
      "hash": "00073cb34978e068e742e27c175688d02da23f341e89373ca68b5e6b5744a847",
      "height": 498989
    }

----

.. _getaddressmempool:

**Command:** ``getaddressmempool``

**Parameters**

  1. a JSON object  *(required)*

    "addresses"     *(required)*
      A JSON list of taddrs

or

  1. A single taddr *(quoted string, required)*

**Output**

  A JSON object with the following key/value pairs:

  "address"     *(string)* 
    The taddr that information is being requested for
  "index"       *(numeric)*
    The offset within the transaction's ``vin`` or ``vout`` array
  "prevout"     *(numeric)*
    Index in the ``vout`` array of the previous (source) transaction
  "prevtxid"    *(string)* 
    The ID of the previous (source) transaction
  "satoshis"    *(numeric)* 
    The value (zatoshis) transferred to (if positive) or from (if negative) the taddr
  "timestamp"   *(string)* 
    The transaction ID
  "txid"        *(string)* 
    The transaction ID

Note that the two keys beginning with ``prev`` are only present if this
entry describes the use of the address as an output (satoshis is less than zero).

**Description**

This RPC returns a JSON list in which each entry contains information
about an unconfirmed (in the mempool) transaction that includes the given
transparent address or addresses as either an input or an output.
Duplicate addresses are ignored.

The ``getaddressdeltas`` RPC returns similar information for confirmed
transactions.

**Examples**

(Note the examples shown here are not reproducible since these
transactions have been mined and are no longer in the mempool.)

.. code-block:: javascript

    $ zcash-cli getaddressmempool '"tmE4gTU1Qf2ViAKPTBNRJt8BTRdwnRtguLo"'
    [
      {
        "address": "tmE4gTU1Qf2ViAKPTBNRJt8BTRdwnRtguLo",
        "txid": "4a27679d4ca1e1f68009a28ae2589c3dac7d3b721533d1199360bfd133102526",
        "index": 0,
        "satoshis": -1000000000,
        "timestamp": 1557867167,
        "prevtxid": "d6267ab2fe5e9a76d252eea8942af70a31df8a3b287001fd6e098dbb3fa8d62f",
        "prevout": 0
      }
    ]
    $ zcash-cli getaddressmempool '{"addresses": ["tmE4gTU1Qf2ViAKPTBNRJt8BTRdwnRtguLo", "tmTzyyT7PDiAfhx7V53kvtbnU1SKCv3niiz"]}'

----

.. _getspentinfo:

**Command:** ``getspentinfo``

**Parameters**

  1. a JSON object with the following keys:

    "txid"       *(string, required)*
      A transaction ID (hash)
    "index"      *(numeric, required)*
      The index in the transaction's ``vout`` array

**Output**

  A JSON object with the following key/value pairs:

  "txid"       *(string)*
    A transaction ID (hash)
  "index"      *(numeric)*
    The index in the transaction's ``vin`` array
  "height"     *(numeric)*
    The height of the block containing the spending transaction

**Description**

Given a transaction output specification (transaction ID and ``vout`` index),
this RPC returns a JSON object specifying the later input
(transaction ID and ``vin`` index) that consumed (spent) this output.
This RPC will fail if the output hasn't yet been spent.

**Examples**

.. code-block:: javascript

    $ zcash-cli getspentinfo '{"txid": "33990288fb116981260be1de10b8c764f997674545ab14f9240f00346333b780", "index": 4}'
    {
      "txid": "b42738de87a3191544fcfca4eed3b326f51b5c1edd2e29920e9846fbeb30ceb9",
      "index": 1,
      "height": 493746
    }

----

.. _getblockhashes:

**Command:** ``getblockhashes``

**Parameters**

  1. high   *(timestamp, required)*

    Return results from blocks mined before this time

  2. low    *(timestamp, required)*

    Return results from blocks mined at or after this time

  3. A JSON object with the following key/value pairs: *(string, optional)*

    "noOrphans"       *(boolean, optional, default=false)*
      Only include blocks on the main chain
    "logicalTimes"    *(boolean, optional, default=false)*
      Include the timestamp of each returned block hash

**Output**

  A JSON array containing block hashes *(strings)*

or, if ``logicalTimes`` is passed as ``true``:

  A JSON array containing objects with the following keys:
  
    "blockhash"      *(string)*
      The hash of a block
    "logicalts"      *(numeric)*
      The time the block was mined

**Description**

This method identifies the blocks that were mined between the given
timestamps (greater or equal to ``low`` and less than ``high``). The
returned entries are sorted by time. If ``noOrphans`` is set to true,
only blocks on the main chain are returned. If ``logicalTimes`` is set
to true, the results include the timestamp of each block.

**Examples**

(Note: The block beginning with ``00127...`` is orphaned on testnet,
so it's omitted from the result of the second example.)

.. code-block:: javascript

    $ zcash-cli getblockhashes 1558141697 1558141576
    [
      "000710e39d80861642829a7f46db665398e4e774f62d0086eeb7e47e22dbb27f",
      "0012749b890523094737cf9b08685e80db0b3f56f4188812264cfaa20317f9e4",
      "000e0a2ca48716b77f00890aeda67f5fd6847ea7e7d8cef5e5c1635d6e0bf778"
    ]
    $ zcash-cli getblockhashes 1558141697 1558141576 '{"noOrphans": true}'
    [
      "000710e39d80861642829a7f46db665398e4e774f62d0086eeb7e47e22dbb27f",
      "000e0a2ca48716b77f00890aeda67f5fd6847ea7e7d8cef5e5c1635d6e0bf778"
    ]
    $ zcash-cli getblockhashes 1558141697 1558141576 '{"noOrphans": false}'
    [
      "000710e39d80861642829a7f46db665398e4e774f62d0086eeb7e47e22dbb27f",
      "0012749b890523094737cf9b08685e80db0b3f56f4188812264cfaa20317f9e4",
      "000e0a2ca48716b77f00890aeda67f5fd6847ea7e7d8cef5e5c1635d6e0bf778"
    ]
    $ zcash-cli getblockhashes 1558141697 1558141576 '{"noOrphans": true, "logicalTimes": true}'
    [
      {
        "blockhash": "000710e39d80861642829a7f46db665398e4e774f62d0086eeb7e47e22dbb27f",
        "logicalts": 1558141585
      },
      {
        "blockhash": "000e0a2ca48716b77f00890aeda67f5fd6847ea7e7d8cef5e5c1635d6e0bf778",
        "logicalts": 1558141600
      }
    ]

----

.. _getblockdeltas:

**Command:** ``getblockdeltas``

**Parameters**

  1. A block hash   *(string, required)*

**Output**

  A JSON object containing information about the block

**Description**

Given a block hash, return information about all inputs and outputs
of all the transactions within the block, and about the block itself
(similar to ``getblock``).

**Examples**

.. code-block:: javascript

    $ zcash-cli getblockdeltas '"00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b"'
    {
      "hash": "00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b",
      "confirmations": 8,
      "size": 1875,
      "height": 497812,
      "version": 4,
      "merkleroot": "3e82b975b005281f6a80c83b0b6378227e25cf5358d4dceddcd9b4616f9c51ba",
      "deltas": [
        {
          "txid": "9fe77b726474cd9b46ec1d0cb23ff11b4a50a97a3af89b8b0fa845d611a9077d",
          "index": 0,
          "inputs": [
          ],
          "outputs": [
            {
              "address": "tmA4rvdJU3HZ4ZUzZSjEUg7wbf1unbDBvGb",
              "satoshis": 1000003848,
              "index": 0
            },
            {
              "address": "t2RpffkzyLRevGM3w9aWdqMX6bd8uuAK3vn",
              "satoshis": 250000000,
              "index": 1
            }
          ]
        },
        {
          "txid": "9dce375054465d5770bbcdbaf1fa6516f23fabfb85f86be460ade0ad177c1731",
          "index": 1,
          "inputs": [
            {
              "address": "tmGygFvgg1B35XeX3oC4e78VSiAyRGcCgME",
              "satoshis": -15083800,
              "index": 0,
              "prevtxid": "2da7f76a2e0a6a6efc22e58d17e58a8d2cef29d119a12d8cb6432f1e4013621a",
              "prevout": 1
            }
          ],
          "outputs": [
            {
              "address": "tmDWk6PT1pE9JbDHqR6an8xJjVj8y8E9xDz",
              "satoshis": 310000,
              "index": 0
            },
            {
              "address": "tmGygFvgg1B35XeX3oC4e78VSiAyRGcCgME",
              "satoshis": 14769952,
              "index": 1
            }
          ]
        }
      ],
      "time": 1558474927,
      "mediantime": 1558474449,
      "nonce": "0000da3417e30c61fa2ce17a1e20e309d7a871e35c4cac1a947f294a91850030",
      "bits": "1f26e516",
      "difficulty": 52.65466254794991,
      "chainwork": "000000000000000000000000000000000000000000000000000000192051a8eb",
      "previousblockhash": "0005e0cb410c2a25dd8de2d3e0b92e2ce485bc24bd05147986007514ada8f9a6",
      "nextblockhash": "001f49bd431d5facbfbce72565d151d74aae7859bab88a8fec966017ab7f30e4"
    }
