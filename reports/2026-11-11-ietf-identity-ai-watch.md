# IETF Identity + AI Standards Watch

Date: 2026-11-11

## Read now

- **draft-ietf-oauth-sd-jwt-vc-26** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.

   Furthermore, this specification updates RFC7800 to allow for the
   Confirmation Claim (cnf) to be used regardless of the presence or
   absence of other claims.
- **draft-ietf-stir-certificate-transparency-06** (new-draft, score 15, adjacent_watchlist) [stir]: [STI Certificate Transparency](https://datatracker.ietf.org/doc/draft-ietf-stir-certificate-transparency/) — This document describes a framework for the use of the Certificate
   Transparency (CT) protocol for publicly logging the existence of
   Secure Telephone Identity (STI) certificates as they are issued or
   observed.  This allows any interested party that is part of the STI
   ecosystem to audit STI certification authority (CA) activity and
   audit both the issuance of suspect certificates and the certificate
   logs themselves.  The intent is to establish a level of trust within
   the STI ecosystem that relies on the verification of telephone
   numbers.  This involves requiring STI certificates to be listed in an
   established log and refusing to honor those that are not.  This
   effectively establishes the precedent that STI CAs must add all
   issued certificates to the logs and thus establishes unique
   association of STI certificates to an authorized provider or assignee
   of a telephone number resource.  In the STI ecosystem, the primary
   role of CT is to provide verifiable trust by detecting the
   unauthorized issuance of duplicate telephone number level delegate
   certificates or provider level certificates.  This provides a robust
   auditable mechanism for the detection of unauthorized creation of
   certificate credentials for illegitimate spoofing of telephone
   numbers or service provider codes (SPC).

   The framework borrows the log structure and API model from RFC 6962
   to enable public auditing and verifiability of certificate issuance.
   While the foundational mechanisms for log operation, Merkle Tree
   construction, and Signed Certificate Timestamps (SCTs) are aligned
   with RFC 6962, this document contextualizes their application in the
   STIR ecosystem, focusing on verifiable control over telephone number
   or service provider code resources.
- **draft-ietf-sidrops-aspa-profile-31** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.

## Monitor

- **draft-ietf-dance-client-auth-17** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DNS-Based Authentication of Named Entities (DANE) protocol
   describes how to publish Transport Layer Security (TLS) server
   certificates or public keys in the DNS, using the TLSA resource
   record.  This document describes how to use the TLSA record to
   publish client certificates or public keys, and also the rules and
   considerations for using them with TLS.  In addition, it defines a
   new TLS extension, DANE Client Identity, to convey the client's
   domain name identity to the server.

## Adjacent / watchlist

_None._

## Ignored after review

- **draft-ietf-dmm-tn-aware-mobility-33** (new-draft, score 0, ignored_after_review) [dmm]: [Mapping 5G slice to Transport Network slice with UDP Source Ports](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
   services of multiple 5G customers to be multiplexed over the same
   infrastructure.  While 5G slicing covers logical separation of
   various aspects of 5G infrastructure and services, user's data plane
   packets over the Radio Access Network (RAN) and Core Network (5GC)
   use IP in many segments of an end-to-end 5G slice.  When end-to-end
   slices in a 5G System use network resources, they are mapped to
   corresponding Transport Network (TN) slice(s) which in turn provide
   the bandwidth, latency, isolation, and other criteria required for
   the realization of a 5G slice.

   This document describes mapping of 5G slices to TN slices using UDP
   source port number of the GTP-U bearer when the TN slice provider is
   separated by an "attachment circuit" from the networks in which the
   5G network functions are deployed, for example, 5G functions that are
   distributed across data centers.  The slice mapping defined here is
   supported transparently when a 5G user device moves across 5G
   attachment points and session anchors.
- **draft-ietf-emailcore-as-31** (new-draft, score 0, ignored_after_review) [emailcore]: [Applicability Statement for IETF Core Email Protocols](https://datatracker.ietf.org/doc/draft-ietf-emailcore-as/) — Electronic mail is one of the oldest Internet applications that is
   still in very active use.  While the basic protocols and formats for
   mail transport and message formats have evolved slowly over the
   years, events and thinking in more recent years have supplemented
   those core protocols with additional features and suggestions for
   their use.  This Applicability Statement describes the relationship
   among many of those protocols and provides guidance and makes
   recommendations for the use of features of the core protocols.
- **draft-ietf-idr-rt-derived-community-14** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route-Target-derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route-Target-derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-idr-ts-flowspec-srv6-policy-22** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  It defines two modes of
   operation: transport steering into an SR Policy ("Mode 1"), in SR-
   MPLS and SRv6 networks, using BGP Extended Communities; and, in SRv6
   networks, transport steering combined with an egress service action
   at the egress node ("Mode 2"), signaled with the BGP Prefix-SID
   Attribute.
- **draft-ietf-savnet-inter-domain-problem-statement-23** (new-draft, score 0, ignored_after_review) [savnet]: [Problem Statement, Gap Analysis, and Requirements for Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/) — This document analyzes the problem space and provides a gap analysis
   of existing inter-domain source address validation (SAV) mechanisms.
   Based on these findings, it outlines the technical requirements for
   future improvements.
- **draft-jabley-dnsop-ordered-answer-section-02** (new-draft, score 0, ignored_after_review) [none]: [Ordering of RRSets in CNAME Responses in the DNS](https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/) — In the DNS, recursive resolvers receive queries and formulate
   corresponding responses by reference to data obtained from
   authoritative servers.  In the case where the query name (QNAME) and
   class (QCLASS) in the query matches an owner name in the DNS where a
   canonical name (CNAME) resource record is published, the response
   includes both the CNAME record and the resource record set
   corresponding to the request's query type (QTYPE) published at the
   CNAME target.  The ordering of these two different RRSets has not
   previously been clearly specified, but operational experience based
   on real-world client implementations confirms that the order is
   important.  This document updates RFC 1034 1035 to provide a clearer
   specification, consistent with deployed implementations.
- **draft-lampin-schc-voici-01** (new-draft, score 0, ignored_after_review) [none]: [VOICI](https://datatracker.ietf.org/doc/draft-lampin-schc-voici/) — The Static Context Header Compression (SCHC) framework identified the
   need for a minimal transport encapsulation that provides Session
   multiplexing when extrinsic Discriminators are insufficient.  This
   document specifies a Link Multiplexer (VOICI) that addresses those
   SCHC-driven requirements while remaining general enough to
   accommodate other compression mechanisms and uncompressed payloads.
   The encapsulation is designed for minimal overhead, reducing to 1
   byte in the common case (7 inline Session IDs), while supporting
   optional integrity protection and original EtherType/port recovery.
- **draft-lampin-schc-voici-compression-01** (new-draft, score 0, ignored_after_review) [none]: [SCHC Compression of VOICI Headers](https://datatracker.ietf.org/doc/draft-lampin-schc-voici-compression/) — This document describes how to compress VOICI headers using SCHC
   rules at a lower stratum, demonstrating that VOICI provides explicit
   routing metadata that is transparently compressed to minimal on-wire
   size while preserving standardized dispatch semantics.  It is
   intended as a reference for implementers deploying VOICI in SCHC-
   based networks and does not modify the VOICI specification itself.

## Errors / fetch failures

_None._
