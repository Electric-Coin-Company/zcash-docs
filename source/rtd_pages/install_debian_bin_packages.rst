:orphan:

.. _install-debian-bin-packages-guide:

Debian Binary Packages Setup
============================

The Zcash Open Development Lab (ZODL) operates a package repository at
``apt.z.cash`` for 64-bit Debian-based distributions. If you'd like to try out
the binary packages, you can set it up on your system and install Zcash from
there.

.. warning::

   **Signing key rotation (2026).** Starting with v6.12.2, the APT repository
   is signed **only** with the ZODL key. The previous ECC key
   (``B1C9 095E AA18 48DB B54D 9DDA 1D05 FDC6 6B37 2CFE``, ``sysadmin@z.cash``)
   is deprecated and its revocation is planned for 2026-06-23. Existing
   installations will see ``NO_PUBKEY 7F4BBBBA23F0617F`` on ``apt-get update``
   until the ZODL key is imported — follow the steps below to add it. See
   `Rotation of the signing keys announcement
   <https://forum.zcashcommunity.com/t/rotation-of-the-signing-keys-for-zcashd-zallet-and-standalone-android-binaries-for-zodl/55144>`_
   on the Zcash Community Forum for background.

First install the following dependency so you can talk to our repository using HTTPS:

.. code-block:: bash

   sudo apt-get update && sudo apt-get install apt-transport-https wget gnupg2

Next add the ZODL signing key to apt's trusted keyring:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | sudo gpg --dearmor -o /usr/share/keyrings/zcash.gpg

``Key fingerprint = 0338 34DD 49DE CF9D BB99 34BC 6C93 CA8E 58E2 6AB1``  (ZODL, ``sysadmin@zodl.com``)

The keyring served at ``https://apt.z.cash/zcash.asc`` contains both the ZODL
key (used to sign v6.12.2 and later) and the legacy ECC key (needed only to
verify older releases until it is revoked on 2026-06-23).

.. note::

   The older ``apt-key add`` method is deprecated on modern Debian and Ubuntu
   systems. Use the ``/usr/share/keyrings/`` path above and reference it from
   the ``sources.list`` entry with ``signed-by=...`` (see below).

Add the repository to your Bullseye sources:

.. code-block:: bash

   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/zcash.gpg] https://apt.z.cash/ bullseye main" | sudo tee /etc/apt/sources.list.d/zcash.list

Or add the repository to your Bookworm sources:

.. code-block:: bash

   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/zcash.gpg] https://apt.z.cash/ bookworm main" | sudo tee /etc/apt/sources.list.d/zcash.list

Update the cache of sources and install Zcash:

.. code-block:: bash
   
   sudo apt-get update && sudo apt-get install zcash

Fetch the zero-knowledge parameters: 

.. code-block:: bash
   
   zcash-fetch-params

Lastly, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.

**Missing Public Key Error**

If you see something like:

``The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 7F4BBBBA23F0617F``

this means your system trusts only the old ECC key. v6.12.2 and later are
signed with the ZODL key (subkey ``7F4BBBBA23F0617F``, primary
``6C93CA8E58E26AB1``). Import the updated keyring from ``apt.z.cash``:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | sudo gpg --dearmor -o /usr/share/keyrings/zcash.gpg
   # If you previously added the key via apt-key, also remove the old entry:
   sudo apt-key del B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE 2>/dev/null || true
   sudo apt-get update

If your ``/etc/apt/sources.list.d/zcash.list`` still references the key
through ``apt-key`` (no ``signed-by=...`` option), update it to point at the
new keyring:

.. code-block:: bash

   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/zcash.gpg] https://apt.z.cash/ bookworm main" | sudo tee /etc/apt/sources.list.d/zcash.list

For any other signing key issues see :ref:`updating_signing_keys`.

See `Rotation of the signing keys announcement
<https://forum.zcashcommunity.com/t/rotation-of-the-signing-keys-for-zcashd-zallet-and-standalone-android-binaries-for-zodl/55144>`_
for background on the key transition.

Troubleshooting
---------------

.. note:: Only x86-64 processors are supported.


If you're starting from a new virtual machine, sudo may not come installed. See this issue for instructions to get up and running: https://github.com/zcash/zcash/issues/1844

**libgomp1 or libstdc++6 version problems**

These libraries are provided with gcc/g++. If you see errors related to updating them, you may need to upgrade your gcc/g++ packages to version 4.9 or later. First check which version you have using ``g++ --version``; if it is before 4.9 then you will need to upgrade.

On Ubuntu Trusty, you can install gcc/g++ 4.9 as follows:

.. code-block:: bash

   sudo add-apt-repository ppa:ubuntu-toolchain-r/test
   sudo apt-get update
   sudo apt-get install g++-4.9
   
Tor
---

The repository is also accessible via Tor, after installing the `apt-transport-tor` package, at the address zcaptnv5ljsxpnjt.onion. Use the following pattern in your sources.list file: ``deb [arch=amd64] tor+http://zcaptnv5ljsxpnjt.onion/ stretch main``

.. _updating_signing_keys:

Updating Signing Keys
---------------------

If your Debian binary package isn't updating due to an error with the public key, you can resolve the problem by updating to the new key. 

**Revoked Key error**

If you see something similar to:

``The following signatures were invalid: REVKEYSIG AEFD26F966E279CD``

Remove the key marked as revoked:

.. code-block:: bash

    sudo apt-key del AEFD26F966E279CD

Then retrieve the updated key:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

Then update the list again:

.. code-block:: bash

    sudo apt-get update


**Expired Key error**

If you see something similar to:

``The following signatures were invalid: KEYEXPIRED 1539886450``

Remove the old signing key:

.. code-block:: bash

    sudo apt-key del 1539886450

Remove the list item from local apt:

.. code-block:: bash

    sudo rm /etc/apt/sources.list.d/zcash.list

Update the repository list:

.. code-block:: bash

    sudo apt-get update

Then retrieve new key:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

Re-get the apt info:

.. code-block:: bash

    echo "deb [arch=amd64] https://apt.z.cash/ bullseye main" | sudo tee /etc/apt/sources.list.d/zcash.list

Then update the list again:

.. code-block:: bash

    sudo apt-get update

At this point you should be able to upgrade with the new public key.
