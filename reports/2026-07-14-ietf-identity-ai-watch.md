# IETF Identity + AI Standards Watch

Date: 2026-07-14

## Read now

- **draft-hardt-email-verification-01** (new-draft, score 9, core_identity) [none]: [Email Verification Protocol](https://datatracker.ietf.org/doc/draft-hardt-email-verification/) — This document defines the Email Verification Protocol (EVP), the
   HTTP-level protocol by which a browser obtains a signed email
   verification token from an issuer and presents it to a relying party
   (RP).  The protocol enables web applications to verify that a user
   controls an email address without sending a verification email.  It
   uses a three-party model in which the browser intermediates between
   the RP and the issuer, hiding the RP's identity from the issuer and
   supporting private, per-RP email addresses to prevent cross-site
   correlation.

   This document covers issuer discovery, the token issuance request,
   the Email Verification Token (EVT) and Key Binding JWT (KB-JWT)
   formats, and token verification.  The browser API — how the user
   selects an email address and how the token is delivered to the RP —
   is defined in the companion W3C Email Verification API
   ([EVP-Browser]).

## Monitor

_None._

## Adjacent / watchlist

- **draft-ietf-cats-oam-fw-00** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections encompassing clients, network paths, and service
   instances.
- **draft-ietf-ipsecme-ikev2-pqc-auth-09** (new-draft, score 3, core_identity) [ipsecme]: [Signature Authentication in the Internet Key Exchange Version 2 (IKEv2) using PQC](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-pqc-auth/) — Signature-based authentication methods are utilized in the Internet
   Key Exchange Version 2 (IKEv2).  The current version of the IKEv2
   protocol, specified in RFC 7296, supports traditional digital
   signatures.

   This document specifies a generic mechanism for integrating post-
   quantum cryptographic (PQC) digital signature algorithms into the
   IKEv2 protocol.  The approach allows for seamless inclusion of any
   PQC signature scheme within the existing authentication framework of
   IKEv2.  Additionally, it outlines how Module-Lattice-Based Digital
   Signatures (ML-DSA) and Stateless Hash-Based Digital Signatures (SLH-
   DSA), can be employed as authentication methods within the IKEv2
   protocol, as they have been standardized by US NIST.
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
- **draft-yang-dhc-dhcp-extension-00** (new-draft, score 3, adjacent_watchlist) [none]: [DHCP New Option Extension based on LLM Capability](https://datatracker.ietf.org/doc/draft-yang-dhc-dhcp-extension/) — This document specifies a DHCP option extension designed for campus
   networks to help client devices distinguish and connect to a master
   device with the LLM (Large Language Model).  The mechanism extends a
   new DHCP option containing two specific parameters within the DHCP
   payload: the master device's LLM address and the master device's LLM
   configuration.  This allows client devices to identify and register
   to LLM-enabled master device during the bootstrap phase.
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
- **draft-ietf-dnsop-structured-dns-error-25** (new-draft, score 0, ignored_after_review) [dnsop]: [Structured Error Data for Filtered DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/) — DNS filtering is widely deployed for various reasons, including
   network security and policy enforcement.  However, filtered DNS
   responses lack structured information for end users to understand the
   reason for the filtering.  Existing mechanisms to provide explanatory
   details to end users cause harm especially if the blocked DNS
   response is for HTTPS resources.

   This document updates RFC 8914 by signaling client support for
   structuring the EXTRA-TEXT field of the Extended DNS Error to provide
   details on the DNS filtering.  Such details can be parsed by the
   client and displayed, logged, or used for other purposes.
- **draft-ietf-idr-bgp-ls-sr-policy-nrp-03** (new-draft, score 0, ignored_after_review) [idr]: [SR Policies Extensions for Network Resource Partition in BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-nrp/) — A Network Resource Partition (NRP) is a subset of the network
   resources and associated policies on each of a connected set of links
   in the underlay network.  An NRP ID is an important network resource
   attribute associated with the Segment Routing (SR) policy and needs
   to be reported to the external components.  This document defines a
   new TLV which enables the headend to report the NRP which the SR
   Policy Candidate Path (CP) is associated with using Border Gateway
   Protocol Link-State (BGP-LS).
- **draft-ietf-idr-rfc4360-bis-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extended Communities Attribute](https://datatracker.ietf.org/doc/draft-ietf-idr-rfc4360-bis/) — This document describes the "Extended Communities" BGP-4 attribute.
   This attribute provides a mechanism for labeling information carried
   in BGP-4.  These labels can be used to control the distribution of
   this information, or for other applications.

   This document obsoletes RFC 4360.

   This document also updates RFC 5701 by adding an "Operational
   Considerations" section.
- **draft-ietf-sidrops-8210bis-26** (new-draft, score 0, ignored_after_review) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RFC6480) prefix origin data, Router Keys, and ASPA
   data from a trusted cache.  This document describes a protocol to
   deliver them.

   This document describes version 2 of the RPKI-Router protocol.
   [RFC6810] describes version 0, and [RFC8210] describes version 1.
   This document is compatible with both.

## Errors / fetch failures

_None._
