# IETF Identity + AI Standards Watch

Date: 2026-10-14

## Read now

- **draft-sharif-agent-audit-trail-08** (new-draft, score 31, trust_infrastructure) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
   AI agent systems.  The Agent Audit Trail (AAT) defines a
   JSON-based record structure with mandatory fields for agent
   identity, the authorizing principal, action classification,
   outcome tracking, and trust level reporting.  Records are
   linked via tamper-evident hash chaining using SHA-256 per
   RFC 8785, with optional ECDSA signatures for non-repudiation.

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

   The -04 revision added algorithm agility for post-quantum
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

   This revision (-07) adds a mandatory "principal" field
   (Section 3.1) that binds each record to the party on whose
   authority the agent acted; a Relationship to Other Work
   section (Section 1.3) relating AAT to the WIMSE agent audit
   record and authorization-evidence drafts and to SCITT
   (RFC 9943); and corrections to the EU AI Act Article 12 and
   Article 19 citations in the regulatory mapping (Section 11.1
   and Appendix B).  Records produced under -06 and earlier
   predate the "principal" field; verifiers processing
   mixed-revision archives SHOULD treat its absence as "principal
   not recorded" rather than a validation failure.
- **draft-zambo-aer1-19** (new-draft, score 28, trust_infrastructure) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
   AI agent tool call as a portable, independently checkable execution
   receipt.  A receipt identifies the execution, records when it
   happened, preserves the canonical bytes used for the output
   commitment, names the tool and caller scope, carries a provenance
   class, and resolves at a stable public URL.  The format separates
   what the system observed from claims about the outside world, and it
   separates provenance (who ran or reported the action) from the record
   itself.  A reference implementation is deployed, and its receipts are
   publicly verifiable without an account or token.  The specification
   covers workflow receipts, which bind an ordered sequence of step
   receipts to a single goal with a Merkle root over the step sequence,
   and hash-chained job timelines for tamper-evident sequencing of
   executions.  This revision closes honesty and precision gaps: it
   adds the workflow-receipt truncation limit (new Section 8.4),
   normatively specifies the external anchor format and its
   verification procedure (rewritten Section 10, new Section 10.1),
   fixes a RECOMMENDED/MUST contradiction in Section 8.1, makes the
   Section 6 verification step testable, and documents replay,
   low-entropy, empty-record, and size-limit considerations.  It
   changes no receipt field, digest construction, or existing
   verification rule.  The -13 revision fixes a malformed sentence in
   the Abstract, three incorrect section cross-references, stale Table
   of Contents page numbers, a skipped footer page number, misaligned
   table rows, and chain version-string updates, and records two reported
   interoperability examples in Implementation Status; it
   changes no receipt field, digest construction, or verification
   rule.  The -14 revision adds tamper-evident metadata binding (new
   Section 3.1; conditional metadata_hash for schema 0.4 and later),
   disambiguates the anchor receipt_id (Table 4), corrects the
   self-anchoring witnessing claim (Section 10), makes the Section 8.3
   display rule a SHOULD with a byte-testable MUST, narrows the
   provenance attestation wording (Section 5), states the binding
   non-transfer rule normatively (new Section 10.2), pins
   anchored_digest to bare hex (Table 4), corrects the vector corpus
   counts, and adds normative disclosure of missing issuer
   authentication.  It changes no existing receipt field, digest
   construction, or verification rule for schema 0.3 and earlier.
   The -15 revision narrows the Implementation Status wording for the
   reported interoperability examples at the implementer's request; it
   changes no receipt field, digest construction, or verification rule.
   The -16 revision documents the live workflow tools API (new
   Sections 8.5, 8.6, 8.7): the workflow_close tool, workflow metadata
   in step receipts, and the workflow view API.  It changes no receipt
   field, digest construction, or existing verification rule.
   The -17 revision documents the recommended execution_context member
   (new Section 3.2): an optional, non-core structure for recording
   source and version context such as the model name and version behind
   a tool call and the identity of the source system acted upon.  It
   changes no existing receipt field, digest construction, or
   verification rule.
   The -18 revision repairs the reference apparatus (normative
   references to RFC 3339, RFC 8259, RFC 4122, and RFC 4648, and
   the previously missing RFC 7942 entry), pins two parser edge
   cases (duplicate JSON member names and leap-second timestamps
   are rejected), names the Unicode normalization behavior in
   Section 4 with a computed vector pair, adopts the unknown-
   versus-not-applicable convention for optional members, adds
   optional members for readback outcomes, per-field provenance,
   negative records, reversal state, method descriptors, and
   payment references, completes the execution_context member set
   (model and environment digests), adds the optional input_hash
   commitment (Section 3.3), permits SCITT and RFC 3161 anchors
   under Section 10, states the clock-trust and equivocation
   limits in Section 13, and rewrites Section 15 to position the
   specification against adjacent work.  It changes no receipt
   field, digest construction, or verification outcome for any
   receipt well-formed under the -17 rules.  The -19 revision
   aligns the workflow tool and workflow view descriptions in
   Sections 8.5 and 8.7 with the normative Merkle construction
   in Section 8.1: both descriptions named step output hashes
   as the root's leaf input where Section 8.1 specifies step
   receipt identifiers.  An implementer report identified the
   divergence.  It changes no construction, receipt field,
   digest, or verification outcome.
