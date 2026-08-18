# IETF Identity + AI Standards Watch

Date: 2026-08-18

## Read now

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
- **draft-ietf-wimse-workload-identity-practices-06** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
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
- **draft-chen-oauth-agent-authz-use-cases-02** (new-draft, score 11, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0 framework
   [RFC6749] and its common extensions.  The analysis identifies
   fundamental mismatches, the goal of this document is to articulate
   these gaps clearly, providing a foundation for future work on new
   extensions within the OAuth Working Group to address the
   authorization needs of the next generation of ai agents.
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
- **draft-fassbender-scitt-time-anchor-04** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
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
- **draft-feng-agentproto-session-requirements-01** (new-draft, score 8, core_identity) [none]: [Requirements for Agent Session Establishment, Capability Negotiation, and Sessionless Interaction](https://datatracker.ietf.org/doc/draft-feng-agentproto-session-requirements/) — This document defines requirements for session-based and sessionless
   interactions between entities.  For session-based interactions, it
   covers endpoint authentication, capability negotiation, session
   establishment, authorization, and lifecycle management.  It also
   defines security and state requirements for interactions, such as
   notifications, probes, and atomic requests, that do not establish a
   session.  It is assumed that the entities involved already know of
   each other; how they came to know each other is outside the scope of
   this document.  At least one party to an interaction is an agent as
   defined in Section 3.  This document is intended as a contribution to
   the agentproto working group's use cases, gap analysis, and
   requirements deliverable.
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
- **draft-dogru-scitt-disclosure-evidence-04** (new-draft, score 7, trust_infrastructure) [none]: [Transformation Evidence and Coverage Reconciliation for Auditable Data Disclosure](https://datatracker.ietf.org/doc/draft-dogru-scitt-disclosure-evidence/) — Audit receipts for automated data access attest to what a gateway
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

- **draft-hko-openpgp-identifiers-for-legacy-devices-01** (new-draft, score 3, core_identity) [none]: [Shortened OpenPGP identifiers for legacy hardware devices](https://datatracker.ietf.org/doc/draft-hko-openpgp-identifiers-for-legacy-devices/) — This document describes an approach for storing a shortened
   fingerprint-based identifier for OpenPGP private key material on
   hardware security devices.
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
- **draft-ietf-idr-bgp-model-21** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Model for Border Gateway Protocol (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) — This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.
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
- **draft-ietf-masque-connect-ethernet-13** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document describes how to proxy Ethernet frames in HTTP.  This
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
- **draft-intra-handshake-fail-08** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
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
- **draft-jgc-netmod-yang-path-00** (new-draft, score 3, core_identity) [none]: [YANG path format (ypath)](https://datatracker.ietf.org/doc/draft-jgc-netmod-yang-path/) — This document defines ypath (YANG path), a single-line, self-
   describing path format for referencing nodes in YANG schema trees,
   YANG instance data, and data filters.  A ypath identifies YANG nodes
   using module-qualified names and list key predicates.  The format is
   closely related to the YANG instance-identifier built-in type but
   additionally supports schema paths, filter wildcards, regular
   expression key matching, key value sets, and path enumeration.
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
- **draft-reddy-tls-composite-mldsa-11** (new-draft, score 3, core_identity) [none]: [Use of Composite ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-reddy-tls-composite-mldsa/) — Compositing the post-quantum ML-DSA signature with traditional
   signature algorithms provides protection against potential breaks or
   critical bugs in ML-DSA or the ML-DSA implementation.  This document
   specifies how such a composite signature can be formed using ML-DSA
   with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide
   authentication in TLS 1.3, including use in certificates.
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
- **draft-correctover-ccs-04** (new-draft, score 2, ignored_after_review) [none]: [Correctover Conformance Shape (CCS): An Evidence Protocol Specification for Agent Runtime Verification](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — The Correctover Conformance Shape (CCS) defines the evidence protocol
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

- **draft-abinabraham-vrrp-unicast-02** (new-draft, score 0, ignored_after_review) [none]: [Unicast Support for the Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-abinabraham-vrrp-unicast/) — The Virtual Router Redundancy Protocol (VRRP) Version 3 as specified
   in RFC 9568 assumes multicast operation on a shared LAN.  Some
   deployments require the VRRP first-hop redundancy function but cannot
   use multicast delivery for VRRP advertisements.  This document
   updates RFC 9568 by defining an optional configured unicast mode for
   VRRP Version 3 in which advertisements are sent to configured peer
   addresses rather than to the VRRP multicast group.  The VRRP packet
   format, state machine, protocol number, virtual IP semantics, and
   Virtual Router MAC behavior remain unchanged from RFC 9568.
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
- **draft-cx-mpls-mna-inband-pm-09** (new-draft, score 0, ignored_after_review) [none]: [MNA for Performance Measurement with Alternate Marking Method](https://datatracker.ietf.org/doc/draft-cx-mpls-mna-inband-pm/) — MPLS Network Action (MNA) is used to indicate action for Label
   Switched Paths (LSPs) and/or MPLS packets, and to transfer data
   needed for the action.

   This document defines MNA encodings for MPLS performance measurement
   with alternate marking method, which performs flow-based packet loss,
   delay, and jitter measurements on MPLS live traffic.
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
- **draft-ietf-6man-icmpv6-ioam-conf-state-11** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 Query for Enabled In-situ OAM Capabilities](https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-ioam-conf-state/) — This document describes the application of the mechanism of
   discovering In-situ OAM (IOAM) capabilities, described in RFC 9359
   "Echo Request/Reply for Enabled In Situ OAM (IOAM) Capabilities", in
   IPv6 networks.  IPv6 Node IOAM Query functionality uses the ICMPv6
   Query messages, allowing the IOAM encapsulating node to discover the
   enabled IOAM capabilities of each IOAM transit and IOAM decapsulating
   node.
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
- **draft-ietf-ccwg-ratelimited-increase-09** (new-draft, score 0, ignored_after_review) [ccwg]: [Increase of the Congestion Window when the Sender Is Rate-Limited](https://datatracker.ietf.org/doc/draft-ietf-ccwg-ratelimited-increase/) — This document specifies how transport protocols increase their
   congestion window when the sender is rate-limited, and updates RFCs
   4341, 5681, 9002, 9260, and 9438.  Such a limitation can be caused by
   the sending application not supplying data or by receiver flow
   control.
- **draft-ietf-cellar-codec-20** (new-draft, score 0, ignored_after_review) [cellar]: [Matroska Media Container Codec Specifications](https://datatracker.ietf.org/doc/draft-ietf-cellar-codec/) — This document defines the Matroska multimedia container codec
   mappings, including the codec ID, layout of data in a Block element
   and in an optional CodecPrivate element.
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
- **draft-ietf-lsr-flood-reduction-arch-03** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Flooding Reduction Algorithm Framework](https://datatracker.ietf.org/doc/draft-ietf-lsr-flood-reduction-arch/) — This document introduces a framework making it possible to deploy
   multiple flood reduction algorithms within the same IGP domain in an
   interoperable fashion.
- **draft-ietf-manet-inet-gap-analysis-07** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
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
- **draft-ietf-regext-balance-02** (new-draft, score 0, ignored_after_review) [regext]: [Balance Mapping for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-ietf-regext-balance/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for retrieving the client balance and other financial
   information.
- **draft-ietf-regext-ext-registry-epp-10** (new-draft, score 0, ignored_after_review) [regext]: [Extension Registry for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-ietf-regext-ext-registry-epp/) — The Extensible Provisioning Protocol (EPP) includes features to add
   functionality by extending the protocol.  It does not, however,
   describe how those extensions are maintained.  This document
   describes a procedure for the registration and management of
   extensions to EPP, and it specifies a format for an IANA registry to
   record those extensions.  If approved, this document obsoletes RFC
   7451.
- **draft-ietf-regext-rdap-extensions-15** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes and clarifies the usage of extensions in
   RDAP.
- **draft-ietf-rift-auto-evpn-07** (new-draft, score 0, ignored_after_review) [rift]: [RIFT Auto-EVPN](https://datatracker.ietf.org/doc/draft-ietf-rift-auto-evpn/) — This document specifies procedures that allow an EVPN overlay to be
   fully and automatically provisioned when using RIFT as underlay by
   leveraging RIFT's no-touch ZTP architecture.
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
- **draft-ietf-spring-stamp-srpm-mpls-05** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-v6ops-6mops-09** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).  The proposed
   approach enables smooth and incremental transition from dual-stack to
   IPv6-only network by allowing IPv6-capable devices to remain
   IPv6-only while the network is seamlessly supplying IPv4 to those
   that require it.
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
- **draft-knodel-nomcom-gender-representation-04** (new-draft, score 0, ignored_after_review) [none]: [Gender Representation in the IETF Nominating Committees](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document extends the existing limit on nomcom representation by
   organization ([RFC8713], Section 4.17) so that not all voting members
   of the IETF Nominating Committee (nomcom) belong to the same gender.
- **draft-lin-idr-bgpls-te-policy-pm-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Advertisement of SR Policy Performance Metric](https://datatracker.ietf.org/doc/draft-lin-idr-bgpls-te-policy-pm/) — This document describes a way to advertise the performance metrics
   for Traffic Engineering (TE) Policy using BGP Link State (BGP-LS).
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
- **draft-richardson-anima-quantum-safe-4ani-00** (new-draft, score 0, ignored_after_review) [none]: [Quantum Safe (PQ) Considerations for Autonomic Network Infrastructure (ANI)](https://datatracker.ietf.org/doc/draft-richardson-anima-quantum-safe-4ani/) — The imminent arrival of a Cryptographically Relevant Quantum Computer
   (CRQC) makes algorithms such as RSA, ECDSA and EdDSA vulnerable to
   attack.  A transition to Quantum-Safe (PQ) algorithms is occurring.

   This document provides specific requirements (Mandatory to Implement)
   for Autonomic Network Infrastructure (ANI/ACP) and AgenticAI
   manufacturers and operators to be able to seamlessly transition to
   Quantum Safe algorithms.
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
- **draft-sfluhrer-ssh-mldsa-07** (new-draft, score 0, ignored_after_review) [none]: [SSH Support of ML-DSA](https://datatracker.ietf.org/doc/draft-sfluhrer-ssh-mldsa/) — This document describes the use of the ML-DSA digital signature
   algorithms in the Secure Shell (SSH) protocol.  Accordingly, this RFC
   updates RFC 4253.
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
- **draft-van-meter-qirg-quantum-network-architecture-01** (new-draft, score 0, ignored_after_review) [none]: [A Quantum Network Architecture](https://datatracker.ietf.org/doc/draft-van-meter-qirg-quantum-network-architecture/) — This quantum network architecture defines a set of planes providing
   different views of the network, supporting different responsibilities
   and modes of operation; a set of device, node and link types; some
   network topologies, deployment scenarios and their relationship to
   applications; and key design decisions as a result of corresponding
   requirements.
- **draft-vangeest-lamps-update-asn1-signed-type-01** (new-draft, score 0, ignored_after_review) [none]: [Updated Parameterized SIGNED ASN.1 Type for X.509 (PKIX)](https://datatracker.ietf.org/doc/draft-vangeest-lamps-update-asn1-signed-type/) — This document updates some ASN.1 modules which conform to the syntax
   of the 2002 version of ASN.1 but feature constraints that are no
   longer consistent with usage of the associated structures.  There are
   no bits-on-the-wire changes to any of the formats; this is simply a
   change to the syntax to better align with current practices.
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
