:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Zcash company provides a binary tarball for download.

`Download Tarball for v2.0.0 <https://z.cash/downloads/zcash-2.0.0-linux64.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below:

.. code-block:: bash

   sha256sum zcash-2.0.0-linux64.tar.gz

Result: ``0597b7d5b6c4e4aa4a1981d7e5870e2e83f7b75622937ed61529b0a459255066``

This checksum was generated from our gitian deterministic build process. View all gitian signatures.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.0-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.0/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
