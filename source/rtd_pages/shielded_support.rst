.. _shielded_support:

Shielded Support Resources
==========================

Everything you need to integrate and support zcash shielded addresses into your light wallet.

.. image:: images/shielded-support.png

Lightwalletd 
------------
A stateless server that serves light clients with blockchain information. It fetches blockchain data from zcashd, processes them to reduce data, and stores it in a database. This allows light clients with different requirements to get relevant data without interacting with zcashd directly.

**Resources**

* `Lightwalletd source code <https://github.com/zcash/lightwalletd>`_
* `Lightwalletd API docs <../lightwalletd/index.html>`_

**Quick info**

* Parallelize-able, stateless, and containerized
* Can run virtually on the cloud (EC2, GCP, AZURE, Docker, etc.)
* Not using load balancers, orchestrators, schedulers (yet)
* Metrics, stress tests, and testing done (ask us)

Android 
-------
We maintain a SDK that allows for wallet functionalities (address management, send, receive, etc.), documentation of the APIs, and a demo app that exercises the SDK.

**Resources**

* `Android SDK source code <https://github.com/zcash/zcash-android-wallet-sdk>`_
* `Android Demo app <https://github.com/zcash/zcash-android-wallet-sdk/tree/master/samples/demo-app>`_ 
*  `Android API docs <../android/zcash-android-wallet-sdk/index.html>`_ 

 
**Quick info**

* Native Android SDK and app, written in Kotlin
* Architecture: targeting ARM64, ARMv7 and x86
* APIs: We support API 16+ but we optimize for API versions 21+
* `Android SDK Threat Model <https://github.com/zcash/zcash-android-wallet-sdk/blob/master/docs/ThreatModel.md>`_

iOS 
---
We maintain a SDK that allows for wallet functionalities (address management, send, receive, etc.), documentation of the APIs, and a demo app that exercises the SDK.

**Resources**

* `iOS SDK source code <https://github.com/zcash/ZcashLightClientKit>`_
* `iOS Demo app <https://github.com/zcash/ZcashLightClientKit/tree/master/Example/ZcashLightClientSample>`_
* `iOS API docs <../ios/jazzy_docs/index.html>`_

**Quick info**

* Native iOS SDK and app, written in Swift
* Less mature then Android SDK but working towards parity
* Targeting the latest (past two 2 years) iPhones


WASM 
----

A minimal functioning demo web wallet that allows desktop OSes to use shielded addresses and separates web-specific wallet functionalities. 

Originally built 2019, and is not actively maintained: https://github.com/str4d/zcon1-demo-wasm. 
