:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, we are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.2.0 <https://z.cash/downloads/zcash-5.2.0-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.2.0-linux64-debian-buster.tar.gz

Result: ``ca69b7ece7a6b0ea9085bc3425b0a57e8fef0f0ea26022aedbcd280d5dcd7526``

`Download Tarball for Debian Bullseye v5.2.0 <https://z.cash/downloads/zcash-5.2.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.2.0-linux64-debian-bullseye.tar.gz

Result: ``ce7113843862f04470d1260e293c393e523b36f8e5cb7b942ed56fa63a8ae77f``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.2.0-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.2.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
