:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for v2.0.6 <https://z.cash/downloads/zcash-2.0.6-linux64.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below:

.. code-block:: bash

   sha256sum zcash-2.0.6-linux64.tar.gz

Result: ``19755c5bffbb91be095add1b6e6e724b4c1c6f0c9c1f43353d51512cdd92e2a1``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master/v2.0.6>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.6-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.6/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
