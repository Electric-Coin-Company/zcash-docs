:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.0.7 <https://z.cash/downloads/zcash-2.0.7-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.0.7 <https://z.cash/downloads/zcash-2.0.7-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.0.7-linux64-debian-jessie.tar.gz

Result: ``90047e923523d7b10aa9af157de054dac9ee004952536b62e1a38cadeec4ac7a``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.0.7-linux64-debian-stretch.tar.gz

Result: ``92c84bb5a95e40f46a720ff112f710d42f3f820887869f362133be7f609e0479``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.0.7-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.0.7/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
