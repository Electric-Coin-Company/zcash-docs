:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.0.7-3 <https://z.cash/downloads/zcash-2.0.7-3-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.0.7-3 <https://z.cash/downloads/zcash-2.0.7-3-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.0.7-3-linux64-debian-jessie.tar.gz

Result: ``e7d4be58e5422d6be58543e3c41859420e0b96638bb6eba43dfaf8ad213f5cf0``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.0.7-3-linux64-debian-stretch.tar.gz

Result: ``b6961c0073c968dc30ed10a752ba657cb76acb22265dbc5f4bae7cc0395b35e4``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.7-3-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.7-3/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
