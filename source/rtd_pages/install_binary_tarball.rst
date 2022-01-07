:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Stretch v4.6.0-1 <https://z.cash/downloads/zcash-4.6.0-1-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-4.6.0-1-linux64-debian-stretch.tar.gz

Result: ``1f8c918244f72ae67ecfd688d640d57b146b6e50292c243f46175e4697a8ecb3``

`Download Tarball for Debian Buster v4.6.0-1 <https://z.cash/downloads/zcash-4.6.0-1-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-4.6.0-1-linux64-debian-buster.tar.gz

Result: ``9de9c71cf837900175ff7889ceb84fcea6e854e6d739fb6aa3c9d12d5a128dc7``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-4.6.0-linux64-debian-stretch.tar.gz

    mv -t /usr/local/bin/ zcash-4.6.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
