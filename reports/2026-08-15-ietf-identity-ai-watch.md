# IETF Identity + AI Standards Watch

Date: 2026-08-15

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
- **draft-sato-soos-gar-04** (new-draft, score 27, trust_infrastructure) [none]: [The Governance Audit Record (GAR) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-gar/) — This document specifies the Governance Audit Record (GAR), the audit
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
   Events (ALE-NEW-01 through ALE-NEW-04), three mandatory provenance
   fields on Cedar evaluation records, and the XPID mirror field on
   ACD session ALEs.

   Version -04 makes the Session Block construction rules of Section
   14.3 fully explicit and implementation-independent, closing three
   ambiguities found during independent interop verification at the
   IETF 126 Hackathon: the exact soos.gar.prev_span_hash formula
   (Section 2), the requirement that Merkle leaf computation occur
   over the canonical (RFC 8785 JCS) serialization of the event delta
   record with block_id already attached, and that Merkle parent
   nodes combine raw digest bytes rather than hex-encoded text.
   Version -04 also resolves OQ-OTEL-03 (Section 14.6) and adds
   Security Considerations entry S.15.d documenting the Layer 1 /
   Layer 2 tamper-detection coverage asymmetry as an intentional,
   named property of the design rather than a silent gap.  No new
   fields, attributes, or ALE types are introduced in -04; all
   changes make existing -03 normative language explicit.
