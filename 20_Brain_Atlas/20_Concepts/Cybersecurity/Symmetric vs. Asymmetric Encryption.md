---
type: concept
title: "Symmetric vs. Asymmetric Encryption"
subject: "Cybersecurity"
date_created: 2026-07-28
tags: [cybersecurity, cryptography, encryption, security-fundamentals]
source: "[[Cybersecurity_Roadmap]]"
source_hash: "1572d01123e2f95e15b99e8b446c7118"
---

## The idea (one clear statement)
**Symmetric Encryption** uses a single shared secret key for both encryption and decryption, whereas **Asymmetric Encryption** uses a mathematically linked key pair (a public key for encryption and a private key for decryption).

## Why it matters / how it connects
*   **Symmetric Encryption (e.g., AES):** Computationally fast and efficient for bulk data encryption, but requires a secure mechanism to share the secret key.
*   **Asymmetric Encryption (e.g., RSA, ECC):** Solves key distribution and enables digital signatures, but is computationally slower.
*   **Hybrid Cryptosystems:** Modern protocols like TLS/HTTPS combine both—using asymmetric cryptography to securely exchange a session key, then switching to symmetric cryptography for fast data transfer.

## Related concepts
- [[CIA Triad]]
- [[Cybersecurity Roadmap]]
- [[Cybersecurity_Roadmap]]
