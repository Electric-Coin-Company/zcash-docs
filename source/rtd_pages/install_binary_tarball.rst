:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Zcash company provides a binary tarball for download.

`Download Tarball for v2.0.3 <https://z.cash/downloads/zcash-2.0.3-linux64.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below:

.. code-block:: bash

   sha256sum zcash-2.0.3-linux64.tar.gz

Result: ``54171c6baf853d306525336d09dc1acab723573f64d1d82efa6b3a975a3354db``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master/v2.0.3>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.3-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.3/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
