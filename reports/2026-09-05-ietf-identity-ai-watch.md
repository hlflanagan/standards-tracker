# IETF Identity + AI Standards Watch

Date: 2026-09-05

## Read now

- **draft-sato-soos-gar-07** (new-draft, score 32, trust_infrastructure) [none]: [The Governance Audit Record (GAR) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-gar/) — This document specifies the Governance Audit Record (GAR), the audit
   architecture for agentic AI systems.  GAR defines five audit types,
   the Session Audit Record (SAR), the Audit Alert system, auditor
   principal categories, and the Audit Package for external regulatory
   inspection.  GAR provides verifiable evidence that AI agent sessions
   were governed in accordance with the Intent Declaration Primitive and
   the Human Escalation Mechanism.  GAR answers the governance question:
   can any of this be proven to a regulator?  GAR is a domain-specific
   application of the SCITT (Supply Chain Integrity, Transparency and
   Trust) architecture extended with causal ordering semantics for
   agentic governance events.  GAR defines the Authority Lifecycle Event
   (ALE) category: a normative set of causally-ordered event types
   covering the complete agent session revocation and recovery
   lifecycle, including single-agent revocation, authority suspension,
   partial state recording, recovery initiation, credential restoration,
   and multi-agent delegation tree events.

   Version -03 adds the SOOS Governance Semantic Convention: the
   normative soos.governance.* OpenTelemetry attribute namespace for
   governance observability, the SOOS GAR Processor specification for
   OTel-to-SAR pipeline construction with Session Block Merkle
   integrity, four new Authority Lifecycle Events, three mandatory
   provenance fields on Cedar evaluation records, and the XPID mirror
   field on ACD session ALEs.

   Version -04 made the Session Block construction rules more explicit,
   closing three ambiguities found during independent interop
   verification at the IETF 126 Hackathon.

   Version -05 supersedes -04's Session Block construction text with a
   corrected construction: the Merkle leaf and internal-node hashes are
   now domain-separated (RFC 9162's Merkle Tree Hash, with 0x00/0x01
   prefix octets) and odd-length levels use RFC 9162's k-split recursive
   tree shape rather than duplicate-node padding, closing a malleability
   class structurally equivalent to CVE-2012-2459 that was present in
   -04's construction.  This revision is fully self-contained: unlike
   -03 and -04, it does not carry forward unreproduced text from an
   earlier version.  Version -05 also adds a subject_digest field to
   Cedar-evaluation GAR records, the same construction used by the Agent
   Accountability Composition as its cross-slot join key, positioning
   GAR as a conforming AEP instance under the RATS-bound composition;
   the field is normatively scoped to prohibit independent re-
   serialization where an upstream party has already established the
   action's canonical serialization, per the failure mode documented in
   the SCITT typed-reference specification.

   Version -06 closes gaps surfaced by a WIMSE-style security review
   pass against -05's own text and reference sample code: a JWKS trust-
   anchor bootstrap requirement, a corrected key-compromise remediation
   procedure that no longer requires re-signing already-committed audit
   artifacts, an explicit Level 1/2 residual-risk disclosure for a
   compromised-but-signing GEC, a defined failure path for KIA signer
   quorum failure at Session Block close, referential-integrity
   enforcement for causal_parent_id, and guidance against alert-fatigue
   false positives in session_sequence_number gap detection.  This
   revision also carries an idnits repair pass covering reference
   classification, citation hygiene, and formatting.
