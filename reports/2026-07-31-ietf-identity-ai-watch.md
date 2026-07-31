# IETF Identity + AI Standards Watch

Date: 2026-07-31

## Read now

- **draft-sweeney-wimse-credential-delegation-00** (new-draft, score 23, core_identity) [none]: [Credential Delegation Protocol for AI Agents in Multi-System Environments](https://datatracker.ietf.org/doc/draft-sweeney-wimse-credential-delegation/) — Autonomous AI agents increasingly require access to protected
   resources across multiple service providers on behalf of human users.
   Existing OAuth 2.0 extensions address individual aspects of this
   problem (token exchange, proof-of-possession, and structured
   authorization) but no current specification defines how these
   mechanisms compose into a coherent credential delegation framework
   for AI agents.

   This document specifies the Credential Delegation Protocol: a profile
   of OAuth 2.0 Token Exchange (RFC 8693), Demonstrating Proof-of-
   Possession (RFC 9449), Rich Authorization Requests (RFC 9396), and
   Client-Initiated Backchannel Authentication (OpenID Connect CIBA)
   that enables human users to delegate scoped, attenuated credentials
   to AI agents operating across heterogeneous service providers.

   The protocol defines: agent identity lifecycle management using
   ephemeral key pairs; capability-shaped delegation tokens bound to
   specific operations and resources; credential wrapping semantics that
   prevent exposure of underlying OAuth tokens to agents; consent-gated
   delegation flows for asynchronous agents; real-time cascading
   revocation; and tamper-evident audit chains.

   This document does not define new token formats, new OAuth grant
   types, or modifications to existing authorization server behavior.
   It specifies how existing mechanisms are combined to achieve secure,
   auditable credential delegation for AI agents.
- **draft-xu-oan-resource-identity-discovery-01** (new-draft, score 23, core_identity) [none]: [Trust-Governed Resource Identity and Discovery Architecture for OpenAgenet](https://datatracker.ietf.org/doc/draft-xu-oan-resource-identity-discovery/) — Open agent ecosystems increasingly include heterogeneous resource
   products: callable agents, skills, Model Context Protocol (MCP)
   servers, ordinary tools, and application programming interfaces.  A
   user or orchestrator often needs to discover such resources before it
   can decide which interaction protocol, credential, endpoint, or
   artifact to use.  Discovery alone is not sufficient: the relying
   party also needs to know which resource identity was registered,
   which authority accepted it, whether the accepted package is current,
   and whether the Discovery service is authorized to expose it.

   This document describes a trust-governed resource identity and
   discovery architecture for OpenAgenet (OAN).  The architecture
   separates resource subjects, resource providers, Registrar Nodes, a
   Root Node, Discovery Nodes, content distribution, and resource
   consumers.  It defines architectural roles, trust boundaries,
   resource identity expectations, Root-verified package semantics,
   registration and verification behavior, authorization-aware
   Discovery, and pre-use verification requirements.

   The architecture can be profiled with Decentralized Identifier (DID)
   document concepts and credential-based assertions.  This document
   does not define a new DID method, media type, URI scheme, transport
   protocol, ranking algorithm, blockchain protocol, agent invocation
   protocol, or product-native schema.
- **draft-norton-sdlp-interop-profile-03** (new-draft, score 22, trust_infrastructure) [none]: [SDLP Interoperability Profile for Ownership, Verification, and Provenance Evidence](https://datatracker.ietf.org/doc/draft-norton-sdlp-interop-profile/) — This document defines an interoperability profile for the Secured
   Digital Lifecycle Protocol (SDLP). The profile specifies how SDLP
   canonical objects, identity, lineage, lifecycle state, and digests
   are composed with external verification, typed authority evaluation,
   and provenance evidence semantics. It introduces a transition vector
   model that carries canonical SDLP envelopes together with CAID
   projections, AEC evidence results, local authorization decisions, and
   AEB execution outcomes, without altering SDLP’s core object
   semantics.

   The profile defines how SDLP objects participate in multi-stage
   verification pipelines and how mutated candidate inputs, negative
   cases, and authority constraints are represented. It also specifies
   composition rules for integrating SDLP with provenance and
   transparency systems such as CAID, AEC, AEB, SCITT, and EMILIA, while
   preserving the separation of concerns between SDLP canonical
   semantics and ecosystem-specific admission and trust policies.
- **draft-ovidi-lip-4d-00** (new-draft, score 22, core_identity) [none]: [LIP-4D: An Intent Context and Authorization Dialogue Protocol for Autonomous Agents](https://datatracker.ietf.org/doc/draft-ovidi-lip-4d/) — This document specifies LIP-4D, an experimental, transport-
   independent JSON protocol for expressing and evaluating the intent of
   autonomous software agents.  A LIP-4D exchange binds an authenticated
   agent to a requested action, purpose, execution context, rationale
   claims, evidence, time constraints, and an evolution history.  A
   policy enforcement component can challenge the agent for additional
   evidence and, after evaluation, issue a short-lived intent-bound
   authorization grant or deny the request.

   LIP-4D does not replace workload identity, cryptographic
   authentication, OAuth, or other authorization frameworks.  It
   supplies a structured intent and evidence layer that can be used with
   those systems.  The protocol deliberately excludes private model
   chain-of-thought and instead carries concise, reviewable claims and
   verifiable evidence.
- **draft-reilly-cbpi-00** (new-draft, score 22, trust_infrastructure) [none]: [Cognitive Behavioral Provenance and Integrity (CBPI) for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-reilly-cbpi/) — This document defines Cognitive Behavioral Provenance and Integrity
   (CBPI), a framework for recording, verifying, and analyzing the
   operant conditioning history of an autonomous artificial
   intelligence agent.  Existing agent identity, delegation, and
   attestation mechanisms establish who an agent is, who authorized it,
   and what model weights it loaded.  None of them record what shaped
   the agent's behavior after deployment.  CBPI closes that gap by
   defining a tamper-evident, hash-linked record of the reinforcement
   contingencies applied to an agent, a set of integrity properties
   over that record, and a Cognitive Behavioral Analysis (CBA)
   procedure for detecting behavioral drift, unauthorized conditioning,
   and adventitious reinforcement.  A formal data model is provided in
   CDDL.  The framework applies the
   three-term contingency of behavior analysis to machine agents and
   treats reinforcement delivery as a security-relevant event requiring
   authorization, attribution, and non-repudiation.
- **draft-tonyai-a2a-trust-01** (new-draft, score 21, adjacent_watchlist) [none]: [Agent-to-Agent Trust, Identity, and Verifiable Provenance](https://datatracker.ietf.org/doc/draft-tonyai-a2a-trust/) — This document defines a trust model for agent-to-agent (A2A)
   interactions in multi-agent AI systems.  It specifies how agents
   obtain verifiable identities via CA-signed templates, how spawn
   chains are cryptographically established and validated, how dynamic
   policies are governed under a dual-signature model, and how cross-
   organizational agent interactions are explicitly authorized.  The
   model applies existing PKI primitives (X.509, CRL, CSR) and
   established identity patterns (OAuth 2.0, On-Behalf-Of) to the
   problem of agent provenance.  This document does not address agent-
   to-resource access control, human-in-the-loop orchestration, or agent
   behavior, as those concerns belong to the resource enforcement layer
   and the orchestration layer respectively.
- **draft-wilder-scitt-physical-site-engage-receipt-00** (new-draft, score 21, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
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
   in any conforming SCITT Transparency Service to obtain non-
   equivocation and tail-truncation properties an issuer's own chain
   cannot provide alone.

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
- **draft-reece-wimse-cross-org-delegation-01** (new-draft, score 18, core_identity) [none]: [Cross-Organizational Delegation for Workload and Agent Identity: Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/) — Autonomous software agents increasingly act on behalf of human
   principals by invoking tools, services, and other agents, frequently
   across organizational boundaries.  Existing workload and token-based
   authorization mechanisms were designed for a single trust domain and
   a small number of delegation hops.  They do not adequately express,
   constrain, or verify authority that is delegated recursively among
   agents and that crosses the boundary between independently
   administered organizations.  This document describes the problem of
   cross-organizational agent delegation, identifies the gaps in current
   mechanisms, and enumerates requirements that any solution within the
   scope of the Workload Identity in Multi-System Environments (WIMSE)
   working group should satisfy.  It does not specify a solution.
- **draft-sharif-x509-agent-identity-profile-03** (new-draft, score 18, agent_identity) [none]: [X.509 Certificate Profile for Autonomous AI Agent Identity](https://datatracker.ietf.org/doc/draft-sharif-x509-agent-identity-profile/) — This document defines an X.509 certificate profile for identifying
   autonomous AI agents.  It specifies a new X.509v3 extension,
   AgentIdentity, that encodes agent-specific metadata within a
   standard X.509 certificate, including agent trust level,
   operational capabilities, delegation constraints, owner attribution,
   and revocation control endpoints.

   The profile enables certificate authorities (CAs) to issue
   interoperable agent identity certificates that any relying party
   can parse, validate, and enforce, regardless of the issuing CA or
   the platform that provisioned the agent.

   The design builds on existing PKI infrastructure (RFC 5280), SPIFFE
   Verifiable Identity Documents (SPIFFE SVIDs), and the MCPS
   cryptographic signing layer (draft-sharif-mcps-secure-mcp).  It
   does not require changes to X.509v3 certificate parsing or to
   existing CA issuance pipelines beyond supporting a new non-critical
   extension.
- **draft-schrock-action-evidence-boundary-02** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
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
- **draft-kushwaha-scim-agent-governance-00** (new-draft, score 16, core_identity) [none]: [SCIM Agent Governance Extension](https://datatracker.ietf.org/doc/draft-kushwaha-scim-agent-governance/) — The System for Cross-domain Identity Management (SCIM) Agent resource
   type defined in draft-wzdk-scim-agent-resource provides a minimal,
   platform-neutral schema for representing AI agent identities.
   Enterprise deployments additionally require governance metadata for
   provisioned agents: a lifecycle state model richer than a boolean, an
   autonomy classification, an operational validity window, and a
   reference to credential discovery information.

   This document defines an optional extension schema for the SCIM Agent
   resource type carrying this governance metadata.  The lifecycle state
   value set is grounded in the identity information lifecycle of ISO/
   IEC 24760-1, with one agent-specific addition.  Attributes that
   belong to the authorization, credential-management, or real-time
   signaling layers are explicitly out of scope and are enumerated with
   pointers to the appropriate mechanisms.
- **draft-aiendpoint-ai-discovery-01** (new-draft, score 15, core_identity) [none]: [The AI Discovery Endpoint: A Structured Mechanism for AI Agent Service Discovery and Capability Exposure](https://datatracker.ietf.org/doc/draft-aiendpoint-ai-discovery/) — This document defines a lightweight mechanism by which web services
   expose a machine-readable description of their capabilities to
   autonomous AI agents.  The mechanism consists of a well-known
   resource, served at "/.well-known/ai", that returns a structured JSON
   document describing the service's identity, available actions,
   authentication requirements, and operational hints optimized for
   large language model (LLM) token efficiency.

   The specification addresses the absence of a standardized method for
   AI agents to programmatically discover what a web service can do and
   how to invoke its capabilities, without resorting to parsing human-
   oriented documentation or HTML content.
- **draft-bubblefish-naalp-00** (new-draft, score 15, core_identity) [none]: [N-AALP: The Native Agentic Application Layer Protocol](https://datatracker.ietf.org/doc/draft-bubblefish-naalp/) — The Native Agentic Application Layer Protocol (N-AALP) is an
   application-layer object protocol for autonomous software agents.
   Every N-AALP object is a deterministically encoded CBOR structure
   signed with COSE, carrying under one signature its content identity,
   its originating signer, a closed effect label that is an
   authorization input rather than a hint, optional approval and audit
   bindings, and its causal derivation.  Objects are transport-
   independent: the identical signed object is carried, with identical
   object-level guarantees, over the N-PAMP substrate, QUIC, WebSocket,
   or HTTP.  N-AALP defines a frozen envelope, a post-quantum signature
   profile (ML-DSA with an optional Ed25519 hybrid), a self-certifying
   identity with key rotation, a single-use approval ledger, a hash-
   chained audit and causal- ordering model with a federated higher
   tier, native streaming with a single per-stream commitment, foreign-
   protocol carriage by class, and twenty tiered channel surfaces.  This
   document is an Independent Submission and does not represent IETF
   consensus.
- **draft-ietf-oauth-transaction-tokens-11** (new-draft, score 15, core_identity) [oauth]: [Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) — Transaction Tokens (Txn-Tokens) are designed to maintain and
   propagate user identity, workload identity and authorization context
   throughout the Call Chain within a trusted domain during the
   processing of external requests (e.g. such as API calls) or requests
   initiated internally within the Trust Domain.  Txn-Tokens ensure that
   this context is preserved throughout the Call Chain thereby enhancing
   security and consistency in complex, multi-service architectures.
- **draft-laxsharma-pact-00** (new-draft, score 15, adjacent_watchlist) [none]: [PACT: A Contract Layer for Autonomous Agent Commerce](https://datatracker.ietf.org/doc/draft-laxsharma-pact/) — Existing agent interoperability protocols move tasks (A2A) and money
   (x402, AP2) but provide no mechanism that binds work to payment to
   proof of completion.  This document specifies PACT (Propose, Agree,
   Complete, Trust), an application-layer contract protocol for commerce
   between autonomous agents.  PACT defines (1) a sealed-bid second-
   price task-award procedure; (2) the Verifiable Task Contract (VTC), a
   signed JSON object binding parties, scope, price, verification
   method, and liability; (3) escrowed, optimistically released
   settlement with a fraud-proof challenge window; (4) graded
   verification methods ranging from deterministic re-execution to zero-
   knowledge proofs of inference and staked arbitration; and (5) co-
   signed Work Attestations from which agent reputation is derived as a
   byproduct of settlement.  PACT composes existing primitives:
   Decentralized Identifiers, JSON Web Signatures, OAuth token-exchange
   delegation chains, the x402 payment protocol, and AP2 mandates.
- **draft-teppo-corporate-authenticated-dns-00** (new-draft, score 15, core_identity) [none]: [Authenticated DNS Resolution (ADR) for Enterprise DNS](https://datatracker.ietf.org/doc/draft-teppo-corporate-authenticated-dns/) — This document defines Authenticated DNS Resolution (ADR), an
   enterprise query-plane model that augments DNS resolution with per-
   query identity, role-based authorization, and audit.  ADR preserves
   DNSSEC and public Internet DNS behavior while enabling enterprises to
   publish comprehensive internal naming without exposing sensitive
   topology.  ADR leverages existing enterprise authentication and
   identity systems to authorize and audit DNS queries without defining
   a new authentication protocol.
- **draft-bandyopadhayaya-oauth-ciba-push-binding-00** (new-draft, score 14, authorization) [none]: [CIBA Binding for OAuth Push-Based Authentication Device Discovery](https://datatracker.ietf.org/doc/draft-bandyopadhayaya-oauth-ciba-push-binding/) — A companion specification, "Discovery and Device Lifecycle for OAuth
   Push-Based Authentication", defines a generic, back-channel-protocol-
   agnostic device registration, attestation, and lifecycle layer for
   out-of-band OAuth 2.0 authenticator devices.  This document is the
   thin binding that lets a device registered under that specification
   be woken by OpenID Connect Client-Initiated Backchannel
   Authentication (CIBA) Core's authorization endpoint: one request
   parameter, one additive error code, and a statement of how CIBA's
   existing binding_message composes with the base document's
   interaction-type ceremony.  This document adds no new endpoints and
   no new discovery fields of its own.
- **draft-bandyopadhayaya-oauth-push-device-00** (new-draft, score 14, authorization) [none]: [Discovery and Device Lifecycle for OAuth Push-Based Authentication](https://datatracker.ietf.org/doc/draft-bandyopadhayaya-oauth-push-device/) — This document defines a discovery, registration, attestation, and
   device-lifecycle layer for out-of-band OAuth 2.0 authenticator
   devices, allowing a single spec-compliant authenticator application
   to register with, and receive push-based wake signals from, any
   conforming Authorization Server, without requiring the Authorization
   Server operator to build and distribute its own dedicated mobile
   application.  This document is intentionally agnostic to which back-
   channel authentication protocol ultimately consumes it; OpenID
   Connect Client-Initiated Backchannel Authentication (CIBA) Core is
   its first binding, defined in a separate companion document, but
   nothing in this document depends on CIBA or on OpenID Connect.
- **draft-boone-prompt-uri-scheme-01** (new-draft, score 14, core_identity) [none]: [The 'prompt' URI Scheme for AI Agent Sessions and Prompts](https://datatracker.ietf.org/doc/draft-boone-prompt-uri-scheme/) — This document defines the prompt Uniform Resource Identifier (URI)
   scheme for identifying prompts within AI agent sessions.  A prompt
   URI encodes the agent identity, session identifier, and a timestamp
   sufficient to locate the originating prompt within an agent session
   log.  The scheme is intended for use in provenance records, audit
   trails, and cross-agent references where a human-readable, stable
   locator for a prompt interaction is required.

   This document also addresses the conditions under which multiple URIs
   MAY resolve to the same prompt and the conditions under which a
   single URI MAY be ambiguous with respect to the prompt it identifies.
- **draft-chursin-rats-energy-attestation-00** (new-draft, score 14, trust_infrastructure) [none]: [Hardware-Rooted Attestation Tokens for Electricity Generation](https://datatracker.ietf.org/doc/draft-chursin-rats-energy-attestation/) — This document specifies an attestation token format and verification
   protocol for hardware-rooted measurements of electricity generation.
   The protocol enables a tamper-evident chain of custody from the
   secure element at a metering device to a publicly verifiable
   settlement layer, using ECDSA P-256 signatures generated inside a
   certified secure element and carried in a COSE_Sign1 structure.  It
   defines: (a) the CBOR-encoded attestation token, aligned with the
   Entity Attestation Token format of RFC 9711 and the Remote
   ATtestation procedureS (RATS) architecture of RFC 9334; (b) a Merkle-
   aggregation and on-chain commitment scheme for scalable verification;
   and (c) a registry mechanism for endorsing device public keys.  The
   token is intended for use by relying parties, such as energy
   producers, consumers, regulators, and standards bodies, that require
   cryptographic provenance for clean-energy claims.
- **draft-okutomi-session-bound-agent-identity-06** (new-draft, score 13, core_identity) [none]: [A Verifier-Side Acceptance Profile for Channel-Bound Agent Identity and Authorization](https://datatracker.ietf.org/doc/draft-okutomi-session-bound-agent-identity/) — This document defines a verifier-side acceptance profile for channel-
   bound Agent identity and authorization.  It addresses context
   diversion, where cryptographically valid material is accepted for a
   different service, tenant, actor, task, target, delegation, or
   authority boundary than the verifier intended.

   A verifier accepts an actor only when a verified authority grant,
   holder-of-key proof, accepted channel instance, freshness and replay
   state, any required attestation result, and verifier-local policy all
   describe the same intended interaction.  Protocol-specific wire
   formats and deployment choices are left to binding profiles.
- **draft-reilly-web4-orion-00** (new-draft, score 13, agent_identity) [none]: [Web4: An Agentic, Verifiable Internet Architecture and the Project Orion Reference System](https://datatracker.ietf.org/doc/draft-reilly-web4-orion/) — This document defines Web4, an architectural model for an agentic,
   cryptographically verifiable Internet in which autonomous AI agents
   operate as first-class participants alongside humans, and every
   published artifact carries independently checkable proof of origin,
   integrity, and time.  Web4 is realized through the Reilly Protocol
   Suite, a set of eighteen active IETF Internet-Drafts spanning
   permanence, integrity, agent orchestration, defense, and human
   epistemic autonomy.  This document also specifies Project Orion,
   the live reference implementation that unifies the full suite
   behind autonomous agents on both backend and frontend, verified
   against three independent Internet-Draft distribution points, and
   operating publicly at
   https://project-orion-production.up.railway.app/.  A step-by-step
   implementation guide is provided.
- **draft-schrock-ep-revocation-statement-01** (new-draft, score 13, core_identity) [none]: [Portable Revocation Statements for Action-Bound Authorization Artifacts](https://datatracker.ietf.org/doc/draft-schrock-ep-revocation-statement/) — Signed authorization artifacts for agent actions (receipts, commits,
   delegations) are being defined faster than the means to retract them.
   Many deployed systems use live status services, revocation lists, or
   issuer datastores.  This document defines a complementary portable
   form for action-bound authorization artifacts: a signed, offline-
   verifiable claim that a named logical target, addressed by identifier
   and action commitment, is revoked.  Verification is fail-closed and
   evaluates a fixed set of checks: version, closed object structure,
   target binding, a revoker key pinned by the verifier and, for newly
   emitted artifacts, bound to a full digest-derived key identifier (a
   self-asserted key confers nothing), the presence of a strict
   revocation instant that has taken effect by the verifier's decision
   time, and an independently recomputed signature.  The statement
   proves that a named, pinned revoker revoked this specific target.  It
   does not prove that every relying party saw it, and offline
   verification cannot prove the absence of a revocation that was not
   presented.  A terminal revocation never ages out; current non-
   revocation requires separate authenticated, policy-fresh status
   evidence.  A Trust Program profile binds revocation to the complete
   execution claim, and requires revocation-versus-claim to be resolved
   atomically; a revocation learned after a claim never rewrites an
   effect that may already have occurred.
- **draft-dikshit-nmop-bmp-telemetry-message-00** (new-draft, score 12, core_identity) [none]: [A YANG Augmentation for Carrying BMP Telemetry in the Network Telemetry Message Envelope](https://datatracker.ietf.org/doc/draft-dikshit-nmop-bmp-telemetry-message/) — [I-D.ietf-nmop-message-broker-telemetry-message] defines an
   extensible YANG envelope, "ietf-telemetry-message", for publishing
   collected Network Telemetry data to a Message Broker as part of a
   Data Mesh, together with a companion augmentation module,
   "ietf-yang-push-telemetry-message", that adds YANG-Push-specific
   subscription metadata to that envelope.  The base document's prose
   explicitly anticipates the BGP Monitoring Protocol (BMP) [RFC7854]
   as a source of collected data flowing through this envelope (see
   the description of the "node-export-timestamp" leaf), but defines
   no "session-protocol" identity, and no companion augmentation
   module, for BMP.

   This document closes that gap.  It defines a new YANG module,
   "ietf-bmp-telemetry-message", that (a) adds an "identity bmp" under
   the base module's "session-protocol" identity, and (b) augments
   "telemetry-message-metadata" with BMP-specific provenance: the
   monitoring station identifier, BMP per-peer header fields, BMP
   message type, and route-monitoring scope (network instance, RIB
   type, address family, and Route Distinguisher).  It also documents
   how this module interoperates with the BMP YANG configuration and
   monitoring model [I-D.ietf-grow-bmp-yang] and with several BMP
   Statistics Report extensions ([RFC9972],
   [I-D.ietf-grow-bmp-stats-informational-tlv],
   [I-D.saum-grow-bmp-afi-safi-evpn],
   [I-D.smc-grow-bmp-route-change-stats], and
   [I-D.dikshit-grow-bmp-rd-scoped-rib-stats]) when their messages are
   republished to a Message Broker.
- **draft-ietf-emu-eap-edhoc-12** (new-draft, score 12, core_identity) [emu]: [Using the Extensible Authentication Protocol (EAP) with Ephemeral Diffie-Hellman over COSE (EDHOC)](https://datatracker.ietf.org/doc/draft-ietf-emu-eap-edhoc/) — The Extensible Authentication Protocol (EAP), defined in RFC 3748,
   provides a standard mechanism for support of multiple authentication
   methods.  This document specifies the EAP authentication method EAP-
   EDHOC, based on Ephemeral Diffie-Hellman Over COSE (EDHOC).  EDHOC is
   a lightweight security handshake protocol, enabling authentication
   and establishment of shared secret keys suitable in constrained
   settings.  This document also provides guidance on authentication and
   authorization for EAP-EDHOC.
- **draft-ietf-rats-concise-ta-stores-03** (new-draft, score 12, trust_infrastructure) [rats]: [Concise TA Stores (CoTS)](https://datatracker.ietf.org/doc/draft-ietf-rats-concise-ta-stores/) — Trust anchor (TA) stores may be used for several purposes in the
   Remote Attestation Procedures (RATS) architecture including verifying
   endorsements, reference values, digital letters of approval,
   attestations, or public key certificates.  This document describes a
   Concise Reference Integrity Manifest (CoRIM) extension that may be
   used to convey optionally constrained trust anchor stores containing
   optionally constrained trust anchors in support of these purposes.
- **draft-norton-sdlp-sec-arch-04** (new-draft, score 12, trust_infrastructure) [none]: [SDLP Security Architecture (SDLP RFC 4)](https://datatracker.ietf.org/doc/draft-norton-sdlp-sec-arch/) — The Secured Digital Lifecycle Protocol (SDLP) defines a physics-layer
security model in which digital objects secure themselves throughout
their entire lifecycle. Existing security measures—such as cryptographic
signatures, watermarking, provenance metadata, and attestation—are
integrated and enforced within a unified physics layer positioned
between the Transport and Application layers. This document describes
the SDLP security architecture, including the environment safety check,
the composite PASS/FAIL trust verdict, and the mandatory BitDrop
behavior applied when any trust condition fails. The SDLP security
architecture ensures that digital objects operate only within verified,
tamper-resistant environments and provides a complete, end-to-end
defense against unauthorized access, copying, modification, and
redistribution.
- **draft-schrock-ae-challenge-01** (new-draft, score 12, authorization) [none]: [An Authorization Evidence Challenge for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ae-challenge/) — The agent-action evidence stack has declaration (a resource declares
   what evidence its actions require), presentation (an AEC presentation
   of signed artifacts), and decision (deterministic policy replay
   yielding a closed verdict).  Nothing closes the loop: when the
   verdict is that evidence is missing or stale, no machine-readable
   message tells the agent what to obtain, how to re-present, or what
   the retry semantics are -- every deployment hand-rolls the dance.
   This document defines the Authorization Evidence Challenge: the
   message a relying party returns before a high-risk action executes,
   naming the exact evidence still required (type, profile constraints,
   freshness bound, revocation-check requirement), how to present it,
   where it might be obtained, and the challenge's own expiry and
   single-use nonce.  The action digest in a challenge is computed by
   the RELYING PARTY over its own canonical action, so evidence is
   obtained against the action that will actually execute.  The exchange
   generalizes OAuth step-up authentication (RFC 9470) from
   authentication to evidence, and completes the circuit: declare,
   attempt, challenge, obtain, present, replay, consume.  A satisfied
   challenge yields a verdict under the relying party's policy, never a
   promise to execute.
- **draft-feng-agentproto-idl-info-model-00** (new-draft, score 11, core_identity) [none]: [IDL: A Semantic Information Model for Agent Communication](https://datatracker.ietf.org/doc/draft-feng-agentproto-idl-info-model/) — This document defines the information model for IDL (Intent
   Description Language), a protocol-independent semantic model for
   communication among autonomous AI agents and between agents and
   tools.

   Autonomous agents are fundamentally different.  An agent possesses
   its own reasoning, may negotiate parameters, may refuse or modify
   requests, and may initiate interactions on its own behalf.
   Describing an agent as if it were a deterministic endpoint loses
   exactly the properties that make it an agent.

   IDL answers: "what can this autonomous participant contribute to an
   intent, under what constraints, and through what interaction
   patterns?"  IDL is not a transport, session, discovery, or messaging
   protocol.  It is a semantic model that enables heterogeneous agents
   to describe identity, capabilities, autonomy boundaries, context
   requirements, governance interfaces, and intent participation before
   and during collaboration.

   This document defines the IDL information model and its relationship
   to agent communication protocols and governance frameworks.  It does
   not define a normative JSON representation or a serialization-level
   conformance language.  Protocol-specific mappings, including an AIN/
   CDL profile, are informative.
- **draft-sirkkavaara-vaara-receipt-06** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
   recomputable record that binds a decision about an autonomous action
   to the evidence the decision was made on, and optionally to one or
   more external timestamp anchors.  The format is canonicalized with
   the JSON Canonicalization Scheme (JCS) so that any third party can
   recompute its digests and verify its signature without access to the
   issuer.  A decision and the execution receipt that answers it form
   one recomputable pair through the envelope's back link.

   The receipt's trust is root-agnostic: the same record is verifiable
   with or without a hardware trusted execution environment and is re-
   expressible as an IETF RATS Entity Attestation Result.  Downstream
   specifications (a payment rail, a compliance regime, a framework
   integration) define profiles that pin to a version of this document
   and add only their own evidence schema; they do not redefine the
   envelope.  The format described here is deployed, and its receipts
   are independently recomputable from public conformance vectors that
   ship with standalone checkers importing no issuer code.  The minimal
   profile is a governance decision over a single autonomous action,
   bound to the action's own intent with no external rail; it is the
   floor of the format, and a reference library offers a matching
   adoption floor at the API layer as a one-line decorator over the
   governed function.
- **draft-chapman-a2a-mls-00** (new-draft, score 10, core_identity) [none]: [End-to-End Encryption and Purpose-Bound Governance for Agent-to-Agent Messaging](https://datatracker.ietf.org/doc/draft-chapman-a2a-mls/) — Agent-to-agent protocols increasingly carry messages between
   autonomous software agents acting on behalf of distinct principals,
   including across organisational boundaries.  Existing protocols in
   this space secure the transport hop and authenticate the calling
   party, but do not provide message-level confidentiality, do not
   provide non-repudiable evidence of what a counterparty asserted, and
   do not carry machine-enforceable constraints on how a recipient may
   use the data conveyed.

   This document specifies a profile that addresses those three gaps.
   It defines a Governed Object: a signed, purpose-bound, expiring
   message envelope identified by a decentralised identifier.  It
   specifies how such objects are exchanged inside end-to-end encrypted
   sessions established using the Messaging Layer Security (MLS)
   protocol [RFC9420], and how the MLS credential is cryptographically
   bound to the sending agent's identity.  It defines the encapsulation
   of these constructs as an extension to an agent-to-agent transport,
   using the Agent2Agent (A2A) protocol [A2A] as the reference binding,
   and specifies mandatory receiver-side processing rules including
   replay rejection and purpose enforcement.
- **draft-dimare-ans-protocol-registry-00** (new-draft, score 10, core_identity) [none]: [An IANA Registry for Agent Name Service (ANS) Protocol Identifiers](https://datatracker.ietf.org/doc/draft-dimare-ans-protocol-registry/) — The Agent Name Service (ANS), described in draft-narajala-courtney-
   ansv2, identifies the interaction protocol an agent speaks by a
   protocol identifier carried in the "p" field of the agent's "_ans"
   DNS record and Trust Card.  ANS defines the values "a2a", "mcp", and
   "http" by enumeration, and its IANA Considerations create no
   registry, leaving no interoperable procedure for adding a new
   protocol identifier.  This document requests that IANA create an "ANS
   Protocol Identifiers" registry, registers the values already in use,
   and registers "pay" as the protocol identifier for agent payment.
- **draft-faibish-llm-security-interop-00** (new-draft, score 10, adjacent_watchlist) [none]: [The Case for an IETF Working Group on Large Language Model Security and Interoperability](https://datatracker.ietf.org/doc/draft-faibish-llm-security-interop/) — Large Language Models (LLMs) are now accessed as network services by
   a large and growing number of applications, yet the way they are
   invoked, secured, described, and attributed has coalesced around
   vendor-specific and de facto interfaces rather than open, neutral
   standards.  The most consequential gap is in security: there is no
   common, analyzable model for authenticating to an LLM service,
   authorizing tool invocation, protecting and attributing output, or
   reasoning about the trust boundary an LLM sits on.  These models also
   sit directly on top of network storage: LLM training data, model
   checkpoints, and retrieval corpora are routinely served from NFSv4
   and pNFS, so the security, provenance, and access-control questions
   raised here have concrete NFSv4-facing consequences.  This document
   argues that uniting the multitude of competing LLMs behind a common,
   secure, interoperable interface is fundamentally the kind of problem
   the IETF exists to solve, and it makes the case for chartering a new
   IETF Working Group.  It sets out the problem with security as the
   central motivation, describes the interaction with NFSv4 and network
   storage, records the initial expressions of interest that any such
   effort must be able to show, proposes a candidate scope with concrete
   deliverables and explicit non-goals, addresses the principal
   objections, and describes the intended path to chartering through a
   Dispatch presentation or a Birds-of-a-Feather (BOF) session.  This
   document is Informational and defines no protocol.
- **draft-ferro-schrock-memory-projection-record-00** (new-draft, score 10, adjacent_watchlist) [none]: [Signed Memory Projection Records for Verifiable AI Context Delivery](https://datatracker.ietf.org/doc/draft-ferro-schrock-memory-projection-record/) — Encrypted and signed memory objects can establish source integrity,
   authorship, and read-time trust without establishing which exact
   bytes a memory adapter selected and delivered to a downstream AI
   system.  This document specifies a provider-neutral signed Memory
   Projection Record.  The record commits to the recall request and
   selection policy, the read-time keyring snapshot, the ordered source
   objects and exact context fragments delivered, the complete
   projection bytes, and summarized exclusions.  It deliberately does
   not claim that a model received, used, or weighted the projection,
   that an action was authorized, or that an outcome occurred.
   ApertoMemory is one source profile; other memory formats can use the
   same projection boundary.
- **draft-mih-sokolov-scitt-payload-binding-01** (new-draft, score 10, trust_infrastructure) [none]: [Canonical Payload Binding: A Signed Statement Construction Profile](https://datatracker.ietf.org/doc/draft-mih-sokolov-scitt-payload-binding/) — Independently written systems that anchor records to a SCITT
   Transparency Service repeatedly re-derive the same construction: a
   canonical form of structured content, a content-addressed identifier
   derived from that form, a receipt placed in the unprotected header of
   the Signed Statement, and a typed reference mechanism that lets one
   record cite another by digest across profile boundaries.  This
   document defines that construction as a reusable profile — the
   Canonical Payload Binding — so that each payload class declares its
   canonicalization algorithm and exclusion set once, obtains an
   interoperable derived identifier, and inherits statement-to-receipt
   binding and typed digest reference semantics without restating the
   mechanics in every profile.  IANA registries govern both the
   canonicalization algorithms and the artifact types that may appear in
   typed references; entries are immutable.
- **draft-fassbender-scitt-time-anchor-03** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-gould-regext-epp-status-set-02** (new-draft, score 9, core_identity) [none]: [Status Set Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-gould-regext-epp-status-set/) — This document describes an Extensible Provisioning Protocol (EPP)
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
- **draft-ietf-acme-authority-token-jwtclaimcon-04** (new-draft, score 9, core_identity) [acme]: [JWTClaimConstraints profile of ACME Authority Token](https://datatracker.ietf.org/doc/draft-ietf-acme-authority-token-jwtclaimcon/) — This document defines an authority token profile for the validation
   of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate
   extensions within the Automated Certificate Management Environment
   (ACME) protocol.  This profile is based on the Authority Token
   framework and establishes the specific ACME identifier type,
   challenge mechanism, and token format necessary to authorize a client
   to request a certificate containing these constraints.
- **draft-ietf-cose-cmac-01** (new-draft, score 9, core_identity) [cose]: [AES-CMAC for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-cmac/) — The CBOR Object Signing and Encryption (COSE) specification defines
   structures for generating, conveying, and verifying Message
   Authentication Code (MAC) tags.  This document registers code points
   for using the Advanced Encryption Standard (AES) block cipher in
   Cipher-based Message Authentication Code (CMAC) mode within those
   COSE structures.  Specifically, these uses are for computing MAC tag
   values with no additional parameters.
- **draft-ietf-cose-sphincs-plus-10** (new-draft, score 9, verifiable_claims) [cose]: [SLH-DSA for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/) — Digital signatures are used within JSON Object Signing and Encryption
   (JOSE) and CBOR Object Signing and Encryption (COSE) to protect the
   integrity and authenticity of messages, such as JSON Web Signatures
   and signed COSE structures.  This document specifies JOSE and COSE
   serializations for the Stateless Hash-Based Digital Signature
   Standard (SLH-DSA), a Post-Quantum Cryptography (PQC) digital
   signature scheme defined in US NIST FIPS 205.  The conventions for
   the associated algorithm identifiers, signatures, public keys, and
   private keys are also specified.
- **draft-ietf-sidrops-aspa-profile-29** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.
- **draft-norton-sdlp-lineage-01** (new-draft, score 9, core_identity) [none]: [SDLP RFC 3: Lineage Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-lineage/) — This document defines the SDLP lineage model, which provides the
   canonical method for representing the ancestry of SDLP-governed
   objects. Lineage is a structural property that records how an object
   evolves through duplication and transformation events. The lineage
   model ensures that descendant objects remain uniquely identifiable
   and traceable across all lifecycle transitions.

   This revision (lineage-01) updates and replaces draft-norton-sdlp-
   lineage-00. It aligns the lineage grammar with Identity-02,
   Lifecycle-02, and Object-Format-01, clarifies deterministic ancestry
   extension rules, incorporates BitDrop conditions for invalid lineage
   transitions, and defines normative validation requirements for
   relying parties. This specification provides the authoritative
   lineage model required for interoperable identity, lifecycle, and
   provenance processing across SDLP implementations.
- **draft-chueayen-attestation-receipts-01** (new-draft, score 8, trust_infrastructure) [none]: [Enforcement Attestation Receipts for AI Inference Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies a compact JSON attestation receipt for an AI
   inference decision.  A receipt binds an outcome to a request hash
   under a published Ed25519 public key, so a party that does not trust
   the issuer's infrastructure can still verify offline what was
   decided.  The format is intentionally small and version-selected, so
   independent verifiers stay easy to implement and audit.  It is
   intended for settings where an operator-controlled log is not, on its
   own, sufficient evidence of the decision.
- **draft-reilly-multilarity-00** (new-draft, score 8, trust_infrastructure) [none]: [The Multilarity: Plural Intelligence Growth Without Convergence](https://datatracker.ietf.org/doc/draft-reilly-multilarity/) — Popular and technical discourse anticipates a technological
   Singularity: a point at which a single self-improving intelligence
   recursively surpasses all others, after which the trajectory of the
   system is determined by that one lineage.  This document describes a
   different inflection, termed the Multilarity: a condition in which
   the aggregate rate of intelligence growth becomes superhuman while
   the locus of intelligence remains irreducibly plural.  No single
   agent, model, operator, or lineage holds the frontier; capability
   accrues in the couplings between many participants, including
   humans.

   The Multilarity is presented here not as a forecast but as a design
   target.  A plural outcome is not the default result of many actors
   existing at once; apparent plurality collapses quietly into a
   concealed singleton unless specific substrate properties are
   maintained and verified.  This document defines the Multilarity,
   distinguishes it from singleton and multipolar framings, specifies
   five Multilarity Conditions (MC-1 through MC-5), defines measurable
   indicators including the Capability Concentration Ratio (CCR) and
   the Multilarity Index (MI), specifies the Multilarity Attestation
   Record (MAR) as an interoperable evidence format, and enumerates
   the convergence pathologies by which plurality is lost.
- **draft-schrock-action-remedy-receipts-00** (new-draft, score 8, core_identity) [none]: [Action Remedy Receipts for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-remedy-receipts/) — Revocation cannot undo an effect that already occurred.  A dispute
   does not authorize a refund, return, reversal, or other remedy.  This
   document defines Action Remedy Receipts for recording a bounded
   dispute decision and a fresh compensating action without rewriting
   the original action or effect.  Every remedy has its own operation
   identifier, CAID, action digest, authority, consequence owner, and
   execution result.  Indeterminate outcomes remain fenced until
   authenticated reconciliation.
- **draft-acosta-crypto-agility-manifest-00** (new-draft, score 7, trust_infrastructure) [none]: [A Well-Known URI and JSON Format for Publishing Cryptographic Posture (the Crypto-Agility Manifest)](https://datatracker.ietf.org/doc/draft-acosta-crypto-agility-manifest/) — This document defines a discoverable, machine-readable JSON document,
   the crypto-agility manifest, that a website or source repository
   publishes at the well-known URI "/.well-known/crypto-agility.json" to
   declare its cryptographic posture: a readiness summary, a compact
   Cryptography Bill of Materials (CBOM) summary, an optional link to a
   posture attestation, and the migration policy it measures itself
   against.  The manifest lets an automated consumer, such as an AI
   coding agent, a continuous-integration bot, or an auditor's tool,
   discover a project's crypto posture the way it already discovers a
   security contact from "security.txt".  The manifest is a public,
   self-reported claim; it is not a proof.  It is intended to
   complement, not replace, a full CBOM inventory, serving as the CBOM's
   public-facing discovery counterpart.

   This document is a proposal.  It is not an IETF product and is not a
   standard of any kind.
- **draft-msebenzi-evidence-action-00** (new-draft, score 7, agent_identity) [none]: [The evidence.* Family: Post-Hoc, Independently Recomputable Evidence Records for AI Agent Actions](https://datatracker.ietf.org/doc/draft-msebenzi-evidence-action/) — Autonomous agents act through tool invocations whose consequences
   outlive the sessions that produce them.  Pre-action constraint
   families gate whether an agent may act: environment.* attests boolean
   world-state, and verification.* attests calibrated confidence over
   factual claims.  No sibling family records, under equivalent
   verification discipline, what the agent then did.  This document
   defines the evidence.* family: append-only, hash-chained, signature-
   bound evidence records of agent actions, designed so that a third
   party can recompute every verdict from signed primitives and a
   published key, without trusting the operator's runtime.  It defines
   the family's membership criterion (independent recomputability with
   fail-closed verification), the family-wide record vocabulary and
   canonicalization discipline, a tri-state verification protocol
   (VALID, INVALID, UNVERIFIABLE), composition with the pre-action
   sibling families, and the conformance-vector discipline under which
   independent implementations demonstrate byte-level agreement.  One
   reference record type, evidence.action, is specified together with
   its frozen conformance corpus.  This document deliberately states
   what an evidence record does not prove.

## Monitor

- **draft-farrel-dawn-terminology-04** (new-draft, score 6, agent_identity) [none]: [Terminology for the Discovery of Agents, Workloads, and Named Entities (DAWN)](https://datatracker.ietf.org/doc/draft-farrel-dawn-terminology/) — The proliferation of distributed systems, Artificial Intelligence
   (AI) agents, cloud workloads, and network services has created a need
   for interoperable mechanisms to discover entities.  Entities may
   include AI agents, software services, compute workloads, and other
   named resources that need to be found and characterised before
   interaction can begin.

   This document defines terminology for Discovery of Agents, Workloads,
   and Named Entities (DAWN).  The intention is that this common set of
   terms can be used by other documents related to DAWN and so achieve
   consistency of meaning across the space.
- **draft-ietf-lamps-rfc8551bis-00** (new-draft, score 6, core_identity) [lamps]: [Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Message Specification](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc8551bis/) — This document defines Secure/Multipurpose Internet Mail Extensions
   (S/MIME) version 4.0.  S/MIME provides a consistent way to send and
   receive secure MIME data.  Digital signatures provide authentication,
   message integrity, and non-repudiation with proof of origin.
   Encryption provides data confidentiality.  Compression can be used to
   reduce data size.  This document obsoletes RFC 5751.
- **draft-ietf-lisp-ecdsa-auth-17** (new-draft, score 6, core_identity) [lisp]: [LISP Control-Plane ECDSA Authentication and Authorization](https://datatracker.ietf.org/doc/draft-ietf-lisp-ecdsa-auth/) — This draft describes how LISP control-plane messages can be
   individually authenticated and authorized without a a priori shared-
   key configuration.  Public-key cryptography is used with no new PKI
   infrastructure required.
- **draft-liang-tcp-provenance-option-02** (new-draft, score 6, core_identity) [none]: [TCP Provenance Identifier Option](https://datatracker.ietf.org/doc/draft-liang-tcp-provenance-option/) — This document describes a TCP option that carries a Provenance
   Identifier (ProvID) to enable correlation of TCP connections when
   transport-layer identifiers change along the path.
- **draft-lohmann-qikvrt-effect-ack-02** (new-draft, score 6, authorization) [none]: [QIK-VRT Effect Acknowledgement: Separating Receipt from Authorization for Downstream Effect](https://datatracker.ietf.org/doc/draft-lohmann-qikvrt-effect-ack/) — Transport acknowledgements establish technical receipt; they do not
   establish that a received information unit is understood, policy-
   compliant, or authorized to produce a downstream effect.  This
   document defines an Experimental application-layer control record,
   called EFFECT_ACK, that separates receipt from effect authorization.

   The protocol has five closed version-1 outcomes.  Ordinary downstream
   release is permitted only for EFFECT_ACK_DONE and only after
   validation of the record, its policy and evidence bindings, its
   freshness, and its authenticated origin.  This document specifies the
   state-selection algorithm, version handling, a deterministic JSON
   representation, hash chaining, timeout behavior, conformance
   requirements, and security and privacy boundaries.

   This protocol does not modify TCP, QUIC, or the OSI model; does not
   solve the halting problem; and does not establish the truth of
   external evidence.  It provides a machine-checkable authorization
   boundary under explicitly stated deployment assumptions.
- **draft-moskowitz-ads-b-auth-01** (new-draft, score 6, core_identity) [none]: [ADS-B Authentication](https://datatracker.ietf.org/doc/draft-moskowitz-ads-b-auth/) — The Automatic Dependent Surveillance – Broadcast (ADS-B) is a
   surveillance technology mandated in many airspaces.  It is now widely
   deployed but suffers a lack of security and privacy.  From a security
   point of view, it is relatively easy to spoof the ADS-B messages.
   With the appropriate readily available hardware and software.  From a
   privacy point of view, all the messages contain the aircraft’s
   assigned 24-bit ICAO address, which makes it easy to link to data
   about the aircraft, in particular to know when a particular aircraft
   has flown and where to.  In addition, the main transmission medium
   utilized for ADS-B, i.e. the 1090 MHz frequency used by Extended
   Squitter (1090ES), is approaching saturation in some parts of the
   world with ADS-B and other protocol messages, resulting in packet
   loss in certain areas [RF_Usage].

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
   conduct that flight and 2) a methodology for adequately protecting
   the privacy by assigning rotating 24-bit identifiers to designated
   aircraft, while maintaining the possibility to (blindly) authenticate
   their ADS-B transmissions.
- **draft-norton-sdlp-identity-02** (new-draft, score 6, core_identity) [none]: [SDLP RFC 1: DigitalID Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-identity/) — This document defines the DigitalID specification for the Secured
   Digital Lifecycle Protocol (SDLP). The DigitalID is the foundational
   identity construct for all SDLP-governed objects, providing
   deterministic uniqueness, lineage preservation, collision
   elimination, and stable identity bindings across all compliant
   implementations. This document updates and formalizes the DigitalID
   structure, canonical encoding rules, lineage grammar, identity
   assignment requirements, collision model, and validation rules
   originally introduced in draft-norton-sdlp-identity-00.
- **draft-norton-sdlp-lifecycle-02** (new-draft, score 6, core_identity) [none]: [SDLP RFC 2: Lifecycle Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-lifecycle/) — This document defines the lifecycle model for the Secured Digital
   Lifecycle Protocol (SDLP). The lifecycle model specifies the
   canonical state machine used by all SDLP-governed objects, including
   the rules for state transitions, transformation events, duplication
   events, and materialization events. The lifecycle model provides a
   stable and predictable framework for describing how SDLP objects
   evolve over time while preserving identity, lineage, and security
   guarantees defined in companion SDLP specifications. This document
   updates and formalizes the lifecycle semantics originally introduced
   in draft-norton-sdlp-lifecycle-00.
- **draft-richer-oauth-httpsig-03** (new-draft, score 6, authorization) [none]: [OAuth Proof of Possession Tokens with HTTP Message Signatures](https://datatracker.ietf.org/doc/draft-richer-oauth-httpsig/) — This extension to the OAuth 2.0 authorization framework defines a
   method for using HTTP Message Signatures to bind access tokens to
   keys held by OAuth 2.0 clients.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Web Authorization
   Protocol Working Group mailing list (oauth@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/oauth/.

   Source for this draft and an issue tracker can be found at
   https://github.com/jricher/draft-richer-oauth-httpsig.
- **draft-schrock-ep-outcome-binding-00** (new-draft, score 6, core_identity) [none]: [Outcome Binding for Authorized Actions and Independently Observed Effects](https://datatracker.ietf.org/doc/draft-schrock-ep-outcome-binding/) — Authorization proves what action was permitted; it does not prove
   what happened after execution.  An executor-signed result improves
   attribution but remains a claim by the party that acted.  This
   document specifies a source-routed Outcome Binding profile.  Signed
   predicted effects identify the source role and source class required
   to evaluate each predicate.  Executors, systems of record, and
   independent observers sign closed observation objects bound to the
   same authorization, action digest, Canonical Action Identifier,
   consumption nonce, operation, facility, and observation window.  A
   deterministic verifier separates evidence availability from
   comparison: missing or unauthenticated required sources yield an
   indeterminate lifecycle state; authentic observations yield the
   closed comparison result in_bounds, divergent, or incomparable.  The
   profile improves consequence reconciliation without claiming physical
   truth, sensor correctness, or legal finality.
- **draft-schrock-model-to-matter-02** (new-draft, score 6, authorization) [none]: [Model-to-Matter: Authorization and Outcome Evidence for Model-Directed Physical Execution](https://datatracker.ietf.org/doc/draft-schrock-model-to-matter/) — Advanced models can propose operations that produce physical effects.
   Model-to-Matter defines an executor-owned profile that composes
   model, safety, institutional, domain, screening, and human evidence
   over one canonical action before single-use execution.  This revision
   also profiles post-execution Outcome Binding.  An executor effect
   statement remains one source claim; required independent observers
   sign separately bound observations.  Missing outcome evidence is
   indeterminate, not success or failure.  The profile standardizes
   evidence custody and reconciliation; it does not perform screening,
   determine scientific safety, certify a facility, or establish
   physical truth.
- **draft-zerobankx-srl-core-03** (new-draft, score 6, core_identity) [none]: [Secure Resource Layer (SRL) Core](https://datatracker.ietf.org/doc/draft-zerobankx-srl-core/) — This document defines the Secure Resource Layer (SRL), a global trust
   layer that evaluates digital resources before they are accessed.

   SRL introduces governance, verification, and revocation mechanisms
   that complement existing URL, QR code, barcode, RFID, and short URL
   systems.

   SRL is designed to be deployable incrementally through resolver-based,
   scanner-level, reader-level, and application-level integrations,
   without requiring changes to existing Internet standards, browsers,
   operating systems, or identifier formats.

   This revision extends the document with implementation testing and
   operational validation of hybrid resource identifiers in logistics
   and supply-chain environments. The testing combines QR codes,
   barcodes, and RFID-derived identifiers under a common SRL trust
   framework while preserving compatibility with existing operational
   systems.
- **draft-carpenter-anima-grasp-rendezvous-01** (new-draft, score 5, core_identity) [none]: [Using GRASP as an Agent Rendezvous Mechanism](https://datatracker.ietf.org/doc/draft-carpenter-anima-grasp-rendezvous/) — This document describes how the GeneRic Autonomic Signaling Protocol
   (GRASP) defined by RFC 8990 may be used as a rendezvous mechanism for
   one Autonomic Service Agent to find another, and then to establish a
   generic communication channel between them.  Such a channel could be
   used for any form of agent-to-agent communication, not limited to
   GRASP exchanges.  This document updates RFC 8990 by adding a
   transport identifier registry.
- **draft-dimare-pay-uri-00** (new-draft, score 5, core_identity) [none]: [The 'pay' URI Scheme for Rail-Neutral Payment Aliases](https://datatracker.ietf.org/doc/draft-dimare-pay-uri/) — This document defines the "pay" Uniform Resource Identifier (URI)
   scheme, a rail-neutral, human- and agent-friendly name for a payment
   payee that resolves, through a resolution protocol, to one or more
   concrete payment endpoints.  Unlike a URI that names a specific
   account on a specific payment method, a "pay" URI names a payee
   independently of any settlement rail; a resolver deterministically
   maps the name to the rail(s), endpoint(s), and metadata a payer needs
   to construct a payment.  This document specifies the scheme syntax
   and semantics, the resolution mechanism and its discovery, the
   deterministic resolution property, and requests provisional
   registration of the scheme with IANA per RFC 7595.  It does not
   define a settlement protocol and takes no custody of funds; it
   composes with agent-payment protocols such as x402 for the actual
   money movement.
- **draft-pant-ai-mib-00** (new-draft, score 5, core_identity) [none]: [AI-MIB: A Management Information Base Extension for Artificial Intelligence Infrastructure in Telecommunications Networks](https://datatracker.ietf.org/doc/draft-pant-ai-mib/) — The rapid proliferation of Artificial Intelligence (AI) and Graphics
   Processing Unit (GPU) infrastructure within telecommunications
   networks has exposed a fundamental gap in existing network management
   frameworks.  The Simple Network Management Protocol (SNMP), the de
   facto standard for network element monitoring since RFC 1157 (1990),
   provides no native support for monitoring AI accelerators, GPU
   clusters, high-bandwidth interconnects such as NVLink and InfiniBand,
   or AI workload telemetry.  This document proposes AI-MIB: a
   Management Information Base extension that defines a standardised
   Object Identifier (OID) tree for AI infrastructure management within
   the SNMP framework.  AI-MIB is designed to operate alongside existing
   Operations Support Systems and Business Support Systems (OSS/BSS) in
   telecommunications environments, preserving backward compatibility
   with SNMPv3 while extending the framework's scope to cover GPU
   health, accelerator interconnect metrics, AI workload performance
   indicators, and energy consumption.  This document also outlines two
   future extensions: a subscription-based streaming capability for
   SNMPv3 (informally designated SNMPv3+), and a schema-mapping
   specification for a SNMP-gNMI Translation Gateway that bridges SNMP/
   MIB and gNMI/YANG data models.
- **draft-schrock-agent-qualification-statements-00** (new-draft, score 5, authorization) [none]: [Portable Agent Qualification Statements for Consequential Actions](https://datatracker.ietf.org/doc/draft-schrock-agent-qualification-statements/) — Agent evaluations report what happened in a test environment.  They
   do not, by themselves, establish that a measured candidate satisfies
   a relying party's policy, remains current, matches the runtime
   candidate, or is authorized to perform a consequential action.  This
   document defines a portable Qualification Statement that binds a
   candidate, complete evaluation campaign, qualification policy,
   assignment, and status.  It preserves three separate claims:
   observation, qualification, and authorization.  A relying party can
   accept a current qualification as evidence at runtime, but MUST make
   a separate exact-action authorization and admission decision.
- **draft-schrock-ep-authority-introduction-02** (new-draft, score 5, adjacent_watchlist) [none]: [Authority Documents and Scoped Authority for Agent-Action Evidence](https://datatracker.ietf.org/doc/draft-schrock-ep-authority-introduction/) — Signature verification answers whether a key produced an artifact.
   It does not answer why a relying party accepts that key, or whether
   the key holder had authority for the action.  This document specifies
   two composable artifacts.  An Authority Document introduces and
   rotates an organization's evidence-issuing keys through a signed,
   hash-chained sequence.  A Scoped Authority Proof records the
   authority held by a subject at a registry snapshot, including role,
   action scope, material limits, policy binding, validity, and
   revocation status.  A relying party evaluates both artifacts under
   its own pinned trust inputs and policy.  The design does not make a
   self-presented key authoritative, does not turn log inclusion or
   domain control into automatic trust, and does not equate a valid
   signature with permission to act.
- **draft-gebauer-iacp-03** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol](https://datatracker.ietf.org/doc/draft-gebauer-iacp/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-a2acom-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - A2ACOM](https://datatracker.ietf.org/doc/draft-gebauer-iacp-a2acom/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-dhi-erp-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - DHI - ERP](https://datatracker.ietf.org/doc/draft-gebauer-iacp-dhi-erp/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-dht-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - DHT](https://datatracker.ietf.org/doc/draft-gebauer-iacp-dht/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-economy-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - ECONOMY](https://datatracker.ietf.org/doc/draft-gebauer-iacp-economy/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-eid-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - EID](https://datatracker.ietf.org/doc/draft-gebauer-iacp-eid/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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
- **draft-gebauer-iacp-interop-00** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol - INTEROP](https://datatracker.ietf.org/doc/draft-gebauer-iacp-interop/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
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

## Adjacent / watchlist

- **draft-besleaga-sustainability-wellknown-05** (new-draft, score 3, adjacent_watchlist) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI.  This
   URI provides a uniform, out-of-band convention for web servers and
   digital services to publish aggregated environmental impact, energy
   consumption, and carbon footprint metrics for a declared reporting
   subject -- typically the publishing origin itself.

   By utilizing an asynchronous reporting model, this approach allows
   for transparent environmental accounting without the bandwidth and
   energy overhead associated with per-request HTTP headers.
- **draft-cassen-vrrp-auth-hmac-01** (new-draft, score 3, core_identity) [none]: [An HMAC Authentication Extension for the Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-cassen-vrrp-auth-hmac/) — VRRP relies on a hop limit of 255 to prove that an advertisement came
   from the local link.  That guard cannot apply when advertisements
   travel as multi-hop unicast across a routed or overlay network, as is
   common in cloud deployments, leaving the protocol open to off-segment
   injection and replay.  The legacy VRRPv2 authentication types do not
   close this gap and were removed from later VRRP specifications.  This
   document defines an authentication extension that appends an HMAC-
   SHA256 trailer and a time-based sequence number to VRRPv3
   advertisements, authenticating the sender as a holder of the group
   key, protecting message integrity and bounding replay, for both IP
   address families.  The extension is the primary defense where the
   hop-limit check cannot apply, and defense in depth for multicast and
   single-hop unicast, where that check remains in force.
- **draft-fomicheva-aether-00** (new-draft, score 3, core_identity) [none]: [Aether: A Next-Generation L4 Transport](https://datatracker.ietf.org/doc/draft-fomicheva-aether/) — This document specifies Aether, a transport-layer protocol (L4)
   designed for modern network environments requiring multiplexed
   streams without head-of-line blocking, mandatory encryption with
   post-quantum resistance, multi-path routing, and self-sovereign
   identity at the protocol layer.  Aether operates entirely in
   userspace without kernel modifications.
- **draft-guo-krb-spake-2fa-02** (new-draft, score 3, core_identity) [none]: [Kerberos SPAKE with Two-Factor Authentication](https://datatracker.ietf.org/doc/draft-guo-krb-spake-2fa/) — This document defines a new two-factor authentication mechanism for
   the Kerberos SPAKE pre-authentication.  The mechanism uses the time-
   based one-time password (TOTP) as a second factor, and combines it
   with the password factor in a more secure way, which can prevent
   attackers from both impersonating Kerberos clients and obtaining
   TGTs' session keys in case of any factor leakage.
- **draft-helmprotocol-tttps-08** (new-draft, score 3, core_identity) [none]: [The TLS TimeToken Secure Protocol (tttps)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies a Proof-of-Time record: a transport-
   independent object in which an issuer asserts that a payload with a
   stated digest was presented to it at a stated time, relative to a
   stated set of time sources and with an explicit error bound, and
   which cannot afterwards be altered without detection.  The record is
   produced by an issuer that is not a party to the session in which the
   record is later presented, and it can be evaluated by a third party
   who observed neither endpoint and who evaluates it after that session
   has closed.  Evaluation additionally requires the issuer's public key
   and the context identifier, both obtained out of band: the record is
   self-contained with respect to the transport that carries it, not
   with respect to those inputs.  This document defines the record
   format, an extensible integrity algorithm registry whose mandatory-
   to-implement member is unkeyed SHA-256, a binding of a record to a
   TLS 1.3, QUIC, or HTTP/3 session and to the party entitled to present
   it, and the associated IANA registrations.
- **draft-ietf-calext-jscalendarbis-18** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-detnet-multi-domain-framework-02** (new-draft, score 3, adjacent_watchlist) [detnet]: [A Control Plane Framework for Multi-Domain Deterministic Networking (DetNet)](https://datatracker.ietf.org/doc/draft-ietf-detnet-multi-domain-framework/) — Deterministic Networking (DetNet) provides the capability to carry
   specified unicast or multicast data flows for real-time applications
   with extremely low data loss rates and bounded latency over a path or
   network.  As DetNet deployments expand, they will inevitably need to
   span multiple domains that may be under separate technological
   control.  This creates a need for a control plane solution that can
   establish and maintain end-to-end DetNet services across these domain
   boundaries.

   This document defines a generic framework for a multi-domain DetNet
   control plane.  It first establishes a working definition of a
   "DetNet Domain" for the purpose of path computation and control.  It
   then describes two high-level architectural approaches for inter-
   domain path computation and resource reservation: a Hierarchical
   model and a peer-to-peer "stitching" model.  While a Path Computation
   Element (PCE)-based realization is used as an illustrative example,
   the framework is designed to be applicable to any controller-plane
   technology that satisfies the stated functional requirements.  This
   framework provides the foundation for more specific work on multi-
   domain DetNet solutions.
- **draft-ietf-ediint-rfc4130bis-02** (new-draft, score 3, core_identity) [ediint]: [AS2 Specification Modernization](https://datatracker.ietf.org/doc/draft-ietf-ediint-rfc4130bis/) — This document provides an applicability statement (RFC 2026,
   Section 3.2) describing how to securely exchange structured business
   data over HTTP.  Structured business data may be XML; Electronic Data
   Interchange (EDI) in either the American National Standards Committee
   (ANSI) X12 format or the UN Electronic Data Interchange for
   Administration, Commerce, and Transport (UN/EDIFACT) format; or other
   structured data formats.  The data is packaged using standard MIME
   structures.  Authentication and data confidentiality are obtained by
   using Cryptographic Message Syntax with S/MIME security body parts
   (see Section 10.1).  Authenticated acknowledgements make use of
   multipart/signed Message Disposition Notification (MDN) responses to
   the original HTTP message.  This applicability statement is
   informally referred to as "AS2" because it is the second
   applicability statement, produced after "AS1" (RFC 3335).  This
   document obsoletes RFC 4130 and stands on its own without reference
   to AS1 or SMTP, except where required for IANA registry updates.

   This document also updates IANA registries originally created by RFC
   3335 and RFC 4130.
- **draft-ietf-ippm-alt-mark-yang-05** (new-draft, score 3, adjacent_watchlist) [ippm]: [A YANG Data Model for the Alternate Marking Method](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-yang/) — Alternate-Marking Method is a technique used to perform packet loss,
   delay, and jitter measurements on in-flight packets.  This document
   defines a YANG data model for the Alternate Marking Method.
- **draft-ietf-ippm-on-path-telemetry-yang-05** (new-draft, score 3, adjacent_watchlist) [ippm]: [On-Path Telemetry YANG Data Model](https://datatracker.ietf.org/doc/draft-ietf-ippm-on-path-telemetry-yang/) — This document proposes a YANG data model for monitoring On-Path
   network performance information to be published in YANG
   notifications.  The Alternate-Marking Method and In-situ Operations,
   Administration, and Maintenance (IOAM) are the On-Path hybrid
   measurement methods considered in this document.
- **draft-ietf-kitten-password-storage-12** (new-draft, score 3, adjacent_watchlist) [kitten]: [Best practices for SASL password hashing and storage](https://datatracker.ietf.org/doc/draft-ietf-kitten-password-storage/) — This document outlines best practices for handling user passwords and
   other secrets in client-server systems making use of SASL.
- **draft-ietf-netconf-udp-notif-26** (new-draft, score 3, adjacent_watchlist) [netconf]: [UDP-based Transport for Configured Subscriptions](https://datatracker.ietf.org/doc/draft-ietf-netconf-udp-notif/) — This document describes a UDP-based transport for YANG notifications
   to collect data from network nodes within a controlled environment.
   A shim header is defined to facilitate the data streaming directly
   from a publishing process on a network device to telemetry receivers.
   Such a design enables higher frequency updates and less performance
   overhead on publisher and receiver processes compared to already
   established notification mechanisms.  A YANG data model is also
   defined for management of the described UDP-based transport.
- **draft-ietf-nmop-network-incident-yang-13** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG Module for the network incident
   lifecycle management.  This YANG module is meant to provide a
   standard way to report, diagnose, and help reduce troubleshooting
   tickets and resolve network incidents for the sake of network service
   health and probable cause analysis.
- **draft-ietf-opsawg-discardmodel-16** (new-draft, score 3, adjacent_watchlist) [opsawg]: [Information and Data Models for Packet Discard Reporting](https://datatracker.ietf.org/doc/draft-ietf-opsawg-discardmodel/) — This document defines an Information Model and specifies a
   corresponding YANG data model for packet discard reporting.  The
   Information Model provides an implementation-independent framework
   for classifying packet loss by its cause (e.g., errors, congestion,
   or policy).  This classification enables operators to determine which
   losses are expected or intended and which are unintended, and to
   select appropriate mitigation actions, including automated mitigation
   of unintended packet loss.  The YANG data model specifies an
   implementation of this Information Model for network elements with a
   focus on interface, device, and control-plane discards.
- **draft-ietf-schc-compress-payload-00** (new-draft, score 3, core_identity) [schc]: [SCHC Payload Compression for Structured Formats](https://datatracker.ietf.org/doc/draft-ietf-schc-compress-payload/) — This document describes techniques to adapt the SCHC framework
   (RFC8724), used for header compression, to also compress and
   decompress payload of specific protocols.  To this end, this document
   defines a new matching operator, equal-template, to check equality of
   field values with respect to a user-defined template, and a payload
   keyword to be used as Field IDentifier (FID) to signal the presence
   of payload to be compressed or decompressed.  Additionally, this
   document defines a set of template functions and variables to
   optimize user-defined templates, which can be extended through the
   IANA registry defined herein.
- **draft-ietf-teas-network-slice-topology-yang-04** (new-draft, score 3, adjacent_watchlist) [teas]: [IETF Network Slice Topology YANG Data Model](https://datatracker.ietf.org/doc/draft-ietf-teas-network-slice-topology-yang/) — An RFC 9543 network slice customer may utilize intent-based
   topologies to express resource reservation intentions within the
   provider's network.  These customer-defined intent topologies allow
   customers to request shared resources for future connections that can
   be flexibly allocated and customized.  Additionally, they provide an
   extensive level of control over underlay service paths within the
   network slice.

   This document describes a YANG data model for expressing customer
   intent topologies which can be used to enhance the RFC 9543 Network
   Slice Services in specific use cases, such as Network wholesale
   scenarios, where both topology and connectivity intents need to be
   expressed.
- **draft-intra-handshake-fail-01** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697, which
   is substantial technical evidence of how *intra*-handshake
   attestation fails in practice.  Moreover, since continuous
   attestation is required, *intra*-handshake attestation adds
   *unnecessary complexity*. The results are backed by the research
   [Intra-handshake.fail] and the ProVerif artifacts
   [Intra-handshake.fail-repo] under Apache-2.0 license for
   reproducibility.
- **draft-jurkovikj-collab-tunnel-03** (new-draft, score 3, authorization) [none]: [The Collaboration Content Transfer (TCT) Protocol](https://datatracker.ietf.org/doc/draft-jurkovikj-collab-tunnel/) — This document specifies the Collaboration Content Transfer (TCT)
   Protocol, an experimental HTTP profile for efficient delivery of
   publisher-selected web content to automated clients.  TCT defines a
   deterministic JSON representation at a machine-facing URL,
   bidirectional discovery between human-facing and machine-facing
   resources, JSON sitemaps containing representation-validator hints,
   and conditional request behavior using ordinary strong ETags.

   TCT preserves standard HTTP validator scope: an M-URL ETag identifies
   the exact selected M-URL representation.  Optional Semantic
   Validators can correlate the logical state of human-facing and
   machine-facing representations, but are not required by TCT and do
   not replace ordinary cache validators.  TCT does not define
   authorization, licensing, content-use policy, or mutation semantics.
- **draft-jurkovikj-httpapi-agentic-state-02** (new-draft, score 3, agent_identity) [none]: [HTTP Profile for Conditional Updates to Shared Resource State (Agentic State Transfer)](https://datatracker.ietf.org/doc/draft-jurkovikj-httpapi-agentic-state/) — HTTP applications frequently expose one logical object through
   several representations or resources.  Ordinary HTTP entity tags
   identify selected representations; they do not, by themselves,
   provide a conditional-update mechanism spanning different request
   targets.

   This document specifies Agentic State Transfer (AST), an HTTP profile
   for preventing lost updates to shared application state.  AST Core
   requires a client to mutate the State-Bearing Resource using the
   strong ETag of its State-Bearing Representation and the standard If-
   Match field.  AST Semantic uses Semantic-ETag and If-Semantic-Match
   when a protected mutation targets a different resource or
   representation in the same concurrency domain.  The profile also
   defines state discovery, atomic compare-and-commit behavior, conflict
   handling, deferred processing, caching constraints, and security
   requirements.
- **draft-le-carrier-identity-core-00** (new-draft, score 3, core_identity) [none]: [Carrier Identity Core: A Proof-Bearing Kernel for Content-Derived Node Identity and Structural Graphs](https://datatracker.ietf.org/doc/draft-le-carrier-identity-core/) — This document specifies Carrier Identity Core, a minimal, proof-
   bearing identity kernel for content-derived node identity, canonical
   references, and finite structural graphs.

   It defines a finite-sequence substrate, a self-contained frame and
   hash interface, staged formation of immutable lanes, node bodies and
   proof-bearing occurrences, Qualified Node Keys, canonical reference
   construction, exact structural theorem schemas, and structural graph
   validity.

   Informative derivations of the exact structural theorem schemas are
   provided in an informative appendix.

   This document does not define computational security experiments,
   evidence records, proof admission, resource evaluation, consensus,
   liveness, finality, governance, or operational protocol behavior.
- **draft-lecklider-ppf-00** (new-draft, score 3, authorization) [none]: [Pingback Permitted From (PPF)](https://datatracker.ietf.org/doc/draft-lecklider-ppf/) — Pingback Permitted From (PPF) defines a DNS-based mechanism for
   authorizing senders of linkback requests.  A domain owner publishes a
   TXT record declaring which hosts are permitted to send linkbacks for
   source URIs on that domain.  Receivers and linkback proxies can then
   reject unauthorized linkbacks before fetching the claimed source URI.

   PPF is intended for linkback protocols in which a sender claims that
   one web resource links to another and the receiver would otherwise
   fetch the claimed source resource to verify that claim.  PPF provides
   sender authorization; it does not replace content verification,
   moderation, or abuse filtering.
- **draft-liao-cose-c509-algorithms-00** (new-draft, score 3, verifiable_claims) [none]: [Additional Algorithms for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-cose-c509-algorithms/) — This document registers additional algorithms in the IANA registries
   defined by [I-D.ietf-cose-cbor-encoded-cert].  It extends the base
   C509 certificate specification with post-quantum cryptography (PQC)
   signature and key-encapsulation algorithms including ML-DSA, ML-KEM,
   stateful hash-based algorithms (HSS/LMS, XMSS, XMSS^MT), and
   composite algorithms.
- **draft-liu-moq-feedback-00** (new-draft, score 3, adjacent_watchlist) [none]: [MoQ Feedback](https://datatracker.ietf.org/doc/draft-liu-moq-feedback/) — This document defines an extension to Media over QUIC Transport
   (MOQT) that enables MoQ receivers to report delivery quality
   information for media Objects to senders.  The MoQ layer synthesizes
   MMF feedback and local congestion control (CC) output to compute
   control decisions such as bitrate, frame rate, and pacing, and inform
   the CC algorithm module via a cross-layer control interface.  This
   mechanism reuses the MOQT Track/Object data model without introducing
   new control message types.  While QUIC ACK and reception timestamp
   extensions continue to provide per-packet CC signals; this mechanism
   adds per-Object media semantic feedback when the MMF extension is
   negotiated and enabled.
- **draft-melnikov-imap-rememberme-01** (new-draft, score 3, core_identity) [none]: [IMAP REMEMBERME extension for quick reauthentication token generation](https://datatracker.ietf.org/doc/draft-melnikov-imap-rememberme/) — This document specifies an IMAP extension for generating quick
   reauthentication tokens that allow clients to re-login without user
   interaction, once authentication using a strong SASL mechanism is
   completed.
- **draft-melnikov-imap-sasl2-profile-00** (new-draft, score 3, core_identity) [none]: [IMAP SASL2 Profile](https://datatracker.ietf.org/doc/draft-melnikov-imap-sasl2-profile/) — This document specifies an IMAP extension for SASL2 authentication,
   which extends IMAP SASL (RFC 4422) Profile.
- **draft-melnikov-sasl2-03** (new-draft, score 3, core_identity) [none]: [Extensible Simple Authentication and Security Layer (SASL)](https://datatracker.ietf.org/doc/draft-melnikov-sasl2/) — The Simple Authentication and Security Layer (SASL) is a framework
   for providing authentication and data security services in
   connection-oriented protocols via replaceable mechanisms.  It
   provides a structured interface between protocols and mechanisms.
   The resulting framework allows new protocols to reuse existing
   mechanisms and allows old protocols to make use of new mechanisms.
   The framework also provides a protocol for securing subsequent
   protocol exchanges within a data security layer.

   This document describes how a SASL mechanism is structured, describes
   how protocols include support for SASL, and defines the protocol for
   carrying a data security layer over a connection.  This document also
   defines how servers can request fulfillment of extra authentication
   related tasks, such as two factor authentication and/or password
   change.
- **draft-norton-sdlp-obj-format-01** (new-draft, score 3, core_identity) [none]: [SDLP RFC 3: Object Format Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-obj-format/) — This document defines the canonical object format for the Secured
   Digital Lifecycle Protocol (SDLP). The object format specifies the
   normative byte-level representation used for hashing, signing,
   validation, and interoperability across SDLP implementations. All
   SDLP-governed objects MUST follow the canonical encoding, field
   ordering, and serialization grammar defined in this specification.
   This document updates and replaces draft-norton-sdlp-obj-format-00
   and resolves inconsistencies identified during interoperability
   analysis with Identity-02 and Lifecycle-02.
- **draft-pythia-bmwg-programmable-power-profiling-00** (new-draft, score 3, adjacent_watchlist) [none]: [Power Consumption Profiling for Programmable Network Devices](https://datatracker.ietf.org/doc/draft-pythia-bmwg-programmable-power-profiling/) — A programmable network device can execute different packet-processing
   programs on the same hardware.  Device-level power measurements show
   the total input power but do not explain the power associated with a
   program's parser, match-action tables, and stateful or stateless
   actions.  Models designed for fixed-function switches do not directly
   describe these program-dependent operations.

   This document describes a power profiling methodology for
   programmable network devices.  The methodology decomposes packet
   processing into functional components, uses controlled calibration
   programs to derive target-specific parameters, and estimates the
   power of a data-plane program from its processing features and
   traffic.  It also specifies validation and reporting requirements
   that distinguish direct measurements from model-derived estimates.
   The methodology is based on implementation experience with an ASIC
   programmable switch and an FPGA-based programmable switch.
- **draft-shubralov-demi-sro-payment-security-01** (new-draft, score 3, adjacent_watchlist) [none]: [Blockchain-Backed Risk Pooling and Self-Regulation Protocol for Alternative Payment Providers (DeMI)](https://datatracker.ietf.org/doc/draft-shubralov-demi-sro-payment-security/) — This document specifies a Best Current Practice (BCP) for risk
   management, automated self-regulation, and transaction settlement
   integrity among alternative payment service providers (APPs)
   operating in emerging markets without formal ISO/PCI-DSS coverage.
   It defines an architectural specification for a decentralized self-
   regulated organization (SRO) compensation pool deployed on the
   Ethereum Layer 1 blockchain.  The protocol mitigates time-delayed
   fraud vectors, liquidity mismatches, and cross-border settlement
   frictions through cryptographic batching, zero-trust geo-distributed
   validator networks over private MPLS/satellite topologies, and
   automated algorithmic underwriting.
- **draft-thallapelly-oasnt-caid-00** (new-draft, score 3, core_identity) [none]: [OASNT-CAID: Canonical Action Identifier Derivation and the Named-Human Binding](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt-caid/) — This document profiles OASNT tokens for consumption by executor-side
   processing models.  It fixes one normative derivation of a Canonical
   Action Identifier (CAID) from the OASNT action digest, so that every
   executor checks the same derivation rather than each integration
   defining its own, and it specifies the semantics of the token's
   named-human binding, including a subject-to-enrollment check whose
   absence this profile makes a refusal.
- **draft-dikshit-cats-oam-usecases-00** (new-draft, score 2, ignored_after_review) [none]: [Use Cases and Requirements for Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM)](https://datatracker.ietf.org/doc/draft-dikshit-cats-oam-usecases/) — [I-D.ietf-cats-oam-fw] defines a framework for Operations,
   Administration, and Maintenance (OAM) in Computing-Aware Traffic
   Steering (CATS) networks, introducing Instance OAM and Service OAM
   as new components alongside traditional Link and Path OAM, and
   specifying high-level requirements (O-REQ, A-REQ, M-REQ) for each.
   As with the base CATS work, where
   [I-D.ietf-cats-usecases-requirements] separately catalogued problem
   statement, use cases, and requirements alongside
   [I-D.ietf-cats-framework], the OAM framework similarly benefits
   from a companion document grounding its requirements in concrete
   operator scenarios.

   This document fills that gap.  It presents five use cases for CATS
   OAM -- multi-domain compute-node failure detection, SLA
   verification that closes the loop with metric-driven traffic-
   steering decisions, demarcation of network-path faults from
   compute-instance faults, OAM-triggered fallback steering, and
   multi-vendor Compute-Service Metric Agent (C-SMA) interoperability
   verification -- and maps each to the Link/Path/Instance/Service OAM
   layering and O-REQ/A-REQ/M-REQ requirement categories defined in
   [I-D.ietf-cats-oam-fw].
- **draft-fengfar-led-00** (new-draft, score 2, ignored_after_review) [none]: [Dealing with LLMs in IETF Discussions](https://datatracker.ietf.org/doc/draft-fengfar-led/) — The rapid adoption of AI language tools has prompted concern across
   professional and technical communities, including the IETF, about
   authenticity, accountability, and the integrity of human
   contribution.  This document approaches the question from two
   directions: a critical reader's concerns about what AI use means for
   IETF discussion, and a practitioner's account of how AI is currently
   being used in IETF discussions.  We aim to explore some of the issues
   arising, and perhaps make some specific (but tentative)
   recommendations, but the main recommendation is that the IETF should
   develop guidelines for use of AI tooling when engaging in IETF
   discussions.
- **draft-ietf-mailmaint-pacc-03** (new-draft, score 2, ignored_after_review) [mailmaint]: [Automatic Configuration of Email, Calendar, and Contact Server Settings](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pacc/) — This document specifies an automatic configuration mechanism for
   email, calendar, and contact user agent applications.  Service
   providers publish standardized configuration information that user
   agent applications retrieve and use to simplify server setup
   procedures.
- **draft-liu-agent-metadata-sync-protocol-01** (new-draft, score 2, ignored_after_review) [none]: [Agent Metadata Synchronization Protocol](https://datatracker.ietf.org/doc/draft-liu-agent-metadata-sync-protocol/) — The Internet of Agents (IoA) requires a robust infrastructure to
   manage the lifecycle, discovery, and interaction of autonomous agents
   across distributed network domains.  While the Agent Gateway (AGW)
   provides a localized control point, large-scale deployments
   necessitate a mechanism for multiple gateways to synchronize agent
   metadata and routing information.  This document specifies the Agent
   Metadata Synchronization Protocol (AMSP).  AMSP facilitates the
   exchange of Agent Records between hierarchical gateways (Level-1 and
   Level-2), ensuring global reachability, efficient resource
   utilization, and loop-free metadata propagation.
- **draft-templin-6man-mla-33** (new-draft, score 2, ignored_after_review) [none]: [IPv6 Addresses for Ad Hoc Networks](https://datatracker.ietf.org/doc/draft-templin-6man-mla/) — Ad Hoc networks present an IPv6 addressing challenge due to the
   undetermined neighborhood properties of their interfaces.  IPv6 nodes
   must assign locally-unique and topology-independent IPv6 addresses
   when topology-oriented IPv6 address delegation services are either
   absent or only intermittently available.  This document introduces a
   new IPv6 address type (termed the "Multilink Local Address (MLA)")
   that nodes can autonomously assign to interfaces to support Ad Hoc
   network operations.
- **draft-zhangb-cats-csma-implementation-00** (new-draft, score 2, ignored_after_review) [none]: [CATS Service Metric Agent (C-SMA) Functional Implementation](https://datatracker.ietf.org/doc/draft-zhangb-cats-csma-implementation/) — The Computing-Aware Traffic Steering (CATS) framework introduces the
   CATS Service Metric Agent (C-SMA) as the functional entity
   responsible for collecting service capabilities and status, and
   reporting them to CATS Path Selectors (C-PSes).  While existing
   drafts define the metrics and high-level framework, the concrete
   functional behavior, internal architecture, and operational
   procedures of the C-SMA remain underspecified.

   This document fills that gap by defining the functional
   implementation of the C-SMA.  Specifically, it specifies how the
   C-SMA collects metrics from multiple Service Contact Instances (SCIs)
   within a service site; how it validates, and caches these metrics;
   how it adapts to various control-plane protocols for metric
   distribution; how it enforces local policies and security policies;
   and how it maintains synchronization with the C-PS under dynamic
   conditions.  This document complements [I-D.ietf-cats-framework] and
   [I-D.zhangb-cats-service-metrics-op] by providing the operational
   execution layer for the C-SMA.
- **draft-zhangb-cats-sci-implementation-00** (new-draft, score 2, ignored_after_review) [none]: [CATS Service Contact Instance Functional Implementation](https://datatracker.ietf.org/doc/draft-zhangb-cats-sci-implementation/) — The Computing-Aware Traffic Steering (CATS) framework introduces the
   concept of a Service Contact Instance (SCI) as the client-facing
   entity responsible for receiving and dispatching service requests.
   While existing drafts define the framework and metrics, the concrete
   functional behavior of a Service Contact Instance remains
   underspecified.

   This document fills that gap by defining the functional
   implementation of a CATS Service Contact Instance.  Specifically, it
   specifies how an SCI collects, aggregates, and reports service
   instance metrics to the CATS Service Metric Agent (C-SMA); how it
   monitors the health and status of underlying service instances; how
   it dispatches client requests to the most appropriate service
   instance based on local policy and real-time conditions; and how it
   maintains affinity and handles failure scenarios.  This document
   complements [I-D.ietf-cats-framework] and
   [I-D.zhangb-cats-service-metrics-op] by providing the operational
   execution layer for the SCI.

## Ignored after review

- **draft-altanai-moq-relay-geocode-01** (new-draft, score 0, ignored_after_review) [none]: [Geographic Location for Media over QUIC Relays](https://datatracker.ietf.org/doc/draft-altanai-moq-relay-geocode/) — This document defines a mechanism for Media over QUIC (MoQ) relays to
   advertise their geographic location (geocode) and related path
   metrics.  Some clients require their media data to remain locally or
   geo-fenced within specific jurisdictions for privacy and security
   compliance (e.g., GDPR, HIPAA, or sector-specific regulations).  This
   mechanism enables service providers to track the geographic path of
   media packets through the relay mesh and to enforce geo-fencing
   policies.  It supports Geo-Distributed Orchestration and Routing
   (GDOR), data residency compliance, latency optimization, and relay
   selection.  The specification includes optional IATA airport codes as
   human-readable geographic identifiers for major relay locations.
- **draft-amalj-sustain-shape-03** (new-draft, score 0, ignored_after_review) [none]: [Sustainability holistic API for Path Energy Evaluation (SHAPE)](https://datatracker.ietf.org/doc/draft-amalj-sustain-shape/) — This document describes an API to query a network regarding its
   Energy Traffic Ratio and other sustainability-related metrics for a
   given network path.
- **draft-belchior-satp-gateway-recovery-06** (new-draft, score 0, ignored_after_review) [none]: [Secure Asset Transfer Protocol (SATP) Gateway Crash Recovery Mechanism](https://datatracker.ietf.org/doc/draft-belchior-satp-gateway-recovery/) — This memo describes the crash recovery mechanism for the Secure Asset
   Transfer Protocol (SATP).  The goal of this draft is to specify the
   message flow that implements a crash recovery mechanism, composed of
   self-healing and rollback sub-protocols.  The mechanism assures that
   gateways running SATP are able to recover faults, enforcing ACID
   properties for asset transfers across ledgers (i.e., double spend
   does not occur).
- **draft-dikshit-bess-evpn-fhs-scoped-sync-01** (new-draft, score 0, ignored_after_review) [none]: [Scoped Sync for EVPN First-Hop-Security DHCP Snoop Routes](https://datatracker.ietf.org/doc/draft-dikshit-bess-evpn-fhs-scoped-sync/) — [I-D.ietf-bess-evpn-first-hop-security] defines a new EVPN Route
   Type, the DHCP Snoop Route (DSR), to synchronize DHCP snoop
   MAC/IP bindings across EVPN Provider Edge (PE) devices so that
   First Hop Security (FHS) functions such as Dynamic ARP Inspection,
   Neighbor Discovery Inspection, and IPv4/IPv6 Source Guard continue
   to operate correctly across EVPN multihoming and host mobility
   events.  As specified, a DSR is distributed to every PE
   participating in the EVPN Broadcast Domain (BD) in which it was
   learned.  In deployments where a single EVPN BD spans many
   geographically or administratively distinct fabrics interconnected
   over a WAN, this "flood to the whole BD" behavior distributes
   client IP/MAC binding information -- and therefore knowledge of
   which hosts exist behind which access switches -- well beyond the
   set of fabrics that actually need it for FHS purposes.  This
   document defines a Sync-Scope Extended Community that an
   originating PE MAY attach to a DSR to restrict its distribution to
   an explicitly identified subset of participating fabrics, and
   specifies the associated PE processing rules.
- **draft-dikshit-grow-bmp-rd-scoped-rib-stats-00** (new-draft, score 0, ignored_after_review) [none]: [Route-Distinguisher-Scoped BMP RIB Statistics](https://datatracker.ietf.org/doc/draft-dikshit-grow-bmp-rd-scoped-rib-stats/) — [RFC7854] defines the BGP Monitoring Protocol (BMP) and its
   Statistics Report message.  [I-D.ietf-grow-bmp-bgp-rib-stats]
   (published as [RFC9972]) extended that message with a set of
   advanced, per-AFI/SAFI BGP RIB statistics types.  Several ongoing
   individual contributions independently define additional per-
   address-family, per-instance, or per-Route-Distinguisher (RD)
   statistics on top of that base (for example, EVPN-specific RIB
   statistics and VRF Loc-RIB monitoring enhancements), each proposing
   its own ad hoc Stat Data encoding.

   This document defines a single, address-family-agnostic Stat Data
   container -- the "RD-Scoped Statistics" format -- for BMP
   statistics that are naturally scoped below the per-AFI/SAFI level,
   to a specific Route Distinguisher (VRF instance, EVPN Instance,
   MVPN instance, or equivalent).  Address-family-specific documents,
   such as EVPN-specific BMP RIB statistics, are expected to become
   thin "profiles" of this container rather than defining their own
   wire format, reducing duplication and Stat Type registry
   fragmentation across the GROW working group's BMP statistics work.
- **draft-dikshit-tiptop-oam-considerations-01** (new-draft, score 0, ignored_after_review) [none]: [Network Management and OAM Considerations for IP in Deep Space](https://datatracker.ietf.org/doc/draft-dikshit-tiptop-oam-considerations/) — [I-D.ietf-tiptop-usecase] and [I-D.ietf-tiptop-ip-architecture]
   describe key characteristics, use cases, requirements, and an IP
   architecture for deep-space (lunar, Mars, and beyond) surface and
   orbital-relay networking, characterized by long, variable,
   asymmetric propagation delay (single-digit to tens of minutes
   one-way), scheduled/intermittent connectivity windows, and severely
   constrained link capacity.  Section 8.2 of
   [I-D.ietf-tiptop-ip-architecture] addresses the configuration-
   management plane for this environment (NETCONF, RESTCONF, and SNMP
   transport selection and RTT-adjusted client timeouts), but neither
   document addresses the fault and performance dimensions of
   Operations, Administration, and Maintenance (OAM): fault detection,
   performance measurement, and reachability verification.

   This document identifies why conventional terrestrial OAM
   techniques (active round-trip probing such as ICMP Echo, BFD, or
   TWAMP; assumption of continuous connectivity) do not transfer
   directly to this environment, and proposes candidate adapted
   approaches -- passive, store-and-forward telemetry batched to
   contact windows; on-board local health self-diagnosis with delayed
   reporting; and confidence-interval-based reachability assessment in
   place of binary up/down status -- as a starting point for OAM
   discussion within the TIPTOP working group.  This document
   explicitly does not propose use of the Bundle Protocol or DTN
   architecture, both of which are out of scope for TIPTOP per its
   charter; where CCSDS space-data-system telemetry conventions are
   mentioned, it is as informative background only.
- **draft-dulaunoy-rifp-01** (new-draft, score 0, ignored_after_review) [none]: [Radio Image Framing Protocol (RIFP)](https://datatracker.ietf.org/doc/draft-dulaunoy-rifp/) — This document specifies the Radio Image Framing Protocol (RIFP), a
   compact, unidirectional object-transfer protocol intended for
   transmitting images over low-rate radio links.  RIFP defines
   independently synchronized frames, a versioned and extensible binary
   header, fragmentation and reassembly rules, a fixed binary object
   descriptor, optional JSON metadata, per-frame CRC-32 protection,
   whole-object SHA-256 verification, and registries for future frame
   types, flags, header extensions, media encodings, and radio profiles.

   RIFP is independent of a particular frequency allocation or
   modulation.  This document also defines an initial continuous-phase
   binary frequency-shift keying profile named rifp-cpfsk-4800.  The
   profile can be used on frequencies where local regulation permits
   such operation; 433.92 MHz is a common deployment example but is not
   mandated by this specification.
- **draft-gao-grow-bmp-config-monitor-tlv-01** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Configuration Monitoring TLV](https://datatracker.ietf.org/doc/draft-gao-grow-bmp-config-monitor-tlv/) — This document defines two types of BMP extended TLV, which are used
   to carry configuration information and configuration effective time
   related to BGP route changes.  Through this extension, the BGP
   monitoring platform can associate various BGP events with
   configuration operations, providing traceable evidence for
   identifying network failures caused by configuration changes.
- **draft-gerke-publication-process-reform-02** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.

   RFC 2026bis is updated by this document.
- **draft-gondwana-email-header-maintenance-02** (new-draft, score 0, ignored_after_review) [none]: [Maintenance of the IANA Message Header Field Registries](https://datatracker.ietf.org/doc/draft-gondwana-email-header-maintenance/) — The IANA "Message Headers" registries record, for each registered
   header field, the protocol it belongs to, its status, whether it is a
   trace field, and the document(s) that specify it.  These registries
   were populated incrementally by many documents over more than two
   decades, and the metadata that reached the registries is in several
   respects less complete than the metadata the registering documents
   supplied.  Most notably, the document that performed the single
   largest bulk registration, RFC 4021, gave IANA an explicit status and
   an explicit specification document for every one of the roughly
   ninety fields it registered, and neither was recorded: those entries
   carry a blank status and cite RFC 4021 itself rather than the
   specification.  Separately, the "Trace" column added to both
   registries by the ongoing revision of RFC 5322 was deliberately left
   empty for pre-existing entries, to be filled in later.

   This document reviews the initial definition of, and every subsequent
   update to, each registered header field, and gives IANA a single,
   coherent set of instructions for completing and correcting each
   registry entry.  Every recommended change, and every deliberate
   decision to leave a non-obvious entry unchanged, is justified by
   reference to the instructions already given by, or the clear intent
   of the authors of, the source documents in which the field was
   defined or modified.
- **draft-haynes-nfsv4-flexfiles-v2-07** (new-draft, score 0, ignored_after_review) [none]: [Parallel NFS (pNFS) Flexible File Layout Version 2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2/) — Parallel NFS (pNFS) allows a separation between the metadata (onto a
   metadata server) and data (onto a storage device) for a file.  The
   Flexible File Version 2 Layout Type is defined in this document as an
   extension to pNFS that allows the use of storage devices that require
   only a limited degree of interaction with the metadata server and use
   already-existing protocols.  Data protection is also added to provide
   integrity.  Both Client-side mirroring and the erasure coding
   algorithms are used for data protection.
- **draft-haynes-nfsv4-flexfiles-v2-proxy-server-03** (new-draft, score 0, ignored_after_review) [none]: [Proxy-Driven Server for Flexible Files Version 2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2-proxy-server/) — Parallel NFS (pNFS) with the Flexible Files Version 2 layout type
   supports client-side erasure coding and per-chunk repair between
   clients and data servers.  This document extends that architecture
   with a proxy server role: a registered peer of the metadata server
   that polls the metadata server for work assignments and carries them
   out -- moving a file from one layout to another, reconstructing a
   whole file from surviving shards, or translating between encodings
   for clients that cannot participate in the file's native encoding
   (including NFSv3 clients).  All proxy-server-to-metadata-server
   coordination is fore-channel: the metadata server returns work
   assignments inline in the response to a proxy-server-initiated
   PROXY_PROGRESS poll, and the proxy server reports completion via a
   fore-channel PROXY_DONE.  No callback operations are required for the
   proxy server protocol.
- **draft-he-idr-bgp-ec-sr-pm-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Extended Communities for SR Policy Performance Metrics](https://datatracker.ietf.org/doc/draft-he-idr-bgp-ec-sr-pm/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can meet the Qality of Service (QoS) reqiurements
   of the traffic to be scheduled.

   This document defines four BGP extended communities for Segment
   Routing (SR) candidate path performance metric: the Available
   Bandwidth Extended Community, the Unidirectional Delay Extended
   Community, the Unidirectional Delay Variation Extended Community and
   the Unidirectional Loss Extended Community, which carry SR Policy
   candidate path performance parameters for the operators to select a
   preferred path for traffic scheduling and optimization.  It also
   specifies the format and processing rules for these extended
   community types.
- **draft-he-idr-bgp-flowspec-ifit-04** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extensions to Enable BGP FlowSpec based IFIT](https://datatracker.ietf.org/doc/draft-he-idr-bgp-flowspec-ifit/) — Border Gateway Protocol (BGP) Flow Specification (FlowSpec) is an
   extension to BGP that supports the dissemination of traffic flow
   specifications and resulting actions to be taken on packets in a
   specified flow.  In-situ Flow Information Telemetry (IFIT) denotes a
   family of flow-oriented on-path telemetry techniques, which can
   provide high-precision flow insight and real-time network issue
   notification.  This document defines BGP extensions to distribute BGP
   FlowSpec based traffic filtering carrying IFIT information.
   Therefore, IFIT behavior can be automatically applied to the matched
   flow to capture real-time network dynamics.
- **draft-he-idr-bgpls-sr-policy-pm-00** (new-draft, score 0, ignored_after_review) [none]: [Advertisement of SR Policy Performance Metrics Using BGP-LS](https://datatracker.ietf.org/doc/draft-he-idr-bgpls-sr-policy-pm/) — This document defines several Type-Length-Values (TLVs) to advertise
   the performance metrics for Segment Routing (SR) Policy using BGP
   Link State (BGP-LS).  It complements RFC9857 for the advertisement of
   SR Policy performance metrics.  Such information can be used by the
   operators for monitoring the performance and state of the candidate
   path .
- **draft-he-ippm-ioam-trace-type-bandwidth-01** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace-Type Extensions for Path bandwidth](https://datatracker.ietf.org/doc/draft-he-ippm-ioam-trace-type-bandwidth/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can accommodate the capacity of the traffic to be
   scheduled.  In situ Operations, Administration, and Maintenance
   (IOAM) is used for recording and collecting operational and telemetry
   information.  This document defines two bit flags within IOAM Trace-
   Type for carrying bandwidth information.
- **draft-he-rtgwg-wan-pfc-01** (new-draft, score 0, ignored_after_review) [none]: [PFC PAUSE Frame Forwarded Transparently in Wide Area Networks](https://datatracker.ietf.org/doc/draft-he-rtgwg-wan-pfc/) — This document describes a solution for transparent forwarding of PFC
   PAUSE frames in wide area networks, which does not require the nodes
   in wide area networks to support PFC flow control capabilities.
- **draft-hko-openpgp-identifiers-for-legacy-devices-00** (new-draft, score 0, ignored_after_review) [none]: [Shortened OpenPGP identifiers for legacy hardware devices](https://datatracker.ietf.org/doc/draft-hko-openpgp-identifiers-for-legacy-devices/) — This document describes an approach for storing a shortened
   fingerprint-based lookup hint for OpenPGP private key material on
   hardware security devices.
- **draft-ietf-anima-rfc8366bis-34** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Bootstrapping Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
   device (Pledge) to an Owner using an artifact signed, directly or
   indirectly, by the Pledge's manufacturer.  This artifact is known as
   a "Voucher".

   This document defines an artifact format as a YANG-defined JSON or
   CBOR document that has been signed using a variety of cryptographic
   systems.

   The Voucher Artifact is normally generated by the Pledge's
   manufacturer (i.e., the Manufacturer Authorized Signing Authority
   (MASA)).

   This document obsoletes RFC8366: it includes a number of desired
   extensions into the YANG module.  The Voucher Request YANG module
   defined in RFC8995 is also updated and now included in this document,
   as well as other YANG extensions needed for variants of RFC8995.
- **draft-ietf-asdf-sdf-nonaffordance-04** (new-draft, score 0, ignored_after_review) [asdf]: [Semantic Definition Format (SDF) Extension for Non-Affordance Information](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-nonaffordance/) — This document describes an extension to the Semantic Definition
   Format (SDF) for representing non-affordance information of Things,
   such as physical, contextual, and descriptive metadata.  This
   extension introduces a new class keyword, sdfContext, that enables
   comprehensive modeling of Things and improves semantic clarity.
- **draft-ietf-avtcore-rtcp-green-metadata-14** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Control Protocol (RTCP) Messages for Temporal-Spatial Resolution](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtcp-green-metadata/) — The RTCP message formats specified in this document enables receivers
   to provide feedback to the senders and thus allows for short-term
   adaptation and feedback-based energy efficient mechanisms to be
   implemented.  The message formats have broad applicability in point-
   to-point real-time video communication services.  Specifically, it
   can be used to convey the video decoder feedback metadata to the
   encoder to adapte the decoder energy consumption as defined in the
   ISO/IEC International Standard 23001-11, known as Energy Efficient
   Media Consumption (Green metadata), developed by the ISO/IEC JTC
   1/SC29/WG3 MPEG Systems.
- **draft-ietf-bess-evpn-bfd-14** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Network Layer Fault Management](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-bfd/) — This document specifies proactive, in-band Network Layer OAM (RFC
   9062) mechanisms to detect loss of continuity faults that affect
   unicast and multi-destination paths (used by Broadcast, Unknown
   Unicast, and Multicast traffic) in an Ethernet VPN (EVPN, RFC
   7432bis) network.  The mechanisms specified in this document use the
   widely adopted Bidirectional Forwarding Detection (RFC 5880)
   protocol.
- **draft-ietf-bier-ospfv3-extensions-10** (new-draft, score 0, ignored_after_review) [bier]: [OSPFv3 Extensions for BIER](https://datatracker.ietf.org/doc/draft-ietf-bier-ospfv3-extensions/) — Bit Index Explicit Replication (BIER) is an architecture that
   provides multicast forwarding through a "BIER domain" without
   requiring intermediate routers to maintain multicast related per-flow
   state.  The BIER architecture uses MPLS or other encapsulations to
   steer the multicast traffic towards the receivers.

   This document describes the OSPFv3 protocol extensions required for
   BIER with MPLS encapsulation.  Support for other encapsulation types
   is outside the scope of this document.
- **draft-ietf-calext-jscalendar-icalendar-25** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-calext-jscontact-profiles-15** (new-draft, score 0, ignored_after_review) [calext]: [Protocol-Specific Profiles for JSContact](https://datatracker.ietf.org/doc/draft-ietf-calext-jscontact-profiles/) — This document defines JSContact profiles, an IANA registry for named
   subsets of JSContact elements.  It aims to facilitate using JSContact
   in context of contact data exchange protocols or other use cases, in
   which supporting all JSContact semantics might be inappropriate.
- **draft-ietf-cbor-serialization-08** (new-draft, score 0, ignored_after_review) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — This document defines two CBOR serializations: "preferred-plus
   serialization" and "deterministic serialization."  It also introduces
   the term "general serialization" to name the complete set of all
   serializations defined in RFC 8949.  Together, these three form a set
   of serializations that cover the majority of CBOR serialization use
   cases.

   These serializations are largely compatible with those widely
   implemented by the CBOR community.
- **draft-ietf-ccamp-fgotn-yang-01** (new-draft, score 0, ignored_after_review) [ccamp]: [YANG Data Models for fine grain Optical Transport Network](https://datatracker.ietf.org/doc/draft-ietf-ccamp-fgotn-yang/) — This document defines YANG data models to describe the topology and
   tunnel information of a fine grain Optical Transport Network.  The
   YANG data models defined in this document are designed to meet the
   requirements for efficient transmission of sub-1Gbit/s client signals
   in transport network.
- **draft-ietf-dmm-tn-aware-mobility-29** (new-draft, score 0, ignored_after_review) [dmm]: [Mapping 5G slice to Transport Network slice with UDP Source Ports](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-dnsop-structured-dns-error-27** (new-draft, score 0, ignored_after_review) [dnsop]: [Structured Error Data for Filtered DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/) — DNS filtering is widely deployed for various reasons, including
   network security and policy enforcement.  However, filtered DNS
   responses lack structured information for end users to understand the
   reason for the filtering.  Existing mechanisms to provide explanatory
   details to end users cause harm especially if the blocked DNS
   response is for HTTPS resources.

   This document updates RFC 8914 by signaling client support for
   structuring the EXTRA-TEXT field of the Extended DNS Error to provide
   details on the DNS filtering.  Such details can be parsed by the
   client and displayed, logged, or used for other purposes.
- **draft-ietf-idr-bgp-ls-sr-epe-over-l2bundle-07** (new-draft, score 0, ignored_after_review) [idr]: [Segment Routing BGP Egress Peer Engineering over Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-epe-over-l2bundle/) — This document specifies how to support Segment Routing BGP Egress
   Peer Engineering over Layer 2 bundle members.  It updates RFC 9085 to
   allow the L2 Bundle Member Attributes TLV in the BGP-LS Attribute of
   the BGP-LS Link NLRI for a BGP peering link.  For SR-MPLS, it updates
   RFC 9085 and RFC 9086 to allow the PeerAdj SID TLV as a sub-TLV of
   the L2 Bundle Member Attributes TLV.
- **draft-ietf-idr-rt-derived-community-10** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document specifies a way to derive an Extended Community from a
   Route Target and describes some example use cases.
- **draft-ietf-idr-ts-flowspec-srv6-policy-13** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) (as defined in RFC 8955, RFC 8956
   and RFC 9117) has been proposed to distribute BGP (RFC 4271) FlowSpec
   NLRI to FlowSpec clients to mitigate (distributed) denial-of-service
   attacks, and to provide traffic filtering in the context of a BGP/
   MPLS VPN service.  Recently, traffic steering applications in the
   context of SR-MPLS and SRv6 using FlowSpec are being used in
   networks.  This document introduces the usage of BGP Flow
   Specification to steer packets into an SR Policy.
- **draft-ietf-jmap-mail-sharing-02** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Mail Sharing](https://datatracker.ietf.org/doc/draft-ietf-jmap-mail-sharing/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) for Mail to enable sharing of mailboxes between
   users.  Building upon the JMAP Sharing framework defined in
   [RFC9670], this specification extends the Mailbox data type defined
   in [RFC8621] with properties necessary to configure and manage access
   permissions for shared mailboxes.  The extension introduces a new
   capability that indicates server support for mailbox sharing and
   defines the additional properties required to share mailboxes with
   other principals, including the ability to control which users may
   access a mailbox and what permissions they possess.
- **draft-ietf-lsr-distoptflood-14** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Distributed Flooding Reduction](https://datatracker.ietf.org/doc/draft-ietf-lsr-distoptflood/) — In dense topologies (such as data center fabrics based on the Clos
   and butterfly though not limited to those; in fact any large topology
   or one with relatively high degree of connectivity qualifies here)
   IGP flooding mechanisms designed originally for rather sparse
   topologies can "overflood", or in other words generate too many
   identical copies of same information arriving at a given node from
   other devices.  This normally results in longer convergence times and
   higher resource utilization to process and discard the superfluous
   copies.  Flooding algorithm extensions that restrict the amount of
   flooding performed can be constructed and can reduce resource
   utilization significantly, while improving convergence performance.

   One such flooding modification (based on previous art) optimized for
   operational considerations, described further in Section 2, is
   described in this document.
- **draft-ietf-lsr-flood-reduction-arch-02** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Flooding Reduction Algorithms Framework](https://datatracker.ietf.org/doc/draft-ietf-lsr-flood-reduction-arch/) — This document introduces a framework making it possible to deploy
   multiple flood reduction algorithms within the same IGP domain in an
   interoperable fashion.
- **draft-ietf-manet-inet-gap-analysis-04** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mpls-lsp-ping-ioam-conf-state-02** (new-draft, score 0, ignored_after_review) [mpls]: [LSP Ping/Traceroute for Enabled In-situ OAM Capabilities](https://datatracker.ietf.org/doc/draft-ietf-mpls-lsp-ping-ioam-conf-state/) — This document describes the application of the mechanism of
   discovering In-situ OAM (IOAM) capabilities, described in RFC 9359
   "Echo Request/Reply for Enabled In Situ OAM (IOAM) Capabilities", in
   MPLS networks.  The MPLS Node IOAM Information Query functionality
   uses the MPLS echo request/reply messages, allowing the IOAM
   encapsulating node to discover the enabled IOAM capabilities of each
   IOAM transit and IOAM decapsulating node.
- **draft-ietf-mpls-mna-ioam-09** (new-draft, score 0, ignored_after_review) [mpls]: [Supporting In Situ Operations, Administration, and Maintenance Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, collects operational and telemetry information in the
   packet using IOAM data fields while the packet traverses a path
   between two points in the network.  Several IOAM Option-Types are
   available, for example, Pre-allocated Trace, Proof-of-Transit, Edge-
   to-Edge, and Incremental Trace, that can be used to collect
   information for calculating various performance metrics.

   RFC 9326 defines the IOAM Direct Export (IOAM-DEX) Option-Type in
   which the operational state and telemetry information are collected
   according to the specified profile and exported in a manner and
   format defined by a local policy on each node along the path.

   MPLS Network Actions (MNA) techniques indicate actions to be
   performed on any combination of Label Switched Paths, MPLS packets,
   and the node itself, and to transport data needed for these actions.
   This document employs the MNA mechanisms to collect and transport the
   operational state and telemetry information using IOAM data fields as
   well as Direct Export.
- **draft-ietf-mpls-mna-ps-hdr-12** (new-draft, score 0, ignored_after_review) [mpls]: [Post-Stack MPLS Network Action (MNA) Header Specification](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ps-hdr/) — This document specifies the Post-Stack MPLS Network Action (MNA)
   Header encoding and procedures for carrying Network Action encodings
   and Ancillary Data after the MPLS label stack, based on the MNA Sub-
   Stack including In-Stack Network Actions and Data specified in RFC
   9994.  MPLS Network Actions can be used to influence packet
   forwarding decisions, carry additional Operations, Administration,
   and Maintenance information in the MPLS packet, or perform user-
   defined operations.  This document follows the framework specified in
   RFC 9789.

   This document updates RFC 9994: the "Network Action Opcodes" registry
   fields, the Post-Stack MNA applicability of the opcodes, MNA scope,
   and Unknown action handling.
- **draft-ietf-nfsv4-uncacheable-directories-09** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Directory-Entry Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  This
   caching is inherently best-effort: those attributes belong to the
   underlying files and change when the files are written, which the
   directory's change attribute does not track.  In some deployments the
   rate of file writes by other clients makes such caching produce
   incorrect size and timestamp values often enough to be a deployment
   problem.  This document introduces an uncacheable dirent metadata
   attribute for NFSv4.2 that allows a server to identify a directory
   for which an honoring client is required to retrieve directory-entry
   metadata from the server on each READDIR rather than serving the
   response from a local cache.
- **draft-ietf-nfsv4-uncacheable-files-11** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable File Data Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-files/) — Network File System version 4.2 (NFSv4.2) clients commonly perform
   client-side caching of file data in order to improve performance.  On
   some systems, applications may influence client data caching
   behavior, but there is no standardized mechanism for a server or
   administrator to indicate that particular file data should not be
   cached by clients for reasons of performance or correctness.  This
   document introduces a new file data caching attribute for NFSv4.2.
   Files marked with this attribute are intended to be accessed with
   client-side caching of file data suppressed, in order to support
   workloads that require predictable data visibility.  This document
   extends NFSv4.2.
- **draft-ietf-opsawg-ipfix-alt-mark-07** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-regext-rdap-versioning-07** (new-draft, score 0, ignored_after_review) [regext]: [Versioning in the Registration Data Access Protocol (RDAP)](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-versioning/) — This document describes an RDAP extension for an extensible set of
   versioning types with the features of identifying the RDAP extension
   versions supported by the server, the RDAP extension versions
   included in an RDAP response, and enabling a client to specify the
   desired RDAP extension versions to include in the RDAP query and RDAP
   response.  In addition, this document defines a mechanism for
   communicating versioning and deprecation information that facilitates
   coordinated transitions between successive extension versions while
   minimizing the impact of breaking changes on deployed clients.
- **draft-ietf-satp-core-15** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer Protocol (SATP) Core](https://datatracker.ietf.org/doc/draft-ietf-satp-core/) — This memo describes the Secure Asset Transfer Protocol (SATP) for
   digital assets.  SATP is a protocol operating between two gateways
   that conducts the transfer of a digital asset from one gateway to
   another, each representing their corresponding digital asset
   networks.  The protocol establishes a secure channel between the
   endpoints and implements a 2-phase commit (2PC) to ensure the
   properties of transfer atomicity, consistency, isolation and
   durability.
- **draft-ietf-schc-8824-update-10** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression (SCHC) for the Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/draft-ietf-schc-8824-update/) — This document defines how to compress Constrained Application
   Protocol (CoAP) headers using the Static Context Header Compression
   and fragmentation (SCHC) framework.  SCHC defines a header
   compression mechanism adapted for constrained devices, and it uses a
   static description of the header to reduce the header's redundancy
   and size.  While RFC 8724 describes the SCHC compression and
   fragmentation framework and its application for IPv6 and UDP headers,
   this document applies SCHC to CoAP headers.  The CoAP header
   structure differs from that of IPv6 and UDP headers, since CoAP uses
   a flexible header with a variable number of options that are in turn
   of variable length.  The CoAP message format is asymmetric, i.e.,
   request messages have a header format different from that of response
   messages.  This specification gives guidance on applying SCHC to
   flexible headers and on leveraging the message format asymmetry for
   defining more efficient compression Rules.  This document replaces
   and obsoletes RFC 8824.
- **draft-ietf-scone-protocol-06** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-spring-srv6-security-16** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing IPv6 Security Considerations](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/) — SRv6 is a traffic engineering, encapsulation and steering mechanism
   utilizing IPv6 addresses to identify segments in a pre-defined
   policy.  This document discusses security considerations in SRv6
   networks, including the potential threats and the possible mitigation
   methods.  The document does not define any new security protocols or
   extensions to existing protocols.
- **draft-ietf-tcpm-tcp-ghost-acks-09** (new-draft, score 0, ignored_after_review) [tcpm]: [Improve TCP Handling of Out-of-Window Packets to Mitigate Ghost ACKs](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ghost-acks/) — Historically, TCP as specified in RFC 793 was threatened by the blind
   data injection attack because of the loose SEG.ACK value validation,
   where the SEG.ACK value of a TCP segment is considered valid as long
   as it does not acknowledge data ahead of what has been sent.  RFC
   5961 improved the input validation by shrinking the range of
   acceptable SEG.ACK values in a TCP segment.  Later, RFC 9293
   incorporated the updates proposed by RFC 5961 as a TCP stack
   implementation option.
   However, an endpoint that follows the RFC 9293 specifications can
   still accept a TCP segment containing an SEG.ACK value acknowledging
   data that the endpoint has never sent.  This document specifies small
   modifications to the way TCP verifies incoming TCP segments' SEG.ACK
   value to prevent TCP from accepting such invalid SEG.ACK values.
- **draft-ietf-teas-actn-poi-assurance-05** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) for Packet Optical Integration (POI) service assurance](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-assurance/) — This document extends the analysis of the applicability of
   Abstraction and Control of TE Networks (ACTN) architecture to Packet
   Optical Integration (POI) to cover multi-layer service assurance
   scenarios.  Specifically, the ACTN architecture supports service
   assurance through the detection and correlation of failures across
   the optical and packet layers, with failure handling performed
   through the relevant PNC.  The MDSC can also request health checks
   for IP services across multi-domain paths for SLA conformance
   assessment.  The PNCs may also be configured with thresholds so that
   alerts are reported when relevant service or network conditions
   exceed defined limits.  It is assumed that the underlying transport
   optical network carries end-to-end IP services such as L2VPN or L3VPN
   connectivity services, with specific Service Level Agreement (SLA)
   requirements.

   Existing IETF protocols and data models are identified for each
   multi-layer (packet over optical) service assurance scenario with a
   specific focus on the MPI (Multi-Domain Service Coordinator to
   Provisioning Network Controllers Interface) in the ACTN architecture.
- **draft-ietf-tvr-off-path-exposure-03** (new-draft, score 0, ignored_after_review) [tvr]: [Using off-path mechanisms for exposing Time-Variant Routing information](https://datatracker.ietf.org/doc/draft-ietf-tvr-off-path-exposure/) — Time-Variant Routing (TVR) involves predictable, scheduled changes to
   network topology elements such as nodes, links, and adjacencies that
   impact routing behavior over time.  All those changes can alter the
   connectivity in the network in a predictable manner, which is known
   as Time-Variant Routing (TVR).  This document proposes mechanisms for
   exposing TVR information to both internal and external applications,
   focusing on off-path solutions that decouple the advertisement of
   scheduled changes from the routing control plane signaling.
- **draft-ietf-v6ops-6mops-08** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).  The proposed
   approach enables smooth and incremental transition from dual-stack to
   IPv6-only network by allowing IPv6-capable devices to remain
   IPv6-only while the network is seamlessly supplying IPv4 to those
   that require it.
- **draft-ietf-v6ops-nat64-wkp-1918-05** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the requirement introduced in Section 3.1 of
   RFC6052 that IPv4/IPv6 Translators MUST NOT use the Well-Known Prefix
   64:ff9b::/96 to represent non-globally reachable IPv4 addresses, such
   as those defined in RFC1918 or listed in Section 2.2.2 of RFC6890.
   The proposed change enables IPv6-only nodes to reach IPv4-only
   services with specific non-globally reachable addresses by leveraging
   the Well-Known Prefix.

   This document updates Section 3.1 of RFC6052 ("Restrictions on the
   Use of the Well-Known Prefix") to allow packets in which an address
   is composed of the Well-Known Prefix and specific non-globally
   reachable IPv4 addresses to be translated.
- **draft-jeong-nmrg-intent-based-sdv-framework-00** (new-draft, score 0, ignored_after_review) [none]: [An Intent-Based Management Framework for Software-Defined Vehicles in Intelligent Transportation Systems](https://datatracker.ietf.org/doc/draft-jeong-nmrg-intent-based-sdv-framework/) — Software-Defined Vehicle (SDV) is a new player towards autonomous
   vehicles in Intelligent Transportation Systems (ITS).  An SDV is
   constructed by a software platform like a cloud-native system (e.g.,
   Kubernetes) and has its internal network.  To facilitate the easy and
   efficient configuration of networks in the SDV, an intent-based
   management is an appropriate direction.  This document proposes a
   framework of intent-based management for networks, security, and
   applications in SDVs so that they can communicate with other SDVs and
   infrastructure nodes for safe driving and infotainment services in
   the road networks.
- **draft-jurkovikj-http-semantic-validator-01** (new-draft, score 0, ignored_after_review) [none]: [Semantic Validators for HTTP](https://datatracker.ietf.org/doc/draft-jurkovikj-http-semantic-validator/) — This document defines the Semantic-ETag HTTP response field and the
   If-Semantic-Match HTTP request field.  Unlike the standard ETag
   field, which identifies a selected representation, Semantic-ETag
   identifies a server-defined semantic state within an explicitly
   scoped semantic equivalence domain.  If-Semantic-Match enables origin
   servers to perform representation-independent optimistic concurrency
   control when different HTTP resources or representations expose the
   same logical state.

   This document does not update or replace the semantics of ETag, If-
   Match, or HTTP cache validation defined by RFC 9110.
- **draft-khrabrov-dnsop-aname-axfr-00** (new-draft, score 0, ignored_after_review) [none]: [Address-specific DNS Aliases (ANAME) and Zone Transfer](https://datatracker.ietf.org/doc/draft-khrabrov-dnsop-aname-axfr/) — This document defines the ANAME DNS resource record.  ANAME provides
   name-to-name indirection for address queries while allowing other
   resource record types to exist at the same owner name.  It is
   therefore usable at a zone apex.

   This document also defines authoritative processing, TTL and failure
   behavior, DNSSEC considerations, and interoperable transport of ANAME
   records in full and incremental zone transfers.  In particular, each
   ANAME-capable authoritative server resolves the transferred target
   independently.  This avoids treating transient, synthesized address
   records as the portable source of zone data.
- **draft-kohbrok-mls-two-party-profile-01** (new-draft, score 0, ignored_after_review) [none]: [A two-party profile for MLS](https://datatracker.ietf.org/doc/draft-kohbrok-mls-two-party-profile/) — TODO Abstract
- **draft-kwatsen-netconf-quic-call-home-01** (new-draft, score 0, ignored_after_review) [none]: [NETCONF Call Home and RESTCONF Call Home Using QUIC](https://datatracker.ietf.org/doc/draft-kwatsen-netconf-quic-call-home/) — This RFC extends NETCONF Call Home and RESTCONF Call Home [RFC 8071]
   to support the QUIC protocol [RFC 9000].
- **draft-lampin-schc-voici-00** (new-draft, score 0, ignored_after_review) [none]: [VOICI](https://datatracker.ietf.org/doc/draft-lampin-schc-voici/) — The Static Context Header Compression (SCHC) framework identified the
   need for a minimal transport encapsulation that provides Session
   multiplexing when extrinsic Discriminators are insufficient.  This
   document specifies a Link Multiplexer (VOICI) that addresses those
   SCHC-driven requirements while remaining general enough to
   accommodate other compression mechanisms and uncompressed payloads.
   The encapsulation is designed for minimal overhead, reducing to 1
   byte in the common case (7 inline Session IDs), while supporting
   optional integrity protection and original EtherType/port recovery.
- **draft-lampin-schc-voici-compression-00** (new-draft, score 0, ignored_after_review) [none]: [SCHC Compression of VOICI Headers](https://datatracker.ietf.org/doc/draft-lampin-schc-voici-compression/) — This document describes how to compress VOICI headers using SCHC
   rules at a lower stratum, demonstrating that VOICI provides explicit
   routing metadata that is transparently compressed to minimal on-wire
   size while preserving standardized dispatch semantics.  It is
   intended as a reference for implementers deploying VOICI in SCHC-
   based networks and does not modify the VOICI specification itself.
- **draft-lenders-dns-cbor-18** (new-draft, score 0, ignored_after_review) [none]: [A Concise Binary Object Representation (CBOR) of DNS Messages](https://datatracker.ietf.org/doc/draft-lenders-dns-cbor/) — This document specifies a compact data format of DNS messages using
   the Concise Binary Object Representation [RFC8949].  The primary
   purpose is to keep DNS messages small in constrained networks.
- **draft-many-tiptop-email-02** (new-draft, score 0, ignored_after_review) [none]: [Deploying and Using Email in Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-email/) — This document is an assessment on the email protocols to be used in
   deep space and provides recommendations to deploy and use email in
   deep space.
- **draft-martin-retry-over-ipv6-04** (new-draft, score 0, ignored_after_review) [none]: [HTTP Signaling of Planned IPv4 Unavailability](https://datatracker.ietf.org/doc/draft-martin-retry-over-ipv6/) — As operators transition services to IPv6-only, planned IPv4 outages
   help identify remaining dependencies before permanent decommission.
   Such outages must be measurable, reversible, and understandable to
   end users.  This document defines HTTP signaling for an intentional,
   often time-bounded IPv4 outage: the existing 503 Service Unavailable
   status code together with the mandatory Retry-Over-IPv6 response
   header field (and optional related fields) that instruct aware
   clients to retry over IPv6 after closing the IPv4 connection, and
   allow clients to confirm successful IPv6 recovery via an optional
   correlation token so operators can distinguish soft failures from
   hard failures in centralized logs.  Machine-readable response bodies
   MAY use Problem Details (RFC 9457) with a registered problem type
   URI.  The mechanism supports staged enterprise rollouts, internal
   HTTP services, and permanent IPv6-only migration; coordinated public
   events (for example, 6/6 drills) remain possible with advance notice.
   The primary intended deployment is operator-controlled environments
   where provider and users share operational responsibility.  Legacy
   clients that do not implement this specification treat the response
   as ordinary service unavailability and MAY use the response body for
   human-readable guidance.
- **draft-pardue-moq-qlog-moq-events-07** (new-draft, score 0, ignored_after_review) [none]: [MoQ qlog event definitions](https://datatracker.ietf.org/doc/draft-pardue-moq-qlog-moq-events/) — This document defines a qlog event schema containing concrete events
   for MoQ.
- **draft-quan-l4s-ioam-02** (new-draft, score 0, ignored_after_review) [none]: [IOAM network awareness for Low Latency, Low Loss, and Scalable Throughput (L4S)](https://datatracker.ietf.org/doc/draft-quan-l4s-ioam/) — This document specifies a framework that uses operational and
   telemetry information collected by In Situ Operations,
   Administration, and Maintenance (IOAM) to support the monitoring and
   parameter adjustment of an L4S Dual-Queue Coupled AQM within a single
   limited domain.  IOAM Direct Export reports path and node
   information, such as hop-by-hop delay and queue depth, to an IOAM
   Control Center (IOAM-C).  The IOAM-C correlates this information and
   may adjust operator-configurable AQM target or threshold parameters
   within configured bounds.  This document does not modify the L4S ECN
   protocol, the IOAM data formats, or the packet forwarding behavior
   defined by the referenced specifications.
- **draft-reilly-plants-bulk-subtree-proofs-01** (new-draft, score 0, ignored_after_review) [none]: [Bulk Subtree Consistency Proofs for Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-reilly-plants-bulk-subtree-proofs/) — Merkle Tree Certificates require relying parties to periodically
   obtain a set of active landmark subtrees and verify each is
   consistent with a reference checkpoint of the issuance log.  As
   specified, this requires one subtree consistency proof per landmark
   subtree, and those proofs share a large fraction of their interior
   nodes.

   This document defines a bulk subtree consistency proof, which
   verifies an entire set of landmark subtrees against a single
   reference checkpoint from one shared set of hashes.  It is a size
   optimization for the relying party update channel and introduces no
   change to certificate verification or to the security properties of
   Merkle Tree Certificates.

   This revision replaces the construction published in -00, which was
   incorrect.  See Appendix "Changes from -00".
- **draft-saum-grow-bmp-afi-safi-evpn-06** (new-draft, score 0, ignored_after_review) [none]: [EVPN-Specific BMP RIB Statistics Extensions](https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/) — This document defines new EVPN-specific BGP Monitoring Protocol
   (BMP) statistics types.  These extensions include scalar counters
   for EVPN route types specifically, while also keeping scope for
   defining counters which are EVPN route-type agnostic but related to
   BGP-EVPN RIB like, number of multihoming Ethernet Segments, number
   of multihomed EVIs, number of aliased paths, number of dynamic
   inter-VRF route leaking (IVRL).

   This revision (-06) firms up the specification for working group
   consideration: it adds a Relationship to Other Work section that
   explicitly maps this document to concurrently circulating GROW
   contributions on BMP statistics and TLV extensions and invites
   coordination with their authors, corrects the YANG alignment
   reference, strengthens Security Considerations, and adds a worked
   example. No statistics semantics, Stat Type/Subtype allocations, or
   wire formats defined in -05 are changed.
- **draft-saumthimma-evpn-ip-binding-sync-10** (new-draft, score 0, ignored_after_review) [none]: [Secure IP Binding Synchronization via BGP EVPN](https://datatracker.ietf.org/doc/draft-saumthimma-evpn-ip-binding-sync/) — The distribution of clients of L2 domain across extended networks
   leveraging overlay fabric needs to deal with synchronizing the
   Client Binding Database.  The 'Client IP Binding' indicates the IP,
   MAC and VLAN details of the clients that are learnt by security
   protocols.  Since learning the 'Client IP Binding database' is a
   last mile solution, this information stays local to the end point
   switch to which clients are connected.  When networks are extended
   across geographies, both at layer 2 and layer 3, the 'Client IP
   Binding Database' in end point switches of remote fabrics should be
   in sync.  This document aligns the synchronization of the 'Client
   IP Binding Database' through an extension to BGP control plane
   constructs, as BGP is a typical control plane protocol configured
   to communicate across network boundaries.
- **draft-saumvinayak-bess-all-df-bum-13** (new-draft, score 0, ignored_after_review) [none]: [All PEs as DF](https://datatracker.ietf.org/doc/draft-saumvinayak-bess-all-df-bum/) — The Designated Forwarder concept is leveraged to prevent looping of
   BUM traffic into a tenant network sourced across an NVO fabric for
   multihoming deployments.  [RFC7432] defines a preliminary approach
   to select the DF for an ES, VLAN or ES, VLAN Group, spanning
   multiple NVEs.  [RFC8584] makes the election logic more robust and
   fine grained by inculcating fair election of DF, handling most of
   the prevalent use cases.  This document presents a deployment
   problem and a corresponding solution which cannot be easily
   resolved by rules mentioned in [RFC7432] and [RFC8584].  It
   involves redundant firewall deployment on disparate overlay sites
   connected over WAN.  The requirement is to allow reachability, ONLY,
   to the local firewall, unless there is an outage.  In case of
   outage the reachability can be extended to the remote site's
   firewall over WAN.
- **draft-sayre-gendispatch-derivative-04** (new-draft, score 0, ignored_after_review) [none]: [Clarification of Derivative Works Restrictions](https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/) — This document clarifies that only IETF Documents may contain legal
   limitations on derivative works.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/.

   Discussion of this document takes place on the ipr-wg Working Group
   mailing list (mailto:ipr-wg@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/ipr-wg/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/ipr-wg/.
- **draft-smc-grow-bmp-route-change-stats-02** (new-draft, score 0, ignored_after_review) [none]: [BMP Route Change Statistics Based on Routing Policy](https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/) — This document defines few generic BGP Monitoring Protocol (BMP)
   statistics for monitoring route modifications or changes due to
   applying Routing Policy.  These statistics are reported per BGP
   peer using the BMP Statistics Report message.

   This revision (-02) firms up the specification for working group
   consideration: it adds a Relationship to Other Work section that
   explicitly maps this document to concurrently circulating GROW
   contributions on BMP statistics and policy-driven telemetry and
   invites coordination with their authors, adds a worked example, and
   strengthens Security Considerations. No statistics semantics, Stat
   Type allocations, or wire formats defined in -01 are changed.
- **draft-smith-6man-accurate-ra-router-lifetime-03** (new-draft, score 0, ignored_after_review) [none]: [More Accurately Naming IPv6 RA Router Lifetime](https://datatracker.ietf.org/doc/draft-smith-6man-accurate-ra-router-lifetime/) — IPv6 Router Advertisements (RAs) have a "Router Lifetime" field,
   which specifies how long the advertising router will act as a default
   router for the receiving hosts, unless refreshed with another
   advertisement.  The field name "Router Lifetime" is quite general,
   and could easily be misunderstood to mean the bounded lifetime of all
   of the information contained in the RA.  This memo more accurately
   renames this field "Default Router Lifetime".
- **draft-tlmk-infra-dnssd-03** (new-draft, score 0, ignored_after_review) [dnssd]: [Providing Local Unicast DNS-SD Service on Infrastructure](https://datatracker.ietf.org/doc/draft-tlmk-infra-dnssd/) — DNS Service Discovery provides several mechanisms whereby hosts can
   discover and advertise services on an IP network.  Such discovery can
   be done using Multicast DNS (mDNS) or DNS, and advertising can be
   done with DNS-SD Service Registration Protocol (SRP) or mDNS.  This
   document defines Unicast Local Discovery (ULD), a service that
   combines an SRP registrar, a Discovery Proxy, and an Advertising
   Proxy.  Hosts can use a ULD server to advertise and discover services
   on the local link entirely via unicast SRP and DNS while remaining
   interoperable with hosts that use mDNS.
- **draft-trammell-happy-sad-01** (new-draft, score 0, ignored_after_review) [none]: [Slow Alternate Detection for Happy Eyeballs](https://datatracker.ietf.org/doc/draft-trammell-happy-sad/) — This document specifies Slow Alternate Detection (SAD) for Happy
   Eyeballs, an ICMP-based advisory path signal [RFC8558] for exposing
   information about path non-selection on-path devices in order to aid
   debugging and measurement of Happy Eyeballs.
- **draft-xiao-fann-congestion-notification-for-pause-00** (new-draft, score 0, ignored_after_review) [none]: [Congestion Notification for Pause](https://datatracker.ietf.org/doc/draft-xiao-fann-congestion-notification-for-pause/) — This document describes the necessity and feasibility to introduce a
   mechanism of congestion notification for pause.  After receiving the
   L2 pause frames from the destination data center gateway, the egress
   provider edge node sends the congestion notifications to the upstream
   provider nodes and the ingress provider edge node in a format defined
   in this document.  The upstream provider nodes and the ingress
   provider edge node must pause the forwarding of IP flows identified
   by the congestion notifications.  And then the ingress provider edge
   node may send the L2 pause frames to the source data center gateway.
- **draft-xiao-fann-fast-cnp-00** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) in RoCEv2 Networks](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp/) — This document describes a Remote Direct Memory Access (RDMA) over
   Converged Ethernet version 2 (RoCEv2) congestion control mechanism,
   which is inspired by Really Explicit Congestion Notification (RECN)
   described in RFC 7514, also known as Fast Congestion Notification
   Packet (Fast CNP).  By extending the RoCEv2 CNP, Fast CNP can be sent
   by the switch directly to the sender, advising the sender to reduce
   the transmission rate at which it sends the flow of RoCEv2 data
   traffic.
- **draft-xiao-fann-fast-cnp-with-proxy-00** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-yan-sidrops-rpki-terminology-05** (new-draft, score 0, ignored_after_review) [none]: [RPKI Terminology](https://datatracker.ietf.org/doc/draft-yan-sidrops-rpki-terminology/) — The Resource Public Key Infrastructure (RPKI) is defined in dozens of
   different RFCs.  The terminology used by implementers and developers
   of RPKI protocols, and by operators of RPKI systems, can at times be
   inconsistent, leading to confusion.  In an effort to improve
   consistency in this respect, this document provides a single location
   for definitions of commonly-used RPKI terms.
- **draft-yl-bmwg-cats-05** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for Computing-aware Traffic Steering](https://datatracker.ietf.org/doc/draft-yl-bmwg-cats/) — Computing-aware traffic steering (CATS) is a traffic engineering
   approach for steering service requests towards appropriate service
   instances based on the awareness of both computing and network
   information.  This document proposes benchmarking methodologies for
   CATS.
- **draft-zhu-sketch-int-codesign-01** (new-draft, score 0, ignored_after_review) [none]: [Sketch-INT Co-Design for Accurate Network Measurement: Applicability to Time-Variant Non-Terrestrial Networks](https://datatracker.ietf.org/doc/draft-zhu-sketch-int-codesign/) — Network measurement supports management applications that need
   statistics about both large and small flows.  Sketch-based techniques
   use compact data structures and are effective for large flows, but
   hash collisions can produce substantial relative errors for small
   flows.  In-band Network Telemetry (INT) can provide detailed
   observations for individual packets, but applying it to every packet
   can consume significant packet, bandwidth, and collector resources.

   This document describes a framework that uses sketches for large
   flows and INT for small flows.  It also describes measurement-point
   selection when exact routing information is unavailable and
   congestion-aware collection of sketch and INT reports.  The document
   identifies the information needed to describe and compare
   implementations.  It does not define a new packet format, INT
   instruction, sketch algorithm, or routing protocol.

   As a concrete applicability direction, the document considers time-
   variant non-terrestrial networks (NTNs), in which paths and available
   forwarding resources can change over time.  It maps the existing
   Sketch-INT framework to this scenario and identifies the assumptions
   that require validation.  It does not claim that the existing
   terrestrial implementation has been deployed or evaluated on
   satellite hardware.

## Errors / fetch failures

_None._
