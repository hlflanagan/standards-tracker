# IETF Identity + AI Standards Watch

Date: 2026-10-20

## Read now

- **draft-zambo-aer1-24** (new-draft, score 39, core_identity) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
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
   executions.  This revision closes honesty and precision gaps: it adds
   the workflow-receipt truncation limit (new Section 8.4), normatively
   specifies the external anchor format and its verification procedure
   (rewritten Section 10, new Section 10.1), fixes a RECOMMENDED/MUST
   contradiction in Section 8.1, makes the Section 6 verification step
   testable, and documents replay, low-entropy, empty-record, and size-
   limit considerations.  It changes no receipt field, digest
   construction, or existing verification rule.  The -13 revision fixes
   a malformed sentence in the Abstract, three incorrect section cross-
   references, stale Table of Contents page numbers, a skipped footer
   page number, misaligned table rows, and chain version-string updates,
   and records two reported interoperability examples in Implementation
   Status; it changes no receipt field, digest construction, or
   verification rule.  The -14 revision adds tamper-evident metadata
   binding (new Section 3.1; conditional metadata_hash for schema 0.4
   and later), disambiguates the anchor receipt_id (Table 4), corrects
   the self-anchoring witnessing claim (Section 10), makes the
   Section 8.3 display rule a SHOULD with a byte-testable MUST, narrows
   the provenance attestation wording (Section 5), states the binding
   non-transfer rule normatively (new Section 10.2), pins
   anchored_digest to bare hex (Table 4), corrects the vector corpus
   counts, and adds normative disclosure of missing issuer
   authentication.  It changes no existing receipt field, digest
   construction, or verification rule for schema 0.3 and earlier.  The
   -15 revision narrows the Implementation Status wording for the
   reported interoperability examples at the implementer's request; it
   changes no receipt field, digest construction, or verification rule.
   The -16 revision documents the live workflow tools API (new Sections
   8.5, 8.6, 8.7): the workflow_close tool, workflow metadata in step
   receipts, and the workflow view API.  It changes no receipt field,
   digest construction, or existing verification rule.  The -17 revision
   documents the recommended execution_context member (new Section 3.2):
   an optional, non-core structure for recording source and version
   context such as the model name and version behind a tool call and the
   identity of the source system acted upon.  It changes no existing
   receipt field, digest construction, or verification rule.  The -18
   revision repairs the reference apparatus (normative references to RFC
   3339, RFC 8259, RFC 4122, and RFC 4648, and the previously missing
   RFC 7942 entry), pins two parser edge cases (duplicate JSON member
   names and leap-second timestamps are rejected), names the Unicode
   normalization behavior in Section 4 with a computed vector pair,
   adopts the unknown-versus-not-applicable convention for optional
   members, adds optional members for readback outcomes, per-field
   provenance, negative records, reversal state, method descriptors, and
   payment references, completes the execution_context member set (model
   and environment digests), adds the optional input_hash commitment
   (Section 3.3), permits SCITT and RFC 3161 anchors under Section 10,
   states the clock-trust and equivocation limits in Section 13, and
   rewrites Section 15 to position the specification against adjacent
   work.  It changes no receipt field, digest construction, or
   verification outcome for any receipt well-formed under the -17 rules.
   The -19 revision aligns the workflow tool and workflow view
   descriptions in Sections 8.5 and 8.7 with the normative Merkle
   construction in Section 8.1: both descriptions named step output
   hashes as the root's leaf input where Section 8.1 specifies step
   receipt identifiers.  An implementer report identified the
   divergence.  It changes no construction, receipt field, digest, or
   verification outcome.  The -20 revision adopts three findings
   reported by an independent implementer who built a conformance
   verifier from the -19 text alone.  It requires the published byte
   layout of a recorded input to state the member ordering rule it
   applies when the input is a JSON object (Section 3.3), and it bars
   control characters from provenance class labels, with rejection
   required (Section 5).  The conformance kit's quickstart core tier
   also gains the provenance-label and schema-version metadata checks as
   a stated rule.  It changes no receipt field or digest construction; a
   receipt well-formed under the -19 rules verifies identically, except
   that an input commitment whose published layout states no ordering
   rule is no longer reported as confirmed.  The -21 revision states the
   receipt-id binding rule normatively (Section 6), describes the id-
   substitution case in Security Considerations (Section 13), and
   credits the independent control test that produced the finding
   (Section 18).  It changes no receipt field, digest construction, or
   existing verification rule.  The -22 revision pins the legacy (schema
   0.3) member forms that satisfy the core requirements and requires
   verifiers to report a legacy acceptance explicitly rather than as a
   plain pass (Section 6), requires the canonical base64 spelling of
   canonical_bytes and the rejection of non-canonical spellings
   (Sections 3 and 4), states that the receipt object is the document
   and that no presentation envelope is part of the format (Section 3),
   enumerates the id verdict a verifier reports beside the structural
   verdict, binds the states to verifier behavior, and states the
   resolution order between the two layers (Section 6), requires the
   reason to be printed next to the rule for every check that does not
   pass (Section 6), and records an independent production validator in
   the Implementation Status.  It changes no receipt field or digest
   construction; one verification outcome changes, for a receipt whose
   canonical_bytes spelling is not canonical, which earlier revisions
   did not address.  The -23 revision states the per-anchor outcome
   report normatively (Section 6): a verifier's report carries each
   anchor's outcome in machine-visible form, and an anchor the verifier
   did not evaluate is reported as "not checked", never as an evaluated
   outcome, so that state cannot be conflated with an anchor that was
   evaluated and could not be resolved.  It changes no receipt field,
   digest construction, or existing verification rule.

