:orphan:

.. _tor:

Tor Support in Zcash
====================
It is possible to run Zcash as a Tor hidden service and connect to such services. *Warning: Tor support does not explicitly support Zcash nor Zcash explicitly support Tor.*

The following directions assume you have a Tor proxy running on port 9050. Many distributions default to having a SOCKS proxy listening on port 9050, but others may not. In particular, the Tor Browser Bundle defaults to listening on port 9150. See `Tor Project FAQ:TBBSocksPort <https://www.torproject.org/docs/faq.html.en#TBBSocksPort>`_ for how to properly configure Tor.


1. Run Zcash through Tor
------------------------

Running Zcash through Tor will make all outgoing connections be anonymized on the network and will suffice for most situations. This is actually quite easy to do! 

Download and run Tor Browser. This will automatically run a SOCKS proxy on 127.0.0.1:9150 (with default configuration settings). While Tor Browser (and its proxy) is running, connect zcashd to it with: 

	.. code-block:: bash
		
		$ zcashd -proxy=127.0.0.1:9050

Zcashd flags used:

	* ``-proxy=ip:port``: sets the proxy server. If SOCKS5 is selected (default), this server will be used to reach .onion addresses as well.

2. Run a Zcash hidden server
----------------------------

It is possible to make a zcashd node reachable from the Tor network. 

Add lines to your /etc/tor/torrc (or equivalent config file) that configures the ports on the Tor side. The directory can be different but the port numbers should be equal to the zcashd P2P listen port (8233 by default). An example is below.

	.. code-block:: bash

		$ HiddenServiceDir /var/lib/tor/zcash-service/
		$ HiddenServicePort 8233 127.0.0.1:8233
		$ HiddenServicePort 18233 127.0.0.1:18233

After that, configure the zcashd node to use the proxy, specific onion service, and turn on the listening feature should suffice. Try: 

	.. code-block:: bash

		$ zcashd -proxy=127.0.0.1:9050 -externalip=zctestseie6wxgio.onion -listen

Zcashd flags used: 

	* ``-proxy=ip:port``: sets the proxy server. If SOCKS5 is selected (default), this server will be used to reach .onion addresses as well.
	* ``-externalip=X``: Tells Zcash about its publicly reachable address, which can be a, ip or .onion address. Onion addresses are given preference for advertising and connections. 
	* ``-listen``: Enable listening for incoming connections with this flag; listening is off by default.


3. Automatically listen on Tor
--------------------------------

Starting with Tor version 0.2.7.1 it is possible, through Tor's control socket API, to create and destroy 'ephemeral' hidden services programmatically. Zcash has been updated to make use of this.

If Tor is running (and proper authentication has been configured), Zcash automatically creates a hidden service to listen on. Zcash will also use Tor automatically to connect to other .onion nodes if the control socket can be successfully opened.

This new feature is enabled by default if Zcash is listening (``-listen``) and requires a Tor connection to work. It can be explicitly disabled with ``-listenonion=0`` and, if not disabled, configured using the ``-torcontrol`` and ``-torpassword`` settings. To show verbose debugging information, pass ``-debug=tor``.

Connecting to Tor's control socket API requires one of two authentication methods to be configured: 

	1.  Cookie authentication, which requires write access to the ``CookieAuthFile`` specified in Tor configuration. In some cases, this is preconfigured and the creation of a hidden service is automatic. If permission problems are seen with ``-debug=tor`` they can be resolved by adding both the user running tor and  the user running zcashd to the same group and setting permissions appropriately. On Debian-based systems the user running zcashd can be added to the debian-tor group, which has the appropriate permissions. 
	2. Authentication with the ``-torpassword`` flag and a ``hash-password``, which can be enabled and specified in Tor configuration.


4. Connect to a Zcash hidden server
-----------------------------------

To test your setup, try connecting via Tor on a different computer to a single Zcash hidden server. Launch zcashd as follows:

.. code-block:: bash
		
	$ zcashd -onion=127.0.0.1:9050 -connect=zctestseie6wxgio.onion

Now use zcash-cli to verify there is only a single peer connection.

.. code-block:: bash
		
	$ zcash-cli getpeerinfo

.. code-block:: javascript
		
	[
	    {
	        "id" : 1,
	        "addr" : "zctestseie6wxgio.onion:18233",
	        ...
	        "version" : 170002,
	        "subver" : "/MagicBean:1.0.0/",
	        ...
	    }
	]

To connect to multiple Tor nodes, use:

.. code-block:: bash
		
	$ zcashd -onion=127.0.0.1:9050 -addnode=zctestseie6wxgio.onion -dnsseed=0 -onlynet=onion
