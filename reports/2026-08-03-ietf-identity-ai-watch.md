# IETF Identity + AI Standards Watch

Date: 2026-08-03

## Read now

- **draft-vso-cpp-core-03** (new-draft, score 27, trust_infrastructure) [none]: [Content Provenance Profile (CPP) Core](https://datatracker.ietf.org/doc/draft-vso-cpp-core/) — The Content Provenance Profile (CPP) is an open specification for
   cryptographically verifiable media capture provenance.  This document
   defines the core data model, hashing conventions, Merkle tree
   construction rules, RFC 3161 Time-Stamp Authority (TSA) anchoring
   protocol, and offline verification procedures for CPP.

   CPP enables capture devices to produce tamper-evident provenance
   records that bind media content to external timestamps via trusted
   third parties.  Unlike self-attestation models, CPP requires
   independent timestamp verification through RFC 3161 TSA services,
   providing externally verifiable proof of when media was captured.

   CPP defines self-attested signer identity, hardware-backed key
   requirements, chain context for partial submission detection, a
   Completeness Invariant for omission detection, an OPTIONAL depth
   analysis extension for screen detection, and an OPTIONAL Pre-Publish
   Verification Extension.  It also defines interoperability mappings
   with the C2PA specification.

   This revision (-03) corrects a normative length constraint on the
   LeafHashMethod value, corrects the description of the relationship
   between the CPP Merkle construction and Certificate Transparency,
   adds a verifier obligation to cross-check TreeSize against the sealed
   event count, documents the limits of leaf-duplication padding, and
   positions CPP within the Verifiable AI Provenance Framework (VAP)
   profile family and relative to the SCITT architecture (RFC 9943).
- **draft-helixar-hdp-agentic-delegation-01** (new-draft, score 24, agent_identity) [none]: [Human Delegation Provenance Protocol (HDP): Cryptographic Chain-of-Custody for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/) — Agentic AI systems operate on behalf of human principals, often
   delegating tasks through multi-step chains of AI agents.  There is
   currently no standard mechanism to record who authorized an agent to
   act, under what scope, and through what chain of delegation, in a way
   that can be verified offline, without a central registry, and without
   third-party trust anchors.

   This document specifies the Human Delegation Provenance Protocol
   (HDP) version 0.1, a lightweight token-based protocol that captures,
   structures, cryptographically signs, and verifies human delegation
   context in agentic AI systems.  An HDP token binds a human
   authorization event to a session, records each agent's delegation
   action as a signed hop in an append-only chain, and enables any
   participant to verify the full provenance record using only the
   issuer's Ed25519 public key and the current session identifier.
   Verification is fully offline.  No registry lookup, no network call,
   and no third-party trust anchor is required.

   HDP's distinguishing contribution is a signed, tamper-evident record
   of each agent's declared action at each hop, an execution audit trail
   that complements, rather than replaces, capability-based delegation
   formats such as UCAN and ZCAP-LD.  The underlying append-only,
   offline-verifiable chain-of-custody mechanism is payload-agnostic;
   human-authorized agentic delegation is the reference profile
   specified in this document.
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
- **draft-flores-aidp-provenance-00** (new-draft, score 17, core_identity) [none]: [The AIDP Provenance Seal and Serving Register](https://datatracker.ietf.org/doc/draft-flores-aidp-provenance/) — A response served by an inference provider carries no verifiable
   statement of what produced it.  A recipient cannot determine which
   model generated a given output, nor whether the endpoint that served
   it was authorized by the party whose name is on it.  Attribution
   today rests on the serving party's own account of events, offered
   after the fact and at its own discretion.

   This document specifies two mechanisms that together make that
   determination decidable by a recipient.  The Provenance Seal is a
   detached signature by which a provider binds a model identifier, its
   own identity, and a timestamp to the exact bytes of a served
   response.  The Serving Register is a signed document listing, for
   each provider, the endpoints authorized to serve its models, the
   public keys that validate its seals, and whether the provider
   declares that it seals every response.  A DNS record under the
   provider's own domain binds that domain to its register entry and to
   its declared sealing policy, so that a suppressed seal is detectable
   rather than merely absent.

   The design follows electronic mail authentication: the seal is
   patterned on DKIM, the register on SPF, and the declared sealing
   policy on the published policy record of DMARC.
- **draft-schrock-action-evidence-boundary-03** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
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
- **draft-schrock-ep-authorization-evidence-chain-05** (new-draft, score 17, authorization) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
   delegation, policy, permit, approval, transparency, capability, and
   execution artifacts.  Each artifact can verify under its own
   specification while still referring to a different action, filling a
   different evidentiary role, or failing a relying party's freshness,
   status, or inter-artifact binding requirement.  This document defines
   the Authorization Evidence Chain (EP-AEC): a transport-agnostic
   composition object and a fail-closed evaluation algorithm that
   preserves native verification, establishes exact material-action
   matching, and evaluates a relying-party-pinned evidence requirement.

   AEC produces SATISFIED or UNSATISFIED and a replayable evaluation
   record.  SATISFIED means only that the presented evidence filled the
   relying party's named evidence requirement at the stated verification
   time.  It is not a universal authorization decision, a policy
   language for the protected application, or proof of execution or
   outcome.  The executor makes the separate local AUTHORIZED decision
   and controls consumption, invocation, and effect handling.
   Qualification evidence can fill a named evidence role but cannot
   authorize an action by itself.  AEC introduces no new component
   receipt type and does not replace any native verifier.
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
- **draft-bu-agentproto-security-principal-binding-04** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-howard-virp-06** (new-draft, score 15, core_identity) [none]: [VIRP: Verified Infrastructure Response Protocol](https://datatracker.ietf.org/doc/draft-howard-virp/) — The Verified Infrastructure Response Protocol (VIRP) defines a trust
   framework for operators -- human or autonomous -- acting on live
   network infrastructure.  As operations shift toward agentic and
   automated systems that can autonomously configure, audit, and
   remediate production environments, the absence of a verifiable chain
   of custody for observations and actions introduces fundamental risks:
   fabricated telemetry, unauthorized state changes, and the inability
   to distinguish legitimate operations from compromise.  VIRP routes
   every observation and every authorization decision through a
   designated collection-and- verification boundary that the requesting
   party does not control.  Observations are authenticated at collection
   time using HMAC-SHA256; in session-bound mode (Section 6.4)
   authentication uses a per-session key and binds the response to
   session, device, sequence, and a command-digest field.  Validating
   the command binding additionally requires trusted request context
   from which the verifier recomputes the command digest.  A two-channel
   architecture separates read-only Observation from write-intent
   Intent, and trust tiers (GREEN/YELLOW/RED/BLACK) govern action
   authorization with human-in-the-loop controls for elevated
   operations.

   VIRP's observation and chain-integrity guarantees are symmetric and
   explicitly scoped by key role; approval and federation records use
   asymmetric Ed25519 signatures.  Distinct key roles authenticate
   observations, chain entries, intents, approvals, and federation
   records (Section 6.1), though the reference implementation currently
   reuses one key across the v1-observation and v2-derivation roles; a
   holder of a symmetric key can both verify and forge within that key's
   scope, so VIRP does not provide publicly verifiable observation
   origin and does not defend a record against an adversary holding the
   relevant key or controlling the collection boundary.  Authentication
   does not certify that a response reflects the managed device's true
   state, only that the boundary obtained and authenticated those bytes
   for that recorded request.  Asymmetric proof of origin and external
   anchoring of the chain are distinct, independent items of future work
   (Section 17).
- **draft-ietf-oauth-transaction-tokens-11** (new-draft, score 15, core_identity) [oauth]: [Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) — Transaction Tokens (Txn-Tokens) are designed to maintain and
   propagate user identity, workload identity and authorization context
   throughout the Call Chain within a trusted domain during the
   processing of external requests (e.g. such as API calls) or requests
   initiated internally within the Trust Domain.  Txn-Tokens ensure that
   this context is preserved throughout the Call Chain thereby enhancing
   security and consistency in complex, multi-service architectures.
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
- **draft-schemacommons-areg-00** (new-draft, score 13, adjacent_watchlist) [none]: [Agent Registry (AREG)](https://datatracker.ietf.org/doc/draft-schemacommons-areg/) — The Agent Registry (AREG) is an open, vendor-neutral specification
   for publishing, discovering, and resolving artificial intelligence
   (AI) agent definitions.  An AREG registry entry is a lightweight
   metadata document that records where a specific version of an agent
   definition can be fetched, who published it, what version it is, and
   how consumers can verify its authenticity.  AREG also defines a REST
   API that conforming registry servers implement to expose search,
   resolution, and publication endpoints to consumers and publishers.

   AREG is the discovery and registry layer of the Schema Commons agent
   stack.  It is designed to compose with the Autonomous Agent
   Interchange Format (AAIF, SC-006), which defines the content of the
   agent definition document that an AREG entry points to, and with the
   Agent Capability and Profile Model (ACPM, SC-014), which provides
   richer capability, trust, cost, and service-level information that a
   registry entry can reference.  Neither AAIF nor ACPM is required for
   a conforming AREG implementation.
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
- **draft-norton-sdlp-lineage-03** (new-draft, score 11, core_identity) [none]: [SDLP Lineage Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-lineage/) — This document defines the SDLP lineage model, which provides the
   canonical method for representing the ancestry of SDLP-governed
   objects. Lineage is a structural property that records how an object
   evolves through duplication and transformation events. The lineage
   model ensures that descendant objects remain uniquely identifiable
   and traceable across all lifecycle transitions.

   Lineage-03 aligns the lineage grammar with Identity-02, Lifecycle-02,
   and Object-Format-07, and defines deterministic ancestry extension
   rules that produce stable, verifiable lineage across all SDLP
   implementations. This revision incorporates BitDrop conditions for
   invalid lineage transitions and specifies normative validation
   requirements for relying parties. Together with Identity-02,
   Lifecycle-02, and Object-Format-07, this document provides the
   authoritative lineage model required for interoperable identity,
   lifecycle, and provenance processing.
- **draft-schrock-ep-bounded-execution-program-00** (new-draft, score 11, authorization) [none]: [Bounded Execution Programs for Consequential Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-execution-program/) — An authorization for one action does not by itself authorize an open-
   ended agent plan.  This document defines an Experimental profile for
   a signed, finite, versioned directed acyclic graph of consequential
   action occurrences.  The program binds a total retained-history
   ceiling.  Each node binds an exact action or a pinned action-matching
   profile, an action- specific Trust Program, outcome-specific
   dependencies, an occurrence ceiling, and fixed charges against
   aggregate attempt budgets.

   A conforming program-aware admission store evaluates reachability and
   budgets in the same linearizable transaction domain as the ordinary
   one-time execution right.  It uses store-owned authorizer trust
   roots, clock, authenticated profile-match verification, and current
   program status; seals a deterministic execution-program resource into
   the AdmissionSnapshot; and fences the program's independent
   authorization digest against ordinary-path admission.  The profile
   does not establish that natural-language intent was understood, that
   a plan is safe or lawful, that provider or effect evidence is true,
   or that every mutation path was mediated.
- **draft-chapman-a2a-mls-03** (new-draft, score 10, core_identity) [none]: [End-to-End Encryption and Purpose-Bound Governance for Agent-to-Agent Messaging](https://datatracker.ietf.org/doc/draft-chapman-a2a-mls/) — Agent-to-agent protocols increasingly carry messages between
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
- **draft-mih-agent-accountability-conformance-00** (new-draft, score 10, authorization) [none]: [Agent Accountability: A Conformance and Verification Method](https://datatracker.ietf.org/doc/draft-mih-agent-accountability-conformance/) — An architecture for auditing agent-driven interactions (draft-
   kuehlewind-audit-architecture) identifies the record types an
   auditable agent system produces — interaction, action, delegation,
   and authorization-transition — and the role of an Auditor that
   determines whether recorded behaviour matched intent and the
   authorization in force.  That architecture does not specify how an
   Auditor, or any independent party, deterministically verifies that a
   set of such records — produced by different parties, in different
   profiles, and composed into one case — is internally consistent and
   correctly derives an audit conclusion.

   This document specifies a horizontal conformance and verification
   methodology for composed agent-accountability records.  It organizes
   conformance into three tiers: the payload-binding layer, per-record-
   type (per-slot) conformance, and composition (combination)
   conformance.  It defines the determinism boundary between what is
   mechanically derivable from the binding rules and the individual
   records, and what is irreducibly semantic; a conformance-vector
   discipline (positive, negative, and must-fail cases, checked in both
   directions) that any record profile reuses rather than reinvents; and
   a deterministic method for deriving composition-conformance vectors
   from binding rules, individual-record vectors, a composition
   manifest, and a set of cross-record predicates.  The methodology is
   profile-agnostic: it applies uniformly to any accountability record
   type and to any declared composition of them, whether those records
   are joined across parties or across attestation layers.  Its lower
   two tiers verify a single record, so the method applies where no
   composition is present and strengthens as records are composed.  It
   is intended as the composition-verification work item of the auditing
   architecture — the one its enumerated work items do not yet cover.
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
- **draft-ranjbar-dane-did-01** (new-draft, score 8, core_identity) [none]: [Rooting Decentralized Identifiers in DNSSEC: A DANE-EE Key-Binding Profile](https://datatracker.ietf.org/doc/draft-ranjbar-dane-did/) — Several Decentralized Identifier (DID) methods root trust in a DNS
   name: did:web binds an identifier to a domain and today verifies its
   keys over the Web PKI, did:dns serves DID data from DNS resource
   records, and did:webvh retrieves its history from an HTTPS location
   derived from a name.  Each either depends on the Web PKI, treats
   DNSSEC as an optional recommendation, or does not bind the
   verification-method key to the name at all.  This document defines a
   single, normative DANE-EE key-binding profile that any DNS-anchored
   DID method can point at rather than reinventing: a verification
   method's public key is published as a TLSA record with certificate
   usage DANE-EE(3), selector SubjectPublicKeyInfo(1), and matching type
   SHA2-256(1) under a DNSSEC-signed name, so that a relying party can
   confirm the key from the DNS root of trust with no certificate
   authority and no fetch from the subject.  The profile binds a name to
   a key and the key to the specific DID document it signs, and no
   further; it states precisely what it does not cover, including
   continuity of holding, and points to where those answers live.
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
- **draft-benaudis-iic-credential-00** (new-draft, score 7, core_identity) [none]: [The Internet Identity Card (IIC) Credential Format: A Self-Contained, Offline-Verifiable Identity Credential with Hybrid Classical and Post-Quantum Signatures](https://datatracker.ietf.org/doc/draft-benaudis-iic-credential/) — This document describes the Internet Identity Card (IIC) credential
   format, version 9.0: a digital identity credential implemented as a
   single self-contained HTML file that can be generated, stored,
   transferred, and cryptographically verified entirely offline, without
   servers, brokers, or network connectivity.  Identity data is
   encrypted with AES-256-GCM under keys derived by Argon2id;
   authenticity is provided by a hybrid signature combining ECDSA P-256
   with ML-DSA-65 (NIST FIPS 204) under a crypto-agile suite registry;
   and integrity is provided by an embedded SHA-256 self-check over a
   canonical serialization of the document.  Each exported credential
   embeds its own verification engine, so verification requires only a
   standard web browser.  This document is published for informational
   purposes, to describe a deployed format whose underlying
   constructions are disclosed as open prior art.
- **draft-kamimura-scitt-refusal-events-03** (new-draft, score 7, trust_infrastructure) [none]: [Verifiable AI Refusal Events using SCITT](https://datatracker.ietf.org/doc/draft-kamimura-scitt-refusal-events/) — This document defines a claim set for recording AI content refusal
   events.  The claim set specifies the semantic content and correlation
   rules for refusal audit trails, independent of any particular
   serialization format.  The claims are designed to be carried within
   SCITT Signed Statements and verified using SCITT Receipts.

   This specification addresses claim semantics and verification
   requirements; it does not mandate a specific encoding.  A CDDL
   definition is provided for CBOR-based implementations, and equivalent
   JSON representations are shown in an appendix for illustration.

   This specification provides auditability of logged refusal decisions.
   It does not define content moderation policies, classification
   criteria, or what AI systems should refuse.
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
- **draft-schrock-ep-bounded-capability-receipts-01** (new-draft, score 7, authorization) [none]: [Bounded Capability Receipts and Durable Spend Control for Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-capability-receipts/) — Agents sometimes need bounded authority to perform more than one
   consequential action without obtaining a new human approval for every
   operation.  A signed token alone cannot enforce a shared budget
   across replicas, survive retries safely, or distinguish an operation
   that never crossed an effect boundary from one whose outcome is
   unknown.

   This document defines a bounded capability receipt and a durable
   reserve-execute-commit protocol.  The receipt binds an issuance
   authorization, a closed action scope, a budget with explicit units, a
   holder proof, an expiry, and any parent capability.  The state
   protocol atomically refuses overspend and replay, fences concurrent
   owners, and charges an indeterminate operation when an external
   effect may have occurred.  Delegation transfers rather than copies
   authority: all direct child allocations are funded by committed
   parent operations before child registration, and their aggregate
   cannot exceed the parent balance within one authoritative atomic
   state domain.  It also defines narrowing-only delegation and evidence
   interfaces.  It does not make a bearer token into human approval,
   does not provide cross-domain or offline global double-spend
   prevention, and does not claim that an authorized action was safe,
   lawful, or successfully executed.

## Monitor

- **draft-ietf-lamps-rfc8551bis-00** (new-draft, score 6, core_identity) [lamps]: [Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Message Specification](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc8551bis/) — This document defines Secure/Multipurpose Internet Mail Extensions
   (S/MIME) version 4.0.  S/MIME provides a consistent way to send and
   receive secure MIME data.  Digital signatures provide authentication,
   message integrity, and non-repudiation with proof of origin.
   Encryption provides data confidentiality.  Compression can be used to
   reduce data size.  This document obsoletes RFC 5751.
- **draft-liang-tcp-provenance-option-02** (new-draft, score 6, core_identity) [none]: [TCP Provenance Identifier Option](https://datatracker.ietf.org/doc/draft-liang-tcp-provenance-option/) — This document describes a TCP option that carries a Provenance
   Identifier (ProvID) to enable correlation of TCP connections when
   transport-layer identifiers change along the path.
- **draft-lohmann-qikvrt-effect-ack-03** (new-draft, score 6, authorization) [none]: [QIK-VRT Effect Acknowledgement: Separating Receipt from Authorization for Downstream Effect](https://datatracker.ietf.org/doc/draft-lohmann-qikvrt-effect-ack/) — Transport acknowledgements establish technical receipt; they do not
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
- **draft-norton-sdlp-obj-format-07** (new-draft, score 6, core_identity) [none]: [SDLP Object Format Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-obj-format/) — This document defines the canonical object format for the Secured
   Digital Lifecycle Protocol (SDLP). The object format specifies the
   normative byte-level representation used for hashing, signing,
   validation, and interoperability across SDLP implementations. All
   SDLP-governed objects MUST follow the canonical encoding, field
   ordering, and serialization grammar defined in this specification.

   Object-Format-07 freezes the canonical envelope grammar and provides
   a concrete example of a fully serialized SDLP object to illustrate
   how DigitalID, InstanceID, Lineage, Timestamp, and Body are encoded
   in practice. This revision also introduces brief application context
   describing how SDLP objects are used in provenance, auditability, and
   regulated-content workflows.

   This document updates and replaces draft-norton-sdlp-obj-format-06
   and provides the authoritative definition of the SDLP object format
   required for interoperable identity, lineage, and lifecycle
   processing.
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
- **draft-schrock-ep-reliance-agreement-00** (new-draft, score 6, authorization) [none]: [Reliance Agreements: Signed Liability Terms Conditioned on Authorization-Evidence Sufficiency](https://datatracker.ietf.org/doc/draft-schrock-ep-reliance-agreement/) — This document defines EP-RELIANCE-AGREEMENT-v1, a signed, machine-
   readable statement of terms conditioned on a specific relying-party
   evidence profile, and EP-RELIANCE-EVENT-v1, a signed per-action
   record joining one action, one reliance result, and one agreement.
   The agreement references the evidence condition by digest rather than
   restating or weakening it.  Every required party signs the same
   canonical bytes, and monetary amounts are represented as decimal
   strings.

   Verification establishes signatures, content integrity, scope, time,
   and digest bindings.  It does not authorize an action, re-evaluate
   the evidence packet, establish legal enforceability, issue insurance,
   determine coverage, allocate fault, prove solvency, reserve funds, or
   compel payment.  Those decisions remain with the relying party and
   the applicable prose agreement, law, and dispute forum.
- **draft-schrock-model-to-matter-03** (new-draft, score 6, authorization) [none]: [Model-to-Matter: Authorization and Outcome Evidence for Model-Directed Physical Execution](https://datatracker.ietf.org/doc/draft-schrock-model-to-matter/) — Advanced models can propose operations that produce physical effects.
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
- **draft-thallapelly-oasnt-enforce-00** (new-draft, score 6, authorization) [none]: [OASNT-ENFORCE: Request-Bound Enforcement of Attested Action Authorization](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt-enforce/) — This document profiles the enforcement of OASNT tokens at the point
   of execution.  It defines the OASNT-Token HTTP field, the rules by
   which an enforcement point derives the observed request from the
   octets it will itself forward, a verification procedure for relying
   parties that hold no request-to-action mapping, uniform refusal
   behavior, and the set of refusals a conforming enforcement point is
   required to produce.  An enforcement point conforming to this profile
   makes a human approval a precondition of execution for the requests
   it fronts, without any change to the protected service.
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
- **draft-ietf-dnsop-filtering-transparency-00** (new-draft, score 4, trust_infrastructure) [dnsop]: [DNS Filtering Transparency](https://datatracker.ietf.org/doc/draft-ietf-dnsop-filtering-transparency/) — [I-D.ietf-dnsop-structured-dns-error] introduces structured error
   data for DNS responses that have been filtered.  This specification
   allows more specific details of filtering incidents to be conveyed.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/public-resolver-errors.
- **draft-reilly-aipref-compliance-00** (new-draft, score 4, adjacent_watchlist) [none]: [Verifiable Compliance Records for AI Usage Preferences](https://datatracker.ietf.org/doc/draft-reilly-aipref-compliance/) — Work in the AI Preferences (AIPREF) Working Group defines a
   vocabulary for expressing preferences about how digital assets may be
   used by automated processing systems, together with mechanisms for
   attaching those preferences to content.  Neither component provides a
   way for a processing entity to demonstrate that it observed an
   expressed preference, nor for a publisher or auditor to verify such a
   demonstration after the fact.

   This document defines the AI Usage Compliance Record (AUCR), a
   structure that binds a retrieved asset, the preference expression in
   force at the moment of retrieval, and the usage category the
   processing entity assigned to that asset.  It defines an aggregation
   scheme that allows a processing entity to attest to very large
   numbers of records with a single signature, a proof mechanism that
   allows an individual publisher to audit only the records concerning
   its own assets, and a discovery mechanism for locating attestations
   and verification keys.  The mechanism is deliberately confined to
   evidence: it makes claims of compliance falsifiable and non-
   repudiable, and takes no position on the legal effect of any
   preference or any record.

## Adjacent / watchlist

- **draft-besleaga-sustainability-wellknown-05** (new-draft, score 3, adjacent_watchlist) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI.  This
   URI provides a uniform, out-of-band convention for web servers and
   digital services to publish aggregated environmental impact, energy
   consumption, and carbon footprint metrics for a declared reporting
   subject -- typically the publishing origin itself.

   By utilizing an asynchronous reporting model, this approach allows
   for transparent environmental accounting without the bandwidth and
   energy overhead associated with per-request HTTP headers.
- **draft-bonica-tcpm-tcp-ao-long-algs-05** (new-draft, score 3, core_identity) [none]: [Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256 and KMAC256.  For
   each MAC algorithm, a corresponding Key Derivation Function (KDF) is
   also added.

   The MAC algorithms described by this document produce 256-bit (i.e.,
   32-byte) MACs.  When 32-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 36 of the 40 bytes available for TCP options.
- **draft-eastlake-dnssd-rfc2931bis-sigzero-02** (new-draft, score 3, core_identity) [none]: [Domain Name System (DNS) Public Key Based Request and Transaction Authentication (SIGZERO, SIG(0))](https://datatracker.ietf.org/doc/draft-eastlake-dnssd-rfc2931bis-sigzero/) — This document specifies the SIGZERO and SIG(0) Domain Name System
   (DNS) Resource Records (RRs) which provide public key based
   authentication of DNS requests and transactions.  SIGZERO is the
   RECOMMENDED option.  This document obsoletes RFC 2931.
- **draft-fomicheva-aether-00** (new-draft, score 3, core_identity) [none]: [Aether: A Next-Generation L4 Transport](https://datatracker.ietf.org/doc/draft-fomicheva-aether/) — This document specifies Aether, a transport-layer protocol (L4)
   designed for modern network environments requiring multiplexed
   streams without head-of-line blocking, mandatory encryption with
   post-quantum resistance, multi-path routing, and self-sovereign
   identity at the protocol layer.  Aether operates entirely in
   userspace without kernel modifications.
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
- **draft-ietf-httpbis-no-vary-search-07** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
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
- **draft-ietf-tcpm-tcp-ao-algs-06** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
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
- **draft-ma-dnssd-srp-service-routing-00** (new-draft, score 3, core_identity) [none]: [Service Type Routing for DNS-SD Service Registration Protocol](https://datatracker.ietf.org/doc/draft-ma-dnssd-srp-service-routing/) — This document defines the _str._dns-sd._udp (Service Type Routing)
   metadata label, a backward-compatible extension for SRP registration.
   This mechanism relaxes the original single-registration-domain
   constraint, enabling clients to publish distinct service types to
   independent target DNS zones and dedicated SRP registrar instances.
   It supports fine-grained operational tuning, administrative isolation
   of heterogeneous services.  This extension only modifies SRP
   registration domain selection logic, fully preserves existing SRP
   wire format, authentication, leasing and discovery behaviors, and
   introduces no impact on DNS-SD service browsing operations.
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
- **draft-wang-ring-load-aware-00** (new-draft, score 3, adjacent_watchlist) [none]: [Load-Adaptive Priority Migration Mechanism for Deterministic Switched Ethernet](https://datatracker.ietf.org/doc/draft-wang-ring-load-aware/) — This document proposes a Load-Adaptive Priority Migration (LAPM)
   mechanism for deterministic switched Ethernet.  The mechanism
   classifies traffic into three criticality levels (TC0/TC1/TC2), which
   are logically equivalent to the foundational classification of
   network slicing.  An inverse M/D/1 queuing model is introduced to
   derive per-hop network utilization from measured forwarding delay,
   requiring no additional probe traffic.  A four-level load
   classification scheme with hysteresis logic drives dynamic remapping
   of the IEEE 802.1Q Priority Code Point (PCP), enabling traffic
   priority to adapt as network load changes.

   LAPM serves as a runtime complement to the scheduling framework
   defined by RFC 9320.  Existing DetNet queuing mechanisms (TAS, CBS,
   CQF, Guaranteed Service) rely on statically pre-configured offline
   parameters, whereas LAPM monitors utilization in real time and
   adaptively adjusts PCP when load levels cross pre-defined thresholds.
   This capability is particularly critical for deployment scenarios
   with time-varying traffic patterns, including automotive backbone
   networks, industrial automation, and professional audio/video
   systems.

   Experimental validation on a 5-node ring topology (1000BASE-T) across
   three traffic classes reveals the existence of three operationally
   distinct regions — normal, transitional, and saturated — where load
   bursts in the transitional region cannot be captured by the EWMA-
   smoothed utilization metric alone.  A cross-domain maximum
   aggregation mechanism coordinates load-level decisions across
   multiple VLANs via a shared global variable, ensuring consistent
   priority migration policy enforcement.

   In summary, the LAPM mechanism provides a means to guarantee low-
   latency transmission for critical flows through dynamic load-based
   priority control.
- **draft-chapman-a2a-offline-delivery-00** (new-draft, score 2, ignored_after_review) [none]: [Offline Delivery and Reachability for Agent-to-Agent Messaging](https://datatracker.ietf.org/doc/draft-chapman-a2a-offline-delivery/) — Agent-to-agent protocols assume a live HTTP or streaming hop.  Many
   deployments cannot keep every agent always reachable: devices sleep,
   cost tiers duty-cycle backends, and operators park agents outside
   business hours.  Senders need a machine-readable asleep signal, a
   bounded expectation for store-and-forward, and validation rules so an
   offline agent is not a spam sink and does not act on forged or
   expired messages after wake.

   This document profiles offline delivery and reachability for A2A-
   style JSON-RPC messaging.  It defines abstract reachability modes, an
   asleep refusal signal, queue bounds and distinct queue-full errors,
   validate-on-dequeue requirements, and split delivery semantics
   (durable persist versus notify).  It is independent of Messaging
   Layer Security (MLS) grouping; deployments that also use [GOMLS] MAY
   apply both profiles.
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

## Ignored after review

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
- **draft-carpenter-rswg-authoring-ethics-06** (new-draft, score 0, ignored_after_review) [none]: [Principles and Guidelines for Assignment of RFC Authorship](https://datatracker.ietf.org/doc/draft-carpenter-rswg-authoring-ethics/) — This document discusses principles and guidelines for assigning
   authorship in RFC documents, including guidelines for the use of
   software tools during document preparation, and for inclusion of
   material from other sourcess.  An important focus is on authors'
   responsibility for the content.  The document also discusses the
   related issues of acknowledgements, editors and contributors.  The
   various RFC streams are expected to apply these guidelines, and
   possibly define their own variations, which will have priority.
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
- **draft-he-rtgwg-wan-pfc-01** (new-draft, score 0, ignored_after_review) [none]: [PFC PAUSE Frame Forwarded Transparently in Wide Area Networks](https://datatracker.ietf.org/doc/draft-he-rtgwg-wan-pfc/) — This document describes a solution for transparent forwarding of PFC
   PAUSE frames in wide area networks, which does not require the nodes
   in wide area networks to support PFC flow control capabilities.
- **draft-hko-openpgp-identifiers-for-legacy-devices-00** (new-draft, score 0, ignored_after_review) [none]: [Shortened OpenPGP identifiers for legacy hardware devices](https://datatracker.ietf.org/doc/draft-hko-openpgp-identifiers-for-legacy-devices/) — This document describes an approach for storing a shortened
   fingerprint-based lookup hint for OpenPGP private key material on
   hardware security devices.
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
- **draft-ietf-calext-jscalendar-icalendar-25** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
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
- **draft-ietf-dmm-tn-aware-mobility-30** (new-draft, score 0, ignored_after_review) [dmm]: [Mapping 5G slice to Transport Network slice with UDP Source Ports](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-mpls-mna-ps-hdr-14** (new-draft, score 0, ignored_after_review) [mpls]: [Post-Stack MPLS Network Action (MNA) Header Specification](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ps-hdr/) — This document specifies the Post-Stack MPLS Network Action (MNA)
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
- **draft-ietf-rtgwg-vrrp-p2mp-bfd-15** (new-draft, score 0, ignored_after_review) [rtgwg]: [Applicability of Bidirectional Forwarding Detection (BFD) for Multi-point Networks in Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-p2mp-bfd/) — This document specifies the applicability of Bidirectional Forwarding
   Detection in multipoint networks to support sub-second failure
   detection for Virtual Router Redundancy Protocol Router Role
   election.  The mechanism enables faster determination of the Active
   Router without requiring any modification to the protocol behavior or
   message formats defined in RFC 9568.
- **draft-ietf-satp-core-15** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer Protocol (SATP) Core](https://datatracker.ietf.org/doc/draft-ietf-satp-core/) — This memo describes the Secure Asset Transfer Protocol (SATP) for
   digital assets.  SATP is a protocol operating between two gateways
   that conducts the transfer of a digital asset from one gateway to
   another, each representing their corresponding digital asset
   networks.  The protocol establishes a secure channel between the
   endpoints and implements a 2-phase commit (2PC) to ensure the
   properties of transfer atomicity, consistency, isolation and
   durability.
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
- **draft-ietf-teas-ns-controller-models-08** (new-draft, score 0, ignored_after_review) [teas]: [IETF Network Slice Controller and its Associated Data Models](https://datatracker.ietf.org/doc/draft-ietf-teas-ns-controller-models/) — This document describes an approach for structuring the IETF Network
   Slice Controller as well as how to use different data models being
   defined for IETF Network Slice Service provision (and how they are
   related).  It is not the purpose of this document to standardize or
   constrain the implementation of the IETF Network Slice Controller.
- **draft-ietf-v6ops-6mops-08** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).  The proposed
   approach enables smooth and incremental transition from dual-stack to
   IPv6-only network by allowing IPv6-capable devices to remain
   IPv6-only while the network is seamlessly supplying IPv4 to those
   that require it.
- **draft-ietf-v6ops-ipv6-only-01** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
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
- **draft-nurpmeso-dkim-access-control-diff-changes-12** (new-draft, score 0, ignored_after_review) [dkim]: [DKIM Access Control and Differential Changes](https://datatracker.ietf.org/doc/draft-nurpmeso-dkim-access-control-diff-changes/) — This document specifies a DKIM (RFC 6376) iteration that allows
   cryptographical verification of SMTP (RFC 5321) envelope data, and of
   any signature along the message path, even beyond IMF (RFC 5322)
   message content changes.  It addresses existing security glitches,
   and introduces active mitigations to embrace collateral damage
   effects of email solutions of the younger past by a standardized
   solution, also by moving complexity away from lower network protocol
   layers, where problems cannot be solved.  It updates DKIM in certain
   aspects that reality has proven to be superfluous, incomplete, or
   obsoleted.
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
- **draft-rabadan-bess-evpn-srv6-ar-00** (new-draft, score 0, ignored_after_review) [none]: [Applicability of EVPN Assisted Replication to SRv6 Tunnels](https://datatracker.ietf.org/doc/draft-rabadan-bess-evpn-srv6-ar/) — Assisted Replication (AR) is an optimized ingress replication
   solution for Ethernet VPN (EVPN) Broadcast and Multicast (BM)
   traffic.  AR offloads the replication effort from ingress Network
   Virtualization Edge (NVE) devices onto Assisted Replication
   Replicators (AR-REPLICATORs).  The base AR specification is focused
   on Network Virtualization Overlay (NVO) networks that use IP tunnels,
   and it is typically deployed for Virtual eXtensible Local Area
   Network (VXLAN).  EVPN services can also be instantiated over Segment
   Routing over IPv6 (SRv6); however, the SRv6 EVPN transport
   specification supports only ingress replication for BUM traffic, and
   the AR procedures rely on IP-tunnel semantics (such as the tunnel
   source and destination IP addresses) that do not map exactly to an
   SRv6 data plane.  As a result, AR cannot be readily deployed over
   SRv6 tunnels.

   This document specifies the applicability of Assisted Replication to
   SRv6 tunnels, for EVPN BM traffic, for selective multicast based on
   Internet Group Management Protocol (IGMP) and Multicast Listener
   Discovery (MLD) proxy, and for EVPN IP multicast traffic based on
   Optimized Inter-Subnet Multicast (OISM).  It defines a new SRv6
   Endpoint behavior for the AR-REPLICATOR role and the associated
   control-plane procedures, so that the AR solution can be used with an
   SRv6 underlay.
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
