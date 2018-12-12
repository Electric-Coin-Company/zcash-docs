.. _root:

.. image:: rtd_pages/images/zcash-logo-gold.png
   :scale: 15
   :align: right

===================
Zcash Documentation
===================

What is Zcash?
--------------

`Zcash <https://z.cash/>`__ is an implementation of the "Zerocash" protocol.
Based on Bitcoin's code, it intends to offer a far higher standard of privacy
through a sophisticated zero-knowledge proving scheme that preserves
confidentiality of transaction metadata. For more technical details, please check out our `Protocol Specification <https://github.com/zcash/zips/raw/master/protocol/protocol.pdf>`_.

**Before you get started with Zcash, please review the important items below:**
    
    :fa:`user-circle` :ref:`code_of_conduct`
      This project adheres to our Code of Conduct. By participating, you are expected to uphold this code.

    :fa:`code` :ref:`development_guidelines`
      A set of guidelines and best practices to contribute to the development of Zcash. 

    :fa:`lock` `Security Information <https://z.cash/support/security/>`_ 
      Zcash is experimental and a work-in-progress. Use at your own risk.

    :fa:`file-code-o` Deprecation Policy 
      A release is considered deprecated 16 weeks after the release day. 
      There is an automatic deprecation shutdown feature which will halt the 
      node sometime after this 16 week time period. The automatic feature 
      is based on block height and can be explicitly disabled.

.. _start:

Getting Started
---------------

For information on Zcash setup, upgrade, installation, build, configuration, and usage please see the :ref:`user_guide`.

.. _help:

Need Help?
----------

Answers to common questions from our users can be found in the `FAQ <https://z.cash/support/faq.html>`_.

.. admonition:: Collaborate 

   Zcash development is an open collaborative process. If you'd like to
   contribute, join our `chat system <https://chat.zcashcommunity.com/>`_
   and check out some of these channels:

    :fa:`comment` `Chat <https://chat.zcashcommunity.com/>`_
      Community Chat
    
    :fa:`comments` `Zcash <https://chat.zcashcommunity.com/channel/zcash>`_
      General user chat
    
    :fa:`random` `Zcash-Dev <https://chat.zcashcommunity.com/channel/zcash-dev>`_ 
      Software and Protocol Development

    :fa:`handshake-o` `Community-Collaboration <https://chat.zcashcommunity.com/channel/community-collaboration>`_ 
      Other open source development related to Zcash

    :fa:`users` `The-Zcash-Foundation <https://chat.zcashcommunity.com/channel/the-zcash-foundation>`_ 
      A room to define and develop the `Zcash Foundation <https://z.cash.foundation>`_ An organization to steward the community, protocol, and science around Zcash.
    
    :fa:`graduation-cap` `Zcash-Apprentices <https://chat.zcashcommunity.com/channel/zcash-apprentices>`_
      A study and peer-education room

    :fa:`magic` `Zcash-Wizards <https://chat.zcashcommunity.com/channel/zcash-wizards>`_
      Mad scientist brainstorming

.. _License:

License
-------

   For license information please see :ref:`License` 

.. toctree::
   :caption: Using Zcashd
   :hidden:

   rtd_pages/user_guide.rst
   rtd_pages/install_debian_bin_packages.rst
   rtd_pages/install_binary_tarball.rst
   rtd_pages/troubleshooting_guide.rst
   rtd_pages/payment_api.rst
   rtd_pages/wallet_backup.rst
   rtd_pages/addresses.rst
   rtd_pages/sapling_turnstile.rst   
   rtd_pages/zcash_conf_guide.rst
   rtd_pages/zcash_mining_guide.rst
   rtd_pages/security_warnings.rst
   rtd_pages/glossary.rst


.. toctree::
   :caption: Developers & Contributors
   :hidden:

   rtd_pages/development_guidelines.rst
   rtd_pages/supported_platform_policy.rst
   rtd_pages/index_zips.rst
   rtd_pages/nu_dev_guide.rst
   rtd_pages/testnet_guide.rst
   rtd_pages/librustzcash_arch.rst
   rtd_pages/ux_wallet_checklist.rst
   rtd_pages/code_of_conduct.rst
   
