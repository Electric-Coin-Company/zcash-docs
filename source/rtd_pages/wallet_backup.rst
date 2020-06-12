:orphan:

.. _wallet_backup:

Wallet Backup Instructions
==========================

Overview 
--------

* Backing up your Zcash private keys is the best way to prevent loss of funds.

* With a backup of your private keys, you (or anyone else) can recover your funds and have access to using them. Because of this, you should store your  backups where they are not susceptible to loss or theft.

* We recommend a backup anytime a new address is generated in the wallet, to ensure all funds are safe. Your existing private keys may not properly back up funds generated in this new address. 

* Note: Sapling shielded addresses (``zs...``) are natively generated from an `HDseed`. Export and import of this seed is not fully supported in the RPC yet. Sapling keys can be exported and imported using the options below but will be treated as standard (non-HD) keys.

Zcashd Backup Instructions
-----------------------------

These instructions are specific for zcashd. For backing up with third-party wallets, please consult with user guides or support channels provided for those services.

1. All methods of backup require an export directory setting in zcash.conf, which is located in the data directory, ``~/.zcash/`` (unless it's been overridden with ``datadir=`` setting). Choose any directory within the home directory as the location for export & backup files. If the directory doesn't exist, it will be created.

2. Add the following line to zcash.conf:  ``exportdir=path/to/chosen/export/directory``. By default, the config file zcashd tries is ``$HOME/.zcash/zcash.conf`` on Debian and Windows, and ``/Users/yourusername/Library/Application\ Support/Zcash/zcash.conf`` on MacOS. 

3. Stop and restart zcashd so that the edits in the config file can take effect. 

4. Back up your wallet! There are multiple ways; pick one follow the instructions: 

	* Backing up a copy of the entire wallet with ``backupwallet``
	* Exporting all private keys for all addresses as a bundle with ``z_exportwallet`` & ``z_importwallet``
	* Exporting a specific private key associated with an address with ``z_exportkey``, ``z_importkey``, ``dumpprivkey`` & ``importprivkey``

	We recommend backing up a copy of the entire wallet, which backs up all the private keys and also useful wallet data. It's also the easiest.  

Zcashd Backup Methods
----------------------

Using ``backupwallet``
++++++++++++++++++++++

	To create a backup of your entire wallet and corresponding data, use:

	``zcash-cli backupwallet <nameofbackup>``

	The backup will be an exact copy of the current state of your wallet.dat file stored in the export directory you specified in the config file. The file path will also be returned.

	If your original `wallet.dat` file becomes inaccessible for whatever reason, you can use your backup by copying it into your data directory and renaming the copy to `wallet.dat`.

	If you generate new addresses in your wallet after using ``backupwallet``, they will not be reflected in the backup file. Due to the deterministic property of HD wallets, if you generate new Sapling shielded addresses in your wallet after using ``backupwallet``, then restoring that wallet file and calling ``z_getnewaddress sapling`` will regenerate keys in the same order that they were created originally. After recreating keys with this method, it is recommended to restart the client using ``-rescan`` to force the client to check for prior transactions and properly update the balances of those addresses. 

Using ``z_exportwallet`` & ``z_importwallet``
+++++++++++++++++++++++++++++++++++++++++++++

	To export private keys in human readable format, use:

	``zcash-cli z_exportwallet <nameofbackup>``

	This will generate a file in the export directory listing all transparent and shielded private keys with their associated public addresses. The file path will be returned in the command line. As of Sapling activation, the shielded private keys in this file will be separated into legacy shielded private keys under the title *Zkeys* and Sapling shielded private keys.

	As of Sapling activation, the export also includes a comment with an HD wallet seed and associated fingerprint, both as hex strings. This seed is *only* for the wallet's Sapling shielded keys and addresses. For example::

	    HDSeed=5fa7753029b99c408e... 
	    fingerprint=5fa7753029b99c408e...
	    

	To import keys into a wallet which were previously exported to a file, use:

	``zcash-cli z_importwallet <path/to/exportdir/nameofbackup>``

	.. note::

	   ``z_importwallet`` does not yet support importing HD seeds but will import Sapling addresses in a standard form (non-HD). To backup and restore the full wallet inclusive of the Sapling HD seed, use the instructions for ``backupwallet`` above.. 

Using ``z_exportkey``, ``z_importkey``, ``dumpprivkey`` & ``importprivkey``
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	To export a single private key for a shielded address, use:

	``zcash-cli z_exportkey <z-address>``

	This will return the private key and will not create a new file.

	For exporting a single private key for a transparent address, you can use the command inherited from Bitcoin:

	``zcash-cli dumpprivkey <t-address>``

	This will return the private key and will not create a new file.

	To import a private key for a shielded address, use:

	``zcash-cli z_importkey <z-priv-key>``

	This will add the key to your wallet and rescan the wallet for associated transactions if it is not already part of the wallet.

	The rescanning process can take a few minutes for a new private key. To skip it, instead use:

	``zcash-cli z_importkey <z-private-key> no``

	For other instructions on fine-tuning the wallet rescan, see the command's help documentation:

	``zcash-cli help z_importkey``

	To import a private key for a transparent address, use:

	``zcash-cli importprivkey <t-priv-key>``

	This has the same functionality as ``z_importkey`` but works with transparent addresses.

	See the command's help documentation for instructions on fine-tuning the wallet rescan:

	``zcash-cli help importprivkey``