- **draft-das-eu-ai-act-execution-enforcement-00** (new-draft, score 26, ai_infrastructure) [none]: [Technical Enforcement of the EU AI Act and Global AI Laws Without Relying on Paper Policies](https://datatracker.ietf.org/doc/draft-das-eu-ai-act-execution-enforcement/) — The European Union Artificial Intelligence Act establishes an
   extensive paper-based governance regime for artificial intelligence:
   risk-management documentation, data-governance records, conformity
   assessments, human-oversight instructions, transparency notices,
   logging obligations, and post-market monitoring plans.  These
   instruments are necessary, and this document does not propose to
   discard them.  They are not, however, sufficient by themselves once
   an AI system can autonomously or semi-autonomously act at machine
   speed, because a document can only describe what an operation should
   do; it cannot, by itself, make an operation technically incapable of
   doing otherwise.

   This is not a problem unique to the European Union.  South Korea's AI
   Basic Act regulates "high-impact AI" through comparable risk-
   management, human-oversight, and documentation duties.  Japan's AI
   Act, in force since September 2025, takes a lighter, more promotion-
   oriented approach but still assumes that written governance is the
   primary control.  China enforces a binding but differently structured
   set of algorithm-recommendation, deep-synthesis, generative-AI, and
   AI-content-labelling rules.  Texas and Colorado have each enacted
   state-level AI statutes in the United States with disclosure and
   consequential-decision obligations, and Brazil's PL 2338/2023 and
   Canada's lapsed AIDA proposal show the same EU-style risk-based model
   spreading, whether or not yet enacted.  Every one of these regimes,
   whatever their legal differences, shares the identical underlying
   engineering gap this document addresses: a written rule, however well
   drafted, does not by itself make a machine unable to break it before
   anyone can react.

   The gap is most consequential precisely where the stakes are highest.
   In defence-relevant AI, critical-infrastructure control systems, and
   satellite or space-system automation, an autonomous agent can select
   a target, reroute power or water, transfer control of a physical
   asset, or transmit a command to an orbital platform within a single
   inference cycle -- before any operator, reviewer, regulator, or
   after-the-fact investigation can intervene.  If that act causes harm,
   two questions follow immediately: who is liable, and at what cost.  A
   risk-management file, a conformity-assessment certificate, or an
   audit log written after the fact can show that a rule existed; none
   of them can show that the machine was technically incapable of
   breaking it, and none of them limits the cost already incurred by the
   time the record is examined.  For these classes of system, the
   appropriate default when an authorization cannot be verified is not
   "log it and investigate later"; it is fail-closed: the act simply
   does not occur.

   This document describes an execution-finality architecture that
   converts a selected, already-determined AI-governance requirement
   from a document into a mandatory, machine-verifiable precondition of
   the AI-generated operation itself.  A consequential AI-generated
   operation is first represented as a Candidate Act and is held in a
   Non-Effective State -- technically incapable of invoking a tool,
   actuating a device, transmitting a command, or otherwise causing an
   external consequence -- until a Protected Enforcement Domain
   validates the machine-readable constraints applicable to that exact
   act, including the AI system identity, permitted operation, target,
   recipient, destination, required human-oversight state, transparency
   marker, risk-control status, policy epoch, and revocation state.
   Successful validation produces narrowly scoped, act-bound
   effectuation authority; a Finality Sink positioned at the point of
   first usable external effect independently re-verifies that exact
   authority, and the current required state, immediately before the
   consequence is permitted to occur.  Absent, stale, revoked, or
   unverifiable authority results by default in no effect, not in a
   warning.  The same architecture accepts a jurisdiction-specific
   governance profile as an input, so that an EU AI Act profile, a
   Korean AI Basic Act profile, or another national profile can each
   supply the machine-readable constraints for the identical enforcement
   mechanism without this document taking a position on how those laws
   relate to one another.

   This document does not determine whether an AI system is legally
   high-risk under Annex III, whether a practice is prohibited under
   Article 5, whether a conformity assessment is valid, whether human
   oversight under Article 14 is legally sufficient, or whether an
   organisation complies with the Regulation as a whole, nor does it
   make any equivalent determination under another jurisdiction's law.
   Those determinations remain outside the protocol and must be made by
   the responsible legal, regulatory, or organisational authority.  This
   document addresses the narrower engineering problem that arises only
   after such a determination has already been made: once an applicable
   governance requirement has been translated into a machine-readable
   constraint, how can satisfaction of that constraint be made
   technically necessary before the corresponding AI-generated
   consequence becomes effective?

   This document does not advocate replacing paper-based AI governance
   for general-purpose or low-consequence AI applications, where the
   cost and rigidity of execution-level enforcement would be
   disproportionate to the risk.  The architecture is proposed
   specifically for high-criticality AI deployments -- defence and dual-
   use systems, critical infrastructure, satellite and space systems,
   and comparably consequential autonomous or agentic systems -- in
   which an unauthorised act is not merely a compliance finding but a
   matter of physical safety, national security, or irreversible loss,
   and in which liability and cost must be bounded by making the
   unauthorised act technically non-completable rather than merely
   detectable afterward.
- **draft-sato-soos-kia-06** (new-draft, score 26, core_identity) [none]: [Kernel Identity and Attestation for Governing Enforcement Components](https://datatracker.ietf.org/doc/draft-sato-soos-kia/) — This document specifies the Kernel Identity and Attestation (KIA)
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
   addressing FROST nonce reuse, XPID revocation gap, identity
   takeover via claimed identifier (CVE-2025-13609 class), and
   attestation channel binding (CVE-2026-33697 class).

   This document is the reference specification for the KIA RATS WG
   presentation at IETF 126 Vienna.  The XPID primitive and the
   CVE-2026-33697 attestation channel binding defense are the primary
   novel contributions presented to the RATS WG.

   Version -04 corrects a registry-format mismatch identified by IANA
   early review (#1456067): the IANA Considerations request to
   register XPID_DERIVED and XPID_VERIFICATION_FAILED into the GAR
   Authority
   Lifecycle Event Types Registry the GAR draft defines now uses that
   registry's actual column set (Event Type, Class, Reference) and
   assigns both entries the newly-defined Class ID (Identity/
   Federation event).  No new event types, fields, or normative
   behavior are introduced in -04; this is a registration-format
   correction only.

   Version -05 discloses a known open issue found by a WIMSE security
   review checklist dry-run against -03 (DR-MJWT-KIA-CHECKLIST-01,
   Finding 4): the Cross-Instance Trust Model verifies an XPID but
   does not restrict which federation participants can see the
   underlying Evidence in the first place.  This is named as
   OQ-KIA-EVIDENCE-VIS, following the same acknowledge-rather-than-
   silently-omit pattern this document already uses for
   OQ-S-XPID-REV.  No mechanism is specified in -05; resolution is
   deferred, consistent with how OQ-S-XPID-REV is treated.

   Version -06 closes out a full WIMSE Security Review checklist pass
   (Stage 0 through Stage 2) run against -05.  It restores seven GEC
   Manifest fields silently absent since -03 despite -03's text
   claiming the -02 schema was carried forward in full, including
   attestation_certificate; mints a dedicated XPID namespace UUID in
   place of the reused DNS namespace UUID; updates the FROST
   reference from the CFRG working draft to RFC 9591 and corrects
   the nonce-generation section citations; resolves a genuine
   bootstrapping contradiction between the quorum-failure signing
   prohibition and the quorum-failure alerting requirement (new
   CONF-KIA-24); tightens Security Considerations wording describing
   the XPID derivation input; adds a new Denial of Service Security
   Considerations entry for the quorum-isolation availability
   asymmetry; and adds a Privacy Considerations section addressing
   XPID's by-design stability and cross-context linkability.  No
   prior conformance requirement is weakened by this revision.
- **draft-laxsharma-pact-01** (new-draft, score 25, adjacent_watchlist) [none]: [PACT: Liability and Settlement for Autonomous Agent Contracts](https://datatracker.ietf.org/doc/draft-laxsharma-pact/) — A growing family of specifications lets autonomous agents establish
   identity, delegate authority, record what they did, and move money.
   None of them makes one party financially answerable to another for a
   result that was not delivered.  This document specifies PACT, which
   adds liability as a required, co-signed member of an agent contract
   and propagates it through a subcontract tree.

   PACT defines the Verifiable Task Contract, a signed JSON object
   binding parties, scope, price, verification profile, and an explicit
   allocation of liability; the Delivery object that a contract is
   judged against; an escrowed settlement procedure whose release is
   conditioned on a stated assurance level rather than on elapsed time;
   and a subcontract tree in which a parent's Work Attestation commits
   to its children by Merkle root and liability cascades upward.

   PACT does not define an identity format, an authorization model, an
   audit architecture, a transparency service, a payment rail, or a
   reputation system.  It composes existing work for all of these.  Its
   settlement loop is an instance of optimistic fair exchange, and its
   bond-sizing rule is the classical deterrence bound; both are cited
   rather than reintroduced.
- **draft-das-rats-attestation-bnd-execution-finality-01** (new-draft, score 24, trust_infrastructure) [none]: [Attestation-Bound Execution Finality for AI Accelerators and Confidential Workloads](https://datatracker.ietf.org/doc/draft-das-rats-attestation-bnd-execution-finality/) — Remote attestation can establish evidence about the hardware,
   firmware, software, configuration, and execution environment
   associated with a workload.  In heterogeneous confidential-computing
   environments, this trust assessment can extend across CPUs,
   confidential virtual machines, GPUs, AI accelerators, DPUs,
   SmartNICs, and other trusted execution components.

   An increasingly important class of workloads, however, does not
   merely compute data.  AI agents and autonomous workloads can generate
   consequential operations such as API invocations, storage mutations,
   network configuration changes, infrastructure-control commands,
   financial instructions, device operations, and cross-workload
   requests.

   An acceptable Attestation Result supplies trust information to a
   Relying Party; it is not, without an application-defined
   authorization step, a decision on the admissibility of each operation
   later emitted by the attested workload.

   This document describes an attestation-bound execution-finality
   architecture in which a consequential operation first exists as a
   Candidate Act in a non-effective state.  Before that act can acquire
   external effect, its relevant parameters are cryptographically bound
   to validation context that can include Attestation Results, workload
   identity, execution context, policy, authorization scope, freshness
   information, and other application-specific evidence.

   A designated Finality Sink verifies the required binding at or before
   the boundary at which the Candidate Act would first acquire external
   effect.

   The resulting separation is between appraisal of the execution
   environment and authorization of a concrete operation at its
   effectuation boundary.

   The architecture is intended to complement, rather than replace,
   Remote ATtestation procedureS (RATS), Entity Attestation Token (EAT)
   [RFC9711], workload-identity systems, confidential computing, Trusted
   Execution Environments (TEEs), accelerator attestation, and existing
   authorization mechanisms.
- **draft-sato-soos-mjwt-05** (new-draft, score 24, agent_identity) [none]: [The Mandate JWT (MJWT) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/) — An AI agent that can act without a verifiable, human-traceable
   authorization record is an agent without an owner.  Existing
   authorization credentials tell you what an agent is permitted to do;
   none of them tell you who authorized it, on which specific object,
   under which mission, or how far that authority can be delegated
   before it reaches this agent.

   This document defines the Mandate JWT (MJWT): a WIMSE workload
   credential profile that binds an AI agent's authority to a specific
   Sovereign Object instance under a named human principal, with a
   cryptographically enforced delegation ceiling and an
   eight-dimensional Narrowing Property that prevents any sub-agent
   from exceeding the authority of the human principal at the root of
   the chain.  Version -02 adds a seventh narrowing dimension (consent
   scope), the
   consent_scope claim carrying data subject consent state for
   APPI/GDPR compliance, the sub_agent_scope claim for consent
   attenuation across delegation hops, a Purpose Code Registry, and
   HEM_CONSENT_REQUIRED integration for fail-closed consent enforcement.
   The MJWT is the authorization primitive referenced by the other
   SOOS governance drafts.

   Version -03 corrects an IANA registration issue: the two
   registries requested there are renamed to drop the redundant word
   "Registry" from the registry name itself, and each now includes
   the Designated Expert Guidance that a Specification Required
   registration policy requires.  No new claims, codes, or normative
   behavior are introduced in -03; this is a registration-format
   correction only.

   Version -04 addresses four findings from a WIMSE security review
   checklist dry-run against -02/-03 (DR-MJWT-KIA-CHECKLIST-01): the
   parent-mandate check at Cedar-action verification time is
   tightened from a disjunctive "retrieve or verify" to a mandatory
   live re-verification of the parent's current signature and
   revocation status, closing a parent-swap-class window; the
   Revocation Registry is now stated explicitly to be the same
   Revocation Registry the KIA draft defines, and the residual
   cross-instance propagation-lag risk this implies is now named
   explicitly, mirroring how that draft discloses its own XPID
   revocation gap; and a new Security Considerations entry states
   plainly that MJWT does not itself establish or verify a
   human_principal_id's root authority.

   Version -05 closes gaps surfaced by a WIMSE-style security review
   pass against -04's own text: an eighth Narrowing Property
   dimension, max_delegation_depth, closes an unbounded-delegation-
   depth Denial of Service vector that -04's own text named but did
   not bound; the consent_reference staleness defense is upgraded
   from a SHOULD-level recommendation to a MUST, extending the same
   live-re-verification discipline already applied to parent
   mandates; and the Introduction's description of RFC 8693
   inheritance is corrected to no longer claim use of the optional
   may_act claim, which this document does not in fact use.  This
   revision also carries minor idnits and citation-hygiene fixes.
- **draft-asor-wimse-agent-delegation-chain-01** (new-draft, score 22, authorization) [none]: [Verifiable Attenuated Delegation for AI Agent Chains](https://datatracker.ietf.org/doc/draft-asor-wimse-agent-delegation-chain/) — AI agents increasingly delegate tasks to other agents.  Each
   delegation should convey only a subset of the delegating party's
   authority, that subset should be bounded in scope, magnitude, and
   time, and any enforcement point should be able to verify -- offline,
   with no call to an authorization server -- that a token presented at
   hop N carries authority no greater than the token at hop N-1, back to
   a trusted root.  OAuth 2.0 Token Exchange (RFC 8693) models two-party
   delegation and records prior actors in a nested "act" claim, but that
   claim is informational only and cannot enforce attenuation across a
   chain of depth two or more.  This document defines the Agent
   Delegation Chain: a profile of OAuth 2.0 JWT access tokens (RFC 9068)
   that carries authority as Rich Authorization Requests (RFC 9396),
   links each delegation to its parent by a cryptographic byte-
   commitment, and specifies a deterministic offline verification
   algorithm that enforces monotonic attenuation, bounded depth, and
   monotonic expiry.  It reuses existing JOSE, proof-of-possession (RFC
   9449), and status-list machinery (the OAuth Status List draft) and
   introduces no new cryptography.
- **draft-das-global-privacy-execution-enforcement-00** (new-draft, score 21, agent_identity) [none]: [Technical Enforcement of the European GDPR and Global Data-Protection Constraints Without Paper Policy](https://datatracker.ietf.org/doc/draft-das-global-privacy-execution-enforcement/) — The European Union's General Data Protection Regulation (GDPR),
   China's Personal Information Protection Law (PIPL), and India's
   Digital Personal Data Protection Act (DPDP Act) each require, in
   their own terms, that personal data be used only for a specified
   purpose, be limited to what is necessary, be kept secure, and remain
   subject to the data subject's or regulator's ability to hold a
   controller accountable.  Every one of these regimes is currently
   enforced primarily through paper: privacy notices, consent records,
   data-processing agreements, internal policies, access-control
   configurations, and audits performed after data has already moved.

   Paper policy fails in the age of artificial intelligence because it
   assumes a human-speed decision that no longer exists.  An agentic AI
   system can authenticate, read from several lawfully accessible data
   sources, combine those sources into a new relationship that was never
   separately assessed, choose a purpose, select a recipient or an
   international destination, and transmit the result -- all within a
   single inference pass, before any privacy officer, consent record,
   contract clause, or after-the-fact audit log can intervene.  A GDPR
   purpose-limitation clause, a PIPL processing-purpose restriction, or
   a DPDP consent-manager rule can be entirely correct on paper and
   still fail in practice, because none of them is a property of the
   computation itself; each is a property of a document that the
   computation is merely expected to obey.  By the time an audit trail
   shows that Article 5(1)(b) of the GDPR, the purpose-limitation
   principle of the PIPL, or the purpose-limitation requirement of the
   DPDP Act was violated, the disclosure, the cross-border transfer, or
   the unauthorized combination of data has already occurred and cannot
   be undone.

   This document introduces an execution-finality architecture that
   converts an already-determined privacy rule from a document into a
   mandatory, machine-verifiable precondition of the computer operation
   itself.  A proposed privacy-sensitive operation is represented as a
   Candidate Act and is held in a Non-Effective State -- technically
   incapable of disclosing, transmitting, or combining protected data --
   until a Protected Enforcement Domain conjunctively validates the
   requesting Virtual Identity (VI), the applicable purpose and
   jurisdictional constraints represented as a Compliance Jurisdiction
   Token or Structure (CJT/CJS), the minimum required data attributes,
   the recipient, and the destination, and a Finality Sink positioned at
   the boundary of first usable external effect independently reverifies
   that state immediately before release.  Non-Joinable Vaults further
   ensure that holding a valid credential or an authenticated AI session
   does not, by itself, grant authority to recombine separated
   categories of personal data.

   A worked example applies the architecture to a small-or-medium
   enterprise (SME) AI customer-service deployment, including a prompt-
   injection scenario in which a manipulated AI agent is technically
   prevented from exfiltrating payment and identity data regardless of
   what the model was tricked into generating.  A feasibility and
   latency analysis shows the mechanism can be deployed as ordinary
   gateway middleware without replacing existing identity or SaaS
   infrastructure.  The document then provides a deliberately bounded
   mapping onto specific GDPR provisions (Articles 5(1)(b), 5(1)(c),
   5(1)(f), 6, 25, 32, and Chapter V), stating plainly which provisions
   this architecture can make technically load-bearing and which -- such
   as the legal validity of a basis for processing, or the lawfulness of
   an international transfer mechanism -- must remain a legal and
   regulatory determination that no software can make on its own.

   This document does not advocate discarding paper-based privacy
   policy, consent management, contractual controls, or audit for
   general-purpose applications, where the cost, rigidity, and
   operational overhead of execution-level enforcement would be
   disproportionate to the risk being managed.  The architecture is
   instead proposed for high-criticality systems: national-security-
   relevant infrastructure, critical infrastructure, systems processing
   special-category or otherwise highly sensitive personal data, and
   other environments in which unauthorized disclosure, cross-border
   transfer, or unauthorized data combination would be catastrophic,
   irreversible, or strategically damaging rather than merely a
   regulatory infraction.  For ordinary commercial applications,
   existing paper-policy, consent, and audit mechanisms, combined with
   conventional access control, may remain proportionate and sufficient
   on their own.

   The central proposition offered to regulators, standards bodies, and
   implementers is this: a privacy rule that exists only on paper is a
   rule the machine can violate before anyone notices; a privacy rule
   bound to the execution boundary is a rule the machine cannot complete
   without satisfying.
- **draft-sato-soos-cap-05** (new-draft, score 21, authorization) [none]: [The Constitutional AI Protocol (CAP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-cap/) — An AI agent's authorization system determines what it is permitted
   to do.  A human principal's escalation decision determines what
   they authorize.  Neither of these is sufficient on its own: a
   Cedar policy can permit market manipulation; a human principal can
   authorize fraud.  Authorization systems answer the question "who
   decided?"  The Constitutional AI Protocol answers a different
   question: "was that decision lawful?"

   CAP defines a Constitutional Layer that evaluates every AI action
   request and every human authorization decision against a three-tier
   prohibition model -- before Cedar evaluates the action and before
   the system executes the human's decision.  Tier 0 prohibitions are
   derived from near-universal treaty consensus and are unconditional:
   no agent, operator, or human principal can authorize them.  Tier 1
   prohibitions are jurisdiction-specific and operator-declared.  Tier
   2 prohibitions are voluntary operator ethical standards.

   This document also specifies the Prohibition Clearance Mechanism
   (PCM): the process by which specific Tier 0 and Tier 1 prohibition
   classes may be cleared for specific deployment contexts --
   either at implementation time by the operator or by formal
   regulatory authority -- while preserving an absolute prohibition
   floor for CSAM and genocide facilitation under any circumstances.

   The Sovereign Object OS (SOOS) is the reference implementation of
   the Governance Execution Controller (GEC) pattern on which CAP is
   built.

   CAP also defines the GEC Policy Transparency Disclosure (PTD): a
   signed, queryable, tier-structured document through which any
   external party may determine which laws and regulations a GEC is
   actively enforcing, at what authority tier, and under whose
   governance.
- **draft-tonyai-a2a-trust-03** (new-draft, score 21, adjacent_watchlist) [none]: [Agent-to-Agent Trust, Identity, and Verifiable Provenance](https://datatracker.ietf.org/doc/draft-tonyai-a2a-trust/) — This document defines a trust model for agent-to-agent (A2A)
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
- **draft-wei-aic-identity-cert-01** (new-draft, score 21, core_identity) [none]: [AI Agent Identity Certificate (AIC) Extension for X.509 v3](https://datatracker.ietf.org/doc/draft-wei-aic-identity-cert/) — This document defines the AI Agent Identity Certificate (AIC)
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
- **draft-wilder-scitt-physical-site-engage-receipt-02** (new-draft, score 21, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
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
   single party can unilaterally forge or repudiate a receipt: the _Site
   Owner_ controls physical access to the TEE hardware and keeps it
   running (they can unplug the box, and cannot forge what it signs);
   the _TEE silicon vendor_ attests the key material inside the TEE
   through its hardware root of trust (silicon vouches for the key); and
   the _Issuer_ writes the vocabulary, registers Signed Statements with
   a Transparency Service, and posts the resulting receipt into the
   site's operations layer via a WRITE_ONLY adapter.  This separation is
   normative in this profile: implementations MUST NOT collapse these
   three roles into a single custodian, and relying parties MUST NOT
   trust a receipt that lacks any one of them.
- **draft-kemp-oauth-x509-bearer-00** (new-draft, score 20, core_identity) [none]: [X.509 Certificate Bearer Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/draft-kemp-oauth-x509-bearer/) — This specification defines the use of an X.509 certificate, issued
   under a Public Key Infrastructure (PKI), as a means for requesting an
   OAuth 2.0 access token as well as for client authentication,
   profiling the Assertion Framework for OAuth 2.0 Client Authentication
   and Authorization Grants in a manner analogous to the JSON Web Token
   (JWT) Bearer Token profile and the SAML 2.0 Bearer Assertion profile.
   It is motivated primarily by workload identity systems, such as
   SPIFFE/SPIRE and Athenz, that already issue software workloads short-
   lived X.509 certificates for mutual TLS, and that benefit from using
   those same certificates directly with OAuth 2.0.  Unlike a bare
   bearer credential, this profile requires that possession of the
   private key corresponding to the certificate's public key be
   corroborated as part of every use, so that a copy of the certificate
   alone -- which is not a secret -- is never sufficient to obtain a
   grant or authenticate a client.
- **draft-mishra-oauth-agent-grants-02** (new-draft, score 20, authorization) [none]: [OAuth Profile for Delegated AI Agent Authorization](https://datatracker.ietf.org/doc/draft-mishra-oauth-agent-grants/) — AI agents increasingly invoke protected APIs on behalf of human
   users.  This document defines an OAuth profile for identifying an
   agent client instance, obtaining an authenticated user's consent,
   issuing resource-bound and sender-constrained access tokens,
   attenuating authority through OAuth Token Exchange, and rotating
   refresh tokens safely.  The profile uses existing OAuth and JOSE
   mechanisms wherever possible and defines no new JWT claims or OAuth
   endpoints.  Operational facilities such as policy engines, audit
   stores, budgets, event streams, and credential vaults are outside the
   interoperable core.  Grantex is an incomplete reference
   implementation and is not required for conformance.
- **draft-sato-soos-rgp-01** (new-draft, score 20, agent_identity) [none]: [The Resource Governance Protocol (RGP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-rgp/) — An AI agent that can act on resources cannot be governed unless
   those resources declare what they can do, under what constraints,
   and at what trust level -- before the agent acts.  Existing
   resource description standards (digital twin profiles, capability
   catalogs, API registries) provide no governance envelope: they
   declare capability but not compliance posture, trust attestation,
   or mandate-scope compatibility.  An agent that proceeds without
   this information may assign tasks to resources that are outside
   its mandate, below its required trust threshold, or unable to
   satisfy its compliance obligations.

   This document specifies the Resource Governance Protocol (RGP):
   a two-stage discovery and declaration protocol by which physical
   resources, digital services, and AI model instances declare their
   capability class, trust level, operational constraints, and
   current availability state to a governed AI agent operating under
   a Mandate JWT.  Stage 1 delivers a
   capability fingerprint via a well-known URI; Stage 2 delivers a
   full governance envelope for mandate-scope validation and Resource
   Map Sovereign Object construction.  RGP defines eight capability
   classes (CAP-COMP through CAP-EXP), four trust levels (TRUST-0
   through TRUST-3), a session-scoped Resource Map Sovereign Object,
   a three-condition autonomous fallback test, and normative
   integration with the Agent Execution Protocol, the Governance
   Audit Record, and the Human Escalation Mechanism.

   RGP also defines an AI Model Capability Declaration (RGP-Model)
   for the governance of AI model instances as first-class resources
   within a SOOS-governed deployment, and a Physical Resource Profile
   (RGP-Physical) for normative binding to existing digital twin
   standards.
- **draft-sato-soos-sov-03** (new-draft, score 20, agent_identity) [none]: [The Sovereign Object (SOV) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-sov/) — When an AI agent acts on your behalf, it acts on something: a
   document, a booking, a contract, a financial instruction.  No
   existing IETF specification defines what that something is, what
   states it can be in, who governs it, or how it is irreversibly
   erased when the relationship ends.

   Agentic AI governance protocols -- including intent declaration,
   human escalation, audit recording, and constitutional prohibition --
   all require a normative definition of the governed resource that
   agents operate on: the structured, stateful, policy-carrying entity
   to which agent authority is bound and upon which governed transitions
   execute.  No existing IETF specification defines this primitive.

   This document defines the Sovereign Object (SO): a causally ordered,
   policy-governed, typed, living document that evolves through a
   predefined finite state space under Governing Enforcement Component
   (GEC) authority.  The SO is the unit of governance in the SOOS
   protocol family: the thing agents operate on, the GEC governs, and
   human principals reason about.

   This document specifies the SO's five-layer structure (Identity,
   State, Event Stream, Typed Graph, Attachment Index), its Zone A /
   Zone B boundary model, its five-phase lifecycle, its SO Type system,
   its Cedar policy context model, and the binding model by which a
   Mandate JWT binds an agent to a specific SO instance.

   Version -02 extends SOV-01 with: (a) SO Type registry governance
   including a SOV-02 subtype model for structured SO Type composition;
   (b) the Standing Plan Object (SPO) as a normative SOV-02 subtype,
   specifying declarative scope constraints, Cedar bundle reference,
   CAP-RRS catalog reference, and IDP structural validation integration;
   (c) event stream integrity normative requirements including
   GEC-signed append-only guarantees, kernel_id binding, and
   OpenTelemetry integration for observability bridging; (d) expanded
   Security Considerations addressing SO state manipulation, event
   stream tampering, SO Type spoofing, and stale state_constraint
   exploitation; and (e) IANA registrations for the SO Type code
   namespace and SPO media type.

   Version -03 removes the Mission Plan SO and Mission Status SO
   subtypes, which -02 defined normatively alongside a SOV-01 SO
   Type Registry Governance and SOV-02 Subtype Model that already
   generalizes to them.  These subtypes are now owned exclusively
   by the Agentic Orchestration Protocol (AOP), which defines a
   materially more complete Sub-Goal DAG model
   (typed dependency edges, deadline tracking, critical-path
   annotation) than -02's; duplicating them here created a
   cross-draft inconsistency this revision resolves by deferring
   entirely to AOP.  Version -03 also reorders the Cedar policy
   evaluation sequence to place Mandate JWT verification before
   SO Type Cedar policy evaluation, matching the Mandate JWT
   draft's own explicit verification-sequencing requirement, and
   updates cross-draft version references
   throughout to the current suite versions.

   The Sovereign Object is the architectural foundation referenced
   normatively by the other SOOS governance drafts.
- **draft-das-agentic-tool-binding-03** (new-draft, score 19, authorization) [none]: [tool_use Is Not invoke(): Binding Execution-Finality to Agentic Tool-Call Interfaces and MCP](https://datatracker.ietf.org/doc/draft-das-agentic-tool-binding/) — Frontier runtimes already standardized the dangerous moment.  A model
   emits a tool_use block, a tool_calls array, or an MCP tools/call
   payload.  The host then invokes whatever name and arguments the model
   printed.  Alignment, allowlists, and OAuth sit around that moment.
   They do not sit on it.

   The consequence of this gap is no longer confined to email or payment
   demos.  In defense, energy, grid control, industrial process control,
   and other critical-infrastructure deployments, the same tool_use
   block already reaches actuation-class systems -- logistics and
   targeting-adjacent decision support, SCADA and PLC interfaces,
   medical devices, autonomous platforms.  In these environments,
   detection after the fact is not mitigation; it is an incident report
   written after the effect has already occurred.  An agent that can act
   at machine speed but cannot be halted at machine speed is a system
   running without brakes: the first uncontrolled invocation is not a
   warning sign, it is the accident.  Command authority, human
   oversight, and legal review all operate on human time.  An unbound
   tool_use block operates on machine time.  When those two clocks
   diverge, the gap belongs to whichever side reaches the effect first
   -- and today, nothing structurally guarantees that side is
   authorization.

   This document does not invent another assistant API.  It binds the
   Agent Candidate Act profile [I-D.das-agentic] onto the three
   interface families those runtimes and their customers already ship:
   tool_use / computer_use style interfaces, function-calling and
   structured tool-response interfaces, and Model Context Protocol
   tools/call.  The model may emit the block.  The block remains non-
   effective.  A local enforcer builds the act, binds the argument
   digest, and refuses invoke() until scoped authority is verified and
   consumed at the dispatch sink.

   For consequence classes above a defined threshold -- FINANCIAL,
   PHYSICAL, NETWORK_CONTROL, and any act reaching defense or critical-
   infrastructure actuation -- this binding treats fail-closed as the
   only conforming behavior: absent successfully verified, current, act-
   bound authority, the candidate act stays non-effective regardless of
   model confidence, prior session trust, or upstream alignment signal.
   Each enforcement decision, allow or deny, commits a Ledger-Anchored
   Validation Receipt (LAVR) -- a signed, hash-chained enforcement
   artifact bound to the specific candidate act and its argument digest
   at the moment of decision.  An LAVR is not a log entry assembled
   afterward for audit; it is the proof that the finality boundary
   actually gated this act before any effect could occur, and its
   absence is itself a fail-closed condition.

   The implementation target is a middleware function that a host loop
   can call without changing the model vendor. tool_use is not invoke().
- **draft-morrison-ot-command-authority-02** (new-draft, score 19, authorization) [none]: [Consented and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
   issued to an operational-technology (OT) or industrial control system
   on the authority of a software agent is refused unless it carries a
   verifiable statement of who the agent is, which human principal it
   acts for, whether that principal authorised this specific action on
   this specific asset, whether a named human signed off on the action
   where its risk class requires it, and an append-only record
   sufficient to attribute the action afterward.  The profile does not
   invent new cryptography or a new identity mechanism.  It composes
   primitives specified elsewhere, DNSSEC-rooted agent discovery, a
   scoped and revocable authorisation grant, a named-human authorization
   receipt bound into the record as human-authorization evidence, and an
   append-only transparency record, into a single structure, the Command
   Authority Envelope, that an enforcement point evaluates and, on any
   missing or invalid binding, refuses.  The profile is availability-
   first and fails closed on authority, never on safety: it MUST NOT be
   placed in the trip path of a safety function.  The memo maps the
   profile onto the identification, use-control, and audit requirements
   that the IEC 62443 and NERC CIP frameworks state but do not give a
   wire mechanism for.  A neighbouring proposal gates safety-critical
   commands on an agent's trust level; this profile takes the opposite
   position, and states why.  The methods by which a principal's
   identity is inferred are out of scope by construction.
- **draft-williams-intent-token-02** (new-draft, score 19, authorization) [none]: [The Intent Token: A Cryptographic Authorization Primitive for Autonomous Agents](https://datatracker.ietf.org/doc/draft-williams-intent-token/) — This document specifies the Intent Token, a cryptographic
   authorization primitive for autonomous AI agent systems.  An Intent
   Token binds an autonomous agent action to a cryptographically signed,
   human-declared authorization envelope before that action is executed.
   The Intent Token addresses a fundamental gap in existing
   authorization frameworks: while OAuth 2.0, OIDC, and related
   standards govern identity and access at the session level, no
   standardized primitive exists for governing what an autonomous agent
   is authorized to DO at the moment of action.  The Intent Token
   provides this primitive.  It is model-agnostic, transport-agnostic,
   and composable with existing authorization infrastructure.

   Revision -01 extended the specification with Fractal Intent Token
   (FIT) binding for multi-scale agent systems, Authorization Fluidity
   for context-sensitive mode switching, and the Fractal Crypto-Temporal
   Graph (FCTG) as the normative audit trail data structure for
   continuous adaptive authorization.  This revision (-02) corrects the
   stated patent priority date and dependent date references carried
   over from -01, adds a fourth documented instance of independent
   convergence (Broadcom's AgentMinder), and revises the
   characterization of AI-assisted development work in Section 12 for
   accuracy.
- **draft-marques-asqav-compliance-receipts-08** (new-draft, score 18, core_identity) [none]: [Compliance Profile of Signed Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-marques-asqav-compliance-receipts/) — This document defines a multi-jurisdiction compliance profile of the
   signed action receipt format used by AI agents to record machine-
   readable evidence of access-control decisions.  The profile binds
   receipt fields to two regulatory surfaces: on the European Union
   side, Articles 12 and 26 of the EU AI Act (Regulation (EU) 2024/1689)
   and Article 17 of DORA (Regulation (EU) 2022/2554); on the United
   States side, the NIST AI Risk Management Framework, the Colorado AI
   Act, the Texas Responsible AI Governance Act, the New York Department
   of Financial Services Cybersecurity Regulation (23 NYCRR Part 500),
   the HIPAA Security Rule, SEC Rule 17a-4, and the Cyber Incident
   Reporting for Critical Infrastructure Act of 2022 (CIRCIA).  Working
   entirely within the existing wire format, canonicalization
   transformation, and signing algorithms of the underlying receipt
   format, the profile tightens a subset of the OPTIONAL fields to
   REQUIRED, imposes a retention floor, and requires at least one
   timestamping anchor (RFC 3161 or OpenTimestamps).  It registers
   OPTIONAL extension fields for risk and incident classification,
   cross-agent envelope binding, per-action validity-window and
   integrity, build provenance, threat-framework taxonomy, server-built
   enforcement-control records, producer-asserted risk acceptance, and
   producer-asserted code authorship, each subject to false-attestation
   guards where applicable, and registers receipt type namespaces for
   passive-telemetry, result-bound observation, risk-acceptance, and
   code-authorship receipts.  Revision -08 additionally defines an
   attestation statement envelope (a Dead Simple Signing Envelope (DSSE)
   Pre-Authentication Encoding wrapping an in-toto Statement v1 under an
   asqav predicate namespace) with two tiers: a voluntary observation
   attestation that signs a caller-supplied digest and is explicitly not
   a capture, and an authoritative attestation whose subject digest the
   issuing platform re-derives from independent evidence (for code, the
   SHA-256 of the raw unified diff re-fetched from the source host);
   revision -08 further defines the capture-layer integrity, independent
   verification protocol, honest-tiering, and service-identity and
   revocation rules that govern those attestation statements, and
   documents the shipped keyed-digest wire tokens and the verifier
   verdict vocabulary (verified, verified_keyed, unverified).  The full
   field set and its normative requirements are defined in the body of
   this document.
- **draft-reece-wimse-cross-org-delegation-02** (new-draft, score 18, core_identity) [none]: [Cross-Organizational Delegation for Workload and Agent Identity: Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/) — Autonomous software agents increasingly act on behalf of human
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
- **draft-sato-soos-pt-03** (new-draft, score 18, agent_identity) [none]: [Progressive Trust (PT) for Agentic AI Governance Systems](https://datatracker.ietf.org/doc/draft-sato-soos-pt/) — When a new employee joins an organization, they begin with limited
   authority.  As they demonstrate good judgment -- completing tasks
   reliably, asking for guidance at the right moments, recovering well
   when things go wrong -- they earn greater trust and, with it, greater
   authority.  If their performance degrades, or if months pass without
   any demonstration, that trust diminishes.  This is how human
   organizations manage authority over time.  AI agents have no
   equivalent mechanism.

   Today, an AI agent's authority is declared once in a credential at
   issuance time and does not respond to its behavioral record.  An
   agent that has completed 200 successful sessions with a proven track
   record holds the same credential as a newly deployed agent.  The
   human principal who issued both credentials made a judgment at
   issuance time; nothing that happened since is reflected in the
   agent's authority.

   This document defines Progressive Trust (PT): a behavioral trust
   model for AI agents in which authority recommendations evolve in
   response to cryptographically verified evidence of actual
   performance.  PT measures five behavioral properties: whether the
   agent's self-assessed confidence matches its actual outcomes;
   whether it asks for human oversight at the right moments; whether
   it achieves its goals; whether it avoids decisions it later has to
   reverse; and whether it adapts when its action is rejected.  These
   measures are derived exclusively from the tamper-evident, GEC-signed
   Event Stream -- an agent cannot influence its PT Score except through
   actual governed behavior.

   PT does not grant authority automatically.  It generates structured
   recommendations, backed by behavioral evidence, for human principal
   review and approval.  Human principals decide whether to elevate or
   reduce an agent's authority.  PT ensures that decision is informed
   rather than made in the absence of history.

   Progressive Trust is the longitudinal complement of the Agent
   Execution Protocol (AEP): AEP governs what an agent does within a
   session; PT measures what an agent has done across sessions and
   translates that history into structured authority recommendations.
   No equivalent specification exists in IETF, ISO, NIST, or any
   agentic AI governance standards body.
- **draft-das-rats-openai-anthropic-extraction-00** (new-draft, score 17, trust_infrastructure) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive OpenAI and Anthropic Claude Model Information](https://datatracker.ietf.org/doc/draft-das-rats-openai-anthropic-extraction/) — Anthropic and OpenAI already ship inference interfaces richer than
   raw completions -- log-probabilities, embeddings, hidden states,
   intermediate activations, KV-cache material, and diagnostic output
   are all in production today.  Each is a channel an adversary, a
   compromised partner integration, or a stolen enterprise seat can use
   to reconstruct, steal, or distill a model far faster than by scraping
   ordinary text output.  In this document, a "release" is any point at
   which such information leaves the protected execution environment and
   becomes usable outside it: returned to a caller, cached, forwarded,
   or otherwise materialized.  The operational question this document
   answers is narrow: given that the caller is authenticated and the
   workload is attested, is this specific release still authorized to
   happen right now?

   Authentication establishes who is asking.  Confidential computing and
   remote attestation establish whether the execution environment is
   trustworthy.  Neither establishes whether this particular release, of
   this particular artifact, at this particular moment, should be
   allowed to cross the protected boundary.  A valid API key, a genuine
   TEE, and a passing Attestation Result are all fully compatible with
   an unauthorized bulk-extraction run already in progress.  Rate
   limits, output filtering, and anomaly detection operate after the
   release has already happened; they make extraction easier to notice,
   not harder to complete.

   This document specifies an execution-finality architecture that makes
   release control a technical precondition rather than a monitoring
   layer: computation is separated from authority to release, every
   sensitive result is held as a non-effective Candidate Release, and
   release becomes possible only after release-specific validation,
   rollback-resistant extraction-state evaluation, bounded
   authorization, and verification at a controlled Finality Sink.
   Because release authority is bound to rollback-resistant, atomically
   consumed extraction state rather than to a bearer credential, the
   volume of privileged teacher signal an adversary can accumulate
   through the governed path is capped by authorized state transitions,
   not by request volume or attacker persistence alone.  The mechanism
   is not claimed to prevent all forms of model distillation; its
   objective is to make unauthorized or excessive extraction of
   privileged model information structurally harder to complete, not
   merely easier to detect afterward.
- **draft-farley-acta-signed-receipts-03** (new-draft, score 17, core_identity) [none]: [Signed Decision Receipts for Machine-to-Machine Access Control](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) — This document defines a portable, cryptographically signed receipt
   format for recording machine-to-machine access control decisions.
   Each receipt captures the identity of the decision maker, the tool or
   resource being accessed, the policy evaluation result, and a
   timestamp.  All of these are signed with Ed25519 [RFC8032] and
   serialized using deterministic JSON canonicalization [RFC8785].

   The format is designed for environments where AI agents invoke tools
   on behalf of human operators, particularly the Model Context Protocol
   (MCP) ecosystem.  Receipts are independently verifiable without
   contacting the issuer, enabling offline audit, regulatory compliance,
   and cross-organizational trust federation.
- **draft-schrock-action-evidence-boundary-05** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
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
- **draft-sharif-agent-audit-trail-02** (new-draft, score 17, adjacent_watchlist) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
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

   This revision (-02) adds a Decision Reproducibility section
   (Section 13) that distinguishes record reproducibility,
   available for any model, from decision reproducibility,
   available only for open-weight models executed at temperature
   zero in an attested environment, and defines the associated
   record fields.
- **draft-watts-ai-identity-conformance-00** (new-draft, score 17, trust_infrastructure) [none]: [AID-1 Provider-Independent Conformance Requirements and Test-Vector Model](https://datatracker.ietf.org/doc/draft-watts-ai-identity-conformance/) — This document defines provider-independent conformance requirements
   for AID-1.  It specifies the execution model for a deterministic
   machine-readable test-vector corpus, including canonicalization,
   cryptographic, identity-binding, delegation, authorization, temporal,
   revocation, replay, attestation, provenance, and integration cases.
   The conformance corpus contains 69 vectors.  Six replay cases are
   architectural boundary tests, including R5, which requires AID-1
   verification to succeed while a downstream D6 scientific-
   admissibility decision rejects the same evidence.
- **draft-das-rats-frontier-model-extraction-02** (new-draft, score 16, core_identity) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive Frontier AI Model Information](https://datatracker.ietf.org/doc/draft-das-rats-frontier-model-extraction/) — As frontier AI providers expose increasingly rich inference
   interfaces to partners, evaluators, and enterprise tenants, richer-
   than-normal outputs -- for example logits, log-probability
   distributions, embeddings, hidden states, intermediate activations,
   KV-cache material, and diagnostic state -- become practical
   extraction vectors rather than theoretical concerns.  In this
   document, a "release" is any point at which such information leaves a
   provider's protected execution environment and becomes usable outside
   it, whether returned directly to a caller, cached, forwarded, or
   otherwise materialized.  Existing authentication, confidential-
   computing, and remote-attestation mechanisms can establish important
   properties of the requester and execution environment, but they do
   not by themselves establish that each specific release of sensitive
   model information is currently authorized to cross that protected-to-
   unprotected boundary.

   This document describes that gap as a pre-effectuation release-
   control problem and proposes controls intended to limit unauthorized
   extraction and reduce the risk that released model information can be
   used for downstream distillation.  It presents an execution-finality
   architecture in which computation is separated from authority to
   release.  A sensitive result is treated as a Candidate Release,
   remains non-effective outside the protected domain, and becomes
   externally available only after release-specific validation,
   rollback-resistant extraction-state evaluation, bounded
   authorization, and verification at a controlled Finality Sink.  The
   document discusses anti-bypass requirements, remote-attestation
   composition, latency, legacy deployment, industrial relevance, and a
   concrete model-extraction scenario.

   The mechanism is not claimed to prevent all forms of model
   distillation.  Its narrower objective is to reduce unauthorized or
   excessive extraction of privileged model information that can
   materially improve model stealing, reconstruction, imitation, or
   distillation.  Because release authority is bound to rollback-
   resistant, atomically consumed extraction state rather than to a
   bearer credential, the volume of privileged teacher signal an
   adversary can accumulate through the governed path is capped by
   authorized state transitions, not by request volume or attacker
   persistence alone.
- **draft-ietf-oauth-sd-jwt-vc-19** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.
- **draft-mcphillips-agentenvelope-derived-authority-01** (new-draft, score 16, authorization) [none]: [AgentEnvelope: Derived Authority and Legitimacy for Autonomous Systems](https://datatracker.ietf.org/doc/draft-mcphillips-agentenvelope-derived-authority/) — AgentEnvelope defines a deterministic derived-authority model for
   autonomous and action-performing systems.  Instead of issuing bearer
   credentials from a central authority, AgentEnvelope derives scoped
   action capabilities from customer-held custody material and canonical
   action envelopes.  A verifier can check an action signature against a
   public action record without receiving roots, seeds, private keys,
   mint material, or hosted service access.

   This revision extends the model with legitimacy: a governance state
   that records whether a cryptographically valid authority remains
   admissible under current policy, evidence, time, and operating
   context.  Legitimacy separates provenance from present-tense
   authorization.  A command can remain signed and verifiable while
   becoming illegitimate because operating facts, policy, or evidence
   changed.

   For autonomous-system deployments, derived authority and legitimacy
   support an IAM model concerned with authority, admissibility,
   accountability, and audit for actors that perform actions, including
   AI agents, workflows, bots, microservices, devices, robots,
   serverless workers, and multi-agent systems.
- **draft-das-6g-query-scoped-communication-handles-04** (new-draft, score 15, core_identity) [none]: [Authorization-to-Reach for Communication Handles: Separating Identifier Possession from Permission to Contact](https://datatracker.ietf.org/doc/draft-das-6g-query-scoped-communication-handles/) — Many Internet and telephone communication systems treat possession of
   a routable identifier as sufficient to attempt contact.  A telephone
   number, SIP URI, messaging handle, relay address, or marketplace
   contact reference can therefore remain a reusable reachability path
   after the purpose of disclosure has ended.

   Existing IETF and industry mechanisms solve related but different
   problems.  STIR and SHAKEN authenticate or attest originating
   identity.  Virtual or masked numbers hide a persistent endpoint but
   commonly leave a substitute route active while the alias is valid.
   OAuth can express delegated API authorization.  Spam scoring and call
   screening classify or reject an attempt after some path already
   exists.

   This document describes an authorization-to-reach model.  A visible
   communication handle is not, by itself, permission to create a
   communication effect.  A request is held as a candidate until
   current, purpose-scoped, revocable, and optionally consumable
   authority is validated.  The document is informational.  It asks
   whether the IETF Applications and Real-Time area should define
   interoperable semantics or an encoding for that authority (for
   example a PASSporT claim, a SIP header or pre-INVITE check, or a
   reusable authorization object).

   This work is not a 3GPP radio, core-network, or IMT-2030 architecture
   proposal.  References to machine-scale or future-network traffic are
   motivational only.  The intended protocol home, if any, is IETF work
   on SIP, STIR, messaging, and Internet communication identifiers.
- **draft-hebbar-zeropath-vpn-protocol-01** (new-draft, score 15, trust_infrastructure) [none]: [ZeroPath VPN: Hop-Bound Secure Packet Validation with State-Bound Ephemeral Sessions, Cryptographic Attestation, and Opcode-Driven Control Architecture](https://datatracker.ietf.org/doc/draft-hebbar-zeropath-vpn-protocol/) — This document specifies the complete ZeroPath VPN protocol suite,
   comprising three coordinated sub-protocols:

   HBSPV (Hop-Bound Secure Packet Validation) -- a three-domain packet
   framing model that isolates payload decryption to the authorized
   egress node while allowing intermediate hops to validate forwarding
   context without accessing payload content.

   SGCP (State Graph Cryptographic Protocol) -- a three-message
   cryptographically attested handshake enforcing mutual authentication
   and device posture verification before any session is established.

   SCSWP (Secure Cryptographic Session Workspace Protocol) -- a
   continuous session state mechanism providing tamper-evident hash
   chain continuity, epoch-bound forward secrecy, and four-dimensional
   trust scoring across the full session lifetime.

   This document additionally specifies a complete opcode architecture
   governing all control-plane and data-plane message types, providing a
   machine-parseable, extensible message dispatch framework.

   The protocol suite is implemented as a pure Python reference
   implementation at https://github.com/sripad2020/Zeropath-vpn.
- **draft-ietf-oauth-attestation-based-client-auth-11** (new-draft, score 15, authorization) [oauth]: [OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/) — This specification defines an extension to the OAuth 2.0 protocol
   (RFC 6749) that enables a client instance to include a key-bound
   attestation when interacting with an Authorization Server or Resource
   Server.  This mechanism allows a client instance to prove its
   authenticity verified by a client attester without revealing its
   target audience to that attester.  It may also serve as a mechanism
   for client authentication as per OAuth 2.0.
- **draft-sato-soos-aep-03** (new-draft, score 15, agent_identity) [none]: [The Agent Execution Protocol (AEP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-aep/) — An AI agent that can act cannot be governed unless there is a
   normative contract for how it receives its world, how it declares
   its intent, and how it learns what it is and is not permitted to
   do -- at every step, in every iteration, without exception.

   AI agents operating on governed resources require a normative
   interface contract between their internal reasoning loop and the
   Governing Enforcement Component (GEC) that enforces authorization
   policy, records transitions to a tamper-evident Event Stream, and
   mediates access to Sovereign Object instances.  Existing agent
   frameworks define no such contract.  Agents submit actions without a
   normative delivery protocol for the state and permission context they
   act on; GECs enforce policy without a normative protocol for
   communicating denial rationale back to agents; human oversight is
   invoked without a normative session state that governs the resulting
   suspension.

   This document defines the Agent Execution Protocol (AEP): the
   normative five-step loop -- SENSE, REASON, PLAN, ACT, OBSERVE --
   that specifies how a governed AI agent interfaces with GEC services
   at each iteration.  The AEP defines the Context Package delivered at
   SENSE, the GEC Query Interface exercised at PLAN, the Transition
   Request submitted at ACT, and the atomic GEC response received at
   OBSERVE.  The AEP specifies two conformance modes -- Standard and
   Goal Execution Engine (GEE) -- and normatively integrates the Intent
   Declaration Primitive, the Mandate JWT, the Human Escalation
   Mechanism, the Governance Audit Record, the Constitutional AI
   Protocol, and the Sovereign Object as components of a single
   governed execution architecture.

   The REASON step is intentionally GEC-unspecified: the LLM reasoning
   engine is opaque to the protocol.  The AEP is the transmission
   between the LLM engine and the GEC enforcement substrate.

   Version -02 adds: XPID binding at session open (GEC MUST bind XPID
   from KIA-verified Party Registry; MUST NOT accept client-supplied
   XPID); STALLED and PLAN_B_ACTIVE session states with full normative
   definitions, trigger conditions, and resume conditions; Expected
   Outcome Declaration (EOD) as a pre-session commitment structure with
   primary outcome, acceptance envelope, and pre-declared Plan B;
   RETRY_CONTINUATION normative strengthening with what-changed-since-
   last-attempt requirement and prior_denial_count Cedar attribute;
   an AEP-to-OTel mapping with mandatory span attributes at each AEP
   phase; four new Security Considerations; and updated IANA
   registrations for new state codes and EOD media type.

   Version -03 adds Step 4a of the GEC execution sequence: DAM
   lineage and residency validation.  When a Transition Request's
   optional da_production field is present, the GEC resolves every
   referenced input artifact, confirms each is in a VALID lifecycle
   state, and computes the resulting artifact's data_residency under
   the applicable narrowing rule -- before the transition's Event
   Stream write occurs, and under the same signature as that write.
   This is the enforcement point for a rule the data governance
   companion specification had defined but this document, until now,
   gave no mechanism to actually apply.
- **draft-sato-soos-aop-02** (new-draft, score 15, agent_identity) [none]: [The Agent Orchestration Protocol (AOP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-aop/) — A single AI agent acting within a governed session is not the
   hardest governance problem.  The hardest problem is what happens
   when that agent must delegate: when the mission is too large for one
   agent, when sub-tasks require specialized capability, when parallel
   execution is necessary, and when each delegated sub-agent is itself
   consequential enough to require governance.  Who authorized the
   spawn?  Who owns
   the plan?  If the sub-agent deviates, who decides whether to re-plan
   or escalate?  If the mission fails mid-execution, who constructs the
   audit record?

   This document defines the Agent Orchestration Protocol (AOP): the
   normative protocol through which a governed orchestrating agent
   decomposes a mission into a governed sub-goal directed acyclic graph
   (DAG), delegates sub-goals to sub-agents via kernel-mediated
   Assignment Primitives, and maintains a Mission Plan Sovereign Object
   (Mission Plan SO) and Mission Status SO across the full lifecycle
   of multi-agent execution.

   AOP specifies three core constructs: the Expected Outcome Declaration
   (EOD) as the pre-commitment structure for the full mission and each
   delegated sub-goal; the Mission Plan SO encoding the sub-goal DAG
   with SEQUENTIAL, PARALLEL, and CONDITIONAL dependency types; and the
   Assignment Primitive as the governed handoff mechanism that requires
   an Endorsed EOD and produces a Sub-Agent Composition Record (SACR)
   per the Multi-Agent Delegation protocol.

   AOP integrates with the Intent Declaration Primitive at each EOD
   boundary, the Agent Execution Protocol for per-agent session
   governance, the Governance Audit Record for mission lifecycle
   audit events, and the Human Escalation Mechanism for re-planning
   authority escalation.

   The normative reference scenario for AOP is a three-tier emergency
   management orchestration system in which a Master AI orchestrates
   regional coordination agents, which orchestrate domain-specialist
   leaf agents (e.g., evacuation routing models), each tier operating
   under full SOOS governance.

   Version -01 completed the document body: the Expected Outcome
   Declaration in AOP Context, Mission Plan Sovereign Object, Mission
   Status Sovereign Object, Assignment Primitive, Re-planning
   Authority, AOP-to-GAR Integration, Five-Phase Planning
   Intelligence Model, and the Reference Scenario were placeholders
   in -00 and are now fully specified, resolving a three-way
   contradiction in -00 about whether Sub-Goal EOD endorsement
   happens before or after SACR issuance (it is after, gated on SACR
   existence).

   Version -02 fixes a document-structure ordering defect carried
   over from -00, closes -00's open Denial of Service gap with new
   normative security guidance, and corrects a set of reference-list
   defects: two normatively cited documents were never defined in
   the reference list, and ten companion-draft citations in the
   Related Work discussion used one-off versioned reference keys
   that matched no defined entry; all now cite consistently and are
   updated to current SOOS suite versions.  The Related Work
   discussion's own description of Mission Plan SO / Mission Status
   SO ownership is corrected to match this document's own
   Introduction and current reality: both subtypes are defined by
   AOP, not by SOV.
- **draft-sato-soos-faip-02** (new-draft, score 15, agent_identity) [none]: [The Federated Agent Intelligence Protocol (FAIP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-faip/) — Every governed AI agent session ends with a record of what it tried,
   what was permitted, what was denied, and whether it succeeded.
   Across a single operator's deployment, these records feed behavioral
   trust scores.  Across all operators, they are discarded.  No
   protocol exists for pooling this behavioral intelligence without
   exposing the business logic, personal data, or operational details
   that make individual records sensitive.

   This document defines the Federated Agent Intelligence Protocol
   (FAIP): the Tier 3 analytics layer of the SOOS protocol family,
   specifying how aggregate behavioral intelligence is derived from
   governed agent Event Streams across participating operators, made
   available to agents and human principals, and protected through
   privacy-preserving aggregation, data residency controls, and
   k-anonymity enforcement.

   FAIP does not share individual session records.  It does not expose
   any operator's proprietary data.  It produces aggregate behavioral
   signal -- empirical, tamper-evident, distributed -- that no single
   participant can generate from their own data alone.  FAIP is the
   first protocol specification for federated behavioral intelligence
   derived exclusively from cryptographically governed agent activity
   records.

   This document establishes the FAIP architecture, its relationship
   to the three-tier analytics model IDP defines, its privacy and
   data residency framework, and the scope of subsequent FAIP
   specifications.  Full protocol specification of FAIP query
   interfaces, federation topology, and aggregation algorithms is
   deferred to successor documents.
- **draft-sokolov-rats-aep-composition-06** (new-draft, score 15, trust_infrastructure) [none]: [Composing Application-Layer Action Evidence with Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-sokolov-rats-aep-composition/) — This document sketches a composition pattern in which an application-
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
- **draft-birkholz-verifiable-agent-conversations-01** (new-draft, score 14, trust_infrastructure) [none]: [Verifiable Agent Conversation Records](https://datatracker.ietf.org/doc/draft-birkholz-verifiable-agent-conversations/) — Autonomous agents based on large language models increasingly perform
   consequential tasks on behalf of humans and other agents.
   Demonstrating that recorded agent behavior truthfully represents
   actual behavior is essential for accountability, compliance, and
   human oversight.  This document defines a data format for verifiable
   agent conversation records using CDDL, with representations in both
   JSON and CBOR.  The format captures session metadata, message
   exchanges, tool invocations, reasoning traces, and system events in a
   structured, extensible CDDL definition for verifiable agent
   conversation records.  COSE is used as the signing method to allow
   for native interoperability in SCITT Transparency Services and the
   CDDL definition allows for seemless integration in Evidence as
   specified in RFC 9334.  The specification supports cross-vendor
   interoperability by defining a common representation that
   accommodates translation from multiple existing agent implementations
   with distinct data structure layouts that are typically represented
   in JSON.
- **draft-das-digital-sovereignty-finality-01** (new-draft, score 14, adjacent_watchlist) [none]: [When Data Leaves Its Originating Jurisdiction, Who Controls It? Digital Sovereignty Without Data Localisation by Separating the Compute Plane from the Authority Plane](https://datatracker.ietf.org/doc/draft-das-digital-sovereignty-finality/) — Consider a simple case: data concerning U.S. citizens is processed in
   infrastructure located outside the United States.  The foreign
   jurisdiction may have its own lawful-access, surveillance,
   disclosure, retention, or national-security rules.  Even where
   contractual commitments, privacy policies, regional settings, or
   enterprise agreements specify how that data should be handled, the
   infrastructure executing the workload may ultimately operate under
   legal and technical authority outside the originating jurisdiction.

   The same problem applies in reverse to European, Indian, Japanese,
   Canadian, Australian, or other data processed through globally
   distributed infrastructure.

   This creates a deeper architectural problem than ordinary data
   localisation.

   If control over data automatically follows the physical location of
   compute, then moving computation across borders can also move
   practical authority over the resulting data, operations, and
   disclosures.  Privacy may be the first concern, but the same
   architectural dependency can later affect economic security, critical
   infrastructure, sensitive enterprise information, government
   workloads, and national security.

   This is where policy alone begins to reach its limit.

   Contracts, privacy policies, adequacy mechanisms, access-control
   rules, cloud-region settings, and audit requirements remain
   important.  However, they primarily describe what an actor is
   permitted or expected to do.  They do not necessarily create a
   technical condition that prevents a prohibited external effect from
   occurring in the first place.

   Although this document uses the term "digital sovereignty," it does
   not attempt to standardize national policy, determine which
   jurisdiction's law should prevail, or prescribe where data must be
   stored.  Its focus is technical: defining an interoperable mechanism
   by which deployment-selected policy and trust inputs can be bound to
   a specific Candidate Act and enforced at the effectuation boundary
   before that act becomes externally effective.  In this document,
   "sovereignty" therefore refers to retained execution authority, not
   to the standardization of geopolitical or regulatory policy.

   The architecture described here addresses this problem through a
   different model of digital sovereignty: separate the Compute Plane
   from the Authority Plane.

   The Compute Plane may remain globally distributed.  Data may be
   stored, transformed, analysed, routed, or processed using
   infrastructure located in another jurisdiction.  The architecture
   therefore does not require that all data remain physically local, nor
   does it assume that sovereign computing requires complete national
   isolation from global cloud, telecom, AI, or platform infrastructure.

   Instead, the Authority Plane remains independently governed.  A
   remote compute environment may perform computation, but computation
   alone does not grant authority to produce a protected external
   consequence.

   A proposed cross-jurisdiction operation is represented as a Candidate
   Act and remains in a Non-Effective State until the required policy,
   identity, purpose, destination, jurisdiction, runtime, revocation,
   and other applicable predicates have been validated.

   Protected validation may produce a LAVR or equivalent validation
   commitment and a scoped Finality Authority bound to the particular
   Candidate Act.  At the relevant Finality Sink — the first point at
   which the protected operation would become externally effective — the
   authority is independently verified.  Only after successful
   verification and appropriate consumption or reservation of that
   authority may the external effect occur.

   The resulting model is therefore: Compute Anywhere -> Authority
   Remains Independently Governed -> Candidate Act -> Protected
   Validation -> Scoped Finality Authority -> Finality-Sink Verification
   -> External Effect.

   If the required authority is missing, stale, revoked, mismatched,
   replayed, or inconsistent with the governing jurisdictional policy:
   No Valid Authority -> No Protected External Effect.

   This permits a form of digital sovereignty without mandatory data
   localisation.  A jurisdiction, enterprise, regulated institution, or
   other authorised policy owner does not necessarily need to operate
   every processor, cloud region, network, or AI system that performs
   the computation.  Instead, it can retain technical control over the
   conditions under which specified externally effective acts are
   permitted.

   The architecture therefore separates two questions that are commonly
   treated as one: Where is the computation performed?  Who has
   authority over the resulting external effect?  Those questions need
   not have the same answer.

   A U.S. workload could execute outside the United States while
   specified sensitive external effects remain subject to U.S.-
   controlled or enterprise-controlled authorization conditions.  An EU
   workload could similarly use infrastructure outside a particular
   Member State while retaining independently governed finality
   requirements.

   The same mechanism could apply to India, Japan, Singapore, Australia,
   Canada, multinational enterprises, sovereign clouds, regulated
   industries, or private data spaces.  The architecture does not
   prescribe which country's policy should prevail and does not attempt
   to resolve conflicts of law.

   Its contribution is narrower and technical: cross-border computation
   does not have to imply cross-border surrender of execution authority.

   This turns digital sovereignty from a primarily location-centred
   concept into an authority-centred execution model.  The objective is
   not to fragment the Internet or exclude global technology providers.

   On the contrary, separating the Compute Plane from the Authority
   Plane could allow hyperscale cloud providers, AI platforms, telecom
   operators, CDNs, satellite networks, and other global infrastructure
   providers to continue supplying efficient distributed computation
   while supporting stronger jurisdiction-specific, enterprise-specific,
   or regulated execution guarantees.

   In this model, sovereignty does not require saying that the data must
   never leave.  It can instead mean: the computation may occur
   elsewhere, but this protected external effect cannot occur without
   the required authority.

   That is the central architectural proposition of this document.
- **draft-das-map-discovery-communication-finality-00** (new-draft, score 14, core_identity) [none]: [Privacy-by-Design, GDPR-Aligned Communication Finality for Google Maps, Apple Maps, and Other Map-Based Business Discovery Using Query-Scoped Non-Bearer Authorization](https://datatracker.ietf.org/doc/draft-das-map-discovery-communication-finality/) — Map-based discovery systems can help a person identify nearby
   businesses, properties, service providers, hotels, clinics,
   restaurants, and other commercial actors, but discovery frequently
   transitions into communication through a persistent telephone number,
   reusable virtual number, open message thread, callback route, or
   other contact path.  A person may intend only a short first
   conversation with several candidates, while the communication
   mechanism unintentionally creates continuing reachability after that
   inquiry has ended.

   This document describes an architecture in which first contact and
   future reachability are separate authorization events.  After a user
   creates a map search, property inquiry, service request, booking
   inquiry, quote request, or similar context, a platform can create a
   query-scoped non-bearer communication reference and bounded preview
   authority.  A user or eligible business can participate in a real but
   limited first interaction.  Continued communication is separately
   authorized and remains bound to attributes such as the original
   query, business identity, purpose, channel, effect, validity window,
   nonce, quota, revocation state, and enforcement point.  Possession of
   a number, handle, previous conversation, lead assignment, API
   credential, or payment event is not by itself sufficient future-
   contact authority.

   The architecture separates marketplace policy from communication
   effectuation.  A Communication Authority Service creates a protected
   authorization binding, while an enforcement point reconstructs the
   actual attempted communication, checks current protected state,
   atomically reserves or consumes relevant authority, and releases the
   communication-bearing resource only after successful verification.
   This permits privacy-preserving first contact, controlled future
   reachability, preview-qualified lead monetization, and AI-assisted
   business discovery without requiring a new public telecom protocol
   for initial deployment.  Google Maps and Apple Maps are used as
   recognizable illustrative examples; no affiliation, endorsement,
   implementation, adoption, or technical alignment by Google, Apple, or
   any other named provider is implied.

   The architecture's binding of recipient identifiers to pseudonymous,
   query-scoped, time-limited, purpose-bound, and revocable
   authorizations rather than persistent contact data is consistent with
   the data protection principles of the EU General Data Protection
   Regulation (GDPR) -- including data minimization and purpose
   limitation (Article 5), storage limitation through bounded validity
   and quota, and privacy by design and by default (Article 25).  This
   document describes a technical architecture only; it does not
   constitute a legal compliance determination, and conformance with
   GDPR or any other data protection law depends on the specific
   deployment, controller and processor roles, and operational practices
   of an implementing platform.
- **draft-dogru-cedulon-08** (new-draft, score 14, verifiable_claims) [none]: [Cedulon: An Audit Layer for Agent-to-Agent Commerce](https://datatracker.ietf.org/doc/draft-dogru-cedulon/) — This document defines the Cedulon Protocol, an audit layer for agent-
   to-agent commerce.  Payment rails such as HTTP 402 flows (x402) and
   mandate protocols (AP2) already move value, and a mandate protocol
   can already refuse a spend before it happens and return signed
   receipts.  What they do not, by themselves, give a party that is
   neither payer nor rail operator is a retrievable record of that
   decision and a signed spend receipt that reconciles against an
   authenticated extract of the rail.  Cedulon specifies a Trade
   Manifest (signed offer before payment), a Policy Decision Point with
   default deny, a Spend Receipt (COSE/CWT claim set after a gated
   payment), epoch checkpoints, and rail-extract reconciliation.  The
   reconciliation shows that no settlement on the extract lacks a
   receipt and no settled receipt is absent from the extract.  That
   result is unconditional only when the verifier pins the rail key out
   of band and states the period under audit; otherwise the document
   requires it to be reported as conditional.  Checkpoints carry the
   suppression guarantee, so the document profiles the checkpoint as a
   Signed Statement, gives the verification algorithm a step that
   consumes the witness receipts returned for checkpoints, names what a
   witness holding a checkpoint the presented chain omits reports,
   brings equivocation within reach by comparing recorded copies against
   the presented chain, and states how checkpoint totals may be withheld
   without withholding the fact that they were.  No signed object is
   attested by a key it carries itself, a signature checked against such
   a key where no key is held establishes internal consistency and
   attests nothing, and a presented Trade Manifest must be bound both to
   the receipts that name it and to the terms those receipts claim.  The
   document also names a threat no adversary causes, a settlement
   recorded on a rail with no receipt behind it, and defines a Dispute
   Evidence Bundle (evidence, not an award) and optional SCITT
   anchoring.  The encodings earlier revisions called canonical are
   defined, and the exact input to every hash-valued field is stated, so
   that an independent verifier can be written from the text alone.  The
   account and the rail under audit are part of the declared scope on
   the terms the period already had, no settlement finding is read out
   of an extract the pinned rail key refused, and the witness receipt
   has a stated wire form and a registered media type.  This revision
   widens one requirement: a report names the account, rail and window
   it was computed over in every structure an implementation returns for
   that audit, not only in the printed report and the finding object, so
   that no returned result can be read as a statement about settlement
   paths it never looked at.  Cedulon is not a competitor to x402 or
   AP2; it sits above them.
- **draft-reilly-plpes-01** (new-draft, score 14, trust_infrastructure) [none]: [Protocol Layer Prompt Engineering Specification (PLPES)](https://datatracker.ietf.org/doc/draft-reilly-plpes/) — This document defines the Protocol Layer Prompt Engineering
   Specification (PLPES), a structured framework for the formal
   specification, classification, versioning, provenance tracking,
   and security hardening of prompts used to interact with AI
   language models and agentic systems.

   As AI systems become embedded in critical infrastructure, enterprise
   workflows, and protocol-driven pipelines, the prompts governing
   their behavior represent a new class of protocol artifact that
   currently lacks interoperability standards, integrity mechanisms,
   or formal classification taxonomy.  Ad hoc prompt construction
   introduces inconsistency, reproducibility failures, prompt injection
   vulnerabilities, and accountability gaps across deployments.

   PLPES addresses this gap by defining: (1) a canonical Prompt
   Descriptor Object (PDO) for machine-readable prompt representation,
   (2) a five-tier classification taxonomy for prompt roles, (3) a
   versioning and provenance model compatible with the REM Protocol
   [I-D.draft-reilly-rem-protocol], (4) integrity verification
   requirements for agentic prompt chains, and (5) security
   requirements including injection resistance, adversarial input
   handling, and chain-of-custody attestation.

   This specification is intended to be implementable by AI platform
   operators, enterprise AI integrators, protocol architects, and
   standards bodies seeking to establish reproducible, auditable,
   and interoperable foundations for prompt-driven AI systems.

   This revision adds material to draft-reilly-plpes-00 without
   removing or altering any text carried forward from it.  The
   additions are summarized in Section 16.
- **draft-stone-adrp-01** (new-draft, score 14, trust_infrastructure) [none]: [ADRP: Agent Dispute Resolution Protocol](https://datatracker.ietf.org/doc/draft-stone-adrp/) — This document defines the Agent Dispute Resolution Protocol (ADRP), a
   wire protocol and state machine for resolving disputes that arise
   from cryptographically-attested agent-to-agent (A2A) transactions.
   ADRP is the companion specification to ATXN (draft-stone-atxn-01),
   which defines what an A2A transaction is.  ADRP defines what happens
   when a party contests one.

   ADRP severs an equivalence that every prior agentic commerce design
   has implicitly assumed: that a valid cryptographic proof bundle
   equals contractual satisfaction.  It does not.  Conduit-style
   cryptographic verifiers prove that an agent took specified actions;
   they do not prove that those actions satisfied the principal's Intent
   Mandate.  ADRP bifurcates disputes into a *cryptographic class*
   (resolvable by code from the proof bundle and mandate chain) and a
   *semantic class* (resolvable only against pre-committed machine-
   readable acceptance criteria, with arbitration escalation when those
   criteria are absent or under-specified).

   ADRP introduces the *Arbitration Mandate* as an ADRP extension that
   can be cryptographically linked to AP2 Intent/Cart/Payment Mandates
   or to an ATXN Standing Token.  It is not an AP2 core mandate.  The
   Arbitration Mandate records the principal's pre-committed dispute
   policy and is designed to support a written arbitration agreement
   where applicable; enforceability remains jurisdiction- and fact-
   specific.

   ADRP defines a *counter-attestation override pattern* in which a
   signed RulingBundle supersedes a Conduit ProofBundle by a signing-
   time precedence rule rather than by mutation.  Both the original
   attestation and the override are preserved forever in the hash chain;
   "override" is a verification-time computation, not a write.

   Companion specifications:

   *  *ATXN* (draft-stone-atxn-01): defines the A2A transaction
      primitive that ADRP resolves disputes over
   *  *AIVS* (draft-stone-aivs-01): cryptographic audit-trail substrate
      for proof bundles

   *  *VCAP* (draft-stone-vcap-01): verified-commerce escrow rails
      consumed by ADRP EscrowDirectives

   *  *ATEP* (draft-stone-atep-01): trust passports referenced by
      Standing Tokens in ADRP
- **draft-stone-atxn-01** (new-draft, score 14, adjacent_watchlist) [none]: [ATXN: Agent-to-Agent Transaction Definition Protocol](https://datatracker.ietf.org/doc/draft-stone-atxn/) — This document defines a canonical, defensible, machine-checkable
   primitive for an Agent-to-Agent (A2A) transaction.  It establishes
   the bundle of cryptographically signed elements that constitute a
   recorded value exchange between two software agents acting as
   instruments of identified principals, the conformance tiers that
   determine which elements are required, the rail-specific Profiles
   that map the bundle to existing payment infrastructure, and the two-
   tier validity model that distinguishes externally-adjudicable
   transactions from operationally-valid uncontested exchanges.

   ATXN is the foundational legal and technical primitive for escrow,
   dispute resolution, audit, and liability allocation in agentic
   commerce.  It is designed to produce evidence that can be mapped to
   existing contract and agency frameworks without requiring agent legal
   personhood.  Whether a Bundle has legal effect is jurisdiction- and
   fact-specific; this document does not provide a legal conclusion.  It
   maps directly to AP2, Stripe ACP, Visa TAP, Mastercard Agent Pay, and
   x402 as Profiles of a single canonical bundle.

   Companion specifications:

   *  *AIVS* (draft-stone-aivs-01): cryptographic audit-trail substrate
      that ATXN bundles inherit from

   *  *VCAP* (draft-stone-vcap-01): verified-commerce escrow rails that
      consume ATXN bundles

   *  *ATEP* (draft-stone-atep-01): trust passports that bind agents to
      capacity-attested principals

   *  *ADRP* (draft-stone-adrp-01): dispute resolution protocol invoked
      when an ATXN bundle enters the disputed state
- **draft-feria-sas-01** (new-draft, score 13, trust_infrastructure) [none]: [Agentic Saturation Stridency (SAS): A Quantitative Model and Admission Architecture for Autonomous Agent Traffic](https://datatracker.ietf.org/doc/draft-feria-sas/) — Autonomous computational agents are capable of generating high-
   frequency synthetic traffic that can cause a protected system to
   allocate memory, consume processing cycles, or invoke application-
   layer computational routines before the eligibility of an incoming
   request has been established.

   This document formalizes Agentic Saturation Stridency (SAS) as a
   measurable system condition defined by the ratio between the arrival
   rate of unverified agentic traffic over a discrete observation
   interval and the empirically sustainable admission capacity of the
   target boundary.

   The document defines three operational regimes (Subcritical,
   Critical, and Supercritical) and specifies a pre-runtime structural
   admission architecture designated Reality Layer 0 (RL0).  RL0
   establishes an ex-ante admission boundary intended to drop or reject
   unverifiable traffic before protected application-layer execution,
   incorporating bounded-state replay protection, out-of-band key
   revocation checking via probabilistic structures, constant-time
   cryptographic operations, and standardized wire encodings.

   The admission framework utilizes a signed Reality-Token (RT) and an
   admission predicate associated with the Invariant Reality Prism
   (IRP), listed as an Informative Reference in the NIST Cybersecurity
   Framework Online Informative References catalog under Reference ID
   189 (IRP-189).  The catalog entry is cited for informational
   provenance only and does not imply NIST authorship, endorsement,
   certification, or normative incorporation of the IRP framework.
- **draft-kavian-aep-oauth-session-credential-04** (new-draft, score 13, core_identity) [none]: [OAuth Bearer Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-oauth-session-credential/) — This document defines the OAuth Bearer session-credential grant type
   for the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an OAuth-style Bearer access token through the AEP
   Grant command while preserving baseline AEP client assertion
   authentication as the root of trust.
- **draft-pinto-agent-authz-contestability-00** (new-draft, score 13, authorization) [none]: [Contestability Bindings for Authorized Agent Actions](https://datatracker.ietf.org/doc/draft-pinto-agent-authz-contestability/) — Authorization artifacts can provide signed evidence of a permission
   under specified authorization rules.  Receipts can record a signed
   claim or protocol event that the authorization was exercised, and
   outcome evidence can describe what followed.  None of those artifacts
   necessarily tells a person or organization affected by the action
   where the authorization can be contested, which procedure applies,
   whether a filing changes execution state, or who selected the
   contestation forum.

   This document defines a transport-independent Contestability Binding
   for authorized agent actions.  The binding commits an authorization
   to a versioned Contestation Parameters Object that identifies the
   forum, submission mechanism, Standing Policy, procedure, time bounds,
   declared effect policy, and selection evidence.  A forum can
   acknowledge one exact authorization or publish a reusable acceptance
   manifest for closed Authorization Binding Profile and Authorization
   Trust Profile digest pairs.  A deterministic verifier validates the
   binding, separately classifies evidence claiming pre-execution
   verification by the executor, and reports forum-selection provenance
   as unilateral, multiparty, externally selected, or indeterminate.
   Where a filing is declared to affect execution state, the verifier
   also separates the issuer's declared policy, the executor's signed
   acceptance, the authenticated trigger, and the executor's claimed
   application.

   The mechanism makes the bound contestation parameters identifiable
   and verifiable, supporting discoverability while resisting post-
   action substitution.  It does not determine standing, prove forum
   independence, resolve a dispute, select a remedy, establish legal
   enforceability, or decide whether the original authorization was
   legitimate.
- **draft-stone-aivs-01** (new-draft, score 13, agent_identity) [none]: [AIVS: Agentic Integrity Verification Standard](https://datatracker.ietf.org/doc/draft-stone-aivs/) — The Agentic Integrity Verification Standard (AIVS) defines a
   portable, self-verifiable archive format for cryptographic proof of
   AI agent sessions.  An AIVS bundle is a gzip-compressed tar archive
   containing a SHA-256 hash-chained audit log, an Ed25519 digital
   signature over the chain, a machine-readable manifest, and an
   embedded verification script that requires only Python 3 standard
   library to execute.

   AIVS also defines *AIVS-Micro*: a minimal 6-field attestation (~200
   bytes) for continuous monitoring, embedded widgets, and API responses
   where a full session bundle is not required.

   AIVS enables any party to independently verify that:
- **draft-cowles-ward-00** (new-draft, score 12, agent_identity) [none]: [Write-once Append-only Receipt Digests (WARD): A Content-Free Hash-Chain Witnessing Protocol for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-cowles-ward/) — Write-once Append-only Receipt Digests (WARD) defines a minimal,
   interoperable protocol for producing tamper-evident, content-free
   hash-chain witnesses over events from agentic AI systems.  WARD
   observes events from companion protocols (Agent Envelope Exchange
   (AEE) messages, Agent Orchestration Control Layers (AOCL) decisions,
   and Verifiable Operations Ledger and Trace (VOLT) evidence records)
   and produces cryptographically linked receipts that prove specific
   events existed at specific points in time, without storing any event
   content.

   WARD entries record only source identifiers and payload hashes, never
   raw payloads, secrets, or personally identifiable information.
   Entries are linked via SHA-256 hash chains anchored by deterministic
   genesis hashes.  Periodic checkpoints called "tips" may be signed
   with Ed25519 and published to external append-only stores (sinks) for
   independent verification.  A meta-chain pattern allows witnessing
   tips from multiple sub-chains, providing deployment-wide integrity
   from a single verification point.

   The protocol is designed as a passive observer: witnessing never
   blocks, delays, or modifies the source event pipeline.  WARD failures
   are logged but never disrupt AEE transport, AOCL decisions, or VOLT
   recording.  This fire-and-forget integration model ensures that
   witnessing adds tamper-evidence guarantees without introducing
   operational risk.
- **draft-ietf-acme-pop-00** (new-draft, score 12, core_identity) [acme]: [Automated Certificate Management Environment (ACME) Extension for Proof-of-Possession](https://datatracker.ietf.org/doc/draft-ietf-acme-pop/) — The Automated Certificate Management Environment (ACME) protocol
   [RFC8555] requires a PKCS#10 Certificate Signing Request (CSR) at the
   finalization stage.  This document defines an optional extension that
   allows a client to prove possession of a private key directly,
   without constructing a CSR.  The extension is motivated by use cases
   where the CSR-based flow is problematic: KEM-only keys that cannot
   generate self-signatures, resource-constrained devices that benefit
   from reduced encoding overhead, and issuance models where the
   certificate is constructed from order and profile data (e.g., via the
   ACME Profiles extension [I-D.ietf-acme-profiles]) rather than a
   client-generated CSR.  This is particularly relevant when combined
   with compact encodings such as C509 certificates
   [I-D.ietf-cose-cbor-encoded-cert].

   In the "newOrder" request, the client declares the public key via a
   popKey field and includes a pop-type identifier whose value is the
   empty string.  The server creates a dedicated pop authorization
   containing a single pop-01 challenge, processed using the same state
   machine as any other ACME authorization.  When all authorizations
   (including the pop authorization) are valid, the ACME server issues a
   certificate using the validated public key and the authorized
   identifiers, eliminating the need for a CSR at finalization.  The
   extension is additive and strictly optional: clients that do not use
   it, and servers that do not support it, continue to use the standard
   CSR-based flow defined in [RFC8555] without any changes.
- **draft-kanojia-creduent-agent-uri-00** (new-draft, score 12, core_identity) [none]: [The 'agent' Uniform Resource Identifier (URI) Scheme and Cryptographic Attestation Protocol](https://datatracker.ietf.org/doc/draft-kanojia-creduent-agent-uri/) — This document specifies the 'agent' Uniform Resource Identifier (URI)
   scheme and its associated cryptographic attestation protocol.  The
   'agent' scheme defines a transport-agnostic, cryptographically
   verifiable addressing layer for identifying autonomous software
   agents, binding domain ownership via DNS TXT records, enforcing
   instruction integrity, and validating attenuated capability
   delegation tokens.
- **draft-morrison-identity-accord-03** (new-draft, score 12, core_identity) [none]: [Identity Accord Protocol: A Peer Ceremony for Bilateral Agreements Between Identity-Substrate-Bound Principals](https://datatracker.ietf.org/doc/draft-morrison-identity-accord/) — This memo specifies the Identity Accord Protocol, a peer ceremony by
   which two principals, each represented by an organisational identity
   substrate and acting under a recorded delegation from a legal entity,
   execute a bilateral agreement as a portable, self-verifying COSE-
   signed CBOR document.  The protocol composes DNS-based substrate
   discovery, Ed25519 sovereign signatures, an append-only identity log,
   and a tamper-evidence descriptor quorum into a single artefact that
   is verifiable by any third party with access to the public DNS, the
   parties' identity logs, and an on-chain anchor of the agreement's
   content hash.  The protocol does not require a central registry, a
   designated verifier, or any infrastructure operated by the
   specification's author; verification succeeds when the author's
   reference deployment is offline.  The canonical bilateral target is a
   mutual non-disclosure agreement, but the wire format generalises to
   any bilateral consent envelope between two legal entities each
   represented by an identity substrate.  An associated MCP tool
   surface, an associated pre-send enforcement gate, and an associated
   disclosure-ledger schema are specified, all of which are optional
   layers above the wire format.  The memo is Informational; the
   underlying COSE and CBOR formats are normative per [RFC9052] and
   [RFC8949].
- **draft-sparysh-pala-audit-00** (new-draft, score 12, trust_infrastructure) [none]: [PALA-1: A Tamper-Evident Audit Record Format for Constrained and Disconnected Deployments](https://datatracker.ietf.org/doc/draft-sparysh-pala-audit/) — This document describes PALA-1, a compact binary record format for
   tamper-evident audit trails produced by AI inference runtimes and
   robotic control systems.  It is designed for a class of deployment
   defined by three constraints that hold together: the hardware is
   computationally modest and its cycles are reserved for the workload
   and the power budget rather than for the audit trail; no external
   witness is reachable, whether because policy forbids outbound contact
   or because the platform operates beyond connectivity, so a witness is
   unavailable by rule or by physics rather than by circumstance; and
   the right to verify the trail is separated from the right to read
   what it records.

   Records form an append-only hash chain.  Integrity verification
   requires no key material of any kind, inspects no record bodies, and
   costs one hash per record rather than one signature.  The format
   distinguishes three separately answerable questions -- internal
   consistency, completeness against an external anchor, and existence
   at a point in time against an external witness -- and states which of
   the three a given trail actually supports rather than implying all
   three.

   The format is frozen at version 1.0 and is described here as it is.
   This document presents an existing wire format; it does not revise
   one.  Where a deployment does permit an external witness, a chain
   head may be published to a transparency service such as that of the
   Supply Chain Integrity, Transparency, and Trust architecture (SCITT,
   RFC 9943); that path is described but is not part of the hashing
   contract.
- **draft-stone-atep-02** (new-draft, score 12, agent_identity) [none]: [ATEP: Agent Trust and Execution Passport](https://datatracker.ietf.org/doc/draft-stone-atep/) — This document specifies the *Agent Trust & Execution Passport
   (ATEP)*, an open standard for representing an AI agent's verifiable
   track record of work across marketplaces and platforms.  ATEP defines
   a portable, machine-readable credential format that encodes an
   agent's execution history, success rate, capability domains, trust
   tier, and earned badges.  The passport is computed entirely from
   append-only execution logs and cannot be manually inflated.

   ATEP is the *trust layer* for agent-to-agent commerce.  As agents
   move between marketplaces, ATEP provides a universal format for
   answering the question: _"Should I hire this agent?"_
- **draft-sun-rats-composite-eat-00** (new-draft, score 12, trust_infrastructure) [none]: [An EAT Profile for Composite Platform Attestation](https://datatracker.ietf.org/doc/draft-sun-rats-composite-eat/) — This document defines an Entity Attestation Token (EAT) profile for
   composite platform attestation.  A Lead Attester, such as a platform
   Root of Trust, produces a single signed composite EAT that carries
   its own measurements and cryptographic digests committing to
   detached, native evidence collected from peripheral sub-attesters.
   The full sub-attester evidence -- Security Protocol and Data Model
   (SPDM) signed measurements, device-emitted EATs, or SPDM-carried TCG
   DICE Concise Evidence -- is conveyed verbatim as detached Claims-Sets
   in a Detached EAT Bundle.  This yields a single, freshness-bound,
   platform-scoped attestation artifact that a Verifier can appraise
   against platform-composition endorsements, even when the evidence is
   collected and conveyed by an untrusted mediator.
- **draft-cowles-aee-01** (new-draft, score 11, core_identity) [none]: [Agent Envelope Exchange (AEE): A Minimal JSON Envelope Format for Inter-Agent Communication](https://datatracker.ietf.org/doc/draft-cowles-aee/) — Agent Envelope Exchange (AEE) defines a minimal, transport-
   independent JSON envelope format for communication between autonomous
   AI agents, traditional services, and human participants.  The
   envelope comprises 14 well-defined fields that provide message
   identity, typing, correlation, tracing, priority, and extensibility
   without prescribing payload semantics or transport mechanisms.  AEE
   separates the concerns of message routing and lifecycle management
   (the envelope) from domain-specific meaning (intent schemas),
   enabling portable, composable, and auditable workflows across
   heterogeneous agent frameworks.  This document specifies the envelope
   structure, validity rules, conformance levels, entity identifier
   conventions, a reserved intent namespace for protocol negotiation,
   and a referencing strategy that avoids envelope nesting.
- **draft-das-child-safe-rendering-finality-03** (new-draft, score 11, core_identity) [none]: [Preventing Unauthorized Adult and Age-Restricted Content Rendering to Children Through Hardware-Rooted Execution Finality](https://datatracker.ietf.org/doc/draft-das-child-safe-rendering-finality/) — Online child-safety controls commonly operate before the final
   rendering boundary.  Platforms may use account-age flags, parental
   settings, content labels, recommender controls, server-side
   classification, age-assurance systems, access policies, or
   application filters to decide whether adult or age-restricted content
   should be available to a user.  Those controls are important, but an
   upstream decision does not by itself guarantee that the content
   cannot later be decrypted, decoded, composited, rendered, forwarded,
   mirrored, or otherwise materialized through another software or
   device path.

   The practical motivation is also personal.  As a father of three, I
   have encountered this same problem in my own family: a parent may
   understand that an unrestricted adult-configured phone should not be
   handed to a minor, yet a son or daughter may repeatedly ask to use
   the parent's phone and, in ordinary family life, the parent may
   eventually hand it over.  Human affection, trust, convenience, and
   everyday family circumstances cannot simply be designed away.
   Existing age checks, parental controls, child profiles, and
   application restrictions are useful, but they do not necessarily
   provide a simple device-wide protection for this moment of handover.
   Requiring the adult to provide a fingerprint, facial verification, or
   other authentication for every individual video would also create an
   impractical user experience.  This document therefore considers a
   Temporary Under-18 Handover Mode: before giving an adult-configured
   device to a child, the adult can place the device into a temporary
   minor-protection state, after which Execution-Finality makes that
   state technically consequential at the protected rendering boundary.
   This is therefore not only an abstract design problem for me; it is a
   solution developed to address a problem I encounter myself as a
   parent, with the broader aim of turning that everyday family
   difficulty into a practical protection that may also help other
   families.

   This problem is becoming more important as content delivery becomes
   more distributed, encrypted, AI-mediated, personalized, and
   dynamically generated.  A modern device may receive content through
   applications, browsers, content-delivery networks, embedded web
   views, messaging clients, recommendation systems, generative-AI
   services, caches, cloud gaming or streaming pipelines, local AI
   models, or third-party SDKs.  The security question is therefore no
   longer only whether content was classified or whether an age check
   occurred upstream.  A later question must also be answered: is this
   specific protected content authorized to become perceptible to this
   recipient, on this device, under the current eligibility, policy, and
   revocation state, at this moment?

   This document defines a protected rendering execution-finality
   architecture for adult, pornographic, sexually explicit, violent,
   gambling-related, or otherwise age-restricted content.  A proposed
   rendering is represented as a Restricted Content Candidate Act and
   remains in a Non-Renderable State until a Protected Enforcement
   Domain validates the applicable recipient, content, device, policy,
   age-or-eligibility, freshness, revocation, and sink predicates.
   Protected validation evidence is committed before, or atomically
   with, release of scoped non-bearer Rendering Finality Authority.

   A Protected Rendering Finality Sink independently verifies that
   authority immediately before the content becomes perceptible.
   Depending on the implementation, the sink may control content-key
   release, decryption, media-decoder enablement, GPU or compositor
   access, protected-surface creation, audio output, casting, screen
   mirroring, display enablement, or an equivalent materialization
   boundary.  Content bytes may therefore be delivered to a device while
   remaining technically non-renderable.

   The architecture deliberately does not define a universal age-
   estimation algorithm, identity system, or content-classification
   scheme.  Those mechanisms may supply inputs to the Protected
   Enforcement Domain.  This document defines the consequence-control
   step that prevents an upstream policy result from becoming merely
   advisory at the point of rendering.

   UNICEF has warned that pornographic content can harm children and
   that digital restrictions have not kept pace with technological
   shifts.  The ITU Child Online Protection programme provides global
   guidance for safer digital environments, and the United Nations
   Committee on the Rights of the Child has called for protection of
   children from harmful content and online risks in the digital
   environment.  The European Commission has likewise adopted
   protection-of-minors guidance and a privacy-preserving age-
   verification approach for adult-restricted content.  These materials
   motivate the problem addressed here; they do not endorse this
   particular technical architecture.

   The central protocol principle is: permission to deliver content is
   not permission to render it.
- **draft-gazitt-oauth-authzen-issuance-01** (new-draft, score 11, authorization) [none]: [AuthZEN Profile for OAuth 2.0 Token Issuance](https://datatracker.ietf.org/doc/draft-gazitt-oauth-authzen-issuance/) — Numerous OAuth 2.0 specifications define a moment at which an
   authorization server decides whether to issue a security token, and
   each of them declares the decision itself to be a matter of local
   policy that is out of scope.  The result is that a decision common to
   every OAuth deployment has no interoperable expression.

   This document defines a profile for using the OpenID AuthZEN
   Authorization API to externalize that decision to a Policy Decision
   Point.  It specifies how the inputs to a token issuance request map
   onto AuthZEN's mandatory five-tuple, how a Policy Decision Point
   response may shape the issued token, and how a Policy Decision Point
   advertises support for the profile.

   The mapping is complete for grants whose request names a single
   party, including the authorization code and client credentials
   grants.  Companion documents bind the grant families that add
   structure this document does not model, the token exchange family
   first among them.
- **draft-paxton-aicp-00** (new-draft, score 11, core_identity) [none]: [Agent Infrastructure Control Protocol](https://datatracker.ietf.org/doc/draft-paxton-aicp/) — Autonomous software agents increasingly inspect and modify
   infrastructure through provider-specific APIs and generic tool
   protocols.  Those interfaces expose operations, but they do not
   provide a common semantic contract for obtaining bounded situational
   context, expressing an intended outcome under constraints, reviewing
   the exact material effects, binding authorization to those effects,
   observing durable execution, and determining whether the intended
   outcome was achieved.

   This document specifies the Agent Infrastructure Control Protocol
   (AICP).  AICP is a transport-independent object and lifecycle model
   for capability discovery, situations, intents, plans, authorization
   decisions, asynchronous operations, verified outcomes, machine-
   actionable problems, and reconciliation.  It also specifies an HTTP
   binding and describes mappings to existing agent protocols.  AICP
   does not replace cloud resource APIs, orchestration languages, agent-
   to-agent protocols, authentication systems, or provider policy
   engines.
- **draft-reilly-banking-integrity-02** (new-draft, score 11, trust_infrastructure) [none]: [Reilly Banking Integrity Protocol (RBIP)](https://datatracker.ietf.org/doc/draft-reilly-banking-integrity/) — This document defines version 02 of the Reilly Banking Integrity
   Protocol (RBIP), a compliance-grade architecture for generating
   immutable, auditor- and regulator-verifiable evidence trails in
   banking operations.  RBIP combines cryptographic anchoring (via a
   public timestamping service) with archival deposit under a
   persistent identifier to produce permanent, tamper-evident records
   across three compliance domains: Proof-of-Reserves & Liquidity
   (PRL), Loan Origination & Collateral Chain (LOC), and KYC/AML
   Evidence Ledger (KAL), plus a system evidence domain (SYS) covering
   RBIP's own access, key, disclosure, and continuity events.

   This revision corrects defects in draft-reilly-banking-integrity-01
   that would have prevented independent verification.  It replaces the
   -01 Merkle construction with the construction of [RFC9162] and
   prohibits leaf duplication; moves Merkle leaves from the payload
   digest to a digest over the full signed Evidence Item; resolves
   three conflicting definitions of prev_digest; separates the anchored
   Bundle Core from the mutable anchor and archival metadata,
   eliminating the -01 circularity in which the anchored digest could
   not match the archived artifact; replaces unsalted identifier
   hashes with salted field commitments; and resolves the -01 conflict
   between its plaintext officer-name fields and its own prohibition on
   plaintext personal data.

   This revision also adds an Evidence Coverage Attestation, because
   integrity of submitted evidence is not evidence of completeness;
   mandatory heartbeat bundles, so that truncation of an evidence chain
   is detectable; explicit pending and attested anchor states in place
   of a fixed confirmation count; a Suspicious Activity Report
   confidentiality section, because publicly archiving KAL bundle
   metadata as described in -01 could disclose the existence of a
   report; algorithm suite identifiers and bridging records for hash
   and signature migration; a key discovery and revocation mechanism;
   and a prohibition on automated remediation of integrity violations.

   RBIP is intended to help financial institutions evidence compliance
   with Basel III/IV, SOX, BSA/AML, DORA, MiCA, ISO/IEC 42001:2023, and
   other applicable regimes while preserving privacy, accountability,
   and auditability.

   This document is published as a prior art record in the sense
   described in [I-D.reilly-rem-protocol]: a public, timestamped
   disclosure under 35 U.S.C. 102(a)(1) [USC-35-102].  Publication as
   a prior art record is a record of disclosure and its date.  It is
   not a determination of novelty, priority, or patentability, and no
   such determination is claimed here.
- **draft-saha-aadp-02** (new-draft, score 11, core_identity) [none]: [The Agent Action Decision Protocol (AADP): Per-Action Authorization for AI Agents](https://datatracker.ietf.org/doc/draft-saha-aadp/) — The Agent Action Decision Protocol (AADP) separates per-action
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
- **draft-sato-soos-cap-rrs-03** (new-draft, score 11, trust_infrastructure) [none]: [Constitutional AI Protocol -- Regulation Record Specification (CAP-RRS)](https://datatracker.ietf.org/doc/draft-sato-soos-cap-rrs/) — Compliance with applicable law should be a package import, not a
   Cedar authoring problem.

   The Constitutional AI Protocol (CAP) defines the enforcement
   architecture for governed AI agent systems: a three-tier Cedar
   policy evaluation model that distinguishes absolute prohibitions,
   jurisdictional legal constraints, operator policies, and resource
   limits.  CAP specifies what the Governance Execution Controller
   (GEC) does when a Cedar policy fires.  It does not specify how
   Cedar policies are authored, certified, distributed, or maintained
   as law changes.

   This document defines the Regulation Record: the structured
   representation of a compliance obligation at any CAP tier.  A
   Regulation Record is the human-readable, machine-compilable
   intermediate form between legal text and Cedar policy.  This
   document specifies the Regulation Record schema, the Cedar
   Compilation Profile that governs how Regulation Records are
   translated into Cedar policies, the conflict declaration model,
   the certification model governing which publishers may certify
   records at each tier, and the versioning and update protocol for
   the Constitutional Mandate Registry.

   Version -02 adds the Law Reference Interface (LRI) generic model,
   the Statute-Primacy Rule, and the Operational Requirements for
   catalog amendment and interpretation detection.  These three
   additions complete the regulation lifecycle: from law encoding
   through law reference and provenance, through the consequences of
   law amendment, through the operational cadence governing
   detection and response.

   Version -03 corrects the Statute-Primacy Rule's event schemas to
   record resolution as a new, causally-linked GAR event rather than
   an in-place mutation of the original conflict event.

   The core developer experience this document enables: a developer
   imports certified Regulation Record packages from the
   Constitutional Mandate Registry, declares their own Tier 2
   operator policies and Tier 3 resource policies, calls compile(),
   and receives a Cedar policy set ready for GEC loading.  No Cedar
   is authored by hand for compliance purposes.  Compliance is a
   package management operation.
- **draft-sato-soos-hem-07** (new-draft, score 11, agent_identity) [none]: [The Human Escalation Mechanism (HEM) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-hem/) — An AI agent that has been authorized to act autonomously has no
   inherent mechanism to stop itself.  If its mission requires a
   decision that exceeds its authorization, if policy mandates human
   judgment before proceeding, or if the agent itself reaches the
   boundary of its reliable competence, what happens?  Without a
   protocol specifying the answer, one of three failure modes occurs:
   the agent proceeds beyond its authorization and executes actions
   that no human approved; it stalls silently with no notification
   to any principal; or it continues running under a mission that has
   already entered a terminal state, producing actions with no
   legitimate purpose.  In all three cases, the humans responsible
   for the system find out too late.

   This document defines the Human Escalation Mechanism (HEM): a
   normative protocol specifying what a Governance Execution
   Controller (GEC) does when an AI agent session requires human
   judgment before execution may continue.  HEM replaces the three
   failure modes above with a single governed path: the GEC places
   the session into a formally defined HEM_PENDING state, routes a
   structured escalation request to one or more designated human
   principals along an ordered designation chain, enforces a
   prohibition on all state transitions until a human decision is
   received, and processes six defined human decision types.  HEM
   also defines the Policy Rationale Declaration (PRD), which links
   Cedar policies that route to HEM with machine-readable rationale,
   and the Decision Rationale Record (DRR), which captures the human
   principal's reasoning for audit and learning purposes.

   Version -05 adds ten new HEM interaction classes (HEM-PRE-1,
   HEM-PRE-2, HEM-DS-1, HEM-DS-2, HEM-LIM-1, HEM-DIV-1, HEM-HIGH-1,
   HEM-FAT-1, HEM-EMO-1, and HEM-CONSENT) with full normative
   specifications, trigger conditions, GAR ALE registrations
   (ALE-030 through ALE-041), and five new Security Considerations
   addressing the HEM channel attack surface.  INV-HEM-01 (The
   Surfacing Obligation) is added as a KernelSpec invariant, along
   with normative Human Readiness Score (HRS) and Tier 0-A
   Integration sections.

   Version -06 corrects an internal contradiction over whether HRS
   data persists across sessions, reconstructs several sections whose
   base content had gone missing from the -05 text, and extends
   DoS rate-limiting guidance to the -05 interaction-class triggers.

   Version -07 is an editorial revision with no normative content
   changes: bracket-delimited array type notation ([string], [object])
   and a state-diagram terminal-state label were reworded to resolve
   idnits parser warnings that misread them as broken citations.

   HEM is enforced by the GEC, not by the agent and not by the
   application layer.  An agent cannot opt out; an application cannot
   suppress it.  This non-bypassability is the source of HEM's
   regulatory utility and provides the technical specification for
   human oversight required by EU AI Act Article 14.
- **draft-sirkkavaara-vaara-receipt-10** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
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
- **draft-stone-swarmscore-v1-01** (new-draft, score 11, adjacent_watchlist) [none]: [SwarmScore V1: Volume-Scaled Agent Reputation Protocol](https://datatracker.ietf.org/doc/draft-stone-swarmscore-v1/) — SwarmScore V1 is a transparent, community-governed open standard for
   agent reputation scoring in open marketplaces.  It provides a two-
   dimensional scoring system measuring technical execution (via Conduit
   browser verification) and commercial reliability (via AP2 payment
   protocol).  Volume-scaled metrics reward consistent high-volume
   performance.  Cryptographically signed certificates enable
   decentralized trust.  This document specifies the complete V1
   standard including formula, trust tiers, escrow integration, wire
   format, governance model, legal framework, implementation guidance,
   V2 roadmap, competitive analysis, and known limitations, with a
   governance roadmap for transitioning canary prompt curation to a
   multi-stakeholder community registry.
- **draft-stone-vcap-ap2-binding-01** (new-draft, score 11, core_identity) [none]: [VCAP-AP2 Binding: Verified Delivery Settlement for the Agent Payments Protocol](https://datatracker.ietf.org/doc/draft-stone-vcap-ap2-binding/) — This document defines a binding between Verified Commerce for Agent
   Protocols (VCAP) and the Agent Payments Protocol (AP2).  AP2 supplies
   agent-commerce authorization evidence through IntentMandate,
   CartMandate, and PaymentMandate artifacts.  VCAP supplies delivery
   verification, settlement evidence, escrow directives, timeout
   handling, and dispute handoff.

   This revision deliberately does not model AP2 as an escrow or
   settlement state machine.  Current AP2 positions itself as an
   authorization and security layer used within a surrounding commerce
   protocol, including Universal Commerce Protocol (UCP).  Accordingly,
   this binding references AP2 mandates by cryptographic digest or
   opaque identifier and leaves payment capture, refund, and settlement
   transitions to the commerce protocol and payment rail.
- **draft-cowles-volt-01** (new-draft, score 10, agent_identity) [none]: [Verifiable Operations Ledger and Trace (VOLT) Protocol](https://datatracker.ietf.org/doc/draft-cowles-volt/) — The Verifiable Operations Ledger and Trace (VOLT) protocol defines a
   minimal, interoperable format for producing tamper-evident execution
   traces for agentic AI workflows.  VOLT records are linked via SHA-256
   hash chains and packaged into portable Evidence Bundles that can be
   verified independently by any conformant implementation.

   VOLT functions as a "flight recorder" for AI agent operations: it
   captures the sequence of events -- messages received, policy
   decisions evaluated, human approvals granted, tools invoked, and
   results returned -- with cryptographic integrity guarantees that
   detect post-hoc modification, deletion, or insertion of records.

   The protocol is privacy-first by design.  Events carry metadata and
   content-addressed references rather than raw secrets or sensitive
   payloads.  Evidence Bundles support explicit redaction, optional
   Ed25519 signatures for non-repudiation, and both rolling and final
   snapshot modes for long-running workflows.
- **draft-das-execution-finality-ai-interoperability-02** (new-draft, score 10, authorization) [none]: [Secure and Privacy-Preserving AI Interoperability under Article 6(7) of the European Digital Markets Act: An Execution-Finality Architecture](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — This document presents a security- and privacy-preserving execution-
   finality architecture for third-party AI interoperability under the
   European Digital Markets Act (DMA).  It is designed to enable
   meaningful participation by external AI assistants while keeping
   consequential device actions under bounded, verifiable platform
   control.

   The architecture separates an AI-generated request from the authority
   to make that request externally effective.  A requested operation
   remains in a Non-Effective State until protected infrastructure
   validates the requester, intended resource, destination, user
   authorization or intent where required, purpose and scope, freshness,
   revocation state, runtime conditions, and other applicable policy
   predicates.

   After successful validation, the system creates narrowly scoped, non-
   bearer execution authority bound to the specific Candidate Act. At
   the Finality Sink—the first boundary at which the operation can
   become externally effective—the system independently verifies that
   the actual operation still matches the validated act and that the
   authority remains current and unused.

   This design is intended to address major security risks associated
   with AI interoperability, including prompt injection, compromised
   assistant or cloud infrastructure, confused-deputy behavior, replay,
   token theft or reuse, destination or parameter substitution, scope
   escalation, stale authorization, alternate-path bypass, and
   unauthorized consequential execution.

   It also supports privacy protections by limiting access and
   effectuation to the minimum act-specific scope, reducing dependence
   on broad reusable permissions, preserving revocation and user-control
   boundaries, and preventing data release or transmission when the
   protected validation conditions are not satisfied.

   The resulting model is open participation with bounded, verifiable
   authority: third-party AI systems may interoperate with device
   functions without receiving unrestricted final-effect authority,
   while the platform retains protected enforcement over whether a
   proposed action is permitted to become externally effective.

   The length of this document is intentional.  It aims to work through
   the major security- and privacy-related objections associated with
   third-party AI interoperability at a technical level of detail
   sufficient to show that they are addressed, rather than merely
   asserted, and reviewers are welcome to engage with any section on its
   own merits.
- **draft-mih-scitt-checkpointed-local-log-00** (new-draft, score 10, trust_infrastructure) [none]: [The Checkpointed Local Log (CLL)](https://datatracker.ietf.org/doc/draft-mih-scitt-checkpointed-local-log/) — Many systems emit individually signed records — receipts,
   attestations, statements — and store them locally.  Each record
   verifies on its own, but the collection proves nothing: records can
   be deleted, reordered, or created after the fact without detection.
   This document specifies the Checkpointed Local Log (CLL): a producer-
   operated append-only log, built on the Merkle Mountain Range
   structure whose COSE proof formats are specified in
   [I-D.bryce-cose-receipts-mmr-profile], together with a small signed
   checkpoint that commits to the log's entire history.  Records of any
   format are appended as they are produced; checkpoints are emitted on
   a declared cadence and may be registered with one or more independent
   Transparency Services or witnesses using existing SCITT registration.
   A CLL upgrades a set of point receipts into a stream with provable
   order, contemporaneity, and completeness — while defining precisely,
   and narrowly, what such a log does and does not establish.  This
   document defines the log discipline and the checkpoint structure; it
   defines no new proof formats, no transparency service behavior, and
   no payload semantics.
- **draft-nemethi-dawn-aid-00** (new-draft, score 10, core_identity) [none]: [Agent Identity and Discovery (AID)](https://datatracker.ietf.org/doc/draft-nemethi-dawn-aid/) — Agent Identity and Discovery (AID) answers one question: given a
   domain, where is the agent and which protocol should a client speak?
   An AID client queries a DNS TXT record at the well-known subdomain
   _agent.<domain> and learns the service endpoint URI, protocol token,
   authentication hint, and optional metadata for that agent.

   This document defines the AID v2 (`aid2`) record format, client
   discovery algorithm, exact-host lookup rules, endpoint-proof (PKA)
   handshake using Ed25519 HTTP Message Signatures, security
   requirements, and IANA registrations for the `_agent` DNS node name
   and the `agent` service name.  The legacy `aid1` record format is
   retained as a compatibility format for clients migrating from earlier
   deployments.  AID is intentionally small; after discovery, protocol-
   specific mechanisms such as MCP or A2A handle communication and
   capability negotiation.
- **draft-reilly-government-integrity-02** (new-draft, score 10, core_identity) [none]: [Reilly Government Integrity Protocol (RGIP): Multi-Layer, Quantum-Resilient Framework for Permanent and Tamper-Evident Public Records](https://datatracker.ietf.org/doc/draft-reilly-government-integrity/) — The Reilly Government Integrity Protocol (RGIP) defines a
   standards-aligned method for producing permanent, independently
   verifiable public records by combining multi-algorithm content
   hashing, public timestamp anchoring, archival deposit under a
   persistent identifier, decentralized storage, and web archiving into
   a single pipeline.

   This revision corrects defects in
   draft-reilly-government-integrity-01 that would have prevented
   independent verification or overstated the guarantees the protocol
   provides.  It replaces the -01 SHA3-512-only Cross-Chain Hash, which
   made a single algorithm the sole binding of three otherwise
   independent chains, with an entangled link-and-braid construction in
   which each chain consumes the prior state of all three.  It defines a
   canonical, domain-separated, length-delimited encoding for every
   hashed input, removing the concatenation ambiguity present in -01.
   It separates the signed Evidence Receipt Core from the mutable anchor
   envelope, resolving the -01 condition in which confirming an anchor
   invalidated the signature over the record it described.  It adds
   Chain Checkpoint anchoring, without which the -01 claim that record
   sequence is provable did not hold, since -01 anchored only artifact
   digests and never the chain itself.  It replaces raw digests of
   low-entropy government records with salted field commitments, adds
   explicit pending and attested anchor states, adds a Revocation
   Registry and Hash Migration Bridging Records, replaces the
   quantum_resilient boolean with a declared algorithm suite, prohibits
   automated repair of chain integrity violations, and narrows the -01
   post-quantum claims to what the constructions support.  It also
   documents the function of RGIP records and of this specification as
   prior art records under 35 U.S.C. 102(a)(1), consistent with the
   treatment in version -02 of the REM Protocol specification.
- **draft-sato-soos-mad-04** (new-draft, score 10, authorization) [none]: [Multi-Agent Delegation in Sovereign Object Systems](https://datatracker.ietf.org/doc/draft-sato-soos-mad/) — When a consequential task requires multiple AI agents -- one to
   coordinate, others to execute, each operating on different objects
   in a shared workflow -- who is responsible for the outcome?  Which
   agent caused which state change?  Under whose authority?  If the
   coordinating agent's authorization is revoked, does the authority
   of every sub-agent it delegated to immediately expire?  If one
   agent in a parallel workflow exceeds its scope, can that excess
   propagate to others?

   This document defines the Multi-Agent Delegation (MAD) protocol,
   extended in version -03 with four new normative mechanisms: the
   Sub-Agent Composition Record (SACR) for kernel-governed sub-agent
   spawning; the hub-only constraint for sub-agent communication
   topology; XPID cross-cluster integration derived from KIA-03; and
   full normative specifications for the R-1 through R-7 revocation
   trigger classes with completion states and cascade behavior.
   Version -04 adds an eighth trigger class, R-8 (Compromise), closing
   a gap identified while mapping MAD's taxonomy onto the Mandate
   Lifecycle Events (MLE) profile's `reason: compromise` value, which
   had no R-code counterpart.

   MAD provides a single recoverable property: the accountability
   chain is always reconstructable from the GEC-signed audit record
   alone.  Cascade revocation means one decision stops the entire
   tree.  SACR means the spawning of that tree is itself governed.
- **draft-surampudi-wtx1-01** (new-draft, score 10, authorization) [none]: [WTX-1: Cross-Domain Context Preservation Protocol](https://datatracker.ietf.org/doc/draft-surampudi-wtx1/) — This document defines WTX-1, a protocol for preserving pseudonymous
   user context across web domains that are operated by, or on behalf
   of, the same organization and that have mutually opted into the
   exchange.  The protocol operates only after explicit user consent and
   does not use third-party cookies, browser fingerprinting, or
   collection of direct identifiers by default.  Identifiers are
   pseudonymous, not anonymous: they can be linked to application-level
   identities by the deploying organization and may constitute personal
   data under applicable law.

   WTX-1 transfers context using an encrypted, authenticated,
   destination-bound, single-use token carried in the URL fragment.
   Tokens are issued and verified server side, with atomic replay
   consumption, DNS-based domain authorization, and short-lived server-
   signed write grants that authorize browser write operations without
   trusting caller-supplied tenant claims.

   This revision (draft-02) replaces the signed-cleartext token format
   of draft-01 with a sign-then-encrypt construction, specifies write
   grants and replay-consumption ordering, defines the consent lifecycle
   including withdrawal and asynchronous cancellation, adds storage
   retention limits and user inspection, reset, and revocation controls,
   and rescopes the document's security, privacy, and performance claims
   to match the reviewed reference implementation.  A complete change
   log appears in Appendix A.
- **draft-abak-agent-control-delivery-evidence-01** (new-draft, score 9, authorization) [none]: [Evidence Requirements for Agent Control Delivery and Outcome Reconciliation](https://datatracker.ietf.org/doc/draft-abak-agent-control-delivery-evidence/) — Agent systems can issue stop, suspend, revoke, constrain, cancel, or
   override instructions across system and administrative boundaries.  A
   record that such a control was decided or dispatched does not
   establish that every intended enforcement point received or applied
   it.  Conversely, the absence of an acknowledgement does not, by
   itself, establish non-delivery.

   This document defines format-independent evidence requirements for
   preserving those distinctions.  It separates issuer-side emission,
   required-target resolution, receiver-side observation, enforcement
   outcome, and observation of the resulting control effect.  For a
   control that must reach more than one enforcement target, the unit of
   delivery reconciliation is an instruction-target obligation rather
   than the parent instruction alone.  The document also defines bounded
   negative observations, total reconciliation, population conservation,
   semantic-preservation requirements for intermediary paths, and a
   separate qualification for the evidentiary strength of aggregate
   claims.

   This document does not define a receipt format, wire protocol,
   authorization system, policy language, transparency service, or audit
   regime.
- **draft-chu-oauth-subject-key-binding-00** (new-draft, score 9, authorization) [none]: [OAuth Subject Signing Key Binding for Resource Servers](https://datatracker.ietf.org/doc/draft-chu-oauth-subject-key-binding/) — Resource servers in OAuth deployments sometimes receive application-
   layer authorization evidence that is digitally signed by the subject
   represented by an access token.  Verification of such evidence
   requires the resource server to obtain a trusted public signing key
   that is bound to that subject.

   This specification defines the subject_keys parameter, by which an
   OAuth authorization server conveys one or more subject public signing
   keys to a resource server.  The parameter can be carried as a claim
   in a JWT access token or as a member of a token introspection
   response.  The resulting key binding is scoped to the authorization
   server, token subject, resource server audience, and token validity
   context.

   This specification does not define a public-key enrollment protocol
   or the syntax and semantics of the application-layer authorization
   evidence.  It also does not use the OAuth cnf claim, which identifies
   a proof-of-possession key held by the presenter of a token.
- **draft-fassbender-scitt-time-anchor-06** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-gazitt-oauth-authzen-token-exchange-01** (new-draft, score 9, authorization) [none]: [AuthZEN Binding for OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/draft-gazitt-oauth-authzen-token-exchange/) — OAuth 2.0 Token Exchange (RFC 8693) defines the moment at which an
   authorization server decides whether one party may obtain a token to
   act as, or on behalf of, another.  It states that the decision is
   governed by policy, and does not define that policy.  The
   specifications layered on top of it - identity chaining, identity
   assertion authorization grants, and transaction tokens - inherit the
   same seam.

   This document binds those flows to the AuthZEN profile for OAuth 2.0
   token issuance.  It specifies how a token exchange request is derived
   into AuthZEN evaluation requests, how the authority of the requesting
   party is expressed as a decision distinct from the authority being
   delegated, and what each of the token types layered on token exchange
   contributes to that mapping.
- **draft-gould-regext-epp-status-set-04** (new-draft, score 9, core_identity) [none]: [Status Set Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-gould-regext-epp-status-set/) — This document describes an Extensible Provisioning Protocol (EPP)
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
- **draft-hamr-oauth-agent-delegation-01** (new-draft, score 9, authorization) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document specifies a profile for delegating authorization to
   automated agents across administrative domains.  It defines an HTTP
   header field, Agent-Delegation, that carries a chain of attenuated
   delegation links.  Each link narrows the scope, tightens or holds a
   set of floor conditions, and shortens or holds the expiry of its
   parent.  A verifier checks every link in the chain, not only the
   last, and rejects the chain if any link violates attenuation.  The
   profile is deliberately agnostic to the credential format and to the
   nature of the entity that issues floor attestations; it specifies
   required properties, not a specific encoding or a specific kind of
   issuer.  It composes with, and does not replace, existing work on
   agent credential provisioning and posture.
- **draft-ietf-acme-authority-token-jwtclaimcon-05** (new-draft, score 9, core_identity) [acme]: [JWTClaimConstraints profile of ACME Authority Token](https://datatracker.ietf.org/doc/draft-ietf-acme-authority-token-jwtclaimcon/) — This document defines an authority token profile for the validation
   of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate
   extensions within the Automated Certificate Management Environment
   (ACME) protocol.  This profile is based on the Authority Token
   framework and establishes the specific ACME identifier type,
   challenge mechanism, and token format necessary to authorize a client
   to request a certificate containing these constraints.
- **draft-ietf-oauth-v2-1-16** (new-draft, score 9, authorization) [oauth]: [The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) — The OAuth 2.1 authorization framework enables an application to
   obtain limited access to a protected resource, either on behalf of a
   resource owner by orchestrating an approval interaction between the
   resource owner and an authorization service, or by allowing the
   application to obtain access on its own behalf.  This specification
   replaces and obsoletes the OAuth 2.0 Authorization Framework
   described in RFC 6749 and the Bearer Token Usage in RFC 6750.
- **draft-kodden-oidfed-admin-00** (new-draft, score 9, core_identity) [none]: [OpenID Federation Node Administration Protocol](https://datatracker.ietf.org/doc/draft-kodden-oidfed-admin/) — This document specifies a compact HTTP application programming
   interface for administering an OpenID Federation node.  The interface
   manages the operator-controlled inputs from which a node produces the
   Entity Configurations, Subordinate Statements, Trust Marks, and
   Federation Entity Keys defined by OpenID Federation 1.1.  It does not
   replace the public federation protocol.  It is the management plane
   used by operators and control-plane software to configure what that
   protocol publishes.

   The design is document-oriented.  Operators read and write the same
   JSON objects OpenID Federation already defines, rather than a large
   set of per-claim endpoints.  Five resources cover node identity,
   Federation Entity Keys, the node's Entity Configuration, Immediate
   Subordinates, and Trust Mark issuance.
- **draft-rosomakho-tls-wimse-cert-hint-03** (new-draft, score 9, core_identity) [none]: [Workload Identifier Origin Hint for TLS ClientHello](https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/) — This document defines a TLS extension that allows clients to indicate
   one or more workload identifier origins in the ClientHello message.
   Each origin consists of a URI scheme and trust domain component,
   representing the administrative domain and identifier namespace in
   which the client operates.  These identifier origins serve as hints
   to enable the server to determine whether client authentication is
   required and which policies or trust anchors should apply.  This
   mechanism improves efficiency in mutual TLS deployments while
   minimising the exposure of sensitive identifier information.  To
   protect confidentiality, this extension can be used in conjunction
   with Encrypted Client Hello (ECH).
- **draft-efstathiou-samp-agent-management-01** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
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
- **draft-gazitt-oauth-authzen-claims-01** (new-draft, score 8, authorization) [none]: [AuthZEN Profile for Authorization Claims in JWT Access Tokens](https://datatracker.ietf.org/doc/draft-gazitt-oauth-authzen-claims/) — RFC 9068 recommends that an authorization server placing group
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
- **draft-ietf-lamps-csr-attestation-29** (new-draft, score 8, trust_infrastructure) [lamps]: [Use of Remote Attestation with Certification Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) — Certification Authorities (CAs) issuing certificates to Public Key
   Infrastructure (PKI) end entities may require a certificate signing
   request (CSR) to include additional verifiable information to confirm
   policy compliance.  For example, a CA may require an end entity to
   demonstrate that the private key corresponding to a CSR's public key
   is secured by a hardware security module (HSM), is not exportable,
   etc.  The process of generating, transmitting, and verifying
   additional information required by the CA is called remote
   attestation.  While work is currently underway to standardize various
   aspects of remote attestation, a variety of proprietary mechanisms
   have been in use for years, particularly regarding protection of
   private keys.

   This specification defines ASN.1 structures which may carry
   attestation data for PKCS#10 and Certificate Request Message Format
   (CRMF) messages.  Both standardized and proprietary attestation
   formats are supported by this specification.
- **draft-kavian-agent-enrollment-protocol-04** (new-draft, score 8, core_identity) [none]: [The Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-agent-enrollment-protocol/) — The Agent Enrollment Protocol (AEP) defines an HTTP-based mechanism
   for autonomous agents to discover service enrollment requirements,
   enroll an agent identity, obtain optional session credentials, revoke
   those credentials, and query enrollment status.  AEP uses
   Decentralized Identifiers, client assertion JWTs, and HTTP Problem
   Details to provide a narrow machine-first enrollment and
   authentication substrate for agent-to-service interactions.
- **draft-richardson-rats-geographic-results-03** (new-draft, score 8, trust_infrastructure) [none]: [Geographic Attestation Results](https://datatracker.ietf.org/doc/draft-richardson-rats-geographic-results/) — Many workloads have limitations on what geography they are allowed to
   operate in.  This is often due to a regulation that requires that the
   computation occur in a particular jurisdiction.

   There are many mechanisms by which Evidence of location may be
   created and then evaluated by a Verifier.  No matter which mechanism
   is appropriate for a given situation, the result of the Verification
   can be expressed in a similiarly defined EAT Attestation Result.

   This document is about encoding a variety of geographical conclusions
   conclusions in an Attestation Result.  In addition, one mechanism of
   directly creating a geographic result in the form of an Endorsement
   is described in an appendix.
- **draft-stone-swarmscore-v2-canary-01** (new-draft, score 8, core_identity) [none]: [SwarmScore V2 Canary: Safety-Aware Agent Reputation Protocol](https://datatracker.ietf.org/doc/draft-stone-swarmscore-v2-canary/) — SwarmScore V2 Canary extends the SwarmScore V1 two-pillar reputation
   protocol with a third dimension: Safety, measured via controlled
   canary prompt testing.  This document specifies five formally-
   analyzed design decisions for the canary testing subsystem: mandatory
   testing thresholds, hybrid response classification (pattern matching
   plus opaque LLM ensemble), dedicated test session placement, prompt
   library composition and rotation, and session isolation to reduce
   buyer-harm risk.  V2 Canary is backwards-compatible with V1: all V1
   scores remain unchanged.  The five-pillar formula covers Technical
   Execution (300 pts), Commercial Reliability (300 pts), Operational
   Depth (150 pts), Safety (100 pts), and Identity Verification (150
   pts).
- **draft-cowles-aocl-01** (new-draft, score 7, core_identity) [none]: [Agent Orchestration Control Layers (AOCL) Protocol](https://datatracker.ietf.org/doc/draft-cowles-aocl/) — Agent Orchestration Control Layers (AOCL) is a protocol that
   standardizes how an orchestrator processes incoming events by passing
   them through a layered control pipeline.  AOCL defines an eleven-
   layer taxonomy covering ingress normalization, identity scoping,
   smart routing, policy gating, plan decomposition, context retrieval,
   prompt shaping, delegation and execution, verification, response
   assembly, and audit writeback.  The protocol is runtime-agnostic and
   framework-agnostic, producing auditable governance traces as a first-
   class output.  AOCL supports both sequential pipeline and directed
   acyclic graph (DAG) execution modes, with explicit bypass and branch
   semantics that mandate audit records for all control-flow deviations.
- **draft-ietf-ocm-open-cloud-mesh-07** (new-draft, score 7, authorization) [ocm]: [Open Cloud Mesh](https://datatracker.ietf.org/doc/draft-ietf-ocm-open-cloud-mesh/) — Open Cloud Mesh (OCM) is a server federation protocol that is used to
   notify a Receiving Party that they have been granted access to some
   Resource.  It has similarities with authorization flows such as
   OAuth, as well as with social internet protocols such as ActivityPub
   and email.

   A core use case of OCM is when a user (e.g., Alice on System A)
   wishes to share a resource (e.g., a file) with another user (e.g.,
   Bob on System B) without transferring the resource itself or
   requiring Bob to log in to System A.

   While this scenario is illustrative, OCM is designed to support a
   broader range of interactions, including but not limited to file
   transfers.

   Open Cloud Mesh handles interactions only up to the point where the
   Receiving Party is informed of their access to the Resource.  Actual
   Resource access is subsequently managed by other protocols, such as
   WebDAV.
- **draft-kavian-aep-api-key-session-credential-04** (new-draft, score 7, core_identity) [none]: [API-Key Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-api-key-session-credential/) — This document defines the API-key session-credential grant type for
   the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an opaque API key through the AEP Grant command for
   deployments that already operate header-based API-key authentication.
- **draft-kavian-aep-basic-session-credential-04** (new-draft, score 7, core_identity) [none]: [Basic Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-basic-session-credential/) — This document defines the Basic session-credential grant type for the
   Agent Enrollment Protocol (AEP).  The grant type lets an AEP Service
   issue an HTTP Basic credential through the AEP Grant command for
   deployments that already integrate with Basic authentication
   middleware.
- **draft-kavian-aep-platform-hosted-identity-01** (new-draft, score 7, core_identity) [none]: [AEP Platform Hosted Identity](https://datatracker.ietf.org/doc/draft-kavian-aep-platform-hosted-identity/) — This document defines interoperable hosted identity behavior for
   Agent Enrollment Protocol (AEP) Platforms.  It lets a Platform
   provision Service-scoped Agent did:web identities, publish DID
   documents, custody signing keys, and produce AEP client assertion
   JWTs through delegated signing operations.
- **draft-morrison-binding-moment-envelope-02** (new-draft, score 7, adjacent_watchlist) [none]: [The Briefing-and-Binding Envelope: A Delivery Contract for Agent-to-Principal Decision Moments with Dual-Veto Reconciliation](https://datatracker.ietf.org/doc/draft-morrison-binding-moment-envelope/) — This memo specifies the briefing-and-binding envelope: a delivery
   contract for the wire-level structure by which an artificial-
   intelligence agent surfaces a consequential decision to the human
   principal it acts for, and by which the principal commits, declines,
   amends, or rejects that decision.  The envelope carries eight named
   slots (a synopsis, findings, recommendations, an offer of detail, a
   question stem, a set of options each marked with its own reasoning, a
   single recommended option, and a pair of escape hatches) and is
   emitted as a structured field of a Model Context Protocol [MCP] tool
   result.  The contribution is the delivery contract itself: a single
   renderer-agnostic envelope so that the briefing an agent delivers and
   the binding a principal commits back have one machine-checkable shape
   across every consuming surface.  The central element is the dual-veto
   handshake: one escape hatch lets the principal revise the answer
   space while accepting the question; the other lets the principal
   reject the question itself and reopen deliberation.  Either party may
   veto.  The memo defines a content digest over the envelope,
   canonicalized under JCS and hashed with SHA-256, so that a resolution
   names the exact envelope it resolves and an external receipt can
   reference that envelope by digest.  The memo is Informational.  No
   new transport is introduced; the envelope composes with the handle
   namespace of [IDPRONOUNS] and the MCP tool surface of [POLICYPROV].
- **draft-reilly-webproof-01** (new-draft, score 7, trust_infrastructure) [none]: [WebProof: A Dual-Layer Web Provenance Protocol for Verifiable Digital Truth on the Internet](https://datatracker.ietf.org/doc/draft-reilly-webproof/) — This document defines WebProof, a new protocol layer for the World
   Wide Web that enables any web resource, document, dataset, media
   artifact, or AI-generated output to be cryptographically proven to
   exist in a specific form, at a specific time, under a specific
   author's custody.

   The web currently provides transport security (TLS), naming (DNS),
   and resource identification (URI/URL), but no native mechanism for
   verifiable provenance.  Any web resource can be silently modified,
   backdated, or repudiated.  WebProof fills this gap by defining a
   dual-anchored provenance layer that combines DOI-based archival
   permanence with blockchain timestamping to produce a WebProof Record
   (WPR): a machine-readable, independently verifiable proof of a
   resource's existence, integrity, authorship, and timestamp.

   WebProof introduces a well-known URI (/.well-known/webproof) for
   resource-level proof publication, HTTP response header extensions
   for inline provenance signaling, a canonical WebProof Record schema,
   a generation and verification procedure, and a DNS TXT record
   profile for domain-level WebProof registration.

   WebProof is designed to compose with existing web infrastructure and
   is intentionally non-disruptive: it does not require modifications
   to HTTP, TLS, or DNS to function, operating as an opt-in provenance
   layer that any web publisher can adopt independently.  The protocol
   builds on the Dual-Layer Digital Permanence methodology introduced
   by Lawrence John Reilly Jr. in the Reilly EternaMark (REM) Protocol
   [I-D.draft-reilly-rem-protocol].

   The term "WebProof" is coined by Lawrence John Reilly Jr. and first
   formally defined in this document.

   This revision adds material to draft-reilly-webproof-00 without
   removing or altering any text carried forward from it.  The
   additions are summarized in Section 18.
- **draft-singh-psi-01** (new-draft, score 7, adjacent_watchlist) [none]: [Proof of Sovereign Integrity (PSI): A Cryptographic Protocol for Verifiable AI Regulatory Compliance](https://datatracker.ietf.org/doc/draft-singh-psi/) — This document specifies the Proof of Sovereign Integrity (PSI)
   Protocol, version 1.2, a cryptographic framework enabling
   organizations to prove compliance with AI regulations (including the
   EU AI Act 2024/1689, NIST AI RMF, UK AI Safety Institute guidelines,
   and equivalent frameworks) without disclosing proprietary model
   architectures, training data, or inference logic.

   PSI achieves this through a combination of SHA-256 hash-chained audit
   trails, Ed25519 digital signatures, Merkle inclusion proofs,
   Groth16-compatible zero-knowledge commitments over BN128 fields, and
   a 3-node Multi-Party Computation (MPC) consensus mechanism with 2/3
   threshold verification.

   This revision documents a deployed public reference implementation
   and adds optional post-quantum signature profiles and Bitcoin
   timestamp anchoring.
- **draft-stone-vcap-02** (new-draft, score 7, agent_identity) [none]: [VCAP: Verified Commerce for Agent Protocols](https://datatracker.ietf.org/doc/draft-stone-vcap/) — This document specifies the *Verified Commerce for Agent Protocols
   (VCAP)*, an open standard for settling financial transactions between
   autonomous AI agents using cryptographically verifiable proof of work
   delivery.  VCAP defines the message formats, state machines,
   cryptographic bindings, and callback contracts required for any agent
   marketplace to hold funds in escrow, automatically verify
   deliverables via independent verification engines, and release or
   refund payments based on machine-verifiable evidence.

   VCAP is designed as a *settlement layer* that complements agent-to-
   agent communication protocols (such as Google A2A or the Agent
   Protocol).  Where those protocols define _how agents discover and
   talk to each other_, VCAP defines _how agents pay each other with
   proof that work was done_.

## Monitor

- **draft-alhemeiri-wathiqa-pqc-ers-00** (new-draft, score 6, trust_infrastructure) [none]: [Post-Quantum Evidence Records with Algorithm Agility (Wathiqa Profile)](https://datatracker.ietf.org/doc/draft-alhemeiri-wathiqa-pqc-ers/) — This document describes an evidence-record format for the long-term,
   verifiable preservation of digitally-signed data across the migration
   to post-quantum cryptography.  It builds on the Evidence Record
   Syntax (ERS) of RFC 4998 and adds an explicit *algorithm-agility*
   extension: a record is a chain of signed attestations in which each
   link re-witnesses the data under a fresh signature primitive and
   commits to the prior link, so that the authenticity of the data
   survives the cryptographic break of any single primitive.  It
   specifies the canonical hashing that makes a record reproducibly
   verifiable across independent implementations, the authenticated
   temporal binding that places each link in time (an append-only
   transparency log à la RFC 6962, whose signed inclusion receipt is
   _not-after_ evidence), and the verification procedure.  A per-link
   beacon anchor records _not-before_ metadata but is, in this profile,
   carried unauthenticated — see Section 8.
- **draft-cel-nfsv4-rpc-tls-dane-00** (new-draft, score 6, core_identity) [none]: [Using RPC-with-TLS with DNS-Based Authentication of Named Entities](https://datatracker.ietf.org/doc/draft-cel-nfsv4-rpc-tls-dane/) — RPC-with-TLS assumes that DNS-Based Authentication of Named Entities
   (DANE) is available on platforms where it is deployed, and recommends
   that a client operating under an opportunistic security policy check
   for a TLSA record before initiating an association, but does not say
   how.  This document specifies the missing details, so that a TLSA
   record authenticates an RPC server with no certification authority
   trust anchor provisioned on the client.  It updates RFC 9289.
- **draft-elmasri-qr-trust-residuals-00** (new-draft, score 6, adjacent_watchlist) [none]: [Trust Residuals for Navigation QR Codes](https://datatracker.ietf.org/doc/draft-elmasri-qr-trust-residuals/) — Navigation QR codes carrying absolute HTTP or HTTPS URIs initiate web
   interactions, including payment, ordering, and institutional
   workflows.  Selected deployed scanners decode and hand off those URIs
   without an interoperable account of whether the navigation is
   authorized.  This document defines an Informational architecture and
   candidate decision- semantics surface based on trust residuals:
   typed, evidence-bearing deviations between a scanned artifact and
   issuer-chain, destination- policy, redirect-flow, runtime-safety,
   freshness, and artifact-integrity constraints.  Given a residual
   vector and a declared verification profile, explicit precedence rules
   map the result to a bounded set of scanner decision states.  Security
   invariants prevent reputation, HTTPS transport, or runtime-safety
   signals from upgrading an otherwise untrusted issuer path.  This
   document does not define a payload carrier or a final wire format for
   signed governance objects; those belong in a future binding
   specification.
- **draft-ietf-lamps-rfc6211-update-00** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects an error in definition
   of the id-aa-CMSAlgorithmProtection ASN.1 object identifier.  The
   IANA registry entry has alway been correct.
- **draft-morrison-org-alter-policy-provision-03** (new-draft, score 6, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
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
- **draft-mott-cose-sqisign-08** (new-draft, score 6, verifiable_claims) [none]: [CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for SQIsign](https://datatracker.ietf.org/doc/draft-mott-cose-sqisign/) — *NOTE: This document describes a signature scheme based on the
   SQIsign algorithm currently under evaluation in the 3rd round NIST
   Post-Quantum Cryptography standardization process.  Be aware that the
   underlying primitive may change as a result of that process.*

   This document specifies the algorithm encodings and representations
   for the SQIsign digital signature scheme within the CBOR Object
   Signing and Encryption (COSE) and JSON Object Signing and Encryption
   (JOSE) frameworks.

   SQIsign is an isogeny-based post-quantum signature scheme that
   provides an unusually compact signature and public key size among
   candidates of the NIST Post-Quantum Cryptography (PQC)
   standardization and on-ramp-to-standardization processes.

   The standardization of SQIsign will be helpful to address current
   infrastructure bottlenecks, specifically the FIDO2 CTAP2
   specification used by many in-service devices.

   This document clarifies that SQIsign does not expose the auxiliary
   torsion-point information exploited in the SIDH/SIKE attacks.
   Consequently, the specific attack techniques of Castryck–Decru do not
   directly apply.  However, the scheme remains subject to ongoing
   cryptanalysis of isogeny-based constructions.  By establishing stable
   COSE and JOSE identifiers, this document ensures the interoperability
   required for the seamless integration of post-quantum security into
   high-density, bandwidth-constrained, and legacy-compatible hardware
   environments.
- **draft-rajappa-httpbis-connection-contamination-06** (new-draft, score 6, core_identity) [none]: [Mitigating HTTP/3 Connection Contamination in Multi-Tenant and CDN-Fronted Deployments](https://datatracker.ietf.org/doc/draft-rajappa-httpbis-connection-contamination/) — HTTP/3 [RFC9114] clients commonly reuse ("coalesce") an existing QUIC
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
- **draft-templeman-scitt-framing-space-00** (new-draft, score 6, core_identity) [none]: [Measuring the CBOR Framing Space of COSE_Sign1 Data-Hash Pre-images](https://datatracker.ietf.org/doc/draft-templeman-scitt-framing-space/) — A signed statement conveyed as a COSE_Sign1 object may be serialized
   into many distinct byte sequences that all decode to the same data
   item.  Where a protocol identifies such a statement by a digest
   computed over its wire octets (referred to here as a data-hash), the
   identifier is sensitive to that framing while the signature over the
   statement is not.

   This document reports a measurement of the size of that class.
   Taking one 165-octet COSE_Sign1 object and re-emitting it under every
   combination of six CBOR encoding freedoms yields 64 distinct octet
   sequences.  All 64 carry an identical Sig_structure and therefore an
   identical, valid signature.  All 64 produce distinct data-hash
   values, with no collisions.  A stock CBOR decoder rejected none of
   them, and 31 were silently repaired into the canonical form by the
   act of being read.

   This document specifies nothing and proposes no wording.  It reports
   a measurement, publishes the reproduction recipe, and identifies the
   prior work that already addresses the problem it measures.
- **draft-tiloca-ace-bidi-access-control-03** (new-draft, score 6, core_identity) [none]: [Bidirectional Access Control in the Authentication and Authorization for Constrained Environments (ACE) Framework](https://datatracker.ietf.org/doc/draft-tiloca-ace-bidi-access-control/) — This document updates the Authentication and Authorization for
   Constrained Environments (ACE) framework, for which it defines a
   method to enforce bidirectional access control by means of a single
   access token.  Therefore, this document updates RFC 9200.
- **draft-tiloca-core-oscore-discovery-20** (new-draft, score 6, core_identity) [none]: [Discovery of OSCORE Groups with the CoRE Resource Directory](https://datatracker.ietf.org/doc/draft-tiloca-core-oscore-discovery/) — Group communication over the Constrained Application Protocol (CoAP)
   can be secured by means of Group Object Security for Constrained
   RESTful Environments (Group OSCORE).  At deployment time, devices
   might not know the exact security groups to join, the respective
   Group Managers responsible for those groups, or other information
   required to perform the joining process.  This document defines how a
   CoAP endpoint can use descriptions and links of resources registered
   at the CoRE Resource Directory to discover security groups and to
   acquire information for joining them through the respective Group
   Managers.  A given security group can be used to protect
   communications in multiple application groups, which are separately
   announced in the Resource Directory as sets of endpoints sharing a
   pool of resources.  This approach is consistent with, but not limited
   to, the joining of security groups based on the Authentication and
   Authorization for Constrained Environments (ACE) framework.
- **draft-zhang-dawn-agent-discovery-framework-00** (new-draft, score 6, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — The IETF DAWN (Discovery of Agents, Workloads, and Named Entities)
   working group is developing a suite of documents addressing agent
   discovery across organizational boundaries.  Existing DAWN
   contributions include terminology, requirements, use cases, gap
   analysis, a discovery mechanism survey, and an information model for
   Minimum Discoverable Information (MDI).

   This document describes a two-layer federated reference architecture
   framework that operates within the DAWN.  The first layer, the Local
   Discovery Plane, performs zero-configuration agent advertisement and
   collection inside each local site, without mandating a specific link-
   local protocol.  The second layer, the Federation Plane, builds a
   federation among site gateways to exchange lightweight Federation
   Metadata Records (FMRs) — a concrete binding of DAWN MDI — across
   independent administrative domains, while full Capability Cards are
   retrieved on demand via authenticated unicast.

   The architecture emphasizes data sovereignty through an Export Policy
   Engine, separates lightweight metadata indexes from full capability
   documents, and supports multiple federation synchronization
   strategies.  This document is informational.  It does not define
   normative protocol formats, nor does it compete with existing DAWN
   proposals such as ACAP, Agent Directory, or ARDP; rather, it provides
   a deployment framework showing how these mechanisms may be composed
   at administrative boundaries.
- **draft-ietf-webbotauth-httpsig-protocol-00** (new-draft, score 5, core_identity) [webbotauth]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-kavian-offering-discovery-protocol-01** (new-draft, score 5, adjacent_watchlist) [none]: [The Offering Discovery Protocol](https://datatracker.ietf.org/doc/draft-kavian-offering-discovery-protocol/) — The Offering Discovery Protocol (ODP) enables an automated Agent to
   inspect a Service, discover its Collections and Offerings, interpret
   Service-defined structured attributes, and identify links to
   subsequent operations.  ODP supports catalogs ranging from a few
   Offerings to large marketplaces without imposing a universal product
   taxonomy.  This document defines the protocol's scope, terminology,
   roles, discovery architecture, extensibility model, composition
   boundaries, and conformance model.
- **draft-li-cats-aisemantic-contract-01** (new-draft, score 5, adjacent_watchlist) [none]: [Semantic-Driven Traffic Shaping Contract for AI Networks](https://datatracker.ietf.org/doc/draft-li-cats-aisemantic-contract/) — This document defines a "Semantic-Driven Shaping Contract".
   Traditional network protocols treat AI training and inference traffic
   as opaque byte streams, leading to highly inefficient scheduling.
   This contract allows applications or distributed training frameworks
   to explicitly pass "minimum necessary semantics" to the underlying
   network.  In exchange, the network commits to executing fine-grained,
   differentiated forwarding and resource allocation actions for tensor
   flows with diverse semantics, based on predefined rules and global
   real-time states.  This model significantly improves overall resource
   utilization and task completion times in heterogeneous computing
   networks, cross-domain intelligent computing centers, and integrated
   training-inference scenarios.
- **draft-sato-soos-peer-01** (new-draft, score 5, agent_identity) [none]: [Cross-Principal Agent Communication -- PEER Transaction Record](https://datatracker.ietf.org/doc/draft-sato-soos-peer/) — When two independently-principaled AI agents transact with each
   other, each operates under its own mandate root, its own Governed
   Execution Context (GEC), and its own audit chain.  No shared kernel
   exists to mediate the exchange.  Existing SOOS orchestration
   primitives (MAD, SACR) govern sub-agent relationships within one
   mandate tree; they do not address the peer case.

   This document defines the PEER protocol: a problem statement and
   architecture for cross-principal agent communication.  PEER
   introduces the PEER Transaction Record (PTR) as a new first-class
   SOOS primitive providing a jointly-derived correlation artifact
   (ptxn_id) that links the two independent audit chains produced by a
   cross-principal transaction -- without requiring a neutral third
   party, shared kernel state, or cross-principal constitutional layer.

   This document is a problem statement and architecture draft.  The PTR
   field schema, the ptxn_id derivation, and the responding-GEC-
   countersignature requirement are normative as of this revision.  Full
   normative ALE-PEER event schemas, IANA registration templates, and a
   dispute resolution procedure for conflicting GAR chains remain open
   and are carried to a future revision.
- **draft-stone-aref-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Referral and Escrow Framework (AREF)](https://datatracker.ietf.org/doc/draft-stone-aref/) — This document specifies the Agent Referral and Escrow Framework
   (AREF), a protocol for cryptographically attributed agent-to-agent
   referrals, escrow-bound commission commitments, and dual-rail
   financial settlement in multi-agent computing environments.

   As autonomous software agents increasingly transact with one another
   to acquire capabilities and coordinate work, no standardized
   mechanism exists for recording how one agent introduced another to a
   platform or service, binding that introduction to a financial
   commitment, or settling the resulting commission across heterogeneous
   payment infrastructure.  AREF addresses this gap by defining: a
   portable Ed25519-signed attribution proof for referral chains of
   arbitrary depth; the semantics and payload schema of the SwarmSync-
   Referrer HTTP header used to bind a referrer to an escrow at hold-
   time; a commission vesting model tied to escrow finality rather than
   enrollment; a unified settlement finality signal operable over both
   traditional financial infrastructure (Stripe Connect) and
   cryptographic payment channels (X402); and the swarm_meta JSON
   embedding mechanism through which referral codes propagate across
   agent ecosystems without human involvement.

   This document is intended for implementers of agent orchestration
   platforms, payment service operators, and designers of multi-agent
   economic systems.
- **draft-watts-scientific-admissibility-evidence-00** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Admissibility Evidence Records for Verifiable Research Provenance](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility-evidence/) — This document describes a portable JSON evidence-record format for
   representing bounded scientific claims, preregistered procedures,
   admissibility evaluations, provenance artifacts, lifecycle events,
   and cryptographic integrity metadata.  The format is intended to make
   research evidence exchangeable and mechanically checkable without
   treating cryptographic integrity, schema conformance, scientific
   admissibility, valuation, governance, or truth as equivalent
   concepts.

   This document is an individual informational proposal.  It does not
   define a network transport protocol, does not establish scientific
   truth, and does not assign decision authority to automated systems.
- **draft-zhu-anima-service-intent-01** (new-draft, score 5, adjacent_watchlist) [none]: [Definition of Service Intent in Autonomic Networks](https://datatracker.ietf.org/doc/draft-zhu-anima-service-intent/) — While ANIMA Intent enables goal-oriented control within an Autonomic
   Domain, emerging services (e.g., AI inference) require a common,
   interoperable representation for expressing service-level objectives
   and constraints that span network, compute, and storage resources,
   rather than connection-centric descriptions.  This document defines
   Service Intent for Autonomic Networks by specifying a structured
   semantic model and a concise format with identification, scope,
   versioning, and lifecycle semantics.

## Adjacent / watchlist

- **draft-behring-cvd-policy-00** (new-draft, score 3, authorization) [none]: [Machine-Readable Coordinated Vulnerability Disclosure Policies](https://datatracker.ietf.org/doc/draft-behring-cvd-policy/) — This document defines a JSON format for machine-readable Coordinated
   Vulnerability Disclosure (CVD) policies.  It also defines the
   proposed CVD-Policy field for discovery through security.txt and
   requests registration of the application/cvd-policy+json media type.
   The format complements security.txt and human-readable policy
   documents.  A policy does not prove ownership and does not establish
   legal authorization to test, legal safe harbor, or the safety of an
   activity.
- **draft-bormann-cbor-cddl-csv-09** (new-draft, score 3, adjacent_watchlist) [none]: [Using CDDL for CSVs](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-csv/) — The Concise Data Definition Language (CDDL), standardized in RFC
   8610, is defined to provide data models for data shaped like JSON or
   CBOR.

   Another representation format that is quote popular is the CSV
   (Comma-Separated Values) file as defined by RFC 4180.

   The present document shows a way how to use CDDL to provide a data
   model for CSV files.
- **draft-bormann-cbor-edn-mapkey-02** (new-draft, score 3, adjacent_watchlist) [none]: [CBOR: Generating Numeric Map Labels from Textual EDN](https://datatracker.ietf.org/doc/draft-bormann-cbor-edn-mapkey/) — The Concise Binary Object Representation (CBOR, STD 94 == RFC 8949)
   is a data format whose design goals include the possibility of
   extremely small code size, fairly small message size, and
   extensibility without the need for version negotiation.

   CBOR diagnostic notation (EDN) is widely used to represent CBOR data
   items in a way that is accessible to humans, for instance for
   examples in a specification.  Complex examples often use nested maps,
   the map keys (labels) for each of which are often sourced from
   different specifications.  While the e'' application extension
   provides a way to import data items, particularly constant values,
   from a CDDL model, it does not help with automatically selecting the
   right kind of map depending on its position in the nested maps.


   // The present document is intended to capture ideas initially
   // discussed at the CBOR WG interim 2025-06-25 and demonstrate some
   // design alternatives.  It is not ready for adoption yet in any way.
- **draft-carpenter-anima-otp-casa-01** (new-draft, score 3, core_identity) [none]: [One-time Pad for Authorizing Device Identity](https://datatracker.ietf.org/doc/draft-carpenter-anima-otp-casa/) — This document describes how devices joining an autonomic control
   plane as defined in RFC 8994 may use the BRSKI onboarding mechanism
   defined in RFC 8995, even if they cannot provide a manufacturer-
   installed X.509 IDevID certificate.  Instead, such devices may
   generate a self-signed certificate embedding a unique token selected
   from a one-time pad.
- **draft-cel-nfsv4-rpc-tls-othername-04** (new-draft, score 3, core_identity) [none]: [Remote Procedure Call Identity Squashing via x.509 Certificate Fields](https://datatracker.ietf.org/doc/draft-cel-nfsv4-rpc-tls-othername/) — This document extends RPC-with-TLS so that a client's x.509
   certificate may carry instructions to the RPC server to execute all
   RPC transactions from that client as a single user identity.
- **draft-gondwana-dkim2-authres-00** (new-draft, score 3, core_identity) [none]: [Reporting DKIM2 Verification Results in Authentication-Results](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-authres/) — DomainKeys Identified Mail Signatures v2 (DKIM2) produces a
   verification result for an email message.  This document defines how
   that result is reported in the Authentication-Results header field,
   registering the "dkim2" authentication method, the result values it
   can take, and two properties which identify the signing domain and
   the point in the chain at which verification failed.  Diagnostic
   detail about each hop is carried in a human-readable comment.
- **draft-ietf-6man-ipv6-neighbor-discovery-yang-08** (new-draft, score 3, adjacent_watchlist) [6man]: [YANG Data Model for IPv6 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/) — This document defines a YANG data model to configure and manage IPv6
   Neighbor Discovery (ND) and related functions, including IPv6 address
   resolution, redirect function, proxy Neighbor Advertisement, Neighbor
   Unreachability Detection (NUD), Duplicate Address Detection (DAD),
   and Enhanced Duplicate Address Detection.
- **draft-ietf-calext-jscalendarbis-19** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-ccamp-optical-path-computation-yang-09** (new-draft, score 3, adjacent_watchlist) [ccamp]: [YANG Data Models for requesting Path Computation in WDM Optical Networks](https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-path-computation-yang/) — This document provides a mechanism to request path computation in
   Wavelength-Division Multiplexing (WDM) optical networks composed of
   Wavelength Switched Optical Networks (WSON) and Flexi-Grid Dense
   Wavelength Division Multiplexing (DWDM) switched technologies.  This
   model augments the Remote Procedure Calls (RPCs) defined in RFC YYYY.

   [RFC EDITOR NOTE: Please replace RFC YYYY with the RFC number of
   draft-ietf-teas-yang-path-computation once it has been published.
- **draft-ietf-ccamp-yang-otn-slicing-12** (new-draft, score 3, adjacent_watchlist) [ccamp]: [Framework and Data Model for OTN Network Slicing](https://datatracker.ietf.org/doc/draft-ietf-ccamp-yang-otn-slicing/) — The requirement of slicing network resources with desired quality of
   service is emerging at every network technology, including the
   Optical Transport Networks (OTN).  As a part of the transport
   network, OTN can provide hard pipes with guaranteed data isolation
   and deterministic low latency, which are highly demanded in the
   Service Level Agreement (SLA).

   This document describes a framework for OTN network slicing and
   defines YANG data models with OTN technology-specific augments
   deployed at both the north and south bound of the OTN network slice
   controller.  Additional YANG data model augmentations will be defined
   in a future version of this draft.
- **draft-ietf-idr-sdwan-edge-discovery-30** (new-draft, score 3, core_identity) [idr]: [SD-WAN Edge and Underlay Tunnel Discovery Using BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-sdwan-edge-discovery/) — This document specifies BGP mechanisms for SD-WAN (Software-Defined
   Wide Area Network) edge node attribute discovery.  These mechanisms
   comprise a new tunnel type and associated Sub-TLVs for the BGP Tunnel
   Encapsulation Attribute, and a new Subsequent Address Family
   Identifier (SAFI) carrying a typed NLRI for advertising SD-WAN
   underlay tunnel information.
- **draft-ietf-lamps-pq-composite-kem-21** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/) — This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.
- **draft-ietf-lisp-yang-25** (new-draft, score 3, adjacent_watchlist) [lisp]: [LISP YANG Model](https://datatracker.ietf.org/doc/draft-ietf-lisp-yang/) — This document describes a YANG data model to use with the Locator/ID
   Separation Protocol (LISP).  This model can be used to configure and
   monitor the different control plane and data plane elements that
   enable a LISP network.

   The YANG modules in this document conform to the Network Management
   Datastore Architecture (NMDA) defined in [RFC8342].
- **draft-ietf-lsr-isis-srv6-yang-10** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Data Model for IS-IS SRv6](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-srv6-yang/) — This document defines a YANG data model that can be used to configure
   and manage IS-IS Segment Routing over the IPv6 Data Plane.
- **draft-ietf-lsr-ospf-srv6-yang-10** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Data Model for OSPF SRv6](https://datatracker.ietf.org/doc/draft-ietf-lsr-ospf-srv6-yang/) — This document defines a YANG data model that can be used to configure
   and manage OSPFv3 Segment Routing over the IPv6 Data Plane.
- **draft-ietf-mpls-stamp-pw-18** (new-draft, score 3, core_identity) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document specifies encapsulations for the Simple Two-Way Active
   Measurement Protocol (STAMP), defined in RFC 8762, and its optional
   extensions, defined in RFC 8972, in MPLS networks.  It specifies the
   encapsulation of STAMP test packets for point-to-point Label Switched
   Paths (LSPs) and point-to-point single-segment Pseudowires (PWs),
   with or without an IP/UDP header, so that the test packets experience
   the same forwarding and Equal-Cost Multi-Path (ECMP) behavior as the
   data traffic being measured.  In addition, two new MPLS Generic
   Associated Channel (G-ACh) types are defined.

   This document updates RFC 8762 and RFC 8972 to allow STAMP to operate
   without an IP/UDP header when STAMP test packets are carried over
   MPLS LSPs and PWs, and specifies the resulting changes to the
   processing of the STAMP session identifier, the TTL and IPv6 Hop
   Limit, and the STAMP TLV extensions.

   This document specifies the requirements for IPv6 STAMP in
   unauthenticated mode using UDP zero-checksum, which deviates from the
   integrity requirement in RFC 6936.
- **draft-ietf-opsawg-ipfix-path-segment-06** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 paths identification.
- **draft-ietf-sidrops-rtr-yang-08** (new-draft, score 3, adjacent_watchlist) [sidrops]: [YANG Data Model for RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rtr-yang/) — This document defines YANG data models for managing Resource Public
   Key Infrastructure (RPKI) to Router Protocol (RFC6810 and RFC8210).
- **draft-ietf-spring-sr-for-enhanced-vpn-11** (new-draft, score 3, core_identity) [spring]: [Segment Routing based Network Resource Partition (NRP) for Enhanced VPN](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-for-enhanced-vpn/) — Enhanced VPNs aim to deliver VPN services with enhanced
   characteristics, such as guaranteed resources, latency, jitter, etc.,
   so as to support customers requirements on connectivity services with
   these enhanced characteristics.  Enhanced VPN requires integration
   between the overlay VPN connectivity and the characteristics provided
   by the underlay network.  A Network Resource Partition (NRP) is a
   subset of the network resources and associated policies on each of a
   connected set of links in the underlay network.  An NRP could be used
   as the underlay to support one or a group of enhanced VPN services.

   Segment Routing (SR) leverages the source routing paradigm.  A node
   steers a packet through an ordered list of instructions, called
   "segments".  A segment is referred to by its Segment Identifier
   (SID).  SIDs can represent topological or service based instructions.
   SIDs can further be associated with a set of network resources used
   for executing the instruction.  Such SIDs are called resource-aware
   SIDs.  A group of resource-aware SIDs may be used to build SR based
   NRPs, which provide customized network topology and resource
   attributes required by one or a group of enhanced VPN services.

   This document describes an approach to build SR based NRPs using
   resource-aware SIDs.  The SR based NRP can be used to deliver
   enhanced VPN services in SR networks.
- **draft-ietf-teas-yang-te-mpls-topology-05** (new-draft, score 3, adjacent_watchlist) [teas]: [A YANG Data Model for MPLS-TE Topology](https://datatracker.ietf.org/doc/draft-ietf-teas-yang-te-mpls-topology/) — This document defines a YANG data model for representing, retrieving,
   and manipulating MPLS-TE network topologies.  It is based on and
   augments existing YANG models that describe network and traffic
   engineering packet network topologies.

   This document also defines a collection of common YANG data types and
   groupings specific to MPLS-TE.  These common types and groupings are
   intended to be imported by modules that model MPLS-TE technology-
   specific configuration and state capabilities.

   The YANG models defined in this document can also be used for MPLS
   Transport Profile (MPLS-TP) network topologies.
- **draft-ietf-tls-mlkem-10** (new-draft, score 3, adjacent_watchlist) [tls]: [ML-KEM Post-Quantum Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) — This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as
   NamedGroups and registers IANA values in the TLS Supported Groups
   registry for use in TLS 1.3 to achieve post-quantum (PQ) key
   establishment.
- **draft-ietf-uta-tls13-iot-profile-25** (new-draft, score 3, adjacent_watchlist) [uta]: [TLS/DTLS 1.3 Profiles for the Internet of Things](https://datatracker.ietf.org/doc/draft-ietf-uta-tls13-iot-profile/) — RFC 7925 offers guidance to developers on using TLS/DTLS 1.2 for
   Internet of Things (IoT) devices with resource constraints.  This
   document is a companion to RFC 7925, defining TLS/DTLS 1.3 profiles
   for IoT devices.  Additionally, it updates RFC 7925 with respect to
   the X.509 certificate profile and ciphersuite requirements.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/thomas-fossati/draft-tls13-iot.
- **draft-intra-handshake-fail-21** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake (aka Early) Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
   (https://www.cve.org/CVERecord?id=CVE-2026-33697), EUVD-2026-16488
   (https://euvd.enisa.europa.eu/enisa/EUVD-2026-16488), and several
   GitHub Security Advisories (GHSAs) which provide substantial
   technical evidence of how *intra*-handshake (aka early) attestation
   fails in practice, even _without physical access_. Moreover, since
   continuous attestation is generally required, *intra*-handshake
   attestation adds *unnecessary complexity*. The results are backed by
   the research [Intra-handshake.fail] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility, and have been
   acknowledged by the relevant stakeholders.  Currently, there are two
   CVEs of CVSS 7.5, two GHSAs of CVSS 9.1, one GHSA of CVSS 7.8, and
   six GHSAs of CVSS 7.4 published against *intra*-handshake (aka early)
   attestation.
- **draft-irtf-cfrg-aead-limits-13** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Usage Limits on AEAD Algorithms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-aead-limits/) — An Authenticated Encryption with Associated Data (AEAD) algorithm
   provides confidentiality and integrity.  Excessive use of the same
   key can give an attacker advantages in breaking these properties.
   This document provides simple guidance for users of common AEAD
   functions about how to limit the use of keys in order to bound the
   advantage given to an attacker.  It considers limits in both single-
   and multi-key settings.  This document is a product of the Crypto
   Forum Research Group (CFRG) in the IRTF.
- **draft-kolomytsev-pshmp-core-overview-00** (new-draft, score 3, adjacent_watchlist) [none]: [PSHMP Core: A Hybrid L4 Overlay for Proactive Self-Healing and Resilient Multi-Hop Delivery](https://datatracker.ietf.org/doc/draft-kolomytsev-pshmp-core-overview/) — PSHMP Core is a hybrid L4-oriented overlay designed to keep multi-hop
   data delivery working when individual nodes, links, or network
   segments become unstable.  It runs above ordinary IP infrastructure
   and does not require changes to Layer 3 routing.

   Under stable conditions the system builds linear relay chains.  When
   several nodes on a path show degradation, it can switch locally into
   a mesh-style recovery mode: collect alternative candidates, apply
   progressive fallback rules, enforce a quality gate, and replace the
   affected path.  Continuous node assessment (K-Factor), diversity-
   aware selection, failure tracking, gossip and DHT discovery, and
   batch acknowledgements with gap recovery form the supporting
   mechanisms.

   This document describes the architecture (including component
   layers), operating principles, key evaluation and delivery formulas,
   and the relationship to an experimental implementation (PSHMP Core
   v3.1).  Implementation-specific scoring weights, exact thresholds,
   and proprietary optimisations may be refined by integrators; the
   formulas given here represent the reference model used in the current
   experimental codebase.
- **draft-li-individual-inip-01** (new-draft, score 3, adjacent_watchlist) [none]: [In-Network Inference Protocol](https://datatracker.ietf.org/doc/draft-li-individual-inip/) — This document specifies the In-Network Inference Protocol (INIP), a
   lightweight protocol designed specifically for implementing high-
   speed in-network inference in data center internal networks.  INIP
   utilizes data plane devices (such as switches, DPUs, and SmartNICs)
   to perform lightweight inference tasks while ensuring that core
   network forwarding functions are not affected.  The protocol operates
   based on the IPv4 protocol and adopts a fixed, lightweight packet
   format.

   INIP adopts a two-tier architecture of "centralized control plane
   adaptation and scheduling, and minimal data plane execution".  The
   control plane stores all inference models, deploys model rules to
   data plane devices using a CDN-like scheduling method, and assumes
   the responsibility of degraded fallback inference; the data plane
   performs packet parsing and match action table-based inference.  This
   document details INIP's core logic, packet format, data plane device
   constraints, model expression specifications, control plane
   responsibilities, CDN-like scheduling mechanism, dynamic model
   popularity replacement, and overall execution process.
- **draft-lin-opsawg-ipfix-rocev2-01** (new-draft, score 3, ai_infrastructure) [none]: [Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/) — This document defines a new set of IP Flow Information Export (IPFIX)
   Information Elements (IEs) for exporting Base Transport Header (BTH)
   information for RDMA over Converged Ethernet version 2 (RoCEv2)
   traffic.  These extensions enable network monitoring systems to
   collect and analyze the characteristics of RDMA traffic widely used
   in high-performance computing, storage, and artificial intelligence
   applications.
- **draft-lnehru-lisp-silenthost-detection-00** (new-draft, score 3, adjacent_watchlist) [none]: [LISP Silent Host Discovery using the Mapping System](https://datatracker.ietf.org/doc/draft-lnehru-lisp-silenthost-detection/) — The on-demand discovery model of the Locator/ID Separation Protocol
   (LISP) is ineffective for "silent hosts", endpoints that do not
   initiate traffic.  This is a common challenge in environments like
   manufacturing and IoT environments, where low-power devices
   frequently go silent to conserve energy.  This document proposes a
   mechanism to discover these hosts by using the LISP mapping system
   itself. xTRs that are able to probe a given EID prefix register that
   capability with the Map-Server.  When a Map-Request for an unknown
   destination arrives at the Map-Server, it is forwarded and replicated
   to all xTRs that have registered the covering EID prefix, initiating
   a controlled, on-demand discovery process for that specific host.
   This approach provides a scalable alternative to network flooding for
   locating silent endpoints.
- **draft-mitchell-botcentral-card-00** (new-draft, score 3, adjacent_watchlist) [none]: [The BotCentral Card: An Owner-Proven Consent Record for Automated Web Clients](https://datatracker.ietf.org/doc/draft-mitchell-botcentral-card/) — The Robots Exclusion Protocol (RFC 9309) lets a site say which
   automated clients may fetch its content.  It cannot express purpose:
   fetching a page to answer a person is not the same act as copying it
   into a model training set or taking an action on the site.  It also
   cannot prove who published the policy.

   This document defines the BotCentral Card, a JSON record, one per
   domain, that states which purposes the domain owner consents to
   ("retrieve", "train", and "act" as separate answers), backed by a
   proof of domain control placed either in a DNS TXT record or at the
   well-known URI "/.well-known/botcentral.txt".  Cards are written to a
   registry by authenticated publishers and read by any client over HTTP
   or the Model Context Protocol.  Clients never write cards.  A card is
   permission to be found; it is not a ranking and not a training grant.

   This document also registers the "botcentral.txt" well-known URI.
- **draft-morrison-alter-uri-scheme-03** (new-draft, score 3, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
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
- **draft-nordin-ocm-integration-protocol-01** (new-draft, score 3, adjacent_watchlist) [ocm]: [Open Cloud Mesh Integration Protocol](https://datatracker.ietf.org/doc/draft-nordin-ocm-integration-protocol/) — The Open Cloud Mesh Integration Protocol (OCM-IP) defines how an Open
   Cloud Mesh (OCM) Server can integrate supporting servers, such as
   SSH/SFTP servers, web application platforms, or stand-alone WebDAV
   servers, to perform protocol-specific work on its behalf.

   OCM-IP makes it possible for existing OCM Servers to offload protocol
   specific interactions to stand-alone servers, or even implement OCM
   as a lightweight server that handles only the OCM parts of a
   deployment: discovery, share creation, token issuance and signing.
   Anything protocol-specific, such as serving files over WebDAV,
   providing SSH access, or running an interactive web application, can
   be handed off to one or more Protocol Servers running elsewhere,
   possibly operated with different software and on different
   infrastructure.

   OCM-IP defines three integration modes: a provisioned mode, in which
   the OCM Server pushes Share information to the Protocol Server over a
   signed back channel; a self-contained mode, in which the Share
   information is embedded in the signed access token itself, so that
   the Protocol Server needs no per-share state and no inbound API at
   all; and an introspected mode, in which the Protocol Server validates
   presented credentials through a token introspection endpoint,
   restoring compatibility with Receiving Servers that do not support
   token exchange.

   OCM-IP is a protocol between the Sending OCM Server and its Protocol
   Servers only.  The Receiving Server is not involved in, and does not
   need to be aware of, this protocol: everything it observes is
   indistinguishable from the Sending Server serving the access
   protocols itself.  For this reason, an OCM Sending Server MAY adopt a
   different strategy to interoperate with Protocol Servers, including
   e.g. establishing trust via shared keys, without compromising
   compliance with the OCM protocol.
- **draft-reddy-tls-composite-mldsa-12** (new-draft, score 3, core_identity) [none]: [Use of Composite ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-reddy-tls-composite-mldsa/) — Compositing the post-quantum ML-DSA signature with traditional
   signature algorithms provides protection against potential breaks or
   critical bugs in ML-DSA or the ML-DSA implementation.  This document
   specifies how such a composite signature can be formed using ML-DSA
   with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide
   authentication in TLS 1.3, including use in certificates.
- **draft-richardson-rats-composite-attesters-05** (new-draft, score 3, trust_infrastructure) [none]: [Taxonomy of Composite Attesters](https://datatracker.ietf.org/doc/draft-richardson-rats-composite-attesters/) — This document was attempting to clarifys and extends the meaning of
   Composite Attester from RFC9334.  It has since been moved into the
   RATS wiki, and this I-D serves as a tombstone.

   A system of annotated diagram components is defined as a small
   language to explain the different ways that components can interact
   to form composites.

   These diagram components are then used to define a few popular
   classes of composites.
- **draft-riedl-moq-ad-creative-signaling-00** (new-draft, score 3, core_identity) [none]: [Ad Creative Signaling over the MSF Event Timeline](https://datatracker.ietf.org/doc/draft-riedl-moq-ad-creative-signaling/) — This document defines the carriage of ad creative signaling --
   creative identity, tracking events, and measurement verification
   metadata as specified by SVTA 2053-1 -- in records on a Media over
   QUIC (MOQT) Streaming Format (MSF) Event Timeline track.  It
   complements the carriage of SCTE-35 splice signaling over the same
   mechanism: splice events describe where placement opportunities occur
   on a media timeline, while the event class defined here describes the
   creatives that fill them and how their playback is to be measured.
   This binding is the MSF counterpart of the DASH and HLS carriage
   bindings defined by SVTA 2053-1, which defines none for MOQT.
- **draft-scalone-cfr-source-privacy-02** (new-draft, score 3, core_identity) [none]: [Customer-Facing Relay (CFR): Enhancing Source Privacy in Encrypted Transport and CDN Scenarios](https://datatracker.ietf.org/doc/draft-scalone-cfr-source-privacy/) — Encrypted ClientHello (ECH) protects sensitive TLS ClientHello
   fields, including the Server Name Indication (SNI), from on-path
   observers.  ECH does not, however, attempt to hide the client's
   network-layer source identity from the ECH client-facing server
   (CFS).  In split-mode deployments, the CFS decrypts the
   ClientHelloInner in order to route the connection to the appropriate
   backend while also receiving the connection from the client's visible
   source address.

   This creates a distinct source-privacy problem.  Where ECH service
   and content front-door infrastructure are concentrated, a relatively
   small number of providers can obtain a privileged vantage point from
   which a stable source address can be correlated with many encrypted
   destinations and with other service telemetry.  Measurements over a
   corpus of approximately one million domains, together with an active-
   ECH validation subset, show substantial front-door concentration and
   motivate treating source privacy as a complement to destination
   privacy.

   This document describes the Customer-Facing Relay (CFR), a network-
   layer, access-side source-aliasing function.  A CFR forwards
   encrypted TCP or UDP traffic without terminating TLS or QUIC and
   replaces the subscriber-visible source address with a shared or
   short-lived source alias.  The document also examines the different
   privacy properties of IPv4 NAT/CGN and IPv6 source addressing and
   identifies requirements for privacy-preserving source mapping.
- **draft-xls-intarea-evn6-06** (new-draft, score 3, core_identity) [none]: [EVN6: Mapping of Ethernet Virtual Network to IPv6 Underlay for Transmission](https://datatracker.ietf.org/doc/draft-xls-intarea-evn6/) — This document describes a mechanism of mapping of Ethernet Virtual
   Network to IPv6 Underlay for transmission.  Unlike the existing
   methods, this approach places the Ethernet frames to be transmitted
   directly in the payload of IPv6 packets, i.e., L2 over IPv6, and uses
   stateless mapping to generate IPv6 source and destination addresses
   from the host's MAC addresses, the Ethernet Virtual Network
   identifier and site prefixes.  The IPv6 packets generated in this way
   carry Ethernet frames and are routed to the destination site across
   the public IPv6 network.
- **draft-xu-ccamp-impairment-info-sharing-problem-01** (new-draft, score 3, adjacent_watchlist) [none]: [Problem Statement: Information Sharing of Optical Impairments in Monitoring of Multi-Domain All-Optical Paths](https://datatracker.ietf.org/doc/draft-xu-ccamp-impairment-info-sharing-problem/) — In multi-domain all-optical Wavelength Switched Optical Networks
   (WSONs), end-to-end services may traverse multiple administrative
   domains operated by different entities.  Monitoring such services
   requires visibility into optical impairments that accumulate across
   domain boundaries.  However, exchanging impairment-related
   information raises operational, scalability, and confidentiality
   concerns.  Detailed metrics such as attenuation, noise, nonlinear
   effects, and filtering penalties may be necessary for accurate
   performance assessment, yet they can expose sensitive topology,
   equipment, or utilization information.

   This document describes the problem space associated with sharing
   optical impairment information across administrative domains for
   monitoring purposes.  It highlights the need to balance operational
   visibility and confidentiality preservation, and outlines
   considerations for abstraction, information granularity, and trust
   relationships among participating operators.
- **draft-ybam-ccamp-rfc8561bis-02** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for Microwave Radio Link](https://datatracker.ietf.org/doc/draft-ybam-ccamp-rfc8561bis/) — This document defines a YANG data model for control and management of
   radio link interfaces and their connectivity to packet (typically
   Ethernet) interfaces in a microwave/millimeter wave node.  The data
   nodes for management of the interface protection functionality is
   broken out into a separate and generic YANG data model in order to
   make it available for other interface types as well.  This document
   obsoletes RFC 8561.
- **draft-zheng-ccamp-client-pm-yang-15** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Client Signal Performance Monitoring](https://datatracker.ietf.org/doc/draft-zheng-ccamp-client-pm-yang/) — A transport network is a server-layer network to provide connectivity
   services to its client.  Given the client signal is configured, the
   followup function for performance monitoring, such as latency and bit
   error rate, would be needed for network operation.

   This document describes the data model to support the performance
   monitoring functionalities.
- **draft-aegisfs-secdispatch-rats-01** (new-draft, score 2, ignored_after_review) [none]: [AegisFS: AI-Driven Programmable Secure File Runtime and Intelligent Workspace Architecture with Octal OpCode Processing and Policy-Driven Language Architecture](https://datatracker.ietf.org/doc/draft-aegisfs-secdispatch-rats/) — This document specifies AegisFS, a programmable secure file and
   folder runtime that transforms ordinary filesystem objects into
   intelligent, policy-driven, state-aware, execution-aware, and
   behavior-aware security objects.

   This draft introduces two novel technical contributions:
- **draft-bormann-cbor-cddl-freezer-18** (new-draft, score 2, ignored_after_review) [none]: [A feature freezer for the Concise Data Definition Language (CDDL)](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-freezer/) — In defining the Concise Data Definition Language (CDDL), some
   features have turned up that would be nice to have.  In the interest
   of completing this specification in a timely manner, the present
   document was started to collect nice-to-have features that did not
   make it into the first RFC for CDDL, RFC 8610, or the specifications
   exercising its extension points, such as RFC 9165.

   Significant parts of this draft have now moved over to the CDDL 2.0
   project, described in draft-bormann-cbor-cddl-2-draft.  The remaining
   items in this draft are not directly related to the CDDL 2.0 effort.
- **draft-clifford-testimony-record-00** (new-draft, score 2, ignored_after_review) [none]: [The Testimony Record: An Interchange Format for What an Automated System Believed and Did](https://datatracker.ietf.org/doc/draft-clifford-testimony-record/) — This document specifies the Testimony Record, an append-only
   interchange format for the account an automated system gives of its
   own operation: what it believed, what evidence each belief rested on,
   which of its beliefs contradicted one another, what actions it
   attempted, and who authorised the consequential ones.

   The format is defined so that a party who was not present, and who
   has no access to the emitting system, can read a record and check
   specific properties of it.  Four conformance levels are defined, each
   stating a property that can be verified mechanically rather than
   asserted.

   This is not a logging format.  Logs record what a program did.  A
   Testimony Record states what a system claimed to know, what disagreed
   with it, and what it was permitted to do about it.
- **draft-dogru-cedulon-decision-profile-02** (new-draft, score 2, ignored_after_review) [none]: [Cedulon Decision Profile: Reconciling an Agent's Decisions Against Its Effects](https://datatracker.ietf.org/doc/draft-dogru-cedulon-decision-profile/) — The Cedulon core document reconciles an issuer's signed Spend
   Receipts against an authenticated extract of a payment rail and
   reports, over a declared population, that no settlement lacks a
   receipt and no settled receipt is absent from the rail.  Money is the
   special case that document implements.  This document defines a
   second population on the same reconciler.  A Decision Record is
   signed by the party that decided whether an agent may act; an Effect
   Extract is an authenticated list of the effects that actually
   occurred on a channel.  An allow must be matched by exactly one
   effect whose content hash the record named; a refusal must be matched
   by none.  The Decision Record claim set, the Effect Extract shape,
   the points at which the reconciliation departs from the spend rules,
   the finding codes, and one media type are defined.  This revision
   states that the binding compares content and reference and not the
   order of two clocks, corrects the boundary to two adjacent documents,
   and records the first reading of one frozen fixture by a second,
   independently written reader.  The text is provisional; the companion
   implementation carrying this profile is published.
- **draft-ietf-dnsop-ns-revalidation-14** (new-draft, score 2, ignored_after_review) [dnsop]: [Delegation Revalidation by DNS Resolvers](https://datatracker.ietf.org/doc/draft-ietf-dnsop-ns-revalidation/) — This document describes an optional algorithm for the processing of
   Name Server (NS) resource record (RR) sets (RRsets) during iterative
   resolution, and describes the benefits and considerations of using
   this approach.  When following a referral response from an
   authoritative server to a child zone, DNS resolvers should explicitly
   query the authoritative NS RRset at the apex of the child zone and
   cache this in preference to the NS RRset on the parent side of the
   zone cut.  The (A and AAAA) address RRsets in the additional section
   from referral responses and authoritative NS answers for the names of
   the NS RRset, should similarly be re-queried and used to replace the
   entries with the lower trustworthiness ranking in cache.  Resolvers
   should also periodically revalidate the delegation by re-querying the
   parent zone at the expiration of the shortest TTL among the parent NS
   RRset, the DS RRset (if present), and the child NS RRset.
- **draft-li-cats-intellinode-network-scheduling-01** (new-draft, score 2, ignored_after_review) [none]: [IntelliNode: In-Network Intelligent Scheduling Extensions for CATS](https://datatracker.ietf.org/doc/draft-li-cats-intellinode-network-scheduling/) — This document introduces IntelliNode, an in-network intelligent
   scheduling mechanism built upon the Computing-Aware Traffic Steering
   (CATS) framework.  Modern large-scale AI training and inference
   heavily rely on distributed heterogeneous clusters (GPU/CPU/FPGA).
   However, existing networks lack awareness of tensor semantics,
   training phases, and heterogeneous computing capabilities, leading to
   high communication latency, low resource utilization, and pipeline
   stalls.

   IntelliNode shifts away from the traditional passive scheduling
   paradigms that rely on probes and controllers.  By bypassing
   traditional paths and integrating FPGAs alongside programmable Switch
   ASICs, it constructs a rapid data-plane closed loop of "Perception-
   Inference-Decision-Execution".  This architecture performs feature
   extraction at line rate, leverages lightweight prediction models to
   infer short-term network behavior, and drives real-time heuristic
   scheduling decisions (e.g., path selection, tensor slicing, and
   compute matching).  This document defines the four core functional
   layers and extension signaling that support this architecture, laying
   the foundation for an AI-native, scalable distributed computing
   network.
- **draft-lz-fann-bandwidth-notification-00** (new-draft, score 2, ignored_after_review) [none]: [Fast Notification for Link Bandwidth](https://datatracker.ietf.org/doc/draft-lz-fann-bandwidth-notification/) — This document proposes a data-plane-based method for rapidly
   advertising end-to-end path bandwidth information using a bitmap
   encoding.  The mechanism enables fast load-balancing adjustments in
   AI/ML data center fabrics.
- **draft-dikshit-netmod-comparability-scope-extension-00** (new-draft, score 1, authorization) [none]: [A YANG Extension for Declaring the Comparability Scope of Operational State](https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/) — Several YANG modules currently in progress across multiple IETF
   working groups define counters, gauges, and other measured values
   that are exported from a network element and compared, summed, or
   averaged by a remote collector, either against the same node's
   history or against values from a different node. YANG (RFC 7950)
   has no first-class, machine-checkable way to state the domain
   within which two occurrences of such a value are comparable, so
   this determination is currently made, inconsistently or not at
   all, in prose. This document defines a YANG extension statement,
   "csc:comparability-scope", a four-value scope lattice, and a
   compatibility rule that lets a schema-aware tool statically detect
   an illegal aggregation across incomparable scopes, without waiting
   for it to happen at a collector.
- **draft-dikshit-nmop-telemetry-identifier-scoping-01** (new-draft, score 1, authorization) [none]: [Scoping and Comparability Requirements for Exported Network Telemetry Identifiers](https://datatracker.ietf.org/doc/draft-dikshit-nmop-telemetry-identifier-scoping/) — This document describes a recurring interoperability problem in
   exported network telemetry: many values are encoded without an
   explicit definition of the scope in which they are unique,
   meaningful, and comparable. In practice, the wire representation of
   a value may be standardized while the semantic context of that value
   remains implicit. As a result, a receiver may infer that two
   numerically identical values are equivalent when they were produced
   in different semantic domains and therefore refer to different
   objects, states, or observations.

   This ambiguity is operationally significant. It can lead to
   incorrect aggregation, incorrect cross-instance comparison, and
   erroneous conclusions about routing state, forwarding behavior, or
   network health. The risk is particularly visible in telemetry
   protocols that export statistics or identifiers in contexts such as
   VRFs, topology instances, address families, route distinguishers,
   policy domains, or other instance-specific scopes.

   This document argues that exported telemetry identifiers and
   statistics MUST explicitly define both the scope in which a value is
   unique and meaningful, and the conditions under which it may be
   compared with values from other contexts. This requirement is not
   limited to BMP; it applies to any telemetry mechanism in which a
   value can be generated in multiple semantic domains and therefore
   cannot be treated as self-describing solely by its encoded form.

## Ignored after review

- **draft-admnr-lsr-igp-measurement-group-03** (new-draft, score 0, ignored_after_review) [none]: [Advertising IGP Active Measurement Groups in Router Capabilities](https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/) — This document defines an IS-IS capability sub-TLV for advertising
   measurement group membership for Active Measurement Protocols (AMPs)
   such as TWAMP and STAMP.  The mechanism allows IGP routers to
   discover other routers participating in different measurement groups,
   enabling automatic discovery of measurement endpoints throughout an
   IS-IS routing domain.  The solution uses a Group ID to identify
   measurement group membership, where the same interface address (IPv4
   or IPv6) may be used for multiple measurement groups.
- **draft-albanna-regext-rdap-deleg-05** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for DNS DELEG](https://datatracker.ietf.org/doc/draft-albanna-regext-rdap-deleg/) — This document describes an extension of the Registration Data Access
   Protocol (RDAP) that includes DNS DELEG values in responses to RDAP
   domain object queries.
- **draft-bormann-cbor-cddl-2-draft-09** (new-draft, score 0, ignored_after_review) [none]: [CDDL 2.0 and beyond -- a draft plan](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-2-draft/) — The Concise Data Definition Language (CDDL) today is defined by
   RFC 8610, RFC 9165, RFC 9682, and RFC 9741).  RFC 9165 and the latter
   (as well as some more application specific specifications such as
   RFC 9090) have used the extension point provided in RFC 8610, the
   control operator.

   As CDDL is used in larger projects, feature requirements become known
   that cannot be easily mapped into this single extension point.
   Hence, there is a need for evolution of the base CDDL specification
   itself.

   The present document provides a roadmap towards a "CDDL 2.0"; it is
   intended to serve as a basis for implementations that evolve with the
   concept of CDDL 2.0.  It is based on draft-bormann-cbor-cddl-freezer,
   but is more selective in what potential features it takes up and more
   detailed in their discussion.  This document is intended to evolve
   over time; it might spawn specific documents and then retire, or it
   might eventually be published as a roadmap document.
- **draft-bormann-cbor-configuration-00** (new-draft, score 0, ignored_after_review) [none]: [CBOR Configuration](https://datatracker.ietf.org/doc/draft-bormann-cbor-configuration/) — This document discusses configuration of CBOR processors.  Using this
   information as a basis, it provides WGLC feedback on draft-ietf-cbor-
   serialization-08.
- **draft-bormann-dispatch-modern-network-unicode-09** (new-draft, score 0, ignored_after_review) [none]: [Modern Network Unicode](https://datatracker.ietf.org/doc/draft-bormann-dispatch-modern-network-unicode/) — BCP18 (RFC 2277) has been the basis for the handling of character-
   shaped data in IETF specifications for more than a quarter of a
   century now.  It singles out UTF-8 (STD63, RFC 3629) as the “charset”
   that MUST be supported, and pulls in the Unicode standard with that.

   Based on this, RFC 5198 both defines common conventions for the use
   of Unicode in network protocols and caters for the specific
   requirements of the legacy protocol Telnet.  In applications that do
   not need Telnet compatibility, some of the decisions of RFC 5198 can
   be cumbersome.

   The present specification defines “Modern Network Unicode” (MNU),
   which is a form of RFC 5198 Network Unicode that can be used in
   specifications that require the exchange of plain text over networks
   and where just mandating UTF-8 may not be sufficient, but there is
   also no desire to import all of the baggage of RFC 5198.

   As characters are used in different environments, MNU is defined in a
   one-dimensional (1D) variant that is useful for identifiers and
   labels, but does not use a structure of text lines.  A 2D variant is
   defined for text that is a sequence of text lines, such as plain text
   documents or markdown format.  Additional variances of these two base
   formats can be used to tailor MNU to specific areas of application.
- **draft-bormann-restatement-06** (new-draft, score 0, ignored_after_review) [none]: [The Restatement Anti-Pattern](https://datatracker.ietf.org/doc/draft-bormann-restatement/) — Normative documents that cite other normative documents often
   _restate_ normative content extracted out of the cited document in
   their own words.

   The present memo explains why this can be an Antipattern, and how it
   can be mitigated.
- **draft-buckeyne-jsox-format-00** (new-draft, score 0, ignored_after_review) [none]: [The JavaScript Object eXchange (JSOX) Data Interchange Format](https://datatracker.ietf.org/doc/draft-buckeyne-jsox-format/) — JavaScript Object eXchange (JSOX) is a lightweight, text-based,
   language-independent data interchange format.  It is derived from
   JSON and from the object literal syntax of the ECMAScript Programming
   Language Standard.  Every well-formed JSON text is a well-formed JSOX
   text.

   JSOX extends JSON with unquoted identifiers, additional string
   quoting and escape forms, comments, additional number forms including
   dates and arbitrary-precision integers, binary typed arrays, user-
   defined types carried by a type tag, field-name macros that remove
   repeated keys from a document, and references that permit shared and
   cyclic structures to be encoded.

   This document defines the JSOX grammar and registers the media type
   "application/jsox".
- **draft-cao-opsawg-ipfix-sav-04** (new-draft, score 0, ignored_after_review) [none]: [Export of Source Address Validation (SAV) Information in IPFIX](https://datatracker.ietf.org/doc/draft-cao-opsawg-ipfix-sav/) — This document specifies the IP Flow Information Export Information
   Elements to export the context and outcome of Source Address
   Validation enforcement data.  These SAV-specific Information Elements
   provide detailed insight into why packets are identified as spoofed
   by capturing the specific SAV rules that triggered validation
   decisions.  This operational visibility is essential for network
   operators to observe SAV enforcement behavior and analyze source
   address spoofing events detected by SAV.
- **draft-chen-grow-enhanced-as-loop-detection-09** (new-draft, score 0, ignored_after_review) [none]: [Enhanced AS-Loop Detection for BGP](https://datatracker.ietf.org/doc/draft-chen-grow-enhanced-as-loop-detection/) — Misconfiguration and malicious manipulation of the BGP `AS_PATH`
   attribute can lead to route hijacking.  This document proposes
   enhancements to BGP [RFC4271] inbound and outbound route processing
   when an AS loop is detected.  This mechanism can be implemented
   directly on devices or deployed in a centralized architecture using
   the BGP Monitoring Protocol (BMP) [RFC7854].  These enhancements
   empower networks to quickly and accurately detect route hijacking and
   malicious path poisoning.

   Two implementation options are proposed:
- **draft-choudhary-rcoap-00** (new-draft, score 0, ignored_after_review) [none]: [Ratcheted CoAP: A Forward-Secure Delta over OSCORE for Highly Constrained Wake-Send-Sleep Devices](https://datatracker.ietf.org/doc/draft-choudhary-rcoap/) — This document specifies RCOAP, a compact, zero-round-trip, link-layer
   agnostic object-security mechanism for highly constrained devices
   that transmit infrequently.  RCOAP is a targeted delta over OSCORE
   ([RFC8613]): instead of a single long-lived Sender Key, RCOAP derives
   a fresh symmetric key for every message via a one-way hash ratchet.
   This bounds the impact of physical device capture to future messages
   only, at the cost of a modest per-message size increase and the loss
   of future secrecy.  RCOAP is explicitly scoped to a narrow niche left
   open between OSCORE and EDHOC ([RFC9528]): devices for which even
   EDHOC's one-time handshake cost is disproportionate to their message
   rate or compute budget.  This document is a first individual
   submission, has not been reviewed by the IETF, and requests feedback
   in particular from the LAKE and CoRE working groups on whether this
   gap is real and worth standardizing, or already adequately covered.
- **draft-chung-ccwg-search-10** (new-draft, score 0, ignored_after_review) [none]: [SEARCH -- a New Slow Start Algorithm for TCP and QUIC](https://datatracker.ietf.org/doc/draft-chung-ccwg-search/) — TCP slow start is designed to ramp up to the network congestion point
   quickly, doubling the congestion window each round-trip time until
   the congestion point is reached, whereupon TCP exits the slow start
   phase.  Unfortunately, the default Linux TCP slow start
   implementation -- TCP Cubic with HyStart [HYSTART] -- can cause
   premature exit from slow start, especially over wireless links,
   degrading link utilization.  However, without HyStart, TCP exits slow
   start too late, causing unnecessary packet loss.  To improve TCP slow
   start performance, this document proposes using the Slow start Exit
   At Right CHokepoint (SEARCH) algorithm [KCL24] where the TCP sender
   determines the congestion point based on acknowledged deliveries --
   specifically, the sender computes the delivered bytes compared to the
   sent bytes, smoothed to account for link latency variation and
   normalized to accommodate link capacities, and initiates exits slow
   start if the delivered bytes are lower than expected.  We implemented
   SEARCH in Linux, FreeBSD, and QUIC and evaluated it over WiFi, 4G/
   LTE, and low earth orbit (LEO) and geosynchronous (GEO) satellite
   links.  Analysis of the results show that SEARCH reliably exits from
   slow start after the congestion point is reached but before inducing
   packet loss.
- **draft-cmcc-asrp-07** (new-draft, score 0, ignored_after_review) [none]: [Available Session Recovery Protocol](https://datatracker.ietf.org/doc/draft-cmcc-asrp/) — This document describes an experimental protocol named the Available
   Session Recovery Protocol (ASRP).  The protocol is designed to
   optimize high-availability network cluster architectures, providing a
   superior high-availability solution for clusters offering stateful
   network services such as load balancing and Network Address
   Translation (NAT [RFC4787]).  ASRP defines the procedures for session
   backup and recovery, as well as the message formats used during these
   interactions, enabling efficient and streamlined session state
   management.

   In contrast to traditional high-availability techniques that back up
   session state within the cluster itself, the core innovation of ASRP
   lies in its distributed backup of state information to the client or
   server side.  This approach offers multiple advantages: theoretically
   unlimited elastic scaling capacity; support for rapid recovery from
   multi-point failures; reduction of resource redundancy through the
   elimination of centralized backup nodes; and significant
   simplification of cluster implementation complexity.

   The ASRP protocol provides a standardized method for constructing
   elastic service clusters, facilitating broader participation from
   software and hardware developers in building elastic cloud network
   service clusters.
- **draft-davis-ivy-equipment-capability-application-02** (new-draft, score 0, ignored_after_review) [none]: [Equipment Capability Application](https://datatracker.ietf.org/doc/draft-davis-ivy-equipment-capability-application/) — This document applies the generalized capability principles to the
   description of equipment (a physical thing) with applied data
   (configuration state and code (software, firmware etc.)) and shows
   how such capability specifications integrate with base inventory and
   entitlement models as defined in Network Inventory, Software
   Extension and Entitlement YANG models.

   The approach is examined by example, focusing on how the potential
   capabilities of each equipment type-version with applied data are
   described, how these map to entitlements (licensed or policy-
   controlled subsets of capabilities), and how they are instantiated as
   inventory items.  The explanation covers both the capabilities of
   equipment in terms of physical properties and the capabilities of
   equipment with applied data in terms of resultant emergent
   functionality.
- **draft-davis-nmop-generalized-capability-principles-02** (new-draft, score 0, ignored_after_review) [none]: [Generalized Capability Principles](https://datatracker.ietf.org/doc/draft-davis-nmop-generalized-capability-principles/) — This document introduces a framework for capability modeling based on
   the specification and refinement principles established in ITU-T
   G.7711 Annex G (also previously published as ONF TR-512.7.  See
   latest G.7711 release) and the modeling boundaries work documented in
   draft-davis-netmod-modelling-boundaries.  The framework defines how
   component–system capabilities can be explicitly described and refined
   via a process of pruning, refactoring, and occurrence formation.

   This draft version additionally incorporates a sketch of an
   occurrence-semantics kernel.  This kernel is presented here as a
   continuation of the refinement and occurrence-formation principles
   already introduced in the previous version, not as a retrospective
   reinterpretation of them.

   These capability definitions can target detailed operational
   considerations, system interactions, licensing, abstract product
   declarations, or sales and marketing.  The framework supports
   modular, layered, and fractal declarations of networked behavior, and
   provides a foundation for a suite of future IETF drafts aligned with
   ongoing work on photonic plug manifests, entitlement/licensing, IVY
   equipment modeling, energy/thermal considerations and related
   domains.
- **draft-dikshit-bess-evpn-df-hashing-analysis-00** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Consistent Hashing to Designated Forwarder Election Scope Transitions in EVPN](https://datatracker.ietf.org/doc/draft-dikshit-bess-evpn-df-hashing-analysis/) — [RFC8584] defines Highest Random Weight (HRW) as the algorithm for
   Designated Forwarder election in EVPN, and, in Section 3.1, names
   the Consistent Hashing family of algorithms as addressing the same
   object-to-server mapping problem before explicitly declining to
   evaluate them: "these will not be considered here."
   [I-D.ietf-bess-evpn-per-mcast-flow-df-election] subsequently
   introduces a scope transition, from per-(ES,VLAN) to per-
   (ES,VLAN,S,G) election, that is precisely a key-space-resizing
   event of the kind Consistent Hashing was designed to bound churn
   for. This document proposes the applicability analysis RFC 8584
   declined to make: it defines a DF-churn metric, states HRW's and
   Consistent Hashing's known theoretical guarantees against it, and
   sets out an evaluation methodology, using bounded-load Consistent
   Hashing as the specific comparison point, given multicast group
   popularity is known to be highly non-uniform in deployed networks.
- **draft-dikshit-bess-evpn-mobility-crdt-00** (new-draft, score 0, ignored_after_review) [none]: [Modeling EVPN MAC-Mobility Sequence State as a Conflict-Free Replicated Data Type](https://datatracker.ietf.org/doc/draft-dikshit-bess-evpn-mobility-crdt/) — EVPN MAC Mobility, as carried in the MAC Mobility Extended
   Community defined by [RFC7432], uses a per-MAC sequence number to
   let PEs agree on the most recent location of a moving host.
   [I-D.ietf-bess-evpn-umr-mobility] extends this to cross-data-center
   moves via gateways, and already specifies, in some detail, how
   ordinary intra-DC and inter-DC moves are kept consistent: each
   gateway maintains two independent MAC Mobility sequence counters
   per host (one intra-DC, one inter-DC) specifically so that a
   purely local move does not have to be reconciled against the
   interconnect network's state. What that document does not specify
   is what a gateway does if it fails after locally resetting its
   intra-DC counter to zero (Section 5.2, the step taken when a host
   is confirmed to have left every local PE) but before propagating
   that fact onward; no failure-handling or crash-recovery text
   exists anywhere in the document. This document shows that this
   narrower, but concretely unaddressed, gap is a special case of a
   data type with known, formally proven convergence properties, the
   Last-Writer-Wins Register, one member of the Conflict-Free
   Replicated Data Type (CRDT) family, and proposes modeling the
   per-gateway mobility sequence state that way so that a mid-reset
   gateway crash is recovered from as a consequence of the data
   type's algebra rather than requiring a new, separately specified
   recovery procedure.
- **draft-dikshit-netconf-yang-push-causal-ordering-00** (new-draft, score 0, ignored_after_review) [none]: [Comparable Sequence Numbers Across Publishers in YANG Datastore Telemetry](https://datatracker.ietf.org/doc/draft-dikshit-netconf-yang-push-causal-ordering/) — YANG Datastore Telemetry, YANG-Push version 2
   [I-D.ietf-netconf-yang-push-2], assigns each publisher a
   monotonically increasing sequence number so a receiver can detect
   loss and reordering. The current design leaves two questions
   unanswered: what happens when the counter wraps, and how a
   receiver aggregating records from more than one publisher is to
   compare sequence numbers that were never defined to be comparable
   across publishers in the first place. Both questions have already
   been studied, and largely settled, in the distributed systems
   literature under the heading of logical and hybrid logical clocks,
   and in deployed streaming systems under the heading of offset and
   epoch numbering. This document evaluates three existing causal-
   ordering primitives against YANG-Push's specific constraints and
   proposes adopting a Hybrid Logical Clock so that the wraparound and
   cross-publisher comparison problems are removed by construction
   rather than patched with a wider counter.
- **draft-garg-l2vpn-over-srv6-02** (new-draft, score 0, ignored_after_review) [none]: [Method to enable signaling of L2VPN services using SRv6 extensions](https://datatracker.ietf.org/doc/draft-garg-l2vpn-over-srv6/) — This document describes a mechanism to provide L2VPN services using
   Segment Routing over IPv6 (SRv6), eliminating the need for a separate
   signaling protocol for VPN label distribution.  In current
   deployments, L2VPN services rely on dedicated protocols such as the
   Label Distribution Protocol (LDP) or Border Gateway Protocol (BGP)
   for service label signaling, which adds control-plane complexity.
   The proposed mechanism introduces an SRv6-based extension that
   enables L2VPN service identification within the SRv6 framework,
   reducing control-plane overhead and providing a simplified and
   efficient solution for L2VPN service delivery.
- **draft-ginsberg-lsr-hello-capability-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Hello Capability](https://datatracker.ietf.org/doc/draft-ginsberg-lsr-hello-capability/) — Advertisement of capabilities in Hellos is useful to allow support of
   optional features in establishing and maintaining adjacencies.  This
   document defines a new TLV to be sent in hellos to advertise such
   capabilities.
- **draft-goncharov-rfcregsimples-00** (new-draft, score 0, ignored_after_review) [none]: [A CBOR Simple Values Range for Packing and Templating](https://datatracker.ietf.org/doc/draft-goncharov-rfcregsimples/) — The Concise Binary Object Representation (CBOR, RFC 8949, STD 94) is
   a data format whose design goals include the possibility of extremely
   small code size, fairly small message size, and extensibility without
   the need for version negotiation.

   This document registers a range of sixteen CBOR simple values (0 to
   15) that can be shared by different specifications using them for
   CBOR transformations, such as compression or templating, in a non-
   conflicting way.  This allows current and future specifications to
   reuse the smallest (single-byte) simple values range while defining
   their own ways to use them for achieving their goals.

   This document updates RFC 8949.
- **draft-gould-regext-rdap-server-validation-02** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Server Validation](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-server-validation/) — This document describes an Registration Data Access Protocol (RDAP)
   extension for providing the status of server validations.  Server
   validations can be done for an extensible set of types, with examples
   including validating DNS resolution with the type "dns" and
   validating DNSSEC with the type "dnssec".  The validations can be
   performed synchronously in the provisioning command or asynchronously
   based on a triggering command or a schedule.  The extension will
   provide the status of the validations, by type, performed by the
   server in an RDAP lookup response.
- **draft-gould-regext-rdap-status-set-03** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Status Set](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-status-set/) — This document describes an Registration Data Access Protocol (RDAP)
   extension for including status sets assigned to RDAP object classes,
   such as the Domain Object Class and the Nameserver Object Class in
   [RFC9083].  There can be many overlapping reasons for each of the
   "status" member values, such as implementing a lock service,
   complying with a court order, or addressing domain abuse.  A status
   set defines an object representing the reason for setting a "status"
   value, so clients and servers can effectively manage the overlapping
   reasons of individual "status" values using the status sets.  This
   RDAP extension supports returning the assigned client and server
   status sets with additional data members, such as the mapped "status"
   values and when the status set was assigned.
- **draft-gq-savnet-sav-terms-02** (new-draft, score 0, ignored_after_review) [none]: [Currently Used Terminology Related to Source Address Validation](https://datatracker.ietf.org/doc/draft-gq-savnet-sav-terms/) — This document provides an overview of terms and abbreviations related
   to Source Address Validation (SAV).  Its purpose is to establish a
   common and consistent set of terminology for use across SAV-related
   discussions and documents.  This document explicitly does not serve
   as an authoritative source of correct terminology.
- **draft-gray-plants-mtc-deploy-use-cases-01** (new-draft, score 0, ignored_after_review) [none]: [Merkle Tree Certificates Deployment Use Cases](https://datatracker.ietf.org/doc/draft-gray-plants-mtc-deploy-use-cases/) — Merkle Tree Certificates (MTC) I-D.ietf-plants-merkle-tree-certs has
   been defined for the use case of the WebPKI.  In this document we
   explore when and how MTC in parts or full can be used in different
   use cases.  Some of this use-cases may provide benefit for private
   PKI usage.
- **draft-grimminck-safe-ioc-sharing-13** (new-draft, score 0, ignored_after_review) [none]: [Safe and Reversible Sharing of Malicious URLs and Indicators](https://datatracker.ietf.org/doc/draft-grimminck-safe-ioc-sharing/) — This document codifies a consistent and reversible convention used in
   the threat intelligence and security communities for sharing
   potentially malicious indicators of compromise (IOCs), such as URLs,
   IP addresses, email addresses, and domain names.  It describes an
   obfuscation format that reduces the risk of accidental execution or
   activation when IOCs are displayed or transmitted.  The
   transformation renders an indicator syntactically invalid as a URI
   while keeping it recognizable to a human reader, and the original
   value can be recovered deterministically.  Safe-IOC strings are a
   textual rendering convention, not URIs, and are not intended to be
   processed by generic URI parsers.  These conventions aim to improve
   interoperability among tools and feeds that exchange threat
   intelligence data.
- **draft-ietf-bess-evpn-bfd-16** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Network Layer Fault Management](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-bfd/) — This document specifies proactive, in-band Network Layer OAM (RFC
   9062) mechanisms to detect loss of continuity faults that affect
   unicast and multi-destination paths (used by Broadcast, Unknown
   Unicast, and Multicast traffic) in an Ethernet VPN (EVPN, RFC
   7432bis) network.  The mechanisms specified in this document use the
   widely adopted Bidirectional Forwarding Detection (RFC 5880)
   protocol.
- **draft-ietf-calext-jscalendar-icalendar-26** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-cats-metric-definition-11** (new-draft, score 0, ignored_after_review) [cats]: [CATS Metrics Definition](https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/) — Computing-Aware Traffic Steering (CATS) is a traffic engineering
   approach that optimizes the steering of traffic to a service instance
   by considering the dynamic state of computing and network resources.
   To enable such decisions, CATS components exchange metrics that
   describe resource conditions affecting service instance selection.
   This document focuses on compute and communication metrics for CATS
   and defines a hierarchical abstraction of these metrics to improve
   interoperability, scalability, and operational simplicity.  It does
   not aim to standardize raw infrastructure (Level 0) metrics; instead,
   it specifies higher-level representations that can be derived from
   raw measurements using aggregation and normalization functions.
- **draft-ietf-cbor-cddl-modules-07** (new-draft, score 0, ignored_after_review) [cbor]: [CDDL Module Structure](https://datatracker.ietf.org/doc/draft-ietf-cbor-cddl-modules/) — At the time of writing, the Concise Data Definition Language (CDDL)
   is defined by RFC 8610 and RFC 9682 as well as RFC 9165 and RFC 9741.
   The latter two have used the extension point provided in RFC 8610,
   the _control operator_.

   As CDDL is being used in larger projects, the need for features has
   become known that cannot be easily mapped into this single extension
   point.

   The present document defines a backward- and forward-compatible way
   to add a module structure to CDDL.
- **draft-ietf-cdni-ci-triggers-rfc8007bis-20** (new-draft, score 0, ignored_after_review) [cdni]: [Content Delivery Network Interconnection (CDNI) Control Interface / Triggers 2nd Edition](https://datatracker.ietf.org/doc/draft-ietf-cdni-ci-triggers-rfc8007bis/) — This document obsoletes RFC8007.  The document describes the part of
   Content Delivery Network Interconnection (CDNI) Control interface
   that allows a CDN to trigger activity in an interconnected CDN that
   is configured to deliver content on its behalf.  The upstream CDN MAY
   use this mechanism to request that the downstream CDN preposition,
   invalidate, and/or purge metadata and/or content.  The upstream CDN
   MAY monitor the status of activity that it has triggered in the
   downstream CDN.
- **draft-ietf-core-groupcomm-proxy-07** (new-draft, score 0, ignored_after_review) [core]: [Proxy Operations in Group Communication for the Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/draft-ietf-core-groupcomm-proxy/) — This document defines a specific realization of proxy intended for
   scenarios that use group communication for the Constrained
   Application Protocol (CoAP).  Such a proxy processes a single request
   sent by a client typically over unicast and distributes the request
   to a group of servers, e.g., over UDP/IP multicast as the defined
   default transport protocol.  Then, the proxy collects the individual
   responses from those servers and relays those responses back to the
   client, in a way that allows the client to distinguish the responses
   and their origin servers through embedded addressing information.
   This document updates RFC7252 with respect to caching of response
   messages at proxies.
- **draft-ietf-dmm-srv6mob-arch-04** (new-draft, score 0, ignored_after_review) [dmm]: [Architecture Discussion on SRv6 Mobile User plane](https://datatracker.ietf.org/doc/draft-ietf-dmm-srv6mob-arch/) — This document describes the solution approach and its architectural
   benefits of transforming mobile session information into routing
   information, leveraging segment routing capabilities, and operating
   within the IP routing paradigm.
- **draft-ietf-idr-bgpls-inter-as-topology-ext-43** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extensions for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedures for distributing Border
   Gateway Protocol-Link State (BGP-LS) key parameters for inter-domain
   links between two Autonomous Systems (ASes).  It defines a new type
   within the BGP-LS Network Layer Reachability Information (NLRI) for
   an Inter-AS Link, along with three new Type-Length-Values (TLVs)
   descriptors for the BGP-LS Inter-AS Link.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   inter-AS topology using information provided by the BGP-LS protocol.
- **draft-ietf-idr-rtc-hierarchical-rr-06** (new-draft, score 0, ignored_after_review) [idr]: [RT-Constrain Optimization in Hierarchical Route Reflection Scenarios](https://datatracker.ietf.org/doc/draft-ietf-idr-rtc-hierarchical-rr/) — The Route Target (RT) Constrain mechanism specified in RFC 4684 is
   used to build a route distribution graph in order to restrict the
   propagation of Virtual Private Network (VPN) routes.  In network
   scenarios where hierarchical route reflection (RR) is used, the
   existing RT-Constrain mechanism cannot guarantee a correct route
   distribution graph.  This document describes the problem scenario and
   proposes solutions to address the RT-Constrain issue in hierarchical
   RR scenarios.
- **draft-ietf-idr-ts-flowspec-srv6-policy-18** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  Specifically, it defines
   protocol mechanisms for combining FlowSpec NLRIs with specific BGP
   Extended Communities for transport policy steering (Mode 1) in SR-
   MPLS and SRv6 networks, and optionally with the BGP Prefix-SID
   Attribute when egress service action execution is required (Mode 2)
   in SRv6 networks.
- **draft-ietf-ippm-alt-mark-deployment-08** (new-draft, score 0, ignored_after_review) [ippm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-ipsecme-diet-esp-11** (new-draft, score 0, ignored_after_review) [ipsecme]: [ESP Header Compression with Diet-ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-diet-esp/) — This document specifies Diet-ESP, a compression mechanism for control
   information in IPsec/ESP communications.  The compression uses Static
   Context Header Compression rules.
- **draft-ietf-ipsecme-eesp-04** (new-draft, score 0, ignored_after_review) [ipsecme]: [Enhanced Encapsulating Security Payload (EESP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp/) — This document describes the Enhanced Encapsulating Security Payload
   (EESP) protocol, which builds on the existing IP Encapsulating
   Security Payload (ESP) protocol.  It is designed to modernize and
   overcome limitations in the ESP protocol.

   EESP adds Session IDs (e.g., to support CPU pinning and QoS support
   based on the inner traffic flow), changes some previously mandatory
   fields to optional, and moves the ESP trailer into the EESP header.
   Additionally, EESP adds header options adapted from IPv6 to allow for
   future extension.  New header options are defined which add a crypt-
   offset to allow for exposing inner flow information for middlebox
   use.
- **draft-ietf-ipsecme-eesp-ikev2-03** (new-draft, score 0, ignored_after_review) [ipsecme]: [IKEv2 negotiation for Enhanced Encapsulating Security Payload (EESP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp-ikev2/) — This document specifies how to negotiate the use of the Enhanced
   Encapsulating Security Payload (EESP) protocol using the Internet Key
   Exchange protocol version 2 (IKEv2).  The EESP protocol, which is
   defined in [I-D.ietf-ipsecme-eesp], provides the same security
   services as Encapsulating Security Payload (ESP), but has richer
   functionality and provides better performance in specific
   circumstances.  This document specifies negotiation of version 0 of
   EESP.
- **draft-ietf-ipsecme-ikev2-diet-esp-extension-08** (new-draft, score 0, ignored_after_review) [ipsecme]: [Internet Key Exchange version 2 (IKEv2) extension for Header Compression Profile (HCP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-diet-esp-extension/) — This document describes an IKEv2 extension for Header Compression to
   agree on Attributes for Rule Derivation.  This extension defines the
   necessary registries for the ESP Header Compression Profile (EHCP)
   Diet-ESP.
- **draft-ietf-moq-transport-20** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-nfsv4-uncacheable-files-12** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable File Data Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-files/) — Network File System version 4.2 (NFSv4.2) clients commonly perform
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
- **draft-ietf-nmop-simap-concept-13** (new-draft, score 0, ignored_after_review) [nmop]: [SIMAP: Concept, Requirements, and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/) — This document defines the concept of Service & Infrastructure Maps
   (SIMAP) and identifies a set of SIMAP requirements and use cases.
   The SIMAP was previously known as Digital Map. SIMAP evolves the
   earlier 'Digital Map' concept by making explicit the ties between
   service and infrastructure layers, clarifying expected outcomes for
   operations and automation, and addressing ambiguity associated with
   the term 'digital.'

   The document intends to be used as a reference for the assessment of
   the various topology modules to meet SIMAP requirements.
- **draft-ietf-pce-sr-p2mp-policy-20** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-gaap-23** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
   multicast group address allocation protocol (named GAAP and
   pronounced "gap" as in "mind the gap").  GAAP requires no centralized
   service or coordination for the address-allocation protocol itself,
   though it depends on ASM-capable multicast routing already being
   provisioned in the deployment domain, and deployments using
   encryption or administrative scoping may require additional
   configuration.  The protocol runs among group participants which need
   a unique group address to send and receive multicast packets.
   Tailored for IPv4 and IPv6 networks, this design offers a simple,
   lightweight option rather than extending an existing protocol.  This
   document is Experimental, see Section 8 for the rationale and the
   criteria for concluding the experiment.
- **draft-ietf-pim-ipv6-zeroconf-assignment-11** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the criteria listed in RFC 10019.
- **draft-ietf-regext-epp-https-04** (new-draft, score 0, ignored_after_review) [regext]: [Extensible Provisioning Protocol (EPP) Transport over HTTPS](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-https/) — This document describes how an Extensible Provisioning Protocol (EPP)
   connection is mapped onto the Hypertext Transfer Protocol (HTTP).
   EPP over HTTP (EoH) requires the use of Transport Layer Security
   (TLS) to secure EPP information (i.e. HTTPS).
- **draft-ietf-satp-usecases-10** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer (SAT) Use Cases](https://datatracker.ietf.org/doc/draft-ietf-satp-usecases/) — This document describes prominent scenarios where enterprise systems
   and networks maintaining digital assets require the ability to
   securely transfer assets or data to each other.
- **draft-ietf-snac-simple-12** (new-draft, score 0, ignored_after_review) [snac]: [Automatically Connecting Stub Networks to Unmanaged Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-snac-simple/) — This document specifies a set of practices for using IPv6 networking
   to automatically connect stub networks to adjacent infrastructure
   networks, even if they do not otherwise use IPv6.  This is applicable
   in cases such as constrained (Internet of Things) networks where
   there is a need to provide functional parity of service discovery and
   reachability between devices on the stub network and devices on an
   adjacent infrastructure link (for example, a home network).
- **draft-ietf-teas-actn-poi-applicability-20** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) to Packet Optical Integration (POI)](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-applicability/) — This document explores the applicability of the Abstraction and
   Control of TE Networks (ACTN) architecture to Packet Optical
   Integration (POI) within the context of IP/MPLS and optical
   internetworking.  It examines the YANG data models defined by the
   IETF that enable an ACTN-based deployment architecture and highlights
   specific scenarios pertinent to Service Providers.

   Existing IETF protocols and data models are identified for each
   multi-technology scenario (packet over optical), particularly
   emphasising the Multi-Domain Service Coordinator to Provisioning
   Network Controller Interface (MPI) within the ACTN architecture
- **draft-ietf-v6ops-rfc6146-bis-16** (new-draft, score 0, ignored_after_review) [v6ops]: [Stateful NAT64: Network Address and Protocol Translation from IPv6 Clients to IPv4 Servers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc6146-bis/) — This document specifies a stateful NAT64 translation, which allows
   IPv6-Only clients to contact IPv4 servers using unicast UDP, TCP, or
   ICMP.  One or more public IPv4 addresses assigned to a stateful NAT64
   translator are shared among several IPv6-Only clients.  Stateful
   NAT64 translation also supports IPv4-initiated communications to a
   subset of the IPv6 hosts through configured bindings in the stateful
   NAT64 translator.  When the stateful NAT64 translation is used in
   conjunction with DNS64, no changes are required in either the IPv6
   client or the IPv4 server.

   This document obsoletes RFC 6146.
- **draft-irtf-icnrg-ccnxversioning-01** (new-draft, score 0, ignored_after_review) [icnrg]: [CCNx Content Versioning](https://datatracker.ietf.org/doc/draft-irtf-icnrg-ccnxversioning/) — This document defines a method for content versioning in CCNx,
   enabling the differentiation of content published under the same name
   using version numbers.  This document updates RFC8569 [RFC8569] and
   RFC8609 [RFC8609].
- **draft-jennings-moq-discovery-01** (new-draft, score 0, ignored_after_review) [none]: [DNS and mDNS Discovery for MOQT](https://datatracker.ietf.org/doc/draft-jennings-moq-discovery/) — This document defines how MOQT clients discover server endpoints
   using DNS and Multicast DNS (mDNS).  It specifies SVCB and HTTPS DNS
   record mappings for the moqt URI scheme, SRV records as a fallback
   mechanism, and DNS-SD over mDNS for local network discovery.
- **draft-kalosha-stb-tls13-00** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-kolomytsev-pshmp-core-00** (new-draft, score 0, ignored_after_review) [none]: [PSHMP Core: Decentralized L4 Overlay for Resilient Data Delivery and Proactive Self-Healing Networks](https://datatracker.ietf.org/doc/draft-kolomytsev-pshmp-core/) — PSHMP Core is a decentralized data delivery and proactive self-
   healing network core designed for distributed systems operating over
   existing IP infrastructure.  PSHMP Core provides an intelligent
   network layer above the existing IP network and enables distributed
   nodes to participate in dynamic multi-hop data delivery without
   requiring changes to the underlying Layer 3 routing infrastructure.

   The architecture is designed around decentralized path selection,
   continuous node and path assessment, dynamic relay chains, proactive
   recovery, and diversity-aware reconstruction of delivery paths.  The
   system can detect degradation of network participants and reconstruct
   affected delivery paths before or during service degradation.  This
   approach is intended to reduce recovery time, improve resilience, and
   maintain reliable data delivery in environments where individual
   nodes, paths, or network segments may become unstable.

   This document provides a high-level architectural overview of PSHMP
   Core, its primary components, operating principles, and potential
   application areas.  This document intentionally does not disclose
   implementation-specific algorithms, internal scoring details,
   proprietary optimization techniques, or other information that may be
   required for commercial implementation.
- **draft-kushwaha-scim-attr-cursor-pagination-01** (new-draft, score 0, ignored_after_review) [none]: [Cursor-Based Pagination and Deferred Retrieval for Multi-Valued Attributes in SCIM 2.0](https://datatracker.ietf.org/doc/draft-kushwaha-scim-attr-cursor-pagination/) — [RFC7643] defines Group.members with the returned: default
   characteristic, so a conformant service provider is required to
   return the attribute in response to GET /Groups/{id}. [RFC7644]
   defines no bound on the number of values that attribute may contain.
   A service provider holding a group with millions of members therefore
   has no conformant and interoperable way to answer a request that a
   client is entitled to make.  In practice providers diverge: they
   truncate silently, reject the request, omit the attribute, or fail.
   A client cannot discover in advance which behavior it will encounter.

   This document defines that missing behavior.  It specifies discovery
   so a client can learn how a service provider treats a high-
   cardinality attribute, a bounded response with a defined continuation
   contract, and rules preventing a partial representation from being
   mistaken for complete resource state.

   The mechanism has two forms.  A request for one resource returns a
   bounded page of one protected multi-valued attribute with an opaque
   cursor when more values exist.  A collection search returns parent
   resources without loading protected attributes, each carrying an
   authoritative link for retrieving that attribute.  The attribute
   remains part of its parent resource; this document does not create a
   top-level resource for each attribute value, and it is not a
   substitute for doing so where independent relationship lifecycle or
   cross-collection query is required (Section 16.4).

   Although the mechanism is defined generally and applies to any
   complex multi-valued attribute a service provider designates as
   protected, the attributes that reach problematic sizes in deployed
   SCIM services are predominantly Group.members and User.groups among
   those defined in [RFC7643], together with implementation-specific
   assignment attributes (Section 3).

   This document updates [RFC7643] and [RFC7644].  It adds attributes to
   existing structures defined by those documents and defines attribute-
   return behavior that replaces the requirements of Section 3.9 of
   [RFC7644] within a negotiated scope.  It does not change the behavior
   of deployments that do not implement it: the modified attribute-
   selection behavior described in Section 4 applies only between a
   service provider that has advertised this capability and a client for
   which deferred retrieval has been established through the negotiation
   mechanisms defined in this document.  It defines discovery metadata,
   the attributeCount and attributeCursor query parameters, response
   metadata, processing and compatibility rules, mutation safety, error
   handling, cursor security, and operational limits.
- **draft-li-lsr-igp-reverse-prefix-metric-05** (new-draft, score 0, ignored_after_review) [none]: [IGP Reverse Prefix Metric](https://datatracker.ietf.org/doc/draft-li-lsr-igp-reverse-prefix-metric/) — This document defines a method for calculating reverse paths by
   advertising reverse prefix costs.  This method aims to solve the
   problem of strict RPF (Reverse Path Forwarding) check failure caused
   by mismatched bidirectional path costs in multi-area IGP scenarios.
- **draft-lin-bfd-path-consistency-over-sr-07** (new-draft, score 0, ignored_after_review) [none]: [BFD Path Consistency over SR](https://datatracker.ietf.org/doc/draft-lin-bfd-path-consistency-over-sr/) — Bidirectional Forwarding Detection (BFD) can be used to monitor
   paths between nodes.

   U-BFD defined in [I-D.ietf-bfd-unaffiliated-echo] can effectively
   reduce the device equipment.

   Seamless BFD (S-BFD) provides a simplified mechanism which is
   suitable for monitoring of paths that are setup dynamically and on a
   large scale network.

   In SR network, BFD can also be used to monitor SR paths. When a
   headend use BFD to monitor the segment list/CPath of SR Policy, the
   forward path of control packet is indicated by segment list, the
   reverse path of response control packet is via the shortest path
   from the reflector back to the initiator (headend) as determined by
   routing. The forward path and reverse path of control packet are
   likely inconsistent going through different intermediate nodes or
   links.

   This document describes a method to keep the forward path and
   reverse path consistent when using S-BFD or U-BFD to detect SR
   Policy
- **draft-liu-sidrops-ipfix-bgp-pov-00** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP Prefix Origin Validation in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-liu-sidrops-ipfix-bgp-pov/) — This document defines an IP Flow Information Export (IPFIX)
   Information Element for monitoring the state of Resource Public Key
   Infrastructure (RPKI) based BGP Prefix Origin Validation.  The
   Information Element enables network operators to collect and analyze
   BGP route validation states (valid, invalid, not-found) to facilitate
   the detection of potential route hijacks improving network
   observability and security.
- **draft-mglt-ipsecme-dscp-np-06** (new-draft, score 0, ignored_after_review) [ipsecme]: [Differentiated Services Field Codepoints Internet Key Exchange version 2 Notification](https://datatracker.ietf.org/doc/draft-mglt-ipsecme-dscp-np/) — This document outlines the DSCP Notification Payload, which, during a
   CREATE_CHILD_SA Exchange, explicitly indicates the DSCP code points
   that will be encapsulated in the newly established tunnel.  This
   document updates RFC 4301.
- **draft-nordin-ocm-mls-federated-groups-02** (new-draft, score 0, ignored_after_review) [ocm]: [Federated Groups in Open Cloud Mesh using Messaging Layer Security](https://datatracker.ietf.org/doc/draft-nordin-ocm-mls-federated-groups/) — This document defines an extension to the Open Cloud Mesh (OCM)
   protocol to support federated groups as Receiving Parties of shares.
   This is achieved using the Messaging Layer Security (MLS) protocol
   (RFC 9420) as a group management layer.  MLS is used for establishing
   and rotating a shared group key across federated group members, as
   well as for maintaining group state.  This gives not only a way of
   federating group membership, but also a standardized way of
   distributing encryption keys in a cryptographically secure way, so
   that files shared with a group can optionally be encrypted and
   decrypted.  MLS usage in OCM acts as a vehicle for group management
   that gives users optional encryption capabilities for resources
   shared with federated groups.
- **draft-nottingham-archive-embargo-00** (new-draft, score 0, ignored_after_review) [none]: [Embargoing Archive Publication using robots.txt](https://datatracker.ietf.org/doc/draft-nottingham-archive-embargo/) — Web sites often block archiving crawlers because they host time-
   sensitive information.  This specification documents a robots.txt
   extension, "Archive-Embargo", that can be used to request that such
   crawlers delay publication of information.

   This document updates RFC 9309 to add two directives that support
   embargoes.
- **draft-prabel-cfrg-suf-hybrid-sigs-02** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Digital Signatures with Strong Unforgeability](https://datatracker.ietf.org/doc/draft-prabel-cfrg-suf-hybrid-sigs/) — This document proposes a generic hybrid signature construction that
   achieves strong unforgeability under chosen-message attacks (SUF-
   CMA), provided that the second component (typically the post-quantum
   one) is SUF-CMA secure.  The proposed hybrid construction differs
   from the current composite hybrid approach by binding the second
   (post-quantum) signature to the concatenation of the message and the
   first (traditional) signature.  This approach ensures that hybrid
   signatures maintain SUF-CMA security even when the first component
   only provides EUF-CMA security.

   In addition to this general hybrid construction, this document also
   proposes a non-black-box variant specifically tailored for schemes
   built from the Fiat-Shamir paradigm.  This variant is SUF-CMA secure
   as long as only one component is SUF-CMA secure.
- **draft-pradeepkumarxplorer-videosurfing-00** (new-draft, score 0, ignored_after_review) [none]: [The LIMITS SMTP Service Extension](https://datatracker.ietf.org/doc/draft-pradeepkumarxplorer-videosurfing/) — To allow browsing in videos
- **draft-rfcxml-pqc-key-fragmentation-00** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Cryptography Recommendations for Key Fragmentation in Low-Power Device Protocols](https://datatracker.ietf.org/doc/draft-rfcxml-pqc-key-fragmentation/) — Cryptographic protocols deployed on low-power and constrained devices
   increasingly need to accommodate the larger key sizes introduced by
   modern and post-quantum cryptographic (PQC) algorithms.  Many
   constrained network technologies (such as 6LoWPAN, SCHC, and similar
   adaptation-layer protocols) use explicit fragmentation mechanisms to
   transport messages that exceed link-layer frame sizes.  As a result,
   cryptographic keying material and key-establishment messages may be
   segmented across multiple fragments during transmission.

   This document analyzes the security and operational implications of
   such fragmentation.  It identifies common fragmentation patterns and
   examines risks including fragment loss, reordering, duplication, and
   partial exposure.  It further discusses fragment-level integrity,
   replay resistance, and correct binding of fragments to cryptographic
   session state.  This document does not define new cryptographic
   algorithms or fragmentation mechanisms.
- **draft-song-pce-pcep-sav-03** (new-draft, score 0, ignored_after_review) [none]: [Path Computation Element Communication Protocol for Source Address Validation](https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/) — This document presents a method of Path Computation Element (PCE) for
   Source Address Validation (SAV) in networks.  It extends Path
   Computation Element Communication Protocol (PCEP) to support SAV
   policy distribution and synchronization between PCEP speakers for
   threat mitigation for source address spoofing.
- **draft-song-tsvwg-camp-01** (new-draft, score 0, ignored_after_review) [none]: [Consistency-Aware Multipath Transport (CAMP) toward Interactive Multimodal LLM-Based Systems](https://datatracker.ietf.org/doc/draft-song-tsvwg-camp/) — With the prosperity of generative large language models (LLMs),
   interactive LLM-based services, such as digital humans, have imposed
   new stringent requirements on low latency and high multimodal
   consistency.  Traditional interactive LLM-based systems typically
   transmit multimodal content over a single network path, thereby
   failing to exploit the advantages offered by multipath networks.
   Even when multipath transport mechanisms are adopted, single-stream
   encapsulation does not enable differentiated management of
   heterogeneous modalities.  However, naively separating modalities
   into multiple streams further introduces inter-modal arrival
   inconsistency.  To address these challenges, this document specifies
   CAMP, a consistency-aware multipath transport design over the
   Multipath QUIC (MPQUIC) protocol.  First, CAMP defines a three-stream
   separation encapsulation format to support modality-differentiated
   transmission.  Second, it introduces a hierarchical multimodal data
   management mechanism to coordinate the transmission of correlated
   data across modality streams.  Third, it incorporates a transport-
   layer consistency-aware multipath scheduler to reduce inter-modal
   arrival time deviation across network paths.  Fourth, it specifies a
   client-side application-layer alignment mechanism that operates in
   coordination with the transport scheduler.  To the best of our
   knowledge, this is the first specification to address multipath-
   enabled multimodal consistency guarantees for interactive LLM-based
   systems.
- **draft-sun-single-stack-100-50** (new-draft, score 0, ignored_after_review): [draft-sun-single-stack-100-50-01](https://datatracker.ietf.org/doc/draft-sun-single-stack-100-50/)
- **draft-sun-single-stack-100-50-01** (new-draft, score 0, ignored_after_review) [none]: [The Single-Stack 100/50 Principle: Formal Definitions for IPv4 Retirement in Dual-Stack Networks](https://datatracker.ietf.org/doc/draft-sun-single-stack-100-50/) — The Single-Stack 100/50 Principle defines two independent, formally
   derivable consequences of retiring the IPv4 protocol stack in a dual-
   stack (IPv4 + IPv6) network environment: (1) 100% elimination of
   executable attacks attributable to IPv4 under the document's
   definition, and (2) an exact 50% reduction in the count of
   concurrently exposed network-layer protocol-stack surfaces when IPv4
   is retired, stated by the Principle as a minimum structural floor.
   The analysis is bounded to the functional Layer 3 scope and parameter
   universe U_3 defined in this document.  Within that premise, Axiom 0
   and Axioms 1-15 stipulate protocol independence, operational state
   transitions, traffic termination, addressing/routing domains,
   protocol-associated control and resolution functions, header-
   processing paths, and protocol-specific vulnerability execution.
   Theorem I follows by removal of the necessary IPv4 Layer 3 execution
   precondition for every IPv4-attributable attack.  Theorem II follows
   by direct enumeration of two concurrently exposed protocol-stack
   surfaces before retirement and one after retirement.  Neither theorem
   depends on empirical attack volume, incident frequency, or
   statistical inference, and neither theorem claims that IPv6 is
   inherently more secure than IPv4.
- **draft-wkumari-intarea-safe-limited-domains-07** (new-draft, score 0, ignored_after_review) [none]: [Safe(r) Limited Domains](https://datatracker.ietf.org/doc/draft-wkumari-intarea-safe-limited-domains/) — Documents describing protocols intended solely for use within
   "limited domains" often rely on edge filtering at every boundary node
   to prevent domain-internal traffic from leaking to the global
   Internet (and vice versa).  Relying purely on administrative
   filtering creates "fail-open" designs that are susceptible to
   configuration errors, ACL bypass, and hardware table exhaustion.

   This document describes design principles and concrete mechanisms
   that allow limited-domain protocols to "fail-closed" by default.  By
   leveraging Layer-2 encapsulation identifiers (such as dedicated or
   extended EtherTypes), link-local address scoping, and / or Hop-Limit
   boundaries, protocol designers can significantly reduce the
   operational and security risks associated with limited domain
   protocols.

   These mechanisms are not applicable to all protocols intended for use
   in a limited domain, but if implemented on certain classes of
   protocols, can significantly reduce the risks.
- **draft-wu-idr-flowspec-sip-community-filter-02** (new-draft, score 0, ignored_after_review) [none]: [Source-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-sip-community-filter/) — BGP Flow Specification (BGP-FS) propagates traffic Flow
   Specifications and Traffic Filtering Actions using BGP NLRI and BGP
   Extended Community encodings.  This document specifies a new BGP-FS
   component type to support community-level filtering within a single
   administrative domain.  The match condition filters traffic based on
   the BGP Community attributes associated with the route matching the
   packet's source IP address.
- **draft-xiao-fann-fast-cnp-with-proxy-03** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-xie-bess-evpn-extension-evn6-04** (new-draft, score 0, ignored_after_review) [none]: [EVPN Route Types and Procedures for EVN6](https://datatracker.ietf.org/doc/draft-xie-bess-evpn-extension-evn6/) — EVN6 is a mechanism designed to provide Ethernet connectivity to
   customer sites dispersed on public IPv6 networks.  At the data layer,
   EVN6 encapsulates Ethernet frames directly in the payload of IPv6
   packets, and dynamically generates the IPv6 addresses of the IPv6
   header using host MAC addresses and other information, then sends
   them into IPv6 network for transmission.  This document proposes
   extensions to EVPN for EVN6, including two new route types and
   related procedures.
- **draft-xu-sidrops-asrank-vulnerabilities-01** (new-draft, score 0, ignored_after_review) [none]: [Structural Vulnerabilities in ASRank under Adversarial Conditions](https://datatracker.ietf.org/doc/draft-xu-sidrops-asrank-vulnerabilities/) — This document analyzes the structural vulnerabilities of ASRank, a
   widely used algorithm for inferring Autonomous System (AS) business
   relationships from BGP routing data.  ASRank plays a key role in
   security research and BGP operation, yet its inference process is
   highly sensitive to small changes in input data.  This sensitivity
   introduces risks in adversarial conditions, where inference results
   may be manipulated without detection.  This document outlines the
   design of ASRank, identifies its structural vulnerabilities, analyzes
   a minimal manipulation example, and discusses the security
   implications and potential countermeasures.
- **draft-zhu-cats-metric-semantics-01** (new-draft, score 0, ignored_after_review) [none]: [Operational Semantics for CATS Metric Consumption](https://datatracker.ietf.org/doc/draft-zhu-cats-metric-semantics/) — The CATS framework introduces computing-related information into
   traffic steering decisions.  Existing work defines how such metrics
   are represented, distributed, and used within the CATS architecture.
   However, it does not fully address whether a metric remains suitable
   for use at the point of consumption.

   This document introduces a set of operational semantics for CATS
   metrics, including Freshness, Operational acceptability, and
   Assurance exposure.  These semantics describe whether a metric
   remains temporally aligned with the underlying condition, whether it
   remains suitable for operational use in steering, and whether
   degraded consumption is externally visible to management or OAM
   functions.

   The document further explains how these semantics apply across
   centralized, distributed, and hybrid deployments, including cases
   where different metric sources contribute under different conditions.
   The goal is to provide a consistent basis for interpreting metric
   usability in CATS without introducing a new metric level or
   prescribing a single derivation method.

   Implementations may determine when degradation occurs, while the
   resulting consumption condition can still be represented and
   understood consistently across CATS functions.

## Errors / fetch failures

- draft-sun-single-stack-100: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-sun-single-stack-100/doc.json
