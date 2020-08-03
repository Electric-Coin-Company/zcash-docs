Architecture and Cryptography
=======================
An overview of the cryptography inside Zcash. Don't worry if you don't understand what this means--this isn't required knowledge to use Zcash or build Zcash apps. However, this is required knowledge for developers who plan to contribute to cryptographic improvements.

Current Design
--------------

zkcrypto/pairing
    - Implements BLS12-381
zkcrypto/bellman
    - Implements Groth16, Circuit API
zcash-hackworks/sapling-crypto
    - Implements Sapling/Sprout circuits on top of bellman
    - Implements Jubjub
    - Implements some Sapling primitives necessary for testing
zcash/librustzcash
    - "Thin" FFI surrounding our crypto, for zcashd

Current Issues
--------------

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

New Design
----------

zkcrypto/jubjub
    - Implements Fp, Jubjub
    - No standard library requirement
zkcrypto/bls12-381 (depends on jubjub)
    - Implements BLS12-381, serial FFT
zkcrypto/bellman
    - Implements common circuit synthesis API, gadgets
zkcrypto/groth16
    - Implements groth16

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