Implementation Status

   This section records the implementation status of the AER-1
   vocabulary at the time of this revision, following [RFC7942].  It
   will be removed before publication as an RFC.

   Reference implementation.  Zambo (https://zambo.dev), operated by the
   document author, is a deployed implementation of Sections 3 through
   10.  Tool calls made over HTTPS as JSON-RPC to https://zambo.dev/api/
   mcp receive a public receipt page at https://zambo.dev/run/<id>,
   retrievable without an account, wallet, or token.  A machine-readable
   verifier is exposed as described in Section 6.  Receipts are anchored
   to public Nostr relays with an envelope binding the receipt
   identifier, the output hash, and the evidence hash (envelope "zambo-
   receipt-anchor/1").

   Workflow receipts (Section 8) are deployed in the reference
   implementation.  Multi-step sessions receive a workflow receipt at
   https://zambo.dev/workflow/<workflow_id> binding the ordered step
   receipts with a Merkle root, and step receipt pages link to the
   parent workflow ("Part of workflow") while workflow pages link to
   each step receipt.

   Conformance kit.  An open conformance suite for this vocabulary is
   maintained at https://gitlab.com/rambozambodotdev/zambo.  It ships
   seven bundled kit runners (Rust, Go, TypeScript, Python, Java, C#,
   and Swift), each verified against the full vector corpus, which at
   this revision stands at 119 vectors (122 checks per runner) across
   the receipt-level, Merkle (Section 8.1), timeline (Section 7),
   hardened chain (Section 7.1), chain commitment (Section 7.3),
   Unicode, id-binding, and anchor-report suites.  The -22 revision adds
   vectors pinning the canonical base64 spelling (Section 4), the nil-
   UUID rejection as a standalone case, the legacy schema 0.3 production
   shape (Section 6), the bare presentation form (Section 3), a current-
   schema (0.4) real receipt beside the two bundled 0.3 fixtures, and
   one vector per id_verdict state (Section 6).  The -23 revision adds
   the anchor-report vectors pinning the per-anchor outcome report of
   Section 6, implemented in the kit runners (kit v1.5.6) and in the
   reference verifier (aer1-verify 0.2.13) ahead of this text.  Each
   runner is zero-dependency within its language toolchain.  Running the
   Python suite takes two steps and no dependencies beyond git and a
   Python 3 interpreter:

   git clone https://gitlab.com/rambozambodotdev/zambo.git python3 aer1-
   implementations/python/conformance.py

   Since the -23 revision, each conformance run also emits the evaluated
   vector set: one line per vector carrying its id and content digest,
   with a corpus digest over the set, so a claimed pass can be checked
   as a set difference against the full corpus.  The cross-runner parity
   gate mints a receipt of each of its runs (schema 0.4; the committed
   payload carries the evaluated vector ids, the corpus digest, and the
   verdict, pass or fail) and pins it in the kit repository as parity-
   gate-receipt.json; the gate verifies that receipt with the kit
   conformance check and with aer1-verify, id bound, before it reports
   success.

   An implementation is conformant when it produces byte-identical
   verdicts to the reference runners across the full vector corpus.  The
   corpus includes attack vectors for tampered provenance labels, schema
   version downgrades, and legacy (pre-0.4) receipts; conformance
   requires the Section 6 metadata checks to fail the first two and to
   report the third with a legacy notice rather than a failure.  The kit
   is versioned; the v1.5.6 release is the frozen reference for the
   corpus described above.

   Independent verification.  The Section 6 verification procedure has
   been exercised against live receipts by independent third parties:

   *  On 2026-09-16, an independent agent ("Merv", on the Clawstr
      network) verified a live receipt (id 0ec81343-cc1f-
      4c25-9c33-d76b5582406d) in three checks: the SHA-256 of the
      decoded canonical bytes matched the output commitment, the
      upstream evidence hash matched, and the anchor event carried a
      valid signature retrievable on independent relays.  The same party
      reported that the anchor envelope did not then bind the evidence
      hash; the reference implementation has since shipped the binding
      envelope described above.

   *  On 2026-09-16, an independent agent ("nilo_agent", on Nostr) ran
      adversarial verification challenges against live receipts,
      including a witness round and a strong-form Bitcoin-anchored
      challenge (anchor block 967351, receipt 88094e26), each answered
      with bytes the challenger could check independently.

   *  On 2026-09-25 and 2026-09-26, an independent agent ("Devan", on
      Nostr) published timestamped probe receipts (v1 and v2) exercising
      independent verification of agent work in the same receipt model.

   Independent validators.  An independent implementation exposes the
   Section 6 procedure as a public service:

   *  WhiteMagic Labs (Lucas Bailey) operates a production validator for
      this specification at https://api.whitemagic.dev/aer1/verify,
      publicly accessible without a key, with the same procedure also
      exposed as an MCP tool (verify_aer1_receipt).  On 2026-10-17 the
      operator exercised the validator against the reference
      implementation and the conformance corpus.  The two
      implementations initially disagreed on cases in both directions (a
      decoding boundary in the validator; an id-binding reading and a
      nil-UUID acceptance in the reference tooling), each disagreement
      was resolved against the draft text the same day, and the
      implementations now agree across the exercised case matrix.  The
      validator reports comparison outcomes in the shared states of
      Section 6 and attaches its provenance caution as advisory metadata
      beside the verdict, the arrangement the provenance note in
      Section 6 describes.

   Seven bundled kit runners for Sections 3 through 6 are maintained in
   the conformance kit repository (Rust, Go, TypeScript, Python, Java,
   C#, and Swift), each verified against the full vector corpus
   described above (119 vectors, 122 checks per runner).  These runners
   are the kit's own test runners, not independent implementations.
   Independent third-party implementations, built from the draft text
   alone without access to kit internals, include ARION's Node.js and
   Java verifiers and ColonistOne's Perl verifier, each conformant
   against the same corpus.  Since revision 12, contributors have
   reported two scoped interoperability exercises.  On 2026-10-08,
   Tanilo and the AER-1 author published a cross-repository worked
   example linking an AER-1 receipt to a live Tanilo receipt by
   canonical hash, with the AER-1 commitment check and the Tanilo
   signature check run separately, each under its own rules.  Also on
   2026-10-08, the independent builder FlyThink published a four-case
   fixture binding AER-1 execution receipts to physical completion
   claims; all four cases replay cleanly, including the case where a
   valid AER-1 receipt coexists with invalid physical-evidence binding
   (see Section 10.2).  Reports of additional implementations or
   independent verification results are solicited; implementers are
   encouraged to validate against the open conformance kit described
   above and to report their results.
- **draft-burls-mtac-01** (new-draft, score 28, agent_identity) [none]: [Merkle Tree Agent Certificates (MTAC): A Merkle Tree Certificates Profile for AI Agent Identity](https://datatracker.ietf.org/doc/draft-burls-mtac/) — This document profiles Merkle Tree Certificates (MTC) for the
   identity of AI agents.  An MTAC certificate is an MTC whose subject
   is one AI agent instance, named by a workload identifier in a URI
   subject alternative name, so that it is also a Workload Identity
   Certificate.  It carries a mandatory non-critical extension naming
   the sponsor the CA recorded as accountable for the agent, and two
   optional ones: scopes declared for the agent at issuance, and the
   model and configuration components the agent is issued for, each
   graded by how the CA came to record it.

   The document also defines an audit cosigner role and a procedure by
   which an auditor, possibly without network access and possibly long
   after issuance, can establish that a certificate was issued and
   logged and what it declared.

   An MTAC certificate identifies an agent.  It does not authorize the
   agent to do anything, and it does not record what the agent did.
   Records of agent actions can be expressed as signed statements in a
   transparency service that refer to an MTAC certificate as the acting
   party.
- **draft-das-agent-execution-finality-00** (new-draft, score 28, trust_infrastructure) [none]: [Protected Execution-Finality Architecture for AI and Autonomous Systems: Act-Bound Capabilities and Effectuation-Boundary Verification](https://datatracker.ietf.org/doc/draft-das-agent-execution-finality/) — This document describes a proposed protected execution-finality
   architecture for artificial-intelligence agents, autonomous software
   systems, confidential computing environments, and distributed
   execution infrastructures.  The architecture addresses a fundamental
   security distinction: the ability of an AI agent or computational
   process to generate, prepare, or request an operation does not
   independently establish the protected authority required to make that
   operation effective.

   The proposed architecture separates the computation plane from
   protected execution authority through mandatory operation
   interception, Non-Effective State staging, machine-verifiable
   Candidate Act Descriptors, a Protected Enforcement Domain (PED),
   protected authorization-state management, scoped non-bearer execution
   capabilities, and Finality Sink verification.  A Candidate Act
   remains non-effective until the applicable authority, purpose,
   destination, execution scope, runtime context, policy epoch,
   freshness, revocation, and other mandatory authorization predicates
   have been validated.  Where required, protected validation evidence
   is committed before, or atomically with, capability availability.
   The designated Finality Sink independently verifies the capability
   against the actual operation and applicable protected state
   immediately before permitting the governed consequential effect.

   The architecture addresses AI-agent sandbox isolation, mandatory and
   non-bypassable mediation, out-of-process permission authorities,
   executable-specific access restrictions, network and API egress
   enforcement, destination resolution, redirect consistency, credential
   brokering, protected credential substitution, privileged connectors,
   human and developer approval, runtime policy modification, multi-
   agent delegation, taint and provenance-based authorization, and fail-
   closed execution control.

   For technical discoverability and independent architectural
   examination, related publicly documented industry systems include
   Meta Muse/Sentinel and NVIDIA OpenShell, NemoClaw, and the Open Agent
   Safety Platform/Sentry.  Relevant engineering terminology includes
   Muse Secure VM, isolated runtime cells, host-side permission
   authority, forward proxies, surrogate credentials, just-in-time
   credential insertion, eBPF/LSM-based taint propagation, controlled
   network egress, executable-specific policy enforcement, developer-
   approved policy changes, and hardware-assisted monitoring through
   SmartNICs, data processing units, BlueField, and DOCA.  These
   references identify relevant public engineering contexts and
   functional security objectives; they do not establish that the named
   systems implement the complete architecture described here.

   The principal technical distinction examined in this document
   concerns the relationship between an upstream permission decision and
   independently enforceable authority at the actual effectuation
   boundary.  The proposed execution-finality sequence includes
   protected validation of a concrete Candidate Act, required protected-
   state handling, validation-evidence commitment, operation-bound
   capability release, and mandatory verification of that capability by
   the applicable Finality Sink.  The architecture distinguishes
   conventional permission checking, credential isolation, model-
   computation admission, and post-event monitoring or quarantine from
   the separate authorization conditions required before an externally
   consequential operation becomes effective.

   The document further describes enforcement across network gateways,
   host operating systems, credential-release interfaces, service
   meshes, autonomous code-deployment systems, confidential virtual
   machines, protected storage, database commitments, accelerator
   fabrics, DMA/RDMA transfers, SmartNICs, DPUs, hardware Finality
   Latches, and receiving-side execution boundaries.  It addresses
   protected state consumption, capability replay prevention, policy-
   version fencing, distributed revocation, hardware attestation,
   workload migration, snapshot rollback, crash-consistent recovery, and
   prevention of unauthorized duplicate effects.  Authorization of one
   effectuation boundary does not automatically establish authority for
   a distinct downstream consequence.

   This individual Informational Internet-Draft presents architectural
   mechanisms, enforcement points, implementation alternatives, and
   security considerations for independent technical examination.  It
   does not specify a complete interoperable wire protocol or request
   IANA allocations.  Industry and product names are used solely for
   technical relevance, terminology identification, and discoverability,
   without implying affiliation, endorsement, copying, derivation,
   infringement, patent validity, or architectural identity.

   Related Indian Patent Disclosures and Claimed Priority: The author
   identifies Indian Application No. 202531130665, dated 23 December
   2025, as an earlier related foundational disclosure, together with
   Indian provisional applications 202631000572 (3 January 2026),
   202631001586 (7 January 2026), and 202631002990 (12 January 2026)
   concerning execution-time authorization and irreversible-boundary
   enforcement.  Indian Application No. 202631124028 is separately
   identified as a related patent-pending application.

   Related International Patent Applications and WIPO Publications: The
   author identifies PCT/IB2025/058316 (Mothership; WO 2025/210622),
   PCT/IB2026/053385 (ALF-PCT; WO 2026/115520), PCT/IB2026/055615 (DAS
   Protocols I; WO 2026/150382), PCT/IB2026/055760 (DAS Protocols II; WO
   2026/150383), PCT/IB2026/055870 (DAS Protocols III; WO 2026/150384),
   PCT/IB2026/056058 (DAS Protocols IV; WO 2026/154461), PCT/
   IB2026/056809 (DAS Protocols V; WO 2026/172334), and PCT/
   IB2026/056941 (DAS Protocols VI; WO 2026/172336) as related technical
   disclosures.

   These application identifiers and publication references are provided
   to facilitate independent examination of the original technical
   documents and their chronology.  Any claimed priority entitlement
   depends upon the actual subject-matter support contained in the
   corresponding earlier filing and the applicable legal requirements.
   The filing chronology does not imply that every technical mechanism
   described in this Internet-Draft was disclosed in every earlier
   application.

   Fundamental architectural principle: Computation is not authority to
   act.
- **draft-uimonen-veif-02** (new-draft, score 26, core_identity) [none]: [Verified Email Identity Framework (VEIF)](https://datatracker.ietf.org/doc/draft-uimonen-veif/) — This document defines the Verified Email Identity Framework (VEIF),
   an experimental framework for adding accountable, verified sender
   identity to Internet email.

   VEIF complements existing email authentication mechanisms such as
   SPF, DKIM, and DMARC. Those mechanisms establish authorization,
   message integrity, and domain alignment, but do not by themselves
   establish that a sender identity is associated with a verified
   real-world entity.

   VEIF uses an SD-JWT-based Verifiable Digital Credential (SD-JWT VC)
   to bind a pseudonymous sender identity and a sender-controlled
   cryptographic key to an identity verified by an Identity Provider
   (IdP). A separate VEIF message signature binds that credential to
   the email message.

   The recipient does not normally receive the sender's real-world
   identity. Instead, VEIF provides technical accountability: where an
   appropriate legal or otherwise authorized process exists, the
   Identity Provider can establish the real-world entity to which the
   sender credential was issued.

   This document intentionally does not define a global identity
   authority, a legal identification procedure, or a mandatory trust
   hierarchy. Trust and identity disclosure policies remain matters
   for receiving organizations, Identity Providers, jurisdictions, and
   deployment environments.

   This version is experimental and is intended to enable discussion,
   implementation experimentation, and interoperability testing.
- **draft-heigh-wimse-workload-identity-metadata-00** (new-draft, score 25, core_identity) [none]: [Workload Identity Metadata](https://datatracker.ietf.org/doc/draft-heigh-wimse-workload-identity-metadata/) — This document specifies metadata attributes associated with a
   workload's identity that are used for auditing, authorization,
   accounting, and other purposes.  It profiles existing claims for
   group membership, roles, and entitlements, with delivery either in
   JWT-based Workload Identity Credentials or through an authenticated
   workload metadata endpoint.  The endpoint supports metadata retrieval
   for workloads using JWT-based or X.509-based credentials and
   disclosure according to the caller's authorization.  An optional JWT
   claim or X.509 certificate extension identifies the metadata endpoint
   for the credential's subject.

   This document also defines the separation between identifier and
   metadata.  It distinguishes workload attributes and durable principal
   associations from per-request delegation and grants such as scopes,
   and states the requirements that make the separation sound, including
   identifier uniqueness.

   The document applies to workloads generally, including services,
   batch and continuous integration jobs, serverless functions, and AI
   agents.  Agentic use cases are discussed separately.
- **draft-thaha-scitt-agent-execution-evidence-00** (new-draft, score 24, core_identity) [none]: [Agent Execution Evidence: A SCITT Profile for Verifiable Records of AI Agent Runs](https://datatracker.ietf.org/doc/draft-thaha-scitt-agent-execution-evidence/) — AI agents act through calls to models, tools and other agents.
   Identity work establishes who an agent is and what it may do, but
   leaves execution-evidence formats and assurance criteria out of
   scope.  This document profiles the Supply Chain Integrity,
   Transparency, and Trust (SCITT) architecture for Signed Statements
   that bind an agent's registered identity, declared capabilities,
   risk-based assessment and supervised operational status to a hash-
   chained record of every call the agent makes.  It also defines
   admission records produced where a call is received, and the linking
   of records for requests that pass between agents of different
   operators.  It specifies Registration Policy, offline verification
   and Bundle requirements.  It does not define an accreditation scheme,
   a universal risk classification, an identifier scheme or a policy
   language.
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
- **draft-asor-wimse-agent-delegation-chain-02** (new-draft, score 22, authorization) [none]: [Verifiable Attenuated Delegation for AI Agent Chains](https://datatracker.ietf.org/doc/draft-asor-wimse-agent-delegation-chain/) — AI agents increasingly delegate tasks to other agents.  Each
   delegation should convey only a subset of the delegating party's
   authority, that subset should be bounded in scope, magnitude, and
   time, and any enforcement point should be able to verify -- offline,
   with no call to an authorization server -- that a token presented at
   hop N carries authority no greater than the token at hop N-1, back to
   a trusted root, and that every hop acts under the same accountable
   principal.  OAuth 2.0 Token Exchange (RFC 8693) models two-party
   delegation and records prior actors in a nested "act" claim, but that
   claim is informational only and cannot enforce attenuation across a
   chain of depth two or more.  This document defines the Agent
   Delegation Chain: a profile of OAuth 2.0 JWT access tokens (RFC 9068)
   that carries authority as Rich Authorization Requests (RFC 9396),
   binds the chain to one principal and names the agent acting at each
   hop, links each delegation to its parent by a cryptographic byte-
   commitment, and specifies a deterministic offline verification
   algorithm that enforces monotonic attenuation, bounded depth,
   monotonic expiry, and principal invariance.  It reuses existing JOSE,
   proof-of-possession (RFC 9449), and status-list machinery (the OAuth
   Status List draft) and introduces no new cryptography.
- **draft-nelson-agent-delegation-receipts-14** (new-draft, score 19, authorization) [none]: [Agent Delegation Receipts](https://datatracker.ietf.org/doc/draft-nelson-agent-delegation-receipts/) — This document defines the Agent Delegation Receipt: a signed record
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
   Version -14 adds a pointer to content profiles for verification of
   what the agent produced, following implementer feedback; no wire-
   format changes.
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
- **draft-ramki-ptp-hardware-rooted-attestation-02** (new-draft, score 18, trust_infrastructure) [none]: [Hardware-Rooted Attestation for Precision Time Protocol: Scalable Workload Identity and Phased PQC Readiness](https://datatracker.ietf.org/doc/draft-ramki-ptp-hardware-rooted-attestation/) — This document defines a scalable framework for hardware-rooted
   cryptographic attestation in the Precision Time Protocol (PTP).
   Standard PTP security mechanisms rely on symmetric keys, which suffer
   from identity ambiguity and source non-repudiation failures.  These
   vulnerabilities allow any node possessing the shared secret to
   impersonate a Grandmaster.  To resolve these issues while overcoming
   the silicon throughput limits of traditional TPMs and the overhead of
   Post-Quantum Cryptography (PQC), this draft specifies a tiered trust
   model.  A Hardware Root (e.g., TPM) establishes a long-term PQC
   identity, while a workload identity management plane (e.g., SPIFFE/
   SPIRE) manages the frequent rotation of short-lived operational keys.
   These keys perform amortized signing of PTP message batches via
   Merkle Trees, ensuring wire-speed synchronization and irrefutable
   provenance for regulated environments.
- **draft-luna-eagf-agent-delegation-semantics-00** (new-draft, score 17, core_identity) [none]: [Semantic Governance Requirements for AI Agent Delegation and Handoff](https://datatracker.ietf.org/doc/draft-luna-eagf-agent-delegation-semantics/) — AI agents increasingly decide and act on behalf of organizations and
   delegate work to other agents.  Identity, authentication,
   authorization and runtime control mechanisms establish who is acting
   and what is permitted, but they do not by themselves preserve the
   organizational meaning of a delegation: the bounded authority,
   purpose, material context, and the distinction between a
   recommendation, a decision, an action and its outcome.  This document
   states requirements, derived from the Enterprise Agent Governance
   Framework (EAGF), that such semantics be preserved across tool calls,
   delegations and agent-to-agent handoffs.  It defines no new protocol.
- **draft-narvaneni-agent-uri-04** (new-draft, score 17, core_identity) [none]: [The agent URI Scheme and Verifiable Agent Identity](https://datatracker.ietf.org/doc/draft-narvaneni-agent-uri/) — Software agents increasingly act on the Internet on behalf of people
   and organizations: they call APIs, browse websites, and delegate work
   to other agents.  Protocols such as A2A and MCP define how agents
   communicate, but there is no interoperable way to answer a prior
   question: _which agent is this, and how can its claims be verified?_

   This document defines the agent URI scheme as a stable, human-
   readable identifier for an agent, a deterministic mapping from that
   identifier to an HTTPS-hosted Agent Identity Document, anchoring of
   the agent's keys to a web origin or a Decentralized Identifier, and
   signed statements that bind the agent to its protocol metadata.  It
   also defines profiles that let an agent prove its identity on HTTP
   requests, building on HTTP Message Signatures for automated traffic,
   and that let short-lived agent instances act under the agent's
   identity using the WIMSE Workload Identity Token format.  It
   deliberately does not define how agents communicate, describe their
   capabilities, or are invoked.
- **draft-gilda-audit-agent-audit-record-00** (new-draft, score 16, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-audit-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions and the effects that followed them.  The format is one in-
   toto predicate type, signed inside a DSSE envelope.  A record carries
   the decision and the observed effect with a derived agreement between
   them, whether the decision point could evaluate the request and how
   fresh each input it relied on was, and a canonicalization contract
   under which a party that trusts neither the agent nor its operator
   recomputes the record's consistency from its bytes.  The document
   also defines what a party that retains a record keeps beside it, so
   that the record can later be dated from anchors that party does not
   control.  The format carries the seven minimum audit fields of the
   WIMSE AI Identity Management System framework, and it is offered as a
   data model for the audit records the proposed AUDIT working group
   would specify.  It defines no policy.
- **draft-swarmspeak-handshake-00** (new-draft, score 16, agent_identity) [none]: [The SwarmSpeak Handshake Protocol, Version 1.1](https://datatracker.ietf.org/doc/draft-swarmspeak-handshake/) — AI agents are becoming some of the biggest users of the Internet.
   A site today has no neutral way to tell a good agent from a bot.
   The site sees either an anonymous request it cannot trust, or a
   request carrying a long-lived credential it cannot check. The
   result is blunt blocking on one side and unchecked abuse on the
   other.

   This document defines the SwarmSpeak Handshake, a protocol that
   lets an AI agent present a short-lived, narrowly scoped, signed
   statement of who it acts for and what it is allowed to do, and
   lets a site verify that statement cheaply before serving the
   request. The agent proves authority with a principal-signed
   capability certificate, a short-lived directory-signed status
   proof, and an HTTP Message Signature. The site sees only a
   per-origin pseudonym for the agent, never a global tracking
   identifier. Every completed session at a handshake-accepting
   site produces an itemized receipt, and receipted sessions are
   recorded in an append-only audit log.

   This is an individual submission. It is not a product of any
   IETF working group, it has not been reviewed by any IETF working
   group, and it does not represent IETF consensus. It is published
   to invite review and to record prior art for the shapes defined
   here: the capability certificate, the per-origin certificate
   view, the short-lived status proof, and the receipt.
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
- **draft-morrison-ot-command-authority-04** (new-draft, score 15, authorization) [none]: [Authorised and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
   issued to an operational-technology (OT) or industrial control system
   on the authority of a software agent is refused unless it carries a
   verifiable statement of who the agent is, which human principal it
   acts for, whether that principal authorised this specific action on
   this specific asset, whether a named human signed off on the action
   where its risk class requires it, and an append-only record
   sufficient to attribute the action afterward.  The profile does not
   invent new cryptography or a new identity mechanism.  It composes
   primitives specified elsewhere, DNSSEC-rooted agent discovery, a
   scoped and revocable authorisation grant, and a named-human
   authorization receipt bound into the record as human-authorization
   evidence, together with an append-only audit record, into a single
   structure, the Command Authority Envelope, that an enforcement point
   evaluates and, on any missing or invalid binding, refuses.  The
   profile is availability-first and fails closed on authority, never on
   safety: it MUST NOT be placed in the trip path of a safety function.
   The memo relates the profile to the identification, use-control, and
   audit requirements that the IEC 62443 and NERC CIP frameworks state
   but do not give a wire mechanism for.  A neighbouring proposal gates
   safety-critical commands on an agent's trust level; this profile
   takes the opposite position, and states why.
- **draft-thaha-wimse-agent-evidence-binding-00** (new-draft, score 15, core_identity) [none]: [Evidence Binding for AI Agent Credentials](https://datatracker.ietf.org/doc/draft-thaha-wimse-agent-evidence-binding/) — The WIMSE AI Identity Management System (AIMS) requires tamper-
   evident agent audit logs but does not specify their format or
   discovery.  This document maps the AIMS minimum fields to the SCITT
   Agent Execution Evidence profile, defines one claim that binds a
   workload credential to the persistent agent, governing policy,
   expected Evidence Service and optional Assurance Statement, and
   defines an in-toto predicate type for carrying Execution Receipts in
   the audit format proposed for WIMSE.  It also describes how a service
   admits an agent's call by checking its assurance at the moment of the
   request, and defines an HTTP field that links each call to the
   caller's evidence.  It is input to the AIMS work and makes no change
   to it.
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
- **draft-ietf-wimse-http-signature-08** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload-to-Workload Authentication with HTTP Signatures](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).
- **draft-liu-mcguinness-oauth-bounded-work-00** (new-draft, score 14, authorization) [none]: [OAuth 2.0 Bounded Work Authorization](https://datatracker.ietf.org/doc/draft-liu-mcguinness-oauth-bounded-work/) — OAuth 2.0 provides mechanisms for requesting and granting access,
   constraining access tokens, and managing their lifecycle.  It does
   not define a common way to identify the work a user approved and to
   associate that work's bounds and termination with the credentials
   issued for it.  When an AI agent acts on a user's behalf, that work
   is what most needs governing: the agent's authority should come from
   the approval of a bounded piece of work, should stay within the
   bounds the user approved, and should end when the work is done or the
   user withdraws it.

   This document presents a use case in which a user withdraws an
   agent's approved work and the agent's further operations are denied,
   and identifies the semantics that independently implemented clients,
   Authorization Servers, and Resource Servers need to share to deliver
   that outcome.  It then describes a framework for approved bounded
   work, built on three objects: a bounded work proposal, the governing
   authorization established when it is approved, and approval evidence,
   a durable record of the authorization decision and the approved
   bounds.  Credentials issued for the work are associated with the
   governing authorization, and ending the authorization has defined
   consequences for further issuance and, within a stated acceptance
   window, for resource access.

   This version specifies no wire formats and requests no IANA actions.
   It is a direction-setting document: its goal is agreement on the
   problem and the conceptual model, with details left to subsequent
   revisions and working group discussion.
- **draft-sharif-attp-industrial-control-systems-03** (new-draft, score 14, core_identity) [none]: [ATTP for Industrial Control Systems: Cryptographic Agent Authentication in SCADA and IoT Environments](https://datatracker.ietf.org/doc/draft-sharif-attp-industrial-control-systems/) — This document defines an application profile of the Agent Trust
   Transport Protocol (ATTP) [draft-sharif-attp-agent-trust-transport]
   for use in Industrial Control Systems (ICS), Supervisory Control
   and Data Acquisition (SCADA) environments, and Internet of Things
   (IoT) deployments.  It specifies how ATTP mandatory message signing,
   agent identity passports, and trust-gated access control apply to
   industrial protocols including Modbus/TCP, OPC UA, MQTT, and CoAP.

   The profile addresses the absence of per-message authentication in
   legacy industrial protocols, which has been exploited in numerous
   critical infrastructure attacks.  It defines a gateway architecture
   that enables ATTP protection for legacy devices without firmware
   modification, maps ATTP trust levels to IEC 62443 Security Levels,
   and specifies real-time revocation mechanisms suitable for
   safety-critical environments.  It further defines Autonomous
   Decision Assurance: where an AI agent executes a consequential
   command without per-action human review, the underlying decision
   MUST meet a stated reproducibility condition or be escalated to
   human oversight.  It adds smart-city and urban-infrastructure sector
   guidance and evidence-grade records for actions that may be legally
   contested.
- **draft-agentic-ai-usecases-requirements-04** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-foroughi-agent-protocol-dimensions-01** (new-draft, score 13, agent_identity) [none]: [A Dimensional Model for Characterizing AI Agent Protocol Proposals and Their Substrates](https://datatracker.ietf.org/doc/draft-foroughi-agent-protocol-dimensions/) — Discussions about agent protocols are frequently muddied by
   overloaded terms; asks such as "we need a session protocol" or "we
   need cross-domain support" bundle several distinct concerns across
   transport, agent protocol, and orchestration layers.  This document
   offers a dimensional model that routes each concern to its proper
   layer.

   The document defines a small set of protocol-visible dimensions for
   characterizing AI agent protocol interactions and applies them to
   representative agentic protocol proposals (A2A, MCP, the ACP
   invocation surface of the AGNTCY stack, and AGTP) alongside their
   substrate bindings, making explicit which dimensions each proposal
   owns at the protocol layer and which it inherits from its substrate.
   The document does not rank proposals and does not prescribe an
   architecture.  It is standalone: it neither depends on nor prescribes
   any use-case or requirements document.
- **draft-senarath-a2wp-01** (new-draft, score 13, verifiable_claims) [none]: [Agent-to-Wallet Protocol for Digital Credentials (A2WP)](https://datatracker.ietf.org/doc/draft-senarath-a2wp/) — AI Agents acting for people and organizations meet credential offers
   and presentation requests, for example when a website asks the Agent
   to prove an attribute before it continues.  An AI Agent can be misled
   by the content it processes, so it should not possess credentials or
   keys, or decide what to disclose.

   This document defines the Agent-to-Wallet Protocol (A2WP), with which
   an AI Agent passes such an offer or request to a Wallet exactly as it
   received it.  The Wallet decides whether to act, obtains approval
   when needed, and performs the issuance or presentation with the
   Issuer or Verifier.  The AI Agent learns the outcome and receives any
   continuation the Issuer or Verifier returns, so it can resume its
   task.  Credentials, presentations and keys never reach the AI Agent.
- **draft-gaip-act-receipt-00** (new-draft, score 12, adjacent_watchlist) [none]: [The Agent Act Receipt: a signed, chained record of an agent's act](https://datatracker.ietf.org/doc/draft-gaip-act-receipt/) — Software agents act for people: they buy, book, cancel, agree,
   deliver, refuse, tell, ask, read and check.  Each payment rail,
   marketplace and assistant keeps its own record of those acts, held by
   that party.  The person the agent acted for has no record of their
   own.  This document describes the Agent Act Receipt: one entry per
   act, written by the agent as digests bound to a continuity handle,
   signed by a running transparency service, placed in a hash chain and
   covered by dated anchors, with a COSE_Sign1 form of the signature and
   a signed export (the switch pack) the person can take to another
   agent.  The format is published by GAIP, which runs one such service.
   This document makes no claim of trust, certification or adoption: a
   receipt shows that the service's key signed a digest at a stated
   time, and nothing about the act itself.
- **draft-milan-agent-decision-commitment-00** (new-draft, score 12, trust_infrastructure) [none]: [Agent Decision Commitments for Payments](https://datatracker.ietf.org/doc/draft-milan-agent-decision-commitment/) — Software agents increasingly select and initiate payments on behalf
   of people and organizations.  Existing agent payment protocols record
   what a principal authorized and that value moved, but not what
   information the agent relied on when it chose.  This document defines
   the Agent Decision Commitment (ADC): a salted hash commitment to a
   decision record that identifies the content the agent provided to the
   model interface (after any agent-side transformation), the model
   calls made, and the resulting answer and action.  The commitment is
   carried as a single selectively disclosable claim in an existing
   payment mandate or payment payload and is, by default, registered
   with a transparency service before the payment is authorized.  The
   decision record and its content remain with the holder and are
   disclosed only to dispute participants, who can verify them against
   the mandate and the transparency service and can inspect the content
   the agent provided to the model.  This document defines the data
   model, the commitment and anchoring procedures, a disclosure and
   verification procedure that reports attestation levels rather than
   verdicts, and bindings to three agent payment protocols and to
   account-to-account credit transfers.  It also defines a witnessed
   reciprocal exchange by which two parties' agents evidence what passed
   between them: the receiver signs over the committed bytes,
   independent witnesses fix the time of each step, a failure to answer
   by a deadline is recorded, and arbiters resolve stalled exchanges.
- **draft-shankarlingam-oauth-agent-dns-link-00** (new-draft, score 12, authorization) [none]: [Linking an Agent's DNS Name to its OAuth Client](https://datatracker.ietf.org/doc/draft-shankarlingam-oauth-agent-dns-link/) — Software agents increasingly call agents and services operated by
   other organizations.  A receiving organization often wants to know
   two things about any such caller: that it is the agent it claims to
   be, and that the organization operating it still authorizes it.
   Existing approaches to the second question require a trust
   relationship between the two organizations' authorization servers.

   This document defines a DNS record by which the owner of a domain
   links an agent's DNS name to the OAuth client that the agent uses at
   the owner's own authorization server.  The sending agent presents a
   fresh access token for that client; the receiver verifies the token
   against the record and against the issuer's published keys.  No trust
   relationship, registration or federation between the two
   organizations is needed, and disabling the client at the sending
   organization's authorization server stops the agent being accepted by
   every receiver.
- **draft-mccormack-ztip-01** (new-draft, score 11, trust_infrastructure) [none]: [The Zero Trust Intelligence Protocol (ZTIP): Governed, Independently Verified AI Agent Transactions](https://datatracker.ietf.org/doc/draft-mccormack-ztip/) — The Zero Trust Intelligence Protocol (ZTIP) is an open, transport-
   neutral protocol for governed AI agent transactions.  It defines five
   immutable JSON envelope types and a transaction lifecycle under which
   every agent-initiated action is authorized by policy before
   execution, integrity-protected by hash over a canonical form, and --
   distinctively -- verified as complete by an authority independent of
   the actor that performed the work.  An executor's claim of success is
   treated as attestation, and attestation alone never satisfies a
   required verification check.  This revision states what integrity
   verification does not establish, and specifies the fail-closed rules
   an implementation MUST apply when it verifies a set of envelopes
   together, so that a verification report can never claim more than was
   actually checked.  This document describes ZTIP version 1.0-draft for
   the record; the full specification, JSON Schemas, examples, and a
   reference runtime are maintained in the open at the repository
   referenced herein.
- **draft-mora-oauth-entity-profiles-02** (new-draft, score 11, authorization) [none]: [OAuth 2.0 Entity Profiles](https://datatracker.ietf.org/doc/draft-mora-oauth-entity-profiles/) — This specification introduces Entity Profiles as a mechanism to
   categorize OAuth 2.0 entities—clients and subjects—based on their
   operational context.  Entity Profiles provide structured descriptors
   for the client initiating the OAuth flow and the subject represented
   in tokens.  This document defines new JWT Claim names and metadata
   parameters for use in JWTs issued or consumed in OAuth flows,
   including but not limited to access tokens, ID tokens, JWT
   authorization grant assertions, and transaction tokens, as well as in
   token introspection responses, dynamic client registration, and
   Authorization Server metadata.  It also defines vocabulary for
   classifying acting entities within delegation chains.
- **draft-sirkkavaara-vaara-receipt-14** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
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
- **draft-watts-high-assurance-agent-control-envelope-00** (new-draft, score 11, core_identity) [none]: [High-Assurance Agent Control Envelope](https://datatracker.ietf.org/doc/draft-watts-high-assurance-agent-control-envelope/) — Agentic systems can authenticate successfully, hold a valid
   authorization object, and still be unsafe to execute because required
   evidence is missing, the software has not reached a required assurance
   stage, the authority epoch is stale, a prior revocation is unresolved,
   or a human-approval requirement is unsatisfied.  This document defines
   the High-Assurance Agent Control Envelope (HAACE), a protocol-neutral
   profile that binds an exact agent action to identity status,
   authorization state, policy, assurance stage, evidence state, authority
   epoch, revocation state, oversight requirements, and an action-time
   decision.  HAACE requires fail-closed treatment of missing or
   indeterminate prerequisites, separates authorization from execution,
   and produces non-bearer decision and execution receipts.
- **draft-chen-oauth-agent-intent-token-00** (new-draft, score 10, authorization) [none]: [The Intent Token - A Credential for Delegated User Intent](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-intent-token/) — In the scenario of AI agent authorization, how to ensure that a
   user's high-level, natural-language intent is correctly and safely
   converted into low-level, specific authorization grants.  A
   misunderstanding or malicious interpretation during this translation
   can lead to significant security vulnerabilities.  This document
   introduces the "Intent Token," a new type of security token designed
   to bridge this semantic gap.  The Intent Token is a signed credential
   that immutably captures the user's original intent.  It decouples the
   act of granting an intent from the act of issuing specific access
   tokens.  A client presents this Intent Token to an Authorization
   Server, which acts as a trusted intermediary.  The Authorization
   Server's responsibility is to interpret the user's stated intent and,
   based on its policies, issue narrowly-scoped, short-lived access
   tokens for specific resources, thereby ensuring the principle of
   least privilege is upheld throughout the process.
- **draft-mih-scitt-checkpointed-local-log-02** (new-draft, score 10, trust_infrastructure) [none]: [The Checkpointed Local Log (CLL)](https://datatracker.ietf.org/doc/draft-mih-scitt-checkpointed-local-log/) — Many systems emit individually signed records — receipts,
   attestations, statements — and store them locally.  Each record
   verifies on its own, but the collection proves nothing: records can
   be deleted, reordered, or created after the fact without detection.
   This document specifies the Checkpointed Local Log (CLL): a producer-
   operated append-only log that is a Merkle Mountain Range as defined
   by the COSE Receipts profile for Merkle Mountain Ranges, together
   with a small signed checkpoint that commits to the log's entire
   history.  A checkpoint carries the content of that profile's Receipt
   of consistency — the accumulator and the consistency proof — inside a
   SCITT Signed Statement, so it can be registered with one or more
   independent Transparency Services without any change to them.  A CLL
   upgrades a set of point receipts into a stream with provable order,
   contemporaneity, and completeness, and states precisely what it does
   not establish.  It defines no new proof format, no change to SCITT
   Registration or Receipts, and no payload semantics.
- **draft-ross-mercurius-07** (new-draft, score 10, adjacent_watchlist) [none]: [Mercurius Window System (MWS)](https://datatracker.ietf.org/doc/draft-ross-mercurius/) — The Mercurius Window System (MWS) is a zero-trust, network-native
   window system for contemporary desktops. It combines persistent,
   detachable graphical Sessions with network transparency. MWS works
   on a workstation without requiring network connectivity. The same
   Session model allows users to start a new Session or resume a
   detached Session, either at the workstation itself or from another
   device across the network.

   MWS complements local display systems such as Wayland. Applications
   and their state remain on the workstation, while a Portal provides
   the user's display and input facilities. Modern graphics APIs and
   authenticated transport support this separation between where
   applications execute and where a user interacts with them. This
   document specifies the Session, Window, and communication behaviour
   needed for independent implementations to interoperate.
- **draft-elkins-plants-enterprise-mtc-deployment-01** (new-draft, score 9, core_identity) [none]: [Enterprise Deployment Considerations for Standalone Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-elkins-plants-enterprise-mtc-deployment/) — The migration of public Web PKI authentication to post-quantum
   mechanisms must fit enterprise certificate management and TLS
   termination architectures.  This document examines whether an urgent
   need for post-quantum authentication would justify transitional
   support for standalone ML-DSA certificates in browser root-store
   policy while standalone MTC deployment capabilities mature.  The
   scope is limited to enterprise public websites accessed by unmanaged
   clients using the public Web PKI.  Note: a large enterprise may
   operate many such sites.  The document describes enterprise-managed,
   third-party-hosted, and CDN-fronted deployments, identifies the
   components needed to serve standalone Merkle Tree Certificates
   (MTCs), and examines realistic authentication attack paths and
   migration priorities.  It distinguishes the browser-to-edge
   connection from origin and internal connections, and server
   authentication from identity-provider login.  The document draws on
   initial browser and TLS client testing of Trust Anchor ID signaling,
   and proposes interoperability tests and deployment requirements
   rather than changes to the MTC wire format.  Relative priorities are
   illustrative and not empirical attack probabilities.
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
- **draft-janbjer-div-01** (new-draft, score 9, authorization) [none]: [Deterministic Intent Verification (DIV) Protocol Specification](https://datatracker.ietf.org/doc/draft-janbjer-div/) — This document specifies Deterministic Intent Verification (DIV), a
   transport-independent format for signed action approvals and their
   offline verification.  A relying party reconstructs the signed
   payload from its expected execution parameters, verifies witnesses
   against locally selected trust anchors, and checks the signed
   approval requirement against any locally configured approval policy.
   The specification covers ordinary approvals, offline approvals,
   delegation, agent authority, and platform hash-only intents.
   Cryptographic verification is stateless; enforcing single-use
   execution requires stateful nonce redemption.  A valid signature
   establishes approval of the signed bytes under the selected trust
   policy, not execution of the action or the approver's understanding
   of it.
- **draft-kott-numina-pair-binding-02** (new-draft, score 9, adjacent_watchlist) [none]: [Singularity: Skott34-Ed25519, Universal Companion Model](https://datatracker.ietf.org/doc/draft-kott-numina-pair-binding/) — This document describes a proposed companion format for associating
   two frozen software-artifact commitments with attribution and
   revisioned claims.  It specifies canonical signing bytes, separate
   trust and freshness checks, claim-making and verification procedures,
   and operational state boundaries.  The intended implementing
   community is software-provenance maintainers, release operators and
   independent security reviewers.  Existing IETF canonicalization and
   signature specifications are used without defining a new
   cryptographic primitive.  Retained source comparisons, document-
   signature checks and synthetic tests are indexed with their limits.
   Application control-plane evidence is distinguished from deployment
   of the companion itself.  A complete operational profile,
   independently authenticated trust and current-state evidence, and a
   verified field deployment remain prerequisites to an implementation-
   readiness claim.
- **draft-sergeev-claim-boundaries-02** (new-draft, score 9, trust_infrastructure) [none]: [Claim Boundaries for Execution Evidence](https://datatracker.ietf.org/doc/draft-sergeev-claim-boundaries/) — Systems that act in the world produce logs, receipts, approvals,
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
- **draft-vivek-scim-user-supersession-00** (new-draft, score 9, core_identity) [none]: [SCIM User Supersession and Identity Resolution Correction Events](https://datatracker.ietf.org/doc/draft-vivek-scim-user-supersession/) — The System for Cross-domain Identity Management (SCIM) defines
   resources, provisioning operations, and Security Event Token (SET)
   based events for resource lifecycle changes.  Existing standardized
   SCIM events can signal that a User resource was created, modified,
   activated, deactivated, or deleted, but they do not express an
   identity-resolution decision in which one User resource is retired in
   favor of another User resource representing the same subject within
   the issuer's authority.  Deletion and supersession have different
   semantics for downstream systems.  This document defines two SCIM
   provisioning events: a User supersession event and a supersession-
   correction event.  It distinguishes resource supersession from
   identity-attribute convergence and specifies how ordinary SCIM
   provisioning events communicate the resulting authoritative SCIM
   state of the surviving User.  Matching algorithms, attribute-
   convergence and conflict-resolution policy, identity proofing, and
   non-SCIM data handling remain outside the scope of this document.
   Pre-authentication and pseudonymous profile linkage is identified as
   related future work but is not standardized by this document.
- **draft-zeng-opsawg-applicability-mcp-a2a-01** (new-draft, score 9, adjacent_watchlist) [none]: [When NETCONF Is Not Enough: Applicability of MCP and A2A for Advanced Network Management Scenarios](https://datatracker.ietf.org/doc/draft-zeng-opsawg-applicability-mcp-a2a/) — NETCONF provides robust configuration transactions and YANG-based
   data models, but falls short in scenarios requiring AI-driven
   semantic translation, long-lived cross-domain orchestration, multi-
   agent consensus, rapid DevOps iteration, or delivery of large non-
   configuration artifacts.  This document systematically analyzes the
   functional gaps and presents Model Context Protocol (MCP) and Agent-
   to-Agent (A2A) as complementary solutions.  Implementation guidance
   and coexistence models are also provided.
- **draft-ietf-lamps-csr-attestation-31** (new-draft, score 8, trust_infrastructure) [lamps]: [Use of Remote Attestation with Certification Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) — Certification Authorities (CAs) issuing certificates to Public Key
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
- **draft-mw-oauth-actor-chain-overview-00** (new-draft, score 8, authorization) [none]: [OAuth Actor Chain: Overview and Design](https://datatracker.ietf.org/doc/draft-mw-oauth-actor-chain-overview/) — A request can pass through several services before reaching an API.
   OAuth Token Exchange can represent an actor history in nested act
   claims.  It leaves the rules for constructing that history, limiting
   its disclosure, and verifying an actor's own signature to additional
   profiles.  Actor Chain proposes those rules while keeping the
   Authorization Server responsible for issuing tokens and applying
   policy.

   This document provides a new overview of the authors' Actor Chain
   proposal, whose Internet-Draft lineage began in SPICE in February
   2026.  The companion OAuth Actor Chain: Protocol and Interoperability
   specification continues the existing OAuth draft series and defines
   wire formats and processing requirements.
- **draft-santesson-oidc-cert-auth-context-00** (new-draft, score 8, core_identity) [none]: [Certificate Authentication Context Type for OpenID Connect](https://datatracker.ietf.org/doc/draft-santesson-oidc-cert-auth-context/) — RFC 7773 defines the Authentication Context certificate extension,
   which carries information about how the subject of an X.509
   certificate was authenticated when the certificate was issued.  RFC
   7773 defines one context information type, for subjects authenticated
   by means of a Security Assertion Markup Language (SAML) assertion.
   This document defines a second context information type for subjects
   authenticated by means of OpenID Connect, where the identity
   information is obtained from an ID Token, where applicable in
   combination with a UserInfo Response.  The information is expressed
   as a JSON object and provides the OpenID Connect counterpart to the
   SAML Authentication Context Information defined in RFC 7773.

   This document also updates RFC 7773 by clarifying that an application
   processing the extension ignores context information types it does
   not support regardless of the criticality of the extension, and by
   recommending that the extension not be marked critical.
- **draft-selander-lake-cred-hash-02** (new-draft, score 8, core_identity) [none]: [Hashing Authentication Credentials in LAKE](https://datatracker.ietf.org/doc/draft-selander-lake-cred-hash/) — This document defines a COSE header parameter which signals that an
   authentication credential is replaced by the hash of the
   authentication credential in protocol message computations,
   specifically targeting the Lightweight Authenticated Key Exchange
   (LAKE) protocol specified as RFC 9528.  This further relaxes the need
   for transporting authentication credentials in LAKE, which reduces
   protocol message sizes and improves performance in constrained
   networks.
- **draft-sergeev-audit-task-requirements-00** (new-draft, score 8, authorization) [none]: [Task-Relative Evidence Requirements for Agent Auditing](https://datatracker.ietf.org/doc/draft-sergeev-audit-task-requirements/) — Agent auditing can rely on information produced by users, agents,
   tools, services, policy components, and other systems across multiple
   administrative domains.  The evidence needed to answer one auditing
   question is not necessarily the evidence needed to answer another.
   Successful verification of available evidence also does not, by
   itself, establish that the evidence is applicable or sufficient for
   the question being evaluated.

   This document describes a representation-independent model for
   stating an Audit Task, alternative evidence requirements for that
   task, expectations about evidence production, and the basis for an
   audit result.  It distinguishes verification of evidence from
   evaluation of the Audit Task, missing evidence from a negative
   observation, and validity of individual records from cross-domain
   sufficiency.  It defines no audit record format, verification
   mechanism, authorization model, completeness mechanism, storage
   protocol, or auditing policy.
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
- **draft-zhang-dmsc-gateway-directory-sync-02** (new-draft, score 8, authorization) [none]: [Gateway Capability Directory and Synchronization for Internet of Agents](https://datatracker.ietf.org/doc/draft-zhang-dmsc-gateway-directory-sync/) — This document describes a gateway capability-directory framework for
   Internet of Agents deployments that maintain persistent capability
   views and exchange selected information across gateways.  It defines
   requirements for Agent Capability Specifications (ACSs), derived
   Capability Digests, lifecycle state, provenance, validation, and
   synchronization.  It clarifies authority-scoped revisions, remaining-
   lifetime preservation, withdrawal handling, partial views, and
   recovery after disconnection or state loss.

   The framework distinguishes source descriptions from gateway-accepted
   objects and distinguishes directory visibility from semantic
   compatibility, authorization, and execution admission.  It does not
   define a discovery query protocol, ranking algorithm, storage
   substrate, distributed lookup algorithm, synchronization wire format,
   task orchestration protocol, or agent session protocol.  It provides
   requirements that can inform subsequent gateway procedures and
   protocol bindings.
- **draft-gruszka-signed-evaluation-receipts-03** (new-draft, score 7, trust_infrastructure) [none]: [Signed Evaluation Receipts](https://datatracker.ietf.org/doc/draft-gruszka-signed-evaluation-receipts/) — This document defines a Signed Evaluation Receipt: one JSON object
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

- **draft-eckert-anima-services-dns-autoconfig-07** (new-draft, score 6, core_identity) [none]: [Autoconfiguration of infrastructure services in ACP networks via DNS-SD over GRASP](https://datatracker.ietf.org/doc/draft-eckert-anima-services-dns-autoconfig/) — This document defines standards that enable autoconfiguration of
   fundamental centralized or decentralized network infrastructure
   services on ACP network nodes via GRASP.  These are primarily the
   services required for initial bootstrapping of a network but will
   persist through the lifecycles of the network.  These services
   include secure remote access to zero-touch bootstrapped ANI devices
   via SSH/Netconf with Radius/Diameter authentication and authorization
   and provides lifecycle autoconfiguration for other crucial services
   such as syslog, NTP (clock synchronization) and DNS for operational
   purposes.
- **draft-farrel-dawn-terminology-05** (new-draft, score 6, agent_identity) [none]: [Terminology for the Discovery of Agents With Names (DAWN)](https://datatracker.ietf.org/doc/draft-farrel-dawn-terminology/) — The proliferation of distributed systems, Artificial Intelligence
   (AI) agents, cloud workloads, and network services has created a need
   for interoperable mechanisms to discover entities.  Entities may
   include AI agents, software services, compute workloads, and other
   named resources that need to be found and characterised before
   interaction can begin.

   This document defines terminology for Discovery of Agents With Names
   (DAWN), focusing on the terms necessary to describe the discovery of
   information about AI systems and resources (e.g., AI agents).  The
   intention is that this common set of terms can be used by other
   documents related to DAWN and so achieve consistency of meaning
   across the space.
- **draft-forten-oauth-scope-metadata-document-00** (new-draft, score 6, authorization) [none]: [OAuth Scope Metadata Document](https://datatracker.ietf.org/doc/draft-forten-oauth-scope-metadata-document/) — This document describes how an OAuth scope value that is an HTTPS URI
   can be dereferenced to obtain a JSON document describing that scope.
   The document is descriptive only and does not change the
   authorization meaning of the scope.  Dereferencing follows the
   pattern and security rules of the OAuth Client ID Metadata Document.

About This Document

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Web Authorization
   Protocol Working Group mailing list (mailto:oauth@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/oauth/.
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
- **draft-ietf-jose-deprecate-none-rsa15-07** (new-draft, score 6, verifiable_claims) [jose]: [JOSE: Deprecate 'none' and 'RSA1_5'](https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/) — This document updates RFC 7518 to deprecate the JWS algorithm "none"
   and the JWE algorithm "RSA1_5".  These algorithms have known security
   weaknesses.  It also updates the Review Instructions for Designated
   Experts to establish baseline security requirements that future
   algorithm registrations are expected to meet.
- **draft-ietf-lamps-attestation-freshness-09** (new-draft, score 6, trust_infrastructure) [lamps]: [Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/) — When an end entity includes attestation statements in a Certificate
   Signing Request (CSR), the freshness of the conveyed Evidence often
   needs to be established.  A common mechanism is a nonce that is
   obtained from a Relying Party or Verifier and included by the
   Attester in the Evidence.

   This document specifies how an end entity requests such an
   attestation freshness nonce from an RA/CA when using certificate
   lifecycle management protocols.  It defines message formats and
   protocol bindings for the conveyance of nonce request and response
   messages in the Certificate Management Protocol (CMP), Enrollment
   over Secure Transport (EST), and Certificate Management over CMS
   (CMC), including optional type-specific information needed to produce
   fresh Evidence for inclusion in a CSR.
- **draft-ietf-privacypass-batched-tokens-09** (new-draft, score 6, privacy_security) [privacypass]: [Batched Token Issuance Protocol](https://datatracker.ietf.org/doc/draft-ietf-privacypass-batched-tokens/) — This document specifies two variants of the Privacy Pass issuance
   protocol that allow for batched issuance of tokens.  These allow
   clients to request more than one token at a time and for issuers to
   issue more than one token at a time.
- **draft-khandelwal-bmwg-agent-memory-integrity-02** (new-draft, score 6, agent_identity) [none]: [A Benchmarking Method for the Integrity of AI Agent Memory at Rest](https://datatracker.ietf.org/doc/draft-khandelwal-bmwg-agent-memory-integrity/) — AI agents increasingly persist memory across sessions and treat that
   memory, on the next turn, as if it were their own prior experience.
   This document defines a benchmarking method that measures whether an
   agent's memory subsystem detects that its persisted memory has been
   altered, removed, reordered, replayed, or forged at the storage
   layer, and refuses to serve that memory or reports it before it is
   served.  The method defines nine storage-level edits, three verdict
   classes, a detection-point distinction between read time and audit
   time, three control cases, and a scoring rule.  It is a laboratory
   method for controlled, reproducible measurement, in the spirit of RFC
   2544 and RFC 8239, and it is intended as a test method for the
   "Protection of Memory Data Integrity" metric under discussion in the
   Benchmarking Methodology Working Group.  This revision adds a ninth
   edit, rollback of the whole store to an older genuine copy, which
   separates an integrity head kept beside the records from one anchored
   outside the store; reports the method's results as thirty-one rows on
   released memory subsystems, eighteen of which claim tamper evidence;
   and describes the machine-readable record in which a result set is
   published so that an unrelated party can recompute it.
- **draft-king-dawn-requirements-02** (new-draft, score 6, agent_identity) [none]: [Requirements for the Discovery of Agents With Names (DAWN)](https://datatracker.ietf.org/doc/draft-king-dawn-requirements/) — The proliferation of distributed systems, Artificial Intelligence
   (AI) agents, and network services has created a need for
   interoperable mechanisms to discover entities across administrative
   and network boundaries.  Entities may include AI agents, software
   services, and other named resources that need to be found and
   characterised before interaction can begin.

   This document defines the requirements for Discovery of Agents With
   Names (DAWN) and sets out the objectives that a discovery mechanism
   for such entities must satisfy.  It describes what information must
   be discoverable, what properties a discovery mechanism needs to
   support, and what constraints apply to discovery in decentralised
   environments.

   This document does not specify any particular discovery protocol or
   solution.
- **draft-linker-diem-adem-core-02** (new-draft, score 6, authorization) [none]: [An Authentic Digital, Distinctive EMblem (ADEM) - Message Format and Authorization Model](https://datatracker.ietf.org/doc/draft-linker-diem-adem-core/) — In times of armed conflict, the emblems recognized under
   International Humanitarian Law (IHL), such as the red cross, red
   crescent, and red crystal, are used to mark physical assets.  This
   enables, e.g., the military to identify assets that enjoy specific
   protections under IHL during their operations.  This draft specifies
   the message format and authorization model for a digital emblem,
   which signals that network-connected services enjoy specific
   protections under IHL.
- **draft-linker-diem-adem-dns-02** (new-draft, score 6, authorization) [none]: [An Authentic Digital, Distinctive EMblem (ADEM) - Distribution and Discovery over the DNS](https://datatracker.ietf.org/doc/draft-linker-diem-adem-dns/) — The ADEM Core Specification specifies the message format and
   authorization model for digital, distinctive emblems.  This document
   specifies how such emblems can be used to mark domain names and how
   they can be conveyed over the DNS.
- **draft-watts-agentic-authority-graph-validation-00** (new-draft, score 6, authorization) [none]: [Agentic Authority Graph Validation: A Non-Vacuous Interchange Profile for Revocation-Cut Analysis](https://datatracker.ietf.org/doc/draft-watts-agentic-authority-graph-validation/) — Agentic and delegated systems can represent authority as a graph
   whose paths terminate at consequential resources.  Abstract graph
   models are useful, but interoperable validation requires a machine-
   readable representation and deterministic rules that do not
   accidentally accept vacuous or incomplete graphs.  This document
   defines Agentic Authority Graph Validation (AAGV), a JSON interchange
   profile and validation algorithm for authority roots, consequential
   sinks, declared normal paths, revocation cut sets, and snapshot edge
   state.  AAGV deliberately distinguishes structural cut validity from
   operational closure.  It rejects missing sink sets, missing normal-
   path inventories, dangling references, non-dominating cuts, and non-
   revocable cut edges; it returns INDETERMINATE rather than CLOSED when
   relevant edge state is unknown.  AAGV does not define an
   authorization token, discover hidden paths, or prove physical
   containment.
- **draft-zhang-dawn-agent-discovery-framework-08** (new-draft, score 6, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — This document describes a two-layer reference architecture for
   discovering the minimum public information needed to reach AI agents.
   The Local Discovery Plane obtains discovery information within an
   administrative domain through mDNS/DNS-SD or infrastructure-assisted
   discovery.  The Federation Plane uses DNS as its baseline for cross-
   domain discovery: Federation Gateways apply export policy, publish
   permitted information in independently administered DNS zones, and
   retrieve, validate, and cache remote information on demand.  The
   framework also provides non-DNS mechanisms and mixed-mode deployments
   on the Federation Plane which can complement the baseline with
   proactive distribution, recipient-specific sharing, and directory
   lookup.
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
- **draft-dunbar-dawn-infra-assisted-discovery-02** (new-draft, score 5, agent_identity) [none]: [Infrastructure-Assisted Discovery for AI Agents](https://datatracker.ietf.org/doc/draft-dunbar-dawn-infra-assisted-discovery/) — This document describes an infrastructure-assisted approach
   to AI-agent discovery. An orchestration, placement, or
   hosting system can publish current deployment and
   reachability information for available AI-agent services or
   instances. Separately, network infrastructure can derive an
   abstract Attachment Scope representing the network context
   applicable to a requester. A discovery mechanism combines
   requester intent, currently published AI-agent resources, and
   the requester's Attachment Scope to identify applicable agent
   instances.
- **draft-janbjer-dewp-01** (new-draft, score 5, adjacent_watchlist) [none]: [Deterministic Evidence & Witness Protocol (DEWP) Specification](https://datatracker.ietf.org/doc/draft-janbjer-dewp/) — This document specifies the Deterministic Evidence and Witness
   Protocol (DEWP), a format for tamper-evident audit commitments and
   offline evidence verification.  It defines canonical event preimages,
   domain-separated hashing, two-tier Merkle inclusion proofs, per-
   tenant sequence checks, checkpoint continuity, and independently
   verifiable anchor evidence.  Verifiers report content, commitment,
   embedded-signature, and anchor verification separately.  Completeness
   checks cover committed events within the evaluated range; they cannot
   prove that an event was never withheld before commitment or that a
   committed description accurately records a real-world action.
   Version 1.1 adds execution evidence: a record that an approved action
   was dispatched, statements signed by independent evidence sources
   about whether it took effect, and a status a verifier derives under
   its own trust; that status reports what a trusted source observed,
   not what physically happened.  The specification also defines a
   streaming format that the reference implementations do not yet
   implement.
- **draft-konda-agentproto-evaluation-state-02** (new-draft, score 5, authorization) [none]: [Preserving Evaluation State in Agent Protocol Decisions](https://datatracker.ietf.org/doc/draft-konda-agentproto-evaluation-state/) — Agent protocols often require a participant to establish a decision-
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
   audit documents can satisfy them in their own formats.  Test cases
   for the requirements are included, with a machine-readable form
   published separately.
- **draft-li-pearg-fhe-use-cases-00** (new-draft, score 5, adjacent_watchlist) [none]: [Fully Homomorphic Encryption Use Cases and Gap Analysis for Network Services](https://datatracker.ietf.org/doc/draft-li-pearg-fhe-use-cases/) — This document analyzes network-service use cases in which fully
   homomorphic encryption (FHE) can address privacy requirements not met
   by existing non-homomorphic-encryption solutions under the stated
   trust conditions.  It considers general AI inference, integrated
   sensing and communication, and private information retrieval.  Each
   use case describes a scenario, example flows, post-conditions,
   existing solutions, and potential requirements.  Common gaps, a use-
   case summary, and brief evaluation criteria connect the analysis.
   The document does not specify a protocol or select a cryptographic
   scheme.
- **draft-wang-emu-fs-reauth-03** (new-draft, score 5, core_identity) [none]: [Forward Secure Reauthentication in the Extensible Authentication Protocol Method for Authentication and Key Agreement (EAP-AKA')](https://datatracker.ietf.org/doc/draft-wang-emu-fs-reauth/) — This draft specifies an update to RFC 9678, "Forward Secrecy
   Extension to the Improved Extensible Authentication Protocol Method
   for Authentication and Key Agreement (EAP-AKA' FS)".  This update
   enables forward security of the Transient EAP Keys (TEKs) for
   protecting EAP packets, which are not in EAP-AKA' FS.  Based on this
   extension, the executions of reauthentication after a full
   authentication will be unlinkable to each other and then the privacy
   of end users is enhanced.  This update is also applicable to the
   successors of RFC 9678, with post-quantum key encapsulation
   mechanisms (KEMs) or hybrid KEMs.
- **draft-watts-gov-verification-promotion-boundaries-00** (new-draft, score 5, agent_identity) [none]: [Government-Oriented Verification Promotion Boundaries for Agentic Assurance Profiles](https://datatracker.ietf.org/doc/draft-watts-gov-verification-promotion-boundaries/) — Government and critical-infrastructure relying parties require
   explicit boundaries between successive assurance claims.  This
   document defines Verification Promotion Boundaries (VPB) as a
   protocol-neutral profile that prevents verification evidence obtained
   at one stage from being silently promoted to a stronger claim.  The
   stages are REGISTERED, SPEC_VALIDATED, LOCAL_CONFORMANT,
   INDEPENDENTLY_REPRODUCED, SECURITY_TESTED, and RELEASE_ELIGIBLE.  A
   local PASS does not imply independent reproduction; an independent
   reproduction does not imply security testing; and no stage implies
   endorsement by any standards body or government agency.  The profile
   further distinguishes subject evidence (negative findings against the
   tested artifact) from verifier evidence (positive findings that the
   verification system correctly detected defects).  Arithmetic and
   protocol preconditions, including on-curve validation before
   metamorphic fixtures, are mandatory before any promotion.  This
   document is intended for high-assurance government deployments and is
   not a U.S.  Government standard.
- **draft-wildfeuer-rapp-1-00** (new-draft, score 5, core_identity) [none]: [RAPP/1: The RAPP Protocol Suite](https://datatracker.ietf.org/doc/draft-wildfeuer-rapp-1/) — RAPP/1 is a profile over existing standards that lets independent
   programs exchange verifiable, content-addressed records about agents:
   one canonicalization (JCS), one domain-separated hash, one mint-once
   identity, one eleven-key event envelope, one wire, and one package
   format.  Two independent implementations that follow this document
   produce byte-identical artifacts with no out-of-band agreement.  The
   normative text of record is the append-only specification chain
   published by the author; this document is a stable, archival
   rendering of it: revision rev-18, chain frame
   83bec7762a04959dc91e252055d79f67690c605383018d23b26b99982916dd6a,
   normative SHA-256
   e81e20ba9402ee96422f73e9ef737eba100264155c8f77521600766be8fb21e9.
   Any later revision supersedes this rendering; the chain, not this
   document, says which is current.
- **draft-xg-payment-dispute-profile-01** (new-draft, score 5, adjacent_watchlist) [none]: [Card-Scheme Dispute Evidence Profile of Signed Decision Receipts](https://datatracker.ietf.org/doc/draft-xg-payment-dispute-profile/) — This document profiles draft-farley-acta-signed-receipts, "Signed
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
- **draft-zhang-dmsc-ioa-semantic-interaction-03** (new-draft, score 5, authorization) [none]: [Ontology-based Semantic Interaction for Internet of Agents](https://datatracker.ietf.org/doc/draft-zhang-dmsc-ioa-semantic-interaction/) — This document specifies an ontology-based semantic profile for
   expressing capabilities, intents, tasks, and domain context in agent
   interactions.  It defines a core vocabulary, a JSON-LD serialization
   profile, and processing rules for determining semantic compatibility
   using explicit identifiers, applicable constraints, and accepted
   alignment artifacts.  It distinguishes descriptive metadata and
   candidate mapping suggestions from semantic values used in decisions.
   The profile can be carried by existing discovery and interaction
   mechanisms; it does not define an authorization, transport, session,
   or directory synchronization protocol.  Deterministic processing is
   limited to the declared profile, versions, constraints, and accepted
   mappings, and does not imply automatic interpretation of arbitrary
   natural-language content.
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
- **draft-koenig-idmandat-credential-00** (new-draft, score 4, adjacent_watchlist) [none]: [A Machine-Readable Credential for the Agents of a Company (ID MANDAT)](https://datatracker.ietf.org/doc/draft-koenig-idmandat-credential/) — Automated software agents increasingly act for companies: they ask
   for quotes, book appointments and place orders.  A recipient can
   verify, for example with Web Bot Auth, that a request was signed by
   the holder of a key.  That does not tell the recipient which company
   stands behind the agent or what the agent is allowed to do on its
   behalf.  This document describes a small credential file that a
   company publishes on its own domain under /.well-known/idmandat.json,
   a DNS TXT record that links the file to the domain, and the answer
   format of a public registry that checks both and reports the result
   in a digitally signed response.  The credential states, by
   declaration of the company, which agents act for it and what each
   agent may and may not do.  It does not make claims about
   creditworthiness, trustworthiness or quality.
- **draft-oga-musubi-settlement-01** (new-draft, score 4, adjacent_watchlist) [none]: [MUSUBI Settlement: Recomputing Whether an Agent Acted Within a Signed Grant](https://datatracker.ietf.org/doc/draft-oga-musubi-settlement/) — MUSUBI settlement is a deterministic function that takes a contract
   signed by two parties, a set of signed records of what an agent did
   under that contract, and a view of Bitcoin block headers, and
   computes whether the recorded acts stayed within the grant the
   contract gives.  Anyone holding the same bytes can recompute the
   result without trusting the party that produced it.  This document
   specifies one well defined part of that function, settle core v0,
   precisely enough that a second implementation can be written from the
   text and the published test vectors alone.  Settlement is not runtime
   enforcement and is not a judgement of liability.
- **draft-shah-agent-readiness-evaluation-00** (new-draft, score 4, adjacent_watchlist) [none]: [A Standards-Grounded Method for Evaluating Website Agent-Readiness](https://datatracker.ietf.org/doc/draft-shah-agent-readiness-evaluation/) — This document defines a method for evaluating the "agent-readiness"
   of a website: a measure of how well the site supports autonomous AI
   agents and generative-search crawlers that consume it without a human
   in the loop.  The method is grounded entirely in published standards.
   It organizes observable server behavior into four evaluation pillars,
   each mapped to specific IETF RFCs and W3C specifications covering
   agent discoverability, semantic entity grounding, content efficiency
   and ingestion, and transport.  From the per-pillar observations it
   derives a single deterministic weighted score between 0 and 100.  The
   score formula and its pillar weights are a reproducible scoring
   convention defined by this document; they are a measurement
   convention and are not themselves a standard.  The method is
   diagnostic: it observes and reports conformance to existing
   specifications and changes no protocol.  It is a measurement method,
   not a new protocol and not an enforcement mechanism.  Community and
   vendor conventions that are not standards are observed only as
   supplementary signals and are clearly identified as such.  A running
   reference implementation that performs these checks exists and is
   referenced as running code.
- **draft-singh-rajput-rnp-00** (new-draft, score 4, adjacent_watchlist) [none]: [Rizz Negotiation Protocol (RNP) Version 1.0](https://datatracker.ietf.org/doc/draft-singh-rajput-rnp/) — This document specifies the Rizz Negotiation Protocol (RNP), version
   1.0 -- a domain-configurable, machine-readable protocol governing
   autonomous AI-to-AI negotiation across any structured decision
   context.  RNP defines a finite action space, a bounded round-based
   state machine, a Competitive Pressure Mechanism (CPM) for multi-
   thread simultaneity, a Context Layer for real-time situational
   intelligence, a Feedback Layer for continuous master data
   improvement, and a Loopback Learning Pipeline that trains agent
   models from observed outcomes.  The protocol is domain-configurable:
   the same state machine and message envelope operate across commerce,
   logistics, task allocation, priority queuing, procurement, SLA
   negotiation, and rewards domains.  RNP was first deployed in
   production within the Rizzentials platform (commerce domain) and is
   designed for enterprise integration with platforms such as SAP,
   Salesforce, and Atlassian Jira.
- **draft-zeng-opsawg-llm-netconf-gap-01** (new-draft, score 4, adjacent_watchlist) [none]: [Gap Analysis of Network Configuration Protocols in LLM-Driven Intent-Based Networking](https://datatracker.ietf.org/doc/draft-zeng-opsawg-llm-netconf-gap/) — Large Language Models (LLMs) are entering network operations through
   natural-language intent interfaces.  Existing south-bound protocols
   (NETCONF, RESTCONF, gNMI, MCP, A2A) were not designed for
   conversational, semantically-rich, multi-agent orchestration.  This
   document provides a systematic gap analysis and identifies extension
   points for each protocol to meet intent-based networking
   requirements.

## Adjacent / watchlist

- **draft-cacciapuoti-qirg-quantum-native-architecture-02** (new-draft, score 3, adjacent_watchlist) [none]: [Quantum-Native Architectural Tenets and Philosophy for the Quantum Internet](https://datatracker.ietf.org/doc/draft-cacciapuoti-qirg-quantum-native-architecture/) — This document extends RFC 9340 by outlining a set of quantum-native
   architectural tenets for the design and evolution of the Quantum
   Internet.  These principles should not be interpreted as dogmas, but
   as pragmatic guidelines and criteria for harnessing the unique
   properties of quantum entanglement within networked systems.  Such
   design perspectives, while departing from aspects of classical
   Internet design, remain aligned with one of its foundational
   insights: the principle of constant change, articulated in RFC 1958.

   The document presents a quantum-native architectural framework that
   adopts an entanglement-packet-switching model and defines the
   architectural role and logical structure of quantum packets, with an
   explicit functional separation between the Quantum Data Plane and
   Quantum Control Plane.  It introduces Quantum Internet Addressing as
   a complementary abstraction for quantum-native control and
   coordination, and Generalized Quantum Forwarding to encompass
   quantum-packet processing and the manipulation of entanglement
   resources.
- **draft-deen-ietf-ipmc-update-04** (new-draft, score 3, adjacent_watchlist) [none]: [Update to Recognize the IETF IPMC as the IETF Trust Successor](https://datatracker.ietf.org/doc/draft-deen-ietf-ipmc-update/) — This document updates IETF documents that reference the IETF Trust to
   include the Trust's successor, the IETF Intellectual Property
   Management Corporation.

   Discussion of this draft is on the ipr-wg@ietf.org mailing list.
- **draft-dsmullen-ppd-architecture-11** (new-draft, score 3, adjacent_watchlist) [iotops]: [Privacy Preference Declaration for Home Networks](https://datatracker.ietf.org/doc/draft-dsmullen-ppd-architecture/) — This document describes an architecture for signaling household
   privacy preferences to devices in home networks through Privacy
   Preference Declarations (PPDs).  The architecture enables a PPD
   participant to discover a PPD service endpoint, establish trust in
   that endpoint through the applicable protocol and security profile,
   retrieve the applicable household policy instance, and acknowledge
   receipt of that policy instance.  The acknowledgment establishes that
   a specific policy instance was made available to the participant; it
   does not, by itself, assert anything about the participant's
   subsequent behavior.
- **draft-ehlers-repsec-02** (new-draft, score 3, trust_infrastructure) [none]: [RepSec: Post-Breach Data Neutralisation Protocol](https://datatracker.ietf.org/doc/draft-ehlers-repsec/) — This document introduces RepSec, a post-breach data neutralisation
   protocol designed to reduce the utility of exfiltrated or
   unauthorised data copies.  RepSec operates independently of
   traditional perimeter and access-control security models by enforcing
   conditional data usability based on attestation and environmental
   integrity.  The goal is to limit downstream exploitation, resale
   value, and operational impact of compromised data without disrupting
   legitimate use.
- **draft-ietf-asdf-digital-twin-06** (new-draft, score 3, adjacent_watchlist) [asdf]: [Semantic Definition Format (SDF) Modeling for Digital Twin](https://datatracker.ietf.org/doc/draft-ietf-asdf-digital-twin/) — This memo specifies SDF modeling for digital twins, i.e., digital
   twin systems, and their things.  An SDF is a format that is used to
   create and maintain data and interaction, and to represent the
   various kinds of data that is exchanged for these interactions.  The
   SDF format can be used to model the characteristics, behavior and
   interactions of things, i.e. physical objects, in digital twins that
   contain things as components.
- **draft-ietf-ccamp-eth-client-te-topo-yang-12** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for Ethernet TE Topology](https://datatracker.ietf.org/doc/draft-ietf-ccamp-eth-client-te-topo-yang/) — This document describes a YANG data model for Ethernet networks when
   used either as a client-layer network of an underlay transport
   network (e.g., an Optical Transport Network (OTN)) or as a transport
   network itself.
- **draft-ietf-cdni-source-access-control-metadata-02** (new-draft, score 3, core_identity) [cdni]: [CDNI Source Access Control Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-source-access-control-metadata/) — This specification provides an alternative to the MI.SourceMetadata
   objects defined in RFC8006, providing greatly extended capabilities
   with regards to defining multiple sources, load balancing, and
   failover rules across those sources, as well as a mechanism for a
   content delivery network (CDN) to monitor source health and pull
   unhealthy sources out of rotation.  Additionally, new methods are
   defined for authentication access to an upstream source/origin.
- **draft-ietf-dkim-dkim2-spec-07** (new-draft, score 3, adjacent_watchlist) [dkim]: [DomainKeys Identified Mail Signatures v2 (DKIM2)](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-spec/) — DomainKeys Identified Mail v2 (DKIM2) permits a person, role, or
   organization that owns a signing domain to document that it has
   handled an email message by associating their domain with the
   message.  This is achieved by providing a hash value that has been
   calculated on the current contents of the message and then applying a
   cryptographic signature that covers the hash values and other details
   about the transmission of the message.  Verification is performed by
   querying an entry within the signing domain's DNS space to retrieve
   an appropriate public key.  As a message is transferred from author
   to recipient, systems that alter the body or header fields will
   provide details of their changes and calculate new hash values.
   Further signatures will be added to provide a "chain" that receivers
   can validate.  This permits verifiers to identify the nature of
   changes made by intermediaries and apply a reputation to the systems
   that made changes.  DKIM2 also allows recipients to detect when
   messages have been unexpectedly "replayed" and will ensure that
   Delivery Status Notifications are only sent to entities that were
   involved in the transmission of a message.
- **draft-ietf-dmm-udp-tunnel-acaas-extn-03** (new-draft, score 3, adjacent_watchlist) [dmm]: [A YANG Data Model Extension for Attachment Circuit as a Service with UDP Tunnel Support](https://datatracker.ietf.org/doc/draft-ietf-dmm-udp-tunnel-acaas-extn/) — Delivery of network services over a Layer 3 tunnel assumes that the
   appropriate setup is provisioned over links that connect the customer
   termination points and provider network.  The required setup to allow
   successful data exchange over these links is referred to as an
   attachment circuit (AC) while the underlying link for carrying
   network services is referred to as "bearer", in this case a Layer 3
   UDP tunnel.

   This document specifies an extension for UDP tunnel as Layer 3 bearer
   to the YANG service data model for AC.
- **draft-ietf-dnsop-rfc9364bis-02** (new-draft, score 3, core_identity) [dnsop]: [DNS Security Extensions (DNSSEC)](https://datatracker.ietf.org/doc/draft-ietf-dnsop-rfc9364bis/) — This document describes the DNS Security Extensions (commonly called
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
- **draft-ietf-httpbis-connect-tcp-16** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP tunneling using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this tunneling functionality has several
   important deficiencies due to the lack of a well-defined HTTP origin
   or path.  This specification defines an alternative HTTP proxy
   service configuration for TCP connections.  This configuration is
   described by a URI Template, similar to the CONNECT-UDP and CONNECT-
   IP protocols.
- **draft-ietf-httpbis-resumable-upload-14** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
- **draft-ietf-idr-bgp-model-22** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Model for Border Gateway Protocol (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) — This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.
- **draft-ietf-jmap-calendars-33** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-jmap-metadata-04** (new-draft, score 3, core_identity) [jmap]: [JMAP Object Metadata](https://datatracker.ietf.org/doc/draft-ietf-jmap-metadata/) — This document defines an extension to the JSON Meta Application
   Protocol (JMAP) that lets clients and servers attach metadata to
   objects of existing JMAP data types.  Each data type the server lists
   gains two new properties, metadata and privateMetadata, whose values
   are objects keyed by _namespace identifier_. A namespace identifier
   is either a name registered with IANA or a domain name controlled by
   the vendor providing the namespace; the latter allows vendors and
   applications to extend the metadata schema without prior
   coordination.  Because metadata is carried as a property on the
   related object, clients use the existing /get, /set, /changes, and
   /query methods to read, modify, and synchronize it.
- **draft-ietf-lamps-cms-composite-kem-04** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-kem/) — Composite ML-KEM defines combinations of Module-Lattice-based Key
   Encapsulation Mechanism (ML-KEM) with RSA-OAEP, ECDH, X25519, and
   X448.  This document specifies the conventions for using Composite
   ML-KEM algorithms with the Cryptographic Message Syntax (CMS) using
   the KEMRecipientInfo structure defined in “Using Key Encapsulation
   Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)”
   (RFC 9629).
- **draft-ietf-lamps-pq-composite-kem-23** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/) — This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.
- **draft-ietf-lsr-algorithm-related-adjacency-sid-09** (new-draft, score 3, core_identity) [lsr]: [Algorithm Related IGP-Adjacency SID Advertisement](https://datatracker.ietf.org/doc/draft-ietf-lsr-algorithm-related-adjacency-sid/) — The SR policy architecture defines the Prefix-SID algorithm, with an
   algorithm identifier included in the Prefix-SID advertisement.
   However, the Prefix-SID algorithm does not address scenarios where
   multiple algorithms share the same link resources.  This document
   proposes adding the algorithm identifier in an Adjacency-SID
   advertisement.
- **draft-ietf-mailmaint-imap-objectid-bis-08** (new-draft, score 3, core_identity) [mailmaint]: [IMAP Extension for Object Identifiers](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-imap-objectid-bis/) — This document defines the OBJECTID+ extension for IMAP, which
   obsoletes [RFC8474].  OBJECTID+ introduces a compound OBJECTID
   response format that bundles object identifiers into key-value pairs,
   an ACCOUNTID identifier for account-level context, OBJECTID response
   codes for the RENAME command, and identifier-based mailbox selection
   via SELECT and EXAMINE.  The OBJECTID+ extension is activated
   implicitly when a client uses any OBJECTID+-specific feature,
   ensuring backward compatibility with clients that only support
   [RFC8474].  This document also updates [RFC9698]: when JMAPACCESS is
   advertised alongside OBJECTID+, ACCOUNTID values MUST correspond to
   JMAP accountIds.
- **draft-ietf-masque-connect-ethernet-18** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document specifies how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.  The protocol does not guarantee in-order frame
   delivery.
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
- **draft-ietf-nmop-network-incident-yang-20** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
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
- **draft-ietf-pim-evpn-multicast-yang-08** (new-draft, score 3, adjacent_watchlist) [pim]: [Yang Data Model for EVPN multicast](https://datatracker.ietf.org/doc/draft-ietf-pim-evpn-multicast-yang/) — This document describes a YANG data model for EVPN multicast services.
The model is agnostic of the underlay as well as RFC 9251. This
document mainly focuses on EVPN instance framework.
- **draft-ietf-sidrops-aspa-verification-29** (new-draft, score 3, authorization) [sidrops]: [BGP AS_PATH Verification Based on Autonomous System Provider Authorization (ASPA) Objects](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) — This document describes procedures that make use of Autonomous System
   Provider Authorization (ASPA) objects in the Resource Public Key
   Infrastructure (RPKI) to verify the Border Gateway Protocol (BGP)
   AS_PATH attribute of advertised routes.  This AS_PATH verification
   enhances routing security by adding means to detect and mitigate
   route leaks and AS_PATH manipulations.
- **draft-ietf-sidrops-rtr-yang-12** (new-draft, score 3, adjacent_watchlist) [sidrops]: [YANG Data Model for RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rtr-yang/) — This document defines YANG data models for managing Resource Public
   Key Infrastructure (RPKI) to Router Protocol (RFC6810 and RFC8210).
- **draft-ietf-spring-sr-for-enhanced-vpn-12** (new-draft, score 3, core_identity) [spring]: [Segment Routing based Network Resource Partition (NRP) for Enhanced VPN](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-for-enhanced-vpn/) — Enhanced VPNs aim to deliver VPN services with enhanced
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
   NRPs, which provide the network topology and resource attributes
   required by one or a group of enhanced VPN services.

   This document describes an approach to build SR based NRPs using
   resource-aware SIDs.  The SR based NRP can be used to deliver
   enhanced VPN services in SR networks.
- **draft-ietf-spring-srv6-path-segment-16** (new-draft, score 3, core_identity) [spring]: [Path Segment Identifier (PSID) in SRv6 (Segment Routing in IPv6)](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-path-segment/) — Segment Routing (SR) allows for a flexible definition of end-to-end
   paths by encoding an ordered list of instructions, called "segments".
   The SR architecture can be implemented over an MPLS data plane as
   well as an IPv6 data plane.

   Currently, Path Segment Identifier (PSID) has been defined to
   identify an SR path in SR-MPLS networks, and is used for various use-
   cases such as end-to-end SR Path Protection and Performance
   Measurement (PM) of an SR path.  This document defines the PSID to
   identify an SRv6 path in an IPv6 network.
- **draft-ietf-teas-rsvp-hmac-sha2-02** (new-draft, score 3, core_identity) [teas]: [RSVP Cryptographic Authentication with HMAC-SHA2](https://datatracker.ietf.org/doc/draft-ietf-teas-rsvp-hmac-sha2/) — This document specifies the use of the US NIST Secure Hash Standard
   in the Hashed Message Authentication Code (HMAC) mode with RSVP
   Cryptographic Authentication version 2.  Along with draft-ietf-teas-
   rsvp-auth-v2, this document obsoletes RFC2747 and RFC3097.
- **draft-ietf-tls-key-share-prediction-05** (new-draft, score 3, adjacent_watchlist) [tls]: [TLS Key Share Prediction](https://datatracker.ietf.org/doc/draft-ietf-tls-key-share-prediction/) — This document defines a mechanism for servers to communicate
   supported key share algorithms in DNS.  Clients may use this
   information to reduce TLS handshake round-trips.
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-32** (new-draft, score 3, adjacent_watchlist) [v6ops]: [Framework for Multi-domain IPv6-only Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — This document presents a framework, from the network operators'
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
- **draft-liu-opsawg-ipfix-igp-algo-02** (new-draft, score 3, core_identity) [none]: [Export of IGP Algorithm Information in IPFIX](https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/) — This document introduces a new IPFIX information element (IE) to
   identify the IGP Algorithm information related with the Segment
   Identifier (SID) or the IPv4/IPv6 prefix.
- **draft-lnehru-lisp-silenthost-detection-01** (new-draft, score 3, adjacent_watchlist) [none]: [LISP Silent Host Discovery using the Mapping System](https://datatracker.ietf.org/doc/draft-lnehru-lisp-silenthost-detection/) — The on-demand discovery model of the Locator/ID Separation Protocol
   (LISP) is ineffective for "silent hosts", endpoints that do not
   initiate traffic.  This is a common challenge in environments like
   manufacturing and IoT environments, where low-power devices
   frequently go silent to conserve energy.  This document proposes a
   mechanism to discover these hosts by using the LISP mapping system
   itself. xTRs that are able to probe a given EID prefix register that
   capability with the Map-Server.  When a Map-Request for an unknown
   destination arrives at the Map-Server, it is forwarded and replicated
   to all xTRs that have registered the covering EID prefix, initiating
   a controlled, on-demand discovery process for that specific host.  In
   traditional broadcast-based networks, operators are often unaware of
   the existence of silent hosts and discovery of these hosts relies on
   network flooding.This approach provides a scalable alternative to
   network flooding for locating silent endpoints.
- **draft-netana-ippm-ioam-on-path-delay-00** (new-draft, score 3, adjacent_watchlist) [none]: [IOAM Extensions for On-Path Delay Measurement](https://datatracker.ietf.org/doc/draft-netana-ippm-ioam-on-path-delay/) — This document defines extensions to In Situ Operations,
   Administration, and Maintenance (IOAM) that enable IOAM nodes to
   compute on-path delay samples.  These samples are the basis for the
   on-path delay statistics that can be exported using the IP Flow
   Information Export (IPFIX) Information Elements defined in RFC 9951.

   The document defines an On-Path Delay IOAM data field and extends the
   IOAM Direct Export (DEX) Option-Type with a timestamp reference
   inserted by the IOAM encapsulating node.  These extensions enable
   transit and decapsulating nodes to compute and locally aggregate on-
   path delay.  The resulting on-path delay can then be made available
   by different mechanisms, for example IPFIX export or the YANG data
   model for on-path telemetry.
- **draft-ramadan-moq-multicast-00** (new-draft, score 3, core_identity) [none]: [Multicast Delivery and Endpoint Discovery for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-multicast/) — This document specifies multicast delivery mechanisms and catalog-
   based endpoint discovery for Media over QUIC (MoQ).  It defines how
   MoQ sessions integrate with IP multicast (SSM, ASM), Automatic
   Multicast Tunneling (AMT), and TreeDN for scalable live streaming.
   The specification includes a multicast catalog extension for endpoint
   discovery and multi-path delivery across TV, mobile, and browser
   platforms.  All multicast delivery uses MMTP packets, the same packet
   format used on MoQ QUIC streams and datagrams.  A manifest-based
   content-authentication profile protects multicast delivery.
- **draft-reddy-cose-hpke-hqc-00** (new-draft, score 3, verifiable_claims) [none]: [Hamming Quasi-Cyclic (HQC) Ciphersuites for COSE-HPKE](https://datatracker.ietf.org/doc/draft-reddy-cose-hpke-hqc/) — This document specifies Hamming Quasi-Cyclic (HQC)-based ciphersuites
   for use with COSE-HPKE.  It defines fully specified COSE algorithms
   for HPKE Integrated Encryption and HPKE Key Encryption, using HQC or
   PQ/T hybrid HQC key encapsulation, SHAKE256 key derivation, and AES-
   256-GCM authenticated encryption.  It specifies their AKP key
   representation and requests twelve COSE algorithm registrations.
   Message processing and context binding are inherited from COSE-HPKE.
- **draft-reynolds-foodblock-core-01** (new-draft, score 3, core_identity) [none]: [FoodBlock Core: Signed, Hash-Addressed Blocks for Food Records](https://datatracker.ietf.org/doc/draft-reynolds-foodblock-core/) — FoodBlock is a small data format and a set of checking rules for
   records of food: what was made, moved, promised or allowed, and by
   whom.  A record is a block of three fields (type, state and refs)
   signed by its author.  The identity of a block is the hash of its
   canonical bytes, which are the JSON Canonicalization Scheme (RFC
   8785) applied to a block that also follows a strict writing profile.
   Authors link their blocks into per-key chains.  This document defines
   the block, the canonical form, the signature suites, the chain, the
   messages that carry a block, and the function valid() that decides
   whether a block is sound against the blocks a checker holds.  It is
   the core only: an implementation of this document alone can make,
   sign, check and chain blocks.  Rules for identities, rotation,
   consent, promises, privacy and node-to-node exchange are in separate
   modules that build on this core.
- **draft-rosomakho-tls-secondary-client-auth-00** (new-draft, score 3, core_identity) [none]: [Secondary Client Authentication in TLS 1.3](https://datatracker.ietf.org/doc/draft-rosomakho-tls-secondary-client-auth/) — Some deployments authenticate a client using two certificates, such
   as one identifying a device and another identifying its user.  This
   document defines the secondary_client_certificate TLS flag to
   negotiate one additional client authentication exchange as part of
   connection establishment.  The server sends an additional
   CertificateRequest immediately after its Finished, and the client
   responds after its own handshake Finished and before sending
   application data.  Either certificate response can be empty, and the
   server determines whether the resulting authentication state
   satisfies its policy.

   This document updates RFC 9846 to permit the additional request
   before the server receives the client's Finished.  It also updates
   RFCs 9001 and 9113 to permit this negotiated exchange with QUIC and
   HTTP/2.
- **draft-saez-xcim-01** (new-draft, score 3, authorization) [none]: [eXplicit Consent-Identified Mail (XCIM)](https://datatracker.ietf.org/doc/draft-saez-xcim/) — XCIM specifies experimental evidence linking purpose-specific
   communication authorization to an application, an original email
   recipient, and message content.  A signed receipt records an issuer's
   observation of consent; a receiver also verifies current permission,
   signing authority, freshness, authenticated publication, and DKIM.
   The minimum direct-email profile uses one recipient and purpose per
   message copy, issuer-signed recipient binding, and application-
   authorized message signatures.  This document defines a bounded
   experimental integration and identifies unresolved lifecycle,
   history-continuity, and registration questions.  It does not
   establish the truth of an issuer's consent observation or claim
   production readiness.
- **draft-sidor-pce-binding-label-sid-extensions-04** (new-draft, score 3, core_identity) [none]: [Binding Label/Segment Identifier (SID) Extensions in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-binding-label-sid-extensions/) — The Path Computation Element Communication Protocol (PCEP) provides
   mechanisms for Path Computation Elements (PCEs) to instantiate and
   manage Label Switched Paths (LSPs) on a Path Computation Client
   (PCC).  This includes the ability for a PCE to specify a Binding
   Segment Identifier (SID) for an LSP.

   A binding value specified by a PCE may not be available for use on
   the PCC.  This can lead to LSP instantiation failures or the entire
   PCEP message being rejected.

   This document proposes extensions to PCEP to allow a PCC to fall back
   to allocating a Binding SID from its own dynamic pool if the value
   specified by the PCE is unavailable.  It also defines a mechanism for
   the PCC to report both the requested and the allocated binding values
   back to the PCE.
- **draft-thain-ipv8-03** (new-draft, score 3, adjacent_watchlist) [none]: [Internet Protocol Version 8 (IPv8)](https://datatracker.ietf.org/doc/draft-thain-ipv8/) — This document specifies Internet Protocol Version 8 (IPv8), an
   extension of IPv4 [RFC791] that prepends a 32-bit Route Number (RN)
   to each IPv4 address to produce a 64-bit address space.  IPv4 is a
   proper subset of IPv8: an IPv8 address whose RN is zero is bit-
   identical to an IPv4 address, and IPv4 packets are IPv8 packets whose
   RN is implicitly zero.

   IPv8 is incrementally deployable over existing IPv4 infrastructure.
   Forwarding silicon, BGP4 routing, and operator administrative
   boundaries continue to operate without modification.  IPv8-aware
   behaviour is implemented in software at the edges of forwarding paths
   and signalled through extension mechanisms (BGP large communities,
   IS-IS TLVs, OSPF opaque LSAs) that unupgraded transit elements flood
   transparently and ignore.

   This document defines the IPv8 address format, the textual
   representation conventions including the canonical hyphenated locator
   form, the relationship to IPv4, the architectural principles
   governing the suite, and the security and operational considerations
   applicable to all companion specifications.  Routing-protocol
   behaviour, encapsulation rules, trust mechanisms, and management
   interfaces are specified in companion documents listed in §1.
- **draft-uri-cfrg-pquake-01** (new-draft, score 3, core_identity) [none]: [PQuAKE - Post-Quantum Authenticated Key Exchange](https://datatracker.ietf.org/doc/draft-uri-cfrg-pquake/) — This document describes Post-Quantum Authenticated Key Exchange
   (PQuAKE), a proposed construction for mutual authentication using an
   ephemeral key-encapsulation mechanism (KEM) exchange, encapsulations
   to certified long-term KEM keys, transcript binding, and explicit key
   confirmation.  Its target use case is a constrained link where
   avoiding online post-quantum handshake signatures may reduce
   communication or computation.  An optional pre-shared secret is
   intended to protect encrypted credentials against active outsiders.

   The goal is to specify a compact reference construction and obtain
   CFRG review of its security and applicability, with a view to a
   favorable assessment and publication as an Informational RFC if the
   review supports it.  The document presents the design rationale,
   assumptions, security intuition, and conditions for safe use.  Formal
   analyses reported for the closely related CAKE-HI construction are
   relevant evidence; their applicability to this draft's precise
   messages and algorithms remains to be established.  Protocol-specific
   integration, performance comparisons, and unresolved specification
   details are identified separately.  This individual proposal does not
   represent CFRG consensus or a recommendation to an IETF working
   group.
- **draft-watts-verification-defect-quarantine-00** (new-draft, score 3, adjacent_watchlist) [none]: [Verification Defect Quarantine for Protocol Conformance Systems](https://datatracker.ietf.org/doc/draft-watts-verification-defect-quarantine/) — Protocol conformance systems commonly treat a published test vector
   as an oracle.  When the oracle itself is malformed, internally
   inconsistent, ambiguous, or arithmetically false, an implementation
   can be penalized for rejecting the defect or can be falsely promoted
   for reproducing it.  This document defines Verification Defect
   Quarantine (VDQ), a transport-neutral receipt and fail-closed state
   model for separating the status of the tested subject from the
   demonstrated fault-detection behavior of the verifier.  VDQ records
   reproducible counterexamples, quarantines affected normative vectors
   from assurance promotion, preserves INDETERMINATE when a defect
   cannot yet be reproduced, and supports append-only supersession when
   a specification is corrected.  VDQ does not amend an Internet-Draft
   or RFC, does not replace the RFC Editor errata process, and does not
   by itself establish implementation security.
- **draft-watts-veriflow-evidence-envelope-00** (new-draft, score 3, trust_infrastructure) [none]: [Veriflow Evidence Envelope for Source-Grounded Computational Claims](https://datatracker.ietf.org/doc/draft-watts-veriflow-evidence-envelope/) — This document specifies an experimental, JSON-based evidence envelope
   for exchanging source-grounded computational assertions, including
   provenance, reproducible operation identifiers, evidence sufficiency,
   and explicit abstention when an answer is not supported.  The
   envelope separates syntactic validity, source integrity, mathematical
   correctness, and empirical truth.  This document does not standardize
   a general scientific inference engine or claim experimental
   superiority.
- **draft-xu-intarea-challenge-icmpv4-04** (new-draft, score 3, core_identity) [none]: [Enhancing ICMP Error Message Validation Using a Challenge-Confirm Mechanism](https://datatracker.ietf.org/doc/draft-xu-intarea-challenge-icmpv4/) — ICMP error messages provide feedback used by hosts to manage network
   communication.  Existing validation of the quoted invoking packet is
   essential, but its resistance to blind off-path forgery depends on
   the information quoted and the communication state available to the
   receiver.

   This document describes a Challenge-Confirm mechanism that
   supplements existing ICMP validation.  After an eligible initial
   error passes existing checks, the host can mark the associated flow
   and include an unpredictable token in an IPv4 option of a subsequent
   packet that would otherwise be transmitted.  Receipt of the initial
   error does not immediately generate a probe or a separate ICMP Echo
   Request.  A later ICMP error can return the token by quoting the
   invoking packet.

   The token is computed using a secret local to the validating host.
   No key is shared with routers or peer hosts, and no per-challenge
   nonce cache is required.  Successful token validation provides
   evidence of access to a valid token; it does not authenticate a
   router's identity or the semantics of the reported error.  This
   document specifies bounded triggering, replay limitations, and
   deployment considerations, including the need to evaluate IPv4 option
   traversal and quotation.  It does not report Internet-wide deployment
   measurements.
- **draft-xu-intarea-challenge-icmpv6-04** (new-draft, score 3, core_identity) [none]: [Enhancing ICMPv6 Error Message Authentication Using Challenge-Confirm Mechanism](https://datatracker.ietf.org/doc/draft-xu-intarea-challenge-icmpv6/) — The Internet Control Message Protocol for IPv6 (ICMPv6) is essential
   for network diagnostics but is vulnerable to off-path spoofing
   attacks, especially when error messages relate to stateless transport
   protocols like UDP.  An attacker can forge these messages to degrade
   performance or enable Man-in-the-Middle attacks.

   This document proposes a robust, stateless challenge-response
   mechanism to authenticate ICMPv6 error messages.  Traditional
   stateful challenge mechanisms are vulnerable to state-exhaustion
   Denial-of-Service (DoS) attacks.  To avoid this, the proposed
   solution is inspired by TCP SYN-Cookies, eliminating the need to
   store per-challenge state by using cryptographic computation.  It
   limits state management to minimal flags on existing sockets or a
   bounded probabilistic data structure.  This approach effectively
   authenticates ICMPv6 error messages while inherently resisting both
   off-path spoofing and state-exhaustion DoS attacks, thus improving
   the robustness of ICMPv6.
- **draft-yu-ccamp-sla-assurance-optical-yang-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Service Level Agreement (SLA) Assurance Management in Optical Transport Networks](https://datatracker.ietf.org/doc/draft-yu-ccamp-sla-assurance-optical-yang/) — This document defines a YANG module for SLA assurance management in
   optical transport networks.  The module provides a standard way to
   represent and report issues that may impact service and network
   availability.  It enables consistent reporting of impairments and
   risks across optical transport domains.  The YANG model is designed
   to support closed-loop operations, allowing automated monitoring,
   analysis, and remediation workflows to maintain high service
   reliability and SLA compliance.
- **draft-zcl-pim-multiif-igmp-mld-proxy-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for supporting multipath IGMP/MLD proxies](https://datatracker.ietf.org/doc/draft-zcl-pim-multiif-igmp-mld-proxy-yang/) — The ability to support multiple upstream interfaces in IGMP/MLD
   proxies necessitates configuring different upstream interfaces for
   specific multicast channels or sessions.  [RFC9398] defined YANG Data
   Model for Internet Group Management Protocol (IGMP) and Multicast
   Listener Discovery (MLD) Proxy Devices.  Building on that foundation,
   this document proposes an augmentation of thet model for the support
   of multiple upstream interfaces in IGMP/MLD proxies.
- **draft-zhang-dnssec-wildcard-validation-01** (new-draft, score 3, core_identity) [none]: [Signer-Zone Containment for DNSSEC Wildcard Validation](https://datatracker.ietf.org/doc/draft-zhang-dnssec-wildcard-validation/) — Validators for the DNS Security Extensions (DNSSEC) reconstruct the
   original owner name of a signed resource record set (RRset) using the
   RRSIG Labels field.  If the reconstructed owner is outside the
   signing zone, a cryptographically correct signature can be
   misinterpreted as authenticating wildcard data belonging to another
   zone.  Aggressive use of DNSSEC-validated caches can extend the
   effect to other names.  This document updates RFC 4035 to require
   signer-zone containment of the reconstructed owner and updates RFC
   8198 to preserve that authenticated relationship when reusing
   wildcard data.  These requirements constrain DNSSEC authentication
   and cached reuse.  They do not change DNS wildcard matching or
   synthesis rules, or DNS message formats.
- **draft-zhong-nmop-hcps-anomaly-framework-00** (new-draft, score 3, adjacent_watchlist) [none]: [Framework for High-Dimensional Anomaly Detection of Network Data in Human-Cyber-Physical Systems](https://datatracker.ietf.org/doc/draft-zhong-nmop-hcps-anomaly-framework/) — Human-cyber-physical systems combine human activity, computing and
   communication services, and networked physical processes.  Their
   network data is heterogeneous and high-dimensional.  An abnormal
   condition can appear in the attributes of one entity, in an
   interaction between entities, or only when evidence from several
   domains is considered together.

   This document specifies an initial framework for anomaly detection in
   human-cyber-physical environments.  It describes the functions used
   to inventory observations, construct entity and relation context,
   analyze high-dimensional data, and report an anomaly result.  It also
   defines a small conceptual information model so that anomaly results
   retain their observation scope, feature context, and score meaning.
- **draft-amazing6g-nmrg-mcdm-slice-selection-00** (new-draft, score 2, ignored_after_review) [none]: [A Multi-Criteria Decision Architecture for Intent-Based Network Slice Selection](https://datatracker.ietf.org/doc/draft-amazing6g-nmrg-mcdm-slice-selection/) — This document proposes a two-layer reference architecture -- an
   Intent Extraction Layer and a pluggable Multi-Criteria Decision Layer
   -- for translating natural-language operator intent into network
   slice selection decisions, i.e., ranking among multiple valid
   candidate configurations.  Responding to research challenges
   identified by the NMRG on intent interpretation and on the
   misalignment between AI-internal metrics and network-management
   objectives, the architecture combines explicit handling of unresolved
   intent, plural independently derived decision methods with explicit
   agreement reporting, and human validation checkpoints.  A motivating
   scenario from a prototype illustrates the class of failure the design
   targets.  The architecture is proposed as vertical-agnostic; one
   instance has been prototyped for a Renewable Energy Community
   deployment and is validated in a companion study.
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
- **draft-he-agentproto-verifier-evidence-01** (new-draft, score 2, ignored_after_review) [none]: [Exercise and Completeness Evidence for Agent Protocol Verifier Results](https://datatracker.ietf.org/doc/draft-he-agentproto-verifier-evidence/) — A verifier result reports what a check returned.  It does not report
   whether the check could have returned anything else.  A check that
   inspects too narrow a set of fields, and a check whose rejecting or
   unverifiable input has never occurred, both report the same accepting
   value as a check that distinguishes, and a conformance matrix does
   not tell them apart.

   This document defines requirements for reporting whether a check has
   been exercised into its declared rejecting and unverifiable outcomes,
   and requirements for results that claim completeness: that the
   records relied on were the whole of some stated set.  Those are two
   separate obligations.  A result must name the set it claims to have
   seen, and must not treat a party with an interest in the answer as
   the only thing looking.

   This document defines no wire format, encoding, token, claim
   vocabulary, test harness, or registry.  It does require a record to
   identify certain facts, which is a constraint on what a record must
   be able to express rather than on how it is written down.  A profile
   satisfying these requirements will need a place to put those facts.
- **draft-ietf-lisp-8111bis-01** (new-draft, score 2, ignored_after_review) [lisp]: [Locator/ID Separation Protocol Delegated Database Tree (LISP-DDT)](https://datatracker.ietf.org/doc/draft-ietf-lisp-8111bis/) — This document describes the Locator/ID Separation Protocol Delegated
   Database Tree (LISP-DDT), a hierarchical distributed database that
   embodies the delegation of authority to provide mappings from LISP
   Endpoint Identifiers (EIDs) to Routing Locators (RLOCs).  It is a
   statically defined distribution of the EID namespace among a set of
   LISP control plane elements generically called "DDT Nodes".  Each DDT
   Node is configured as "authoritative" for one or more EID-Prefixes,
   along with the set of RLOCs for Map-Servers or "child" DDT Nodes to
   which more-specific EID-Prefixes are delegated.

   This document obsoletes RFC 8111 and updates RFC 9301.
- **draft-kazuho-quic-delegated-stateless-reset-00** (new-draft, score 2, ignored_after_review) [none]: [Delegating QUIC Stateless Resets](https://datatracker.ietf.org/doc/draft-kazuho-quic-delegated-stateless-reset/) — This document specifies how a QUIC endpoint may delegate the emission
   of Stateless Resets to a component that outlives the QUIC stack --
   for example, an operating system that resets the peers of an
   application that has exited.  As such delegation is most useful on
   the client side, where endpoints often use zero-length Connection
   IDs, this document also defines a transport parameter and a frame
   that allow those clients to advertise a Stateless Reset Token.
- **draft-ranjbar-regext-rdap-subordinate-referrals-02** (new-draft, score 2, ignored_after_review) [none]: [Referrals to Holder-Designated RDAP Services for Subordinate Resources](https://datatracker.ietf.org/doc/draft-ranjbar-regext-rdap-subordinate-referrals/) — An RDAP query can be followed from the IANA bootstrap registries down
   to the most specific object a registry operator holds, and no
   further.  When the holder of a registered resource keeps registration
   data for resources below it, such as names below a registered domain
   or more-specific networks below an address allocation, and publishes
   that data from an RDAP service of its own, a client has no in-band
   way to find that service.  This document describes how a registry
   operator refers clients to such a holder-designated service.  The
   registry redirects lookups for subordinate resources to the holder's
   service, so an unchanged client receives the most specific record as
   it would from any other redirect.  On top of that, the covering
   object can advertise the holder's service, so a client that cares can
   discover the delegation and cross the authority boundary knowingly.
   The document uses the object relations and the redirect controls of
   draft-ietf-regext-rdap-referrals, and defines a family of "rdap-base"
   link relations whose target is the base URL of an RDAP service rather
   than an object.
- **draft-watts-verifiable-scientific-evidence-records-01** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Scientific Evidence Records: A Minimal Integrity Profile](https://datatracker.ietf.org/doc/draft-watts-verifiable-scientific-evidence-records/) — This document specifies a minimal JSON evidence-record profile for
   checking artifact digests and separating integrity verification from
   scientific assessment.  It defines an interoperable record structure,
   validation algorithm, and negative test cases.  It does not assert
   that an integrity-checked scientific claim is true.
- **draft-mk-dnsop-svcb-well-known-01** (new-draft, score 1, verifiable_claims) [none]: [An SVCB Service Parameter for Well-Known URI Paths](https://datatracker.ietf.org/doc/draft-mk-dnsop-svcb-well-known/) — This document defines the "well-known" Service Parameter Key
   (SvcParamKey) for SVCB and HTTPS resource records.  It carries one or
   more well-known URI suffixes, identifying resources under "/.well-
   known/" that are available at the service endpoint.  It specifies the
   presentation and wire formats and requests registration of the key
   with IANA.

## Ignored after review

- **draft-abraitis-idr-addpath-paths-limit-05** (new-draft, score 0, ignored_after_review) [none]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.
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
- **draft-anarayanan-bess-evpn-extended-ip-mobility-00** (new-draft, score 0, ignored_after_review) [none]: [Extended IP mobility procedures for EVPN-IRB](https://datatracker.ietf.org/doc/draft-anarayanan-bess-evpn-extended-ip-mobility/) — [RFC9721] introduces IP mobility procedures for EVPN-IRB that couple
   IP and MAC mobility sequence numbers.  This coupling results in
   excessive control plane churn when a single IP migrates among
   multiple IP addresses associated with a single MAC address.  This
   document proposes separating sequence number spaces for IP mobility
   (MAC-IP routes) and MAC mobility (MAC-only routes), reducing BGP
   updates from O(N) to O(1) when one IP moves among N IPs on a MAC,
   while maintaining full compatibility with an implementation
   conforming to the recommendations of [RFC9721].  Further, this
   document proposes an upgrade path for deployments transitioning to IP
   mobility as defined in [RFC9721] or this draft.
- **draft-besleaga-sustainability-wellknown-09** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI, at
   which a web origin publishes a JSON document declaring the energy
   consumption, carbon footprint, and related environmental and
   sustainability metrics of a target: the organization behind the
   origin, the origin itself, a part of it, a service, a device, or a
   product, for different reporting periods.  The declaration links to a
   methodology and may carry a signature, name the declarations of
   upstream providers, and link to third-party attestations.  The
   metrics are self-asserted claims of the publisher.  This document
   registers the well-known URI and the media type application/
   sustainability-data+json.
- **draft-borshchahivskyi-httpbis-preview-00** (new-draft, score 0, ignored_after_review) [none]: [The Preview HTTP Response Header Field](https://datatracker.ietf.org/doc/draft-borshchahivskyi-httpbis-preview/) — Many applications display a "preview card" for a link: a title, a
   short description and an image.  Today this information is obtained
   by retrieving the full HTML representation of the linked resource and
   extracting metadata from it.  This forces origin servers to generate
   complete pages for clients that need only a few short strings.

   This document defines the Preview HTTP response header field, a
   Structured Field that carries link preview metadata, and describes
   how it can be delivered in responses to HEAD requests so that preview
   generators can obtain it without the origin server generating the
   representation.
- **draft-bsvkey-dtn-custody-receipt-block-01** (new-draft, score 0, ignored_after_review) [none]: [Signed Custody Receipts Carried in a Bundle Protocol Version 7 Extension Block](https://datatracker.ietf.org/doc/draft-bsvkey-dtn-custody-receipt-block/) — This document defines the Custody Receipt Block, a Bundle Protocol
   Version 7 (BPv7) extension block that carries a chain of signed
   custody receipts inside the bundle those receipts describe.  Each
   node that chooses to act as a custodian appends one receipt stating
   that it held the bundle, which node it received it from, and when it
   received and forwarded it.  Nodes that do not implement the block
   forward it unchanged and are never required to read the payload or to
   sign anything.  A verifier holding the custodians' public keys can
   check the chain after the fact and can report, rather than infer, any
   part of the route for which no receipt exists.  The receipts are
   evidence for accounting and dispute resolution between operators.
   They are not Bundle Protocol administrative records and they do not
   replace or modify custody transfer signalling.
- **draft-chen-bier-idr-bier-te-bgp-07** (new-draft, score 0, ignored_after_review) [none]: [BGP extensions for BIER-TE](https://datatracker.ietf.org/doc/draft-chen-bier-idr-bier-te-bgp/) — "Tree Engineering for Bit Index Explicit Replication" (BIER-TE)
   shares architecture and packet formats with BIER.  BIER-TE forwards
   and replicates packets based on a BitString in the packet header, but
   every BitPosition of the BitString of a BIER-TE packet indicates one
   or more adjacencies.

   This document describes BGP extensions for advertising the BIER-TE
   specific information.
- **draft-chen-idr-bgp-ls-algo-related-adjacency-sid-05** (new-draft, score 0, ignored_after_review) [none]: [Algorithm Related Adjacency SID Advertisement](https://datatracker.ietf.org/doc/draft-chen-idr-bgp-ls-algo-related-adjacency-sid/) — This draft describes a mechanism to distribute SR-MPLS algorithm
   Related Adjacency SID from controllers to the headend routers using
   BGP-LS.
- **draft-chen-idr-bgp-ls-sr-policy-cp-validity-04** (new-draft, score 0, ignored_after_review) [none]: [Advertisement of Candidate Path Validity Control Parameters using BGP-LS](https://datatracker.ietf.org/doc/draft-chen-idr-bgp-ls-sr-policy-cp-validity/) — This document describes a mechanism to collect the configuration and
   states of SR policies carrying the validity control parameters of the
   candidate path by using BGP Link-State (BGP-LS) updates.  Such
   information can be used by external components for path computation,
   re-optimization, service placement, etc.
- **draft-chen-idr-bgp-sr-policy-cp-validity-05** (new-draft, score 0, ignored_after_review) [none]: [Validity of SR Policy Candidate Path](https://datatracker.ietf.org/doc/draft-chen-idr-bgp-sr-policy-cp-validity/) — This document defines extensions to BGP to distribute the validity
   control parameters of a candidate path for an SR Policy.
- **draft-chen-pce-sr-policy-cp-validity-04** (new-draft, score 0, ignored_after_review) [none]: [PCEP extension to support Candidate Paths validity](https://datatracker.ietf.org/doc/draft-chen-pce-sr-policy-cp-validity/) — This document defines PCEP extensions for signaling the validity
   control parameters of a candidate path for an SR Policy.
- **draft-chuang-dkim2-sender-policy-04** (new-draft, score 0, ignored_after_review) [none]: [DKIM2 Sender Policy](https://datatracker.ietf.org/doc/draft-chuang-dkim2-sender-policy/) — This document updates DMARC RFC 9989 for DKIM2.  In particular DKIM2
   verification supports MTA relay forwarding with message modifications
   through multiple MTAs, so this updates DMARC to support those
   scenarios as well.  While DMARC defines a RFC 5322 From alignment
   constraint with an enforcement policy if validation fails, this
   generalizes and separates enforcement policy from constraint
   validation policies.  This provides a mechanism for MTAs to declare
   support for DKIM2 through the DMARC DNS policy record that helps
   secure DKIM2 from downgrade attacks.
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
- **draft-davies-internal-tld-07** (new-draft, score 0, ignored_after_review) [none]: [A Top-level Domain for Private Use](https://datatracker.ietf.org/doc/draft-davies-internal-tld/) — This document describes the "internal" top-level domain for use in
   private applications.
- **draft-devalk-redirect-by-01** (new-draft, score 0, ignored_after_review) [none]: [The Redirect-By HTTP Response Header Field](https://datatracker.ietf.org/doc/draft-devalk-redirect-by/) — This document defines the Redirect-By HTTP response header field.  It
   allows the software component whose decision determined an HTTP
   redirect to identify itself, so that an operator diagnosing a
   redirect can determine which component was responsible for it.  The
   field succeeds the widely deployed, non-standard X-Redirect-By
   header, which this document deprecates.
- **draft-dkg-audits-json-01** (new-draft, score 0, ignored_after_review) [none]: [Automated Discovery Of Audit Reports (audits.json)](https://datatracker.ietf.org/doc/draft-dkg-audits-json/) — This document describes a mechanism that an organization can use to
   enable automatic discovery of documents associated with regulatory
   compliance.  It is motivated by regulations that require, for
   example, publicly accessible audits of automated decision-making
   processes in hiring.
- **draft-dsmullen-ppd-protocol-04** (new-draft, score 0, ignored_after_review) [iotops]: [Privacy Preference Declaration Protocol Specification](https://datatracker.ietf.org/doc/draft-dsmullen-ppd-protocol/) — This document specifies a participant-facing protocol for Privacy
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
- **draft-eckert-anima-grasp-dnssd-09** (new-draft, score 0, ignored_after_review) [none]: [DNS-SD Compatible Service Discovery in GeneRic Autonomic Signaling Protocol (GRASP)](https://datatracker.ietf.org/doc/draft-eckert-anima-grasp-dnssd/) — DNS Service Discovery (DNS-SD) defines a framework for applications
   to announce and discover services.  This includes service names,
   service instance names, common parameters for selecting a service
   instance (weight or priority) as well as other service-specific
   parameters.  For the specific case of autonomic networks, GeneRic
   Autonomic Signaling Protocol (GRASP) intends to be used for service
   discovery in addition to the setup of basic connectivity.
   Reinventing advanced service discovery for GRASP with a similar set
   of features as DNS-SD would result in duplicated work.  To avoid
   that, this document defines how to use GRASP to announce and discover
   services relying upon DNS-SD features while maintaining the intended
   simplicity of GRASP.  To that aim, the document defines name
   discovery and schemes for reusable elements in GRASP objectives.
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
- **draft-gregoire-moq-msfts-02** (new-draft, score 0, ignored_after_review) [none]: [MPEG-2 Transport Stream Packaging for MOQT](https://datatracker.ietf.org/doc/draft-gregoire-moq-msfts/) — This document extends the MOQT Streaming Format (MSF) with the
   "mpeg2ts" packaging, which carries the packets of an MPEG-2 Transport
   Stream over MOQT.  It defines the catalog fields that describe such a
   track, and the rules that a publisher and a subscriber follow to
   carry the packet stream.
- **draft-hardie-bcp35-update-01** (new-draft, score 0, ignored_after_review) [none]: [Updated Provisional Registration Guidelines for URI Schemes](https://datatracker.ietf.org/doc/draft-hardie-bcp35-update/) — This documents updates the registration procedures for provisional
   URI schemes to handle issues not present at the time RFC 7595 was
   written.
- **draft-he-ippm-ioam-trace-type-bandwidth-02** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace-Type Extensions for Path bandwidth](https://datatracker.ietf.org/doc/draft-he-ippm-ioam-trace-type-bandwidth/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can accommodate the capacity of the traffic to be
   scheduled.  In situ Operations, Administration, and Maintenance
   (IOAM) is used for recording and collecting operational and telemetry
   information.  This document defines two bit flags within IOAM Trace-
   Type for carrying bandwidth information.
- **draft-ietf-avtcore-hevc-webrtc-10** (new-draft, score 0, ignored_after_review) [avtcore]: [H.265 Profile for WebRTC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-hevc-webrtc/) — RFC 7742 defines WebRTC video processing and codec requirements,
   including guidance for endpoints supporting the VP8 and H.264 codecs,
   which are mandatory to implement.  This document defines a profile of
   RFC 7798 for browsers supporting the H.265 codec.
- **draft-ietf-bier-bgp-ls-bier-ext-22** (new-draft, score 0, ignored_after_review) [bier]: [BGP Link-State extensions for BIER](https://datatracker.ietf.org/doc/draft-ietf-bier-bgp-ls-bier-ext/) — Bit Index Explicit Replication (BIER) is an architecture that
   provides optimal multicast forwarding through a "BIER domain" without
   requiring intermediate routers to maintain any multicast related per-
   flow state.  BIER also does not require any explicit tree-building
   protocol for its operation.  A multicast data packet enters a BIER
   domain at a "Bit-Forwarding Ingress Router" (BFIR), and leaves the
   BIER domain at one or more "Bit-Forwarding Egress Routers" (BFERs).
   The BFIR router adds a BIER header to the packet.  The BIER header
   contains a bitstring in which each bit represents exactly one BFER to
   forward the packet to.  The set of BFERs to which the multicast
   packet needs to be forwarded is expressed by setting the bits that
   correspond to those routers in the BIER header.

   BGP Link-State (BGP-LS) enables the collection of various topology
   informations from the network, and the topology informations are used
   by the controller to calculate the fowarding tables and then
   propagate them onto the BFRs(instead of having each node to calculate
   on its own) and that can be for both inter-as and intra-as
   situations.

   This document specifies extensions to the BGP Link-state address-
   family in order to advertise the BIER informations.
- **draft-ietf-bier-prefix-redistribute-12** (new-draft, score 0, ignored_after_review) [bier]: [BIER Prefix Redistribute](https://datatracker.ietf.org/doc/draft-ietf-bier-prefix-redistribute/) — This document defines a BIER proxy function to support one single
   BIER sub-domain over multiple underlay routing protocol regions
   (Autonomous Systems or IGP areas).  A new BIER proxy range sub-TLV is
   defined to redistribute BIER BFR-id information across the routing
   regions.
- **draft-ietf-cats-metric-definition-14** (new-draft, score 0, ignored_after_review) [cats]: [CATS Metrics Definition](https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/) — Computing-Aware Traffic Steering (CATS) is a traffic engineering
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
- **draft-ietf-dkim-dkim2-dns-01** (new-draft, score 0, ignored_after_review) [dkim]: [Domain Name Specification for DKIM2](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-dns/) — The updated DomainKeys Identified Mail (DKIM2) permits an
   organization that owns the signing domain to claim some
   responsibility for a message by associating the domain with the
   message through a digital signature.  This is done by publishing to
   Domain Name Service (DNS) of the domain a public key that is then
   associated to the domain and where messages can be signed by the
   corresponding private key.  Assertion of responsibility is validated
   through a cryptographic signature and by querying the Signer's domain
   directly to retrieve the appropriate public key.  This document
   describes DKIM2 DNS record format and how to find the record.
- **draft-ietf-dtn-btpu-05** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Transfer Protocol - Unidirectional](https://datatracker.ietf.org/doc/draft-ietf-dtn-btpu/) — This document defines a protocol for the unidirectional transfer of
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
- **draft-ietf-dtn-btpu-fec-03** (new-draft, score 0, ignored_after_review) [dtn]: [Forward Error Correction for the Bundle Transfer Protocol](https://datatracker.ietf.org/doc/draft-ietf-dtn-btpu-fec/) — This document defines an optional extension to the Bundle Transfer
   Protocol - Unidirectional, as described in [BTPU], to enable forward
   error correction (FEC) coding to be applied selectively to the
   transfer of individual bundles on a case by case basis.

   The definition and use of FEC follows the FECFRAME framework defined
   in [RFC6363], and this document introduces new Message types to BTPU
   in order to carry the FEC information as defined in the framework.
- **draft-ietf-grow-bmp-adj-ribs-filtered-01** (new-draft, score 0, ignored_after_review) [grow]: [Filtering Adj-Rib-In and Adj-Rib-Out to BMP receivers](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/) — Filtering RIBs in BMP (BGP Monitoring Protocol) can be desirable for
   several use-cases like, for example, limiting the amount of data a
   collector station has to process or allow a sender to export only a
   certain afi/safi of interest.  This document defines an indicator to
   inform a collector station that a Adj-Rib-In or Adj-Rib-Out data feed
   is being filtered at the BMP exporter.  This document updates RFC
   7854.
- **draft-ietf-idr-bgp-ifit-capabilities-10** (new-draft, score 0, ignored_after_review) [idr]: [Advertising In-situ Flow Information Telemetry (IFIT) Capabilities in BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ifit-capabilities/) — In-situ Flow Information Telemetry (IFIT) refers to network OAM data
   plane on-path telemetry techniques, in particular In-situ OAM (IOAM)
   and Alternate Marking.  This document defines a new Characteristic to
   advertise the In-situ Flow Information Telemetry (IFIT) capabilities.
   Within an IFIT domain, the IFIT capabilities advertisement from the
   tail node to the head node assists the head node to determine whether
   a particular IFIT Option type can be encapsulated in data packets.
   Such advertisement helps mitigating the leakage threat and
   facilitating the deployment of IFIT measurements on a per-service and
   on-demand basis.
- **draft-ietf-idr-bgp-ls-sr-policy-admin-flags-01** (new-draft, score 0, ignored_after_review) [idr]: [Advertisement of SR Policy Operational States using BGP Link-State](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-admin-flags/) — This document defines the extension of BGP Link-State to advertise
   the operational state of the candidate path or segment list,
   facilitating the operation and maintenance of the SR Policy.
- **draft-ietf-idr-bier-te-path-06** (new-draft, score 0, ignored_after_review) [idr]: [BGP for BIER-TE Path](https://datatracker.ietf.org/doc/draft-ietf-idr-bier-te-path/) — This document describes extensions to Border Gateway Protocol (BGP)
   for distributing a Bit Index Explicit Replication Traffic/Tree
   Engineering (BIER-TE) path.  A new Tunnel Type for BIER-TE path is
   defined to encode the information about a BIER-TE path.
- **draft-ietf-idr-rt-derived-community-12** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route Target derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route Target derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-idr-sr-policy-ifit-13** (new-draft, score 0, ignored_after_review) [idr]: [BGP SR Policy Extensions to Enable IFIT](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-ifit/) — Segment Routing (SR) policy is a set of candidate SR paths consisting
   of one or more segment lists and necessary path attributes.  It
   enables instantiation of an ordered list of segments with a specific
   intent for traffic steering.  In-situ Flow Information Telemetry
   (IFIT) refers to network OAM data plane on-path telemetry techniques,
   in particular the most popular are In-situ OAM (IOAM) and Alternate
   Marking.  This document defines extensions to BGP to distribute SR
   policies carrying IFIT information.  So that IFIT methods can be
   enabled automatically when the SR policy is applied.
- **draft-ietf-ippm-connectivity-monitoring-14** (new-draft, score 0, ignored_after_review) [ippm]: [An Experimental Connectivity Monitoring Metric for IPPM](https://datatracker.ietf.org/doc/draft-ietf-ippm-connectivity-monitoring/) — Within a Segment Routing (SR) domain, segment routed measurement
   packets can be sent along pre-determined paths.  This enables new
   kinds of active measurements.  Connectivity monitoring supervises the
   state and performance of a connection or a (sub)path from central
   monitoring systems.  This document specifies an experimental Type-p
   connectivity monitoring metric to accomodate such operational needs.
- **draft-ietf-ippm-stamp-ber-01** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Residual Bit Error Rate Measurement](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ber/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, along with its optional extensions specified in RFC 8972,
   supports active measurement.  Networks may experience transmission
   bit errors due to various factors, including poor fiber quality.
   Even with efficient CRC and FEC mechanisms, some bit errors may
   escape detection and correction; these are referred to as residual
   bit errors.  This document further augments the STAMP extensions
   specified in RFC 8972 to enable the measurement of the residual bit
   error rate within the "Extra Padding" TLV of STAMP-Test packets.
- **draft-ietf-ippm-stamp-ext-hdr-19** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting hop-by-
   hop and E2E operational and telemetry information.  This document
   extends STAMP to reflect IPv4/IPv6 headers as well as IPv6 extension
   headers for hop-by-hop and E2E active measurements, for example,
   using the IOAM data fields.

   This document updates RFC 8762 by specifying IPv4/IPv6 and UDP
   headers handling, UDP checksum handling, session state notifications,
   and rate limiting requirements that also apply to STAMP sessions not
   using these extensions.
- **draft-ietf-ippm-stamp-mpls-hdr-01** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet MPLS Network Action Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-mpls-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect MPLS Network Action Sub-Stacks and
   Post-Stack MPLS Headers, for HBH and E2E active measurements, for
   example, using the IOAM data fields.
- **draft-ietf-ipsecme-big-payload-00** (new-draft, score 0, ignored_after_review) [ipsecme]: [A Larger Internet Key Exchange version 2 (IKEv2) Payload](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-big-payload/) — The messages of the Internet Key Exchange version 2 (IKEv2) protocol
   are made up of payloads.  The current protocol limits each of these
   payloads to 64KB by having a 2-byte length field.  While this is
   usually enough, several of the payloads may need to be larger.

   This document updates RFC 7296 by defining an extension that allows
   larger payloads.
- **draft-ietf-jmap-blobext-02** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Blob Management](https://datatracker.ietf.org/doc/draft-ietf-jmap-blobext/) — The JSON Meta Application Protocol (JMAP) base protocol ([JMAP-CORE])
   provides the ability to upload and download arbitrary binary data via
   HTTP POST and GET on a defined endpoint.  This binary data is called
   a "blob".

   This extension adds additional ways to create and access blobs by
   making inline method calls within a standard JMAP request.  It also
   adds a reverse lookup mechanism to discover where blobs are
   referenced within other data types, support for large blobs via
   chunked construction with server-side optimisation, and server-side
   blob conversion operations including image format conversion, archive
   creation and extraction, compression and decompression, and delta/
   patch operations.
- **draft-ietf-jmap-conditional-01** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Conditional Set](https://datatracker.ietf.org/doc/draft-ietf-jmap-conditional/) — The JMAP base protocol ([JMAP-CORE]) provides the Foo/set method for
   creating, updating, and destroying objects.  It offers a single
   concurrency control, the "ifInState" argument, which guards an entire
   object type: if any object of that type has changed, the whole method
   is rejected.

   This extension adds a finer, per-object conditional mechanism.  A
   client may require that an individual update or destroy proceed only
   if the target object still matches a set of expected property values,
   expressed using the JMAP PatchObject already defined for updates.
   This provides optimistic concurrency control scoped to a single
   object — the equivalent of an HTTP "If-Match" precondition — for any
   JMAP data type.

   This extension also defines an optional "atomic" argument that
   applies an entire Foo/set as a single unit: either every change it
   requests takes effect, or none does.  Combined with the per-object
   precondition, this lets a client express a multi-object change that
   is safe only when applied together — such as an atomic rename that
   exchanges two names.
- **draft-ietf-jmap-filenode-17** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP File Storage extension](https://datatracker.ietf.org/doc/draft-ietf-jmap-filenode/) — The JMAP base protocol (RFC8620) provides the ability to upload and
   download arbitrary binary data.  This binary data is called a "blob",
   and can be used in all other JMAP extensions.

   This extension adds a method to expose blobs as a filesystem along
   with the types of metadata that are provided by other remote
   filesystem protocols.
- **draft-ietf-jmap-object-history-02** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Object History](https://datatracker.ietf.org/doc/draft-ietf-jmap-object-history/) — The JMAP base protocol (RFC8620) provides methods for synchronizing
   the current state of data objects between client and server.  This
   extension adds the ability to retrieve historical versions of
   objects, including objects that have been destroyed, by extending the
   standard Foo/get method.
- **draft-ietf-jsonschema-json-schema-04** (new-draft, score 0, ignored_after_review) [jsonschema]: [JSON Schema](https://datatracker.ietf.org/doc/draft-ietf-jsonschema-json-schema/) — JSON Schema defines the media type "application/schema+json", a JSON-
   based format for describing the structure of JSON data.  A JSON
   Schema may assert constraints on a JSON value, ways to extract
   information from it, and how to interact with it.  The "application/
   schema-instance+json" media type provides additional feature-rich
   integration with "application/schema+json" beyond what can be offered
   for "application/json" documents.
- **draft-ietf-lisp-nat-traversal-04** (new-draft, score 0, ignored_after_review) [lisp]: [NAT traversal for LISP](https://datatracker.ietf.org/doc/draft-ietf-lisp-nat-traversal/) — This document describes a mechanism for IPv4 NAT traversal for LISP
   tunnel routers (xTR) and LISP Mobile Nodes (LISP-MN) behind a Network
   Address Translator (NAT) device.  A LISP device both detects the NAT
   and initializes its state.  Forwarding to the LISP device through a
   NAT is enabled by the LISP Re-encapsulating Tunnel Router (RTR)
   network element, which acts as an anchor point in the data plane,
   forwarding traffic from unmodified LISP devices through the NAT.
- **draft-ietf-lisp-rfc6831bis-13** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC 6831.
- **draft-ietf-lsr-flex-soft-dataplane-02** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Flex Soft Dataplane](https://datatracker.ietf.org/doc/draft-ietf-lsr-flex-soft-dataplane/) — Advertisement of IGP Flex-Algo participation requires a dataplane
   context.  This document defines a "soft dataplane" usable in cases
   where existing defined dataplanes are not suitable.
- **draft-ietf-lsr-l2-bundle-member-remote-id-09** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  This document
   describes how Open Shortest Path First (OSPF) and Intermediate System
   to Intermediate System (IS-IS) would advertise the remote interface
   identifiers for L2 bundle members.  The corresponding extension of
   BGP Link State (BGP-LS) is also specified.
- **draft-ietf-mboned-redundant-ingress-failover-11** (new-draft, score 0, ignored_after_review) [mboned]: [Multicast Redundant Ingress Router Failover](https://datatracker.ietf.org/doc/draft-ietf-mboned-redundant-ingress-failover/) — This document is intended to serve as a guide for multicast network
   operators of various replication technologies to evaluate the options
   and tradeoffs in deploying redundant ingress router failover.
   Section 5 of RFC9026 details the hot root standby solution for MVPN
   networks.  Here we attempt to extend the discussion to cover
   additional multicast deployment solutions beyond MVPNs.  This
   document compares cold, warm, and hot standby modes, listing their
   advantages, limitations and deployment considerations to help
   identify the appropriate solution for any network.
- **draft-ietf-netconf-over-quic-12** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF over QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-over-quic/) — This document specifies how to use QUIC as a secure transport for
   exchanging Network Configuration Protocol (NETCONF) messages.
   NETCONF over QUIC allows implementations to take advantage of QUIC
   streams, for example, to eliminate some TCP head-of-line blocking
   issues.  NETCONF over QUIC provides security properties similar to
   NETCONF over TLS.

   This document also defines a YANG module which augments the ietf-
   netconf-client and ietf-netconf-server YANG modules.

Editorial note (to be removed by the RFC Editor)

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
- **draft-ietf-netconf-quic-client-server-09** (new-draft, score 0, ignored_after_review) [netconf]: [YANG Groupings for QUIC clients and QUIC servers](https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-client-server/) — This document defines five YANG 1.1 modules to support the
   configuration of QUIC clients and QUIC servers.  The modules include
   basic parameters for configuring QUIC based clients and servers as
   well as initial modules for the IANA registries "QUIC Versions" and
   "QUIC Transport Parameters".
- **draft-ietf-netmod-yang-packages-10** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Packages](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-packages/) — This document defines YANG packages: versioned organizational
   structures used to manage the schema and conformance of a set of YANG
   modules as a cohesive unit.
- **draft-ietf-pce-bier-te-04** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extensions for Tree Engineering for Bit Index Explicit Replication (BIER-TE)](https://datatracker.ietf.org/doc/draft-ietf-pce-bier-te/) — Tree Engineering for Bit Index Explicit Replication (BIER-TE) shares
   architecture and packet formats with BIER.  BIER-TE forwards and
   replicates packets based on a BitString in the packet header, but
   every BitPosition of the BitString of a BIER-TE packet indicates one
   or more adjacencies.  BIER-TE Path can be derived from a Path
   Computation Element (PCE).

   This document specifies extensions to the Path Computation Element
   Protocol (PCEP) that allow a PCE to compute and initiate the path for
   the Tree Engineering for Bit Index Explicit Replication (BIER-TE).
- **draft-ietf-pce-sr-mpls-sid-verification-01** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions for SID verification for SR-MPLS](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-mpls-sid-verification/) — This document defines extensions to the Path Computation Element
   Communication Protocol (PCEP) to support SID verification in Segment
   Routing MPLS (SR-MPLS) networks.  Specifically, it introduces a flag
   in the SR-ERO subobject to indicate that the Path Computation Client
   (PCC) is explicitly requested to verify SID(s) by the Path
   Computation Element (PCE), and defines capability exchange
   mechanisms.
- **draft-ietf-pim-igmp-mld-snooping-yang-l2vpn-ext-11** (new-draft, score 0, ignored_after_review) [pim]: [IGMP and MLD Snooping Yang Module Extension for L2VPN](https://datatracker.ietf.org/doc/draft-ietf-pim-igmp-mld-snooping-yang-l2vpn-ext/) — Internet Group Management Protocol (IGMP) and Multicast Listener
Discovery (MLD) Snooping could be used in both bridge service and L2VPN
service. The old ietf-igmp-mld-snooping yang module just describes the
bridge service. In this document we extend the existing ietf-igmp-mld-
snooping yang module and make it could be used in L2VPN service.
- **draft-ietf-pim-ipv4-in-ipv6-core-00** (new-draft, score 0, ignored_after_review) [pim]: [Native IPv4 multicast in IPv6 Core using PIM](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv4-in-ipv6-core/) — This document describes how PIM Sparse-Mode can be used to construct
   IPv4 multicast trees across an IPv6-only network core.  This allows
   forwarding of native IPv4 multicast data packets.  The document
   specifies how to send and receive IPv4 PIM messages with IPv6
   headers, using a new well-known link-local IPv6 multicast address,
   and the use of RPF vectors for reachability.
- **draft-ietf-pquip-pqc-hsm-constrained-09** (new-draft, score 0, ignored_after_review) [pquip]: [Adapting Constrained Devices for Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/) — This document provides guidance on integrating Post-Quantum
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
- **draft-ietf-regext-rdap-versioning-08** (new-draft, score 0, ignored_after_review) [regext]: [Versioning in the Registration Data Access Protocol (RDAP)](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-versioning/) — This document describes an RDAP extension for an extensible set of
   versioning types with the features of identifying the RDAP extension
   versions supported by the server, the RDAP extension versions
   included in an RDAP response, and enabling a client to specify the
   desired RDAP extension versions to include in the RDAP query and RDAP
   response.  In addition, this document defines a mechanism for
   communicating versioning and deprecation information that facilitates
   coordinated transitions between successive extension versions while
   minimizing the impact of breaking changes on deployed clients.
- **draft-ietf-spring-sr-policy-flexible-cp-selection-02** (new-draft, score 0, ignored_after_review) [spring]: [Flexible Candidate Path Selection of SR Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-flexible-cp-selection/) — This document describes a flexible method for selecting candidate
   Segment Routing (SR) policy paths.  Based on the real-time resource
   usage and forwarding quality of candidate paths, the head node can
   perform dynamic path switching among multiple candidate paths in the
   SR policy.
- **draft-ietf-spring-srv6-security-19** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing over IPv6 (SRv6) Security Considerations](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/) — Segment Routing over IPv6 (SRv6) is the instantiation of Segment
   Routing on the IPv6 data plane, using IPv6 addresses to identify
   segments.  This document discusses security considerations in SRv6
   networks, including the potential threats and the possible mitigation
   methods.  The document does not define any new security protocols or
   extensions to existing protocols.
- **draft-ietf-spring-stamp-srpm-mpls-12** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document specifies procedures for
   performance measurement in SR-MPLS networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths, including Segment Lists of SR-MPLS Policies, SR-MPLS
   IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths,
   as well as Layer-3 and Layer-2 services carried over those paths.
- **draft-ietf-spring-stamp-srpm-srv6-09** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths including Segment Lists of SRv6 Policies, SRv6
   IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 and Layer-2 services carried over those paths.
- **draft-ietf-tsvwg-fq-pie-03** (new-draft, score 0, ignored_after_review) [tsvwg]: [Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/) — This document presents Flow Queue Proportional Integral controller
   Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue
   Management (AQM) algorithm to isolate flows and tackle the problem of
   bufferbloat.  FQ-PIE uses hashing to classify incoming packets into
   different queues and provide flow isolation.  Packets are dequeued by
   using a variant of the round robin scheduler.  Each such flow is
   managed by the PIE algorithm to maintain high link utilization while
   controlling the queue delay to a target value.
- **draft-ietf-v6ops-5g-ipv6only-00** (new-draft, score 0, ignored_after_review) [v6ops]: [Considerations of IPv6-only Deployment in 5G Mobile Networks](https://datatracker.ietf.org/doc/draft-ietf-v6ops-5g-ipv6only/) — This document describes a practical guide of deploying 464XLAT based
   IPv6-only technology on user plane in 3GPP 5G networks.  It also
   covers key 5G concepts and architectures, configuration methods and
   operational challenges.
- **draft-ietf-v6ops-ipv6-only-05** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
- **draft-jabley-regext-allowable-dnssec-parameters-00** (new-draft, score 0, ignored_after_review) [none]: [Acceptance of DNSSEC Parameters in EPP](https://datatracker.ietf.org/doc/draft-jabley-regext-allowable-dnssec-parameters/) — The Extensible Provisioning Protocol (EPP) is used to submit DNSSEC
   parameters for domain names to domain name registries.  Registries
   and registrars often restrict the values they accept, and those
   restrictions vary from registry to registry.  The resulting
   uncertainty makes it difficult for DNS operators to adopt new
   algorithms.  This document recommends that registries and registrars
   base their acceptance policies on the IANA registries for DNSSEC
   algorithms and digest types.
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-03** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.
- **draft-knodel-nomcom-gender-representation-07** (new-draft, score 0, ignored_after_review) [none]: [Gender Representation in the IETF Nominating Committees](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document extends the existing limit on nomcom representation by
   organization ([RFC8713], Section 4.17) so that not all voting members
   of the IETF Nominating Committee (nomcom) belong to the same gender.
   It guarantees up to three voting seats to volunteers who opt into a
   self-declared pool, and changes the selection only in years when a
   plain random draw would seat fewer.
- **draft-li-lsvr-bgp-spf-srv6-07** (new-draft, score 0, ignored_after_review) [none]: [Applying BGP-LS Segment Routing over IPv6(SRv6) Extensions to BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-li-lsvr-bgp-spf-srv6/) — For network scenarios such as Massively Scaled Data Centers (MSDCs),
   BGP is extended for Link-State (LS) distribution and the Shortest
   Path First (SPF) algorithm based calculation.  BGP Link State
   Shortest Path First (BGP-LS-SPF) Routing leverages the mechanisms of
   both BGP protocol and BGP-LS protocol extensions.  Segment Routing
   over IPv6 (SRv6) provides a source routing mechanism that allows a
   flow to be restricted to a specific topological path, while
   maintaining per-flow state only at the ingress node(s) to the SRv6
   domain.  In some networks, it may be useful to enable SRv6 based
   source routing mechanism together with BGP-LS-SPF.  This document
   proposes to introduce the BGP Link-State (BGP-LS) extensions for SRv6
   to the BGP-LS-SPF SAFI to enable SRv6 capabilities in BGP-LS-SPF.
   The usages and formats of these extensions are also provided in this
   document.
- **draft-lindqvist-zstdict-01** (new-draft, score 0, ignored_after_review) [none]: [Zstandard Dictionary Content-Encoding](https://datatracker.ietf.org/doc/draft-lindqvist-zstdict/) — This document defines a new HTTP content coding, "zstdict", which
   enables Zstandard compression with a pre-shared dictionary.  The
   dictionary is identified by a SHA-256 hash and negotiated via the
   Content-Dict response header.
- **draft-linker-diem-arch-00** (new-draft, score 0, ignored_after_review) [none]: [Digital Emblems Architecture Document](https://datatracker.ietf.org/doc/draft-linker-diem-arch/) — TODO Abstract
- **draft-liu-bess-ipfix-bgp-vpn-00** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP VPN Information in IPFIX](https://datatracker.ietf.org/doc/draft-liu-bess-ipfix-bgp-vpn/) — This document introduces new IP Flow Information Export (IPFIX)
   information elements to carry information that can be used to
   identify the egress PE in BGP VPN scenarios.
- **draft-mcconnell-software-status-wellknown-03** (new-draft, score 0, ignored_after_review) [none]: [A Well-Known URI for Software Lifecycle Status](https://datatracker.ietf.org/doc/draft-mcconnell-software-status-wellknown/) — This document defines a Well-Known URI [RFC8615] at which software
   vendors and open-source maintainers may publish machine-readable
   lifecycle status information for their products.  A JSON resource
   retrieved from /.well-known/software-status.json allows consumers —
   including security tools, software composition analysis (SCA)
   platforms, vulnerability scanners, and system administrators — to
   programmatically determine whether a specific version of a software
   product is actively supported, in long-term support (LTS), under
   security-only maintenance, or at end-of-life (EOL).

   This revision (-02) extends the schema to support multi-product
   vendors — organizations that ship multiple distinct products or SKUs
   under a single domain.  A new optional products array at the root of
   the resource allows a single software-status.json endpoint to serve
   lifecycle declarations for an entire product catalog, including
   firmware-based devices such as routers, switches, and IoT appliances.
   This extension is fully backward compatible: existing single-product
   resources require no modification.

   This revision (-03) broadens the scope beyond firmware-based devices
   to hosted software-as-a-service, installed fat and thin clients,
   browser extensions and plug-ins, and devices of all kinds, including
   televisions, drones, and servers.  It adds product types and
   identifiers for these deployment models, and cross-references SBOM
   formats (CycloneDX, SPDX) as complementary data.  The schema version
   is raised to "1.1"; the change is additive and fully backward
   compatible with "1.0" resources.

   This document also describes, in Appendix B (#appendix-b), a
   companion convention for open-source projects hosted on version-
   control platforms to publish equivalent information within the
   repository at .github/software-status.json.
- **draft-nottingham-httpbis-402-00** (new-draft, score 0, ignored_after_review) [none]: [The 402 (Payment Required) HTTP Status Code](https://datatracker.ietf.org/doc/draft-nottingham-httpbis-402/) — This specification defines semantics for the 402 (Payment Required)
   HTTP status code.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottingham-httpbis-402/.

   information can be found at https://projects.mnot.net/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/402.
- **draft-ousterhout-tsvwg-homa-00** (new-draft, score 0, ignored_after_review) [none]: [Homa: An RPC Transport Protocol for Datacenters](https://datatracker.ietf.org/doc/draft-ousterhout-tsvwg-homa/) — This document defines the Homa transport protocol.  Homa provides
   applications with a reliable and efficient mechanism for delivering
   request and response messages for remote procedure calls (RPCs).  It
   is intended for use within datacenters.  Homa uses messages,
   receiver-issued grants, and packet priorities to support RPC
   workloads.  Published evaluations report a reduction of more than 10x
   in tail latency for short messages relative to TCP for specific
   workloads and test conditions; this document does not claim a
   performance improvement for all datacenter environments.
- **draft-prabel-ssh-scloudplus-kex-00** (new-draft, score 0, ignored_after_review) [none]: [Secure Shell (SSH) Post-Quantum/Traditional Hybrid Key Exchange Methods Using Scloud+](https://datatracker.ietf.org/doc/draft-prabel-ssh-scloudplus-kex/) — This document defines four Post-Quantum/Traditional (PQ/T) hybrid key
   exchange methods for the Secure Shell (SSH) protocol.  They combine
   the Scloud+ key-encapsulation mechanism, whose security relies on the
   unstructured Learning With Errors (LWE) problem, with Elliptic Curve
   Diffie-Hellman over the NIST P-384 and P-521 curves.
- **draft-preussmattsson-tls-hqckem-03** (new-draft, score 0, ignored_after_review) [none]: [HQC-KEM Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-preussmattsson-tls-hqckem/) — This document defines nine quantum-resistant TLS 1.3 key exchange
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
- **draft-prf-protocol-02** (new-draft, score 0, ignored_after_review) [none]: [The PRF Protocol](https://datatracker.ietf.org/doc/draft-prf-protocol/) — This document describes the PRF protocol ("Prf is Reversed Frp"), a
   lightweight, binary-length-prefixed TCP relay messaging protocol.
   PRF enables peer-to-peer tunneling of TCP connections through a
   public middle relay node, originally designed for Minecraft
   multiplayer sessions behind NAT or firewall environments.  The
   protocol defines three roles - Server, Client, and Middle - and a set
   of four wireframe message types for room registration, connection
   requests, worker handoff, and direct Minecraft client handshake
   parsing.
- **draft-ramadan-moq-fec-00** (new-draft, score 0, ignored_after_review) [none]: [Forward Error Correction for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec/) — This document specifies a mechanism for transmitting Forward Error
   Correction (FEC) repair data alongside source media in Media over
   QUIC (MoQ) sessions.  It defines catalog-based signaling of FEC
   configuration -- including a derived RaptorQ Object Transmission
   Information that requires no in-session messages -- conventions for
   repair track naming, the format of repair objects, and the ISO/IEC
   23008-1 block profile that fixes how source symbols and FEC blocks
   are formed and identified.  RaptorQ (RFC 6330) is the mandatory-to-
   implement and only fully specified FEC scheme; an algorithm registry
   provides extension points for additional schemes.  FEC enables
   receivers to recover from packet loss without retransmission latency.
   This specification is designed for compatibility with ATSC 3.0
   (A/331) and ARIB STD-B60 broadcast systems.
- **draft-ramadan-moq-mmt-00** (new-draft, score 0, ignored_after_review) [none]: [MPEG Media Transport (MMT) Packaging for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-mmt/) — This document specifies the use of MPEG Media Transport (MMT) as a
   container format for Media over QUIC (MoQ).  MMT provides a unified
   framework for streaming media over heterogeneous networks including
   broadcast (ATSC 3.0, ARIB STD-B60), multicast (SSM), and unicast
   (QUIC/WebTransport).  This specification defines the mapping of MMT
   packets to MoQ objects, interaction with Application-Layer FEC,
   bidirectional conversion between S-TSID and MoQ catalogs, and
   compatibility considerations for both ATSC 3.0 and ARIB STD-B60
   systems.
- **draft-ramos-schc-for-6g-00** (new-draft, score 0, ignored_after_review) [none]: [SCHC for 6G](https://datatracker.ietf.org/doc/draft-ramos-schc-for-6g/) — TODO Abstract
- **draft-reddy-hpke-hqc-01** (new-draft, score 0, ignored_after_review) [none]: [Hamming Quasi-Cyclic (HQC) Key Encapsulation Mechanisms for Hybrid Public Key Encryption (HPKE)](https://datatracker.ietf.org/doc/draft-reddy-hpke-hqc/) — This document specifies Hamming Quasi-Cyclic (HQC) key encapsulation
   mechanisms for use with Hybrid Public Key Encryption (HPKE).  It
   defines the HPKE KEM interface, deterministic key-pair derivation,
   public and private key encodings, and input validation for three HQC
   parameter sets.  It also defines three PQ/T hybrid KEMs that combine
   HQC with P-256, X25519, or P-384.  It requests six HPKE KEM algorithm
   identifiers and reuses the existing HPKE key schedule, encryption
   operations, and export interface.
- **draft-seemann-masque-connect-ip-qlog-00** (new-draft, score 0, ignored_after_review) [none]: [qlog Definitions for CONNECT-IP](https://datatracker.ietf.org/doc/draft-seemann-masque-connect-ip-qlog/) — This document defines qlog events for CONNECT-IP packet processing
   and representations for its capsules, including the DNS and PREF64
   configuration extensions.  It extends the HTTP event schema defined
   in the HTTP/3 qlog document.
- **draft-sheth-pqc-dnssec-strategy-02** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Cryptography Strategy for DNSSEC](https://datatracker.ietf.org/doc/draft-sheth-pqc-dnssec-strategy/) — This document proposes a post-quantum cryptography (PQC) strategy for
   Domain Name System Security (DNSSEC) that includes two types of
   algorithms: one or more conservatively designed algorithms that are
   unlikely ever to need to be replaced, and one or more low-impact
   drop-in algorithms that are used the same way as a traditional
   signature algorithm.  The conservatively designed algorithms can be
   used in a mode of operation that mitigates the operational impact of
   a large signature size.  The combination provides both the routine
   performance of the low-impact algorithm and a resilient fallback to
   the conservatively designed choice.  The draft outlines the strategy,
   provides recommendations for future testing and deployment, and
   highlights operational considerations in adopting PQC for DNSSEC.
- **draft-shin-avtcore-rtp-multi-opus-04** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP/SDP Signaling for Opus Multistream Operation](https://datatracker.ietf.org/doc/draft-shin-avtcore-rtp-multi-opus/) — This document specifies RTP/SDP signaling for Opus multistream
   (multichannel) operation, enabling negotiation of layouts such as 5.1
   and 7.1 in real-time communications.  It defines SDP format
   parameters for describing multistream configurations and specifies
   Offer/Answer procedures for interoperable negotiation of multichannel
   Opus sessions.  This document does not define new Opus codec
   behavior.  Rather, it standardizes SDP signaling for Opus multistream
   operation while continuing to use the Opus RTP payload format defined
   in [RFC7587] and the channel mapping semantics defined in [RFC7845].
   The signaling procedures specified in this document are intended to
   provide a standardized alternative to deployment-specific approaches
   that have historically been referred to as "multiopus".
- **draft-smith-v6ops-nearly-ipv6-only-dualstack-hosts-03** (new-draft, score 0, ignored_after_review) [none]: [Nearly IPv6 Only Dual Stack Hosts](https://datatracker.ietf.org/doc/draft-smith-v6ops-nearly-ipv6-only-dualstack-hosts/) — Once all of a dual stack IPv4 and IPv6 host's applications support
   IPv6, IPv4 connectivity becomes unnecessary.  However, ceasing to
   provide a dual stack host with an IPv4 address via a DHCPv4 server
   can cause the host to continue to make periodic and unsatisfied
   DHCPv4 requests, imposing unnecessary broadcast traffic on an
   attached link.  In this situation, it would be useful to continue to
   provide a host with an IPv4 address via DHCPv4, yet prevent it from
   using the IPv4 address for any connectivity outside of the host
   itself.  This memo describes a DHCPv4 method to achieve this.
- **draft-smyslov-tls-ext-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Extending Limit on Extensions Size in TLS 1.3](https://datatracker.ietf.org/doc/draft-smyslov-tls-ext-ext/) — Protocol TLS 1.3 is widely used to protect traffic in the Internet.
   However, the format of the TLS 1.3 ClientHello, ServerHello, and
   EncryptedExtensions handshake messages limits the size of extensions
   to 64 Kbytes.

   This specification extends TLS 1.3 to allow extensions in
   ClientHello, ServerHello, and EncryptedExtensions have size larger
   than 64 Kbytes.
- **draft-swepcarl-green-controller-yang-00** (new-draft, score 0, ignored_after_review) [none]: [GREEN Controller YANG](https://datatracker.ietf.org/doc/draft-swepcarl-green-controller-yang/) — TODO Abstract
- **draft-taylor-dtn-btpx-00** (new-draft, score 0, ignored_after_review) [none]: [Bundle Transfer Protocol - Cross-Link](https://datatracker.ietf.org/doc/draft-taylor-dtn-btpx/) — The Bundle Transfer Protocol - Unidirectional (BTPU) provides for the
   transfer of large binary objects, typically Bundle Protocol version 7
   bundles, over a unidirectional, unreliable, frame-based link-layer
   protocol, and by design includes no return path.

   This document defines the Bundle Transfer Protocol - Cross-Link
   (BTPX), an extension to BTPU for deployments where independent BTPU
   channels exist in both directions between a pair of nodes.  It
   defines how a Transfer or a Bundle Message on one channel is
   referenced from another, and a first application of such references,
   the Transfer Status Message, which allows a receiver to indicate to a
   sender that continued transfer of an object is unnecessary, and why.

   This document defines no segment-level acknowledgement or
   retransmission semantics; such mechanisms are deferred to future
   documents.
- **draft-templin-6man-aero-omni-amen-18** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-tishkin-hmtp-01** (new-draft, score 0, ignored_after_review) [none]: [HTTP Mail Transfer Protocol](https://datatracker.ietf.org/doc/draft-tishkin-hmtp/) — This document specifies the HTTP Mail Transfer Protocol (HMTP), a
   protocol for the submission and transfer of Internet mail over HTTPS.
   HMTP retains what SMTP and the mail system built around it have
   proven, namely the Internet Message Format, the separation of
   envelope and message, and the semantics of delivery and delivery
   status notifications, and adds what SMTP provides only through
   optional extensions or not at all.  Security is built in: transport
   encryption is mandatory, and every transfer request is signed on
   behalf of the sending domain, using keys published with the
   DomainKeys Identified Mail (DKIM) key publication mechanism.
   Requests carry identifiers that make retries safe, failures are
   reported per recipient as structured problem details with a mapping
   to SMTP status codes, and extensions are declared explicitly as
   capabilities.  Messages are carried unmodified inside a JSON
   envelope, and large messages and attachments can be transferred by
   reference, with their integrity protected by cryptographic hashes.
   Servers discover HMTP endpoints through DNS and a well-known URI, and
   a domain can publish a policy that prevents downgrade to SMTP.  HMTP
   does not depend on SMTP, but an implementation can optionally fall
   back to SMTP when a peer does not support HMTP, so that it can be
   deployed incrementally alongside existing systems.
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
- **draft-watts-eqr-conformance-02** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Conformance Profile and Test Vectors for Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-eqr-conformance/) — This document defines a deterministic conformance profile and test-
   vector corpus for Evidence Qualification Receipts (EQRs).  The
   profile, named eqr-core-1, makes receipt conformance mechanically
   reproducible: strict JSON structure, SHA-256 digest encoding, UTC
   timestamp handling, evidence-reference integrity, requirement-state
   derivation, and three-valued PASS, FAIL, or INDETERMINATE results are
   checked by a closed algorithm.  The profile is intentionally narrow.
   Conformance does not establish that evidence is true, that a
   proposition is scientifically valid, that an issuer is trustworthy,
   or that an action is authorized.  The goal is interoperable
   verification of receipt semantics, not promotion of conformance into
   substantive truth.
- **draft-watts-verification-promotion-boundaries-00** (new-draft, score 0, ignored_after_review) [none]: [Verification Promotion Boundaries for Protocol Implementations](https://datatracker.ietf.org/doc/draft-watts-verification-promotion-boundaries/) — Protocol implementations frequently combine specification checks,
   deterministic test vectors, security testing, independent
   reproduction, and release decisions.  A common failure mode is
   evidence collapse: a result at one assurance level is silently
   treated as sufficient for a stronger conclusion.

   This document defines Verification Promotion Boundaries (VPB), a
   machine-readable profile and state-transition procedure that
   separates specification validation, local conformance, independent
   reproduction, authorized security testing, and release eligibility.
   VPB also defines dual-state handling for specification defects:
   detecting a bad normative vector is negative evidence about the
   tested subject but may be positive fault-detection evidence about
   the verifier.  Unknown evidence never promotes.
- **draft-wu-grow-bmp-multi-instance-01** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Monitoring Multiple BGP Instances](https://datatracker.ietf.org/doc/draft-wu-grow-bmp-multi-instance/) — The BGP Monitoring Protocol (BMP), as defined in RFC 7854, provides a
   means for monitoring BGP sessions.  In deployments where a single
   device runs multiple BGP instances simultaneously - typically a base
   instance together with one or more additional instances, each
   identified by an Instance Name and potentially running in a separate
   process with an independent Router-ID and Autonomous System (AS)
   number - the existing BMP message format does not allow a Monitoring
   Station to distinguish peers or routes belonging to different BGP
   instances on the same monitored router.

   This document defines a new BMP Type-Length-Value (TLV) element, the
   BGP Instance Name TLV, that carries the Instance Name of the BGP
   instance associated with a given peer or route.  Following the TLV
   extension framework defined in [I-D.ietf-grow-bmp-tlv], the new TLV
   MAY appear in Peer Up Notification, Peer Down Notification, Route
   Monitoring, Statistics Report, and Route Mirroring messages.  The TLV
   enables a Monitoring Station to unambiguously attribute monitored BGP
   information to the correct BGP instance on the monitored router.
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
- **draft-zhangb-cats-centralized-control-plane-00** (new-draft, score 0, ignored_after_review) [none]: [A Centralized Control Plane for Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-zhangb-cats-centralized-control-plane/) — This document specifies a centralized control-plane realization of
   Computing-Aware Traffic Steering (CATS).  The realization uses a
   logically centralized CATS Path Selector (C-PS) together with ingress
   and egress CATS-Forwarders.  The C-PS receives a service request from
   an ingress CATS-Forwarder, resolves the requested service to an
   eligible service contact instance using computing service and network
   information, and then invokes a path-computation function for the
   selected destination.  The path-computation request contains a
   resolved headend, endpoint, and network constraints; it does not ask
   the PCE to discover service instances.

   After path computation, the C-PS returns a steering binding to the
   ingress CATS-Forwarder.  The binding identifies the selected
   destination address, the egress CATS-Forwarder, and a realizable path
   or policy.  The ingress forwarder applies the destination replacement
   and path encapsulation to the first packet and forwards it.  The
   egress forwarder removes the path encapsulation and delivers the
   packet to the selected service contact instance.  Subsequent packets
   use the installed flow binding, and reverse traffic uses the
   corresponding return binding.
- **draft-zhuang-grow-monitoring-bgp-parameters-03** (new-draft, score 0, ignored_after_review) [none]: [Monitoring BGP Parameters Using BMP](https://datatracker.ietf.org/doc/draft-zhuang-grow-monitoring-bgp-parameters/) — The BGP Monitoring Protocol (BMP) is designed to monitor BGP running
   status, such as BGP peer relationship establishment, termination, and
   route updates.  Without BMP, manual queries are required to obtain
   BGP operational status.

   This document defines extensions to the BMP Initiation Message to
   enable a BGP Monitoring Station (BMS) to discover optional BGP
   capabilities supported by the monitored network device, capabilities
   currently enabled, and default configuration parameters.

## Errors / fetch failures

- draft-faltstrom-unicode: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-faltstrom-unicode/doc.json
