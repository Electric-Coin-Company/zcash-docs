# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Types of Changes
`Added` for new features.

`Changed` for changes in existing functionality.

`Deprecated` for soon-to-be removed features.

`Removed` for now removed features.

`Fixed` for any bug fixes.

`Security` in case of vulnerabilities.

## [v6.12.2] - 2026-05-06

### Security
- Fixed: The v4 (Sapling) transaction deserializer silently accepted transactions with no Spend descriptions and no Output descriptions but with a non-zero `valueBalanceSapling` — the value was discarded during deserialization, so the consensus check that should have rejected such transactions never fired. Zebra rejects this encoding at deserialization time; zcashd now matches, closing a potential consensus split.
- Fixed: In NU5 and later, the authorizing data of v5 transactions (transparent input scripts, Sapling and Orchard proofs and signatures) is committed by the header's `hashBlockCommitments` via `hashAuthDataRoot`, but not by `hashMerkleRoot`. A poisoned block body whose `hashMerkleRoot` matched the honest header but was inconsistent with `hashBlockCommitments` could be persisted to disk, and on the sidechain path could permanently invalidate an otherwise valid header. `hashBlockCommitments` is now pre-checked in `AcceptBlock` for active-tip extensions; the sidechain mismatch is treated as body-replaceable and only the affected block-index body state is reset.
- Fixed: The v6.12.1 Orchard `epk` check rejected only the all-zeros identity encoding; it did not reject other 32-byte strings that fail to encode a valid Pallas curve point (non-canonical `x ≥ q_P` and canonical `x` for which `x³ + 5` is a non-residue). The check has been broadened to require that `epk` decodes to a valid non-identity Pallas point, matching Zebra.

### Changed
- Signing: Release artifacts (tarballs and APT `Release.gpg`) are now signed **only** with the ZODL key (`sysadmin@zodl.com`, fingerprint `0338 34DD 49DE CF9D BB99 34BC 6C93 CA8E 58E2 6AB1`). The legacy ECC key (`B1C9 095E AA18 48DB B54D 9DDA 1D05 FDC6 6B37 2CFE`, `sysadmin@z.cash`) is deprecated; revocation is planned for 2026-06-23. Users verifying with the ECC key alone will need to import the ZODL key from `https://apt.z.cash/zcash.asc`. See [Rotation of the signing keys announcement](https://forum.zcashcommunity.com/t/rotation-of-the-signing-keys-for-zcashd-zallet-and-standalone-android-binaries-for-zodl/55144).
- Docs: `install_debian_bin_packages.rst` now uses `/usr/share/keyrings/zcash.gpg` with `signed-by=...` instead of the deprecated `apt-key add` flow.

## [v6.12.1] - 2026-04-18

### Security
- Fixed: Orchard transaction with an `rk` encoding the identity point on the Pallas curve could cause zcashd to panic during proof verification. Identity `rk` is now rejected before proof verification.
- Fixed: Enforced that the ephemeral public key `epk` in each Orchard action encodes a non-identity point, resolving a potential consensus split with Zebra.
- Fixed: Duplicate block header could silently reset pool balance tracking fields, disabling ZIP 209 turnstile enforcement. Pool value initialization now occurs after the duplicate-data check.
- Fixed: Corrupted per-block pool deltas could be persisted to disk via the duplicate-header bug. Added a chain supply checkpoint at NU6.1 activation and recomputes shielded pool deltas from block data on startup.

### Changed
- Hardened pool balance accumulation against undefined behaviour due to signed integer overflow.
- Improved exception safety around calls to value computation functions.

