.. _testnet_guide:

Testnet Guide
=============

The Zcash testnet is an alternative blockchain that attempts to mimic the main Zcash network for testing purposes. Testnet coins are distinct from actual ZEC and do not have value. Developers and users can experiment with the testnet without having to use valuable currency. The testnet is also used to test network upgrades and their activation before committing to the upgrade on the main Zcash network.

Joining
-------

In order to use the testnet, you must:

:fa:`arrow-circle-right` Follow the :ref:`user_guide` to install a Zcash node
    
:fa:`arrow-circle-right` Set the :ref:`ugConfiguration` for your node to sync with testnet (and optionally mine testnet coins)

Using
-----

:fa:`arrow-circle-right` Obtain testnet coins (TAZ)
    You can use the `testnet faucet <https://faucet.testnet.z.cash/>`_ or enable mining in your configuration to obtain TAZ
    
:fa:`arrow-circle-right` Creating transactions
    Use the :ref:`payment_api` to create transactions on testnet

:fa:`arrow-circle-right` Testnet explorers
    You can use the `Zcash testnet explorer <https://explorer.testnet.z.cash/>`_ or other, third-party testnet explorers including `testnet.zcha.in <https://testnet.zcha.in/>`_.
    
    .. note::

       See the :ref:`nu_dev_guide` for details on testing network upgrades.
