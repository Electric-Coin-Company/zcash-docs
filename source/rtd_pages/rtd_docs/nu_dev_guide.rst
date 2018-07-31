.. _nu_dev_guide:

Network Upgrade Developer Guide
===============================

Overwinter
----------

Overwinter is the first network upgrade for Zcash. Its purpose is strengthening 
the protocol for future network upgrades. It includes versioning, replay 
protection for network upgrades, performance improvements for transparent 
transactions, a new feature of transaction expiry, and more.

Overwinter activated successfully at block ``347500``

Common Issues
+++++++++++++

tx-overwinter-active
    This error is simply saying that Overwinter has been activated and 
    your client must be upgraded to the latest version. Upgrade your 
    client and try again. If the issue persists try restarting the 
    client. If this error is appearing on a third party app like a 
    mobile wallet, please file a support request with the developer 
    of the product and let us know in the 
    `#user-support <https://chat.zcashcommunity.com/channel/user-support>`_ 
    channel on the community chat - https://chat.zcashcommunity.com/

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
    causes the node to sync very slowly. We are aware of this bug and have 
    written a fix but it will not be live until the 2.0.0 release which is 
    scheduled for mid-August. The bug has to do with your node incorrectly 
    banning peer nodes. The end result is your node will sync very slowly as 
    it will not be able to maintain as many connections to other nodes as usual. 
    The command `clearbanned` will temporarily fix the issue by removing all 
    banned peers from your banned list, however they will be re-added slowly. 
    Occasionally running the `clearbanned` command could speed up the syncing process.
