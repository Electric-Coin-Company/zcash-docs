:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Zcash company provides a binary tarball for download.

`Download Tarball for v2.0.4 <https://z.cash/downloads/zcash-2.0.4-linux64.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below:

.. code-block:: bash

   sha256sum zcash-2.0.4-linux64.tar.gz

Result: ``529900fa311509274cc3912ae886a3b8e193ae8a91801f810c3ca58f44bd1730``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master/v2.0.4>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.4-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.4/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
