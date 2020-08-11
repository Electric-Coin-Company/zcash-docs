Architecture and Cryptography
=============================
An overview of the cryptography inside Zcash. Don't worry if you don't understand what this means--this isn't required knowledge to use Zcash or build Zcash apps. However, this is required knowledge for developers who plan to contribute to cryptographic improvements.

Current Design
--------------

librustzcash/pairing
    - `pairing` is a crate for using pairing-friendly elliptic curves. Currently, only the [BLS12-381](https://z.cash/blog/new-snark-curve.html) construction is implemented.
librustzcash/bellman
    - `bellman` is a crate for building zk-SNARK circuits. It provides circuit traits and primitive structures, as well as basic gadget implementations such as booleans and number abstractions.
librustzcash/jubjub
    - `jubjub` is a pure Rust implementation of the Jubjub elliptic curve group and its associated fields.
librustzcash/zcash_primitives
    - Implements some Sapling primitives necessary for testing
librustzcash/zcash_proofs
    - Implements Sapling/Sprout circuits on top of bellman, and the APIs for creating and verifying proofs.
librustzcash/zcash_history
    - Special implementation of Merkle mountain ranges (MMR) for Zcash!
librustzcash/zcash_client_backend
    - This library contains Rust structs and traits for creating shielded Zcash light clients.
zcash/src/rust
    - FFI library crate that exposes the Zcash Rust components to the C++ `zcashd` full node.

Current Issues
--------------

.. TODO: update this based on open issues in `librustzcash` repo

- We’re doing lots of refactorings and improvements to the code, 
  but these will span many different crates until we get to a stable 
  point. Hard to review and coordinate.

    - Example: bellman is going to be a “circuit-only” thing, agnostic to the proving system. 
      groth16 crate will handle groth16.
    - Example: hardware wallets only want/need jubjub and sapling primitives, so we need to 
      pull out zk-SNARK stuff (which requires an allocator, standard library, etc.)

- Code is inconsistent (with naming, as far as we know) with specification

- Nothing is labeled as constant/variable time

----

Roadmap
-------

.. TODO: update this based on open issues in `librustzcash` repo

librustzcash/pairing
    - `pairing` is being refactored into a generic library for working with pairing-friendly curves. After the refactor, `pairing` will provide basic traits for pairing-friendly elliptic curve constructions, while specific curves will be in separate crates.
librustzcash/bellman
    - `bellman` is being refactored into a generic proving library. Currently it is pairing-specific, and different types of proving systems need to be implemented as sub-modules. After the refactor, `bellman` will be generic using the `ff` and `group` crates, while specific proving systems will be separate crates that pull in the dependencies they require.
librustzcash/zcash_client_sqlite
    - Warning: This is an alpha build, not yet intended for 3rd party use.
    - This library contains APIs that collectively implement a Zcash light client in an SQLite database. We are actively rebasing this and adding features where / when needed.

Strategy
--------

- librustzcash repository is a Rust workspace containing all of our dependencies, 
  for the time being, via git subtrees

- We refactor code and integrate test vectors closely, following stringent code review processes and quality policies

- Later, we break the subtrees out into crates with stable APIs

End Goal
--------

- Complete cleanup of code (match spec, best practices)

- More members of the team learn how all this stuff works, good documentation

- Refactor of code into modular pieces that all relate to each other nicely

- no_std support for hardware wallets and other projects

- In the meantime, everything is CI’d and developed together

- The coolest, most awesome crypto codebase written in Rust anywhere in the world


