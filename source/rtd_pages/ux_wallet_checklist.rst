:orphan:
.. _ux_wallet_checklist:

Zcash Feature UX Checklist
=============================

If you’re building a wallet that supports Zcash, we encourage that you follow these guidelines.

Addresses
+++++++++

Use an address persistently for each use
    Use an address like how you would use different bank accounts (spending, saving, 
    business spending). Transparent addresses aren’t private, so we 
    urge users to keep this in mind. We discourage using a new transparent address for each 
    transaction; this only provides a `false sense of privacy <https://blog.z.cash/transaction-linkability/>`_ .
    Shielded addresses maintain the privacy of transactions, there is no added benefit of using a 
    new shielded address per transaction.

Indicate that transparent addresses are not encrypted! 
    A transaction involving a transparent address (either as sender or recipient) posts the details of 
    the transparent address and amount publicly on the blockchain.

Indicate that shielded addresses are encrypted! 
    A shielded transaction, where funds are sent from one shielded address to another shielded address, 
    only reveals a transaction legitimately and safely happened. The sender, receiver, and amount 
    are not revealed on the blockchain.

If there is no zaddr support, state so clearly 
    Most wallets throw an error stating, “invalid address” or “invalid input.” We suggest instead saying, 
    “shielded address are not supported.” to indicate that shielded addresses are still valid addresses.

Provide taddr and zaddr support if possible 
    Shielded addresses provide privacy via encryption and is Zcash’s main feature. However, most mobile 
    and desktop wallets don’t support sending to shielded addresses, so some users will likely be unable 
    to send ZEC to a shielded address.

Warn users when sending from zaddrs to taddrs (deshielding transactions)
    Explicitly tell users that they are about to reveal transaction information. We don’t think warnings 
    other types of transactions are necessary.

Show an available balance vs owned balance
    Show two balances, one which includes unconfirmed finds, and another not including unconfirmed funds, 
    i.e. “Balance: 621.14321 ZEC (605.35620 ZEC spendable).”


Transactions
++++++++++++

Clearly state the fee structure
    The default transaction fee is set at 0.0001 ZEC. We encourage that you use the default fee, 
    so that transparent and shielded transactions have the same fee--that way, privacy doesn’t cost 
    more for users!

Disable users from setting their own transaction fees 
    Do not allow users to customize fees. Our network is fast enough that mining incentivization is 
    not an issue. Unique transaction fees can cause linkability within transactions, especially for zaddrs.

Do not differentiate between types of transactions
    We do not currently distinguish between different types of Zcash transactions: transparent 
    (transparent to transparent), shielding (transparent to shielded), deshielding (shielded to 
    transparent), and shielded (shielded to shielded) transactions. This is complicated by the 
    ability to send to/from a combination of shielded and transparent addresses.

Use the default transaction expiry time 
    Transaction expiry (see ZIP `here <https://github.com/zcash/zips/blob/master/zip-0203.rst>`_) is set 
    to 20 blocks by default, which is ~1 hour. Use this default global runtime option so Zcash users can 
    develop a consistent expectation of when Zcash transactions expire. We don’t support expiry time as 
    a per-transaction runtime option.

Visibly mark newly sent transactions in a "pending" state 
    We suggest having a “pending transactions” or “unconfirmed transactions” section, but you can also 
    distinguish it in the list of chronological transactions by using a color or an icon.

Tell the user the expected remaining time to expiry
    Users should be able to see how much time/blocks are remaining until their transaction expires. 
    Once confirmed (10+ confirmations), unmark the sent transaction visibly in a “complete” state.

If expired, visibly mark the transaction expired and notify the user
    Rather than deleting the attempted transaction, keep the expired transaction in the log,
    but distinguished as such. We also encourage giving users suggestions on 
    `troubleshooting their transaction <https://z.cash/support/faq.html#transaction-not-mined>`_ .

Viewing Keys
++++++++++++

Use viewing keys for watch only wallets
    Share a `viewing key <https://blog.z.cash/viewing-keys-selective-disclosure/>`_ with yourself to create a 
    wallet that tracks your funds while keeping your main funds offline. Watch-only wallets are the first 
    application of viewing keys; we exploring additional use cases as well.

Secure communication channel
    Encourage secure communication channels by supporting one; viewing keys should not be copy and 
    pasted into a text or email.

Indicate that viewing keys are for all incoming transactions: 
    At version 1.0.14, a viewing key allows the holder of the key to see all incoming transactions 
    since the zaddr was created, but not outgoing transactions.

Memo Fields
+++++++++++

Show the memo field in the UI
    Even if the `memo field <https://blog.z.cash/encrypted-memo-field/>`_ is empty, show that 
    the field is empty rather than removing it from the UI. This is a good nudge to remind users 
    that a memo field exists.

Liberal Use 
    The memo field is always present and is always exactly 512 bytes long; this is necessary for 
    privacy so that an observer can’t detect the different usage patterns and memos. This means 
    that the cost is baked in so that you don’t pay a higher fee for including a memo, so 
    encourage users to use the memo.