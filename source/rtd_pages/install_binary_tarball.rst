:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, we are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.4.0 <https://z.cash/downloads/zcash-5.4.0-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.4.0-linux64-debian-buster.tar.gz

Result: ``629acff33e687a52ddfe006b9607eda9dcfb1bba69d8533aad8750c8aad13229``

`Download Tarball for Debian Bullseye v5.4.0 <https://z.cash/downloads/zcash-5.4.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.4.0-linux64-debian-bullseye.tar.gz

Result: ``d4ae16e06a29c0c8d31f5d109da83a374acaacc40032ab35cce017f47cdc7bae``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.4.0-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.4.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
