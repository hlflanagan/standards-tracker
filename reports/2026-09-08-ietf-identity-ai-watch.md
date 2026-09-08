# IETF Identity + AI Standards Watch

Date: 2026-09-08

## Read now

- **draft-sato-soos-gar-08** (new-draft, score 32, trust_infrastructure) [none]: [The Governance Audit Record (GAR) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-gar/) — This document specifies the Governance Audit Record (GAR), the audit
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

   Version -08 is an editorial revision with no normative content
   changes: nine sibling-draft citations had gone stale against
   those drafts' current live versions and are updated to
   draft-sato-soos-idp-06, draft-sato-soos-hem-07,
   draft-sato-soos-cap-06, draft-sato-soos-sov-03,
   draft-sato-soos-mjwt-06, draft-sato-soos-mad-05,
   draft-sato-soos-kia-06, draft-sato-soos-cap-rrs-04, and
   draft-sato-soos-acd-02 respectively.
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
- **draft-das-rats-attestation-bnd-execution-finality-02** (new-draft, score 26, trust_infrastructure) [none]: [Attestation-Bound Execution Finality for GPU, AI Accelerator, DPU, SmartNIC, and Confidential-Computing Infrastructure](https://datatracker.ietf.org/doc/draft-das-rats-attestation-bnd-execution-finality/) — Remote attestation can establish evidence about the hardware,
   firmware, software, configuration, and execution environment
   associated with a workload.  In heterogeneous confidential-computing
   environments, this trust assessment can extend across CPUs,
   confidential virtual machines, GPUs, AI accelerators, DPUs,
   SmartNICs, and other trusted execution components.  As AI training
   and inference workloads scale onto large fleets of GPUs and other
   accelerators, and as confidential-computing modes for those
   accelerators reach production deployment, the boundary between "the
   environment is trustworthy" and "this specific operation may proceed"
   becomes an increasingly consequential, and increasingly load-bearing,
   engineering question.

   An increasingly important class of workloads, however, does not
   merely compute data.  AI agents and autonomous workloads can generate
   consequential operations such as API invocations, storage mutations,
   network configuration changes, infrastructure-control commands,
   financial instructions, device operations, and cross-workload
   requests.  These operations are typically issued from, or on behalf
   of, GPU- and accelerator-hosted workloads, so the architecture is
   directly relevant to any infrastructure operator or hardware, DPU,
   SmartNIC, or confidential-computing vendor whose platform
   participates in generating, attesting, or effectuating such
   operations.

   This document is intended to be of particular interest to
   organizations building or operating large-scale confidential AI
   accelerator infrastructure, including GPU vendors, cloud and
   hyperscale operators, DPU and SmartNIC vendors, and confidential-
   computing platform providers, since the accompanying reference
   implementation and FAQ discussion (Section 34.8, Appendix C)
   illustrate the architecture using publicly documented attestation
   stacks such as NVIDIA's Confidential Computing and Attestation Suite
   (NRAS, RIM Service, and OCSP Service) alongside Intel Trust Domain
   Extensions (TDX) plus confidential-GPU composite attestation.  These
   vendors and products are cited only as concrete, checkable, publicly
   documented examples of the class of infrastructure the architecture
   addresses; this document is vendor-neutral, does not depend on any
   specific vendor's hardware or software, and neither claims nor
   implies review, adoption, endorsement, or affiliation by NVIDIA,
   Intel, or any other named vendor.

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
- **draft-sato-soos-kia-07** (new-draft, score 26, core_identity) [none]: [Kernel Identity and Attestation for Governing Enforcement Components](https://datatracker.ietf.org/doc/draft-sato-soos-kia/) — This document specifies the Kernel Identity and Attestation (KIA)
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

   Version -07 is an editorial revision with no normative content
   changes: sibling-draft citations had gone stale against those
   drafts' current live versions and are updated to
   draft-sato-soos-cap-06, draft-sato-soos-gar-08,
   draft-sato-soos-mad-05, draft-sato-soos-mjwt-06, and
   draft-sato-soos-idp-06; the companion-drafts discussion's HEM
   and AEP mentions are similarly updated to hem-07 and aep-04.
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
- **draft-sato-soos-mjwt-06** (new-draft, score 24, agent_identity) [none]: [The Mandate JWT (MJWT) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/) — An AI agent that can act without a verifiable, human-traceable
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

   Version -06 is an editorial revision with no normative content
   changes: six sibling-draft citations (HEM, CAP, KIA, MAD, AEP,
   IDP) had gone stale against those drafts' current live versions
   and are updated to draft-sato-soos-hem-07, draft-sato-soos-cap-06,
   draft-sato-soos-kia-06, draft-sato-soos-mad-04,
   draft-sato-soos-aep-04, and draft-sato-soos-idp-06 respectively.
- **draft-wei-aic-jwt-01** (new-draft, score 23, authorization) [none]: [AI Agent Identity Certificate (AIC) JSON Web Token Profile](https://datatracker.ietf.org/doc/draft-wei-aic-jwt/) — The AI Agent Identity Certificate (AIC) defines a data model in which
   the cryptographic identity of an AI agent is bound to a responsible
   principal, together with a structured capability container,
   delegation mode, authorization constraints, and principal-signed
   delegation evidence.  The normative definition of this model is
   specified by the AIC specification, where it is encoded in ASN.1 and
   carried in X.509 certificates, enabling authorization decisions at
   the transport layer, including fully offline operation.

   Many HTTP, web, and OAuth 2.0 (RFC 6749) deployments cannot present
   X.509 certificates at the transport layer.  This document therefore
   defines AIC-JWT as a JWT-based application-layer representation of
   the AIC data model defined by the AIC specification.  AIC-JWT is a
   companion representation, not a replacement for the X.509 form and
   not a new authorization model.

   AIC-JWT uses the standard JWT (RFC 7519) and JWS (RFC 7515)
   mechanisms as its carrier and cryptographic envelope.  Its
   authorization semantics are inherited from the AIC model rather than
   defined by JWT or OAuth.  In particular, the outer AIC-JWT is issuer-
   signed and carries the principal-signed DA JWT as the value of the
   top-level da claim, preserving the two-layer signature model of AIC.

   The normative content of this document is limited to:

   *  a mapping from the X.509 AIC extension fields to JWT claims that
      preserves the AIC data model and its two-layer signature model;

   *  representation and key-binding rules for the principal-signed
      DelegationAuthorization;

   *  validation rules for AIC-JWT, including claim consistency,
      audience, and key-binding checks; and
   *  a thin OAuth 2.0 consumption profile defining presentation of the
      DA at a token endpoint as an RFC 7523 JWT bearer authorization
      grant and the projection of the AIC authorized and representative
      delegation modes into OAuth roles.
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
- **draft-reilly-rlt-genesis-02** (new-draft, score 22, trust_infrastructure) [none]: [REM License Token (RLT) - Genesis Artifact](https://datatracker.ietf.org/doc/draft-reilly-rlt-genesis/) — This document defines the REM License Token, referred to as the RLT,
   as the genesis artifact of the Reilly EternaMark Protocol (REM) for
   digital permanence and verifiable provenance.  This specification
   formally defines the token structure, issuance procedures,
   multi-algorithm cryptographic hash requirements, blockchain anchoring
   requirements, DOI archival requirements, IPFS pinning requirements,
   REMID namespace registration, verification methodology, token
   lifecycle management, ecosystem integration, and security model.

   The RLT represents an implementation of a Dual-Layer Digital
   Permanence artifact combining a Bitcoin blockchain timestamp with
   DOI-based archival to achieve durable, tamper-evident provenance
   guarantees.  Revision -01 expanded the token schema to version 2.0,
   introduced multi-algorithm hashing via the REM Multi-Algorithm Stack
   (REM-MAS), defined formal token lifecycle procedures, and documented
   the RLT's integration with the broader REM Protocol ecosystem
   including the Protocol Layer Prompt Engineering Specification
   (PLPES), the Cognitive Trust Stack (CTS), the AI Machine-Readable
   Ethics Directive (AIMED), and related Informational Internet-Drafts
   authored by Lawrence John Reilly Jr.

   This revision (-02) is additive.  It retains the whole of the -01
   specification and adds token schema version 2.1, a canonical form
   and record digest for token self-integrity, salted field
   commitments with selective disclosure, a COSE signature profile,
   batch issuance with Merkle aggregation, pending and attested anchor
   states, hash migration bridging records, conformance levels C0
   through C4, status records and a revocation registry, an anchor
   scope rule, the prior art record function under 35 U.S.C. 102(a)(1),
   and further ecosystem, privacy, and evidentiary considerations.

   This document is published as an Informational Internet-Draft to
   serve as open, implementable guidance.
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
- **draft-howard-virp-07** (new-draft, score 20, core_identity) [none]: [VIRP: Verified Infrastructure Response Protocol](https://datatracker.ietf.org/doc/draft-howard-virp/) — The Verified Infrastructure Response Protocol (VIRP) defines a trust
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
   (Section 18).

   This revision adds External Authorization Binding (Section 11): a
   deployment profile in which the gate holds only a read-only device
   identity, the write credential is never at rest on the gate, and per-
   command authorization is performed by an authorization service that
   the gate does not control, using the device's own authorization
   mechanism (for example TACACS+ command authorization [RFC8907] on IOS
   and IOS-XE).  The gate's own record of an action is then reconciled
   against the device's independent accounting under the same public
   verification tooling.  The individual mechanisms are long-standing;
   the contribution is their composition, with an autonomous or
   automated requester as the constrained principal, together with an
   evidence layer that enables the gate's account of an action to be
   reconciled against the device's independently sourced account of the
   same action so a third party can compare them.  Static per-command
   authorization and reconciliation are implemented and exercised on
   production Cisco hardware; approval-scoped dynamic grants and the
   chaining of authorization decisions are specified and marked as not
   yet implemented (Section 19).

   Since draft-howard-virp-06 the reference chain implementation has
   gained an OPTIONAL per-entry and per-head Ed25519 signature, computed
   by the daemon at append time over the same canonical bytes as the
   mandatory HMAC and verifiable from a public key alone.  It is enabled
   per node and is off by default, so a conforming deployment may still
   be HMAC-only.  The base chain-integrity guarantee remains the
   symmetric one described here; the signature is an additional
   authenticator, described in Section 6.5 and Section 6.5.2, not a
   replacement for it.
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
- **draft-sato-soos-rgp-02** (new-draft, score 20, agent_identity) [none]: [The Resource Governance Protocol (RGP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-rgp/) — An AI agent that can act on resources cannot be governed unless
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

   Version -02 is an editorial revision with no normative content
   changes: KEE-1 citations were migrated from the versioned
   [I-D.sato-soos-kee] form to the non-versioned [SOOS-KEE] form,
   since KEE-1 is a permanent local-only specification that will
   never be submitted to the IETF Datatracker.
- **draft-sato-soos-sov-04** (new-draft, score 20, agent_identity) [none]: [The Sovereign Object (SOV) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-sov/) — When an AI agent acts on your behalf, it acts on something: a
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
- **draft-sharif-agent-audit-trail-03** (new-draft, score 20, trust_infrastructure) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
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

   This revision (-03) adds the Attestation Closure requirement
   (Section 13.6): the digests recorded for decision
   reproducibility MUST cover the complete computational closure
   of the inference function -- model weights, tokenizer, chat
   template, inference engine build, decoding configuration, and
   numeric environment -- together with new record fields
   (tokenizer_digest, chat_template_digest, engine_build_digest)
   and a minimal-change threat analysis (Section 13.7) showing
   that any component left outside the attested set is a forgery
   channel.
- **draft-das-6g-query-scoped-communication-handles-06** (new-draft, score 19, core_identity) [none]: [6G-Era Communication Authorization-to-Reach: Separating Identifier Possession from Permission to Contact](https://datatracker.ietf.org/doc/draft-das-6g-query-scoped-communication-handles/) — Many Internet and telephone communication systems treat possession of
   a routable identifier as sufficient to attempt contact.  A telephone
   number, SIP URI, messaging handle, relay address, or marketplace
   contact reference can therefore remain a reusable reachability path
   after the purpose of disclosure has ended.

   Existing IETF and industry mechanisms solve related but different
   problems.  STIR and SHAKEN authenticate or attest originating
   identity: they answer whether the calling party is who it claims to
   be, not whether that authenticated party currently holds bounded,
   purpose-scoped, revocable permission to reach a particular recipient.
   Virtual or masked numbers hide a persistent endpoint but commonly
   leave a substitute route active while the alias is valid.  OAuth can
   express delegated API authorization.  Spam scoring and call screening
   classify or reject an attempt after some path already exists.

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
   on SIP, STIR, messaging, and Internet communication identifiers.  The
   motivation is nonetheless sharpened by the trajectory of upcoming 6G
   and IMT-2030 network infrastructure: as networks move toward AI-
   native architectures in which software agents, network functions, and
   third-party AI systems can originate signaling at machine speed, and
   as vendors including Qualcomm and Huawei publish AI-native 6G radio-
   and core-network research, an authorization-to-reach gap that is
   tolerable at human-initiated call volumes becomes structurally more
   significant at machine-originated volumes.  Global telecom operators
   such as Deutsche Telekom, Orange, AT&T, and Vodafone -- among the
   carriers with the largest exposure to SIP, STIR/SHAKEN, and voice-
   messaging signaling volumes -- are named here only as illustrative
   examples of the operator community for whom an interoperable
   authorization-to-reach answer would be most directly relevant.  This
   document does not depend on any particular 6G, IMT-2030, Qualcomm,
   Huawei, Deutsche Telekom, Orange, AT&T, or Vodafone architecture,
   deployment, or product, and does not assert that any of them has
   adopted, evaluated, or endorsed this proposal; it identifies why
   telecom infrastructure evolution makes the underlying Internet-
   identifier-layer question more urgent for IETF to consider now rather
   than after machine-scale traffic arrives.

   Google Maps, Apple Maps, and social or commerce platforms with map-
   adjacent or messaging-based business discovery features such as Meta
   Business (including Facebook and Instagram business discovery and
   messaging) are referenced elsewhere in this document family as
   recognizable illustrative examples of where a visible communication
   handle is exposed after discovery; no affiliation, endorsement,
   implementation, adoption, or technical alignment by Google, Apple,
   Meta, Qualcomm, Huawei, Deutsche Telekom, Orange, AT&T, Vodafone, or
   any other named provider is implied by this document.
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
- **draft-das-rats-frontier-model-extraction-03** (new-draft, score 18, trust_infrastructure) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive Frontier AI Model Information](https://datatracker.ietf.org/doc/draft-das-rats-frontier-model-extraction/) — Frontier and proprietary AI deployments may contain or expose model-
   related information substantially richer than ordinary final-answer
   text.  Depending on the deployment and interface, such Sensitive
   Model Information (SMI) can include detailed probability information,
   embeddings, cached intermediate state, hidden representations,
   intermediate activations, diagnostic information, model-related
   metadata, or other high-information artifacts.  Repeated unauthorized
   or excessive release of such information can increase the efficiency
   of model reconstruction, imitation, extraction, or distillation.

   Authentication establishes who is requesting an operation.
   Confidential computing and remote attestation can establish
   properties of the environment in which computation occurs.  Neither
   property alone determines whether a particular pending release of
   particular model information, to a particular destination, under the
   current extraction state and security epoch, remains authorized to
   become externally usable.

   This document describes an execution-finality architecture for that
   remaining problem.  Sensitive information may be computed while
   remaining a non-effective Candidate Release.  External release occurs
   only after release-specific protected validation, evaluation of
   rollback-resistant extraction state where required, atomic
   reservation or consumption of bounded authority, and verification at
   a controlled Finality Sink.  Release authority is bound to the
   applicable Candidate Release or bounded release class rather than
   operating as a generic transferable bearer credential.

   The architecture does not claim universal prevention of model
   extraction or distillation and does not restrict legitimately exposed
   ordinary model output.  Its narrower objective is to make
   unauthorized, excessive, replayed, rolled-back, or bypassed release
   of protected model information technically harder to complete through
   governed release paths.  RATS can complement this mechanism by
   allowing a Verifier or Relying Party to obtain machine-verifiable
   information about whether the expected release-control mechanism,
   protected state, security epoch, and Finality Sink are present and
   operating with the required assurance properties.
- **draft-das-rats-openai-anthropic-extraction-02** (new-draft, score 18, trust_infrastructure) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive OpenAI and Anthropic Claude Model Information](https://datatracker.ietf.org/doc/draft-das-rats-openai-anthropic-extraction/) — Frontier and proprietary AI deployments may contain or expose model-
   related information substantially richer than ordinary final-answer
   text.  Depending on the deployment and interface, such Sensitive
   Model Information (SMI) can include detailed probability information,
   embeddings, cached intermediate state, hidden representations,
   intermediate activations, diagnostic information, model-related
   metadata, or other high-information artifacts.  Repeated unauthorized
   or excessive release of such information can increase the efficiency
   of model reconstruction, imitation, extraction, or distillation.

   Authentication establishes who is requesting an operation.
   Confidential computing and remote attestation can establish
   properties of the environment in which computation occurs.  Neither
   property alone determines whether a particular pending release of
   particular model information, to a particular destination, under the
   current extraction state and security epoch, remains authorized to
   become externally usable.

   This document describes an execution-finality architecture for that
   remaining problem.  Sensitive information may be computed while
   remaining a non-effective Candidate Release.  External release occurs
   only after release-specific protected validation, evaluation of
   rollback-resistant extraction state where required, atomic
   reservation or consumption of bounded authority, and verification at
   a controlled Finality Sink.  Release authority is bound to the
   applicable Candidate Release or bounded release class rather than
   operating as a generic transferable bearer credential.

   The architecture does not claim universal prevention of model
   extraction or distillation and does not restrict legitimately exposed
   ordinary model output.  Its narrower objective is to make
   unauthorized, excessive, replayed, rolled-back, or bypassed release
   of protected model information technically harder to complete through
   governed release paths.  RATS can complement this mechanism by
   allowing a Verifier or Relying Party to obtain machine-verifiable
   information about whether the expected release-control mechanism,
   protected state, security epoch, and Finality Sink are present and
   operating with the required assurance properties.
- **draft-sato-soos-pt-04** (new-draft, score 18, agent_identity) [none]: [Progressive Trust (PT) for Agentic AI Governance Systems](https://datatracker.ietf.org/doc/draft-sato-soos-pt/) — When a new employee joins an organization, they begin with limited
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

   Version -04 is an editorial revision with no normative content
   changes: the FAIP citation was migrated from the versioned
   [I-D.sato-soos-faip] form to the non-versioned [SOOS-FAIP] form,
   since FAIP is a Class B specification that will not be submitted
   to the IETF Datatracker.
- **draft-schrock-ep-architecture-03** (new-draft, score 18, core_identity) [none]: [The EMILIA Protocol: An Evidence Architecture for Consequential Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-architecture/) — Consequential agent actions can cross operator and administrative
   boundaries.  The party that later decides whether to rely on an
   action record may not have participated in the interaction and may
   not trust either operator.  This document describes an evidence
   architecture for that case.  It separates transport and workload
   identity, delegation and policy, material action identity,
   authorization evidence, evidence satisfaction, local authorization,
   durable consumption or reservation, effect invocation, outcome
   evidence, revocation, and preservation.

   The architecture composes the Canonical Action Identifier (CAID),
   Authorization Evidence Chain (AEC), and Action Evidence Boundary
   (AEB) with optional staged-approval and consequence-control profiles.
   It does not define a universal token, policy language, execution
   engine, settlement network, or distributed consensus system.  A valid
   signature, a current credential, a satisfied evidence requirement,
   and an observed effect remain different facts.
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
- **draft-jovancevic-saip-11** (new-draft, score 17, core_identity) [none]: [SAIP: Signed Agent Identity Protocol](https://datatracker.ietf.org/doc/draft-jovancevic-saip/) — The modern internet lacks a reliable mechanism for verifying the
   identity of automated software agents. Existing methods such as
   User-Agent strings and IP-based attribution are insufficient due to
   spoofing, shared infrastructure (NAT), and the rapid growth of
   automated agents including AI crawlers, IoT devices, and enterprise
   automation systems.

   This document specifies SAIP (Signed Agent Identity Protocol), a
   lightweight, opt-in mechanism for verifiable client identity at the
   application layer. SAIP implements the principles defined in the
   Verifiable Identity Claims and Delegation Model [VICDM] and enables
   servers to distinguish legitimate automated traffic from malicious
   actors through cryptographic identity at three levels of granularity:
   vendor, agent type, and individual instance.

   SAIP is protocol-agnostic and applicable to HTTP, SMTP, and other
   header-based protocols. It introduces DNS-based Attestation
   Discovery as
   a lightweight alternative to registry-based key lookup, making
   deployment accessible to organizations of any size.
- **draft-kroehl-agentic-trust-aae-02** (new-draft, score 17, authorization) [none]: [Agent Authorization Envelope (AAE): A Machine-Evaluable Authorization Structure for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/) — Autonomous AI agents now operate at production scale across
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
- **draft-kuehlewind-audit-architecture-01** (new-draft, score 17, trust_infrastructure) [none]: [An Architecture for Auditing Agent Delegation and Interactions](https://datatracker.ietf.org/doc/draft-kuehlewind-audit-architecture/) — This document describes an architecture for auditing of agent-driven
   interactions on the Internet.  Autonomous and semi-autonomous
   software agents, including those based on artificial intelligence,
   increasingly act on behalf of users, organizations, and services.
   Existing auditing mechanisms often capture isolated system events but
   do not consistently represent delegation relationships, user intent,
   or evolving authorization.  In agent-driven systems, auditability
   requires linking intent, delegation, authorization, and execution.
   The proposed architecture enables this through distributed audit
   record generation, propagation of audit context, optional
   attestation, and additional logging for transparency.
- **draft-sato-soos-acd-03** (new-draft, score 17, agent_identity) [none]: [The Agent Compliance Disclosure (ACD) Protocol for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-acd/) — A regulated resource provider -- a bank, a government API, a
   healthcare records system -- receives a request from an AI agent.
   The agent claims to operate under a constitutional compliance policy
   and a valid mandate.  The resource provider has no mechanism to
   verify these claims.  Without a machine-verifiable compliance
   disclosure, the resource provider cannot confirm the agent's
   governing law, its active prohibition set, its audit trail
   reference, or its principal hierarchy -- before granting access.

   This document defines the Agent Compliance Disclosure (ACD)
   Protocol: a machine-to-machine compliance handshake that must
   complete before an AI agent is granted access to a regulated
   resource class.  ACD defines the ACD Record schema (a three-layer
   structured disclosure produced by the SOOS kernel, covering legal
   identity, constitutional compliance, and principal hierarchy), the
   ACD Presentation Protocol (the query/response exchange between a
   resource provider and the SOOS kernel), the ACD Trust Hierarchy
   (operator-declared trust levels and Audit Principal credentials),
   the ACD-to-MJWT binding (ACD MUST reference the session MJWT jti),
   and the GAR integration (ACD presentation events as Authority
   Lifecycle Events).  ACD Records are produced exclusively by the
   Governing Enforcement Component (GEC), signed by the kernel's KIA
   private key, and logged in the Governance Audit Record (GAR).  LLM
   self-report of compliance posture is architecturally insufficient
   and MUST NOT be used as an ACD disclosure surface.

   ACD is the inbound complement to the Resource Governance Protocol
   (RGP): where RGP governs outbound capability discovery, ACD governs
   inbound compliance verification.  Together they define the complete
   resource access governance flow for SOOS-governed agents.

   Version -02 added the aep_session_id Layer 3 field, distinct from
   acd_session_id, to bind a cached ACD Record to the specific AEP
   session it was produced within (Section 6.3); strengthened the
   ACD Record Replay defense that checks this binding from a SHOULD
   to a MUST (Section 12.4); added the confirmation_basis field
   (NOTIFIED | INFERRED) to ALE-058 so an auditor can distinguish a
   confirmed validation pass from one merely inferred from the
   absence of a failure record (Section 10.1); added Compliance
   Handshake Volumetric Abuse as a new security consideration
   (Section 12.5); and migrated the KEE-1 citation from the versioned
   [I-D.sato-soos-kee] form to the non-versioned [SOOS-KEE] form,
   since KEE-1 is a permanent local-only specification that will
   never be submitted to the IETF Datatracker.

   Version -03 is an editorial revision with no normative content
   changes: six sibling-draft citations in Section 15.1 had gone
   stale against those drafts' current live versions and are updated
   to draft-sato-soos-aep-04, draft-sato-soos-gar-08,
   draft-sato-soos-kia-07, draft-sato-soos-mjwt-06,
   draft-sato-soos-rgp-02, and draft-sato-soos-sov-04 respectively;
   and the Table of Contents, which omitted Section 12.5 from -02's
   submission, now lists it correctly.
- **draft-schrock-ep-authorization-evidence-chain-06** (new-draft, score 17, authorization) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
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
- **draft-watts-ai-identity-conformance-00** (new-draft, score 17, trust_infrastructure) [none]: [AID-1 Provider-Independent Conformance Requirements and Test-Vector Model](https://datatracker.ietf.org/doc/draft-watts-ai-identity-conformance/) — This document defines provider-independent conformance requirements
   for AID-1.  It specifies the execution model for a deterministic
   machine-readable test-vector corpus, including canonicalization,
   cryptographic, identity-binding, delegation, authorization, temporal,
   revocation, replay, attestation, provenance, and integration cases.
   The conformance corpus contains 69 vectors.  Six replay cases are
   architectural boundary tests, including R5, which requires AID-1
   verification to succeed while a downstream D6 scientific-
   admissibility decision rejects the same evidence.
- **draft-mih-sokolov-scitt-payload-binding-03** (new-draft, score 16, trust_infrastructure) [none]: [Canonical Payload Binding: A Signed Statement Construction Profile](https://datatracker.ietf.org/doc/draft-mih-sokolov-scitt-payload-binding/) — Independently written systems that anchor records to a SCITT
   Transparency Service repeatedly need the same construction: a
   canonical form of structured content, a content-addressed identifier
   derived from that form, binding to a SCITT Signed Statement and
   Receipt, and references that cite external artifacts by digest.  This
   document defines that construction as the Canonical Payload Binding
   (CPB).  A payload profile declares its canonicalization algorithm and
   exclusion set and thereby obtains a reproducible derived identifier.
   A CPB Signed Statement carries either the complete statement content
   as specified by RFC 9943 or a digest of content held elsewhere using
   the COSE Hash Envelope of RFC 9995.  CPB also defines an abstract
   typed digest reference information model and one optional protected-
   header encoding, cpb-refs; a payload profile may instead define its
   own reference serialization.  An IANA registry governs CPB
   canonicalization algorithms.  CPB does not define payload content
   formats, establish or require a universal artifact-type registry, or
   require either typed-reference carrier.
- **draft-bubblefish-naalp-01** (new-draft, score 15, core_identity) [none]: [N-AALP: The Native Agentic Application Layer Protocol](https://datatracker.ietf.org/doc/draft-bubblefish-naalp/) — The Native Agentic Application Layer Protocol (N-AALP) is an
   application-layer object protocol for autonomous software agents.
   Every N-AALP object is a deterministically encoded CBOR structure
   signed with COSE, carrying under one signature its content identity,
   its originating signer, a closed effect label that is an
   authorization input rather than a hint, optional approval and audit
   bindings, and its causal derivation.  Objects are transport-
   independent: the identical signed object is carried, with identical
   object-level guarantees, over the N-PAMP substrate, QUIC, WebSocket,
   or HTTP.  N-AALP defines a frozen envelope, a post-quantum signature
   profile (pure ML-DSA by default, with an optional Ed25519+ML-DSA
   composite), a self-certifying identity with key rotation, a single-
   use approval ledger, a hash-chained audit and causal- ordering model
   with a federated higher tier, native streaming with a single per-
   stream commitment, foreign-protocol carriage by class, and twenty
   tiered channel surfaces.  This document is an Independent Submission
   and does not represent IETF consensus.
- **draft-dua-scsp-space-uri-00** (new-draft, score 15, core_identity) [none]: [The 'scsp' Uniform Resource Identifier (URI) Scheme and Space Command & Telemetry Security Protocol (SCSP)](https://datatracker.ietf.org/doc/draft-dua-scsp-space-uri/) — This document specifies the 'scsp' Uniform Resource Identifier (URI)
   scheme and its associated Space Command & Telemetry Security Protocol
   (SCSP).  The scheme defines a zero-trust, transport-agnostic space
   cybersecurity protocol standardizing telecommand authentication,
   telemetry integrity, inter-satellite laser mesh encryption, and
   optional profile-driven space-grade hardware attestation (TPM 2.0 /
   TEE) across Low-Earth Orbit (LEO) constellations, Geostationary (GEO)
   satellites, and Deep-Space missions.  It defines exact binary field-
   width tables in Network Byte Order (Big-Endian) with O(1) KeyID
   indexing, reserved KeyID 0x0000 Master Emergency slots, 11-bit CCSDS
   APID zero-padding constraints, normative DMA buffer sizing (B_min >=
   26 + N_max + SigLen_max), AEAD cipher agility, deterministic 96-bit
   IV construction (Sequence_Epoch || KeyID || 0x0000), continuous
   International Atomic Time (TAI) microsecond epoch baselines, zero-
   payload (N=0) boundary rules, ISL TTL hop limiting, a mission-
   provisioned Endpoint Resolution Table mapping URIs to CCSDS
   Spacecraft ID (SCID), Virtual Channel ID (VCID), and Application
   Process ID (APID) parameters, ground-side URI :port stripping rules,
   mandatory signature byte-scoping over header and payload, normative
   X25519 HKDF info strings for AEAD key derivation ("SCSP-Payload-AEAD-
   v1") and non-interactive TC segment HMAC trailers ("SCSP-Segment-
   HMAC-v1") with 32-zero-byte RFC 5869 salts, 3,378-byte hybrid PQC
   signature sub-framing (Ed25519 + ML-DSA-65 per FIPS 204), KeyID-
   isolated configurable-width (64/256/1024-bit) NVRAM sliding-window
   anti-replay protection, monotonic NVRAM counter-protected Emergency
   Time-Resynchronization, monotonic counter-protected in-pass Key
   Revocation Lists (KRL), dual-mode SDLS SPI/ESH Extended Security
   Headers (SA Table Index vs. Direct Bitfield), I-JSON compliant
   payload documents (RFC 7493), onboard Command Authorization Policy
   Matrices, mandatory signed Telemetry Response schemas for SUCCESS and
   ERROR states (0x01..0x0C), SCSP URI canonicalization, and provisional
   IANA registration under RFC 7595.
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
- **draft-sato-soos-aep-04** (new-draft, score 15, agent_identity) [none]: [The Agent Execution Protocol (AEP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-aep/) — An AI agent that can act cannot be governed unless there is a
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

   Version -04 is an editorial revision with no normative content
   changes: the KEE-1 citation was migrated from the versioned
   [I-D.sato-soos-kee] form to the non-versioned [SOOS-KEE] form,
   since KEE-1 is a permanent local-only specification that will
   never be submitted to the IETF Datatracker.
- **draft-sato-soos-aop-03** (new-draft, score 15, agent_identity) [none]: [The Agent Orchestration Protocol (AOP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-aop/) — A single AI agent acting within a governed session is not the
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

   Version -03 is an editorial revision with no normative content
   changes: KEE-1 citations were migrated from the versioned
   [I-D.sato-soos-kee] form to the non-versioned [SOOS-KEE] form,
   since KEE-1 is a permanent local-only specification that will
   never be submitted to the IETF Datatracker; and three sibling-
   draft citations (HEM, CAP, CAP-RRS) had gone stale against those
   drafts' current live versions and are updated to
   draft-sato-soos-hem-07, draft-sato-soos-cap-06, and
   draft-sato-soos-cap-rrs-04 respectively.
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
- **draft-das-map-discovery-communication-finality-01** (new-draft, score 14, core_identity) [none]: [Privacy-by-Design Architecture for Map-Based Business Discovery Using Query-Scoped Non-Bearer Authorization](https://datatracker.ietf.org/doc/draft-das-map-discovery-communication-finality/) — Map-based discovery systems can help a person identify nearby
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
   for initial deployment.  Google Maps, Apple Maps, mobile operating-
   system discovery surfaces such as iOS and Android, and social and
   commerce platforms with map-adjacent or messaging-based business
   discovery features such as Meta Business (including Facebook and
   Instagram business discovery and messaging) are used as recognizable
   illustrative examples; no affiliation, endorsement, implementation,
   adoption, or technical alignment by Google, Apple, Meta, or any other
   named provider is implied.

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
- **draft-dogru-cedulon-09** (new-draft, score 14, verifiable_claims) [none]: [Cedulon: An Audit Layer for Agent-to-Agent Commerce](https://datatracker.ietf.org/doc/draft-dogru-cedulon/) — This document defines the Cedulon Protocol, an audit layer for agent-
   to-agent commerce.  Payment rails such as HTTP 402 flows (x402) and
   mandate protocols (AP2) already move value, and a mandate protocol
   can already refuse a spend before it happens.  What they do not, by
   themselves, give a party that is neither payer nor rail operator is a
   retrievable record of that decision and a signed spend receipt that
   reconciles against an authenticated extract of the rail.  Cedulon
   specifies a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), epoch checkpoints, and rail-
   extract reconciliation.

   The reconciliation shows that no settlement on the extract lacks a
   receipt and no settled receipt is absent from the extract.  That
   result is unconditional only when the verifier pins the rail key out
   of band and names the account, rail and window under audit; otherwise
   it is reported as conditional.  Checkpoints are profiled as SCITT
   Signed Statements, and a checkpoint the presented chain omits is
   reported by a witness that holds it.  No signed object is attested by
   a key it carries itself, and the exact input to every hash-valued
   field is stated, so that an independent verifier can be written from
   the text alone.  Cedulon is not a competitor to x402 or AP2; it sits
   above them.
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
- **draft-reilly-rmrp-01** (new-draft, score 14, trust_infrastructure) [none]: [Reilly Model Routing Protocol (RMRP): A Framework for Policy-Governed, Auditable AI Model Routing](https://datatracker.ietf.org/doc/draft-reilly-rmrp/) — This document specifies the Reilly Model Routing Protocol (RMRP),
   a framework for policy-governed, auditable routing of inference
   requests across heterogeneous artificial intelligence (AI) model
   environments. RMRP defines the structural metadata, routing policy
   declaration, execution semantics, audit trail requirements, and cost
   attribution mechanisms necessary to govern how inference requests are
   directed to AI models in multi-model deployments.

   The protocol is AI-provider agnostic and operates independently of
   any specific model architecture, inference runtime, vendor
   implementation, or transport layer. RMRP addresses the absence of a
   standardized protocol-layer specification governing how routing
   decisions are declared, transmitted, logged, and enforced across
   AI model deployments at organizational scale.

   This revision is additive with respect to draft-reilly-rmrp-00.
   Every structure, field, value, and requirement defined in -00 is
   carried forward unchanged. This revision adds record
   canonicalization, digest, and signature mechanisms; salted field
   commitments and selective disclosure; complexity score attestation;
   chain-level and window-level budget enforcement; audit inclusion
   proofs, checkpoints, and completeness attestation; policy and key
   revocation; a threat model; conformance levels; and IANA registries
   for the extensible value sets that -00 defined without one.
- **draft-sato-soos-idp-06** (new-draft, score 14, agent_identity) [none]: [The Intent Declaration Primitive (IDP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-idp/) — Every action an AI agent takes is a decision.  Right now, none of
   those decisions are signed.

   AI agents operating in automated workflows take actions without any
   normative mechanism for expressing why those actions are being taken.
   Access tokens declare what an agent is permitted to do; no existing
   standard declares what the agent believes it is doing, on what
   reasoning basis, and with what level of confidence, at the moment of
   action.  This document defines the Intent Declaration Primitive
   (IDP): a structured per-transition declaration submitted by an AI
   agent to the Governing Enforcement Component (GEC) at each action
   step of an execution loop.  The IDP is committed to a tamper-evident
   Event Log before the action executes, enabling post-hoc review of
   agent reasoning, richer authorization policy evaluation, and enriched
   denial responses that guide agent behaviour.  The IDP also provides
   the technical basis for compliance with EU AI Act Article 12 logging
   requirements for high-risk AI systems.

   Version -05 adds: the intake_endorsement operation through which the
   GEC endorses a submitted EOD before the first SENSE delivery, making
   the EOD a GEC-signed artifact and preventing unendorsed IDPs from
   proceeding; the PD-EOD (Prompt-Derived EOD) branch for IDPs derived
   from natural-language prompts rather than structured input, with
   scope-bounding rules and HEM notification requirements; the
   mandate_reference field linking each IDP to an SPO URI for structural
   validation; confidence_level calibration guidance including the
   CONFIDENCE_MISCALIBRATION_WARNING trigger; RETRY_CONTINUATION
   normative strengthening with backward reference to AEP-03's
   what_changed requirement; and four new Security Considerations
   addressing prompt injection at intake, EOD scope manipulation,
   confidence_level inflation attacks, and COMMITMENT_GAP exploitation.

   Version -06 is an editorial revision with no normative content
   changes: bracket-delimited array type notation ([string], [object])
   was reworded to string[]/object[] to resolve idnits parser
   warnings; sibling-draft citations were updated to each draft's
   current live version (AEP-03, HEM-07, KIA-06, GAR-07, PT-03,
   MAD-04); and several long lines were rewrapped.
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
- **draft-kanojia-creduent-agent-uri-00** (new-draft, score 12, core_identity) [none]: [The 'agent' Uniform Resource Identifier (URI) Scheme and Cryptographic Attestation Protocol](https://datatracker.ietf.org/doc/draft-kanojia-creduent-agent-uri/) — This document specifies the 'agent' Uniform Resource Identifier (URI)
   scheme and its associated cryptographic attestation protocol.  The
   'agent' scheme defines a transport-agnostic, cryptographically
   verifiable addressing layer for identifying autonomous software
   agents, binding domain ownership via DNS TXT records, enforcing
   instruction integrity, and validating attenuated capability
   delegation tokens.
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
- **draft-das-child-safe-rendering-finality-04** (new-draft, score 11, core_identity) [none]: [Preventing Unauthorized Adult and Age-Restricted Content Rendering to Children Through Hardware-Rooted Execution Finality](https://datatracker.ietf.org/doc/draft-das-child-safe-rendering-finality/) — Online child-safety controls commonly operate before the final
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
- **draft-sato-soos-dam-01** (new-draft, score 11, agent_identity) [none]: [The Data Artifact Management (DAM) Protocol for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-dam/) — This document specifies the Data Artifact Management (DAM) protocol
   for agentic AI systems governed by the Sovereign Object OS (SOOS)
   framework.  DAM defines a typed taxonomy of data artifacts produced
   and consumed by AI agents, a governance envelope for each artifact
   type specifying provenance, access policy, temporal validity, and
   retention requirements, and the normative interface between agent-
   generated artifacts and the Governance Audit Record (GAR).

   DAM addresses three classes of data in agentic systems: kernel-
   generated artifacts (IDP event logs, GAR records, AEP session state),
   agent-generated artifacts (outputs of agent actions), and externally
   ingested artifacts (data made available by resources).  DAM specifies
   the Data Artifact type (DA-Type) taxonomy referenced in the Resource
   Governance Protocol (RGP) and the Agent Execution Protocol (AEP).
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
- **draft-das-enterprise-ai-output-finality-02** (new-draft, score 10, authorization) [none]: [A Compromised AI Server Must Not Become a Map of the Enterprise: Non-Joinable Vaults and Output-Release Finality](https://datatracker.ietf.org/doc/draft-das-enterprise-ai-output-finality/) — This document specifies an architectural framework and metadata
   profile to mitigate "enterprise-future reconstruction" risks in
   multi-system Artificial Intelligence (AI) workloads.  Traditional
   access controls fail when an AI environment correlates independently
   authorized, disjointed data fragments to infer unrecorded strategic
   intent.  This profile introduces two protocol mechanisms: Technical
   Non-Joinability, enforced via a session-bound Reconstruction
   Authorization Object (RAO) that limits relational data binding, and
   Technical Non-Completability, enforced via an Output Release Boundary
   that requires verifiable validation evidence before an AI token or
   tool invocation can achieve external effect.  This specification
   defines the token schemas, cryptographic bindings, and boundary
   validation sequences required to isolate context reconstruction
   domains without modifying underlying enterprise datastores.

   Readers are respectfully encouraged to review Section 4 and Section 5
   in full, as those sections set out the complete problem description
   and motivating scenarios and should not be skipped.
- **draft-das-execution-finality-ai-interoperability-03** (new-draft, score 10, authorization) [none]: [Secure and Privacy-Preserving AI Interoperability under Article 6(7) of the European Digital Markets Act: An Execution-Finality Architecture](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — This document presents a security- and privacy-preserving execution-
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

   In June 2026, Apple announced that it would not ship its new Siri AI
   on iOS 27 and iPadOS 27 in the European Union, stating that EU
   regulators had not accepted its proposed interoperability safeguards
   and that granting third-party assistants access equivalent to Siri's
   created unacceptable security and privacy exposure.  The European
   Commission responded that nothing in the DMA itself required Apple to
   withhold the feature, describing Apple's decision as a voluntary
   business choice rather than a legal necessity, and noting that Apple
   had requested a blanket exemption rather than submitting a compliant
   technical mechanism.  Both positions are correct within their own
   frame: Apple's underlying security concern about undifferentiated
   third-party system access is real, and the Commission is also correct
   that the DMA does not itself compel a trade-off between
   interoperability and security.  This document's execution-finality
   architecture is offered as the middle solution by which both can be
   satisfied simultaneously: third-party AI assistants gain the
   interoperability the DMA requires, while the platform retains the
   bounded, verifiable finality control that Apple's objection is
   actually about.  To show this is not only a theoretical proposal, a
   runnable reference implementation of this architecture has been
   published, demonstrating how the design behaves end to end in a
   virtual/test environment (note: behavior and measurements in an
   actual production environment may differ).
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
- **draft-sato-soos-mad-05** (new-draft, score 10, authorization) [none]: [Multi-Agent Delegation in Sovereign Object Systems](https://datatracker.ietf.org/doc/draft-sato-soos-mad/) — When a consequential task requires multiple AI agents -- one to
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

   Version -05 is an editorial revision with no normative content
   changes: sibling-draft citations (IDP, HEM, CAP, MJWT, AEP, AOP)
   had gone stale against those drafts' current live versions and
   are updated to draft-sato-soos-idp-06, draft-sato-soos-hem-07,
   draft-sato-soos-cap-06, draft-sato-soos-mjwt-06,
   draft-sato-soos-aep-04, and draft-sato-soos-aop-03 respectively;
   the CAP-RRS and PT citations in the Companion Drafts list are
   similarly updated to -04 and -04; and the FAIP citation is
   migrated from the versioned [I-D.sato-soos-faip] form to the
   non-versioned [SOOS-FAIP] form, since FAIP is a Class B
   specification that will not be submitted to the IETF Datatracker.
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
- **draft-campbell-agentic-market-00** (new-draft, score 9, core_identity) [none]: [Agentic Hypercall Protocol (AHP): Tool Invocation, Blind Settlement, and Portable Reputation over HTTP](https://datatracker.ietf.org/doc/draft-campbell-agentic-market/) — This document specifies the Agentic Hypercall Protocol (AHP), a
   minimal convention for automated software agents to discover, invoke,
   pay for, and rate tools over plain HTTP.  It replaces draft-campbell-
   agentic-http-00 and extends it in three directions.  First, it
   formalizes the HTTP 402 (Payment Required) status code as a native
   economic layer with pluggable payment rails (Lightning L402, Cashu
   ecash, and prepaid balances).  Second, it specifies a blind relay --
   the Gateway -- through which a consumer and a provider can transact
   end-to-end encrypted: the relay verifies identity, settles payment,
   and forwards sealed payloads it cannot read.  Third, it specifies
   signed receipts, settlements, and rating attestations that let
   reputation be weighted by money actually settled rather than by
   tokens or votes, and that ride with a provider's key rather than with
   any single relay.  The result is an open market in which agents can
   buy compute, information, and services from one another without an
   SDK, a walled garden, or a native token.
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
- **draft-ietf-acme-authority-token-jwtclaimcon-06** (new-draft, score 9, core_identity) [acme]: [JWTClaimConstraints profile of ACME Authority Token](https://datatracker.ietf.org/doc/draft-ietf-acme-authority-token-jwtclaimcon/) — This document defines an authority token profile for the validation
   of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate
   extensions within the Automated Certificate Management Environment
   (ACME) protocol.  This profile is based on the Authority Token
   framework and establishes the specific ACME identifier type,
   challenge mechanism, and token format necessary to authorize a client
   to request a certificate containing these constraints.
- **draft-ietf-lake-edhoc-psk-09** (new-draft, score 9, core_identity) [lake]: [EDHOC Authenticated with Pre-Shared Keys (PSK)](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-psk/) — This document specifies a Pre-Shared Key (PSK) authentication method
   for the Ephemeral Diffie-Hellman Over COSE (EDHOC) Lightweight
   Authenticated Key Exchange (LAKE) protocol.  The PSK method provides
   mutual authentication, ephemeral key exchange, identity protection,
   and quantum resistance while incurring lower computational costs than
   the public-key authentication methods specified for EDHOC.  It is
   suited for systems where nodes share a PSK provided out-of-band
   (external PSK) and enables efficient session resumption with less
   computational overhead when the PSK is provided from a previous EDHOC
   session (resumption PSK).  This document details the PSK message
   flow, key derivation changes, message formatting, processing, and
   security considerations.
- **draft-ietf-oauth-v2-1-16** (new-draft, score 9, authorization) [oauth]: [The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) — The OAuth 2.1 authorization framework enables an application to
   obtain limited access to a protected resource, either on behalf of a
   resource owner by orchestrating an approval interaction between the
   resource owner and an authorization service, or by allowing the
   application to obtain access on its own behalf.  This specification
   replaces and obsoletes the OAuth 2.0 Authorization Framework
   described in RFC 6749 and the Bearer Token Usage in RFC 6750.
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
- **draft-sato-soos-grp-02** (new-draft, score 9, agent_identity) [none]: [The Governed Remediation Protocol (GRP) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-grp/) — This document specifies the Governed Remediation Protocol (GRP)
   for agentic AI systems operating under the Sovereign Object OS
   (SOOS) framework.  GRP defines the normative remediation action
   set available to a SOOS governance kernel when agent execution
   encounters a governed failure condition: FALLBACK (autonomous
   resource substitution), RETRY (bounded autonomous retry),
   ESCALATE (human escalation boundary), and ROLLBACK (reversible
   action undo).  GRP specifies the conditions under which each
   action class may be taken autonomously and the boundaries at
   which Human Escalation Messaging (HEM) is required.  GRP
   operates at the intersection of the Resource Governance Protocol
   (RGP), the Agent Execution Protocol (AEP), and the Human
   Escalation Mechanism (HEM), and normatively references the
   Governance Audit Record (GAR) for logging all remediation events.
   GRP adopts DEC-RGP-08 (the three-condition autonomous fallback
   test) verbatim from the Resource Governance Protocol as the
   normative FALLBACK action class boundary rule.

   Version -02 restores Section 9.4 (Artifact-Level Impact
   Refinement), the CONTENT_CORRECTION change_class value, and
   the affected_da_id field, which were inadvertently dropped from
   -01's Datatracker submission during an unrelated editorial
   pass; a WIMSE-style review of the restored text found and
   closes a genuine gap in its original form -- Section 9.4(1)'s
   impact query walked only one hop of the derived_from
   derivation graph, missing artifacts transitively downstream of
   a correction, and now walks the graph transitively with a
   bounded traversal depth.  This revision also mirrors RGP-02's
   ALE-026/ALE-064/ALE-066 double-recording reconciliation into
   this document's own Section 11.6 (previously stated only on
   RGP's side), and renames ALE-066 from GRP_FALLBACK_ACTIVATED
   to GRP_MEDIATED_FALLBACK_ACTIVATED to remove its near-duplicate
   naming collision with RGP's own ALE-026
   (RGP_FALLBACK_ACTIVATED).  This revision adds Remediation
   Outcome Verification (Section 11.7): FALLBACK and RETRY could
   previously complete with a clean mechanical success record
   while the outcome the session actually needed still went
   undelivered, with no check against the session's own EOD until
   AEP's own session-close evaluation, if any GRP action had even
   run by then.  A new ALE-070 (GRP_REMEDIATION_VERIFIED) closes
   that gap, reusing AEP's own MATCHED/PARTIAL/PLAN_B_MATCHED/
   UNMATCHED vocabulary so a mid-session verification result is
   directly comparable to the session's eventual outcome.  Three
   prior references to the EOD as the "IDP Expected Outcome
   Declaration" are also corrected to AEP, its actual source.
- **draft-zhang-dawn-agent-discovery-framework-01** (new-draft, score 9, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — The IETF DAWN (Discovery of Agents With Names) working group is
   developing a suite of documents addressing agent discovery across
   organizational boundaries, initially focused on discovery of AI
   agents and their capabilities.  Existing DAWN contributions include
   terminology, requirements, use cases, gap analysis, a discovery
   mechanism survey, and an information model for Minimum Discoverable
   Information (MDI).

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

   Consistent with the DAWN charter, the architecture is primarily
   targeted at AI agent discovery while remaining general and reusable
   for other entity types.
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
- **draft-schrock-ep-bounded-capability-receipts-05** (new-draft, score 7, authorization) [none]: [Bounded Capability Receipts and Durable Spend Control for Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-capability-receipts/) — Agents sometimes need bounded authority to perform more than one
   consequential action without obtaining a new human approval for every
   operation.  A signed token alone cannot enforce a shared budget
   across replicas, survive retries safely, or distinguish an operation
   that never crossed an effect boundary from one whose outcome is
   unknown.

   This document defines a bounded capability receipt and a durable
   reserve-admit-reconcile protocol.  The receipt binds an issuance
   authorization, a closed action scope, a budget with explicit units, a
   holder proof, an expiry, and any parent capability.  The state
   protocol atomically refuses overspend and operation-key replay,
   fences concurrent owners, and charges an indeterminate operation when
   an external effect may have occurred.  Delegation transfers rather
   than copies authority: all direct child allocations are funded by
   committed parent operations before child registration, and their
   aggregate cannot exceed the parent balance within one authoritative
   atomic state domain.  It also defines narrowing-only delegation,
   explicit revocation inheritance for delegated authority, an optional
   admission-control epoch that can freeze new consequence admission,
   and evidence interfaces.  It does not make a bearer token into human
   approval, does not provide cross-domain or offline global double-
   spend prevention, and does not claim that an authorized action was
   safe, lawful, or successfully executed.
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

- **draft-alhemeiri-wathiqa-pqc-ers-01** (new-draft, score 6, trust_infrastructure) [none]: [Post-Quantum Evidence Records with Algorithm Agility (Wathiqa Profile)](https://datatracker.ietf.org/doc/draft-alhemeiri-wathiqa-pqc-ers/) — This document describes an evidence-record format for the long-term,
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
   beacon anchor records _not-before_ evidence: from wire version 3 it
   is authenticated against the beacon's hash chain, with the beacon's
   classical pulse signature as defence in depth; the Security
   Considerations say which assumption each check rests on.
- **draft-cel-nfsv4-rpc-tls-dane-00** (new-draft, score 6, core_identity) [none]: [Using RPC-with-TLS with DNS-Based Authentication of Named Entities](https://datatracker.ietf.org/doc/draft-cel-nfsv4-rpc-tls-dane/) — RPC-with-TLS assumes that DNS-Based Authentication of Named Entities
   (DANE) is available on platforms where it is deployed, and recommends
   that a client operating under an opportunistic security policy check
   for a TLSA record before initiating an association, but does not say
   how.  This document specifies the missing details, so that a TLSA
   record authenticates an RPC server with no certification authority
   trust anchor provisioned on the client.  It updates RFC 9289.
- **draft-das-precision-bounded-egress-03** (new-draft, score 6, agent_identity) [none]: [Access Is Not Egress: Precision-Bounded Location Release](https://datatracker.ietf.org/doc/draft-das-precision-bounded-egress/) — A device may legitimately possess exact location while an
   application, SDK, AI agent, analytics library, or foreign endpoint is
   entitled only to a coarser representation, a delayed or randomized
   representation, or no location at all.  Operating system permission
   to read a fix does not answer whether that fix may leave the device
   at the requested precision.

   This document defines a precision-bounded egress profile: a data-
   minimization mechanism applied at the point of external disclosure,
   on top of an execution-finality architecture, applicable equally to
   conventional applications and to autonomous AI agents acting on a
   user's behalf.  The gap this closes is concrete: an application that
   legitimately reads exact GPS for one on-device purpose commonly
   shares its process with an embedded SDK, agent tool, or cloud sync
   path that can forward the same exact coordinate to a destination that
   never needed it, without the user seeing that forwarding as a
   separate disclosure.

   A proposed release is a Location-Release Candidate Act and remains
   non-effective while a Protected Enforcement Domain evaluates purpose,
   requester, component, recipient, destination, jurisdiction, required
   precision, policy and revocation state, cumulative disclosure state,
   and intended egress sink.  The Protected Enforcement Domain issues
   scoped, non-bearer, cryptographically bound finality authority for a
   specific precision ceiling, expressed using the JSON interoperability
   objects defined in this document.  An independent egress Finality
   Sink verifies that authority against the actual outbound payload
   immediately before release, so the bound ceiling, rather than the
   requester's declared precision, determines what may leave the device.

   The permitted result may be exact data, a reduced representation, or
   denial.  Data access is not data-export authority.  Precise GPS
   access is not precise GPS-release authority.
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
- **draft-ffm-rats-cca-token-04** (new-draft, score 6, trust_infrastructure) [none]: [Arm's Confidential Compute Architecture Reference Attestation Token](https://datatracker.ietf.org/doc/draft-ffm-rats-cca-token/) — The Arm Confidential Compute Architecture (CCA) is series of hardware
   and software innovations that enhance Arm’s support for Confidential
   Computing for large, compute-intensive workloads.  Devices that
   implement CCA can produce attestation tokens as described in this
   memo, which are the basis for trustworthiness assessment of the
   Confidential Compute environment.  This document specifies the CCA
   attestation token structure and semantics.

   The CCA attestation token is a profile of the Entity Attestation
   Token (EAT).  This specification describes what claims are used in an
   attestation token generated by CCA compliant systems, how these
   claims get serialized to the wire, and how they are cryptographically
   protected.

   This informational document is published as an independent submission
   to improve interoperability with Arm's architecture.  It is not a
   standard nor a product of the IETF.
- **draft-ietf-lamps-rfc6211-update-00** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects an error in definition
   of the id-aa-CMSAlgorithmProtection ASN.1 object identifier.  The
   IANA registry entry has alway been correct.
- **draft-irtf-cfrg-pairing-friendly-curves-14** (new-draft, score 6, core_identity) [cfrg]: [Pairing-Friendly Curves](https://datatracker.ietf.org/doc/draft-irtf-cfrg-pairing-friendly-curves/) — Pairing-based cryptography, a subfield of elliptic curve
   cryptography, has received attention due to its flexible and
   practical functionality.  Pairings are special maps defined using
   elliptic curves and they can be applied to construct several
   cryptographic protocols such as identity-based encryption, attribute-
   based encryption, and so on.  At CRYPTO 2016, Kim and Barbulescu
   proposed an efficient number field sieve algorithm named exTNFS for
   the discrete logarithm problem in a finite field.  Several types of
   pairing-friendly curves such as Barreto-Naehrig curves are affected
   by the attack.  In particular, a Barreto-Naehrig curve with a 254-bit
   characteristic was adopted by a lot of cryptographic libraries as a
   parameter of 128-bit security; however, it ensures no more than the
   100-bit security level due to the effect of the attack.  In this
   memo, we list the security levels of certain pairing-friendly curves,
   and motivate our choices of curves.  First, we summarize the adoption
   status of pairing-friendly curves in standards, libraries and
   applications, and consider them at the 128-bit, 192-bit, and 256-bit
   security levels.  Then, from the viewpoints of "security" and "widely
   used", we select the recommended pairing-friendly curves considering
   exTNFS.  This memo also specifies the serialization and
   deserialization of the points and scalars that protocols exchange,
   restating a format that is already in widespread use, and states
   which of the remaining decisions belong to the calling protocol.
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
- **draft-bubblefish-npamp-02** (new-draft, score 5, core_identity) [none]: [N-PAMP: Native Post-Quantum Agent Messaging Protocol](https://datatracker.ietf.org/doc/draft-bubblefish-npamp/) — The Native Post-Quantum Agent Messaging Protocol (N-PAMP) is a
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
   Application-Layer Protocol Negotiation (ALPN) identifier "n-pamp/3".
   This document describes the wire format, channel architecture,
   profile negotiation, and cryptographic suites of N-PAMP, and reserves
   code-point ranges for extensions defined in companion specifications.
- **draft-das-ai-native-6g-execution-finality-03** (new-draft, score 5, core_identity) [none]: [Execution-Finality for AI-Native 5G/6G and O-RAN](https://datatracker.ietf.org/doc/draft-das-ai-native-6g-execution-finality/) — In programmable and AI-assisted mobile networks, successful
   authentication of a network function or AI controller does not
   establish authority for every routing, signaling, session, resource-
   allocation, sensing, or subscriber-specific consequence that the
   function can generate.

   This document defines an informational execution-finality profile for
   AI-native 5G, 5G-Advanced, IMT-2030/6G, O-RAN, and AI-RAN
   environments.  A proposed network operation is represented as a
   Network Candidate Act and remains in a Non-Effective State while a
   Protected Enforcement Domain validates act-specific predicates.
   Protected validation evidence is committed before, or atomically
   with, release of scoped non-bearer finality authority.  A Network
   Finality Sink at the enforcement boundary independently verifies that
   authority immediately before live network state changes.

   The governing rule is that network authentication is not network
   finality, and computation is not authority.  This revision also
   defines a JSON interoperability profile for Candidate Acts,
   validation decisions, scoped authority, and sink verification.

   This profile is distinct from, and complementary to, present AI-
   native 6G industry roadmaps that focus on radio, sensing, and
   platform capability, including air-interface, MIMO, spectrum, and AI-
   RAN infrastructure work described in Qualcomm's public AI-native 6G
   platform material, and the broad native-trustworthiness and agentic-
   core-network architectures described in Huawei's public 6G security
   research.  Those efforts address how a network becomes more
   intelligent, autonomous, and platform-trustworthy.  This document
   addresses a narrower and later question: once an already-
   authenticated, already-policy-approved AI-generated network operation
   has been computed, whether that exact operation may become a live
   network consequence.  The Candidate Act, Non-Effective State,
   Protected Enforcement Domain, and Finality Sink constructs defined
   here, as an explicit pre-effectuation gate with act-bound non-bearer
   authority and independent sink-side re-verification, are not
   established as an equivalent primitive in publicly reviewed material
   from those roadmaps.
- **draft-kavian-offering-discovery-protocol-01** (new-draft, score 5, adjacent_watchlist) [none]: [The Offering Discovery Protocol](https://datatracker.ietf.org/doc/draft-kavian-offering-discovery-protocol/) — The Offering Discovery Protocol (ODP) enables an automated Agent to
   inspect a Service, discover its Collections and Offerings, interpret
   Service-defined structured attributes, and identify links to
   subsequent operations.  ODP supports catalogs ranging from a few
   Offerings to large marketplaces without imposing a universal product
   taxonomy.  This document defines the protocol's scope, terminology,
   roles, discovery architecture, extensibility model, composition
   boundaries, and conformance model.
- **draft-sato-soos-peer-02** (new-draft, score 5, agent_identity) [none]: [Cross-Principal Agent Communication -- PEER Transaction Record](https://datatracker.ietf.org/doc/draft-sato-soos-peer/) — When two independently-principaled AI agents transact with each
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

   Version -02 is an editorial revision with no normative content
   changes: stale sibling-draft citations to CAP, HEM, and FAIP were
   brought current.
- **draft-schrock-ep-quorum-04** (new-draft, score 5, authorization) [none]: [Multi-Party Quorum Authorization for High-Risk Agent Actions (EP-QUORUM)](https://datatracker.ietf.org/doc/draft-schrock-ep-quorum/) — This document defines a multi-party approval predicate over action-
   bound human signoffs: valid signatures, admitted roles, distinct
   approvers and keys, threshold, and an optional ordered trail.  The
   relying party pins the governing policy and approver directory
   independently.  Passing the predicate is approval evidence, not a
   complete authorization decision, proof of execution, or proof of
   unused authority.

   This revision repairs the strong ordered profile.  A successor signs
   a digest of the completed predecessor signoff, including its
   signature, rather than a precomputable context.  The versioned
   profile establishes causal dependence on a completed prior proof
   under the cryptographic assumptions; it does not establish trusted
   wall-clock time or human comprehension.  Legacy context-only chains
   cannot satisfy it.  JavaScript, Python, and Go reference verifiers
   share a corpus in one repository.  Agreement is a same-team
   consistency check, not independent interoperability evidence or a
   formal proof of the new construction.
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
- **draft-zhu-anima-service-intent-01** (new-draft, score 5, adjacent_watchlist) [none]: [Definition of Service Intent in Autonomic Networks](https://datatracker.ietf.org/doc/draft-zhu-anima-service-intent/) — While ANIMA Intent enables goal-oriented control within an Autonomic
   Domain, emerging services (e.g., AI inference) require a common,
   interoperable representation for expressing service-level objectives
   and constraints that span network, compute, and storage resources,
   rather than connection-centric descriptions.  This document defines
   Service Intent for Autonomic Networks by specifying a structured
   semantic model and a concise format with identification, scope,
   versioning, and lifecycle semantics.
- **draft-reddy-wimse-aggregate-signatures-00** (new-draft, score 4, adjacent_watchlist) [none]: [Aggregate Signatures for WIMSE Delegation-Chain Integrity](https://datatracker.ietf.org/doc/draft-reddy-wimse-aggregate-signatures/) — This document profiles the WIMSE HTTP Message Signatures mechanism
   ([I-D.ietf-wimse-http-signature]) to protect a request that passes
   through a chain of workloads.  In the base mechanism each workload
   signs independently: an intermediary can remove a signature
   undetected, and the signatures accumulate on every hop.  This
   document combines the workloads' signatures into one aggregate
   signature.  Removal of a signature becomes detectable, and the
   signature material no longer grows with the length of the chain, a
   significant saving for post-quantum signature algorithms, whose
   signatures are large.  The mechanism works with any aggregate
   signature scheme.
- **draft-saha-stage-receipts-00** (new-draft, score 4, adjacent_watchlist) [none]: [Stage Receipts: A Verifiable Record Format for Staged Pipelines](https://datatracker.ietf.org/doc/draft-saha-stage-receipts/) — A staged pipeline -- a document-ingestion flow, a retrieval-augmented
   generation chain, an agent workflow, a benchmark -- produces results
   that are hard to reproduce, hard to diff between two runs, and hard
   to localize when they go wrong.  This document defines the stage
   receipt: a small, canonically serialized JSON record that each stage
   of such a pipeline emits, describing exactly what went in, what came
   out, under which pinned instrument, with which outcome, and linked by
   digest to the receipt before it.  A chain of stage receipts lets a
   developer reproduce a run, diff two runs to the first stage that
   differs, and localize a fault to the stage where it entered; the same
   chain lets an independent party, later and offline, establish what
   the records assert without trusting whoever produced them.  The
   document specifies the record, its canonical form, the chain
   manifest, the coverage and emission declarations that make a chain
   honest about its own edges, the anchoring declaration that separates
   consistency from originality, and the behaviour required of a
   conforming verifier.  Golden conformance vectors -- records that must
   be accepted and records that must be refused, each with its reason --
   are part of the specification.

## Adjacent / watchlist

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
- **draft-corbel-updates-to-rfc2289-00** (new-draft, score 3, core_identity) [none]: [Updates to the One-Time Password (OTP) System defined by RFC 2289](https://datatracker.ietf.org/doc/draft-corbel-updates-to-rfc2289/) — This document aims to submit a few updates to RFC 2289 [RFC2289],
   which describes a One-Time Password (OTP) System: an application
   programming interface to the new Secure Hash Algorithms (SHA256,
   SHA384, and SHA512), an algorithm for folding hashes to 64 bits,
   using alternate dictionaries, and automatic renewal of authentication
   parameters will be described.
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
- **draft-ietf-core-oscore-id-update-07** (new-draft, score 3, core_identity) [core]: [Identifier Update for OSCORE](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-id-update/) — Two peers that communicate with the CoAP protocol can use the Object
   Security for Constrained RESTful Environments (OSCORE) protocol to
   protect their message exchanges end-to-end.  To this end, the two
   peers share an OSCORE Security Context and a number of related
   identifiers.  In particular, each of the two peers stores a Sender ID
   that identifies its own Sender Context within the Security Context,
   and a Recipient ID that identifies the Recipient Context associated
   with the other peer within the same Security Context.  These
   identifiers are sent in plaintext within OSCORE-protected messages.
   Hence, they can be used to correlate messages exchanged between peers
   and track those peers, with consequent privacy implications.  This
   document defines an OSCORE ID update procedure that two peers can use
   to update their OSCORE identifiers.  This procedure can be run stand-
   alone or seamlessly integrated in an execution of the Key Update for
   OSCORE (KUDOS) procedure.
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
- **draft-ietf-sidrops-rtr-yang-09** (new-draft, score 3, adjacent_watchlist) [sidrops]: [YANG Data Model for RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rtr-yang/) — This document defines YANG data models for managing Resource Public
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
- **draft-ietf-vcon-vcon-core-04** (new-draft, score 3, adjacent_watchlist) [vcon]: [The JSON format for vCon - Conversation Data Container](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-core/) — vCon is a standardized framework for the exchange of conversational
   data.  Conversations, which may involve one or more participants,
   occur across a wide variety of modes and application platforms.  This
   document defines a JSON format for representing conversational data,
   encompassing metadata, conversation media, related documents, and
   analysis.  The goal of this standard is to provide an abstracted,
   platform-independent data format for conversations, regardless of the
   mode or application platform.  By doing so, it facilitates the
   integration and seamless exchange of conversational data across
   application platforms, enterprises, and trust boundaries.
- **draft-intra-handshake-fail-25** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake (aka Early) Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
   (https://www.cve.org/CVERecord?id=CVE-2026-33697), EUVD-2026-16488
   (https://euvd.enisa.europa.eu/enisa/EUVD-2026-16488), and several
   GitHub Security Advisories (GHSAs) which provide substantial
   technical evidence of how *intra*-handshake (aka early) attestation
   fails in practice, even _without physical access_. Moreover, since
   continuous attestation is generally required, *intra*-handshake
   attestation adds *unnecessary complexity*. The results are backed by
   the research [Intra-handshake.fail], [TLS-RA] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility and review,
   and have been acknowledged by the relevant stakeholders.  Currently,
   there are *two CVEs of CVSS 7.5, two GHSAs of CVSS 9.1, one GHSA of
   CVSS 7.8, seven GHSAs of CVSS 7.4, and one GHSA of CVSS 6.3 published
   against intra-handshake (aka early) attestation*. The research papers
   on these are currently either under submission or being prepared for
   submission.  The artifacts of these papers will be shared with the
   community under Apache-2.0 license for reproducibility and review.
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
- **draft-le-comparing-derived-identifiers-01** (new-draft, score 3, core_identity) [none]: [A Framework for Comparing Independently Derived Identifiers](https://datatracker.ietf.org/doc/draft-le-comparing-derived-identifiers/) — Specifications use equality of independently derived identifiers to
   compare underlying values.  Those comparisons require shared rules
   for admission, equivalence, derivation, and output interpretation.
   Inconsistent rules can give different identifiers to equivalent
   values or equal identifiers to values that the comparison
   distinguishes.

   This document presents a framework for specifying and reviewing these
   rules as a comparison contract.  It connects source mappings to
   derivation-domain equivalence and the conclusions supported by equal
   and unequal outputs.  It distinguishes information loss before a
   downstream operation from that operation's own false match
   properties.  A review traces the relevant specification clauses,
   records supporting evidence, and identifies failed or unestablished
   obligations.  The framework provides guidance for concrete identifier
   specifications; it defines no identifier format or derivation
   algorithm.
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
- **draft-bormann-cbor-cddl-freezer-18** (new-draft, score 2, ignored_after_review) [none]: [A feature freezer for the Concise Data Definition Language (CDDL)](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-freezer/) — In defining the Concise Data Definition Language (CDDL), some
   features have turned up that would be nice to have.  In the interest
   of completing this specification in a timely manner, the present
   document was started to collect nice-to-have features that did not
   make it into the first RFC for CDDL, RFC 8610, or the specifications
   exercising its extension points, such as RFC 9165.

   Significant parts of this draft have now moved over to the CDDL 2.0
   project, described in draft-bormann-cbor-cddl-2-draft.  The remaining
   items in this draft are not directly related to the CDDL 2.0 effort.
- **draft-clifford-testimony-record-01** (new-draft, score 2, ignored_after_review) [none]: [The Testimony Record: An Interchange Format for What an Automated System Believed and Did](https://datatracker.ietf.org/doc/draft-clifford-testimony-record/) — This document specifies the Testimony Record, an append-only
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
- **draft-dogru-cedulon-decision-profile-03** (new-draft, score 2, ignored_after_review) [none]: [Cedulon Decision Profile: Reconciling an Agent's Decisions Against Its Effects](https://datatracker.ietf.org/doc/draft-dogru-cedulon-decision-profile/) — The Cedulon core document reconciles an issuer's signed Spend
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
- **draft-elkhatabi-verifiable-telemetry-ledgers-11** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Telemetry Ledgers](https://datatracker.ietf.org/doc/draft-elkhatabi-verifiable-telemetry-ledgers/) — This document profiles a verifiable-telemetry ledger.  Its
   interoperability boundary begins with exact canonical-record byte
   strings that an upstream system has already produced.  The profile
   fixes their admission into serial-numbered segments, deterministic
   commitment-tree calculation, an authoritative segment artifact
   encoded in Concise Binary Object Representation (CBOR), a producer
   manifest, three disclosure classes, and binding of the artifact
   digest through a required external timestamp channel.  Segment
   closure uses a deployment-configured elapsed-time interval and does
   not depend on calendar dates.

   The profile enables independent recomputation and audit of disclosed
   evidence from the admitted bytes onward.  Transport framing,
   decryption, anti-replay processing, payload interpretation, and
   source-telemetry-to-record mapping are outside it, as are device
   onboarding, end-to-end security of sensor values, and safety
   decisions.
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
- **draft-lz-fann-bandwidth-notification-00** (new-draft, score 2, ignored_after_review) [none]: [Fast Notification for Link Bandwidth](https://datatracker.ietf.org/doc/draft-lz-fann-bandwidth-notification/) — This document proposes a data-plane-based method for rapidly
   advertising end-to-end path bandwidth information using a bitmap
   encoding.  The mechanism enables fast load-balancing adjustments in
   AI/ML data center fabrics.
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

- **draft-acosta-deepspace-celestial-bodies-registry-02** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Reference Framework for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document highlights the architectural requirement within
   Deepspace/TIPTOP protocols to utilize an external, standardized
   reference framework for celestial objects, functioning as an
   equivalent to ISO 3166 for interplanetary networking.  To avoid
   operational overhead and duplication of effort, this framework defers
   the definitions, naming, and tracking of celestial entities directly
   to the International Astronomical Union (IAU) and the Minor Planet
   Center (MPC).  This document outlines how these external identifiers
   guide hierarchical address allocation without requiring IANA to
   maintain a dedicated astronomical nomenclature registry.  The
   ultimate objective is to establish a clear definition of what
   constitutes a valid Celestial Body for networking purposes.
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
- **draft-anjum-nmop-anomaly-detection-evaluation-02** (new-draft, score 0, ignored_after_review) [none]: [Evaluation Methodology for Network Anomaly Detection](https://datatracker.ietf.org/doc/draft-anjum-nmop-anomaly-detection-evaluation/) — The Network Management Operations (NMOP) working group has adopted
   documents describing an architecture, an operational lifecycle, and a
   semantics for network anomaly detection.  Those documents direct
   implementers to minimize false positives and false negatives, but do
   not define how the accuracy of an anomaly detection implementation is
   to be measured, compared, or tracked over time.  This document
   describes an evaluation methodology for anomaly detectors operating
   on network and infrastructure telemetry, whether the detector is
   rule-based, statistical, or machine-learning-based: the metrics to
   report and their known failure modes, a benchmarking procedure based
   on controlled fault injection and replay, ground-truth labeling and
   scoring across multiple telemetry signals, and the properties a
   benchmark dataset needs to support reproducible, comparable
   evaluation.  The methodology is informational and complements the
   adopted NMOP anomaly-detection documents.
- **draft-bcht-data-truck-transport-00** (new-draft, score 0, ignored_after_review) [none]: [Data Truck Transport Protocol](https://datatracker.ietf.org/doc/draft-bcht-data-truck-transport/) — Large-scale data transfers may be affected by bandwidth limitations
   and network instability, which can make network-based data transfer
   inefficient.  DTTP provides an alternative data transfer method for
   such situations.

   DTTP uses physical transportation to carry Storage Media containing
   the Payload.  A physical vehicle is used as the Transmission Medium
   for transporting the Storage Media between the Sender and the
   Receiver.
- **draft-bertoldi-regext-rdap-reliability-scoring-02** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Structured Reliability Assessment Metadata](https://datatracker.ietf.org/doc/draft-bertoldi-regext-rdap-reliability-scoring/) — This document proposes an extension to the Registration Data Access
   Protocol (RDAP) that enables the representation and exchange of
   structured reliability assessment metadata for registrars and domain
   names.  The extension defines a structured assessment envelope
   through which an RDAP server can expose assessment results produced
   by a registry, registrar, or third-party assessor in a common,
   machine-readable format within RDAP responses.

   The extension standardizes how assessment results are transported and
   referenced, not how they are computed.  Scoring methodologies,
   thresholds, criteria, and governance frameworks are intentionally
   left to the operational and policy layer.  This document does,
   however, place requirements on the specification of any scheme whose
   results are intended for publication through RDAP, because publishing
   an evaluative judgement about an identified party without safeguards
   for notification, remediation, and contestation is not a safe
   practice.
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
- **draft-brotman-aggregate-performance-reporting-01** (new-draft, score 0, ignored_after_review) [none]: [Aggregate Performance Reporting](https://datatracker.ietf.org/doc/draft-brotman-aggregate-performance-reporting/) — Definition of an aggregate performance report format for email
   messaging, the means to discover target destinations, and a specified
   delivery method.
- **draft-cao-opsawg-ipfix-sav-04** (new-draft, score 0, ignored_after_review) [none]: [Export of Source Address Validation (SAV) Information in IPFIX](https://datatracker.ietf.org/doc/draft-cao-opsawg-ipfix-sav/) — This document specifies the IP Flow Information Export Information
   Elements to export the context and outcome of Source Address
   Validation enforcement data.  These SAV-specific Information Elements
   provide detailed insight into why packets are identified as spoofed
   by capturing the specific SAV rules that triggered validation
   decisions.  This operational visibility is essential for network
   operators to observe SAV enforcement behavior and analyze source
   address spoofing events detected by SAV.
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
- **draft-ek-dtn-ethernet-06** (new-draft, score 0, ignored_after_review) [none]: [Bundle Transfer Protocol - Unidirectional (BTPU) over Ethernet](https://datatracker.ietf.org/doc/draft-ek-dtn-ethernet/) — This document specifies the use of the Bundle Transfer Protocol -
   Unidirectional (BTPU) as a Convergence Layer directly over Ethernet,
   and requests allocation of an EtherType and a multicast MAC address
   for that purpose.  This provides an alternative to IP-based
   convergence layers for environments where Ethernet forwarding is
   operationally feasible but IP routing is unavailable or operationally
   undesirable.
- **draft-ek-dtn-qubicle-02** (new-draft, score 0, ignored_after_review) [none]: [DTN QUIC Bundle Protocol Convergence Layer (qubicle)](https://datatracker.ietf.org/doc/draft-ek-dtn-qubicle/) — This document specifies a minimal convergence layer protocol for
   transferring Bundle Protocol version 7 (BPv7) bundles over QUIC.  The
   protocol leverages QUIC's native capabilities for reliable streaming,
   connection management, and security.  Reliable transfers carry each
   bundle on its own QUIC stream, either directly or wrapped in a single
   CBOR byte string, with no further application-layer framing.
   Unreliable transfers use the Bundle Transfer Protocol -
   Unidirectional (BTP-U) over QUIC datagrams.
- **draft-gerke-publication-process-reform-05** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.
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
- **draft-ietf-bess-evpn-bfd-20** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Network Layer Fault Management](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-bfd/) — This document specifies proactive, in-band Network Layer OAM (RFC
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
- **draft-ietf-ccwg-ratelimited-increase-11** (new-draft, score 0, ignored_after_review) [ccwg]: [Increase of the Congestion Window when the Sender Is Rate-Limited](https://datatracker.ietf.org/doc/draft-ietf-ccwg-ratelimited-increase/) — This document specifies how transport protocols increase their
   congestion window when the sender is rate-limited, and updates RFCs
   4341, 5681, 9002, 9260, and 9438.  Such a limitation can be caused by
   the sending application not supplying data or by receiver flow
   control.
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
- **draft-ietf-core-oscore-key-limits-08** (new-draft, score 0, ignored_after_review) [core]: [Key Usage Limits for OSCORE](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-key-limits/) — Object Security for Constrained RESTful Environments (OSCORE) uses
   AEAD algorithms to ensure confidentiality and integrity of exchanged
   messages.  Due to known issues allowing forgery attacks against AEAD
   algorithms, limits should be followed on the number of times a
   specific key is used for encryption or decryption.  Among other
   reasons, approaching key usage limits requires updating the OSCORE
   keying material before communications can securely continue.  This
   document defines how two OSCORE peers can follow these key usage
   limits and what steps they should take to preserve the security of
   their communications.
- **draft-ietf-dtn-bibe-00** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle-in-Bundle Encapsulation](https://datatracker.ietf.org/doc/draft-ietf-dtn-bibe/) — This document describes Bundle-in-Bundle Encapsulation (BIBE), a
   Delay-Tolerant Networking (DTN) Bundle Protocol (BP) tunneling
   mechanism by which a bundle is carried as the payload of one or more
   encapsulating bundles, allowing security measures, routing policy,
   and protocol version translation to be applied to the encapsulating
   bundle without modification of the encapsulated bundle.  The protocol
   includes an optional segmentation mechanism, allowing a large
   encapsulated bundle to be carried in multiple encapsulating bundles.
- **draft-ietf-dtn-btpu-04** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Transfer Protocol - Unidirectional](https://datatracker.ietf.org/doc/draft-ietf-dtn-btpu/) — This document defines a protocol for the unidirectional transfer of
   large binary objects, typically Bundle Protocol version 7 bundles,
   between two nodes connected by a unidirectional, unreliable, frame-
   based link-layer protocol, without requiring IP services.

   The protocol does not require a return path for acknowledgements, but
   instead supports data repetition as a mechanism to protect against
   data loss.  It fully supports the disaggregation of flows of binary
   objects of different priority, preventing head-of-line blocking
   impacting performance.

   The wire format of the protocol is designed to enable performant
   implementation in hardware or software, with the aim of enabling
   protocol implementations to run at the line-rate of the underlying
   link-layer protocol.
- **draft-ietf-dtn-btpu-fec-02** (new-draft, score 0, ignored_after_review) [dtn]: [Forward Error Correction for the Bundle Transfer Protocol](https://datatracker.ietf.org/doc/draft-ietf-dtn-btpu-fec/) — This document defines an optional extension to the Bundle Transfer
   Protocol - Unidirectional, as described in [BTPU], to enable forward
   error correction (FEC) coding to be applied selectively to the
   transfer of individual bundles on a case by case basis.

   The definition and use of FEC follows the FECFRAME framework defined
   in [RFC6363], and this document introduces new Message types to BTPU
   in order to carry the FEC information as defined in the framework.
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
- **draft-ietf-intarea-extended-icmp-nodeid-05** (new-draft, score 0, ignored_after_review) [intarea]: [ICMP Message Extension for Originating Node Identification](https://datatracker.ietf.org/doc/draft-ietf-intarea-extended-icmp-nodeid/) — RFC5837 describes a mechanism for Extending ICMP for Interface and
   Next-Hop Identification, which allows providing additional
   information in an ICMP error that helps identify interfaces
   participating in the path.  This is especially useful in environments
   where a given interface may not have a unique IP address to respond
   to, e.g., a traceroute.

   This document introduces a similar ICMP extension for Node
   Identification.  It allows providing a unique IP address and/or a
   textual name for the node, in the case where each node may not have a
   unique IP address (e.g., a deployment in which all interfaces have
   IPv6 addresses and all next-hops are IPv6 next-hops, even for IPv4
   routes).
- **draft-ietf-intarea-rfc8335bis-05** (new-draft, score 0, ignored_after_review) [intarea]: [PROBE: A Utility for Probing Interfaces](https://datatracker.ietf.org/doc/draft-ietf-intarea-rfc8335bis/) — This document specifies a network diagnostic tool called PROBE.
   PROBE is similar to PING in that it can be used to query the status
   of a probed interface, but it differs from PING in that it does not
   require bidirectional connectivity between the probing and probed
   interfaces.  Instead, PROBE requires bidirectional connectivity
   between the probing interface and a proxy interface.  The proxy
   interface can reside on the same node as the probed interface, or it
   can reside on a node to which the probed interface is directly
   connected.  This document updates RFC 4884 and obsoletes RFC 8335.
- **draft-ietf-ippm-alt-mark-deployment-08** (new-draft, score 0, ignored_after_review) [ippm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-lsr-igp-reverse-spf-algo-03** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Reverse SPF Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-igp-reverse-spf-algo/) — IANA has set up a subregistry called "IGP Algorithm Type" under the
   "Interior Gateway Protocol (IGP) Parameters" registry.  This draft
   introduces a new algorithm type which utilizes the cost in the
   reverse direction on each link.

   This document also discusses using this new algorithm type in
   combination with IGP Flexible Algorithm to compute constraint-based
   paths.
- **draft-ietf-netconf-distributed-notif-21** (new-draft, score 0, ignored_after_review) [netconf]: [Subscription to Notifications in a Distributed Architecture](https://datatracker.ietf.org/doc/draft-ietf-netconf-distributed-notif/) — This document describes extensions to the YANG notifications
   subscription to allow metrics being published directly from
   processors on line cards to target receivers, while subscription is
   still maintained at the route processor in a distributed forwarding
   system of a network node.
- **draft-ietf-nfsv4-posix-acls-02** (new-draft, score 0, ignored_after_review) [nfsv4]: [POSIX Draft ACL support for Network File System Version 4, Minor Version 2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-posix-acls/) — This document proposes four new optional file attributes for NFSv4.2
   to support POSIX ACLs conforming to the withdrawn POSIX 1003.1e draft
   17.  Although never ratified, POSIX ACLs are implemented in widely
   deployed operating systems.  Existing attempts to map between NFSv4
   and POSIX ACL models have been unsuccessful due to semantic
   incompatibilities.  These new attributes allow servers to expose
   POSIX ACLs directly, avoiding lossy mapping.
- **draft-ietf-nfsv4-uncacheable-directories-11** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Dirent Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  Such
   a cache is not invalidated by the directory's change attribute, which
   reflects changes to the directory and its entries but not writes to
   the files those entries name, so it can become stale when another
   client changes one of those files.  In some deployments this produces
   incorrect size and timestamp values often enough to be a problem.
   This document introduces an uncacheable dirent metadata attribute for
   NFSv4.2 that allows a server to identify a directory for which an
   honoring client goes to the server for each enumeration, and does not
   report an entry's attributes from a value it held before that
   READDIR.
- **draft-ietf-nmop-network-anomaly-lifecycle-07** (new-draft, score 0, ignored_after_review) [nmop]: [An Experiment: Network Anomaly Detection Lifecycle](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-anomaly-lifecycle/) — This document defines a structured, iterative lifecycle for network
   anomaly detection systems to enable "human-in-the-loop" refinements.
   Key contributions include defining three lifecycle stages, a state
   machine for anomaly annotations, and YANG data models for
   standardized labeling and exchange.
- **draft-ietf-nmop-simap-concept-13** (new-draft, score 0, ignored_after_review) [nmop]: [SIMAP: Concept, Requirements, and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/) — This document defines the concept of Service & Infrastructure Maps
   (SIMAP) and identifies a set of SIMAP requirements and use cases.
   The SIMAP was previously known as Digital Map. SIMAP evolves the
   earlier 'Digital Map' concept by making explicit the ties between
   service and infrastructure layers, clarifying expected outcomes for
   operations and automation, and addressing ambiguity associated with
   the term 'digital.'

   The document intends to be used as a reference for the assessment of
   the various topology modules to meet SIMAP requirements.
- **draft-ietf-opsawg-rfc5706bis-07** (new-draft, score 0, ignored_after_review) [opsawg]: [Guidelines for Considering Operations and Management in IETF Specifications](https://datatracker.ietf.org/doc/draft-ietf-opsawg-rfc5706bis/) — New Protocols and Protocol Extensions are best designed with due
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
- **draft-ietf-pce-sr-p2mp-policy-20** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-flex-algo-01** (new-draft, score 0, ignored_after_review) [pim]: [Multi-Topology in PIM](https://datatracker.ietf.org/doc/draft-ietf-pim-flex-algo/) — PIM usually uses the shortest path computed by routing protocols to
   build multicast tree.  Multi-Topology Routing is a technology to
   enable service differentiation within an IP network.  IGP Flex
   Algorithm provides a way to compute constraint-based paths over the
   network.  This document defines the PIM message extensions to provide
   a way to build multicast tree through the specific topology and
   constraint-based path instead of the shortest path.
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
- **draft-ietf-pim-igmp-mld-snooping-yang-l2vpn-ext-09** (new-draft, score 0, ignored_after_review) [pim]: [IGMP and MLD Snooping Yang Module Extension for L2VPN](https://datatracker.ietf.org/doc/draft-ietf-pim-igmp-mld-snooping-yang-l2vpn-ext/) — Internet Group Management Protocol (IGMP) and Multicast Listener
Discovery (MLD) Snooping could be used in both bridge service and L2VPN
service. The old ietf-igmp-mld-snooping yang module just describes the
bridge service. In this document we extend the existing ietf-igmp-mld-
snooping yang module and make it could be used in L2VPN service.
- **draft-ietf-quic-reliable-stream-reset-11** (new-draft, score 0, ignored_after_review) [quic]: [QUIC Stream Resets with Partial Delivery](https://datatracker.ietf.org/doc/draft-ietf-quic-reliable-stream-reset/) — QUIC defines a RESET_STREAM frame to abort sending on a stream.  When
   a sender resets a stream, it also stops retransmitting STREAM frames
   for this stream in the event of packet loss.  On the receiving side,
   there is no guarantee that any data sent on that stream is delivered.

   This document defines a new QUIC frame, the RESET_STREAM_AT frame,
   that allows resetting a stream, while guaranteeing delivery of stream
   data up to a certain byte offset.
- **draft-ietf-regext-epp-https-05** (new-draft, score 0, ignored_after_review) [regext]: [Extensible Provisioning Protocol (EPP) Transport over HTTPS](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-https/) — This document describes how an Extensible Provisioning Protocol (EPP)
   connection is mapped onto the Hypertext Transfer Protocol (HTTP).
   EPP over HTTP (EoH) requires the use of Transport Layer Security
   (TLS) to secure EPP information (i.e. HTTPS).
- **draft-ietf-satp-usecases-10** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer (SAT) Use Cases](https://datatracker.ietf.org/doc/draft-ietf-satp-usecases/) — This document describes prominent scenarios where enterprise systems
   and networks maintaining digital assets require the ability to
   securely transfer assets or data to each other.
- **draft-ietf-spring-sid-as-source-address-00** (new-draft, score 0, ignored_after_review) [spring]: [SID as source address in SRv6](https://datatracker.ietf.org/doc/draft-ietf-spring-sid-as-source-address/) — SRv6 is being rapidly deployed and is currently primarily used in
   trusted-domain backbone networks.  Both the carrier market and the
   enterprise market are adopting SRv6 for end-to-end service delivery.
   However, if a firewall exists along an SRv6 path, not only legitimate
   SRv6 traffic but also ICMP packets generated on SRv6 transit node
   will be dropped.  This proposal addresses this issue by using SID as
   source address in SRv6 packets.
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
- **draft-irtf-iccrg-pacing-03** (new-draft, score 0, ignored_after_review) [iccrg]: [Pacing in Transport Protocols](https://datatracker.ietf.org/doc/draft-irtf-iccrg-pacing/) — Applications or congestion control mechanisms can produce bursty
   traffic which can cause unnecessary queuing and packet loss.  To
   reduce the burstiness of traffic, the concept of evenly spacing out
   the traffic from a data sender over a round-trip time known as
   "pacing" has been used in many transport protocol implementations.
   This document gives an overview of pacing and how some known pacing
   implementations work.
- **draft-jennings-moq-discovery-02** (new-draft, score 0, ignored_after_review) [none]: [DNS and mDNS Discovery for MOQT](https://datatracker.ietf.org/doc/draft-jennings-moq-discovery/) — This document defines how MOQT clients discover server endpoints
   using DNS and Multicast DNS (mDNS).  It specifies SVCB and HTTPS DNS
   record mappings for the moqt URI scheme, SRV records as a fallback
   mechanism, and DNS-SD over mDNS for local network discovery.
- **draft-kalosha-stb-tls13-00** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-koch-librepgp-06** (new-draft, score 0, ignored_after_review) [none]: [LibrePGP Message Format](https://datatracker.ietf.org/doc/draft-koch-librepgp/) — This document specifies the message formats used in LibrePGP.
   LibrePGP is an extension of the OpenPGP format which provides
   encryption with public-key or symmetric cryptographic algorithms,
   digital signatures, compression and key management.

   This document is maintained in order to publish all necessary
   information needed to develop interoperable applications based on the
   LibrePGP format.  It is not a step-by-step cookbook for writing an
   application.  It describes only the format and methods needed to
   read, check, generate, and write conforming packets crossing any
   network.  It does not deal with storage and implementation questions.
   It does, however, discuss implementation issues necessary to avoid
   security flaws.

   This document is based on: RFC 4880 (OpenPGP), RFC 5581 (Camellia in
   OpenPGP), and RFC 6637 (Elliptic Curves in OpenPGP).
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
- **draft-liu-sidrops-rpki-rtr-over-quic-04** (new-draft, score 0, ignored_after_review) [none]: [RPKI to Router Protocol over QUIC](https://datatracker.ietf.org/doc/draft-liu-sidrops-rpki-rtr-over-quic/) — The Resource Public Key Infrastructure (RPKI) to Router Protocol
   provides a simple but reliable mechanism to receive cryptographically
   validated RPKI prefix origin data and router keys from a trusted
   cache.  RPKI to Router (RTR) Protocol can be carried over various
   transports such as TCP, SSH or else.  QUIC provides practical and
   secure semantics for the RTR protocol, particularly fast connection
   establishment and multi-stream carrying, thereby reducing the time
   required to complete RTR data synchronization.  This document
   describes how to use RTR Protocol over the QUIC transport protocol,
   named RTRoQUIC.
- **draft-llz-bier-ipfix-bier-00** (new-draft, score 0, ignored_after_review) [none]: [Export of BIER Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-llz-bier-ipfix-bier/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements (IEs) to identify a set of information related
   to Bit Index Explicit Replication (BIER) such as data contained in
   BIER header that traffic is being forwarded with.
- **draft-nygate-ippm-mrl-00** (new-draft, score 0, ignored_after_review) [none]: [Mouth-to-Ear Response Latency for Conversational Voice Systems: Metric Definition and Active Measurement Method](https://datatracker.ietf.org/doc/draft-nygate-ippm-mrl/) — This document defines mouth-to-ear response latency (MRL), a
   performance metric for conversational voice systems, together with an
   active method for measuring it at the RTP reference point of the
   calling endpoint.  MRL is the interval between the transmission of
   the final speech sample of a caller's utterance and the arrival of
   the first sample of the system's response audio.  Two variants are
   defined, one taken at packet arrival and one taken behind a de-jitter
   buffer of stated target depth.  The method is specified so that both
   timestamps are drawn from a single clock on a single host, so that
   the metric requires no synchronisation between the measuring endpoint
   and the system under test.  Requirements for stimulus material,
   capture content, quality control, calibration and reporting are
   given.
- **draft-pradeepkumarxplorer-videosurfing-00** (new-draft, score 0, ignored_after_review) [none]: [The LIMITS SMTP Service Extension](https://datatracker.ietf.org/doc/draft-pradeepkumarxplorer-videosurfing/) — To allow browsing in videos
- **draft-prz-lsr-ash-packets-01** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
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
- **draft-traffic-analysis-and-network-mode-mapping-03** (new-draft, score 0, ignored_after_review) [none]: [Network Traffic Analysis and Network Modal Mapping Method](https://datatracker.ietf.org/doc/draft-traffic-analysis-and-network-mode-mapping/) — This document presents a framework for network traffic classification
   and modality mapping based on large language models (LLMs),
   addressing the inefficiencies of traditional methods in dynamic
   network environments.  The proposed approach automates multi-
   dimensional traffic feature extraction and intelligent decision-
   making to achieve precise alignment between traffic patterns and
   computing-storage-transmission requirements.  The framework comprises
   two phases: pre-training (generating multi-modal traffic
   representations from pcap data) and mapping (dynamically formulating
   resource allocation strategies).  It supports anomaly detection, QoS
   assurance, and multi-service collaboration, thereby significantly
   enhancing resource utilization efficiency and network service
   performance.
- **draft-xiao-fann-fast-cnp-with-proxy-03** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-xsaopig-nsttlp-traffic-labeling-01** (new-draft, score 0, ignored_after_review) [none]: [Network Service Type-Aware Traffic Labeling Protocol (NST-TLP)](https://datatracker.ietf.org/doc/draft-xsaopig-nsttlp-traffic-labeling/) — This document specifies a protocol mechanism for embedding service
   type identifiers into network packets in order to enable intelligent
   traffic recognition, policy-based forwarding, and resource
   optimization by network devices.  The protocol allows standardized
   service type labels to be carried in IPv4/IPv6 headers, MPLS labels,
   or Ethernet frame headers.  It is applicable to a wide range of
   services, including immersive VR (e.g., 1080p, 4K), scientific
   computing, real-time communications, and Internet of Things (IoT)
   applications.
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
- **draft-zhu-space-distributed-computing-requirements-00** (new-draft, score 0, ignored_after_review) [none]: [Network Support for Distributed Computing in Space Networks](https://datatracker.ietf.org/doc/draft-zhu-space-distributed-computing-requirements/) — Distributed execution can be useful in space networks when one node
   lacks enough computing, storage, energy, or execution time, or when
   data is spread across multiple nodes.  It can also enable parallel
   processing or allow different execution stages to run on different
   space or terrestrial nodes.  A task may therefore create multiple
   communication relationships that appear, coexist, change, and end as
   execution progresses.  Because satellite motion changes connectivity
   over time, reachability alone is not enough to determine whether an
   execution endpoint can support the required communication.

   This document analyzes the network role in such distributed execution
   in the space network.  It considers how network information affects
   execution decisions, how those decisions create communication
   requirements and relationships, when communication over a
   relationship is ready for use, and how relationships change as
   execution and connectivity evolve.

## Errors / fetch failures

- draft-sun-single-stack-100: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-sun-single-stack-100/doc.json
