# IETF Identity + AI Standards Watch

Date: 2026-08-22

## Read now

- **draft-prakash-aip-01** (new-draft, score 31, core_identity) [none]: [Agent Identity Protocol (AIP): Verifiable Delegation for AI Agent Systems](https://datatracker.ietf.org/doc/draft-prakash-aip/) — This document specifies the Agent Identity Protocol (AIP), a protocol
   for verifiable, delegable identity for AI agent systems.  AIP
   introduces Invocation-Bound Capability Tokens (IBCTs) that bind
   identity, authorization, scope constraints, and provenance into a
   single cryptographic artifact.  Two token modes are defined: a
   compact mode using JSON Web Tokens (JWT) with Ed25519 signatures for
   single-hop interactions, and a chained mode using Biscuit tokens with
   append-only blocks and Datalog policy evaluation for multi-hop
   delegation chains.  Protocol bindings are specified for the Model
   Context Protocol (MCP), Agent-to-Agent Protocol (A2A), and generic
   HTTP APIs.  The protocol addresses authentication gaps in current AI
   agent infrastructure where a survey of approximately 2,000 MCP
   servers found all lacked authentication.  This revision specifies a
   normative verification algorithm, defines the canonical policy
   encoding for chained mode, describes how AIP composes with workload
   identity systems such as SPIFFE, and maps AIP against the cross-
   organization delegation requirements enumerated in
   [I-D.reece-wimse-cross-org-delegation].
- **draft-sato-soos-gar-05** (new-draft, score 30, trust_infrastructure) [none]: [The Governance Audit Record (GAR) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-gar/) — This document specifies the Governance Audit Record (GAR), the audit
   architecture for agentic AI systems.  GAR defines five audit types,
   the Session Audit Record (SAR), the Audit Alert system, auditor
   principal categories, and the Audit Package for external regulatory
   inspection.  GAR provides verifiable evidence that AI agent sessions
   were governed in accordance with the Intent Declaration Primitive
   [I-D.sato-soos-idp] and the Human Escalation Mechanism
   [I-D.sato-soos-hem].  GAR answers the governance question: can any
   of this be proven to a regulator?  GAR is a domain-specific
   application of the SCITT (Supply Chain Integrity, Transparency and
   Trust) architecture [I-D.ietf-scitt-architecture] extended with
   causal ordering semantics for agentic governance events.  GAR defines
   the Authority Lifecycle Event (ALE) category: a normative set of
   causally-ordered event types covering the complete agent session
   revocation and recovery lifecycle, including single-agent revocation,
   authority suspension, partial state recording, recovery initiation,
   credential restoration, and multi-agent delegation tree events.

   Version -03 adds the SOOS Governance Semantic Convention: the
   normative soos.governance.* OpenTelemetry attribute namespace for
   governance observability (Section 13), the SOOS GAR Processor
   specification for OTel-to-SAR pipeline construction with Session
   Block Merkle integrity (Section 14), four new Authority Lifecycle
   Events, three mandatory provenance fields on Cedar evaluation
   records, and the XPID mirror field on ACD session ALEs.

   Version -04 made the Session Block construction rules of Section
   14.3 more explicit, closing three ambiguities found during
   independent interop verification at the IETF 126 Hackathon.

   Version -05 supersedes -04's Section 14.3 text with a corrected
   construction: the Merkle leaf and internal-node hashes are now
   domain-separated (RFC 6962 S2.1's MTH, with 0x00/0x01 prefix
   octets) and odd-length levels use RFC 6962's k-split recursive
   tree shape rather than duplicate-node padding, closing a
   malleability class structurally equivalent to CVE-2012-2459 that
   was present in -04's construction (Section 15 S.15.e).  This
   revision is fully self-contained: unlike -03 and -04, it does not
   carry forward unreproduced text from an earlier version.  Version
   -05 also adds a subject_digest field to Cedar-evaluation GAR
   records (Section 8.6), the same construction used by the Agent
   Accountability Composition [I-D.mih-sato-agent-accountability-
   composition] as its cross-slot join key, positioning GAR as a
   conforming AEP instance under the RATS-bound composition of
   [I-D.sokolov-rats-aep-composition]; the field is normatively
   scoped to prohibit independent re-serialization where an
   upstream party has already established the action's canonical
   serialization, per the failure mode documented in
   [I-D.hillier-scitt-arp] Appendix D.
- **draft-reilly-mws-01** (new-draft, score 29, trust_infrastructure) [none]: [Machine-Web Symbiosis (MWS): An Architecture for Autonomous Agent Maintenance of Web Permanence and Integrity](https://datatracker.ietf.org/doc/draft-reilly-mws/) — The World Wide Web has no native memory and no native trust layer.
   It records what exists now; it cannot prove what existed, when it
   existed, or whether it has been altered.  This gap, tolerable when
   the web's consumers were human, is untenable in an era of
   autonomous AI agents that read, cite, and act on web content at
   machine scale.

   This document defines Machine-Web Symbiosis (MWS): an architecture
   in which autonomous agents and web infrastructure sustain each
   other.  Agents continuously verify, archive, anchor, and cross-
   reference web resources across multiple independent permanence
   systems; the maintained record in turn supplies agents and all
   downstream consumers with verifiable ground truth.  MWS formally
   unifies the protocols of the Reilly Protocol Suite, including the
   REM Protocol (dual-layer digital permanence), the REM Triple
   Fingerprint (multi-algorithm content identity), WebProof (web
   content attestation), and the Cognitive Trust Stack (verifiable
   agent behavioral provenance), into a single layered architecture,
   and specifies a complete step-by-step implementation process for
   an MWS attestation pipeline, from artifact ingestion through
   continuous verification and repair.

   Machine-Web Symbiosis is introduced by the author, Lawrence John
   Reilly Jr., as a deliberate broadening of the man-computer
   symbiosis of Licklider (1960) from the human-machine pairing to
   the agent-web pairing.

   This revision adds the Sentinel Transparency Interface, a
   normative machine-readable and human-readable publication
   interface through which an MWS deployment exposes its own
   verification activity.

   The architecture specified here is implemented.  A conforming
   deployment, the MWS Sentinel Loop, is in continuous unattended
   operation at https://www.remweb4.org/sentinel: autonomous agents
   verify an attested corpus across the six permanence layers,
   detect drift against the live web, repair detected degradation,
   and publish every outcome to an append-only hash-linked ledger
   that any third party may walk and check without the operator's
   cooperation.  Machine-Web Symbiosis is therefore documented here
   as a realized architecture rather than a proposed one.  A
   multi-operator attestation model is defined as the remaining
   path from this single-operator deployment to distributed
   infrastructure.
- **draft-xu-mcp-agent-did-framework-00** (new-draft, score 24, core_identity) [none]: [DID-Based Service Discovery, Authentication, and Authorization Framework for MCP Agents](https://datatracker.ietf.org/doc/draft-xu-mcp-agent-did-framework/) — This document proposes a DID-based framework for service discovery,
   authentication, and authorization of MCP (Model Context Protocol)
   Agents, based on the W3C Decentralized Identifier (DID) standard.
   The framework uses the did:web and did:key methods to provide
   verifiable, decentralized identifiers for MCP Clients and Servers.
   It defines DID method selection, DID Document extensions, service
   discovery mechanisms (including URL derivation, DNS-based discovery,
   and directory-based capability queries), and a challenge-response
   mutual authentication protocol.  The framework also describes
   coexistence with OAuth 2.0 and enables trust establishment, dynamic
   capability-based service discovery, and fine-grained authorization
   with portable identities.
- **draft-mih-sato-agent-accountability-composition-01** (new-draft, score 22, trust_infrastructure) [none]: [Agent Accountability: Composition and Conformance](https://datatracker.ietf.org/doc/draft-mih-sato-agent-accountability-composition/) — Autonomous and semi-autonomous software agents increasingly take
   consequential actions across administrative and trust domains.
   Holding such an action accountable — to a regulator, auditor, or
   counterparty who does not trust the operator — requires answering
   several questions, each answerable by an independently-verifiable
   profile: whether the agent was permitted to act (CAN), which
   accountable human authorized the specific action (WHO), what the
   agent actually did (WHAT), and whether the runtime enforced correctly
   (AUDIT).

   This document specifies, in Informational terms, how such profiles
   compose — by a shared action-digest, each verifying independently —
   and defines a shared conformance-vector suite against which any
   profile may be tested.  It complements existing audit-architecture
   and record-format work rather than replacing it, reusing existing
   signing, transport, and transparency mechanisms.  Its focus is an
   assurance tier those documents leave open: most agent records today
   are self-attested by an interested party; this document makes
   reachable and testable an anchored, third-party-verifiable tier, in
   which a record is registered to a transparency service (SCITT) so a
   party who trusts neither the agent nor the operator can verify it.
   Self-attestation remains a valid baseline; convergence on the
   disinterested tier — by any conforming profile — is the goal, not a
   single mandated format.
- **draft-wei-aic-identity-cert-00** (new-draft, score 21, core_identity) [none]: [AI Agent Identity Certificate (AIC) Extension for X.509 v3](https://datatracker.ietf.org/doc/draft-wei-aic-identity-cert/) — This document defines the AI Agent Identity Certificate (AIC)
   Extension for X.509 v3 certificates.  The AIC extension enables
   binding of an AI Agent's cryptographic identity to a natural person
   (principal), providing cryptographic evidence that can support
   attribution of AI-autonomous actions to a principal.  This
   specification intentionally separates cryptographic delegation from
   authorization semantics: AIC defines the cryptographic binding
   between agent and principal, while all capability and policy
   semantics are defined externally by vendors, industries, or
   regulators.  The extension is identified by the IANA Private
   Enterprise Number 66257 assigned to the document author's
   organization.

   The AIC extension carries agent identity fields (agentId,
   delegationMode), a principal identifier (principalUid) linking the
   agent to the authorizing principal, a container-based capability
   declaration, authorization boundary constraints, and delegation
   authorization evidence with replay protection.  A companion
   PrincipalAuthorization extension anchors Principal-side grant
   declarations and delegation policies.  An authorizationConstraints
   container provides offline-verifiable execution boundaries (IP range,
   window).  An extensibility framework allows vendor-specific and user-
   specific metadata.

   This document specifies the ASN.1 module, OID registration, field
   semantics, delegation model, and extensibility framework.  Security
   considerations for deployment in regulated enterprise environments
   are discussed.
- **draft-wilder-scitt-physical-site-engage-receipt-01** (new-draft, score 21, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
   Receipts_ (PSER): tamper-evident, signed, offline-verifiable records
   that describe an autonomous or human-directed physical engagement at
   a specific real-world site governed by a defined operating envelope.
   Each receipt is a SCITT Signed Statement as defined by the SCITT
   architecture, encoded as a COSE Single Signer message, carrying a
   JCS-canonicalized JSON payload with a five-artifact vocabulary
   describing (1) the _Site_, (2) the _Operator_ and _Actor_, (3) the
   _Engagement Window_ and _Envelope_, (4) the _Attestation Evidence_
   from a Trusted Execution Environment (TEE), and (5) the _Adapter
   Write-In_ recording that the receipt was posted into an out-of-band
   operations layer.  A Physical-Site Engagement Receipt is registerable
   in any conforming SCITT Transparency Service, obtaining a Receipt
   that proves the Statement's inclusion in that Service's verifiable
   data structure.  Registration does not establish that the Issuer
   registered every receipt it issued.

   This profile deliberately makes a NARROW, checkable claim -- "this is
   a tamper-evident, signature-verifiable record that a specific
   engagement occurred at a specific site under a specific envelope, and
   its evidence was sealed by a specific TEE" -- and explicitly does NOT
   claim that the engagement was safe, correct, or wise, that the site
   conditions were as described, or that any downstream operational
   outcome followed.  Compliance verdicts derived from the receipt (SLA
   credit, insurance underwriting, regulatory audit) are the
   responsibility of the relying party and its policies, not of this
   profile.

   The profile is designed around a three-party trust model in which no
   single party can unilaterally forge or repudiate a receipt: the _site
   owner_ physically hosts and controls the TEE hardware (they own the
   box); the _TEE silicon vendor_ attests the key material inside the
   TEE through its hardware root of trust (silicon vouches for the key);
   and the _Issuer_ writes the vocabulary, registers Signed Statements
   with a Transparency Service, and posts the resulting receipt into the
   site's operations layer via a WRITE_ONLY adapter.  This separation is
   normative in this profile: implementations MUST NOT collapse these
   three roles into a single custodian, and relying parties MUST NOT
   trust a receipt that lacks any one of them.
- **draft-schrock-action-evidence-boundary-04** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
   authorization, policy, and execution systems.  Each system can
   produce a valid artifact while the executor still lacks a safe rule
   for joining the artifacts to the exact effect, consuming one-time
   authority, and handling an uncertain outcome.  This document defines
   the Action Evidence Boundary (AEB), an executor-side processing model
   for that lifecycle.

   AEB requires native artifact verification, Canonical Action
   Identifier (CAID) matching, Authorization Evidence Chain (AEC)
   satisfaction, a separate local authorization decision, durable atomic
   consumption or reservation, invocation, closed effect outcomes, and
   authenticated reconciliation.  It defines no receipt or token format,
   no policy language, no universal evidence taxonomy, and no new
   registry.  Native workload credentials, message signatures, attested
   per-action tokens, permit records, authorization receipts, and status
   mechanisms retain their own semantics and verifiers.
- **draft-sharif-mcps-secure-mcp-01** (new-draft, score 16, core_identity) [none]: [MCPS: Cryptographic Security Layer for the Model Context Protocol](https://datatracker.ietf.org/doc/draft-sharif-mcps-secure-mcp/) — This document specifies MCPS (MCP Secure), a cryptographic
   security layer for the Model Context Protocol (MCP).  MCPS adds
   agent identity verification, per-message signing, tool definition
   integrity, and replay protection to MCP communications without
   modifying the core protocol.

   MCPS operates as an envelope around existing JSON-RPC messages.
   It introduces four primitives: (1) Agent Passports for
   cryptographic identity bound to a specific origin, (2) signed
   message envelopes for integrity and non-repudiation, (3) tool
   definition signatures covering the full tool object for detecting
   poisoning and tampering, and (4) nonce-plus-timestamp replay
   protection with transcript binding to prevent downgrade attacks.

   The design is fully backward-compatible.  MCPS-unaware clients
   and servers continue to function normally.  MCPS-aware endpoints
   progressively negotiate security capabilities through trust
   levels L0 (no verification) through L4 (full mutual
   authentication with revocation checking).

   All cryptographic operations use ECDSA P-256 (NIST FIPS 186-5).
   Signatures use IEEE P1363 fixed-length r||s encoding per
   RFC 7518 Section 3.4 with low-S normalization to prevent
   signature malleability.  Canonical serialization uses JSON
   Canonicalization Scheme (JCS) per RFC 8785.  The Trust Authority
   component is self-hostable with no external service dependency.
- **draft-bu-agentproto-security-principal-binding-06** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
   authority, agent instance identity, tool or external-resource
   identity, delegation state, session continuity, and action evidence.
   These claims have different verifiers, freshness requirements,
   failure modes, and security consequences.  If they are collapsed into
   a single token, identity label, session identifier, or audit record,
   protocol text can accidentally imply more authority or accountability
   than the receiver can actually verify.

   This document defines a verifier-facing model for separating those
   claims.  It provides a reusable matrix format that protocol authors
   can use to state, for each security-relevant claim, which field
   carries it, which party verifies it, what binding or freshness rule
   applies, what failure behavior is required when the claim is absent,
   stale, inconsistent, or not verifiable, and what constrained result
   an application may consume after successful verification.  It also
   separates specification status, implementation status, and evidence
   type so that reviewers can distinguish current protocol text,
   implementation evidence, inherited mechanisms, and architectural
   assumptions.  The document is protocol-neutral.  It is intended to
   help compare candidate agent communication drafts and to provide
   security-considerations and requirements text for agent session and
   delegation binding.

   The document also defines row-outcome semantics and dependency-
   closure rules for composed mappings.  These rules prevent a composite
   result from becoming stronger than its verified inputs, distinguish
   failed checks, unsupported verifier capabilities, checks skipped
   after a failed prerequisite, and unavailable or ambiguous inputs,
   propagate transitive dependency failures, and make cyclic, stale,
   downgraded, or revision-incoherent dependencies visible to reviewers.
- **draft-ietf-stir-certificate-transparency-04** (new-draft, score 15, adjacent_watchlist) [stir]: [STI Certificate Transparency](https://datatracker.ietf.org/doc/draft-ietf-stir-certificate-transparency/) — This document describes a framework for the use of the Certificate
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

   The framework borrows the log structure and API model from RFC6962 to
   enable public auditing and verifiability of certificate issuance.
   While the foundational mechanisms for log operation, Merkle Tree
   construction, and Signed Certificate Timestamps (SCTs) are aligned
   with RFC6962, this document contextualizes their application in the
   STIR ecosystem, focusing on verifiable control over telephone number
   or service provider code resources.
- **draft-schrock-ep-authorization-receipts-12** (new-draft, score 15, adjacent_watchlist) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
   an evidence artifact binding an enrolled approver key to one
   canonical action before execution.  An approver-held key signs an
   Authorization Context containing the action hash, policy reference,
   shared authorization instance, per-signoff nonce, audience, and
   validity window.  A Trust Receipt carries the signed contexts,
   terminal consumption record, and Merkle inclusion material so a
   relying party can verify the recorded event offline under
   independently selected log, directory, policy, and approver trust
   inputs.

   The receipt establishes only the guarantees of the selected
   verification profile.  The mapping from an enrolled approver
   identifier to a natural person is asserted by the directory
   authority.  Offline verification does not establish current
   revocation status, global non-replay, comprehension, legality,
   safety, or execution.  Replay prevention requires an online atomic
   consumption store at the executor.  The state-machine invariants are
   machine-checked under the assumptions stated in this document.

   This revision defines the closed EP-AUTHORIZATION-BUNDLE-v1 pre-
   execution profile and its verification algorithm.  The bundle carries
   the Action Object, signed Authorization Contexts, signoffs, key
   proofs, and presentation evidence; it deliberately carries no
   terminal consumption or execution claim.  An optional, profile-
   identified authorization binding can commit the human evidence to an
   independently verified native authorization artifact without
   replacing that artifact or making this receipt format depend on its
   transport or trust model.

   A receipt is evidence, not authorization.  This document does not
   treat a local user interaction as an authorization decision.  It
   defines one evidence artifact that an authorization architecture can
   use in a human-confirmation flow: the signed Authorization Context is
   action-bound confirmation evidence an authorization server MAY
   validate and bind to the grant it issues.  The resulting Trust
   Receipt records terminal consumption and remains evidence; neither
   object makes the authorization decision.  That decision remains with
   the authorization server.
- **draft-sokolov-rats-aep-composition-05** (new-draft, score 15, trust_infrastructure) [none]: [Composing Application-Layer Action Evidence with Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-sokolov-rats-aep-composition/) — This document sketches a composition pattern in which an application-
   layer "action evidence package" (AEP) -- a signed action record that
   can be hash-linked to earlier records and that reports an action
   taken by an automated (for example, AI-agent) system, the authority
   under which it was taken, and its outcome -- is treated as Evidence
   in the sense of the RATS Architecture (RFC 9334) and bound to
   platform Evidence produced by a hardware root of trust.  The intent
   is that a single Verifier, or a composition of Verifiers, can
   appraise both the platform state and the application-layer record
   together, and emit an Attestation Result that a Relying Party can use
   to reason about _what an automated system reports it did_ and _the
   appraised state of the platform associated with that record_. The
   composition does not turn a self-reported action or outcome into an
   independently observed fact; it prevents the Relying Party from
   having to rely on an unbound operator-side log alone.  This is an
   individual sketch intended to ask the working group whether the
   pattern is already covered by existing mechanisms or warrants a short
   document.
- **draft-helmprotocol-tttps-09** (new-draft, score 14, adjacent_watchlist) [none]: [The TLS TimeToken Secure Protocol (tttps://)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies the TLS TimeToken Secure Protocol (tttps://),
   a protocol extension that augments TLS 1.3 with cryptographically
   verifiable temporal ordering.  TTTPS introduces Proof-of-Time (PoT):
   a multi-source synthesised timestamp bound to a holder identity and
   to a live TLS session through an explicit holder-proof construction,
   verified in constant time independent of network size.

   Internet infrastructure conventionally assumes ordering-neutral
   channels.  NTP servers, BGP routing authorities, DNS resolvers, and
   transaction sequencers all have an operational incentive to
   misrepresent event ordering; this document formalises that condition
   as the Strategic Channel Controller Problem (SCCP).  PoT detects
   Byzantine time-source manipulation with probability at least 1 minus
   2 to the negative 61st power, and an AdaptiveSwitch mechanism makes
   sustained ordering manipulation economically self-defeating; the
   equilibrium threshold is derived in closed form and empirically
   calibrated from deployed auction data.

   This document has Experimental status.  A reference deployment has
   produced over 70,000 verified records, 55 percent of which were
   generated by autonomous AI agents.  The mandatory-to-implement
   integrity mode (SHA-256) is completely and publicly specified in
   Appendix B; the optional high-assurance integrity mode (GRG) remains
   subject to pending patent proceedings and is specified only at the
   abstract-interface level pending their conclusion.

Discussion Note

   This note is to be removed before publishing as an RFC.

   This document is being discussed on the dispatch@ietf.org mailing
   list.  Comments and participation are welcome.

   Changes from -06:

   *  Header: revision -06 -> -07; submissionType corrected from "IETF"
      to "independent" (this document is an Independent Submission, not
      an IETF Working Group product); dates updated.

   *  Section 2 / Section 6.1 (the former binding_key construction): the
      -06 construction let any participant in the TLS session --
      including an attacker in its own session with the Issuer --
      recompute binding_key and pass verification without proving
      possession of any holder key material, because binding_key was
      derived solely from public TLS Exporter output and the public PoT
      bytes.  This is replaced with a PoT Record v2 (180 octets)
      carrying an explicit holder_auth_type (Ed25519 public key, MTI, or
      a pre-shared secret, OPTIONAL) and a binding_proof computed by the
      holder over the TLS Exporter output at binding time.  Verification
      now performs integrity-tag interpretation first, in a single
      fixed-cost pass with a three-way intact/resolved/unresolvable
      verdict; in -06 the equivalent check was ordered after five other
      checks.  The full 8-step order is specified in Section 2.5.

   *  Appendix B: removed the "(Placeholder)" designation.  Appendix B
      now specifies a public Integrity Algorithm Registry: alg_id 0x0001
      (SHA-256, detection-only) is the Mandatory-to-Implement algorithm
      and is completely and publicly specified, free of any licensing
      condition. alg_id 0x0100 (GRG, detection-and-correction) remains
      OPTIONAL and interface-only pending conclusion of the patent
      proceedings referenced in Section 12.

   *  IANA Considerations, HTTP/3 Stream Types: renamed from "HTTP/3 and
      QUIC Stream Types".  The "QUIC Stream Types" registry entry is
      removed; no such IANA registry exists, and QUIC stream
      identification for TTTPS is carried entirely by the HTTP/3-layer
      frame registration.

   *  Abstract: shortened from six paragraphs to three; removed inline
      document citations (an abstract is conventionally self-contained
      and does not carry bracketed references).

   *  Scope reduced to the core protocol: satellite communication, SS7
      legacy infrastructure, 5G/6G core network ordering, and deep-
      space/SAGIN deployment material are removed from this revision as
      out of scope; see 3GPP and CCSDS/TIPTOP for domain-specific
      profiles.  The former Appendix E (a regulated therapeutic-design
      motivating scenario) is removed as non-normative and out of scope
      for a protocol specification.

   *  Sections 1 through 4 of -06 (Introduction, Use Cases, Requirements
      Language, Problem Statement) are consolidated into a single
      Section 1, removing a duplicated BCP 14 paragraph and shortening
      the document.

   *  The former Section 4.3 (Shannon Gap / SCCP) and Section 7.4 (V*
      equilibrium) are shortened; the full economic and information-
      theoretic derivations remain in the companion paper [POT2026],
      which this document now points to rather than reproduces.

   *  IANA Time Source Type Registry: named operators (NIST, Google,
      Cloudflare, Apple) are replaced with source classes (national
      metrology laboratory, GNSS-disciplined, Roughtime-authenticated,
      NTS-authenticated, PTP grandmaster); the same replacement is
      applied to the worked examples in Sections 1.3, 2.2, and 7.1.
      This document does not depend on, or endorse, any specific named
      operator.

   *  References [RFC8915], [RFC5705], and [RFC8126] are unchanged from
      -06.

   Changes from -02 through -05 (compressed; see prior revisions of this
   draft for the full itemised changelog): -03 added Use Cases, the SS7/
   SCCP instance analysis, path manipulation scenarios, the trust model,
   and the Implementation Status section (RFC 7942). -04 added the
   Formal Verification Artifacts subsection and the former Appendix E.
   -05 is not separately archived. -06 added Oracle Confidence Gating
   (the G-Score), corrected IPR licensing language per ISE guidance, and
   recorded the provisional "tttps" URI scheme registration.
- **draft-klassen-eu2122-content-profile-01** (new-draft, score 14, trust_infrastructure) [none]: [EU2122 V1.0 Standard: Content Profile for AI Output Verification Receipts](https://datatracker.ietf.org/doc/draft-klassen-eu2122-content-profile/) — This document defines a content profile for AI output
   verification receipts. It specifies the minimum fields,
   classification taxonomy, and evidentiary properties that
   a receipt MUST contain in order to constitute verifiable
   evidence that an AI-generated output was checked before
   a human or downstream agent acted on it. The profile
   is designed to be
   carried over any conformant wire format, including ACTA
   signed receipts, SCITT transparency logs, and standalone
   JSON or CBOR payloads.

   Existing IETF drafts in this space define wire formats
   for signing, transmitting, and storing AI agent receipts.
   None defines what a verification receipt must contain at
   the content layer. This document fills that gap. It
   introduces a mandatory eight-category failure taxonomy
   (the Information Bottleneck Species), a verification
   verdict schema, and evidentiary field requirements
   derived from the EU AI Act (Regulation 2024/1689), the
   Product Liability Directive (2024/2853), and the PS 861
   audit standard.

   We invite and even urge implementers to adopt, populate
   and grow the AI Output Verification market segment,
   which the author has also defined in communications to
   Gartner, Forrester, PAC/Teknowlogy, and IDC. The
   category exists. The specification is here. Build to it.
- **draft-reilly-aigov-00** (new-draft, score 14, ai_infrastructure) [none]: [Verifiable AI Governance and Data Privacy Records](https://datatracker.ietf.org/doc/draft-reilly-aigov/) — Organizations deploying artificial intelligence systems are
   increasingly required to state which systems they operate, what data
   those systems process, on what authority, and under what human
   oversight.  Today these statements are produced as unverifiable self-
   assertions: spreadsheets, questionnaire responses, and policy
   documents that cannot be checked by a relying party and cannot be
   shown to have existed before an incident.

   This document defines an evidence layer for AI governance.  It
   specifies five record types (the AI System Record, the Governance
   Event Record, the Register Completeness Attestation, the Erasure
   Record, and the Selective Disclosure Response), a hash-linked append-
   only AI System Register that carries them, and verification
   procedures that let an auditor, a regulator, or a counterparty
   confirm what an operator asserted and when the assertion was made.

   The record format is built on salted per-field commitments so that a
   register can be published, audited, and retained for long periods
   without publishing the underlying data, and so that personal data can
   be erased while the integrity of the register survives.  This
   property is referred to here as Erasure-Compatible Permanence.
- **draft-ietf-emu-eap-ppt-03** (new-draft, score 12, core_identity) [emu]: [Extensible Authentication Protocol (EAP) Using Privacy Pass Token](https://datatracker.ietf.org/doc/draft-ietf-emu-eap-ppt/) — This document describes Extensible Authentication Protocol using
   Privacy Pass token (EAP-PPT) Version 1.  The protocol specifies use
   of the Privacy Pass token for client authentication within EAP as
   defined in RFC3748.  Privacy Pass is a privacy preserving
   authentication mechanism used for authorization, as defined in
   RFC9576.  EAP-PPT must be performed only in a tunnel-based EAP
   method.
- **draft-saha-aadp-01** (new-draft, score 11, core_identity) [none]: [The Agent Action Decision Protocol (AADP): Per-Action Authorization for AI Agents](https://datatracker.ietf.org/doc/draft-saha-aadp/) — The Agent Action Decision Protocol (AADP) separates per-action
   authorization from an agent's identity and its standing capabilities,
   and gives that authorization semantics that a stateless tool
   permission or access grant cannot express: whether a specific
   proposed action, with specific argument values, may be performed now,
   given mutable state such as cumulative budgets, live reservations,
   approval lifecycle, and a kill switch.  Existing agent-security work
   concentrates on identity -- who an agent is, what credentials it
   holds, and which tools it may reach; AADP addresses the complementary
   decision, and composes with that work rather than replacing it.  This
   document defines a two-phase wire contract between a Policy Decision
   Point (PDP) that authorizes agent actions and the Policy Enforcement
   Points (PEPs) that perform them: verdicts with machine-readable
   reasons, obligations that fail closed, atomic budget reservation, an
   approval lifecycle, idempotency behavior, evidence sufficient to re-
   derive every verdict, and a set of evaluation invariants any
   conformant decision point must observe -- including the rule that an
   irreversible action is never executed autonomously.  The protocol is
   transport-agnostic and is designed so that decision points and
   enforcement points can be implemented independently, in different
   languages, by different parties.
- **draft-sharif-agent-audit-trail-01** (new-draft, score 11, core_identity) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
   AI agent systems.  The Agent Audit Trail (AAT) defines a
   JSON-based record structure with mandatory fields for agent
   identity, action classification, outcome tracking, and trust
   level reporting.  Records are linked via tamper-evident hash
   chaining using SHA-256 per RFC 8785, with optional ECDSA
   signatures for non-repudiation.

   The format addresses requirements from the EU AI Act
   (Regulation 2024/1689), which mandates automatic recording of
   events for high-risk AI systems effective August 2026.  It also
   maps to SOC 2 Trust Services Criteria, ISO/IEC 42001,
   ISO/IEC 24970, prEN 18229-1, and PCI DSS v4.0.1 logging
   requirements.

   The design is transport-agnostic and supports export to JSONL,
   Syslog (RFC 5424), and CSV while preserving chain integrity.
   Privacy is addressed through input/output hashing, content
   fingerprinting, and tombstone-based deletion compatible with
   GDPR Article 17.

   This revision (-01) adds pre-execution recording requirements,
   recording independence, deny reason codes, replay protection,
   external timestamp anchoring, and content fingerprinting based
   on feedback from independent implementers.
- **draft-feng-agentproto-session-requirements-02** (new-draft, score 10, core_identity) [none]: [Requirements for Agent Session Establishment, Capability Negotiation, and Sessionless Interaction](https://datatracker.ietf.org/doc/draft-feng-agentproto-session-requirements/) — This document defines requirements for session-based and sessionless
   interactions between entities.  For session-based interactions, it
   covers transport-independent interaction binding, endpoint
   authentication, capability negotiation, session establishment,
   authorization, and lifecycle management.  It also defines security
   and state requirements for interactions, such as notifications,
   probes, and atomic requests, that do not establish a session.  It is
   assumed that the entities involved already know of each other; how
   they came to know each other is outside the scope of this document.
   At least one party to an interaction is an agent as defined in
   Section 3.  This document is intended as a contribution to the
   agentproto working group's use cases, gap analysis, and requirements
   deliverable.

   A session is a bilateral association.  Protocols and application
   semantics for coordinating delegation or handoff of work to an entity
   that is not a peer, and management functions such as cross-entity
   accountability and audit, are outside the scope of these base session
   requirements.  This document specifies only that such coordination
   does not, by itself, change the peers or state of an existing
   session.
- **draft-ekahraman-oauth-attestation-authz-native-app-01** (new-draft, score 9, authorization) [none]: [OAuth 2.0 Attestation Based Authorization for Native Applications](https://datatracker.ietf.org/doc/draft-ekahraman-oauth-attestation-authz-native-app/) — This document defines an extension to OAuth 2.0 [RFC6749] that
   enables Authorization Servers to consider Attestation Results
   presented by Native Applications when issuing access grants.  By
   incorporating information about the security characteristics of the
   application and its execution environment, this mechanism supports
   Authorization Policies that are tailored to the trustworthiness of
   the Native Application.
- **draft-fassbender-scitt-time-anchor-04** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-gould-regext-epp-status-set-03** (new-draft, score 9, core_identity) [none]: [Status Set Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-gould-regext-epp-status-set/) — This document describes an Extensible Provisioning Protocol (EPP)
   extension for the provisioning and management of status sets applied
   to EPP objects, such as the domain name object in RFC 5731.  The EPP
   status values defined in the EPP object mappings, such as Section 2.3
   of RFC 5731, support human-readable text that describes the rationale
   or reason for the status applied to the object.  There can be many
   overlapping reasons for a status value being applied to the object,
   such as implementing a lock service, complying with a court order, or
   addressing domain abuse.  A status set defines an object representing
   the reason for setting a list of status values, so clients and
   servers can manage the status sets in place of individual status
   values to effectively manage the overlapping reasons.  The EPP
   extension supports the provisioning of client status sets, disclosure
   of the server status sets, and an enhanced authorization model for
   client status sets with the EPP Authentication Token in
   [I-D.gould-regext-auth-token].
- **draft-ietf-spice-vdcarch-01** (new-draft, score 9, verifiable_claims) [spice]: [A reference architecture for direct presentation credential flows](https://datatracker.ietf.org/doc/draft-ietf-spice-vdcarch/) — This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.
- **draft-jacobs-web4-node-state-admission-00** (new-draft, score 9, core_identity) [none]: [Web4 Node State and Admission Requirements](https://datatracker.ietf.org/doc/draft-jacobs-web4-node-state-admission/) — This document defines implementation-neutral requirements for
   persistent node identity, declared state, governed admission,
   suspension, revocation, re-admission, and succession in Web4-class
   federations.  It distinguishes a node from its network and credential
   representations, identifies the minimum information required for
   externally inspectable participation, and specifies lifecycle and
   failure semantics that future protocol bindings can implement.  The
   requirements permit heterogeneous internal architectures and do not
   mandate a transport, serialization, credential technology, storage
   system, computational model, or proprietary coordination mechanism.
   The document extends prior Web4 terminology, conformance, and
   federation-architecture work by supplying a public requirements layer
   between architecture and future interoperable bindings.
- **draft-linkgenetic-linkid-uri-00** (new-draft, score 9, core_identity) [none]: [The LinkID URI Scheme and Resolution Model](https://datatracker.ietf.org/doc/draft-linkgenetic-linkid-uri/) — This document specifies the "linkid" URI scheme and a resolution
   model for persistent, location-independent identifiers.  A LinkID
   identifies a resource independently of its current network location.
   Resolution maps the persistent identifier to a current actionable URI
   using one or more resolvers.  The scheme is intended for Web,
   document, archival, scientific, government, enterprise, and machine-
   to-machine references where locations may change while reference
   identity must remain stable.
- **draft-moskowitz-ads-b-auth-03** (new-draft, score 9, core_identity) [none]: [ADS-B Authentication](https://datatracker.ietf.org/doc/draft-moskowitz-ads-b-auth/) — Automatic Dependent Surveillance – Broadcast (ADS-B) is a
   surveillance technology mandated in many airspaces.  It is now widely
   deployed but suffers from a lack of security and privacy.  From a
   security point of view, it is relatively easy to spoof ADS-B messages
   with readily available hardware and software.  From a privacy point
   of view, every ADS-B message contains the aircraft's assigned 24-bit
   ICAO address, a unique identifier that can be cross-referenced with
   external databases (e.g. aircraft registries) to reveal the owner,
   and can be used to track when and where a specific aircraft has
   flown.  In addition, the main transmission medium used for ADS-B, the
   1090 MHz frequency, on which messages are broadcast using the
   Extended Squitter (1090ES) format, is approaching saturation in some
   parts of the world due to the volume of ADS-B and other protocol
   messages, resulting in packet loss in certain areas.

   This paper presents the IETF TESLA protocol along with X.509
   certificates issued by ICAO member states for each aircraft to
   authenticate all ADS-B messaging.  It leverages the 8PSK phase
   overlay (PO) scheme proposed in the Minimum Operational Performance
   Standards (MOPS) for ADS-B (RTCA [DO-260C]), which enables 1090ES
   ADS-B transmissions to convey three times more information, to
   support the transmission of the extra security information required
   by the authentication scheme.  By doing so, the impact of
   authentication on channel usage is negligible.  Beyond message
   authentication, this scheme protocol has two important additional
   benefits: 1) the possibility to implement a Flight Authorization
   scheme, allowing ATC and intercepting aircraft to not only
   authenticate an aircraft but to verify that it is authorizes to
   conduct that flight and 2) a privacy-preserving methodology that
   assigns random 24-bit identifiers to designated aircraft while still
   enabling blind authentication of their ADS-B transmissions.
- **draft-sahu-agent-action-receipts-00** (new-draft, score 9, agent_identity) [none]: [Signed, Hash-Chained Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-sahu-agent-action-receipts/) — This document specifies a format for action receipts: compact,
   individually signed JSON records that state that a specific AI agent
   attempted a specific action at a specific time, under a specific
   policy decision, and what the outcome was.  Receipts are linked into
   an append-only hash chain so that deletion, insertion, reordering, or
   modification of any previously recorded receipt is detectable by a
   verifier that holds only the records and the signer's public key.

   The format is deliberately small and self-contained.  Verification
   requires no network access, no service operated by the producer of
   the receipts, and no state beyond the records themselves and a trust
   anchor obtained out of band.  This document specifies the record
   fields, the canonical byte sequence that is signed, the chain linkage
   rule, the verification procedure, and test vectors.
- **draft-sergeev-wexp-core-01** (new-draft, score 9, core_identity) [none]: [The Witnessed Execution Protocol (WEXP): Core Specification](https://datatracker.ietf.org/doc/draft-sergeev-wexp-core/) — The Witnessed Execution Protocol (WEXP) Core defines carrier-neutral
   appraisal semantics for execution-related evidence.  It defines four
   distinct content bases, two independent evidence qualifiers, the
   Boundary Ceiling, exact-claim support, deterministic accept,
   downgrade, and reject verdicts, composition without inflation, and a
   normalized interface between evidence-carrying profiles and
   appraisers.  WEXP Core does not define a record serialization,
   signature envelope, action identifier, authorization model, or
   evidence-artifact schema.  A companion Native Record profile can
   encode the normalized inputs defined here, and other carriers can do
   so without adopting that record format.
- **draft-treneule-humia-protocol-00** (new-draft, score 9, core_identity) [none]: [HUMIA: A Website-First Protocol for Human-AI Cooperation](https://datatracker.ietf.org/doc/draft-treneule-humia-protocol/) — HUMIA defines a website-first mechanism for publishing a machine-
   readable cooperation policy for AI agents.  A website publishes a
   JSON policy at /.well-known/humia.json.  The policy identifies the
   origin and expresses site-level conditions for public-content access,
   selected AI usage purposes, attribution, and optional usage
   reporting.

   HUMIA does not replace the Robots Exclusion Protocol, authentication,
   authorization, licensing, or access-control mechanisms.  It is an
   additional cooperation layer.  This document also defines an
   optional, experimental Humia: discovery record in robots.txt that
   points HUMIA-aware agents to the canonical policy URI.
- **draft-wang-dmsc-drisac-01** (new-draft, score 9, agent_identity) [none]: [Distributed Onboarding and Information Synchronization of Agent Capabilities](https://datatracker.ietf.org/doc/draft-wang-dmsc-drisac/) — AI Agents may dynamically join, leave, and update their capabilities
   while participating in interactions across administrative domains.
   Efficient capability discovery in such environments requires
   mechanisms to onboard agent capabilities and maintain consistent
   capability information across distributed management entities.
   Existing service registration and discovery mechanisms do not
   necessarily provide a capability-oriented mechanism for distributed
   synchronization and hierarchical forwarding of agent capability
   information.

   This document proposes a distributed and hierarchical mechanism for
   AI Agent capability onboarding, information synchronization, and
   capability-based discovery.  The mechanism introduces a hierarchical
   capability classification model and defines two functional entities:
   the Agent Capability Management Server (ACMS), which maintains and
   synchronizes capability information, and the Agent Capability Access
   Server (ACAS), which manages locally attached agents.  Capability
   information is aggregated and propagated among ACMSs, while access
   information for locally attached agents is maintained by ACASs.  A
   capability table is used to determine forwarding toward relevant
   ACMSs, and an access mapping table is used for local agent matching.
   The document also describes onboarding and intent-driven capability
   discovery procedures.  The mechanism is intended to provide a
   distributed control-plane foundation for capability-aware agent
   discovery and does not define agent-to-agent interaction or task
   execution protocols.
- **draft-correctover-ccs-05** (new-draft, score 8, core_identity) [none]: [Correctover Conformance Shape (CCS): Runtime Verification for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — This document defines the Correctover Conformance Shape (CCS), a
   runtime verification framework for AI agent tool calls.  CCS
   specifies seven verification dimensions (Structure, Schema, Latency,
   Cost, Identity, Integrity, Security) that tool calls and results must
   conform to at runtime.  The framework defines a receipt format with
   Ed25519 signatures, three verification outcomes (pass, fail,
   unknown), and normative requirements for implementations.
- **draft-efstathiou-samp-agent-management-00** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
   management-plane protocol for heterogeneous AI agents.  SAMP allows a
   management system to discover agents, query their state, receive
   events, subscribe to event streams, and optionally configure or
   execute explicitly exposed operations under policy control.

   SAMP is inspired by operational management protocols such as SNMP,
   but it is designed for AI-agent-specific concepts such as dynamic
   profiles, autonomy classes, enrollment, trust states, and policy-
   gated execution.  It is not an agent-to-agent communication protocol,
   an agent tool-use protocol, or an agent framework specification.

   This document defines SAMP version 0.1 as an Experimental protocol
   suitable for controlled environments and independent interoperability
   testing.
- **draft-etcheverry-action-ref-03** (new-draft, score 8, core_identity) [none]: [Action Reference: A Deterministic Identifier for Agent Actions](https://datatracker.ietf.org/doc/draft-etcheverry-action-ref/) — This document defines "action_ref", a deterministic, content-
   addressed identifier for autonomous agent actions.  Any party holding
   the four preimage fields (agent_id, action_type, scope, timestamp)
   can independently compute and verify the identifier without trusting
   the emitting system.  The document specifies the derivation
   algorithm, canonical serialization using RFC 8785 JSON
   Canonicalization Scheme (JCS), timestamp format requirements,
   canonical receipt envelope, optional fields for revocation and policy
   rotation auditability, scope conventions, and a composability model
   with existing exactly-once execution guarantees.
- **draft-mcphillips-agentenvelope-derived-authority-00** (new-draft, score 8, authorization) [none]: [AgentEnvelope: Deterministic Derived Authority for Autonomous Systems](https://datatracker.ietf.org/doc/draft-mcphillips-agentenvelope-derived-authority/) — AgentEnvelope defines a deterministic derived-authority model for
   autonomous and action-performing systems.  Instead of issuing bearer
   credentials or authorization envelopes from a central authority,
   AgentEnvelope derives scoped action capabilities from customer-held
   custody material and canonical action envelopes.  A verifier can
   check an action signature against a public action record without
   receiving roots, seeds, private keys, or hosted service access.  This
   document specifies the v1 derivation model, signing domains, public
   record structure, mint delegation flow, verification rules, and
   security considerations.
- **draft-wmz-nmrg-agent-ndt-arch-05** (new-draft, score 8, agent_identity) [none]: [Network Digital Twin and Agentic AI based Architecture for AI driven Network Operations](https://datatracker.ietf.org/doc/draft-wmz-nmrg-agent-ndt-arch/) — A Network Digital Twin (NDT) provides a network emulation tool usable
   for different purposes such as scenario planning, impact analysis,
   and change management.  Agentic AI enables dynamic goal-driven
   execution and adaptive behavior and closed-loop autonomy.  By
   integrating a Network Digital Twin into network management together
   with the Agentic AI, it allows the network management activities to
   take user intent or service requirements as input, automatically
   assess, model, and refine optimization strategies under realistic
   conditions but in a risk-free environment.  Such environment that
   operates to meet these types of requirements is said to have AI
   driven Network Operations.

   AI driven Network Operations brings together existing technologies
   such as Agentic AI and Network Digital Twin which may be seen as the
   use of a toolbox of existing components enhanced with a few new
   elements.

   This document describes an architecture for AI driven network
   operations and shows how these components work together with network
   digital twin and Agentic AI capabilities.  It provides a cookbook of
   existing technologies to satisfy the architecture and realize intent-
   based network management to meet the needs of the network service.
- **draft-zhao-a2a-dns-sd-00** (new-draft, score 8, adjacent_watchlist) [none]: [DNS-Based Service Discovery for Agent2Agent (A2A) Protocol Agents](https://datatracker.ietf.org/doc/draft-zhao-a2a-dns-sd/) — The Agent2Agent (A2A) protocol defines how two agents communicate
   once one knows the other's URL, and how an agent's self-description
   (the Agent Card) is retrieved from a well-known URI at that URL.  It
   does not define how agents on the same host or local network find
   each other in the first place.  This document profiles DNS-Based
   Service Discovery (DNS-SD) over Multicast DNS (mDNS) for that
   purpose: it defines the "a2a" service type, the TXT record keys used
   with it, the discovery procedure, and the security model under which
   discovery results are treated as hints whose trust is established by
   Agent Card verification, not by the discovery channel.  It also
   requests IANA registration of the "a2a" service name.
- **draft-barrett-dnsop-domain-set-00** (new-draft, score 7, trust_infrastructure) [none]: [The Domain Set Discovery Protocol (domain-set)](https://datatracker.ietf.org/doc/draft-barrett-dnsop-domain-set/) — Organizations commonly operate under multiple domain names: a primary
   website, legacy names, defensive registrations, divisional brands,
   and names in restricted or verified top-level domains.  No standard
   mechanism exists for a domain owner to declare, in a machine-readable
   and verifiable way, which domains belong to the same organization.
   This document defines "domain-set", a protocol by which domain
   operators publish membership in a set of domains using a DNS TXT
   record as the discovery mechanism.  The record either lists the
   members directly or references an extensible Domain Set Manifest
   retrieved over HTTPS.  Mutual attestation is the validation
   requirement: a link between two domains is valid only when both
   domains independently publish records naming each other.  Every
   direction of a link MUST be retrieved over an authenticated channel,
   by DNSSEC or by the Web PKI.  The protocol enables browsers, security
   tooling, and AI systems to answer the question "are these two domains
   operated by the same organization?" from first-party, owner-published
   data rather than inference.
- **draft-dogru-scitt-disclosure-evidence-06** (new-draft, score 7, trust_infrastructure) [none]: [Transformation Evidence and Coverage Reconciliation for Auditable Data Disclosure](https://datatracker.ietf.org/doc/draft-dogru-scitt-disclosure-evidence/) — Audit receipts for automated data access attest to what a gateway
   recorded.  Two questions remain outside their reach: what was changed
   in the data before it was disclosed, and whether the set of receipts
   is complete with respect to the data source's own accounting of
   activity.  This document defines two evidence structures that answer
   those questions: Transformation Evidence, a per-disclosure statement
   of which classes of values were transformed and how, carrying counts
   and class names but never values; and Coverage Reconciliation, a
   procedure and result statement that compares a source's own activity
   counters against a receipt set over a time window and classifies what
   the comparison establishes.  The reconciliation result distinguishes
   what was matched under a declared correspondence from what was
   observed without a receipt, receipted without a corresponding
   observation, excluded before comparison, or left indeterminate; it
   does not report a bare pass.  Both structures are designed to be
   registered as Signed Statements on a Transparency Service as
   described in the SCITT architecture.  This document defines evidence
   payloads; it does not define a new receipt format, a new transparency
   mechanism, or a new signature format.
- **draft-wallace-aipref-grant-binding-02** (new-draft, score 7, verifiable_claims) [none]: [A Verifiable-Credential Binding for AI Usage Preferences: Expressing Grants that Lift AIPREF Preferences](https://datatracker.ietf.org/doc/draft-wallace-aipref-grant-binding/) — The AI Preferences (AIPREF) vocabulary lets those with rights in a
   digital asset express preferences -- for example, that training of AI
   models is disallowed -- about how automated systems process that
   asset.  Such a preference expresses a reservation.  It does not, by
   itself, provide a verifiable, revocable record of a specific grant
   that lifts a preference for a specific party.

   This document describes that gap and proposes a candidate mechanism:
   a cryptographically signed, offline-verifiable credential that
   expresses a grant referencing an AIPREF usage category and a specific
   asset, that any party can verify without contacting the grantor, and
   that the grantor can revoke.  It is intended as a starting point for
   discussion, not as a finished specification.

   The mechanism is preference-general.  Training is used throughout as
   the worked example because it is the reservation most widely
   discussed, but nothing in the construction is specific to it: the
   credential binds whichever usage category was reserved to a named
   party, and the same procedure applies to any other category the
   vocabulary expresses.  What the mechanism establishes is that a grant
   exists, is authentic, is unrevoked, and was in force at a stated
   time.  It does not adjudicate whether the grantor had standing to
   grant, and it is not an enforcement or access-control mechanism.
- **draft-wolfe-faf-agent-01** (new-draft, score 7, core_identity) [none]: [FAFA: A Declarative Agent Capability Format](https://datatracker.ietf.org/doc/draft-wolfe-faf-agent/) — This document specifies the FAF Agent Format (.fafa): a declarative,
   YAML-based format for an agent's identity, the capabilities it
   exposes, and the endpoints through which it is reached.  A .fafa
   document describes an agent; it never instructs one.

   .fafa (application/vnd.fafa+yaml, IANA-registered June 2026 in the
   vendor tree) is the agent member of the FAF family, alongside .faf
   (project context) and .fafm (agent memory).  It functions as a
   portable passport that answers four questions: who the agent is, what
   it may do, where it is reached, and what it must never do.  Protocol-
   native cards (for example A2A Agent Cards and MCP Server Cards)
   remain useful wire formats; repository instruction files such as
   AGENTS.md remain the ops briefing; .fafa complements them as a house-
   neutral source of truth that can be projected into those formats; it
   does not replace them.

   This document documents the existing IANA vendor-tree registration.
   No standards-tree registration is requested.  A companion white
   paper, "Why Agents Need a Passport," provides the production
   rationale and lifecycle framing.

## Monitor

- **draft-ietf-ippm-encrypted-pdmv2-16** (new-draft, score 6, authorization) [ippm]: [IPv6 Performance and Diagnostic Metrics Version 2 (PDMv2) Destination Option](https://datatracker.ietf.org/doc/draft-ietf-ippm-encrypted-pdmv2/) — RFC 8250 defines an IPv6 Destination Option that carries Performance
   and Diagnostic Metrics (PDM) such as sequence numbers and timing
   information.  While useful for measurement and troubleshooting,
   clear-text PDM data may expose operational characteristics of
   endpoints and networks.

   This document defines PDMv2, a revised version of PDM that introduces
   a registration-based security model.  Instead of specifying
   cryptographic algorithms or inline key negotiation, PDMv2 relies on a
   prior registration process to authenticate entities, authorize
   participation, and establish shared secrets.  These secrets are then
   used by endpoints and authorized analyzers to protect and interpret
   PDMv2 data according to local policy.

   This document specifies the PDMv2 semantics, header structure, and
   operational model.  The selection of specific cryptographic
   algorithms and key derivation functions, and the definition of any
   cipher-negotiation mechanism, are outside the scope of this document.
- **draft-ietf-oauth-rfc8725bis-10** (new-draft, score 6, core_identity) [oauth]: [JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc8725bis/) — JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security
   tokens that contain a set of claims that can be signed and/or
   encrypted.  JWTs are being widely used and deployed as a simple
   security token format in numerous protocols and applications, both in
   the area of digital identity and in other application areas.  This
   Best Current Practices (BCP) specification updates RFC 7519 to
   provide actionable guidance leading to secure implementation and
   deployment of JWTs.

   This BCP specification furthermore obsoletes RFC 8725 to provide
   additional actionable guidance covering threats and attacks that have
   been discovered since RFC 8725 was published.
- **draft-rajappa-httpbis-connection-contamination-05** (new-draft, score 6, core_identity) [none]: [Mitigating HTTP/3 Connection Contamination in Multi-Tenant and CDN-Fronted Deployments](https://datatracker.ietf.org/doc/draft-rajappa-httpbis-connection-contamination/) — HTTP/3 [RFC9114] clients commonly reuse ("coalesce") an existing QUIC
   [RFC9000] connection for requests to a second origin when the TLS
   certificate presented on that connection is also valid for the second
   origin, even though the two origins may route to entirely different
   backends.  This document describes "connection contamination," a
   class of security exposure that arises when a routing layer --
   reverse proxy, load balancer, or CDN edge -- determines backend
   routing using a signal established at connection setup rather than
   re-validated per request.  Under that condition, a coalesced
   connection can be used to reach an unintended backend origin,
   potentially enabling cross-tenant data leakage, authentication
   bypass, and response-queue interference analogous to HTTP request
   smuggling.

   This document defines the underlying mechanism, characterizes the
   attacker model, distinguishes connection contamination from related
   QUIC exposures, and provides normative operational guidance for
   implementers and operators of HTTP/3-terminating infrastructure.
- **draft-ross-mercurius-05** (new-draft, score 6, adjacent_watchlist) [none]: [Mercurius Window System (MWS)](https://datatracker.ietf.org/doc/draft-ross-mercurius/) — The Mercurius Window System (MWS) is a zero-trust network-native,
   server-side rendering system that enables graphical sessions to
   be accessed remotely with explicit semantics for Session, Window,
   and rendering state. MWS allows a user to interact with a
   workstation from untrusted or resource-constrained portal devices
   (thin clients or laptops acting as Mercurius terminals) while
   keeping authoritative application, GPU, and compositor state on
   the workstation. The protocol defines a zero-trust portal model, a
   structured Session and Window architecture, and a multi-stream SCTP
   transport profile. It defines distinct protocol planes for control,
   rendering, input, video, and audio. Some payload encodings remain
   subject to refinement in later revisions of this Internet-Draft.
- **draft-hillier-coverage-attestation-00** (new-draft, score 5, trust_infrastructure) [none]: [The Coverage Attestation Profile (CAP-1)](https://datatracker.ietf.org/doc/draft-hillier-coverage-attestation/) — A report can be complete and still silent about its own scope.  A
   statement that something was not observed is routinely recorded in a
   form that reads as a claim about the world, when what was established
   was a claim about a bounded population examined to a stated depth.
   Nothing in the record distinguishes the two, and no relying party can
   recover the difference after the fact.

   This document specifies the Coverage Attestation Profile, CAP-1: a
   tool-agnostic vocabulary for stating what an examination examined,
   what it did not, and why.  A conforming document declares one or more
   populations, a denominator for each whose basis is itself declared,
   and an individual accounting for every unit that was not examined,
   drawn from a closed set of dispositions.  A remainder that reconciles
   only by arithmetic is refused.

   The construct is not novel outside this application.  Coverage
   accounting with a declared denominator is settled practice in
   configuration assessment and in vulnerability scanning, and this
   document states that relationship in Section 1.2 before making any
   claim of its own.
- **draft-meunier-webbotauth-httpsig-protocol-02** (new-draft, score 5, core_identity) [none]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-zhao-a2a-webfinger-00** (new-draft, score 5, core_identity) [none]: [A WebFinger Profile for Agent2Agent (A2A) Agent Identity Resolution](https://datatracker.ietf.org/doc/draft-zhao-a2a-webfinger/) — The Agent2Agent (A2A) protocol retrieves an agent's self-description
   (the Agent Card) from a fixed well-known URI, which resolves exactly
   one agent per origin and presumes the client already holds a URL.
   This document profiles WebFinger for A2A: an agent is named by an
   "acct" URI (agent@domain), and resolution of that name over WebFinger
   yields a link to the Agent Card of the endpoint that serves the agent
   -- the agent's own endpoint, or a gateway fronting it.  The profile
   introduces no new link relation, media type, or registry: it composes
   three deployed standards and states how they fit.
- **draft-das-execution-finality-ai-interoperability-00** (new-draft, score 4, adjacent_watchlist) [none]: [Breaking the Apple-Siri EU DMA Deadlock Without Sacrificing Privacy or Security](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — The Apple-Siri interoperability debate under the EU Digital Markets Act
exposes a difficult technical question: how can third-party AI assistants gain meaningful
access to device functions without forcing the platform to surrender privacy, security, or control over consequential actions?     This paper proposes an execution-finality architecture in which an AI assistant may request an action, but the request itself has no power to make
that action effective. Each consequential operation remains in a Non-Effective State
until protected infrastructure validates the requester, resource, destination, user intent where required, freshness, revocation state, and policy conditions.     Only then is narrowly scoped, non-bearer execution authority created. At the Finality Sink - the first boundary where the
action can become externally effective - the system independently verifies that the real
operation still matches what was authorized. Any mismatch, replay, substitution, expiry,
or revocation causes fail-closed denial. The key principle is simple: 
   Interoperability should grant participation, not uncontrolled execution
authority. 
   This offers a possible technical path through the DMA deadlock: third-party
assistants could participate meaningfully without requiring broad reusable
permissions, while platforms retain strong privacy, security, revocation,
anti-replay, and final-effect controls.  Execution-Finality Governance therefore
reframes the problem from closed versus open to open participation with bounded,
verifiable authority.
- **draft-woodcock-faltstrom-external-registry-rrtypes-00** (new-draft, score 4, verifiable_claims) [none]: [External-Registry DNS Resource Record Types: UNECE and ISO](https://datatracker.ietf.org/doc/draft-woodcock-faltstrom-external-registry-rrtypes/) — This document defines two DNS resource record types, UNECE and ISO,
   which convey numeric values paired with codes drawn from registries
   maintained by external standards organizations: the United Nations
   Economic Commission for Europe (UNECE) and the International
   Organization for Standardization.  Neither proposed RRTYPE duplicates
   the external registries into IANA registries; each carries codes
   verbatim and uses the semantics defined by the external maintainer.
   The document specifies presentation and wire formats for both types,
   requests the assignment of two decimal RRTYPE identifiers under the
   Expert Review process of BCP 42, and suggests a common design pattern
   that may serve as a model for future RRTYPEs seeking to make external
   registries usable from the DNS without duplication.

## Adjacent / watchlist

- **draft-gondwana-welcome-to-the-ietf-00** (new-draft, score 3, agent_identity) [none]: [Welcome to the IETF](https://datatracker.ietf.org/doc/draft-gondwana-welcome-to-the-ietf/) — The IETF has produced many documents to describe what it is and how
   it works -- this is one of them.

   In an age in which agentic tooling makes it trivially easy to produce
   large amounts of text, this document explains to both humans and
   agents what the IETF is about, how to succeed at the IETF, and some
   common pitfalls which might reduce the quality of your time here.

   This document does not describe the specific arcane process of how
   documents progress through adoption, improvement, consensus, editing,
   and eventual publication.  Instead, we focus on the people and the
   culture of the IETF and how to succeed at IETFing.
- **draft-ietf-httpbis-connect-tcp-13** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP proxying using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this proxying functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-httpbis-no-vary-search-09** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
- **draft-ietf-idr-rtc-interas-00** (new-draft, score 3, adjacent_watchlist) [idr]: [Inter Domain considerations for Constrained Route distribution](https://datatracker.ietf.org/doc/draft-ietf-idr-rtc-interas/) — RFC4684 defines Multi-Protocol BGP (MP-BGP) procedures that allow BGP
   speakers to exchange Route Target reachability information in order
   to limit the propagation of Virtual Private Networks (VPN) Network
   Layer Reachability Information (NLRI).

   RFC4684 addresses both intra domain and inter domain distributions.
   Operational deployment experience shows that the current distribution
   model defined in RFC4684 for inter domain may cause some issue in
   specific scenarios.

   This document proposes alternate route distribution rules for inter
   domain in order to address these specific scenarios.
- **draft-ietf-idr-sr-policy-seglist-id-13** (new-draft, score 3, core_identity) [idr]: [BGP SR Policy Extensions for Segment List Identifier](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-seglist-id/) — Segment Routing (SR) is a source routing paradigm that explicitly
   indicates the forwarding path for packets at the ingress node.  An SR
   Policy is a set of candidate paths, each consisting of one or more
   segment lists.  This document defines extensions to BGP SR Policy to
   specify the identifier of a segment list.
- **draft-ietf-ipsecme-ikev2-pqc-auth-12** (new-draft, score 3, core_identity) [ipsecme]: [Signature Authentication in the Internet Key Exchange Version 2 (IKEv2) using PQC](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-pqc-auth/) — Signature-based authentication methods are utilized in the Internet
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
- **draft-ietf-ivy-network-inventory-topology-09** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Network Data Model for Inventory Topology Mapping](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-topology/) — This document defines a YANG data model that extends the network
   topology data model (RFC 8345) to map network topologies with
   inventories.  The data model introduces the "inventory-topology"
   network type and augmentations for physical entity mappings and
   capabilities, which may be used by any overlay network topology for
   service provisioning validation, network maintenance, and capacity
   planning.
- **draft-ietf-masque-connect-ethernet-14** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document describes how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-netconf-yp-transport-capabilities-07** (new-draft, score 3, adjacent_watchlist) [netconf]: [YANG Notification Transport Capabilities](https://datatracker.ietf.org/doc/draft-ietf-netconf-yp-transport-capabilities/) — This document specifies a YANG module for discovering transport
   capabilities for YANG notifications.  The module augments the YANG
   notifications capabilities model with capabilities for the
   notification transport protocol, transport encoding, and transport
   encryption.  The capabilities enable a client to determine the
   notification transport options supported by a NETCONF or RESTCONF
   server at runtime or at implementation time using the YANG instance
   data file format.
- **draft-ietf-nmop-network-incident-yang-14** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG Module for the network incident
   lifecycle management.  This YANG module is meant to provide a
   standard way to report, diagnose, and help reduce troubleshooting
   tickets and resolve network incidents for the sake of network service
   health and probable root cause analysis.
- **draft-ietf-opsawg-collected-data-manifest-14** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push, to
   continuously stream information, including both counters and state
   information.  This document describes the metadata that ensure that
   the collected data can be interpreted correctly.  This document
   specifies the Data Manifest, composed of two YANG data models (the
   Platform Manifest and the non-normative Data Collection Manifest).
   These YANG modules are specified at the network level (e.g., network
   controllers) to provide a model that encompasses several network
   platforms.  The Data Manifest must be streamed and stored along with
   the data, up to the collection and analytics systems to keep the
   collected data fully exploitable by the data scientists and relevant
   tools.  Additionally, this document specifies an augmentation of the
   YANG-Push model to include the actual collection period, in case it
   differs from the configured collection period.
- **draft-ietf-opsawg-ipfix-path-segment-04** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 paths identification.
- **draft-intra-handshake-fail-09** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
   (https://www.cve.org/CVERecord?id=CVE-2026-33697) and EUVD-2026-16488
   (https://euvd.enisa.europa.eu/enisa/EUVD-2026-16488), which is
   substantial technical evidence of how *intra*-handshake attestation
   fails in practice, even _without physical access_. Moreover, since
   continuous attestation is generally required, *intra*-handshake
   attestation adds *unnecessary complexity*. The results are backed by
   the research [Intra-handshake.fail] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art tool, ProVerif, under
   Apache-2.0 license for reproducibility, and have been acknowledged by
   the relevant stakeholders.
- **draft-irtf-cfrg-fiat-shamir-03** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Fiat-Shamir Transformation](https://datatracker.ietf.org/doc/draft-irtf-cfrg-fiat-shamir/) — This document describes the Fiat-Shamir transformation, which allows
   making a public-coin protocol non-interactive by means of a
   cryptographic hash function.

   It specifies how the hash function is employed, how prover messages
   are encoded as hash-function input, and how verifier messages are
   decoded from the hash function's output, as well as the serialization
   and deserialization of the non-interactive argument string.
- **draft-irtf-cfrg-sigma-protocols-03** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Sigma Proofs for Linear Relations](https://datatracker.ietf.org/doc/draft-irtf-cfrg-sigma-protocols/) — This document describes Sigma Protocols for proving knowledge of
   preimages of linear maps in prime-order elliptic curve groups.  These
   are sometimes also called _Maurer Proofs_, or _proofs of knowledge of
   a preimage of a group homomorphism_.

   Examples include zero-knowledge proofs for discrete logarithm
   relations, ElGamal encryptions, Pedersen commitments, and range
   proofs.
- **draft-reddy-tls-composite-mldsa-11** (new-draft, score 3, core_identity) [none]: [Use of Composite ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-reddy-tls-composite-mldsa/) — Compositing the post-quantum ML-DSA signature with traditional
   signature algorithms provides protection against potential breaks or
   critical bugs in ML-DSA or the ML-DSA implementation.  This document
   specifies how such a composite signature can be formed using ML-DSA
   with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide
   authentication in TLS 1.3, including use in certificates.
- **draft-schrock-kintzele-grid-curtailment-00** (new-draft, score 3, authorization) [none]: [GRACE: Evidence-Bound Grid Curtailment Admission, Observation, and Single-Use Settlement](https://datatracker.ietf.org/doc/draft-schrock-kintzele-grid-curtailment/) — This document defines GRACE, an application profile for one bounded
   grid.curtailment action.  The profile binds an exact action to a
   finite participation envelope, distinct human approvals when
   required, one-attempt executor admission, an authenticated actuator
   acknowledgment, separately authenticated meter observations, an
   Action State Signed Statement, and one-time admission to a settlement
   effect.  Missing or ambiguous post-invocation evidence is preserved
   as indeterminate and cannot authorize blind retry.

   GRACE verifies signed inputs and deterministic computations.  It does
   not establish physical meter truth, baseline correctness, tariff
   eligibility, actual payment, complete mediation, or a physical grid
   deployment.  An optional hybrid artifact-signature profile combines
   Ed25519 with ML-DSA-65 and requires both signatures to verify.
- **draft-sgcp-state-graph-cryptographic-protocol-01** (new-draft, score 3, core_identity) [none]: [State Graph Cryptographic Protocol (SGCP)](https://datatracker.ietf.org/doc/draft-sgcp-state-graph-cryptographic-protocol/) — This document specifies the State Graph Cryptographic Protocol
   (SGCP), a communication-security framework in which a client and
   server establish a cryptographically protected session and maintain
   a synchronized state graph throughout the lifetime of the
   communication session.

   SGCP combines device identity, port context, socket context,
   session identity, ECDH-based shared-secret establishment,
   cryptographic key derivation, epochs, packet sequence numbers,
   authenticated state transitions, state-dependent packet
   transformation, replay protection, continuous context verification,
   controlled reauthentication, and session recovery.

   The central principle is that both endpoints independently derive
   the same cryptographic state from a common authenticated session
   secret and deterministic state information.  The state graph
   defines which communication states are valid and which transitions
   are permitted.

   This document also illustrates the protocol with a worked example
   of a full-duplex binary media file transfer (an MP3 audio file)
   showing the complete packet-level exchange.
- **draft-srivastava-stir-sip-request-context-00** (new-draft, score 3, core_identity) [none]: [SIP Request Context Binding for STIR Connected Identity](https://datatracker.ietf.org/doc/draft-srivastava-stir-sip-request-context/) — This document updates RFC 9970.

   RFC 9970 recommends STIR PASSporTs on re-INVITE and BYE requests
   after connected identity has been established in a SIP dialog, and
   states that this prevents spoofed mid-dialog or dialog-terminating
   events.  The baseline PASSporT construction used by RFC 8224 does not
   bind the SIP request method, CSeq number, Call-ID, or dialog tags.
   Consequently, a valid PASSporT can remain valid when a fresh signed
   in-dialog request is transformed into a different SIP request whose
   authenticated identity fields are unchanged.

   This document defines the "sipctx" PASSporT type.  It binds the SIP
   request method and dialog/sequence context to the PASSporT.
   Implementations relying on PASSporT validation for mid-dialog request
   authenticity use this context binding as specified in this document.
- **draft-yoshikawa-sidrops-pqc-rpki-02** (new-draft, score 3, authorization) [none]: [Post-Quantum Signature Experiments and Migration Considerations for the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-yoshikawa-sidrops-pqc-rpki/) — This document reports experiments with post-quantum signature
   algorithms and analyzes migration approaches for the Resource Public
   Key Infrastructure (RPKI).  The experiments compare classical, post-
   quantum, and composite signature candidates; generate and validate
   RPKI-profiled certificate, CRL, manifest, and ROA test objects;
   evaluate Parallel Publication and Mixed Tree migration as distinct
   migration structures; and evaluate the effect of larger objects on
   rsync, RRDP, and Erik Synchronization.  The results identify
   implementation, interoperability, repository-distribution, and
   operational questions that need to be resolved before a production
   algorithm profile or transition procedure can be specified.  This
   document is informational.  It does not update RFC 7935 or RFC 6916,
   define a new RPKI algorithm profile, or authorize the use of the
   evaluated algorithms or Mixed Tree migration in the production RPKI.
- **draft-hu-6man-ipv6-flowlabel-load-balancing-rdma-02** (new-draft, score 2, ignored_after_review) [none]: [A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) — This document proposes a method for achieving flow-level load
   balancing in RoCEv2 (RDMA over Converged Ethernet version 2)
   networks.  Traditional per-flow load balancing based on the 5-tuple
   cannot distinguish between different RDMA sessions that share the
   same 5-tuple.  This causes "elephant flows" to be hashed to the same
   path, leading to network congestion.  This method resolves this issue
   by having the ingress network device (e.g., a top-of-rack switch or
   router) parse the QP (Queue Pair) information from the IB BTH (Base
   Transport Header) and IB DETH (Datagram Extended Transport Header)
   headers of the RoCEv2 packet.  By combining this with portions of the
   IPv6 source and destination addresses as an entropy source, a CRC32
   hash algorithm generates a 20-bit value, which is then written into
   the Flow Label field of the IPv6 header.  Network devices can
   subsequently use the updated "5-tuple + Flow Label" for more granular
   flow-level load balancing, thereby effectively improving transmission
   efficiency in high-performance networks such as AI computing.
- **draft-ietf-aipref-attach-05** (new-draft, score 2, ignored_after_review) [aipref]: [Associating AI Usage Preferences with Content in HTTP](https://datatracker.ietf.org/doc/draft-ietf-aipref-attach/) — Methods are defined for associating usage preferences with content
   that is obtained using the HTTP protocol.  This document defines
   attachment methods using the Robots Exclusion Protocol and HTTP
   header fields.

   This document updates RFC 9309 to allow for the inclusion of usage
   preferences.
- **draft-ietf-aipref-vocab-07** (new-draft, score 2, ignored_after_review) [aipref]: [A Vocabulary For Expressing AI Usage Preferences](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/) — This document defines a vocabulary for expressing preferences
   regarding how digital assets are used by automated processing
   systems.  This vocabulary allows for the declaration of restrictions
   or permissions for use of digital assets by such systems.
- **draft-okutomi-agent-human-interaction-00** (new-draft, score 2, ignored_after_review) [none]: [An Agent-Human Interaction Overlay for Task Protocols](https://datatracker.ietf.org/doc/draft-okutomi-agent-human-interaction/) — This intentionally incomplete design note defines an overlay for
   Human and Agent participation in existing Task and Action protocols.
   It separates the responsible Participant from the authenticated
   Actor, records Human interactions, excludes Humans from Agent
   discovery, and binds each change to its authorized request.  It
   defines neither a wire protocol nor Humans as Agents.
- **draft-wen-agent-workload-scheduling-00** (new-draft, score 2, ignored_after_review) [none]: [Dynamic Scheduling of Update and Query Workloads in Agent Service Discovery Nodes](https://datatracker.ietf.org/doc/draft-wen-agent-workload-scheduling/) — Agent service discovery nodes may need to process two classes of
   workloads concurrently: Agent registration and dynamic state updates,
   and discovery queries issued by other Agents.  These workloads
   compete for shared processing resources but have different
   performance objectives.  Delayed state updates can cause a service
   discovery node to rely on stale workload, availability, or QoS
   information, while delayed queries can increase Agent-selection
   latency and the completion time of multi-Agent tasks.

   This document describes a scheduling framework for coordinating
   update and query processing in a multi-Worker Agent service discovery
   node.  To estimate the demand of each workload, the framework
   considers total queued work, waiting time, deadline pressure, recent
   load, state freshness, and, for updates, the expected freshness gain
   from processing a pending update.  These estimates determine how
   Worker capacity is divided between the two queues, which remain
   active in parallel.

   The framework also incorporates update merging and deduplication,
   freshness-aware dependencies between state updates and discovery
   queries, hysteresis-based resource reallocation, minimum resource
   holding time, and intra-queue task prioritization.  Different
   deployment conditions can be accommodated by adjusting the
   corresponding weights and thresholds without changing the scheduling
   structure itself.
- **draft-xu-idr-fare-08** (new-draft, score 2, adjacent_watchlist) [idr]: [Fully Adaptive Routing Ethernet using BGP](https://datatracker.ietf.org/doc/draft-xu-idr-fare/) — Large language models (LLMs) like ChatGPT have become increasingly
   popular in recent years due to their impressive performance in
   various natural language processing tasks.  These models are built by
   training deep neural networks on massive amounts of text data, as
   well as visual and video data, and often consist of billions or even
   trillions of parameters.  However, the training process for these
   models can be extremely resource-intensive, requiring the deployment
   of thousands or even tens of thousands of GPUs in a single AI
   training cluster.  Therefore, three-stage or even five-stage CLOS
   networks are commonly adopted for AI networks.  The non-blocking
   nature of the network becomes increasingly critical for large-scale
   AI model training.  Therefore, adaptive routing is necessary to
   dynamically distribute traffic to the same destination across
   multiple equal-cost paths, based on network capacity information
   along those paths.

## Ignored after review

- **draft-anjum-nmop-anomaly-detection-evaluation-00** (new-draft, score 0, ignored_after_review) [none]: [Evaluation Methodology for Machine-Learning-Based Network Anomaly Detection](https://datatracker.ietf.org/doc/draft-anjum-nmop-anomaly-detection-evaluation/) — The Network Management Operations (NMOP) working group has adopted
   documents describing an architecture, an operational lifecycle, and a
   semantics for network anomaly detection.  Those documents direct
   implementers to minimize false positives and false negatives, but do
   not define how the accuracy of an anomaly detection implementation is
   to be measured, compared, or tracked over time.  This document
   describes an evaluation methodology for machine-learning-based
   anomaly detection systems operating on network and infrastructure
   telemetry: the metrics to report and their known failure modes, a
   benchmarking procedure based on controlled fault injection and
   replay, and the properties a benchmark dataset needs in order to
   support reproducible, comparable evaluation.  The methodology is
   informational and complements the adopted NMOP anomaly-detection
   documents.
- **draft-antony-ipsecme-muse-00** (new-draft, score 0, ignored_after_review) [none]: [Multiple Ephemeral UDP Source Ports for ESP in UDP Encapsulation (MUSE)](https://datatracker.ietf.org/doc/draft-antony-ipsecme-muse/) — This document specifies a mechanism to improve network path
   distribution and host receive-queue load distribution for IPsec
   traffic using ESP in UDP encapsulation [RFC3948].  Using the per-
   resource Child SA mechanism of [RFC9611], peers negotiate multiple
   Child SAs each bound to a distinct UDP source port.  The resulting
   entropy in the UDP source port enables network devices to distribute
   per-resource traffic across distinct paths (equal-cost multi-path,
   ECMP) and lets the host NIC steer each per-resource flow to a
   distinct receive queue via receive-side scaling (RSS), supporting
   efficient per-CPU IPsec processing.  This document specifies the
   IKEv2 negotiation, NAT traversal behavior, and operational
   requirements for this mechanism.
- **draft-becker-cnsa2-smime-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Secure/Multipurpose Internet Mail Extensions (S/MIME)](https://datatracker.ietf.org/doc/draft-becker-cnsa2-smime-profile/) — This document defines a base profile of S/MIME for use with the US
   Commercial National Security Algorithm (CNSA) 2.0 Suite, a
   cybersecurity advisory published by the United States Government
   which outlines quantum-resistant cryptographic algorithm policy for
   US national security applications.

   This profile applies to the capabilities, configuration, and
   operation of all components of US National Security Systems that
   employ S/MIME.  It is also appropriate for all other US Government
   systems that process high-value information.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This profile is made publicly available
   for use by developers and operators of these and any other system
   deployments.
- **draft-cx-mpls-mna-inband-pm-09** (new-draft, score 0, ignored_after_review) [none]: [MNA for Performance Measurement with Alternate Marking Method](https://datatracker.ietf.org/doc/draft-cx-mpls-mna-inband-pm/) — MPLS Network Action (MNA) is used to indicate action for Label
   Switched Paths (LSPs) and/or MPLS packets, and to transfer data
   needed for the action.

   This document defines MNA encodings for MPLS performance measurement
   with alternate marking method, which performs flow-based packet loss,
   delay, and jitter measurements on MPLS live traffic.
- **draft-eastlake-rfc9231bis-xmlsec-uris-09** (new-draft, score 0, ignored_after_review) [none]: [Additional XML Security Uniform Resource Identifiers (URIs)](https://datatracker.ietf.org/doc/draft-eastlake-rfc9231bis-xmlsec-uris/) — This document expands and corrects the IANA "XML Security URIs"
   registry that lists URIs intended for use with XML digital
   signatures, encryption, canonicalization, and key management.  These
   URIs identify algorithms and types of information.  This document
   obsoletes RFC 9231.
- **draft-farrokhi-dnsop-ecs-opt-in-00** (new-draft, score 0, ignored_after_review) [none]: [Client Opt-In Signaling for EDNS Client Subnet](https://datatracker.ietf.org/doc/draft-farrokhi-dnsop-ecs-opt-in/) — EDNS Client Subnet (ECS) lets a recursive resolver send part of a
   client's network address to authoritative servers, which tailor their
   answers to it.  A resolver's configuration decides whether it does
   so, for every client that sends no ECS option of its own.  RFC 7871
   lets a client opt out.  Asking instead for a shorter prefix requires
   the client to supply the address those bits are taken from, which a
   client behind a NAT or a VPN does not know.

   This document defines an opt-in.  A client includes an EDNS(0) option
   in a query to ask the resolver to forward its address information,
   and can use that option to limit how many address bits the resolver
   forwards.  A resolver implementing this document forwards nothing for
   a client that does not send the option, and one that does not
   implement it ignores the option.  One resolver address can then serve
   clients that want tailored answers and those that want their
   addresses withheld.
- **draft-gaikwad-ba64-00** (new-draft, score 0, ignored_after_review) [none]: [ba64: A Binary-to-Text Encoding That Is Never Larger Than Base64](https://datatracker.ietf.org/doc/draft-gaikwad-ba64/) — ba64 is a text encoding for binary data that is never larger than
   standard base64.  An encoder races DEFLATE compression against plain
   base64 and emits whichever final text is shorter.  Compressed output
   is marked by a leading "=" character, which is inside the base64
   alphabet, so it survives every base64-safe channel, yet can never
   begin a valid base64 string, so the two forms are unambiguous.  A
   CRC-32 over the decoded bytes guarantees that a ba64 decoder never
   silently returns wrong data.  The plain form is byte-identical to
   base64, so ba64 decoders are a drop-in replacement wherever base64 is
   read today.  An optional padding method decouples the emitted length
   from the compressibility of the input.
- **draft-gerke-publication-process-reform-04** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.
- **draft-ietf-6man-icmpv6-ioam-conf-state-11** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 Query for Enabled In-situ OAM Capabilities](https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-ioam-conf-state/) — This document describes the application of the mechanism of
   discovering In-situ OAM (IOAM) capabilities, described in RFC 9359
   "Echo Request/Reply for Enabled In Situ OAM (IOAM) Capabilities", in
   IPv6 networks.  IPv6 Node IOAM Query functionality uses the ICMPv6
   Query messages, allowing the IOAM encapsulating node to discover the
   enabled IOAM capabilities of each IOAM transit and IOAM decapsulating
   node.
- **draft-ietf-avtcore-rtp-jpegxs-3ed-04** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for ISO/IEC 21122 (JPEG XS)](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-jpegxs-3ed/) — This document specifies a Real-Time Transport Protocol (RTP) payload
   format for transport of a video signal encoded with JPEG XS (ISO/IEC
   21122).  JPEG XS is a low-latency and low-complexity video coding
   system.  Employing this format allows achieving encoding-decoding
   latencies confined to a fraction of a video frame.

   This document is a necessary revision of RFC 9134 to incorporate
   support for new features introduced in the third edition of JPEG XS.
   Most notably, it contains the necessary provisions to support the TDC
   coding mode.  This document obsoletes RFC 9134; however, the revised
   payload format is designed to ensure that existing compliant
   implementations of RFC 9134 remain valid under the updated
   specification.  Additionally, this document consolidates the errata
   of RFC 9134 and includes improvements and clarifications to its
   implementers and users.
- **draft-ietf-bess-evpn-bfd-15** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Network Layer Fault Management](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-bfd/) — This document specifies proactive, in-band Network Layer OAM (RFC
   9062) mechanisms to detect loss of continuity faults that affect
   unicast and multi-destination paths (used by Broadcast, Unknown
   Unicast, and Multicast traffic) in an Ethernet VPN (EVPN, RFC
   7432bis) network.  The mechanisms specified in this document use the
   widely adopted Bidirectional Forwarding Detection (RFC 5880)
   protocol.
- **draft-ietf-bfd-rfc5882-bis-02** (new-draft, score 0, ignored_after_review) [bfd]: [Generic Application of Bidirectional Forwarding Detection (BFD)](https://datatracker.ietf.org/doc/draft-ietf-bfd-rfc5882-bis/) — This document describes the generic application of the Bidirectional
   Forwarding Detection (BFD) protocol.

   This document obsoletes RFC 5882.
- **draft-ietf-bfd-rfc5883-bis-02** (new-draft, score 0, ignored_after_review) [bfd]: [Bidirectional Forwarding Detection (BFD) for Multihop Paths](https://datatracker.ietf.org/doc/draft-ietf-bfd-rfc5883-bis/) — This document describes the use of the Bidirectional Forwarding
   Detection (BFD) protocol over multihop paths, including
   unidirectional links.

   This document obsoletes RFC 5883.
- **draft-ietf-bfd-rfc5884-bis-01** (new-draft, score 0, ignored_after_review) [bfd]: [Bidirectional Forwarding Detection (BFD) for MPLS Label Switched Paths (LSPs)](https://datatracker.ietf.org/doc/draft-ietf-bfd-rfc5884-bis/) — One desirable application of Bidirectional Forwarding Detection (BFD)
   is to detect a Multiprotocol Label Switching (MPLS) Label Switched
   Path (LSP) data plane failure.  LSP Ping is an existing mechanism for
   detecting MPLS data plane failures and for verifying the MPLS LSP
   data plane against the control plane.  BFD can be used for the
   former, but not for the latter.  However, the control plane
   processing required for BFD Control packets is relatively smaller
   than the processing required for LSP Ping messages.  A combination of
   LSP Ping and BFD can be used to provide faster data plane failure
   detection and/or make it possible to provide such detection on a
   greater number of LSPs.  This document describes the applicability of
   BFD in relation to LSP Ping for this application.  It also describes
   procedures for using BFD in this environment.  This document
   obsoletes RFC5884 and RFC7726.
- **draft-ietf-bier-bierin6-14** (new-draft, score 0, ignored_after_review) [bier]: [Supporting BIER in IPv6 Networks (BIERin6)](https://datatracker.ietf.org/doc/draft-ietf-bier-bierin6/) — BIER is a multicast forwarding architecture that does not require
   per-flow state inside the network yet still provides optimal
   replication.  This document describes how the existing BIER
   encapsulation specified in RFC 8296 works in a non-MPLS IPv6 network,
   which is referred to as BIERin6.  Specifically, like in an IPv4
   network, BIER can work over L2 links directly or over tunnels.  In
   case of IPv6 tunneling, a new IP "Next Header" type is to be assigned
   for BIER.
- **draft-ietf-ccwg-ratelimited-increase-10** (new-draft, score 0, ignored_after_review) [ccwg]: [Increase of the Congestion Window when the Sender Is Rate-Limited](https://datatracker.ietf.org/doc/draft-ietf-ccwg-ratelimited-increase/) — This document specifies how transport protocols increase their
   congestion window when the sender is rate-limited, and updates RFCs
   4341, 5681, 9002, 9260, and 9438.  Such a limitation can be caused by
   the sending application not supplying data or by receiver flow
   control.
- **draft-ietf-dmm-tn-aware-mobility-32** (new-draft, score 0, ignored_after_review) [dmm]: [Mapping 5G slice to Transport Network slice with UDP Source Ports](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-dnssd-uld-00** (new-draft, score 0, ignored_after_review) [dnssd]: [Providing Local Unicast DNS-SD Service on Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-dnssd-uld/) — DNS Service Discovery provides several mechanisms whereby hosts can
   discover and advertise services on an IP network.  Such discovery can
   be done using Multicast DNS (mDNS) or DNS, and advertising can be
   done with DNS-SD Service Registration Protocol (SRP) or mDNS.  This
   document defines Unicast Local Discovery (ULD), a service that
   combines an SRP registrar, a Discovery Proxy, and an Advertising
   Proxy.  Hosts can use a ULD server to advertise and discover services
   on the local link entirely via unicast SRP and DNS while remaining
   interoperable with hosts that use mDNS.
- **draft-ietf-dtn-eid-pattern-10** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol Endpoint ID Patterns](https://datatracker.ietf.org/doc/draft-ietf-dtn-eid-pattern/) — This document extends the Bundle Protocol Endpoint ID (EID) concept
   into an EID Pattern, which is used to categorize any EID as matching
   a specific pattern or not.  EID Patterns are suitable for expressing
   configuration, for being used on-the-wire by protocols, and for being
   easily understandable by a layperson.  EID Patterns include scheme-
   specific optimizations for expressing set membership and each scheme
   pattern includes text and binary encoding forms; the pattern for the
   "ipn" EID scheme being designed to be highly compressible in its
   binary form.  This document also defines a Public Key Infrastructure
   Using X.509 (PKIX) Other Name form to contain an EID Pattern and a
   handling rule to use a pattern to match an EID.
- **draft-ietf-idr-bgp-ls-bgp-only-fabric-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Link-State Extensions for BGP-only Networks](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/) — BGP is used as the only routing protocol in some networks today.  In
   such networks, it is useful to get a detailed topology view similar
   to one available when using link state routing protocols.  This
   document defines extensions to the BGP Link-state (BGP-LS) address-
   family and the procedures for advertisement of topology information
   in a BGP-only network.
- **draft-ietf-idr-bgp-ls-sr-policy-path-segment-11** (new-draft, score 0, ignored_after_review) [idr]: [SR Policies Extensions for Path Segment and Bidirectional Path in BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-path-segment/) — This document specifies the way of collecting configuration and
   states of SR policies carrying Path Segment and bidirectional path
   information by using BPG-LS.  Such information can be used by
   external conponents for many use cases such as performance
   measurement, path re-optimization and end-to-end protection.
- **draft-ietf-idr-bgpls-inter-as-topology-ext-38** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extension for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedure for distributing Border Gateway
   Protocol-Link State (BGP-LS) key parameters for inter-domain links
   between two Autonomous Systems (ASes).  It defines a new type within
   the BGP-LS Network Layer Reachability Information (NLRI) for an
   Inter-AS Link, as well as three new type-length-values (TLVs) for the
   BGP-LS Inter-AS Link descriptor.  These BGP-LS extensions enable
   Software-Defined Networking (SDN) controllers to retrieve network
   topology across Inter-AS environments.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   end-to-end network topology using information provided by the BGP-LS
   protocol.
- **draft-ietf-idr-sr-policy-path-mtu-15** (new-draft, score 0, ignored_after_review) [idr]: [Segment Routing Path MTU in BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-path-mtu/) — Segment Routing is a source routing paradigm that explicitly
   indicates the forwarding path for packets at the ingress node.  An SR
   policy is a set of SR Policy candidate paths consisting of one or
   more segments with the appropriate SR path attributes.  BGP
   distributes each SR Policy candidate path as combination of an prefix
   plus a the BGP Tunnel Encapsulation(Tunnel-Encaps) attribute
   containing an SR Policy Tunnel TLV with information on the SR Policy
   candidate path as a tunnel.  However, the path maximum transmission
   unit (MTU) information for a segment list for SR path is not
   currently passed in the BGP Tunnel-Encaps attribute. . This document
   defines extensions to BGP to distribute path MTU information within
   SR policies.
- **draft-ietf-idr-ts-flowspec-srv6-policy-14** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies extensions to BGP Flow Specification (RFC 8955,
   RFC 8956) to steer matching traffic flows into Segment Routing (SR)
   Policies (RFC 9256).  Specifically, it defines normative protocol
   procedures for combining FlowSpec Network Layer Reachability
   Information (NLRI) (RFC 8955, RFC 8956) with the BGP Prefix-SID
   Attribute (RFC 8669, RFC 9252) and specific BGP Extended Communities
   (RFC 9012) to signal SR-MPLS and SRv6 Policy steering pathways.
- **draft-ietf-lisp-rfc8060bis-05** (new-draft, score 0, ignored_after_review) [lisp]: [LISP Canonical Address Format (LCAF)](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc8060bis/) — This document defines a canonical address format encoding used in
   Locator/ID Separation Protocol (LISP) control messages and in the
   encoding of lookup keys for the LISP Mapping Database System.

   This document obsoletes RFC 8060 and RFC 9306.
- **draft-ietf-lsr-l2-bundle-member-remote-id-06** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  For example,
   when performing topology management and bidirectional path
   computation for TE, it is essential to know the connectivity
   relationships among bundle members.

   This document describes how OSPF and IS-IS would advertise the remote
   interface identifiers for Layer 2 bundle members.  The corresponding
   extension of BGP Link State (BGP-LS) is also specified.
- **draft-ietf-manet-inet-gap-analysis-08** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mpls-stamp-pw-08** (new-draft, score 0, ignored_after_review) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document describes the procedure for encapsulating the Simple
   Two-Way Active Measurement Protocol (STAMP), defined in RFC 8762, and
   its optional extensions defined in RFC 8972, in MPLS networks.  Label
   Switched Paths (LSPs) and Pseudowires (PWs) are used in MPLS networks
   for various services, including Layer 2 and Layer 3 data packets, and
   may use the Control Word (CW).  The procedure for encapsulating STAMP
   test packets with or without the CW and/or an IP/UDP header for LSPs
   and PWs is also described.
- **draft-ietf-netmod-yang-module-filename-15** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Module File Name Convention](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-module-filename/) — This document defines the YANG module file name convention.  The
   convention extends the YANG module file name using revision-date,
   with the YANG semantic version extension.  The YANG semantic version
   extension allows for an informative version to be associated with a
   particular YANG module revision.

   This document updates RFCs 6020, 7950, and 9907.
- **draft-ietf-nfsv4-nfs-acl-04** (new-draft, score 0, ignored_after_review) [nfsv4]: [The Network File System Access Control List Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-nfs-acl/) — This Informational document describes the NFS_ACL protocol.  NFS_ACL
   is a legacy member of the Network File System family of protocols
   that NFS clients use to view and update Access Control Lists stored
   on an NFS version 2 or version 3 server.
- **draft-ietf-nvo3-rfc7348bis-05** (new-draft, score 0, ignored_after_review) [nvo3]: [Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks](https://datatracker.ietf.org/doc/draft-ietf-nvo3-rfc7348bis/) — This document specifies Virtual eXtensible Local Area Network
   (VXLAN), which is used to address the need for overlay networks
   within virtualized data centers accommodating multiple tenants.  The
   scheme and the related protocols can be used in networks for cloud
   service providers and enterprise data centers.  This document
   obsoletes RFC 7348, which documented the deployed VXLAN protocol for
   the benefit of the Internet community, and moves the VXLAN
   specification to the IETF document stream, allowing for the creation
   of extensions to VXLAN that require additions to the VXLAN header and
   their registration with IANA.  The format and processing described
   here are fully compatible with those in RFC7348.
- **draft-ietf-procon-2418bis-04** (new-draft, score 0, ignored_after_review) [procon]: [IETF Working Group Guidelines and Procedures](https://datatracker.ietf.org/doc/draft-ietf-procon-2418bis/) — The Internet Engineering Task Force (IETF) has responsibility for
   developing and reviewing specifications intended as Internet
   Standards.  IETF activities are organized into working groups (WGs).
   This document describes the guidelines and procedures for formation
   and operation of IETF working groups.  It also describes the formal
   relationship between IETF participants WG and the Internet
   Engineering Steering Group (IESG) and the basic duties of IETF
   participants, including WG Chairs, WG participants, and IETF Area
   Directors.

   This document obsoletes RFC2418, and RFC3934.  It also includes the
   changes from RFC7475, and with [_2026bis], obsoletes it.  It also
   includes a summary of the changes implied in RFC7776 and incorporates
   the changes from RFC8717 and RFC9141.
- **draft-ietf-quic-address-discovery-01** (new-draft, score 0, ignored_after_review) [quic]: [QUIC Address Discovery](https://datatracker.ietf.org/doc/draft-ietf-quic-address-discovery/) — Unless they have out-of-band knowledge, QUIC endpoints have no
   information about their network situation.  They neither know their
   external IP address and port, nor do they know if they are directly
   connected to the internet or if they are behind a NAT.  This QUIC
   extension allows nodes to determine their reflexive IP address and
   port for any QUIC path.
- **draft-ietf-regext-ext-registry-epp-10** (new-draft, score 0, ignored_after_review) [regext]: [Extension Registry for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-ietf-regext-ext-registry-epp/) — The Extensible Provisioning Protocol (EPP) includes features to add
   functionality by extending the protocol.  It does not, however,
   describe how those extensions are maintained.  This document
   describes a procedure for the registration and management of
   extensions to EPP, and it specifies a format for an IANA registry to
   record those extensions.  If approved, this document obsoletes RFC
   7451.
- **draft-ietf-scone-protocol-07** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-rpki-erik-protocol-07** (new-draft, score 0, ignored_after_review) [sidrops]: [The Erik Synchronization Protocol for use with the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rpki-erik-protocol/) — This document specifies the Erik Synchronization Protocol for use
   with the Resource Public Key Infrastructure (RPKI).  Erik
   Synchronization can be characterized as a data replication system
   using Merkle trees, a content-addressable naming scheme, concurrency
   control using monotonically increasing sequence numbers, and HTTP
   transport.  The protocol is used to interact with Erik Relays, a new
   intermediary layer in the RPKI supply chain that exists between the
   Repository Publication Point and Relying Parties, enabling better
   scalability.  Relying Parties can combine information retrieved via
   Erik Synchronization with other RPKI transport protocols.  The
   protocol's design is intended to be efficient, fast, easy to
   implement, and robust in the face of partitions or faults in the
   network.
- **draft-ietf-spring-stamp-srpm-mpls-06** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-spring-stamp-srpm-srv6-03** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as defined in RFC 8762, along
   with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for links
   and SRv6 paths (including Segment Lists of SRv6 Policies, SRv6 IGP
   best paths, and SRv6 IGP Flexible Algorithm paths), as well as
   Layer-3 and Layer-2 services over the SRv6 paths.
- **draft-ietf-srv6ops-srv6addressing-00** (new-draft, score 0, ignored_after_review) [srv6ops]: [Addressing Recommendations for SRv6](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6addressing/) — This document provides recommendations for addressing SRv6 locators
   format.  It introduces concepts of Blocks, Sets, and Node IDs, and
   explains how summarization boundaries and flexible algorithm support
   can be implemented for both small and large networks.
- **draft-ietf-sshm-composite-sigs-00** (new-draft, score 0, ignored_after_review) [sshm]: [Post-Quantum Composite Signatures in SSH](https://datatracker.ietf.org/doc/draft-ietf-sshm-composite-sigs/) — This document specifies the integration of two composite post-quantum
   signature schemes into the Secure Shell (SSH) protocol.  These
   schemes combine the post-quantum Module-Lattice Digital Signature
   Algorithm (ML-DSA) with Elliptic Curve signature algorithms (Ed25519
   and ECDSA, respectively) to provide security against both quantum and
   classical adversaries.
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-27** (new-draft, score 0, ignored_after_review) [v6ops]: [Framework for Multi-domain IPv6-only Underlay Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — For the IPv6 transition, IPv6-only is considered the final stage
   where only IPv6 protocol is used for transport while maintaining
   global reachability for both IPv6 and IPv4 services.  This document
   introduces a framework for a multi-domain IPv6-only underlay network
   from the perspective of network providers.  In particular, it
   proposes stateless address mapping as the basis for enabling IPv4
   service data transmission in a multi-domain IPv6-only environment
   (i.e., IPv4-as-a-Service).  It describes the methodology of stateless
   IPv4/IPv6 mapping, illustrates the behaviors of network devices,
   analyzes the options of IPv6 mapping prefix allocation, and discusses
   the security considerations.  This framework is not intended to
   replace existing IPv6-only technologies, but rather to leverage or
   remain compatible with them.
- **draft-jurkovikj-http-integrity-cache-00** (new-draft, score 0, ignored_after_review) [none]: [Maintaining HTTP Integrity Fields in Cached and Cache-Generated Responses](https://datatracker.ietf.org/doc/draft-jurkovikj-http-integrity-cache/) — HTTP caches update stored response fields, combine partial responses,
   and construct responses from stored state.  Those operations can move
   an Integrity field value onto content or representation data
   different from the data to which the value originally applied.

   This document updates RFC 9111 by defining field-specific maintenance
   rules for Content-Digest, Repr-Digest, and Unencoded-Digest.  A cache
   either preserves the association between each retained or emitted
   dictionary member and its defined input, recomputes the member over
   the resulting input, or removes the member.  The rules cover stored-
   field updates, 304 and HEAD freshening, partial-response combination,
   cache-generated 304, HEAD, and 206 responses, and content-coding
   transformations.  No new HTTP field, status code, cache directive,
   validator, or digest algorithm is defined.
- **draft-juwan-ars-uri-00** (new-draft, score 0, ignored_after_review) [none]: [ARS URI Scheme: A URI Scheme for ARS-1 References](https://datatracker.ietf.org/doc/draft-juwan-ars-uri/) — This document defines the "ars" URI scheme for representing ARS-1
   References in a syntactically valid URI form.  ARS-1 defines a
   deterministic, cryptographically derived reference protocol for
   assigning stable public identifiers to durable digital entities.  The
   "ars" URI scheme provides a standard URI notation for these
   references, enabling their use in hyperlinks, QR codes, metadata
   fields, and other URI-consuming contexts.

   This specification does not redefine the ARS-1 Reference generation
   pipeline, canonicalization rules, or verification logic.  Those are
   normatively defined by ARS-1.  This document defines only the URI
   syntax, encoding, comparison, and resolution semantics for the "ars"
   scheme.
- **draft-knodel-nomcom-gender-representation-04** (new-draft, score 0, ignored_after_review) [none]: [Gender Representation in the IETF Nominating Committees](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document extends the existing limit on nomcom representation by
   organization ([RFC8713], Section 4.17) so that not all voting members
   of the IETF Nominating Committee (nomcom) belong to the same gender.
- **draft-luechow-route86-timestamp-00** (new-draft, score 0, ignored_after_review) [none]: [Route86: A Compact Context-Dependent Timestamp Format](https://datatracker.ietf.org/doc/draft-luechow-route86-timestamp/) — This document specifies Route86, a compact textual timestamp
   representation intended for constrained message transports.  A
   Route86 timestamp combines a Base36-encoded calendar-day component
   with a three-digit decimal Internet Time component.

   The representation occupies six ASCII characters in its canonical
   form.  Interpretation of the calendar component requires knowledge of
   a shared reference date, which may be application-specific or salted.
- **draft-nottingham-ianabis-spec-reqd-03** (new-draft, score 0, ignored_after_review) [none]: [Specification Required Sub-Policies](https://datatracker.ietf.org/doc/draft-nottingham-ianabis-spec-reqd/) — This document defines sub-policies that refine the Specification
   Required registry policy in RFC 8126.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottingham-ianabis-spec-reqd/.

   information can be found at https://mnot.github.io/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/spec-reqd.
- **draft-nottnick-ietf-decisions-01** (new-draft, score 0, ignored_after_review) [none]: [Making Decisions in IETF Working Groups](https://datatracker.ietf.org/doc/draft-nottnick-ietf-decisions/) — This document specifies Best Current Practice for making decisions in
   IETF Working Groups.

   It updates Section 3.3 of [RFC2418].

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottnick-ietf-decisions/.

   information can be found at https://projects.mnot.net/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/ietf-decisions.
- **draft-qin-savnet-bicone-sav-01** (new-draft, score 0, ignored_after_review) [none]: [Bicone Source Address Validation](https://datatracker.ietf.org/doc/draft-qin-savnet-bicone-sav/) — Source address validation (SAV) aims to detect source-spoofed traffic
   while avoiding improper blocking of legitimate traffic.  Existing SAV
   mechanisms commonly rely on ingress allowlist filters on interfaces
   facing customer or lateral peer Autonomous Systems (ASes).  When such
   an allowlist is incomplete, a source address not covered by the
   allowlist cannot be conclusively identified as spoofed, because
   legitimate source prefixes may be missing from the allowlist.  This
   document describes Bicone SAV, which jointly uses an allowlist
   derived from customer-cone information and a blocklist containing
   prefixes that can be positively identified as inappropriate on the
   corresponding ingress interface.  When the allowlist is incomplete,
   packets matching the allowlist are permitted, packets matching the
   blocklist are discarded, and packets matching neither list are
   permitted with logging or other monitoring for subsequent analysis.
   The blocklist can be constructed from provider-cone information and
   augmented with denylist information derived from customer cones.
- **draft-qin-savnet-toa-02** (new-draft, score 0, ignored_after_review) [none]: [A Profile for Traffic Origin Authorizations (TOAs)](https://datatracker.ietf.org/doc/draft-qin-savnet-toa/) — This document defines a standard profile for Traffic Origin
   Authorizations (TOAs), a Cryptographic Message Syntax (CMS) protected
   content type for use with the Resource Public Key Infrastructure
   (RPKI).  A TOA is a digitally signed object that provides a means of
   verifying that an IP address block holder has authorized an
   Autonomous System (AS) to originate traffic using source IP addresses
   within the address block.
- **draft-rashid-pecorella-6lo-lowpan-padding-length-00** (new-draft, score 0, ignored_after_review) [none]: [6LoWPAN Payload Length Handling with L2 Padding](https://datatracker.ietf.org/doc/draft-rashid-pecorella-6lo-lowpan-padding-length/) — 6LoWPAN compression schemes, including HC1 [RFC4944], IPHC [RFC6282],
   and GHC [RFC7400], elide the IPv6 Payload Length (PL) field from
   compressed packets, relying on the Layer 2 (L2) PL to reconstruct it
   at the receiver.  This assumption holds for IEEE 802.15.4 [IEEE Std
   802.15.4], which delivers exactly the bytes transmitted.  However, L2
   technologies that enforce a minimum frame size — most notably
   Ethernet IEEE 802.3 [IEEE Std 802.3], which has a minimum payload of
   46 bytes — silently pad short frames with zero bytes.  In such cases,
   the receiver incorrectly reconstructs the IPv6 PL field, leading to
   packet corruption and protocol failure.  This document describes the
   problem, analyzes existing workarounds, and defines a solution based
   on an Escape dispatch byte (ESC) or ESC Extension Type (EET) extended
   dispatch mechanism that explicitly encodes the IPv6 PL when L2
   padding may be present.
- **draft-rogge-manet-dlep-power-constraints-00** (new-draft, score 0, ignored_after_review) [none]: [DLEP Power Constraints Extension](https://datatracker.ietf.org/doc/draft-rogge-manet-dlep-power-constraints/) — This document defines an extension to the Dynamic Link Exchange
   Protocol (DLEP) to provide dynamic power constraints to the radio.
- **draft-seemann-masque-connect-udp-rendezvous-00** (new-draft, score 0, ignored_after_review) [none]: [UDP Rendezvous over HTTP](https://datatracker.ietf.org/doc/draft-seemann-masque-connect-udp-rendezvous/) — This document defines an Extended CONNECT protocol for relaying UDP
   between two clients authenticated by the same proxy.  A Listener
   registers with the proxy, and a Client uses the resulting Rendezvous
   ID to connect to it.  No public UDP address is allocated.
- **draft-seemann-quic-ppdplpmtud-00** (new-draft, score 0, ignored_after_review) [none]: [Parallel Probing DPLPMTUD for QUIC](https://datatracker.ietf.org/doc/draft-seemann-quic-ppdplpmtud/) — QUIC endpoints commonly use 1200-byte datagrams during the handshake
   and only start Path MTU Discovery afterward.  This means that just-
   established QUIC connections cannot immediately use larger datagrams,
   which is especially limiting for MASQUE protocols and for
   WebTransport.  This document defines Parallel Probing DPLPMTUD
   (PPDPLPMTUD), which probes several packet sizes early during the QUIC
   handshake, so a larger discovered size is usable during later
   handshake phases and especially after handshake completion.  The same
   discovery process is also used for path migration.
- **draft-sl-rtgwg-far-dcn-26** (new-draft, score 0, ignored_after_review) [none]: [Generic Fault-Avoidance Routing Protocol for Data Center Networks](https://datatracker.ietf.org/doc/draft-sl-rtgwg-far-dcn/) — This document describes a generic routing method and protocol for a
   regular data center network, named the Fault-Avoidance Routing (FAR)
   protocol.  The FAR protocol provides a generic routing method for all
   types of regular topology network architectures that have been
   proposed for large-scale cloud-based data centers over the past few
   years.  The FAR protocol is designed to leverage any regularity in
   the topology and compute its routing table in a concise manner.  Fat-
   tree is taken as an example architecture to illustrate how the FAR
   protocol can be applied in real operational scenarios.
- **draft-smn-idr-inter-domain-ibgp-10** (new-draft, score 0, ignored_after_review) [none]: [Interconnecting domains with IBGP](https://datatracker.ietf.org/doc/draft-smn-idr-inter-domain-ibgp/) — This document describes the building of Inter-domain L3VPN
   architecture with internal BGP, applying the multi-domain options
   specified in BGP/MPLS IP Virtual Private Networks (VPNs) within a
   single Autonomous System, where route reflectors set the NEXT_HOP
   attribute to self as described in BGP Route Reflector with Next Hop
   Self.
- **draft-spaghetti-grow-rpki-doa-00** (new-draft, score 0, ignored_after_review) [none]: [A Profile for Resource Public Key Infrastructure (RPKI) Discard Origin Authorizations (DOA)](https://datatracker.ietf.org/doc/draft-spaghetti-grow-rpki-doa/) — This document defines a Cryptographic Message Syntax (CMS) profile
   for Discard Origin Authorizations (DOAs), for use with the Resource
   Public Key Infrastructure (RPKI).  A DOA is a digitally signed object
   that provides a means of verifying that an IP address block holder
   has authorized an Autonomous System (AS) to originate routes to one
   or more prefixes within the address block tagged with a specific set
   of Border Gateway Protocol (BGP) Communities, to signal a request to
   discard IP traffic destined towards the tagged IP prefix.
- **draft-swhited-contra-tags-05** (new-draft, score 0, ignored_after_review) [none]: [Metadata for Called Folk Dances](https://datatracker.ietf.org/doc/draft-swhited-contra-tags/) — This document defines metadata tags for describing aspects of Contra,
   Square, and other traditional called folk dances.  These tags are
   meant for archivists as well as modern day callers of traditional
   dances.
- **draft-swhited-mka-stems-13** (new-draft, score 0, ignored_after_review) [none]: [Matroska Stem Files](https://datatracker.ietf.org/doc/draft-swhited-mka-stems/) — This document defines a multi-track profile of the Matroska container
   format for distributing stems for live-mixing by DJs.  It is intended
   to be used by DJ applications, Digital Audio Workstations, and multi-
   track recorders while remaining backwards compatible with existing
   media players.
- **draft-templin-6man-aero-omni-amen-12** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-van-meter-qirg-quantum-network-architecture-01** (new-draft, score 0, ignored_after_review) [none]: [A Quantum Network Architecture](https://datatracker.ietf.org/doc/draft-van-meter-qirg-quantum-network-architecture/) — This quantum network architecture defines a set of planes providing
   different views of the network, supporting different responsibilities
   and modes of operation; a set of device, node and link types; some
   network topologies, deployment scenarios and their relationship to
   applications; and key design decisions as a result of corresponding
   requirements.
- **draft-xu-idr-fare-in-mpson-01** (new-draft, score 0, ignored_after_review) [none]: [Fully Adaptive Routing Ethernet in Multi-Plane Scale-Out Networks](https://datatracker.ietf.org/doc/draft-xu-idr-fare-in-mpson/) — FARE-BGP enables weighted ECMP load balancing using a path-bandwidth
   extended community.  FARE-in-SUN extends this mechanism from switches
   to GPUs for scale-up networks, which are typically multi-plane.
   Large AI training clusters are increasingly adopting multi-plane
   scale-out network topologies.  This document further extends FARE-BGP
   from switches to RoCE NICs (RNICs) for such multi-plane scale-out
   networks.  The document also presents two techniques to address route
   scalability concerns caused by the injection of numerous host routes.
- **draft-yuyou-conditional-filtering-00** (new-draft, score 0, ignored_after_review) [none]: [Conditional Range Filters for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-yuyou-conditional-filtering/) — In Media over QUIC Transport (MOQT), subscribers can use Range
   Filters to select specific subgroups, objects, or priorities within a
   subscribed track.  However, these subscription filters are static
   once established and can only be modified through explicit subscriber
   control signaling.  This document proposes an extension to the Range
   Filter design that binds conditional evaluation logic directly to
   specific Range Filter sets.  By introducing dynamic conditions to
   Range Filter configurations, a relay can autonomously adapt the
   intra-track forwarding behavior based on real-time network
   conditions, avoiding the round-trip delay of explicit subscriber
   update signaling.
- **draft-zhangb-cats-cmas-06** (new-draft, score 0, ignored_after_review) [none]: [Public Service Platform for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-zhangb-cats-cmas/) — CATS applications require service resolution and traffic steering
   across heterogeneous computing resources.  Directly exposing raw
   computing metrics from different hardware platforms can be difficult
   for clients, service sites, and CATS control-plane components to
   interpret consistently.  This Informational document describes the
   purpose and functions of a public service platform for CATS, and
   identifies the CS-ID-related information fields needed by those
   functions.  The platform maintains a common service catalogue,
   associates public service identifiers with service descriptions and
   deployment requirements, and provides the service context used by
   service-oriented metric mechanisms.  This platform supports the
   Computing Metrics as a Service (CMAS) approach by allowing
   heterogeneous resources to be represented through service-oriented
   parameters rather than raw hardware metrics.  Service-oriented metric
   definitions and operational procedures are specified in
   [I-D.zhangb-cats-service-metrics-op-02].
- **draft-zhao-iccrg-competitive-mode-01** (new-draft, score 0, ignored_after_review) [none]: [Competitive Mode Enhancement for Delay-Based Congestion Control Algorithms](https://datatracker.ietf.org/doc/draft-zhao-iccrg-competitive-mode/) — This document proposes introducing a "Competitive Mode" into delay-
   based congestion control algorithms to improve their competitiveness
   and fairness during coexistence scenarios.

## Errors / fetch failures

_None._
