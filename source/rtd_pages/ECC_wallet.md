# Light Client Development

The following resources allow development of apps and services that can transact on the blockchain without downloading an entire copy of the blockchain. A light client (also known as lightweight node) is referencing a trusted full node's copy of the blockchain, whereas a full node is a node that fully enforces all of the rules of the blockchain. 

The following resources have been used to build shielded mobile wallets, companion apps for full nodes, and more. 

## Overview of Resources
This [overview of light client components](lightclient_support.html) lists the available resources to build a light client on Zcash. Currently, a light client requires a trusted server to host the blockchain information and to process them into a compact block, which contains less than half as big as a block on chain. Light clients can use this interface to stay current with the Zcash network with less bandwidth and memory requirements. 

## Contributing Guidelines
We have [contributing guidelines](https://github.com/zcash/ZcashLightClientKit/blob/master/CONTIBUTING.md), which are the same across our repos. Tl;dr: We love pull requests! We have some rules for code and comments, which we'd like for you to follow before submitting a PR. All contributions will be licensed under the MIT license. 

## Light Client Threat Model
This [threat model](wallet_threat_model.html) “security invariants” that the apps and SDK should currently provide, as well as pointing out their limitations. This document is intended for curious technical users of the ECC wallet apps as well as developers making use of the SDK in their own apps.