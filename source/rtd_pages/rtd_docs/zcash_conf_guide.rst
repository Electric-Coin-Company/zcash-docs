.. _zcash_conf_guide:

Zcash.conf Guide
================

Below contains information for additional configuration of the ``zcash.conf`` file.

Network-Related Settings
------------------------

+-------------------------+----------------------------------------------------------------------------------------------------------+
|**Parameter**            | **Description & Example**                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| testnet                 | Run on the test network instead of the real zcash network.                                               |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    testnet=0                                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| regtest                 | Run a regression test network                                                                            |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    regtest=0                                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| proxy                   | Connect via a SOCKS5 proxy                                                                               |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    proxy=127.0.0.1:9050                                                                                  |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| bind                    |  Bind to given address and always listen on it. Use [host]:port notation for IPv6                        |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    bind=<addr>                                                                                           |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| whitebind               | | Bind to given address and whitelist peers connecting to it. Use [host]:port                            |
|                         | | notation for IPv6                                                                                      |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    whitebind=<addr>                                                                                      |
+-------------------------+----------------------------------------------------------------------------------------------------------+

.. admonition:: Quick Primer on addnode vs connect

   Let's say for instance you use ``addnode=4.2.2.4`` addnode will connect you to and tell you about the
   nodes connected to 4.2.2.4. In addition it will tell the other nodes connected to it that you 
   exist so they can connect to you. Connect will not do the above when you 'connect' to it. 
   It will *only* connect you to 4.2.2.4 and no one else. So if you're behind a firewall, or 
   have other problems finding nodes, add some using 'addnode'. If you want to stay private, 
   use 'connect' to only connect to "trusted" nodes. If you run multiple nodes on a LAN, 
   there's no need for all of them to open lots of connections.  Instead 'connect' them all 
   to one node that is port forwarded and has lots of connections.

   Thanks goes to [Noodle] on Freenode.


+-------------------------+----------------------------------------------------------------------------------------------------------+
|**Parameter**            | **Description & Example**                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| addnode                 | Use as many addnode= settings as you like to connect to specific peers                                   |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    addnode=69.164.218.197                                                                                |
|                         |    addnode=10.0.0.2:8233                                                                                 |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| connect                 | | Alternatively use as many connect= settings as you like to connect                                     |
|                         | | ONLY to specific peers                                                                                 |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    connect=69.164.218.197                                                                                |
|                         |    connect=10.0.0.1:8233                                                                                 |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| listen                  | Listening mode, enabled by default except when 'connect' is being used                                   |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    listen=1                                                                                              |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| maxconnections          | Maximum number of inbound+outbound connections.                                                          |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    maxconnections=6                                                                                      |
+-------------------------+----------------------------------------------------------------------------------------------------------+

JSON-RPC Options
----------------

Controlling a running Zcash/zcashd process

+-------------------------+----------------------------------------------------------------------------------------------------------+
|**Parameter**            | **Description & Example**                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| addnode                 | Use as many addnode= settings as you like to connect to specific peers                                   |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    addnode=69.164.218.197                                                                                |
|                         |    addnode=10.0.0.2:8233                                                                                 |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| server                  | Tells zcashd to accept JSON-RPC commands (set as default if not specified)                               |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    server=1                                                                                              |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcbind                 | | Bind to given address to listen for JSON-RPC connections. Use [host]:port                              |
|                         | | notation for IPv6. This option can be specified multiple times                                         |
|                         | | (default: bind to all interfaces)                                                                      |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcbind=<addr>                                                                                        |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcuser                 | You must set rpcuser and rpcpassword to secure the JSON-RPC api                                          |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcuser=Ulysses                                                                                       |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcpassword             | You must set rpcuser and rpcpassword to secure the JSON-RPC api                                          |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcpassword=YourSuperGreatPasswordNumber_DO_NOT_USE_THIS                                              |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcclienttimeout        | | How many seconds zcash will wait for a complete RPC HTTP request.                                      |
|                         | | after the HTTP connection is established.                                                              |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcclienttimeout=30                                                                                   |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcallowip              | | By default, only RPC connections from localhost are allowed.                                           |
|                         | | Specify as many rpcallowip= settings as you like to allow                                              |
|                         | | connections from other hosts, either as a single IPv4/IPv6                                             |
|                         | | or with a subnet specification.                                                                        |
|                         |                                                                                                          |
|                         | .. note::                                                                                                |
|                         |                                                                                                          |
|                         |    | Opening up the RPC port to hosts outside your local trusted network                                 |
|                         |    | is NOT RECOMMENDED, because the rpcpassword is transmitted over the                                 |
|                         |    | network unencrypted and also because anyone that can authenticate on                                |
|                         |    | the RPC port can steal your keys + take over the account running zcashd                             |
|                         |    | For more information see https://github.com/zcash/zcash/issues/1497                                 |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcallowip=10.1.1.34/255.255.255.0                                                                    |
|                         |    rpcallowip=1.2.3.4/24                                                                                 |
|                         |    rpcallowip=2001:db8:85a3:0:0:8a2e:370:7334/96                                                         |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcport                 | Listen for RPC connections on this TCP port:                                                             |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcport=83232                                                                                         |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| rpcconnect              | | You can use Zcash or zcashd to send commands to Zcash/zcashd                                           |
|                         | | running on another host using this option:                                                             |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    rpcconnect=127.0.0.1                                                                                  |
+-------------------------+----------------------------------------------------------------------------------------------------------+

Transaction Fee
---------------

+-------------------------+----------------------------------------------------------------------------------------------------------+
|**Parameter**            | **Description & Example**                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| sendfreetransactions    | Send transactions as zero-fee transactions if possible (default: 0)                                      |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    sendfreetransactions=0                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| txconfirmtarget         | | Create transactions that have enough fees (or priority) so they are                                    |
|                         | | likely to # begin confirmation within n blocks (default: 1). This                                      |
|                         | | setting is overridden by the -paytxfee option.                                                         |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    txconfirmtarget=n                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------+

Miscellaneous Options
---------------------


+-------------------------+----------------------------------------------------------------------------------------------------------+
|**Parameter**            | **Description & Example**                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| gen                     | Enable attempt to mine zcash.                                                                            |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    gen=0                                                                                                 |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| genproclimit            | Set the number of threads to be used for mining zcash (-1 = all cores).                                  |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    genproclimit=1                                                                                        |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| equihashsolver          | | Specify a different Equihash solver (e.g. "tromp") to try to mine zcash                                |
|                         | | faster when gen=1.                                                                                     |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    equihashsolver=default                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| keypool                 | | Pre-generate this many public/private key pairs, so wallet backups will be valid for                   |
|                         | | both prior transactions and several dozen future transactions.                                         |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    keypool=100                                                                                           |
+-------------------------+----------------------------------------------------------------------------------------------------------+
| paytxfee                | | Pay an optional transaction fee every time you send zcash.  Transactions with fees                     |
|                         | | are more likely than free transactions to be included in generated blocks, so may                      |
|                         | | be validated sooner. This setting does not affect private transactions created with                    |
|                         | | ``z_sendmany``                                                                                         |
|                         |                                                                                                          |
|                         | .. code-block:: bash                                                                                     |
|                         |                                                                                                          |
|                         |    paytxfee=0.00                                                                                         |
+-------------------------+----------------------------------------------------------------------------------------------------------+