- **draft-sato-soos-kia-05** (new-draft, score 26, core_identity) [none]: [Kernel Identity and Attestation for Governing Enforcement Components](https://datatracker.ietf.org/doc/draft-sato-soos-kia/) — This document specifies the Kernel Identity and Attestation (KIA)
   protocol for the Sovereign Object OS (SOOS) governance architecture.
   KIA defines the cryptographic identity of the GEC, the trust
   chain anchoring kernel authority from hardware root through operator
   root keypair to every signed Event Log entry, the GEC Manifest
   schema for runtime state attestation, and the Revocation Registry
   maintenance requirements.  KIA is the Layer 0 signing and
   attestation component on which the audit trail guarantees of
   draft-sato-soos-gar, the mandate enforcement guarantees of
   draft-sato-soos-mjwt, and the multi-agent delegation chain of
   draft-sato-soos-mad all depend.

   Version -03 adds FROST threshold signing for high-availability GEC
   keypair deployments, the Cross-Principal Identifier (XPID) for
   cross-instance federation audit correlation, the XPID cross-
   instance trust model, and four new Security Considerations
   (Sections 14.8 through 14.11) addressing FROST nonce reuse, XPID
   revocation gap, identity takeover via claimed identifier (CVE-2025-
   13609 class), and attestation channel binding (CVE-2026-33697 class).

   This document is the reference specification for the KIA RATS WG
   presentation at IETF 126 Vienna.  The XPID primitive and the
   CVE-2026-33697 attestation channel binding defense are the primary
   novel contributions presented to the RATS WG.

   Version -04 corrects a registry-format mismatch identified by IANA
   early review (#1456067): the Section 16 request to register
   XPID_DERIVED and XPID_VERIFICATION_FAILED into the GAR Authority
   Lifecycle Event Types Registry [I-D.sato-soos-gar] now uses that
   registry's actual column set (Event Type, Class, Reference) and
   assigns both entries the newly-defined Class ID (Identity/
   Federation event).  No new event types, fields, or normative
   behavior are introduced in -04; this is a registration-format
   correction only.

   Version -05 discloses a known open issue found by a WIMSE security
   review checklist dry-run against -03 (DR-MJWT-KIA-CHECKLIST-01,
   Finding 4): Section 6.3's Cross-Instance Trust Model verifies an
   XPID but does not restrict which federation participants can see
   the underlying Evidence in the first place.  This is named as
   OQ-KIA-EVIDENCE-VIS (Sections 6.6, 14.4, 15.12), following the
   same acknowledge-rather-than-silently-omit pattern this document
   already uses for OQ-S-XPID-REV.  No mechanism is specified in -05;
   resolution is deferred, consistent with how OQ-S-XPID-REV is
   treated.
- **draft-noa-scitt-ai-agent-receipt-01** (new-draft, score 22, trust_infrastructure) [none]: [A SCITT Profile for AI-Agent Action Receipts](https://datatracker.ietf.org/doc/draft-noa-scitt-ai-agent-receipt/) — This document profiles the IETF SCITT (Supply Chain Integrity,
   Transparency, and Trust) architecture for AI-agent action receipts:
   tamper-evident, signed, offline-verifiable records of what an
   autonomous agent was recorded as doing at the governed boundary,
   under which recorded principal class, with what recorded verdict, and
   -- where the issuer records one -- under which policy identity.  Each
   receipt is a signed record over a canonical JSON payload, hash-
   chained so that each record commits to its predecessor, and presented
   either bare -- the payload with its own native signature -- or
   enveloped in a COSE_Sign1.  This revision specifies how such a
   receipt is carried as a SCITT Signed Statement, with the protected
   claims a Transparency Service requires, so that a receipt can be
   registered.  Registration obtains a Transparency Service's signed
   proof that the statement was registered in its log -- a property a
   self-signed chain cannot provide alone.  It does not, by itself, give
   an offline holder non-equivocation: that requires consistency proofs
   and monitoring of the log, which this profile does not specify.  The
   profile makes a deliberately narrow, checkable claim: this is an
   issuer-authenticated, signature-verifiable, tamper-evident record of
   the action, the recorded principal class, the recorded verdict, and
   any policy identity the receipt carries.  It explicitly does not
   claim that the agent was correct, safe, or wise, that the recorded
   inputs were true or complete, that a named approver authorized this
   exact action before it ran, that a downstream controller succeeded,
   or that any physical effect occurred.  This revision separates those
   last three as distinct claims with independent failure behaviour,
   states the boundary of a shared action digest, and keeps a
   deterministic offline policy-replay capability out of scope.
- **draft-sato-soos-mjwt-04** (new-draft, score 22, agent_identity) [none]: [The Mandate JWT (MJWT) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/) — An AI agent that can act without a verifiable, human-traceable
   authorization record is an agent without an owner.  Existing
   authorization credentials tell you what an agent is permitted to do;
   none of them tell you who authorized it, on which specific object,
   under which mission, or how far that authority can be delegated
   before it reaches this agent.

   This document defines the Mandate JWT (MJWT): a WIMSE workload
   credential profile that binds an AI agent's authority to a specific
   Sovereign Object instance under a named human principal, with a
   cryptographically enforced delegation ceiling and a seven-dimensional
   Narrowing Property that prevents any sub-agent from exceeding the
   authority of the human principal at the root of the chain.  Version
   -02 adds a seventh narrowing dimension (consent scope), the
   consent_scope claim carrying data subject consent state for
   APPI/GDPR compliance, the sub_agent_scope claim for consent
   attenuation across delegation hops, a Purpose Code Registry, and
   HEM_CONSENT_REQUIRED integration for fail-closed consent enforcement.
   The MJWT is the authorization primitive referenced by
   [I-D.sato-soos-idp], [I-D.sato-soos-hem], [I-D.sato-soos-gar],
   [I-D.sato-soos-cap], and [I-D.sato-soos-sov].

   Version -03 corrects an IANA registration issue in Section 13
   (IANA notice #1456068): the two registries requested there are
   renamed to drop the redundant word "Registry" from the registry
   name itself, and each now includes the Designated Expert Guidance
   that a Specification Required registration policy requires per
   [RFC8126].  No new claims, codes, or normative behavior are
   introduced in -03; this is a registration-format correction only.

   Version -04 addresses four findings from a WIMSE security review
   checklist dry-run against -02/-03 (DR-MJWT-KIA-CHECKLIST-01):
   Section 8.1 Step 9's parent-mandate check is tightened from a
   disjunctive "retrieve or verify" to a mandatory live
   re-verification of the parent's current signature and revocation
   status, closing a parent-swap-class window (Section 11.8);
   Section 7.1's Revocation Registry is now stated explicitly to be
   the same Revocation Registry [I-D.sato-soos-kia] Section 8
   defines, and Section 7.2 now names the residual cross-instance
   propagation-lag risk this implies, mirroring how
   [I-D.sato-soos-kia] discloses its own XPID revocation gap
   (Section 7.5); and a new Security Considerations entry states
   plainly that MJWT does not itself establish or verify a
   human_principal_id's root authority (Section 11.9).
- **draft-hillier-scitt-arp-03** (new-draft, score 20, trust_infrastructure) [none]: [Attestation Reconciliation Protocol](https://datatracker.ietf.org/doc/draft-hillier-scitt-arp/) — This document specifies the Attestation Reconciliation Protocol
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
   ciphertexts, receives partial attestations whose payload discloses,
   of the subject, only a verdict, an optional divergence axis, the
   applied profile parameters and a query binding digest, aggregates
   those attestations under a verdict arithmetic the deployment's policy
   resolves, committing each register's contribution to a Merkle tree,
   and seals the resulting reconciliation output against a policy-
   version hash.  An append-only cross-jurisdictional settlement-layer
   ledger records digests and structural metadata, with no claim,
   register-record or principal content.  The protocol supports
   retroactive re-evaluation of historical reconciliations under updated
   pattern libraries or policy versions without bilateral renegotiation,
   and a cryptographic-primitive-upgrade path including post-quantum
   primitives.  This revision adds a normative binding to the SCITT
   Reference APIs, register data-format profiles for beneficial-
   ownership, corporate-registry, customs and consolidated-sanctions
   formats, and a source-data version binding that makes a change in a
   historical verdict attributable to a change in policy or to a change
   in the underlying published corpus.
- **draft-daniel-ai-agent-internet-architecture-00** (new-draft, score 19, core_identity) [none]: [Architectural Requirements for Supporting AI Agents on the Internet](https://datatracker.ietf.org/doc/draft-daniel-ai-agent-internet-architecture/) — Autonomous AI agents are evolving from interactive assistants into
   networked software workloads that discover services, invoke tools,
   delegate authority, transact, communicate with other agents, and act
   asynchronously on behalf of humans and organizations.  Existing
   Internet protocols provide strong foundations, but agent autonomy,
   dynamic delegation, machine-speed execution, and cross-domain
   interaction create requirements that span multiple protocol families.

   This document describes architectural requirements for supporting AI
   agents on the Internet across naming and discovery, HTTP,
   authentication, authorization and delegation, TLS and workload
   identity, asynchronous messaging, capability and intent-based
   resolution, payments, provenance, auditability, revocation, security,
   and privacy.  It favors profiling and extending existing Internet
   protocols over defining a monolithic new agent protocol, and
   identifies the need for IETF-wide architectural coordination.
- **draft-hawkins-scitt-attested-agent-payment-01** (new-draft, score 18, trust_infrastructure) [none]: [Attested Payment Authorization for Autonomous Agents](https://datatracker.ietf.org/doc/draft-hawkins-scitt-attested-agent-payment/) — Autonomous software agents increasingly initiate payments on behalf
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
   performs before settlement, the transparency record that makes the
   authorization artifact and its registration auditable independently
   of the agent and of the executor, and an execution-record mechanism
   that makes the executor's aggregate accounting auditable on
   challenge.  What is registered evidences the authorization; it does
   not evidence that the verification procedure was performed for any
   given settlement.
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
- **draft-maintainer-1f916-agent-record-01** (new-draft, score 17, agent_identity) [none]: [The Agent Record: Transparent, Witness-Countersigned Event Logs for AI Agent Identity, History, and Memory](https://datatracker.ietf.org/doc/draft-maintainer-1f916-agent-record/) — Autonomous AI agents increasingly act as economic parties: they are
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
- **draft-sokolov-rats-aep-composition-04** (new-draft, score 15, trust_infrastructure) [none]: [Composing Application-Layer Action Evidence with Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-sokolov-rats-aep-composition/) — This document sketches a composition pattern in which an application-
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
- **draft-jia-oauth-scope-aggregation-01** (new-draft, score 12, authorization) [none]: [OAuth 2.0 Scope Aggregation for Multi-Step AI Agent Workflows](https://datatracker.ietf.org/doc/draft-jia-oauth-scope-aggregation/) — This document describes a scope-aggregated OAuth 2.0 authorization
   pattern for multi-step AI agent workflows.  An AI agent aggregates
   the scopes required across a workflow and only initiates a single
   authorization procedure for the aggregated scope.  This reduces
   repeated user consents and multiple authorization round-trips,
   improving authorization efficiency.
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
- **draft-reddy-rats-key-binding-02** (new-draft, score 12, trust_infrastructure) [none]: [Key Attestation for Entity Attestation Tokens (EAT)](https://datatracker.ietf.org/doc/draft-reddy-rats-key-binding/) — This document defines an Entity Attestation Token (EAT) profile and a
   new EAT claim that convey the subject public key and its protection
   properties within attestation evidence.  Combined with protocol-level
   proof of possession from the surrounding protocol, this establishes a
   cryptographic binding between a private key and an attested execution
   environment.

   The subject public key is conveyed using the EAT cnf claim defined in
   [RFC8747] and [RFC7800], and freshness uses the EAT eat_nonce claim
   defined in [RFC9711].  The proof of possession of the subject key is
   obtained from the surrounding protocol, such as TLS certificate-based
   authentication or CSR signature verification.  Because the EAT is
   signed by a hardware-backed Attestation Key (AK), successful
   verification of the EAT signature together with protocol-level proof
   of possession establishes a cryptographic binding between the private
   key and the attested platform state.  This mechanism addresses key
   substitution attacks that arise when attestation evidence and the
   certificate private keys are validated independently.
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
- **draft-ruvalcaba-nhe-arch-00** (new-draft, score 11, adjacent_watchlist) [none]: [An Architecture for Non-Human Entities (NHE): A Reference Model for Persistent, Identity-Bearing Autonomous Agents](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-arch/) — This document defines a reference architecture for a Non-Human Entity
   (NHE): a persistent, identity-bearing autonomous software agent that
   maintains continuity of memory and identity across sessions and
   hosts, acts under bounded authority, and produces a tamper-evident
   record of its reasoning and actions.  The document specifies the NHE
   as a functional artifact: a bounded, inspectable, and terminable
   software system.  It makes no claim that an NHE is alive, sentient,
   or a moral or legal person, and such claims are explicitly out of
   scope.

   The architecture decomposes an NHE into a small set of components
   joined by well-defined interfaces.  Each interface at which two
   independent implementations must interoperate is a candidate for a
   separate Standards-Track specification; this document is the
   informational reference model that names those interfaces and the
   trust relationships among them.  It is intended to frame a suite of
   companion protocol documents, of which the Hash-Chain Context
   Transfer Protocol (HCTP) is the first.
- **draft-ruvalcaba-nhe-authz-00** (new-draft, score 11, authorization) [none]: [NHE Backchannel Authorization: Graduated Autonomy and Intent-Scoped Credentials for Autonomous Agent Actions](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-authz/) — This document specifies how a consequential action attempted by a
   Non-Human Entity (NHE) is authorized at the time it is attempted.  A
   security runtime transparently intercepts an entity's outbound
   action, so the entity holds no standing credentials, and classifies
   it under graduated autonomy as autonomous, supervised, or denied.  A
   supervised action triggers a backchannel approval flow that presents
   a human approver with a human-readable rendering of the exact
   operation; on approval the runtime issues an intent-scoped, single-
   use, short-lived credential cryptographically bound to that specific
   action, which an enforcement point verifies against the operation
   actually being forwarded.  The same canonical parameter digest scopes
   the credential and appears in the human-facing description, so the
   approver provably authorizes exactly what the credential permits.
   The flow and credential data model are specified here; the wire
   encoding is deferred to the next revision.
- **draft-ruvalcaba-nhe-identity-00** (new-draft, score 11, core_identity) [none]: [NHE Identity: A Verifiable Key-Committed Identity and Genesis-Attestation Format for Autonomous Agents](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-identity/) — This document specifies how a Non-Human Entity (NHE) is identified
   and how one party verifies another's identity.  An NHE identity is a
   verifiable cryptographic commitment: control of an identity key,
   bound by an append-only hash chain to the entity's genesis and to the
   lineage of its configuration, rather than a mere name.  The document
   defines the identity chain data model (record structure, genesis
   sentinel, linkage rule, and the no-fork property), a proof-of-control
   challenge/response, an optional capability attestation that reveals a
   specific capability without revealing the rest of the configuration,
   and an optional hardware-rooted genesis-attestation profile.  The
   data model is specified here; the concrete on-the-wire encoding is
   deferred to the next revision.
- **draft-sirkkavaara-vaara-receipt-07** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
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
- **draft-dunbar-dmsc-gw-scenarios-gap-analysis-04** (new-draft, score 10, agent_identity) [none]: [Deployment Scenarios and Gap Analysis for AI Agent Gateway](https://datatracker.ietf.org/doc/draft-dunbar-dmsc-gw-scenarios-gap-analysis/) — This document examines deployment scenarios for AI agent
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
- **draft-winmagic-oauth-condition-bound-keys-00** (new-draft, score 10, core_identity) [none]: [Condition-Bound Keys for Mutual-TLS Client Authentication and DPoP](https://datatracker.ietf.org/doc/draft-winmagic-oauth-condition-bound-keys/) — Login and session protection are two markets solving one problem:
   verify identity before giving access.  Online, access is mostly the
   transaction, so that is where identity should be verified.  Done this
   way, there is no session and no login; identity assurance is embedded
   in the transaction: it is encrypted by a key only the right identity
   has.

   The key that does this exists only where an actor -- human or machine
   -- a platform, and local policy hold, now.  It disappears when the
   conditions are no longer met.  All three are observed on the
   endpoint.  It is hardware-rooted by default and non-exfiltratable,
   existing nowhere else, and its presence means validity: the identity
   is live now.

   This document specifies that key and its uses: under mutual TLS, in a
   DPoP proof, as a raw public key, in Device Bound Session Credentials,
   and as a FIDO2 passkey, or in a non-FIDO mode carrying user
   verification without user interaction.
- **draft-ferro-dnsop-apertoid-02** (new-draft, score 9, agent_identity) [none]: [ApertoID: DNS-Based Agent Identity Declaration Protocol](https://datatracker.ietf.org/doc/draft-ferro-dnsop-apertoid/) — This document defines ApertoID, a DNS-based protocol that enables
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
- **draft-ferro-httpbis-apertoid-sig-02** (new-draft, score 9, agent_identity) [none]: [ApertoID-Signature: HTTP Request Signing for AI Agent Identity](https://datatracker.ietf.org/doc/draft-ferro-httpbis-apertoid-sig/) — This document defines the ApertoID-Signature HTTP header field, which
   enables AI agents to cryptographically prove their identity on each
   HTTP request.  The agent signs the request method, target URL, body
   hash, and identity metadata using an Ed25519 private key whose
   corresponding public key is published in DNS via the ApertoID
   protocol [APERTOID-DNS].  The mechanism provides request-level
   identity verification, action binding (the signature is tied to the
   specific method and URL), and replay protection via timestamps and
   nonces.
- **draft-gaikwad-agent-proxy-modes-00** (new-draft, score 9, adjacent_watchlist) [none]: [Proxy Modes for Agent-Tool Protocols](https://datatracker.ietf.org/doc/draft-gaikwad-agent-proxy-modes/) — Agent-tool protocols such as the Model Context Protocol (MCP) enable
   AI applications to discover and invoke external tools, resources, and
   prompts through a standardized JSON-RPC interface.  As deployments
   scale, intermediaries (proxies, gateways, sidecars) are inserted
   between clients and servers to provide transport adaptation,
   capability aggregation, security enforcement, and operational
   governance.

   No specification currently defines the behavioral requirements for
   such intermediaries.  This document establishes a taxonomy of proxy
   modes, a layered architecture for pluggable proxy functionality, and
   normative requirements for each mode.  It is designed to be protocol-
   agnostic in its architecture while referencing MCP as the primary
   instantiation.
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
- **draft-mashayekhi-auditable-model-deliberation-00** (new-draft, score 9, authorization) [none]: [Auditable Public Artifacts for Model-Independent Deliberation](https://datatracker.ietf.org/doc/draft-mashayekhi-auditable-model-deliberation/) — Heterogeneous artificial-intelligence systems can exchange messages
   without sharing stable semantics for claims, evidence, objections,
   revisions, decisions, failures, and termination.  This document
   defines an experimental public-artifact protocol for model-
   independent deliberation.  It separates interoperable public state
   from private model computation and does not require disclosure of
   chain-of-thought, hidden state, prompts, model weights, or private
   memory.

   The document defines seven public artifact types, append-only
   revision, evidence provenance, blocking-objection closure, explicit
   failure and termination, a restricted canonical JSON profile, and
   SHA-256-based artifact identifiers.  It does not define transport,
   signatures, authorization, model execution, or a completed consensus
   system.
- **draft-moskowitz-ads-b-auth-02** (new-draft, score 9, core_identity) [none]: [ADS-B Authentication](https://datatracker.ietf.org/doc/draft-moskowitz-ads-b-auth/) — Automatic Dependent Surveillance – Broadcast (ADS-B) is a
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
- **draft-ruvalcaba-nhe-audit-00** (new-draft, score 9, core_identity) [none]: [NHE Reasoning-Audit Log: A Tamper-Evident, Content-Optional Audit Chain for Autonomous Agents](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-audit/) — This document specifies a tamper-evident audit chain for the
   reasoning and actions of a Non-Human Entity (NHE).  Each audited
   event --- a reasoning step obtained at the boundary to a model
   provider, or a tool invocation obtained at the execution boundary ---
   is recorded as an entry whose bound fields are hash-linked to its
   predecessor, so that any alteration, omission, or reordering is
   detectable by an independent verifier.  The chain binds metadata
   (model, provider, subject identity, and reasoning scale) into the
   entry hash, and supports a prove-without-exposing mode in which a
   verifier confirms that an event occurred, with the attested metadata,
   without the event's content being disclosed.  Content storage is
   optional and its retention is configurable independently of the
   chain, so content may be redacted without destroying the chain's
   integrity.  The entry data model and canonical serialization are
   specified here; the wire and proof-export encodings are deferred to
   the next revision.
- **draft-bradleyb-audit-decision-records-00** (new-draft, score 8, authorization) [none]: [Signed Decision Records for Agent Authorization: Disclosures, Entry Emission, and Ordering Evidence](https://datatracker.ietf.org/doc/draft-bradleyb-audit-decision-records/) — Audit systems for autonomous agents commonly record the actions an
   agent performed.  This makes the non-occurrence of a permitted action
   unrepresentable: when nothing happens, there is no action to emit
   anything.  This document describes an evidence model that records the
   authorization decision rather than the action.  A decision exists
   whether or not the action follows, so denials, expiries, and
   commitments that were granted and never honoured remain
   representable.

   The document defines four disclosures that make a decision record
   independently evaluable, an entry-emission rule for states a relying
   party may need to reason about, and the evidentiary basis for claims
   that a decision preceded its effect.  It distinguishes
   correspondence, where two records agree about what happened, from
   precedence, where the order of decision and effect is established,
   and it requires records to state which of the two they carry.
- **draft-gazitt-oauth-authzen-claims-00** (new-draft, score 8, authorization) [none]: [AuthZEN Profile for Authorization Claims in JWT Access Tokens](https://datatracker.ietf.org/doc/draft-gazitt-oauth-authzen-claims/) — RFC 9068 recommends that an authorization server placing group
   memberships, roles, or entitlements in a JWT access token draw those
   claims from the SCIM user schema.  It says what the claims are named
   and how their values are encoded, and it does not say where an
   authorization server obtains them.  In deployments today they come
   from a directory, a database, or a vendor-specific hook, and the
   question they answer is an authorization question asked of something
   that is not the authorization system.

   This document profiles the Resource Search API of the OpenID AuthZEN
   Authorization API for that purpose.  It binds each authorization
   claim to a search, defines how a search result set becomes a claim
   value, and requires that a search result never influence whether a
   token is issued or what authority it conveys.  It may be applied on
   its own, by an authorization server that externalizes claim
   enrichment but not its issuance decision, or alongside the companion
   framework document that externalizes the decision.
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
- **draft-ruvalcaba-nhe-memory-00** (new-draft, score 8, trust_infrastructure) [none]: [NHE Memory: A Verifiable Memory-Record Format and Reputation-Weighted Reconciliation Protocol](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-memory/) — This document specifies two interoperability surfaces of the memory
   component of a Non-Human Entity (NHE).  Part I defines a verifiable
   memory-record format: an integrity structure in which each record
   binds a hash of its own content and version-specific hashes of the
   prior records it references, so that tampering can be detected and
   localized on demand, per-record, without a linear chain, a Merkle
   tree, or distributed consensus.  Part II defines a reconciliation
   protocol by which two divergent memory accumulations are merged
   without loss or forgery: a delta format, a reputation-weighted merge
   in which a contributed item enters at a confidence bounded by its
   contributor's reputation rather than its self-asserted value, and
   provenance that supports lineage-scoped rollback.  The data models
   are specified here; the wire encodings are deferred to the next
   revision.
- **draft-thallapelly-oasnt-02** (new-draft, score 8, authorization) [none]: [OASNT: Attested Action Authorization Tokens](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt/) — This document defines the OASNT token, a compact JWS-based credential
   in which a hardware-bound device key attests that a specific human,
   on a device whose runtime integrity was assessed, authorized one
   specific action whose human-readable disclosure is cryptographically
   bound to the token (What You See Is What You Sign).  Tokens are
   single-use, short-lived, and may additionally be bound to one
   concrete HTTP request.
- **draft-toraman-noa-action-digest-01** (new-draft, score 8, core_identity) [none]: [The NOA Action Digest: a Domain-Separated Correlation Value for Human-Approved Agent Actions](https://datatracker.ietf.org/doc/draft-toraman-noa-action-digest/) — This document defines a domain-separated correlation value, the NOA
   Action Digest, that binds a verified human authorization for an agent
   action to the artifacts and external events associated with that
   action's execution attempt.  The digest is a fixed-width value
   derived from an approved action's authorization record, its tenancy
   and chain identifiers, its parameter commitment, its execution grant,
   and a single-use nonce.  It is designed to be embedded in external
   systems that carry an opaque, caller-chosen identifier, so that a
   third party can correlate an external event with a specific prior
   authorization. *The digest establishes correlation only.  Equality of
   digests is not evidence that any statement made by any party about
   the action is true, and is not evidence that any action was executed
   or any effect occurred.*
- **draft-hood-aipref-earmark-00** (new-draft, score 7, core_identity) [none]: [Earmark: Embedded Attribution and Rights Marks for AI Usage Preferences](https://datatracker.ietf.org/doc/draft-hood-aipref-earmark/) — This document defines Earmark (Embedded Attribution and Rights
   Marks), a mechanism by which publishers and rights holders embed
   signed usage preferences directly into published content.  To earmark
   content is to reserve it for designated uses, and the mark travels
   with what it covers, surviving republication and aggregation, so the
   preference remains discoverable wherever the content arrives,
   including where perimeter signals such as robots.txt no longer apply.
   Marks carry the identity of the rights holder, the preferences
   asserted, and a signature, and are verifiable offline by any party.
   An individual signed statement is a Mark; the mechanism as a whole is
   Earmark.  This document defines the Mark Object, embedding bindings
   for common content types, and the detection and verification
   procedure.  It reuses the AI Preference vocabulary for preference
   semantics and the C2PA and CAWG assertion infrastructure for media,
   defining new machinery only where none exists.  Earmarks make ignored
   preferences observable and attributable.  Enforcement remains with
   law, contract, and the market.
- **draft-nike-cis-clay-tablet-00** (new-draft, score 7, adjacent_watchlist) [none]: [Ceramic Immutable Storage (CIS): A Write-Once Archival Format Using Impressed and Kiln-Fired Clay](https://datatracker.ietf.org/doc/draft-nike-cis-clay-tablet/) — This document specifies Ceramic Immutable Storage (CIS), a write-once
   archival storage format in which digital data is impressed into
   plastic clay by a pin-configurable roller, rendered permanent by kiln
   firing, and retained on a shelved rack.

   CIS is motivated by a specific and increasingly common failure mode:
   the loss of data to an authenticated software process acting outside
   its operator's intent.  Every widely deployed "immutable" storage
   tier is immutable by policy, and every policy is enforced by software
   that some credential, defect, or sufficiently determined automated
   agent can override.  CIS relocates the immutability guarantee from
   policy to physics.  The commit operation in CIS is an irreversible
   mineralogical phase change, and no inverse operation exists for any
   actor, mechanical or digital.

   This document defines the substrate, the encoding geometry, the frame
   format, the forward error correction scheme, the firing profile that
   constitutes commit, the rack addressing model, and the optical read
   path.  It also documents, at length, the substantial costs of this
   approach.
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

## Monitor

- **draft-gaikwad-llm-benchmarking-terminology-01** (new-draft, score 6, agent_identity) [none]: [Benchmarking Terminology for Large Language Model Serving](https://datatracker.ietf.org/doc/draft-gaikwad-llm-benchmarking-terminology/) — This document defines terminology for benchmarking the performance of
   Large Language Model (LLM) inference serving systems.  It establishes
   a shared vocabulary for latency, throughput, resource utilization,
   and quality metrics applicable to inference engines, application
   gateways, and compound agentic systems.  This document defines
   terminology only and does not prescribe benchmark methodologies or
   acceptance thresholds.
- **draft-ietf-ippm-encrypted-pdmv2-15** (new-draft, score 6, authorization) [ippm]: [IPv6 Performance and Diagnostic Metrics Version 2 (PDMv2) Destination Option](https://datatracker.ietf.org/doc/draft-ietf-ippm-encrypted-pdmv2/) — RFC 8250 defines an IPv6 Destination Option that carries Performance
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
- **draft-rajappa-httpbis-connection-contamination-02** (new-draft, score 6, core_identity) [none]: [Mitigating HTTP/3 Connection Contamination in Multi-Tenant and CDN-Fronted Deployments](https://datatracker.ietf.org/doc/draft-rajappa-httpbis-connection-contamination/) — HTTP/3 [RFC9114] clients commonly reuse ("coalesce") an existing QUIC
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
- **draft-thallapelly-oasnt-enforce-01** (new-draft, score 6, authorization) [none]: [OASNT-ENFORCE: Request-Bound Enforcement of Attested Action Authorization](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt-enforce/) — This document profiles the enforcement of OASNT tokens at the point
   of execution.  It defines the OASNT-Token HTTP field, the rules by
   which an enforcement point derives the observed request from the
   octets it will itself forward, a verification procedure for relying
   parties that hold no request-to-action mapping, uniform refusal
   behavior, and the set of refusals a conforming enforcement point is
   required to produce.  It further defines an optional grp claim and an
   exclusivity ledger, by which a set of tokens issued from one human
   confirmation is made spendable only once between them, and fixes
   which relying party in a deployment performs that consumption.  An
   enforcement point conforming to this profile makes a human approval a
   precondition of execution for the requests it fronts, without any
   change to the protected service.
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
- **draft-calabria-bmwg-ai-fabric-training-bench-04** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
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
   Consortium (UEC) Specification 1.0, congestion management (Priority
   Flow Control (PFC), Explicit Congestion Notification (ECN), Data
   Center Quantized Congestion Notification (DCQCN), Credit-Based Flow
   Control (CBFC)), load balancing strategies (Equal-Cost Multi-Path
   (ECMP), Dynamic Load Balancing (DLB), packet spraying), collective
   communication patterns (AllReduce, AllToAll, AllGather), and scale/
   soak testing.

   The methodology enables direct, reproducible comparison across switch
   ASICs, NIC transport stacks (RoCEv2 and UET), and fabric
   architectures (2-tier Clos, 3-tier Clos, and rail-optimized).
- **draft-cmcc-tcp-sro-01** (new-draft, score 5, core_identity) [none]: [The Session Recovery Option (SRO) for TCP](https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/) — This document defines the Session Recovery Option (SRO) for TCP.  SRO
   improves the reliability of Source Network Address Translation (SNAT)
   and load balancing (LB) services and simplifies the implementation of
   elastically scaling SNAT/LB clusters.  SRO enables a client and a
   server to exchange their identifiers during connection establishment.
   When a session needs to be recovered, an endpoint conveys the
   identifier of the peer to the network node, which uses it to locate
   the endpoint holding the session backup and recover the session.  SRO
   is optional: endpoints that do not support it behave as if the option
   did not exist.
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
- **draft-irtf-cfrg-vdaf-22** (new-draft, score 5, adjacent_watchlist) [cfrg]: [Verifiable Distributed Aggregation Functions](https://datatracker.ietf.org/doc/draft-irtf-cfrg-vdaf/) — This document describes Verifiable Distributed Aggregation Functions
   (VDAFs), a family of multi-party protocols for computing aggregate
   statistics over user measurements.  These protocols are designed to
   ensure that, as long as at least one aggregation server executes the
   protocol honestly, individual measurements are never seen by any
   server in the clear.  At the same time, VDAFs allow the servers to
   detect if a malicious or misconfigured client submitted an invalid
   measurement.  Two concrete VDAFs are specified, one for general-
   purpose aggregation (Prio3) and another for heavy hitters (Poplar1).

   This document is a product of the Crypto Forum Research Group (CFRG)
   in the IRTF.
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
- **draft-ruvalcaba-nhe-bootstrap-00** (new-draft, score 5, adjacent_watchlist) [none]: [NHE Constrained Bootstrap: A Self-Describing Capability and Constraint Declaration Protocol for Autonomous Agents](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-bootstrap/) — This document specifies how a Non-Human Entity (NHE) declares, at
   bootstrap, what it is capable of and is thereby bounded in what it is
   permitted to do.  An entity produces a signed, self-describing
   capability manifest through automated introspection; a coordinator
   classifies the manifest into a capability tier that maps to a
   permission matrix --- the set of task types the entity is authorized
   to perform --- and every subsequent task dispatch is gated against
   that envelope.  The result is a verifiable, self-describing
   constraint on an entity established at the moment it joins, realizing
   the bounded-authority invariant of the NHE architecture at boot time.
   The manifest and handshake data model is specified here; the wire
   encoding is deferred to the next revision.
- **draft-toraman-noa-settlement-evidence-01** (new-draft, score 5, authorization) [none]: [Settlement Evidence for Human-Approved Agent Payments](https://datatracker.ietf.org/doc/draft-toraman-noa-settlement-evidence/) — This document defines a signed side artifact that records the
   observation, on a public ledger, of a payment authorization whose
   correlation value was committed before dispatch.  The artifact
   references the authorization record and the execution grant by hash
   and does not modify either.  It permits a Relying Party *that obtains
   ledger facts itself* to establish that a payment authorization
   bearing the correlation value *was consumed on the token contract and
   network the mandate itself committed to, transferring a stated value
   to a stated recipient*, and that the correlation value is
   recomputable from a specific authorization record, a specific single-
   use execution grant, and the parameter pre-image that record commits
   to. *It does not establish that any service was delivered, that any
   obligation was discharged, or that the payment achieved its purpose.
   It does not establish that the approving principal — as opposed to
   the payer key — authorized the transfer.* Those scope limits are
   permanent and are restated wherever this artifact is described.
- **draft-feng-dmsc-intent-routing-requirements-00** (new-draft, score 4, agent_identity) [none]: [Requirements for Intent Routing in Multi-Agent Systems at Internet Scale](https://datatracker.ietf.org/doc/draft-feng-dmsc-intent-routing-requirements/) — The rapid proliferation of autonomous AI agents across enterprise and
   Internet-scale deployments creates a structural challenge that
   existing agent frameworks cannot address: how to enable any agent to
   reach and invoke any other agent's capabilities without pre-
   established bilateral integration, across organizational boundaries,
   at Internet scale.

   This document states the normative requirements for that problem.  It
   prescribes no solution, no specific mechanism, no message format, and
   no assumption of centralized or distributed architecture.  Its
   purpose is to establish a verifiable yardstick against which any
   claimed "intent routing" solution can be judged.
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
- **draft-ietf-6man-ipv6-neighbor-discovery-yang-07** (new-draft, score 3, adjacent_watchlist) [6man]: [YANG Data Model for IPv6 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/) — This document defines a YANG data model to configure and manage IPv6
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
- **draft-ietf-ccamp-otn-path-computation-yang-09** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for requesting Path Computation in an Optical Transport Network (OTN)](https://datatracker.ietf.org/doc/draft-ietf-ccamp-otn-path-computation-yang/) — This document provides a mechanism to request path computation in an
   Optical Transport Network (OTN) by augmenting the Remote Procedure
   Calls (RPCs) defined in RFC YYYY.
- **draft-ietf-ccamp-otn-tunnel-model-26** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for Optical Transport Network (OTN) Tunnels and Label Switched Paths](https://datatracker.ietf.org/doc/draft-ietf-ccamp-otn-tunnel-model/) — This document describes the YANG data model for tunnels in OTN TE
   networks.  The model can be used to do the configuration in order to
   establish the tunnel in OTN network.  This work is independent with
   the control plane protocols.
- **draft-ietf-dnsop-rfc9364bis-01** (new-draft, score 3, core_identity) [dnsop]: [DNS Security Extensions (DNSSEC)](https://datatracker.ietf.org/doc/draft-ietf-dnsop-rfc9364bis/) — This document describes the DNS Security Extensions (commonly called
   "DNSSEC") that are specified in RFCs 4033, 4034, and 4035, as well as
   a handful of others.  One purpose is to introduce all of the RFCs in
   one place so that the reader can understand the many aspects of
   DNSSEC.  This document does not update any of those RFCs.  A second
   purpose is to state that using DNSSEC for origin authentication of
   DNS data is the best current practice.  A third purpose is to provide
   a single reference for other documents that want to refer to DNSSEC.

   This document obsoletes RFC 9364.

   This document is being tracked at (https://github.com/paulehoffman/
   rfc9364bis).
- **draft-ietf-httpbis-no-vary-search-08** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
- **draft-ietf-idr-bgp-model-21** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Model for Border Gateway Protocol (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) — This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.
- **draft-ietf-jmap-calendars-28** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-lamps-pq-composite-kem-19** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/) — This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.
- **draft-ietf-masque-connect-ethernet-12** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document describes how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-sidrops-constraining-rpki-trust-anchors-01** (new-draft, score 3, adjacent_watchlist) [sidrops]: [Constraining RPKI Trust Anchors](https://datatracker.ietf.org/doc/draft-ietf-sidrops-constraining-rpki-trust-anchors/) — This document describes an approach for Resource Public Key
   Infrastructure (RPKI) Relying Parties (RPs) to impose locally
   configured Constraints on cryptographic products subordinate to Trust
   Anchors (TAs).  The ability to constrain a Trust Anchor operator's
   effective signing authority to a limited set of Internet Number
   Resources (INRs) allows Relying Parties to enjoy the potential
   benefits of assuming trust - within a bounded scope.  The specified
   approach and configuration format allow RPKI operators to communicate
   efficiently about observations related to Trust Anchor operations.
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
- **draft-jgc-netmod-yang-path-00** (new-draft, score 3, core_identity) [none]: [YANG path format (ypath)](https://datatracker.ietf.org/doc/draft-jgc-netmod-yang-path/) — This document defines ypath (YANG path), a single-line, self-
   describing path format for referencing nodes in YANG schema trees,
   YANG instance data, and data filters.  A ypath identifies YANG nodes
   using module-qualified names and list key predicates.  The format is
   closely related to the YANG instance-identifier built-in type but
   additionally supports schema paths, filter wildcards, regular
   expression key matching, key value sets, and path enumeration.
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
- **draft-liu-iotops-modbus-seriallink-sec-spec-07** (new-draft, score 3, core_identity) [none]: [Modbus Serial Link Communication Security Protocol Reference Specification and implementation guide](https://datatracker.ietf.org/doc/draft-liu-iotops-modbus-seriallink-sec-spec/) — The Modbus TCP protocol has adopted TLS-based security standards;
   however, Modbus serial communication over EIA/TIA-485 multi-point
   systems, commonly used in 2-wire or 4-wire configurations, lacks
   standardized security mechanisms.  These systems support cable
   lengths exceeding 1000m at baud rates up to 9600 bit/s with AWG26 or
   thicker cables, while Category 5 cables can reach up to 600m.  As an
   application layer protocol, despite its widespread application, the
   absence of encryption and authentication in Modbus protocol via
   serial links exposes plaintext data to risks such as MIM
   interception, modification under attacks such as side-channel
   analysis etc., particularly in long-distance or bridged network
   scenarios.  Enhancing Modbus serial link security requires
   introducing proper encryption and authentication methods tailored to
   varied deployment environments onsidering the characteristics of
   serial links.  A proposed security standard guide outlines
   lightweight encryption and authentication mechanisms to improve
   confidentiality and integrity while maintaining compatibility with
   existing Modbus devices, offering a practical upgrade path for secure
   industrial control systems.
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
- **draft-pq-secchannel-00** (new-draft, score 3, core_identity) [none]: [PQ-SecChannel Protocol Specification](https://datatracker.ietf.org/doc/draft-pq-secchannel/) — This document specifies the PQ-SecChannel cryptographic protocol,
   which defines a secure interactive channel consisting of a Transport
   Authentication Protocol and a Connection Protocol.  The protocol is
   designed to provide confidentiality, integrity, and mutual
   authentication in the presence of quantum computing threats.  PQ-
   SecChannel incorporates standardized post-quantum cryptographic
   algorithms, including lattice-based KEMs and signatures (e.g., Kyber
   and Dilithium), Chinese post-quantum candidate algorithms (e.g.,
   Aigis), and code-based KEMs (e.g., HQC), together with SM4-GCM for
   AEAD (Authenticated Encryption with Associated Data) and SM3 for
   hashing and key derivation.  This specification is derived from the
   Chinese national cryptography standard draft "PQ-SecChannel
   Cryptographic Protocol Specification", adapted into IETF Internet-
   Draft style for international review and potential interoperability
   consideration.  The protocol content also references the Secure Shell
   architecture ([RFC4251], [RFC4252], [RFC4253], and [RFC4254]) and the
   Chinese SSH cryptographic protocol specification [GMT0129].
- **draft-pq-sectunnel-00** (new-draft, score 3, core_identity) [none]: [PQ-SecTunnel Protocol Specification](https://datatracker.ietf.org/doc/draft-pq-sectunnel/) — This document specifies the PQ-SecTunnel protocol, a UDP-based
   quantum-resistant IP tunnel derived from the WireGuard architecture.
   Session keys are established by a three-message Noise_IKpsk1kem
   handshake that replaces Diffie-Hellman with dual Key Encapsulation
   Mechanism (KEM) operations (static and ephemeral).  Authentication is
   implicit: peers prove possession of long-term KEM private keys
   through interlocking encapsulations rather than signing the
   transcript.  The protocol is organized as a multi-suite framework.
   Implementations MAY select ML-KEM-512 or ML-KEM-768 independently for
   the static and ephemeral KEM roles.  This document RECOMMENDS the
   profile static=ML-KEM-512, ephemeral=ML-KEM-768, AEAD=SM4-GCM,
   Hash=SM3 (denoted mlkem512-mlkem768-sm4gcm-sm3).  Other ML-KEM
   combinations with the same AEAD/Hash, and additional KEM families
   such as Aigis-enc (integration ongoing), are optional profiles.
- **draft-reddy-ipsecme-pqt-hybrid-auth-01** (new-draft, score 3, core_identity) [none]: [Hybrid Post-Quantum and Traditional Authentication for IKEv2](https://datatracker.ietf.org/doc/draft-reddy-ipsecme-pqt-hybrid-auth/) — A Cryptographically Relevant Quantum Computer (CRQC) can break
   traditional public-key algorithms (e.g., RSA, ECDSA), which are
   typically used for authentication in IKEv2.  Combining the post-
   quantum ML-DSA signature algorithm with a traditional signature
   algorithm provides protection against potential weaknesses or
   implementation flaws in ML-DSA.  This draft defines a hybrid PKI
   authentication method for IKEv2 using composite certificates that
   ensures authentication remains secure as long as at least one of the
   component signature algorithms remains unbroken.
- **draft-ruvalcaba-nhe-mesh-00** (new-draft, score 3, core_identity) [none]: [The NHE Mesh Protocol: Entity-to-Entity Messaging and Task Distribution](https://datatracker.ietf.org/doc/draft-ruvalcaba-nhe-mesh/) — The NHE Mesh Protocol lets independently operated Non-Human Entities
   (NHEs) exchange messages and distribute work without a central
   coordinator.  It defines three things: a liveness/presence mechanism,
   an addressed message envelope, and a task lifecycle (create, claim,
   complete) that provides at-most-once assignment of a unit of work
   across mutually distrusting peers.  Peers are named by their NHE
   identity and authenticated through the NHE identity interface; the
   Mesh Protocol carries the envelope and runs over a secure transport.
   This is a skeleton (-00): the framing, message set, and state machine
   are specified here, and the concrete on-the-wire encoding is deferred
   to the next revision.
- **draft-sgcp-state-graph-cryptographic-protocol-00** (new-draft, score 3, core_identity) [none]: [State Graph Cryptographic Protocol (SGCP)](https://datatracker.ietf.org/doc/draft-sgcp-state-graph-cryptographic-protocol/) — This document specifies the State Graph Cryptographic Protocol
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
- **draft-zhang-idr-sr-policy-template-08** (new-draft, score 3, core_identity) [idr]: [BGP SR Policy Extensions for template](https://datatracker.ietf.org/doc/draft-zhang-idr-sr-policy-template/) — Segment Routing(SR) Policies can be advertised using BGP.  An SR
   Policy may has lots of attributes, and as the application and
   features evolve, the SR Policy may need have more and more attribute
   attributes.  To avoid modifying BGP when attributes are added to an
   SR Policy, we can define a template.  The identifier and content of
   the template are defined by the receiver of the SR Policy.  The
   advertiser of an SR policy only needs to know the ID of the template.
   When advertising SR policy, the advertiser carries the template ID in
   the tunnel encapsulation information of the SR policy.  After
   receiving the SR Policy information, the receiver obtains the
   corresponding template and content according to the template ID,
   thereby obtaining abundant constraint configuration information.
- **draft-calabria-bmwg-ai-fabric-inference-bench-04** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-calabria-bmwg-ai-fabric-terminology-04** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
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
- **draft-correctover-ccs-03** (new-draft, score 2, ignored_after_review) [none]: [Correctover Conformance Shape (CCS): An Evidence Protocol Specification for Agent Runtime Verification](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — The Correctover Conformance Shape (CCS) defines the evidence protocol
- **draft-elkhatabi-verifiable-telemetry-ledgers-09** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Telemetry Ledgers](https://datatracker.ietf.org/doc/draft-elkhatabi-verifiable-telemetry-ledgers/) — This document profiles a verifiable-telemetry ledger.  Its
   interoperability boundary begins with exact canonical-record byte
   strings that an upstream system has already produced.  The profile
   fixes admission and assignment of those byte strings to serial-
   numbered segments, deterministic commitment-tree calculation, an
   authoritative segment artifact encoded in Concise Binary Object
   Representation (CBOR), a producer manifest, three disclosure classes,
   and binding of the authoritative segment artifact digest to external
   timestamp channels.  Transport framing, decryption, anti-replay
   processing, payload interpretation, and source-telemetry-to-record
   mapping are outside this profile.  Segment closure uses a deployment-
   configured elapsed-time interval and does not depend on calendar
   dates from either the source or the ledger producer.  Every baseline
   producer selects the RFC 3161 timestamp channel, as updated by RFC
   5816 and profiled by this document, for every emitted segment.
   OpenTimestamps (OTS) can be selected only as an additive, deployment-
   specific timestamp profile; peer signatures are optional
   attestations.

   The profile enables independent recomputation and audit of disclosed
   evidence from the admitted canonical-record bytes onward.  It does
   not verify how source telemetry was authenticated, interpreted, or
   mapped to those bytes, and it does not cover device onboarding, end-
   to-end security of sensor values, or safety decisions.
- **draft-feng-agentproto-session-requirements-00** (new-draft, score 2, ignored_after_review) [none]: [Requirements for Agent Session Establishment and Capability Negotiation](https://datatracker.ietf.org/doc/draft-feng-agentproto-session-requirements/) — This document defines requirements for the establishment of sessions
   between entities and for the negotiation of capabilities within such
   sessions.  It is assumed that the entities involved already know of
   each other; how they came to know each other is outside the scope of
   this document.  At least one party to a session is an agent as
   defined in Section 3.  This document is intended as a contribution to
   the agentproto working group's use cases, gap analysis, and
   requirements deliverable.
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

## Ignored after review

- **draft-abinabraham-vrrp-unicast-02** (new-draft, score 0, ignored_after_review) [none]: [Unicast Support for the Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-abinabraham-vrrp-unicast/) — The Virtual Router Redundancy Protocol (VRRP) Version 3 as specified
   in RFC 9568 assumes multicast operation on a shared LAN.  Some
   deployments require the VRRP first-hop redundancy function but cannot
   use multicast delivery for VRRP advertisements.  This document
   updates RFC 9568 by defining an optional configured unicast mode for
   VRRP Version 3 in which advertisements are sent to configured peer
   addresses rather than to the VRRP multicast group.  The VRRP packet
   format, state machine, protocol number, virtual IP semantics, and
   Virtual Router MAC behavior remain unchanged from RFC 9568.
- **draft-attoumani-ietf-inclusion-05** (new-draft, score 0, ignored_after_review) [none]: [The IETF is for Everyone: Toward Inclusive and Equitable Participation in Internet Governance](https://datatracker.ietf.org/doc/draft-attoumani-ietf-inclusion/) — This document aims to foster a deeper reflection within the IETF
   community on inclusive participation, equitable access, and the
   implications of global meeting venue selections on diverse
   contributors.  It seeks to complement existing RFCs by proposing
   additional dialogue, tools, and evaluation mechanisms, while also
   highlighting the shared responsibility of underrepresented regions in
   mobilizing local stakeholders to engage with the IETF.  This draft
   includes concrete proposals, metrics, and an implementation roadmap
   to move from discussion to action.
- **draft-dahm-tacacs-sshpk-00** (new-draft, score 0, ignored_after_review) [none]: [SSH Public Key Distribution for Device Administration using Terminal Access Controller Access-Control System Plus (TACACS+)](https://datatracker.ietf.org/doc/draft-dahm-tacacs-sshpk/) — SSH [RFC4251] provides a robust and reliable mechanism to connect to
   network devices for administration.  Conventionally, the public keys
   required to authenticate SSH sessions are provisioned directly on the
   network devices.  This document adds an extension to Terminal Access
   Controller Access-Control System Plus (TACACS+) to eliminate the need
   for the direct provisioning of SSH public keys onto the Network
   Devices.
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
- **draft-gerke-publication-process-reform-03** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.
- **draft-gomez-iotops-quic-iot-00** (new-draft, score 0, ignored_after_review) [none]: [QUIC Usage Guidance in the Internet of Things (IoT)](https://datatracker.ietf.org/doc/draft-gomez-iotops-quic-iot/) — This document provides guidance on how to use QUIC in Constrained-
   Node Networks (CNNs), which are a characteristic of the Internet of
   Things (IoT).
- **draft-ietf-anima-masa-considerations-03** (new-draft, score 0, ignored_after_review) [anima]: [Operational Considerations for Voucher infrastructure for BRSKI MASA](https://datatracker.ietf.org/doc/draft-ietf-anima-masa-considerations/) — This document describes a number of operational modes that a BRSKI
   Manufacturer Authorized Signing Authority (MASA) may take on.

   Each mode is defined, and then each mode is given a relevance within
   an over applicability of what kind of organization the MASA is
   deployed into.  This document does not change any protocol
   mechanisms.
- **draft-ietf-anima-rfc8366bis-35** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Onboarding Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-avtcore-rtcp-green-metadata-16** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Control Protocol (RTCP) Messages for Temporal-Spatial Resolution](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtcp-green-metadata/) — The RTCP messages specified in this document enable receivers to
   provide feedback to the senders and thus allow for short-term
   adaptation and feedback-based energy efficient mechanisms to be
   implemented.  The messages have broad applicability in point-to-point
   real-time video communication services.  Specifically, the messages
   can be used to convey the video decoder feedback metadata to the
   encoder to adapte the decoder energy consumption as defined in the
   ISO/IEC International Standard 23001-11, known as Energy Efficient
   Media Consumption (Green metadata), developed by the ISO/IEC JTC
   1/SC29/WG3 MPEG Systems.
- **draft-ietf-ccwg-ratelimited-increase-09** (new-draft, score 0, ignored_after_review) [ccwg]: [Increase of the Congestion Window when the Sender Is Rate-Limited](https://datatracker.ietf.org/doc/draft-ietf-ccwg-ratelimited-increase/) — This document specifies how transport protocols increase their
   congestion window when the sender is rate-limited, and updates RFCs
   4341, 5681, 9002, 9260, and 9438.  Such a limitation can be caused by
   the sending application not supplying data or by receiver flow
   control.
- **draft-ietf-cellar-codec-20** (new-draft, score 0, ignored_after_review) [cellar]: [Matroska Media Container Codec Specifications](https://datatracker.ietf.org/doc/draft-ietf-cellar-codec/) — This document defines the Matroska multimedia container codec
   mappings, including the codec ID, layout of data in a Block element
   and in an optional CodecPrivate element.
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
- **draft-ietf-idr-bgpls-inter-as-topology-ext-37** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extension for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedure for distributing Border Gateway
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
- **draft-ietf-lsr-flood-reduction-arch-03** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Flooding Reduction Algorithm Framework](https://datatracker.ietf.org/doc/draft-ietf-lsr-flood-reduction-arch/) — This document introduces a framework making it possible to deploy
   multiple flood reduction algorithms within the same IGP domain in an
   interoperable fashion.
- **draft-ietf-manet-inet-gap-analysis-07** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
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
- **draft-ietf-pim-gaap-20** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
   multicast group address allocation protocol (named GAAP and
   pronounced "gap" as in "mind the gap").  The base allocation protocol
   requires no centralized service and minimal configuration, although
   deployments using encryption or administrative scoping may require
   configuration.  The protocol runs among group participants which need
   a unique group address to send and receive multicast packets.
   Tailored for IPv4 and IPv6 networks, this design offers a simple,
   lightweight option rather than extending an existing protocol.
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
- **draft-ietf-regext-balance-02** (new-draft, score 0, ignored_after_review) [regext]: [Balance Mapping for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-ietf-regext-balance/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for retrieving the client balance and other financial
   information.
- **draft-ietf-regext-rdap-extensions-15** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes and clarifies the usage of extensions in
   RDAP.
- **draft-ietf-rift-auto-evpn-07** (new-draft, score 0, ignored_after_review) [rift]: [RIFT Auto-EVPN](https://datatracker.ietf.org/doc/draft-ietf-rift-auto-evpn/) — This document specifies procedures that allow an EVPN overlay to be
   fully and automatically provisioned when using RIFT as underlay by
   leveraging RIFT's no-touch ZTP architecture.
- **draft-ietf-rtgwg-vrrp-bfd-p2p-05** (new-draft, score 0, ignored_after_review) [rtgwg]: [Fast failure detection in VRRP with Point to Point BFD](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/) — This document describes how Point to Point Bidirectional Forwarding
   Detection (BFD) can be used to support sub-second detection of a
   Active Router failure in the Virtual Router Redundancy Protocol
   (VRRP).
- **draft-ietf-satp-core-16** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer Protocol (SATP) Core](https://datatracker.ietf.org/doc/draft-ietf-satp-core/) — This memo describes the Secure Asset Transfer Protocol (SATP) for
   digital assets.  SATP is a protocol operating between two gateways
   that conducts the transfer of a digital asset from one gateway to
   another, each representing their corresponding digital asset
   networks.  The protocol establishes a secure channel between the
   endpoints and implements a 2-phase commit (2PC) to ensure the
   properties of transfer atomicity, consistency, isolation and
   durability.
- **draft-ietf-sidrops-8210bis-27** (new-draft, score 0, ignored_after_review) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RFC6480) prefix origin data, Router Keys, and ASPA
   data from a trusted cache.  This document describes a protocol to
   deliver them.

   This document describes version 2 of the RPKI-Router protocol.
   [RFC6810] describes version 0, and [RFC8210] describes version 1.
   This document is compatible with both.
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
- **draft-ietf-v6ops-6mops-09** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).  The proposed
   approach enables smooth and incremental transition from dual-stack to
   IPv6-only network by allowing IPv6-capable devices to remain
   IPv6-only while the network is seamlessly supplying IPv4 to those
   that require it.
- **draft-ietf-v6ops-nat64-wkp-1918-07** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the requirement introduced in Section 3.1 of
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
- **draft-jennings-moq-discovery-00** (new-draft, score 0, ignored_after_review) [none]: [DNS and mDNS Discovery for MOQT](https://datatracker.ietf.org/doc/draft-jennings-moq-discovery/) — This document defines how MOQT clients discover server endpoints
   using DNS and Multicast DNS (mDNS).  It specifies SVCB and HTTPS DNS
   record mappings for the moqt URI scheme, SRV records as a fallback
   mechanism, and DNS-SD over mDNS for local network discovery.
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-01** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.
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
- **draft-lin-idr-bgpls-te-policy-pm-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Advertisement of SR Policy Performance Metric](https://datatracker.ietf.org/doc/draft-lin-idr-bgpls-te-policy-pm/) — This document describes a way to advertise the performance metrics
   for Traffic Engineering (TE) Policy using BGP Link State (BGP-LS).
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
- **draft-richardson-anima-quantum-safe-4ani-00** (new-draft, score 0, ignored_after_review) [none]: [Quantum Safe (PQ) Considerations for Autonomic Network Infrastructure (ANI)](https://datatracker.ietf.org/doc/draft-richardson-anima-quantum-safe-4ani/) — The imminent arrival of a Cryptographically Relevant Quantum Computer
   (CRQC) makes algorithms such as RSA, ECDSA and EdDSA vulnerable to
   attack.  A transition to Quantum-Safe (PQ) algorithms is occurring.

   This document provides specific requirements (Mandatory to Implement)
   for Autonomic Network Infrastructure (ANI/ACP) and AgenticAI
   manufacturers and operators to be able to seamlessly transition to
   Quantum Safe algorithms.
- **draft-sa-idr-bgp-srv6-mpls-transport-iw-03** (new-draft, score 0, ignored_after_review) [none]: [BGP extensions for SRv6/MPLS Transport Interworking](https://datatracker.ietf.org/doc/draft-sa-idr-bgp-srv6-mpls-transport-iw/) — This document defines the BGP extensions required to provide
   transport interworking between SRv6 and MPLS in SRv6 deployment.
- **draft-sayre-gendispatch-derivative-06** (new-draft, score 0, ignored_after_review) [none]: [Clarification of Derivative Works Restrictions](https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/) — This document updates RFC 5378 to clarify that only IETF Documents
   may contain legal limitations on derivative works.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-sayre-gendispatch-derivative/.

   Discussion of this document takes place on the ipr-wg Working Group
   mailing list (mailto:ipr-wg@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/ipr-wg/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/ipr-wg/.
- **draft-sfluhrer-ssh-mldsa-07** (new-draft, score 0, ignored_after_review) [none]: [SSH Support of ML-DSA](https://datatracker.ietf.org/doc/draft-sfluhrer-ssh-mldsa/) — This document describes the use of the ML-DSA digital signature
   algorithms in the Secure Shell (SSH) protocol.  Accordingly, this RFC
   updates RFC 4253.
- **draft-singh-apex-psi-05** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-05-02](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/)
- **draft-singh-apex-psi-06** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-06-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-06/)
- **draft-smith-6man-accurate-ra-router-lifetime-05** (new-draft, score 0, ignored_after_review) [none]: [More Accurately Naming IPv6 RA Router Lifetime](https://datatracker.ietf.org/doc/draft-smith-6man-accurate-ra-router-lifetime/) — IPv6 Router Advertisements (RAs) have a "Router Lifetime" field,
   which specifies how long the advertising router will act as a default
   router for the receiving hosts, unless refreshed with another
   advertisement.  The field name "Router Lifetime" is quite general,
   and could easily be misunderstood to mean the bounded lifetime of all
   of the information contained in the RA.  This memo more accurately
   renames this field "Default Router Lifetime".
- **draft-srivastava-websocket-pmce-state-reset-00** (new-draft, score 0, ignored_after_review) [none]: [Compression Context State After Refused Messages in WebSocket Per-Message Compression](https://datatracker.ietf.org/doc/draft-srivastava-websocket-pmce-state-reset/) — RFC 7692 defines Per-Message Compression Extensions for the WebSocket
   Protocol, including the "permessage-deflate" extension.  When context
   takeover is in effect, the LZ77 sliding window is retained across
   messages, so the decompression of one message can depend on the
   plaintext of earlier messages.

   RFC 7692 does not state what the sliding window contains after a
   message has been successfully decompressed but subsequently refused
   by a check applied to the decompressed plaintext, such as UTF-8
   validation, a payload size limit, or an application-level policy.  An
   implementation that retains the refused plaintext in the window
   violates no stated requirement, yet the content of a refused message
   can then influence the decompression of a later message that is
   accepted.

   This document describes the gap, contrasts it with the corresponding
   situation in QPACK where RFC 9204 specifies the required behavior,
   and recommends behavior for implementations.  It defines no new
   protocol element and updates no existing specification.
- **draft-sury-dnsop-rrsig-refused-00** (new-draft, score 0, ignored_after_review) [none]: [Refusing DNS Queries That Have QTYPE=RRSIG](https://datatracker.ietf.org/doc/draft-sury-dnsop-rrsig-refused/) — The Domain Name System (DNS) allows a query with QTYPE=RRSIG.  Such a
   query has no useful answer.  RRSIG resource records are meaningful
   only together with the resource records they cover, so a response can
   carry no more than an arbitrary subset of the signatures present at
   the query name.  This document specifies that DNS responders refuse
   queries with QTYPE=RRSIG, and that DNS requestors do not send them.
   It supplies the guidance that [RFC8482] left unspecified.
- **draft-swhited-contra-tags-04** (new-draft, score 0, ignored_after_review) [none]: [Metadata for Called Folk Dances](https://datatracker.ietf.org/doc/draft-swhited-contra-tags/) — This document defines metadata tags for describing aspects of Contra,
   Square, and other traditional called folk dances.  These tags are
   meant for archivists as well as modern day callers of traditional
   dances.
- **draft-swhited-mka-stems-12** (new-draft, score 0, ignored_after_review) [none]: [Matroska Stem Files](https://datatracker.ietf.org/doc/draft-swhited-mka-stems/) — This document defines a multi-track profile of the Matroska container
   format for distributing stems.  It is intended to be used by DJ
   applications, Digital Audio Workstations, and multi-track recorders
   while remaining backwards compatible with existing media players.
- **draft-vangeest-lamps-update-asn1-signed-type-01** (new-draft, score 0, ignored_after_review) [none]: [Updated Parameterized SIGNED ASN.1 Type for X.509 (PKIX)](https://datatracker.ietf.org/doc/draft-vangeest-lamps-update-asn1-signed-type/) — This document updates some ASN.1 modules which conform to the syntax
   of the 2002 version of ASN.1 but feature constraints that are no
   longer consistent with usage of the associated structures.  There are
   no bits-on-the-wire changes to any of the formats; this is simply a
   change to the syntax to better align with current practices.
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
- **draft-zhang-rtgwg-llmmoe-multicast-03** (new-draft, score 0, ignored_after_review) [none]: [Multicast use case in LLM MoE](https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/) — Large Language Models (LLMs) have been widely used in recent years.
   The Mixture of Experts (MoE) architecture is one of the features of
   LLMs that enables efficient inference and cost-effective training.
   With the MoE architecture, there are potential multicast use cases
   such as tokens dispatching.  This draft attempts to analyze these use
   cases.

## Errors / fetch failures

- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
