# IETF Identity + AI Standards Watch

Date: 2026-07-18

## Read now

_None._

## Monitor

_None._

## Adjacent / watchlist

- **draft-ietf-lsr-ospf-flex-algo-yang-15** (new-draft, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for OSPF Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-ospf-flex-algo-yang/) — This document defines a YANG data model to support OSPF Application-
   Specific Link Attributes and Flexible Algorithm.  It also creates the
   initial version of IANA-maintained YANG modules for IGP Algorithm
   Types, IGP Metric-Types, and IGP Link Attribute Applications.

   This document updates RFCs 8665, 9350, and 9843.
- **draft-sullivan-cfrg-raae-02** (new-draft, score 3, core_identity) [none]: [Random-Access Authenticated Encryption](https://datatracker.ietf.org/doc/draft-sullivan-cfrg-raae/) — This document defines random-access authenticated encryption (raAE),
   a primitive that partitions a message into an indexed sequence of
   segments that can be encrypted and decrypted independently and in any
   order.  It also specifies SEAL (Segmented Encryption and
   Authentication Layer), a parameterized construction that defines a
   family of concrete raAE instantiations, one for each valid choice of
   an Authenticated Encryption with Associated Data (AEAD) algorithm, a
   key derivation function (KDF), and associated parameters.

   SEAL provides two profiles, immutable (write-once) and mutable (in-
   place ciphertext rewrite), each with per-segment authentication.  A
   separately configured snapshot authenticator can additionally
   authenticate the complete, indexed segment set.

   The document also defines the security notions of raAE, specifies the
   requirements for conforming constructions, analyzes SEAL against
   those requirements, and provides example cipher suites and test
   vectors.
- **draft-agent-gw-02** (new-draft, score 2, ignored_after_review) [none]: [Agent Communication Gateway for Semantic Routing and Working Memory](https://datatracker.ietf.org/doc/draft-agent-gw/) — This document presents an architectural framework for an Agent
   Communication Gateway (Agent-GW), designed to support large-scale,
   heterogeneous, and dynamic multi-agent collaboration across
   administrative and protocol boundaries.

   As agents evolve from isolated entities to a collaborative digital
   workforce, the infrastructure must transition from rigid, endpoint-
   based connectivity to intent-based interaction.  This draft proposes
   Agent-GW as an infrastructure hub that provides native primitives for
   Semantic Routing (dispatching tasks by intent and capability),
   Working Memory (shared structured context across multi-step
   workflows), automated protocol adaptation (normalizing heterogeneous
   interfaces into a unified agent-facing protocol), oracle-free agent
   evaluation, and collaborative inference acceleration via a Knowledge
   Delivery Network (KDN).

   Beyond a single-gateway deployment, this document defines a
   hierarchical architecture for wide-area, multi-domain agent networks:
   three gateway tiers (access, domain, and inter-domain).  It describes
   which traffic classes traverse which tiers on both the data plane and
   the control plane, and specifies cross-domain semantic routing, name
   resolution, resilience, and operational considerations.

## Ignored after review

- **draft-ietf-bmwg-sr-bench-meth-07** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR)](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) performance for Segment Routing over IPv6 (SRv6) and MPLS (SR-
   MPLS).
- **draft-ietf-idr-rfc4360-bis-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extended Communities Attribute](https://datatracker.ietf.org/doc/draft-ietf-idr-rfc4360-bis/) — This document describes the "Extended Communities" BGP-4 attribute.
   This attribute provides a mechanism for labeling information carried
   in BGP-4.  These labels can be used to control the distribution of
   this information, or for other applications.

   This document obsoletes RFC 4360.

   This document also updates RFC 5701 by adding an "Operational
   Considerations" section.

## Errors / fetch failures

_None._