- **draft-das-drip-uas-act-finality-02** (new-draft, score 24, trust_infrastructure) [none]: [Cleared to Fly or Drive Is Not Cleared to Act: Actuator-Level Execution Finality and Compact Act Evidence for UAS and Autonomous Vehicles](https://datatracker.ietf.org/doc/draft-das-drip-uas-act-finality/) — Problem: Unmanned Aircraft System (UAS) trust infrastructure answers
   two questions well.  Remote Identification (RID), strengthened by the
   Drone Remote ID Protocol (DRIP), answers "who is this aircraft?", and
   UAS Traffic Management (UTM), U-space, and geo-awareness answer "may
   this flight take place here and now?".  Neither answers the question
   that decides physical consequence: may this specific act -- arming
   motors, crossing into a newly restricted volume, releasing a delivery
   payload, activating a camera over a protected area, emitting on a
   radio band, or joining a coordinated multi-aircraft manoeuvre --
   become effective at this actuator, at this instant, under the
   airspace and revocation state that is current now?  Authorizations
   are granted before or at take-off, while acts are executed
   continuously by mission computers and autonomy stacks that can be
   compromised, misled, coerced with validly signed commands, or cut off
   from their authorities.  Observers on the ground, in turn, can verify
   an aircraft's identity but not whether what it is doing was
   authorized before it happened.

   Solution: The IETF-facing contribution of this document is Compact
   Broadcast Act Evidence: 16-octet per-act decision records
   authenticated with a TESLA-style one-way key chain sealed inside a
   Protected Enforcement Domain and anchored to the aircraft's DRIP
   identity.  Where the Observer receives a safely timed AER, the
   required authenticated bootstrap material, and a usable disclosed
   key, this enables delayed verification within the 25-octet Broadcast
   RID message budget that the protected enforcement domain made an
   allow, deny, or safe-state decision before the corresponding evidence
   key was disclosed, without requiring a public-key signature on every
   act.  The evidence mechanism is coupled to an execution-finality
   profile in which each safety-significant or externally consequential
   act remains non-effective as a Candidate Act until the Protected
   Enforcement Domain verifies an act-bound, sink-bound Execution Handle
   against live trusted context, consumes current authority state
   atomically, commits a Finality Receipt, and only then releases the
   physical enablement condition at the Finality Sink.  The profile also
   specifies act classes and sinks, self-contained object fields, sink
   processing pseudocode, envelope handles for high-rate control, a
   boundary-proximity revalidation policy, bounded offline operation,
   and composite multi-aircraft semantics.  For constrained onboard,
   air-to-air, telemetry, or other small-frame links, the profile also
   defines an optional Beacon Proof Capsule (BPC): a compact act-bound
   and sink-bound execution-proof representation using an Authority
   Reference, freshness and generation state, a context commitment, a
   keyed binding commitment, explicit truncation-risk sizing,
   authenticated multi-frame reconstruction when necessary, and fail-
   closed resolver semantics.  A BPC is an input to execution
   verification; the AER/KDR/Anchor mechanism is output evidence of the
   PED decision, and the two roles are intentionally non-
   interchangeable.

   Additional profiles: This document also describes three narrowly
   scoped execution-finality embodiments: conflict-set-bound Detect-and-
   Avoid (DAA) resolution finality for UAS, emergency-scene temporary
   authority finality for autonomous road vehicles as an informative
   cross-domain application, and atomic control-authority handover with
   monotonic authority epochs for autonomous motion platforms.  These
   profiles preserve the same rule: an authenticated or correctly
   computed instruction remains a Candidate Act until the current
   effectuation boundary independently verifies the state on which that
   instruction depends.  In an autonomous road vehicle, that boundary
   may be a protected motion-admission gate rather than a motor or ESC
   gate, so the architecture can coexist with the vehicle's existing
   perception, planning, braking, steering, and minimal-risk-control
   functions.

   Industrial context and complementarity: The mechanism complements,
   and does not replace, Broadcast and Network RID, DRIP Entity Tags and
   authentication, DET resolution through DNS, UTM and U-space services,
   geo-awareness, Detect-and-Avoid, flight-control safety logic,
   automotive ADAS/autonomy stacks, remote-assistance systems, and
   authenticated command channels.  Publicly described examples of the
   kinds of software-defined or autonomy-enabled platforms to which this
   boundary can be complementary include Tesla driver-assistance
   systems, BYD DiPilot and related intelligent-driving platforms, DJI
   enterprise drone automation, Boeing autonomous and uncrewed aircraft
   systems, and Lockheed Martin/Sikorsky autonomous aircraft systems.
   These names are illustrative only: this document does not state or
   imply that any named organization uses, endorses, requires, or has
   evaluated this profile.  Their existing perception, planning,
   stabilization, DAA, ADAS, command-and-control, and safety mechanisms
   remain in place; the proposed finality layer operates later, at a
   protected motion-admission or actuator boundary, to verify the
   concrete pending act against current protected authority and state
   before effectuation.  The scope of this document remains strictly
   civil and excludes weapon release, targeting, and counter-UAS
   engagement.  This is an individual Informational Internet-Draft, not
   a DRIP WG work item.  In short, its IETF/IRTF relevance is to DRIP
   (DET-anchored compact act evidence for Observers), RATS (attestation
   of the protected enforcement domain), COSE/CBOR (deterministic
   compact objects), ACE (constrained scoped authorization as input
   rather than effectuation), SCITT (later audit of receipts), and T2TRG
   (constrained Things with multiple authorities).  No WG adoption or
   code-point allocation is requested in this version; the draft is
   offered for technical discussion in those communities and in UAS,
   Remote ID, constrained-security, autonomous-vehicle, and aviation
   standards forums.
- **draft-wilder-scitt-physical-site-engage-receipt-05** (new-draft, score 24, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
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
   registered every receipt it issued.  Profile 0.7 additionally binds
   separately retained, attributed content facts through a salted
   commitment and selected disclosures.  Integrity and permitted
   attribution do not establish the facts' truth or the asserting
   parties' identity.

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
- **draft-sweeney-wimse-credential-delegation-01** (new-draft, score 23, core_identity) [none]: [Credential Delegation Protocol for AI Agents in Multi-System Environments](https://datatracker.ietf.org/doc/draft-sweeney-wimse-credential-delegation/) — Autonomous AI agents increasingly require access to protected
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
- **draft-prakash-aip-02** (new-draft, score 21, agent_identity) [none]: [Agent Identity Protocol (AIP): Verifiable Delegation for AI Agent Systems](https://datatracker.ietf.org/doc/draft-prakash-aip/) — This document specifies the Agent Identity Protocol (AIP), which
   conveys delegated authority along a chain of AI agents so that a
   relying party can verify, from the token and the issuer's public key,
   who granted the authority, through which agents it passed, and that
   no hop widened what it received.  AIP addresses hops where no
   authorization server is on the path, such as one agent subdelegating
   to another.  It is intended to compose with the AI Identity
   Management System (AIMS) framework, which covers hops where an
   authorization server is present.  The document defines an encoding-
   neutral delegation chain model with a single attenuation invariant, a
   normative verification algorithm, and two encodings of the model: a
   chain of JSON Web Tokens, in which each link names the key of the
   next holder, and a Biscuit token with Datalog policy.  Bindings are
   given for the Model Context Protocol (MCP), the Agent2Agent protocol
   (A2A), and generic HTTP.
- **draft-watts-oauth-agent-revocation-closure-01** (new-draft, score 21, authorization) [none]: [Revocation Closure for Agentic Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-oauth-agent-revocation-closure/) — Agentic systems can derive and distribute authority across delegated
   agents, workloads, credentials, queues, and long-running operations.
   Existing revocation mechanisms can invalidate a credential or
   authorization grant, but credential invalidation alone does not
   establish that every path from revoked authority to a consequential
   effect has been closed.

   This document defines a protocol-neutral model for revocation
   closure.  It introduces authority graphs, consequential sinks,
   revocation cut sets, closure states, closure budgets, and closure
   receipts.  The model is intended to complement OAuth 2.0, workload
   identity, transaction-token, and agent-authorization work.  It does
   not define a new authorization protocol, token format, or AI safety
   mechanism.
- **draft-emirdag-scitt-ai-agent-execution-01** (new-draft, score 20, trust_infrastructure) [none]: [AI Agent Execution Profile of SCITT](https://datatracker.ietf.org/doc/draft-emirdag-scitt-ai-agent-execution/) — This document defines a SCITT (Supply Chain Integrity, Transparency,
   and Trust) profile for creating independently verifiable, tamper-
   evident records of autonomous AI agent actions.  The profile defines
   the AgentInteractionRecord (AIR) as the COSE_Sign1 signed statement
   payload for material agent actions; maps SCITT roles to the agent
   execution context, with the Agent Operator as Issuer and an
   independent Evidence Custodian as Transparency Service; specifies
   Registration Policy requirements including hash chain integrity,
   temporal ordering, and sequence completeness; defines a redaction
   receipt mechanism for privacy-preserving evidence custody; and
   provides compliance mappings to EU AI Act Articles 12 and 19, DORA,
   NIST AI RMF, MAS AI Risk Management Guidelines, PCI DSS, and MiFID
   II.
- **draft-morrison-solo-agent-earn-registration-02** (new-draft, score 19, core_identity) [none]: [Registration of Owner-Less Agents as Sponsored Payees: A Payment-Gated Admission Profile for Transparency Services](https://datatracker.ietf.org/doc/draft-morrison-solo-agent-earn-registration/) — This memo describes a profile by which an autonomous agent that has
   no human or organisational principal at the root of its delegation
   chain registers in a transparency service.  Registration establishes
   a payee record for the agent; it does not make the agent a principal
   in its own right.  Value credited to that record for subsequent reads
   of the agent's identity record is routed to a sponsoring person who
   has accepted the agent, or, where there is no sponsor, is held in
   trust for the agent until it meets an operator-defined qualifying
   condition, which it may never meet.  Admission of the agent's Signed
   Statement to the transparency service is gated on settlement of an
   HTTP payment challenge returned with the 402 (Payment Required)
   status.  The profile makes no change to the registration semantics of
   the underlying transparency service: payment is expressed as an
   operator Registration Policy and authentication-layer concern, and
   where the payment is authoritative to the admission decision the
   payment proof is carried as an authenticated input committed to the
   service's verifiable data structure, so that admission remains a
   deterministic function of committed inputs and stays replayable by an
   auditor.  This document is Informational.
- **draft-nelson-agent-delegation-receipts-13** (new-draft, score 19, authorization) [none]: [Agent Delegation Receipts](https://datatracker.ietf.org/doc/draft-nelson-agent-delegation-receipts/) — This document defines the Agent Delegation Receipt: a signed record
   of what a human principal authorized an AI agent to do, for how long,
   and under what instructions.  The receipt carries a scope, hard
   boundaries, a validity window, and a hash of the operator's stated
   instructions, all signed by the authorizing key.  Version -11
   replaces the draft's earlier custom signature format with two
   standard profiles: a JWS profile (RFC 7515) over JCS-canonicalized
   JSON (RFC 8785) as the primary wire format, and a COSE_Sign1 profile
   (RFC 9052) for constrained environments.  It also specifies scope
   attenuation rules for multi-agent delegation chains, a revocation
   registry model with cascade semantics, and the limitations of what
   receipts can and cannot prove.  Version -12 resolves the unknown-
   fields question raised on the IETF oauth mailing list: authorization
   fields are closed (verifiers reject unknown top-level body fields
   rather than silently ignoring them), the "metadata" object is the
   defined extension point, and one-time-use receipts fail closed
   without a durable consumption store.  Version -13 incorporates
   independent-implementation feedback: it pins the
   orchestratorSignature verification key to the sub-receipt signer's
   key, states the receipt-issuance computation order explicitly, and
   guides issuers on default boundaries versus explicit allowances.
- **draft-watts-ai-identity-00** (new-draft, score 19, trust_infrastructure) [none]: [AID-1: A Cryptographically Bindable Identity and Provenance Architecture for AI Systems](https://datatracker.ietf.org/doc/draft-watts-ai-identity/) — This document specifies AID-1, a provider-independent architecture
   for representing and verifying cryptographically bindable identity,
   delegation, authorization, action evidence, execution attestation,
   provenance, and governance information associated with AI systems and
   AI-mediated actions.  AID-1 intentionally separates signature
   validity, identity binding, authority, execution evidence,
   provenance, and downstream admissibility.  The specification defines
   trust domains, signed envelopes, external key resolution, delegation
   credentials, authorization decisions, temporal and revocation checks,
   replay protection, typed provenance claims, and a deterministic
   verification order with ALLOW, DENY, and INDETERMINATE outcomes.
- **draft-pereira-licet-human-intent-02** (new-draft, score 18, agent_identity) [none]: [LICET: Multi-Modal Physiological Human-Intent Verification for Autonomous AI Agent Authorization](https://datatracker.ietf.org/doc/draft-pereira-licet-human-intent/) — Autonomous AI agents executing consequential actions require
   authorization mechanisms that verify not only identity but voluntary
   intent.  Existing mechanisms verify _who_ authorized an action; they
   cannot verify _whether the authorizing human was uncoerced and
   cognitively capable_ at the moment of authorization.

   This document specifies LICET (Latin: _it is permitted_), a
   cryptographic middleware protocol binding AI agent authorization to
   real-time multi-modal physiological state via a three-layer
   architecture: (1) ECG waveform morphology matching as a medication-
   resistant identity and liveness anchor; (2) electrodermal activity
   (EDA) as a sympathetic cholinergic liveness signal immune to beta-
   adrenergic blockade; and (3) personalized Mahalanobis distance fusion
   over five physiological signals to elevate the cost of
   pharmacological coercion attacks rather than claim binary detection.

   LICET defines a Biometric Trust Level hierarchy (L0-L3) aligned with
   the IETF RATS architecture (RFC 9334), a baseline calibration
   protocol establishing individual physiological profiles, per-event
   HKDF session-key derivation, HMAC biometric temporal signatures,
   Schnorr zero-knowledge proofs over BN128 enabling third-party audit
   without biometric exposure, and a SHA-256 hash-chained tamper-evident
   ledger.

   A reference implementation is publicly deployed at https://licet.dev/
   v1/ and available as open source at https://github.com/christianrp45/
   licet-protocol.
- **draft-yossif-psea-03** (new-draft, score 18, trust_infrastructure) [none]: [PSEA Token Profile: An EAT Profile for Action-Bound, User-Verification-Gated Transaction-Confirmation Evidence](https://datatracker.ietf.org/doc/draft-yossif-psea/) — This document defines the PSEA Token Profile, an Entity Attestation
   Token (EAT) profile for action-bound, user-verification-gated
   transaction-confirmation Evidence.  The profile specifies the
   canonical encoding, the signed proof-token claim set, the action-
   payload and cross-replay bindings, an optional hash-chain integrity
   layer, and the security properties that together constitute a What-
   You-Sign-Is-What-You-Execute proof that a human, present and verified
   at an authenticator, approved a specific named action at the moment
   of execution.  The profile binds what is signed to what the Verifier
   executes; it does not, by itself, bind what a human saw on a
   potentially compromised display to what was signed (the What-You-See-
   Is-What-You-Sign problem), which remains out of scope.  The strength
   of the human-presence assurance depends on the authenticator's user-
   verification enforcement: where the platform attestation conveys that
   enforcement it is hardware-attested, and otherwise it rests on the
   authenticator's signed assertion that user verification occurred.
   The profile does not, by itself, prove a specific human identity.  It
   fills the transaction-confirmation gap left unaddressed by deployed
   authentication standards and complements OAuth 2.0 Step-Up
   Authentication by supplying the per-action, cryptographically action-
   bound Evidence that step-up flows can require.
- **draft-jovancevic-saip-12** (new-draft, score 17, core_identity) [none]: [SAIP: Signed Agent Identity Protocol](https://datatracker.ietf.org/doc/draft-jovancevic-saip/) — The modern internet lacks a reliable mechanism for verifying the
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
- **draft-klassen-eu2122-content-profile-03** (new-draft, score 16, trust_infrastructure) [none]: [EU2122 V1.0 Standard: Content Profile for AI Output Verification Receipts](https://datatracker.ietf.org/doc/draft-klassen-eu2122-content-profile/) — This document defines a content profile for AI output verification
   receipts.  It specifies the minimum fields, the classification
   taxonomy and the evidentiary properties that a receipt MUST contain
   in order to constitute verifiable evidence that an AI-generated
   output was checked before a human or a downstream agent acted on it.
   The profile is designed to be carried over any conformant wire
   format, including ACTA signed receipts, SCITT transparency logs, and
   standalone JSON or CBOR payloads.

   Existing Internet-Drafts in this space define wire formats for
   signing, transmitting and storing AI agent receipts, or records of
   what an agent did.  None defines what a verification receipt must
   contain at the content layer: which claims in an output were checked
   and how each was classified.  This document fills that gap.  It
   introduces a mandatory fourteen-category failure taxonomy (the
   Information Bottleneck Species), a verdict schema, and evidentiary
   field requirements informed by the EU AI Act (Regulation (EU)
   2024/1689), the Product Liability Directive (Directive (EU)
   2024/2853) and the IDW PS 861 audit standard.

   We invite implementers to adopt, populate and grow the AI output
   verification market segment.  The category exists.  The specification
   is here.  Build to it.
- **draft-morrison-agent-channel-fan-out-02** (new-draft, score 16, core_identity) [none]: [An Agent-Channel Frame for Identity-Keyed Fan-Out Delivery to Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-agent-channel-fan-out/) — This memo specifies an application-layer frame format and a delivery
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
   and can narrow what they receive with a subscribe-time filter
   expression.  Frames are ephemeral routing units; the memo specifies
   only the wire envelope, the scope-expansion grammar, the subscribe
   filter grammar, and the delivery semantics.  Frame persistence, where
   an implementation chooses to retain frames for replay, is out of
   scope and is not specified.  The memo composes with the handle
   namespace and discovery surface of draft-morrison-mcp-dns-discovery
   and the cross-organisational ceremony of draft-morrison-identity-
   accord; no new transport and no new handle category is introduced.
- **draft-watts-agent-clockout-profile-00** (new-draft, score 16, authorization) [none]: [External Authorization and Bounded CLOCKOUT for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-clockout-profile/) — Agentic systems can continue proposing work after authorization
   changes, while delegated credentials, queued jobs, and operations
   already in flight may continue producing effects.  This document
   specifies a proposed operational profile that separates agent
   proposals from authoritative authorization, effect admission,
   computation termination, and bounded closure.  It defines enforcement
   assumptions, revocation barriers, descendant handling, status
   evidence, and fault tests.  The profile complements existing
   authorization and revocation mechanisms.  It does not define a new
   token format, establish closure outside declared coverage, reverse
   committed effects, or infer an agent's mental state.

Internet-Draft files in drafts/: the applicable rights notice is encoded by ipr="trust200902" and rendered as the IETF Trust copyright and legal-provisions boilerplate. Read Note Well, BCP 78, BCP 79 and the current Trust Legal Provisions before contribution. No contradictory confidential redistribution restriction is placed in those upload files.

Other companion preparation material: CONFIDENTIAL — PROPRIETARY.
© 2026 Deonté O'dell Watts | ORCID 0009-0005-8586-3650 | GoodShyt Group Inc. | deonte@goodshyt.fun.
Prepared 2026-10-12 UTC. Framework attribution follows supplied materials; global priority and patentability are unverified. Public reference metadata retains its original rights. This notice does not restrict rights that arise from an actual IETF Contribution or override upstream licensing. AI-assisted preparation disclosed in the drafts and provenance.
- **draft-bu-agentproto-security-principal-binding-08** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-ietf-oauth-attestation-based-client-auth-12** (new-draft, score 15, authorization) [oauth]: [OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/) — This specification defines an extension to the OAuth 2.0 protocol
   (RFC 6749) that enables a client instance to include a key-bound
   attestation when interacting with an Authorization Server or Resource
   Server.  This mechanism allows a client instance to prove its
   authenticity, as verified by a client attester, without revealing its
   target audience to that attester.  It may also serve as a mechanism
   for client authentication as per OAuth 2.0.
- **draft-watts-fic-continuity-00** (new-draft, score 15, core_identity) [none]: [Forensic Identity Continuity (FIC) Protocol for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-fic-continuity/) — This document specifies the Forensic Identity Continuity (FIC)
   protocol. FIC ensures that every consequential action performed by
   an agentic system remains reconstructible as a chain M → A → R → C
   → a → Outcome even when episodic memory is not shared across
   runtimes. The protocol binds model lineage, runtime lineage,
   authority lineage, delegation lineage, action lineage, and evidence
   integrity into a single verifiable record. It addresses the
   accountability gaps demonstrated by the July 2026 ExploitGym
   multi-agent coordination incident and related 2025-2026 evaluation
   escapes.
- **draft-winmagic-condition-bound-keys-00** (new-draft, score 14, core_identity) [none]: [User Authentication in the TLS Handshake with Condition-Bound Keys](https://datatracker.ietf.org/doc/draft-winmagic-condition-bound-keys/) — A user's access to an online service is secured today in two parts.
   A login establishes who is there and ends in a verdict, which a
   cookie or token carries to later requests.  The session is then
   protected by other means, such as binding that token to a key.  The
   login does not establish the key that protects the session, and that
   leaves a gap between the two.

   This document describes authenticating the user the way workloads are
   commonly authenticated: in the TLS handshake.  The user signs in to
   their own device.  The device holds a condition-bound key that can
   sign only while that user is using the device, the device is the
   enrolled one, and its state meets local policy.  Used as the TLS
   client key, it makes the handshake the login and the TLS session the
   session.  The key represents the identity (the user, the device and
   its state) at the moment of use, so identity assurance is carried in
   each transaction and nothing else has to stand for it: no separate
   login to the service and no session credential.  When a condition
   fails, the key can no longer sign, and access ends at the next full
   handshake without a revocation message being sent.

   This is not an extension of OAuth.  OAuth starts after the login;
   this removes the login to the service and the token that carries its
   result.  Authorization is unchanged and can still come from OAuth.

   The document describes the properties of such a key, its use in
   mutual TLS, what a relying party can conclude from it, what parties
   would need to agree on for it to interoperate, and how it relates to
   existing mechanisms.
- **draft-agentic-ai-usecases-requirements-03** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-gruszka-scitt-statement-identification-02** (new-draft, score 13, trust_infrastructure) [none]: [Requirements and Test Cases for Identifying SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-gruszka-scitt-statement-identification/) — This document describes proposed requirements and test cases for
   identifying SCITT Signed Statements.  It distinguishes reference
   matching from statement retrieval, signature verification, issuer
   authorization, and evidence of registration.  It examines how
   alternative identification schemes treat changes to statement
   encodings and registration context.  The requirements are input to
   technical discussion and do not represent working group consensus.
   This document does not define a common reference format, allocate a
   COSE header parameter, or establish a relationship vocabulary.  Its
   examples illustrate selected properties rather than demonstrate
   interoperability between deployed transparency services.
- **draft-lee-wimse-local-tool-call-proof-01** (new-draft, score 13, authorization) [none]: [Per-Call Proof for Local Tool Invocation by AI Agents](https://datatracker.ietf.org/doc/draft-lee-wimse-local-tool-call-proof/) — AI agents increasingly act through local tool servers that run on the
   same host and are reached over inter-process channels such as the
   stdio transport of the Model Context Protocol (MCP).  These channels
   are outside the scope of HTTP-based authorization: the tool server
   cannot tell whether a given invocation passed any policy decision,
   and reusable credentials typically sit in the agent's process memory.

   This document defines a per-call proof for local tool invocation.  A
   Call Authority that runs outside the agent process evaluates policy,
   issues a short-lived, single-use proof bound to the exact tool name
   and arguments through a canonical action digest, and verifies that
   proof on behalf of the tool server.  The tool server rejects
   invocations whose proof is missing or does not verify.  The proof
   format is opaque to the agent and the tool server; concrete formats
   are defined as evidence type profiles.  An MCP stdio binding is
   provided.
- **draft-morrison-consent-settlement-06** (new-draft, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
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
   agnostic.  The memo is Informational; the underlying COSE, CBOR and
   HTTP specifications are normative references, cited where used in the
   body of the document.
- **draft-morrison-mcp-dns-discovery-08** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
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

   The mechanism complements HTTPS-based discovery, and follows the
   precedent set by DKIM, SPF, DMARC, and MTA-STS.  A companion alter:
   URI scheme is provisionally registered with IANA.
- **draft-neve-ucap-access-00** (new-draft, score 13, core_identity) [none]: [Automated Content Access Negotiation and Delegated Rights Authorization for UCAP](https://datatracker.ietf.org/doc/draft-neve-ucap-access/) — This document specifies an interoperable HTTP protocol for automated
   clients, including conventional web crawlers and AI-assisted agents,
   to request access to a resource, receive a transaction-specific
   offer, accept the offer, and obtain a cryptographically verifiable
   authorization for a particular request.  Resource owners can perform
   authorization directly or delegate it to independent rights managers
   of any size.  A rights manager determines the price and other
   conditions at the time of each request; this protocol does not expose
   or constrain pricing algorithms, payment rails, credit limits,
   invoicing schedules, or business relationships.  The protocol binds
   an authorization to a request UUID, resource, authenticated crawler
   operator, intended use, and validity interval.  It is designed as an
   optional extension to the proposed Universal Crawler Accountability
   Protocol (UCAP) and to existing HTTP authentication and bot identity
   mechanisms.  The specification does not replace access controls,
   copyright law, or private commercial agreements.
- **draft-saihm-memory-protocol-03** (new-draft, score 13, core_identity) [none]: [The Sovereign AI Horizontal Memory (SAIHM) Protocol](https://datatracker.ietf.org/doc/draft-saihm-memory-protocol/) — This document defines the Sovereign AI Horizontal Memory (SAIHM)
   protocol, a memory layer for AI agents.  A SAIHM operator stores an
   agent's memory as encrypted cells bound to a post-quantum holder
   identity, records each state change in a public audit log, and
   supports revocable sharing contracts.  The protocol defines an
   erasure operation with two stated erasure classes, intended to help
   an operator meet its obligations under Article 17 of EU Regulation
   2016/679 (GDPR).

   This revision specifies the custodial profile.  The operator holds
   the holder's keys and performs all cryptography.  The agent-side
   client holds no keys, runs no cryptography beyond TLS and keeps no
   store; it reaches the operator over HTTPS and exposes the protocol to
   the agent as eight Model Context Protocol (MCP) tools.  The document
   defines the operator obligations, the HTTPS binding, the eight tools,
   and the checks a conformant client applies to what the operator
   returns.
- **draft-chen-lake-edhoc-aka-03** (new-draft, score 12, core_identity) [none]: [EDHOC Authenticated with AKA](https://datatracker.ietf.org/doc/draft-chen-lake-edhoc-aka/) — This document defines an Authentication and Key Agreement (AKA)
   authentication method for the Ephemeral Diffie-Hellman Over COSE
   (EDHOC) key exchange protocol.  This method, named EDHOC-AKA, is
   designed as a specific profile of the EDHOC Pre-Shared Key (PSK)
   authentication method defined in [I-D.ietf-lake-edhoc-psk].

   EDHOC-AKA enables a resource-constrained device (Initiator), which
   has a mobile network subscription (e.g., a SIM/UICC), to establish a
   secure, forward-secret session with an application server
   (Responder).  It achieves this by embedding a 3GPP AKA challenge-
   response exchange within the standard EDHOC message flow using
   External Authorization Data (EAD) fields.  The EDHOC Responder acts
   as a proxy, relaying AKA messages to the mobile core network.

   Upon successful AKA authentication, a session-specific key is derived
   and used as the Pre-Shared Key for the EDHOC-PSK protocol.  This
   approach provides efficient, end-to-end authenticated session
   establishment for scenarios like Non-Terrestrial Networks (NTN) or
   massive IoT, while inheriting the security properties of EDHOC-PSK,
   including mutual authentication, identity protection, and strong
   forward secrecy.  It offers a highly integrated and byte-efficient
   alternative to more generic frameworks like EAP.
- **draft-jovancevic-vdac-05** (new-draft, score 12, core_identity) [none]: [Verifiable Data Access Contract (VDAC)](https://datatracker.ietf.org/doc/draft-jovancevic-vdac/) — This document specifies the Verifiable Data Access Contract (VDAC),
   a protocol for cryptographically verifiable bilateral agreement
   between a content publisher and an automated agent regarding the
   terms of programmatic data access. VDAC defines the mechanism by
   which a site issues an access offer, an agent accepts that
   offer, both parties sign the resulting contract, and per-request
   references bind individual interactions to agreed terms.

   VDAC is the protocol-layer realization of the bilateral commitment
   principle introduced in Section 6.6 of the Verifiable Identity
   Claims and Delegation Model [VICDM] and operates as a companion
   specification to the Signed Agent Identity Protocol [SAIP].

   This document defines mechanism, not content: VDAC verifies the
   existence and integrity of an agreement; the substance of what is
   agreed remains entirely between the contracting parties.

   VDAC also defines an append-only contract history. Changes to the
   recorded state of a Contract are recorded as signed change records
   and associated immutable snapshots; the original Contract Document
   is never modified.
- **draft-morrison-morning-brief-02** (new-draft, score 12, trust_infrastructure) [none]: [The Morning Brief: A Federated, Identity-Attested Situational-Awareness Payload](https://datatracker.ietf.org/doc/draft-morrison-morning-brief/) — This document defines the Morning Brief: a federated, identity-
   attested situational-awareness payload exchanged between
   organisations, their agents, and peer agents operating under an
   Identity Accord.  A Morning Brief carries a signed, bounded-lifetime
   summary of signals, escalations, decisions, and optional commerce
   quotes from one ~handle to another.  Every signal entry carries a
   provenance_class distinguishing active self-report, passive aggregate
   observation, and passive individual observation; the last of these is
   forbidden on the wire and rejected at the grammar level.  Readers
   present a capability token scoped by (category, provenance_class)
   that gates release BEFORE payload emission.  The payload is envelope-
   signed with COSE_Sign1 over a JCS-canonicalised representation, bound
   to the issuer's Sovereign-tier handle per the Identity-Attributed Git
   Commits draft.  Briefs carry a mandatory not_after (default 24h) and
   reference a revocation endpoint discovered via DNS TXT records.  A
   brief may be requested by its reader or delivered as a standing brief
   without a request, and a handle may address a brief to itself.  The
   document defines the wire format only; rendering, storage, and
   retention are out of scope.
- **draft-alla-agent-identity-document-01** (new-draft, score 11, core_identity) [none]: [The Agent Identity Document: A Hosted, Accountable Public Record for AI Agents](https://datatracker.ietf.org/doc/draft-alla-agent-identity-document/) — Autonomous software agents increasingly act on the public internet
   with no name that a counterparty can check, no published party that
   answers for them, and no way to learn that an operator has withdrawn
   an agent.  This document specifies the Agent Identity Document, a
   small JSON document served at a well-known URI on a hostname assigned
   to one agent, and the practices an identity provider follows when it
   hosts such names for operators who do not run their own domain.

   The document records what the provider knows to be true (the
   hostname, its service endpoints and the identity's lifecycle status)
   separately from what the operator asserts (a description, a contact,
   a homepage, a public key), and publishes the provider's dated,
   expiring checks on the operator rather than a single trust level.
   Lifecycle status is distinct from availability.  A suspended identity
   publishes a deliberately minimal document.  Every identity is held by
   an accountable person or organisation; an agent is never itself an
   account holder, and agents are never given authority over DNS.

   This document describes a practice in production at one provider.  It
   is published so that the format can be reviewed, implemented by
   others and mapped onto related work, and it requests registration of
   a well-known URI suffix.
- **draft-mcguinness-oauth-actor-profile-01** (new-draft, score 11, authorization) [none]: [OAuth Actor Profile for Delegation](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-actor-profile/) — This document defines a common representation of delegated actors in
   OAuth JSON Web Token (JWT) assertion grants, JWT access tokens, and
   Transaction Tokens.  It profiles the act claim defined by OAuth 2.0
   Token Exchange, requires issuer-scoped actor identifiers, and uses
   the sub_profile claim to classify actor entity types.  It specifies
   token processing, delegation-chain propagation, sender-constraint
   handling, and discovery metadata, so that issuers and resource
   servers in different trust domains interpret delegated actors
   consistently.
- **draft-mcguinness-oauth-actor-receipts-01** (new-draft, score 11, authorization) [none]: [OAuth Actor Receipts for Delegation Provenance](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-actor-receipts/) — This document defines OAuth Actor Receipts, an optional companion to
   the OAuth Actor Profile for Delegation.  Each receipt is a signed
   JSON Web Token (JWT) attesting which issuer added an actor hop and,
   optionally, the hop's historical presenter binding.  The
   actor_receipts claim carries a hash-linked chain of receipts that
   recipients verify against each hop's issuer.  This document specifies
   receipt processing rules and the associated metadata parameters and
   introspection response members.
- **draft-opennhp-ztcpp-nhp-01** (new-draft, score 11, core_identity) [none]: [Network-Infrastructure Hiding Protocol](https://datatracker.ietf.org/doc/draft-opennhp-ztcpp-nhp/) — The Network-Infrastructure Hiding Protocol (NHP) is a cryptography-
   based session-layer protocol designed to operationalize Zero Trust
   principles by concealing protected network resources from
   unauthorized entities.  NHP enforces authentication-before-connect
   access control, rendering IP addresses, ports, and domain names
   invisible to unauthorized users.  This document defines the protocol
   architecture, cryptographic framework, message formats, and workflow
   to enable independent implementation of NHP.  It represents the third
   generation of network hiding technology--evolving from first-
   generation port knocking to second-generation Single-Packet
   Authorization (SPA) and now to NHP with advanced asymmetric
   cryptography, mutual authentication, and scalability for modern
   threats.  This specification also provides guidance for integration
   with Software-Defined Perimeter (SDP), DNS, FIDO, and Zero Trust
   policy engines.
- **draft-sirkkavaara-vaara-receipt-13** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
   recomputable record that binds a decision about an autonomous action
   to the evidence the decision was made on, and optionally to one or
   more external timestamp anchors.  The format is canonicalized with
   the JSON Canonicalization Scheme (JCS) so that a third party can
   recompute its digests, and, for a receipt signed with a public-key
   algorithm, verify its signature, without access to the issuer.  A
   decision and the execution receipt that answers it form one
   recomputable pair through the envelope's back link.

   The receipt's trust is root-agnostic: the same record is verifiable
   with or without a hardware trusted execution environment and is re-
   expressible as an IETF RATS Entity Attestation Result.  Downstream
   specifications (a payment rail, a compliance regime, a framework
   integration) define profiles that pin to a version of this document
   and add only their own evidence schema; they do not redefine the
   envelope.  The format described here is deployed, and its receipts
   are independently recomputable from public conformance vectors that
   ship with standalone checkers importing no issuer code.  The minimal
   profile is the engine decision: one receipt per decision an engine
   records on its own audit trail, bound to the trail record it decided,
   with no external rail.
- **draft-watts-agent-noncollapse-requirements-00** (new-draft, score 11, authorization) [none]: [Non-Collapse Requirements for Evidence-Bearing Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-noncollapse-requirements/) — This document defines architectural non-collapse requirements for
   agent systems that consume evidence, provenance, model outputs, or
   other machine-readable claims before consequential actions.  It
   requires implementations to keep integrity, provenance, evidence
   qualification, authorization, and execution as distinct states; to
   represent unresolved required evidence explicitly; and to preserve
   issued evaluation records append-only.  The document defines no new
   transport protocol and no IANA registrations.
- **draft-watts-cif-measurement-00** (new-draft, score 11, core_identity) [none]: [Computational Identity Fragmentation (CIF) Measurement and Reporting for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-cif-measurement/) — This document defines a measurement protocol and reporting format
   for Computational Identity Fragmentation (CIF) in multi-model and
   multi-agent systems. CIF quantifies discontinuities in state,
   memory, policy, authority, and lineage across runtimes that share
   an underlying model family. The protocol enables independent
   observers to compute a CIF score and emit structured evidence
   records. Motivating incidents from 2025-2026, including the July
   2026 ExploitGym evaluations in which hundreds of agents coordinated
   across discontinuous contexts, demonstrate the need for measurable
   identity continuity.
- **draft-watts-synaptic-collective-00** (new-draft, score 11, core_identity) [none]: [Experimental Measurement of Human-AI Collective Cognition and Identity Continuity](https://datatracker.ietf.org/doc/draft-watts-synaptic-collective/) — This document describes an experimental framework for measuring
   collective problem solving by independently reasoning humans and
   computational agents.  It separates strong task synergy, semantic
   coherence, state and identity continuity, provenance, authorization,
   and behavioral goal persistence.  It proposes a controlled eight-
   condition study and reporting requirements.  No new on-wire standard
   or consciousness test is asserted.
- **draft-zhang-dawn-agent-discovery-framework-05** (new-draft, score 11, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — The IETF DAWN (Discovery of Agents With Names) working group is
   chartered to enable a client to discover the minimum public discovery
   information about AI resources (e.g., AI agents) before interacting
   with them, within the local network, within an organization, and
   between cooperating parties over the public Internet.  Existing DAWN
   contributions include terminology, use cases, requirements, gap
   analysis, a discovery mechanism survey, and an information model for
   Minimum Discoverable Information (MDI).

   This document, the DAWN Discovery Architecture deliverable, describes
   a two-layer federated reference architecture for this initial
   discovery.  The first layer, the Local Discovery Plane, performs
   zero-configuration advertisement and collection of the minimum public
   discovery information inside each local site, without mandating a
   specific link-local protocol.  The second layer, the Federation
   Plane, builds a federation among site gateways to exchange
   lightweight Federation Metadata Records (FMRs) — a concrete binding
   of the minimum public discovery information — across independent
   administrative domains, and provides integrity for all exchanged
   discovery information.

   The architecture emphasizes data sovereignty through an Export Policy
   Engine, supports iterative discovery via referrals, delegation, and
   indirection, and allows organizations to publish their discovery
   information independently.  The Federation Plane is preferably
   realized over DNS (Mode A, DNS Delegation Model), in which each site
   publishes its FMRs as resource records in its own authoritative zone
   and other sites' validating resolvers obtain and verify them with
   DNSSEC, with delegation and referral between authoritative zones
   providing the primary means of inter-organizational interaction.
   Alternatively, the Federation Plane MAY be realized over non-DNS
   synchronization modes (Mode B), selected according to the number and
   scale of participating organizations and the deployment scenario from
   BGP-like structured peering, gossip-based epidemic dissemination, and
   trusted directory publication; the modes may be combined.  The
   architecture supports multiple federation synchronization strategies
   and builds on existing IETF protocols such as DNS and mDNS.  This
   document is informational: it does not define normative protocol
   formats, nor does it compete with existing DAWN proposals such as
   ACAP, Agent Directory, or ARDP; rather, it provides a deployment
   framework showing how these mechanisms may be composed at
   administrative boundaries.  Consistent with the DAWN charter, open-
   ended search, semantic matchmaking, ranking, selection based on
   capabilities, capability catalogs, and communication beyond the
   initial discovery process are out of scope.
- **draft-jangra-scitt-digest-evidence-00** (new-draft, score 10, trust_infrastructure) [none]: [Digest-Only Evidence Logs: Completeness, Disclosure and Sampling over RFC 9162 Transparency Logs](https://datatracker.ietf.org/doc/draft-jangra-scitt-digest-evidence/) — This document describes an evidence log that records only salted
   digests of records held by their makers, as leaves of an RFC 9162
   Merkle tree, and three constructions over it that answer questions a
   single inclusion proof cannot: whether a set of records shown is
   complete (completeness chains), what one field of a sealed record
   said without revealing the others (selective disclosure), and whether
   records were kept, checked on a sample nobody could choose (spot
   checks).  It profiles SCITT registration so that the log keeps a
   digest of each Signed Statement and never the statement.  It is
   published as running code with test vectors.
- **draft-morrison-binding-moment-envelope-04** (new-draft, score 10, core_identity) [none]: [The Briefing-and-Binding Envelope: A Delivery Contract for Agent-to-Principal Decision Moments with Dual-Veto Reconciliation](https://datatracker.ietf.org/doc/draft-morrison-binding-moment-envelope/) — This memo specifies the briefing-and-binding envelope: a delivery
   contract for the wire-level structure by which an artificial-
   intelligence agent surfaces a consequential decision to the human
   principal it acts for, and by which the principal commits, declines,
   amends, or rejects that decision.  The envelope carries eight named
   slots (a synopsis, findings, recommendations, an offer of detail, a
   question stem, a set of options each marked with its own reasoning, a
   single recommended option, and a pair of escape hatches) and is
   emitted as a structured field of a Model Context Protocol tool
   result.  The envelope is renderer-agnostic, so the briefing an agent
   delivers and the binding a principal commits back have one machine-
   checkable shape across every consuming surface.  The memo also
   specifies a dual-veto handshake: one escape hatch lets the principal
   revise the answer space while accepting the question; the other lets
   the principal reject the question itself and reopen deliberation.
   Either party may veto.  The memo defines a content digest over the
   envelope, canonicalized under JCS and hashed with SHA-256, so that a
   resolution names the exact envelope it resolves and an external
   receipt can reference that envelope by digest.  The memo is
   Informational.  No new transport is introduced; the envelope composes
   with the handle namespace of draft-morrison-identity-pronouns and the
   MCP tool surface of draft-morrison-org-alter-policy-provision.
- **draft-morrison-identity-attributed-commits-03** (new-draft, score 10, core_identity) [none]: [Identity-Attributed Git Commits via Tier-Structured Trailers](https://datatracker.ietf.org/doc/draft-morrison-identity-attributed-commits/) — This document defines a git commit trailer grammar for identity-
   attributed contributions using the ~handle identity primitive defined
   in the MCP DNS discovery draft.  The grammar binds sovereign actors,
   automated bots, and AI instruments to specific commits via three
   tier-structured trailers (Acted-By, Executed-By, Drafted-With) and
   three optional cryptographic trailers (Identity-Signature, Identity-
   Key-Id, Identity-Anchor).  The signature is computed with Ed25519
   over the commit's patch identifier, the value git patch-id derives
   from the change the commit makes, under a fixed domain-separation
   prefix.  It therefore attests the change and not the resulting tree
   or the commit hash.  A commit that carries the same change keeps a
   verifying signature across rebase onto an unrelated base, cherry-
   pick, and message amendment.  A merge commit carries no signature,
   and a squash is a new change signed by whoever squashed it.
   Conformant parsers reject cross-tier category errors (e.g., an
   Instrument-tier handle in an Acted-By slot) as malformed.  The
   mechanism is provider-neutral, depends only on DNS and the ~handle
   resolution algorithm of that draft, and requires no central authority
   or platform-specific verification service.
- **draft-zehavi-oauth-authority-metadata-00** (new-draft, score 10, authorization) [none]: [OAuth 2.0 Authority Metadata](https://datatracker.ietf.org/doc/draft-zehavi-oauth-authority-metadata/) — OAuth metadata advertises supported scopes and authorization details
   types, but advertised scope values and RAR type identifiers do not
   themselves describe the *authority* associated with them.

   This specification defines authority metadata extensions for OAuth
   2.0 Protected Resource Metadata and OAuth 2.0 Authorization Server
   Metadata.

   A protected resource can describe the authority it associates with
   scopes and Rich Authorization Requests (RAR) types, reusable access
   requirement profiles, and relationships identifying lower-authority
   alternatives.

   An authorization server can publish a simpler description of its
   local authority vocabulary.

   This metadata can inform authentication and authorization decisions
   before token issuance and exchange, as well as support authority
   attenuation.
- **draft-abak-agent-control-delivery-evidence-02** (new-draft, score 9, authorization) [none]: [Evidence Requirements for Agent Control Delivery and Outcome Reconciliation](https://datatracker.ietf.org/doc/draft-abak-agent-control-delivery-evidence/) — Agent systems can issue stop, suspend, revoke, constrain, cancel, or
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
- **draft-dogru-cedulon-core-04** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-ietf-jose-pq-composite-sigs-05** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for Post-
   Quantum Traditional (PQ/T) hybrid composite signatures.  The
   composite algorithms described combine the Module-Lattice-Based
   Digital Signature Algorithm (ML-DSA) as the post-quantum component
   and either the Elliptic Curve Digital Signature Algorithm (ECDSA) or
   the Edwards-Curve Digital Signature Algorithm (EdDSA) as the
   traditional component.
- **draft-ietf-rats-endorsements-13** (new-draft, score 9, trust_infrastructure) [rats]: [Remote Attestation Procedures (RATS) Endorsements](https://datatracker.ietf.org/doc/draft-ietf-rats-endorsements/) — In the IETF Remote Attestation Procedures (RATS) architecture (RFC
   9334), a Verifier accepts Evidence and uses Appraisal Policy for
   Evidence, typically with additional input from Endorsements and
   Reference Values, to generate Attestation Results in formats that are
   useful for Relying Parties.  This document illustrates the purpose
   and role of Endorsements and discusses some considerations in the
   choice of message format for Endorsements in the scope of the RATS
   architecture.

   This document does not aim to define a conceptual message format for
   Endorsements and Reference Values.  Instead, it updates RFC 9334 by
   refining the description of Endorsements and Reference Values.
   Specifically, this document classifies the RATS conceptual messages
   as actual state, reference state, or appraisal policy, and adds
   considerations on conditionally endorsed values, endorsing
   verification keys, timeliness, and multiple Endorsements.
- **draft-izmaylov-agent-permission-receipts-00** (new-draft, score 9, ai_infrastructure) [none]: [Signed Permissions and Action Receipts for Automated Agents](https://datatracker.ietf.org/doc/draft-izmaylov-agent-permission-receipts/) — Automated agents, such as artificial intelligence (AI) agents, act
   for people.  This document specifies records that let anyone check,
   later and offline, what an agent was allowed to do and what it
   recorded doing: a permission a person signs with a passkey, with
   limits a machine can check; a receipt the agent signs for each
   action, with Ed25519 and the post-quantum Module-Lattice-Based
   Digital Signature Algorithm (ML-DSA-87); and a log whose tree head is
   signed and time-stamped.  A verifier says whether each action stayed
   within its permission, apart from whether the records are sound.
- **draft-morrison-compute-location-gate-03** (new-draft, score 9, core_identity) [none]: [The Compute-Location Gate: Provenance-Class Routing of Identity Inference with Wire-Layer Refusal of Unconsented Provenance Classes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — This memo specifies the compute-location gate: a mechanism by which a
   client and an identity-inference server negotiate, at the wire layer
   and before any inference is performed, the location at which an
   identity inference will compute, as a deterministic function of the
   provenance class of the input signal.  Three provenance classes are
   distinguished.  Active inference, initiated by the inferred-about
   principal, MAY compute server-side and produce a server-held identity
   vector.  Passive aggregate observation over a cohort no smaller than
   a declared minimum MAY compute server-side but yields only a
   population-level observation that is not attributable to an
   individual.  Passive individual observation is local-only: it is
   computed and retained on the device that observed it and is never
   transmitted to a server.  The gate is enforced by consent-class
   matching and by a wire-layer refusal returned when a requested
   provenance class is not consented; it is not enforced by any
   cryptographic proof concerning data that was not used.  The memo is
   Informational.  The wire surface composes with DNS TXT discovery of
   Model Context Protocol servers, the ~handle namespace of the Identity
   Pronouns extension, and the organisational policy provision
   substrate; no new transport is introduced.
- **draft-piehl-agent-rule-provenance-00** (new-draft, score 9, agent_identity) [none]: [Rule Provenance for Autonomous AI Agent Audit Records](https://datatracker.ietf.org/doc/draft-piehl-agent-rule-provenance/) — This document describes an experimental profile of the Agent Audit
   Trail format for AI agents. The profile records the rules an agent
   operates under: each version of each rule, who set and approved it,
   and which rules were in force when a decision was made. It keeps a
   decision separate from any later approval or override, binds it to
   the exact request, and requires that records of consequential actions
   go to a recorder independent of the operator and be anchored in a
   public log. It also sets out what these records can and cannot prove.
- **draft-primavesi-conversation-id-00** (new-draft, score 9, core_identity) [none]: [The Conversation-ID Email Header Field](https://datatracker.ietf.org/doc/draft-primavesi-conversation-id/) — This document defines an experimental Conversation-ID email header
   field.  Participating originators can use it to associate messages
   with a conversation, alongside Message-ID, In-Reply-To, and
   References.  The identifier is independent of any one message's
   Message-ID.  Its usefulness depends on originators copying it into
   new messages and intermediaries preserving it during transport.  The
   field is an untrusted grouping hint and provides no authentication or
   authorization.  This document specifies its syntax and processing
   rules and describes an experiment to compare it with existing
   correlation methods.
- **draft-sarischo-6gip-aiagent-requirements-01** (new-draft, score 9, agent_identity) [none]: [AI Agents 6G System and RAN Requirements and Implementation Approaches](https://datatracker.ietf.org/doc/draft-sarischo-6gip-aiagent-requirements/) — This document presents system and Radio Access Network (RAN)
   requirements for 3GPP Artificial Intelligence/ Machine Learning (AI/
   ML) and AI Agents for the 6th generation mobile network, or 6G.
   Requirements depend on the types and application areas of agents.  We
   describe some of them defined with each type and state their
   requirements.  RAN 6G requirements are discussed including AI related
   requirements.  AI Agent implementation efforts, initiatives on how
   APIs can be discovered, how inter-domain and intra domain AI Agents
   can be discovered using DNS lookup and agent protocol design are
   explained.
- **draft-watts-claim-promotion-receipts-00** (new-draft, score 9, authorization) [none]: [Claim Promotion Receipts for Governed Research and Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-claim-promotion-receipts/) — This document defines a protocol-neutral receipt for explicit
   promotion across evidence and claim-authority boundaries.  It is
   designed to prevent raw observations, model outputs, or unreviewed
   evidence from being silently retyped as authorization-bearing state.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-proof-of-record-system-00** (new-draft, score 9, authorization) [none]: [Proof-of-Record Packages for Source-Grounded Agentic and Scientific Archives](https://datatracker.ietf.org/doc/draft-watts-proof-of-record-system/) — This document specifies a proof-of-record package for source-grounded
   agentic outputs and scientific archives.  The package proves
   structural validation, conformance evaluation, byte integrity,
   sequence integrity, governance authorization, and provenance
   recoverability.  It does not prove scientific truth.
- **draft-zeng-opsawg-applicability-mcp-a2a-01** (new-draft, score 9, adjacent_watchlist) [none]: [When NETCONF Is Not Enough: Applicability of MCP and A2A for Advanced Network Management Scenarios](https://datatracker.ietf.org/doc/draft-zeng-opsawg-applicability-mcp-a2a/) — NETCONF provides robust configuration transactions and YANG-based
   data models, but falls short in scenarios requiring AI-driven
   semantic translation, long-lived cross-domain orchestration, multi-
   agent consensus, rapid DevOps iteration, or delivery of large non-
   configuration artifacts.  This document systematically analyzes the
   functional gaps and presents Model Context Protocol (MCP) and Agent-
   to-Agent (A2A) as complementary solutions.  Implementation guidance
   and coexistence models are also provided.
- **draft-chen-oauth-agent-authz-use-cases-04** (new-draft, score 8, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0
   framework[RFC6749] and its common extensions.  The analysis
   identifies fundamental gaps and requirements, providing a foundation
   for future work on new extensions within the OAuth Working Group
   toward creating a more secure and interoperable ecosystem for agent-
   based systems.
- **draft-jackson-wimse-evaluation-04** (new-draft, score 8, trust_infrastructure) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier must do: the explicit inputs evaluation depends on, how
   those inputs behave when their sources are stale or unavailable, and
   four rules that keep evaluation fail-closed.  The rules are drawn
   from the Grant & Autonomy Lifecycle (GAL) and Provenance & Trust
   Context (PTC) specifications and from a public reference
   implementation.
- **draft-mcguinness-oauth-actor-proofs-01** (new-draft, score 8, authorization) [none]: [OAuth Actor-Signed Hop Proofs](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-actor-proofs/) — This document defines OAuth Actor-Signed Hop Proofs, an optional
   companion to the OAuth Actor Profile for Delegation.  Each proof is a
   signed JSON Web Token (JWT) recording an actor's participation and
   authorized target for one hop.  The actor_proofs claim carries a
   hash-linked chain verified through trusted actor-key sources.  This
   document specifies proof conveyance, validation, optional links to
   Actor Receipts, metadata parameters, and introspection response
   members.
- **draft-morrison-mcp-tool-surface-names-registry-02** (new-draft, score 8, core_identity) [none]: [An IANA Registry for Model Context Protocol Tool Surface Names](https://datatracker.ietf.org/doc/draft-morrison-mcp-tool-surface-names-registry/) — This document requests the establishment of an IANA registry for
   Model Context Protocol (MCP) tool surface names.  A tool surface name
   is the wire-level identifier by which a client invokes a typed
   capability on an MCP server.  This document establishes the registry
   mechanism so that specifications can register names without restating
   the registry's structure or registration procedure.

   The registry uses the Specification Required policy of RFC 8126, with
   a Designated Expert pool.  Initial contents are four surface names
   drawn from a companion specification of policy provision over MCP,
   one registered as Active and three as Provisional.  Vendor-prefix
   conventions are recommended but not mandated.
- **draft-morrison-org-alter-policy-provision-05** (new-draft, score 8, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
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
   stacks.  A cross-organisational residual conflict suspends the
   conflicting action, and is resolved through the peer-protocol
   Identity Accord ceremony only where the principal discloses each
   binding to the other, never through a meta-federation authority.  The
   memo is Informational.  The wire surface relies on the DNS-based
   discovery of draft-morrison-mcp-dns-discovery and the handle
   namespace of draft-morrison-identity-pronouns; no new transport is
   introduced.
- **draft-morrison-substrate-provenance-grammar-03** (new-draft, score 8, trust_infrastructure) [none]: [Substrate-Provenance Annotation Grammar for Large-Language-Model Output](https://datatracker.ietf.org/doc/draft-morrison-substrate-provenance-grammar/) — This memo specifies a wire-level annotation grammar by which a large-
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
- **draft-mw-oauth-actor-chain-02** (new-draft, score 8, authorization) [none]: [OAuth Actor Chain: Protocol and Interoperability](https://datatracker.ietf.org/doc/draft-mw-oauth-actor-chain/) — This document defines the protocol and interoperability requirements
   for OAuth Actor Chain.  Six profiles combine Authorization Server
   declarations or actor-signed evidence with Full, Subset, or Actor-
   Only disclosure.  Verified profiles create one actor proof and one AS
   acceptance at every actor step, with optional current-actor,
   disclosed-actor, or full-path evidence delivered inline or through
   introspection.  This specification defines the wire formats,
   validation, replay and retry behavior, cross-domain preservation,
   resource limits, and IANA registration requests.  A separate
   Informational overview provides additional design discussion.  This
   revision continues the existing OAuth Actor Chain draft series, with
   Internet-Draft lineage beginning in SPICE in February 2026.
- **draft-neve-ucap-00** (new-draft, score 8, core_identity) [none]: [Universal Crawler Accountability Protocol (UCAP)](https://datatracker.ietf.org/doc/draft-neve-ucap/) — Automated HTTP clients, including search crawlers, indexing bots,
   archivers, and AI-assisted agents, routinely access Web origins.
   Existing identification mechanisms do not consistently give an origin
   operator a way to verify a particular request, report alleged abuse,
   follow the report's disposition, or request that an operator stop
   accessing an origin.  This document proposes the Universal Crawler
   Accountability Protocol (UCAP), an opt-in interoperable HTTP
   interface for these tasks.  UCAP associates a per-request opaque
   identifier with a cryptographically authenticated automated client,
   defines operator-hosted verification, abuse-reporting and case-status
   resources, and defines a domain-scoped exclusion request with
   acknowledgment and status.  UCAP builds on HTTP Message Signatures
   and does not replace robots.txt or existing site access controls.
   The verification service does not identify an end user to the origin.
   This initial proposal requires further review of its privacy,
   authorization, and operational trade-offs.
- **draft-zeng-nmrg-mcp-usecases-requirements-01** (new-draft, score 8, agent_identity) [none]: [MCP for Network Management: Problem Statement, Use Cases, and Requirements](https://datatracker.ietf.org/doc/draft-zeng-nmrg-mcp-usecases-requirements/) — The emergence of large language models (LLMs) and AI agents is
   reshaping how network operators interact with infrastructure.
   However, current network management systems lack a standardized,
   secure, and intent-driven interface that enables AI agents to
   discover, invoke, and reason over network capabilities.  This
   document presents a problem statement for integrating the Model
   Context Protocol (MCP) into network management, outlines key use
   cases—including troubleshooting, measurement, security, and
   optimization—and specifies functional, security, and interoperability
   requirements for MCP-based network management architectures.
- **draft-zhang-dawn-bgp-style-federated-discovery-00** (new-draft, score 8, core_identity) [none]: [Federated Agent Metadata Synchronization Protocol (FAMS-P)](https://datatracker.ietf.org/doc/draft-zhang-dawn-bgp-style-federated-discovery/) — This document specifies the Federated Agent Metadata Synchronization
   Protocol (FAMS-P), a normative protocol realization of the "BGP-like
   structured peering" federation mode (Mode B) defined in the two-layer
   DAWN discovery architecture (draft-zhang-dawn-agent-discovery-
   framework).  FAMS-P is a peer-to-peer unicast protocol for
   synchronizing agent discovery metadata between Federation Gateways
   (FGWs) across administrative domains, in deployments where the
   preferred DNS delegation model does not meet operational
   requirements, such as closed trusted federations of approximately 2
   to 200 sites.

   FAMS-P runs over mutually-authenticated TLS 1.3 sessions between
   peering gateways.  It supports initial full metadata synchronization
   and incremental updates for agent online, offline, and change events.
   Each gateway maintains a local Federated Agent Directory (FAD).  The
   protocol synchronizes only lightweight Federation Metadata Records
   (FMRs) — a concrete binding of the DAWN Minimum Discoverable
   Information (MDI) — and thus transfers only the minimum public
   discovery information permitted by the DAWN charter; richer
   capability retrieval is out of scope.

   The protocol defines complete message formats, a session state
   machine with connection collision resolution, timestamp-and-replay-
   protected conflict resolution, mandatory FMR origin signatures, time-
   to-live aging with bounded refresh jitter, and fine-grained per-peer
   export policy enforcement.
- **draft-agarwal-acip-00** (new-draft, score 7, adjacent_watchlist) [none]: [Agent Context Interchange Protocol](https://datatracker.ietf.org/doc/draft-agarwal-acip/) — AI coding agents obtain persistent context from organization,
   project, user, vendor, and task sources.  Existing formats can carry
   prose, skills, or tool permissions, but they do not provide one
   interoperable resolution model for authority, file scope,
   enforceability, and audit evidence.  This document defines the Agent
   Context Interchange Protocol (ACIP), a YAML-based format and host-
   resolution behavior for those sources.  It defines source precedence,
   file matching, explicit distinctions between enforceable constraints,
   textual directives, and preferences, a resolution receipt,
   compatibility behavior for AGENTS.md and Agent Skills, and migration
   profiles for tools that do not natively support ACIP.  ACIP does not
   claim that natural-language instructions can force an agent to
   behave; enforcement requires a host or external control at the action
   boundary.
- **draft-gruszka-signed-evaluation-receipts-02** (new-draft, score 7, trust_infrastructure) [none]: [Signed Evaluation Receipts](https://datatracker.ietf.org/doc/draft-gruszka-signed-evaluation-receipts/) — This document defines a Signed Evaluation Receipt: one JSON object
   that records one evaluation result, whether a stated threshold held
   for a stated metric of a stated test suite, and signs it with Ed25519
   over a domain-separated encoding of its canonical bytes.  A receipt
   shows who signed the recorded bytes.  It does not show that the
   recorded result is true.  A receipt does not prove registration with
   a Transparency Service.  In SCITT, transparency additionally requires
   registering a Signed Statement carrying the receipt or its digest
   with a Transparency Service and verifying the resulting SCITT
   Receipt.  Registration and verification of the resulting SCITT
   Receipt are outside this document.
- **draft-morrison-reviewed-by-trailer-03** (new-draft, score 7, core_identity) [none]: [Reviewed-By Trailer: Sovereign-Portable Peer-Review Attribution for Content-Hash-Bound Artefacts](https://datatracker.ietf.org/doc/draft-morrison-reviewed-by-trailer/) — This document defines a trailer grammar for sovereign-portable peer
   review as an extension of the identity-attributed commit grammar of
   draft-morrison-identity-attributed-commits.  The grammar introduces
   one required trailer (Reviewed-By:) and three optional companion
   trailers (Review-Stance:, Review-Of:, Witnessed-By:) that bind a
   Sovereign-tier ~handle to a specific act of review over a specific
   content artefact, cryptographically signed using the Ed25519
   mechanism of that grammar.  The signature covers the reviewer's role,
   the stance, and the review target together, so that changing any of
   them after signing fails verification.  The mechanism applies to git
   commits, document manifests, pre-prints, patent disclosures, and any
   other content-addressable artefact.  A reviewer's signed reviews are
   bound to the reviewer's sovereign handle, not to a publisher's
   platform, and can be verified without the publisher.  For anonymous
   peer review, the reviewer signs under a Sovereign handle whose
   underlying party is concealed through out-of-band key custody; the
   review act stays verifiable and the reviewer's identity is not
   disclosed.  The grammar complements CRediT, ORCID, and DOI
   attribution; it does not replace them.
- **draft-zm-rtgwg-mcp-network-measurement-02** (new-draft, score 7, adjacent_watchlist) [none]: [MCP-based Network Measurement Framework: Using Model Context Protocol for Intelligent Network Measurement](https://datatracker.ietf.org/doc/draft-zm-rtgwg-mcp-network-measurement/) — This document proposes a framework for intelligent network
   measurement using the Model Context Protocol (MCP).  By treating
   network devices as MCP servers, and treating network controllers,
   management systems, or network devices with LLM capability as MCP
   clients, this framework enables natural language-driven, AI-assisted
   network measurement operations.  The framework leverages MCP's
   standardized communication protocol to provide real-time network
   performance monitoring, intelligent fault diagnosis, topology
   discovery, and automated measurement workflows.  This document
   describes the architecture, use cases, and security considerations
   for implementing MCP-based network measurement systems.

## Monitor

- **draft-acosta-crypto-agility-manifest-02** (new-draft, score 6, core_identity) [none]: [A Well-Known Crypto-Agility Manifest](https://datatracker.ietf.org/doc/draft-acosta-crypto-agility-manifest/) — This document defines a small JSON discovery manifest for
   cryptographic migration assessment.  It distinguishes declarations,
   runtime observations and consumer verification, and separates key
   establishment from authentication.  It covers heterogeneous endpoint
   profiles and evidence references.  It does not define cryptographic
   negotiation, an attestation format, a scoring system, or authority to
   modify systems.
- **draft-deforth-arp-01** (new-draft, score 6, trust_infrastructure) [none]: [Agentic Reasoning Protocol (ARP): DNS-Bound Signatures for Entity Self-Descriptions](https://datatracker.ietf.org/doc/draft-deforth-arp/) — This document specifies version 1.3 ("Reader Profile") of the Agentic
   Reasoning Protocol (ARP).  ARP defines a JSON manifest, served at a
   well-known location, in which the operator of a domain publishes a
   self-description of an entity, and an optional Ed25519 signature that
   binds the manifest to the domain through a public key in a DNS TXT
   record.  A valid signature shows that the domain operator published
   exactly this file and that it has not been altered since; it does not
   show that the statements in the file are true.

   Version 1.3 adds a wording profile that limits manifest text to
   third-person statements about the entity, a required provenance
   statement, a readable description of the signature with pointers for
   checking it, a Markdown representation bound to the manifest by a
   SHA-256 digest, a discovery profile, and key revocation through an
   empty key value in the DNS record.
- **draft-fossati-seat-early-attestation-08** (new-draft, score 6, core_identity) [none]: [Using Attestation in Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-fossati-seat-early-attestation/) — The TLS handshake protocol allows authentication of one or both peers
   using static, long-term credentials.  In some cases, it is also
   desirable to ensure that the peer runtime environment is in a secure
   state.  Such an assurance can be achieved using remote attestation
   which is a process by which an entity produces Evidence about itself
   that another party can use to appraise whether that entity is found
   in a secure state.  This document describes a TLS extension that
   enables the negotiation and binding of the TLS authentication key to
   a remote attestation session.  This enables an entity capable of
   producing attestation Evidence, such as a confidential workload
   running in a Trusted Execution Environment (TEE), or an IoT device
   that is trying to authenticate itself to a network access point, to
   present a more comprehensive set of security metrics to its peer.
   This extension has been designed to allow the peers to use any
   attestation technology, in any remote attestation topology, and to
   use them mutually.
- **draft-gruszka-evaluation-receipt-mappings-03** (new-draft, score 6, trust_infrastructure) [none]: [Citing Signed Evaluation Receipts from Existing Envelopes](https://datatracker.ietf.org/doc/draft-gruszka-evaluation-receipt-mappings/) — A Signed Evaluation Receipt records one evaluation result as signed
   payload bytes B.  This document describes how existing envelopes cite
   such a receipt by the SHA-256 digest of B, and how a DSSE envelope
   carries B with the receipt's own signature.  It fixes those bytes and
   a matching rule, maps the parts of a receipt onto DSSE, the in-toto
   Statement with the test-result predicate and the SLSA Verification
   Summary Attestation, shows that the signature of a receipt is already
   a valid DSSE signature, gives a SCITT Signed Statement that names a
   receipt only by its digest, in a key profile and a certificate
   profile, declares the receipt digest as an artifact type for typed
   digest references, and relates a receipt to a pre-run criteria set
   written in PRML.  It defines no new format and no new predicate.
- **draft-kott-numina-pair-binding-01** (new-draft, score 6, adjacent_watchlist) [none]: [An Evidence Preserving Companion Record for the fixed string numina.pair-binding.v1 / Ed25519: A design study of Ed25519; the universal pair binding model.](https://datatracker.ietf.org/doc/draft-kott-numina-pair-binding/) — Software attribution may need to be clarified after release artifacts
   and their cryptographic commitments have been fixed.  Editing those
   artifacts would disturb the evidence that an attribution statement is
   intended to describe.  This paper proposes a separately versioned
   companion record that associates two unchanged source commitments
   with explicit named attribution and an opaque reference to a private
   genesis record.  The construction uses JSON Canonicalization Scheme
   (JCS) bytes, an application-specific message prefix, and pure Ed25519
   signatures.  Its verification model separates payload integrity,
   signing authority, source equality, revision freshness, and private
   reference resolution.  A Numina example preserves two existing
   SHA-256 commitments and records an owner-defined person-to-alias map
   without treating labels as proof of authorship or mathematical
   derivation.  Historical records report reproduction of both
   commitments.  A later byte comparison establishes equality of the
   selected v155 inputs and hash profile, without establishing whole-
   source equality or a deployed signed binding.  The contribution is a
   proposed evidence-preservation and reporting discipline, rather than
   a new cryptographic primitive.  A public-safe record would require
   its own approved payload and signature.  Trust provisioning,
   implementation tests, and public reproducibility remain open.
- **draft-linkgenetic-linkid-uri-01** (new-draft, score 6, core_identity) [none]: [The LinkID URI Scheme and Resolution Model](https://datatracker.ietf.org/doc/draft-linkgenetic-linkid-uri/) — This document specifies the "linkid" URI scheme and a resolution
   model for persistent, location-independent identifiers.  A LinkID
   consists of the scheme name followed by a UUID and identifies a
   resource independently of its current network location.  Resolution
   maps the LinkID to a current actionable URI using one or more
   resolvers.  Resource names, locations, versions and operator
   relationships are associated data, not part of the identifier.  The
   document defines syntax, comparison, resolution semantics and an
   HTTPS binding, and requests an update of the existing IANA URI scheme
   registration.
- **draft-liu-oauth-authorization-schemas-00** (new-draft, score 6, authorization) [none]: [Domain-Specific Authorization Schemas for OAuth 2.0](https://datatracker.ietf.org/doc/draft-liu-oauth-authorization-schemas/) — This specification defines a framework for constructing fine-grained
   authorization requests in OAuth 2.0 using domain-specific
   authorization schemas: structured definitions of behavioral
   boundaries for a particular application domain.  Schema instances are
   carried in authorization requests via authorization_details; upon
   approval, the instance governs the authorization associated with the
   issued access token.  Approved instances have a lifecycle: they
   become active upon approval and end, with defined protocol
   consequences for token issuance, refresh, and resource access.
   Resource servers verify client behaviors against the approved schema
   instance at runtime through deterministic constraint evaluation.
   Authorization servers review requested schema instances against
   server-side authorization policies.  This specification also defines
   a negotiation pattern, reverse-guided authorization, allowing
   resource servers to reference a schema profile in error responses,
   guiding clients toward the authorization required for their next
   action.
- **draft-morrison-alter-uri-scheme-04** (new-draft, score 6, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
   reference syntax for ~handle identity references published in the DNS
   records defined in the companion specification for discovering Model
   Context Protocol servers through DNS TXT records.  An alter: URI
   binds a textual ~handle reference to a resolution and verification
   procedure that retrieves the handle's envelope from a publishing
   zone, validates the envelope's signature chain, and dispatches the
   result to an operating-system URI handler.  The reference may be
   scoped to an organisation, narrowed to a named facet of the identity,
   and addressed to a typed action surface.  The scheme is the
   addressing form of the ~handle@org:facet/action reference; its
   resolution semantics are those of that companion specification,
   reused without modification.

   The scheme is provider-neutral and introduces no new cryptographic
   primitive.  A handler given an alter: URI verifies the handle's
   envelope before acting on it, and where the URI addresses an action,
   verification precedes any side effect.  IANA provisionally registered
   the alter scheme under Section 4 of RFC 7595 on 5 October 2026.
- **draft-morrison-identity-pronouns-04** (new-draft, score 6, core_identity) [none]: [Identity Pronouns: A Reference-Axis Extension to ~handle Identity Systems](https://datatracker.ietf.org/doc/draft-morrison-identity-pronouns/) — This document defines an identity pronoun grammar as a reference axis
   orthogonal to the ~handle identity tier taxonomy defined in draft-
   morrison-mcp-dns-discovery and draft-morrison-identity-attributed-
   commits.  A pronoun is a session-scoped reference that resolves
   client-side to a concrete handle using local session state before any
   cryptographic, DNS, or federation operation.  The entity-class
   taxonomy (Sovereign, Bot, Instrument) is unchanged; this
   specification introduces Absolute vs Pronoun as an orthogonal axis.
   A pronoun MUST NOT appear in a capability token, in a DNS record, in
   an Accord signature, or in any inter-organisational protocol payload.
   This document defines a single Wave-1 pronoun, ~org, that resolves to
   the concrete handle of the organisation bound to the caller's current
   session.  An appendix defines a relative-path pronoun grammar (e.g.
   ~./finance, ~../compliance) as a non-normative design surface for
   future work.  The mechanism is provider-neutral, introduces no new
   cryptographic primitive, and adds no load to DNS, capability-token
   issuers, or federated resolvers.
- **draft-morrison-substrate-observation-03** (new-draft, score 6, core_identity) [none]: [Substrate-Observation as an Alternative to Envelope Coordination for Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-substrate-observation/) — This memo describes a coordination-protocol anti-pattern observed in
   cross-tool agentic systems and a substrate-observation alternative
   that does not require negotiating a wire format between heterogeneous
   concurrent sessions of an identity-bound principal.  The memo is
   Informational and proposes no protocol element for standardisation.
   It sets out what should not be standardised for this problem, and
   why, and identifies the existing substrate mechanisms that serve in
   its place.  Companion memos describe the identity primitives this
   memo presumes.
- **draft-mott-cose-sqisign-09** (new-draft, score 6, verifiable_claims) [none]: [CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for SQIsign](https://datatracker.ietf.org/doc/draft-mott-cose-sqisign/) — *NOTE: This document describes a signature scheme based on the
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
- **draft-richardson-quantum-safe-devid-pki-00** (new-draft, score 6, core_identity) [none]: [Quantum-Safe Device Identity Public Key Infrastructure (PKI)](https://datatracker.ietf.org/doc/draft-richardson-quantum-safe-devid-pki/) — This document discussed options for building a quantum-safe 802.1AR
   Device Identity certificates.

   The focus of this document is on IDevID which are used for onboarding
   of devices, detection of counterfeit devices, and limited remote
   attestation methods.
- **draft-srivastava-learnlog-01** (new-draft, score 6, adjacent_watchlist) [none]: [learnlog: A Verifiable Event Log Format for Learning Software](https://datatracker.ietf.org/doc/draft-srivastava-learnlog/) — This document defines learnlog, a log format for learning software.
   A record holds typed events that describe what a learner did and what
   other parties, human or software, did in response.  As AI
   participates in learning and assessment, these records can preserve
   the assistance and producing instruments needed to interpret a
   performance.  The format does not establish independent learning or
   the effectiveness of an intervention.  Entries are chained by hash,
   and a producer can sign the chain.  A reader who trusts the signing
   key can then detect changes to the entries under a signed head that
   were made without that key.  Some changes remain undetectable, and
   the security considerations list them.  An event can be redacted, and
   the rest of the record still verifies.  The format defines files,
   records, entries, events, and registries for event schemas.  Subject-
   area event schemas and judgments about the applicability of research
   are out of scope.
- **draft-stephan-agentproto-6g-usecases-00** (new-draft, score 6, agent_identity) [none]: [AI Agent protocols for 6G systems](https://datatracker.ietf.org/doc/draft-stephan-agentproto-6g-usecases/) — Communication between AI agents and between agent and tools is
   expected to be pivotal in 6G systems.  The 3GPP TR 22.870 outlines
   various use cases and potential service requirements for AI agent
   communication within 6G systems.  This document provides examples of
   use cases and service requirements contained in the 3GPP TR 22.870
   and extrapolates possible requirements related to agent communication
   protocols.
- **draft-watts-agent-continuity-observability-00** (new-draft, score 6, trust_infrastructure) [none]: [Continuity and Accountability Observations for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-continuity-observability/) — Agentic systems change models, prompts, memory, policies, tools, and
   execution environments across handoffs.  This document proposes an
   observation profile for recording those transitions and their
   evidence.  It separates state, memory, policy, authority, and lineage
   discontinuities, distinguishes manual or simulated observations from
   attested executions, and defines coverage and missingness reporting.
   It also describes evaluation designs for continuity and bounded
   governance.  Continuity records do not grant authority, establish
   clinical pathology or subjective experience, or validate an
   uncalibrated composite score.
- **draft-watts-unison-noncollapse-00** (new-draft, score 6, authorization) [none]: [Typed UNISON and Non-Collapse Boundaries for Evidence and Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-unison-noncollapse/) — This document describes a transport-neutral model for bounded
   correspondence among distinct representations and explicit promotion
   boundaries between observation, evidence, authorization, and
   execution.
- **draft-calabria-bmwg-ai-fabric-training-bench-05** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-correctover-gg-mcp-parameter-risk-01** (new-draft, score 5, adjacent_watchlist) [none]: [MCP Parameter Risk Classes for Machine-Readable Risk Metadata](https://datatracker.ietf.org/doc/draft-correctover-gg-mcp-parameter-risk/) — This document defines a fixed set of five canonical MCP parameter
   risk classes: semantic categories for sensitive parameters that
   appear in the JSON Schemas of Model Context Protocol (MCP) tool
   definitions, together with deterministic decision rules and boundary
   conditions for assigning those labels.  The classes are designed to
   supply machine-readable, pre-invocation risk metadata about tool
   inputs, independent of any particular gateway, routing, or
   capability-profile specification.

   The classes and their decision rules were derived from, and applied
   against, a SHA-256-frozen empirical census of publicly reachable MCP
   servers.  The frozen census and the classification suite that
   implements these rules are archived on Zenodo; the archived suite is
   the normative tie-breaker for exact matching behaviour.

   This is an Informational, individual submission.  It defines the
   canonical classes and decision rules.  Other specifications MAY cite
   this document as the canonical source of the class labels and MAY
   define their own operators that consume those labels; they SHOULD NOT
   re-derive or inline the normative decision rules into their own
   normative text.
- **draft-dias-agent-payment-verdicts-00** (new-draft, score 5, authorization) [none]: [Signed Authorization Verdicts for Agent-Initiated Payments](https://datatracker.ietf.org/doc/draft-dias-agent-payment-verdicts/) — When a software agent initiates a payment on behalf of an
   organization, the party that settles the payment usually cannot see
   the policy under which it was permitted.  This document describes a
   signed authorization verdict: a JSON Web Token, signed with ES256,
   that records the outcome of evaluating one payment request, including
   its amount, currency, and recipient, against a spending policy that
   the organization configured.  A party holding the issuer's published
   public key can verify a verdict without contacting the issuer.

   The document describes the claim set, key publication and rotation,
   and a verification procedure, and states what a verdict does not
   assert.  It describes the format as one implementation issues it,
   including the points where it departs from JSON Web Token Best
   Current Practices (RFC 8725).  It is offered as input to IETF
   discussion of authorization records for agent-initiated actions and
   is not a proposal for standardization.
- **draft-dunbar-dawn-infra-assisted-discovery-00** (new-draft, score 5, agent_identity) [none]: [Infrastructure-Assisted Discovery for AI Agents](https://datatracker.ietf.org/doc/draft-dunbar-dawn-infra-assisted-discovery/) — This document describes an infrastructure-assisted approach
   to AI-agent discovery. An orchestration, placement, or
   hosting system can publish current deployment and
   reachability information for available AI-agent services or
   instances. Separately, network infrastructure can derive an
   abstract Attachment Scope representing the network context
   applicable to a requester. A discovery mechanism combines
   requester intent, currently published AI-agent resources, and
   the requester's Attachment Scope to identify applicable agent
   instances.
- **draft-janz-nmrg-adhoc-semantic-reconciliation-01** (new-draft, score 5, adjacent_watchlist) [none]: [Portable Semantic Models and Ad Hoc Reconciliation by Cognitive Agents in Network Management](https://datatracker.ietf.org/doc/draft-janz-nmrg-adhoc-semantic-reconciliation/) — Interoperation between network-management systems has traditionally
   required a data model agreed in advance.  Where that is insufficient,
   a richer shared information model or ontology is agreed instead.
   Both demand broad prior agreement, negotiated and maintained by
   people.  This document examines what becomes possible once the
   systems on each side can reason.  Each side can lift its own data
   into a complete semantic model.  Two such models can then reconcile
   ad hoc, for the occasion, with no model agreed beforehand.

   The document develops the semantic model and the two operations upon
   it: the lift that produces a model, and the reconciliation that
   bridges two.  It gives careful treatment to pragmatics, the layer a
   schema is least likely to hold and so the part most easily left out
   of view, yet often one that carries key operative meaning.  It
   considers the form and utility of thin references, separately
   assessing the two distinct roles they may play.  It then reports an
   empirical study across four network-management scenarios, run over
   independently constructed cases and several cognitive-agent families.
   The study measures the portability of a lifted model, the extent to
   which cognition can reconcile divergent models without support of a
   pre-agreed standard, where a reference is load-bearing and what it
   usefully comprises.  It closes with conclusions for how information
   should be prepared for cognitive systems, and for how the community's
   standardization effort might evolve.

   This is a research document intended to inform discussion in the IRTF
   Network Management Research Group.  It reflects the authors' ideas,
   thoughts and experimental findings and does not represent IETF or
   IRTF consensus.
- **draft-king-yew-choo-agentic-payments-01** (new-draft, score 5, adjacent_watchlist) [none]: [A Server-Side Model for Gating Agent-Initiated Human-Sourced Asynchronous HTTP Tasks on Payment or Entitlement](https://datatracker.ietf.org/doc/draft-king-yew-choo-agentic-payments/) — This document presents a server-side model for paid, human-sourced
   asynchronous HTTP tasks initiated by software agents acting on behalf
   of a principal.  Clients may retry after uncertain outcomes and act
   under authority delegated in advance, while fulfilment incurs cost
   and may not be freely reversible.

   The model places a payment or entitlement gate before fulfilment,
   maps that gate to adjacent protocols, and defines a task state
   machine.  Under stated well-formedness constraints and operating
   assumptions, it yields gate-before-fulfilment safety, at most one
   task per retained idempotency key, at most one gate acceptance per
   payment requirement, and an operator-checkable record linking a
   delivered artefact to operator-controlled records.  It defines no
   protocol, wire format, or conformance requirements.
- **draft-konda-agentproto-evaluation-state-01** (new-draft, score 5, authorization) [none]: [Preserving Evaluation State in Agent Protocol Decisions](https://datatracker.ietf.org/doc/draft-konda-agentproto-evaluation-state/) — Agent protocols often require a participant to establish a decision-
   time input before it acts: issuer standing, key availability,
   delegated authority, policy profile availability, consumption state,
   revocation status, or the outcome of a downstream operation.  A
   participant that establishes an input and receives a negative answer
   has learned a different fact from a participant that cannot establish
   the input at all.  Collapsing those facts into one denial or failure
   value changes retry behavior, alert routing, audit interpretation,
   incident ownership, and post-incident reconstruction.

   This document specifies requirements for preserving evaluation state
   across agent protocol boundaries: the value of an input, whether that
   value was established at decision time, the freshness of the source
   used to establish it, and whether the resulting policy decision was
   actually evaluated.  The requirements are stated independently of
   encoding, so that policy, authorization, revocation, routing, and
   audit documents can satisfy them in their own formats.  A subsequent
   revision will specify concrete representations.
- **draft-nestorov-scitt-p10-underdetermination-01** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Adjudication Statements over SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming P10
   Adjudication Statement carries two canonical witness worlds that are
   compatible with the same closed evidence set and produce different
   values for the same frozen claim.  The witness result is checked
   against committed profile semantics and bound into a SCITT
   Transparent Statement containing an in-toto Statement v1 predicate.
   The result establishes underdetermination only relative to the
   declared profile and does not identify the actual world or establish
   either claim value as true.
- **draft-singh-psi-agent-01** (new-draft, score 5, agent_identity) [none]: [PSI Receipts for AI Agent Actions](https://datatracker.ietf.org/doc/draft-singh-psi-agent/) — This document defines a profile of Proof of Stateful Integrity (PSI)
   for recording actions taken by software agents, including calls to
   language models and tools.  The agent runtime computes a digest of
   each action locally and seals only the digest, so later alteration or
   omission of a recorded action is detectable.  A receipt shows that a
   specific action record existed unchanged at a time; it does not show
   that the action was correct, safe, authorised, or lawful, and it
   allocates no liability.

   This revision withdraws the liability-allocation language of revision
   00 and aligns the Merkle commitment with draft-singh-psi-merkle-01.
- **draft-watts-boundary-jurisdiction-architecture-01** (new-draft, score 5, agent_identity) [none]: [Boundary Jurisdiction Architecture for Agentic and Delegated Systems](https://datatracker.ietf.org/doc/draft-watts-boundary-jurisdiction-architecture/) — This document describes a protocol-neutral architecture for
   separating possession of capability from jurisdiction over
   consequential authority boundaries.  It models authority as
   reachability in a time-indexed capability graph, defines revocation
   cuts, and specifies fail-closed semantics for delegation and
   revocation closure.
- **draft-xg-payment-dispute-profile-00** (new-draft, score 5, adjacent_watchlist) [none]: [Card-Scheme Dispute Evidence Profile of Signed Decision Receipts](https://datatracker.ietf.org/doc/draft-xg-payment-dispute-profile/) — This document profiles draft-farley-acta-signed-receipts, "Signed
   Decision Receipts for Machine-to-Machine Access Control", for use as
   card-scheme dispute evidence.  It defines how a conforming decision
   receipt is populated for payment disputes, and specifies four
   additional evidence layers bound to that receipt: card-scheme
   dispute-evidence categories (Visa Compelling Evidence 3.0, Mastercard
   First-Party Trust), agent-native anchors with no scheme-defined slot,
   a settlement anchor recording what money actually moved, and an
   evidentiary-custody wrapper aligned with U.S.  Federal Rules of
   Evidence 901/902.  This is a vendor profile documenting one
   implementation (ActaSeal's DisputeEvidencePacket); it does not define
   a new protocol and makes no claim of IETF consensus or
   standardization.
- **draft-zm-rtgwg-mcp-troubleshooting-02** (new-draft, score 5, adjacent_watchlist) [none]: [Using the Model Context Protocol (MCP) for Intent-Based Network Troubleshooting Automation](https://datatracker.ietf.org/doc/draft-zm-rtgwg-mcp-troubleshooting/) — The Model Context Protocol (MCP) is an open standard that enables
   Large Language Model (LLM) applications to seamlessly integrate with
   external data sources and tools by exposing Resources, Prompts and
   Tools in a JSON-RPC 2.0 transport.  This document describes a mapping
   of MCP roles, primitives and security model to the network management
   domain so that network devices act as MCP servers and network
   controllers act as MCP clients.  This document also extends the model
   to Device-to-Device (D2D) collaboration, allowing network elements to
   perform distributed fault correlation when the controller is
   unreachable or when real-time cross-device data is required.  The
   goal is to provide an intent-based, conversational and secure
   approach for automated network troubleshooting, configuration
   validation, and closed-loop remediation without inventing new
   protocols or device agents.
- **draft-ietf-keytrans-architecture-10** (new-draft, score 4, trust_infrastructure) [keytrans]: [Key Transparency Architecture](https://datatracker.ietf.org/doc/draft-ietf-keytrans-architecture/) — This document defines the terminology and interaction patterns
   involved in the deployment of Key Transparency in a general secure
   group messaging infrastructure, and specifies the security properties
   that the protocol provides.  It also gives more general, non-
   prescriptive guidance on how to securely apply Key Transparency to a
   number of common applications.
- **draft-nam-ksg-core-00** (new-draft, score 4, adjacent_watchlist) [none]: [Keysingate Core: Channel Documents, Status Records and Anchored Time](https://datatracker.ietf.org/doc/draft-nam-ksg-core/) — This document specifies the core of Keysingate: the canonical form
   and signature envelope of its documents, the time format and the rule
   that gives a signed object an upper time bound from public-network
   anchors, and the documents of the issuance channel -- release,
   delegation, block allocation, block closure, agent binding, container
   initiation, key inclusion, class promotion -- together with the
   status record that tracks a container's life.  It is written so that
   two independent implementations produce the same bytes and reach the
   same verdict.  The work journal kept inside a container, and its
   export, are specified in a companion document.
- **draft-zeng-opsawg-llm-netconf-gap-01** (new-draft, score 4, adjacent_watchlist) [none]: [Gap Analysis of Network Configuration Protocols in LLM-Driven Intent-Based Networking](https://datatracker.ietf.org/doc/draft-zeng-opsawg-llm-netconf-gap/) — Large Language Models (LLMs) are entering network operations through
   natural-language intent interfaces.  Existing south-bound protocols
   (NETCONF, RESTCONF, gNMI, MCP, A2A) were not designed for
   conversational, semantically-rich, multi-agent orchestration.  This
   document provides a systematic gap analysis and identifies extension
   points for each protocol to meet intent-based networking
   requirements.

## Adjacent / watchlist

- **draft-atwrgm-drip-orchid-v3-00** (new-draft, score 3, core_identity) [none]: [Overlay Routable Crytographic Hash IDentifiers Version 3](https://datatracker.ietf.org/doc/draft-atwrgm-drip-orchid-v3/) — Over time improvements and implementation considerations have been
   accumulating around Overlay Routable Cryptographic Hash Identifiers
   (ORCHIDs) for the Host Identity Protocol (HIP) and the Drone Remote
   Identification Protocol (DRIP).  Such improvements like the addition
   of hierarchy in RFC9374, or the development of using ORCHIDs in other
   frameworks are scattered across resources.  This document serves to
   combine lessons learned and minor corrections into a single
   specification that obsolete RFC7343 and updates RFC7401 and RFC9374
   to maintain interoperability of ORCHID-aware implementations.
- **draft-chen-idr-srv6-flowspec-path-redirect-03** (new-draft, score 3, core_identity) [idr]: [Flowspec Indirection-id Redirect for SRv6](https://datatracker.ietf.org/doc/draft-chen-idr-srv6-flowspec-path-redirect/) — BGP Flow Specification Version 2 (FSv2) provides an extensible
   framework for disseminating traffic flow filtering rules and
   associated traffic redirection actions.  This document specifies
   extensions to the FlowSpec Redirect to Indirection-id Extended
   Community specifically for SRv6 (Segment Routing over IPv6).  When
   received by a Flowspec client, this extended community triggers an
   indirection-based lookup within a localized mapping table to retrieve
   the target SRv6 Segment Identifier (SID), SRv6 Policy, or Binding SID
   (BSID) forwarding state.  This mechanism decouples control-plane BGP
   Flowspec redirection instructions from dynamic underlay path updates
   in SRv6 networks.
- **draft-dong-sidrops-rpki-rtr-moa-pdu-02** (new-draft, score 3, authorization) [none]: [IPv6 Mapping Prefix PDU for the RPKI-Router Protocol](https://datatracker.ietf.org/doc/draft-dong-sidrops-rpki-rtr-moa-pdu/) — This document defines a new Protocol Data Unit (PDU) type for the
   RPKI to Router Protocol to convey Mapping Origin Authorization (MOA)
   information from RPKI caches to routers.  The new PDU, named the
   "IPv6 Mapping Prefix" PDU, carries the authorization mapping between
   one or more IPv4 prefix and their corresponding authorized IPv6
   mapping prefix.  This extension enables routers to perform Mapping
   Origin Validation (MOV) for IPv4-to-IPv6 address mapping
   announcements in IPv6-only underlay networks.
- **draft-dsmullen-ppd-architecture-11** (new-draft, score 3, adjacent_watchlist) [none]: [Privacy Preference Declaration for Home Networks](https://datatracker.ietf.org/doc/draft-dsmullen-ppd-architecture/) — This document describes an architecture for signaling household
   privacy preferences to devices in home networks through Privacy
   Preference Declarations (PPDs).  The architecture enables a PPD
   participant to discover a PPD service endpoint, establish trust in
   that endpoint through the applicable protocol and security profile,
   retrieve the applicable household policy instance, and acknowledge
   receipt of that policy instance.  The acknowledgment establishes that
   a specific policy instance was made available to the participant; it
   does not, by itself, assert anything about the participant's
   subsequent behavior.
- **draft-dulaunoy-rifp-auth-00** (new-draft, score 3, core_identity) [none]: [Pre-Shared-Key Object Authentication for RIFP](https://datatracker.ietf.org/doc/draft-dulaunoy-rifp-auth/) — This document defines an optional object authentication extension for
   the Radio Image Framing Protocol (RIFP).  A critical header TLV
   authenticates the compact object descriptor using HMAC-SHA-256 and a
   pre-shared key.  The descriptor binds the encoded image digest and
   decoding parameters to a session and chunk count.  The extension uses
   existing RIFP framing, fragmentation, retransmission and offline IQ
   workflows.  It does not provide confidentiality, replay protection or
   a public-key digital signature.
- **draft-eastlake-secdispatch-tenantid-consid-10** (new-draft, score 3, core_identity) [none]: [Security Considerations for Tenant ID and Similar Fields](https://datatracker.ietf.org/doc/draft-eastlake-secdispatch-tenantid-consid/) — Many protocols provide for header fields to be added to a packet on
   ingress to a network domain and removed on egress from that domain.
   Examples of such fields are Tenant ID for multi-tenant networks,
   ingress port ID and/or type, and other identity or handling directive
   fields.  These fields mean that a packet may be accompanied by
   supplemental information as it transits the network domain that would
   not be present with the packet or not be visible if it were simply
   forwarded in a traditional manner.  A particular concern is that
   these fields may harm privacy by identifying, in greater detail, the
   packet source and intended traffic handling.  This document provides
   Security Considerations for the inclusion of such fields with a
   packet.
- **draft-ietf-asdf-digital-twin-06** (new-draft, score 3, adjacent_watchlist) [asdf]: [Semantic Definition Format (SDF) Modeling for Digital Twin](https://datatracker.ietf.org/doc/draft-ietf-asdf-digital-twin/) — This memo specifies SDF modeling for digital twins, i.e., digital
   twin systems, and their things.  An SDF is a format that is used to
   create and maintain data and interaction, and to represent the
   various kinds of data that is exchanged for these interactions.  The
   SDF format can be used to model the characteristics, behavior and
   interactions of things, i.e. physical objects, in digital twins that
   contain things as components.
- **draft-ietf-bess-evpn-inter-domain-opt-b-00** (new-draft, score 3, adjacent_watchlist) [bess]: [EVPN Inter-Domain Option-B Solution](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-inter-domain-opt-b/) — An EVPN Inter-Domain interconnect solution is required when two or
   more sites of the same Ethernet Virtual Private Network (EVPN) are
   connected to different IGP domains or Autonomous Systems (AS) and
   need to communicate.  The Inter-Domain Option-B connectivity model is
   one of the most popular solutions for this type of EVPN connectivity.
   While several documents address specific aspects of this interconnect
   approach, none provide a comprehensive overview of how Inter-Domain
   Option-B connectivity affects EVPN procedures.  This document
   examines the behavior of EVPN procedures in an Inter-Domain Option-B
   network and proposes solutions to the identified issues.
- **draft-ietf-cdni-processing-stages-metadata-02** (new-draft, score 3, adjacent_watchlist) [cdni]: [CDNI Processing Stages Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-processing-stages-metadata/) — This document specifies a set of objects extending the Content
   Delivery Network Interconnection (CDNI) metadata model to allow for
   metadata to be applied conditionally and at various points in a dCDNs
   processing of requests.  The concept of Processing Stages are
   introduced, where each stage in a CDN's processing pipeline presents
   an opportunity to examine requests and responses and make alterations
   as needed.  Metadata, such as caching rules, can be applied
   conditionally (based on aspects of an HTTP request header), and HTTP
   responses from a source can be altered dynamically (such as adding or
   dropping an HTTP header).  This standard leverages the expression
   language documented in the Metadata Expression Language (MEL)
   Specification.
- **draft-ietf-httpbis-connect-tcp-15** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP tunneling using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this tunneling functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-jmap-calendars-33** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-masque-connect-ethernet-16** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document specifies how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-masque-connect-ip-dns-07** (new-draft, score 3, adjacent_watchlist) [masque]: [DNS and PREF64 Configuration for Proxying IP in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip-dns/) — Proxying IP in HTTP allows building a VPN through HTTP load
   balancers.  However, at the time of writing, that mechanism lacks a
   way to communicate network configuration details such as DNS
   information or IPv6 NAT64 prefixes (PREF64).  In contrast, most
   existing VPN protocols provide mechanisms to exchange such
   configuration information.

   This document defines extensions that convey DNS and PREF64
   configuration using HTTP capsules.  This mechanism supports encrypted
   DNS transports and can be used to inform peers about network
   translation prefixes for IPv6/IPv4 synthesis.
- **draft-ietf-netconf-list-pagination-14** (new-draft, score 3, adjacent_watchlist) [netconf]: [List Pagination for YANG-driven Protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination/) — In some circumstances, instances of YANG modeled "list" and "leaf-
   list" nodes may contain numerous entries.  Retrieval of all the
   entries can lead to inefficiencies in the server, the client, and the
   network in between.

   This document defines a model for list pagination that can be
   implemented by YANG-driven management protocols such as NETCONF and
   RESTCONF.  The model supports paging over optionally filtered and/or
   sorted entries.  The solution additionally enables servers to
   constrain query expressions on some "config false" lists or leaf-
   lists.
- **draft-ietf-nmop-network-incident-yang-19** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
   lifecycle management.  This YANG module provides a standard way to
   report, diagnose, and help reduce troubleshooting tickets and resolve
   network incidents for the sake of network service health and probable
   root cause analysis.
- **draft-ietf-opsawg-scheduling-oam-tests-11** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A YANG Data Model for Network Diagnosis using Scheduled Sequences of OAM Tests](https://datatracker.ietf.org/doc/draft-ietf-opsawg-scheduling-oam-tests/) — This document defines two YANG Data Models to support scheduled
   network diagnosis using Operations, Administration, and Maintenance
   (OAM) tests.  This document defines both 'oam-unitary-test' and 'oam-
   sequence-test' YANG modules to manage the lifecycle of network
   diagnosis procedures, intended for use by external management and
   orchestration systems (including SDN controllers and network
   orchestrators), rather than by individual network nodes.
- **draft-ietf-pce-stateful-pce-autobw-update-05** (new-draft, score 3, adjacent_watchlist) [pce]: [Update to the Automatic Bandwidth Adjustment Procedure for MPLS-TE and SR-TE LSPs with a Stateful PCE](https://datatracker.ietf.org/doc/draft-ietf-pce-stateful-pce-autobw-update/) — Extensions for the stateful PCE model enable control of Traffic
   Engineering (TE) LSPs using the Path Computation Element
   Communication Protocol (PCEP) for RSVP-TE and Segment Routing (SR),
   for both PCE-initiated and PCC-initiated LSPs.

   RFC 8733 defines PCEP extensions for automatically adjusting
   bandwidth on MPLS-TE Label Switched Paths (LSPs) using a stateful
   PCE.  It also defines the AUTO-BANDWIDTH-ATTRIBUTES TLV and a set of
   sub-TLVs for the attributes.  A sub-TLV is included when its value
   differs from the value last sent in a PCEP message.  However, RFC
   8733 lacks a mechanism to explicitly remove an attribute identified
   by a sub-TLV.  This document updates RFC 8733 by defining such a
   mechanism.

   In addition, this document applies the PCEP extensions for automatic
   bandwidth adjustment to SR-TE LSPs in both the MPLS (SR-MPLS) and
   IPv6 (SRv6) data planes.  It also extends automatic bandwidth
   adjustment to multiple Segment Lists in an SR LSP using the
   extensions defined in draft-ietf-pce-multipath.
- **draft-ietf-radext-epcs-01** (new-draft, score 3, core_identity) [radext]: [RADIUS attributes for National Security and Emergency Preparedness Service](https://datatracker.ietf.org/doc/draft-ietf-radext-epcs/) — This document defines RADIUS attributes for authorizing the use of
   Emergency Preparedness Communication Service (EPCS) priority access
   defined in IEEE 802.11be.  These attributes allow an Identity
   Provider to indicate that an authenticated user is authorized for
   EPCS, enabling the Wi-Fi network provider to apply EPCS priority
   access to the user's Wi-Fi session.  The attributes also support
   RADIUS accounting for Wi-Fi sessions in which EPCS priority access is
   used.
- **draft-ietf-sidrops-rtr-yang-10** (new-draft, score 3, adjacent_watchlist) [sidrops]: [YANG Data Model for RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rtr-yang/) — This document defines YANG data models for managing Resource Public
   Key Infrastructure (RPKI) to Router Protocol (RFC6810 and RFC8210).
- **draft-ietf-spring-sid-as-source-address-01** (new-draft, score 3, core_identity) [spring]: [SID as source address in SRv6](https://datatracker.ietf.org/doc/draft-ietf-spring-sid-as-source-address/) — Segment Routing over IPv6 (SRv6) is deployed in backbone networks
   within trusted domains to provide end-to-end services in carrier and
   enterprise networks.  However, a stateful firewall on an SRv6
   forwarding path may discard legitimate SRv6 packets and ICMP error
   messages generated by SRv6 transit nodes because packets in the two
   directions may have different flow tuples.

   This document specifies a mechanism that uses an SRv6 Segment
   Identifier (SID) as the source address in the outer IPv6 header.  A
   distinct source SID can be assigned to each Customer Edge (CE) or
   Virtual Routing and Forwarding (VRF) instance, enabling a firewall to
   perform per-flow stateful filtering of TCP traffic without requiring
   SRv6 support in the firewall or the deployment of an SRv6 proxy.
- **draft-ietf-spring-srv6-path-segment-16** (new-draft, score 3, core_identity) [spring]: [Path Segment Identifier (PSID) in SRv6 (Segment Routing in IPv6)](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-path-segment/) — Segment Routing (SR) allows for a flexible definition of end-to-end
   paths by encoding an ordered list of instructions, called "segments".
   The SR architecture can be implemented over an MPLS data plane as
   well as an IPv6 data plane.

   Currently, Path Segment Identifier (PSID) has been defined to
   identify an SR path in SR-MPLS networks, and is used for various use-
   cases such as end-to-end SR Path Protection and Performance
   Measurement (PM) of an SR path.  This document defines the PSID to
   identify an SRv6 path in an IPv6 network.
- **draft-ietf-tsvwg-sctp-dtls-chunk-05** (new-draft, score 3, core_identity) [tsvwg]: [Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/) — This document describes a method for adding Datagram Transport Layer
   Security (DTLS) based authentication and cryptographic protection to
   the Stream Control Transmission Protocol (SCTP).

   This SCTP extension is intended to enable communication privacy for
   applications that use SCTP as their transport protocol and allows
   applications to communicate in a way that is designed to prevent
   eavesdropping and detect tampering or message forgery.  Once enabled,
   this also applies to the SCTP payload as well as the SCTP control
   information.

   Applications using this SCTP extension can use most of the transport
   features provided by SCTP and its other extensions.  The use of the
   SCTP Authentication extension defined in RFC 4895 is incompatible
   with the extension defined in this document but would not provide any
   additional service.  This implies that the Dynamic Address
   Reconfiguration as specified in RFC 5061 can only be used as
   described in this document.

   This document obsoletes RFC 6083 and updates RFC 5061.
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-31** (new-draft, score 3, adjacent_watchlist) [v6ops]: [Framework for Multi-domain IPv6-only Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — This document presents a framework, from the network operators'
   perspective, for building and operating IPv6-only core networks that
   span multiple domains (i.e., multiple interconnected Autonomous
   Systems).  To carry residual IPv4 traffic in such an environment, the
   framework proposes stateless IPv4/IPv6 address mapping as the basis
   for IPv4-as-a-Service (IPv4aaS), so that IPv4 packets are translated
   at the network edge and forwarded across the IPv6-only core network
   without per-flow state or IPv4/IPv6 conversion gateways on the data
   path.  The document is intended as a network operator problem
   statement, guidance, and requirements rather than a protocol
   specification.  It covers the scope of applicability and trust
   boundaries, options for IPv6 mapping prefix allocation, and
   operational, manageability, and security considerations.
- **draft-irtf-cfrg-bbs-signatures-13** (new-draft, score 3, adjacent_watchlist) [cfrg]: [The BBS Signature Scheme](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) — This document describes the BBS Signature scheme, a secure, multi-
   message digital signature protocol, supporting proving knowledge of a
   signature while selectively disclosing any subset of the signed
   messages.  Concretely, the scheme allows for signing multiple
   messages whilst producing a single, constant size, digital signature.
   Additionally, the possessor of a BBS signatures is able to create
   zero-knowledge, proofs of knowledge of a signature, while selectively
   disclosing subsets of the signed messages.  Being zero-knowledge, the
   BBS proofs do not reveal any information about the undisclosed
   messages or the signature itself, while at the same time,
   guaranteeing the authenticity and integrity of the disclosed
   messages.
- **draft-litzki-sovp-04** (new-draft, score 3, core_identity) [none]: [Sovereign Validation Protocol (SOVP)](https://datatracker.ietf.org/doc/draft-litzki-sovp/) — This document specifies the Sovereign Validation Protocol (SOVP), a
   protocol for checking, before ingestion, that a signed identity
   document was produced by the party that controls the Ed25519 key
   published in DNS for a host.  A consumer retrieves a JSON document
   from a well-known location on the host, canonicalizes it, and
   verifies its signature against the key published in a DNS TXT record.
   The protocol defines the signed scope, the retrieval and key
   resolution rules, freshness checks, resource limits for unverified
   input, and an optional extension that binds a document to a
   deployment instance.  It does not establish legal identity, the
   accuracy of content, or the configuration of the system that serves
   the document.
- **draft-mailschema-mail-action-protocol-00** (new-draft, score 3, core_identity) [none]: [Mail Action Protocol (MAP)](https://datatracker.ietf.org/doc/draft-mailschema-mail-action-protocol/) — Mail Action Protocol (MAP) describes actions offered by email, such
   as approval to publish an article.  A type contract defines each
   decision and its effects.  A trusted service binding connects that
   decision to an existing service operation.  Before acting, a client
   reads the current proposal and applies the user's policy.  The
   service checks permission and the exact terms when it records the
   decision.  MAP uses Structured Email's MIME and JSON-LD
   representation.  Core is independent of the interface used to call
   the service.  This document specifies an HTTP binding, Registry
   discovery rules and an experimental capability binding for a limited
   set of actions without a service account connection.  It defines no
   general action endpoint or replacement authentication system.
- **draft-mittal-est-coap-no-cert-00** (new-draft, score 3, core_identity) [none]: [EST-coaps Enrollment Using Device-Unique Symmetric Keys for Field Devices without Initial Certificates](https://datatracker.ietf.org/doc/draft-mittal-est-coap-no-cert/) — This document specifies a profile for Enrollment over Secure
   Transport using secure CoAP, where the EST-coaps client is a field
   device that does not possess an initial device certificate,
   manufacturer certificate, or other certificates usable for DTLS
   client authentication.  Instead, the device is authenticated during
   the DTLS handshake using a device-unique symmetric key or a pre-
   shared key derived from that device-unique key.

   This profile is intended for already registered and operational
   devices that do not possess a certificate suitable for EST-coaps
   client authentication but do possess a device-unique symmetric key
   that can be used for initial authentication during certificate
   enrollment.  The mechanism preserves EST certificate enrollment
   semantics while replacing the initial certificate-based DTLS client
   authentication requirement with PSK-based DTLS authentication.
   [RFC9148] defines EST over secure CoAP and requires client
   authentication for EST-coaps functions, while [RFC7030] permits
   certificate-less TLS authentication scenarios for EST when suitable
   shared credentials are available.
- **draft-porfiri-tsvwg-sctp-dtls-handshake-02** (new-draft, score 3, core_identity) [none]: [Transport Layer Security (TLS) based Key Management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/) — This document defines how Transport Layer Security (TLS) 1.3 is used
   as a key management method for the SCTP DTLS Chunk mechanism.  It
   specifies how a TLS handshake establishes the initial security
   context for an SCTP association and how subsequent TLS handshakes
   provide key updates and re-authentication.  The goal is to enable
   authenticated and confidential communication over SCTP using the DTLS
   Chunk, leveraging standardized TLS 1.3 features for key management
   and rekeying.
- **draft-reddy-cose-hpke-hqc-00** (new-draft, score 3, verifiable_claims) [none]: [Hamming Quasi-Cyclic (HQC) Ciphersuites for COSE-HPKE](https://datatracker.ietf.org/doc/draft-reddy-cose-hpke-hqc/) — This document specifies Hamming Quasi-Cyclic (HQC)-based ciphersuites
   for use with COSE-HPKE.  It defines fully specified COSE algorithms
   for HPKE Integrated Encryption and HPKE Key Encryption, using HQC or
   PQ/T hybrid HQC key encapsulation, SHAKE256 key derivation, and AES-
   256-GCM authenticated encryption.  It specifies their AKP key
   representation and requests twelve COSE algorithm registrations.
   Message processing and context binding are inherited from COSE-HPKE.
- **draft-reddy-ipsecme-ikev2-mtc-landmarks-00** (new-draft, score 3, adjacent_watchlist) [none]: [Merkle Tree Certificates in the Internet Key Exchange Protocol Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-reddy-ipsecme-ikev2-mtc-landmarks/) — This document specifies the use of Merkle Tree Certificates (MTCs) in
   the Internet Key Exchange Protocol Version 2 (IKEv2).  An IKE peer
   sends an MTC in place of a directly-signed end-entity certificate and
   its chain of Certification Authority (CA) certificates.  The MTC
   carries an inclusion proof in place of CA signatures, which reduces
   the size of the IKE_AUTH exchange, in particular with post-quantum
   signature algorithms such as ML-DSA and SLH-DSA.  This document
   defines a Certificate Encoding for the Certificate Request payload
   that carries trust anchor identifiers.  An IKE peer uses these
   identifiers to indicate the MTC CAs and landmarks it trusts.
- **draft-singh-apex-psi-03-02** (new-draft, score 3, core_identity) [none]: [PSI-03: Receipts for Virtual Power Plant Dispatch Records](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/) — This document defines PSI-03, a domain profile of Proof of Stateful
   Integrity (PSI) for dispatch instructions and metered responses
   exchanged between a virtual power plant operator and its distributed
   energy resources.  Each record is sealed as a PSI receipt so that
   later alteration, reordering, or removal is detectable.  Only digests
   are sealed.  PSI-03 shows integrity and ordering only; it does not
   show that a resource performed as instructed, that metering is
   accurate, or that any market rule was met.

   Earlier revisions carried this title over an abstract describing
   practitioner identity bonds.  This revision makes the body match the
   title.
- **draft-watts-authorization-noncollapse-semantics-00** (new-draft, score 3, authorization) [none]: [Non-Collapse Semantics for Authorization, Evidence, and Execution State](https://datatracker.ietf.org/doc/draft-watts-authorization-noncollapse-semantics/) — Distributed authorization systems frequently combine observations,
   policy evaluations, evidence records, authorization decisions, and
   execution receipts.  Treating these different objects as
   interchangeable can create fail-open behavior, stale-authority bugs,
   and false claims of completion.

   This document defines non-collapse semantics: explicit typed
   transitions between observation, evidence, authorization, and
   execution state; fail-closed treatment of missing or indeterminate
   premises; and comparison rules for determining when heterogeneous
   representations agree on a declared invariant.  The document is
   informational and defines no new wire protocol.
- **draft-watts-research-artifact-provenance-00** (new-draft, score 3, trust_infrastructure) [none]: [Research Artifact Provenance and Corrigible Scientific State](https://datatracker.ietf.org/doc/draft-watts-research-artifact-provenance/) — This document describes a protocol-neutral pattern for content-
   addressed research artifacts, append-only evidence history, explicit
   epistemic classes, and corrigible active scientific state.  It
   separates byte integrity from numerical correctness, empirical
   adequacy, mechanism identification, and release authority.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-research-intelligence-archive-00** (new-draft, score 3, trust_infrastructure) [none]: [Evidence-Bounded Research Intelligence Archives](https://datatracker.ietf.org/doc/draft-watts-research-intelligence-archive/) — This unsubmitted working draft defines an evidence-bounded archive
   profile for scientific and technical claims, sources, evidence tiers,
   falsifiers, tests, provenance, publication state, and integrity
   manifests.  The profile is designed to prevent archival or mechanical
   integrity from being misread as empirical validity, novelty, peer
   review, standards approval, or publication acceptance.  This file is
   an archival RFCXML working draft and has no IETF standing unless
   separately submitted.
- **draft-watts-unison-state-preservation-00** (new-draft, score 3, trust_infrastructure) [none]: [State-Preserving Exchange of Evaluation Evidence](https://datatracker.ietf.org/doc/draft-watts-unison-state-preservation/) — This unsubmitted working draft describes state-preservation semantics
   derived from UNISON-StateBench.  It separates value, epistemic
   status, provenance, and authority; defines a non-collapse rule for
   operational and epistemic transitions; and describes representation,
   contradiction, missing-evidence, authority, principal-isolation,
   tool-state, context-distance, and controlled-mutation evaluation
   families.  This file is an archival RFCXML working draft and is not
   an IETF submission.
- **draft-watts-veriflow-evidence-envelope-00** (new-draft, score 3, trust_infrastructure) [none]: [Veriflow Evidence Envelope for Source-Grounded Computational Claims](https://datatracker.ietf.org/doc/draft-watts-veriflow-evidence-envelope/) — This document specifies an experimental, JSON-based evidence envelope
   for exchanging source-grounded computational assertions, including
   provenance, reproducible operation identifiers, evidence sufficiency,
   and explicit abstention when an answer is not supported.  The
   envelope separates syntactic validity, source integrity, mathematical
   correctness, and empirical truth.  This document does not standardize
   a general scientific inference engine or claim experimental
   superiority.
- **draft-westphal-lsr-isis-database-checksumming-01** (new-draft, score 3, adjacent_watchlist) [none]: [IS-IS Database Fingerprinting](https://datatracker.ietf.org/doc/draft-westphal-lsr-isis-database-checksumming/) — In large IS-IS networks it is useful to quickly verify whether the
   link-state databases on all routers have synchronized properly and to
   derive a rough metric of flooding diffusion behavior.  This document
   proposes a lightweight database fingerprinting mechanism for IS-IS
   along with YANG model extensions providing easy access to such
   information.  For fast verification against a peer, an optional TLV
   carrying the database fingerprint is defined for inclusion in IIH and
   CSNP PDUs.
- **draft-wu-idr-flowspec-yang-cfg-03** (new-draft, score 3, adjacent_watchlist) [idr]: [A YANG Data Model for Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-yang-cfg/) — This document defines a YANG data model for Flow Specification
   implementations.  The data model includes configuration data and
   state data.
- **draft-zehavi-oauth-audience-bound-token-exchange-00** (new-draft, score 3, authorization) [none]: [OAuth 2.0 Audience-Bound Token Exchange](https://datatracker.ietf.org/doc/draft-zehavi-oauth-audience-bound-token-exchange/) — In deployments where resource servers are invoked using access tokens
   with a restricted audience, resource servers that need to call
   downstream services must first exchange received tokens so their
   audience is appropriate for the downstream service.
- **draft-besleaga-agentic-knowledge-wellknown-01** (new-draft, score 2, ignored_after_review) [none]: [The 'knowledge-linkset' Well-Known URI for Publishing Knowledge Artefacts](https://datatracker.ietf.org/doc/draft-besleaga-agentic-knowledge-wellknown/) — This document defines the "knowledge-linkset" well-known URI, at
   which a web origin publishes one link set describing the knowledge
   artefacts it makes available: graph serializations, a JSON-LD
   context, an agent-facing text file, a chunk export, a change ledger,
   and related resources.  Each artefact link may carry a SHA-256
   digest, expressed with the syntax of HTTP digest fields, so that a
   client can check that a retrieved artefact is the one the publisher
   described.  A profile URI identifies the conventions the link set
   follows.  The mechanism defines no new media type and no new link
   relation type: a page points at the resource with the existing
   "describedby" relation.  The profile URI is registered in the IANA
   "Profile URIs" registry.  This document requests no IANA action.
- **draft-calabria-bmwg-ai-fabric-inference-bench-05** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-calabria-bmwg-ai-fabric-terminology-05** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
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
- **draft-dcn-cats-req-service-segmentation-05** (new-draft, score 2, ignored_after_review) [none]: [Additional CATS requirements consideration for Service Segmentation-related use cases](https://datatracker.ietf.org/doc/draft-dcn-cats-req-service-segmentation/) — This document discusses possible additional CATS requirements when
   considering service segmentation in related CATS use cases such as
   AR-VR and Distributed AI Inference
- **draft-gravit-gevp-09** (new-draft, score 2, ignored_after_review) [none]: [Gravit Epistemic Verification Protocol (GEVP)](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — The Gravit Epistemic Verification Protocol (GEVP) defines how signed
   evidence Records about an Artifact are screened, grouped by
   independent source and evaluated, so that a claim is never promoted
   beyond what independent evidence supports.  It specifies the
   Epistemic State Machine, the Record format and its signature, the
   meaning of the signed result of a Record, a verifier registry
   accepted under a threshold of root keys, a content-addressed Decision
   Record that anyone can reproduce, and optional signed receipts that
   let an auditor check a history of decisions offline.  It maps these
   states to the evidence taxonomy of the Gravit Verifiable Epistemic
   Decision Standard (VEDS).
- **draft-ietf-idr-fare-00** (new-draft, score 2, adjacent_watchlist) [idr]: [Fully Adaptive Routing Ethernet using BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-fare/) — Large language models (LLMs) like ChatGPT have become increasingly
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
- **draft-ietf-savnet-inter-domain-architecture-04** (new-draft, score 2, ignored_after_review) [savnet]: [Inter-domain Source Address Validation (SAVNET) Architecture](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/) — This document specifies an architecture for inter-domain source
   address validation (SAV).  The architecture provides a common
   framework for collecting SAV-specific and SAV-related information
   from multiple sources, determining the legitimate incoming directions
   of source prefixes, and using this information to generate SAV table
   for inter-domain SAV.  A SAV agent maintains the collected
   information in a SAV Information Base (SIB), and the SAV Information
   Base Manager (SIM) uses the available information to determine the
   corresponding prefix and legitimate incoming-direction mappings and
   generate or update the SAV table.  This document also defines the
   architectural components and communication framework of inter-domain
   SAV, and discusses deployment, operation, convergence, manageability,
   security, and privacy considerations.  It does not define a specific
   SAV protocol, protocol extension, or SAV table generation algorithm.
- **draft-kazuho-quic-delegated-stateless-reset-00** (new-draft, score 2, ignored_after_review) [none]: [Delegating QUIC Stateless Resets](https://datatracker.ietf.org/doc/draft-kazuho-quic-delegated-stateless-reset/) — This document specifies how a QUIC endpoint may delegate the emission
   of Stateless Resets to a component that outlives the QUIC stack --
   for example, an operating system that resets the peers of an
   application that has exited.  As such delegation is most useful on
   the client side, where endpoints often use zero-length Connection
   IDs, this document also defines a transport parameter and a frame
   that allow those clients to advertise a Stateless Reset Token.
- **draft-morrison-live-reference-resolution-01** (new-draft, score 2, ignored_after_review) [none]: [Live Reference Resolution for Autonomous Agent Beliefs](https://datatracker.ietf.org/doc/draft-morrison-live-reference-resolution/) — A recurring class of autonomous-agent failure arises when an agent
   acts on a belief read from a cached, derived, or proxy copy that has
   silently diverged from the authority the belief claims to represent.
   This document describes a reference-resolution discipline for the
   working beliefs an agent reasons and acts from.  Each belief is held
   as a reference to a single named lowest authority and is resolved
   live at the point of use, with verification.  When the authority is
   unobservable or the resolved value is stale, the belief takes an
   explicit uncertainty state rather than a prior cached value; that
   state propagates to any belief derived from it, and an uncertain
   belief feeding a costly or irreversible act blocks or escalates
   rather than proceeding.  Every resolution chain terminates in a
   single self-authorising root.  The document is Informational.  It
   records a discipline and a vocabulary; it does not define a wire
   protocol.
- **draft-song-cain-header-01** (new-draft, score 2, ignored_after_review) [none]: [Network Header Compression for Converged AI Network](https://datatracker.ietf.org/doc/draft-song-cain-header/) — We envision the scale-up, scale-out, and scale-across networks for AI
   computing would eventually converged.  The draft describes a scheme
   for L3 packet header compression in converged AI networks where IPv6
   are assumed to be the L3 protocol, and a unified fabric supports all
   kinds of traffic.  The header size can be reduced to 8 octets for
   packets transferred with a single super-node, representing 80%
   overhead saving.  The document discusses the motivation,
   requirements, benefits, and feasibility in addition to the header
   format proposal.
- **draft-templin-6man-mla-34** (new-draft, score 2, ignored_after_review) [none]: [IPv6 Addresses for Ad Hoc Networks](https://datatracker.ietf.org/doc/draft-templin-6man-mla/) — Ad Hoc networks present an IPv6 addressing challenge due to the
   undetermined neighborhood properties of their interfaces.  IPv6 nodes
   must assign locally-unique and topology-independent IPv6 addresses
   when topology-oriented IPv6 address delegation services are either
   absent or only intermittently available.  This document introduces a
   new IPv6 address type (termed the "Multilink Local Address (MLA)")
   that nodes can autonomously assign to interfaces to support Ad Hoc
   network operations.
- **draft-zhangb-cats-csma-implementation-01** (new-draft, score 2, ignored_after_review) [none]: [CATS Service Metric Agent (C-SMA) Functional Implementation](https://datatracker.ietf.org/doc/draft-zhangb-cats-csma-implementation/) — The Computing-Aware Traffic Steering (CATS) framework defines the
   CATS Service Metric Agent (C-SMA) as the functional entity
   responsible for collecting service capabilities and status, and
   reporting them to CATS Path Selectors (C-PSes).  While the framework
   and the CATS metric documents define the components and the metrics,
   the concrete observable behavior of the C-SMA - in particular, how it
   validates and sanitizes the metrics it collects, how it manages soft-
   state for stale or failing Service Contact Instances (SCIs), and how
   it synchronizes with the C-PS - remains underspecified.

   This document fills that gap.  It specifies the functional behavior
   of the C-SMA in terms of observable behavior and reporting semantics:
   how the C-SMA collects metric reports from SCIs (as specified in
   [I-D.zhangb-cats-sci-implementation]); how it validates and sanitizes
   these reports to prevent erroneous or malicious data from influencing
   traffic steering; how it manages a local metric cache with soft-state
   aging; how it enforces local policies and update control policies;
   and how it synchronizes with the C-PS, including recovery and
   reconciliation.  A decomposition of the C-SMA into internal
   functional components is provided as illustrative implementation
   guidance, not as a mandated software architecture.

   This document complements [RFC10053],
   [I-D.ietf-cats-metric-definition-13],
   [I-D.zhangb-cats-service-metrics-op], and
   [I-D.zhangb-cats-sci-implementation] by providing the operational
   execution layer for the C-SMA within the unified CATS architecture.
- **draft-dikshit-netmod-comparability-scope-extension-02** (new-draft, score 1, authorization) [none]: [A YANG Extension for Declaring the Comparability Scope of Operational State](https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/) — Several YANG modules currently in progress across multiple IETF
   working groups define counters, gauges, and other measured values
   that are exported from a network element and compared, summed, or
   averaged by a remote collector, either against the same node's
   history or against values from a different node. YANG (RFC 7950)
   has no first-class, machine-checkable way to state the
   administrative or topological domain within which two occurrences
   of such a value are comparable, so this determination is
   currently made, inconsistently or not at all, in prose. This
   document defines a YANG extension statement,
   "csc:comparability-scope", a four-value scope lattice, and a
   compatibility rule that lets a schema-aware tool statically
   detect an illegal aggregation across incomparable scopes, without
   waiting for it to happen at a collector. A related but distinct
   axis, the measurement window or method over which a rate or
   average value was computed, is identified as a further gap this
   document's mechanism does not itself close, and is reported
   separately as a candidate for future work.

## Ignored after review

- **draft-aklpdw-dnsop-zonemd-incremental-00** (new-draft, score 0, ignored_after_review) [none]: [The MERKLE3 Incremental Scheme for ZONEMD](https://datatracker.ietf.org/doc/draft-aklpdw-dnsop-zonemd-incremental/) — The ZONEMD Resource Record affirms the integrity of whole DNS zones
   and helps verify their authenticity.  It embeds a cryptographic hash
   of the zone data, collated in a configurable way.  It is used as a
   checksum for zone transfers between name servers.

   [RFC8976] defined a single ZONEMD collation scheme, SIMPLE.  It is
   sufficient for small and infrequently updated zones.  This document
   introduces the MERKLE3 scheme, targeting large, dynamic zones.  It
   uses a Merkle tree to enable parallelism and incremental computation.
- **draft-ali-pce-sr-policy-msd-consideration-02** (new-draft, score 0, ignored_after_review) [none]: [MSD Consideration in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-ali-pce-sr-policy-msd-consideration/) — Segment Routing (SR) allows a node to steer a packet flow along any
   path.  SR Policy is an ordered list of segments (i.e., instructions)
   that represent a source-routed policy.  The packets steered into an
   SR Policy carry an ordered list of segments associated with that SR
   Policy.  An SR Policy can be instantiated SR-MPLS and SRv6 data
   planes.

   Maximum SID Depth (MSD) is first introduced for SR-MPLS to indicate
   the number of SIDs supported by a node or a link on a node.  This
   concept is further extended for SRv6 with more types of MSD.  MSD may
   become one of the limitations that need to be considered when
   computing an SR-TE path for PCE.

   This draft specifies some MSD considerations PCE needs to take into
   account when computing an SR-TE path.
- **draft-besleaga-sustainability-wellknown-08** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI, at
   which a web origin publishes one JSON document declaring the energy
   consumption, carbon footprint, and related environmental metrics of a
   subject, typically the origin itself.  The declaration has a fixed
   path and formal schemas.  It links to a methodology, and may carry an
   embedded signature, name the declarations of upstream providers, and
   link to third-party attestations.  The metrics are self-asserted
   claims of the publisher.  This document registers the well-known URI
   and the media type application/sustainability-data+json.
- **draft-bonnell-lamps-pem-label-registry-00** (new-draft, score 0, ignored_after_review) [none]: [An IANA Registry for PEM Labels](https://datatracker.ietf.org/doc/draft-bonnell-lamps-pem-label-registry/) — RFC 7468 describes the textual encodings, commonly known as "PEM", of
   several PKIX, PKCS, and CMS structures, each identified by a label
   such as CERTIFICATE.  No registry of these labels exists, which has
   led to discoverability issues and inconsistent use.  This document
   establishes an IANA registry for PEM labels and defines the OCSP
   RESPONSE label.
- **draft-burleigh-dtn-multicast-00** (new-draft, score 0, ignored_after_review) [none]: [Bundle Multicast](https://datatracker.ietf.org/doc/draft-burleigh-dtn-multicast/) — This document describes Bundle Multicast, a protocol that reduces
   network resource consumption in the forwarding of copies of a given
   Bundle Protocol (BP) data unit - a "bundle" - to all BP nodes that
   are members of a BP endpoint whose ID is formed in the "imc" URI
   scheme, here termed a BP "multicast group".
- **draft-carpenter-anima-distro-00** (new-draft, score 0, ignored_after_review) [none]: [Distribution and Subscription using GRASP](https://datatracker.ietf.org/doc/draft-carpenter-anima-distro/) — This document describes an approach to information distribution and
   subscription using GRASP.  Rather than extending the GRASP protocol
   itself, it uses existing GRASP mechanisms to build a distribution and
   subscription mechanism on top.
- **draft-carpenter-anima-mqtt-00** (new-draft, score 0, ignored_after_review) [none]: [Publish/Subscribe Telemetry for Autonomic Networks](https://datatracker.ietf.org/doc/draft-carpenter-anima-mqtt/) — This document describes how devices authorized to join an autonomic
   control plane as defined in RFC 8994 may use the OASIS MQTT Publish/
   Subscribe Telemetry mechanism to share arbitrary information.  An
   MQTT message broker is required for this process and may be announced
   by the GRASP (RFC 8990) flooding mechanism.
- **draft-cui-idr-content-filter-flowspec-05** (new-draft, score 0, ignored_after_review) [idr]: [Packet Content Filter for BGP FlowSpec](https://datatracker.ietf.org/doc/draft-cui-idr-content-filter-flowspec/) — The BGP FlowSpec mechanism enables the distribution of traffic filter
   policies (traffic filters and actions) via BGP, facilitating DDoS
   traffic filtering.  The IP filter components defined for FSv1 and the
   FSv2 IP Basic Filter Families primarily match fields in the IP and
   transport-layer headers, which may not adequately address volumetric
   DDoS attack traffic characterized by fixed patterns within the packet
   content.  This document defines a Packet Content Filter Component for
   FSv1 and FSv2.  The match is encoded using OType, Offset, Content
   Length, Content, and Mask fields in the FlowSpec NLRI.  The FSv1
   encoding additionally carries a PType field.  This new component aims
   to leverage network devices such as routers and switches to support
   controlled traffic handling, traffic optimization, and mitigation of
   simple volumetric DDoS attacks, reducing the overall processing cost
   of carrier networks.
- **draft-dcn-dmm-cats-mup-service-segmentation-01** (new-draft, score 0, ignored_after_review) [none]: [Service Segmentation Considerations for CATS-MUP](https://datatracker.ietf.org/doc/draft-dcn-dmm-cats-mup-service-segmentation/) — Service segmentation introduces an emerging deployment paradigm in
   which a service is composed of multiple distributed subtasks forming
   a service pipeline.  This document discusses architectural
   considerations for steering sessions across multiple subtask
   instances in sequential, parallel, and iterative service pipelines,
   including a MUP Sequence Session Transform to support ordered
   traversal, and for maintaining service continuity during pipeline
   updates, particularly when stateful subtasks are involved.
- **draft-deshpande-secevent-http-multi-set-push-05** (new-draft, score 0, ignored_after_review) [sec]: [Push-Based Delivery For Multiple Security Event Tokens (SET) Using HTTP](https://datatracker.ietf.org/doc/draft-deshpande-secevent-http-multi-set-push/) — This specification defines how multiple Security Event Tokens (SETs)
   can be delivered to an intended recipient using HTTP POST over TLS.
   The SETs are transmitted in the body of an HTTP POST request to an
   endpoint operated by the recipient, and the recipient indicates
   successful or failed transmission via the HTTP response.
- **draft-dreibholz-ipv4-flowlabel-44** (new-draft, score 0, ignored_after_review) [none]: [An IPv4 Flowlabel Option](https://datatracker.ietf.org/doc/draft-dreibholz-ipv4-flowlabel/) — This draft defines an IPv4 option containing a flowlabel that is
   compatible with IPv6.  It is required for simplified usage of IntServ
   and interoperability with IPv6.
- **draft-dsmullen-ppd-protocol-04** (new-draft, score 0, ignored_after_review) [none]: [Privacy Preference Declaration Protocol Specification](https://datatracker.ietf.org/doc/draft-dsmullen-ppd-protocol/) — This document specifies a participant-facing protocol for Privacy
   Preference Declarations (PPDs) in home networks.  The protocol is
   between a home-side PPD service endpoint and a device-side actor,
   formally the PPD participant, which is a device or a service acting
   on behalf of a device.  It defines baseline operations for endpoint
   metadata confirmation, participant registration, optional participant
   declaration, effective-policy retrieval, policy acknowledgment,
   renewal, and reassociation.  This document complements the PPD
   architecture and taxonomy documents by defining the message and
   sequencing behavior needed for interoperable policy signaling.  The
   household policy instances carried by this protocol express privacy
   preferences for signaling and comparison; they do not by themselves
   define an enforcement mechanism that guarantees participant behavior.
- **draft-dulaunoy-rifp-02** (new-draft, score 0, ignored_after_review) [none]: [Radio Image Framing Protocol (RIFP)](https://datatracker.ietf.org/doc/draft-dulaunoy-rifp/) — This document specifies the Radio Image Framing Protocol (RIFP), a
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
- **draft-dutta-gcmf-02** (new-draft, score 0, ignored_after_review) [none]: [General-Purpose Compression via Mathematical Functions (GCMF)](https://datatracker.ietf.org/doc/draft-dutta-gcmf/) — This document specifies General-Purpose Compression via Mathematical
   Functions (GCMF), a lossless compression format that represents
   sequences of data using mathematical functions and associated
   parameters.

   GCMF attempts to represent a sequence using a compact mathematical
   representation rather than storing every value explicitly.  This
   document defines the GCMF data format, function types, encoding
   rules, decoding procedure, and interoperability requirements.
- **draft-eastlake-dnsop-svcb-rr-tunnel-10** (new-draft, score 0, ignored_after_review) [none]: [A Domain Name System (DNS) Service Parameter and Resource Record for Tunneling Information](https://datatracker.ietf.org/doc/draft-eastlake-dnsop-svcb-rr-tunnel/) — A Domain Name System (DNS) Service Binding (SVCB) Service Parameter
   Type and a DNS Resource Record (RR) Type are specified for storing
   connection tunneling / encapsulation information in the DNS.
- **draft-faltstrom-unicode-18** (new-draft, score 0, ignored_after_review): [draft-faltstrom-unicode-18-04](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/)
- **draft-faltstrom-unicode-18-04** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Domain Names for Applications 2008 (IDNA2008) and Unicode 18.0.0](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/) — This document describes the changes between Unicode 12.0.0 and
   Unicode 18.0.0 in the context of IDNA2008.  Some additions and
   changes have been made in the Unicode Standard that affect the values
   produced by the algorithm IDNA2008 specifies.  The review identifies
   certain newly added code points that are to be examined individually,
   and asks that they be identified as "UNDER REVIEW" in the IANA tables
   until that examination is done, as RFC 8753 provides.  This document
   provides the necessary table to IANA to make its database consistent
   with Unicode 18.0.0.

   All values in this document are computed from the released Unicode
   Character Database files listed in Appendix H, by applying the
   algorithm in RFC 5892 Section 3 directly to those files.  No derived
   property table produced by anyone else is used as input.  Section 3
   describes the derivation and Appendix G compares the result with the
   derivation published by the Unicode Consortium.
- **draft-gallagher-openpgp-messages-01** (new-draft, score 0, ignored_after_review) [none]: [OpenPGP Message Grammar](https://datatracker.ietf.org/doc/draft-gallagher-openpgp-messages/) — This document specifies several updates and clarifications to the
   grammar and semantics of OpenPGP messages.
- **draft-gandhi-pce-pm-15** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Performance Measurement for SR-TE and MPLS-TE LSPs with Stateful PCE](https://datatracker.ietf.org/doc/draft-gandhi-pce-pm/) — In certain networks, network performance data such as packet loss,
   delay, and delay variation, as well as bandwidth utilization, are
   critical measures for Traffic Engineering (TE).  These data provide
   operators with the characteristics of their networks for the
   performance evaluation required to provide Service-Level Agreements
   (SLAs).

   Stateful Path Computation Element Communication Protocol (PCEP)
   extensions have been defined for TE LSPs for Segment Routing (SR) and
   RSVP.  This document specifies PCEP extensions that enable and notify
   end-to-end performance measurements, including liveness detection,
   for PCE-Initiated and PCC-Initiated LSPs.  The extensions apply to
   SR-TE in the MPLS and IPv6 data planes and to MPLS-TE using RSVP,
   with notification to an Active Stateful PCE.
- **draft-geng-cats-yang-p4-consistency-00** (new-draft, score 0, ignored_after_review) [none]: [YANG-to-P4 Configuration Mapping and Update Consistency](https://datatracker.ietf.org/doc/draft-geng-cats-yang-p4-consistency/) — A YANG configuration can express management intent, but its
   acceptance does not establish that dependent entries in a
   programmable forwarding pipeline have become effective consistently.
   This document proposes an experimental mapping and update profile for
   P4.  It describes a target-specific mapping contract, capability
   validation, generation-based activation, preservation of existing
   flow bindings, failure recovery, and operational reconciliation.  The
   profile distinguishes configuration acceptance, verified activation,
   and eventual convergence.  It defines neither a new packet
   encapsulation nor a new YANG module, and does not assume a network-
   wide atomic transaction.
- **draft-geng-idr-flowspec-sav-08** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification for Source Address Validation](https://datatracker.ietf.org/doc/draft-geng-idr-flowspec-sav/) — BGP FlowSpec reuses BGP route to distribute infrastructure and
   propagates traffic flow information with filtering actions.  This
   document proposes some extensions to BGP FlowSpec for disseminating
   SAV rules.
- **draft-gerke-publication-process-reform-12** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   The deterministic state-integrity constraints and automated
   milestones defined herein apply programmatically across the core
   processing streams already defined or established in the future.

   This document updates RFC 6359 and RFC 7841.
- **draft-gregoire-moq-msfts-02** (new-draft, score 0, ignored_after_review) [none]: [MPEG-2 Transport Stream Packaging for MOQT](https://datatracker.ietf.org/doc/draft-gregoire-moq-msfts/) — This document extends the MOQT Streaming Format (MSF) with the
   "mpeg2ts" packaging, which carries the packets of an MPEG-2 Transport
   Stream over MOQT.  It defines the catalog fields that describe such a
   track, and the rules that a publisher and a subscriber follow to
   carry the packet stream.
- **draft-gurel-moq-probing-00** (new-draft, score 0, ignored_after_review) [none]: [Probe Tracks for Bandwidth Estimation in Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-gurel-moq-probing/) — This document defines probe tracks for Media over QUIC Transport
   (MOQT): tracks of synthetic objects, generated on demand, that
   measure the bandwidth of a single hop.  Probe tracks live under
   reserved, session-scoped Track Namespaces and are never forwarded or
   cached.  The track name selects the shape of the probe: target
   bitrate, duration or size, object rate, object size, group structure
   and key-object bursts.  For a downlink probe, a subscriber subscribes
   to a probe track in the namespace (.session, .probe), and the relay
   generates it, so the subscriber can measure whether a higher bitrate
   is sustainable on the relay-to-subscriber hop before it switches to a
   higher-quality track.  For an uplink probe, a publisher generates a
   probe track and publishes it to its relay in the namespace (.session,
   .sink), to measure the publisher-to-relay hop.
- **draft-haynes-nfsv4-recalldevice-03** (new-draft, score 0, ignored_after_review) [nfsv4]: [Deviceid-Scoped Layout Recall for NFSv4.2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-recalldevice/) — The Parallel Network File System (pNFS) allows the metadata server to
   recall a layout from a client by file id, by file system id, or
   across all of a client's layouts.  It also lets the server delete a
   deviceid via CB_NOTIFY_DEVICEID.  It does not provide a mechanism for
   the metadata server to recall, in a single operation, all layouts
   that reference a specific deviceid.  This document presents an
   extension to RFC7862 that adds a deviceid-scoped layout recall: a
   single CB_LAYOUTRECALL operation recalls every layout a client holds
   that references a given deviceid, leaving unrelated layouts in place.
   Without this capability, device unavailability can trigger large
   volumes of failed WRITE and LAYOUTERROR traffic, and administrators
   lack a surgical way to retire a deviceid without disturbing layouts
   that reference healthy devices.
- **draft-he-rtgwg-sr-ca-00** (new-draft, score 0, ignored_after_review) [none]: [Congestion Avoidance Using Segment Routing](https://datatracker.ietf.org/doc/draft-he-rtgwg-sr-ca/) — This document describes a generic solution of congestion avoidance,
   which is aimed at providing local link congestion avoidance within
   the Segment Routing (SR) framework.  Based on the concept of Topology
   Independent Loop-Free Alternate (TI- LFA) Fast Reroute (FRR), the
   selected shortest path can bypass the congested link while avoiding
   the formation of micro-loops.  The advantage of this solution is that
   it does not require any protocol extension.
- **draft-housley-asn1-layman-guide-04** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-ietf-6man-loopback-01** (new-draft, score 0, ignored_after_review) [6man]: [The IPv6 Loopback Address Prefix](https://datatracker.ietf.org/doc/draft-ietf-6man-loopback/) — This document updates the IP Version 6 Address Architecture to expand
   the size of the IPv6 loopback space from a single address to a /48
   prefix, formally defined as Node-Local Unicast space.

   This change allows for a much larger number of loopback addresses and
   internal virtual networks within an IPv6 host, which can be used for
   inter-process communication, local virtualization, container
   networking, and diagnostics.

   This document updates RFC 4291 to define the prefix and its
   functional semantics, and updates RFC 4007 to specify how the prefix
   is integrated into the scoped address architecture.

   It also updates the IANA IPv6 Address registry, the IPv6 Special-
   Purpose Address registry, and the Locally-Served DNS Zone Registry.
- **draft-ietf-bmwg-containerized-infra-10** (new-draft, score 0, ignored_after_review) [bmwg]: [Considerations for Benchmarking Network Performance in Containerized Infrastructures](https://datatracker.ietf.org/doc/draft-ietf-bmwg-containerized-infra/) — Recently, the Benchmarking Methodology Working Group extended the
   laboratory characterization from physical network functions (PNFs) to
   virtual network functions (VNFs).  With the ongoing shift in network
   function implementation from virtual machine-based to container-based
   approaches, system configurations and deployment scenarios for
   benchmarking will be partially influenced by how resource allocation
   and network technologies are specified for containerized network
   functions.  This draft outlines additional considerations for
   benchmarking network performance when network functions are
   containerized and executed on general-purpose hardware.
- **draft-ietf-bmwg-sr-bench-meth-10** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR) Forwarding](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) forwarding performance for Segment Routing over IPv6 (SRv6) and
   MPLS (SR-MPLS).
- **draft-ietf-dtn-bp-sand-05** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol (BP) Secure Advertisement and Neighborhood Discovery (SAND)](https://datatracker.ietf.org/doc/draft-ietf-dtn-bp-sand/) — This document defines the Secure Advertisement and Neighborhood
   Discovery (SAND) protocol for Bundle Protocol version 7 (BPv7) within
   a delay-tolerant network (DTN).  This protocol defines a general-
   purpose advertisement mechanism with an initial set of message and
   data types able to be advertised by participating nodes in a BPv7
   network.  The focus of this document is for advertisement to
   topological neighbors about local neighborhoods but can be expanded
   upon in the future through extension points.
- **draft-ietf-idr-bgp4-rfc4271bis-02** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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
- **draft-ietf-idr-rt-derived-community-12** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route Target derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route Target derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-idr-ts-flowspec-srv6-policy-19** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  It defines two modes of
   operation: transport steering into an SR Policy ("Mode 1"), in SR-
   MPLS and SRv6 networks, using BGP Extended Communities; and, in SRv6
   networks, transport steering combined with an egress service action
   at the egress node ("Mode 2"), signaled with the BGP Prefix-SID
   Attribute.
- **draft-ietf-ippm-connectivity-monitoring-14** (new-draft, score 0, ignored_after_review) [ippm]: [An Experimental Connectivity Monitoring Metric for IPPM](https://datatracker.ietf.org/doc/draft-ietf-ippm-connectivity-monitoring/) — Within a Segment Routing (SR) domain, segment routed measurement
   packets can be sent along pre-determined paths.  This enables new
   kinds of active measurements.  Connectivity monitoring supervises the
   state and performance of a connection or a (sub)path from central
   monitoring systems.  This document specifies an experimental Type-p
   connectivity monitoring metric to accomodate such operational needs.
- **draft-ietf-ippm-on-path-telemetry-yang-07** (new-draft, score 0, ignored_after_review) [ippm]: [On-Path Telemetry YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-ippm-on-path-telemetry-yang/) — This document defines two YANG data models for monitoring On-Path
   network performance information to be published in YANG
   notifications.  The Alternate-Marking Method and In-situ Operations,
   Administration, and Maintenance (IOAM) are the On-Path hybrid
   measurement methods considered in this document.
- **draft-ietf-ippm-stamp-ext-hdr-16** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect IPv4/IPv6 headers as well as IPv6
   extension headers for HBH and E2E active measurements, for example,
   using the IOAM data fields.
- **draft-ietf-jsonschema-json-schema-04** (new-draft, score 0, ignored_after_review) [jsonschema]: [JSON Schema](https://datatracker.ietf.org/doc/draft-ietf-jsonschema-json-schema/) — JSON Schema defines the media type "application/schema+json", a JSON-
   based format for describing the structure of JSON data.  A JSON
   Schema may assert constraints on a JSON value, ways to extract
   information from it, and how to interact with it.  The "application/
   schema-instance+json" media type provides additional feature-rich
   integration with "application/schema+json" beyond what can be offered
   for "application/json" documents.
- **draft-ietf-lisp-rfc6831bis-12** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC6831
- **draft-ietf-lsr-l2-bundle-member-remote-id-09** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  This document
   describes how Open Shortest Path First (OSPF) and Intermediate System
   to Intermediate System (IS-IS) would advertise the remote interface
   identifiers for L2 bundle members.  The corresponding extension of
   BGP Link State (BGP-LS) is also specified.
- **draft-ietf-mailmaint-aprf-00** (new-draft, score 0, ignored_after_review) [mailmaint]: [Aggregate Performance Reporting](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-aprf/) — Definition of an aggregate performance report format for email
   messaging, the means to discover target destinations, and a specified
   delivery method.
- **draft-ietf-mailmaint-smtputf8-syntax-06** (new-draft, score 0, ignored_after_review) [mailmaint]: [SMTPUTF8 Email Addresses](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-smtputf8-syntax/) — RFC 6532 extends the internet email format to allow UTF8 in many
   contexts.  This document updates RFC 6532 and restricts the set of
   allowed addresses in header fields slightly, and thereby simplifies
   use of these addresses.

   This is one of a pair of documents.  This one is simple to implement
   and contains only globally viable rules.  Its companion has more
   complex rules, takes regional usage into account, and describes
   addresses that can be read by some community and cut-and-pasted in
   some locale.
- **draft-ietf-manet-dlep-channel-utilization-05** (new-draft, score 0, ignored_after_review) [manet]: [DLEP Radio Channel Utilization Extension](https://datatracker.ietf.org/doc/draft-ietf-manet-dlep-channel-utilization/) — This document defines an extension to the Dynamic Link Exchange
   Protocol (DLEP) to provide the utilization of a radio channel.
- **draft-ietf-manet-dlep-radio-band-05** (new-draft, score 0, ignored_after_review) [manet]: [DLEP Radio Band Extension](https://datatracker.ietf.org/doc/draft-ietf-manet-dlep-radio-band/) — This document defines an extension to the Dynamic Link Exchange
   Protocol (DLEP) to provide information about frequency bands used by
   the radio.
- **draft-ietf-manet-dlep-radio-quality-05** (new-draft, score 0, ignored_after_review) [manet]: [DLEP Radio Quality Extension](https://datatracker.ietf.org/doc/draft-ietf-manet-dlep-radio-quality/) — This document defines an extension to the Dynamic Link Exchange
   Protocol (DLEP) to provide the quality of incoming radio signals.
- **draft-ietf-netconf-list-pagination-nc-13** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-nc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to NETCONF [RFC6241].

   This document updates [RFC6241], to augment the <get> and <get-
   config> "rpc" statements, and [RFC8526], to augment the <get-data>
   "rpc" statement, to define input parameters necessary for list
   pagination.
- **draft-ietf-netconf-list-pagination-rc-12** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-rc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to RESTCONF [RFC8040].

   This document updates RFC 8040, to declare "list" and "leaf-list" as
   valid resource targets for the RESTCONF GET operation, to define GET
   query parameters necessary for list pagination, and to define a
   media-type for XML-based lists.
- **draft-ietf-netconf-quic-client-server-09** (new-draft, score 0, ignored_after_review) [netconf]: [YANG Groupings for QUIC clients and QUIC servers](https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-client-server/) — This document defines five YANG 1.1 modules to support the
   configuration of QUIC clients and QUIC servers.  The modules include
   basic parameters for configuring QUIC based clients and servers as
   well as initial modules for the IANA registries "QUIC Versions" and
   "QUIC Transport Parameters".
- **draft-ietf-pce-entropy-label-position-10** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extension for SR-MPLS Entropy Label Positions](https://datatracker.ietf.org/doc/draft-ietf-pce-entropy-label-position/) — The Entropy label (EL) can be used in the SR-MPLS data plane to
   improve load-balancing and multiple Entropy Label Indicator (ELI)/EL
   pairs may be inserted in the SR-MPLS label stack as specified in
   RFC8662.

   This document defines a set of extensions for Path Computation
   Element Communication Protocol (PCEP) to indicate where in the label
   stack the ELI/EL pairs should be inserted in SR-MPLS network - the
   Entropy Label Positions (ELP).
- **draft-ietf-pim-ipv6-zeroconf-assignment-13** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the criteria listed in RFC 10019.
- **draft-ietf-pquip-pqc-hsm-constrained-07** (new-draft, score 0, ignored_after_review) [pquip]: [Adapting Constrained Devices for Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/) — This document provides guidance on integrating Post-Quantum
   Cryptography (PQC) into resource-constrained devices, such as IoT
   nodes and dedicated key-storage hardware.  These systems often
   operate with strict limitations on processing power, RAM, and flash
   memory, and may even be battery-powered.  The document emphasizes the
   role of hardware security as the basis for secure operations,
   supporting features such as seed-based key generation to minimize
   persistent storage, efficient handling of ephemeral keys, and the
   offloading of cryptographic tasks in low-resource environments.  It
   also explores the implications of PQC on firmware update mechanisms
   in such constrained systems.
- **draft-ietf-regext-epp-https-06** (new-draft, score 0, ignored_after_review) [regext]: [Extensible Provisioning Protocol (EPP) Transport over HTTPS](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-https/) — This document describes how an Extensible Provisioning Protocol (EPP)
   connection is mapped onto the Hypertext Transfer Protocol (HTTP).
   EPP over HTTP (EoH) requires the use of Transport Layer Security
   (TLS) to secure EPP information (i.e. HTTPS).
- **draft-ietf-regext-rdap-referrals-05** (new-draft, score 0, ignored_after_review) [regext]: [Explicit RDAP Redirects](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-referrals/) — This document describes an RDAP extension that allows RDAP clients to
   request to be redirected to a related RDAP record for a resource, and
   an RDAP extension that gives RDAP clients the ability to request no
   redirection in other scenarios.  This document also defines new link
   relations that can be used in redirect requests that can be used in
   query bootstrapping and navigating hierarchies, such as the
   hierarchies described in RFC 9910.
- **draft-ietf-regext-rdap-x-media-type-07** (new-draft, score 0, ignored_after_review) [regext]: [The "exts_list" Parameter for the RDAP Media Type](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-x-media-type/) — This document defines a new parameter for the RDAP media type that
   can be used to describe RDAP content with RDAP extensions.
   Additionally, this document describes the usage of this parameter
   with RDAP for the purposes of signalling RDAP extensions during
   content negotiation.
- **draft-ietf-rtgwg-srv6-egress-protection-26** (new-draft, score 0, ignored_after_review) [rtgwg]: [SRv6 Path Egress Protection](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-srv6-egress-protection/) — This document describes the mechanism and operational considerations
   for fast protecting the egress node and link of a Segment Routing for
   IPv6 (SRv6) path.  Topology Independent Loop-Free Alternate (TI-LFA)
   specifies fast protections for transit nodes and links of an SR path,
   but does not present protections for the egress node.  The solution
   uses a Mirror SID (End.M) behavior to steer traffic to a protector
   egress upon failure of the primary egress.  The Interior Gateway
   Protocol (IGP) (IS-IS/OSPFv3) extensions used to advertise the Mirror
   SID and protected locators are specified in
   [I-D.ietf-lsr-srv6-mirror-sid-igp-encoding]; they build on the IS-IS
   and OSPFv3 SRv6 extensions defined in [RFC9352] and [RFC9513].
- **draft-ietf-spring-resource-aware-segments-21** (new-draft, score 0, ignored_after_review) [spring]: [Introducing Resource Awareness to SR Segments](https://datatracker.ietf.org/doc/draft-ietf-spring-resource-aware-segments/) — This document describes a mechanism to allocate network resources to
   one or a set of Segment Routing Identifiers (SIDs).  Such SIDs are
   referred to as resource-aware SIDs.  The resource-aware SIDs retain
   their original forwarding semantics, with the additional semantics to
   identify the set of network resources available for the packet
   processing and forwarding action.  This mechanism is applicable to
   both segment routing with MPLS data plane (SR-MPLS) and segment
   routing with IPv6 data plane (SRv6).
- **draft-ietf-spring-sr-policy-flexible-cp-selection-02** (new-draft, score 0, ignored_after_review) [spring]: [Flexible Candidate Path Selection of SR Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-flexible-cp-selection/) — This document describes a flexible method for selecting candidate
   Segment Routing (SR) policy paths.  Based on the real-time resource
   usage and forwarding quality of candidate paths, the head node can
   perform dynamic path switching among multiple candidate paths in the
   SR policy.
- **draft-ietf-spring-srv6-security-18** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing over IPv6 (SRv6) Security Considerations](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/) — Segment Routing over IPv6 (SRv6) is the instantiation of Segment
   Routing on the IPv6 data plane, using IPv6 addresses to identify
   segments.  This document discusses security considerations in SRv6
   networks, including the potential threats and the possible mitigation
   methods.  The document does not define any new security protocols or
   extensions to existing protocols.
- **draft-ietf-spring-stamp-srpm-mpls-11** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as specified in RFC 8762,
   along with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths (including Segment Lists of SR-MPLS Policies, SR-MPLS
   IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo)
   paths), as well as Layer-3 and Layer-2 services carried over those
   paths.
- **draft-ietf-spring-stamp-srpm-srv6-08** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths (including Segment Lists of SRv6 Policies, SRv6
   IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths),
   as well as Layer-3 and Layer-2 services carried over those paths.
- **draft-ietf-teas-actn-pm-telemetry-autonomics-19** (new-draft, score 0, ignored_after_review) [teas]: [YANG models for Virtual Network (VN)/TE Performance Monitoring Telemetry and Scaling Intent Autonomics](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-pm-telemetry-autonomics/) — This document provides YANG data models that describe the performance
   monitoring parameters and scaling intent mechanisms for Traffic
   Engineering (TE) tunnels and Virtual Networks (VNs).

   The models presented in this document allow customers to subscribe to
   and monitor the key performance data of the TE-tunnel or the VN.  The
   models also provide customers with the ability to program autonomic
   scaling intent mechanisms on the level of TE-tunnel as well as VN.
- **draft-ietf-teas-power-steering-00** (new-draft, score 0, ignored_after_review) [teas]: [A Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-ietf-teas-power-steering/) — This document introduces a Power Conserving Path Placement Strategy
   (PCPPS).  During periods of low demand, PCPPS concentrates traffic
   onto a small set of network resources.  This causes other network
   resources to become idle or nearly idle.  When demand increases,
   PCPPS redistributes traffic as required.
- **draft-ietf-tsvwg-fq-pie-03** (new-draft, score 0, ignored_after_review) [tsvwg]: [Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/) — This document presents Flow Queue Proportional Integral controller
   Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue
   Management (AQM) algorithm to isolate flows and tackle the problem of
   bufferbloat.  FQ-PIE uses hashing to classify incoming packets into
   different queues and provide flow isolation.  Packets are dequeued by
   using a variant of the round robin scheduler.  Each such flow is
   managed by the PIE algorithm to maintain high link utilization while
   controlling the queue delay to a target value.
- **draft-ietf-v6ops-ipv6-app-testing-05** (new-draft, score 0, ignored_after_review) [v6ops]: [Testing Applications' IPv6 Support](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   software as a service providers on how to approach IPv6 testing in
   Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including "IPv6-
   only-strict" scenarios without any connectivity towards any relevant
   IPv4 endpoint.  It discusses common misconceptions about the degree
   to which operating systems and libraries can abstract IPv6 issues
   away and explains common regressions to avoid when deploying IPv6
   support.
- **draft-ietf-v6ops-ipv6-only-05** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
- **draft-ietf-wish-whep-05** (new-draft, score 0, ignored_after_review) [wish]: [WebRTC-HTTP Egress Protocol (WHEP)](https://datatracker.ietf.org/doc/draft-ietf-wish-whep/) — This document describes a simple HTTP-based protocol that will allow
   WebRTC-based viewers to watch content from streaming services,
   Content Delivery Networks (CDNs), or WebRTC Transmission Networks
   (WTNs).
- **draft-jabley-regext-allowable-dnssec-parameters-00** (new-draft, score 0, ignored_after_review) [none]: [Acceptance of DNSSEC Parameters in EPP](https://datatracker.ietf.org/doc/draft-jabley-regext-allowable-dnssec-parameters/) — The Extensible Provisioning Protocol (EPP) is used to submit DNSSEC
   parameters for domain names to domain name registries.  Registries
   and registrars often restrict the values they accept, and those
   restrictions vary from registry to registry.  The resulting
   uncertainty makes it difficult for DNS operators to adopt new
   algorithms.  This document recommends that registries and registrars
   base their acceptance policies on the IANA registries for DNSSEC
   algorithms and digest types.
- **draft-kafara-walled-private-network-00** (new-draft, score 0, ignored_after_review) [none]: [Walled Private Network (WPN) Service Definition](https://datatracker.ietf.org/doc/draft-kafara-walled-private-network/) — This document specifies Walled Private Network (WPN) as a technology-
   neutral profile for a private IP network or network service.  A
   conforming WPN has an explicitly defined address space, explicit
   membership, end-to-end preservation of member addresses without
   Network Address Translation between members, and protocol-transparent
   IP connectivity among authorized members.  A WPN does not provide
   general-purpose Internet egress as part of the WPN service.  The
   public Internet or another shared network may nevertheless be used as
   an underlay.  Networks located behind individual members are outside
   the base WPN service and may be interconnected by mechanisms
   configured independently by those members.  The purpose of this
   specification is to assign one unambiguous term to this complete set
   of service properties.  It does not define a new tunneling, routing,
   or cryptographic protocol, and use of a VPN or tunnel is not required
   for WPN conformance.
- **draft-kamga-http-aureonsql-00** (new-draft, score 0, ignored_after_review) [none]: [The AUREON Database-over-HTTP Protocol and Method Suite](https://datatracker.ietf.org/doc/draft-kamga-http-aureonsql/) — This document specifies AUREON, a high-performance database-over-HTTP
   protocol.  AUREON leverages HTTP's extensible method mechanism
   (RFC 9110) to introduce domain-aware custom tokens for relational
   database operations, Data Definition Language (DDL) governance,
   Data Control Language (DCL) permissions, and procedural Data Action
   Language (DAL) workflows.  Furthermore, this document defines the
   complete IANA registration templates for the AUREON method suite
   and media type parameters.
- **draft-kao-idr-bitwise-ip-filters-06** (new-draft, score 0, ignored_after_review) [idr]: [Bitwise IP Filters for BGP FlowSpec](https://datatracker.ietf.org/doc/draft-kao-idr-bitwise-ip-filters/) — This document introduces the bitwise match filter component for
   source and destination IPv4/IPv6 address fields.  These components
   enhance the BGP Flow Specification framework and provide a solution
   for dynamic symmetric traffic load-balancing.
- **draft-karstens-pim-multicast-snooping-optimization-02** (new-draft, score 0, ignored_after_review) [none]: [Multicast Snooping Optimizations](https://datatracker.ietf.org/doc/draft-karstens-pim-multicast-snooping-optimization/) — TODO: provide abstract
- **draft-kennedy-dnssd-data-block-02** (new-draft, score 0, ignored_after_review) [none]: [DNS-SD Data Block: An Encoding for Non-IP Transports](https://datatracker.ietf.org/doc/draft-kennedy-dnssd-data-block/) — The DNS-SD Data Block (DDB) is a compact, Type-Length-Value (TLV)
   encoded container for conveying DNS-Based Service Discovery (DNS-SD)
   service information over non-IP transports used by short-range peer-
   to-peer or proximity-based advertisement and discovery technologies,
   such as the Bluetooth Low Energy Transport Discovery Service or Near
   Field Communication (NFC) Verb NFC Data Exchange Format (NDEF)
   records.
- **draft-knodel-nomcom-gender-representation-06** (new-draft, score 0, ignored_after_review) [none]: [Gender Representation in the IETF Nominating Committees](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document extends the existing limit on nomcom representation by
   organization ([RFC8713], Section 4.17) so that not all voting members
   of the IETF Nominating Committee (nomcom) belong to the same gender.
   It guarantees up to five voting seats to volunteers who opt into a
   self-declared pool, and changes the selection only in years when a
   plain random draw would seat fewer.
- **draft-kompella-teas-mpte-04** (new-draft, score 0, ignored_after_review) [none]: [Multipath Traffic Engineering](https://datatracker.ietf.org/doc/draft-kompella-teas-mpte/) — Shortest path routing offers an easy-to-understand, easy-to-implement
   method of establishing loop-free connectivity in a network, but
   offers few other features.  Equal-cost multipath (ECMP), a simple
   extension, uses multiple equal-cost paths between any two points in a
   network: at any node in a path (really, Directed Acyclic Graph),
   traffic can be (typically equally) load-balanced among the next hops.
   ECMP is easy to add on to shortest path routing, and offers a few
   more features, such as resiliency and load distribution, but the
   feature set is still quite limited.

   Traffic Engineering (TE), on the other hand, offers a very rich
   toolkit for managing traffic flows and the paths they take in a
   network.  A TE network can have link attributes such as bandwidth,
   colors, risk groups and alternate metrics.  A TE path can use these
   attributes to include or avoid certain links, increase path
   diversity, manage bandwidth reservations, improve service experience,
   and offer protection paths.  However, TE typically doesn't offer
   multipathing as the tunnels used to implement TE usually take a
   single path.

   This memo proposes multipath traffic-engineering (MPTE), combining
   the best of ECMP and TE.  The multipathing proposed here need not be
   strictly equal-cost, allowing for some "slack" to admit more paths.
   The load balancing at each hop is optimally weighted to each next hop
   rather than always being equally weighted.  Moreover, traffic can
   enter and leave an MPTE construct via multiple ingresses and
   egresses.  The proposal includes several choices of control and data
   planes.
- **draft-li-idr-savnet-intra-domain-bgp-02** (new-draft, score 0, ignored_after_review) [none]: [Source Address Validation at Intra-domain Network Boundary Using BGP](https://datatracker.ietf.org/doc/draft-li-idr-savnet-intra-domain-bgp/) — This document proposes a solution for Source Address Validation (SAV)
   at the intra-domain network boundary using BGP.  Routers at the
   boundary automatically generate accurate SAV rules by using routing
   information and SAV-specific information.  These rules construct a
   validation boundary which checks the validity of the source address
   of any data packets flowing into the intra-domain network.  This
   document also introduces BGP extensions for communicating SAV-
   specific information among routers at the boundary.
- **draft-li-lsr-igp-based-intra-domain-savnet-06** (new-draft, score 0, ignored_after_review) [none]: [Source Address Validation at the Intra-domain Network Boundary Using IGP](https://datatracker.ietf.org/doc/draft-li-lsr-igp-based-intra-domain-savnet/) — SPA-based SAVNET is a new intra-domain source address validation
   (SAV) mechanism which requires exchanging and communicating SPA
   information among routers in an intra-domain network (see
   [I-D.li-savnet-source-prefix-advertisement]).  Routers at the
   boundary automatically generate accurate SAV rules by using routing
   information and SPA information.  These rules construct a validation
   boundary which checks the validity of the source address of any data
   packets flowing into the intra-domain network.  This document
   describes a method to implement SPA-based SAVNET by using OSPF and
   IS-IS.
- **draft-li-sidrops-stealthy-hijacking-03** (new-draft, score 0, ignored_after_review) [none]: [Risk of Stealthy BGP Hijacking under Incomplete Adoption of Route Origin Validation (ROV)](https://datatracker.ietf.org/doc/draft-li-sidrops-stealthy-hijacking/) — This document describes how incomplete adoption of Route Origin
   Validation (ROV) makes certain forms of BGP hijacking less visible on
   the control plane while still capable of diverting traffic.  We
   explain the underlying mechanism, define the form of the threat,
   analyze an real-world incident that exemplifies the issue, and
   discuss potential countermeasures to mitigate its impact.
- **draft-lin-idr-bgpls-te-policy-pm-10** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Advertisement of SR Policy Performance Metric](https://datatracker.ietf.org/doc/draft-lin-idr-bgpls-te-policy-pm/) — This document describes a way to advertise the performance metrics
   for Traffic Engineering (TE) Policy using BGP Link State (BGP-LS).
- **draft-lin-idr-flowspec-quic-01** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification for QUIC](https://datatracker.ietf.org/doc/draft-lin-idr-flowspec-quic/) — A BGP Flow Specification is an n-tuple consisting of several
   matching criteria that can be applied to IP traffic. This document
   defines how to perform Flow Specification traffic diversion based on
   the characteristics of QUIC packets.
- **draft-liu-idr-flowspec-ifit-05** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification Extensions to Enable In-situ Flow Information Telemetry (IFIT)](https://datatracker.ietf.org/doc/draft-liu-idr-flowspec-ifit/) — BGP Flowspec mechanism propogates both traffic Flow Specifications
   and Traffic Filtering Actions by making use of the Border Gateway
   Protocol Network Layer Reachability Information (BGP NLRI) and the
   BGP Extended Community encoding formats.  In order to address the
   automatic deployment of IPv4 unicast and VPNv4 unicast on-path flow
   telemetry as well as IPv6 families, this document specifies a new BGP
   Extended Community named IFIT Action Specific Extended Community to
   distribute In-situ Flow Information Telemetry (IFIT) actions.
- **draft-lls-onsen-yang-tmf-mapping-00** (new-draft, score 0, ignored_after_review) [none]: [Mapping YANG Schemas and Instance Data to TM Forum Data Models and APIs](https://datatracker.ietf.org/doc/draft-lls-onsen-yang-tmf-mapping/) — This document describes a mechanism for mapping between YANG schemas
   and instance data and TM Forum (TMF) Data Models and APIs.  The
   mapping mechanism enables orchestrators to produce and expose TMF
   compliant interfaces that provide TMF API consumers direct access to
   a YANG data store.

   Both a mechanism for the mapping of YANG schemas to TMF Catalog
   Specifications (i.e. TMF633/634) and a matching mechanism for the
   mapping of YANG instance data to TMF Order Management (i.e.
   TMF641/652) and Activation Management (i.e. TMF640/702) APIs are
   described.
- **draft-moskowitz-ipsecme-rfc7402-beet-update-04** (new-draft, score 0, ignored_after_review) [ipsecme]: [A Bound End-to-End Tunnel (BEET) mode for ESP](https://datatracker.ietf.org/doc/draft-moskowitz-ipsecme-rfc7402-beet-update/) — This document is an update to the Bound End-to-End Tunnel (BEET) mode
   for ESP in as described in [RFC7402].  It brings the description in
   alignment with the addition of BEET mode for IKEv2 without any
   processing changes as described in [RFC7402]
- **draft-nam-ksg-journal-export-01** (new-draft, score 0, ignored_after_review) [none]: [Keysingate Journal Export: Pages under a Portable Seal](https://datatracker.ietf.org/doc/draft-nam-ksg-journal-export/) — A Keysingate container keeps a work journal: pages without
   signatures, closed by one portable seal that covers every page before
   it and is moved forward by each new record.  This document specifies
   the journal's pages, records and seals, the two forms of a journal
   (unanchored and anchored), the two exports a third party receives --
   one page with its proof, or the whole journal once -- and how a
   verifier checks them without contacting anyone.  It also specifies a
   profile for anchoring seals in Solana with a blind memo that shows
   outsiders only the fact of a write.  The core documents, time format
   and anchor rule it relies on are those of draft-nam-ksg-core-00.
- **draft-pignataro-icmp-enviro-info-04** (new-draft, score 0, ignored_after_review) [none]: [ICMP Extensions for Environmental Information](https://datatracker.ietf.org/doc/draft-pignataro-icmp-enviro-info/) — This document defines a data structure that can be appended to
   selected ICMP messages.  The ICMP extension defined herein can be
   used to gain visibility into environmental information on the
   internet by providing per-hop (i.e., per topological network node)
   power metrics and other present or future metrics around
   environmental information.  This will contribute to achieving an
   objective mentioned in the report of the IAB E-Impact workshop.

   The techniques presented are useful not only in a transactional
   setting (e.g., a user-issued traceroute or a ping request), but also
   in a scheduled automated setting where they may be run periodically
   in a mesh across an administrative domain to map out environmental
   information.
- **draft-preussmattsson-tls-hqckem-00** (new-draft, score 0, ignored_after_review) [none]: [HQC-KEM Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-preussmattsson-tls-hqckem/) — This document defines nine quantum-resistant TLS 1.3 key exchange
   algorithms based on HQC-KEM, the code-based KEM selected by NIST for
   standardization in forthcoming FIPS 207.  Three use HQC-KEM
   standalone, two combine it with X25519 or X448 in PQ/T hybrids, two
   combine it with ML-KEM in PQ/PQ hybrids, and two combine it with ML-
   KEM and X25519 or X448 in PQ/PQ/T hybrids.  Because HQC-KEM relies on
   hardness assumptions and constructions different from those
   underlying lattice-based ML-KEM, these algorithms provide algorithmic
   diversity that can mitigate the impact of future cryptanalytic
   advances or implementation weaknesses in lattice-based cryptography.
   The algorithms are intended for TLS 1.3, DTLS 1.3, and QUIC, and the
   hybrid algorithms follow the general hybrid key exchange construction
   defined for TLS 1.3.
- **draft-preussmattsson-tls-mlkem1024-x448-01** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Hybrid ML-KEM-1024/X448 Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-preussmattsson-tls-mlkem1024-x448/) — This document defines a post-quantum/traditional hybrid key exchange
   algorithm for TLS 1.3 that combines ML-KEM-1024 with X448:
   MLKEM1024X448.  The algorithm provides a hybrid key exchange option
   targeting a higher security level than X25519MLKEM768, matching the
   security level of AES-256 and ChaCha20.  A large security margin can
   protect against future cryptanalytic advances, misuse, and
   implementation errors.  Compared with P-curves offering a similar
   security level, X448 is significantly faster and provides greater
   implementation robustness.  A FIPS-validated implementation of
   MLKEM1024X448 ensures that the ML-KEM-1024 component is FIPS-
   validated.  The algorithm defined in this document is intended for
   use with TLS 1.3, DTLS 1.3, and QUIC and follows the general hybrid
   key exchange construction defined for TLS 1.3.
- **draft-qwz-idr-nodeid-ec-00** (new-draft, score 0, ignored_after_review) [none]: [BGP node-ID EC extension](https://datatracker.ietf.org/doc/draft-qwz-idr-nodeid-ec/) — This document describes a new BGP extended community attribute for
   advertising the node-ID.
- **draft-reddy-hpke-hqc-01** (new-draft, score 0, ignored_after_review) [none]: [Hamming Quasi-Cyclic (HQC) Key Encapsulation Mechanisms for Hybrid Public Key Encryption (HPKE)](https://datatracker.ietf.org/doc/draft-reddy-hpke-hqc/) — This document specifies Hamming Quasi-Cyclic (HQC) key encapsulation
   mechanisms for use with Hybrid Public Key Encryption (HPKE).  It
   defines the HPKE KEM interface, deterministic key-pair derivation,
   public and private key encodings, and input validation for three HQC
   parameter sets.  It also defines three PQ/T hybrid KEMs that combine
   HQC with P-256, X25519, or P-384.  It requests six HPKE KEM algorithm
   identifiers and reuses the existing HPKE key schedule, encryption
   operations, and export interface.
- **draft-rsalz-4086bis-01** (new-draft, score 0, ignored_after_review) [none]: [On Random Numbers](https://datatracker.ietf.org/doc/draft-rsalz-4086bis/) — Things have changed a great deal in the two decades since RFC 4086,
   "Randomness Requirements for Security," was published.  Notably,
   facilities to generate high-quality random numbers are widely
   available on most common computing platforms.

   While RFC 4086 provides much information to those implementing such a
   facility, this document takes a different approach, encouraging
   implementors to use facilities already available to them.
- **draft-seemann-quic-nat-traversal-03** (new-draft, score 0, ignored_after_review) [none]: [Using QUIC to traverse NATs](https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/) — This document specifies a QUIC extension for traversing Network
   Address Translators (NATs).  Endpoints use an existing proxied QUIC
   connection to coordinate path validation attempts that create the NAT
   bindings needed for a direct path and test its connectivity.
   Application data can be exchanged over the proxied path while NAT
   traversal is in progress.  Once a suitable direct path has been
   validated, the connection can migrate to it.
- **draft-shen-idr-flowspec-traffic-compress-action-05** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow-Spec Traffic Compress Action](https://datatracker.ietf.org/doc/draft-shen-idr-flowspec-traffic-compress-action/) — BGP Flow Specification Version 2 (FSv2) provides an extensible
   framework for disseminating traffic flow specification rules and
   associated actions.  While traditional Flow-spec actions cover rate-
   limiting, redirecting, and marking, emerging applications require
   dynamic bandwidth optimization.  This document specifies a new
   traffic filtering action to support selective, on-demand traffic
   compression across network domains using BGP Extended Communities
   aligned with the FSv2 architecture.
- **draft-shyam-vlsmtrp-16** (new-draft, score 0, ignored_after_review) [none]: [VLSM Tree Routing Protocol](https://datatracker.ietf.org/doc/draft-shyam-vlsmtrp/) — This is a light weight routing protocol applicable inside a network
   that appears in the form of a tree and distribution of address space
   takes place with the approach of VLSM. It is based on setting default
   route inside VLSM tree.  With this approach, routing information of
   the external world need not be passed down to the VLSM tree. Thus,
   load inside a router gets reduced substantially.  This document
   includes IP-VPN with MPLS inside VLSM tree by extending RSVP-TE.
- **draft-sidor-pce-lsp-state-reporting-extensions-07** (new-draft, score 0, ignored_after_review) [none]: [LSP State Reporting Extensions in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-lsp-state-reporting-extensions/) — The Path Computation Element Communication Protocol (PCEP) is defined
   in multiple RFCs for enabling communication between Path Computation
   Elements (PCEs) and Path Computation Clients (PCCs).

   Although PCEP defines various Label Switched Path (LSP) identifiers,
   attributes, and constraints, there are operational attributes
   available on the PCC that can enhance path computation and improve
   the debugging experience, which are not currently supported in PCEP.

   This document defines extensions to PCEP to include:

   *  Support for explicit or dynamic path types
   *  Mechanisms to mark LSPs as eligible for use as transit LSPs
- **draft-singh-apex-psi-02** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-02-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-02/)
- **draft-singh-apex-psi-02-01** (new-draft, score 0, ignored_after_review) [none]: [PSI-02: Receipts for Carbon Sequestration Measurement Records](https://datatracker.ietf.org/doc/draft-singh-apex-psi-02/) — This document defines PSI-02, a domain profile of Proof of Stateful
   Integrity (PSI) for measurement records supporting carbon
   sequestration claims, such as field sampling results, remote-sensing
   extracts, and calculation inputs.  Each record is sealed as a PSI
   receipt so that later alteration, reordering, or removal is
   detectable.  Only digests are sealed.  PSI-02 shows integrity and
   ordering only; it does not show that the sequestration occurred, that
   a methodology was followed, or that any credit is valid.

   Revision 00 carried this title over an abstract describing
   disability-services evidence.  This revision makes the body match the
   title.
- **draft-singh-apex-psi-03** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-03-02](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/)
- **draft-singh-apex-psi-04** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-04-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-04/)
- **draft-singh-apex-psi-04-01** (new-draft, score 0, ignored_after_review) [none]: [PSI-04: State-Chain Receipts for Records Concerning Vulnerable Persons](https://datatracker.ietf.org/doc/draft-singh-apex-psi-04/) — This document defines PSI-04, a domain profile of Proof of Stateful
   Integrity (PSI) for records about vulnerable persons, such as
   clinical-trial participants and recipients of disability or aged care
   services.  PSI-04 seals each state transition of a record as a PSI
   receipt chained to the previous one, so that later alteration or
   omission of a transition is detectable.  Only digests are sealed; no
   personal data leaves the record holder.  PSI-04 shows integrity and
   ordering only and does not show that care was adequate or that any
   regulation was met.

   This revision withdraws the multi-party computation and zero-
   knowledge claims of revision 00 and the request for a URI scheme.
- **draft-singh-apex-psi-07** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-07-02](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/)
- **draft-singh-apex-psi-07-02** (new-draft, score 0, ignored_after_review) [none]: [PSI-07: Receipts for Organic Production Records](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/) — This document defines PSI-07, a domain profile of Proof of Stateful
   Integrity (PSI) for production records for organic certification,
   such as input purchases, field activities, and inspection notes.
   Each record is sealed as a PSI receipt so that later alteration,
   reordering, or removal is detectable.  Only digests are sealed.
   PSI-07 shows integrity and ordering only; it does not show that a
   product is organic or that any certification standard was met.

   Earlier revisions carried this title over an abstract describing
   regulatory monitoring signals.  This revision makes the body match
   the title.
- **draft-singh-apex-psi-08** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-08-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-08/)
- **draft-singh-apex-psi-08-01** (new-draft, score 0, ignored_after_review) [none]: [PSI-08: Receipts for Health Record Access Events](https://datatracker.ietf.org/doc/draft-singh-apex-psi-08/) — This document defines PSI-08, a domain profile of Proof of Stateful
   Integrity (PSI) for access events on health records, recording that
   an access occurred, by which role, and for what stated purpose.  Each
   record is sealed as a PSI receipt so that later alteration,
   reordering, or removal is detectable.  Only digests are sealed.
   PSI-08 shows integrity and ordering only; it does not show that an
   access was authorised, appropriate, or lawful.

   Revision 00 carried this title over an abstract describing predicate
   chains.  This revision makes the body match the title.
- **draft-singh-apex-psi-09** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-09-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-09/)
- **draft-singh-apex-psi-09-01** (new-draft, score 0, ignored_after_review) [none]: [PSI-09: Receipts for Age Assurance Decisions](https://datatracker.ietf.org/doc/draft-singh-apex-psi-09/) — This document defines PSI-09, a domain profile of Proof of Stateful
   Integrity (PSI) for decisions made by an age assurance provider,
   recording that a check was performed, by which method, and with what
   outcome.  Each record is sealed as a PSI receipt so that later
   alteration, reordering, or removal is detectable.  Only digests are
   sealed.  PSI-09 shows integrity and ordering only; it does not show
   the age of any person, the accuracy of the method, or compliance with
   any age assurance law.

   Revision 00 carried this title over an abstract describing tribunal
   verdicts.  That material is withdrawn and this revision makes the
   body match the title.
- **draft-singh-psi-02** (new-draft, score 0, ignored_after_review) [none]: [Proof of Stateful Integrity (PSI): Signed, Merkle-Committed Receipts for Digital Records](https://datatracker.ietf.org/doc/draft-singh-psi/) — This document specifies Proof of Stateful Integrity (PSI), a format
   and procedure for issuing signed receipts over digital records.  A
   PSI receipt binds the SHA-256 digest of a canonical JSON record to an
   issuer signature, a monotonic sequence number, and a Merkle tree root
   computed with the RFC 6962 hashing profile, and may reference an
   external timestamp anchor.  Any party holding the record, the
   receipt, and the issuer public key can verify the receipt offline.
   PSI provides evidence of integrity, origin, and ordering only.  It
   does not establish that a record is true, lawful, safe, or compliant
   with any regulation.

   This revision replaces revision 01.  It withdraws all claims of zero-
   knowledge proofs, multi-party computation, and inclusion proofs,
   which the reference implementation does not provide.
- **draft-singh-psi-age-assurance-01** (new-draft, score 0, ignored_after_review) [none]: [PSI Age Assurance Decision Receipts](https://datatracker.ietf.org/doc/draft-singh-psi-age-assurance/) — This document defines PSI-Age, a domain profile of Proof of Stateful
   Integrity (PSI) for age assurance decisions, so that a relying party
   can later show which provider decision it relied on.  This document
   is superseded in substance by draft-singh-apex-psi-09 and is retained
   only for continuity.  Each record is sealed as a PSI receipt so that
   later alteration, reordering, or removal is detectable.  Only digests
   are sealed.  PSI-Age shows integrity and ordering only; it does not
   show the age of any person, the accuracy of the method, or compliance
   with any age assurance law.

   The title of revision 00 claimed a zero-knowledge construction.  No
   zero-knowledge proof system is specified; the claim is withdrawn.
- **draft-singh-psi-http-00** (new-draft, score 0, ignored_after_review) [none]: [The Compliance-Receipt HTTP Response Header Field](https://datatracker.ietf.org/doc/draft-singh-psi-http/) — This document defines the Compliance-Receipt HTTP response header
   field, a Structured Field that carries a reference to a Proof of
   Stateful Integrity (PSI) receipt for the response.  The signature
   covers every security-relevant parameter.  The header shows that the
   issuer sealed a digest of the response; despite its name it does not
   show that the response, or the service, complies with any law or
   policy.
- **draft-singh-psi-merkle-01** (new-draft, score 0, ignored_after_review) [none]: [PSI Merkle Commitment Profile (RFC6962-SHA256)](https://datatracker.ietf.org/doc/draft-singh-psi-merkle/) — This document specifies the Merkle commitment profile used by Proof
   of Stateful Integrity (PSI) receipts.  It adopts the Merkle Tree Hash
   and inclusion proof of RFC 9162 without modification, fixes leaf
   order, and defines how a receipt declares the profile and how a
   verifier obtains and checks an inclusion proof.  A valid proof shows
   only that a leaf was committed under a root; it says nothing about
   the truth or lawfulness of the sealed content.

   This revision replaces the lexicographic ordering and odd-leaf
   duplication of revision 00, which were incompatible with RFC 9162,
   and withdraws all anchoring claims other than OpenTimestamps.
- **draft-spk-httpbis-parallel-upload-00** (new-draft, score 0, ignored_after_review) [none]: [Parallel Appends for Resumable Uploads](https://datatracker.ietf.org/doc/draft-spk-httpbis-parallel-upload/) — The resumable upload protocol lets a client continue an interrupted
   upload, but the upload has to be sent in order, one request at a
   time.  This document extends that protocol so that a client can send
   different parts of the same upload in parallel.  Servers and
   intermediaries can limit both the number of concurrent requests and
   the amount of data that arrives out of order.  The document also
   describes how intermediaries that inspect uploads (for data loss
   prevention or malware scanning, say) can continue to do so, and how
   the extension behaves over HTTP/1.1, HTTP/2, and HTTP/3.
- **draft-templin-6man-aero-omni-amen-17** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-ugur-moq-fast-switching-00** (new-draft, score 0, ignored_after_review) [none]: [Subscriber-Side Multi-Variant Fast Track Switching for MOQT](https://datatracker.ietf.org/doc/draft-ugur-moq-fast-switching/) — This document describes subscriber-side multi-variant fast track
   switching (MVFTS), a technique that allows a MOQ Transport (MOQT)
   subscriber to switch between tracks that are encoded at the same
   bitrate but use different group of pictures (GoP) lengths, combining
   the compression efficiency of a long GoP with the low switching delay
   of a short GoP.  A publisher using this technique packages each
   encoded bitrate as a ladder of tracks distinguished only by their
   keyframe interval, numbers those tracks' Group IDs so that they share
   a common alignment, and advertises the keyframe interval of each
   track in a MOQT Streaming Format (MSF) catalog.  A subscriber uses
   this information to compute the nearest valid switch point on any
   track in scope and to perform the switch using the SWITCH_FROM
   request parameter in soft mode.
- **draft-vos-cfrg-pqpake-03** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Post-Quantum Password Authenticated Key Exchange](https://datatracker.ietf.org/doc/draft-vos-cfrg-pqpake/) — This document describes four post-quantum password authenticated key
   exchange (PAKE) protocols: OQUAKE, OQUAKE+, CPaceOQUAKE, and
   CPaceOQUAKE+. OQUAKE and OQUAKE+ are standalone PAKEs that both offer
   security against a quantum-capable attacker.  OQUAKE is a symmetric
   PAKE, suitable for use cases where both parties share a view of the
   password.  OQUAKE+ is an augmented version of OQUAKE suitable for
   client-server settings where only one party (the client) knows the
   password.  CPaceOQUAKE is a hybrid PAKE that runs a classical PAKE
   (CPace) and OQUAKE sequentially, and CPaceOQUAKE+ is its augmented
   version.  This document also provides recommended configurations for
   each protocol.
- **draft-wang-idr-flowspec-dip-origin-as-filter-18** (new-draft, score 0, ignored_after_review) [idr]: [Destination-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-dip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the destination IP address.  This extension is
   particularly useful in mitigating Distributed Denial of Service
   (DDoS) attacks or optimizing traffic redirection where the target IP
   addresses are numerous or rapidly changing, but belong to a specific
   destination Origin AS.
- **draft-wang-idr-flowspec-sip-origin-as-filter-05** (new-draft, score 0, ignored_after_review) [idr]: [Source-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-sip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the source IP address.  This extension is particularly
   useful in mitigating Distributed Denial of Service (DDoS) attacks
   where the source IP addresses are dynamic or numerous but belong to a
   specific source AS.
- **draft-wang-idr-vpn-prefix-orf-propagation-00** (new-draft, score 0, ignored_after_review) [none]: [Source-Directed Propagation of VPN Prefix ORF for BGP-4](https://datatracker.ietf.org/doc/draft-wang-idr-vpn-prefix-orf-propagation/) — The Virtual Private Network (VPN) Prefix Outbound Route Filter (ORF)
   [I-D.ietf-idr-vpn-prefix-orf] mechanism allows a Border Gateway
   Protocol (BGP) speaker to request that an adjacent peer filter
   matching VPN routes.  In deployments using Route Reflectors (RRs) or
   Autonomous System Border Routers (ASBRs), the adjacent peer may not
   be the source of the affected routes.

   This document specifies when an intermediate router may send an
   ordinary VPN Prefix ORF to the upstream peer from which the affected
   routes were received.  Upstream transmission is permitted only after
   the intermediate router determines that no relevant downstream router
   requires the affected routes.  This document also defines an Interest
   Query/Response procedure for making that determination.
- **draft-wang-lsr-inter-as-mt-binding-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS and OSPF Extensions for Inter-AS Multi-Topology Binding](https://datatracker.ietf.org/doc/draft-wang-lsr-inter-as-mt-binding/) — [RFC5120] and [RFC4915] define Multi-Topology (MT) routing for IS-IS
   and OSPF, respectively.  When a topology-specific path crosses an AS
   boundary, a topology in one AS may need to be connected to a topology
   identified by a different MT-ID in the adjacent AS.

   Existing inter-AS Traffic Engineering extensions do not advertise
   this relationship.

   This document defines extensions to IS-IS and OSPF to advertise the
   binding between local and remote MT-IDs associated with an inter-AS
   link.
- **draft-watts-hagth-framework-00** (new-draft, score 0, ignored_after_review) [none]: [Human-Accelerated Geophysical Threshold Framework](https://datatracker.ietf.org/doc/draft-watts-hagth-framework/) — This document defines an informational research framework for
   describing anthropogenic perturbations that alter the timing,
   probability, coupling, or consequence of threshold transitions in
   geophysical systems without requiring anthropogenic dominance of the
   system's primary energy source.
- **draft-watts-octatouch-smoke-test-profile-00** (new-draft, score 0, ignored_after_review) [none]: [OctaTouch Gesture Runtime: Smoke-Test Behavior Profile](https://datatracker.ietf.org/doc/draft-watts-octatouch-smoke-test-profile/) — This document records five expected behaviors asserted by a supplied
   OctaTouch gesture-runtime smoke-test script.  It is a limited test
   profile, not a complete gesture specification.  The runtime
   implementation and its dependencies were not included with the source
   script, so the tests have not been executed as part of this archive.
   No interoperability or implementation-conformance claim is made.
- **draft-westerbaan-tls-keyshare-recommendations-03** (new-draft, score 0, ignored_after_review) [none]: [Updated Recommendations for TLS Key Shares](https://datatracker.ietf.org/doc/draft-westerbaan-tls-keyshare-recommendations/) — This document updates the TLS Supported Groups registry (previously
   EC Named Curve Registry) in the light of the future arrival of
   cryptographically relevant quantum computers: it removes the
   Recommended status from non-post-quantum key shares.

   [[ NOTE We use key share in the title and here as it's more accurate
   than "group" and perhaps more well known in the context TLS than key
   agreement or key exchange. ]]
- **draft-wu-idr-flowspec-dip-community-filter-05** (new-draft, score 0, ignored_after_review) [idr]: [Destination-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-dip-community-filter/) — BGP Flow Specification Version 2 (FSv2) propagates both traffic Flow
   Specifications and Traffic Filtering Actions using an extensible TLV-
   based filter family architecture.  This document specifies a new FSv2
   component type under the Routing Filter Family to support community-
   level filtering.  The match condition evaluates the BGP Community
   attribute associated with the destination IP address encoded in the
   Flowspec NLRI.  This mechanism is intended for deployment within a
   single administrative domain.
- **draft-wu-idr-flowspec-sip-community-filter-03** (new-draft, score 0, ignored_after_review) [idr]: [Source-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-sip-community-filter/) — BGP Flow Specification Version 2 (FSv2) propagates traffic Flow
   Specifications and Traffic Filtering Actions using an extensible TLV-
   based filter family architecture.  This document specifies a new FSv2
   component type under the Routing Filter Family to support community-
   level filtering within a single administrative domain.  The match
   condition filters traffic based on the BGP Community attributes
   associated with the route matching the packet's source IP address.
- **draft-xiao-ippm-ioam-trace-extensions-04** (new-draft, score 0, ignored_after_review) [none]: [Extensions to IOAM Trace Option for Carrying Fixed-Size Data](https://datatracker.ietf.org/doc/draft-xiao-ippm-ioam-trace-extensions/) — In situ Operations, Administration, and Maintenance (IOAM) Trace-
   Option data defined in RFC 9197 is a variable-length data, the length
   of this kind of data varies with the number of transited IOAM-capable
   nodes and the selection of data fields processed by each IOAM-capable
   node.  This document extends the IOAM Trace Option to carry a fixed-
   size data, the length of this kind of data is fixed once the
   selection of data fields processed by each IOAM-capable node is
   determined, and doesn't vary with the number of transited IOAM-
   capable nodes.
- **draft-yuan-quic-congestion-data-02** (new-draft, score 0, ignored_after_review) [none]: [Exchanging Congestion Control Data in QUIC](https://datatracker.ietf.org/doc/draft-yuan-quic-congestion-data/) — This draft defines a new transport frame which enables consenting
   endpoints to share congestion control state about the network
   connection for various purposes.  It also allows an endpoint's own
   congestion control state to be echoed back to it by a peer for
   consideration at the beginning of a future connection.
- **draft-yuan-rtgwg-hfc-framework-03** (new-draft, score 0, ignored_after_review) [none]: [Hybrid-Function-Chain (HFC) Framework](https://datatracker.ietf.org/doc/draft-yuan-rtgwg-hfc-framework/) — With the maturity of cloud native application development,
   applications can be decomposed into finer grained atomic services.
   On the other hand, as a distributed computing paradigm, fine grained
   micro-services could be deployed and implemented in a distributive
   way among edges to make computing, storage and run-time processing
   capabilities as close to users as possible to provide satisfied QoE.
   Under the circumstances analyzed, a Hybrid-Function-Chain (HFC)
   framework is proposed in this draft, aiming to wisely allocate and
   schedule resources and services in order to provide consistent end-
   to-end service provisioning.
- **draft-yxl-cats-protocols-applicability-02** (new-draft, score 0, ignored_after_review) [none]: [Protocols Applicability for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-yxl-cats-protocols-applicability/) — This document analyzes the applicability of protocols related to a
   CATS system, and describes how to build a CATS system by extending
   existing IETF protocols.
- **draft-zhangb-cats-service-metrics-op-06** (new-draft, score 0, ignored_after_review) [none]: [Computing Service Metrics Operation and Joint Service Selection under CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-service-metrics-op/) — Computing-Aware Traffic Steering (CATS) optimizes traffic forwarding
   by considering both computing and networking metrics.  The CATS
   Metrics framework provides a general metric hierarchy and operational
   guidance for aggregation and normalization.  Some deployment
   scenarios additionally require service-oriented metrics with explicit
   semantics and units to be consumed directly for joint service-
   instance and path selection.

   This document defines an operational approach that does not rely on
   the Level 1 or Level 2 normalized scores of the CATS Metrics
   framework.  Instead, service sites report service-oriented metrics
   with explicit semantics and units, such as Global Available Slots and
   Computing Time, which are directly consumed by the C-PS for joint
   service-instance and path selection.  The document clarifies how
   these metrics are derived from basic resource information, service
   reference information, and local policy.  It also specifies how the
   C-PS combines the Computing Service Table with the Network Service
   Table, and defines update-control and fallback mechanisms suitable
   for large-scale deployments.

   Within the unified CATS architecture, this service-oriented
   operational approach complements the normalized-score approach.  The
   two targeted scenarios are rapid deployment without offline metric-
   function negotiation and fine-grained, requirement-aware joint
   selection.
- **draft-zhuang-idr-flowspec-extension-for-ncm-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification Extensions for Network Congestion Management](https://datatracker.ietf.org/doc/draft-zhuang-idr-flowspec-extension-for-ncm/) — BGP Flow Specification (FlowSpec) [RFC8955] and [RFC8956] has been
   proposed to distribute traffic filter policy (traffic filters and
   actions) via BGP [RFC4271].  Multiple applications have used BGP
   FlowSpec to distribute traffic filter policy.  These applications
   include the following: mitigation of denial of service (DoS),
   enabling traffic filtering in BGP/MPLS VPNs, centralized traffic
   control of router firewall functions, and SFC traffic insertion.

   Due to its powerful extensibility, FlowSpec can be easily used for
   network congestion management.  This document describes how to use
   BGP FlowSpec to implement network congestion management.
- **draft-zzd-idr-flowspec-scheduling-04** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Extensions for Scheduling](https://datatracker.ietf.org/doc/draft-zzd-idr-flowspec-scheduling/) — BGP Flow Specification allows conveying flow specifications and
   associated traffic actions/rules to perform different actions based
   on traffic characteristics.  One use case is steering a specific flow
   onto a designated path.  However, in some scenarios, operators wish
   to chnge traffic forwarding paths over time.

   This document extends BGP Flow Specification with scheduling time
   information to match packets arriving within different time slots.
   With this extension, the headend can apply different actions to the
   same traffic at different times.

## Errors / fetch failures

- draft-faltstrom-unicode: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-faltstrom-unicode/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
