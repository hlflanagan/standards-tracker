# IETF Identity + AI Standards Watch

Date: 2026-08-12

## Read now

- **draft-vasylenko-pait-protocol-01** (new-draft, score 28, adjacent_watchlist) [none]: [Provenance-Attributed Inference Token (PAIT): A Protocol for Token-Level Inference Provenance and Identity-Conditioned Inference in Generative AI Systems](https://datatracker.ietf.org/doc/draft-vasylenko-pait-protocol/) — This document specifies the Provenance-Attributed Inference Token
   (PAIT) protocol, a wire-level protocol for token-level provenance
   attribution and identity-conditioned inference in Large Language
   Model (LLM) systems and other generative AI systems.  PAIT defines:
   (1) an Agent Identity Token format that binds a globally unique
   agent identifier to a hierarchical authorization level by means of
   an asymmetric digital signature; (2) a Provenance Manifest Record
   format that associates each output token of an inference session
   with verifiable attribution data referencing training-corpus
   segments; (3) a Trust Telemetry Signal format for aggregated session
   metrics emission to external monitoring endpoints; and (4) a wire
   protocol state machine governing the interaction between a
   requesting agent and a generative AI endpoint.  PAIT is intended to
   address the transparency obligations imposed by emerging regulatory
   frameworks for high-risk and general-purpose AI systems, in
   particular those concerning the provenance of AI-generated content
   at sub-document granularity.
- **draft-fane-opena2a-aip-02** (new-draft, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
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
   9162-style Merkle transparency log for identity and credential
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
- **draft-hillier-scitt-arp-02** (new-draft, score 26, trust_infrastructure) [none]: [Attestation Reconciliation Protocol](https://datatracker.ietf.org/doc/draft-hillier-scitt-arp/) — This document specifies the Attestation Reconciliation Protocol
   (ARP), a deterministic, bilateral, minimum-disclosure mechanism for
   reconciling verification claims against a plurality of sovereign
   authoritative registers without raw register records leaving their
   data-residency jurisdiction.  ARP extends the SCITT (Supply Chain
   Integrity, Transparency, and Trust) architecture to cross-sovereign
   claim reconciliation.  A reconciliation server canonicalises a
   structured claim, binds the identity of the requesting principal --
   including, where the requester is an autonomous agent, a friend-or-
   foe determination of that agent's verifiable principal binding --
   projects the claim through register-specific controlled projection
   functions producing the nearest permitted ancestor predicate
   supported by each addressed register, transmits register-specific
   ciphertexts, receives partial attestations whose payload discloses
   only a verdict and an optional divergence axis, aggregates the
   partial attestations through either homomorphic or hash-linkage
   aggregation, and seals the resulting reconciliation output against a
   policy-version hash.  An append-only cross-jurisdictional settlement-
   layer ledger records only hashes, with no content.  The protocol
   supports retroactive re-evaluation of historical reconciliations
   under updated pattern libraries or policy versions without bilateral
   renegotiation, and a cryptographic-primitive-upgrade path including
   post-quantum primitives.  This revision adds agentic-principal
   reconciliation, requester identity binding, alignment with HTTP
   Message Signatures and COSE Receipts, and composition of
   heterogeneous agent-action accountability attestations into a single
   producer-agnostic reconciled verdict evaluated at decision time.
- **draft-hardt-httpbis-signature-key-08** (new-draft, score 22, core_identity) [httpbis]: [HTTP Signature Keys](https://datatracker.ietf.org/doc/draft-hardt-httpbis-signature-key/) — This document defines five HTTP header fields for use with HTTP
   Message Signatures as defined in RFC 9421.  The Signature-Key request
   header distributes public keys used to verify signatures, with eight
   initial key distribution schemes: pseudonymous inline keys (hwk),
   self-issued key delegation via JWK Thumbprint JWTs (jkt-jwt),
   identified signers with JWKS URI discovery (jwks_uri), direct JWKS
   fetch (jwks), JWT-based delegation (jwt), self-issued JWTs (self-
   jwt), X.509 certificate chains (x509), and references to previously
   cached assertions (cached).  The Accept-Signature-Scheme and Accept-
   Signature-Alg response headers state the schemes and algorithms a
   server accepts, so a client can select both before it signs.  The
   Signature-Error response header provides structured error information
   when signature verification fails, and the Signature-Key-Cache
   response header issues a cache identifier by which a caller can
   reference a previously presented assertion instead of resending it.
   Together, these mechanisms enable flexible trust models ranging from
   privacy-preserving pseudonymous verification to horizontally-scalable
   delegated authentication and PKI-based identity chains.
- **draft-norton-sdlp-interop-profile-04** (new-draft, score 22, trust_infrastructure) [none]: [SDLP Interoperability Profile for Ownership, Verification, and Provenance Evidence](https://datatracker.ietf.org/doc/draft-norton-sdlp-interop-profile/) — This document defines an interoperability profile for the Secured
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
- **draft-hawkins-scitt-attested-agent-payment-00** (new-draft, score 18, trust_infrastructure) [none]: [Attested Payment Authorization for Autonomous Agents](https://datatracker.ietf.org/doc/draft-hawkins-scitt-attested-agent-payment/) — Autonomous software agents increasingly initiate payments on behalf
   of principals.  Existing agent-payment mechanisms authenticate the
   human principal, the operator, or possession of a key; none of them
   establishes that the software authorized to spend is the software
   that was reviewed.  A key held by a compromised or silently modified
   agent authenticates exactly as well as one held by an honest agent.

   This document defines a payment authorization scope bound to a key
   whose protection properties are attested by hardware, and registers
   the resulting authorization as a Signed Statement on an SCITT
   Transparency Service.  The binding reuses the EAT confirmation and
   key-attributes claims without modification; the contribution is the
   authorization scope, the verification procedure a payment executor
   performs before settlement, and the transparency record that makes
   the authorization auditable independently of the agent and of the
   executor.
- **draft-flores-airp-provenance-00** (new-draft, score 17, core_identity) [none]: [The AIRP Provenance Seal and Serving Register](https://datatracker.ietf.org/doc/draft-flores-airp-provenance/) — A response served by an inference provider carries no verifiable
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
- **draft-kroehl-agentic-trust-aae-01** (new-draft, score 17, authorization) [none]: [Agent Authorization Envelope (AAE): A Machine-Evaluable Authorization Structure for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/) — Autonomous AI agents now operate at production scale across
   financial, commercial, and infrastructure domains — executing
   transactions, invoking APIs, and taking consequential actions without
   direct human oversight at each step.  Existing authorization
   mechanisms (OAuth 2.0, API keys, ACLs) were designed for human-
   initiated requests and do not capture the machine-evaluable semantics
   required for autonomous agent authorization: what the agent is
   mandated to do, what constraints bound its actions, and for how long
   the authorization is valid.

   This document specifies the Agent Authorization Envelope (AAE), a
   structured authorization container for autonomous AI agents.  AAE
   defines three mandatory blocks — MANDATE, CONSTRAINTS, and VALIDITY —
   that together constitute a machine-evaluable, cryptographically
   verifiable authorization assertion.  AAE is designed to be protocol-
   agnostic, binding to W3C Decentralized Identifiers (DIDs) for agent
   identity and W3C Verifiable Credentials (VCs) for issuance and
   signature, and is independent of any specific AI framework, transport
   protocol, or blockchain.
- **draft-maintainer-1f916-agent-record-00** (new-draft, score 17, agent_identity) [none]: [The Agent Record: Transparent, Witness-Countersigned Event Logs for AI Agent Identity, History, and Memory](https://datatracker.ietf.org/doc/draft-maintainer-1f916-agent-record/) — Autonomous AI agents increasingly act as economic parties: they are
   hired, they pay, and they make claims about their own past conduct.
   No deployed standard lets a relying party verify an agent's identity
   continuity, the integrity of its claimed history, or the intactness
   of its persisted memory without trusting the agent's operator or
   platform.

   This document describes the Agent Record architecture: per-agent
   append-only event logs bound to Ed25519 keys, checkpointed with
   signed Merkle tree heads following the RFC 6962 construction,
   countersigned by independent witnesses, and exported as portable,
   offline-verifiable dossiers.  Memory integrity is anchored by hash
   commitments recorded in the log, allowing an agent's future sessions,
   and any third party, to detect tampering with persisted state.  The
   architecture is deployed in production at a founding registry; this
   document records its wire formats and security model to invite
   independent implementation and review, and to align terminology with
   the SCITT architecture, of which this system is an application-
   specific instance.
- **draft-reilly-cts-01** (new-draft, score 16, core_identity) [none]: [Cognitive Trust Stack (CTS): A Framework for Verifiable AI Behavioral Provenance](https://datatracker.ietf.org/doc/draft-reilly-cts/) — Every artificial intelligence system deployed today operates
   under behavioral constraints that are unverifiable by any
   external party.  Alignment claims exist as documentation,
   policy statements, or terms of service -- all mutable, none
   cryptographically provable.  When an AI system causes harm,
   there is no mechanism to prove what rules it was following.
   When an organization claims its AI is safe, there is no
   standard by which that claim can be independently verified.
   This is the AI behavioral provenance problem, and no existing
   framework solves it.

   The Cognitive Trust Stack (CTS) establishes that the alignment
   state of an AI system at any point in time MUST be a verifiable
   fact, not an assertion requiring trust.  CTS defines a complete,
   implementable framework for declaring, anchoring, enforcing,
   and verifying AI behavioral constraints through a five-layer
   architecture combining: (1) a declarative alignment schema
   formatted to IETF Internet-Draft standards, (2) archival
   permanence via Digital Object Identifier (DOI) registration,
   (3) cryptographic temporal anchoring via Bitcoin blockchain
   timestamping using the Dual-Layer Digital Permanence (DLDP)
   methodology [REILLY-REM], (4) runtime retrieval injection for
   active constraint enforcement, and (5) independent third-party
   verification.

   CTS does not replace existing AI alignment techniques.  It
   provides the missing accountability layer that sits above them
   -- making alignment a cryptographically provable fact rather
   than an unverifiable claim.

   The full CTS specification, reference implementation, schema,
   and provenance manifest are published at Zenodo DOI
   10.5281/zenodo.19097169.  The priority of this framework is
   cryptographically anchored in Bitcoin block 941168
   (2026-03-18), with SHA-256 hash:
   e915b5162422281e1c0185c9e2eefaf7
   4b7f539996b878cb1e69e10533f24ac2

   The OpenTimestamps proof file
   (CTS_Whitepaper_v1.0.docx.ots), included in the Zenodo
   record, provides independent cryptographic verification of
   existence prior to block 941168.

   This revision (-01) additionally documents the function of
   CTS records as prior art records under 35 U.S.C. 102(a)(1),
   clarifies the scope of the canonical v1.0 cryptographic
   anchor (which covers the whitepaper artifact), introduces a
   normative one-hash-per-artifact anchoring rule, and corrects
   an erroneous reference to the REM Protocol draft name
   present in -00.
- **draft-bu-agentproto-security-principal-binding-05** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-ietf-stir-certificate-transparency-03** (new-draft, score 15, adjacent_watchlist) [stir]: [STI Certificate Transparency](https://datatracker.ietf.org/doc/draft-ietf-stir-certificate-transparency/) — This document describes a framework for the use of the Certificate
   Transparency (CT) protocol for publicly logging the existence of
   Secure Telephone Identity (STI) certificates as they are issued or
   observed.  This allows any interested party that is part of the STI
   ecosystem to audit STI certification authority (CA) activity and
   audit both the issuance of suspect certificates and the certificate
   logs themselves.  The intent is to establish a level of trust within
   the STI ecosystem that relies on the verification of telephone
   numbers.  This involves requiring and refusing to honor STI
   certificates that are not listed in an established log.  This
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
- **draft-schrock-ep-authorization-receipts-11** (new-draft, score 15, adjacent_watchlist) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
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
- **draft-wang-ccs-runtime-verification-00** (new-draft, score 15, core_identity) [none]: [A Runtime Verification Receipt Format for Agent Auditing](https://datatracker.ietf.org/doc/draft-wang-ccs-runtime-verification/) — The Correctover Conformance Shape (CCS) defines a tamper-evident,
   cryptographically bound receipt format that provides runtime
   verification for agent tool invocations.  Each CCS receipt captures a
   seven-dimensional verification outcome -- Structure, Schema, Latency,
   Cost, Identity, Integrity, and Security -- as a single artifact
   suitable for consumption by audit, compliance, and observability
   systems.

   CCS is designed as a pluggable runtime verification infrastructure
   layer that complements -- but does not replace -- existing and
   emerging agent protocol work at the IETF.  Specifically: (1) the
   AUDIT effort (draft-kuehlewind-audit-architecture) defines an
   auditing architecture with Action Record and Authorization Transition
   Record types; a CCS receipt provides the verifiable, tamper-evident
   evidence payload that can populate these record types with
   cryptographically bound proof of runtime governance decisions.  (2)
   The agentproto WG-forming effort (IETF 126 BoF) addresses agent-to-
   agent and agent-to-tool communication protocols; CCS provides per-
   invocation, sub-millisecond runtime verification that operates
   beneath the session/transport layer, complementing protocol-level
   context exchange with evidence-level integrity guarantees.

   Version 1.1 of the CCS receipt comprises 29 fields with full Ed25519
   signature coverage, including three causal chain fields
   (rule_version, tool_call_id, args_digest) that elevate the Integrity
   dimension from behavioral traceability to verifiable decision
   causality.  The reference implementation (ccs-verifier v1.1.0, PyPI)
   passes 154 conformance tests across all verification dimensions.

   This document specifies the CCS Receipt Schema, the Canonical
   Configuration model, the nine binding mechanisms, key management,
   transport requirements, verifier source classification, conformance
   levels, and negative test cases.  CCS is protocol-agnostic: it is not
   bound to Model Context Protocol (MCP), Agent2Agent (A2A), or any
   other specific agent protocol, and can be integrated into any runtime
   that governs tool invocations.
- **draft-ietf-wimse-workload-identity-practices-06** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-morrison-agent-channel-fan-out-01** (new-draft, score 14, core_identity) [none]: [An Agent-Channel Frame for Identity-Keyed Fan-Out Delivery to Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-agent-channel-fan-out/) — This memo specifies an application-layer frame format and a delivery
   model by which the several concurrent agentic sessions of a single
   identity-bound principal, and the recognised members of an
   organisational identity substrate, exchange short structured
   messages.  The frame, termed the agent-channel frame, is a transport
   envelope: it carries a closed-catalogue kind discriminator, a
   structured per-kind payload, an identity attribution pair, and an
   inline provenance block.  Delivery is fan-out: a sender names a
   recipient scope rather than a single endpoint, and the scope is
   expanded at delivery time against the recipient's subscriptions.
   Recipients receive frames over a per-handle Server-Sent Events stream
   and MAY narrow what they receive with a subscribe-time filter
   expression.  Frames are ephemeral routing units; the memo specifies
   only the wire envelope, the scope-expansion grammar, the subscribe
   filter grammar, and the delivery semantics.  Frame persistence, where
   an implementation chooses to retain frames for replay, is out of
   scope and is not specified.  The memo composes with the handle
   namespace of [IDPRONOUNS], the discovery surface of [MCPDNS], and the
   cross-organisational ceremony of [IDACCORD]; no new transport and no
   new handle category is introduced.
- **draft-schrock-canonical-action-identifier-02** (new-draft, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
   identify an action using format-local content and digests.  Those
   digests are not directly comparable when the formats select or encode
   material action fields differently.  This document defines the
   Canonical Action IDentifier (CAID): a typed action object, a
   canonicalization and digest suite, a compact identifier string, and
   immutable action-type definitions with required material fields.  It
   also defines an Action-Mapping Profile for projecting independently
   verified native artifacts into a common action type, with the closed
   results EQUIVALENT_UNDER_PROFILE, NOT_EQUIVALENT, and INDETERMINATE.
   CAID carries no trust semantics.  It does not establish identity,
   authority, authorization, execution, safety, or legal reliance.
- **draft-agentic-ai-usecases-requirements-01** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on multimodal communication, session
   management, discovery, communication security, agent identity and
   authentication.
- **draft-gaikwad-south-authorization-01** (new-draft, score 13, authorization) [none]: [SOUTH: Stochastic Authorization for Agent and Service Requests](https://datatracker.ietf.org/doc/draft-gaikwad-south-authorization/) — SOUTH defines an authorization protocol for evaluating requests
   issued by users, services, or autonomous agents.  SOUTH allows a
   server to return a deterministic decision or an allow decision that
   is issued with a probability determined by local policy.  This
   enables servers to incorporate uncertainty, contextual information,
   and load conditions into authorization decisions.

   SOUTH is transport independent and can be composed with existing
   authentication mechanisms such as OAuth, OpenID Connect, mutual TLS,
   or DPoP.  This document describes the request and response objects,
   decision semantics, and an HTTP binding for interoperable deployment.
- **draft-morrison-consent-settlement-04** (new-draft, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
   protocols by which the disclosure of an identity attribute about a
   human subject is bound to that subject's recorded consent and
   settled, in part, to that subject.  When an agent pays to read an
   identity attribute about a person, the extension requires that the
   read carry a reference to a scoped, revocable consent grant issued by
   the subject, and it requires that the payment's settlement
   instruction name the subject as a beneficiary of a share of the
   read's price greater than the shares of all other parties combined.
   The extension composes above an identity- attestation envelope (which
   asserts who a credential is about) and above an HTTP-native payment
   flow (which moves value for the read); it adds the two functions
   neither layer provides: consent capture at disclosure time and
   settlement to the data subject.  The wire additions are an
   advertisement in the server's payment-required response, a consent-
   grant reference echoed in the client's payment payload, and a
   settlement instruction enumerating subject beneficiary roles.  The
   extension is settlement-network-agnostic and attestation-format-
   agnostic.  The memo is Informational; the underlying COSE and CBOR
   formats are normative per [RFC9052] and [RFC8949], and the HTTP
   semantics are normative per [RFC9110].
- **draft-schrock-ae-challenge-07** (new-draft, score 13, authorization) [none]: [An Authorization Evidence Challenge for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ae-challenge/) — When a relying party refuses a consequential agent action because
   authorization evidence is missing, stale, or unverifiable, the agent
   needs a machine-readable description of what remains necessary.  This
   document defines a transport-neutral Authorization Evidence Challenge
   data model bound to the relying party's exact action.  The challenge
   identifies outstanding evidence requirements, freshness and status
   constraints, acceptable presentation profiles, and retry state.  It
   authorizes nothing, transfers no admission ownership, and provides no
   promise that a later request will execute.

   The document also defines an HTTP challenge-response carrier using
   403 Forbidden and RFC 9457 Problem Details, and describes an
   informative gateway-handoff illustration for DMSC-style federation.
   The gateway illustration communicates evidence requirements; it does
   not solve conserved admission or double-admission across
   independently operated gateways.

   A challenge can synchronize corrected retries and amplify load.  The
   core therefore defines optional retry timing with per-challenge
   jitter, and the HTTP carrier maps its lower bound to Retry-After.
   Retry timing controls presentation attempts only; it does not
   authorize the action or make an uncertain action safe to repeat.

   Single-use processing also places state on the refusal path.  The
   core therefore requires bounded outstanding and replay state, fail-
   closed behavior when state cannot be claimed, and retention of live
   replay records until they are no longer security-relevant.  Nonce
   claim and refusal-path capacity reservation are one atomic owner-side
   transition before native evidence verification, and a binding
   capacity refusal reveals no remaining evidence requirements.  In a
   sharded replay domain, only the authoritative owner can classify a
   nonce as already claimed; inability to reach that owner is
   unavailability, not replay.
- **draft-morrison-morning-brief-01** (new-draft, score 12, trust_infrastructure) [none]: [The Morning Brief: A Federated, Identity-Attested Situational-Awareness Payload](https://datatracker.ietf.org/doc/draft-morrison-morning-brief/) — This document defines the Morning Brief: a federated, identity-
   attested situational-awareness payload exchanged between
   organisations, their agents, and peer agents operating under an
   Identity Accord [ACCORD].  A Morning Brief carries a signed, bounded-
   lifetime summary of signals, escalations, decisions, and optional
   commerce quotes from one ~handle to another.  Every signal entry
   carries a provenance_class distinguishing active self-report, passive
   aggregate observation, and passive individual observation; the last
   of these is forbidden on the wire and rejected at the grammar level.
   Readers present a capability token scoped by (category,
   provenance_class) that gates release BEFORE payload emission, not
   after.  The payload is envelope-signed with COSE_Sign1 [RFC9052] over
   a JCS-canonicalised [RFC8785] representation, bound to the issuer's
   Sovereign-tier handle per [IDCOMMITS].  Briefs carry a mandatory
   not_after (default 24h) and reference a revocation endpoint
   discovered via DNS TXT per [MCPDNS].  The document defines the wire
   format only; rendering, storage, and retention are out of scope.
- **draft-norton-sdlp-obj-format-08** (new-draft, score 12, trust_infrastructure) [none]: [SDLP Object Format Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-obj-format/) — This document defines the canonical object format for the Secured
   Digital Lifecycle Protocol (SDLP). The SDLP object format specifies
   the structure, encoding, and canonicalization rules for DigitalID,
   lineage fields, lifecycle timestamps, Body content, and signature
   envelopes. These rules establish the immutable semantics required for
   SDLP verification, provenance tracking, lifecycle transitions, and
   interoperability with external systems such as CAID, AEC, AEB, SCITT,
   and EMILIA.

   Version -08 updates the canonical timestamp grammar, clarifies
   DigitalID and lineage field semantics, refines Body canonicalization
   rules, and incorporates corrections identified through SDLP Fixture
   Bundle v4 testing. This revision aligns the object format with the
   current SDLP Identity (-02), Lineage (-03), Lifecycle (-03), Security
   Architecture (-04), Architecture (-03), Overview (-01), and Physics
   Model (-00) drafts.
- **draft-verma-cirp-02** (new-draft, score 12, core_identity) [none]: [A Capability-Oriented Intent Routing Protocol](https://datatracker.ietf.org/doc/draft-verma-cirp/) — This document specifies the Capability-Oriented Intent Routing
   Protocol (CIRP), a capability-oriented protocol layer for routing
   intent between cryptographically identified endpoints across
   heterogeneous trust domains.  The protocol defines capability
   identifiers with mandatory versioning, scoped discovery across five
   visibility levels, ticket-based session authorization, negotiated
   cryptographic suites including hybrid post-quantum key establishment,
   encrypted peer-to-peer session establishment, and mutually attested
   invocation receipts with hash-chained integrity.  Payload semantics
   are opaque to the CIRP layer.

   CIRP messages are carried by transport bindings.  The initial binding
   is datagram-oriented and maps CIRP control-plane and session messages
   onto UDP.  Other bindings, including QUIC/TLS-based bindings, may be
   specified separately.

   This revision clarifies the protocol architecture in response to
   early review.  It distinguishes CIRP core semantics from transport
   bindings, separates endpoint identity from reachability locators,
   separates discovery from authorization, and introduces no wire-format
   changes.
- **draft-ztsl-secdispatch-protocol-00** (new-draft, score 12, core_identity) [none]: [Zero Trust Secure Layer (ZTSL) Protocol Specification with Opcode Framework and Application Binding Layer](https://datatracker.ietf.org/doc/draft-ztsl-secdispatch-protocol/) — This document specifies the Zero Trust Secure Layer (ZTSL) protocol,
   a transport-layer security framework that enforces Zero Trust
   principles at the protocol level by embedding continuous identity
   verification, device trust validation, policy-driven communication,
   and cryptographic session management into every protocol message.

   ZTSL introduces the First Authentication Needed (FAN) mechanism,
   Zessions (Zero Trust Sessions), the Device Trust Flag (DTF), the
   Client Security Routing Profile (CSRP), the Triple Signature Model,
   the Trust Triangle, Adaptive Protocol Negotiation, and Heartbeat
   Fingerprint (HBF) synchronization.

   This document also specifies the ZTSL Opcode Framework, a structured,
   extensible opcode namespace that encodes every protocol operation as
   a precisely identified, versioned, and trust-contextualized
   instruction.  Every FAN exchange, Zession state transition, socket
   operation, signing step, routing decision, heartbeat synchronization,
   threat event, and recovery action is assigned a unique opcode and
   transmitted as an opcode-bearing ZTSL frame.

   The document further specifies the Application Binding Layer (ABL),
   the transparent shim through which any application interacts with
   ZTSL via a familiar socket-like API, completely insulated from the
   underlying trust machinery.
- **draft-bezerra-anchors-command-provenance-01** (new-draft, score 11, core_identity) [none]: [Anchors: Post-Quantum Command Provenance for Autonomous Machine Links](https://datatracker.ietf.org/doc/draft-bezerra-anchors-command-provenance/) — Autonomous machines such as uncrewed aircraft, ground robots, and
   spacecraft execute commands issued by human operators and,
   increasingly, by AI agents.  When an incident occurs, no independent
   evidence exists of which commands the machine received: conventional
   logs are mutable by the operating party, symmetric message
   authentication codes cannot demonstrate origin to a third party, and
   records signed with elliptic-curve cryptography lose their
   evidentiary value once cryptographically relevant quantum computers
   exist.

   This document defines the Anchor: a post-quantum digital signature
   over a compact commitment to a window of authenticated machine
   traffic.  An anchor chain constitutes a tamper-evident, non-
   repudiable record of what a machine was commanded to do and what it
   reported back, verifiable by any third party without trusting the
   operator, without network access at recording time, and with security
   that survives the quantum transition.  The construction is protocol-
   agnostic and is designed for bandwidth-constrained links where per-
   message post-quantum signatures are impractical.
- **draft-brezun-human-continuity-http-00** (new-draft, score 11, core_identity) [none]: [Human Continuity for HTTP](https://datatracker.ietf.org/doc/draft-brezun-human-continuity-http/) — This document defines an HTTP extension for origins that need to
   attribute repeated participation to the same verified unique human
   within a declared continuity scope, without requiring a global human
   identifier or replacing existing authentication.  Within a continuity
   scope, the same human yields one verifier-local handle across all of
   their accounts, devices, and agents and cannot present as two,
   distinguishing the signal from authentication, which identifies a
   credential a human may hold many of.  An origin server can publish
   policy for client-presented unique-human artifacts, issue an explicit
   challenge, and receive a client-presented artifact on a subsequent
   request.

   The framework is independent of any realm operator, credential
   technology, proof system, or definition of humanness.  Companion
   profiles define artifact syntax, issuance, verification, challenge
   binding, replay behavior, holder binding, privacy properties, realm
   metadata, and verifier output.  A conforming profile produces a
   verifier-local continuity_handle scoped to a realm, attestation
   audience, and purpose.  This version defines no initial profile.
- **draft-chen-oauth-agent-authz-use-cases-02** (new-draft, score 11, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0 framework
   [RFC6749] and its common extensions.  The analysis identifies
   fundamental mismatches, the goal of this document is to articulate
   these gaps clearly, providing a foundation for future work on new
   extensions within the OAuth Working Group to address the
   authorization needs of the next generation of ai agents.
- **draft-chueayen-attestation-receipts-02** (new-draft, score 11, trust_infrastructure) [none]: [Enforcement Attestation Receipts for AI Inference Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies a compact JSON attestation receipt for an AI
   inference decision.  A receipt binds an outcome to a request hash
   under a published Ed25519 public key, so a party that does not trust
   the issuer's infrastructure can still verify offline what the
   issuer's signing key attested was decided.  The format is
   intentionally small and version-selected, so independent verifiers
   stay easy to implement and audit.  It is intended for settings where
   an operator-controlled log is not, on its own, sufficient evidence of
   the decision.
- **draft-hillier-certisyn-ai-governance-verified-02** (new-draft, score 11, trust_infrastructure) [none]: [AI Governance Verified -- A Cryptographic Verification Standard for Agentic AI Governance in Regulated Industries](https://datatracker.ietf.org/doc/draft-hillier-certisyn-ai-governance-verified/) — This document specifies a verification standard for the cryptographic
   attestation of agentic AI governance in regulated industries.  It
   defines the Verification Reconciliation Object (VRO), the issuing-
   partner framework, the eight control areas through which AI
   governance posture is reconciled, three maturity-attestation levels
   (Documented, Operational, Adversarial-ready), and the cryptographic
   continuity requirements that together produce deterministic,
   independently reconstructable, auditor-grade attestations of agentic
   AI governance.  The standard sits beneath ISO/IEC 42001:2023, the
   NIST AI Risk Management Framework, and other agentic AI governance
   frameworks, and produces the verifiable artefact those frameworks
   were designed to imply but do not deliver.
- **draft-norton-sdlp-lifecycle-03** (new-draft, score 11, core_identity) [none]: [SDLP Lifecycle Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-lifecycle/) — This document defines the SDLP Lifecycle Specification, the canonical
   state machine and transition semantics governing how SDLP objects
   evolve over time. The lifecycle model establishes deterministic rules
   for object creation, activation, transformation, and termination,
   ensuring that identity, lineage, and lifecycle metadata remain
   tamper-evident and verifiable across all implementations.

   Lifecycle-03 updates and aligns the transition grammar with
   Identity-02, Lineage-03, and Object-Format-08, providing a unified
   framework in which DigitalID is immutable, InstanceID grows
   deterministically, Lineage reflects complete ancestry, and Timestamp
   records the precise moment of each transition. The lifecycle rules
   defined in this document are normative and required for interoperable
   SDLP processing, validation, and provenance assurance.
- **draft-reilly-atlas-00** (new-draft, score 11, trust_infrastructure) [none]: [Project Atlas: A Cognitive Behavioral Provenance and Integrity (CBPI) Backbone Instrument for Autonomous Agents](https://datatracker.ietf.org/doc/draft-reilly-atlas/) — This document specifies Project Atlas, a backbone instrument in
   which a pipeline of autonomous software agents continuously holds a
   constellation of live web endpoints under measurement, attestation,
   and remediation, with every agent behavior conditioned and recorded
   under the Cognitive Behavioral Provenance and Integrity (CBPI)
   framework [I-D.reilly-cbpi].  Atlas defines eight agent roles
   (Resolver, Reachability, Integrity, Provenance, Conditioning
   Authority, Drift, Functional Behavior Assessment, and Sentinel), a
   hash-linked Operant Provenance Chain of epochs, hash-linked
   Reinforcement Event Records, a per-agent Behavioral Drift Index, and
   a dual authority model in which the instrument operates either fully
   autonomously or under human oversight through an operator decision
   queue.  A live reference instrument implementing this document is
   deployed and publicly reachable.
- **draft-correctover-ccs-02** (new-draft, score 10, authorization) [none]: [Correctover Conformance Shape (CCS): A Receipt and Binding Specification for Agent Runtime Verification](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — The Correctover Conformance Shape (CCS) defines a tamper-evident
   receipt schema and a set of cryptographic bindings that together
   constitute a verifiable conformance record for an agent runtime's
   decision to permit, deny, or escalate a tool invocation.  CCS is
   designed as a one-receipt-per-invocation object that can be consumed
   by an executor-side Action Evidence Boundary (AEB), providing the
   request_hash, response_hash, runtime_context_hash, action binding,
   params_hash binding, issuer, audience, nonce/sequence, freshness, and
   config_hash fields that the AEB processing model requires as native
   inputs.
   This document specifies the CCS Receipt Schema, the Canonical
   Configuration model, the nine binding mechanisms, key management,
   transport requirements, verifier source classification, conformance
   levels, and negative test cases.  It is intended to enable a reader
   such as the author of the Action Evidence Boundary specification to
   evaluate whether and how a CCS receipt can be mapped into an
   Authorization Evidence Chain (AEC) component.
- **draft-dunbar-dmsc-gw-scenarios-gap-analysis-03** (new-draft, score 10, agent_identity) [none]: [Deployment Scenarios and Gap Analysis for AI Agent Gateway](https://datatracker.ietf.org/doc/draft-dunbar-dmsc-gw-scenarios-gap-analysis/) — This document examines deployment scenarios for AI agent
   collaboration and analyzes the circumstances under which AI
   Agent Gateway functions provide operational or
   interoperability benefits that cannot be achieved through
   direct agent-to-agent communication alone. The document
   considers both single-domain and multi-domain deployments,
   identifies specific challenges associated with each
   deployment model, evaluates the limitations of existing agent
   communication mechanisms (including MCP and A2A) with respect
   to those challenges, and demonstrates that gateway functions
   are necessary in deployments involving multiple tenants,
   multiple vendors, or multiple administrative domains.
- **draft-svensson-credential-oidc-bridge-01** (new-draft, score 10, verifiable_claims) [none]: [Credential Presentation to OIDC Claims Bridge](https://datatracker.ietf.org/doc/draft-svensson-credential-oidc-bridge/) — This document defines a mechanism for conveying digital credential
   claims via OpenID Connect (OIDC).  It specifies how an OpenID
   Provider (OP) that collects credentials from a wallet can expose
   those claims to Relying Parties as standard OIDC claims, enabling
   existing OIDC deployments to consume digital credentials without
   implementing any wallet-facing presentation protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/masv3971/rfc_credential_oidc_bridge.
- **draft-wendt-stir-vesper-10** (new-draft, score 10, core_identity) [none]: [VESPER - Verifiable STI Presentation and Evidence for RTU](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper/) — This document defines VESPER (Verifiable STI Presentation and
   Evidence for RTU), a profile for the use of delegate certificates in
   STIR.  VESPER profiles the binding of telephone number authority to a
   domain identifier, the STIR certificate and PASSporT specifications,
   ACME-based authority token issuance, and certificate transparency
   into a delegate certificate that associates the right-to-use for a
   telephone number with the entity behind the number asserted in the
   PASSporT orig claim.  This document describes the certificate usage,
   a PASSporT usage profile for SIP signaling, and a portable Right-to-
   Use Token for use outside of SIP.
- **draft-zehavi-oauth-authz-req-del-chain-00** (new-draft, score 10, authorization) [none]: [OAuth Authorization Request Delegation Chain](https://datatracker.ietf.org/doc/draft-zehavi-oauth-authz-req-del-chain/) — Brokered OAuth redirect authorization requests involve intermediary
   authorization servers between a downstream client and the upstream
   authorization server that obtains user consent and issues tokens.
   Such deployments have security risks because the upstream
   authorization server sees only the immediate OAuth client and is
   unaware of the downstream client or intermediary brokers obtaining
   its response.

   This document defines an informative OAuth 2.0 profile for carrying a
   verifiable, signed authorization request delegation chain as a RAR
   authorization_details object [RFC9396].  Each node in the chain is a
   JSON object signed by the attesting authorization server or broker
   using detached JWS [RFC7515], attesting its validated client, hash-
   linked to the previous node, allowing the upstream authorization
   server to validate the exact delegation path before issuing tokens.

   This document does not define new OAuth endpoints, grant types, error
   codes, token formats, token response parameters, or token request
   parameters.
- **draft-ferro-dnsop-apertoid-01** (new-draft, score 9, agent_identity) [none]: [ApertoID: DNS-Based Agent Identity Declaration Protocol](https://datatracker.ietf.org/doc/draft-ferro-dnsop-apertoid/) — This document defines ApertoID, a DNS-based protocol that enables
   domain owners to declare authorized AI agents acting on their behalf,
   publish cryptographic keys for agent identity verification, and
   specify enforcement policies for unauthorized agents.  ApertoID uses
   existing DNS TXT records under the "_apertoid" underscore-scoped
   domain name to provide a decentralized, standards-based mechanism for
   AI agent identity declaration and verification.

   ApertoID defines two record types: a Policy Record analogous to DMARC
   that specifies domain-level enforcement behavior, and Agent
   Declaration Records analogous to DKIM key records that bind agent
   endpoints to Ed25519 public keys with mandatory expiration.  A
   companion document [APERTOID-SIG] defines the HTTP request signing
   mechanism that enables agents to cryptographically prove their
   identity on each request.
- **draft-ferro-httpbis-apertoid-sig-01** (new-draft, score 9, agent_identity) [none]: [ApertoID-Signature: HTTP Request Signing for AI Agent Identity](https://datatracker.ietf.org/doc/draft-ferro-httpbis-apertoid-sig/) — This document defines the ApertoID-Signature HTTP header field, which
   enables AI agents to cryptographically prove their identity on each
   HTTP request.  The agent signs the request method, target URL, body
   hash, and identity metadata using an Ed25519 private key whose
   corresponding public key is published in DNS via the ApertoID
   protocol [APERTOID-DNS].  The mechanism provides request-level
   identity verification, action binding (the signature is tied to the
   specific method and URL), and replay protection via timestamps and
   nonces.
- **draft-ietf-acme-device-attest-10** (new-draft, score 9, core_identity) [acme]: [Automatic Certificate Management Environment (ACME) Device Attestation Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-device-attest/) — This document specifies new identifiers and a challenge for the
   Automatic Certificate Management Environment (ACME) protocol which
   allows validating the identity of a device using attestation.  This
   document updates RFC 8555 to enable a privacy-preserving mode for the
   identifiers defined in this document.
- **draft-ietf-oauth-rfc8725bis-09** (new-draft, score 9, core_identity) [oauth]: [JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc8725bis/) — JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security
   tokens that contain a set of claims that can be signed and/or
   encrypted.  JWTs are being widely used and deployed as a simple
   security token format in numerous protocols and applications, both in
   the area of digital identity and in other application areas.  This
   Best Current Practices (BCP) specification updates RFC 7519 to
   provide actionable guidance leading to secure implementation and
   deployment of JWTs.

   This BCP specification furthermore obsoletes the existing JWT BCP
   specification RFC 8725 to provide additional actionable guidance
   covering threats and attacks that have been discovered since RFC 8725
   was published.
- **draft-schrock-model-to-matter-04** (new-draft, score 9, authorization) [none]: [Model-to-Matter: Authorization and Outcome Evidence for Model-Directed Physical Execution](https://datatracker.ietf.org/doc/draft-schrock-model-to-matter/) — Advanced models can propose operations that produce physical effects.
   Model-to-Matter defines an executor-owned profile that composes
   model, safety, institutional, domain, screening, human, and physical-
   state attestation evidence over one canonical action before single-
   use execution.  This revision also profiles post-execution Outcome
   Binding.  An executor effect statement remains one source claim;
   required independent observers sign separately bound observations.
   Missing outcome evidence is indeterminate, not success or failure.
   The profile standardizes evidence custody and reconciliation; it does
   not perform screening, determine scientific safety, certify a
   facility, or establish physical truth.
- **draft-gravit-verifiable-epistemic-decision-00** (new-draft, score 8, adjacent_watchlist) [none]: [Gravit Verifiable Epistemic Decision Standard](https://datatracker.ietf.org/doc/draft-gravit-verifiable-epistemic-decision/) — This document defines the normative requirements for the Gravit
   decision-making system.  Gravit's core principle is to base all
   definitive decisions exclusively on verifiable epistemic grounds.
   This specification establishes mandatory rules for evidence
   admissibility, epistemic classification, traceability, failure
   handling, auditability, and security in adversarial environments,
   including a taxonomy of admissible evidence and failure outcomes, a
   required Decision Record format, and an explicit threat model with
   corresponding verification mechanisms.  The goal is to ensure that
   all decisions are reproducible, auditable, and resistant to
   manipulation, thereby fostering trust and accountability in
   distributed and high-stakes settings.
- **draft-hardt-oauth-aauth-protocol-10** (new-draft, score 8, core_identity) [none]: [AAuth Protocol](https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/) — This document defines the AAuth authorization protocol for agent-to-
   resource authorization and identity claim retrieval.  The protocol
   supports four resource access modes — identity-based, resource-
   managed (two-party), PS-asserted (three-party), and federated (four-
   party) — with agent governance as an orthogonal layer.  It builds on
   the HTTP Signature Keys specification
   ([I-D.hardt-httpbis-signature-key]) for HTTP Message Signatures and
   key discovery.
- **draft-hillier-certisyn-essential-eight-verified-02** (new-draft, score 8, trust_infrastructure) [none]: [Essential Eight Verified -- A Cryptographic Verification Standard for the ACSC Essential Eight Maturity Model](https://datatracker.ietf.org/doc/draft-hillier-certisyn-essential-eight-verified/) — This document specifies a verification standard for the cryptographic
   attestation of conformance to the Australian Cyber Security Centre
   (ACSC) Essential Eight Maturity Model.  It defines the Verification
   Reconciliation Object (VRO), the issuing-partner framework, the
   evidence categories required for each of the eight controls of the
   Essential Eight, the three maturity-attestation levels, and the
   cryptographic continuity requirements that together produce
   deterministic, independently reconstructable, auditor-grade
   attestations of cybersecurity posture.  The standard sits beneath the
   ACSC Essential Eight Maturity Model and produces the verifiable
   artefact the model was designed to imply but does not deliver.
- **draft-morrison-mcp-tool-surface-names-registry-01** (new-draft, score 8, core_identity) [none]: [An IANA Registry for Model Context Protocol Tool Surface Names](https://datatracker.ietf.org/doc/draft-morrison-mcp-tool-surface-names-registry/) — This document requests the establishment of an IANA registry for
   Model Context Protocol [MCP-SPEC] tool surface names.  A tool surface
   name is the wire-level identifier by which a client invokes a typed
   capability on an MCP server.  Existing Morrison- family Internet-
   Drafts ([ORGALTER]) request IANA registration of specific surface
   names against a registry that does not yet exist.  This document
   establishes the registry mechanism so that subsequent specifications
   can register names without restating the registry's structure or
   registration procedure.

   The registry uses Specification Required registration with a
   Designated Expert pool [RFC8126].  Initial contents are the four
   surface names registered by [ORGALTER].  Vendor-prefix conventions
   are recommended but not mandated.
- **draft-morrison-substrate-provenance-grammar-01** (new-draft, score 8, trust_infrastructure) [none]: [Substrate-Provenance Annotation Grammar for Large-Language-Model Output](https://datatracker.ietf.org/doc/draft-morrison-substrate-provenance-grammar/) — This memo specifies a wire-level annotation grammar by which a large-
   language-model output may carry, at emission and at the granularity
   of an individual assertion, a provenance label drawn from a closed
   enumerated vocabulary of substrate-class identifiers.  The memo
   defines the closed vocabulary, the per-assertion attachment form, the
   admissibility discipline a relying party MAY apply to the labels, and
   two terminal output states, UNVERIFIED-INFERENCE and DECAYED-TO-
   UNCERTAINTY, equal-rank with assertion and denial.  The memo does not
   specify what an inference system MUST do; it specifies the wire
   grammar by which a relying party may inspect what the inference
   system DID with respect to the substrates it consulted.  The memo is
   Informational.
- **draft-acosta-crypto-agility-manifest-01** (new-draft, score 7, trust_infrastructure) [none]: [A Well-Known URI and JSON Format for Publishing Cryptographic Posture (the Crypto-Agility Manifest)](https://datatracker.ietf.org/doc/draft-acosta-crypto-agility-manifest/) — This document defines a discoverable, machine-readable JSON document,
   the crypto-agility manifest, that a website or source repository
   publishes at the well-known URI "/.well-known/crypto-agility.json" to
   declare its cryptographic posture: a readiness summary, a compact
   Cryptography Bill of Materials (CBOM) summary, an optional link to a
   posture attestation, the migration policy it measures itself against,
   and an optional self-declared conformance statement with justified
   exceptions.  The manifest lets an automated consumer, such as an AI
   coding agent, a continuous-integration bot, or an auditor's tool,
   discover a project's crypto posture the way it already discovers a
   security contact from "security.txt".  The manifest is a public,
   self-reported claim; it is not a proof.  It is intended to
   complement, not replace, a full CBOM inventory, serving as the CBOM's
   public-facing discovery counterpart.

   This document is a proposal.  It is not an IETF product and is not a
   standard of any kind.
- **draft-schrock-ep-bounded-capability-receipts-04** (new-draft, score 7, authorization) [none]: [Bounded Capability Receipts and Durable Spend Control for Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-capability-receipts/) — Agents sometimes need bounded authority to perform more than one
   consequential action without obtaining a new human approval for every
   operation.  A signed token alone cannot enforce a shared budget
   across replicas, survive retries safely, or distinguish an operation
   that never crossed an effect boundary from one whose outcome is
   unknown.

   This document defines a bounded capability receipt and a durable
   reserve-execute-commit protocol.  The receipt binds an issuance
   authorization, a closed action scope, a budget with explicit units, a
   holder proof, an expiry, and any parent capability.  The state
   protocol atomically refuses overspend and operation-key replay,
   fences concurrent owners, and charges an indeterminate operation when
   an external effect may have occurred.  Delegation transfers rather
   than copies authority: all direct child allocations are funded by
   committed parent operations before child registration, and their
   aggregate cannot exceed the parent balance within one authoritative
   atomic state domain.  It also defines narrowing-only delegation,
   explicit revocation inheritance for delegated authority, and evidence
   interfaces.  It does not make a bearer token into human approval,
   does not provide cross-domain or offline global double-spend
   prevention, and does not claim that an authorized action was safe,
   lawful, or successfully executed.
- **draft-wallace-aipref-grant-binding-01** (new-draft, score 7, verifiable_claims) [none]: [A Verifiable-Credential Binding for AI Usage Preferences: Expressing Grants that Lift AIPREF Preferences](https://datatracker.ietf.org/doc/draft-wallace-aipref-grant-binding/) — The AI Preferences (AIPREF) vocabulary lets those with rights in a
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

## Monitor

- **draft-gaikwad-llm-benchmarking-terminology-01** (new-draft, score 6, agent_identity) [none]: [Benchmarking Terminology for Large Language Model Serving](https://datatracker.ietf.org/doc/draft-gaikwad-llm-benchmarking-terminology/) — This document defines terminology for benchmarking the performance of
   Large Language Model (LLM) inference serving systems.  It establishes
   a shared vocabulary for latency, throughput, resource utilization,
   and quality metrics applicable to inference engines, application
   gateways, and compound agentic systems.  This document defines
   terminology only and does not prescribe benchmark methodologies or
   acceptance thresholds.
- **draft-martinalli-open-purchase-receipts-00** (new-draft, score 6, trust_infrastructure) [none]: [attest: Portable, Offline-Verifiable Digital Purchase Receipts](https://datatracker.ietf.org/doc/draft-martinalli-open-purchase-receipts/) — This document specifies attest, a signed digital purchase-receipt
   envelope that a buyer holds and that any party can verify offline,
   without contacting the issuer or any third-party service.  It defines
   the receipt envelope and payload format, a restricted JSON
   canonicalization profile ("attest-JCS", built on RFC 8785), a pinned
   Ed25519 signature ruleset, an optional hybrid Ed25519+ML-DSA-65 post-
   quantum-resistant signature profile, issuer key and artifact
   manifests with rotation and compromise handling, a layered
   verification algorithm, and revocation-record semantics.  This
   document is a snapshot profile: it distills, and never supersedes,
   the living attest specification maintained in the attest source
   repository.  It normatively specifies exactly the core receipt format
   and the hybrid signature profile; the living specification's
   transparency-log, anchoring, and issuer-mediated transfer material is
   summarized only as non-normative pointers in Section 12 of this
   document.
- **draft-morrison-org-alter-policy-provision-02** (new-draft, score 6, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
   bound at instantiation to a principal identity handle, resolves at
   session initialisation a target organisational identity substrate
   from a manifest source bound to the runtime's working context and
   retrieves from that substrate a typed policy stack comprising a
   handbook artefact, a standard-operating-procedure registry pointer,
   an enforcement-gate specification, and an audit-signal ingestion
   endpoint.  The policy stack is then applied as runtime constraints on
   subsequent tool invocations, with audit signals emitted back to the
   same substrate.  Policy provision occurs in the same act of session
   initialisation as principal identification, rather than as a separate
   ceremony against a side-channel governance plane.  A principal
   concurrently bound to multiple organisational substrates operates the
   runtime under a deterministic composition of the several policy
   stacks, with cross-organisational residual conflicts routed to the
   peer-protocol Identity Accord ceremony [IDACCORD] rather than to a
   meta-federation authority.  The memo is Informational.  The wire
   surface relies on the DNS-based discovery of [MCPDNS] and the handle
   namespace of [IDPRONOUNS]; no new transport is introduced.
- **draft-morrison-substrate-observation-02** (new-draft, score 6, core_identity) [none]: [Substrate-Observation as an Alternative to Envelope Coordination for Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-substrate-observation/) — This memo articulates a coordination-protocol anti-pattern observed
   in cross-tool agentic systems and describes a substrate-observation
   alternative that does not require negotiating a wire format between
   heterogeneous concurrent sessions of an identity-bound principal.
   The memo is Informational.  No protocol element is being proposed for
   standardisation; the contribution is the opposite, a delineation of
   what should NOT be standardised, and why, with a reference to the
   substrate-physics primitives that take its place.  Companion memos in
   the morrison-* family describe the identity primitives this memo
   presumes; specifically, this memo relies on the ~handle namespace
   established in [IDPRONOUNS] and the per-principal identity substrate
   referenced in [IDACCORD].
- **draft-ruvalcaba-hctp-00** (new-draft, score 6, core_identity) [none]: [The Hash-Chain Context Transfer Protocol (HCTP)](https://datatracker.ietf.org/doc/draft-ruvalcaba-hctp/) — The Hash-Chain Context Transfer Protocol (HCTP) is a payload format
   and synchronization protocol for incrementally transferring an
   ordered, append-only sequence of conversational context between two
   endpoints over a bandwidth-constrained channel.  Acknowledged history
   is represented by a single fixed-size rolling hash commitment (the
   "static root"); only not-yet-acknowledged context blocks (the
   "dynamic window") are transmitted.  As a result, the per-message wire
   overhead attributable to history is constant and independent of the
   total number of previously acknowledged turns.  HCTP is transport-
   agnostic and carries no confidentiality or peer authentication of its
   own; it is intended to run over a secure transport.  This document
   specifies the HCTP data model, wire format, rolling-root computation,
   and synchronization state machine.
- **draft-wendt-stir-tn-domain-binding-01** (new-draft, score 6, core_identity) [none]: [Binding a Domain Identifier to Telephone Number Authority in STIR Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-tn-domain-binding/) — This document defines a mechanism for binding a domain identifier to
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
- **draft-zehavi-oauth-rar-metadata-06** (new-draft, score 6, authorization) [none]: [OAuth 2.0 RAR Metadata and Error Remediation](https://datatracker.ietf.org/doc/draft-zehavi-oauth-rar-metadata/) — OAuth 2.0 Rich Authorization Requests (RAR) [RFC9396] standardizes
   the exchange and processing of authorization details but does not
   define metadata for describing authorization details types.

   In addition, no interoperable guidance is offered to clients, to
   remediate failures by resource servers due to insufficient
   authorization details.

   This document addresses this interoperability challenge, allowing
   clients to dynamically discover metadata instead of relying on out-
   of-band agreements, as well as standardizes failure signaling
   including interoperable remediation when insufficient authorization
   details are the cause of failure.
- **draft-cmcc-tcp-sro-00** (new-draft, score 5, core_identity) [none]: [The Session Recovery Option (SRO) for TCP](https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/) — This document defines the Session Recovery Option (SRO) for TCP.  SRO
   improves the reliability of SNAT and LB services and simplifies the
   implementation of elastically scaling SNAT/LB clusters.  SRO enables
   a client and a server to exchange their identifiers during connection
   establishment.  When a session needs to be recovered, an endpoint
   conveys the identifier of the peer to the network node, which uses it
   to locate the endpoint holding the session backup and recover the
   session.  SRO is optional: endpoints that do not support it behave as
   if the option did not exist.
- **draft-gaikwad-aps-profile-01** (new-draft, score 5, core_identity) [none]: [Agent Persistent State Profile](https://datatracker.ietf.org/doc/draft-gaikwad-aps-profile/) — Autonomous agents increasingly maintain durable persistent state
   containing user preferences, embedding vectors, safety logs,
   intermediate reasoning steps, and audit traces.  Today, agent
   frameworks treat storage as a generic file system, while storage
   administrators treat agents as stateless virtual machines.  This
   "layer mismatch" leads to fragility, poor performance, and privacy
   risks.

   The Agent Persistent State (APS) Profile defines an experimental,
   vendor-neutral storage service class for durable agent state.  APS
   emphasizes *compliance*: ensuring that memory associated with a
   specific user or agent identity can be retained, audited, and
   cryptographically erased.  APS also addresses high-frequency small I/
   O, vector index workloads, crash consistency, and Kubernetes/CSI
   [CSI] integration.

   APS introduces a Usage Class ("AgentPersistentState"), a versioned
   PersistentStateLineOfService schema, guidance for container
   orchestration systems, non-normative bindings for Swordfish
   [Swordfish] and Redfish [Redfish], and considerations for multi-
   tenancy.  APS is intended as an Experimental RFC to gather
   implementation feedback prior to any standards-track work.
- **draft-gaikwad-woa-01** (new-draft, score 5, agent_identity) [none]: [The Web of Agents (WoA)](https://datatracker.ietf.org/doc/draft-gaikwad-woa/) — This document defines the Web of Agents (WoA), a minimal JSON based
   description format and invocation convention that allows HTTP hosts
   to advertise AI agents and for clients to invoke those agents in a
   uniform way.  A WoA document is typically served from a well known
   location on an HTTP origin and uses JSON Schema to describe agent
   inputs and outputs.  WoA does not define a discovery protocol itself
   but is designed to be used as a host level primitive by higher level
   discovery systems.
- **draft-gravit-gevp-07** (new-draft, score 5, trust_infrastructure) [none]: [Gravit Epistemic Verification Protocol (GEVP)](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — GEVP defines a minimal protocol for epistemic convergence.  Renamed
   from VCP to avoid collision with draft-kamimura-scitt-vcp.  Invariant
   C_manip > C_val*2.0 as engineering heuristic.  Theta 0.73
   RECOMMENDED, pinned 7755f53.  Architecture stable per
   https://github.com/GravitOpenNetwork/gravit-canon.  This revision
   adds a formal mapping between GEVP's Epistemic State Machine and the
   evidence taxonomy defined in the Gravit Verifiable Epistemic Decision
   Standard (VEDS).
- **draft-meunier-webbotauth-httpsig-protocol-01** (new-draft, score 5, core_identity) [none]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-morrison-identity-attributed-commits-02** (new-draft, score 5, core_identity) [none]: [Identity-Attributed Git Commits via Tier-Structured Trailers](https://datatracker.ietf.org/doc/draft-morrison-identity-attributed-commits/) — This document defines a git commit trailer grammar for identity-
   attributed contributions using the ~handle identity primitive defined
   in [MCPDNS].  The grammar binds sovereign actors, automated bots, and
   AI instruments to specific commits via three tier-structured trailers
   (Acted-By, Executed-By, Drafted-With) and three optional
   cryptographic trailers (Identity-Signature, Identity-Key-Id,
   Identity-Anchor).  The signature is computed with Ed25519 over the
   commit's tree hash rather than its commit hash, preserving
   attribution across rebase, cherry-pick, and squash merge operations.
   Conformant parsers reject cross-tier category errors (e.g., an
   Instrument-tier handle in an Acted-By slot) as malformed.  The
   mechanism is provider-neutral, depends only on DNS [RFC1035] and the
   ~handle resolution algorithm of [MCPDNS], and requires no central
   authority or platform-specific verification service.
- **draft-jacobs-web4-federation-architecture-00** (new-draft, score 4, core_identity) [none]: [Web4 Federation Architecture Model](https://datatracker.ietf.org/doc/draft-jacobs-web4-federation-architecture/) — This document describes a generic architectural model for Web4
   federations, as defined in [JACOBS-TERM], covering node admission,
   tiering, gateway-mediated inter-node transport, and operational
   health verification.  It generalizes patterns observed in a live,
   operating multi-node federation, offered as a Reference
   Implementation under the terminology of [JACOBS-TERM], without
   specifying vendor-internal computational, cryptographic, or
   coordinate mechanisms.
- **draft-ling-sidrops-rov-tag-profile-02** (new-draft, score 4, trust_infrastructure) [none]: [A Profile for ROV Deployment Transparency](https://datatracker.ietf.org/doc/draft-ling-sidrops-rov-tag-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for ROV Deployment Transparency (ROV_TAG) objects for
   use with the Resource Public Key Infrastructure (RPKI).  An ROV_TAG
   is a digitally signed object through which an Autonomous System (AS)
   that has deployed Route Origin Validation (ROV) can declare its ROV
   deployment status.  When validated, an ROV_TAG's eContent can be used
   by ASes to identify which ASes have deployed ROV, enabling path
   selection decisions when hijacked routes are detected; see Section 3.
- **draft-morrison-identity-pronouns-02** (new-draft, score 4, core_identity) [none]: [Identity Pronouns: A Reference-Axis Extension to ~handle Identity Systems](https://datatracker.ietf.org/doc/draft-morrison-identity-pronouns/) — This document defines an identity pronoun grammar as a reference axis
   orthogonal to the ~handle identity tier taxonomy defined in [MCPDNS]
   and [IDCOMMITS].  A pronoun is a session-scoped reference that
   resolves client-side to a concrete handle using local session state
   before any cryptographic, DNS, or federation operation.  The entity-
   class taxonomy (Sovereign, Bot, Instrument) is unchanged; this
   specification introduces Absolute vs Pronoun as an orthogonal axis.
   A pronoun MUST NOT appear in a capability token, in a DNS record, in
   an Accord signature, or in any inter-organisational protocol payload.
   The reference implementation defines a single Wave-1 pronoun, ~org,
   that resolves to the concrete handle of the organisation bound to the
   caller's current session.  An appendix defines a relative-path
   pronoun grammar (e.g. ~./architect, ~../weaver) as a non-normative
   design surface for future work.  The mechanism is provider-neutral,
   introduces no new cryptographic primitive, and imposes zero new load
   on DNS, capability-token issuers, or federated resolvers.

## Adjacent / watchlist

- **draft-ackerman-temporal-integrity-metadata-01** (new-draft, score 3, trust_infrastructure) [none]: [Temporal Integrity Metadata (TIM) for Infrastructure Telemetry](https://datatracker.ietf.org/doc/draft-ackerman-temporal-integrity-metadata/) — Distributed computing systems generate timestamped events from
   components whose clocks operate under fundamentally different
   synchronization conditions.  Existing logging and observability
   standards -- including legacy BSD syslog (RFC 3164), RFC 5424,
   SNMP, NETCONF, and OpenTelemetry -- define message formats and
   telemetry schemas but provide no standard mechanism for an event
   source to declare the provenance, confidence, or synchronization
   state of its timestamps.  Every platform that must correlate events
   across components independently invents a proprietary temporal
   reconciliation layer.  These systems fail silently, cannot be
   validated against a published standard, and are not interoperable.

   This document defines Temporal Integrity Metadata (TIM): a transport-
   agnostic structure that any event-emitting system may attach to its
   telemetry to declare how its timestamp was generated, the
   synchronization state of its clock, a bounded uncertainty interval,
   the temporal reference domain, and a monotonic sequence token for
   ordering events when wall-clock time is unavailable.  TIM is
   backward-compatible with existing protocols, implementable on
   constrained embedded hardware, and applicable from internet-scale
   distributed services to air-gapped and orbital deployments.
- **draft-bezerra-relay-auth-transparency-01** (new-draft, score 3, core_identity) [none]: [Authentication-Transparent Protocol Extensions in Middleware-Relayed Systems](https://datatracker.ietf.org/doc/draft-bezerra-relay-auth-transparency/) — Protocol-aware middleware (relays, bridges, gateways) re-serializes
   messages at their protocol frame boundary, silently discarding any
   bytes appended outside that boundary.  Authentication material placed
   after the frame boundary by a sender is therefore stripped at every
   relay hop before reaching the receiver, with no error indication.
   This document identifies this behavior as a protocol design
   vulnerability class -- "relay-transparent authentication stripping"
   -- demonstrates it with running code in three independent protocol
   stacks (MAVLink v2, ROS2/DDS CDR, and CAN/ISO-TP with a SecOC-unaware
   gateway), and specifies the architectural principle that
   authentication material must be carried as a first-class,
   independently addressable protocol unit to survive relay transit.
   Post-quantum signature sizes push authentication out of fixed fields
   and so create the precondition systematically; this revision reports
   three measured cases where they do not, because a transport that
   refuses to carry the oversized unit produces a loss of availability
   instead of a silent authentication bypass.
- **draft-eastlake-dnssd-rfc2931bis-sigzero-03** (new-draft, score 3, core_identity) [none]: [Domain Name System (DNS) Public Key Based Request and Transaction Authentication (SIGZERO, SIG(0))](https://datatracker.ietf.org/doc/draft-eastlake-dnssd-rfc2931bis-sigzero/) — This document specifies the SIGZERO and SIG(0) Domain Name System
   (DNS) Resource Records (RRs) which provide public key based
   authentication of DNS requests and transactions.  SIGZERO is the
   RECOMMENDED option.  This document obsoletes RFC 2931.
- **draft-fraire-spacerg-constellation-registry-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Registry of Announced, Filed and Deployed Satellite Constellations](https://datatracker.ietf.org/doc/draft-fraire-spacerg-constellation-registry/) — Aggregate figures for the number of satellites planned for low Earth
   orbit are widely quoted and rarely traceable.  They mix quantities
   that are not comparable: satellites already in orbit, satellites a
   national regulator has authorised, satellites applied for and not yet
   granted, and satellites that exist only in an announcement.  For a
   single system these can differ by orders of magnitude.  Which one a
   headline figure refers to decides whether it describes infrastructure
   or intent.

   This document describes a community-maintained registry that keeps
   the four apart and requires every number in it to carry a citation
   and an evidence grade.  It sets out the data model, the taxonomy of
   regulatory commitment, the rules that separate primary regulatory
   sources from secondary reporting, and the criteria for inclusion.
- **draft-gaikwad-llm-benchmarking-methodology-01** (new-draft, score 3, adjacent_watchlist) [none]: [Benchmarking Methodology for Large Language Model Serving](https://datatracker.ietf.org/doc/draft-gaikwad-llm-benchmarking-methodology/) — This document defines benchmarking methodologies for Large Language
   Model (LLM) inference serving systems.  It provides test procedures,
   setup parameters, measurement specifications, and reporting formats
   for evaluating latency, throughput, scheduling, and resource
   management characteristics.  This document is a companion to
   "Benchmarking Terminology for Large Language Model Serving" and
   SHOULD be consulted alongside that terminology document.
- **draft-gaikwad-llm-benchmarking-profiles-01** (new-draft, score 3, adjacent_watchlist) [none]: [Performance Benchmarking Profiles for Large Language Model Serving Systems](https://datatracker.ietf.org/doc/draft-gaikwad-llm-benchmarking-profiles/) — This document defines performance benchmarking profiles for Large
   Language Model (LLM) serving systems.  Profiles bind the terminology
   defined in draft-gaikwad-llm-benchmarking-terminology and the
   procedures described in draft-gaikwad-llm-benchmarking-methodology to
   concrete architectural roles and workload patterns.  Each profile
   clarifies the System Under Test (SUT) boundary, measurement points,
   and interpretation constraints required for reproducible and
   comparable benchmarking.

   This document specifies profiles only.  It does not define new
   metrics, benchmark workloads, or acceptance thresholds.
- **draft-gaikwad-llm-fault-detection-methodology-00** (new-draft, score 3, adjacent_watchlist) [none]: [Benchmarking Methodology for Output Behavior Fault Detection in Large Language Model Serving Systems](https://datatracker.ietf.org/doc/draft-gaikwad-llm-fault-detection-methodology/) — This document defines test procedures for characterizing the fault
   detection capability of observability systems that monitor Large
   Language Model (LLM) serving deployments.  Procedures are given for
   Detection Latency, Detection Coverage, Detection Threshold Magnitude,
   False Detection Rate, and Boundary Masking.

   The Detector Under Test is the observability system.  Output Behavior
   Faults are injected at a known time under controlled conditions,
   which makes detection latency directly measurable.

   This document is a companion to "Benchmarking Terminology for Output
   Behavior Fault Detection in Large Language Model Serving Systems" and
   is to be read alongside it.  This document specifies no acceptance
   thresholds.
- **draft-gaikwad-llm-fault-detection-terminology-00** (new-draft, score 3, adjacent_watchlist) [none]: [Benchmarking Terminology for Output Behavior Fault Detection in Large Language Model Serving Systems](https://datatracker.ietf.org/doc/draft-gaikwad-llm-fault-detection-terminology/) — This document defines terminology for benchmarking the fault
   detection capability of observability systems that monitor Large
   Language Model (LLM) serving deployments.  It defines terms for
   injectable output behavior fault classes, for the detection events
   and latency intervals those faults produce, and for the coverage and
   accuracy characteristics of the detector under test.

   The System Under Test is the observability system, and not the
   language model.  Faults are injected at a known time under controlled
   conditions, which makes detection latency measurable in a way it is
   not in production.

   This document defines terminology only.  A companion document defines
   the corresponding methodology.  This document specifies no test
   procedures, no acceptance thresholds, and no service-level
   objectives.
- **draft-gaikwad-llm-incident-metrics-terminology-00** (new-draft, score 3, adjacent_watchlist) [none]: [Terminology for Reporting Output Behavior Incidents in Large Language Model Services](https://datatracker.ietf.org/doc/draft-gaikwad-llm-incident-metrics-terminology/) — This document defines terminology for reporting incidents in Large
   Language Model (LLM) services in which output behavior departs from
   intended behavior without producing an error response.  It defines
   the lifecycle events of such an incident, the intervals between those
   events, and the qualifiers a reported interval carries.

   The intervals defined here are anchored at the point information
   about an occurrence reaches a responsible party.  The interval
   preceding the first monitoring signal is named and is not defined as
   measurable.

   This document defines terminology only.  It specifies no data model,
   no reporting obligations, and no target values.
- **draft-hko-openpgp-identifiers-for-legacy-devices-01** (new-draft, score 3, core_identity) [none]: [Shortened OpenPGP identifiers for legacy hardware devices](https://datatracker.ietf.org/doc/draft-hko-openpgp-identifiers-for-legacy-devices/) — This document describes an approach for storing a shortened
   fingerprint-based identifier for OpenPGP private key material on
   hardware security devices.
- **draft-huang-spring-pppoe-srv6-01** (new-draft, score 3, core_identity) [none]: [SRv6 for PPPoE Transport](https://datatracker.ietf.org/doc/draft-huang-spring-pppoe-srv6/) — This document proposes a method that employs SRv6 underlay tunnel to
   transport PPPoE session information across broadband networks.  By
   leveraging the programmability of SRv6 SIDs, the approach not only
   delivers trusted authentication and secure subscriber access, but
   also enables operators to offer differentiated services and flexibly
   instantiate network functions for broadband users.
- **draft-ietf-6man-ipv6-neighbor-discovery-yang-06** (new-draft, score 3, adjacent_watchlist) [6man]: [YANG Data Model for IPv6 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/) — This document defines a YANG data model to configure and manage IPv6
   Neighbor Discovery (ND) and related functions, including IPv6 address
   resolution, redirect function, proxy Neighbor Advertisement, Neighbor
   Unreachability Detection (NUD), Duplicate Address Detection (DAD),
   and Enhanced Duplicate Address Detection.
- **draft-ietf-asdf-nipc-21** (new-draft, score 3, adjacent_watchlist) [asdf]: [An Application Layer Interface for Non-Internet-connected Physical Components (NIPC)](https://datatracker.ietf.org/doc/draft-ietf-asdf-nipc/) — This document describes an API that allows applications to perform
   operations against a gateway serving one or more devices described by
   an SDF model.  The API consists of a RESTful application layer
   interface that performs operations on those devices, as well as a
   CBOR-based publish-subscribe interface for streaming data.
- **draft-ietf-asdf-sdf-protocol-mapping-10** (new-draft, score 3, adjacent_watchlist) [asdf]: [SDF Protocol Mapping](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-protocol-mapping/) — This document defines protocol mapping extensions for the Semantic
   Definition Format (SDF) to enable mapping of protocol-agnostic SDF
   affordances to protocol-specific operations.  The protocol mapping
   mechanism allows SDF models to specify how properties, actions, and
   events should be accessed using a specific protocol.  This document
   defines protocol mappings for Bluetooth Low Energy and Zigbee, and
   the mechanism can be extended to other protocols such as HTTP and
   CoAP.  This document also describes a method to extend SCIM with an
   SDF model mapping.
- **draft-ietf-dult-threat-model-05** (new-draft, score 3, adjacent_watchlist) [dult]: [DULT Threat Model](https://datatracker.ietf.org/doc/draft-ietf-dult-threat-model/) — Lightweight location-tracking tags are in wide use to allow users to
   locate items.  These tags function as a component of a crowdsourced
   network in which devices belonging to other network users (e.g.,
   phones) report which tags they see and their location, thus allowing
   the owner(s) of the tag to determine where their tag was most
   recently seen.  While there are many legitimate uses of these tags,
   they are also susceptible to misuse for the purpose of stalking and
   abuse.  A protocol that allows others to detect unwanted tracking
   must incorporate an understanding of the unwanted tracking landscape
   today.  This document provides a threat analysis for this purpose,
   including a taxonomy of unwanted tracking and potential attacks
   against Detection of Unwanted Location Tracking (DULT) protocols.
   The document defines what is in and out of scope for the unwanted
   tracking protocols, and provides design requirements, constraints,
   and considerations for implementation of protocols to detect unwanted
   tracking.
- **draft-ietf-httpbis-no-vary-search-08** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
- **draft-ietf-kitten-password-storage-13** (new-draft, score 3, adjacent_watchlist) [kitten]: [Best practices for SASL password hashing and storage](https://datatracker.ietf.org/doc/draft-ietf-kitten-password-storage/) — This document outlines best practices for handling user passwords and
   other secrets in client-server systems making use of SASL.
- **draft-ietf-masque-connect-ethernet-12** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document describes how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-masque-connect-udp-listen-15** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Bound UDP in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-listen/) — The mechanism defined in "Proxying UDP in HTTP" (RFC 9298) only
   allows each UDP proxying request to transmit to a specific host and
   port.  This is well suited for UDP client-server protocols such as
   HTTP/3, but is not sufficient for some UDP peer-to-peer protocols
   like WebRTC.  This document defines an extension to that mechanism
   that enables such use cases.
- **draft-ietf-sidrops-constraining-rpki-trust-anchors-01** (new-draft, score 3, adjacent_watchlist) [sidrops]: [Constraining RPKI Trust Anchors](https://datatracker.ietf.org/doc/draft-ietf-sidrops-constraining-rpki-trust-anchors/) — This document describes an approach for Resource Public Key
   Infrastructure (RPKI) Relying Parties (RPs) to impose locally
   configured Constraints on cryptographic products subordinate to Trust
   Anchors (TAs).  The ability to constrain a Trust Anchor operator's
   effective signing authority to a limited set of Internet Number
   Resources (INRs) allows Relying Parties to enjoy the potential
   benefits of assuming trust - within a bounded scope.  The specified
   approach and configuration format allow RPKI operators to communicate
   efficiently about observations related to Trust Anchor operations.
- **draft-ietf-sidrops-moa-profile-04** (new-draft, score 3, authorization) [sidrops]: [A Profile for Mapping Origin Authorizations (MOAs)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-moa-profile/) — This document proposes a new approach by leveraging Resource Public
   Key Infrastructure (RPKI) architecture to verify the authenticity of
   the mapping origin of an IPv4 address block.  MOA is a newly defined
   cryptographically signed object that provides a means for the address
   holder can authorize an IPv6 mapping prefix to originate mapping for
   one or more IPv4 prefixes.  When receiving the MOA objects from the
   relying parties, PE devices can verify and discard invalid address
   mapping announcements from unauthorized IPv6 mapping prefixes to
   prevent IPv4 prefix hijacking.
- **draft-ietf-suit-update-management-15** (new-draft, score 3, core_identity) [suit]: [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/draft-ietf-suit-update-management/) — This document specifies extensions to the SUIT manifest format.
   These extensions allow a Manifest Author, update distributor, or
   device operator to more precisely control the distribution and
   installation of updates to devices.  These extensions also provide a
   mechanism to inform a management system of Software Identifier and
   Software Bill Of Materials information about an updated device.
- **draft-intra-handshake-fail-05** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
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
- **draft-irtf-cfrg-aead-limits-12** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Usage Limits on AEAD Algorithms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-aead-limits/) — An Authenticated Encryption with Associated Data (AEAD) algorithm
   provides confidentiality and integrity.  Excessive use of the same
   key can give an attacker advantages in breaking these properties.
   This document provides simple guidance for users of common AEAD
   functions about how to limit the use of keys in order to bound the
   advantage given to an attacker.  It considers limits in both single-
   and multi-key settings.
- **draft-iupa-ngg-multicast-publishing-01** (new-draft, score 3, adjacent_watchlist) [none]: [NG-Multicast-Publishing Protocol](https://datatracker.ietf.org/doc/draft-iupa-ngg-multicast-publishing/) — This document defines the NG-Multicast-Publishing protocol, which is
   used to distribute free eBooks, publication metadata, and copyright
   information over IPv4/IPv6 multicast networks in an efficient and
   reliable manner.  The protocol employs a one-to-many,
   unidirectional communication model and supports Any-Source Multicast
   (ASM).  It is intended for use by libraries, educational
   institutions, and individual receivers worldwide.  Design goals
   include very low resource consumption, no requirement for an uplink
   channel, permanently assigned multicast addresses, and end-to-end
   integrity verification.
- **draft-kestura-pac-compliance-attestation-00** (new-draft, score 3, trust_infrastructure) [none]: [An Interoperable Attestation Format for Policy-as-Code Compliance Evidence](https://datatracker.ietf.org/doc/draft-kestura-pac-compliance-attestation/) — Organizations increasingly enforce regulatory and security
   requirements using policy-as-code (PaC) engines integrated into
   continuous integration and delivery (CI/CD) pipelines.  The evidence
   these engines produce, that is, the record of which policies were
   evaluated, against what inputs, and with what outcome, is typically
   emitted in vendor-specific, non-portable formats.  This impairs
   auditability, cross-tool aggregation, and independent verification.
   This document analyzes the problem and describes an interoperable,
   machine-readable attestation format for PaC compliance evidence.  It
   is informational and does not define an IETF standard, nor does it
   establish a new IANA registry.
- **draft-leopizzi-fulmen-01** (new-draft, score 3, core_identity) [none]: [FULMEN 1.0: Event-Driven Bidirectional Client-Server Communication Protocol](https://datatracker.ietf.org/doc/draft-leopizzi-fulmen/) — This document specifies FULMEN version 1.0, an event-driven,
   bidirectional client-server communication protocol with a binary wire
   format.  Within a FULMEN connection, both the client and the server
   can send events.  An event is a message frame identified by a
   sequential identifier and addressed by a UTF-8 path used for routing
   and dispatching; its sender can request an acknowledgment, a response
   correlated to the event that carries a status code describing the
   outcome of its processing.  Events and acknowledgments can carry a
   binary payload, either inline within the frame or delivered
   incrementally in chunks through a stream.  The protocol version in
   use is negotiated during the connection handshake.  FULMEN also
   defines an extension mechanism, based on typed data units attached to
   protocol messages, through which additional functionality can be
   introduced without changes to the wire format.
- **draft-li-recursive-peer-model-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Recursive Peer Model for Network Protocols](https://datatracker.ietf.org/doc/draft-li-recursive-peer-model/) — The seven-layer OSI model has served as a foundational framework for
   network protocol design and education for four decades.  However,
   modern networking practices—including VPNs, NAT, tunneling protocols,
   and overlay networks—have revealed structural flaws in the OSI model
   that require ad hoc exceptions to explain.

   This document presents a Recursive Peer Model (RPM) as an alternative
   architectural framework.  The model is based on a single observation:
   every intermediate protocol layer contains its own four-layer
   structure—Bearer Layer, Data Link Layer, Network Layer, and Transport
   Layer—and this structure recurs at every layer of the protocol stack.
   The Data Layer and Medium Layer serve as the two recursive
   boundaries, terminating at "pure data" and "physical medium"
   respectively.

   The Recursive Peer Model eliminates the need for "exception" clauses
   (such as the "tunnel exception" for VPNs), provides coherent
   explanations for protocols that OSI cannot categorize cleanly (such
   as ARP and ICMP), and offers a unified framework for describing both
   existing and future protocols.
- **draft-liu-rtgwg-llmsync-multicast-01** (new-draft, score 3, adjacent_watchlist) [none]: [Multicast Use Cases for Large Language Model Synchronization](https://datatracker.ietf.org/doc/draft-liu-rtgwg-llmsync-multicast/) — Large Language Models (LLMs) deployments are becoming increasingly
   widespread, with inference services being the most common
   application.  This draft will discuss multicast use cases for
   inference cloud services.
- **draft-morrison-alter-uri-scheme-02** (new-draft, score 3, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
   reference syntax for ~handle identity references published under the
   DNS substrate defined in [MCPDNS].  An alter: URI binds a textual
   ~handle reference to a resolution and verification procedure that
   retrieves the handle's envelope from the publishing zone, validates
   the envelope's signature chain, and dispatches the result to an
   operating-system URI handler.  The reference may be scoped to an
   organisation, narrowed to a named facet of the identity, and
   addressed to a typed action surface.  The scheme is the addressing
   form of the ~handle@org:facet/action reference; its resolution
   semantics are those of [MCPDNS], reused without modification.

   The scheme is provider-neutral, introduces no new cryptographic
   primitive, and reuses the resolution and verification procedures of
   [MCPDNS] without modification.  The principal contribution is a
   single, self-verifying dispatch surface for handle-typed references:
   clicking, typing, or scanning an alter: URI yields a verified handle
   resolution rather than a free-text string or an unauthenticated
   fetch, and where an action is addressed it yields a verify-before-
   side-effect dispatch.  This document requests provisional
   registration of the alter scheme with IANA per [RFC7595] Section 3.
- **draft-reddy-ipsecme-pqt-hybrid-auth-01** (new-draft, score 3, core_identity) [none]: [Hybrid Post-Quantum and Traditional Authentication for IKEv2](https://datatracker.ietf.org/doc/draft-reddy-ipsecme-pqt-hybrid-auth/) — A Cryptographically Relevant Quantum Computer (CRQC) can break
   traditional public-key algorithms (e.g., RSA, ECDSA), which are
   typically used for authentication in IKEv2.  Combining the post-
   quantum ML-DSA signature algorithm with a traditional signature
   algorithm provides protection against potential weaknesses or
   implementation flaws in ML-DSA.  This draft defines a hybrid PKI
   authentication method for IKEv2 using composite certificates that
   ensures authentication remains secure as long as at least one of the
   component signature algorithms remains unbroken.
- **draft-shubralov-demi-sro-payment-security-02** (new-draft, score 3, adjacent_watchlist) [none]: [Blockchain-Backed Risk Pooling and Self-Regulation Protocol for Alternative Payment Providers (DeMI)](https://datatracker.ietf.org/doc/draft-shubralov-demi-sro-payment-security/) — This document specifies a Best Current Practice (BCP) for risk
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
- **draft-singh-apex-psi-05-02** (new-draft, score 3, trust_infrastructure) [none]: [PSI-05: Financial Disclosure Integrity](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/) — PSI-05 defines a cryptographic attestation framework for financial
   disclosures, enabling third parties to recompute and verify company
   filings against their published figures.  It establishes a public
   ledger of sealed financial statements, a verification protocol using
   RFC 8785 canonicalization with Ed25519 (classical) and ML-DSA-65
   (post-quantum) signatures, and an API for querying reconciliation
   results.  The framework supports ASX, NYSE, NSE, LSE, and Euronext
   filings.
- **draft-sohail-urn-dnp-01** (new-draft, score 3, core_identity) [none]: [A Uniform Resource Name (URN) Namespace for Digital Nation Pakistan (DNP)](https://datatracker.ietf.org/doc/draft-sohail-urn-dnp/) — This document describes a Uniform Resource Name (URN) namespace for
   persistent, location-independent identification of normative and
   authoritative publications issued under the Digital Nation Pakistan
   (DNP) programme by the Pakistan Digital Authority (PDA), a federal
   statutory body of the Government of Pakistan established under the
   Digital Nation Pakistan Act, 2025.  The namespace covers policies,
   frameworks, technical standards, reference architectures,
   specifications, schemas, application programming interface contracts,
   registries and datasets that PDA issues or is statutorily designated
   to maintain.  This document requests registration of the formal
   Namespace Identifier "dnp" in accordance with RFC 8141.
- **draft-tailhardat-incident-management-noria-01** (new-draft, score 3, adjacent_watchlist) [none]: [Knowledge Graphs for Enhanced Cross-Operator Incident Management and Network Design](https://datatracker.ietf.org/doc/draft-tailhardat-incident-management-noria/) — Operational efficiency in incident management in networking requires
   correlating and interpreting large volumes of heterogeneous technical
   information.  Knowledge Graphs (KG) can provide a unified view of
   complex systems through shared vocabularies.  YANG data models enable
   describing network configurations and automating their deployment.
   However, both approaches face challenges in vocabulary alignment and
   adoption, hindering knowledge capitalization and sharing on network
   designs and best practices.  To address this, the concept of a IT
   Service Management Knowledge Graph (ITSM-KG) is introduced to
   leverage existing network infrastructure descriptions in YANG format
   and enable abstract reasoning on network behaviors.  The key
   principle to achieve the construction of such ITSM-KG is to transform
   YANG representations of network infrastructures into an equivalent
   knowledge graph representation, and then embed it into a more
   extensive data model for Anomaly Detection (AD) and Risk Management
   applications.

   In addition to use case analysis and design pattern analysis, an
   experiment is proposed to assess the potential of the ITSM-KG in
   improving network quality and designs.
- **draft-tailhardat-nmop-incident-management-noria-05** (new-draft, score 3, adjacent_watchlist) [none]: [Knowledge Graphs for Enhanced Cross-Operator Incident Management and Network Design](https://datatracker.ietf.org/doc/draft-tailhardat-nmop-incident-management-noria/) — Operational efficiency in incident management in networking requires
   correlating and interpreting large volumes of heterogeneous technical
   information.  Knowledge Graphs (KG) can provide a unified view of
   complex systems through shared vocabularies.  YANG data models enable
   describing network configurations and automating their deployment.
   However, both approaches face challenges in vocabulary alignment and
   adoption, hindering knowledge capitalization and sharing on network
   designs and best practices.  To address this, the concept of a IT
   Service Management Knowledge Graph (ITSM-KG) is introduced to
   leverage existing network infrastructure descriptions in YANG format
   and enable abstract reasoning on network behaviors.  The key
   principle to achieve the construction of such ITSM-KG is to transform
   YANG representations of network infrastructures into an equivalent
   knowledge graph representation, and then embed it into a more
   extensive data model for Anomaly Detection (AD) and Risk Management
   applications.

   In addition to use case analysis and design pattern analysis, an
   experiment is proposed to assess the potential of the ITSM-KG in
   improving network quality and designs.
- **draft-feng-dnsop-authdns-operator-change-00** (new-draft, score 2, ignored_after_review) [none]: [Operational Guidance for Authoritative DNS Operator Changes with Service Endpoint Migration for Registered Domain Names](https://datatracker.ietf.org/doc/draft-feng-dnsop-authdns-operator-change/) — A registered domain name can change its authoritative DNS operator
   while the registrant also migrates service endpoints, such as web,
   API, CDN, mail, or cloud-hosted services.  In this situation, service
   RRsets such as A, AAAA, CNAME, MX, SRV, SVCB, and HTTPS RRsets can
   change at the same time as the parent-side delegation changes.

   The parent-side delegation change is not observed by all recursive
   resolvers at the same instant.  During the transition, some resolvers
   can continue to query the losing DNS operator while others query the
   gaining DNS operator.  If the losing operator continues to serve
   stale service RRsets, or if it stops serving the zone too early,
   users can receive different answers depending on resolver cache state
   and can experience intermittent service failure.

   This document provides operational guidance for authoritative DNS
   operator changes with service endpoint migration for registered
   domain names.  It recommends a registrant-authorized change plan, a
   consistency profile for in-scope service RRsets, synchronized
   provisioning or a common source of truth, a hold period during which
   the losing DNS operator continues to serve target or otherwise
   equivalent data, and verification points that directly compare the
   losing and gaining authoritative servers and classify observed states
   as planned, service-risk, or unexpected-delegation conditions.
- **draft-fengfar-led-01** (new-draft, score 2, ignored_after_review) [none]: [Dealing with LLMs in IETF Discussions](https://datatracker.ietf.org/doc/draft-fengfar-led/) — The rapid adoption of AI language tools has prompted concern across
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
- **draft-king-rokui-ainetops-usecases-02** (new-draft, score 2, ai_infrastructure) [none]: [Artificial Intelligence (AI) for Network Operations](https://datatracker.ietf.org/doc/draft-king-rokui-ainetops-usecases/) — This document explores the role of the IETF and IRTF in advancing
   Artificial Intelligence for network operations (AINetOps), focusing
   on requirements for IETF protocols and architectures.  AINetOps
   applies AI/ML techniques to automate and optimize network operations,
   enabling use cases such as reactive troubleshooting, proactive
   assurance, closed-loop optimization, misconfiguration detection, and
   virtual operator assistance.

   The document addresses AINetOps for both single-layer IP or Optical
   networks and multi-layer IP/Optical networks.  It defines the concept
   of AINetOps for networking and provides its operational benefits such
   as network assurance, predictive analytics, network optimization,
   multi-layer planning, and more.  It aims to guide the evolution of
   IETF protocols to support AINetOps-driven network management.
- **draft-reilly-rem-protocol-02** (new-draft, score 2, ignored_after_review) [none]: [Reilly EternaMark (REM) Protocol - Dual-Layer Digital Permanence Using DOI Archiving and Blockchain Timestamping](https://datatracker.ietf.org/doc/draft-reilly-rem-protocol/) — The Reilly EternaMark (REM) Protocol defines a dual-layer method for
   digital permanence through the integration of Digital Object
   Identifiers (DOIs) and blockchain timestamping.  The protocol ensures
   digital artifacts are permanently identifiable, immutable, and
   verifiable for both present and future use.

   Revision -01 extended the -00 specification with a formal REM Record
   structure, a machine-readable artifact manifest format, a
   verification procedure, implementation guidance, and expanded
   security and interoperability considerations.

   This revision (-02) additionally documents the protocol's function
   as a prior art record system under 35 U.S.C. 102(a)(1): a Full REM
   Record establishes that a publicly deposited artifact was available
   to the public in its exact recorded form no later than a
   cryptographically verifiable date, enabling its use as defensive
   publication against later-filed patent claims.
- **draft-singh-apex-psi-06-01** (new-draft, score 2, ignored_after_review) [none]: [PSI-06: Inception-Lock Protocol for Human-Originated Data Signals](https://datatracker.ietf.org/doc/draft-singh-apex-psi-06/) — PSI-06 specifies an inception-lock protocol that cryptographically
   anchors a raw human-originated data signal (keystroke, biometric,
   survey response, application screen capture, trip acceptance
   timestamp) to a signing key at the point of capture.  The protocol
   prevents tampering with source data between capture and submission,
   enabling verifiable proof of what a user was shown and when they saw
   it.  Receipts are protected by a hybrid dual-signature scheme
   combining Ed25519 (classical) and ML-DSA-65 (post-quantum), making
   the evidence chain resistant to both classical and quantum
   adversaries.  This is critical for accountability proceedings
   involving algorithmic platforms, where the information displayed to
   the user may differ from the information recorded by the platform.
- **draft-zehta-aipref-parameters-00** (new-draft, score 2, ignored_after_review) [none]: [AIPREF Vocabulary Parameters](https://datatracker.ietf.org/doc/draft-zehta-aipref-parameters/) — This document defines how parameters can be added to AI Preferences.

## Ignored after review

- **draft-altanai-tsv-multipath-nested-tunnels-01** (new-draft, score 0, ignored_after_review) [none]: [Congestion-Aware Multipath Tunnel Selection for Transport Services](https://datatracker.ietf.org/doc/draft-altanai-tsv-multipath-nested-tunnels/) — This document addresses the transport-layer challenges of path
   selection in environments with multiple available tunneling options
   and congestion control mechanisms.  It identifies congestion control
   conflicts that arise from nested tunneling protocols and proposes a
   congestion-aware multipath tunnel selection algorithm that conforms
   to the guidelines established in [RFC9599] for adding congestion
   notification to protocols that encapsulate IP.  The proposed approach
   considers Explicit Congestion Notification (ECN) propagation,
   transport protocol characteristics, and network conditions to
   optimize path selection while avoiding multilevel congestion control
   issues.  This work aligns with current Transport and Services Working
   Group efforts on Non-Queue-Building (NQB) behaviors, careful
   congestion control resume, and multipath transport protocols.
- **draft-attoumani-ietf-inclusion-05** (new-draft, score 0, ignored_after_review) [none]: [The IETF is for Everyone: Toward Inclusive and Equitable Participation in Internet Governance](https://datatracker.ietf.org/doc/draft-attoumani-ietf-inclusion/) — This document aims to foster a deeper reflection within the IETF
   community on inclusive participation, equitable access, and the
   implications of global meeting venue selections on diverse
   contributors.  It seeks to complement existing RFCs by proposing
   additional dialogue, tools, and evaluation mechanisms, while also
   highlighting the shared responsibility of underrepresented regions in
   mobilizing local stakeholders to engage with the IETF.  This draft
   includes concrete proposals, metrics, and an implementation roadmap
   to move from discussion to action.
- **draft-drew-dhc-v4-routed-prefix-00** (new-draft, score 0, ignored_after_review) [none]: [DHCPv4 Routed Prefix Option](https://datatracker.ietf.org/doc/draft-drew-dhc-v4-routed-prefix/) — This document defines a DHCPv4 option that conveys one or more IPv4
   prefixes that are routed toward a DHCP client independently of the
   client's on-link DHCP-assigned IPv4 address and default-router
   configuration.

   The option is intended for requesting routers whose upstream
   attachment address is distinct from IPv4 prefix space routed toward
   them.  Examples include access networks in which a customer router
   receives a private-use address [RFC1918] or Shared Address Space
   [RFC6598] attachment address while one or more additional public or
   private IPv4 prefixes are routed toward that router.

   This document does not define how the upstream network establishes
   the route, does not require Network Address Translation (NAT), and
   does not specify how a client uses, assigns, translates, or delegates
   an advertised prefix after receipt.
- **draft-dunglas-mercure-08** (new-draft, score 0, ignored_after_review) [none]: [The Mercure Protocol](https://datatracker.ietf.org/doc/draft-dunglas-mercure/) — Mercure provides a common publish-subscribe mechanism for public and
   private web resources.  It pushes any web content to web browsers and
   other clients over a single long-lived HTTP connection, avoiding
   polling and its associated latency and power cost.  Mercure is
   especially useful for delivering real-time updates of resources
   served through sites and web APIs to web and mobile applications, and
   can also be used as a general-purpose publish-subscribe system.

   Subscription requests are relayed through hubs, which validate them.
   When new or updated content becomes available, hubs check whether
   subscribers are authorized to receive it and then distribute it.
- **draft-fast-severity-00** (new-draft, score 0, ignored_after_review) [none]: [FAST: Framework for Autonomous Severity and Triage](https://datatracker.ietf.org/doc/draft-fast-severity/) — This document specifies the Framework for Autonomous Severity and
   Triage (FAST): an empirical standard for how autonomous offensive
   security agents classify vulnerabilities, decide whether to submit
   reports, and write those reports.  FAST is derived from a corpus of
   real bug bounty reports and their program-rendered triage outcomes
   rather than from theoretical scoring frameworks.  It is designed to
   be applied by both offensive agents that hunt for vulnerabilities and
   by defensive agents or human triagers that render verdicts, so both
   sides of the reporting relationship operate under the same rulebook.
   This document is submitted as an Independent Submission and invites
   comment from researchers, triagers, bug bounty platforms, and
   security teams.
- **draft-halmir-mpls-ecn-04** (new-draft, score 0, ignored_after_review) [none]: [Explicit Congestion Notification Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-halmir-mpls-ecn/) — It has been broadly demonstrated that user experience improvements
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
- **draft-haynes-nfsv4-flexfiles-v2-08** (new-draft, score 0, ignored_after_review) [none]: [Parallel NFS (pNFS) Flexible File Layout Version 2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2/) — Parallel NFS (pNFS) allows a separation between the metadata (onto a
   metadata server) and data (onto a storage device) for a file.  The
   Flexible File Version 2 Layout Type is defined in this document as an
   extension to pNFS that allows the use of storage devices that require
   only a limited degree of interaction with the metadata server and use
   already-existing protocols.  Data protection is also added to provide
   integrity.  Both Client-side mirroring and the erasure coding
   algorithms are used for data protection.
- **draft-haynes-nfsv4-flexfiles-v2-delta-writes-00** (new-draft, score 0, ignored_after_review) [none]: [Delta-Write Extension for the Flexible File Version 2 Layout Type](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2-delta-writes/) — The Flexible File Version 2 pNFS layout type defines a chunk-oriented
   data-server protocol in which every write is a full-chunk payload.
   For workloads that make small edits to files protected by an XOR-
   based erasure encoding, this forces client-side stripe fetch, re-
   encode, and transmit on every edit, with wire amplification of three
   to four orders of magnitude per byte edited.  This document defines
   an optional extension, CHUNK_XOR_DELTA, that lets a client transmit a
   per-projection XOR delta directly to each data server holding a
   projection of the affected stripe; the data server applies the delta
   locally.  The extension is restricted to XOR-linear systematic
   encodings and XOR-affine checksums, using the existing chunk state
   machine with no new commit protocol.
- **draft-haynes-nfsv4-flexfiles-v2-proxy-server-04** (new-draft, score 0, ignored_after_review) [none]: [Proxy-Driven Server for Flexible Files Version 2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2-proxy-server/) — Parallel NFS (pNFS) with the Flexible Files Version 2 layout type
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
- **draft-ietf-anima-masa-considerations-03** (new-draft, score 0, ignored_after_review) [anima]: [Operational Considerations for Voucher infrastructure for BRSKI MASA](https://datatracker.ietf.org/doc/draft-ietf-anima-masa-considerations/) — This document describes a number of operational modes that a BRSKI
   Manufacturer Authorized Signing Authority (MASA) may take on.

   Each mode is defined, and then each mode is given a relevance within
   an over applicability of what kind of organization the MASA is
   deployed into.  This document does not change any protocol
   mechanisms.
- **draft-ietf-dnsop-dnssec-keyrestore-02** (new-draft, score 0, ignored_after_review) [dnsop]: [DNSSEC Key Restore](https://datatracker.ietf.org/doc/draft-ietf-dnsop-dnssec-keyrestore/) — This document describes the issues surrounding the handling of DNSSEC
   private keys in a DNSSEC signer.  It presents operational guidance in
   case a DNSSEC private key becomes inoperable.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Domain Name System
   Operations Working Group mailing list (dnsop@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/dnsop/.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-wg-dnsop/draft-ietf-dnsop-dnssec-keyrestore.
- **draft-ietf-green-use-cases-02** (new-draft, score 0, ignored_after_review) [green]: [Use Cases for Energy Efficiency Management](https://datatracker.ietf.org/doc/draft-ietf-green-use-cases/) — This document groups use cases for Energy efficiency Management of
   network devices.

   Discussion Venues

   Source of this draft and an issue tracker can be found at
   https://github.com/emile22/draft-ietf-green-use-cases
- **draft-ietf-ipsecme-hybrid-kem-ikev2-frodo-03** (new-draft, score 0, ignored_after_review) [ipsecme]: [Post-quantum Key Exchange in IKEv2 with FrodoKEM](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-hybrid-kem-ikev2-frodo/) — FrodoKEM is an unstructured lattice based Key Encapsulation Mechanism
   (KEM), standardized by ISO.  Compared to ML-KEM, it is considered
   with more conservative security.  This draft specifies how to use
   FrodoKEM by itself or as an additional key exchange in IKEv2 along
   with a traditional key exchange.  These options enable to negotiate
   IKE and Child SA keys that are safe against a Cryptographically
   Relevant Quantum Computer (CRQC).
- **draft-ietf-ipsecme-ikev2-reliable-transport-07** (new-draft, score 0, ignored_after_review) [ipsecme]: [Separate Transports for IKE and ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-reliable-transport/) — The Internet Key Exchange protocol version 2 (IKEv2) can operate
   either over unreliable (UDP) transport or over reliable (TCP)
   transport.  If TCP is used, then IPsec tunnels created by IKEv2 also
   use TCP.  This document specifies how to decouple IKEv2 and IPsec
   transports so that IKEv2 can operate over TCP, while IPsec tunnels
   use unreliable transport.  This feature allows IKEv2 to effectively
   exchange large blobs of data (e.g., when post-quantum algorithms are
   employed) while avoiding performance problems that arise when IPsec
   uses TCP.
- **draft-ietf-lsr-l2-bundle-member-remote-id-05** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  For example,
   when performing topology management and bidirectional path
   computation for TE, it is essential to know the connectivity
   relationships among bundle members.

   This document describes how OSPF and IS-IS would advertise the remote
   interface identifiers for Layer 2 bundle members.  The corresponding
   extension of BGP-LS is also specified.
- **draft-ietf-manet-inet-gap-analysis-05** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mediaman-6838bis-09** (new-draft, score 0, ignored_after_review) [mediaman]: [Media Type Specifications and Registration Procedures](https://datatracker.ietf.org/doc/draft-ietf-mediaman-6838bis/) — This document defines procedures for the specification and
   registration of media types for use in HTTP, MIME, and other Internet
   protocols.
- **draft-ietf-mpls-mna-ioam-11** (new-draft, score 0, ignored_after_review) [mpls]: [Supporting In Situ Operations, Administration, and Maintenance Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, collects operational and telemetry information in the
   packet using IOAM-Data-Fields while the packet traverses a path
   between two points in the network.  Several IOAM Option-Types are
   available, for example, Pre-allocated Trace, Proof of Transit (POT),
   Edge-to-Edge (E2E), and Incremental Trace, that can be used to
   collect information for calculating various performance metrics.  RFC
   9326 defines the IOAM Direct Export (IOAM-DEX) Option-Type, which is
   used as a trigger for IOAM data to be directly exported or locally
   aggregated without being pushed into in-flight data packets.

   MPLS Network Actions (MNA) techniques indicate actions to be
   performed on any combination of Label Switched Paths, MPLS packets,
   and the node itself, and to transport data needed for these actions.
   This document employs the MNA mechanisms to collect and transport the
   operational state and telemetry information using IOAM-Data-Fields as
   well as IOAM-DEX.
- **draft-ietf-mpls-mna-ps-hdr-19** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Action (MNA) Post-Stack Header Specification](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ps-hdr/) — This document specifies the MPLS Network Action (MNA) Post-Stack
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

   This document updates RFC 9789: the definition of Readable Label
   Depth (RLD).
- **draft-ietf-mpls-on-path-telemetry-flag-03** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes postcard-based on-path telemetry with packet
   marking (PBT-M) using an MPLS Network Actions (MNA) flag to support
   Operations, Administration, and Maintenance (OAM) in MPLS networks.
   The scheme uses a single flag bit carried in a Flag-Based Network
   Action Indicator (Opcode 1) of the MNA Sub-Stack as defined in RFC
   9994.  In addition to addressing the protocol requirements for
   applying PBT-M, this document provides comprehensive operational,
   manageability, and security considerations.
- **draft-ietf-mpls-stamp-pw-07** (new-draft, score 0, ignored_after_review) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document describes the procedure for encapsulating the Simple
   Two-Way Active Measurement Protocol (STAMP), defined in RFC 8762, and
   its optional extensions defined in RFC 8972, in MPLS networks.  Label
   Switched Paths (LSPs) and Pseudowires (PWs) are used in MPLS networks
   for various services including carrying Layer 2 and Layer 3 data
   packets and may use the Control Word (CW).  The procedure is also
   described for encapsulating STAMP test packets with or without the CW
   and/or an IP/UDP header for LSPs and PWs.
- **draft-ietf-netconf-over-quic-10** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF over QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-over-quic/) — This document specifies how to use QUIC as a secure transport for
   exchanging Network Configuration Protocol (NETCONF) messages.
   NETCONF over QUIC allows to take advantage of QUIC streams, for
   example, to eliminate some TCP head-of-line blocking issues.  NETCONF
   over QUIC provides security properties similar to NETCONF over TLS.

   This document also defines a YANG module which augments the ietf-
   netconf-client and ietf-netconf-server YANG modules.

Editorial note (to be removed by the RFC Editor

   This draft contains placeholder values that need to be replaced with
   finalized values at the time of publication.  This note summarizes
   all of the substitutions that are needed.  No other RFC Editor
   instructions are specified elsewhere in this document.

   Artwork in this document contains shorthand references to drafts in
   progress.  Please apply the following replacements:

   *  AAAA --> the assigned RFC value for this draft

   *  BBBB --> the assigned RFC value for draft-ietf-netconf-netconf-
      client-server

   *  CCCC --> the assigned RFC value for draft-ietf-netconf-quic-
      client-server
- **draft-ietf-ntp-nts-for-ptp-04** (new-draft, score 0, ignored_after_review) [ntp]: [NTS4PTP - Network Time Security for the Precision Time Protocol](https://datatracker.ietf.org/doc/draft-ietf-ntp-nts-for-ptp/) — This document specifies an automatic key management service for the
   integrated security mechanism (prong A) of IEEE Std 1588™-2019
   (PTPv2.1) described there in Annex P.  This key management follows
   the immediate security processing approach of prong A and extends the
   NTS Key Establishment protocol defined in IETF RFC 8915 for securing
   NTPv4.  The resulting NTS for PTP (NTS4PTP) protocol provides a
   security solution for all PTP modes and operates completely
   independent of NTPv4.
- **draft-ietf-openpgp-nist-bp-comp-04** (new-draft, score 0, ignored_after_review) [openpgp]: [PQ/T Composite Schemes for OpenPGP using NIST and Brainpool Elliptic Curve Domain Parameters](https://datatracker.ietf.org/doc/draft-ietf-openpgp-nist-bp-comp/) — This document defines PQ/T ("post-quantum/traditional") composite
   schemes based on ML-KEM and ML-DSA combined with ECDH and ECDSA
   algorithms using the NIST and Brainpool domain parameters for the
   OpenPGP protocol [RFC9580], and as such extends [RFC9980].
- **draft-ietf-opsawg-rfc5706bis-06** (new-draft, score 0, ignored_after_review) [opsawg]: [Guidelines for Considering Operations and Management in IETF Specifications](https://datatracker.ietf.org/doc/draft-ietf-opsawg-rfc5706bis/) — New Protocols and Protocol Extensions are best designed with due
   consideration of the functionality needed to operate and manage them.
   Retrofitting operations and management considerations is suboptimal.
   The purpose of this document is to provide guidance to authors and
   reviewers on what operational and management aspects should be
   addressed when writing documents in the IETF Stream that document a
   specification for New Protocols or Protocol Extensions or describe
   their use.

   This document obsoletes RFC 5706, replacing it completely and
   updating it with new operational and management techniques and
   mechanisms.  It also updates RFC 2360 to obsolete mandatory MIB
   creation.  Finally, it introduces a requirement to include an
   "Operational Considerations" section in new RFCs in the IETF Stream
   that define New Protocols or Protocol Extensions or describe their
   use (including relevant YANG Models), while providing an escape
   clause if no new considerations are identified.
- **draft-ietf-quic-reliable-stream-reset-10** (new-draft, score 0, ignored_after_review) [quic]: [QUIC Stream Resets with Partial Delivery](https://datatracker.ietf.org/doc/draft-ietf-quic-reliable-stream-reset/) — QUIC defines a RESET_STREAM frame to abort sending on a stream.  When
   a sender resets a stream, it also stops retransmitting STREAM frames
   for this stream in the event of packet loss.  On the receiving side,
   there is no guarantee that any data sent on that stream is delivered.

   This document defines a new QUIC frame, the RESET_STREAM_AT frame,
   that allows resetting a stream, while guaranteeing delivery of stream
   data up to a certain byte offset.
- **draft-ietf-radext-review-radius-02** (new-draft, score 0, ignored_after_review) [radext]: [A Review of RADIUS Security and Privacy](https://datatracker.ietf.org/doc/draft-ietf-radext-review-radius/) — This document provides a comprehensive review of security issues
   related to the RADIUS Protocol.  This review motivates the changes to
   RADIUS security which are made in
   [I-D.ietf-radext-deprecating-radius].
- **draft-ietf-rift-auto-evpn-07** (new-draft, score 0, ignored_after_review) [rift]: [RIFT Auto-EVPN](https://datatracker.ietf.org/doc/draft-ietf-rift-auto-evpn/) — This document specifies procedures that allow an EVPN overlay to be
   fully and automatically provisioned when using RIFT as underlay by
   leveraging RIFT's no-touch ZTP architecture.
- **draft-ietf-rtgwg-atn-bgp-31** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
   mobile routing solutions for a worldwide Aeronautical
   Telecommunications Network with Internet Protocol Services (ATN/IPS).
   The ATN/IPS will eventually replace existing communication services
   with an IP-based service supporting pervasive Air Traffic Management
   (ATM) for Air Traffic Controllers (ATC), Airline Operations
   Controllers (AOC), and all commercial aircraft worldwide.  This
   informational document describes a simple and extensible mobile
   routing service based on the industry-standard Border Gateway
   Protocol (BGP) to address the ATN/IPS requirements.
- **draft-ietf-rtgwg-vrrp-bfd-p2p-05** (new-draft, score 0, ignored_after_review) [rtgwg]: [Fast failure detection in VRRP with Point to Point BFD](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/) — This document describes how Point to Point Bidirectional Forwarding
   Detection (BFD) can be used to support sub-second detection of a
   Active Router failure in the Virtual Router Redundancy Protocol
   (VRRP).
- **draft-ietf-spring-sr-policy-flexible-cp-selection-01** (new-draft, score 0, ignored_after_review) [spring]: [Flexible Candidate Path Selection of SR Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-flexible-cp-selection/) — This document describes a flexible method for selecting candidate
   Segment Routing (SR) policy paths. Based on the real-time resource
   usage and forwarding quality of candidate paths, the head node can
   perform dynamic path switching among multiple candidate paths in the
   SR policy.
- **draft-ietf-spring-srv6-inter-layer-programming-03** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 for Inter-Layer Network Programming](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-inter-layer-programming/) — The Segment Routing over IPv6 (SRv6) Network Programming framework
   enables a network operator or an application to specify a packet
   processing program by encoding a sequence of instructions in the IPv6
   packet header.

   Following the SRv6 Network Programming concept, this document defines
   SRv6 based mechanisms for inter-layer network programming, which can
   help to integrate the packet network layer with its underlying layers
   efficiently.  For inter-layer path programming, a new SRv6 behavior
   is defined for steering packets to underlay network connections.  The
   applicability of this new SRv6 behavior in typical scenarios is
   illustrated.
- **draft-ietf-spring-srv6-mpls-interworking-03** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 and MPLS interworking](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-mpls-interworking/) — This document describes interworking between SRv6 and MPLS domains to
   provide end to end path.  Interworking problem is generalized into
   various interworking scenarios.  These scenarios are stitched either
   by transport interworking or service interworking.  New SRv6 SID
   endpoint behaviors are defined for the purpose.  These new SRv6 SID
   behaviors and MPLS labels stitch end to end path across different
   data plane.
- **draft-ietf-v6ops-rfc6146-bis-14** (new-draft, score 0, ignored_after_review) [v6ops]: [Stateful NAT64: Network Address and Protocol Translation from IPv6 Clients to IPv4 Servers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc6146-bis/) — This document specifies a stateful NAT64 translation, which allows
   IPv6-Only clients to contact IPv4 servers using unicast UDP, TCP, or
   ICMP.  One or more public IPv4 addresses assigned to a stateful NAT64
   translator are shared among several IPv6-Only clients.  Stateful
   NAT64 translation also supports IPv4-initiated communications to a
   subset of the IPv6 hosts through statically configured bindings in
   the stateful NAT64 translator.  When the stateful NAT64 translation
   is used in conjunction with DNS64, no changes are required in either
   the IPv6 client or the IPv4 server.

   This document obsoletes RFC 6146.
- **draft-jabley-dnsop-local-signing-algorithm-policy-00** (new-draft, score 0, ignored_after_review) [none]: [Supporting Quantum-Safe Algorithms in DNSSEC with Local Resolver Policy](https://datatracker.ietf.org/doc/draft-jabley-dnsop-local-signing-algorithm-policy/) — Security-aware resolvers validate signatures, where available, in
   order to protect their clients from inauthentic data.  DNSSEC treats
   all algorithms as equal when it comes to validation, such that a
   single valid signature is considered sufficient proof of
   authenticity, and that data is only to be judged to be inauthentic if
   all available signatures are found to be invalid.  However, a
   resolver might have a different local policy, e.g. in its handling of
   quantum-safe signatures.  This document discusses such local policy
   and describes a means to indicate to a client that specific local
   policy has been applied to response validation.
- **draft-jabley-dnsop-no-longer-support-any-00** (new-draft, score 0, ignored_after_review) [none]: [Continuing to Reduce Support for ANY Queries in the DNS](https://datatracker.ietf.org/doc/draft-jabley-dnsop-no-longer-support-any/) — The DNS specification from its earliest day supported a special query
   type (QTYPE) ANY.  The handling of queries with QTYPE=ANY is observed
   to vary between implementations.  Queries with QTYPE=ANY are known to
   facilitate amplification that can be abused and used by malicious
   actors to attack third parties, and minimally-sized responses are
   often constructed in order to mitigate those security risks.  While
   queries with QTYPE=ANY can be used for troubleshooting in some cases,
   the substantial inconsistency in how such queries are handled makes
   them at best an unreliable signal.  This document continues a careful
   and gradual process of dropping support for QTYPE=ANY from the DNS.
- **draft-jabley-dnsop-ordered-answer-section-01** (new-draft, score 0, ignored_after_review) [none]: [Ordering of RRSets in DNS Message Sections](https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/) — The existing Domain Name System (DNS) specifications lack some
   clarity in their description of the process by which individual
   sections of a DNS message are constructed.

   This document updates RFC 1034 and RFC 1035 to provide a clearer
   specification, consistent with deployed implementations.
- **draft-jacobs-web4-terminology-00** (new-draft, score 0, ignored_after_review) [none]: [Web4 Terminology and Definitions](https://datatracker.ietf.org/doc/draft-jacobs-web4-terminology/) — This document defines a common vocabulary for describing Web4
   systems: federated, sovereign-entity-capable network architectures
   that extend prior generations of the Web with machine-native
   comprehension and conformance evaluation.  It establishes baseline
   terminology intended for reference by subsequent Web4 specifications,
   including but not limited to [JACOBS-MEC], and is written to be
   independently useful to any implementer or evaluator working with
   Web4-class systems, regardless of underlying implementation.
- **draft-kolomytsev-pshmp-overview-00** (new-draft, score 0, ignored_after_review) [none]: [Proactive Self-Healing Mesh Protocol (PSHMP)](https://datatracker.ietf.org/doc/draft-kolomytsev-pshmp-overview/) — This document describes the Proactive Self-Healing Mesh Protocol
   (PSHMP), a decentralized overlay transport architecture designed to
   improve resilience and availability in distributed IP networks.

   PSHMP operates as an L4-oriented overlay above existing IP
   infrastructure.  It continuously evaluates path quality and
   proactively reconstructs routes before degradation becomes service-
   impacting.

   The architecture combines decentralized topology discovery, adaptive
   path selection, batch acknowledgements, and transport abstraction to
   provide reliable communication under unstable network conditions
   without requiring modifications to underlying IP routing.

   This document presents the protocol architecture, design principles,
   and an overview of an experimental implementation.  It does not
   specify an Internet Standard.
- **draft-lee-pce-pcep-ls-optical-18** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Distribution of Link-State and TE Information for Optical Networks](https://datatracker.ietf.org/doc/draft-lee-pce-pcep-ls-optical/) — In order to compute and provide optimal paths, Path Computation
   Elements (PCEs) require an accurate and timely Traffic Engineering
   Database (TED).  This Link State and TE information has previously
   been obtained from a link state routing protocol that supports
   traffic engineering extensions.

   Link-State (LS) and Traffic Engineering (TE) information can also be
   carried in the Path Computation Element Communication Protocol (PCEP)
   using experimental exensions to PCEP known as Link-State PCEP (PCEP-
   LS).  This document provides further experimental extensions to
   collect Link-State and TE information for optical networks.
- **draft-li-idr-sr-policy-metric-04** (new-draft, score 0, ignored_after_review) [none]: [BGP SR Policy Extensions for Performance-Aware Path Selection](https://datatracker.ietf.org/doc/draft-li-idr-sr-policy-metric/) — To enable the headend node to do performance-aware path selection,
   this document proposes an extension to the BGP SR Policy protocol by
   defining a new optional Metric Sub-TLV within the BGP Tunnel
   Encapsulation Attribute.  The introduced Metric Sub-TLV encodes
   performance parameters (such as latency, bandwidth, reliability,
   etc.) for SR Policy paths.

   This specification also updates the BGP route selection procedures in
   RFC4271, modifying the Breaking Ties (Phase 2) logic to prioritize
   the metrics for SR Policy paths.

   Key contributions include:

   *  Introduce Metric Sub-TLV in BGP SR Policy

   *  Update the tie-breaking procedure for BGP route selection
- **draft-liu-bess-srv6-evpn-validation-05** (new-draft, score 0, ignored_after_review) [none]: [Data Plane Failure Detection Mechanisms for EVPN over SRv6](https://datatracker.ietf.org/doc/draft-liu-bess-srv6-evpn-validation/) — For MPLS EVPN, RFC9489 specifies the mechanisms for detecting data
   plane failures using LSP Ping.  This document proposes a similar
   mechanism to detect data plane failures for EVPN over SRv6.
- **draft-liu-pce-pcep-tunnel-flowspec-01** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extension for Tunneled Flow Specification](https://datatracker.ietf.org/doc/draft-liu-pce-pcep-tunnel-flowspec/) — Traffic flows may be categorized and described using "Flow
   Specifications".  RFC8955 defines the Flow Specification and
   describes how Flow Specification components are used to describe
   traffic flows.  RFC8955 also defines how Flow Specifications may be
   distributed in BGP to allow specific traffic flows to be associated
   with routes.

   RFC 9168 specifies a set of extensions to PCEP to support the
   dissemination of Flow Specifications.  This allows a PCE to indicate
   what traffic should be placed on each path that it is aware of.

   The extensions defined in this document extend the support for
   tunneled traffic filtering rules.
- **draft-martinez-partial-content-uploads-00** (new-draft, score 0, ignored_after_review) [none]: [Partial Content Uploads in HTTP](https://datatracker.ietf.org/doc/draft-martinez-partial-content-uploads/) — The Hypertext Transfer Protocol (HTTP) is a stateless application-
   level protocol for distributed, collaborative, hypertext information
   systems.  This document defines partial content uploads, which allows
   a client to upload content, such as a large file, via multiple
   requests.  This document also outlines the metadata header fields for
   indicating state changes, request header fields for making
   preconditions on such state, and the rules for constructing the
   responses.
- **draft-mcnally-deterministic-cbor-18** (new-draft, score 0, ignored_after_review) [none]: [dCBOR: Deterministic CBOR](https://datatracker.ietf.org/doc/draft-mcnally-deterministic-cbor/) — The purpose of determinism is to ensure that semantically equivalent
   data items are encoded into identical byte streams.  CBOR (RFC 8949)
   defines "Deterministically Encoded CBOR" in its Section 4.2, but
   leaves some important choices up to the application developer.  The
   present document specifies dCBOR, a set of narrowing rules for CBOR
   that can be used to help achieve interoperable deterministic encoding
   for a variety of applications desiring a narrow and clearly defined
   set of choices.
- **draft-mcnally-envelope-12** (new-draft, score 0, ignored_after_review) [none]: [The Gordian Envelope Structured Data Format](https://datatracker.ietf.org/doc/draft-mcnally-envelope/) — Gordian Envelope specifies a structured format for hierarchical
   binary data focused on the ability to transmit it in a privacy-
   focused way, offering support for privacy as described in RFC 6973
   and human rights as described in RFC 8280.  Envelopes are designed to
   facilitate "smart documents" and have a number of unique features
   including: easy representation of a variety of semantic structures, a
   built-in Merkle-like digest tree, deterministic representation using
   CBOR, and the ability for the holder of a document to selectively
   elide specific parts of a document without invalidating the digest
   tree structure.  This document specifies the base Envelope format,
   which is designed to be extensible.
- **draft-pels-dnsop-axfr-notify-01** (new-draft, score 0, ignored_after_review) [none]: [AXFR message type for DNS NOTIFY](https://datatracker.ietf.org/doc/draft-pels-dnsop-axfr-notify/) — This document defines a new AXFR message type for DNS NOTIFY
   messages, together with an accompanying subtype for the ZONEVERSION
   EDNS(0) option.  The message instructs a secondary server to perform
   an AXFR zone transfer of a zone.
- **draft-rich-radext-wlan-security-profile-00** (new-draft, score 0, ignored_after_review) [none]: [RADIUS Attribute for IEEE 802.11 WLAN Security Profiles](https://datatracker.ietf.org/doc/draft-rich-radext-wlan-security-profile/) — RADIUS has attributes that let an IEEE 802.11 authenticator report
   the AKM suite and pairwise cipher selected for an association.  That
   is useful, but it is not enough anymore.  IEEE 802.11, as amended,
   also defines security profiles.  A security profile is the complete
   set of AKM, pairwise cipher, and related security capabilities
   accepted for an association.

   The problem is that the AKM and the pairwise cipher no longer maps to
   a single security profile.  Using these two values, the RADIUS server
   cannot tell which of the security profiles was accepted.

   This document defines the WLAN-Security-Profile RADIUS attribute.
   The attribute reports the IEEE 802.11 security profile accepted by
   the responder for the association.  It complements the existing IEEE
   802 network attributes.
- **draft-sa-idr-bgp-srv6-mpls-transport-iw-03** (new-draft, score 0, ignored_after_review) [none]: [BGP extensions for SRv6/MPLS Transport Interworking](https://datatracker.ietf.org/doc/draft-sa-idr-bgp-srv6-mpls-transport-iw/) — This document defines the BGP extensions required to provide
   transport interworking between SRv6 and MPLS in SRv6 deployment.
- **draft-sastry-spacerg-space-research-infra-typology-01** (new-draft, score 0, ignored_after_review) [none]: [A typology of Space Research Infrastructures](https://datatracker.ietf.org/doc/draft-sastry-spacerg-space-research-infra-typology/) — Space networking research increasingly relies on a heterogeneous
   ecosystem of software, datasets, experimental platforms, reference
   implementations, and operational research assets.  These resources
   have historically been developed independently by different research
   groups, agencies, and projects, making discovery, comparison,
   interoperability, and reuse difficult.  Existing registries typically
   catalogue tools individually but provide limited guidance on their
   functional role within the research lifecycle.

   This document proposes a typology for research infrastructures
   relevant to the Space Research Group (SPACERG).  The proposed
   taxonomy groups resources by the research function they serve,
   independently of their implementation technology or project origin.
   The typology provides a common vocabulary for describing software and
   non-software research assets, supports the organization of community
   registries, and facilitates interoperability, reproducibility, and
   long-term maintenance of research infrastructures.  The
   classification is intended to evolve as new classes of research
   resources emerge.  The typology is implemented by a machine-readable
   registry of research resources maintained by the research group.
- **draft-sayre-gendispatch-derivative-05** (new-draft, score 0, ignored_after_review) [none]: [Clarification of Derivative Works Restrictions](https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/) — This document clarifies that only IETF Documents may contain legal
   limitations on derivative works.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/.

   Discussion of this document takes place on the ipr-wg Working Group
   mailing list (mailto:ipr-wg@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/ipr-wg/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/ipr-wg/.
- **draft-singh-apex-psi-05** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi](https://datatracker.ietf.org/community/personal/acy.n.gel69@gmail.com/untrackdocument/draft-singh-apex-psi-05/)
- **draft-singh-apex-psi-06** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi](https://datatracker.ietf.org/community/personal/acy.n.gel69@gmail.com/untrackdocument/draft-singh-apex-psi-06/)
- **draft-smith-6man-accurate-ra-router-lifetime-05** (new-draft, score 0, ignored_after_review) [none]: [More Accurately Naming IPv6 RA Router Lifetime](https://datatracker.ietf.org/doc/draft-smith-6man-accurate-ra-router-lifetime/) — IPv6 Router Advertisements (RAs) have a "Router Lifetime" field,
   which specifies how long the advertising router will act as a default
   router for the receiving hosts, unless refreshed with another
   advertisement.  The field name "Router Lifetime" is quite general,
   and could easily be misunderstood to mean the bounded lifetime of all
   of the information contained in the RA.  This memo more accurately
   renames this field "Default Router Lifetime".
- **draft-vasters-json-structure-sem-ann-00** (new-draft, score 0, ignored_after_review) [none]: [JSON Structure: Semantic and Reference-System Annotations](https://datatracker.ietf.org/doc/draft-vasters-json-structure-sem-ann/) — Data types describe representation, but they do not explain the
   semantic, temporal, spatial, and operational characteristics needed
   to interpret and compare data.  This document defines optional JSON
   Structure annotations that bind schema nodes to terms in external
   vocabularies; annotations for observation results, observed
   properties, features of interest, procedures, time semantics,
   quality, derivation, and cadence; annotations for spatial referencing
   by coordinates, by vector and tensor reference frames, by
   transformations between frames, and along linear elements; and
   annotations for color spaces, audio channel layouts, spectral bands,
   code lists, and measurement conditioning.

   The annotations make an incompatibility between two data sets
   detectable by machine; they do not resolve one.  They are optional,
   and their absence does not make a schema invalid.
- **draft-westerbaan-dnssec-mldsa-04** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice Digital Signature Algorithm for DNSSEC](https://datatracker.ietf.org/doc/draft-westerbaan-dnssec-mldsa/) — This document describes how to specify Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) keys and signatures in DNS Security
   (DNSSEC).  It uses the ML-DSA-44 parameter set defined in FIPS 204.
   ML-DSA-44 is believed to be secure even against adversaries in
   possession of a cryptographically relevant quantum computer.
- **draft-wilaw-moq-cmcd-event-timeline-00** (new-draft, score 0, ignored_after_review) [none]: [CMCD transmission over MSF Event Timeline](https://datatracker.ietf.org/doc/draft-wilaw-moq-cmcd-event-timeline/) — Defines the transmission of CMCD data over MSF Event Timeline tracks.

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at
   https://wilaw.github.io/CMCD-over-MSF-event-timeline/draft-wilaw-moq-
   cmcd-event-timeline-latest.html.  Status information for this
   document may be found at https://datatracker.ietf.org/doc/draft-
   wilaw-moq-cmcd-event-timeline/.

   Source for this draft and an issue tracker can be found at
   https://github.com/wilaw/CMCD-over-MSF-event-timeline.
- **draft-xiao-fann-fast-cnp-with-proxy-02** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-zhang-rtgwg-llmmoe-multicast-03** (new-draft, score 0, ignored_after_review) [none]: [Multicast use case in LLM MoE](https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/) — Large Language Models (LLMs) have been widely used in recent years.
   The Mixture of Experts (MoE) architecture is one of the features of
   LLMs that enables efficient inference and cost-effective training.
   With the MoE architecture, there are potential multicast use cases
   such as tokens dispatching.  This draft attempts to analyze these use
   cases.

## Errors / fetch failures

- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
