:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.2-3 <https://z.cash/downloads/zcash-2.1.2-3-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.2-3 <https://z.cash/downloads/zcash-2.1.2-3-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.2-3-linux64-debian-jessie.tar.gz

Result: ``71d8072e2b6be2f237d122548c828da096018b888a970e6645d7deef0d1fed64``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.2-3-linux64-debian-stretch.tar.gz

Result: ``5c54cc5f6cca7c798adeca5a5b1e58b08a6f48b4304ef72e323e74f05635e136``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.2-3-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.2-3/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
