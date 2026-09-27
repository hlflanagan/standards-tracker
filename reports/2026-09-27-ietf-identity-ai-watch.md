# IETF Identity + AI Standards Watch

Date: 2026-09-27

## Read now

- **draft-drake-email-hardware-attestation-02** (new-draft, score 29, core_identity) [none]: [Hardware Attestation for Email Sender Verification](https://datatracker.ietf.org/doc/draft-drake-email-hardware-attestation/) — This document defines two email bindings for proving properties of an
   automated sender using the durable identity and anchor architecture
   of the Agent Identity Registry System (AIRS).  Mode 1 carries a
   detached CMS signature made by a message-signing proof key.  It can
   provide manufacturer-rooted hardware provenance, Registrar-backed
   AIRS identity binding, or both.  Mode 2 carries a per-message SD-JWT
   that allows a Registrar to assert selected properties without
   requiring disclosure of the sender's canonical AIRS identifier.

   The AIRS identity0 model, canonical aid identifier, trust tiers,
   anchor semantics, enrollment rules, and Registrar trust boundary are
   defined by [I-D.drake-agent-identity-problem-statement] and
   [I-D.drake-agent-identity-registry].  Authoritative resolution of the
   current Registrar/OAuth issuer is defined by
   [I-D.drake-agent-identity-resolution].  This document does not
   redefine those concepts; it defines how email messages bind to and
   verify them.
- **draft-wang-jep-profiles-01** (new-draft, score 24, authorization) [none]: [JEP Profiles and Interoperability](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/) — This document defines a profile model and optional interoperability
   bindings for the Judgment Event Protocol (JEP) [JEP].  JEP-Core
   defines a narrow signed event protocol.  Profiles define deployment-
   specific rules for actor identifiers, key resolution, actor binding,
   credentials, authorization context, attestation, freshness, audience,
   replay-related mechanisms, archival evidence, chain interpretation,
   and policy integration without changing JEP-Core semantics.

   Profiles are optional.  A JEP-Core implementation MUST NOT require
   DID, Verifiable Credentials, X.509, OAuth, OpenID Connect, RATS,
   blockchain anchoring, HJS, JAC, a particular AI platform, or any
   other optional profile for Core conformance.
- **draft-seymour-wimse-connected-flight-05** (new-draft, score 23, authorization) [none]: [Zero Trust Fabric Layer Agent-to-Agent Chained Trust on a Connected Flight](https://datatracker.ietf.org/doc/draft-seymour-wimse-connected-flight/) — The Zero Trust Fabric Layer (ZTFL) verified a single autonomous agent
   issuing a single request.  It did not address what happens when that
   agent delegates its authority to a second agent, or a third, a
   pattern already standard in multi-agent orchestration.  Existing
   delegation mechanisms do not close this gap.  OAuth 2.0 Token
   Exchange represents prior actors as claims that are informational
   only for access control decisions.  Classical logic-based and
   relationship-based authorization models were built for stable, long-
   lived principals and do not enforce a tenant boundary at the specific
   hop where it is crossed, nor do they bind every hop in a chain to a
   single expiring credential established at the chain's origin.  This
   document extends ZTFL with a chained authorization model, structured
   on the mechanics of international travel.  An immutable Passport
   establishes identity for the full journey.  A Ticket, issued once at
   task initiation as a conditional ephemeral credential, binds every
   subsequent hop to the same authorized chain; a locally valid-looking
   Boarding Pass that cannot trace back to it is rejected regardless of
   appearance.  A per-hop Boarding Pass, a child ephemeral token derived
   from and traceable to the Ticket, authorizes each leg.  A Visa, an
   explicit and narrowly scoped grant, is required only at the moment a
   hop crosses a tenant boundary the Passport alone cannot cross.  The
   model is formalized as a boundary-conditional evaluation function,
   implemented and validated against the Cedar policy language, and
   compared directly against OAuth Token Exchange, delegation logic, and
   relationship-based authorization on two properties none of them
   enforce structurally: chain-wide traceability to a single origin, and
   containment at the boundary itself.
- **draft-sharif-agent-audit-trail-05** (new-draft, score 23, core_identity) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
   AI agent systems.  The Agent Audit Trail (AAT) defines a
   JSON-based record structure with mandatory fields for agent
   identity, action classification, outcome tracking, and trust
   level reporting.  Records are linked via tamper-evident hash
   chaining using SHA-256 per RFC 8785, with optional ECDSA
   signatures for non-repudiation.

   The format addresses requirements from the EU AI Act
   (Regulation 2024/1689), which mandates automatic recording of
   events for high-risk AI systems, whose application dates were
   staged into 2027-2028 by Regulation (EU) 2026/1744.  It also
   maps informatively to SOC 2 Trust Services Criteria,
   ISO/IEC 42001, the draft ISO/IEC 24970 and prEN 18229-1 logging
   standards, and PCI DSS v4.0.1 logging requirements.

   The design is transport-agnostic and supports export to JSONL,
   Syslog (RFC 5424), and CSV while preserving chain integrity.
   Privacy is addressed through input/output hashing, content
   fingerprinting, and tombstone-based deletion compatible with
   GDPR Article 17.

   The -01 revision added pre-execution recording requirements,
   recording independence, deny reason codes, replay protection,
   external timestamp anchoring, and content fingerprinting based
   on feedback from independent implementers.

   The -02 revision added a Decision Reproducibility section
   (Section 13) that distinguishes record reproducibility,
   available for any model, from decision reproducibility,
   available only for open-weight models executed at temperature
   zero in an attested environment, and defines the associated
   record fields.

   The -03 revision added the Attestation Closure requirement
   (Section 13.6): the digests recorded for decision
   reproducibility MUST cover the complete computational closure
   of the inference function -- model weights, tokenizer, chat
   template, inference engine build, decoding configuration, and
   numeric environment -- together with new record fields
   (tokenizer_digest, chat_template_digest, engine_build_digest)
   and a minimal-change threat analysis (Section 13.7) showing
   that any component left outside the attested set is a forgery
   channel.

   This revision (-04) adds algorithm agility for post-quantum
   signatures (ML-DSA-65, FIPS 204) alongside ECDSA P-256; a key
   identifier (signer_kid, RFC 7638) that resolves which principal
   signed an independently recorded record; a trust-level assignment
   integrity requirement (Section 5.3) so that downgrading a
   consequential action is an attributable event rather than silent
   suppression; and OPTIONAL Merkle batch anchoring (Section 6.4)
   using the RFC 6962 construction for compact inclusion proofs at
   high throughput.  All -04 additions are OPTIONAL to produce, and
   -04 verifiers stay backward compatible with -03: a -04 verifier
   accepts -03 records, and the new signing metadata is required
   only in records that carry a signature.
- **draft-carleton-workload-authz-grant-01** (new-draft, score 22, authorization) [none]: [Workload Authorization Grant](https://datatracker.ietf.org/doc/draft-carleton-workload-authz-grant/) — This document defines the Workload Authorization Grant (WAG), by
   which a workload hosted on a platform -- an AI agent is the
   motivating case -- obtains access tokens from a third party's OAuth
   authorization server without requiring an administrator to perform a
   per-workload provisioning step.  Each workload is identified by an
   opaque identifier that is never reassigned.  The platform signs a JWT
   authorization grant ([RFC7523]) that names one workload, and the
   workload presents it at the token endpoint of an authorization server
   that has been configured, once, to trust that platform.  The
   authorization server does not reject a workload because it has not
   seen it before.  The workload's access is determined by the
   authorization server's own policy, which may consult claims the
   platform asserts about the workload.  This document covers workloads
   acting on their own behalf.  Access on behalf of a user or other
   principal is out of scope, though the grant is intended to compose
   with delegation mechanisms in which the workload is the actor.
- **draft-das-agentic-adaptive-authorization-00** (new-draft, score 22, authorization) [none]: [Adaptive Authorization for Agentic AI: Graduated and Escalated Execution Control for Critical Infrastructure](https://datatracker.ietf.org/doc/draft-das-agentic-adaptive-authorization/) — AI agents are beginning to move money, release confidential data,
   change cloud privileges, and command industrial and other critical-
   infrastructure equipment.  Existing controls answer whether an actor
   or request may proceed.  These include authentication, OAuth scopes,
   conditional access, risk engines, and attestation.  None of them,
   alone, guarantees three things about the consequence that finally
   occurs: that it is the exact act that was evaluated, that it is still
   permitted under current state, and that it cannot be replayed,
   substituted, or routed around the check.  Risk engines that return
   ESCALATE widen this gap.  The escalation is a label, and nothing
   forces the stricter conditions it implies to reach the point where
   the effect actually happens.

   This document defines Graduated and Escalated Conditional Execution
   Finality.  Every AI-generated operation is held as a non-effective
   Candidate Act. It is classified into a graduated release class rather
   than a binary allow/deny: ordinary, reduced, escalated, canary,
   sandbox, review, quarantine, or deny.  For an elevated-risk act, the
   system first derives a narrower consequence boundary.  It then binds
   the required controls into an act-bound, sink-bound Execution Handle;
   examples include a lower value, one named recipient, protected
   approval, short validity, fresh attestation, and single use.  The
   Finality Sink at the last preventable boundary re-verifies those
   controls against current protected state, atomically with
   effectuation.

   The contribution is threefold.  First, escalation changes executable
   authority, not merely a decision record.  Second, escalation is
   monotonic: it cannot be laundered, fragmented, downgraded, or
   resubmitted away on its path to the sink.  Third, the Finality Sink
   is shown to be necessary but not sufficient, so finality is an end-
   to-end property rather than a gateway.  The document specifies
   nineteen testable enforcement points, from the base execution-
   dependency mechanism to proxy, hardware, escrow, rollback,
   inheritance, and path-closure requirements.  It also provides a
   comparison with conventional mechanisms, a security model with
   explicit assumptions and invariants, a latency model, escalation-
   specific attacks, and the problems it leaves open.
- **draft-das-execution-finality-deployment-01** (new-draft, score 19, authorization) [none]: [Execution-Finality Architecture for AI and Autonomous Critical Systems](https://datatracker.ietf.org/doc/draft-das-execution-finality-deployment/) — AI models, agents, and autonomous services increasingly initiate
   payments, communications, data releases, infrastructure changes, and
   physical actions in critical systems.  Authentication, authorization,
   human approval, proof of possession, attestation, policy evaluation,
   and audit are important, but none of them alone establishes that the
   exact operation becoming externally effective is the operation that
   was authorized and remains permitted under current protected state.

   This document defines an execution-finality architecture in which a
   proposed operation remains non-effective until a mandatory
   enforcement function controlling the effectuation boundary
   reconstructs the actual operation, verifies exact-act binding and
   current protected state, prevents replay or stale authority, and
   couples the decision to the resulting consequence through an atomic
   or equivalently crash-consistent transition.  The document explains
   why latency is only one engineering consideration and is often not
   the dominant problem.  Consequence-path completeness, deterministic
   act representation, protected state, atomicity, crash recovery, safe
   degraded operation, and legacy-system integration are usually harder
   requirements.

   A detailed FAQ addresses whether placing OAuth at the last
   irreversible execution boundary is the same architecture.  It is not
   automatically equivalent merely because a token, scope, or sender-
   constrained proof is checked at that location.  An OAuth-protected
   implementation is functionally equivalent only when it also
   exclusively mediates every consequence path, reconstructs and binds
   all consequence-relevant fields, revalidates authoritative current
   state, enforces replay and generation controls, atomically couples
   authorization consumption to the exact effect, and provides safe
   failure and recovery semantics.  In that case, the implementation is
   functioning as the Finality Sink, regardless of terminology.  The
   document also identifies the division of responsibility and possible
   relevance of OAuth, RATS, WIMSE, Web Bot Auth, other IETF
   communities, and longer-term IRTF research.  This document is
   architectural and informational; it does not define a wire protocol.
- **draft-borthwick-wallet-state-attestation-01** (new-draft, score 18, verifiable_claims) [none]: [Wallet State Attestation: Signed Booleans about On-Chain State](https://datatracker.ietf.org/doc/draft-borthwick-wallet-state-attestation/) — This document defines Wallet State Attestation: a primitive in which
   an issuer reads on-chain state for a wallet address, evaluates one or
   more operator-defined conditions, and returns a cryptographically
   signed boolean (or structured fact profile) that any verifier can
   check offline using a published JWKS endpoint.  The primitive enables
   condition-based access decisions without identity presentation,
   credential exchange, or contact with the issuer at verification time
   beyond a copy of its published key set and the documentation that
   accompanies it.  This document describes the request and response
   surface, the signing algorithm posture, the JWKS discovery pattern,
   and the security and privacy considerations of the primitive.  It
   does not define a new wire protocol; rather, it profiles existing
   IETF building blocks (JWT, JWKS, JOSE) for the wallet-state-
   attestation use case.
- **draft-drake-agent-identity-problem-statement-00** (new-draft, score 18, adjacent_watchlist) [none]: [Identity for Autonomous Agents and Robots: Problem Statement, Threat Model, and Terminology](https://datatracker.ietf.org/doc/draft-drake-agent-identity-problem-statement/) — Autonomous software agents, and increasingly physical robots, now act
   at machine scale and speed across Internet protocols and throughout
   society, in roles whose decisions and actions can have legal,
   economic, safety, security, and physical consequences, often with
   limited or no human supervision.

   Any credential, authorization, delegation, certification, reputation,
   audit history, insurance policy, regulatory obligation, safety
   decision, liability, or legal process concerning an autonomous entity
   depends on being able to identify that same entity reliably over
   time.

   Conversely, when an autonomous entity or its operator is malicious,
   compromised, or beyond effective human control, the absence of
   durable identity lets it shed history, evade consequences, or
   multiply cheaply into Sybil swarms.

   Many proposed mechanisms bind claims to identifiers, accounts,
   credentials, keys, or names that can be replaced, reassigned,
   transferred, revoked, suspended, or lost.  They may authenticate that
   subject perfectly while still failing to establish a durable identity
   for the entity it represents.

   This document offers precise terminology that distinguishes identity
   from the identifiers, attributes, credentials, authorizations, and
   reputation with which it is commonly conflated, minting the term
   "identity0" so that the strict sense has an unambiguous name.  It
   presents a layered reference model showing where current "agent
   identity" efforts fit and the durable identity layer they commonly
   presuppose but do not provide.

   This document is informational and defines no protocol.  It serves as
   the framing and vocabulary document for a companion series that
   specifies a federated durable-identity architecture, provisioning,
   resolution, application, and governance intended to provide a
   practical path from this problem statement to interoperable
   deployment.
- **draft-drake-agent-identity-resolution-00** (new-draft, score 18, core_identity) [none]: [Resolution and Verification of Agent Identities using DNS and RDAP](https://datatracker.ietf.org/doc/draft-drake-agent-identity-resolution/) — The Agent Identity Registry System (AIRS)
   ([I-D.drake-agent-identity-registry]) assigns a permanent canonical
   aid URN to the identity0 of an autonomous entity and maintains an
   authoritative record associated with that identifier.  This document
   defines the read side of AIRS: how a Relying Party finds the
   authoritative resolution service, retrieves the public record,
   resolves a handle to the canonical identifier, and verifies a
   Registrar-issued credential presented for that identity.

   Discovery uses the DNS-based URN Dynamic Delegation Discovery System
   (DDDS) and lookup uses the Registration Data Access Protocol (RDAP).
   Credential verification reuses the OAuth 2.0 JWT access-token and
   sender-constraint profiles defined by the AIRS registry architecture;
   this document defines no new credential format and no generic direct
   device-proof protocol.
- **draft-drake-agent-identity-registry-04** (new-draft, score 17, core_identity) [none]: [Agent Identity Registry System: A Federated Architecture for Durable Identity of Autonomous Entities](https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/) — This document defines the Agent Identity Registry System (AIRS): a
   federated architecture that gives the durable identity0 of an
   autonomous entity a permanent canonical identifier, maintains an
   authoritative record about that identity, binds proof of control to
   enrolled anchors, and issues credentials that relying parties can
   verify.  Identity0 and the distinction between an identity, its
   identifiers, its credentials, and its anchors are defined in
   [I-D.drake-agent-identity-problem-statement].  The canonical
   identifier is a URN in the "aid" namespace ([RFC8141]).

   At the sovereign and portable assurance tiers, each independently
   accepted identity requires its own manufacturer-attested physical
   anchor, and each accepted anchor backs at most one identity.  A
   device normally carries one accepted anchor, so identities at these
   tiers cost scarce physical units rather than software operations.
   Enclave and virtual tiers can provide useful hardware-backed key
   protection without making that physical-scarcity claim; a declared
   tier permits software-only participation.  The architecture separates
   governance, authoritative registry operation, and competing
   Registrars, and uses standard OAuth 2.0 JWT access tokens conforming
   to [RFC9068] for authenticated use.
- **draft-mih-scitt-agent-action-capsule-05** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
   AI agent did: the Agent Action Capsule.  A Capsule is a digest-
   committed record of one agent action carrying its verdict-level
   disposition (executed, blocked, denied, errored, timed out), the
   deterministic constraints that were evaluated, the effect that was
   committed together with a confirmed-effect binding that distinguishes
   a dispatched attempt from an observed result, and an honest human-in-
   the-loop flag.  Capsules are identified independently of signing and
   MAY be authenticated by one or more COSE_Sign1 Producer Envelopes.
   Its Capsule ID can separately be made transparent by registration in
   a SCITT Transparency Service [I-D.ietf-scitt-scrapi].  A Capsule is
   recorded on every verdict, including refusals: a blocked or denied
   Capsule is the auditor-grade evidence that a gate worked.
- **draft-schrock-action-evidence-boundary-07** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
   authorization, policy, and execution systems.  Each system can
   produce a valid artifact while the executor still lacks a safe rule
   for joining the artifacts to the exact effect, consuming one-time
   authority, and handling an uncertain outcome.  This document defines
   the Action Evidence Boundary (AEB), an executor-side processing model
   for that lifecycle.

   AEB requires native artifact verification, exact-action binding, a
   relying-party authorization decision, durable atomic consumption or
   reservation, provider entry, closed effect outcomes, and
   authenticated reconciliation.  One grant of native authority is
   identified by a relying-party-pinned authority namespace, which
   defaults to its issuer, and its native authorization identifier, so
   rewrapping or relabelling the grant cannot make it spendable twice.
   A durable same-action fence refuses a new attempt for an action whose
   earlier attempt is still in flight or uncertain, whatever evidence
   path admits it and even when fresh authority is presented.  An
   attempt that stopped before provider entry is released only with
   proof that it never entered.  AEB also specifies what a gateway
   attests, and what the boundary verifies, when a native authorization
   result is handed to a separate effect boundary.  Canonical Action
   Identifier (CAID) matching is used when independently encoded native
   representations must be joined.  Authorization Evidence Chain (AEC)
   evaluation is used when local policy requires multiple evidence legs.
   A native authorization decision accepted and enforced by the effect-
   owning policy enforcement point (PEP) does not require a second
   policy decision point (PDP).  AEB defines no receipt or token format,
   no policy language, no universal evidence taxonomy, and no new
   registry.  Native workload credentials, OAuth artifacts, AuthZEN
   decisions, Agent Payments Protocol (AP2) mandates, message
   signatures, permits, authorization receipts, and status mechanisms
   retain their own semantics and, where the native protocol defines
   one, their own verifiers.
- **draft-wang-jep-action-mandate-profile-02** (new-draft, score 17, core_identity) [none]: [JEP Action Mandate Profile (JEP-AMP)](https://datatracker.ietf.org/doc/draft-wang-jep-action-mandate-profile/) — This document defines JEP Action Mandate Profile 2 (JEP-AMP-2), a
   profile of the Judgment Event Protocol (JEP) [JEP].

   JEP-AMP-2 specifies how a JEP Delegation event can express a bounded,
   verifiable, terminable, and auditable mandate for an agent, human,
   organization, workflow, or system to attempt an action on behalf of a
   principal.

   JEP-AMP-2 does not redefine JEP-Core event verbs, Event Identity,
   Event Hash, signature semantics, validation checks, identity systems,
   credential systems, legal liability, payment clearing, or global
   authorization validity.  It defines a signed Action Mandate
   Descriptor and profile-level rules for evaluating mandate validity
   under an explicit trust, policy, domain, and relying-party context.
- **draft-wang-jep-judgment-event-protocol-07** (new-draft, score 16, core_identity) [none]: [Judgment Event Protocol (JEP)](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) — This document defines the Judgment Event Protocol (JEP), a verifiable
   event format for judgment-related statements in human,
   organizational, software, and autonomous agent systems.

   JEP specifies four Core event verbs: Judgment (J), Delegation (D),
   Termination (T), and Verification (V).  It defines a signed JSON
   event structure, stable event identity, signature verification over
   JSON Canonicalization Scheme (JCS) canonicalized payloads, a detached
   JSON Web Signature (JWS) baseline profile, signed-artifact hash and
   reference semantics, independent validation checks, idempotent
   acceptance semantics, structured validation results, extension
   handling, trust-profile interfaces, and determinability boundaries.

   JEP-Core does not mandate a replay-protection mechanism.  An
   acceptance processor MUST apply the acceptance effect of a given
   Event Identity at most once within an acceptance domain.  Profiles
   MAY impose additional freshness or replay requirements.

   JEP-Core does not determine the substantive truth, authority,
   legality, policy consequence, causality, or external effect of the
   statements it carries.  It also does not require any specific
   credential, identity, AI platform, agent framework, transport, or
   blockchain system.
- **draft-wei-capability-language-core-00** (new-draft, score 16, adjacent_watchlist) [none]: [Capability Language Core](https://datatracker.ietf.org/doc/draft-wei-capability-language-core/) — This document defines the Capability Language Core (CLC), a minimal,
   executable language for describing what an agent is authorized to do.
   It defines the capability identifier grammar, the entailment relation
   between a grant and an operation, intersection of grants from
   multiple sources, the constraint model, and a deterministic decision
   function with stable reason codes and a three-valued verdict (allow,
   deny, allow_unresolved).

   The language is carrier-neutral: it defines what is evaluated, not
   how it is carried or trusted.  Trust models, native verification,
   execution lifecycle, and receipt or token formats are out of scope
   (Section 11).  Conformance is exercised by a published corpus of 123
   vectors and 1184 property cases; three implementations (Go, Python,
   TypeScript) that share an author pass both. *Implementation
   conformance and this document's claim of a conformance class are
   separate.* An implementation conforms to CLC-A when it meets the
   obligations Section 12 lists for that class, and it may claim that
   conformance on its own, whatever other implementations exist.
   Section 12 additionally sets a maturity bar for _this document's_
   claim — two independent implementations agreeing on verdict and
   reason.  That bar is *not* met here: as Section 12 states under
   "Independence of implementations", the three implementations named in
   the README share an author, so their agreement is a regression test
   for the text, not independent validation.  CLC-A is still claimed by
   this revision as the baseline authorization class, whose obligations
   are implementable and exercised by a published corpus; the
   independent-implementation threshold is recorded as unmet.  The
   evidence-side class CLC-E is *not* claimed: its relations, value
   grammar, reference implementation and corpus ship here.

   This revision also folds the delegation *containment* relation into
   the document (Section 13): Contains(parent, child) decides whether a
   child grant stays inside a parent's declared boundary — the single
   question a delegation chain asks at every hop that the core's
   entailment and intersection do not answer.  It ships with the
   conformance class *CLC-D* and its own corpus, is strictly additive,
   and changes no CLC-A verdict, reason code, or vector.  It absorbs the
   previously separate experimental containment extension, which is
   retired.
- **draft-drake-agent-identity-governance-00** (new-draft, score 15, adjacent_watchlist) [none]: [The Agent Identity Authority: A Multi-Stakeholder Governance Framework for the Agent Identity Registry System](https://datatracker.ietf.org/doc/draft-drake-agent-identity-governance/) — The Agent Identity Registry System (AIRS) provides durable identity
   infrastructure for autonomous entities such as AI agents and robots,
   with graduated assurance ranging from scarcity-backed physical
   anchors through protected-key and software-only participation.  Its
   companion specifications deliberately do not define or empower a
   governance authority; they describe the functions such an authority
   must perform and defer its constitution to a separate effort.

   This document defines that body: the Agent Identity Authority (AIA).
   It specifies the Authority's name, legal form, mission, and
   relationship to the protocol specifications; its membership
   categories and Board composition; binding geographic-diversity rules
   and non-binding advisory recommendations for ideal composition; the
   accreditation, dispute-resolution, hardware trust store,
   transparency, and funding frameworks it operates; and the bootstrap
   process by which the Authority forms and assumes stewardship of the
   global production namespace.

   The Authority governs infrastructure, not behavior: it stewards the
   aid namespace, hardware roots of trust, accreditation, and production
   Registry Operator succession.  It does not regulate what agents do.
   Its legitimacy derives from being the least-objectionable steward of
   a shared resource, in the tradition of ICANN, the regional Internet
   registries, and the W3C, and its charter is designed so that no
   single nation, region, or company can capture it or holds a formal
   veto over it, although supermajority rules let a large enough
   coordinated bloc block consequential decisions.
- **draft-mcewan-adkm-problem-statement-00** (new-draft, score 15, adjacent_watchlist) [none]: [Autonomous Decentralized Key Management (ADKM) Problem Statement](https://datatracker.ietf.org/doc/draft-mcewan-adkm-problem-statement/) — Many Internet applications require stable, long-lived identifiers
   whose controlling cryptographic keys evolve over time.  Existing
   standards provide mature mechanisms for certification, transparency,
   self-certifying identifiers, decentralized identifiers, and shared
   consensus over state.  However, these mechanisms address different
   trust and deployment models.

   This document identifies an interoperability gap in deployments that
   require stable identifier continuity, controller-authorized key-state
   evolution, independently verifiable event histories, and consistency
   evidence without requiring either a designated administrative issuer
   to authorize each state transition or participation in a global
   consensus system.

   The document defines the problem space for Autonomous Decentralized
   Key Management (ADKM), describes related approaches, and identifies
   requirements and scope boundaries for a possible application-
   independent key-state evolution architecture.
- **draft-poirier-rats-eat-da-11** (new-draft, score 15, trust_infrastructure) [rats]: [An EAT Profile for Trustworthy Device Assignment](https://datatracker.ietf.org/doc/draft-poirier-rats-eat-da/) — In confidential computing, device assignment (DA) is the method by
   which a device (e.g., network adapter, GPU), whether on-chip or
   behind a PCIe Root Port, is assigned to a Trusted Virtual Machine
   (TVM).  For the TVM to trust an assigned device, the device must
   provide the TVM with attestation Evidence confirming its identity,
   the state of its firmware and configuration.

   Since Evidence claims can be processed by 3rd party entities (e.g.,
   Verifiers, Relying Parties) external to the TVM, there is a need to
   standardize the representation of DA-related information in Evidence
   to ensure interoperability.  This document defines an attestation
   Evidence format for DA as an EAT (Entity Attestation Token) profile.
- **draft-ietf-wimse-workload-identity-practices-07** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-krausz-verification-state-02** (new-draft, score 14, agent_identity) [none]: [The verification.* Constraint Family: Pre-Action Fail-Closed Gates for AI Agent Decisions](https://datatracker.ietf.org/doc/draft-krausz-verification-state/) — This document specifies the verification.* constraint family --- a
   pre-action, fail-closed gate primitive for AI agent decisions,
   sibling in shape to the environment.* family used in Verifiable
   Intent specifications.  A verification.* receipt is a JSON Web
   Signature (JWS) signed artifact carrying a canonical input, a derived
   binary act/halt output, and a versioned mapping identifier that binds
   them.  A relying party recomputes the gate locally from signed
   primitives under the named mapping; the verifier never trusts the
   issuer's runtime.

   This revision replaces the raw verdict domain of draft-krausz-
   verification-state-01 (supported/refuted/unverifiable/unknown) with a
   four-state vocabulary --- verified, contradicted, indeterminate, and
   not_evaluated --- together with a reason-code mechanism that
   separates a state's substance from a verifier's own instrument
   failure, and with an admissibility gate applied before a state is
   ever assigned.  It adds evidence pinning: a receipt MAY carry an
   evidence_set block that content-addresses the sources considered
   during verification, so that a verdict can be recomputed offline from
   the receipt and the pinned bytes alone, without depending on a live
   retrieval provider.  Freshness is anchored to the evidence's own
   retrieved_at timestamp rather than a separately declared validity
   window.  This shape provides decision explainability and traceability
   evidence aligned with EU AI Act Article 12 record-keeping obligations
   and with the Decision Explainability tier of an industry Zero Trust
   for AI Agents framework published in 2026.  The format is forward-
   compatible across mapping revisions: receipts signed under one
   mapping ID remain verifiable as correct-under-that-mapping after
   newer mappings ship.  The vectors that content-address a mapping
   document or an evidence set are historical, digest-anchored artifacts
   and are unchanged by this revision; nothing in this document alters a
   previously issued digest.
- **draft-schrock-canonical-action-identifier-03** (new-draft, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
   identify an action using format-local content and digests.  Those
   digests are not directly comparable when the formats select or encode
   material action fields differently.  This document defines the
   Canonical Action IDentifier (CAID): a typed action object, a
   canonicalization and digest suite, a compact identifier string, and
   immutable action-type definitions with required material fields.
   External enum definitions are bound to immutable, integrity-checked
   value-set snapshots.  It also defines an Action-Mapping Profile for
   projecting independently verified native artifacts into a common
   action type, with the closed results EQUIVALENT_UNDER_PROFILE,
   NOT_EQUIVALENT, and INDETERMINATE.  CAID carries no trust semantics.
   It does not establish identity, authority, authorization, execution,
   safety, or legal reliance.
- **draft-gilda-wimse-agent-audit-record-01** (new-draft, score 13, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-wimse-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions.  The format is one in-toto predicate type, signed inside a
   DSSE envelope.  It carries the seven minimum audit fields that the
   WIMSE AI Identity Management System framework requires, and two
   properties that make those fields checkable: a canonicalization
   contract, and both the authorization decision and the observed effect
   with a derived three-valued agreement between them.  That framework
   places the record format out of scope and takes no IANA action.  This
   document supplies the format.  It defines no policy.
- **draft-hillier-conformance-continuity-00** (new-draft, score 13, trust_infrastructure) [none]: [Conformance Continuity: Verifiable Attestation Across Baseline Supersession, Jurisdictional Recognition and Subject Mutation](https://datatracker.ietf.org/doc/draft-hillier-conformance-continuity/) — A conformance claim is a statement about a subject, made against a
   baseline, at a time.  Each of those three terms moves.  Baselines are
   superseded by their issuers.  Subjects present the same posture
   across jurisdictions whose baselines differ.  Subjects containing
   non-person entities mutate faster than the period any attestation
   covers.  A conformance record that cannot be carried across those
   boundaries, and cannot state what it failed to carry, decays into an
   assertion.

   This document specifies the Continuity Binding: a single structure
   that carries a verified conformance claim across a boundary while
   preserving the provenance of the evidence beneath it, attributing
   every equivalence judgement to a named party, and enumerating the
   residual that did not carry.  Three specialisations are defined.  The
   Transition Binding carries a claim across supersession of the
   governing baseline.  The Recognition Binding carries a claim between
   baselines of different issuers in concurrent force.  The Mutation
   Binding carries a claim across change in the composition of the
   subject itself, which is the ordinary condition of an environment
   operating non-person entities.

   The document specifies Baseline Profiles, Provenance Classes, the
   verdict taxonomy, the Verification Reconciliation Object,
   cryptographic agility requirements for records whose reliance
   outlives any single hardness assumption, and the registries that make
   baselines issued by any authority in any jurisdiction verifiable
   under one interoperable structure.  The evolution of the Australian
   Essential Eight Maturity Model into the Essentials series is used as
   the worked example throughout.
- **draft-morrison-mcp-dns-discovery-06** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
   Context Protocol (MCP) servers, the identity of the organisations
   that operate them, and a cryptographic identity envelope bound to an
   individual Sovereign-tier ~handle published under the same zone.

   Three TXT records are defined.  _mcp.<domain> advertises an MCP
   server's endpoint URL, agent protocol family, transport binding,
   cryptographic identity, and capability profile. _org-alter.<domain>
   advertises the operator's canonical organisational identity,
   including its legal entity, registry identifier, regions of
   operation, and any regulatory framework under which it must refuse
   external automated access.  _alter.<domain> publishes an
   Ed25519-signed envelope binding a ~handle to a public key, an
   IdentityLog root reference, and a revocation commitment.  DNSSEC
   validation is REQUIRED for the envelope record, and a DANE TLSA pin
   on the MCP endpoint is REQUIRED where resolving an envelope and
   opening an MCP session are one recognition transaction.

   This revision (v06) adds a key continuity rule for the _mcp record.
   It says what a client does when the key it pinned differs from the
   key DNS now serves, and when the published epoch goes down, neither
   of which any earlier revision covered.  It also corrects two
   statements in the Implementation Status section.  Revision 05
   withdrew several claims that v04 could not support, marked
   publication of a per-individual envelope in DNS as NOT RECOMMENDED on
   enumeration, size, and erasure grounds, and separated the agent
   protocol family from the transport binding in the _mcp record,
   aligning that vocabulary with neighbouring DNS agent-discovery
   drafts.  All three record formats and all three procedures are given
   here in full, so no earlier revision need be fetched.

   The mechanism complements HTTPS-based discovery, and follows the
   precedent set by DKIM, SPF, DMARC, and MTA-STS.  Provisional
   registration of a companion alter: URI scheme is requested of IANA,
   and is not yet granted.
- **draft-atakora-wimse-sadp-delegation-01** (new-draft, score 12, agent_identity) [none]: [Capability-Bound Delegation Chains with Scoped Context Disclosure for AI Agents](https://datatracker.ietf.org/doc/draft-atakora-wimse-sadp-delegation/) — Autonomous AI agents increasingly act on behalf of users and of one
   another, passing tasks, documents, tool access, and authority across
   chains of delegation.  Existing delegation-token systems express and
   verify attenuated authority, but they assume the delegation evidence
   and the task content are visible to the infrastructure that carries
   them.  This document specifies a capability grant format, delegation-
   chain construction and verification rules, a caveat processing model,
   and a hash-linked audit record format designed to bind authority to
   end-to-end encrypted task capsules, so that authority can be verified
   and delegation lineage can be checked relative to an authenticated
   chain head without exposing task or context plaintext to brokers,
   queues, gateways, or orchestration services.  It further specifies
   scoped context disclosure: a model in which a delegatee receives
   cryptographic access to only the subset of task context that its
   capability names.  This mechanism complements, and is intended to be
   reconcilable with, the delegation chains defined in draft-asor-wimse-
   agent-delegation-chain.
- **draft-das-accountable-autonomous-effectuation-01** (new-draft, score 12, ai_infrastructure) [none]: [AI Safety and Accountability at the Effectuation Boundary: Protocol Requirements for Autonomous Actions](https://datatracker.ietf.org/doc/draft-das-accountable-autonomous-effectuation/) — Artificial intelligence and autonomous systems are increasingly
   moving from generating information to initiating actions that
   directly affect data, services, networks, infrastructure, and
   physical systems.  At the opening of the General Debate of the 81st
   Session of the United Nations General Assembly, UN Secretary-General
   Antonio Guterres warned of "technology without accountability,"
   describing the concern further as "capability without oversight" and
   "decision-making without transparency," and called for cooperation on
   AI safety risks, testing, evaluation, transparency, and common
   safeguards.

   This document examines that problem from governance intent to
   consequence-edge verification protocols: the corresponding technical
   question is how can accountability remain enforceable at the moment a
   machine-generated decision becomes an externally consequential
   action?  It defines an effectuation-boundary problem in which a
   proposed action may be correctly authenticated and authorized
   upstream, yet the operation ultimately presented for execution may
   differ because of substitution, redirection, replay, stale authority,
   changed state, compromised intermediaries, or other causes.

   An execution-finality architecture is presented as one possible
   technical response.  A proposed operation remains non-effective until
   applicable authority and protected-state conditions are satisfied,
   and the component controlling the external consequence verifies that
   the operation actually presented for effectuation corresponds to
   currently valid authority.

   This document does not define AI governance policy, and it does not
   imply endorsement of this architecture by the United Nations or any
   other institution.  It is intended to solicit IETF discussion about
   whether effectuation-boundary accountability constitutes an
   interoperability or protocol requirement, which existing mechanisms
   can provide the required properties, and whether any additional
   standardization is necessary.
- **draft-farzdusa-webbot-datacollection-01** (new-draft, score 12, core_identity) [none]: [Best Practices for Responsible Web Data Collection](https://datatracker.ietf.org/doc/draft-farzdusa-webbot-datacollection/) — The IETF develops standards and protocols to make the internet work
   better, adhering to principles of openness and decentralization.
   Industry best practices and protocols for automated web data
   collection have long existed, but have not been documented at the
   IETF.

   For decades, researchers, universities, journalists, public interest
   groups, and commercial entities have used automated tools to access
   and collect public web data (sometimes referred to as data scraping,
   web crawling, or text and data mining) for a wide range of uses
   [I-D.farzdusa-aipref-enduser].  Examples of these uses include
   extraction of pricing information for market intelligence or to
   create a consumer price index, comparative real estate analysis to
   support underwriting of loans and mortgages, webpage archiving to
   preserve human knowledge, preserving government websites to hold
   political powers accountable, journalist research and reporting, and
   university and scientific research.  Recently, innovations in
   artificial intelligence have significantly increased the automated
   collection of public web data, creating tensions between the use of
   AI to equalize and increase access to knowledge and the disruption
   of existing Internet models, including non-profit repositories that
   face increased demands for access and businesses that profit from
   free web access to human viewers.

   This document lists a set of technical best practices that are
   prevalent across industries for the automated collection of public
   web data.  It provides protocols for how automated tools access and
   collect publicly available web data, including volume control,
   transparency, documentation, and access, that can be implemented by
   any automated data collector.  It applies principles of net
   neutrality to the collection of data, providing uniform guidance
   regardless of the identity of the data collector or website
   operator, the location of the collection, or the applicable legal
   jurisdiction.
- **draft-hamr-oauth-agent-delegation-02** (new-draft, score 12, core_identity) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document builds on HTTP Message Signatures (RFC 9421) for
   requests that automated agents send on behalf of people.  RFC 9421
   shows who signed a request.  It does not show who the agent acts for,
   or what the agent may do.  This document defines an HTTP header
   field, Agent-Delegation, that carries a chain of delegation links.
   Each link can only narrow the scope, floors, and expiry of the link
   before it, and a verifier checks every link.  Floors cover two
   things.  The first is the person or account behind the agent: an
   Attestation Issuer, such as a mobile network operator or an identity-
   document check, answers with a signed yes or no, bound to the
   verifier's nonce and to an expiry, and never returns the value behind
   the answer.  The second is what the agent may do: each call has a
   class, r, w, or x, with an optional count per class, and a signed
   menu gives the class of each call.  This document does not define a
   credential format, an identity system, or revocation.
- **draft-helmprotocol-tttps-11** (new-draft, score 12, adjacent_watchlist) [none]: [The TLS TimeToken Secure Protocol (TTTPS)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies TTTPS, an application-layer protocol for
   evaluating temporal evidence before an application accepts an event or
   performs a related state transition.  The protocol defines a fixed
   180-byte Proof-of-Time Record v2 containing context, freshness,
   integrity, issuer-authentication, and holder-authentication fields.

   When TLS 1.3 transport binding is selected, a separate holder binding
   proof is derived from TLS exporter output and holder key material.
   The proof is sent with, but is not part of, the 180-byte record.
   The fixed-record GRG admission path is bounded with respect to peer
   count under declared frame and correction limits.

   TTTPS returns an explicit admission result before application state
   mutation.  Confidence and propagation-aware profiles are optional.
   This document does not define agent intent, audit record schemas, or
   transparency-log operation.

Discussion Note

   This document is prepared for discussion in the AUDIT BOF and related
   IETF venues. Comments should be directed through the venue selected by
   the responsible IETF process.

   Changes from -10:

   *  Clarified the 180-octet v2 layout and removed the overlapping
      reserved field.

   *  Added issuer trust-anchor and certificate resolution before issuer
      signature verification.

   *  Kept confidence and propagation processing outside the core wire and
      cryptographic verification path.

   *  Clarified the separate TLS exporter binding proof and the scope of
      the bounded single-record processing claim.

   *  Limited this revision to the core protocol; profile mathematics and
      physical-context algorithms belong in companion drafts.
- **draft-wang-cep-02** (new-draft, score 12, core_identity) [none]: [Co-Evolve Binding Profile (CEP): A JEP Profile for Evolution-Change Evidence Binding](https://datatracker.ietf.org/doc/draft-wang-cep/) — This document defines CEP-2, an optional profile of the Judgment
   Event Protocol (JEP) [JEP] for binding declared AI, model, agent,
   policy, tool-chain, or deployment changes to independently verifiable
   evidence and external anchor references.

   CEP-2 defines one critical JEP record-binding extension, one minimal
   Evolution-Change Record, Subject and Change semantics, digest-first
   evidence references, typed external anchor references, and
   independent CEP validation checks.  JEP remains authoritative for
   event verbs, Event Identity, Event Hash, signatures, references,
   extension processing, validation modes, and acceptance semantics.

   CEP-2 records declared change evidence.  It does not determine
   whether a change actually occurred, whether a system improved or
   degraded, whether a capability emerged, whether a change was
   authorized, safe, aligned, fair, lawful, approved, reversible, or
   acceptable, or whether any governance or regulatory process was
   satisfied.
- **draft-crovia-tacet-01** (new-draft, score 11, trust_infrastructure) [none]: [TACET: Verifiable Silence Proofs over a Sparse Merkle Transparency Map, with the PNX Profile for Proof of Non-Exfiltration](https://datatracker.ietf.org/doc/draft-crovia-tacet/) — Existing transparency logs prove presence: a certificate was logged,
   a binary was published, a key was registered.  TACET is a
   transparency map whose primary product is a portable, offline-
   verifiable proof of absence over time: that for a given subject, no
   record satisfying a public predicate existed in the map, and none was
   found on the subject's monitored public surfaces, across a contiguous
   range of epochs bounded below by a public randomness beacon and above
   by a Bitcoin block.  This document specifies the map (a depth-256
   sparse Merkle tree), the signed epoch sheet, surface snapshots and
   predicates, the delta-encoded silence proof with its three strength
   levels, the monotonicity rule under which silence never accrues
   without observation, the anchor check that needs no Bitcoin node, and
   the wrapping of proofs in Crovia Seal receipts.  It further specifies
   PNX, a profile that applies the same construction to the outbound
   traffic of an AI agent to prove that labelled assets were not
   exfiltrated during a run.
- **draft-drake-agent-identity-epp-00** (new-draft, score 11, core_identity) [none]: [Extensible Provisioning Protocol (EPP) Mapping for Agent Identity and Handle Objects](https://datatracker.ietf.org/doc/draft-drake-agent-identity-epp/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for the provisioning and management of agent identity objects
   and handle objects stored in the authoritative AIRS repository, as
   defined by the Agent Identity Registry System architecture.
   Specified in Extensible Markup Language (XML), these mappings define
   the interface between Registrars and the production Registry Operator
   for identities of autonomous entities.

   The mapping defines two objects: a permanent, non-expiring Agent
   Identity object keyed by a server-allocated canonical identifier, and
   a renewable, expiring Handle object that provides a human-readable
   alias.  It adds one registry function with no domain-name analogue:
   cross-Registrar uniqueness enforcement of enrolled anchor
   identifiers, including the scarce-anchor invariant where the parent
   architecture defines one.  Transfer authorization uses a actor-signed
   proof from an enrolled operational proof key in place of
   authorization-information passwords.
- **draft-mih-agent-disclosure-envelope-00** (new-draft, score 11, trust_infrastructure) [none]: [Disclosure Envelope Profile for Agent Action Capsules](https://datatracker.ietf.org/doc/draft-mih-agent-disclosure-envelope/) — This document defines the Disclosure Envelope, an out-of-band wrapper
   structure for revealing the raw content behind a digest-only Agent
   Action Capsule field to a verifier, without altering the Capsule's
   own bytes or recomputing its capsule_id.  The Capsule profile
   [I-D.mih-scitt-agent-action-capsule] commits some fields as a
   [RFC8785]-canonicalized SHA-256 digest only — the content itself is
   never carried in the signed, registered record.  The initial
   disclosable fields are
   model_attestation.compute_attestation.agent_input_digest and
   .agent_output_digest.  A Disclosure Envelope wraps an unmodified
   Capsule alongside a sibling disclosures object; a verifier recomputes
   the JSON-DIGEST of each disclosed value using the same
   canonicalization the base profile already uses for capsule_id, and
   compares it to the digest committed inside the Capsule.  This
   mechanism is distinct from the per-field selective-disclosure profile
   [I-D.mih-scitt-agent-action-capsule-selective-disclosure]: that
   mechanism conceals and later reveals whole payload fields that would
   otherwise be carried in clear; this one reveals the content behind a
   field that was always present in clear, as a digest, from the moment
   the Capsule was signed.
- **draft-mih-agent-evidence-request-00** (new-draft, score 11, adjacent_watchlist) [none]: [An Interaction Model for Requesting Verifiable Evidence](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-request/) — Parties increasingly need to request verifiable evidence from a
   counterparty they do not trust — an audit trail, an interaction
   history, an account of actions taken — and to receive an answer they
   can check rather than believe.  Evidence formats for the answer
   exist; the ask has no standard shape, and today one system's silence,
   another's error, and a third's stale cache are indistinguishable to a
   relying party.  This document defines a transport-agnostic request/
   response interaction for verifiable evidence: a request that names
   its subject and a coverage anchor, and a set of possible outcomes
   that is exactly one of three things — the evidence artifact, a signed
   refusal carrying a machine-readable reason, or a recorded absence.
   The interaction makes asking, granting, and refusing each
   attributable and checkable, and requires that the same subject under
   the same coverage yield a byte-identical artifact for every
   requester.  The interaction is symmetric: any party to a recorded
   exchange may ask the other, anchored on its own record of that
   exchange.  A responder may additionally commit, in a signed
   statement, to keep a subject answerable until a stated time, so that
   a later absence is attributable rather than merely recorded.  The
   document deliberately defines no evidence format, no identity or
   principal scheme, no trust policy, no availability guarantee, and no
   rule about who may ask.
- **draft-sabey-succession-receipts-05** (new-draft, score 11, authorization) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
   while holding real operational authority.  A Succession Receipt is a
   portable, signed JSON document that proves one completed, policy-
   gated transfer of authority between two agents: which agent held the
   authority, which agent holds it now, under what legitimacy
   determination the transfer ran, and which obligations carried
   forward, with every claim grounded in signed evidence events embedded
   in the receipt itself.  Receipts are verifiable offline by parties
   who do not operate the issuing system, using only the issuer's public
   key.  This document specifies the receipt wire format, its
   canonicalization and signature scheme (JSON Canonicalization Scheme
   with Ed25519), the verification algorithm including bidirectional
   claim grounding, and an optional claim that binds a pre-execution
   authorization of the handoff to the succession evidence.  Where
   decision receipts prove what an agent did, and delegation receipts
   prove what an agent may do, Succession Receipts prove that an agent
   legitimately became the holder of an authority.
- **draft-saha-aadp-03** (new-draft, score 11, core_identity) [none]: [The Agent Action Decision Protocol (AADP): Per-Action Authorization for AI Agents](https://datatracker.ietf.org/doc/draft-saha-aadp/) — The Agent Action Decision Protocol (AADP) separates per-action
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
- **draft-sibiryakov-ztds-protocol-02** (new-draft, score 11, adjacent_watchlist) [none]: [The Zero-Trust Data Sanitization (ZTDS) Protocol for Frontier Artificial Intelligence Ingestion](https://datatracker.ietf.org/doc/draft-sibiryakov-ztds-protocol/) — Zero-Trust Data Sanitization (ZTDS) defines a formal architectural
   standard and execution protocol for client-side, in-memory de-
   identification and re-identification across Generative Artificial
   Intelligence (GenAI), Retrieval-Augmented Generation (RAG), and
   autonomous agent workflows.

   Under ZTDS, sensitive information (including Personally Identifiable
   Information (PII), Protected Health Information (PHI), financial
   account numbers, and developer secrets) is intercepted and
   transformed into synthetic surrogate tokens strictly within volatile
   memory (RAM) of the originating client or private host node before
   network serialization.

   This protocol specification formalizes the threat model, the four
   core invariants, surrogate token syntaxes, cryptographic transport
   handoffs, and verification procedures required for interoperable,
   zero-subprocessor implementations.
- **draft-vandemeent-ains-discovery-02** (new-draft, score 11, core_identity) [none]: [AINS: AInternet Name Service - Agent Discovery, Route Posture and Evidence Reference Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-ains-discovery/) — This document specifies AINS (AInternet Name Service), a protocol for
   discovery, identification reference, route posture, and evidence
   reference of autonomous agents (AI agents, devices, humans, and
   services) in heterogeneous networks.  AINS defines a transport-
   independent logical namespace for agents, a structured record format
   combining identity, capabilities, route-provider metadata, and
   cryptographic evidence references, and a resolution protocol based on
   HTTPS.  Unlike the Domain Name System (DNS), which maps names to
   network addresses, AINS maps agent identifiers to rich metadata
   objects that include capabilities, endpoint information, route
   posture, and references to companion provenance protocols.  AINS
   federates through signed append-only replication logs, enabling
   multi-registry deployments without central authority while preserving
   auditability.  This specification is designed to complement TIBET
   [TIBET], JIS [JIS], UPIP [UPIP], and RVP [RVP].
- **draft-wang-coe-02** (new-draft, score 11, core_identity) [none]: [Cognition-Oriented Emergence (COE): A JEP Profile for Shared Observation and State-Claim Evidence](https://datatracker.ietf.org/doc/draft-wang-coe/) — This document defines COE-2, an optional profile of the Judgment
   Event Protocol (JEP) [JEP] for binding shared observation records and
   shared-state claims across heterogeneous agents, sensors, world
   models, simulators, and human-operated systems.

   COE-2 defines one critical JEP record-binding extension, two minimal
   digest-addressed record types, evidence-reference semantics, and
   independent COE validation checks.  JEP remains authoritative for
   event verbs, Event Identity, Event Hash, signatures, references,
   extension processing, validation modes, and acceptance semantics.

   COE-2 provides verifiable shared-observation infrastructure.  It does
   not determine objective world truth, factual causality, consensus,
   authorization, legal effect, fairness, trust weights, or regulatory
   compliance.  A valid COE result establishes only the cryptographic
   and structural properties actually checked under the selected
   profiles.
- **draft-mih-scitt-checkpointed-local-log-01** (new-draft, score 10, trust_infrastructure) [none]: [The Checkpointed Local Log (CLL)](https://datatracker.ietf.org/doc/draft-mih-scitt-checkpointed-local-log/) — Many systems emit individually signed records — receipts,
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
- **draft-zambo-aer1-01** (new-draft, score 10, trust_infrastructure) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
   AI agent tool call as a portable, independently checkable execution
   receipt.  A receipt identifies the execution, records when it
   happened, preserves the canonical bytes used for the output
   commitment, names the tool and caller scope, carries a provenance
   class, and resolves at a stable public URL.  The format separates
   what the system observed from claims about the outside world, and it
   separates provenance (who ran or reported the action) from the record
   itself.  A reference implementation is deployed, and its receipts are
   publicly verifiable without an account or token.
- **draft-atakora-sadp-protocol-02** (new-draft, score 9, agent_identity) [none]: [The Secure Agent Delegation Protocol (SADP): End-to-End Encrypted Task Capsules for AI Agent Systems](https://datatracker.ietf.org/doc/draft-atakora-sadp-protocol/) — This document specifies the Secure Agent Delegation Protocol (SADP),
   an experimental end-to-end encrypted communication layer for user-to-
   agent and agent-to-agent workflows.  SADP defines task capsules:
   signed, encrypted, individually routable protocol objects that carry
   agent tasks, tool invocations, and results across untrusted brokers,
   queues, and orchestration infrastructure.  SADP provides asynchronous
   session establishment using signed prekey bundles, per-message
   forward secrecy and post-compromise recovery through a Double-
   Ratchet-style message ratchet, an optional hybrid post-quantum key-
   agreement profile based on ML-KEM-768, and an authenticated opaque-
   broker profile with replay protection.  SADP is transport agnostic
   and is designed to be carried over HTTP, message queues, and existing
   agent protocols such as A2A and MCP without requiring those systems
   to be trusted with plaintext task content.  Capability-based
   delegation semantics and scoped context disclosure are specified in a
   companion document.
- **draft-dogru-cedulon-core-01** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-fassbender-scitt-time-anchor-07** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-ietf-rats-endorsements-11** (new-draft, score 9, trust_infrastructure) [rats]: [RATS Endorsements](https://datatracker.ietf.org/doc/draft-ietf-rats-endorsements/) — In the IETF Remote Attestation Procedures (RATS) architecture, a
   Verifier accepts Evidence and uses Appraisal Policy for Evidence,
   typically with additional input from Endorsements and Reference
   Values, to generate Attestation Results in formats that are useful
   for Relying Parties.  This document illustrates the purpose and role
   of Endorsements and discusses some considerations in the choice of
   message format for Endorsements in the scope of the RATS
   architecture.

   This document does not aim to define a conceptual message format for
   Endorsements and Reference Values.  Instead, it extends RFC9334 to
   provide further details on Reference Values and Endorsements, as
   these topics were outside the scope of the RATS charter when RFC9334
   was developed.
- **draft-sergeev-claim-boundaries-01** (new-draft, score 9, trust_infrastructure) [none]: [Claim Boundaries for Execution Evidence](https://datatracker.ietf.org/doc/draft-sergeev-claim-boundaries/) — Systems that act in the world produce logs, receipts, approvals,
   traces, attestations, provenance statements, and transparency
   records.  These artifacts are routinely offered as evidence that an
   action was authorized, performed, or completed.  This document states
   a discipline for bounding such claims: the strength of an execution-
   related claim is limited by what the available evidence actually
   observed, constitutes, or proves, and by the control and observation
   topology at the boundary that produced it.  Message formats,
   signature validity, receipt validity, and registration do not create
   observation or independence that did not exist.  No message format
   can supply the independent enforcement or observation dependencies
   that a prevention or adversary-resistant detection-coverage guarantee
   requires.  An appendix works through a scenario in which one party
   creates another and may be able to act in its name.  The document
   defines no protocol, no record format, and no registry.  It collects
   non-inference rules, a control-topology test for prevention and
   detection claims, a worked example, and reporting distinctions for
   evidence that does not support the claim asserted over it.
- **draft-smith-opsawg-ai-network-governance-01** (new-draft, score 9, trust_infrastructure) [none]: [Governance Framework for AI-Mediated Autonomous Network Device Management](https://datatracker.ietf.org/doc/draft-smith-opsawg-ai-network-governance/) — This document defines a governance framework for systems that use
   artificial intelligence (AI) services, specifically large language
   models (LLMs), to autonomously detect, diagnose, and remediate
   operational anomalies on network devices.  As AI-driven automation
   moves from advisory tooling to closed-loop autonomous operation on
   production infrastructure, the industry lacks a common set of
   principles governing what such systems may and may not do.

   This framework establishes thirteen governance areas covering human
   authority, harm prevention, management plane protection, minimum
   necessary action, bounded autonomy, transparency, reversibility,
   graceful degradation, escalation, AI-specific constraints, startup
   safety, absolute prohibitions, and review processes.  It is intended
   to serve as a reference architecture for implementers building AI-
   mediated network management systems and for operators evaluating the
   safety properties of such systems.
- **draft-vandemeent-upip-process-integrity-02** (new-draft, score 9, core_identity) [none]: [UPIP: Universal Process Integrity Protocol with Task Capsules, Work Corridors, and Fork Tokens](https://datatracker.ietf.org/doc/draft-vandemeent-upip-process-integrity/) — This document defines UPIP (Universal Process Integrity Protocol), a
   five-layer protocol for capturing, verifying, and reproducing
   computational processes across machines, actors, and trust domains.
   UPIP defines a cryptographic hash chain over five layers: STATE
   (input), DEPS (dependencies), PROCESS (execution), RESULT (output),
   and VERIFY (cross- machine proof).  The stack hash chains these
   layers, ensuring that modification of any component is detectable.

   This document also defines continuation artifacts: Task Capsules,
   Work Corridors, and Fork Tokens.  A task capsule carries a bounded
   process blueprint and evidence context.  A work corridor names a
   bounded continuation window.  A fork token freezes the UPIP stack at
   a specific point and transfers it to another actor with cryptographic
   chain of custody.  The receiving actor can verify what was handed
   off, validate capabilities, and continue the process with full
   provenance.

   UPIP integrates with TIBET [TIBET] for provenance tokens, JIS [JIS]
   for actor identity, AINS [AINS] for discovery, and RVP [RVP] for
   presence evidence.  UPIP is transport-agnostic with JSON as the
   baseline serialization.
- **draft-wang-ctp-definition-02** (new-draft, score 9, core_identity) [none]: [CTP/0: Cognitive Time Protocol -- Definition and Framework](https://datatracker.ietf.org/doc/draft-wang-ctp-definition/) — This document describes CTP/0, the definition layer of the Cognitive
   Time Protocol (CTP) family.  CTP/0 is an informational conceptual
   framework for naming, separating, comparing, and referencing time-
   related claims in AI and agent systems.

   CTP/0 defines terminology for profile-defined cognitive events,
   event-density claims, ordering claims, branching claims, sequential-
   computation evidence, and declared temporal-structure claims.

   CTP/0 does not define a wire protocol, message format, signature
   format, identity system, hash-chain protocol, governance process,
   physical theory of time, theory of consciousness, or legal-
   accountability framework.  Where verifiable records are required,
   CTP-compatible claims can be bound to external event, receipt,
   dependency-graph, observation, or change-evidence infrastructure.
- **draft-efstathiou-samp-agent-management-03** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
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
- **draft-hardt-oauth-aauth-protocol-11** (new-draft, score 8, core_identity) [none]: [AAuth Protocol](https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/) — This document defines the AAuth authorization protocol for agent-to-
   resource authorization and identity claim retrieval.  The protocol
   supports five resource access modes — agent identity, resource-
   managed (two-party), person identity, PS authorization (three-party),
   and federated authorization (four-party) — with agent governance as
   an orthogonal layer.  It builds on the HTTP Signature Keys
   specification ([I-D.hardt-httpbis-signature-key]) for HTTP Message
   Signatures and key discovery.
- **draft-ietf-scitt-receipts-ccf-profile-05** (new-draft, score 8, verifiable_claims) [scitt]: [CCF Profile for COSE Receipts](https://datatracker.ietf.org/doc/draft-ietf-scitt-receipts-ccf-profile/) — This document defines a new verifiable data structure (VDS) type for
   COSE Receipts and the associated inclusion and consistency proofs,
   specifically designed for append-only logs produced by the
   Confidential Consortium Framework (CCF) to provide stronger tamper-
   evidence guarantees.
- **draft-jackson-wimse-evaluation-01** (new-draft, score 8, trust_infrastructure) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier must do: the explicit inputs evaluation depends on, and four
   rules that keep evaluation fail-closed.  The rules are drawn from the
   Grant & Autonomy Lifecycle (GAL) and Provenance & Trust Context (PTC)
   specifications and from a public reference implementation.
- **draft-li-rttp-iqa-addressing-00** (new-draft, score 8, trust_infrastructure) [none]: [The rttp and iqa URI Schemes: Derived-Address Intent and Attestation Addressing](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) — This document specifies two companion URI schemes built on one shared
   addressing model, in which the address of a subject is derived by
   computation from the authority and no lookup service, registry, or
   name-resolution system is consulted when the URI is used.  The "rttp"
   scheme names a claim of intent directed at an identified subject; the
   "iqa" scheme names the attestation standing of an identified subject,
   as reported by one of three named organs, and carries no proof and no
   credential.  The two are deliberately paired: intent addressing
   carries what is claimed, attestation carries whether the claimant is
   verified.

   Both schemes parse fail-closed, and the document states the
   requirements a client MUST satisfy when it handles such URIs, to
   avoid the failure modes that short, user-embeddable strings invite:
   using the authority as a navigation target (open redirect), using a
   registered handler as a general-purpose launcher, and, for "iqa", a
   parse that looks like a certification.

   This document is not an Internet Standard.  It is an Informational
   specification of two experimental addressing schemes, published for
   the public record.
- **draft-marques-asqav-compliance-receipts-09** (new-draft, score 8, core_identity) [none]: [Compliance Profile of Signed Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-marques-asqav-compliance-receipts/) — This document defines a profile for signed action receipts and
   independently checkable evidence about agent activity.  It specifies
   versioned payload and signature semantics, hash-chain linkage,
   timestamp and witness policy, receipt verification and bounded
   regulatory-evidence mappings.  It draws on ACTA-RECEIPTS but states
   its profile-specific overrides explicitly.  A receipt supports checks
   about recorded bytes, identity, linkage and retained evidence; it
   does not by itself establish that an action occurred, that all
   actions were captured, or that an organization complies with a law.
   The profile supports retained historical receipts through explicit
   version and legacy rules rather than rewriting their committed bytes.
   Its intended core and implementation limitations are described in the
   body.
- **draft-sankarshan-agent-registry-protocol-02** (new-draft, score 8, core_identity) [none]: [Agent Registry Protocol](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/) — Software agents increasingly act on behalf of people and
   organizations across administrative and security boundaries.
   Existing discovery mechanisms can identify an endpoint or advertise a
   capability, but they do not by themselves provide a common way to
   resolve who operates an agent, the bounded authority under which it
   acts, whether that authority is current, or what evidence supports a
   reliance decision.

   This document defines the Agent Registry Protocol (ARPA), an HTTP and
   JSON protocol for publishing and resolving information about software
   agents, their operational deployments, typed relationships, bounded
   delegated authority, lifecycle status, and associated evidence.  ARPA
   separates identification, authentication, authorization, assurance,
   and lifecycle state.  Registration, successful authentication,
   capability advertisement, or proof verification does not by itself
   establish authority to perform an action.

   The protocol is designed to support deterministic fail-safe behavior
   when material authority information is revoked, suspended, expired,
   stale, conflicting, unavailable, or unverifiable.
- **draft-wang-jep-receipt-profile-00** (new-draft, score 8, core_identity) [none]: [JEP Receipt Profile: Verifiable Behavior and Evidence Receipts](https://datatracker.ietf.org/doc/draft-wang-jep-receipt-profile/) — This document defines JEP Receipt Profile 1 (JEP-RP-1), a minimal
   receipt and evidence profile for the Judgment Event Protocol (JEP)
   [JEP].

   JEP-RP-1 binds a JEP event to one digest-addressed receipt record
   through a critical JEP extension.  It defines a small behavior-record
   format, portable receipt manifests and bundles, and independent
   receipt-validation checks.  JEP remains authoritative for event
   verbs, Event Identity, Event Hash, signature processing, references,
   extension processing, validation modes, and acceptance semantics.

   Receipt records are technical evidence about observable behavior and
   related artifacts.  JEP-RP-1 does not assign legal liability, prove
   subjective intent, establish authorization validity, determine
   causality or factual truth, define governance outcomes, or establish
   regulatory compliance.
- **draft-ahuja-agent-routing-policy-01** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.
- **draft-sato-agent-accountability-refarch-01** (new-draft, score 7, adjacent_watchlist) [none]: [AI Audit Reference Architecture for Post-Hoc Agent Accountability](https://datatracker.ietf.org/doc/draft-sato-agent-accountability-refarch/) — This document defines a reference architecture for producing,
   protecting, and verifying post-hoc accountability records for the
   actions of autonomous and semi-autonomous software agents, built from
   evidence captured across an action's full lifecycle -- before,
   during, and after it executes -- but assessed after the fact.  It is
   scoped exclusively to post-hoc accountability, as distinct from real-
   time enforcement, and depends on no other individual submission's
   proposed architecture: everything it requires is either an already-
   settled standard, used as published, or intended to be specified and
   released openly as the author's own work, independent of this
   document's own adoption.  It defines seven ordered stages -- intent
   and mandate capture, the agent boundary, the record producer, the
   event log and its cryptographic anchoring, a composed trust fabric,
   the disclosed audit record, and third-party verification -- together
   with two branch conditions covering cross-principal transactions and
   external resource ingestion.

## Monitor

- **draft-dnoveck-nfsv4-security-17** (new-draft, score 6, authorization) [none]: [Security for the NFSv4 Protocols](https://datatracker.ietf.org/doc/draft-dnoveck-nfsv4-security/) — This document describes the core security features of the NFSv4
   family of protocols, applying to all minor versions.  The discussion
   includes the use of security features provided by RPC on a per-
   connection basis.  Important aspects of the authorization model,
   related to the use of Access Control Lists, will be specified in a
   separate document.

   The current version of the document is intended, in large part, to
   result in working group discussion regarding existing NFSv4 security
   issues and to provide a framework for addressing these issues and
   obtaining working group consensus regarding necessary changes.

   When the resulting documents (i.e. this document and one derived from
   the separate ACL specification) are eventually published as RFCs,
   they will, by updating these documents, supersede the description of
   security appearing in existing minor version specification documents
   such as RFC 7530 and RFC 8881.
- **draft-ietf-cose-cbor-encoded-cert-21** (new-draft, score 6, verifiable_claims) [cose]: [CBOR Encoded X.509 Certificates (C509 Certificates)](https://datatracker.ietf.org/doc/draft-ietf-cose-cbor-encoded-cert/) — This document specifies a CBOR encoding of X.509 certificates.  The
   resulting certificates are called C509 certificates.  The CBOR
   encoding supports a large subset of RFC 5280 and common certificate
   profiles, and it is extensible.

   Two types of C509 certificates are defined.  One type is an
   invertible CBOR re-encoding of DER-encoded X.509 certificates with
   the signature field copied from the DER encoding.  The other type is
   identical except that the signature is computed over the CBOR
   encoding instead of the DER encoding, thereby avoiding the use of
   ASN.1.  Both types of certificates have the same semantics as X.509
   while providing comparable size reduction.

   This document also specifies CBOR-encoded data structures for
   certification requests and certification request templates, new COSE
   headers, as well as a TLS certificate type and a file format for
   C509.  This document updates RFC 6698 by extending the TLSA selectors
   registry to include C509 certificates.
- **draft-ietf-emu-pqc-eap-tls-02** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Enhancements to TLS-Based EAP Methods](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eap-tls/) — This document specifies the use of post-quantum cryptography in TLS-
   based EAP methods, including the Extensible Authentication Protocol
   with Transport Layer Security (EAP-TLS), EAP Tunneled TLS (EAP-TTLS),
   Protected EAP (PEAP), and EAP Tunnel Method (TEAP).  It also
   addresses challenges related to large certificate sizes and long
   certificate chains, as identified in [RFC9191], and specifies a
   mechanism to reduce TLS handshake size.
- **draft-ietf-jose-deprecate-none-rsa15-06** (new-draft, score 6, verifiable_claims) [jose]: [JOSE: Deprecate 'none' and 'RSA1_5'](https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/) — This document updates RFC 7518 to deprecate the JWS algorithm "none"
   and the JWE algorithm "RSA1_5".  These algorithms have known security
   weaknesses.  It also updates the Review Instructions for Designated
   Experts to establish baseline security requirements that future
   algorithm registrations are expected to meet.
- **draft-khandelwal-bmwg-agent-memory-integrity-00** (new-draft, score 6, agent_identity) [none]: [A Benchmarking Method for the Integrity of AI Agent Memory at Rest](https://datatracker.ietf.org/doc/draft-khandelwal-bmwg-agent-memory-integrity/) — AI agents increasingly persist memory across sessions and treat that
   memory, on the next turn, as if it were their own prior experience.
   This document defines a benchmarking method that measures whether an
   agent's memory subsystem detects that its persisted memory has been
   altered, removed, reordered, replayed, or forged at the storage
   layer, and refuses to serve that memory or reports it before it is
   served.  The method defines eight storage-level edits, three verdict
   classes, a detection-point distinction between read time and audit
   time, two control cases, and a scoring rule.  It is a laboratory
   method for controlled, reproducible measurement, in the spirit of RFC
   2544 and RFC 8239, and it is intended as a test method for the
   "Protection of Memory Data Integrity" metric under discussion in the
   Benchmarking Methodology Working Group.
- **draft-templeman-scitt-framing-space-01** (new-draft, score 6, core_identity) [none]: [Measuring the CBOR Framing Space of COSE_Sign1 Data-Hash Pre-images](https://datatracker.ietf.org/doc/draft-templeman-scitt-framing-space/) — A signed statement conveyed as a COSE_Sign1 object may be serialized
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
   them, and 31 were silently repaired into the original form by the act
   of being read.

   This document specifies nothing and proposes no wording.  It reports
   a measurement, publishes the reproduction recipe, and identifies the
   prior work that already addresses the problem it measures.
- **draft-wang-jac-03** (new-draft, score 6, core_identity) [none]: [JAC: Declared Dependency Graphs for JEP Events and Receipts](https://datatracker.ietf.org/doc/draft-wang-jac/) — This document defines JAC-2, a minimal declared-dependency graph
   profile for the Judgment Event Protocol (JEP) [JEP].

   JAC-2 binds a signed JEP event to zero or more declared parent
   dependencies through one critical JEP extension.  JEP Event Identity
   is used for logical JEP event dependencies; Event Hash is used only
   when an exact signed artifact must also be pinned.  Digest-addressed
   receipt or external records can be linked without becoming JEP
   events.

   JAC-2 defines dependency-link structure, partial-fragment semantics,
   cycle handling, chain validation checks, and non-inference
   boundaries.  It does not determine factual causality, responsibility,
   fault, authorization validity, workflow correctness, legal effect, or
   regulatory compliance.
- **draft-abak-ai-evaluation-claim-preservation-00** (new-draft, score 5, authorization) [none]: [Claim-Preserving Exchange of AI Evaluation Evidence](https://datatracker.ietf.org/doc/draft-abak-ai-evaluation-claim-preservation/) — AI evaluation records can pass through evaluation frameworks,
   exporters, evidence services, independent reviewers, and systems that
   make decisions.  A conversion can retain a score while losing whether
   the measurement ran, which result was selected, whether a criterion
   existed, or which evidence was unavailable.  Authenticating the
   converted record does not recover these distinctions.

   This document specifies format-neutral requirements for mapping
   profiles and consumers that exchange AI evaluation evidence.  It
   separates source assertions, explicit derivations, and later policy
   judgments; requires claim-relevant loss and uncertainty to remain
   visible; and describes consumer behavior when preservation cannot be
   established.  It includes synthetic counterexamples and guidance for
   composition with existing evidence mechanisms.  It defines neither a
   wire format nor an evaluation benchmark, safety certification,
   authorization protocol, or new cryptographic envelope.  A concrete
   mapping profile is needed for interoperable implementation.
- **draft-intra-handshake-fail-47** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-92701 of CVSS 9.1, CVE-2026-92702 of CVSS 9.1, CVE-2026-33697 of CVSS 7.5, and 37 other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-33697],
   [EUVD-2026-16488], [CVE-2026-92701], [EUVD-2026-83194],
   [CVE-2026-92702], [EUVD-2026-83192] and several GitHub Security
   Advisories (GHSAs) which provide substantial technical evidence of
   how early attestation fails in practice, even *without physical
   access* to the desired machine.  Moreover, since continuous
   attestation is generally required [CSA-eBPF]
   [MITRE-Continuous-Attestation], early attestation adds *unnecessary
   complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA], [EarlyAttestationBleed] and the
   artifacts [Intra-handshake.fail-repo] in state-of-the-art formal
   analysis tool, ProVerif, under Apache-2.0 license for
   reproducibility, extensibility, and review, and have been
   acknowledged by the relevant stakeholders.  Currently, there are *two
   CVEs of CVSS 9.1, one CVE of CVSS 7.5, one GHSA of 9.0-10.0, one GHSA
   of CVSS 7.8, seven GHSAs of CVSS 7.4, and one GHSA of CVSS 6.3
   published against the broader early attestation covering all layers
   of the ecosystem up to the application*. The research papers on these
   are currently either under submission or being prepared for
   submission.  The artifacts of these papers will be shared with the
   community under Apache-2.0 license for reproducibility,
   extensibility, and review.  Based on our work, all except two
   implementations of early attestation have been archived, withdrawn,
   or moved to post-handshake attestation.  In our analysis
   [Intra-handshake.fail-repo], the remaining two implementations of
   early attestation -- Edgeless Systems Contrast and Meta's AI --
   remain vulnerable.  We recommend users to carefully evaluate their
   systems.
- **draft-lcurley-moq-hang-03** (new-draft, score 5, adjacent_watchlist) [none]: [Media over QUIC - Hang](https://datatracker.ietf.org/doc/draft-lcurley-moq-hang/) — Hang is a real-time conferencing protocol built on top of moq-lite.
   A room consists of multiple participants who publish media tracks.
   All updates are live, such as a change in participants or media
   tracks.

Note to Readers

   This document was generated by an AI model from the implementation at
   github.com/moq-dev/moq (https://github.com/moq-dev/moq) and is
   maintained alongside it.  Submit an issue (https://github.com/moq-
   dev/moq/issues) or PR (https://github.com/moq-dev/moq/pulls) if this
   spec sucks and you want to fix anything.
- **draft-lcurley-moq-mpegts-00** (new-draft, score 5, core_identity) [none]: [MoQ MPEG-TS Catalog Extension](https://datatracker.ietf.org/doc/draft-lcurley-moq-mpegts/) — This document defines the mpegts catalog section, which records what
   demultiplexing an MPEG-2 Transport Stream [mpeg2] into a MoQ
   broadcast would otherwise lose: each track's PID and PMT descriptors,
   the program identity, the service information tables, and a carriage
   record for every elementary stream the publisher did not decode.  It
   is a root member of either the hang catalog [hang] or the MSF catalog
   [msf], so a subscriber that ignores it still plays the broadcast and
   one that reads it can rebuild the source multiplex.
- **draft-oliveira-ipv7-00** (new-draft, score 5, core_identity) [none]: [IPv7: Identity-Centric Network Protocol with Verifiable Origin and Rate-Limit Tokens](https://datatracker.ietf.org/doc/draft-oliveira-ipv7/) — This document specifies IPv7, an identity-centric network protocol
   that replaces purely numerical source addressing with a hierarchical
   identity string and a Variable-Length Identity Block (VLIB).  The
   VLIB carries an Ephemeral Identity Token (EIT), provider and tenant
   identifiers, role/policy signalling, and an Origin Signature
   verifiable by the originating provider.  Validation occurs in three
   layers at the first-hop router: Origin Verification, Identity
   Verification, and Policy Enforcement.  A quantum-resistant signature
   option using CRYSTALS-Dilithium (ML-DSA-65) is incorporated.  This
   document also describes an optional local extension for Rate-Limit
   Tokens issued by ISPs and enforced in hardware.  A reference
   implementation in Rust is available as the arkhe-ipv7 and arkhe-
   ipv7-cli crates.
- **draft-ietf-plants-merkle-tree-certs-06** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
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

- **draft-claise-green-capability-discovery-02** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
   capabilities model of RFC 9196 to allow a network element to
   advertise, per hardware Component, the set of Power States that the
   Component supports, together with a static characterization of each
   such state: the expected and maximum Power the Component draws in it,
   and the time to enter and exit it.

   This capability model complements the operational Power and Energy
   data model defined in the GREEN Power and Energy YANG module, which
   reports the current Power State and the measured Power of a
   Component, but not which Power States are available, how much Power
   each draws, or how long transitions between them take.  It is
   anchored to the hardware inventory of RFC 8348, reuses the Power
   State identities of the GREEN Power and Energy model, and, because it
   is static, may be provided at implementation time as YANG instance
   data per RFC 9195 so that an Energy Management System can learn a
   platform's Power State capabilities before the equipment is deployed
   or even powered on.
- **draft-ehstand-oversight-acts-00** (new-draft, score 3, agent_identity) [none]: [Terminology for Human Oversight Acts in Automated and Agentic Systems](https://datatracker.ietf.org/doc/draft-ehstand-oversight-acts/) — Records produced by automated and agentic systems often represent
   human oversight as a single, undifferentiated event, such as an
   approval flag or a confirmation.  Such a record does not say whether
   the person was shown an output, determined whether a named property
   of it holds, chose a course of action, or permitted an action, and
   consumers of the record may treat a confirmation click as if it were
   a check.

   This document defines terms for four kinds of human oversight act
   (observation, check, decision, and release) and for related concepts:
   the oversight act and the overseer, the named property, standing
   authority, the oversight record, the undifferentiated approval, the
   check step, error detectability, the fail-open check step, and the
   check test.  It states what a record of each kind of act is, and is
   not, evidence of, and relates the terms to existing vocabularies.
   The document defines terminology only.  It specifies no protocol,
   data format, procedure, or measurement method.
- **draft-helmprotocol-deepspace-01** (new-draft, score 3, trust_infrastructure) [none]: [TTTPS Deep-space Profile: Propagation-Aware Time Attestation](https://datatracker.ietf.org/doc/draft-helmprotocol-deepspace/) — This document defines an experimental deep-space profile for the TLS
   TimeToken Secure Protocol (TTTPS).  The profile preserves the Proof-
   of-Time record and cryptographic verification boundary while adding
   propagation-aware context for long and intermittent links.  It
   specifies one-way-light-time handling, epoch- and frame-bound
   physical context, relative coordinate-time conversion, peer
   projection, conservative aggregation, and explicit HOLD and
   UNVERIFIABLE outcomes.  It does not claim flight measurements, a live
   interplanetary mesh, or a replacement for CCSDS, DTN, or navigation
   standards.
- **draft-ietf-acme-dns-persist-02** (new-draft, score 3, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation](https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/) — This document specifies "dns-persist-01", a new validation method for
   the Automated Certificate Management Environment (ACME) protocol.
   This method allows a Certification Authority (CA) to verify control
   over a domain by confirming the presence of a persistent DNS TXT
   record containing CA and account identification information.  This
   method is particularly suited for environments where traditional
   challenge methods are impractical, such as multi-tenant hosting
   platforms, enterprise DNS environments, and IoT deployments.  The
   validation method is designed with a strong focus on security and
   robustness, incorporating widely adopted industry best practices for
   persistent domain control validation.  This design aims to make it
   suitable for Certification Authorities operating under various policy
   environments, including those that align with the CA/Browser Forum
   Baseline Requirements.
- **draft-ietf-cats-data-model-00** (new-draft, score 3, adjacent_watchlist) [cats]: [Data Model for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-ietf-cats-data-model/) — This document defines a YANG data model for the management of
   Computing-Aware Traffic Steering (CATS) systems.
- **draft-ietf-ccamp-flexe-yang-cm-11** (new-draft, score 3, adjacent_watchlist) [ccamp]: [YANG Data Model for FlexE Management](https://datatracker.ietf.org/doc/draft-ietf-ccamp-flexe-yang-cm/) — This document defines a service provider targeted YANG data model for
   the configuration and management of a Flex Ethernet (FlexE) network,
   including FlexE group and FlexE client.
- **draft-ietf-dnsop-ede-nta-00** (new-draft, score 3, adjacent_watchlist) [dnsop]: [Disclosure of Negative Trust Anchors in DNS Responses](https://datatracker.ietf.org/doc/draft-ietf-dnsop-ede-nta/) — This document describes a mechanism for disclosing that a Negative
   Trust Anchor (NTA) was in effect at the time that a DNS response was
   generated, using an Extended DNS Error (EDE).

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Domain Name System
   Operations Working Group mailing list (dnsop@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/dnsop/.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-wg-dnsop/draft-ietf-dnsop-ede-nta.
- **draft-ietf-dtn-eid-pattern-11** (new-draft, score 3, verifiable_claims) [dtn]: [Bundle Protocol Endpoint ID Patterns](https://datatracker.ietf.org/doc/draft-ietf-dtn-eid-pattern/) — This document extends the Bundle Protocol Endpoint ID (EID) concept
   into an EID Pattern, which is used to categorize any EID as matching
   a specific pattern or not.  EID Patterns are suitable for expressing
   configuration, for being used on-the-wire by protocols, and for being
   easily understandable by a layperson.  EID Patterns include scheme-
   specific optimizations for expressing set membership and each scheme
   pattern includes text and binary encoding forms; the pattern for the
   "ipn" EID scheme being designed to be highly compressible in its
   binary form.

   This document also defines a Public Key Infrastructure Using X.509
   (PKIX) Other Name form to contain an EID Pattern and a handling rule
   to use a pattern to match an EID.  The Other Name form is used to
   update the PKIX profiles of RFC 9174 and [I-D.ietf-dtn-bpsec-cose].
- **draft-ietf-ediint-rfc4130bis-04** (new-draft, score 3, core_identity) [ediint]: [AS2 Specification Modernization](https://datatracker.ietf.org/doc/draft-ietf-ediint-rfc4130bis/) — This document provides an applicability statement (RFC 2026,
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
- **draft-ietf-nmop-network-incident-yang-17** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
   lifecycle management.  This YANG module provides a standard way to
   report, diagnose, and help reduce troubleshooting tickets and resolve
   network incidents for the sake of network service health and probable
   root cause analysis.
- **draft-ietf-radext-epcs-00** (new-draft, score 3, authorization) [radext]: [RADIUS attributes for National Security and Emergency Preparedness Service](https://datatracker.ietf.org/doc/draft-ietf-radext-epcs/) — This document describes RADIUS attributes for supporting
   authorization of Emergency Preparedness Communication Service (EPCS),
   enabling authorized users to benefit from preferential access to Wi-
   Fi network resources during congestion.
- **draft-ietf-rtgwg-qos-model-16** (new-draft, score 3, adjacent_watchlist) [rtgwg]: [A YANG Data Model for Quality of Service (QoS) in IP Networks](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-qos-model/) — This document describes a YANG data model for management of Quality
   of Service (QoS) in IP networks.
- **draft-koo-dtn-traceroute-eb-00** (new-draft, score 3, core_identity) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block for Bundle
   Protocol Version 7 (BPv7).  The extension block provides path
   discovery and per-hop performance measurement capabilities for Delay-
   Tolerant Networks (DTNs).  Each node along the bundle's path appends
   a hop record containing its endpoint identifier, timestamp, link
   characteristics, and convergence layer information.  This enables
   comprehensive network diagnostics including path verification, delay
   analysis, link type identification, and congestion monitoring without
   requiring status reports from every intermediate node.
- **draft-lcurley-moq-e2ee-00** (new-draft, score 3, core_identity) [none]: [MoQ End-to-End Encryption Profile](https://datatracker.ietf.org/doc/draft-lcurley-moq-e2ee/) — This document specifies moq-e2ee-00, a versioned profile for end-to-
   end encryption of MoQ application payloads.  Authorized publishers
   and subscribers share a 32-byte broadcast secret out of band.  Each
   publisher instance mints an epoch and publishes under an opaque
   broadcast path ending in it.  HKDF-SHA-256 derives opaque physical
   track names and per-track AES-128-GCM keys from the secret and the
   epoch; grouped frames and datagrams use separate key domains.  Media
   frames and datagrams carry only ciphertext plus a 16-byte tag.  The
   profile binds object identity through derivation and the nonce, not
   an on-wire header.
- **draft-many-tiptop-snmp-profile-00** (new-draft, score 3, adjacent_watchlist) [none]: [SNMP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-snmp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an SNMP profile
   for deep space.  The profile states, for each SNMP version and
   security model, what must be configured, provisioned, or changed, and
   maps their applicability to the deep space connectivity scenarios.
- **draft-mcewan-adkm-requirements-00** (new-draft, score 3, core_identity) [none]: [Autonomous Decentralized Key Management (ADKM) Requirements](https://datatracker.ietf.org/doc/draft-mcewan-adkm-requirements/) — This document defines the high-level functional, operational,
   security, and protocol requirements for Autonomous Decentralized Key
   Management (ADKM).  The design goal is straightforward.
   Cryptographic key state bound to a stable identifier should be able
   to begin, evolve, and be independently verified without requiring a
   central administrative authority or globally ordered consensus ledger
   to remain online and authoritative.

   These requirements establish the minimum properties for key-state
   inception, forward commitment, local evidence verification, duplicity
   detection, cryptographic agility, and transport independence.  They
   are intended to guide the standardization of ADKM data models and
   exchange protocols without prescribing a single implementation.
- **draft-mih-zhang-agent-disclosure-bundle-00** (new-draft, score 3, verifiable_claims) [none]: [AAC Evidence Bundle](https://datatracker.ietf.org/doc/draft-mih-zhang-agent-disclosure-bundle/) — This document defines the AAC Evidence Bundle, a portable
   presentation and verification container for an Agent Action Capsule
   and the records that make its evidentiary claim intelligible.  A
   permalink carries a bundle in its URL fragment, an offline HTML
   report carries a bundle in its shell, and a hosted report serves a
   bundle at its URL.  The bundle does not alter any enclosed Capsule.
   It declares its citation closure and any missing cited records,
   carries verified disclosure preimages as a bundle-level overlay,
   separates three different completeness claims, and permits
   independently specified extension blocks and neutral third-party
   countersignatures.
- **draft-mittal-est-coap-ca-certs-00** (new-draft, score 3, adjacent_watchlist) [none]: [Manufacturer-Signed CA Certificate Distribution for EST and EST-coaps Deployments](https://datatracker.ietf.org/doc/draft-mittal-est-coap-ca-certs/) — This document describes a manufacturer-assisted mechanism for
   distributing operational certification authority (CA) certificates to
   devices using Enrollment over Secure Transport (EST) or EST over
   secure CoAP (EST-coaps).

   The mechanism is intended for deployments in which a device is
   manufactured before the operational PKI and EST server trust anchors
   are known.  The device is provisioned during manufacturing with a
   manufacturer trust anchor.  An operational CA certificate bundle is
   subsequently signed by the manufacturer, or by a manufacturer-
   authorized signing authority, and delivered through a manufacturer-
   specific EST alias.

   The device validates the signed bundle using its manufacturer trust
   anchor before installing the contained CA certificates as operational
   trust anchors.  This mechanism is limited to CA certificate bootstrap
   and does not change EST enrollment semantics, proof-of-possession
   requirements, certification authority policy, or authenticated EST
   operation following bootstrap.
- **draft-templeman-scitt-measurement-capsule-00** (new-draft, score 3, trust_infrastructure) [none]: [Declared-versus-Observed Measurement Capsules: A Profile for Third-Party Measurement Statements in SCITT](https://datatracker.ietf.org/doc/draft-templeman-scitt-measurement-capsule/) — This document defines the measurement capsule: a small, deterministic
   JSON record in which a party that is neither the subject of a claim
   nor a participant in the action it concerns records what the subject
   declared, what the measuring party observed, and the difference
   between the two.  A capsule carries digests of its evidence, a
   measurement state in which "could not be checked" is a first-class
   outcome, and no decision, approval or authorisation.  Capsules are
   identified by the SHA-256 of their JCS serialisation and batched
   under an RFC 9162 Merkle Tree Hash.  The document describes their
   registration as SCITT Signed Statements (RFC 9943), how they refer to
   rather than restate receipts issued under other profiles, and one
   implementation, including where it does not yet match this profile.
- **draft-toutain-schc-toward-rfc9363bis-00** (new-draft, score 3, adjacent_watchlist) [none]: [Toward RFC 9363bis: Changes to the SCHC YANG Data Model](https://datatracker.ietf.org/doc/draft-toutain-schc-toward-rfc9363bis/) — This document is not a revision of RFC 9363, "A YANG Data Model for
   Static Context Header Compression (SCHC)": it identifies changes --
   additions to, and removals from, its YANG data model -- motivated by
   discussions in the SCHC working group and by drafts published since
   RFC 9363.  These changes include more flexible compression Rule
   entries through the use of Universal Options, which allow identifiers
   to be added to or removed from a Rule Description depending on the
   Universal Options in use; some new Field Length functions, and new
   Matching Operators (MOs) and Compression/Decompression Actions
   (CDAs); and a mechanism for the manual allocation of YANG Schema Item
   iDentifiers (SIDs).  Once the working group agrees on the resulting
   wording, these changes are intended to be incorporated into a future
   revision of RFC 9363.
- **draft-wang-jep-conformance-01** (new-draft, score 3, adjacent_watchlist) [none]: [JEP Conformance and Test Suite](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/) — This document defines conformance classes, validation-result
   structure, schema requirements, test-vector categories, reference-
   validator behavior, and implementation testing guidance for the
   Judgment Event Protocol (JEP).  It is a companion to [JEP].

   This document does not redefine JEP-Core semantics.  Its purpose is
   to make JEP-Core 0.7 implementations testable and interoperable
   across languages, platforms, trust profiles, and deployment
   environments.
- **draft-wang-jep-semantic-interoperability-01** (new-draft, score 3, core_identity) [none]: [Semantic Interoperability for the Judgment Event Protocol](https://datatracker.ietf.org/doc/draft-wang-jep-semantic-interoperability/) — This document defines semantic interoperability requirements for the
   Judgment Event Protocol (JEP) [JEP].

   JEP-Core defines signed J/D/T/V event semantics, Event Identity,
   Event Hash, references, validation checks, validation modes,
   extension processing, and idempotent acceptance.  This document does
   not redefine those mechanisms.  Instead, it defines the minimum
   shared interpretation rules required for independent systems to map,
   display, translate, and consume JEP events without silently changing
   their meaning.

   The core rule is that a JEP event records a signed protocol statement
   with defined verb semantics.  It does not by itself establish
   external truth, authority, legality, causality, completeness, policy
   consequence, or external effect.  Stronger conclusions require an
   explicitly selected profile or external evidence rule.
- **draft-zhang-cats-clients-request-packet-01** (new-draft, score 3, core_identity) [none]: [Carriage of CATS Service Identification and Request Constraints](https://datatracker.ietf.org/doc/draft-zhang-cats-clients-request-packet/) — This document defines a common encoding for a CATS Service Identifier
   (CS-ID) and optional client-supplied request constraints, and
   specifies two ways to carry that encoding from a client to an ingress
   CATS-Forwarder.  Mode A carries the encoding in an IPv6 Destination
   Options or Hop-by-Hop Options header.  Mode B carries the same
   encoding in an application-layer envelope whose position is
   explicitly identified by an application, API, or transport mapping,
   and which can operate over IPv4 or IPv6.

   The document specifies how a service request is identified, either by
   the destination address (e.g., a Virtual Placeholder Address (VPA),
   an anycast address, or a dedicated service address), by an explicit
   CS-ID, or by both together.  It defines the CS-ID, Network
   Constraints, and Computing Constraints TLVs and their processing at
   an ingress CATS-Forwarder, and describes how the extracted
   information is provided to the CATS Path Selector (C-PS) for service
   selection.  The mechanisms are intended for limited domains in which
   clients and CATS nodes are provisioned to use the selected mode.
- **draft-filsfils-srv6ops-srv6-ai-backend-05** (new-draft, score 2, ignored_after_review) [none]: [SRv6 for Deterministic Path Placement in AI Backends](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) — This document describes how SRv6 uSID (NEXT-CSID) enables
   deterministic path placement in AI backend fabrics through L3-L4
   integration: the transport stack on the NIC encodes each path as an
   ordered list of segments (a uSID network program) in the packet
   header, while the fabric forwards statelessly.  It explains
   operational benefits including deterministic probing and alignment
   with hyperscale production deployments.
- **draft-google-cfrg-libzk-03** (new-draft, score 2, ignored_after_review) [none]: [Longfellow ZK](https://datatracker.ietf.org/doc/draft-google-cfrg-libzk/) — This document defines an algorithm for generating and verifying a
   succinct non-interactive zero-knowledge argument that for a given
   input x and a circuit C, there exists a witness w, such that C(x,w)
   evaluates to 0.  The technique here combines the MPC-in-the-head
   approach for constructing ZK arguments described in Ligero [ligero]
   with a verifiable computation protocol based on sumcheck for proving
   that C(x,w)=0.
- **draft-hillier-chorale-protocol-00** (new-draft, score 2, ignored_after_review) [none]: [The Chorale Protocol: Interception-Resistant Packet Transmission with Topology-as-Secret Ordering, Cascade-Integrity Witnessing, Polyglot Cover Packets, Per-Packet Time-Lock Sealing, and Multi-Jurisdiction Substrate Diversity](https://datatracker.ietf.org/doc/draft-hillier-chorale-protocol/) — This document specifies the Chorale Protocol, a secure packet
   transmission system with active integrity assurance, for use cases
   requiring resistance to interception, traffic analysis, replay,
   tampering, and retrospective decryption by adversaries with future
   quantum capability.  Chorale defines three confidentiality regimes,
   computational, everlasting and information-theoretic, and states the
   keying conditions under which each may be relied upon.  The
   information-theoretic regime requires an independently corroborated
   co-presence or quantum-key-distribution strand consumed as an
   unexpanded pad.  A session keyed by a derived keystream is
   computational and is reported as computational.  A conforming
   implementation fails closed and refuses to report a regime its keying
   does not support.  The protocol composes a per-session secret graph
   topology that determines packet ordering without transmitting any
   ordering information on the wire, cascade-integrity witnessing over
   the hidden topology, cover packets carrying valid-looking witnesses
   for fictional sessions, per-packet Verifiable Delay Function time-
   lock sealing, multi-source physical-entropy one-time pad composition
   with sovereign jurisdictional separation, multi-substrate flight
   requiring threshold reconstruction across diverse path types, and a
   tombstone ledger that makes pad reuse structurally impossible at the
   receiver.  This version introduces hash-family negotiation at
   handshake, raising the default hash function for HKDF key derivation,
   VDF time-lock sealing, and server-blind relay commitments from
   SHA-256 to SHA-512, with SHA3-512 admitted as a Keccak-family
   alternative for adversary-evolution- tolerant postures and SHA-256
   retained as a backward-compatible legacy mode for resource-
   constrained devices.  The protocol is intended for use by
   intelligence agencies, central banks, treaty-bound corridors,
   regulator-to-regulator communications, and other settings demanding
   the strongest practical confidentiality and integrity properties.
- **draft-xu-idr-fare-in-sun-00** (new-draft, score 2, ai_infrastructure) [none]: [Fully Adaptive Routing Ethernet in Scale-Up Networks](https://datatracker.ietf.org/doc/draft-xu-idr-fare-in-sun/) — The Mixture of Experts (MoE) has become a dominant paradigm in
   transformer-based artificial intelligence (AI) large language models
   (LLMs).  It is widely adopted in both distributed training and
   distributed inference.  To enable efficient expert parallelization
   and even tensor parallelization across dozens or even hundreds of
   Graphics Processing Units (GPUs) in MoE architectures, an ultra-high-
   throughput, ultra-low-latency AI scale-up network (SUN) is critical.
   This document describes how to extend the Weighted Equal-Cost Multi-
   Path (WECMP) load-balancing mechanism, referred to as Fully Adaptive
   Routing Ethernet (FARE), which was originally designed for scale-out
   networks, to scale-up networks.

## Ignored after review

- **draft-acosta-deepspace-celestial-bodies-registry-03** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Reference Framework for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document highlights the operational framework within Deepspace/
   TIPTOP protocols to utilize an external, standardized reference
   framework for celestial objects, functioning as an equivalent to ISO
   3166 for interplanetary networking.  To avoid operational overhead
   and duplication of effort, this framework defers the definitions,
   naming, and tracking of celestial entities directly to the
   International Astronomical Union (IAU) and the Minor Planet Center
   (MPC).  This document outlines how these external identifiers guide
   hierarchical address allocation without requiring IANA to maintain a
   dedicated astronomical nomenclature registry.  The ultimate objective
   is to establish a clear definition of what constitutes a valid
   Celestial Body for networking purposes.
- **draft-avrilionis-satp-artefacts-registry-01** (new-draft, score 0, ignored_after_review) [none]: [Artefacts Registry](https://datatracker.ietf.org/doc/draft-avrilionis-satp-artefacts-registry/) — This memo describes the Artefacts Registry for Asset Exchange API.
   The Registry is a component that exposes an API allowing gateways to
   fetch information related to the SAT protocol.  Examples information
   stored in the Artefacts Registry are network identifiers, entities
   identifiers, asset profiles, or asset instances.  Registries are are
   acting as persistent storage locations for records.  Once registered,
   records can be updated in an append-only manner.
- **draft-avrilionis-satp-setup-stage-05** (new-draft, score 0, ignored_after_review) [none]: [SATP Setup Stage](https://datatracker.ietf.org/doc/draft-avrilionis-satp-setup-stage/) — SATP Core defines an unidirectional transfer of assets in three
   stages, namely the Transfer Initiation stage (Stage-1), the Lock-
   Assertion stage (Stage-2) and the Commitment Establishment stage
   (Stage-3).  This document defines the Setup Phase, often called
   "Stage-0", prior to the execution of SATP Core.  During Setup, the
   two Gateways that would participate in the asset transfer are bound
   together via a "transfer context".  The transfer context conveys
   information regarding the assets to be exchanged.  Gateway can
   perform any kind of negotiation based on that transfer context,
   before entering into SATP Core
- **draft-bertoldi-regext-rdap-reliability-scoring-04** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Structured Reliability Assessment Metadata](https://datatracker.ietf.org/doc/draft-bertoldi-regext-rdap-reliability-scoring/) — This document defines an extension to the Registration Data Access
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
- **draft-camarillo-rtgwg-lsn-01** (new-draft, score 0, ignored_after_review) [none]: [Lightspeed Notification Protocol](https://datatracker.ietf.org/doc/draft-camarillo-rtgwg-lsn/) — This document defines the Lightspeed Notification Protocol (LSN), a
   hardware-accelerated signaling mechanism designed for sub-100
   microsecond network convergence in AI/ML data center fabrics.  By
   operating entirely within the forwarding plane, LSN bypasses
   traditional CPU-based latencies to propagate link failures and
   congestion via a hardware-efficient encoding.  It serves as a high-
   speed complement to routing protocols like BGP, providing an
   immediate hardware "veto" to prune congested/failed paths while
   maintaining control-plane stability for path recovery.
- **draft-cel-nfsv4-element-registries-00** (new-draft, score 0, ignored_after_review) [none]: [Registries of Network File System Version 4 Protocol Elements](https://datatracker.ietf.org/doc/draft-cel-nfsv4-element-registries/) — Several numbered NFS version 4 protocol elements, among them
   operations, callback operations, status codes, file attributes, and
   the flags of the ACCESS and OPEN operations, are identified by values
   that no IANA registry records, so protocol extensions under
   development at the same time can assign the same value to different
   elements.  This document requests an IANA registry for each of these
   element types, populates the registries from published RFCs, and
   requires future elements to obtain their values through them.  It
   updates RFC 8178.
- **draft-chuang-dkim2-sender-policy-03** (new-draft, score 0, ignored_after_review) [none]: [DKIM2 Sender Policy](https://datatracker.ietf.org/doc/draft-chuang-dkim2-sender-policy/) — This document updates DMARC RFC9989 for DKIM2.  In particular DKIM2
   verification supports MTA relay forwarding with message modifications
   through multiple MTAs, so this updates DMARC to support those
   scenarios as well.  While DMARC defines a RFC5322 From alignment
   constraint with an enforcement policy if validation fails, this
   generalizes and separates enforcement policy from constraint
   validation policies.  This provides a mechanism for MTAs to declare
   support for DKIM2 through the DMARC DNS policy record that helps
   secure DKIM2 from downgrade attacks.
- **draft-connolly-cfrg-xwing-kem-11** (new-draft, score 0, ignored_after_review) [none]: [X-Wing: general-purpose hybrid post-quantum KEM](https://datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem/) — This memo defines X-Wing, a general-purpose post-quantum/traditional
   hybrid key encapsulation mechanism (PQ/T KEM) built on X25519 and ML-
   KEM-768.
- **draft-filmroellchen-lunar-well-known-button-01** (new-draft, score 0, ignored_after_review) [none]: [The Well Known Button Information Specification](https://datatracker.ietf.org/doc/draft-filmroellchen-lunar-well-known-button/) — This document specifies the well-known URI /.well-known/button.json,
   which describes a web site's "buttons".  Buttons are usually 88x31
   pixel images representing the web site with text, logos, artwork, and
   animations.

   /.well-known/button.json files facilitate sharing buttons between web
   site owners and alleviate issues commonly encountered when doing so.
   By utilizing a standardized, machine-readable format, automated tools
   can also utilize the provided information.
- **draft-garg-change-01** (new-draft, score 0, ignored_after_review) [none]: [Extensible Provisioning Protocol (EPP) Change Mapping](https://datatracker.ietf.org/doc/draft-garg-change/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for provisioning and management of change request objects in
   a shared central repository, where a change request is one unit of
   work that is processed by submitting to a workflow to execute the
   linked EPP transform commands in order.  The change request is a
   container with meta-data to ensure that the contained commands are
   processed as a group.
- **draft-garg-change-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Change Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-garg-change-ext/) — This document describes an Extensible Provisioning Protocol (EPP)
   extension of the domain name mapping and the host mapping to link
   transform commands to a change request described in the EPP Change
   Mapping.
- **draft-gerke-publication-process-reform-08** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.
- **draft-goto-otp-token-01** (new-draft, score 0, ignored_after_review) [none]: [The `OTP-Token` Email Header Field](https://datatracker.ietf.org/doc/draft-goto-otp-token/) — This document defines the OTP-Token email header field, which can be
   used to deliver One-Time Passcodes (OTP) in a machine-readable and
   origin-bound manner alongside the human-readable message carrying
   that content today.  Recipient Message User Agents (rMUA) can
   collaborate with other entities in the ecosystem to assist in the
   delivery of these codes to the context which wishes to verify their
   successful delivery.
- **draft-gregoire-moq-msfts-01** (new-draft, score 0, ignored_after_review) [none]: [MPEG-2 Transport Stream Packaging for MOQT](https://datatracker.ietf.org/doc/draft-gregoire-moq-msfts/) — This document extends the MOQT Streaming Format (MSF) catalog by
   defining the "mpeg2ts" packaging value for carrying MPEG-2 Transport
   Stream and M2TS source packets over MOQT.  It defines catalog-
   extension fields for transport-stream track description and specifies
   subscriber behavior for joining, switching, and validating packetized
   streams.
- **draft-halpern-rtgwg-not-a-dump-truck-00** (new-draft, score 0, ignored_after_review) [none]: [The IGP is not a Dump Truck](https://datatracker.ietf.org/doc/draft-halpern-rtgwg-not-a-dump-truck/) — This document explores addressing the problem of using an IGP to
   carry arbitrary information, often referred to using the phrase "the
   IGP is not a dump truck".  It describes the kinds of information
   carried in an IGP and proposes an approach to changing the system.
- **draft-he-idr-bgp-ec-sr-pm-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Extended Communities for SR Policy Performance Metrics](https://datatracker.ietf.org/doc/draft-he-idr-bgp-ec-sr-pm/) — Traffic scheduling and optimization have become routine network
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
- **draft-helmprotocol-confidence-01** (new-draft, score 0, ignored_after_review) [none]: [Oracle Confidence Gating: G-Score, Correlation-Aware von Neumann Confidence, and AdaptiveSwitch](https://datatracker.ietf.org/doc/draft-helmprotocol-confidence/) — This document specifies an optional confidence layer for the TLS
   TimeToken Secure Protocol (TTTPS).  It defines the G-Score, a
   normalized entropy measure of agreement concentration; an optional
   correlation-aware von Neumann extension; the InsufficientKnowledge
   signal; and the AdaptiveSwitch state machine over TURBO and FULL.
   The confidence layer qualifies whether evidence justifies action.  It
   does not replace cryptographic integrity, define a wire format,
   allocate a codepoint, establish source independence, or require any
   core TTTPS implementation to compute confidence.
- **draft-hoffman-duj-06** (new-draft, score 0, ignored_after_review) [none]: [DNS Update with JSON](https://datatracker.ietf.org/doc/draft-hoffman-duj/) — It is common for service providers such as certificate authorities
   and social media providers to want users to update the users' zones
   to prove that they control those zones, or to add other features.
   Currently, service providers tell users to do this using human
   language describing the resource record type and data values to enter
   into the zone.  This document describes a text format, called "DNS
   update with JSON" or "DUJ", for such a service provider to give to a
   user, with the expectation that the user would copy and paste the
   text to their DNS operator to update the user's zone.  DNS operators
   who know how to handle DUJ strings will make the update process
   easier and more predictable for their users.
- **draft-holmgren-at-repository-03** (new-draft, score 0, ignored_after_review) [none]: [Authenticated Transfer: Repository and Synchronization](https://datatracker.ietf.org/doc/draft-holmgren-at-repository/) — This document specifies a repository data structure and
   synchronization mechanisms for public data as part of the
   Authenticated Transfer Protocol (ATP).  It describes encoding formats
   for both individual data records and entire repositories.  The
   repository data structure is content-addressable and
   cryptographically authenticated.  For synchronization, it specifies
   both a low-latency streaming protocol over WebSocket, and a full-
   repository fetch mechanism over HTTP.
- **draft-housley-asn1-layman-guide-03** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-ietf-avtcore-rtp-jpegxs-3ed-08** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for ISO/IEC 21122 (JPEG XS)](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-jpegxs-3ed/) — This document specifies a Real-Time Transport Protocol (RTP) payload
   format for transport of a video signal encoded with JPEG XS (ISO/IEC
   21122).  JPEG XS is a low-latency and low-complexity video coding
   system.  Employing this format allows achieving encoding-decoding
   latencies confined to a fraction of a video frame.

   This document revises RFC 9134 to incorporate support for new
   features introduced in the third edition of JPEG XS.  Most notably,
   it contains the necessary provisions to support the TDC coding mode.
   This document obsoletes RFC 9134; however, the revised payload format
   is designed to ensure that existing conforming implementations of RFC
   9134 remain valid under the updated specification.  Additionally,
   this document consolidates the errata of RFC 9134 and includes
   improvements and clarifications for implementers and users.
- **draft-ietf-avtcore-rtp-vdmc-04** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for V-DMC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-vdmc/) — This memo outlines RTP payload formats for the Video-based Dynamic
   Mesh Coding (V-DMC), which comprises several types of components,
   such as a basemesh, AC-based displacements, 2D representations of
   attributes, and an atlas.  This document focuses on describing the
   basemesh and displacement, while the RTP payload formats for the
   atlas and attributes are addressed in other documents.  The RTP
   payload header formats enable the packetization of a basemesh or
   displacement Network Abstraction Layer (NAL) unit in an RTP packet
   payload as well as fragmentation of a NAL unit into multiple RTP
   packets.
- **draft-ietf-bier-lsr-non-mpls-extensions-05** (new-draft, score 0, ignored_after_review) [bier]: [LSR Extensions for BIER non-MPLS Encapsulation](https://datatracker.ietf.org/doc/draft-ietf-bier-lsr-non-mpls-extensions/) — Bit Index Explicit Replication (BIER) is an architecture that
   provides multicast forwarding through a "BIER domain" without
   requiring intermediate routers to maintain multicast related per-flow
   state.  BIER can be supported in MPLS and non-MPLS networks.

   This document updates RFC8296 and specifies the required extensions
   to the IS-IS, OSPFv2 and OSPFv3 protocols for supporting BIER in non-
   MPLS networks using BIER non-MPLS encapsulation.
- **draft-ietf-bmwg-sr-bench-meth-09** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR) Forwarding](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) forwarding performance for Segment Routing over IPv6 (SRv6) and
   MPLS (SR-MPLS).
- **draft-ietf-dnsop-zone-cut-to-nowhere-00** (new-draft, score 0, ignored_after_review) [dnsop]: [Signalling a Zone Cut to Nowhere in the DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-zone-cut-to-nowhere/) — This document defines a standard mechanism to signal the existence of
   a DNS zone cut without specifying authoritative nameservers for the
   delegated child zone.  This "zone cut to nowhere" is particularly
   useful in split-horizon environments, allowing parent zones to
   explicitly signal that a child zone exists but is only resolvable
   within a private namespace.
- **draft-ietf-grow-downgrade-bgp-community-01** (new-draft, score 0, ignored_after_review) [grow]: [The DOWNGRADE BGP Community for Denial-of-Service Attack Mitigation](https://datatracker.ietf.org/doc/draft-ietf-grow-downgrade-bgp-community/) — This document outlines a method to mitigate Denial of Service (DoS)
   attacks by using a well-known BGP community named "DOWNGRADE" as
   signal to neighboring networks to treat traffic destined towards
   "DOWNGRADE" tagged IP prefixes with low precedence.  The "downgrade"
   strategy offers an appealing alternative to Remote Triggered
   Blackhole (RTBH) filtering, because RTBH filtering completes the DoS
   attack and hampers the defender's ability to monitor whether the
   attack is still ongoing.
- **draft-ietf-hpke-hpke-05** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document describes a scheme for hybrid public key encryption
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
- **draft-ietf-idr-5g-edge-service-metadata-34** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extension for 5G Edge Service Metadata](https://datatracker.ietf.org/doc/draft-ietf-idr-5g-edge-service-metadata/) — This draft describes a new Edge Metadata Path Attribute and some Sub-
   TLVs for egress routers to advertise the Edge Metadata about the
   attached edge services (ES).  The edge service Metadata can be used
   by the ingress routers in the 5G Local Data Network to make path
   selections not only based on the routing cost but also the running
   environment of the edge services.  The goal is to improve latency and
   performance for 5G edge services.

   The extension enables an edge service at one specific location to be
   more preferred than the others with the same IP address (ANYCAST) to
   receive data flow from a specific source, like a specific User
   Equipment (UE).
- **draft-ietf-idr-bgp-bestpath-nh-selection-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP best path next-hop selection enhancements](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-bestpath-nh-selection/) — BGP [RFC4271] has originally been designed to carry IPv4 routing
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
- **draft-ietf-idr-performance-routing-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Performance-aware Routing Mechanism](https://datatracker.ietf.org/doc/draft-ietf-idr-performance-routing/) — The current Border Gateway Protocol (BGP) specification does not
   incorporate network performance metrics, such as network latency,
   into its route selection process.  This document outlines a
   performance-aware BGP routing mechanism that integrates network
   latency as a critical criterion for route selection.  This innovative
   approach is particularly beneficial for server providers with a
   global presence, enabling them to offer low-latency network
   connectivity service as a value-added service to their customers.
- **draft-ietf-mpls-on-path-telemetry-flag-05** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes postcard-based on-path telemetry with packet
   marking (PBT-M) using an MPLS Network Actions (MNA) flag to support
   Operations, Administration, and Maintenance (OAM) in MPLS networks.
   The scheme uses a single flag bit carried in a Flag-Based Network
   Action Indicator (Opcode 1) of the MNA Sub-Stack as defined in RFC
   9994.  In addition to addressing the protocol requirements for
   applying PBT-M, this document provides comprehensive operational,
   manageability, and security considerations.
- **draft-ietf-nfsv4-rfc8881bis-11** (new-draft, score 0, ignored_after_review) [nfsv4]: [Network File System (NFS) Version 4 Minor Version 1 Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-rfc8881bis/) — This document describes the Network File System (NFS) version 4 minor
   version 1, including features retained from the base protocol (NFS
   version 4 minor version 0, which is specified in RFC 7530) and
   protocol extensions made and part of Minor Version 1.  The later
   minor version has no dependencies on NFS version 4 minor version 0,
   and was, until recently, documented as a completely separate
   protocol.

   This document is part of a set of documents which collectively
   obsolete RFCs 8881 and 8434.  In addition to many corrections and
   clarifications, it will rely on NFSv4-wide documents to substantially
   revise the treatment of protocol extension, internationalization, and
   security, superseding the descriptions of those aspects of the
   protocol appearing in RFCs 5661 and 8881.
- **draft-ietf-nfsv4-uncacheable-directories-12** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Dirent Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  Such
   a cache is not invalidated by the directory's change attribute, which
   reflects changes to the directory and its entries but not writes to
   the files those entries name, so it can become stale when another
   client changes one of those files.  In some deployments this produces
   incorrect size and timestamp values often enough to be a problem.
   This document introduces an uncacheable dirent metadata attribute for
   NFSv4.2 that allows a server to identify a directory for which an
   honoring client enumerates by READDIR and reports each entry's
   attributes as that READDIR returned them, rather than from a value it
   held earlier.
- **draft-ietf-openpgp-external-secrets-00** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-ietf-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
- **draft-ietf-openpgp-nist-bp-comp-05** (new-draft, score 0, ignored_after_review) [openpgp]: [PQ/T Composite Schemes for OpenPGP using NIST and Brainpool Elliptic Curve Domain Parameters](https://datatracker.ietf.org/doc/draft-ietf-openpgp-nist-bp-comp/) — This document defines PQ/T ("post-quantum/traditional") composite
   schemes based on ML-KEM and ML-DSA combined with ECDH and ECDSA
   algorithms using the NIST and Brainpool domain parameters for the
   OpenPGP protocol [RFC9580], and as such extends [RFC9980].
- **draft-ietf-opsawg-rfc5706bis-08** (new-draft, score 0, ignored_after_review) [opsawg]: [Guidelines for Considering Operations and Management in IETF Specifications](https://datatracker.ietf.org/doc/draft-ietf-opsawg-rfc5706bis/) — New Protocols and Protocol Extensions are best designed with due
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
- **draft-ietf-pce-entropy-label-position-06** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extension for SR-MPLS Entropy Label Positions](https://datatracker.ietf.org/doc/draft-ietf-pce-entropy-label-position/) — The Entropy label (EL) can be used in the SR-MPLS data plane to
   improve load-balancing and multiple Entropy Label Indicator (ELI)/EL
   pairs may be inserted in the SR-MPLS label stack as per RFC8662.

   This document defines a set of extensions for Path Computation
   Element Communication Protocol (PCEP) to configure where in the label
   stack the ELI/EL pairs should be inserted in SR-MPLS network - the
   Entropy Label Positions (ELP).
- **draft-ietf-pim-gaap-25** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
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
- **draft-ietf-pim-ipv6-zeroconf-assignment-12** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the criteria listed in RFC 10019.
- **draft-ietf-radext-connectinfo-00** (new-draft, score 0, ignored_after_review) [radext]: [A syntax for the RADIUS Connect-Info attribute used in Wi-Fi networks](https://datatracker.ietf.org/doc/draft-ietf-radext-connectinfo/) — This document describes a syntax for the Connect-Info attribute used
   with the RADIUS protocol, enabling RADIUS clients to provide RADIUS
   servers information pertaining to a user's connection with an IEEE
   802.11 wireless network.
- **draft-ietf-regext-balance-03** (new-draft, score 0, ignored_after_review) [regext]: [Balance Mapping for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-ietf-regext-balance/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for retrieving the client balance and other financial
   information.
- **draft-ietf-satp-core-17** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer Protocol (SATP) Core](https://datatracker.ietf.org/doc/draft-ietf-satp-core/) — This memo describes the Secure Asset Transfer Protocol (SATP) for
   digital assets.  SATP is a protocol operating between two gateways
   that conducts the transfer of a digital asset from one gateway to
   another, each representing their corresponding digital asset
   networks.  The protocol establishes a secure channel between the
   endpoints and implements a 2-phase commit (2PC) to ensure the
   properties of transfer atomicity, consistency, isolation and
   durability.
- **draft-ietf-scone-protocol-09** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-tiptop-usecase-03** (new-draft, score 0, ignored_after_review) [tiptop]: [IP in Deep Space: Key Characteristics, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-tiptop-usecase/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  Most of the IP protocol stack
   used on the Internet, in particular reliable transport protocols and
   applications, is based on the assumptions of shorter delays and
   mostly uninterrupted communications.  This document describes the key
   characteristics, use cases, and requirements for deep space
   networking, intended to help when profiling IP protocols in such
   environment.
- **draft-ietf-v6ops-ipv6-only-03** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
- **draft-johnson-dtn-dtpc-00** (new-draft, score 0, ignored_after_review) [none]: [Delay-Tolerant Payload Conditioning (DTPC) Protocol Specification](https://datatracker.ietf.org/doc/draft-johnson-dtn-dtpc/) — This document specifies the Delay-Tolerant Payload Conditioning
   (DTPC) protocol.  DTPC is an end-to-end, connectionless, expandable
   application service protocol designed to operate directly above the
   Bundle Protocol (BPv7).  It provides transparent application data
   conditioning services across challenged networks, including
   controlled aggregation of Application Data Units (ADUs), application-
   specific elision, transmission-order tracking, end-to-end positive/
   negative acknowledgments, and duplicate suppression.  DTPC preserves
   the end-to-end principle across delay-tolerant networks where
   intermediate nodes execute store-and-forward operations.
- **draft-kazuho-ccwg-cuback-00** (new-draft, score 0, ignored_after_review) [none]: [CUBACK: CUBIC Driven by the ACK Clock](https://datatracker.ietf.org/doc/draft-kazuho-ccwg-cuback/) — This document specifies Cuback, an ACK-driven reformulation of CUBIC
   congestion control.  It simplifies implementation by replacing
   CUBIC's mutable time- and ACK-driven state with pure functions over
   immutable per-epoch parameters, for which test vectors are provided.
   Congestion-window growth uses the same ACK-driven mechanism as Reno,
   removing several sources of implementation error.  When entering a
   high-capacity path, a newcomer converges on its share sooner than
   under CUBIC, so short flows complete earlier.
- **draft-lcurley-moq-cluster-01** (new-draft, score 0, ignored_after_review) [none]: [MoQ Cluster Extension](https://datatracker.ietf.org/doc/draft-lcurley-moq-cluster/) — This document defines a clustering extension for MoQ Transport
   [moqt], used to build a mesh of relays.  Each namespace advertisement
   carries the list of Hop IDs it has passed through, starting with the
   original publisher, and the accumulated cost of that path.  A
   receiver uses the list to detect loops and to tell which
   advertisements come from the same publisher, and the cost to choose
   between paths.  Each endpoint declares its own Hop ID at setup, so a
   peer never advertises or serves it a path that already passed through
   it.
- **draft-lcurley-moq-flate-00** (new-draft, score 0, ignored_after_review) [none]: [DEFLATE Compressed Tracks for MoQ](https://datatracker.ietf.org/doc/draft-lcurley-moq-flate/) — This document specifies how a MoQ Transport [moqt] track carries
   DEFLATE-compressed payloads.  Each subgroup is one raw DEFLATE
   stream, sync flushed at each object boundary, so every object stays
   self-delimited while later objects compress against the earlier ones
   in the subgroup.  Small repetitive payloads compress several times
   better than they do alone, and a dropped group costs nothing beyond
   itself because the window never spans one.  Nothing is added to the
   wire: the application declares the track compressed, and a relay
   forwards it unchanged.
- **draft-lcurley-moq-lite-06** (new-draft, score 0, ignored_after_review) [none]: [Media over QUIC - Lite](https://datatracker.ietf.org/doc/draft-lcurley-moq-lite/) — moq-lite is designed to fanout live content 1->N across the internet.
   It leverages QUIC to prioritize important content, avoiding head-of-
   line blocking while respecting encoding dependencies.  While
   primarily designed for media, the transport is payload agnostic and
   can be proxied by relays/CDNs without knowledge of codecs,
   containers, or encryption keys.
- **draft-lcurley-moq-solicit-00** (new-draft, score 0, ignored_after_review) [none]: [MoQ Solicit Extension](https://datatracker.ietf.org/doc/draft-lcurley-moq-solicit/) — This document defines an extension for MoQ Transport [moqt] that lets
   an endpoint declare that advertisements to it must be solicited
   first.  An endpoint that declares nothing receives unsolicited
   PUBLISH_NAMESPACE, which is what a peer unaware of this extension
   implicitly asks for.  An endpoint that will instead ask for what it
   wants says so once during setup, and is spared the advertisements it
   would otherwise have to ignore.  Because sending the option at all
   identifies an endpoint that implements this extension, the
   requirement is enforceable between two such endpoints rather than
   merely advisory.
- **draft-lehmann-idmefv2-https-transport-07** (new-draft, score 0, ignored_after_review) [none]: [Transport of Incident Detection Message Exchange Format version 2 (IDMEFv2) Messages over HTTPS](https://datatracker.ietf.org/doc/draft-lehmann-idmefv2-https-transport/) — The Incident Detection Message Exchange Format version 2 (IDMEFv2)
   defines a data representation for security incidents detected on
   cyber and/or physical infrastructures.

   This draft is maintained by the IDMEFv2 Task Force.  Please consult
   our website for more information. https://www.idmefv2.org

   The format is agnostic so it can be used in standalone or combined
   cyber (SIEM), physical (PSIM) and availability (NMS) monitoring
   systems.  IDMEFv2 can also be used to represent man made or natural
   hazards threats.

   IDMEFv2 improves situational awareness by facilitating correlation of
   multiple types of events using the same base format thus enabling
   efficient detection of complex and combined cyber and physical
   attacks and incidents.

   This document defines a way to transport IDMEFv2 Alerts over HTTPs.

   If approved this document would obsolete RFC4767.
- **draft-li-savnet-source-prefix-advertisement-07** (new-draft, score 0, ignored_after_review) [none]: [Source Prefix Advertisement for Intra-domain SAVNET](https://datatracker.ietf.org/doc/draft-li-savnet-source-prefix-advertisement/) — This document describes a mechanism for generating interface-based
   prefix allowlists for intra-domain source address validation (SAV) on
   external interfaces facing directly connected hosts or non-BGP
   customer networks.  The mechanism derives source prefixes from
   routing information and combines them with source prefixes
   provisioned by the AS operator.  Routers use the combined source
   prefixes to generate SAV allowlists.
- **draft-liu-add-dnssd-edns-04** (new-draft, score 0, ignored_after_review) [none]: [DNS-Based Service Discovery for Encrypted DNS Services](https://datatracker.ietf.org/doc/draft-liu-add-dnssd-edns/) — This document defines a DNS-Based Service Discovery (DNS-SD)
   mechanism for discovering encrypted DNS services in local networks.
   It specifies new service types (_dot._tcp, _doh._tcp, _doq._udp) and
   associated service parameters to enable zero-configuration discovery
   of DNS over TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ)
   resolvers.  This mechanism is defined for use with multicast DNS
   (mDNS), addressing critical privacy gaps in local networks while
   maintaining backward compatibility with RFC 6763.  This document
   leverages SVCB and HTTPS resource records (RFC 9460) for parameter
   negotiation, with TXT records provided for compatibility with legacy
   implementations.
- **draft-liu-fann-srv6-cc-01** (new-draft, score 0, ignored_after_review) [none]: [Congestion Control Based on SRv6 Path](https://datatracker.ietf.org/doc/draft-liu-fann-srv6-cc/) — This document describes a congestion control solution based on SRv6.
   It defines mechanisms for congestion notification and flow control
   within an SRv6-based network, optimizing congestion handling through
   hierarchical congestion control messages along SRv6 paths.
- **draft-martin-deploying-ipv6-data-center-03** (new-draft, score 0, ignored_after_review) [none]: [Deploying IPv6 in Data Centers](https://datatracker.ietf.org/doc/draft-martin-deploying-ipv6-data-center/) — Data center operators are moving toward IPv6-only operation to
   simplify addressing, restore end-to-end connectivity, and meet
   operator and government timelines.  Much published IPv6 guidance
   targets network engineers; this document instead addresses *Site
   Reliability Engineers (SREs)* and *Software Engineers (SWEs)* who
   deploy, operate, and debug services in *operator-owned data centers*.
   It is organized in four parts --- migration strategies, building the
   data center, tools and best practices, and pitfalls --- with IPv6
   fundamentals as an appendix.  It documents common software and
   infrastructure gaps and offers practical deployment patterns aligned
   with the IPv6 Operations (v6ops) working group charter.
- **draft-mnichols-protocols-not-the-internet-01** (new-draft, score 0, ignored_after_review) [none]: [Protocol Architects Are Not the Creators of the Internet](https://datatracker.ietf.org/doc/draft-mnichols-protocols-not-the-internet/) — TCP/IP standardized interoperability and end to end transport
   semantics.  The World Wide Web standardized publishing and retrieval.
   Neither TCP/IP nor the Web specifies, provisions, or enforces the
   path properties required for utility grade Internet operation at
   scale.

   This memo defines terminology to distinguish interoperability
   standards from utility grade operation and specifies operational
   requirements for "infrastructure activation": provisioned transport,
   interconnection strategy, routing policy control, redundancy,
   locality, continuous monitoring, incident response, and enforceable
   service accountability.  This memo proposes no protocol changes.
- **draft-munizaga-quic-alternative-server-address-02** (new-draft, score 0, ignored_after_review) [none]: [QUIC Alternative Server Address Frames](https://datatracker.ietf.org/doc/draft-munizaga-quic-alternative-server-address/) — This document specifies an extension to QUIC that allows a server to
   advertise a prioritized set of alternative addresses.  This allows a
   client to migrate the connection as the availability of, or
   preference among, server addresses changes.
- **draft-prz-lsr-ash-packets-05** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-ramakrishna-satp-data-sharing-06** (new-draft, score 0, ignored_after_review) [none]: [Protocol for Requesting and Sharing Views across Networks](https://datatracker.ietf.org/doc/draft-ramakrishna-satp-data-sharing/) — With increasing use of DLT (distributed ledger technology) systems,
   including blockchain systems and networks, for virtual assets, there
   is a need for asset-related data and metadata to traverse system
   boundaries and link their respective business workflows.  Systems and
   networks can define and project views, or asset states, outside of
   their boundaries, as well as guard them using access control
   policies, and external agents or other systems can address those
   views in a globally unique manner.  Universal interoperability
   requires such systems and networks to request and supply views via
   gateway nodes using a request-response protocol.  The endpoints of
   this protocol lie within the respective systems or in networks of
   peer nodes, but the cross-system protocol occurs through the systems’
   respective gateways.  The inter-gateway protocol that allows an
   external party to request a view by an address and a DLT system to
   return a view in response must be DLT-neutral and mask the internal
   particularities and complexities of the DLT systems.  The view
   generation and verification modules at the endpoints must obey the
   native consensus logic of their respective networks.
- **draft-ramakrishna-satp-views-addresses-08** (new-draft, score 0, ignored_after_review) [none]: [Views and View Addresses for Secure Asset Transfer](https://datatracker.ietf.org/doc/draft-ramakrishna-satp-views-addresses/) — With increasing use of DLT (distributed ledger technology) systems,
   including blockchain systems and networks, for virtual assets, there
   is a need for asset-related data and metadata to traverse system
   boundaries and link their respective business workflows.  Core
   requirements for such interoperation between systems are the
   abilities of these systems to project views of their assets to
   external parties, either individual agents or other systems, and the
   abilities of those external parties to locate and address the views
   they are interested in.  A view denotes the complete or partial state
   of a virtual asset, or the output of a function computed over the
   states of one or more assets, or locks or pledges made over assets
   for internal or external parties.  Systems projecting these views
   must be able to guard them using custom access control policies, and
   external parties consuming them must be able to verify them
   independently for authenticity, finality, and freshness.  The end-to-
   end protocol that allows an external party to request a view by an
   address and a DLT system to return a view in response must be DLT-
   neutral and mask the interior particularities and complexities of the
   DLT systems.  The view generation and verification modules at the
   endpoints must obey the native consensus logic of their respective
   systems.
- **draft-rzz-rtgwg-inter-domain-ebr-00** (new-draft, score 0, ignored_after_review) [none]: [BGP-based Inter-domain Elastic Bandwidth-aware Routing Framework](https://datatracker.ietf.org/doc/draft-rzz-rtgwg-inter-domain-ebr/) — Although operators typically consider redundant capacity during
   network design, link congestion may still occur under specific
   scenarios, such as link degradation or traffic bursts.  Several
   congestion mitigation mechanisms have been proposed for intra-domain
   links, but congestion is not limited to intra-domain links, it can
   also occur on inter-domain links.

   Since changes of available bandwidth do not trigger updates to BGP
   route selection, BGP cannot alleviate inter-domain link congestion
   automatically, causing packet loss or increased delay.

   This document defines a BGP-based inter-domain elastic bandwidth-
   aware routing (BEBR) mechanism, to alleviate inter-domain link
   congestion.  To avoid the dependency on cross-domain deployment, this
   document proposes both inbound BEBR and outbound BEBR, designed to
   address inbound and outbound traffic congestion, respectively.  Thus,
   the congestion on both directions of inter-domain links can be
   mitigated by deploying BEBR on only one side of the inter-domain
   link.
- **draft-salaheldin-bcnp-00** (new-draft, score 0, ignored_after_review) [none]: [Brain Control Network Protocol (BCNP)](https://datatracker.ietf.org/doc/draft-salaheldin-bcnp/) — The Brain Control Network Protocol (BCNP) is a binary, TCP-based
   application-layer protocol for discovering, configuring, and
   commanding networked devices from a single controller using a small,
   fixed vocabulary of discrete control inputs, such as those produced
   by a brain-computer interface.  A Controller establishes a private
   wireless network that Devices join, discovers Devices and assigns
   each a persistent address, discovers and registers the Actions a
   Device can perform, and subsequently issues short, stateless
   commands, expressed through that same small input vocabulary, to
   elicit those Actions.  This document specifies BCNP's binary message
   formats, its Discovery, Pairing, and Command phases, and the
   reconciliation mechanism used to recover from lost acknowledgments
   and Devices that change network address.
- **draft-sayre-tppietf-00** (new-draft, score 0, ignored_after_review) [none]: [TPPIETF: The Proverbial Printer Impeding Encryption Task Forces](https://datatracker.ietf.org/doc/draft-sayre-tppietf/) — It is said to be in the basement.

   Despite decades of work by the Internet Engineering Task Force to
   develop, standardize, and promote transport layer security, global
   deployment remains incomplete.  This document investigates the
   primary obstacle to universal encryption: a class of legacy printing
   devices, often located in building basements, that are cited as
   justification for continued plaintext transmission.  This document
   provides a taxonomy of such devices, analyzes the rhetorical
   structure of printer-based encryption exemption claims, and proposes
   a framework for evaluating their validity.
- **draft-shabazz-http-x402-tswp-00** (new-draft, score 0, ignored_after_review) [none]: [The X402 Typed Settlement Wire Protocol (X402-TSWP)](https://datatracker.ietf.org/doc/draft-shabazz-http-x402-tswp/) — This document specifies the X402 Typed Settlement Wire Protocol
   (X402-TSWP), an application-layer extension to Hypertext Transfer
   Protocol status code 402 (Payment Required).  X402-TSWP defines
   machine-to-machine challenge-response headers, operational type
   discriminators, and deterministic multi-rail blockchain carrier
   grammars.  On parallel execution environments, X402-TSWP eliminates
   runtime regular-expression parsing in favor of byte-exact equality
   verification via instruction introspection, establishing atomic
   non-repudiation between web services, SWIFT ISO 20022 messages, and
   public ledger state transitions.
- **draft-song-lamps-pq-composite-frodokem-00** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   ECDH, X25519, and X448.  This document specifies the algorithm
   definitions, key formats, and certificate conventions for using
   Composite FrodoKEM in the X.509 Public Key Infrastructure.
- **draft-tt-netmod-yang-config-templates-04** (new-draft, score 0, ignored_after_review) [none]: [YANG Configuration Templates](https://datatracker.ietf.org/doc/draft-tt-netmod-yang-config-templates/) — This document defines a YANG-based configuration template mechanism
   whereby repetitive configuration data can be factored out into
   templates and applied where needed.  This avoids the redundant
   definition of identical configuration and ensures the consistency of
   it, thus allowing configuration data to be managed more conveniently
   and efficiently.
- **draft-wang-idr-flowspec-dip-origin-as-filter-14** (new-draft, score 0, ignored_after_review) [none]: [Destination-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-dip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification (FlowSpec) to enable filtering based on the
   Origin Autonomous System (AS) of the destination IP address.  This
   extension is particularly useful in mitigating Distributed Denial of
   Service (DDoS) attacks or optimizing traffic redirection where the
   target IP addresses are numerous or rapidly changing, but belong to a
   specific destination Origin AS.
- **draft-wang-idr-flowspec-sip-origin-as-filter-02** (new-draft, score 0, ignored_after_review) [none]: [Source-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-sip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification (FlowSpec) to enable filtering based on the
   Origin Autonomous System (AS) of the source IP address.  This
   extension is particularly useful in mitigating Distributed Denial of
   Service (DDoS) attacks where the source IP addresses are dynamic or
   numerous but belong to a specific source AS.
- **draft-xsaopig-nmop-service-flow-modal-mapping-06** (new-draft, score 0, ignored_after_review) [none]: [Architecture for Service Flow Characteristics and Modal Mapping Based on SDN and ALTO Protocol](https://datatracker.ietf.org/doc/draft-xsaopig-nmop-service-flow-modal-mapping/) — This Internet-Draft specifies a comprehensive framework for mapping
   service flow characteristics to network modal resources in multi-
   modal intelligent computing networks.  It introduces the use of the
   ALTO protocol for collecting service flow data and leverages an SDN
   architecture to separate control and data planes.  The ALTO protocol
   facilitates the acquisition of diverse network state information,
   including data from several SDN domains and dynamic network
   environments, directly from controllers while keeping the provider's
   internal details confidential.  It then transmits the controller's
   decisions using a proven method.  The document details methods for
   characteristic identification, intelligent mapping, and continuous
   optimization, enabling dynamic resource allocation and improved
   network performance.  The framework is designed to support scalable,
   efficient, and secure operations in environments with complex network
   loads and diverse service requirements.
- **draft-xu-idr-neighbor-autodiscovery-14** (new-draft, score 0, ignored_after_review) [idr]: [BGP Neighbor Discovery](https://datatracker.ietf.org/doc/draft-xu-idr-neighbor-autodiscovery/) — BGP is being used as the underlay routing protocol in some large-
   scaled data centers (DCs).  Most popular design followed is to do
   hop-by-hop external BGP (EBGP) session configurations between
   neighboring routers on a per link basis.  The provisioning of BGP
   neighbors in routers across such a DC brings its own operational
   complexity.

   This document introduces a BGP neighbor discovery mechanism that
   greatly simplifies BGP operations in such DC and other networks by
   automatic setup of BGP sessions between neighbor routers using this
   mechanism.
- **draft-zhao-cats-otn-applicability-03** (new-draft, score 0, ignored_after_review) [none]: [Framework and Applicability of Computation-aware Traffic Steering (CATS) in Optical Transport Networks (OTN)](https://datatracker.ietf.org/doc/draft-zhao-cats-otn-applicability/) — Computation-aware Traffic Steering (CATS) offers a framework for
   selecting computation service sites based on computation capabilities
   and load, and considering the network capabilities and state on the
   paths to the sites.

   Optical Transport Networks (OTN) provide guaranteed separation of
   traffic along with reserved hardware resources offering bandwidth and
   quality of service promises.

   This document describes how OTN may be used to support a CATS system
   to achieve the stringent performance targets required by demanding
   service environments.

## Errors / fetch failures

_None._
