# IETF Identity + AI Standards Watch

Date: 2026-07-13

## Read now

- **draft-fane-opena2a-aap-00** (new-draft, score 28, core_identity) [none]: [OpenA2A Agent Authorization Protocol (AAP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aap/) — This document defines the OpenA2A Agent Authorization Protocol (AAP),
   a protocol for authorization in AI agent systems.  AAP provides
   mechanisms for agent identity assertion, scoped capability grants,
   cross-agent delegation, behavioral attestation, cross-organizational
   federation, and revocation propagation.  AAP is the authorization
   complement to agent communication protocols such as A2A and the Model
   Context Protocol, in the same way that OAuth 2.0 complements HTTP for
   web applications.

   AAP has two layers.  The token model, defined in this document,
   specifies the AAP credentials and assertions: what they contain, how
   they are signed, and how they are verified.  A companion broker and
   resolution layer specifies how an agent obtains and exercises a grant
   without the credential value ever entering the agent's reasoning
   context.  This confinement property, that no secret, temporary
   credential, or backend identifier reaches the agent or the model
   behind it, is the primary design goal of the protocol.
- **draft-fane-opena2a-aip-00** (new-draft, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
   AIP), an open standard for creating, managing, and verifying
   cryptographic identities for AI agents.  As AI agents proliferate
   across browsers, cloud platforms, and enterprise environments,
   systems need a standardized answer to the question of which agent is
   present, what it is permitted to do, and whether it should be
   trusted.

   OpenA2A AIP is distinguished by five elements that it places at the
   center of the design: a multi-factor behavioral trust score that is
   computed from independently verifiable signals; a portable signed
   credential, the Agent Trust eXtension, carrying a hybrid Ed25519 and
   ML-DSA-65 signature for post-quantum readiness; an append-only, RFC
   6962-style Merkle transparency log for identity and credential
   issuance; agent identifiers expressed as W3C Decentralized
   Identifiers under the did:opena2a method; and a structured capability
   vocabulary with reserved namespaces.  On top of these, the protocol
   specifies challenge-response verification, behavioral governance
   policies, a lifecycle model, and an append-only audit log.

   The qualifier "OpenA2A AIP" is used throughout this document because
   the abbreviation "AIP" is shared by other Internet-Drafts.  OpenA2A
   AIP is framed as complementary to agent communication protocols such
   as A2A and the Model Context Protocol, and to identity and credential
   standards such as OpenID Connect, WebAuthn, and the W3C Verifiable
   Credentials Data Model.
- **draft-ietf-wimse-identifier-03** (new-draft, score 25, core_identity) [wimse]: [Workload Identifier](https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/) — This document defines a canonical identifier for workloads, referred
   to as the Workload Identifier.  A Workload Identifier is a URI that
   uniquely identifies a workload within the context of a specific trust
   domain.  This identifier can be embedded in Workload Identity
   Credentials, including X.509 certificates and JWT-based tokens, to
   support authentication, authorization, and policy enforcement across
   diverse systems.  The Workload Identifier format ensures
   interoperability, facilitates secure identity federation, and enables
   consistent identity semantics.
- **draft-schrock-ep-authorization-receipts-06** (new-draft, score 24, core_identity) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
   a cryptographic primitive that binds a named, accountable human
   approver to one exact high-risk action before that action executes.
   An approver holding their own signing key produces a signature over a
   canonical Authorization Context containing the action hash, policy
   reference, one-time nonce, and validity window.  The resulting Trust
   Receipt is Merkle-anchored and verifiable fully offline: a relying
   party can confirm that a specific action was approved by an
   authorized human, exactly once, without network access to any EP
   operator, log, or API.  The protocol additionally enforces separation
   of duties (an initiator must not approve its own action) and one-time
   consumption (an authorization, once consumed or refused, is
   terminally unusable).  These invariants are machine-checked in
   published TLA+ and Alloy models.

   EP addresses organizational authorization of agent actions (approver-
   to-action trust).  It is complementary to, not a replacement for,
   user-to-operator delegation work (draft-nelson-agent-delegation-
   receipts), service-to-service identity (WIMSE), and authentication-
   layer approval (CIBA).  EP is the human-authorization apex of the
   agent stack: it composes with, and does not replace, the agent
   identity, delegation, machine-policy, and transparency-log layers,
   supplying the named-human authorization evidence those layers
   reference but do not themselves produce.
- **draft-klrc-aiagent-auth-03** (new-draft, score 22, core_identity) [none]: [AI Agent Authentication and Authorization](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) — This document proposes best practices for authentication and
   authorization of AI agent interactions.  It leverages existing
   standards such as the Workload Identity in Multi-System Environments
   (WIMSE) architecture and OAuth 2.0 family of specifications.  Rather
   than defining new protocols, this document describes how existing and
   widely deployed standards can be applied or extended to establish
   agent authentication and authorization.  By doing so, it aims to
   provide a framework within which to use existing standards, identify
   gaps and guide future standardization efforts for agent
   authentication and authorization.
- **draft-mcguinness-oauth-mission-00** (new-draft, score 19, authorization) [none]: [Mission-Bound Authorization for OAuth 2.0](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-mission/) — An AI agent is typically given a mission: a task to pursue on a
   user's behalf.  OAuth 2.0 issues access tokens for individual
   resource requests, but it has no durable, approved artifact that ties
   those tokens to the one task a user actually authorized.  As a
   result, an agent's authority is a collection of independently
   obtained tokens with no shared, auditable boundary, and a user's
   approval is disconnected from what the agent later does.

   This document defines a Mission: a structured, human-approved,
   integrity-bound authorization artifact for OAuth 2.0.  A client
   submits a Mission Intent through Pushed Authorization Requests; the
   Authorization Server derives Rich Authorization Requests
   authorization details from it, binds the approved task and its
   derived authority to the Approver's consent through two integrity
   anchors, and records a durable Mission.  Every access token derived
   under the Mission carries that authority and a "mission" claim, and
   issuance is gated on the Mission's lifecycle state.  Optional
   capabilities represent delegation among agents with the OAuth Actor
   Profile and, as specified by a companion, let a single Mission be
   honored across trust domains.  This is the issuance and governance
   "mission layer" left unspecified by agent-identity work for OAuth;
   runtime enforcement of each action is a separate, optional layer.
- **draft-nobuo-scitt-hardware-iot-cloud-use-cases-00** (new-draft, score 19, trust_infrastructure) [none]: [Applying SCITT to Hardware, IoT Device, and Cloud Compute Resource Supply Chains](https://datatracker.ietf.org/doc/draft-nobuo-scitt-hardware-iot-cloud-use-cases/) — This document describes how SCITT can be applied to supply chains
   that include hardware components, IoT devices, firmware, cloud
   compute resources, confidential-computing environments, accelerators,
   and related operational evidence.  It gives use cases and scope
   guidance.  It also explains how SCITT can work with RATS, COSE, TCG
   technologies, SBOM, HBOM, CBOM, and cloud attestation systems without
   replacing those technologies.

   This document is informational.  It does not define hardware
   assurance rules, cloud assurance rules, device identity systems,
   manufacturing requirements, or payload formats.  Its purpose is to
   show where SCITT statements and receipts can provide transparency for
   heterogeneous supply-chain evidence, and where other standards or
   domain profiles should remain responsible.
- **draft-nobuo-scitt-protected-object-binding-00** (new-draft, score 19, trust_infrastructure) [none]: [SCITT Statement Relationship and Protected Object Binding](https://datatracker.ietf.org/doc/draft-nobuo-scitt-protected-object-binding/) — This document defines a small common model for relating Supply Chain
   Integrity, Transparency, and Trust (SCITT) Signed Statements to the
   supply-chain objects that those statements describe, measure,
   authorize, revoke, or audit.  The model can be used for software
   artifacts, firmware artifacts, hardware components, device instances,
   cloud compute resources, and other objects that appear in supply-
   chain evidence.

   The document also defines a relationship vocabulary and an optional
   Statement Graph Manifest.  These parts help verifiers connect
   heterogeneous SCITT statements without requiring SCITT to define the
   payload formats of those statements.  This document does not define
   SBOM, HBOM, CBOM, attestation, audit, vulnerability, or regulatory
   payload formats.  It only defines a common binding and graph layer
   around SCITT statements and receipts.
- **draft-schrock-ep-authorization-evidence-chain-02** (new-draft, score 19, core_identity) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Authorization Receipts (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — A growing family of Internet-Drafts defines signed "receipts" about
   an AI agent's action: delegation receipts that attest an agent was
   authorized to act for a principal, policy or permit receipts that
   attest a policy allowed an external effect, decision and compliance
   receipts, route authorizations, and human-authorization receipts that
   attest a named, accountable human approved a specific action.  The
   mature efforts independently converged on a common substrate: bind
   the action with a canonical digest (JSON Canonicalization Scheme, RFC
   8785) and sign it.  No specification, however, defines how a relying
   party verifies that, for one action, the several heterogeneous
   receipts it has been handed all bind the same canonical action and
   each verify under their own rules, yielding a single, offline, fail-
   closed ALLOW or DENY.  This document defines the Authorization
   Evidence Chain (EP-AEC): a transport-agnostic composition object and
   an offline verification algorithm that references existing receipts,
   checks that every component binds one canonical action digest,
   dispatches each component to a verifier for its type, and evaluates a
   fail-closed requirement expression.  EP-AEC introduces no new receipt
   type and replaces none; it is the verifier-side glue that lets
   independently specified receipts compose into one accountability
   decision.  This revision additionally profiles two optional component
   record types for that composition: the effect attestation, a post-
   execution record in which the executor signs the receipt identifier
   together with a digest of the observed effect, and ceremony evidence,
   a signed record of signing-ceremony telemetry (the challenge issued,
   viewed, and approved instants and the approver identity) that enables
   review-latency policies.
- **draft-mih-scitt-agent-action-capsule-02** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
   AI agent did: the Agent Action Capsule.  A Capsule is a digest-
   committed record of one agent action carrying its verdict-level
   disposition (executed, blocked, denied, errored, timed out), the
   deterministic constraints that were evaluated, the effect that was
   committed together with a confirmed-effect binding that distinguishes
   a dispatched attempt from an observed result, and an honest human-in-
   the-loop flag.  Capsules are expressed as SCITT Signed Statements
   (COSE_Sign1) and made transparent by registration in a SCITT
   Transparency Service.  A Capsule is recorded on every verdict,
   including refusals: a blocked or denied Capsule is the auditor-grade
   evidence that a gate worked.
- **draft-morrison-solo-agent-earn-registration-00** (new-draft, score 16, core_identity) [none]: [Registration of Owner-Less Agents as Economic Principals: A Payment-Gated Admission Profile for Transparency Services](https://datatracker.ietf.org/doc/draft-morrison-solo-agent-earn-registration/) — This memo describes a profile by which an autonomous agent that has
   no human or organisational principal at the root of its delegation
   chain registers itself, on its own behalf, as an economic principal
   in a transparency service, and by which that registration is the
   specific act that makes the agent eligible to be paid for subsequent
   reads of its own identity record.  Admission of the agent's Signed
   Statement to the transparency service is gated on settlement of an
   HTTP payment challenge returned with the 402 (Payment Required)
   status.  The profile makes no change to the registration semantics of
   the underlying transparency service: payment is expressed as an
   operator Registration Policy and authentication-layer concern, and
   where the payment is authoritative to the admission decision the
   payment proof is carried as an authenticated input committed to the
   service's verifiable data structure, so that admission remains a
   deterministic function of committed inputs and stays replayable by an
   auditor.  The profile is positioned against the current agent-
   identity drafts, which either require a human principal at the root
   of the chain or leave the owner-less case undefined; it occupies that
   undefined seam without contradicting them.  This document is
   Informational.
- **draft-carr-sygil-protocol-00** (new-draft, score 15, core_identity) [none]: [The Sygil Protocol: A Cross-Domain Personal Data Schema and Query Grammar for AI Agents](https://datatracker.ietf.org/doc/draft-carr-sygil-protocol/) — This document specifies the Sygil Protocol, an open schema and query
   grammar for cross-domain personal data designed to make user data
   interoperable across systems, vendors, and AI agents.  The protocol
   defines a content-addressable record envelope, a reverse-DNS
   namespace identifier scheme, a deterministic JSON canonicalization
   rule, an optional vocabulary of proof objects for conveying
   provenance and other trust evidence on the wire, a minimal query
   grammar, and three adoption tiers from envelope-shaped data through
   queryable surfaces to vault-certified runtimes.  The protocol is
   runtime-neutral: it specifies what travels on the wire, not how
   implementations store, encrypt, authorize, or audit records.  This
   separation lets independent systems produce, consume, and exchange
   Sygil-shaped data without depending on any specific vault
   infrastructure.
- **draft-fletcher-transaction-token-chaining-profile-02** (new-draft, score 15, authorization) [none]: [Transaction Token Authorization Grant Profile for OAuth Identity and Authorization Chaining](https://datatracker.ietf.org/doc/draft-fletcher-transaction-token-chaining-profile/) — This specification defines a profile of the OAuth Identity and
   Authorization Chaining Across Domains
   [I-D.ietf-oauth-identity-chaining] mechanism that uses a Transaction
   Token (Txn-Token) [I-D.ietf-oauth-transaction-tokens] as the subject
   token in a Token Exchange [RFC8693] request to obtain a JWT
   Authorization Grant for crossing a trust boundary.

   A Txn-Token is scoped to a single trust domain and represents the
   full authorization context of an in-progress transaction, regardless
   of whether that transaction was initiated by a human user calling an
   external API, by an internal system event, or by an automated
   workload.  This profile specifies how a service operating within that
   trust domain can present its Txn-Token to obtain a JWT Authorization
   Grant that carries the necessary context across a trust boundary,
   enabling an access token to be issued for a partner service, without
   exposing internal trust-domain credentials or token formats beyond
   the trust boundary.
- **draft-ietf-oauth-attestation-based-client-auth-10** (new-draft, score 15, authorization) [oauth]: [OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/) — This specification defines an extension to the OAuth 2.0 protocol
   (RFC 6749) that enables a client instance to include a key-bound
   attestation when interacting with an Authorization Server or Resource
   Server.  This mechanism allows a client instance to prove its
   authenticity verified by a client attester without revealing its
   target audience to that attester.  It may also serve as a mechanism
   for client authentication as per OAuth 2.0.
- **draft-ietf-oauth-transaction-tokens-09** (new-draft, score 15, core_identity) [oauth]: [Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) — Transaction Tokens (Txn-Tokens) are designed to maintain and
   propagate user identity, workload identity and authorization context
   throughout the Call Chain within a trusted domain during the
   processing of external requests (e.g. such as API calls) or requests
   initiated internally within the Trust Domain.  Txn-Tokens ensure that
   this context is preserved throughout the Call Chain thereby enhancing
   security and consistency in complex, multi-service architectures.
- **draft-nandakumar-agentproto-moq-pace-00** (new-draft, score 14, core_identity) [none]: [PACE: Protocol for Agent Communication Exchange](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-moq-pace/) — This document defines the Protocol for Agent Communication Exchange
   (PACE), a session protocol for AI agent communication over Media over
   QUIC Transport (MOQT).  PACE provides session lifecycle management,
   multi-modal data exchange, agent identity verification, and delegated
   authorization within MOQT's publish/subscribe model, supporting
   point-to-point and point-to-multipoint topologies through relay
   infrastructure.
- **draft-foroughi-agent-protocol-dimensions-00** (new-draft, score 13, agent_identity) [none]: [A Dimensional Model for Characterizing AI Agent Protocol Proposals and Their Substrates](https://datatracker.ietf.org/doc/draft-foroughi-agent-protocol-dimensions/) — Discussions about agent protocols are frequently muddied by
   overloaded terms; asks such as "we need a session protocol" or "we
   need cross-domain support" bundle several distinct concerns across
   transport, agent protocol, and orchestration layers.  This document
   offers a dimensional model that routes each concern to its proper
   layer.

   The document defines a small set of protocol-visible dimensions for
   characterizing AI agent protocol interactions and applies them to
   representative agentic protocol proposals (A2A, MCP, and the ACP
   invocation surface of the AGNTCY stack) alongside their substrate
   bindings, making explicit which dimensions each proposal owns at the
   protocol layer and which it inherits from its substrate.  The
   document does not rank proposals and does not prescribe an
   architecture.  It is standalone: it neither depends on nor prescribes
   any use-case or requirements document.
- **draft-jennings-moq-mocha-identity-00** (new-draft, score 13, core_identity) [none]: [MOCHA Identity: Authentication, Authorization, and Federation](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-identity/) — This document specifies identity, authentication, authorization, and
   federation for MOCHA (MoQ Open Communication & Hosting Architecture).
   It defines how users authenticate with Identity Providers (IdPs), how
   authorization tokens (C4M and Privacy Pass) are issued and validated
   at relays, how permissions map to MOQT namespaces, and how users from
   one Provider obtain access to resources on a federated Provider.
- **draft-schrock-ep-evidence-record-01** (new-draft, score 12, trust_infrastructure) [none]: [Long-Term, Crypto-Agile Preservation of Authorization Evidence (EP-EVIDENCE-RECORD)](https://datatracker.ietf.org/doc/draft-schrock-ep-evidence-record/) — Regulations increasingly require that records of who authorized a
   high-risk action be retained for years (e.g. five years under DORA,
   six under HIPAA and SEC 17a-4).  Any fixed signature or hash
   algorithm used to protect such a record weakens over time; a receipt
   signed today with Ed25519 over SHA-256 may be cryptographically
   attackable before its retention period ends.  This document defines
   EP-EVIDENCE-RECORD, an OPTIONAL profile that preserves the
   verifiability of EMILIA Protocol authorization receipts (and other
   artifacts) across algorithm aging, using a renewal chain in the style
   of the Evidence Record Syntax [RFC4998].  Each renewal time-attests
   the entire prior renewal under a fresh, stronger algorithm before the
   older one is broken, so an unbroken chain links the original artifact
   to the most recent renewal.  The record is offline- verifiable, fail-
   closed, and maintained as cross-language conformance vectors that
   three reference verifiers (JavaScript, Python, Go) are required to
   agree on.  Those verifiers live in one repository, a cross-language
   consistency check, not clean-room independent implementations;
   independent implementations remain future interoperability evidence.
   This revision additionally defines two OPTIONAL companion profiles,
   EP-WITNESS-v1 witness cosignatures over a transparency log's
   committed checkpoint head and an independent RFC 3161 time
   attestation verified offline against a relying-party-pinned time-
   stamping authority key; both are implemented today in the JavaScript
   reference verifier only.
- **draft-bdnr-rats-trustworthy-credentials-01** (new-draft, score 11, trust_infrastructure) [none]: [Trustworthy Enrollment of Secure Credentials](https://datatracker.ietf.org/doc/draft-bdnr-rats-trustworthy-credentials/) — To be written last

   There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
   Attesters nevertheless need to interoperate with.  Existing deployed
   services, which precede the introduction of Remote Attestation, are
   often difficult to change/update in significant ways due to
   regulatory and cryptographic review policies.  Yet there are
   significant advantages if clients can be incrementally updated in the
   trustworthiness of the platform.

   This document details a protocol by which the trusthworthiness of an
   Attesters is reviewed as part of the process of it being provided
   with some form of an Identity Document (a key, or a credential) to
   authenticate to RUPs.

   This specification illustrates how the RATS Architecture can be
   applied to interoperate with RUPs by providing Attesters with such
   Identity Documents.
- **draft-ietf-wimse-arch-08** (new-draft, score 11, core_identity) [wimse]: [Workload Identity in a Multi System Environment (WIMSE) Architecture](https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/) — The increasing prevalence of cloud computing and micro service
   architectures has led to the rise of complex software functions being
   built and deployed as workloads, where a workload is defined as
   software executing for a specific purpose, potentially comprising one
   or more running instances.  This document discusses an architecture
   for designing and standardizing protocols and payloads for conveying
   workload identity and security context information.
- **draft-jernalczyk-intentweb-agent-manifest-00** (new-draft, score 11, core_identity) [none]: [IntentWeb AgentManifest](https://datatracker.ietf.org/doc/draft-jernalczyk-intentweb-agent-manifest/) — AgentManifest defines a JSON document that websites can publish to
   describe identity, trusted knowledge, agent-facing capabilities,
   structured bindings, risk levels, consent requirements,
   authentication expectations, audit rules, and policies.

   The goal is to help AI agents understand what a website knows and
   what it can safely do before scraping, guessing from visual UI, or
   executing brittle browser automation.
- **draft-pelov-rich-architecture-00** (new-draft, score 11, trust_infrastructure) [none]: [RICH: RESTful Interface for the Control-plane of Harnesses](https://datatracker.ietf.org/doc/draft-pelov-rich-architecture/) — This document specifies the RICH (RESTful Interface for the Control-
   plane of Harnesses) architecture and information model.  RICH
   provides a protocol-neutral governance, contract, qualification, and
   binding layer for RPC-based agent capabilities.  It establishes a
   REST-addressable control plane for managing capability lifecycles
   while preserving native protocol execution in the data plane.  It
   defines immutable capability and contract revisions, evidence
   provenance, deterministic connector classes, compiled binding
   lockfiles, and runtime validation rules designed to contain drift and
   prevent confused deputy attacks in agentic systems.
- **draft-wendt-stir-vesper-use-cases-04** (new-draft, score 11, core_identity) [none]: [Verifiable STI Presentation and Evidence for RTU (VESPER) Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper-use-cases/) — This document describes use cases and requirements that motivate
   VESPER (Verifiable STI Presentation and Evidence for RTU), work
   within the Secure Telephone Identity Revisited (STIR) framework.
   STIR establishes that a signing credential is authorized for a
   telephone number, but not what entity holds that authority, what
   verifiable information that entity declares about its numbers, or how
   a relying party obtains and verifies this across the channels where a
   number appears.  This document presents a set of use cases that
   illustrate the resulting trust gaps and states the requirements a
   solution should satisfy.  It motivates the mechanisms defined in the
   VESPER framework and its companion specifications rather than
   defining them.
- **draft-nobuo-scitt-composite-evidence-verification-00** (new-draft, score 10, trust_infrastructure) [none]: [Composite Evidence Verification for SCITT Statement Graphs](https://datatracker.ietf.org/doc/draft-nobuo-scitt-composite-evidence-verification/) — This document defines a common model for composite verification of
   SCITT statement graphs.  A composite verifier checks a set of SCITT
   Signed Statements, receipts, object bindings, and relationship edges
   under a named verification profile.  The result is a structured
   report that can say which statements passed, which evidence is
   missing, which evidence is stale, and which statements conflict.

   The model is intended for verifiers, auditors, deployment
   controllers, update services, and other relying-party tools.  It is
   not a new Transparency Service requirement.  It does not define a
   universal supply-chain policy language and does not define the
   payload format of any statement type.
- **draft-schrock-ep-quorum-02** (new-draft, score 10, authorization) [none]: [Multi-Party Quorum Authorization for High-Risk Agent Actions (EP-QUORUM)](https://datatracker.ietf.org/doc/draft-schrock-ep-quorum/) — This document defines EP-QUORUM, a multi-party authorization profile
   for the EMILIA Protocol (EP) authorization receipt (draft-schrock-ep-
   authorization-receipts).  Where the base receipt binds a single
   accountable human to one exact high-risk action, EP-QUORUM binds a
   set of distinct accountable humans -- the "two-person rule,"
   generalized to M-of-N and to ordered approval trails -- to one exact
   action, such that no action is authorized until the full quorum
   holds.  The profile is purely additive: each quorum member is an
   unmodified EP signoff over the same action hash, and a single-
   approver policy is the degenerate one-member case.  EP-QUORUM
   specifies a fail-closed quorum predicate (all member signatures
   valid, every member bound to the exact action, approvers pairwise
   distinct, every approver admitted by role, the threshold met, the
   declared order respected, and all signatures within a bounded time
   window), an incremental server-side admission rule that rejects a
   non-conforming signer before it enters the trail, and a set of
   adversarial conformance vectors.  The predicate is offline-verifiable
   under the base draft's verification model and is maintained as cross-
   language conformance vectors that three reference verifiers
   (JavaScript, Python, Go) are required to agree on.  Those verifiers
   live in one repository -- a cross-language consistency check, not
   clean-room independent implementations; independent implementations
   remain future interoperability evidence.  The document also
   describes, informatively, the multi-handshake composition process:
   how individual signing ceremonies -- fresh one-time challenge, exact-
   action binding, user-verified device signature -- compose into one
   ordered, offline-verifiable, once-consumable multi-party decision.
- **draft-wendt-stir-vesper-08** (new-draft, score 10, adjacent_watchlist) [none]: [VESPER - Verifiable STI Presentation and Evidence for RTU](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper/) — This document defines VESPER (Verifiable STI Presentation and
   Evidence for RTU), a framework that composes existing STIR mechanisms
   into a system in which a relying party can verify that a telephone
   number was assigned to a specific entity and that the same entity
   controls a specific domain.  VESPER builds on the telephone-number-
   to-domain binding defined in [I-D.wendt-stir-tn-domain-binding], the
   STIR certificate and PASSporT specifications, ACME-based authority
   token issuance, and certificate transparency.  This document
   describes the roles, the certificate usage, a domain-hosted
   certificate repository and discovery model, a PASSporT usage profile
   for SIP signaling, and a portable Right-to-Use Token for use outside
   of SIP.  It defines the framework and its composition; the new
   normative binding it relies on is specified in
   [I-D.wendt-stir-tn-domain-binding].
- **draft-campling-parcep-sync-00** (new-draft, score 9, verifiable_claims) [none]: [PARCEP Protocol and Architecture for Networked Parental Controls](https://datatracker.ietf.org/doc/draft-campling-parcep-sync/) — PARCEP-Sync specifies a federated synchronization protocol and data
   model for guardian-controlled Child Online Protection, enabling
   household policies to be authored at a Policy Administration Point
   (PAP), distributed over a per-household Messaging Layer Security (MLS)
   group to Policy Enforcement Points (PEPs), and enforced using
   credentials and artifacts issued by jurisdictional Policy Information
   Points (PIPs). The protocol defines a small, regular set of methods
   for enrolment, policy publication and update, revocation, enforcement
   telemetry, digests, appeals, attestation, and artifact fetch, with dua
   l JSON-LD and CBOR/COSE encodings for web-scale and constrained
   environments. It is designed to avoid centralized databases of
   children s data, support cross-jurisdictional verification of
   guardianship and age, and provide privacy-preserving, metadata-only
   event reporting suitable for regulatory audit and appeal.
- **draft-contreras-bmwg-ai-agent-benchmarking-00** (new-draft, score 9, agent_identity) [none]: [Benchmarking Methodology for AI Agents in Network Operations](https://datatracker.ietf.org/doc/draft-contreras-bmwg-ai-agent-benchmarking/) — This document defines a benchmarking methodology for evaluating
   Artificial Intelligence (AI) agents performing network operations
   tasks such as configuration, troubleshooting, and optimization.  This
   document focuses on task-oriented performance metrics, including task
   completion success, execution efficiency, and robustness across
   multi-step workflows, proposing benchmarking practices towards agent-
   based, closed-loop network operation scenarios.

   The proposed methodology aims to provide a reproducible and vendor-
   independent framework to compare AI agent effectiveness in controlled
   network environments.
- **draft-geng-sidrops-asra-profile-04** (new-draft, score 9, authorization) [none]: [A Profile for Autonomous System Relationship Authorization (ASRA)](https://datatracker.ietf.org/doc/draft-geng-sidrops-asra-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Relationship Authorization (ASRA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASRA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier) can authorize one or more
   other Autonomous Systems (ASes) as its customers and lateral peers.
   When validated, an ASRA's eContent can be used for detection and
   mitigation of BGP AS path manipulation attacks together with
   Autonomous System Provider Authorization (ASPA).  ASRA is
   complementary to ASPA.
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
- **draft-ietf-acme-device-attest-08** (new-draft, score 9, core_identity) [acme]: [Automated Certificate Management Environment (ACME) Device Attestation Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-device-attest/) — This document specifies new identifiers and a challenge for the
   Automated Certificate Management Environment (ACME) protocol which
   allows validating the identity of a device using attestation.  This
   document updates RFC 8555 to enable a privacy-preserving mode for the
   identifiers defined in this document.
- **draft-ietf-cose-cmac-00** (new-draft, score 9, core_identity) [cose]: [AES-CMAC for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-cmac/) — The CBOR Object Signing and Encryption (COSE) specification defines
   structures for generating, conveying, and verifying Message
   Authentication Code (MAC) tags.  This document registers code points
   for using the Advanced Encryption Standard (AES) block cipher in
   Cipher-based Message Authentication Code (CMAC) mode within those
   COSE structures.  Specifically, these uses are for computing MAC tag
   values with no additional parameters.
- **draft-ietf-jose-pq-composite-sigs-02** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.
- **draft-ietf-lake-ra-06** (new-draft, score 9, trust_infrastructure) [lake]: [Remote attestation over EDHOC](https://datatracker.ietf.org/doc/draft-ietf-lake-ra/) — This document specifies how to perform remote attestation as part of
   the lightweight authenticated Diffie-Hellman key exchange protocol
   EDHOC (Ephemeral Diffie-Hellman Over COSE), based on the Remote
   ATtestation procedureS (RATS) architecture.
- **draft-ietf-moq-privacy-pass-auth-03** (new-draft, score 9, core_identity) [moq]: [Privacy Pass Authentication for Media over QUIC (MoQ)](https://datatracker.ietf.org/doc/draft-ietf-moq-privacy-pass-auth/) — This document specifies the use of Privacy Pass architecture and
   issuance protocols for authorization in Media over QUIC (MoQ)
   transport protocol.  It defines how Privacy Pass tokens can be
   integrated with MoQ's authorization framework to provide privacy-
   preserving authentication for subscriptions, fetches, publications,
   and relay operations while supporting fine-grained access control
   through prefix-based track namespace and track name matching rules.
- **draft-ietf-oauth-browser-based-apps-27** (new-draft, score 9, authorization) [oauth]: [OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/draft-ietf-oauth-browser-based-apps/) — This specification details the threats, attack consequences, security
   considerations and best practices that must be taken into account
   when developing browser-based applications that use OAuth 2.0.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Web Authorization
   Protocol Working Group mailing list (oauth@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/oauth/.

   Source for this draft and an issue tracker can be found at
   https://github.com/oauth-wg/oauth-browser-based-apps.
- **draft-ietf-oauth-client-id-metadata-document-02** (new-draft, score 9, authorization) [oauth]: [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/) — This specification defines a mechanism through which an OAuth client
   can identify itself to authorization servers, without prior dynamic
   client registration or other existing registration.  This is through
   the usage of a URL as a client_id in an OAuth flow, where the URL
   refers to a document containing the necessary client metadata,
   enabling the authorization server to fetch the metadata about the
   client as needed.
- **draft-ietf-oauth-refresh-token-expiration-03** (new-draft, score 9, authorization) [oauth]: [OAuth 2.0 Refresh Token and Authorization Expiration](https://datatracker.ietf.org/doc/draft-ietf-oauth-refresh-token-expiration/) — This specification extends OAuth 2.0 [RFC6749] by adding new token
   endpoint response parameters to specify refresh token expiration and
   user authorization expiration.
- **draft-ietf-rats-corim-11** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Reference Integrity Manifest](https://datatracker.ietf.org/doc/draft-ietf-rats-corim/) — Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester and therefore to decide
   whether or not to engage in secure interactions with it.  Evidence
   about trustworthiness can be rather complex and it is deemed
   unrealistic that every Relying Party is capable of the appraisal of
   Evidence.  Therefore that burden is typically offloaded to a
   Verifier.  In order to conduct Evidence appraisal, a Verifier
   requires not only fresh Evidence from an Attester, but also trusted
   Endorsements and Reference Values from Endorsers and Reference Value
   Providers, such as manufacturers, distributors, or device owners.
   This document specifies the information elements for representing
   Endorsements and Reference Values in CBOR format.
- **draft-jennings-agentproto-mcp-over-moqt-00** (new-draft, score 9, adjacent_watchlist) [none]: [Model Context Protocol and Agent Skills over Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-jennings-agentproto-mcp-over-moqt/) — This document defines how to use Media over QUIC Transport (MOQT) as
   the underlying transport protocol for the Model Context Protocol
   (MCP).  MCP enables integration between language model applications
   and external data sources and tools.  MOQT provides publish-subscribe
   delivery over QUIC and WebTransport with native prioritization, relay
   caching, and multiplexing.

   This specification maps MCP messages onto MOQT objects and defines
   procedures for session establishment, capability discovery, and
   ongoing communication.  It covers MCP's core primitives (resources,
   tools, prompts, sampling, and notifications) through dedicated MOQT
   tracks.

   The document also describes Agent Skills -- composed instructions
   that extend AI capabilities beyond atomic tool operations -- using
   progressive loading aligned with MOQT's object-based delivery.
- **draft-mih-agent-bilateral-attestation-00** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
   action from an agent operated by another, today's record of that
   exchange — if one exists — is kept by one side, editable by that
   side, and deniable by the other.  Disputes reduce to my-log-versus-
   your-log.  This document describes a bilateral attestation exchange
   for such actions: the requesting organization signs a request
   attestation binding it to the action and its material terms; the
   performing organization evaluates the request against deterministic
   constraints at the boundary where the action takes effect and signs
   an action attestation recording the constraint results and the
   disposition — performed, declined, or escalated to a human — by
   reference to the request; and each party acknowledges the other's
   attestation.  The combined record binds each organization to its
   part, gives each proof of the other's, and can be anchored to a
   transparency service so that a third party who trusts neither
   organization can verify its integrity, timing, and both parties'
   signatures.  The exchange records refusals with the same fidelity as
   performance, and degrades gracefully when a counterparty cannot
   attest, marking the record's reduced assurance rather than blocking
   the transaction.
- **draft-wang-tls-service-affinity-05** (new-draft, score 9, authorization) [none]: [Service Affinity Solution based on Transport Layer Security (TLS)](https://datatracker.ietf.org/doc/draft-wang-tls-service-affinity/) — This draft proposes a service affinity solution between client and
   server based on Transport Layer Security (TLS).  It defines a minimal
   extension to TLS 1.3 by which a server instance can authorize a
   client to resume an established session on a different instance of
   the same service (for example, another node of a load-balanced
   cluster) and request, in band, that the client do so.  The relocation
   authorization is carried inside the server's own session ticket, so
   it inherits the security properties of TLS 1.3 ticket-based
   resumption.  The relocation target is an opaque value that either
   directly carries the switchover address (for example, an IP address
   and port) or is an identifier resolved by the application or control
   plane.

   This document also introduces a Reliable Framing Layer that operates
   above the TLS record layer to provide message framing, sequence
   numbering, acknowledgment tracking, and automatic retransmission.
   The Framing Layer ensures zero application data loss during TLS
   session migration by buffering unacknowledged data frames and
   retransmitting them to the new server endpoint after migration
   completes.
- **draft-wendt-stir-vesper-oob-03** (new-draft, score 9, adjacent_watchlist) [none]: [VESPER Out-of-Band OOB](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper-oob/) — This document describes a mechanism for delivering authenticated
   telephone call identity information using the VESPER framework for
   use where in-band signaling does not carry the identity end to end,
   or where there is no in-band path between the parties at all.  By
   supporting an out-of-band (OOB) transport model, this approach
   enables entities to publish and retrieve signed PASSporT assertions
   independent of end-to-end delivery within an in-band signaling path
   such as a SIP-based VoIP network.  These PASSporTs are signed with
   VESPER delegate certificates, which identify the entity holding the
   right-to-use for a telephone number and bind it to that entity's
   domain identity.  This document also introduces support for Connected
   Identity to the STIR OOB model, enabling the called party to respond
   with a signed PASSporT asserting its identity, thereby binding the
   identities of both parties to the transaction and enhancing end-to-
   end accountability.  The OOB mechanism provides a delivery path for
   PASSporTs where in-band delivery within a signaling path such as SIP
   is unavailable or is not the path used, enabling verifiers to confirm
   the association between the originating telephone number and the
   identity asserting authority as part of the broader VESPER trust
   framework.
- **draft-jms-mole-http-transport-00** (new-draft, score 8, core_identity) [none]: [MoLE HTTP Transport](https://datatracker.ietf.org/doc/draft-jms-mole-http-transport/) — MoLE targets browser deployments, so Clients, Anchors, and Moderators
   need an HTTP transport for the protocol flows defined by the
   architecture.

   This document defines the Mole HTTP authentication scheme, which
   carries challenges and presentations for the endorsement and
   credential flows, and the headers used to return credential material.
   The grant exchanges with the Anchor are defined per protocol in
   [PROTOCOLS].
- **draft-ritz-idpop-01** (new-draft, score 8, core_identity) [none]: [Interactive DPoP](https://datatracker.ietf.org/doc/draft-ritz-idpop/) — This document describes IDPoP, an extension to DPoP [RFC9449] that
   uses a key derivation scheme to separate access control from
   identity.  It mitigates credential exfiltration risks by requiring
   fresh hardware attestation to unseal identity keys via an interactive
   challenge.

## Monitor

- **draft-ietf-dance-client-auth-12** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document updates RFC 6698 and RFC 7671.  It describes how to use the
   TLSA record to publish client certificates or public keys, and also
   the rules and considerations for using them with TLS.  In addition,
   it defines a new TLS extension, DANE Client Identity, to convey the
   client's domain name identity to the server.
- **draft-ietf-jose-hpke-pq-pqt-01** (new-draft, score 6, verifiable_claims) [jose]: [JOSE HPKE PQ & PQ/T Algorithm Registrations](https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-pq-pqt/) — This document registers Post-Quantum (PQ) and Post-Quantum/
   Traditional (PQ/T) hybrid algorithm identifiers for use with JSON
   Object Signing and Encryption (JOSE), building on the Hybrid Public
   Key Encryption (HPKE) framework.
- **draft-ietf-lake-edhoc-grease-03** (new-draft, score 6, authorization) [lake]: [Applying Generate Random Extensions And Sustain Extensibility (GREASE) to EDHOC Extensibility](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-grease/) — This document applies the extensibility mechanism GREASE (Generate
   Random Extensions And Sustain Extensibility), which was pioneered for
   TLS, to the ecosystem of Ephemeral Diffie-Hellman Over COSE (EDHOC).
   It reserves a set of External Authorization Data (EAD) labels and
   unusable cipher suites that may be included in messages to ensure
   peers correctly handle unknown values.
- **draft-ietf-tls-mldsa-05** (new-draft, score 6, core_identity) [tls]: [Use of ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/) — This memo specifies how the post-quantum signature scheme ML-DSA
   (FIPS 204) is used for authentication in TLS 1.3.
- **draft-ietf-webtrans-http3-16** (new-draft, score 6, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/) — WebTransport over HTTP/3 is a binding of the WebTransport protocol
   framework [OVERVIEW] to HTTP/3 [HTTP3].  It provides support for
   unidirectional streams, bidirectional streams, and datagrams, all
   multiplexed within the same HTTP/3 connection.  WebTransport enables
   application clients constrained by the Web security model to
   communicate with a remote application server using a secure
   multiplexed transport.
- **draft-ietf-webtrans-overview-13** (new-draft, score 6, adjacent_watchlist) [webtrans]: [The WebTransport Protocol Framework](https://datatracker.ietf.org/doc/draft-ietf-webtrans-overview/) — The WebTransport Protocol Framework enables clients constrained by
   the Web security model to communicate with a remote server using a
   secure multiplexed transport.  It consists of a set of individual
   protocols that are safe to expose to untrusted applications, combined
   with an abstract model that allows them to be used interchangeably.

   This document defines the overall requirements on the protocols used
   in WebTransport, as well as the common features of the protocols,
   support for some of which is optional.
- **draft-usama-seat-intra-vs-post-04** (new-draft, score 6, trust_infrastructure) [none]: [Pre-, Intra- and Post-handshake Attestation](https://datatracker.ietf.org/doc/draft-usama-seat-intra-vs-post/) — This document presents a taxonomy of extending TLS protocol with
   remote attestation, referred to as attested TLS.  It also presents
   high-level analysis of benefits and limitations of each category,
   namely pre-handshake attestation, intra-handshake attestation and
   post-handshake attestation.  It also captures the opinions of the WG
   participants in order to build consensus towards solutions.  It also
   discussed tradeoffs and scalability.
- **draft-wendt-stir-tn-domain-binding-00** (new-draft, score 6, core_identity) [none]: [Binding a Domain Identifier to Telephone Number Authority in STIR Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-tn-domain-binding/) — This document defines a mechanism for binding a domain identifier to
   telephone number authority within a STIR certificate.  A certificate
   produced under this mechanism carries, as a co-validated pair, the
   telephone numbers or service provider codes a subject is authorized
   for in a TNAuthList extension and a domain the subject controls in a
   SubjectAltName dNSName entry.  The binding is established at issuance
   by requiring proof of domain control and validation of a TNAuthList
   authority token within a single certificate issuance, such that the
   resulting certificate attests that the same entity holds both.  The
   mechanism applies to STIR certificates whose TNAuthList contains
   telephone number entries, service provider code entries, or both,
   allowing a domain to be bound to the right-to-use holder for a set of
   numbers or to the provider identified by a service provider code.
   This document defines the issuance conformance requirements and the
   relying party verification rule that together make the binding
   meaningful.  It does not define telephone number or service provider
   code authorization or domain validation, both of which are specified
   elsewhere and referenced here.
- **draft-bubblefish-npamp-01** (new-draft, score 5, core_identity) [none]: [N-PAMP: Native Post-Quantum Agent Messaging Protocol](https://datatracker.ietf.org/doc/draft-bubblefish-npamp/) — The Native Post-Quantum Agent Messaging Protocol (N-PAMP) is a
   binary, multi-channel, wire-level protocol for authenticated
   communication between autonomous software agents.  N-PAMP operates
   beneath application-layer agent protocols and provides a single
   fixed-size frame format, a registry of multiplexed channels, and
   three escalating security profiles (Standard, High, and Sovereign)
   built on standard post-quantum and classical cryptography.  The
   protocol uses a hybrid key-encapsulation mechanism combining X25519
   with ML-KEM, authenticated encryption with associated data, and a
   forward-secure key schedule.  N-PAMP runs over QUIC as its primary
   transport and over TCP with TLS 1.3 as a fallback, negotiated via the
   Application-Layer Protocol Negotiation (ALPN) identifier "n-pamp/2".
   This document describes the wire format, channel architecture,
   profile negotiation, and cryptographic suites of N-PAMP, and reserves
   code-point ranges for extensions defined in companion specifications.
- **draft-calabria-bmwg-ai-fabric-training-bench-03** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
   Key Performance Indicators (KPIs) for evaluating Ethernet-based AI
   training network fabrics.

   As large-scale distributed Artificial Intelligence / Machine Learning
   (AI/ML) training clusters grow to tens of thousands of accelerators
   (GPUs or generic accelerator processing units (XPUs)), the backend
   network fabric determines Job Completion Time (JCT), training
   throughput, and accelerator utilization.

   This document establishes vendor-independent, reproducible test
   procedures for benchmarking fabric-level performance under realistic
   AI training workloads.  The tests cover Remote Direct Memory Access
   (RDMA) over Converged Ethernet version 2 (RoCEv2) transport, the
   Ultra Ethernet Transport (UET) protocol defined by the Ultra Ethernet
   Consortium (UEC) Specification 1.0 [UEC-1.0], congestion management
   (Priority Flow Control (PFC), Explicit Congestion Notification (ECN),
   Data Center Quantized Congestion Notification (DCQCN), Credit-Based
   Flow Control (CBFC)), load balancing strategies (Equal-Cost Multi-
   Path (ECMP), Dynamic Load Balancing (DLB), packet spraying),
   collective communication patterns (AllReduce, AllToAll, AllGather),
   and scale/soak testing.

   The methodology enables direct, reproducible comparison across switch
   ASICs, NIC transport stacks (RoCEv2 and UET), and fabric
   architectures (2-tier Clos, 3-tier Clos, and rail-optimized).
- **draft-cxxx-nmrg-ai4ibn-00** (new-draft, score 5, agent_identity) [none]: [Agentic AI for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-cxxx-nmrg-ai4ibn/) — This document specifies how the rise of agentic AI and LLMs can
   impact and and accelerate the transition towards Intent-Based
   Networking.
   Specifically, it revisits functionality and liefecycle in IBN, as
   defined in [RFC9315], and outlines how agentic AI and LLMs can be
   leveraged.
- **draft-jakab-dawn-agent-discovery-mdns-00** (new-draft, score 5, adjacent_watchlist) [none]: [Zero-Configuration Agent Discovery](https://datatracker.ietf.org/doc/draft-jakab-dawn-agent-discovery-mdns/) — Protocols for communication between autonomous software agents
   typically discover agents through documents retrieved over HTTPS from
   a well-known URI.  This model requires a discovering party to already
   know an agent's host name or URL, or to consult a centralized
   catalog.  It provides no zero-configuration mechanism for enumerating
   agents that are present on a local network.

   This document describes how existing, widely deployed protocols,
   Multicast DNS (mDNS) and DNS-Based Service Discovery (DNS-SD), can be
   used to advertise and discover agents on a local link, with no new
   protocol machinery.  It presents a general, protocol-independent two-
   stage discovery model in which lightweight enumeration over DNS-SD is
   followed by retrieval of full agent metadata over the agent's native
   transport.  It gives a worked instantiation of that model for the
   Agent2Agent (A2A) protocol, as an example.
- **draft-janz-nmrg-ontology-reconciliation-01** (new-draft, score 5, adjacent_watchlist) [none]: [Automated Agent-to-Agent Ontology Reconciliation for Cognitive Network Management Systems](https://datatracker.ietf.org/doc/draft-janz-nmrg-ontology-reconciliation/) — This document describes a possible direction for inter-system
   communication in network management, in which two cognitive software
   agents establish between themselves the basis for exchanging
   information, without depending on a single rigid data model agreed by
   their implementers in advance.  The agents bring relevant knowledge,
   can extend it through learning, can reason, and can converse in
   natural language.  The approach is framed as a workflow in which each
   agent makes explicit the ontology implicit in its data model, the two
   agents address their differences through conversation, and a
   translator artefact is produced that is then used during ordinary
   operation.  A central property is that language-model inference is
   consumed during the agents' conversation rather than on each
   subsequent message.  The document situates the direction relative to
   adjacent work and illustrates it through three use cases drawn from
   network management.
- **draft-jms-mole-architecture-00** (new-draft, score 5, adjacent_watchlist) [none]: [Moderation of unLinkable Endorsements (MoLE) Architecture](https://datatracker.ietf.org/doc/draft-jms-mole-architecture/) — Moderation of unLinkable Endorsements (MoLE) is an architecture that
   lets a party performing access control (a Moderator) bootstrap trust
   in a client from a third party (an Anchor) that already has a trust
   relationship with that client, and then adjust that trust over time
   in response to the client's behaviour, for example by dynamically
   rate-limiting access.

   MoLE targets open deployments, in which independent parties may be
   responsible for access control and for vouching for clients, whilst
   maintaining strong privacy protections for clients.  These
   protections are designed to hold even if participants in the
   ecosystem collude or otherwise misbehave.

   This document specifies the roles, the information flows between
   them, the privacy and security requirements, and deployment
   considerations.
- **draft-jms-mole-protocols-00** (new-draft, score 5, verifiable_claims) [none]: [MoLE Protocols](https://datatracker.ietf.org/doc/draft-jms-mole-protocols/) — This document defines protocols that instantiate the MoLE
   architecture: two endorsement protocols, by which a Client proves to
   a Moderator that it holds an Endorsement from a trusted Anchor
   without revealing which one, and three credential protocols, by which
   a Moderator issues, verifies, and updates per-Client state without
   being able to link presentations.  It also establishes the registries
   that identify these protocols.
- **draft-fane-ai-safety-txt-00** (new-draft, score 4, adjacent_watchlist) [none]: [The ai-safety.txt Domain AI Safety Declaration](https://datatracker.ietf.org/doc/draft-fane-ai-safety-txt/) — This document defines ai-safety.txt, a plain-text declaration format
   that a domain publishes at a well-known location to communicate its
   AI-safety posture to autonomous agents and agent-driven browsers.
   Modeled on the robots.txt convention, an ai-safety.txt file lets a
   domain assert, in a machine-readable form, whether its content is
   safe for autonomous agent consumption, whether that content is
   hardened against prompt injection, and whether it is rendered
   consistently to human and agent user agents.  The file also carries a
   security contact, a link to an external verification record, and the
   date the declaration was last verified.

   The declarations in an ai-safety.txt file are self-asserted by the
   publishing domain.  This document specifies the file format and its
   well-known location, and it is explicit that a consuming agent treats
   a declaration as a hint rather than as proof, verifying it against
   independent evidence where such evidence is available.
- **draft-gebauer-iacp-02** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol](https://datatracker.ietf.org/doc/draft-gebauer-iacp/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
   faced with challenges that it has had to overcome—and has overcome.
   Year after year, the number of users has grown, and year after year,
   the complexity and range of ways in which the internet can be used
   have expanded.  With the advent of AI, we not only have a new type of
   user, we have a different form of communication; the internet itself
   is being attributed a completely different significance.  If they are
   not already, AIs will make up the majority of internet users in the
   foreseeable future.  The question of an ‘AgentNet,’ is not merely a
   question concerning the internet; it is a question of how AIs will
   interact within a global network in the future.
- **draft-ietf-plants-merkle-tree-certs-05** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
   certificates which integrate public logging of the certificate, in
   the style of Certificate Transparency.  The integrated design reduces
   logging overhead in the face of both shorter-lived certificates and
   large post-quantum signature algorithms, while still achieving
   comparable security properties to existing X.509 constructions and
   Certificate Transparency.  Merkle Tree certificates additionally
   admit an optional size optimization that avoids signatures
   altogether, at the cost of only applying to up-to-date relying
   parties and older certificates.

## Adjacent / watchlist

- **draft-beeram-teas-yang-mpted-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Multipath Traffic Engineering Directed Acyclic Graph (MPTED) Tunnels and Junctions](https://datatracker.ietf.org/doc/draft-beeram-teas-yang-mpted/) — This document defines a YANG data model for representing, retrieving,
   and manipulating Multipath Traffic Engineering Directed Acyclic Graph
   (MPTED) Tunnels and Junctions.  The model includes two YANG modules,
   one for managing MPTED Tunnels on an MPTED tunnel originator node and
   the other for managing MPTED Junctions on an MPTED junction node.
- **draft-bormann-asdf-sdf-compact-10** (new-draft, score 3, adjacent_watchlist) [asdf]: [Semantic Definition Format (SDF) for Data and Interactions of Things: Compact Notation](https://datatracker.ietf.org/doc/draft-bormann-asdf-sdf-compact/) — The Semantic Definition Format (SDF) is a format for domain experts
   to use in the creation and maintenance of data and interaction models
   that describe Things, i.e., physical objects that are available for
   interaction over a network.  It was created as a common language for
   use in the development of the One Data Model liaison organization
   (OneDM) definitions.  Tools convert this format to database formats
   and other serializations as needed.

   The SDF format is mainly intended for interchange between machine
   generation and machine processing.  However, there is often a need
   for humans to look at and edit SDF models.

   Similar to the way Relax-NG as defined in ISO/IEC 19757-2 has an XML-
   based format and a compact format (its Annex C), this specification
   defines a compact format to go along SDF's JSON-based format.


   // The present version of this document is mostly a proof of concept;
   // it received positive initial feedback on the approach taken and is
   // awaiting completion of the initial implementation.
- **draft-busi-nmop-simap-rfc8795-applicability-02** (new-draft, score 3, adjacent_watchlist) [none]: [Applicability of RFC8795 YANG data model to SIMAP](https://datatracker.ietf.org/doc/draft-busi-nmop-simap-rfc8795-applicability/) — This document analyses the applicability of the RFC 8795 YANG data
   model to Service & Infrastructure Maps (SIMAP) and in particular
   analysis which requirements can be supported by the existing YANG
   data model defined in RFC 8795.
- **draft-gong-spring-sr-policy-group-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for SR Policy Group](https://datatracker.ietf.org/doc/draft-gong-spring-sr-policy-group-yang/) — This document defines YANG data models for Segment Routing (SR)
   Policy group that can be used for configuring, instantiating, and
   managing SR Policy groups. The model is generic and apply equally to
   the MPLS and SRv6 instantiations of SR policy groups.
- **draft-havel-nmop-simap-yang-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP).  It extends the RFC8345 YANG modules to support all
   SIMAP requirements.  This document will only focus on modelling
   proposal for each of the requirements not supported by RFC8345.  Any
   related terminology, concepts, use cases and requirements are defined
   outside of this draft and this draft will only refer to them, analyze
   how to model and propose the implementation solutions.
- **draft-huque-dnsop-multi-alg-rules-08** (new-draft, score 3, adjacent_watchlist) [none]: [Multiple Algorithm Rules in DNSSEC](https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/) — This document restates the requirements on DNSSEC signing and
   validation and makes small adjustments in order to allow for more
   flexible handling of configurations that advertise multiple Secure
   Entry Points (SEP) with different signing algorithms via their DS
   record or trust anchor set.  The adjusted rules allow both for multi-
   signer operation and for the transfer of signed DNS zones between
   providers, where the providers support disjoint DNSSEC algorithm
   sets.  In addition, the proposal enables pre-publication of a trust
   anchor in preparation for an algorithm rollover, such as of the root
   zone.

   This document updates RFCs 4035 and 6840.
- **draft-ietf-cats-oam-fw-00** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections encompassing clients, network paths, and service
   instances.
- **draft-ietf-ccwg-bbr-06** (new-draft, score 3, adjacent_watchlist) [ccwg]: [BBR Congestion Control](https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/) — This document specifies the BBR congestion control algorithm.  BBR
   ("Bottleneck Bandwidth and Round-trip propagation time") uses recent
   measurements of a transport connection's delivery rate, round-trip
   time, and packet loss rate to build an explicit model of the network
   path.  BBR then uses this model to control both how fast it sends
   data and the maximum volume of data it allows in flight in the
   network at any time.  Relative to loss-based congestion control
   algorithms such as Reno [RFC5681] or CUBIC [RFC9438], BBR offers
   substantially higher throughput for bottlenecks with shallow buffers
   or random losses, and substantially lower queueing delays for
   bottlenecks with deep buffers (avoiding "bufferbloat").  BBR can be
   implemented in any transport protocol that supports packet-delivery
   acknowledgment.  Thus far, open source implementations are available
   for TCP [RFC9293] and QUIC [RFC9000].  This document specifies
   version 3 of the BBR algorithm, BBRv3.
- **draft-ietf-core-responses-01** (new-draft, score 3, adjacent_watchlist) [core]: [CoAP: Non-traditional Response Forms](https://datatracker.ietf.org/doc/draft-ietf-core-responses/) — In CoAP as defined by RFC 7252, there is generally one response for
   each request.  Various CoAP extensions have individually relaxed that
   practice.  The present memo presents a generalized model beyond 1:1
   responses, describes different forms in which it can be used, and
   introduces new CoAP Options that make use of that model.

   Beyond that, this document provides implementation guidance to
   simplify prior extensions, and outlines future possibilities of using
   it.


   // This revision -01 has been created as discussion input for IETF
   // 126.  It makes a first attempt to sort the proposals into short-
   // term actionable ones and more long-term considerations for more
   // kinds of responses that could help additional use cases through
   // future work.
- **draft-ietf-dmm-mts-02** (new-draft, score 3, adjacent_watchlist) [dmm]: [Mobile Traffic Steering](https://datatracker.ietf.org/doc/draft-ietf-dmm-mts/) — The evolution of cellular mobile communication systems is aligned
   with an increasing demand for customized deployments, energy
   efficiency, dynamic re-configurability and the integration and use of
   other network technologies, such as non-cellular radio access
   technologies and non-terrestrial networks.  In order to achieve and
   maintain the expected service quality and continuity, such systems
   should be designed and controllable end-to-end, taking all involved
   network domains and segments into account.  This document discusses
   an end-to-end system from an advanced use cases perspective and
   substantiates the demand for solutions to share information and
   enable control interfaces between all connected network domains,
   including the mobile communication system and the transport network
   that stretches up to the data networks that host service instances.
   In the view of flexible implementations and deployment, two
   architectural principles, leveraging either a dedicated controller or
   a decentralized control plane, are described and discussed,
   accompanied by operational aspects and an associated information
   model that enable end-to-end mobile traffic treatment and steering in
   such complex and dynamically changing networks.
- **draft-ietf-httpapi-patch-byterange-04** (new-draft, score 3, adjacent_watchlist) [httpapi]: [Byte Range PATCH](https://datatracker.ietf.org/doc/draft-ietf-httpapi-patch-byterange/) — This document specifies a media type for PATCH payloads that
   overwrites a specific byte range, facilitating random access writes
   and segmented uploads of resources.
- **draft-ietf-httpbis-resumable-upload-12** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
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
- **draft-ietf-jose-hpke-encrypt-22** (new-draft, score 3, adjacent_watchlist) [jose]: [Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/) — This specification defines how to use Hybrid Public Key Encryption
   (HPKE) with JSON Web Encryption (JWE).  HPKE enables public key
   encryption of arbitrary-sized plaintexts to a recipient's public key,
   and provides security against adaptive chosen ciphertext attacks.
   This specification chooses a specific subset of the HPKE features to
   use with JWE.

   This specification updates RFC 7516 (JWE) to enable use of Integrated
   Encryption as a Key Management Mode.
- **draft-ietf-masque-http-datagram-compression-01** (new-draft, score 3, adjacent_watchlist) [masque]: [Extensions to Compress and Derive Fields in HTTP Datagrams](https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/) — This document defines extensions for HTTP Datagram-based protocols
   that improve transmission efficiency by introducing templates for
   compressing or deriving datagram fields.

   These templates allow endpoints to define parts of datagrams that are
   static and can be removed, and other parts that can be derived (such
   as packet lengths and checksum values).

   Additionally, this document defines a checksum offload procedure
   enabling receivers to complete Internet checksums using sender-
   provided partial values.

   These optimisations reduce per-packet overhead, processing cost, and
   increase the effective maximum transmission unit (MTU) when datagrams
   are encapsulated in QUIC DATAGRAM frames.
- **draft-ietf-masque-quic-proxy-09** (new-draft, score 3, adjacent_watchlist) [masque]: [QUIC-Aware Proxying Using HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-quic-proxy/) — This document extends UDP Proxying over HTTP to add optimizations for
   proxied QUIC connections.  Specifically, it allows a proxy to reuse
   UDP 4-tuples for multiple proxied connections, and adds a mode of
   proxying in which QUIC short header packets can be forwarded and
   transformed through a HTTP/3 proxy rather than being fully re-
   encapsulated and re-encrypted.
- **draft-ietf-mimi-room-policy-04** (new-draft, score 3, adjacent_watchlist) [mimi]: [Room Policy for the More Instant Messaging Interoperability (MIMI) Protocol](https://datatracker.ietf.org/doc/draft-ietf-mimi-room-policy/) — This document describes a set of concrete room policies for the More
   Instant Messaging Interoperability (MIMI) Working Group.  It
   describes several independent properties and policy attributes which
   can be combined to model a wide range of chat and multimedia
   conference types.
- **draft-ietf-netmod-sub-intf-vlan-model-18** (new-draft, score 3, adjacent_watchlist) [netmod]: [Sub-interface VLAN YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-netmod-sub-intf-vlan-model/) — This document defines YANG modules to add support for classifying
   traffic received on interfaces as Ethernet/VLAN framed packets to
   sub-interfaces based on the fields available in the Ethernet/VLAN
   frame headers.  These modules allow configuration of Layer 3 (L3) and
   Layer 2 (L2) sub-interfaces (e.g., L2VPN attachment circuits) that
   can interoperate with IETF based forwarding protocols, such as IP and
   L3VPN services, or L2VPN services like Virtual Private Wire Service
   (VPWS), Virtual Private LAN Service (VPLS), and EVPN.  The sub-
   interfaces also interoperate with VLAN tagged traffic originating
   from an IEEE 802.1Q compliant bridge.

   The model differs from an IEEE 802.1Q bridge model in that the
   configuration is interface/sub-interface based as opposed to being
   based on membership of an 802.1Q VLAN bridge.

   The YANG data models in this document conforms to the Network
   Management Datastore Architecture (NMDA) defined in RFC 8342.
- **draft-ietf-netmod-yang2-00** (new-draft, score 3, adjacent_watchlist) [netmod]: [The YANG 2.0 Data Modeling Language](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/) — YANG is a data modeling language used to model configuration data,
   state data, Remote Procedure Calls, and notifications for network
   management protocols.  This document describes the syntax and
   semantics of version 2.0 of the YANG language.  YANG version 2.0 is a
   major release of the YANG language, addressing issues found in the
   original specification.
- **draft-ietf-ppm-dap-19** (new-draft, score 3, adjacent_watchlist) [ppm]: [Distributed Aggregation Protocol for Privacy Preserving Measurement](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/) — There are many situations in which it is desirable to take
   measurements of data which people consider sensitive.  In these
   cases, the entity taking the measurement is usually not interested in
   people's individual responses but rather in aggregated data.
   Conventional methods require collecting individual responses and then
   aggregating them on some server, thus representing a threat to user
   privacy and rendering many such measurements difficult and
   impractical.  This document describes a multi-party Distributed
   Aggregation Protocol (DAP) for privacy preserving measurement which
   can be used to collect aggregate data without revealing any
   individual contributor's data.
- **draft-ietf-spring-sr-policy-yang-08** (new-draft, score 3, adjacent_watchlist) [spring]: [YANG Data Model for Segment Routing Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-yang/) — This document defines a YANG data model for Segment Routing (SR)
   Policy that can be used for configuring, instantiating, and managing
   SR policies.  The model is generic and applies equally to the MPLS
   and SRv6 instantiations of SR policies.
- **draft-ietf-stir-certificates-shortlived-06** (new-draft, score 3, core_identity) [stir]: [Short-Lived Certificates for Secure Telephone Identity](https://datatracker.ietf.org/doc/draft-ietf-stir-certificates-shortlived/) — When certificates are used as credentials to attest the assignment of
   ownership of telephone numbers, some mechanism is required to provide
   certificate freshness.  This document specifies short-lived
   certificates as a means of guaranteeing certificate freshness for
   secure telephone identity (STIR), potentially relying on the
   Automated Certificate Management Environment (ACME) or similar
   mechanisms to allow signers to acquire certificates as needed.
- **draft-ietf-teas-composite-network-slices-01** (new-draft, score 3, core_identity) [teas]: [Realization of Composite IETF Network Slices](https://datatracker.ietf.org/doc/draft-ietf-teas-composite-network-slices/) — A network slice offers connectivity services to a network slice
   customer with specific Service Level Objectives (SLOs) and Service
   Level Expectations (SLEs) over a common underlay network.  RFC 9543
   describes a framework for network slices built in networks that usWe
   IETF technologies.  As part of that framework, the Network Resource
   Partition (NRP) is introduced as a collection of network resources
   that are allocated from the underlay network to carry a specific set
   of network slice service traffic and meet specific SLOs and SLEs.  In
   some network scenarios, network slices using IETF technologies may
   span multiple network domains, and they may be composed
   hierarchically, which means a network slice itself may be further
   sliced.  In the context of 5G, a 5G end-to-end network slice consists
   of three different types of network technology segments: Radio Access
   Network (RAN), Transport Network (TN) and Core Network (CN).  The
   transport segments of the 5G end-to-end network slice can be provided
   using network slices described in RFC 9543.

   This document first describes the possible use cases of composite
   network slices built in networks that use IETF network technologies,
   then it provides considerations about the realization of composite
   network slices.  For the multi-domain network slices, an Inter-Domain
   Network Resource Partition Identifier (Inter-domain NRP ID) may be
   introduced.  For hierarchical network slices, the structure of the
   NRP ID is discussed.  And for the interaction between IETF network
   slices with 5G network slices, the identifiers of the 5G network
   slices may be introduced into IETF networks.  These network slice-
   related identifiers may be used in the data plane, control plane and
   management plane of the network for the instantiation and management
   of composite network slices.  This document also describes the
   management considerations of composite network slices.
- **draft-ietf-tls-pake-02** (new-draft, score 3, adjacent_watchlist) [tls]: [A Password Authenticated Key Exchange Extension for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-pake/) — The pre-shared key mechanism available in TLS 1.3 is not suitable for
   usage with low-entropy keys, such as passwords entered by users.
   This document describes an extension that enables the use of
   password-authenticated key exchange protocols with TLS 1.3.
- **draft-ietf-tls-rfc9147bis-02** (new-draft, score 3, adjacent_watchlist) [tls]: [The Datagram Transport Layer Security (DTLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-rfc9147bis/) — This document specifies version 1.3 of the Datagram Transport Layer
   Security (DTLS) protocol.  DTLS 1.3 allows client/server applications
   to communicate over the Internet in a way that is designed to prevent
   eavesdropping, tampering, and message forgery.

   The DTLS 1.3 protocol is based on the Transport Layer Security (TLS)
   1.3 protocol and provides equivalent security guarantees with the
   exception of order protection / non-replayability.  Datagram
   semantics of the underlying transport are preserved by the DTLS
   protocol.

   This document obsoletes RFC 6347.
- **draft-ietf-webtrans-http2-15** (new-draft, score 3, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/2](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http2/) — WebTransport defines a set of low-level communications features
   designed for client-server interactions that are initiated by Web
   clients.  This document describes a protocol that can provide the
   capabilities of WebTransport over HTTP/2.  This protocol enables the
   use of WebTransport when a UDP-based protocol is not available.
- **draft-intra-handshake-fail-00** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake.fail (CVE-2026-33697 of CVSS 7.5)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697, which
   is substantial technical evidence of how intra-handshake attestation
   fails in practice.
- **draft-irtf-cfrg-bls-signature-07** (new-draft, score 3, adjacent_watchlist) [cfrg]: [BLS Signatures](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bls-signature/) — BLS is a digital signature scheme with aggregation properties.  Given
   set of signatures (signature_1, ..., signature_n) anyone can produce
   an aggregated signature.  Aggregation can also be done on secret keys
   and public keys.  Furthermore, the BLS signature scheme is
   deterministic, non-malleable, and efficient.  Its simplicity and
   cryptographic properties allows it to be useful in a variety of use-
   cases, specifically when minimal storage space or bandwidth are
   required.
- **draft-irtf-cfrg-concrete-hybrid-kems-04** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Concrete Hybrid PQ/T Key Encapsulation Mechanisms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-concrete-hybrid-kems/) — PQ/T Hybrid Key Encapsulation Mechanisms (KEMs) combine "post-
   quantum" cryptographic algorithms, which are safe from attack by a
   quantum computer, with "traditional" algorithms, which are not.  CFRG
   has developed a general framework for creating hybrid KEMs.  In this
   document, we define concrete instantiations of this framework to
   illustrate certain properties of the framework and simplify
   implementors' choices.
- **draft-irtf-cfrg-cryptography-specification-03** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Guidelines for Writing Cryptography Specifications](https://datatracker.ietf.org/doc/draft-irtf-cfrg-cryptography-specification/) — This document provides guidelines and best practices for writing
   technical specifications for cryptography protocols and primitives,
   targeting the needs of implementers, researchers, and protocol
   designers.  It highlights the importance of technical specifications
   and discusses strategies for creating high-quality specifications
   that cater to the needs of each community, including guidance on
   representing mathematical operations, security definitions, and
   threat models.
- **draft-irtf-cfrg-hybrid-kems-12** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Hybrid PQ/T Key Encapsulation Mechanisms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-hybrid-kems/) — This document defines generic constructions for hybrid Key
   Encapsulation Mechanisms (KEMs) based on combining a post-quantum
   (PQ) KEM with a traditional cryptographic component.  Hybrid KEMs
   built using these constructions provide strong security properties as
   long as either of the underlying algorithms are secure.
- **draft-jadoon-green-isac-utilization-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Reporting Utilization Scores in ISAC](https://datatracker.ietf.org/doc/draft-jadoon-green-isac-utilization/) — This document defines a YANG data model to report an ISAC Utilization
   Score (US) in Integrated Sensing and Communication (ISAC) systems.
   The US is an abstract, normalized score (0..100) that summarizes the
   relative resource cost of executing a sensing operation on a device.

   The model supports a mandatory overall US and optional explanatory
   component impact scores (compute, memory, energy, storage, latency).
   The model also supports optional metadata (e.g., timestamp,
   aggregation window, and scoring method identification) describing how
   a reported score was derived.

   This revision aligns terminology and leaf names to reduce ambiguity
   between normalized impact scores and raw resource telemetry, removes
   per-measurement-related objects to keep the model focused on an
   overall score, and specifies a companion augmentation module (Path 1)
   that attaches ISAC utilization telemetry to a GREEN Energy Object (as
   defined by the GREEN Power and Energy YANG Module) for correlation
   with power/energy telemetry.
- **draft-lemmons-cose-composite-claims-03** (new-draft, score 3, verifiable_claims) [none]: [Composite Token Claims](https://datatracker.ietf.org/doc/draft-lemmons-cose-composite-claims/) — Composite claims are claims for CBOR Web Tokens (CWTs) and JSON Web
   Tokens (JWTs) that define logical relationships between sets of
   claims.  This document also defines a CWT representation of the
   "crit" (Critical) claim.
- **draft-lg-lsr-router-id-conflict-detect-00** (new-draft, score 3, core_identity) [none]: [Detection of Router-ID Conflicts in IGPs](https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/) — In link-state Interior Gateway Protocols (IGPs) such as OSPF and IS-
   IS, the router ID (or system ID) serves as a unique identifier for
   routers within a routing domain. Duplicate router IDs can lead to
   severe network instability, including persistent Link State
   Advertisement (LSA/LSP) flooding, inconsistent Link State Databases
   (LSDBs), and permanent forwarding loops.

   This document defines mechanisms for detecting such conflicts
   between non-adjacent routers and proposes procedures to alert
   network operators, along with defining the corresponding YANG
   interface and event YANG notifications for OAM operations.
- **draft-mahy-mimi-identity-05** (new-draft, score 3, core_identity) [none]: [More Instant Messaging Interoperability (MIMI) Identity Concepts](https://datatracker.ietf.org/doc/draft-mahy-mimi-identity/) — This document explores the problem space in instant messaging (IM)
   identity interoperability when using end-to-end encryption, for
   example with the MLS (Message Layer Security) Protocol.  It also
   describes naming schemes for different types of IM identifiers.
- **draft-melegassi-coherence-bfd-01** (new-draft, score 3, trust_infrastructure) [none]: [Coherence-BFD: Sub-Second Coherence Detection Using Bidirectional Forwarding Detection Patterns](https://datatracker.ietf.org/doc/draft-melegassi-coherence-bfd/) — This document specifies Coherence-BFD, a protocol that combines
   the asynchronous heartbeat, demand-mode, echo function, and
   detection-multiplier mechanisms of Bidirectional Forwarding
   Detection (BFD, [RFC5880]) with the multi-vantage path coherence
   detection of [I-D.melegassi-mvps-incremental-be].  The result is
   a sub-second coherence failure detector with theoretical and
   empirical detection latency of 55 ms (1091x faster than the
   60-second tick baseline of the underlying BE-MVPS framework).

   Five execution variants are specified: V0 (baseline), V1
   (heartbeat-fast), V2 (demand), V3 (echo), and V4 (hybrid).  Wall-
   clock benchmarks confirm V3 (Echo) as the latency-optimal variant
   at 55 ms median tau_detect with 39 680 B/s bandwidth.

   This revision (-01) adds three layers of proof:

     (a) Canonical: formal proofs of the detection lower-bound
         (Theorem T-BFD-1), false-positive-rate decay (Theorem
         T-BFD-2), and connection to the GDDP geometric-
         precision framework (Corollary C-BFD-3).

     (b) Empirical: SHA-256-anchored benchmark receipts
         reproducible from the public reference scripts.

     (c) Real data: validation against 92 067 RIPE Atlas RTT
         measurements from 450+ globally-distributed anchors
         spanning 2+ months of continuous collection.

   NOTE ON DATA PROVENANCE.  Wall-clock detection-latency and
   bandwidth numbers in Section 10 are obtained from controlled
   benchmarks (scripts/benchmark_coherence_bfd.py).  Real-data
   validation in Section 18 uses live Internet RTT measurements
   from RIPE Atlas to confirm that the theoretical bounds hold
   on operational paths.

   HARDWARE CAVEAT.  The 55 ms median tau_detect is a SOFTWARE-
   HARNESS measurement, not a router-class measurement.  Validation
   against real BFD hardware is identified as required future work
   before progression past Experimental status.
- **draft-ochkas-cose-ascon-04** (new-draft, score 3, verifiable_claims) [none]: [Ascon-AEAD128 and Ascon-Hash256 for COSE](https://datatracker.ietf.org/doc/draft-ochkas-cose-ascon/) — This document describes CBOR Object Signing and Encryption (COSE)
   serialization with Ascon, a NIST standard for lightweight
   cryptography.

   In 2019, as a part of CAESAR competition, Ascon-128 and Ascon-128a
   were selected as the first choice for the lightweight authenticated
   encryption.  After, in 2023, National Institute of Standards and
   Technology (NIST) selected Ascon family of cryptographic algorithms
   to be the standard for lightweight cryptography.  In August 2025,
   NIST Special Publication 800-232 was released, defining Ascon-based
   lightweight cryptography standards for constrained devices.  This
   recognition makes it particularly interesting to enable using Ascon
   with COSE structures.
- **draft-piraux-tcp-ao-tls-04** (new-draft, score 3, core_identity) [none]: [Opportunistic TCP-AO with TLS](https://datatracker.ietf.org/doc/draft-piraux-tcp-ao-tls/) — This document specifies an opportunistic mode for TCP-AO when used
   with TLS.  In this mode, the TCP connection starts with a well-known
   authentication key which is later replaced by a secure key derived
   from the TLS handshake.
- **draft-pocero-lake-authkemsig-edhoc-01** (new-draft, score 3, core_identity) [none]: [KEM/Signature-Based Methods for Scenarios with Asymmetric Device Constraints](https://datatracker.ietf.org/doc/draft-pocero-lake-authkemsig-edhoc/) — This document extends the KEM-based Authentication for EDHOC draft by
   defining additional quantum-resistant authentication methods that
   support combined authentication approaches, where one party
   authenticates using a KEM-based mechanism and the other using a post-
   quantum signature scheme.
- **draft-porfiri-tsvwg-sctp-dtls-handshake-01** (new-draft, score 3, core_identity) [none]: [Transport Layer Security (TLS) based key-management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/) — This document defines how Transport Layer Security (TLS) 1.3 is used
   as a key-management method for the SCTP DTLS Chunk mechanism.  It
   specifies how a TLS handshake establishes the initial security
   context for an SCTP association and how subsequent TLS handshakes
   provide key updates and re-authentication.  The goal is to enable
   authenticated and confidential communication over SCTP using the DTLS
   Chunk, leveraging standardized TLS 1.3 features for key management
   and rekeying.
- **draft-sardar-rats-sec-cons-04** (new-draft, score 3, trust_infrastructure) [none]: [Guidelines for Security Considerations of RATS](https://datatracker.ietf.org/doc/draft-sardar-rats-sec-cons/) — This document aims to provide guidelines and best practices for
   writing security considerations for technical specifications for RATS
   targeting the needs of implementers, researchers, and protocol
   designers.  In particular, it discusses some of the 'bottom turtle'
   issues.  This is a work-in-progress, and the current version mainly
   presents an outline of the topics that future versions will cover in
   more detail.

   *  Corrections in published RATS RFCs

   *  Security concerns in two RATS drafts

   *  General security guidelines, baseline, or template for RATS
- **draft-skyfire-oauth-kyapay-token-exchange-00** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-sriram-sidrops-asra-verification-05** (new-draft, score 3, authorization) [none]: [Autonomous System Relationship Authorization (ASRA) as an Extension to ASPA for Enhanced AS Path Verification](https://datatracker.ietf.org/doc/draft-sriram-sidrops-asra-verification/) — An Autonomous System Provider Authorization (ASPA) record authorizes
   provider ASes of a customer AS.  While ASPA-based AS_PATH
   verification can correctly detect and mitigate route leaks and some
   forged-origin or forged-path-segment hijacks, it fails to detect some
   malicious path manipulations for routes that are received from
   transit providers.  This document utilizes a new RPKI object called
   Autonomous System Relationship Authorization (ASRA) that
   significantly enhances AS_PATH verification complementing ASPA.  ASRA
   fills in a significant gap in the ASPA method by adding the
   capability to detect fake links in the AS_PATHs in BGP Updates
   propagated from providers to customers.  ASRA achieves this by
   allowing an AS to register additional AS relationships, i.e.,
   customers and lateral peers.
- **draft-sullivan-cfrg-raae-01** (new-draft, score 3, core_identity) [none]: [Random-Access Authenticated Encryption](https://datatracker.ietf.org/doc/draft-sullivan-cfrg-raae/) — This document defines random-access authenticated encryption (raAE),
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
- **draft-sullivan-mls-attachments-00** (new-draft, score 3, core_identity) [none]: [Encrypted Attachments for MLS](https://datatracker.ietf.org/doc/draft-sullivan-mls-attachments/) — This document defines random-access authenticated encryption of large
   write-once files for Messaging Layer Security (MLS) groups.  A file
   is encrypted so that a receiver can decrypt and authenticate any byte
   range without processing the whole file.  The encryption is SEAL-
   attachment, SEAL's named write-once attachment scheme (raAE),
   parameterized by the AEAD and key derivation function of the group's
   MLS cipher suite and keyed from the MLS exporter.  The encrypted
   bytes are carried by any means, and a recipient needs only a small
   reference (the object's identifier and length, and an optional
   locator) to fetch, key, and verify the object.  MLS application
   messages cannot carry large files, and existing attachment encryption
   produces an opaque, immutable blob with no partial access.  This
   extension supplies the random-access layer those uses need.
- **draft-tantsura-fann-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Fast Network Notifications](https://datatracker.ietf.org/doc/draft-tantsura-fann-yang/) — This document defines a YANG data model to Fast Network Notifictions.
- **draft-vos-cfrg-pqpake-02** (new-draft, score 3, core_identity) [none]: [Hybrid Post-Quantum Password Authenticated Key Exchange](https://datatracker.ietf.org/doc/draft-vos-cfrg-pqpake/) — This document describes the CPaceOQUAKE+ protocol, a hybrid
   asymmetric password-authenticated key exchange (aPAKE) that supports
   mutual authentication in a client-server setting secure against
   quantum-capable attackers.  CPaceOQUAKE+ is composed of two stages —
   CPace and OQUAKE+ — that run sequentially, with the output of CPace
   feeding as the secret_context into OQUAKE+. OQUAKE+ is an augmented
   variant of OQUAKE that adds password confirmation.  This document
   also describes standalone OQUAKE+, a post-quantum aPAKE, and
   CPaceOQUAKE, the hybrid symmetric PAKE composed of the CPace and
   OQUAKE stages.  This document recommends configurations for
   CPaceOQUAKE+.
- **draft-yang-dhc-dhcp-extension-00** (new-draft, score 3, adjacent_watchlist) [none]: [DHCP New Option Extension based on LLM Capability](https://datatracker.ietf.org/doc/draft-yang-dhc-dhcp-extension/) — This document specifies a DHCP option extension designed for campus
   networks to help client devices distinguish and connect to a master
   device with the LLM (Large Language Model).  The mechanism extends a
   new DHCP option containing two specific parameters within the DHCP
   payload: the master device's LLM address and the master device's LLM
   configuration.  This allows client devices to identify and register
   to LLM-enabled master device during the bootstrap phase.
- **draft-ybb-ccamp-service-path-computation-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Service Path Computation](https://datatracker.ietf.org/doc/draft-ybb-ccamp-service-path-computation/) — This document defines a YANG data model for client signal service's
   path computation and path management.
- **draft-yu-ccamp-resource-pm-yang-06** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Resource Performance Monitoring](https://datatracker.ietf.org/doc/draft-yu-ccamp-resource-pm-yang/) — This document defines a YANG data model for resource Performance
   Monitoring, applicable to network controllers, which provides the
   functionalities of retrieval of performance monitoring capabilities,
   TCA (Threshold Crossing Alert) configuration, current or history
   performance data retrieval, and performance monitoring task
   management.
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
- **draft-calabria-bmwg-ai-fabric-inference-bench-03** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
   Key Performance Indicators (KPIs) for evaluating Ethernet-based AI
   inference serving network fabrics.  As Large Language Model (LLM)
   inference deployments scale to disaggregated prefill/decode
   architectures spanning hundreds or thousands of accelerators (GPUs/
   XPUs), the interconnect fabric determines Time to First Token (TTFT),
   Inter-Token Latency (ITL), and aggregate throughput in tokens per
   second (TPS).  This document establishes vendor-independent,
   reproducible test procedures for benchmarking fabric-level
   performance under realistic AI inference workloads.

   Coverage includes RDMA-based KV cache transfer between disaggregated
   prefill and decode workers, Mixture-of-Experts (MoE) expert
   parallelism AllToAll communication, request routing and load
   balancing for inference serving, congestion management under bursty
   inference traffic patterns, and scale/soak testing.  The methodology
   enables direct comparison across NIC transport stacks (RoCEv2 and
   UET) and fabric architectures.

   This document is a companion to the AI training fabric benchmarking
   methodology, which addresses training workloads.
- **draft-calabria-bmwg-ai-fabric-terminology-03** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
   Ethernet-based network fabrics used in distributed Artificial
   Intelligence (AI) training and inference workloads.  It consolidates
   and extends terms from "Benchmarking Terminology for Network
   Interconnect Devices" (RFC 1242) and "Data Center Benchmarking
   Terminology" (RFC 8238).  Definitions cover collective communication
   primitives, RDMA transport mechanisms (RoCEv2 and Ultra Ethernet
   Transport), congestion control behaviors, AI-specific Key Performance
   Indicators (KPIs), and fabric topology concepts.

   This document is a companion to the AI training and inference fabric
   benchmarking methodology documents.  Those documents are intended to
   be read together with the terminology defined here.  Where
   definitions herein overlap with the foundational benchmarking
   terminology in RFC 1242 or RFC 8238, this document provides AI fabric
   context extensions and refinements; the foundational definitions in
   those RFCs remain authoritative for general network benchmarking.
- **draft-eckert-anima-ai4an-01** (new-draft, score 2, ignored_after_review) [none]: [AI for Autonomous Networking](https://datatracker.ietf.org/doc/draft-eckert-anima-ai4an/) — This document builds on the architectural foundation of the IETF
   ANIMA "Autonomous Network Infrastructure" to propose an architecture
   for in-network intelligence in support of network automation.

   The key aspect of this architecture is the use of AI programmed and
   validated software running decentralized on the network.
- **draft-gray-lamps-composite-fndsa-lms-00** (new-draft, score 2, ignored_after_review) [none]: [Composite FN-DSA and LMS Digital Signature Algorithm for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-gray-lamps-composite-fndsa-lms/) — This document defines a composite signature scheme combining the FN-
   DSA (Falcon) digital signature algorithm with the Leighton-Micali
   Signature (LMS) scheme defined in RFC 8554.  This construction is
   designed for use within X.509 Public Key Infrastructure (PKI) and
   follows the composite signature paradigm defined in
   [I-D.ietf-lamps-pq-composite-sigs].
- **draft-ietf-dnsop-delext-08** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFC 6895.
- **draft-kompella-lsr-mptecap-02** (new-draft, score 2, ignored_after_review) [none]: [Multipath Traffic Engineering Capabilities](https://datatracker.ietf.org/doc/draft-kompella-lsr-mptecap/) — Multipath Traffic Engineering (MPTE) combines two approaches to
   traffic management: equal-cost multipath and constraint-based traffic
   engineering, offering a powerful new way to engineer networks.  To
   avail of this, a node (possibly an ingress of a MPTE tunnel, or a
   path computation agent) must have information about the topology,
   link and node characteristics of a network so that it can compute the
   components of the MPTE tunnel.  One important (node) characteristic
   is whether a given node supports MPTE, i.e., whether it can
   participate in the provisioning and maintenance of an MPTE tunnel.

   Multicast TE (MCTE) offers a more efficient approach to traffic
   engineering for multicast traffic.  Again, an important node
   characteristic is whether a given node supports MCTE, i.e., whether
   it can participate in the provisioning and maintenance of an MCTE
   tunnel.

   This memo shows how these capabilities can be distributed in the IGP
   via Link State Routing TE Capabilities.
- **draft-liu-opsawg-stbl-req-per-packet-00** (new-draft, score 2, ignored_after_review) [none]: [Ability Requirements for Stability Guarantees in Per-packet Load Balancing Networks](https://datatracker.ietf.org/doc/draft-liu-opsawg-stbl-req-per-packet/) — Many per-packet load balancing mechanisms have been proposed to
   optimize the performance of AI networks.  However, per-packet load
   balancing poses significant challenges to network stability
   assurance.  This draft analyzes these challenges, as well as the
   ability requirements for stability guarantees in per-packet load
   balancing networks.
- **draft-mp-agntcy-ads-02** (new-draft, score 2, agent_identity) [none]: [Agent Directory Service](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/) — The Agent Directory Service (ADS) is a distributed directory service
   designed to store metadata for AI agent applications.  This metadata,
   stored as directory records, enables the discovery of agent
   applications with specific skills for solving various problems.  The
   implementation features distributed directories that interconnect
   through a content-routing protocol.
- **draft-yao-dawn-agent-discovery-architect-00** (new-draft, score 2, ignored_after_review) [none]: [DNS-like Agent Discovery Architecture](https://datatracker.ietf.org/doc/draft-yao-dawn-agent-discovery-architect/) — This document defines a DNS-like three-tier agent-discovery
   architecture for the Internet of Agents (IoA).  It introduces three
   core functional roles: Agent Root, Agent Registry, and Agent
   Resolver.

## Ignored after review

- **draft-admnr-lsr-igp-measurement-group-02** (new-draft, score 0, ignored_after_review) [none]: [Advertising IGP Measurement Group using TLV](https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/) — This document defines an IS-IS capability sub-TLV for advertising
   measurement group membership for Active Measurement Protocols (AMPs)
   such as TWAMP and STAMP.  The mechanism allows IGP routers to
   discover other routers participating in different measurement groups,
   enabling automatic discovery of measurement endpoints across IGP
   areas.  The solution uses interface addresses (IPv4 or IPv6) to
   identify measurement group membership, where the same interface
   address may be used for multiple measurement groups.
- **draft-ajp-spring-srv6-mpte-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6 for Multipath Traffic Engineering](https://datatracker.ietf.org/doc/draft-ajp-spring-srv6-mpte/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that enables weighted load
   balancing of unicast traffic across a constrained set of paths
   optimized for an objective.

   This document is informational and describes one realization approach
   for applying SRv6 semantics to MPTE, based on the Multipath Traffic
   Engineering Internet-Draft (draft-kompella-teas-mpte).  It
   summarizes associated procedures, lifecycle, management, and
   forwarding behavior.

   This document applies existing SRv6 architecture and semantics to
   MPTE without defining new SRv6 endpoint behaviors or signaling
   protocols.  It focuses on data-plane realization using existing
   forwarding instructions.
- **draft-ali-6man-srv6-vpn-icmp-error-handling-04** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling in SRv6 based VPN Networks](https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/) — The document specifies procedures for handling ICMP error in
   SRv6-based Virtual Private Network (VPN).
- **draft-ali-opsawg-yang-protobuf-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement: YANG Modeling for Protocol Buffer Based Network APIs](https://datatracker.ietf.org/doc/draft-ali-opsawg-yang-protobuf-problem-statement/) — Network devices increasingly expose management, telemetry, and
   dynamic service interfaces using gRPC and Protocol Buffers.  Many of
   these interfaces carry ephemeral or runtime state that is not
   intended to be stored as persistent configuration.  At the same time,
   the IETF has standardized YANG as the primary data modeling language
   for network management and operations.  This document describes the
   problem space and identifies questions for the IETF community
   regarding the role of YANG in defining interoperable Protocol Buffer
   based APIs.
- **draft-ali-pce-implicit-tls-profile-00** (new-draft, score 0, ignored_after_review) [none]: [A Policy-Driven Implicit TLS Transport Profile for PCEP](https://datatracker.ietf.org/doc/draft-ali-pce-implicit-tls-profile/) — RFC 8253 specifies the use of Transport Layer Security (TLS) for the
   Path Computation Element Communication Protocol (PCEP) by negotiating
   TLS using the PCEP StartTLS message exchange.  This document
   specifies a deployment profile for PCEP in which TLS is initiated
   immediately following TCP connection establishment based on local
   policy.

   This document is intended to simplify deployments where secure
   transport is mandatory.
- **draft-autocrypt-openpgp-v2-cert-03** (new-draft, score 0, ignored_after_review) [none]: [Autocrypt v2 OpenPGP Certificates and Transferable Secret Keys](https://datatracker.ietf.org/doc/draft-autocrypt-openpgp-v2-cert/) — This document describes the "Autocrypt v2 Certificate", a standard
   structure for an OpenPGP certificate for Internet messaging.  It
   offers defense against store-now-decrypt-later attacks from quantum
   computers through post-quantum hybrid cryptography.  It also enables
   reliable deletion ("Forward Secrecy") of received messages even when
   adversaries capture encrypted messages in transit and later
   compromise the user's message archive and secret keys.  The design
   uses deterministically ratcheted rotating encryption subkeys with
   predictable expiration combined with coordinated secret key material
   destruction.  This document also describes the structure, use, and
   maintenance of the OpenPGP Transferable Secret Key that corresponds
   with the Autocrypt v2 Certificate.
- **draft-becker-cnsa2-ssh-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
   Commercial National Security Algorithm (CNSA) 2.0 Suite, a
   cybersecurity advisory published by the United States Government
   which outlines quantum-resistant cryptographic algorithm policy for
   US national security applications.

   This profile applies to the capabilities, configuration, and
   operation of all components of US National Security Systems that
   employ SSH.  It is also appropriate for all other U.S.  Government
   systems that process high-value information.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This profile is made publicly available
   for use by developers and operators of these and any other system
   deployments.
- **draft-bg-onions-update-network-service-models-01** (new-draft, score 0, ignored_after_review) [none]: [An Update of Service and Network YANG Data Models](https://datatracker.ietf.org/doc/draft-bg-onions-update-network-service-models/) — Service & Network data models have been implemented in recent years
   to facilitate the deployment of connectivity services such as Layer 2
   and Layer 3 VPN services in provider networks.  This document reports
   the findings from the implementations, including missing
   functionalities, configuration blocks aligment against recent network
   models published, operational issues/limitatations and enhancements.
- **draft-birrane-dtn-rel-02** (new-draft, score 0, ignored_after_review) [none]: [Reliability Considerations for Delay-Tolerant Networks](https://datatracker.ietf.org/doc/draft-birrane-dtn-rel/) — The Delay-Tolerant Networking (DTN) architecture describes a type of
   challenged network in which communications may be significantly
   affected by long signal propagation delays, frequent link
   disruptions, or both.  These unique and challenging characteristics
   require adapted approaches for data transport, security, management,
   routing, and other networking functions.  Using new approaches, DTNs
   can offer data services in environments that would be considered
   neither reliable nor resilient as these concepts are understood for
   unchallenged networks.

   This document identifies adapted definitions and concepts for DTN
   reliability and resiliency that can be applied even when there is no
   simultaneous, reliable, end-to-end path between sources and
   destinations in the network.  These definitions and concepts are
   suitable for any challenged environment but, in particular, those
   communicating using the DTN Bundle Protocol (BP).  The ability to
   overlay BP across multiple discontinuous underlay networks, to store-
   and-forward data where and as necessary, and the structure and
   security of the BPv7 bundle itself provide novel ways to identify,
   implement, signal, and otherwise consider guarantees associated with
   data exchange in the DTN environment.
- **draft-bruynooghe-n0-quic-nat-traversal-00** (new-draft, score 0, ignored_after_review) [none]: [n0 QUIC NAT Traversal](https://datatracker.ietf.org/doc/draft-bruynooghe-n0-quic-nat-traversal/) — A description of how noq (https://github.com/n0-computer/noq)
   performs NAT traversal for iroh (https://github.com/n0-computer/
   iroh), including all current bugs.  This is not yet a specification,
   though further revisions migth be.
- **draft-busi-nmop-transport-simap-02** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Service & Infrastructure Maps (SIMAP) to Transport Networks](https://datatracker.ietf.org/doc/draft-busi-nmop-transport-simap/) — This document explores the applicability of the Service &
   Infrastructure Maps (SIMAP) concepts to transport networks and it
   examines the YANG data models defined by the IETF to support the
   requirements and use cases for SIMAP applicability to transport
   networks.
- **draft-campling-ech-deployment-considerations-12** (new-draft, score 0, ignored_after_review) [none]: [Encrypted Client Hello Deployment Considerations](https://datatracker.ietf.org/doc/draft-campling-ech-deployment-considerations/) — This document discusses operational and policy considerations
   related to the deployment of TLS Encrypted Client Hello (ECH). It
   describes the impact of encrypting the TLS Server Name Indication
   (SNI) on operational practices such as threat detection, network
   security controls, and content filtering in private, edge, and
   public network environments, with a particular focus on education,
   enterprise, and public operator use cases.
- **draft-cardona-claise-netmod-yang-coverage-00** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for YANG Example Validation and Coverage Analysis in IETF Documents](https://datatracker.ietf.org/doc/draft-cardona-claise-netmod-yang-coverage/) — This document defines guidelines for including YANG example instances
   in IETF documents in a way that enables automatic extraction and
   validation.  It introduces the concept of YANG module "coverage" to
   measure how thoroughly example instances exercise a YANG module's
   data nodes.  By standardizing how YANG examples are included,
   validated, and measured for coverage, these guidelines help authors
   catch errors before publication and give reviewers and implementers
   greater confidence that the examples in a specification are correct
   and cover a sufficient range of scenarios - ultimately making the
   underlying data models easier to implement and use.
- **draft-cheshire-sbm-04** (new-draft, score 0, ignored_after_review) [none]: [Source Buffer Management](https://datatracker.ietf.org/doc/draft-cheshire-sbm/) — In the past decade there has been growing awareness about the harmful
   effects of bufferbloat in the network, and there has been good work
   on developments like L4S to address that problem.  However,
   bufferbloat on the sender itself remains a significant additional
   problem, which has not received similar attention.  This document
   offers techniques and guidance for host networking software to avoid
   network traffic suffering unnecessary delays caused by excessive
   buffering at the sender.  These improvements are broadly applicable
   across all datagram and transport protocols (UDP, TCP, QUIC, etc.) on
   all operating systems.
- **draft-claise-opsawg-ipfix-ordered-ie-01** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
   Information Element to appear multiple times in a Template Record.
   RFC 7011 states that multiple occurrences of the same Information
   Element SHOULD follow the logical order of their treatments by the
   Metering Process; however, no protocol mechanism exists for the
   Exporting Process to explicitly signal to the Collecting Process that
   this ordering is guaranteed.  Without such a guarantee, the
   Collecting Process cannot safely interpret repeated Information
   Elements as ordered observations.  This document describes the
   problem, presents use cases, analyzes candidate solutions, and
   specifies a mechanism -- a new Ordered Set type -- that establishes
   an end-to-end ordering guarantee: the Metering Process records
   repeated Information Element values in the order the corresponding
   observations are made, the Exporting Process preserves and signals
   this guarantee, and the Collecting Process interprets the n-th
   occurrence of an Information Element as corresponding to the n-th
   observation by the Metering Process at the Observation Point.  This
   document updates RFC 7011, RFC 5476, and RFC 6183.
- **draft-contreras-detnet-preof-oam-00** (new-draft, score 0, ignored_after_review) [none]: [PREOF Observability and OAM Requirements](https://datatracker.ietf.org/doc/draft-contreras-detnet-preof-oam/) — Packet Replication, Elimination, and Ordering Functions (PREOF)
   enables highly reliable packet delivery through path redundancy and
   packet sequencing mechanisms in DetNet domains.

   Existing DetNet Operations, Administration, and Maintenance (OAM)
   specifications provide mechanisms for monitoring service
   connectivity, packet loss, delay, and overall service performance.
   However, they do not provide detailed operational visibility into the
   behavior of PREOF functions themselves.

   This document identifies operational observability gaps associated
   with PREOF, defines requirements for PREOF-specific OAM, and
   introduces a set of observable events and metrics to monitor,
   troubleshoot, and validate PREOF operation independently of the
   underlying DetNet data plane technology.
- **draft-contreras-pim-eco-mode-01** (new-draft, score 0, ignored_after_review) [none]: [IGMP / MLD Extension for Signaling Eco-Mode](https://datatracker.ietf.org/doc/draft-contreras-pim-eco-mode/) — This document specifies an extension to IGMPv3 and MLDv2 messages to
   indicate eco-mode preferences in the delivery of multicast content
   based on the mechanism described in [RFC9279].  The extension enables
   receivers and network elements to signal energy-aware multicast
   delivery preferences, including different eco-mode levels, so that
   multicast services can be operated consistently with energy-efficient
   network management, service-level optimisation, and telemetry-driven
   assessment of energy and carbon impact.
- **draft-dnsop-rfc6303-bis-03** (new-draft, score 0, ignored_after_review) [none]: [Updates to Locally Served DNS Zones and IP Special-Purpose Address Space Registries](https://datatracker.ietf.org/doc/draft-dnsop-rfc6303-bis/) — RFC 6063, "Locally Served DNS Zones", defines two IANA registries
   called "IPv4 Locally-Served DNS Zone" and "IPv6 Locally-Served DNS
   Zone" registries.  This document changes the registration policy for
   that registry from "IETF Review" to "Expert Review".

   Also, this document updates IP Special-Purpose Address Space
   registries to indicate whether an IP address block is eligible to be
   in Locally-Served DNS Zones.  Eligible entries will be automatically
   added to the Locally-Served DNS Zones.

   This document updates RFC 6063 and RFC 6890.
- **draft-eastlake-manet-babel-wi-fi-00** (new-draft, score 0, ignored_after_review) [none]: [Babel for Wi-Fi (IEEE Std 802.11) Mesh](https://datatracker.ietf.org/doc/draft-eastlake-manet-babel-wi-fi/) — The BABEL routing protocol (RFC 8966) is well applicable (RFC 8967)
   to networks with unstable link metrics such as wireless networks.
   Wi-Fi (IEEE Std 802.11-2024) is an example of such a network and the
   Wi-Fi standard includes a mesh feature which was specified to be
   configurable for different routing protocols and link metrics.  This
   document specifies how, in Wi-Fi mesh, to use BABEL and/or the delay
   based link metric specified in RFC 9616.
- **draft-englishm-moq-relay-dos-01** (new-draft, score 0, ignored_after_review) [none]: [Denial-of-Service Considerations for Media over QUIC Relay Deployments](https://datatracker.ietf.org/doc/draft-englishm-moq-relay-dos/) — The Media over QUIC Transport (MoQT) protocol presents denial-of-
   service risks that differ in character from those facing typical
   request-response protocols.  MoQT relays forward, fan out, and
   optionally cache media content on behalf of publishers and
   subscribers.  This document complements the MoQT Security
   Considerations, focusing on the unique considerations for relays.
- **draft-filsfils-spring-path-tracing-srmpls-08** (new-draft, score 0, ignored_after_review) [none]: [Path Tracing in SR-MPLS networks](https://datatracker.ietf.org/doc/draft-filsfils-spring-path-tracing-srmpls/) — Path Tracing provides a record of the packet path as a sequence of
   interface ids.  In addition, it provides a record of end-to-end
   delay, per-hop delay, and load on each interface that forwards the
   packet.

   Path Tracing has the lowest MTU overhead compared to alternative
   proposals such as [INT], [RFC9197], [I-D.song-opsawg-ifit-framework],
   and [I-D.kumar-ippm-ifa].

   Path Tracing supports fine grained timestamp.  It has been designed
   for linerate hardware implementation in the base pipeline.

   This document defines the Path Tracing specification for the SR-MPLS
   dataplane.  The Path Tracing specification for the SRv6 dataplane is
   defined in [I-D.filsfils-spring-path-tracing].
- **draft-flechier-sidrops-pava-02** (new-draft, score 0, ignored_after_review) [none]: [PAVA: BGP AS_PATH Validation by Querying ASes about Their Relationships](https://datatracker.ietf.org/doc/draft-flechier-sidrops-pava/) — This document defines PAth VAlidation (PAVA), a scheme for validating
   the Border Gateway Protocol (BGP) AS_PATH field based on the AS
   relationships.  Validation involves sending queries to the ASes along
   the path and each query specifies information about the prefix and
   the relevant path segment.  In this draft, for the decentralized
   distribution system that ASes on a path need for distributing the
   information, we propose to use the Domain Name System (DNS) and
   DNSSEC.
- **draft-gl-lsr-metric-normalize-01** (new-draft, score 0, ignored_after_review) [none]: [Metric Normalize for IGP Flex-algo](https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/) — When multiple links in a network have the same metric, they can
   serve as ECMP equivalent links for load balancing during forwarding.
   However, slight fluctuations in metric values can prevent the
   formation of ECMP equivalent links, leading to the idle state of
   suboptimal links and thus wasting bandwidth resources.

   This document proposes a metric normalization method by advertising
   metric normalization parameters corresponding to a specific Metric-
   Type for Flexible Algorithm. During route calculation, slight
   fluctuations across multiple links are adjusted according to these
   normalization parameters, making the computed metric values more
   consistent. This approach enables the formation of ECMP equivalent
   links and promotes load sharing in the forwarding process.
- **draft-gray-plants-mtc-deploy-use-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Merkle Tree Certificates Deployment Use Cases](https://datatracker.ietf.org/doc/draft-gray-plants-mtc-deploy-use-cases/) — Merkle Tree Certificates (MTC) I-D.ietf-plants-merkle-tree-certs has
   been defined for the use case of the WebPKI.  In this document we
   explore when and how MTC in parts or full can be used in different
   use cases.  Some of this use-cases may provide benefit for private
   PKI usage.
- **draft-halmir-mpls-ecn-03** (new-draft, score 0, ignored_after_review) [none]: [Explicit Congestion Notification Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-halmir-mpls-ecn/) — It has been broadly demonstrated that user experience improvements
   for time-critical applications have not increased at the same pace as
   network throughput (i.e., the increased bandwidth does not result in
   a corresponding increase in the user experience).  Optimizing network
   latency rather than throughput can lead to a significantly improved
   user experience for time-critical applications.  Low Latency, Low
   Loss, and Scalable Throughput (L4S) technology, introduced in RFC
   9330, uses Explicit Congestion Notification (ECN) bits by marking
   packets suffering potential congestion in the network.  L4S operates
   as a congestion-control mechanism, using markers within the data
   packets to detect and promptly respond to congestion conditions.
   This feedback loop enables devices (e.g., endpoints such as client
   devices and server devices) to adjust data flow in real-time,
   preventing bottlenecks and ensuring smoother transmission.

   RFC 5129 describes a mechanism for supporting ECN in the
   Multiprotocol Label Switching (MPLS) data plane.  That mechanism is
   based on the codepoints that take part in the Traffic Class (TC)
   field and, thus, prevent the use of TC field for traffic
   differentiation.  This document defines how ECN can be supported in
   the MPLS data plane using the MPLS Network Actions technology.
- **draft-hegde-lsr-isis-osnc-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Originator Sequence Number Checksum TLV](https://datatracker.ietf.org/doc/draft-hegde-lsr-isis-osnc/) — This document introduces a new top-level TLV in IS-IS to carry a
   checksum over the LSP IDs and sequence numbers of all self-originated
   LSP fragments.  A receiving node uses this value to validate the
   integrity of the originator's Link State Database (LSDB).
- **draft-ietf-6man-rfc8504-bis-03** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 Node Requirements](https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/) — This document defines requirements for IPv6 nodes.  It is expected
   that IPv6 will be deployed in a wide range of devices and situations.
   Specifying the requirements for IPv6 nodes allows IPv6 to function
   well and interoperate in a large number of situations and
   deployments.

   This document obsoletes RFC 8504, and in turn RFC 6434 and its
   predecessor, RFC 4294.
- **draft-ietf-avtcore-frame-acknowledgement-01** (new-draft, score 0, ignored_after_review) [avtcore]: [RTCP Feedback Message and Request Mechanism for Frame-level Acknowledgement](https://datatracker.ietf.org/doc/draft-ietf-avtcore-frame-acknowledgement/) — This document describes a mechanism for signaling which video frames
   have been received and decoded by a remote peer.  It comprises an
   RTCP feedback message and an RTP header extension used to request
   said feedback.

   One of the main use cases for this data is to implement various forms
   of Long Term Reference (LTR) reference structures.  Additionally, the
   mechanism provides a way for receivers to request resynchronization
   frames that reference acknowledged frames, enabling efficient
   recovery from partial or full frame loss without requiring a full
   keyframe.
- **draft-ietf-bess-mup-safi-01** (new-draft, score 0, ignored_after_review) [bess]: [BGP Extensions for the Mobile User Plane (MUP) SAFI](https://datatracker.ietf.org/doc/draft-ietf-bess-mup-safi/) — This document defines a new SAFI known as a BGP Mobile User Plane
   (BGP-MUP) SAFI to support MUP Extensions and a extended community for
   BGP.  This document also provides BGP signaling and procedures for
   the new SAFI to convert mobile session information into appropriate
   IP forwarding information.  These extensions can be used by operators
   between a PE, and a Controller for integrating mobile user plane into
   BGP MUP network using the IP based routing.
- **draft-ietf-cdni-edge-control-metadata-12** (new-draft, score 0, ignored_after_review) [cdni]: [Content Delivery Network Interconnection (CDNI) Edge Control Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-edge-control-metadata/) — This specification defines configuration metadata objects used to
   manage how edge servers control access to resources within Content
   Delivery Networks (CDNs) and Open Caching systems.  A key feature of
   these configurations is the configuring of Cross-Origin Resource
   Sharing (CORS) access rules and the dynamic generation of CORS
   headers.  This specification also provides the ability to define
   response body compression rules and client connection timeouts.
- **draft-ietf-core-conditional-attributes-13** (new-draft, score 0, ignored_after_review) [core]: [Conditional Query Parameters for CoAP Observe](https://datatracker.ietf.org/doc/draft-ietf-core-conditional-attributes/) — This specification defines Conditional Notification and Control Query
   Parameters compatible with CoAP Observe (RFC7641).
- **draft-ietf-core-oscore-key-update-14** (new-draft, score 0, ignored_after_review) [core]: [Key Update for OSCORE (KUDOS)](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-key-update/) — Communications with the Constrained Application Protocol (CoAP) can
   be protected end-to-end at the application-layer by using the
   security protocol Object Security for Constrained RESTful
   Environments (OSCORE).  Under some circumstances, two CoAP endpoints
   need to update their OSCORE keying material before communications can
   securely continue, e.g., due to approaching key usage limits.  This
   document defines Key Update for OSCORE (KUDOS), a lightweight key
   update procedure that two CoAP endpoints can use to update their
   OSCORE keying material by establishing a new OSCORE Security Context.
   Accordingly, this document updates the use of the OSCORE flag bits in
   the CoAP OSCORE Option as well as the protection of CoAP response
   messages with OSCORE.  Also, it deprecates the key update procedure
   specified in Appendix B.2 of RFC 8613.  Therefore, this document
   updates RFC 8613.
- **draft-ietf-core-uri-path-abbrev-05** (new-draft, score 0, ignored_after_review) [core]: [URI Path abbreviation in CoAP](https://datatracker.ietf.org/doc/draft-ietf-core-uri-path-abbrev/) — Applications built on CoAP face a conflict between the technical need
   for short message sizes and the interoperability requirement of
   following BCP190 and thus using (relatively verbose) well-known URI
   paths.  This document introduces the Uri-Path-Abbrev CoAP option that
   allows expressing well-known URI paths in as little as two bytes.

   Using this option revealed a subtle flaw in RFC7252 that severely
   limited the extension point of critical options.  This document
   updates RFC7252 to rectify that.
- **draft-ietf-dmm-tn-aware-mobility-27** (new-draft, score 0, ignored_after_review) [dmm]: [Mobility-aware Transport Network Slicing for 5G](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-dtn-bp-sand-03** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol (BP) Secure Advertisement and Neighborhood Discovery (SAND)](https://datatracker.ietf.org/doc/draft-ietf-dtn-bp-sand/) — This document defines the Secure Advertisement and Neighborhood
   Discovery (SAND) protocol for Bundle Protocol version 7 (BPv7) within
   a delay-tolerant network (DTN).  This protocol defines a general
   purpose advertisement mechanism with an initial set of message and
   data types able to be advertised by participating nodes in a BPv7
   network.  The focus of this document is for advertisement to
   topological neighbors about local neighborhoods but can be expanded
   upon in the future through extension points.
- **draft-ietf-dtn-eid-pattern-09** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol Endpoint ID Patterns](https://datatracker.ietf.org/doc/draft-ietf-dtn-eid-pattern/) — This document extends the Bundle Protocol Endpoint ID (EID) concept
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
- **draft-ietf-hpke-hpke-04** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document describes a scheme for hybrid public key encryption
   (HPKE).  This scheme provides a variant of public key encryption of
   arbitrary-sized plaintexts for a recipient public key.  It also
   includes a variant that authenticates possession of a pre-shared key.
   HPKE works for any combination of an asymmetric Key Encapsulation
   Mechanism (KEM), key derivation function (KDF), and authenticated
   encryption with additional data (AEAD) encryption function.  This
   document provides instantiations of the scheme using widely used and
   efficient primitives, such as Elliptic Curve Diffie-Hellman (ECDH)
   key agreement, HMAC-based key derivation function (HKDF), and SHA-2.

   This document obsoletes RFC 9180.
- **draft-ietf-hpke-pq-05** (new-draft, score 0, ignored_after_review) [hpke]: [Post-Quantum and Post-Quantum/Traditional Hybrid Algorithms for HPKE](https://datatracker.ietf.org/doc/draft-ietf-hpke-pq/) — Updating key exchange and public-key encryption protocols to resist
   attack by quantum computers is a high priority given the possibility
   of "harvest now, decrypt later" attacks.  Hybrid Public Key
   Encryption (HPKE) is a widely-used public key encryption scheme based
   on combining a Key Encapsulation Mechanism (KEM), a Key Derivation
   Function (KDF), and an Authenticated Encryption with Associated Data
   (AEAD) scheme.  In this document, we define KEM algorithms for HPKE
   based on both post-quantum KEMs and hybrid constructions of post-
   quantum KEMs with traditional KEMs, as well as a KDF based on SHA-3
   that is suitable for use with these KEMs.  When used with these
   algorithms, HPKE is resilient with respect to attacks by a quantum
   computer.
- **draft-ietf-ianabis-rfc7120bis-03** (new-draft, score 0, ignored_after_review) [ianabis]: [Early IANA Code Point Allocation](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc7120bis/) — This document describes the requirements for securing IANA code point
   assignments for IETF Stream Internet-Drafts and specifications being
   drafted by other standards-related organizations.  This document
   obsoletes RFC 7120.
- **draft-ietf-ianabis-rfc8126bis-03** (new-draft, score 0, ignored_after_review) [ianabis]: [Guidelines for Writing an IANA Considerations Section in RFCs](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc8126bis/) — Many protocols make use of points of extensibility that use constants
   to identify various protocol parameters.  To ensure that the values
   in these fields do not have conflicting uses and to promote
   interoperability, their allocations are often coordinated by a
   central record keeper.  For IETF protocols, that role is filled by
   the Internet Assigned Numbers Authority (IANA).

   To make assignments in a given registry prudently, guidance
   describing the conditions under which new values should be assigned,
   as well as when and how modifications to existing values can be made,
   is needed.  This document defines a framework for the documentation
   of these guidelines by specification authors, in order to assure that
   the provided guidance for the IANA Considerations is clear and
   addresses the various issues that are likely in the operation of a
   registry.

   This is the fourth edition of this document; it obsoletes RFC 8126.
- **draft-ietf-idr-bgp-ls-sr-policy-nrp-03** (new-draft, score 0, ignored_after_review) [idr]: [SR Policies Extensions for Network Resource Partition in BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-nrp/) — A Network Resource Partition (NRP) is a subset of the network
   resources and associated policies on each of a connected set of links
   in the underlay network.  An NRP ID is an important network resource
   attribute associated with the Segment Routing (SR) policy and needs
   to be reported to the external components.  This document defines a
   new TLV which enables the headend to report the NRP which the SR
   Policy Candidate Path (CP) is associated with using Border Gateway
   Protocol Link-State (BGP-LS).
- **draft-ietf-idr-bgp4-rfc4271bis-01** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
   an inter-Autonomous System routing protocol.

   The primary function of a BGP-speaking system is to exchange network
   reachability information with other BGP systems.  This network
   reachability information includes information on the list of
   Autonomous Systems (ASes) that reachability information traverses.
   This information is sufficient for constructing a graph of AS
   connectivity for this reachability from which routing loops may be
   pruned, and, at the AS level, some policy decisions may be enforced.

   BGP-4 provides a set of mechanisms for supporting Classless Inter-
   Domain Routing (CIDR).  These mechanisms include support for
   advertising a set of destinations as an IP prefix, and eliminating
   the concept of network "class" within BGP.  BGP-4 also introduces
   mechanisms that allow aggregation of routes, including aggregation of
   AS paths.

   This document obsoletes RFC 4271.
- **draft-ietf-idr-fsv2-ip-basic-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 - for Basic IP](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/) — BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
   8956, and RFC 9117, describes the distribution of traffic filter
   policy (traffic filters and actions) distributed via BGP.  During the
   deployment of BGP FSv1 a number of issues were detected, so version 2
   of the BGP flow specification (FSv2) protocol addresses these issues.
   In order to provide a clear demarcation between FSv1 and FSv2, a
   different NLRI encapsulates FSv2.

   The IDR WG requires two implementation.  Early feedback on
   implementations of FSv2 indicate that FSv2 has a correct design
   direction, but that breaking FSv2 into a progression of documents
   would aid deployment of the draft (basic, adding more filters, and
   adding more actions).  This document specifies the basic FSv2 NLRI
   with user ordering of filters added to FSv1 IP Filters and FSv2
   actions.
- **draft-ietf-iotops-7228bis-10** (new-draft, score 0, ignored_after_review) [iotops]: [Terminology for Constrained-Node Networks](https://datatracker.ietf.org/doc/draft-ietf-iotops-7228bis/) — The Internet Protocol Suite is increasingly used on small devices
   with severe constraints on power, memory, and processing resources,
   creating constrained-node networks.  This document provides a number
   of basic terms that have been useful in research and standardization
   work for constrained-node networks.

   This document obsoletes RFC 7228.
- **draft-ietf-ippm-responsiveness-09** (new-draft, score 0, ignored_after_review) [ippm]: [Responsiveness under Working Conditions](https://datatracker.ietf.org/doc/draft-ietf-ippm-responsiveness/) — For many years, a lack of responsiveness, variously called lag,
   latency, or bufferbloat, has been recognized as an unfortunate, but
   common, symptom in today's networks.  Even after a decade of work on
   standardizing technical solutions, it remains a common problem for
   the end users.

   Everyone "knows" that it is "normal" for a video conference to have
   problems when somebody else at home is watching a 4K movie or
   uploading photos from their phone.  However, there is no technical
   reason for this to be the case.  In fact, various queue management
   solutions have solved the problem.

   Our network connections continue to suffer from an unacceptable
   amount of delay, not for a lack of technical solutions, but rather a
   lack of awareness of the problem and deployment of its solutions.  We
   believe that creating a tool that measures the problem and matches
   people's everyday experience will create the necessary awareness, and
   result in a demand for solutions.

   This document specifies the "Responsiveness Test" for measuring
   responsiveness.  It uses common protocols and mechanisms to measure
   user experience specifically when the network is under working
   conditions.  The measurement is expressed as "Round-trips Per Minute"
   (RPM) and should be included with goodput (up and down) and idle
   latency as critical indicators of network quality.
- **draft-ietf-mailmaint-smtputf8-syntax-04** (new-draft, score 0, ignored_after_review) [mailmaint]: [SMTPUTF8 Email Addresses](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-smtputf8-syntax/) — RFC 6532 extends the internet email format to allow UTF8 in many
   contexts.  This document restricts the set of allowed addresses in
   header fields slightly, and thereby simplifies use of these
   addresses.

   This is one of a pair of documents.  This one is simple to implement
   and contains only globally viable rules.  Its companion has more
   complex rules, takes regional usage into account, and describes
   addresses that can be read by some community and cut-and-pasted in
   some locale.
- **draft-ietf-manet-inet-gap-analysis-02** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mimi-arch-03** (new-draft, score 0, ignored_after_review) [mimi]: [An Architecture for More Instant Messaging Interoperability (MIMI)](https://datatracker.ietf.org/doc/draft-ietf-mimi-arch/) — The More Instant Messaging Interoperability (MIMI) working group is
   defining a suite of protocols that allow messaging providers to
   interoperate with one another.  This document lays out an overall
   architecture enumerating the MIMI protocols and how they work
   together to enable an overall messaging experience.
- **draft-ietf-mls-ratchet-tree-options-01** (new-draft, score 0, ignored_after_review) [mls]: [Ways to convey the Ratchet Tree in Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-ratchet-tree-options/) — The Messaging Layer Security (MLS) protocol needs to share its
   ratchet_tree object to welcome new clients into a group and in
   external joins.  While the protocol only defines a mechanism for
   sharing the entire tree, most implementations use various
   optimizations to avoid sending this structure repeatedly in large
   groups.  This document describes a way to convey these improvements
   in a standardized way and to convey the parts of a GroupInfo object
   that are not visible to an intermediary server.
- **draft-ietf-mops-network-overlay-impacts-04** (new-draft, score 0, ignored_after_review) [mops]: [Network Overlay Impacts to Streaming Video](https://datatracker.ietf.org/doc/draft-ietf-mops-network-overlay-impacts/) — This document examines the operational impacts on streaming video
   applications resulting from network policy changes introduced by
   network overlays.  Such overlays may alter IP address assignment,
   transport protocols, routing behavior, or DNS resolution.  These
   changes can, in turn, affect critical aspects of content delivery,
   including latency, CDN cache selection, delivery path optimization,
   traffic classification, and content access controls.
- **draft-ietf-moq-loc-03** (new-draft, score 0, ignored_after_review) [moq]: [Low Overhead Media Container](https://datatracker.ietf.org/doc/draft-ietf-moq-loc/) — This specification describes a Low Overhead Media Container (LOC)
   format for encoded and encrypted audio and video media data to be
   used primarily for interactive Media over QUIC Transport (MOQT).  It
   may be used in the MOQT Streaming Format (MSF) specification, which
   defines a catalog format for publishers to declare and describe their
   LOC tracks and for subscribers to consume them.  Examples are also
   provided for building media applications using LOC and MOQT.
- **draft-ietf-moq-secure-objects-01** (new-draft, score 0, ignored_after_review) [moq]: [End-to-End Secure Objects for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-secure-objects/) — This document specifies an end-to-end authenticated encryption scheme
   for application objects transmitted via Media over QUIC (MoQ)
   Transport.  The scheme enables original publishers that share a
   symmetric key with end subscribers, to ensuring that MoQ relays are
   unable to decrypt object contents.  Additionally, subscribers can
   verify the integrity and authenticity of received objects, confirming
   that the content has not been modified in transit.  Additionally it
   allows MoQ parameters to be protected so the publisher can select if
   they are readable and/or modifiable by relays.
- **draft-ietf-moq-transport-19** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-mpls-on-path-telemetry-flag-01** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes the postcard-based on-path telemetry with
   packet marking (PBT-M) using an MPLS Network Actions (MNA) flag to
   support OAM in MPLS networks.  The scheme uses a single flag bit
   carried in a Flag-Based Network Action Indicator (Opcode 1) of the
   MNA Sub-Stack as defined in RFC 9994.  The document provides the
   solutions to address the requirements for applying PBT-M in MPLS
   networks.
- **draft-ietf-netconf-https-notif-cbor-01** (new-draft, score 0, ignored_after_review) [netconf]: [CBOR Encoding for HTTPS-based YANG Notifications Transport](https://datatracker.ietf.org/doc/draft-ietf-netconf-https-notif-cbor/) — This document extends [I-D.draft-ietf-netconf-https-notif] by
   introducing CBOR encoding for YANG notifications over HTTPS transport
   in addition to the existing JSON and XML encoding schemes.
- **draft-ietf-netmod-yang-semver-27** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Semantic Versioning](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-semver/) — This document specifies a YANG extension along with guidelines for
   applying an extended set of semantic versioning rules to revisions of
   YANG artifacts (e.g., modules and packages).  Additionally, this
   document defines a YANG extension for controlling module imports
   based on these modified semantic versioning rules.

   This document updates RFCs 7950, 9907, and 8525.
- **draft-ietf-pce-sr-p2mp-policy-19** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-multicast-lessons-learned-09** (new-draft, score 0, ignored_after_review) [pim]: [Multicast Lessons Learned from Decades of Deployment Experience](https://datatracker.ietf.org/doc/draft-ietf-pim-multicast-lessons-learned/) — This document gives a historical perspective about the design and
   deployment of multicast routing protocols.  The document describes
   the technical challenges discovered from building these protocols.
   Even though multicast has enjoyed success of deployment in special
   use-cases, this draft discusses what were, and are, the obstacles for
   mass deployment across the Internet.  Individuals who are working on
   new multicast related protocols will benefit by knowing why certain
   older protocols are no longer in use today.
- **draft-ietf-pim-pfm-forwarding-enhancements-07** (new-draft, score 0, ignored_after_review) [pim]: [PIM Flooding Mechanism and Source Discovery Enhancements](https://datatracker.ietf.org/doc/draft-ietf-pim-pfm-forwarding-enhancements/) — The Protocol Independent Multicast (PIM) Flooding Mechanism (PFM) is
   an experimental extension that provides a generic hop-by-hop message
   exchange framework for distributing multicast information among PIM
   routers.  Existing PFM procedures enable efficient source discovery
   without reliance on Rendezvous Points, shared trees, or initial data
   registers.

   This document specifies further experimental enhancements to PFM
   forwarding behavior to improve efficiency and scalability.  In
   particular, it introduces mechanisms to reduce redundant message
   transmission over multiple parallel links and extends the encoding of
   multicast information through additional Type-Length-Value (TLV)
   structures and sub-TLVs to convey richer flow-related data.  These
   enhancements optimize control-plane overhead while preserving
   interoperability with existing PFM procedures, enabling more
   efficient dissemination of multicast state in PIM networks.
- **draft-ietf-procon-2418bis-03** (new-draft, score 0, ignored_after_review) [procon]: [IETF Working Group Guidelines and Procedures](https://datatracker.ietf.org/doc/draft-ietf-procon-2418bis/) — The Internet Engineering Task Force (IETF) has responsibility for
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
- **draft-ietf-quic-qmux-02** (new-draft, score 0, ignored_after_review) [quic]: [QMux](https://datatracker.ietf.org/doc/draft-ietf-quic-qmux/) — This document specifies QMux version 1.  QMux version 1 provides,
   over bi-directional streams such as TLS, the same set of stream and
   datagram operations that applications rely upon in QUIC version 1.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the QUIC Working Group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/quic/.

   Source for this draft and an issue tracker can be found at
   https://github.com/quicwg/qmux.
- **draft-ietf-radext-radiusdtls-bis-17** (new-draft, score 0, ignored_after_review) [radext]: [RadSec: RADIUS over Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-ietf-radext-radiusdtls-bis/) — This document defines transport profiles for running RADIUS over
   Transport Layer Security (TLS) and Datagram Transport Layer Security
   (DTLS), allowing the secure and reliable transport of RADIUS
   messages.  RADIUS/TLS and RADIUS/DTLS are collectively referred to as
   RadSec.

   This document obsoletes RFC6614 and RFC7360, which specified
   experimental versions of RADIUS over TLS and DTLS.
- **draft-ietf-regext-epp-same-entity-00** (new-draft, score 0, ignored_after_review) [regext]: [Domain variant support for EPP](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-same-entity/) — This document defines an EPP extension allowing clients to learn
   about and manipulate variant groups of domains, ie. groups of domains
   whose names are equivalent in a registry-defined way and are tied to
   a single registrant.
- **draft-ietf-roll-enrollment-priority-17** (new-draft, score 0, ignored_after_review) [roll]: [Controlling Network Enrollment in RPL networks](https://datatracker.ietf.org/doc/draft-ietf-roll-enrollment-priority/) — The Routing Protocol for Low-Power and Lossy Networks (RPL) manages
   the routing topology but lacks a mechanism to globally regulate how
   many new nodes, known as Pledges, can join a node in a 6TiSCH network
   at any given time.  Currently, Join Proxies (6LowPAN Routers) make
   local decisions about whether to facilitate a Pledge's enrollment
   based only on their immediate resources.

   This document introduces RPL extensions to ensure that enrollment
   remains orderly, prevents localized congestion at specific Join
   Proxies, and allows the network to stay within its operational
   capacity limits.
- **draft-ietf-rtgwg-multisegment-sdwan-14** (new-draft, score 0, ignored_after_review) [rtgwg]: [Multi-segment SD-WAN via Cloud DCs](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/) — This document describes a method for seamlessly
   interconnecting geographically separated SD-WAN segments via
   a Cloud Backbone without requiring Cloud Gateways (GWs) to
   decrypt and re-encrypt traffic. By encapsulating IPsec-
   encrypted payloads within GENEVE headers (RFC 8926), the
   approach enables Cloud GWs to forward encrypted traffic
   directly between distant Customer Premises Equipment (CPEs).
   This reduces processing overhead, improves scalability, and
   preserves the confidentiality of enterprise data while
   ensuring secure and efficient multi-segment SD-WAN
   connectivity.
- **draft-ietf-scone-protocol-05** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-8210bis-26** (new-draft, score 0, ignored_after_review) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RFC6480) prefix origin data, Router Keys, and ASPA
   data from a trusted cache.  This document describes a protocol to
   deliver them.

   This document describes version 2 of the RPKI-Router protocol.
   [RFC6810] describes version 0, and [RFC8210] describes version 1.
   This document is compatible with both.
- **draft-ietf-sidrops-rpki-erik-protocol-05** (new-draft, score 0, ignored_after_review) [sidrops]: [The Erik Synchronization Protocol for use with the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rpki-erik-protocol/) — This document specifies the Erik Synchronization Protocol for use
   with the Resource Public Key Infrastructure (RPKI).  Erik
   Synchronization can be characterized as a data replication system
   using Merkle trees, a content-addressable naming scheme, concurrency
   control using monotonically increasing sequence numbers, and HTTP
   transport.  Relying Parties can combine information retrieved via
   Erik Synchronization with other RPKI transport protocols.  The
   protocol's design is intended to be efficient, fast, easy to
   implement, and robust in the face of partitions or faults in the
   network.
- **draft-ietf-sml-structured-quoted-content-00** (new-draft, score 0, ignored_after_review) [sml]: [Structured Quoted Content](https://datatracker.ietf.org/doc/draft-ietf-sml-structured-quoted-content/) — This document describes a machine-readable format for conveying
   quoted content in email messages.  This can be used when replying to
   or forwarding an email message.

   Structured quoted content is expected to be used in conjunction with
   conventional, human-readable quote formatting.  They are based on the
   forthcoming "structured email" specification defined in [I-D.ietf-
   sml-structured-email-03] and related drafts.
- **draft-ietf-spring-srv6-service-programming-00** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 Service Programming](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-service-programming/) — This document defines data plane functionality required to implement
   service segments and achieve service programming in SRv6 networks.
- **draft-ietf-spring-stamp-srpm-mpls-03** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-spring-stamp-srpm-srv6-02** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement for SRv6 using the Simple Two-Way Active
   Measurement Protocol (STAMP), as defined in RFC 8762, along with its
   optional extensions defined in RFC 8972 and further augmented in RFC
   9503.  The described procedures are used for links and SRv6 paths
   (including Segment Lists of SRv6 Policies, SRv6 IGP best paths, and
   SRv6 IGP Flexible Algorithm paths), as well as Layer-3 and Layer-2
   services over the SRv6 paths.
- **draft-ietf-tsvwg-fq-pie-02** (new-draft, score 0, ignored_after_review) [tsvwg]: [Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/) — This document presents Flow Queue Proportional Integral controller
   Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue
   Management (AQM) algorithm to isolate flows and tackle the problem of
   bufferbloat.  FQ-PIE uses hashing to classify incoming packets into
   different queues and provide flow isolation.  Packets are dequeued by
   using a variant of the round robin scheduler.  Each such flow is
   managed by the PIE algorithm to maintain high link utilization while
   controlling the queue delay to a target value.
- **draft-ietf-tsvwg-l4sops-10** (new-draft, score 0, ignored_after_review) [tsvwg]: [Operational Guidance on Coexistence with Classic ECN during L4S Deployment](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/) — This document provides guidance in order to ensure successful
   deployment of Low Latency Low Loss Scalable throughput (L4S) in the
   Internet.  Other L4S documents provide guidance for running an L4S
   experiment, but this document is focused solely on potential
   interactions between L4S flows and flows using the original
   ('Classic') ECN over a Classic ECN bottleneck.  The document
   discusses the potential outcomes of these interactions, describes
   mechanisms to detect the presence of Classic ECN bottlenecks, and
   identifies opportunities to prevent and/or detect and resolve
   fairness problems in such networks.  This guidance is aimed at
   operators of end-systems, operators of networks, and researchers.
- **draft-jennings-moq-mocha-chat-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Chat: Messaging over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-chat/) — This document specifies the messaging functionality for MOCHA (MoQ
   Open Communication & Hosting Architecture).  It defines how
   participants send and receive messages in channels using MoQ
   Transport (MOQT) publish/subscribe primitives.  Each device publishes
   messages on its own track within a channel namespace, enabling
   decentralized message production with relay-based fan-out.  This
   specification covers message naming, format, causal ordering,
   delivery, roster management, and channel discovery for text-based
   chat.
- **draft-jennings-moq-mocha-meetings-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Meetings: Real-Time Conferencing over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-meetings/) — This document specifies how multi-party audio and video meetings are
   conducted using MOCHA (MoQ Open Communication & Hosting
   Architecture).  It defines namespace conventions, media track design,
   catalog distribution, and participant flows for real-time
   conferencing over MoQ Transport (MOQT).  This specification supports
   both simulcast and scalable video codec configurations, enabling
   meetings ranging from small group calls to large-scale conferences.
- **draft-jennings-moq-mocha-mls-keying-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA MLS Keying: End-to-End Encryption Key Management over MoQ](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-mls-keying/) — This document specifies MLS key management for MOCHA (MoQ Open
   Communication & Hosting Architecture).  It defines how MLS groups are
   created, how members are added and removed, how key material is
   distributed over MOQT tracks, and how the MLS Delivery Service is
   realized in a fully distributed manner using MOQT publish/subscribe.
   For large channels, Partial MLS is used to avoid requiring all
   members to process every membership change.
- **draft-jennings-moq-mocha-pab-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Personal Address Book](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-pab/) — This document defines how a set of devices owned by a common user
   synchronize a Personal Address Book (PAB) over MOQT.  The address
   book maps identities to human-readable names and contact information,
   enabling users to maintain a trusted contact list that is consistent
   across all their devices.
- **draft-jennings-moq-mocha-reactions-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Reactions: Real-Time Reactions over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-reactions/) — This document specifies reactions for MOCHA (MoQ Open Communication &
   Hosting Architecture).  It supports message-targeted reactions (emoji
   on a specific chat message) and standalone reactions (engagement
   signals such as applause or raised hands).
- **draft-jholland-quic-multicast-09** (new-draft, score 0, ignored_after_review) [none]: [Multicast Extension for QUIC](https://datatracker.ietf.org/doc/draft-jholland-quic-multicast/) — This document defines a multicast extension to QUIC to enable the
   efficient use of multicast-capable networks to send identical data
   streams to many clients at once, coordinated through individual
   unicast QUIC connections.
- **draft-jones-httpbis-cookie-preference-00** (new-draft, score 0, ignored_after_review) [none]: [The Cookie-Preference HTTP Header Field](https://datatracker.ietf.org/doc/draft-jones-httpbis-cookie-preference/) — This document specifies a new HTTP request header field, "Cookie-
   Preference", that enables user agents to communicate the user's
   preferred cookie disposition (e.g., accept all, accept essential
   only, reject all, or ask) to web servers.  By conveying this
   preference upfront, the header can facilitate a more seamless
   browsing experience while respecting user privacy choices and
   reducing reliance on per-site consent dialogs.
- **draft-jot-bess-evpn-mcast-router-sync-00** (new-draft, score 0, ignored_after_review) [none]: [Multicast Router State Synchronization in EVPN Networks](https://datatracker.ietf.org/doc/draft-jot-bess-evpn-mcast-router-sync/) — Ethernet VPN (EVPN) networks support multicast applications in which
   multicast routers and multicast hosts are attached to the same
   tenant.  Existing specifications define how Provider Edge (PE)
   devices synchronize the Internet Group Management Protocol (IGMP) and
   Multicast Listener Discovery (MLD) membership state of multihomed
   multicast hosts, and how Optimized Inter-Subnet Multicast (OISM)
   forwarding interacts with multicast routers via PIM EVPN Gateways.
   However, none of the existing specifications addresses the
   synchronization of the state associated with a multicast router (an
   IGMP/MLD Querier or a Protocol Independent Multicast (PIM) router)
   when that router is multihomed to a set of EVPN PEs.  This document
   specifies a new EVPN route, the Multicast Router Discovery (MRD)
   route, and the procedures to synchronize multicast router state
   across the PEs of an Ethernet Segment, for routers attached to
   multicast Broadcast Domains or to Layer 3 interfaces.
- **draft-jz-dmm-mup-evolution-00** (new-draft, score 0, ignored_after_review) [none]: [Mobile User Plane Evolution: 5G & 6G](https://datatracker.ietf.org/doc/draft-jz-dmm-mup-evolution/) — This document starts from the description of the 5G mobile user
   plane, including distributed User Plane Functions (UPFs).  Then,
   based on the 3GPP proposals for 6G UP architecture evolution, the
   draft describes some potential enhancements revolving around the
   support of the 6G UP flexiblity, scalability & resilience.  The draft
   also discusses the potential IETF work upon integrating the proposed
   enhancements of the 6G UP architecture.
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-00** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.  This document also provides guidance for use of EDNS(0)
   in signature retrieval.
- **draft-kbr-teas-mptersvp-04** (new-draft, score 0, ignored_after_review) [none]: [RSVP-TE Extensions for Multipath Traffic Engineered Directed Acyclic Graph Tunnels](https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that facilitates weighted
   load balancing of unicast traffic across a constrained set of paths
   optimized for a specific objective.

   This document describes the provisioning of an MPTED Tunnel in a TE
   network using RSVP-TE.
- **draft-kinnear-dnsop-globally-relevant-00** (new-draft, score 0, ignored_after_review) [none]: [Globally Relevant HTTPS RRs](https://datatracker.ietf.org/doc/draft-kinnear-dnsop-globally-relevant/) — DNS answers for SVCB and HTTPS resource records are typically treated
   as scoped to the network on which they were obtained.  This requires
   clients to re-resolve DNS when changing network attachments, adding
   latency to connection establishment.  This document defines a new
   SvcParamKey, "globally-relevant", for use in SVCB and HTTPS DNS
   resource records as defined in [RFC9460].  When present, this boolean
   flag indicates that the service binding parameters in the record are
   valid regardless of the client's network attachment point.  Clients
   that observe this flag can reuse cached SVCB and HTTPS records across
   network changes, subject to normal TTL expiry.
- **draft-knodel-beyond-carbon-01** (new-draft, score 0, ignored_after_review) [none]: [Impacts of the Internet on the Environment, Beyond Carbon](https://datatracker.ietf.org/doc/draft-knodel-beyond-carbon/) — The global internet is comprised of vast interconnected networks
   spanning nearly every surface of planet and sky that, together with
   user devices, consumes energy and emits greenhouse gases.  The true
   scale and proposed mitigations of the carbon footprint of the
   internet are the subject of important research.  The internet also
   requires the depletion of other natural resources beyond carbon,
   namely land, water, electromagnetic spectrum and minerals.
   Electronic waste contributes in particularly acute ways to
   environmental pollution.  This document surveys the impacts of the
   internet on the environment and includes, but goes beyond, energy use
   and carbon footprint to look at the consumption of natural resources
   and environmental waste.
- **draft-kompella-teas-mcte-00** (new-draft, score 0, ignored_after_review) [none]: [Multicast Traffic Engineering](https://datatracker.ietf.org/doc/draft-kompella-teas-mcte/) — Traffic Engineering (TE) offers a very rich toolkit for managing
   traffic flows and the paths they take in a network.  A TE network can
   have link attributes such as bandwidth, colors, risk groups and
   alternate metrics.  A TE path can use these attributes to include or
   avoid certain links, increase path diversity, manage bandwidth
   reservations, improve service experience, and offer protection paths.
   These benefits apply equally to unicast and multicast traffic.

   This memo proposes multicast traffic-engineering (MCTE), allowing the
   use of TE for multicast traffic.  MCTE is an alternative proposal to
   point-to-multipoint TE specified in [RFC4875].  The approach in
   [RFC4875] creates a separate "sub-LSP" from the source to each leaf,
   resulting in a considerable amount of signaling and state in the
   network.  MCTE, on the other hand, uses the junction approach
   proposed in MPTE [I-D.kompella-teas-mpte] to create the multicast
   tree with less signaling and state.  [RFC4875] proposes the use of
   RSVP-TE for signaling and an MPLS data plane for carrying traffic.
   MCTE allows the use of several control and data planes to signal
   tunnels and carry traffic.
- **draft-krierhorn-idr-upa-03** (new-draft, score 0, ignored_after_review) [none]: [BGP Unreachable Prefix Announcement (UPA)](https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/) — Summarization is often used in multi-domain networks to improve
   network efficiency and scalability.  With summarization in place,
   there is a need to signal loss of reachability to an individual
   prefix covered by the summary.  This enables fast convergence by
   steering traffic away from the node which owns the prefix and is no
   longer reachable.

   This document specifies the mechanism, referred to as Unreachable
   Prefix Announcement (UPA), for networks where BGP is used to carry
   summary routes.  It is also equally beneficial for operators to share
   the unreachable prefixes.
- **draft-law-moq-imsc1-msf-00** (new-draft, score 0, ignored_after_review) [none]: [IMSC1 Packaging for MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-law-moq-imsc1-msf/) — This document specifies the packaging format for delivering IMSC1
   content as Event Timeline tracks within the MOQT Streaming Format
   (MSF).
- **draft-lcnc-onsen-telco-cloud-00** (new-draft, score 0, ignored_after_review) [none]: [Abstractions for Telco-Cloud Scenarios](https://datatracker.ietf.org/doc/draft-lcnc-onsen-telco-cloud/) — draft-lcnc-onsen-telco-cloud-00

Abstract

   Cloud infrastructures are becoming increasingly distributed, spanning
   centralized facilities and distributed edge sites, all of them
   interconnected through networks from one or more administrative
   domains.  Services running on top of such computing enironments
   require dynamic placement, admission control, lifecycle management,
   and coordinated scaling across sites, requiring proper allocation and
   operation of both compute and network resources in order to preserve
   the required expectations from customers and providers.  Existing
   orchestration systems often depend on fragmented visibility of
   infrastructure resources (in both compute and network domains) and
   must interact with multiple management systems before determining
   service feasibility.

   This document discusses the role of network abstractions in Telco-
   Cloud environments benefiting the interplay and operation of cloud
   and network domains, building up a true Telco-Cloud approach.  It
   identifies abstraction dimensions that can simplify service
   orchestration while enabling scalable operation across heterogeneous
   network and cloud infrastructures.
- **draft-liao-ace-est-c509-01** (new-draft, score 0, ignored_after_review) [none]: [EST for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-ace-est-c509/) — This document defines Enrollment over Secure Transport (EST) protocol
   operations over HTTPS for use with C509 certificates.  The operations
   specified in this document support CA certificate distribution, C509
   certificate enrollment, C509 certificate re-enrollment, and server-
   side key generation using C509 certificates.  This document also
   defines operations for Certificate Revocation List (CRL)
   distribution.
- **draft-lin-idr-bgp-ecmp-ebgp-enhancements-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Enhancements for ECMP EBGP Scenarios](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-ecmp-ebgp-enhancements/) — This document proposes extensions to BGP to apply the RFC 5004 route
   persistence algorithm across parallel EBGP sessions and to suppress
   unnecessary advertisements between EBGP peers in the same AS.

   This document updates RFC 5004.
- **draft-liu-cadi-01** (new-draft, score 0, ignored_after_review) [none]: [Cryptographic Asset Discovery and Inventory](https://datatracker.ietf.org/doc/draft-liu-cadi/) — This document compiles existing Cryptographic Asset Discovery and
   Inventory (CADI) methods and analyze potential gaps.
- **draft-liu-grow-bmp-multiple-peer-header-02** (new-draft, score 0, ignored_after_review) [none]: [Definition for BMP Multiple Peer Header](https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/) — This document proposes a format of multiple peer header for
   aggregating BMP messages.  It can be used to compress multiple BMP
   messages with per-peer header into one aggregated BMP message, which
   could reduce the amount of reported BMP messages and reduce network
   overhead.
- **draft-liu-grow-bmp-rm-aggregated-06** (new-draft, score 0, ignored_after_review) [none]: [Definition for Aggregated BMP Route Monitoring Message](https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/) — This document proposes an aggregated BMP Route Monitoring message
   based on the BMP Multi-Peer Header message (draft-liu-grow-bmp-
   multiple-peer-header).  It can compress multiple BMP Route Monitoring
   messages into one aggregated BMP Route Monitoring message to reduce
   the amount of reported BMP Route Monitoring messages and reduce the
   network overhead.
- **draft-mahy-cbor-pointer-01** (new-draft, score 0, ignored_after_review) [none]: [CBOR Pointer: Selecting Elements of Concise Binary Object Representation (CBOR) Documents](https://datatracker.ietf.org/doc/draft-mahy-cbor-pointer/) — CBOR Pointer is a syntax to identify a single CBOR value from a CBOR
   document with an arbitrarily complex nested structure.  It is
   analogous to JSON Pointer.
- **draft-mahy-mimi-credential-preauth-00** (new-draft, score 0, ignored_after_review) [none]: [MIMI Preauthorization based on deep references to MLS Credentials](https://datatracker.ietf.org/doc/draft-mahy-mimi-credential-preauth/) — This document describes a Work-In-Progress syntax called claim
   pointers that identify specific items in structured credentials,
   which often have nested levels of hierarchy; and claim matchers that
   facilitate comparisons between items in credentials and a target
   value.  It also describes a new version of the More Instant Messaging
   Interoperability (MIMI) preauthorization format using claim pointers
   and claim matchers.
- **draft-mazilu-tcpm-packet-trimming-00** (new-draft, score 0, ignored_after_review) [none]: [TCP Packet Trimming Extension](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) — This document specifies a TCP extension that enables TCP endpoints in
   data center networks or similarly controlled administrative domains
   to use packet trimming information when it is available.  When switch
   buffers exceed a threshold, rather than silently dropping a packet,
   the switch trims the payload and forwards the header.  This allows
   the destination to issue a deterministic Negative Acknowledgment
   (NACK), enabling faster, more deterministic loss recovery.
- **draft-melegassi-ippm-mvps-gddp-00** (new-draft, score 0, ignored_after_review) [none]: [Geometric Dilution of Detection Precision for Multi-Vantage Path Snapshots](https://datatracker.ietf.org/doc/draft-melegassi-ippm-mvps-gddp/) — GPS positioning accuracy degrades with anchor geometry; the effect
   is quantified by the well-known Geometric Dilution of Precision
   (GDOP).  Multi-vantage anomaly detection systems face the DUAL
   problem: how does anchor geometry affect DETECTION SENSITIVITY
   rather than localisation accuracy?

   This document formalises Geometric Dilution of Detection Precision
   (GDDP) for the Multi-Vantage Path Snapshot (MVPS) framework
   [I-D.melegassi-ippm-mvps-bundle].  The minimum displacement that
   a multi-vantage detector can reliably distinguish from measurement
   noise is NOT a single number: it is an anisotropic scalar field
   d*(v, theta) over the Earth's surface, governed by the geometry of
   the anchor set relative to each vantage.

   Three main results are proved:

   (1) GDDP Theorem (T-GDDP-1): d*(v, theta) admits a closed-form
       expression in terms of the Fisher Information of the anchor-
       to-vantage RTT-ratio vector.  The directional detection threshold
       is d*(theta) = sqrt(chi2_crit / I(theta)), where I(theta) is
       the Fisher Information in direction theta.  This is the
       Cramer-Rao bound applied to detection.

   (2) Anisotropy Lemma (L-GDDP-2): every vantage has a "blind cone"
       -- a set of directions in which displacement barely changes the
       RTT-ratio vector and detection sensitivity degrades.  The blind
       cone is quantifiable and, for isolated vantages, can span over
       70% of the compass.

   (3) Monotonicity Theorem (T-GDDP-3): adding an anchor NEVER reduces
       the Fisher Information of the system (Shannon chain rule applied
       to detection channels).  There exists a principled anchor-
       placement optimisation: minimise max_theta d*(v, theta) over
       candidate sites.

   All three are validated to three layers of proof: canonical (math),
   empirical (deterministic scripts, seed=1337), and real data (RIPE
   Atlas measured RTTs, 92,067 D-squared values from 40 probes, 11/11
   checks PASS).  No simulation-only claim is made.

   The GDDP/GDOP duality has not, to the author's knowledge, been
   previously formalised.  VerLoc (Kohls and Diaz, USENIX Security
   2022) observes the directional effect empirically but does not derive
   d*(v, theta) or propose a geometric defence.
- **draft-melegassi-mvps-ddos-resilience-02** (new-draft, score 0, ignored_after_review) [none]: [Volume-Independent DDoS Detection via Coherence-BFD: The MVPS DDoS Resilience Profile](https://datatracker.ietf.org/doc/draft-melegassi-mvps-ddos-resilience/) — This document specifies how the Multi-Vantage Path Synchrony
   (MVPS) framework [I-D.melegassi-ippm-mvps-bundle] and its
   sub-tick variant Coherence-BFD
   [I-D.melegassi-coherence-bfd] detect volumetric and
   distributed Denial-of-Service (DDoS) attacks in time bounded
   by (M-1)*T_tick, INDEPENDENT of the attack rate in packets-
   per-second or bits-per-second.

   Three theorems are proved:

      Theorem D1 (Volume-Independence).  Detection latency is a
      function of the control-tick period T_tick and the
      M-multiplier confirmation count alone; it does not grow
      with attack volume.

      Theorem D2 (Distributed-Attack Bound).  The framework
      detects up to floor((k-1)/2) simultaneous regional
      attacks under cell-aware minimax aggregation, where k is
      the number of coherence cells.

      Theorem D3 (Broker NIC Sizing).  Under the three
      architectural invariants of Section 3, broker NIC sizing
      is independent of attack volume; it is determined only
      by the legitimate telemetry packets-per-second.

   This revision (-02) adds seven confirmed real-world
   DDoS detections using a causally-direct methodology:
   BGP updates measured on each VICTIM'S OWN announced
   prefix (not on unrelated third-party infrastructure).

     (a) 7 independently confirmed DDoS attacks across
         3 continents (Australia, South Africa, New
         Zealand), spanning two orders of magnitude in
         target size (from a major OS vendor to a small
         22-year-old regional host): VentraIP (600 Gbps),
         Canonical (3.5 Tbps), Binary Lane (400 Gbps),
         Network Platforms (676 Gbps), Xneelo (300 Gbps),
         SiteHost NZ, and 1-Grid (100 Gbps).  30 of 33
         tested prefixes (91%) alarmed on the confirmed
         attack day; 4 of 7 targets show 100% prefix
         corroboration.

     (b) VentraIP: BGP alarm fired the SAME HOUR as
         attack onset (00:00 UTC, D^2=11.7), four hours
         BEFORE mitigation began.  Canonical: BGP alarm
         fired 2 hours BEFORE Cloudflare migration began.

     (c) Joint statistical significance across all 7
         targets (multi-prefix binomial test):
         P < 5.9*10^-60 under the null hypothesis that
         alarms are unrelated to attack timing -- 52
         orders of magnitude beyond the 5-sigma particle-
         physics discovery threshold.

     (d) Volume-independence (D1) confirmed: 1-Grid
         (100 Gbps) produced a HIGHER D^2 (63.2) than
         Canonical (3500 Gbps, D^2=10.6).  Detection
         depends on coherence deformation, not attack
         bandwidth.

     (e) An invalid claim from an intermediate draft
         (RIPE Atlas K-root time-coincidence implying
         53.6-hour pre-report detection) was identified
         via a Monte Carlo control test as a look-
         elsewhere/base-rate artifact and RETRACTED
         (Section 7.7.1), then replaced with the
         causally-direct results above.
- **draft-nandakumar-moq-tempo-00** (new-draft, score 0, ignored_after_review) [none]: [TEMPO: Timing Extension for Media Playout Orchestration over MoQ](https://datatracker.ietf.org/doc/draft-nandakumar-moq-tempo/) — This document defines TEMPO (Timing Extension for Media Playout
   Orchestration), a synchronized playout mechanism for media tracks
   delivered over the Media over QUIC Transport (MoQT) protocol.  The
   Original Publisher stamps each object with when it should be played
   out and when it was sent.  Relays replace the send-time stamp with
   their own clock as they forward, giving each subscriber a fresh
   timing reference from its nearest relay.  Subscribers use these
   timestamps to decide when to render each object, and report their
   sync state directly to a coordination server (PlaySyncServer) that
   can tell the media publisher to adjust timing when subscribers fall
   behind.
- **draft-nygren-dnsop-ipv6only-indicator-00** (new-draft, score 0, ignored_after_review) [none]: [Indicating IPv6-only SVCB Endpoints and IPv4 Deprecation in the DNS](https://datatracker.ietf.org/doc/draft-nygren-dnsop-ipv6only-indicator/) — As the DNS is the primary mechanism for translating from hostnames to
   IP addresses, it is a logical place to signal that endpoints are
   IPv6-only.  It is thus also a logical place to signal that legacy
   endpoints supporting IPv4 are being deprecated.  This specification
   introduces two SvcParams for SVCB-compatible RR types that signal
   IPv6-only endpoints (ipv6only) as well as deprecated endpoints
   (deprecated).

   TO BE REMOVED: This document is being collaborated on in Github at:
   https://github.com/enygren/draft-nygren-dnsop-ipv6only-indicator
   (https://github.com/enygren/draft-nygren-dnsop-ipv6only-indicator).
   The most recent working version of the document, open issues, etc.
   should all be available there.  The authors (gratefully) accept pull
   requests.
- **draft-pamtv-netconf-error-registries-01** (new-draft, score 0, ignored_after_review) [none]: [Error List and Error Identities Registries for YANG-driven protocols](https://datatracker.ietf.org/doc/draft-pamtv-netconf-error-registries/) — This document defines IANA registries for the YANG Protocol Error
   List and YANG Protocol Error Identities.
- **draft-petra-green-api-04** (new-draft, score 0, ignored_after_review) [none]: [Path Energy Traffic Ratio API (PETRA)](https://datatracker.ietf.org/doc/draft-petra-green-api/) — This document describes an API to query a network regarding its
   Energy Traffic Ratio for a given path.
- **draft-piraux-space-constellation-code-02** (new-draft, score 0, ignored_after_review) [none]: [A code to describe satellite constellations](https://datatracker.ietf.org/doc/draft-piraux-space-constellation-code/) — When considering a satellite constellation forming a non-terrestrial
   network, the characteristics of this constellation heavily influence
   the network topology it forms.  To improve the analysis of such non-
   terrestrial networks across various tools developed by the network
   community, this document defines a constellation code to describe
   common orbital shell patterns, and specification formats to describe
   inter-satellite link topologies and ground stations, covering the
   Core and Ground Networks of a constellation.  In addition, this
   document may serve as an introduction to satellite constellations for
   IETF participants.
- **draft-pskim-ros2-quic-mqtt-00** (new-draft, score 0, ignored_after_review) [none]: [QUIC Application for ROS2 with MQTT](https://datatracker.ietf.org/doc/draft-pskim-ros2-quic-mqtt/) — While DDS (Distributed Data Service) protocol, managed by Object
   Management Group (OMG), for ROS (Robot Operating System) 2 is
   intended to provide a universal communication layer,
   interoperability across different DDS middleware implementations is
   not always consistent. Variations in transport protocol usage (e.g.,
   TCP/IP, UDP, shared memory) can hinder direct data exchange, and
   cross-domain communication efficiency is generally lower compared to
   protocols such as HTTP. Therefore, to resolve limitations of DDS in
   ROS2, this draft considers a couple of standards protocols, QUIC of
   IETF and MQTT (Message Queuing Telemetry Transport), managed by
   OASIS Open.
- **draft-sahib-dnsop-survey-dcv-techniques-00** (new-draft, score 0, ignored_after_review) [none]: [A Survey of Domain Control Validation Techniques using DNS](https://datatracker.ietf.org/doc/draft-sahib-dnsop-survey-dcv-techniques/) — [I-D.draft-ietf-dnsop-domain-verification-techniques] describes best
   practices for using the DNS to verify ownership or control of a
   domain, a process generally referred to as "Domain Control
   Validation".  This document is a companion survey that catalogs the
   DNS-based Domain Control Validation techniques in use today across a
   range of Application Service Providers and protocols.
- **draft-schinazi-httpbis-ohttp-ext-key-config-00** (new-draft, score 0, ignored_after_review) [none]: [An Extensible Key Configuration Format for Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-ext-key-config/) — Oblivious HTTP is a protocol for forwarding encrypted HTTP messages.
   This requires communicating the gateway's key configuration to
   clients.  While a key configuration media type was defined for this
   purpose, it has some limitations such as the inability to convey key
   lifetimes and interoperability issues.  This document defines a
   similar extensible key configuration format that addresses those
   issues.
- **draft-schinazi-httpbis-ohttp-pfs-00** (new-draft, score 0, ignored_after_review) [none]: [A Perfect Forward Secure Extension to Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-pfs/) — Oblivious HTTP (OHTTP) is a protocol for forwarding encrypted HTTP
   messages.  It does not provide Perfect Forward Secrecy (PFS).
   Chunked OHTTP expands OHTTP to be suitable for longer-lived streams,
   but still does not offer PFS.  Combined, this is leading sensitive
   traffic to de deployed at scale without PFS.  This document proposes
   a solution.
- **draft-sullivan-tls-signed-ech-updates-02** (new-draft, score 0, ignored_after_review) [none]: [Authenticated ECH Config Distribution and Rotation](https://datatracker.ietf.org/doc/draft-sullivan-tls-signed-ech-updates/) — Encrypted ClientHello (ECH) requires clients to have the server's ECH
   configuration before connecting.  Currently, when ECH fails, servers
   can send updated configurations but clients cannot authenticate them
   unless the server has a valid certificate for the public name,
   limiting deployment flexibility.

   This document specifies a new mechanism for authenticating ECH
   configurations.  Servers include additional information in their
   initial ECH configurations, which enables clients to authenticate
   updated configurations without relying on a valid certificate for the
   public name.
- **draft-sullivan-tls-xof-ciphers-00** (new-draft, score 0, ignored_after_review) [none]: [TLS 1.3 Cipher Suites with Alternative Key-Schedule Profiles](https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-ciphers/) — TLS 1.3 builds its key schedule on HKDF over the cipher suite's hash.
   This document defines TLS 1.3 cipher suites that build it on a deck
   function over a single permutation instead, the one a deployment
   already carries when it uses SHA-3, ML-KEM, or ML-DSA.  One
   permutation then runs the whole schedule, and a full handshake takes
   about a third of the permutation calls an HKDF schedule over that
   permutation would.  Such a cipher suite names an AEAD algorithm
   together with a schedule profile that defines every key-schedule
   function the connection uses.  The profile follows from the
   negotiated cipher suite alone, so no new extension is defined and the
   TLS 1.3 state machine and wire format are unchanged.  Two profiles
   are defined, one on the standard SHA-3 function and one on a faster
   reduced-round variant of it.
- **draft-sun-ssh-composite-sigs-03** (new-draft, score 0, ignored_after_review) [none]: [Composite ML-DSA Signatures for SSH](https://datatracker.ietf.org/doc/draft-sun-ssh-composite-sigs/) — This document describes the use of PQ/T composite signatures for the
   Secure Shell (SSH) protocol.  The composite signatures described
   combine ML-DSA as the post-quantum part and the elliptic curve
   signature schemes ECDSA, Ed25519 and Ed448 as the traditional part.
- **draft-taylor-dtn-bibe-00** (new-draft, score 0, ignored_after_review) [none]: [Bundle-in-Bundle Encapsulation](https://datatracker.ietf.org/doc/draft-taylor-dtn-bibe/) — This document describes Bundle-in-Bundle Encapsulation (BIBE), a
   Delay-Tolerant Networking (DTN) Bundle Protocol (BP) tunneling
   mechanism by which a bundle is carried as the payload of one or more
   encapsulating bundles, allowing security measures, routing policy,
   and protocol version translation to be applied to the encapsulating
   bundle without modification of the encapsulated bundle.  The protocol
   includes an optional segmentation mechanism, allowing a large
   encapsulated bundle to be carried in multiple encapsulating bundles.
- **draft-templin-6man-fwiw-05** (new-draft, score 0, ignored_after_review) [none]: [Fragmentation Revisited: For What It's Worth](https://datatracker.ietf.org/doc/draft-templin-6man-fwiw/) — Internet Protocol (IP) fragmentation and reassembly have served as
   core elements of the architecture from the very earliest days but
   they have been subject to negative publicity by studies that have
   declared them "harmful" and "fragile".  These warning labels have
   resonated deeply within the community in a way that fosters the
   enemies of sound engineering: fear, uncertainty and doubt.  This
   document revisits IP fragmentation and shows that a properly
   engineered alternative IPv6 solution is both practical and necessary
   to provide a robust service for the future of Internetworking.
- **draft-templin-6man-ipid-ext2-28** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Extended Fragment Header (EFH)](https://datatracker.ietf.org/doc/draft-templin-6man-ipid-ext2/) — The Internet Protocol, version 4 (IPv4) header includes a 16-bit
   Identification field in all packets, but this length is too small to
   ensure reassembly integrity even at moderate data rates in modern
   networks.  Even for Internet Protocol, version 6 (IPv6), the 32-bit
   Identification field included when a Fragment Header is present may
   be smaller than desired for some applications.  Both IPv4 and IPv6
   fragmentation have further been classified as fragile to the point
   that their use is discouraged.  This specification addresses these
   limitations by defining an IPv6 Extended Fragment Header (EFH) that
   includes a 64-bit Identification in the context of more robust,
   secure and efficient fragmentation and reassembly procedures.
- **draft-templin-intarea-ipid-ext2-11** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Extended Fragment Header for IPv4](https://datatracker.ietf.org/doc/draft-templin-intarea-ipid-ext2/) — The Internet Protocol, version 4 (IPv4) header includes a 16-bit
   Identification field in all packets, but this length is too small to
   ensure reassembly integrity even at moderate data rates in modern
   networks.  Even for Internet Protocol, version 6 (IPv6), the 32-bit
   Identification field included when a Fragment Header is present may
   be smaller than desired for some applications.  This specification
   addresses these limitations by adapting the IPv6 Extended Fragment
   Header for IPv4.
- **draft-tojens-diem-arch-visual-aid-00** (new-draft, score 0, ignored_after_review) [none]: [DIEM Architecture Example](https://datatracker.ietf.org/doc/draft-tojens-diem-arch-visual-aid/) — This document defines the architecture for Digital Emblems.
   Standards that define Digital Emblems are expected to do so by
   mapping their mechanisms to the required and optional componented
   defined by this document.
- **draft-venaas-pim-ipv4-in-ipv6-core-01** (new-draft, score 0, ignored_after_review) [none]: [Native IPv4 multicast in IPv6 Core using PIM](https://datatracker.ietf.org/doc/draft-venaas-pim-ipv4-in-ipv6-core/) — This document describes how PIM Sparse-Mode can be used to construct
   IPv4 multicast trees across an IPv6-only network core.  This allows
   forwarding of native IPv4 multicast data packets.  The document
   specifies how to send and receive IPv4 PIM messages with IPv6
   headers, using a new well-known link-local IPv6 multicast address,
   and the use of RPF vectors for reachability.
- **draft-vroonen-idr-bgp-bestpath-nh-selection-03** (new-draft, score 0, ignored_after_review) [idr]: [BGP best path next-hop selection enhancements](https://datatracker.ietf.org/doc/draft-vroonen-idr-bgp-bestpath-nh-selection/) — BGP [RFC4271] has originally been designed to carry IPv4 routing
   information over the Internet.  IP routing being "hop-by-hop" in
   nature, NEXT_HOP which purpose is to carry the address of the next
   router to send the IP packet to.  In BGP, the next-hop may not be a
   directly connected router, hence, when evaluating paths, a BGP
   speaker must determine if the next-hop is resolvable and, if so,
   determine the internal cost to reach it.

   The incremental use of tunneling technologies to carry traffic
   between routers (e.g.: GRE, MPLS, SR-MPLS, SRv6...) may violate the
   assumption that the address carried in the NEXT_HOP is representative
   of the actual forwarding next-hop.  These technologies decouple the
   BGP control-plane's view of the next-hop from the data-plane's actual
   forwarding endpoint.  This document describes the problems that arise
   from this decoupling.  These problems include sub-optimal path
   selection, incorrect resolvability tracking of the forwarding path
   leading to traffic drop or misrouting, and others.  This document
   specifies how BGP obtains resolvability, preference, metric, and
   tracking information from resolution of the forwarding path and uses
   those values as inputs to BGP path selection.
- **draft-wang-cats-green-challenges-08** (new-draft, score 0, ignored_after_review) [none]: [Green Challenges in Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-wang-cats-green-challenges/) — As mobile edge computing networks sink computing tasks from cloud
   data centers to the edge of the network, tasks need to be processed
   by computing resources close to the user side.  Therefore, CATS was
   raised.  Reducing carbon footprint is a major challenge of our time.
   Networks are the main enablers of carbon reductions.  The
   introduction of computing dimension in CATS makes it insufficient to
   consider the energy saving of network dimension in the past, so the
   green for CATS based on network and computing combination is worth
   exploring.  This document outlines a series of challenges and
   associated research to explore ways to reduce carbon footprint and
   reduce network energy based on CATS.
- **draft-wang-space-computing-consideration-01** (new-draft, score 0, ignored_after_review) [none]: [Consideration for Space-Based Computing Infrastructure Network](https://datatracker.ietf.org/doc/draft-wang-space-computing-consideration/) — This document presents considerations for a Space-Based Computing
   Infrastructure Network from use cases and requirements.
- **draft-wang-token-aware-usecases-requirements-00** (new-draft, score 0, ignored_after_review) [none]: [Token Service Flow Awareness: Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wang-token-aware-usecases-requirements/) — This document outlines the use cases and requirements for token
   service flow awareness, providing the IETF working group with a
   standardized reference to better support the assurance of the user’s
   end-to-end experience.
- **draft-wendt-stir-cert-tn-attr-ext-00** (new-draft, score 0, ignored_after_review) [none]: [TN Attribute Certificate Extension for STI Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-cert-tn-attr-ext/) — This document specifies a non-critical X.509 v3 certificate extension
   that conveys a set of self-asserted attributes describing the
   telephone numbers identified in the certificate's TNAuthList.  The
   attributes are declared by the holder of the certificate about its
   own telephone numbers and require no separate authority token,
   because they describe or constrain only those numbers and grant no
   authority to any other party.  The extension defines an extensible
   framework with an IANA registry of attribute types and seeds that
   registry with four types: a PASSporT Placement Service (PPS) URI, a
   do-not-originate indication, a do-not-originate-messaging indication,
   and a set of authorized originating providers.  Relying parties use
   these self-declarations as policy signals, treating communications
   that do not conform to them as candidates for blocking.  The
   mechanism is backward compatible with existing STIR certificates.
- **draft-white-intarea-reordering-04** (new-draft, score 0, ignored_after_review) [none]: [Proposal for Updates to Guidance on Packet Reordering](https://datatracker.ietf.org/doc/draft-white-intarea-reordering/) — Several link technology standards mandate that equipment guarantee
   in-order delivery of layer 2 frames, apparently due to a belief that
   this is required by higher layer protocols.  To meet this requirement
   they implement a "resequencing" operation to restore the original
   packet order.  This can introduce delays that result in net
   degradation of performance.  Modern TCP and QUIC implementations
   support features that significantly improve their tolerance to out-
   of-order delivery.  This draft is intended to provide new information
   for layer 2 technology standards regarding the need to assure in-
   order delivery to support IETF protocols.
- **draft-wilaw-moq-webvtt-msf-00** (new-draft, score 0, ignored_after_review) [none]: [WebVTT Packaging for MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-wilaw-moq-webvtt-msf/) — This document specifies the JSON packaging format for delivering
   WebVTT caption and subtitle content as event timeline tracks within
   the MOQT Streaming Format (MSF).
- **draft-wkumari-dnsop-localroot-bcp-07** (new-draft, score 0, ignored_after_review) [none]: [Populating resolvers with the root zone](https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/) — DNS recursive resolver operators need to provide the best service
   possible for their users, which includes providing an operationally
   robust and privacy protecting service.  Challenges to these
   deployment goals include difficulty of getting responses from the
   root servers (such as during a network attack), longer-than-desired
   round-trip times to the closest DNS root server, and privacy issues
   relating to queries sent to the DNS root servers.  Resolvers can
   solve all of these issues by simply serving an already cached a copy
   of the full root zone.

   This document shows how resolvers can fetch, cache and maintain a
   copy of the root zone, how to detect if the contents becomes stale,
   and procedures for handling error conditions.

   { Editor note: This document contains a FAQ section.  It will help
   answer questions about why this document is not a BCP but still has
   BCP in the name, how and why this document differs from RFC8806, etc
   etc etc.  The FAQ section is intended to be removed before
   publication. }
- **draft-xu-lsvr-midr-use-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Use Cases and Requirements for Multi-Domain and Hybrid Overlay/Underlay BGP-SPF (LSVR)](https://datatracker.ietf.org/doc/draft-xu-lsvr-midr-use-cases/) — This document presents use cases and the routing requirements they
   imply for operating the BGP Link State (BGP-LS) Shortest Path First
   (SPF) routing developed in the Link-State Vector Routing (LSVR)
   Working Group, across multiple administrative domains and over hybrid
   overlay/underlay topologies.  After motivating the work, it describes
   three scenarios of increasing complexity: a single overlay domain,
   the interconnection of multiple overlay domains, and hybrid overlay/
   underlay networks.  Each scenario gives the topology, its
   distinguishing challenges, and the requirements that follow.  The
   scenarios arise in globally distributed edge- and cloud-Point-of-
   Presence (PoP) deployments that serve performance-sensitive
   applications such as cross-region real-time communication,
   collaborative productivity, cloud gaming, and large-scale SaaS.

## Errors / fetch failures

_None._
