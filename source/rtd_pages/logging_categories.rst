.. _Logging Categories:

Logging Categories
====================

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Category
     - Description
   * - ``addrman``
     - Logging related to tracking network peer addresses in memory before caching to `peers.dat`.
   * - ``alert``
     - Logging related to Version Upgrades (status bar)
   * - ``bench``
     - Logging related to benchmarking.
   * - ``coindb``
     - Logging related to the storage of transaction outputs.
   * - ``db``
     - Logging related to storage of wallet data (data that is relevant to the spend authority and/or viewing keys that the wallet is using to track transactions).
   * - ``estimatefee``
     - Logging related to Fee Calculations
   * - ``http``
     - Logging related to HTTP requests & HTTP work queuing.
   * - ``libevent``
     - Logging related to HTTP event threading.
   * - ``mempool``
     - Logging related to in-memory ephemeral storage for incoming transactions.
   * - ``net``
     - Logging related to network data incoming and outgoing.
   * - ``paymentdisclosure``
     - Logging related to `disclosing the details of a shielded payment <https://garethtdavies.medium.com/an-introduction-to-payment-disclosure-in-zcash-96748c209d49>`_.
   * - ``pow``
     - Logging related to the Equihash Proof-of-Work algorithm.
   * - ``proxy``
     - Logging related to SOCKS5 proxy authentication.
   * - ``prune``
     - Logging related to removing block/rev files in order to remain under target space goal.
   * - ``receiveunsafe``
     - Logging related to accessing unencrypted notes.
   * - ``reindex``
     - Logging related to the process of rebuilding wallet state by replaying and re-evaluating the blockchain data from a specific height forward.
   * - ``rpc``
     - Logging related to maintaining the HTTP RPC service.
   * - ``selectcoins``
     - Logging related to the automatic `selection of coins <https://murch.one/wp-content/uploads/2016/11/erhardt2016coinselection.pdf>`_ to be spent that is produced during transaction construction by the wallet.
   * - ``tor``
     - Logging related to communication with a locally running Tor process.
   * - ``zmq``
     - Logging related to ZeroMQ inter-process notifications.
   * - ``zrpc``
     - Logging related to transaction building & async operations.
   * - ``zrpcunsafe (implies zrpc)``
     - Same as ``zrpc`` utilizes a separate log category as the information logged is private and more care should be taken not to leak it.
