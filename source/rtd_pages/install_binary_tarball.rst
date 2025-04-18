:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.2.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.2.0 <https://download.z.cash/downloads/zcash-6.2.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.2.0-linux64-debian-bullseye.tar.gz

Result: ``71cf378c27582a4b9f9d57cafc2b5a57a46e9e52a5eda33be112dc9790c64c6f``

`Download Tarball for Debian Bookworm v6.2.0 <https://download.z.cash/downloads/zcash-6.2.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.2.0-linux64-debian-bookworm.tar.gz

Result: ``7bd3e81cc317c3788148cf3ca2780b72538f45be81efe5f9d63d5aad0310bd6f``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.2.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.2.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
