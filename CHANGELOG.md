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

## [v6.12.1] - 2026-04-18

### Security
- Fixed: Orchard transaction with an `rk` encoding the identity point on the Pallas curve could cause zcashd to panic during proof verification. Identity `rk` is now rejected before proof verification.
- Fixed: Enforced that the ephemeral public key `epk` in each Orchard action encodes a non-identity point, resolving a potential consensus split with Zebra.
- Fixed: Duplicate block header could silently reset pool balance tracking fields, disabling ZIP 209 turnstile enforcement. Pool value initialization now occurs after the duplicate-data check.
- Fixed: Corrupted per-block pool deltas could be persisted to disk via the duplicate-header bug. Added a chain supply checkpoint at NU6.1 activation and recomputes shielded pool deltas from block data on startup.

### Changed
- Hardened pool balance accumulation against undefined behaviour due to signed integer overflow.
- Improved exception safety around calls to value computation functions.

