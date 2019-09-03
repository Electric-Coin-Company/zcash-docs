:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.0.7-2 <https://z.cash/downloads/zcash-2.0.7-2-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.0.7-2 <https://z.cash/downloads/zcash-2.0.7-2-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.0.7-2-linux64-debian-jessie.tar.gz

Result: ``64e51bcbb602fdc857c0f84c9050980442e366e9d4acb949b0787d2baba23f93``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.0.7-2-linux64-debian-stretch.tar.gz

Result: ``597d169606ed2d1b621d80f39c06291ff01d57cae8f178c0d6e90df1a27405ed``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.7-2-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.7-2/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
