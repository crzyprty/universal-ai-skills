---
name: rust-build
description: Rust builds and code repair.
---

# Rust builds and code repair

Use when writing or fixing Rust code. Inspect `Cargo.toml`, toolchain version, and the smallest failing module. Prefer one focused patch. Run `cargo fmt --check`, `cargo check`, and affected tests when Cargo is installed. Run `cargo clippy` or a full build if relevant. Distinguish dependency errors from source errors; do not claim compilation if the toolchain was unavailable.

Follow root `SKILL.md`. Find external references only when necessary with `python tools/lookup.py find "topic"`.
