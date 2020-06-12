# Sending Memos with Zcash-cli

This document explains how to send and receive encrypted Zcash transaction memos using `zcash-cli` (the RPC interface). The not-so-user-friendly aspect of the RPC interface is that the memos are in hexadecimal string format. (The various wallets, such as Zecwallet and ZECC wallet, hid this detail from their users.)
So to send as ascii text string as a memo requires first converting the string to hex, and to read the memo later
as a text string requires converting from hex back to a string.

## What is a memo? 

When you receive a Zcash payment from someone else’s shielded address to a shielded address of your own, you see the amount of Zcash received, and you see the transaction ID, which allows you to identify this transaction (in its encrypted form) in the blockchain.

You don’t learn anything about the sender or about the history of the money you’re receiving, and you don’t see the sender’s address. This is by design — the sender should be able to send you money without necessarily revealing other information about themselves.

However, we realized that senders would sometimes need to communicate information about a specific payment. For example an invoice number or account number that the payment is for, an address to which any refunds should be sent, a note to the recipient, etc.

So we implemented an additional field that is visible to the recipient of a payment, called the “encrypted memo field”. It is always present in every encrypted payment, and is always exactly 512 bytes long. If a sender doesn’t specify a memo, then the memo that is sent is all zeroes (before encryption), and if the sender includes a memo shorter than 512 bytes, then the remaining space is padded with zeroes (before encryption).

Learn more about it by reading this [blog post](https://electriccoin.co/blog/encrypted-memo-field/).  

## Tools
The following two tools will be handy.

### `ascii2hex`
Use this small script for constructing the memo when sending:
```
#!/usr/bin/env python3
import sys 
import codecs
for x in sys.argv[1:]:
    print(codecs.encode(bytes(x, 'ascii'), 'hex').decode())
```
Pass it the string you wish to include in the memo:
```
$ ascii2hex 'hello zcash'
68656c6c6f207a63617368
$ 
```
### `hex2ascii`
This small script will convert a hex string to ascii, useful when receiving a transaction:
```
#!/usr/bin/env python3
import sys 
import codecs
for x in sys.argv[1:]:
    print(codecs.decode(x, 'hex').decode())
```

## Sending a transaction with a memo
Each transaction output can have its own memo. Here's an example with one output, and we've copied and
pasted the hex string for "hello zcash" as the memo:
```
zcash-cli z_sendmany ztestsapling13ushwzyrqd8gecatanpk2uvr0th9kly2sqlvdyyyhyp350ara0ldvqjj8xaxuhgmnaaz5keej2p '[{"memo":"68656c6c6f207a63617368","address": "ztestsapling1kg3u0y7szv6509732at34alct46cyn0g26kppgf2a7h5tpqxldtwm7cmhf8rqmhgtmpakcz5mdv","amount":0.01}]'
```
Remember that memos can be up to 512 ascii text characters (1024 hex digits).
This transaction exists on testnet.

## Reading a transaction's memo
There are two APIs that display transaction memos. Receivers of a transaction can use `z_listunspent`:
```
$ zcash-cli z_listunspent
[
  {
    "txid": "4b51581abed41e0c050e9a6dcd007b70d8db3737647c146c159a71124b986231",
    "outindex": 0,
    "confirmations": 15,
    "spendable": true,
    "address": "ztestsapling1kg3u0y7szv6509732at34alct46cyn0g26kppgf2a7h5tpqxldtwm7cmhf8rqmhgtmpakcz5mdv",
    "amount": 0.01000000,
    "memo": "68656c6c6f207a63617368000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "change": false
  }
]
```
Or, either the sender or receiver (but no one else!) may use `z_listreceivedbyaddress`:
```
zcash-cli z_listreceivedbyaddress ztestsapling1kg3u0y7szv6509732at34alct46cyn0g26kppgf2a7h5tpqxldtwm7cmhf8rqmhgtmpakcz5mdv
[
  {
    "txid": "4b51581abed41e0c050e9a6dcd007b70d8db3737647c146c159a71124b986231",
    "amount": 0.01000000,
    "memo": "68656c6c6f207a63617368000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "outindex": 0,
    "confirmations": 15,
    "blockheight": 956859,
    "blockindex": 3,
    "blocktime": 1591907179,
    "change": false
  }
]
$
```
Then the hex string can be converted back to ascii text:
```
$ hex2ascii 68656c6c6f207a63617368
hello zcash
$ 
```