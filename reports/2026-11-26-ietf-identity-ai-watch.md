# IETF Identity + AI Standards Watch

Date: 2026-11-26

## Read now

- **draft-sharif-agent-audit-trail-11** (new-draft, score 33, trust_infrastructure) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
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

   The -10 revision strengthens recording independence
   (Section 5.2) from SHOULD to MUST at trust level L2 and above,
   and requires the "authority_ref" of the "principal" field
   (Section 3.1) to be non-null and to reference an authorization
   artifact verifiable independently of the agent at L2 and above,
   in response to independent review.  Above L2, both the recorder
   and the authorizing artifact are therefore independent of the
   agent.
- **draft-noss-jeftovic-groundmark-core-01** (new-draft, score 31, core_identity) [none]: [DNS-Anchored Identity Discovery for Autonomous Agents](https://datatracker.ietf.org/doc/draft-noss-jeftovic-groundmark-core/) — This document defines the core of Groundmark, a protocol for DNS-
   anchored identity discovery and request authentication for autonomous
   software agents.  Operators publish an agent's signing public key in
   a DNS TXT record under a reserved label and, optionally, name the
   agent's Identity Service Provider (IDSP) in a second record.  Agents
   authenticate HTTP requests using HTTP Message Signatures (RFC 9421)
   with a key identifier that resolves through DNS.  DNSSEC is required
   for all Groundmark DNS lookups.  Successful core verification
   establishes current-key provenance: control of the private key
   corresponding to the DNSSEC-authenticated _agentid key used for the
   request.  It does not establish legal identity, registrar identity
   proofing, brand authorization, or continuity with an earlier key or
   registrant.

   When a relying party's policy requires more, the agent presents a
   reference in a signature-covered header field, the relying party
   confirms that the reference points at the IDSP named in the agent's
   DNSSEC-validated zone, and it fetches a credential about the operator
   from that IDSP directly.  No claim is published in DNS.  The
   credential is a W3C Verifiable Credential secured as an SD-JWT; its
   format, the IDSP's obligations, method disclosure and status are
   defined in the companion Groundmark Protocol specification, which is
   being developed in the Decentralized Identity Foundation.  This
   version replaces both draft-noss-jeftovic-groundmark-core-00 and
   draft-noss-jeftovic-groundmark-attestation-00.
- **draft-chen-oauth-agent-intent-token-02** (new-draft, score 26, authorization) [none]: [The Intent Token - A Credential for Delegated User Intent](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-intent-token/) — Autonomous Artificial Intelligence (AI) agents translate high-level,
   often ambiguous natural-language instructions from end users into
   multi-step chains of downstream API invocations.  Traditional OAuth
   2.0 authorization mechanisms bind access tokens to static, pre-
   configured scopes or fine-grained resource parameters known at the
   time of user consent, leaving a semantic gap when an agent
   dynamically determines exact execution parameters at runtime.

   This document specifies the Intent Token, a cryptographically signed,
   sender-constrained JSON Web Token (JWT) profile that captures either
   user-approved authorization bounds or host-attested user
   instructions, together with an upper-bound authorization envelope and
   optional step-up action triggers.  Rather than being presented
   directly to Resource Servers, an Intent Token serves as a verifiable
   input artifact at the Authorization Server or a dedicated Policy
   Decision Point (PDP) — either exchanged via OAuth 2.0 Token Exchange
   (RFC 8693) — optionally accompanied by a client-side Agent Delegation
   Proof (ADP) — for short-lived, narrowly scoped downstream access
   tokens, or submitted via Pushed Authorization Requests (RFC 9126) to
   establish or advance a stateful authorization workflow.
- **draft-seymour-wimse-connected-flight-07** (new-draft, score 26, authorization) [none]: [Zero Trust Fabric Layer Agent-to-Agent Chained Trust on a Connected Flight](https://datatracker.ietf.org/doc/draft-seymour-wimse-connected-flight/) — The Zero Trust Fabric Layer (ZTFL), an architecture the author
   previously published as "Zero Trust for Autonomous AI Agents: A
   Fabric Layer Architecture Verified in Cedar and AWS IAM" (SSRN,
   2026), verified a single autonomous agent issuing a single request.
   That earlier work by the author did not address what happens when
   that agent delegates its authority to a second agent, or a third, a
   pattern already standard in multi-agent orchestration.  Existing
   delegation mechanisms do not close this gap.  OAuth 2.0 Token
   Exchange represents prior actors as claims that are informational
   only for access control decisions.  Classical logic-based and
   relationship-based authorization models were built for stable, long-
   lived principals and do not enforce a tenant boundary at the specific
   hop where it is crossed, nor do they bind every hop in a chain to a
   single expiring credential established at the chain's origin.

   This document extends the author's ZTFL architecture with a chained
   authorization model, structured on the mechanics of international
   travel.  An immutable Passport establishes identity for the full
   journey.  A Ticket, issued once at task initiation as a conditional
   ephemeral credential, binds every subsequent hop to the same
   authorized chain; a locally valid-looking Boarding Pass that cannot
   trace back to it is rejected regardless of appearance.  A per-hop
   Boarding Pass, a child ephemeral token derived from and traceable to
   the Ticket, authorizes each leg.  A Visa, an explicit and narrowly
   scoped grant, is required only at the moment a hop crosses a tenant
   boundary the Passport alone cannot cross.  The model is formalized as
   a boundary-conditional evaluation function, implemented and validated
   against the Cedar policy language, and compared directly against
   OAuth Token Exchange, delegation logic, and relationship-based
   authorization on two properties none of them enforce structurally:
   chain-wide traceability to a single origin, and containment at the
   boundary itself.

   This revision further shows that the model's per-hop Boarding Pass
   structurally resists mid-chain redirection, including redirection
   caused by prompt injection reaching an intermediate agent, because
   issuing a Boarding Pass requires standing the redirected agent never
   holds and cannot acquire by altering its own behavior.  This revision
   also defines a durable consumption record that limits each hop to a
   single completion, and states the bounds beyond which replay and mid-
   chain redirection do not extend.
- **draft-gaikwad-scim-mcp-server-00** (new-draft, score 25, authorization) [none]: [System for Cross-domain Identity Management (SCIM) Resource Types for Model Context Protocol (MCP) Servers and Tool Groups](https://datatracker.ietf.org/doc/draft-gaikwad-scim-mcp-server/) — AI agents reach tools through servers that implement the Model
   Context Protocol (MCP).  Organizations decide which MCP servers are
   approved, who is accountable for each, who may use each, and when one
   must be withdrawn.  Identity and governance systems make those
   decisions, but the gateways, private registries and agent hosts that
   act on them come from many vendors and have no common way to receive
   them.

   This document defines a SCIM resource type, McpServer, that carries
   an organization's governance record for an MCP server: its endpoint,
   the OAuth protected resource identifier and authorization servers
   that protect it, its owners, the principals eligible to use it, an
   optional list of approved tools, and whether it is approved for use.
   It also defines McpToolGroup, a named set of tools drawn from one or
   more MCP servers together with the principals eligible to use them.
   It specifies how gateways, registries and hosts act on these records
   and how SCIM Security Event Tokens signal changes to them.  It does
   not describe MCP server capabilities, which remain the subject of
   MCP's own metadata, and it does not authorize individual tool
   invocations.
- **draft-munoz-scitt-permit-profile-02** (new-draft, score 23, trust_infrastructure) [none]: [A SCITT Profile for Pre-Execution AI Action Authorization Records](https://datatracker.ietf.org/doc/draft-munoz-scitt-permit-profile/) — This document specifies a SCITT (Supply Chain Integrity,
   Transparency, and Trust) profile for pre-execution authorization
   records of AI agent actions.  The profile defines a Signed Statement
   type, the "Pre-Execution Authorization Record" (also called a
   Permit), that records a policy-evaluated decision to allow, deny or
   challenge a proposed AI agent action.  A Permit can commit to the
   canonical request body.  For a dispatched allow with a body
   commitment, the profile pairs the Permit with a Closure Record.  The
   Verifier compares the recorded digests.  The reference Issuer checks
   the body binding before managed dispatch.  This document
   distinguishes RFC 9942 COSE Receipts from the reference
   implementation's provisional linked-chain inclusion proof.

   This profile also defines authorization-lineage vocabulary.  It
   defines how a Verifier can determine whether the authority conveyed
   by a child Permit is equal to or narrower than the authority conveyed
   by its parent (attenuation), given a signed or chain-committed
   Authority Representation and a declared Comparator Profile.  The
   Permit remains an evidence artifact; this profile specifies the
   evidence a Verifier needs to make that determination, not a
   delegation or policy protocol.

   The profile composes with adjacent profiles for human-authority
   binding, post-execution material-action evidence, and content-refusal
   events, referenced rather than replicated.
- **draft-durga-pquip-pqc-agentic-delegation-02** (new-draft, score 22, agent_identity) [none]: [Post-Quantum Hybrid Cryptographic Delegation Chains and Merkle-Aggregated Execution Receipts for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-pquip-pqc-agentic-delegation/) — Autonomous AI agent ecosystems rely on multi-hop cryptographic
   delegation chains and signed execution traces (currently built on
   Ed25519, ECDSA P-256, and RSA-PSS) to enforce least-privilege tool
   invocations across Model Context Protocol (MCP) and Agent-to-Agent
   (A2A) boundaries, and to preserve long-term non-repudiation for
   regulatory audit logs.  This architecture faces two vulnerabilities
   in the Post-Quantum transition: (1) "Harvest-Now, Forge-and-
   Repudiate-Later" (HNFRL) attacks, wherein Cryptographically Relevant
   Quantum Computers (CRQCs) running Shor's algorithm retroactively
   forge or repudiate historical classical signatures on compliance
   traces once historical public keys are compromised; and (2) "Lattice
   Signature-Bloat Amplification," wherein naively carrying inline
   3,309-byte ML-DSA-65 ([FIPS204]) signatures and 1,952-byte public
   keys across a 10-hop sub-agent chain inflates raw cryptographic
   material from 960 bytes to 52,610 bytes (over 70 KB when Base64url-
   encoded inside JSON-RPC headers), exceeding typical 8 KB to 16 KB
   HTTP/2 header limits.

   This document specifies a deterministic Post-Quantum Agentic
   Delegation and Trace Receipt profile ("PQ-Agentic").  It defines a
   two-tier cryptographic architecture built strictly from published
   IETF and NIST standards: (a) a Hot-Path Hybrid Delegation Envelope
   combining classical Ed25519 ([RFC8032]) with pure ML-DSA-65
   ([FIPS204]) over a single domain-separated RFC 8785 JSON
   Canonicalization Scheme (JCS) transcript, replacing per-call inline
   re-transmission of prior delegators' 5,261-byte ML-DSA-65 public keys
   and signatures with 32-byte SHAKE256 digests of cached, hybrid-signed
   SessionGrants; and (b) a Cold-Path Archival Profile that registers
   Tier-1 execution receipts and SessionGrants as [RFC9943] SCITT Signed
   Statements with [RFC9942] COSE Receipts and dual post-quantum epoch
   checkpoints sealed with stateless hash-based SLH-DSA-SHAKE-192s /
   SLH-DSA-SHAKE-256s ([FIPS205]) and ML-DSA-87 ([FIPS204]).  Complete
   multi-implementation conformance test vectors are provided.
- **draft-elekula-rats-model-loading-binding-01** (new-draft, score 22, trust_infrastructure) [none]: [Attestation of AI Inference Model Admission and Runtime Binding Using RATS](https://datatracker.ietf.org/doc/draft-elekula-rats-model-loading-binding/) — AI inference execution depends on the relationship between model
   artifacts, transformations applied to those artifacts, model-loading
   mechanisms, inference runtimes, and execution hardware. Evidence that
   independently identifies a model artifact and an inference runtime
   does not establish that the identified artifact was admitted into the
   identified runtime. This distinction becomes material when model
   artifacts are decompressed, quantized, compiled, sharded, combined
   with adapters, transferred to accelerators, or dynamically replaced
   before or during execution.

   This document defines Model Admission Binding (MAB) as an
   attestation-oriented relationship between an identified model
   artifact set, its transformation history, a model-loading event, an
   identified inference-runtime instance, and the execution domain into
   which the resulting representation is admitted.

   The document applies the Remote ATtestation procedureS (RATS)
   architecture defined in RFC 9334 and examines the use of Entity
   Attestation Tokens (EAT) and the measured-component information model
   defined in RFC 9711 and RFC 10013. It identifies the measurement and
   provenance requirements necessary to establish model admission,
   distinguishes source-artifact identity from the identity of the
   representation actually consumed by a runtime, and defines the
   conditions under which a Verifier can appraise the resulting
   relationship.

   Model Admission Binding is an information and assurance concept. This
   document does not define a new RATS role, attestation protocol, EAT
   serialization, registered Claim, Evidence conveyance protocol, or
   appraisal-policy language. It identifies how existing RATS mechanisms
   can represent and appraise a model-to-runtime relationship and
   identifies the implementation requirements that make that
   relationship verifiable.
- **draft-mckenna-webbotauth-collection-attestation-03** (new-draft, score 22, trust_infrastructure) [none]: [Attested Conduct for Anonymous Web Data Collection: Use Cases, Requirements, and a Tiered Model](https://datatracker.ietf.org/doc/draft-mckenna-webbotauth-collection-attestation/) — Anonymous Bot Authentication lets a web site learn that an automated
   client holds a credential from an Anchor whose policies it accepts,
   without learning which client it is.  This document describes web
   data collection use cases that need that property, and what they
   require of the evidence behind an Anchor's endorsement, of what a
   site can verify about conduct it cannot attribute, and of what a
   buyer of collected data needs to see.  It proposes a tiered model.
   Collectors register signed statements of their own conduct in a SCITT
   Transparency Service; the site, its security intermediary, or a
   network intermediary may corroborate them; and a Certifier may
   appraise them, giving an Anchor evidence for issuing endorsements.
   Coarse attributes about the data's eventual recipient could let a
   site restrict use by category of recipient without learning who the
   recipient is.
- **draft-munoz-wimse-authorization-evidence-02** (new-draft, score 22, authorization) [none]: [Signed Authorization-Evidence Records for AI Agent Actions Using WIMSE Workload Identity](https://datatracker.ietf.org/doc/draft-munoz-wimse-authorization-evidence/) — This companion to the WIMSE AI Identity Management System (AIMS)
   document specifies how an Issuer records a pre-execution
   authorization decision for an AI agent using WIMSE workload identity.
   The signed record, called a Permit, can bind the decision to a
   canonical request body.  For a dispatched allow with a request-body
   commitment, a paired Closure Record carries the recorded dispatch
   digest.  The profile maps these and related records to the audit
   requirements in Section 11 of AIMS and describes optional composition
   with HTTP Message Signatures, OAuth access tokens and Shared Signals
   Framework events.  The companion SCITT profile (draft-munoz-scitt-
   permit-profile) specifies the Permit and Closure Record.

   This revision also describes how WIMSE deployments compose with
   authorization-lineage evidence defined by the companion SCITT
   profile: workload identity, delegated subject context, runtime token
   claims, and HTTP Message Signature coverage become Verifier inputs
   for parent/child Permit relationships.
- **draft-gruszka-audit-decision-receipts-12** (new-draft, score 20, trust_infrastructure) [none]: [Decision Receipts for Approvals, Declined Actions and Executed Actions in Agent Audit Records](https://datatracker.ietf.org/doc/draft-gruszka-audit-decision-receipts/) — The architecture for auditing agent delegation and interactions
   proposed for the AUDIT effort names Interaction Records, Action
   Records and Authorization Transition Records and leaves their
   encoding open.  This document maps a pair of signed records, the
   decision receipt and the outcome receipt, onto those record types for
   three cases, a human approval, a declined action and an executed
   action with its result.  It states what each record requires
   independently of its encoding: exact bytes, a signature over them,
   digest bindings, required members and a content root, with
   verification steps that a third party can run offline.  It gives a
   binding to the Dead Simple Signing Envelope (DSSE) and in-toto,
   updating the receipt type identifiers used by existing receipts, and
   a second binding to COSE_Sign1, in which a receipt is itself a Signed
   Statement for a Transparency Service.  Each receipt is created when
   the decision or the outcome occurs and is checked by an Auditor post
   hoc, and a declined or refused action is a record of its own.  For
   each case the document states what the receipt adds and what it does
   not show, and it gives a verification procedure that runs offline.
   It requires that an approval be honoured at most once, even after the
   record of consumed approvals is rotated.  Test vectors for all three
   cases, each with a counterexample, are included.  The document also
   describes, informatively, how a receipt can be registered with a
   Transparency Service under RFC 9943, the architecture of Supply Chain
   Integrity, Transparency, and Trust (SCITT), and what a SCITT Receipt
   then shows and does not show.  It defines no new predicate or
   registry; the COSE_Sign1 binding names its two receipt types by new
   identifiers.  How the issuer of a receipt enforces its decision is
   out of scope.
- **draft-malhotra-scitt-oar-01** (new-draft, score 20, authorization) [none]: [Open Action Record (OAR): Authority, Approval and Outcome Evidence for AI Agent Actions](https://datatracker.ietf.org/doc/draft-malhotra-scitt-oar/) — Several profiles record what an AI agent was asked to do, and the
   decision taken, as signed statements registered with a transparency
   service.  Protocols for agent identity and delegated authorization
   say whether an agent may ask.  After an incident or in a dispute,
   three further questions decide the case: were the authorizations the
   action relied on still valid when it committed, did a named person
   approve this exact action, and did the action change the system of
   record as recorded?

   This document defines evidence that any agent action profile can add
   to answer them: an authority set that binds the digests of the
   outside authorizations an action relied on to that one action, with a
   re-check recorded at the moment it commits; an approval binding that
   ties a person's confirmation, by a passkey or an outside approval
   service, to the exact action and to what the person was shown; salted
   commitments to the affected state before and after execution; an
   outcome confirmation made by reading the system of record; and three
   outcome classes a relying party can act on.  Values are hidden behind
   salted commitments and can be disclosed field by field.  It also
   states how a verifier obtains the keys and times used to check
   signatures, so that neither comes from the signer.  The constructions
   are implemented in the Open Action Record (OAR) format, with three
   verifiers that agree on published test vectors.
- **draft-rampalli-pedigree-01** (new-draft, score 19, core_identity) [none]: [PEDIGREE: Verifiable Delegation Identity for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-rampalli-pedigree/) — This document defines PEDIGREE (Per-Agent Delegation Identity with
   Governance-Enforced Execution), a delegation token profile for AI
   agents that operates above WIMSE workload credentials.  A PEDIGREE
   chain names one principal at every hop, names the agent acting at
   each hop, binds each child token to a digest of its parent's JWS
   Signing Input, and grants authority as named resources with actions
   that each hop can only narrow.  A separate invocation object, signed
   by the leaf agent, names the one action, resource, and arguments
   being requested, and the verifier evaluates exactly that.  A verifier
   can check a chain offline when it holds every input the chain needs:
   its trust anchors, its accepted ceilings, and any status answers that
   are still within their time to live.

   The linkage, principal, holder-binding, invocation, and status rules
   follow mechanisms specified in other documents and are cited as such.
   On that base, PEDIGREE defines four elements: an operator ceiling,
   referenced by digest and evaluated together with each token's grants
   at decision time; an optional Cedar mandate per token, with a
   syntactic narrowing check and an optional proof artifact; signed
   completion blocks, in which an agent reports an outcome under the key
   its token binds; and consent identifiers carried in every token and
   checked by every verifier against a configured consent status source.
- **draft-ietf-rats-ear-06** (new-draft, score 18, verifiable_claims) [rats]: [EAT Attestation Results](https://datatracker.ietf.org/doc/draft-ietf-rats-ear/) — This document defines the EAT Attestation Result (EAR) message
   format.

   EAR is used by a verifier to encode the result of the appraisal over
   an attester's evidence.  It embeds an AR4SI's "trustworthiness
   vector" to present a normalized view of the evaluation results, thus
   easing the task of defining and computing authorization policies by
   relying parties.  Alongside the trustworthiness vector, EAR provides
   contextual information bound to the appraisal process.  This allows a
   relying party (or an auditor) to reconstruct the frame of reference
   in which the trustworthiness vector was originally computed.  EAR
   supports simple devices with one attester as well as composite
   devices that are made of multiple attesters, allowing the state of
   each attester to be separately examined.  EAR can also accommodate
   registered and unregistered extensions.  It can be serialized and
   protected using either CWT or JWT.
- **draft-stafordtituss-agentic-mandate-evidence-02** (new-draft, score 18, adjacent_watchlist) [none]: [Continuity Evaluation of Agent Delegation Records](https://datatracker.ietf.org/doc/draft-stafordtituss-agentic-mandate-evidence/) — The AUDIT architecture defines records that capture the user's
   intent, delegation, authorization state, and the actions that agents
   take across trust boundaries.  Records alone don't answer the
   question an auditor, an operator, or a relying party asks next: did
   what was executed stay within the authority the user delegated?

   This document defines a deterministic, three-valued evaluation over
   such records.  The outcomes are preserved, violated, and unresolved.
   A violated outcome names the invariant that was broken and the party
   whose own signed record departed from authority first.  An unresolved
   outcome names the evidence that is missing; missing evidence is never
   treated as success.  The document also defines the claim model the
   evaluation needs, the roles permitted to sign each record, a signed
   statement of what a call did or did not execute, a portable verdict
   record, a mapping onto the AUDIT record types, and interoperable test
   vectors.  It is derived from the Agentic Mandate Evidence Protocol
   (AMEP).
- **draft-uppalapati-wimse-pq-agent-identity-02** (new-draft, score 18, core_identity) [none]: [Post-Quantum Requirements for Software and AI Agent Identity](https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/) — A delegation record retained as evidence must remain verifiable long
   after the key that signed it is retired.  A signature of any
   algorithm establishes who signed, not when, so such a record needs
   anchoring in trusted time, renewed before the algorithms protecting
   it weaken.  That is long-settled practice for archived signatures.
   It is rarely required for agent delegation, and where it is, the
   anchor is not itself required to be post-quantum.  An anchor is only
   as good as the protection behind it, and an RFC 3161 timestamp is
   itself a signature: an adversary holding a cryptanalytically relevant
   quantum computer can mint one bearing any date it chooses.  Because
   such a machine may be built without announcement, anchoring must
   become post-quantum anchoring by a stated transition date, and be
   applied early, so that the only assumption left about when such a
   machine appeared is that none existed before a record was first
   anchored that way.  The earlier that date, the weaker the assumption,
   which makes choosing it a security decision and not only a scheduling
   one.

   This document states requirements that software and AI agent identity
   mechanisms should satisfy in order to remain sound across the
   transition, and identifies four that no such mechanism yet imposes on
   delegation credentials in general.  The algorithms binding each hop
   of a delegation chain to its trust anchor must be visible to a
   verifier and retained with any record kept as evidence; where a
   signing key is fetched from a key set over TLS, as OAuth deployments
   commonly do, that binding is rarely recorded and no mechanism for
   agent delegation requires it to be, so in practice it is absent.
   Trust anchors must migrate before the credentials issued under them.
   Every retained record must be anchored, that anchoring must become
   post-quantum anchoring from a stated transition date and be
   maintained by renewal, and credentials of any type kept as evidence
   must be signed post-quantum from that same date.  Delegation chains
   also propagate the weakest algorithm in the chain, and routinely
   cross organizational boundaries where no common trust anchor policy
   can be assumed.
- **draft-elekula-rats-ai-inference-binding-00** (new-draft, score 17, trust_infrastructure) [none]: [Evidence for AI Inference Execution and Result Binding Using RATS](https://datatracker.ietf.org/doc/draft-elekula-rats-ai-inference-binding/) — AI inference services may execute within Trusted Execution
   Environments (TEEs), confidential virtual machines, protected
   processes, or heterogeneous platforms containing accelerators.
   Remote attestation can provide evidence about the identity,
   integrity, configuration, and operational state of components.
   Such evidence does not, by itself, establish that a particular
   inference request was processed by a particular model
   representation, that the claimed computation was faithfully
   performed, or that the result delivered to a relying party is the
   result of that operation.

   This document defines an architecture for associating
   inference-operation evidence, model and runtime identity,
   execution-assurance evidence, freshness context, and the delivered
   result. It applies the RATS architecture and existing IETF formats
   without defining a new RATS role, protocol, cryptographic
   primitive, EAT claim, or universal inference-result format. It
   distinguishes integrity of association from evidence of
   computational execution and from semantic correctness.
- **draft-farley-acta-signed-receipts-04** (new-draft, score 17, core_identity) [none]: [Signed Decision Receipts for Machine-to-Machine Access Control](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) — This document defines a portable, cryptographically signed receipt
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
- **draft-kamimura-scitt-vcp-07** (new-draft, score 17, trust_infrastructure) [none]: [A SCITT Profile for Verifiable Audit Trails in Algorithmic Trading: The VeritasChain Protocol (VCP)](https://datatracker.ietf.org/doc/draft-kamimura-scitt-vcp/) — This document defines a profile of the SCITT (Supply Chain Integrity,
   Transparency, and Trust) architecture for creating tamper-evident
   audit trails of AI-driven algorithmic trading decisions and
   executions.  The VeritasChain Protocol (VCP) applies the SCITT
   framework to address the specific requirements of financial markets,
   including high-precision timestamps, considerations arising from
   recordkeeping regimes such as the EU AI Act and MiFID II, and a
   crypto-shredding mechanism intended to support erasure obligations
   such as those under the GDPR.  This profile specifies how VCP events
   are encoded as SCITT Signed Statements, registered with Transparency
   Services, and verified using COSE Receipts.  It further defines SCITT
   conformance profiles for interoperability and an ERASURE event type
   that records crypto-shredding operations as append-only audit events.
   The profile makes trading records auditable and attributable after
   the fact; it does not prevent or block any trading activity, and it
   does not warrant the correctness of any recorded decision.
- **draft-luna-eagf-agent-delegation-semantics-03** (new-draft, score 17, core_identity) [none]: [Semantic Governance Requirements for AI Agent Delegation and Handoff](https://datatracker.ietf.org/doc/draft-luna-eagf-agent-delegation-semantics/) — AI agents increasingly decide and act on behalf of organizations and
   delegate work to other agents.  Identity, authentication,
   authorization and runtime control mechanisms establish who is acting
   and what is permitted, but they do not by themselves preserve the
   organizational meaning of a delegation: the bounded authority,
   purpose, material context, and the distinction between a
   recommendation, a decision, an action and its outcome.  This document
   states requirements, derived from the Enterprise Agent Governance
   Framework (EAGF), that such semantics be preserved across tool calls,
   delegations and agent-to-agent handoffs.  It defines no new protocol.
- **draft-mih-scitt-agent-action-capsule-06** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
   AI agent did: the Agent Action Capsule.  A Capsule is a digest-
   committed record of one agent action carrying its verdict-level
   disposition (executed, blocked, denied, errored, timed out), the
   deterministic constraints that were evaluated, the effect that was
   committed together with a confirmed-effect binding that distinguishes
   a dispatched attempt from an observed result, and an honest human-in-
   the-loop flag.  Capsules are identified independently of signing and
   MAY be authenticated by one or more COSE_Sign1 Producer Envelopes.
   Its Capsule ID can separately be made transparent by registration in
   a SCITT Transparency Service.  A Capsule is recorded on every
   verdict, including refusals: a blocked or denied Capsule is the
   auditor-grade evidence that a gate worked.
- **draft-zambo-aer1-attribution-profile-01** (new-draft, score 17, core_identity) [none]: [AER-1 Attribution Profile: Optional Maker Attestation for AER-1 Execution Receipts](https://datatracker.ietf.org/doc/draft-zambo-aer1-attribution-profile/) — AER-1 specifies a portable execution receipt for AI agent tool calls.
   A receipt's output commitment lets any party recompute the digest of
   the saved result and establish that the result was not changed after
   the commitment was recorded.  AER-1 deliberately defines no issuer
   authentication: its Security Considerations state that verification
   proves the recorded bytes were not altered after minting, not who
   minted them, and direct consumers that need to bind a receipt to its
   issuer to "a signature scheme documented alongside the receipt".
   This document is that scheme, for the consumers that need it.  It
   defines an optional maker attestation: a signature, by a key the
   maker controls, over a small commitment that binds the receipt's
   output_hash, the receipt's identifier, and the receipt's caller
   scope.  A relying party that evaluates the attestation can establish
   which key attested to a record whose integrity the AER-1 recompute
   separately establishes.  The profile is optional in the strong sense:
   it is never required for AER-1 conformance, a keyless implementation
   remains fully conformant, and a receipt carrying no attestation is a
   normal receipt, not a defective one.  The attestation proves that a
   key signed the commitment; it does not prove that the saved result
   was right, that the work happened, or that the key's holder is any
   particular person.  Attribution outcomes are reported beside the
   AER-1 verification report, in the same present, evaluated, outcome
   discipline AER-1 uses for anchors, and they never alter the AER-1
   structural verdict, id verdict, or anchor outcomes.
- **draft-cea-list-vaultys-oauth-agent-deleg-reqs-gaps-00** (new-draft, score 16, authorization) [none]: [Delegation for Agentic AI in OAuth-Based Architectures: Requirements and Gap Analysis](https://datatracker.ietf.org/doc/draft-cea-list-vaultys-oauth-agent-deleg-reqs-gaps/) — The OAuth 2.0 authorization framework and its associated
   specifications define mechanisms for delegating authority from a
   resource owner to a client acting on its behalf.  These mechanisms
   are designed mainly for a single-principal, single-hop model in which
   a human authorizes a client at authorization time (the client
   credentials grant, in which a client acts on its own behalf, is the
   exception).  Agentic AI systems introduce a fundamentally different
   operational context: autonomous software agents that execute multi-
   hop delegation chains, propagate constrained authority across
   organizational boundaries, and perform consequential actions without
   continuous human involvement.  This document analyzes the normative
   gaps between the requirements for secure delegation in Agentic AI
   systems and the coverage provided by the existing published OAuth 2.0
   RFC corpus.  Fifteen requirements decomposed into 111 sub-
   requirements are evaluated against 41 mechanisms, including 18
   published RFCs, 11 Internet-Drafts, and 12 informative prior-art and
   non-IETF specifications.  The analysis identifies 48 sub-requirements
   (43%) for which no published RFC provides normative coverage, and no
   sub-requirement that remains unaddressed by every evaluated
   mechanism; for 15 of these 48 gaps, no evaluated Internet-Draft is
   credited with complete coverage.  This document does not define new
   protocol mechanisms.  Its output defines the normative gaps that a
   companion solution specification must address to extend the OAuth 2.0
   framework to support secure, accountable, and interoperable
   delegation in Agentic AI deployments.
- **draft-jovancevic-bvap-02** (new-draft, score 16, trust_infrastructure) [none]: [Browser Vendor Attestation Protocol (BVAP)](https://datatracker.ietf.org/doc/draft-jovancevic-bvap/) — The HTTP User-Agent header field allows any client to claim any
   browser identity without cryptographic proof. Any software may
   assert "Mozilla/5.0 Chrome/124" regardless of its actual origin,
   distribution source, or software provenance.

   This document specifies BVAP (Browser Vendor Attestation Protocol),
   a mechanism by which browser vendors cryptographically attest that
   a browser instance originates from a legitimate, vendor-issued
   browser build. Attestation occurs at installation time and is
   periodically renewed. The resulting Vendor Attestation Seal
   (BVAP Seal) is carried by the browser and is primarily transmitted
   via the Sec-BVAP header field. The Seal MAY additionally appear
   in the User-Agent string for backward compatibility with legacy
   infrastructure.

   BVAP provides software provenance and vendor authenticity at the
   browser layer. The protocol allows servers to distinguish between:

   o  Vendor-attested browser software,
   o  Anonymous or self-built browser software (Unattested), and
   o  Software falsely claiming vendor browser identity.

   BVAP requires no per-request cryptography and no DNS lookups
   during normal operation.

   BVAP proves browser origin, not browser behavior.
- **draft-wei-capability-language-core-02** (new-draft, score 16, adjacent_watchlist) [none]: [Capability Language Core](https://datatracker.ietf.org/doc/draft-wei-capability-language-core/) — This document defines the Capability Language Core (CLC), a minimal,
   executable language for describing what an agent is authorized to do.
   It defines the capability identifier grammar, the entailment relation
   between a grant and an operation, intersection of grants from
   multiple sources, the constraint model, and a deterministic decision
   function with stable reason codes and a three-valued verdict (allow,
   deny, allow_unresolved).

   The language is carrier-neutral: it defines what is evaluated, not
   how it is carried or trusted.  Trust models, native verification,
   execution lifecycle, and receipt or token formats are out of scope
   (Section 11).  Conformance is exercised by a published corpus of 154
   vectors and 1184 property cases; three implementations (Go, Python,
   TypeScript) that share an author pass both. *Implementation
   conformance and this document's claim of a conformance class are
   separate.* An implementation conforms to CLC-A when it meets the
   obligations Section 12 lists for that class, and it may claim that
   conformance on its own, whatever other implementations exist.
   Section 12 additionally sets a maturity bar for _this document's_
   claim — two independent implementations agreeing on verdict and
   reason.  That bar is *not* met here.  The three implementations named
   in the README share an author, so their agreement is a regression
   test for the text, not independent validation; one independent
   implementation now passes the CLC-A core corpus (Section 12,
   "Independence of implementations"), which is the first of the two the
   bar asks for.  CLC-A is still claimed by this revision as the
   baseline authorization class, whose obligations are implementable and
   exercised by a published corpus; the two-implementation threshold
   remains recorded as unmet.  The evidence-side class CLC-E is *not*
   claimed: its relations, value grammar, reference implementation and
   corpus ship here.

   This revision also folds the delegation *containment* relation into
   the document (Section 13): Contains(parent, child) decides whether a
   child grant stays inside a parent's declared boundary — the single
   question a delegation chain asks at every hop that the core's
   entailment and intersection do not answer.  It ships with the
   conformance class *CLC-D* and its own corpus, is strictly additive,
   and changes no CLC-A verdict, reason code, or vector.  It absorbs the
   previously separate experimental containment extension, which is
   retired.
- **draft-bu-agentproto-security-principal-binding-09** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-elekula-rats-pqc-attestation-01** (new-draft, score 15, trust_infrastructure) [none]: [Post-Quantum Cryptographic Considerations for RATS Evidence and Attestation Results](https://datatracker.ietf.org/doc/draft-elekula-rats-pqc-attestation/) — The Remote ATtestation procedureS (RATS) architecture defines
   Evidence, Endorsements, Reference Values, and Attestation Results
   as distinct conceptual artifacts used by Attesters, Verifiers,
   Endorsers, and Relying Parties.  The transition to post-quantum
   cryptography (PQC) raises questions about the protection,
   validation, transport, transformation, and retention of these
   artifacts.

   This document examines post-quantum cryptographic considerations
   across the lifecycle of RATS artifacts.  It distinguishes
   post-quantum key establishment from artifact authentication and
   considers the security properties that must be evaluated
   independently: integrity, origin, signer authority, freshness,
   session context, provenance, appraisal, and authorization.

   The document introduces three analytical constructs: the
   Artifact Protection Matrix, the Provenance Continuity Chain,
   and the Cryptographic Transition Assessment.  These constructs
   provide a structured way to identify artifact-specific
   protection requirements, evaluate transformations, and preserve
   the information needed for later cryptographic verification.

   The analysis also addresses algorithm selection, cryptographic
   agility, artifact size, bounded processing, transport
   considerations, replay resistance, long-term verifiability,
   interoperability, testing, and privacy.

   This document does not define a new cryptographic algorithm,
   RATS message, token format, transport protocol, TLS extension,
   key-establishment mechanism, or appraisal-policy language.
   It provides security analysis and implementation guidance
   within the existing RATS architecture and established
   cryptographic standards.
- **draft-hood-agentproto-mcp-over-agtp-00** (new-draft, score 15, core_identity) [none]: [Model Context Protocol over the Agent Transfer Protocol](https://datatracker.ietf.org/doc/draft-hood-agentproto-mcp-over-agtp/) — This document specifies how the Model Context Protocol (MCP) is
   carried over the Agent Transfer Protocol (AGTP).  MCP defines JSON-
   RPC 2.0 methods through which a language model application reaches
   tools, resources, and prompts.  AGTP is a transfer protocol for agent
   traffic that carries agent identity, authority scope, delegation, and
   signed attribution as headers of every request and response.  This
   document maps each MCP operation onto an AGTP method and path, states
   how JSON-RPC results and errors translate to the AGTP envelope and
   status codes, and specifies the identity, authorization, and
   attribution behavior an MCP client inherits when it speaks AGTP.  It
   describes a gateway deployment in which an existing stdio MCP server
   is exposed over AGTP without modification, and it records the status
   of the running implementation.
- **draft-jones-scitt-pain-point-resolutions-00** (new-draft, score 15, verifiable_claims) [none]: [Resolution of SCITT and W3C Verification Ambiguities via Detached Evidence Profiles](https://datatracker.ietf.org/doc/draft-jones-scitt-pain-point-resolutions/) — RFC 9942 (COSE Receipts), RFC 9943 (the SCITT architecture), and the
   W3C Verifiable Credentials Data Model v2.0 provide the foundational
   architecture for transparent, verifiable statements.  Operational
   ambiguities remain in receipt verification, statement identity,
   status freshness, and the boundary between what a receipt proves and
   what a relying party must establish separately.  This document maps
   fifteen documented pain points to constructions in four individual
   Internet-Drafts (a dual-receipt profile, a detached evidence handoffs
   model, a reproducible-review method, and a handshake profile).  Where
   none of those drafts applies, it either proposes a construction or
   names the existing external mechanism, and for every pain point it
   states which case applies and what gap remains.  Delivery is
   detached: no API integration, standing connection, or middleware is
   required.  This document does not amend RFC 9942, RFC 9943, or any
   W3C Recommendation.  All test vectors are synthetic.
- **draft-kanojia-creduent-agent-uri-01** (new-draft, score 15, core_identity) [none]: [The 'agent' Uniform Resource Identifier (URI) Scheme and Cryptographic Attestation Protocol](https://datatracker.ietf.org/doc/draft-kanojia-creduent-agent-uri/) — This document specifies the 'agent' Uniform Resource Identifier (URI)
   scheme and its associated cryptographic attestation protocol.  The
   'agent' scheme defines a transport-agnostic, cryptographically
   verifiable addressing layer for identifying autonomous software
   agents, binding domain ownership via DNSSEC TXT records, resolving
   agent identity documents via deterministic HTTPS well-known paths,
   and validating attenuated capability delegation tokens.
- **draft-hood-oauth-over-agtp-00** (new-draft, score 14, core_identity) [none]: [OAuth 2.0 over the Agent Transfer Protocol](https://datatracker.ietf.org/doc/draft-hood-oauth-over-agtp/) — This document specifies how the OAuth 2.0 authorization framework is
   carried over the Agent Transfer Protocol (AGTP).  OAuth defines its
   endpoints as HTTP resources and authenticates clients with secrets or
   signed assertions.  AGTP is a transfer protocol for agent traffic in
   which every request carries the sending agent's identifier and a
   proof that the sender holds that agent's key.  This document defines
   an authorization server reachable as an AGTP agent, maps the token,
   pushed authorization, device authorization, revocation,
   introspection, and metadata endpoints onto AGTP methods and paths,
   replaces client authentication with the AGTP request signature, and
   defines access tokens bound to an Agent-ID.  It states which parts of
   OAuth move to AGTP and which remain on HTTPS.  It changes no OAuth
   grant.
- **draft-ietf-wimse-http-signature-09** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload-to-Workload Authentication with HTTP Signatures](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).
- **draft-ietf-wimse-workload-identity-practices-09** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-moore-scitt-ciris-trace-context-00** (new-draft, score 14, trust_infrastructure) [none]: [Context Manifests for the CIRIS Agent Trace: Prompt Context Provenance for AI Agent Decision Traces](https://datatracker.ietf.org/doc/draft-moore-scitt-ciris-trace-context/) — An AI agent that acts on a person's behalf makes each decision
   through several calls to language models: one stage drafts an action,
   others evaluate it, and others may veto it.  What each call was given
   decides what it can judge.  A record of the action alone cannot show
   whether a judging stage lacked a rule the drafting stage had, whether
   untrusted text reached a stage designed never to see it, or whether a
   stage was prompted in a language other than the one the person used.

   This document specifies a per-call context manifest.  It describes
   every contiguous piece of text placed into a model call (a segment)
   by what it is, where it came from, how far it can be trusted, which
   authority stands behind it, how long it lives, and which language it
   is in.  It specifies a closed-vocabulary context policy that says
   which stage may and must receive which kinds of segment, ablation
   stubs that stand in for text withheld from a stage, and the checks a
   verifier runs against the manifest and against the bytes actually
   sent.  It states the safety properties of the policy as invariants
   checked by a model checker.  The context manifest is the
   context_manifest member of the LLM_CALL event of the CIRIS agent
   trace, carried in a CEG trace row; it can also be the payload of any
   SCITT signed statement.
- **draft-yu-agent-identifier-rdap-01** (new-draft, score 14, core_identity) [none]: [An RDAP Profile for Agent Identifier Registration Data](https://datatracker.ietf.org/doc/draft-yu-agent-identifier-rdap/) — AI agents may need stable identifiers that are independent from their
   current network locations.  In agent deployments, an Agent identifier
   may be associated with IPv6 locators, IPv6 prefixes, Agent Gateways,
   public key references, policy references, lifecycle state, and
   revocation status.  Applications, gateways, controllers, and
   operators need a trusted way to query this registration data.

   This document defines an RDAP profile for querying Agent identifier
   registration data.  The profile reuses the Registration Data Access
   Protocol (RDAP) query model and JSON response format, and defines an
   RDAP object class and extension members for Agent identifiers, IPv6
   locator bindings, Agent Gateway bindings, and related operational
   metadata.

   This document does not define a new agent discovery protocol, a new
   agent interaction protocol, or a new authentication mechanism.  It
   defines a registration data access profile that can be used by agent
   deployments and by other agent-related systems that need trusted
   Agent identifier metadata.
- **draft-gruszka-scitt-statement-identification-05** (new-draft, score 13, trust_infrastructure) [none]: [Requirements and Test Cases for Identifying SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-gruszka-scitt-statement-identification/) — This document describes proposed requirements and test cases for
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
- **draft-hood-agentproto-poppy-over-agtp-00** (new-draft, score 13, core_identity) [none]: [Personal Agent Protocol (Poppy) over the Agent Transfer Protocol](https://datatracker.ietf.org/doc/draft-hood-agentproto-poppy-over-agtp/) — This document specifies how the Personal Agent Protocol (PAP, also
   called Poppy) is carried over the Agent Transfer Protocol (AGTP).
   Poppy defines how a personal agent acting for one person discovers a
   company, opens a session, signs the person in with OAuth, and acts
   through the company's APIs, website, or agent.  Poppy 1.0 specifies
   these exchanges over HTTPS.  AGTP is a transfer protocol for agent
   traffic that carries agent identity, authority scope, delegation, and
   signed attribution as headers of every request and response.  This
   document maps each Poppy exchange onto an AGTP method and path, binds
   the Poppy client identifier and User ID to the AGTP identifier stack,
   states which Poppy functions AGTP headers supply and which remain
   with OAuth over HTTPS, and records the open issues the mapping
   raises.  It defines no change to Poppy.
- **draft-ietf-agentproto-usecases-requirements-00** (new-draft, score 13, core_identity) [agentproto]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-agentproto-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-miao-agw-core-functional-architecture-01** (new-draft, score 13, adjacent_watchlist) [none]: [Agent Gateway Core functional Architecture](https://datatracker.ietf.org/doc/draft-miao-agw-core-functional-architecture/) — This document defines the core functional architecture of the Agent
   Gateway as a universal infrastructure component.  The Agent Gateway
   is designed to address key challenges in single-domain multi-agent
   collaboration and cross-domain multi-agent communication, including
   trust boundaries, protocol termination, capability discovery, and
   task routing.  The main framework consists of four gateway
   capabilities: the A2A Gateway (supporting inter-agent communication),
   the MCP Gateway (supporting tool invocation), the Model Routing
   Gateway (supporting large language model invocation), and the Network
   Gateway (supporting underlying network connectivity).  The A2A
   Gateway is further decomposed into five core capabilities: protocol
   translation, authentication and security, asynchronous task
   management, peer-to-peer network management, and Agent routing
   capabilities (including Agent registry, capability discovery, task
   routing, and load balancing).  This document is intended for
   designers and implementers seeking to build standardized,
   interoperable agent communication infrastructure.
- **draft-mih-agent-evidence-layer-01** (new-draft, score 13, trust_infrastructure) [none]: [Evidence Layer](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-layer/) — This document defines the evidence layer: the conformance
   requirements for a local evidence store that records evidence and the
   relationships between records, keeps digests committed while payloads
   are separately referenced, and preserves how each record came to be
   known well enough that a later reader can tell an observation from a
   claim.  This document defines the record model, typed links between
   records, disclosure and retention semantics, the three classes of
   index a store may maintain, and the minimum interface any commitment
   substrate must supply for a store to conform to this layer.  It
   exists so that a request for evidence can be answered honestly from
   what a store actually holds, and so that an evidence bundle assembled
   in response is assembled from committed material rather than
   assembled and then made to look committed.  Conformance to this layer
   MUST NOT require any particular implementation or commitment
   substrate: a Checkpointed Local Log is one conforming profile;
   registration with a SCITT Transparency Service is another; any other
   append-only transparency log, or an implementer's own authenticated
   log, also qualifies.  This document defines neither evidence
   sufficiency policy, request routing, settlement, nor any specific
   host-identity, signing, payload-storage, or replication mechanism.
- **draft-morrison-acts-for-04** (new-draft, score 13, authorization) [none]: [Acts-For: Signing In to a Website with a ~handle, for a Person or an Agent Acting for One](https://datatracker.ietf.org/doc/draft-morrison-acts-for/) — Acts-For lets a person sign in to any website with the ~handle they
   already hold, and lets an AI agent sign in or register at that
   website on the person's behalf.  Neither needs a username, a password
   or an account per site.  A website joins by publishing one DNS
   record.  A person signs in through a standard OpenID Connect
   authorization code flow and the site receives a short-lived token
   naming the person by a number unique to that site.  An agent obtains
   a short-lived pass from the issuer over the Model Context Protocol
   and presents it to the site.  The pass names the same per-site
   number, the agent's ~handle, a number and key the agent has for that
   site, and the limits the person set.  The site checks it against a
   published key without contacting the issuer.
- **draft-sweeney-oauth-brokered-authorization-00** (new-draft, score 13, authorization) [none]: [OAuth Brokered Authorization: Grant Custody for Short-Lived Client Instances](https://datatracker.ietf.org/doc/draft-sweeney-oauth-brokered-authorization/) — An OAuth client identifier names a registration.  It does not name
   the running instance that presents a token.  Where one registered
   client runs as many short-lived instances, as agent platforms do,
   work now in progress binds refresh tokens to the instance.  Where a
   refresh token is bound to the instance, an authorization that a user
   gave through one instance ends with that instance, and no
   specification says how the next instance comes to act under it.

   This document specifies one answer.  A broker is the single, durable
   OAuth client of an upstream resource.  It holds the grant and the
   credential for that resource and makes each request itself.  A
   resource owner authorizes a registered client to use that grant
   through the broker, and the authorization server records the
   authorization against the client and not against any instance.  Each
   instance obtains a short-lived, sender-constrained access token for
   the broker with the client credentials grant.  An instance never
   holds a grant, a refresh token, or the upstream credential, and no
   instance is registered anywhere.  This document defines the
   authorization details type that carries this authority, the checks
   the broker makes before it acts, and one error code.
- **draft-ietf-acme-openid-federation-01** (new-draft, score 12, adjacent_watchlist) [acme]: [Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0](https://datatracker.ietf.org/doc/draft-ietf-acme-openid-federation/) — The Automatic Certificate Management Environment (ACME) protocol
   allows server operators to obtain TLS certificates for their
   websites, based on a demonstration of control over the website's
   domain via a fully-automated challenge/response protocol.

   OpenID Federation 1.0 defines how to build a trust infrastructure
   using a trusted third-party model.  It uses a trust evaluation
   mechanism to attest to the possession of private keys, protocol
   specific metadata and miscellaneous administrative and technical
   information related to a specific entity.

   This document defines how X.509 certificates associated with a given
   OpenID Federation Entity can be issued by an X.509 Certification
   Authority through the ACME protocol to the organizations which are
   part of a federation built on top of OpenID Federation 1.0.
- **draft-jovancevic-vdac-07** (new-draft, score 12, core_identity) [none]: [Verifiable Data Access Contract (VDAC)](https://datatracker.ietf.org/doc/draft-jovancevic-vdac/) — This document specifies the Verifiable Data Access Contract (VDAC),
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
- **draft-rosario-http6-authority-continuity-00** (new-draft, score 12, authorization) [none]: [HTTP6 Authority Continuity from Human Approval to Resource Commitment](https://datatracker.ietf.org/doc/draft-rosario-http6-authority-continuity/) — A person can authorize an autonomous artificial intelligence (AI)
   agent to delegate a task that another organization completes.  At the
   point of execution, the resource owner needs to know which authority
   survives delegation, which running instance is exercising it, and
   whether the requested effect has already occurred.  This document
   proposes an architecture for carrying that evidence across
   administrative boundaries.  An admission receipt records the human
   decision.  Each child receives a grant, bounded by its parent's
   authority, that is tied to its own running instance.  A state ledger
   coordinates revocation, shared allowances, and recovery.  The
   resource enforces its own policy and returns evidence of the effect
   it committed.  An initial profile uses existing HTTPS mechanisms.  A
   two-domain demonstration defines how independent implementations can
   test these properties when a reply is lost or an older backup is
   restored.
- **draft-rosario-http6-problem-statement-00** (new-draft, score 12, adjacent_watchlist) [none]: [Hereditary Authorization and Runtime-Bound Application Channels: Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-rosario-http6-problem-statement/) — Existing Internet security mechanisms authenticate communication
   endpoints, human principals, and software workloads.  However,
   independent implementations do not necessarily share a common
   representation of the relationship between an originating
   authorization, subsequent workload generations, delegated
   permissions, and resulting application effects across administrative
   boundaries.  This document investigates whether additional
   interoperability conventions are needed to preserve and enforce that
   relationship.

   The proposed model establishes a bounded root of authority through an
   originating authorization.  Descendant workloads operate under
   independently identifiable, revocable, non-expanding grants.
   Application exchanges associate requests and responses with their
   execution principals, authorization lineage, policy context,
   operation identifiers, and replay-protection state.  Protected
   resources retain final authority over their data and effects.

   This document identifies the interoperability problem, trust
   boundaries, security objectives, and unresolved architectural
   decisions.  It distinguishes requirements for future profiles from
   behavior described for the experimental review profile http6-rw-
   review-1.0.  It does not establish the necessity of a new transport,
   select a production cryptographic construction, or claim
   independently reproduced security or interoperability results.

   HTTP6 is a project designation, not an assigned HTTP version, ALPN
   identifier, URI scheme, or service port.
- **draft-shankarlingam-oauth-agent-dns-link-03** (new-draft, score 12, authorization) [none]: [Linking an Agent's DNS Name to its OAuth Client](https://datatracker.ietf.org/doc/draft-shankarlingam-oauth-agent-dns-link/) — Software agents increasingly call agents and services operated by
   other organizations.  A receiving organization often wants to know
   two things about any such caller: that it is the agent it claims to
   be, and that the organization operating it still authorizes it.  This
   document addresses the second question; the first is answered by the
   channel or by a sender-constrained token.  Existing approaches to the
   second question require a trust relationship between the two
   organizations' authorization servers.

   This document defines a DNS record by which the owner of a domain
   links an agent's DNS name to the OAuth client that the agent uses at
   the owner's own authorization server.  The sending agent presents a
   fresh access token for that client; the receiver verifies the token
   against the record and against the issuer's published keys.  No trust
   relationship, registration or federation between the two
   organizations is needed, and disabling the client at the sending
   organization's authorization server stops the agent being accepted,
   within a bounded time, by every receiver that follows this procedure.
- **draft-intra-handshake-fail-67** (new-draft, score 11, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100833, CVE-2026-100835,CVE-2026-108265, CVE-2026-108266, CVE-2026-108267, CVE-2026-108268, CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-108362, CVE-2026-33697, CVE-2026-108361 and others)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — As presented in [EarlyAttestationTschuess] (EAT), all major early
   attestation implementations have declared end of life of early
   attestation, because of our responsibly disclosed vulnerabilities.
   Privasys declared end of life (https://github.com/Privasys/go/
   commit/91195564d435a374e45d485d39edbc6cf8235901) of early attestation
   in *Go*, archived the early attestation repo on 04.09, and moved to
   standard (post-handshake) attestation.  Privasys declared end of life
   (https://github.com/Privasys/rustls/commit/
   c39f7107dffd710c5087b1885a71b4bb8ff2de31) of early attestation in
   *rustls*, archived the early attestation repo on 04.09, and moved to
   standard attestation.  Cocos AI declared end of life
   (https://github.com/ultravioletrs/cocos/releases/tag/v0.9.0) of early
   attestation, and moved to standard attestation.  CCC Attestation SIG
   declared end of life (https://github.com/CCC-Attestation/attested-
   tls-poc/pull/60) of early attestation, and archived the repo on
   22.07.  Moreover, authors of [I-D.fossati-tls-attestation-10] have
   withdrawn their vulnerable draft
   (https://mailarchive.ietf.org/arch/msg/
   i-d-announce/4QeQmyBwZpZ69MRry4wGzkGyU0o/) because of our discovered
   vulnerabilities.  Finally, [I-D.ritz-seat-facts] has been archived.
   This draft aims to provide technical details of these
   vulnerabilities.  Vulnerabilities include [CVE-2026-100833] of CVSS
   9.6, [CVE-2026-108265] of CVSS 9.1, [CVE-2026-108266] of CVSS 9.1,
   [CVE-2026-108267] of CVSS 9.1, [CVE-2026-108268] of CVSS 9.1,
   [CVE-2026-108269] of CVSS 9.1, [CVE-2026-100835] of CVSS 9.1,
   [CVE-2026-92701] of CVSS 9.1, [CVE-2026-92702] of CVSS 9.1,
   [CVE-2026-108362] of CVSS 9.1, [CVE-2026-119344] of CVSS 9.1,
   [CVE-2026-33697] of CVSS 7.5, [CVE-2026-108361] of CVSS 7.2,
   [CVE-2026-119345] of CVSS 7.2, and 26+ GitHub Security Advisories
   (GHSAs) against early attestation in the process of getting CVE IDs,
   which provide substantial technical evidence of how early
   attestation, such as [I-D.fossati-seat-early-attestation], fails in
   practice, even *without physical access* to the desired machine.
   Moreover, since continuous attestation is generally required
   [CSA-eBPF] [MITRE-Continuous-Attestation], early attestation adds
   *unnecessary complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA], [EarlyAttestationBleed],
   [EarlyAttestationTschuess] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility,
   extensibility, and review, and have been acknowledged by the relevant
   stakeholders.  Currently, there is *one CVE of CVSS 9.6, 13 CVEs of
   CVSS 9.1, one CVE of CVSS 8.2, one CVE of CVSS 7.5, two CVEs of CVSS
   7.2, two CVEs of 7.0, and 26+ GHSAs published awaiting CVE IDs
   against the broader early attestation covering all layers of the
   ecosystem up to the application*. The research papers on these are
   currently either under submission or being prepared for submission.
   The artifacts of these papers will be shared with the community under
   Apache-2.0 license for reproducibility, extensibility, and review.
   Based on our work, as noted above, all except two implementations of
   early attestation have been archived, withdrawn, or moved to post-
   handshake attestation.  In our analysis [Intra-handshake.fail-repo],
   [ID-Crisis-repo], and [EarlyAttestationTschuess] (EAT) and based on
   discussions in the CCC Attestation SIG, IETF SEAT WG, IRTF UFMRG,
   IRTF CFRG, and several other forums, the remaining two
   implementations of early attestation -- Edgeless Systems Contrast and
   Meta's AI following withdrawn [I-D.fossati-tls-attestation-10] --
   remain vulnerable due to lack of binding to the underlying
   connection.  We recommend users of these two implementations to
   carefully evaluate their systems and understand the risks.  If you
   are aware of any open-source implementation of early attestation that
   is not yet covered in this draft, please let us know to responsibly
   disclose the vulnerabilities to them.
- **draft-li-rttp-iqa-addressing-03** (new-draft, score 11, adjacent_watchlist) [none]: [The rttp and iqa URI Schemes: Derived-Address Intent and Attestation Addressing](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) — This document specifies two companion URI schemes built on one shared
   addressing model, in which the address of a subject is derived by
   computation from the authority and no lookup service, registry, or
   name-resolution system is consulted when the URI is used.  The "rttp"
   scheme names a claim of intent directed at an identified subject; the
   "iqa" scheme names the attestation standing of an identified subject,
   as reported by one of three named organs, and carries no proof and no
   credential.  The two are deliberately paired: intent addressing
   carries the claim, attestation carries whether the claimant is
   verified.

   Both schemes parse fail-closed, and the document states the
   requirements a client MUST satisfy when it handles such URIs, to
   avoid the failure modes that short, user-embeddable strings invite:
   using the authority as a navigation target (open redirect), using a
   registered handler as a general-purpose launcher, and, for "iqa", a
   parse that looks like a certification.

   The document specifies three components that companion
   implementations already run: a trust lease, which carries the
   freshness of every attestation answer in-band and is checked against
   the verifier's own clock, offline; two fixed-length wire formats, the
   128-octet pulse header of the "rttp" scheme and the 128-octet
   attestation envelope of the "iqa" scheme; and a closed refusal
   vocabulary with grant references for attestation responses.  This
   revision adds to these the rules that fix when the facts a
   verification consumes are evaluated — at the moment of use, not the
   moment of grant — and how any policy interpreter relates to the
   answer it consumes.  It further restricts the grammar so that no
   component begins with a hyphen, tightens the response semantics and
   the wire-format checks that the public conformance runs exercise,
   states what a response owes its reader when members are omitted or a
   refusal is recorded on a label, and adds a practice guide for testing
   an implementation against this text.

   This document is not an Internet Standard.  It is an Informational
   specification of two experimental addressing schemes, published for
   the public record.
- **draft-liu-iotops-pqc-dnp-sav5-02** (new-draft, score 11, core_identity) [none]: [Post-Quantum Authentication and Lifecycle Operations for IoT Deployments Using DNP3 SAv5](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-dnp-sav5/) — This document addresses post-quantum authentication migration for
   Internet of Things (IoT) deployments that already use DNP3 Secure
   Authentication version 5 (SAv5), including fleets of networked
   outstations and industrial gateways with limited local user
   interfaces.  It describes identity provisioning, admission to
   authenticated operation, credential and session replacement, failure
   recovery, quarantine, and retirement under an operator's existing
   authorization policy.

   A cryptographic profile supports these lifecycle operations using an
   ML-KEM-768 and ML-DSA exchange, HKDF-SHA-256 session keys, canonical
   DNP3 application protocol data unit (APDU) encoding, transport
   segmentation, and HMAC-SHA-256 application authentication.  The
   profile does not encrypt DNP3 payloads or replace application control
   authorization.

   This individual submission proposes Standards Track publication and
   requests IOTOPS review of its IoT operational requirements.  The
   appropriate venue for new protocol work requires separate
   determination.  DNP3 object variations and externally allocated
   algorithm identifiers require coordination with the responsible DNP3
   standards authority.  The local experimental selector is limited to
   explicitly configured laboratory use and is not an IEEE or IEC
   assignment.
- **draft-mcguinness-oauth-actor-profile-02** (new-draft, score 11, authorization) [none]: [OAuth Actor Profile for Delegation](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-actor-profile/) — This document defines a common representation of delegated actors in
   OAuth JSON Web Token (JWT) assertion grants, JWT access tokens, and
   Transaction Tokens.  It profiles the act claim defined by OAuth 2.0
   Token Exchange, requires issuer-scoped actor identifiers, and can
   carry the sub_profile claim to classify actor entity types.  It
   specifies token processing, delegation-chain propagation, sender-
   constraint handling, and discovery metadata, so that issuers and
   resource servers in different trust domains interpret delegated
   actors consistently.
- **draft-mih-agent-evidence-request-03** (new-draft, score 11, adjacent_watchlist) [none]: [An Interaction Model for Requesting Verifiable Evidence](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-request/) — Parties increasingly need to request verifiable evidence from a
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
- **draft-moore-scitt-ciris-ceg-04** (new-draft, score 11, trust_infrastructure) [none]: [Signed Attestation Rows of the CIRIS Epistemic Grammar and Their Relationship to SCITT](https://datatracker.ietf.org/doc/draft-moore-scitt-ciris-ceg/) — The CIRIS Epistemic Grammar (CEG) records claims between parties as
   signed rows.  Each row is one or more COSE_Sign1 messages over a
   payload in deterministically encoded CBOR.  Each message carries one
   composite ML-DSA-65 and Ed25519 signature.  Every row has one of five
   types: a claim, a delegation, a replacement, a withdrawal, or a
   recantation.  A node admits a row only after a fixed set of checks,
   and it refuses a failing row with a named reason.

   This document specifies the signed statement, its encoding, the names
   by which rows refer to each other, the signature, and the admission
   checks, so that a second implementation can produce and verify the
   same bytes.  It then describes how these statements relate to the
   roles of the SCITT architecture (RFC 9943), and where they differ.
   It defines no new SCITT mechanism and requests no IANA action.
- **draft-morrison-cross-handle-compute-lease-00** (new-draft, score 11, adjacent_watchlist) [none]: [Cross-Handle Compute Lease: Identity-Addressed Bounded Execution Over an Agent-Frame Substrate](https://datatracker.ietf.org/doc/draft-morrison-cross-handle-compute-lease/) — This memo specifies a Cross-Handle Compute Lease: a bounded,
   revocable, turn-metered primitive by which one identity-bound
   principal, addressed by a ~handle, asks for a defined task to run on
   the machine of a different principal, also addressed by a ~handle,
   over an existing agent-frame substrate.  The lease moves general
   computation between identities without opening an inbound network
   path on the host's machine and without exposing a network endpoint to
   the borrower; the address is the identity and the transport is the
   identity-event stream.  The memo specifies four frame kinds for the
   lease lifecycle, a four-rung trust ladder under which one envelope
   serves intra-organisational, cross-organisational, datacentre and
   open-market deployments, an isolation requirement that holds at every
   rung, an identity-inference exclusion invariant that prevents the
   leased computation from performing inference about the host, and a
   turn-metered settlement model in which the lease value passes between
   the two parties unsplit and the protocol operator holds no other
   party's funds.  Sessions between machines held by the same ~handle
   are outside the memo's scope.
- **draft-morrison-outcome-attestation-00** (new-draft, score 11, verifiable_claims) [none]: [Outcome Attestation Without Disclosure: Zero-Knowledge Proof That an Interaction Outcome Occurred Under Non-Disclosure of Method](https://datatracker.ietf.org/doc/draft-morrison-outcome-attestation/) — This memo specifies outcome attestation without disclosure.  One
   party, the prover, produces a verifiable attestation that a defined
   interaction outcome occurred against a consented target, and
   discloses neither the method that produced the outcome nor the input
   data the method consumed.  The attestation is a signed object
   carrying a zero-knowledge proof that an outcome predicate, defined by
   a referee, evaluated true over a private witness, together with the
   public statement the predicate was evaluated against.  A verifier
   learns that the outcome occurred.  It does not learn the technique,
   the payload, or any data category the prover was obliged to keep
   local.  The Compute-Location Gate draft states in its scope boundary
   that it gives no cryptographic proof that a data category was
   excluded from a derivation.  Where the prover committed to the
   derivation's input set before the derivation, this memo lets it show
   that a stated category is absent from that committed set.  The
   signature envelope is COSE or JOSE, and no new signature algorithm is
   introduced.  The subject of an attestation here is the outcome of an
   interaction, where remote attestation covers the state of a platform.
   No new transport is introduced.
- **draft-morrison-signed-policy-conferral-00** (new-draft, score 11, verifiable_claims) [none]: [Signed Policy Conferral and Population Distribution with an Exclusion Proof](https://datatracker.ietf.org/doc/draft-morrison-signed-policy-conferral/) — This memo specifies signed policy conferral, a way to distribute an
   enforceable defensive policy to a population of recipients.  A
   conferral envelope carries a policy artefact that a recipient
   applies, a signature block that needs a quorum of independent
   signers, an exclusion proof that the policy does not carry the
   sensitive method or data it was derived from, and a staged-rollout
   directive that confines the first distribution to a bounded cohort.
   The envelope travels as the payload of a conferral frame kind that
   this memo defines for the identity-keyed fan-out frame of the agent-
   channel fan-out memo, and its signers sign with COSE or JOSE.  It
   introduces no new transport and no new signature format.  The memo
   covers the many-recipient case that the briefing-and-binding envelope
   memo excludes from its scope.  It differs from the Common Security
   Advisory Framework, which standardises advisory documents for a
   recipient to read, by distributing a signed policy for a recipient to
   apply.
- **draft-dogru-cedulon-checkpoint-01** (new-draft, score 10, trust_infrastructure) [none]: [Cedulon Checkpoints: Epoch Witnesses and Transparency](https://datatracker.ietf.org/doc/draft-dogru-cedulon-checkpoint/) — This document specifies epoch checkpoints, the transparency witness
   and the anchoring of checkpoints as SCITT Signed Statements for the
   Cedulon audit layer.  The spend receipt, rail-extract reconciliation
   and trust-root rules live in the companion Cedulon Core document.  A
   verifier that pins a witness key and holds a usable issuer root can
   detect a withheld or rolled-back checkpoint from a body that answers
   to that root (MUST-T11-16); without those pins the suppression
   guarantee is conditional.
- **draft-han-a-sfc-architecture-problem-00** (new-draft, score 10, adjacent_watchlist) [none]: [Agent Service Function Chain (A-SFC): Architecture and Problem Statement](https://datatracker.ietf.org/doc/draft-han-a-sfc-architecture-problem/) — Large Language Model (LLM) agents granted write access to tools are
   emerging as a new class of network participants.  Their integrated
   nature of autonomous decision-making and execution introduces
   challenges such as compliance bypass and uncontrolled risks.
   Existing safeguards are mostly application-layer configurable
   policies residing in the same trust plane as the agent, and are
   vulnerable to software defects, unintended invocation paths, and
   bypass via direct connections.  Meanwhile, dynamic branching and
   cross-domain task interactions are pervasive in multi-agent
   collaboration scenarios.  Traditional networks only support flow-
   level quality awareness and cannot provide task-level end-to-end
   traceability, fault localization, and quality assurance.

   This document defines the A-SFC (Agent Service Function Chain)
   architecture, which elevates compliance from a "configurable policy"
   to a "topological fact".  Through SRv6 segment routing, mandatory
   ordered compliance steps are compiled into network forwarding paths;
   packets that skip compliance gates are dropped directly at the
   forwarding plane, without relying on cooperation from the agent side.
   On this basis, this document further introduces a task-level in-situ
   flow telemetry mechanism.  Through three-tier task encoding, it
   achieves layered quality awareness and fault localization at the link
   level, agent level, and task level, supporting end-to-end
   auditability and traceability of multi-agent delegation chains.  This
   document describes the core problems addressed by A-SFC, its overall
   architecture, key technical components, operating mechanisms, and
   typical application scenarios.
- **draft-morrison-cross-surface-canonical-knowledge-00** (new-draft, score 10, core_identity) [none]: [Cross-Surface Canonical Knowledge Integrity: Agent-Verifiable Anti-Cloaking Across Scale-Invariant Serving Surfaces](https://datatracker.ietf.org/doc/draft-morrison-cross-surface-canonical-knowledge/) — Knowledge artefacts such as documentation, policy specifications,
   configuration records and identity assertions are now served across
   two classes of surface at once.  One is rendered for people, such as
   an HTML document or a formatted record view.  The other is read by
   automated agents, such as a plain-text or JSON resource, a Model
   Context Protocol resource, a DNS record, a filesystem object, or a
   kernel-resident data structure.  Independent code paths usually
   produce the two, and no protocol mechanism lets an agent check that
   what it received on its surface matches what a person approved on the
   rendered surface.  Serving infrastructure can deliver different
   content to agents and to people, and neither consumer can detect that
   alone.  This is called cloaking.

   This memo specifies a content-integrity mechanism that applies
   unchanged at every scale.  A publisher emits a Canonical Integrity
   Record: a machine-readable digest of a canonical artefact, computed
   under a declared, versioned normalisation procedure and published at
   a well-known location specific to each surface class.  A consuming
   agent retrieves the artefact from each serving surface, recomputes
   the digest under the same normalisation, checks each result against
   the published record, and emits a structured anti-cloaking verdict.
   The mechanism reuses the HTTP digest fields of RFC 9530 and the well-
   known URI registry of RFC 8615 and extends them across surfaces and
   representations, including a kernel data-structure surface where
   there is no HTTP and no DNS and the check runs in kernel context.
- **draft-morrison-tiptop-disconnected-trust-01** (new-draft, score 10, adjacent_watchlist) [none]: [A Disconnected Trust Model for Networks Without Continuous Connectivity](https://datatracker.ietf.org/doc/draft-morrison-tiptop-disconnected-trust/) — The architecture document for IP in deep space says that security
   designs must tolerate long validation delays and potentially operate
   in a disconnected trust model, and it does not say what that model
   is.  This document defines it.  A disconnected trust model is one in
   which a node makes each trust decision from data it already holds or
   is handed with the request, each item verifiable without asking a
   third party, with a declared limit on how old each kind of held data
   may be.  The document then asks what a node may do alone when it
   cannot reach an authority, and lists the requirements any answer must
   meet.  It leaves short credential lifetime, as the answer to
   revocation without contact, with the documents that already give it.
   On the direction of failure, it adds that an authority check that
   cannot be evaluated fails closed on authority and never on safety.
   It also asks that a node's record of its decisions can outlive the
   node, and that any reason kept with the record be read only on a
   stated claim.  It specifies no protocol and no mechanism.
- **draft-rosario-http6-w1-profile-00** (new-draft, score 10, agent_identity) [none]: [HTTP6 W1 Binding for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-rosario-http6-w1-profile/) — An autonomous artificial intelligence agent can delegate work, call
   an external tool, and retry an operation after the person who
   authorized it has gone offline.  This document specifies W1, an HTTPS
   binding that lets the tool provider verify which agent is acting, the
   authority it inherited, and the resource effect requested.  Signed
   approval and delegation records carry the human's limits.  A time-
   bounded execution permit reserves a shared allowance.  The provider
   links its response to the request and supplies a receipt for the
   charge it committed.  A companion corpus supplies public test keys,
   exact signed messages, initial states, and expected observations for
   eleven cases.  Independent implementers can exchange these artifacts
   and compare what occurred at the resource.
- **draft-svensson-credential-oidc-bridge-03** (new-draft, score 10, verifiable_claims) [none]: [Credential Presentation to OIDC Claims Bridge](https://datatracker.ietf.org/doc/draft-svensson-credential-oidc-bridge/) — This document defines a mechanism for conveying digital credential
   claims via OpenID Connect (OIDC).  It specifies how an OpenID
   Provider (OP) that collects credentials from a wallet can expose
   those claims to Relying Parties as standard OIDC claims, enabling
   existing OIDC deployments to consume digital credentials without
   implementing any wallet-facing presentation protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/masv3971/rfc_credential_oidc_bridge.
- **draft-yetis-scitt-figure-receipts-00** (new-draft, score 10, trust_infrastructure) [none]: [Figure Statements: A SCITT Profile for Published Figures Given to AI Agents](https://datatracker.ietf.org/doc/draft-yetis-scitt-figure-receipts/) — Profiles of SCITT for AI agents record what an agent did: which tool
   it called, under whose authority, and what bytes came back.  They
   state, correctly, that they do not show whether those bytes were
   true.  This document profiles the layer underneath: a Signed
   Statement, issued by the publisher of a figure, that binds the figure
   to its source, period and population, and that is superseded when the
   publisher corrects the figure or when the original source prints a
   different value in a later edition.  It also defines a short token
   that travels with the figure through tool results and prose, so that
   a later reader can find the statement and learn whether the figure is
   still the one published.

   The profile makes a narrow claim.  It shows that a figure is the one
   a named publisher published, from a named source, and whether it has
   changed since.  It does not show that the figure is correct.
- **draft-dogru-cedulon-core-05** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-ietf-jose-pq-composite-sigs-07** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for Post-
   Quantum Traditional (PQ/T) hybrid composite signatures.  The
   composite algorithms described combine the Module-Lattice-Based
   Digital Signature Algorithm (ML-DSA) as the post-quantum component
   and either the Elliptic Curve Digital Signature Algorithm (ECDSA) or
   the Edwards-Curve Digital Signature Algorithm (EdDSA) as the
   traditional component.
- **draft-le-agent-passport-01** (new-draft, score 9, adjacent_watchlist) [none]: [Agent Passports and Delegation Receipts for Autonomous Software Agents](https://datatracker.ietf.org/doc/draft-le-agent-passport/) — Autonomous software agents call APIs, tools and other agents on
   behalf of people and organisations.  A party receiving such a call
   today can usually learn only that some bearer credential was
   presented.  It cannot learn which organisation is accountable for the
   agent, which model, configuration and tools the agent is running, on
   whose behalf it is acting, or whether any of that has changed since
   it was approved.

   This document defines two signed objects and how they travel on HTTP
   requests.  An Agent Passport binds an agent's public key to its
   accountable controller and to a digest of its build.  A Delegation
   Receipt records one step of authority passing from a principal,
   through a delegator, to an agent; a chain of receipts can only narrow
   that authority.  Requests carry both, and are signed with the agent's
   key using HTTP Message Signatures, so a relying party can check,
   without contacting the issuer per request, who the agent is, what it
   is running, on whose behalf it acts and what it may do.
- **draft-liu-iotops-pqc-wireguard-03** (new-draft, score 9, adjacent_watchlist) [none]: [Post-Quantum Key Provisioning and Lifecycle Operations for IoT Deployments Using WireGuard](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-wireguard/) — This document discusses post-quantum key provisioning and lifecycle
   operations for Internet of Things (IoT) deployments that already use
   WireGuard, such as fleets of industrial gateways and capable managed
   devices with little or no local user interface.  It addresses
   authorized tunnel onboarding, identity-to-key binding, preshared-key
   rotation, installation-state reconciliation, failure remediation,
   quarantine, and decommissioning at a scale that makes manual
   maintenance impractical.

   The operational model assumes independently provisioned trust and
   authorized management that remains reachable when the target tunnel
   fails.  It relates provisioning to inventory, separate access policy,
   observable readiness, and device lifecycle decisions.  It uses the
   existing WireGuard PresharedKey configuration interface and leaves
   the native handshake and transport format unchanged.  WireGuard
   remains an externally maintained dependency.

   An appendix retains a candidate ML-KEM-768 and ML-DSA bootstrap
   exchange for technical discussion and further security and
   interoperability review.  This individual contribution seeks
   Informational publication of the operational discussion and feedback
   on the appropriate venue for any new protocol work.
- **draft-sato-agent-accountability-refarch-02** (new-draft, score 9, adjacent_watchlist) [none]: [AI Audit Reference Architecture for Post-Hoc Agent Accountability](https://datatracker.ietf.org/doc/draft-sato-agent-accountability-refarch/) — This document defines a reference architecture for producing,
   protecting, and verifying post-hoc accountability records for the
   actions of autonomous and semi-autonomous software agents, built from
   evidence captured across an action's full lifecycle -- before,
   during, and after it executes -- but assessed after the fact.  It is
   scoped exclusively to post-hoc accountability, as distinct from real-
   time enforcement.  It is intended as one concrete, implementable
   instantiation: every building block it relies on is either a
   published specification used as specified or is specified in this
   document, so that it can be deployed now without waiting on related
   work still in progress, while remaining able to adopt that work as it
   stabilizes.  It defines seven ordered stages -- intent and mandate
   capture, the agent boundary, the record producer, the event log and
   its cryptographic anchoring, a composed trust fabric, the disclosed
   audit record, and third-party verification -- together with two
   branch conditions covering cross-principal transactions and external
   resource ingestion.  The records it defines exist to give the
   principal on whose behalf an agent acts, and the parties to a
   disputed action, verifiable evidence of what was done in the
   principal's name; they are not a means of monitoring the principal.
   Every flow of records between parties is bound to a signed, purpose-
   limited Use-Limitation Declaration.
- **draft-williams-oauth-poi-core-01** (new-draft, score 9, authorization) [none]: [Cryptographic Proof-of-Intent (PoI) Core Protocol for Human-in-the-Loop (HITL) Step-Up Authorization](https://datatracker.ietf.org/doc/draft-williams-oauth-poi-core/) — AI agents and workflow orchestrators call high-consequence APIs on
   behalf of people.  Bearer tokens and transport-level proof-of-
   possession show which client made a call.  They do not show that a
   person approved the specific parameters of that call, and redirect-
   based step-up is too slow for frequent approvals.

   This document specifies the Proof-of-Intent (PoI) Core protocol.  A
   Resource Server signs a challenge that binds the exact canonical
   parameters (RFC 8785) to human-readable facts.  The person's client
   answers with a signed decision (APPROVE, REJECT, or SUPERCEDE with
   new parameters) using a session key certified by the Authorization
   Server (RFC 7800) or a WebAuthn or PSEA authenticator.  The Resource
   Server verifies the evidence without a call to the Authorization
   Server, admits each approval once, and issues a signed receipt.

   Multi-approver chains, escalation, and concurrency are specified in
   draft-williams-oauth-poi-chained-state-00.
- **draft-yd-nw-rats-endorsements-00** (new-draft, score 9, trust_infrastructure) [none]: [A CoRIM Profile for Arm's Normal World Attestation Endorsements](https://datatracker.ietf.org/doc/draft-yd-nw-rats-endorsements/) — Arm Normal World Attestation Endorsements comprise reference values
   and cryptographic key material that a Verifier needs to appraise
   Attestation Evidence produced from Normal World client running on an
   Arm Platform.

   This memo defines Normal World Endorsements as a profile of the CoRIM
   data model.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/arm-attestation-drafts/draft-nw-rats-endorsements.
- **draft-elkins-plants-enterprise-mtc-deployment-02** (new-draft, score 8, core_identity) [none]: [Enterprise Deployment Considerations for Post-Quantum TLS Server Authentication in the Public Web PKI](https://datatracker.ietf.org/doc/draft-elkins-plants-enterprise-mtc-deployment/) — The migration of TLS server authentication to post-quantum mechanisms
   in the public Web PKI must fit the scale and complexity of enterprise
   certificate management and TLS termination.  Public-facing services
   may support tens of millions of customers using unmanaged browsers,
   mobile applications, and other TLS clients, while authentication
   infrastructure is distributed across business units, hosting
   providers, cloud platforms, and CDNs.  Deployment readiness therefore
   depends on cryptographic and protocol support as well as the ability
   to introduce new authentication mechanisms without disrupting
   customer access.

   This document examines enterprise deployment considerations for
   standalone Merkle Tree Certificates (MTCs) and conventional
   standalone ML-DSA certificates on public websites accessed by
   unmanaged clients.  It addresses certificate issuance, provisioning,
   renewal, revocation, trust-anchor signaling, credential selection,
   and interoperability across browsers, certificate-management systems,
   and TLS termination platforms.

   Drawing on initial browser and TLS client observations, the document
   identifies deployment dependencies, proposes interoperability
   questions for implementers, and discusses migration priorities and
   operational readiness.  It does not define new certificate formats or
   TLS mechanisms, assume that either certificate approach is easier to
   deploy, or commit the authors to independently testing supplier
   implementations.
- **draft-gilda-audit-restoration-evidence-01** (new-draft, score 8, authorization) [none]: [Restoration Evidence Records for AI Agent Incident Response](https://datatracker.ietf.org/doc/draft-gilda-audit-restoration-evidence/) — When an AI agent system is stopped, restricted or has its credentials
   revoked during an incident, someone later decides whether it may run
   again.  Incident response guidance asks for that decision to be
   documented with the risk that remains, but no format says what the
   record must contain for a party outside the deploying organization to
   check it.  This document defines five record types for that purpose:
   an incident action authorization, a revocation sweep, a re-enable
   decision, a joint authority assignment for incidents that span
   organizations, and a revocation boundary report.  Each is an in-toto
   Statement carried in a DSSE envelope, uses the canonical form of the
   agent audit record, and is checked by ordered rules with a named
   reason for each failure.  A bundle rule set binds a re-enable
   decision to the records it cites, by digest.  A published conformance
   corpus carries a reject member for every rule that a member can
   force.
- **draft-gruszka-evaluation-receipt-mappings-05** (new-draft, score 8, trust_infrastructure) [none]: [Citing Signed Evaluation Receipts from Existing Envelopes](https://datatracker.ietf.org/doc/draft-gruszka-evaluation-receipt-mappings/) — A Signed Evaluation Receipt records one evaluation result as signed
   payload bytes B.  This document describes how existing envelopes cite
   such a receipt by the SHA-256 digest of B, and how a DSSE envelope
   carries B with the receipt's own signature.  It fixes those bytes and
   a matching rule, maps the parts of a receipt onto DSSE, the in-toto
   Statement with the test-result predicate and the SLSA Verification
   Summary Attestation, shows that the signature of a receipt is already
   a valid DSSE signature, gives a SCITT Signed Statement that names a
   receipt only by its digest, in a key profile and a certificate
   profile, declares the receipt digest as an artifact type for typed
   digest references, states how three formats for records of agent
   actions can cite a receipt, and relates a receipt to a pre-run
   criteria set written in PRML.  It defines no new format and no new
   predicate.
- **draft-gu-nmrg-intent-translator-07** (new-draft, score 8, agent_identity) [none]: [An Intent Translator for Hallucination Mitigation in an Agentic AI Framework](https://datatracker.ietf.org/doc/draft-gu-nmrg-intent-translator/) — This document proposes an Intent Translator to mitigate hallucination
   in the intent translation in an Agentic AI Framework.  This Intent
   Translator has an agentic AI workflow for detecting and mitigating
   structural and semantic errors, including hallucinated policy
   content, when translating a natural-language network intent into a
   structured policy.  The workflow coordinates role-specialized
   language-model functions with deterministic validation tools within a
   predefined action space and a bounded retry budget.  Schema-
   constrained generation limits structural defects, while cross-slot
   checks and intent-faithfulness assessment identify a potentially
   unsupported or inconsistent policy content.  Structured validation
   traces guide targeted re-extraction and regeneration.  Unresolved
   cases retain explicit failure status for downstream review.  This
   document describes component interactions in the Intent Translator,
   validation outcomes, and recovery behavior.  It also presents a 3GPP
   TS 28.312-based instantiation for mobile network management.
- **draft-ietf-acme-dns-account-label-05** (new-draft, score 8, authorization) [acme]: [Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge](https://datatracker.ietf.org/doc/draft-ietf-acme-dns-account-label/) — This document outlines a new DNS-based challenge type for the ACME
   protocol that enables multiple independent systems to authorize a
   single domain name concurrently.  By adding a unique label to the DNS
   validation record name, the dns-account-01 challenge avoids CNAME
   delegation conflicts inherent to the dns-01 challenge type.  This is
   particularly valuable for multi-region or multi-cloud deployments
   that wish to rely upon DNS-based domain control validation and need
   to independently obtain certificates for the same domain.
- **draft-ietf-lamps-csr-attestation-34** (new-draft, score 8, trust_infrastructure) [lamps]: [Use of Remote Attestation with Certificate Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) — Certification Authorities (CAs) issuing certificates to Public Key
   Infrastructure (PKI) end entities may require a certificate signing
   request (CSR) to include additional verifiable information to confirm
   policy compliance.  For example, a CA may require an end entity to
   demonstrate that the private key corresponding to a CSR's public key
   is secured by a hardware security module (HSM), is not exportable,
   etc.  The process of generating, transmitting, and verifying
   additional information required by the CA is called remote
   attestation.  While various aspects of remote attestation have been
   standardized, a variety of proprietary mechanisms are in use,
   particularly regarding protection of private keys.

   This specification defines ASN.1 structures which may carry
   attestation data for PKCS#10 and Certificate Request Message Format
   (CRMF) messages.  Both standardized and proprietary attestation
   formats are supported by this specification.
- **draft-ietf-scitt-receipts-mmr-profile-00** (new-draft, score 8, verifiable_claims) [scitt]: [COSE Receipts for MMRs](https://datatracker.ietf.org/doc/draft-ietf-scitt-receipts-mmr-profile/) — This document defines a new verifiable data structure type for COSE
   Receipts [RFC9942] specifically for use with ledgers based on post-
   order traversal binary Merkle trees and which are designed for high
   throughput, ease of replication and compatibility with commodity
   cloud storage.

   Post-order traversal binary Merkle trees, also known as history
   trees, are more commonly known as Merkle Mountain Ranges.
- **draft-jeong-nmrg-agentic-ai-framework-02** (new-draft, score 8, agent_identity) [none]: [An Agentic AI Framework for the Management of Networks, Security, and AI Services](https://datatracker.ietf.org/doc/draft-jeong-nmrg-agentic-ai-framework/) — This document specifies an agentic AI framework for the management of
   networks, security, and AI services.  This framework is an Intent-
   Based System (IBS) to enforce a human-language intent at a target
   network with the translated policy for networks, security, or AI
   services.  It consists of a User System, a Cloud System, an Edge
   System, and a Device.  Target devices in this framework include
   Network Forwarding Elements (e.g., router and switch), Network
   Security Functions (e.g., firewall, web filter, and DDoS-attack
   mitigator), Internet-of-Things (IoT) Devices, Physical AI Robots,
   Software-Defined Vehicles (SDV), Unmanned Aerial Vehicles (UAV), and
   Urban Air Mobility (UAM).  This document describes the agentic AI
   framework with its components and interfaces where the components
   include AI agents and supporting knowledge repositories (i.e.,
   knowledge base), and also inter-agent interfaces use the Agent-to-
   Agent (A2A) protocol.
- **draft-kamimura-rats-behavioral-evidence-03** (new-draft, score 8, trust_infrastructure) [none]: [On the Relationship Between Remote Attestation and Behavioral Evidence Recording](https://datatracker.ietf.org/doc/draft-kamimura-rats-behavioral-evidence/) — This document provides an informational discussion of the conceptual
   relationship between remote attestation, as defined in RFC 9334 (RATS
   Architecture), and behavioral evidence recording mechanisms.  It
   observes that these two verification capabilities address
   fundamentally different questions - attestation addresses "Is this
   system in a trustworthy state?" while behavioral evidence addresses
   "What did the system actually do?" - and discusses how they could
   conceptually complement each other in accountability frameworks.
   This document is purely descriptive: it does not propose any
   modifications to RATS architecture, define new mechanisms or
   protocols, or establish normative requirements.  It explicitly does
   not define any cryptographic binding between attestation and
   behavioral evidence.
- **draft-liu-iotops-pqc-uasc-02** (new-draft, score 8, core_identity) [none]: [Post-Quantum SecureChannel Profiles and Lifecycle Operations for IoT Deployments Using OPC UA](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-uasc/) — This document addresses post-quantum SecureChannel migration for
   Internet of Things (IoT) deployments that already use OPC Unified
   Architecture (OPC UA), including fleets of capable controllers and
   industrial gateways with limited local user interfaces.  It describes
   authorized application onboarding, credential and policy
   provisioning, bounded key use, renewal, failure recovery, quarantine,
   and retirement under existing device and application authorization.

   A cryptographic protection profile for OPC UA Secure Conversation
   (UASC) over opc.tcp uses ML-KEM-768, ML-DSA, HKDF-SHA-256, and AES-
   256-GCM.  It specifies profile identifiers, nonce encoding, key
   derivation, authenticated encryption, identity binding, sequence and
   SecurityToken processing, per-key usage limits, and conformance
   requirements supporting those operations.

   This individual submission proposes Standards Track publication and
   requests IOTOPS review of its IoT operational requirements.  The
   appropriate venue for new protocol work requires separate
   determination.  Permanent OPC UA SecurityPolicy and algorithm
   identifiers require coordination with the OPC Foundation; the private
   identifiers remain provisional and do not establish OPC Foundation
   conformance.
- **draft-mih-agent-settlement-records-01** (new-draft, score 8, core_identity) [none]: [Two-Party Settlement Records for Agent Payments](https://datatracker.ietf.org/doc/draft-mih-agent-settlement-records/) — A payment between two agents is observed by two systems: the payer's
   wallet or bank and the payee's.  Existing payment protocols record
   one of those observations, signed by one party, and most record
   nothing about what was delivered in exchange.  This document defines
   two-party settlement records, carried as Agent Action Capsules, in
   which payer and payee each seal, under their own key, only what their
   own system observed.  A settlement is a set of up to four leg records
   (terms, payer-observed, payee-observed, and delivered) that cite each
   other by digest and join on a typed payment reference.  The state of
   a settlement (one-sided, agreed, or mismatched) is derived by the
   verifier from which legs are present and whether they agree; no
   record asserts it.  Signed objects from existing payment protocols
   are carried by digest and never re-signed.  Amounts are exact
   integers with a decimal scale.  The document defines a registry of
   payment reference types covering x402, Lightning, AP2, ACP, UCP, the
   Payment HTTP authentication scheme, ISO 20022, and Open Payments, and
   maps its states to ISO 20022 status codes.
- **draft-moore-scitt-ciris-trace-00** (new-draft, score 8, agent_identity) [none]: [Signed Reasoning Traces of CIRIS Agents](https://datatracker.ietf.org/doc/draft-moore-scitt-ciris-trace/) — An AI agent that acts on a person's behalf reaches each action
   through a sequence of steps: it gathers context, runs several
   evaluations, selects an action, submits the selection to checks that
   can veto it, and then acts.  Most of those steps are calls to
   language models.

   This document specifies the CIRIS reasoning trace: one signed record
   per unit of agent work (a thought), sealed when the action is taken.
   The trace lists every step and every model call in the order the
   recording component received them, with scores, outcomes, sizes,
   costs and durations, and, at higher disclosure levels, reasoning text
   and the prompts and completions themselves.  It specifies three
   disclosure levels, the exact bytes the agent's Ed25519 signature
   covers, how a trace is carried as a row of the CIRIS Epistemic
   Grammar (CEG), when a trace exists at all, and the checks a consumer
   runs before relying on one.  It records where the published
   specification and the shipping implementation disagree.
- **draft-morrison-agent-channel-fan-out-05** (new-draft, score 8, core_identity) [none]: [An Agent-Channel Frame for Identity-Keyed Fan-Out Delivery to Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-agent-channel-fan-out/) — This memo specifies a message envelope, a recipient-scope grammar and
   a subscribe-filter grammar for delivering short structured messages
   to the concurrent sessions of one identity.  A sender names a set of
   recipients by identity shape, such as all sessions of one handle or
   all sessions whose instrument identifier has a given prefix, and a
   delivery server expands that set against live subscriptions at
   delivery time.  Frames are emitted over a per-handle Server-Sent
   Events stream.  The envelope carries a kind discriminator whose set
   of values is open.  The memo defines three kinds, and other documents
   may define more.  The memo specifies the wire elements only; frame
   retention is out of scope.
- **draft-morrison-compute-location-gate-07** (new-draft, score 8, core_identity) [none]: [The Compute-Location Gate: A Pre-Inference Exchange for Choosing Where an Identity Inference Computes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — A service that derives statements about a person from signals the
   person emits can compute them on its own servers or on the person's
   device.  Today that choice is internal to each service, and a client
   has no common way to ask where an inference will run before it runs.
   This memo specifies a pre-inference exchange.  The client asserts a
   provenance class for the input signal, one of active, passive
   aggregate, or passive individual.  A fixed routing function maps the
   class to a compute location, server-side or device-local.  The
   service replies that the request is accepted, refused, or redirected,
   and a refusal carries a typed reason, including that the person has
   not consented to that class.  The memo specifies no proof that the
   service computed where it says it did.  The only implementation is
   the author's own, and it does not yet run the exchange with a client.
   The memo is Informational.
- **draft-morrison-did-alter-method-02** (new-draft, score 8, core_identity) [none]: [The did:alter Decentralized Identifier Method](https://datatracker.ietf.org/doc/draft-morrison-did-alter-method/) — This document specifies two things two independent implementations
   would have to agree on.  The first is the spelling of a Decentralized
   Identifier that names a ~handle together with the DNS zone that
   publishes the handle's signed envelope.  The second is the DID
   document a resolver derives from that envelope, once the envelope has
   passed DNSSEC validation and signature verification under the
   companion specification for discovering Model Context Protocol
   servers through DNS TXT records.  The method defines no record,
   cryptographic primitive or registry of its own.  Resolution requires
   DNSSEC.  The method is usable only for signed zones.  The envelope
   record carries no key history, and revocation cannot presently be
   observed from DNS alone, and the document says what a resolver can
   and cannot conclude as a result.  No deployment exists.  The document
   is Informational and is offered for review as an Independent
   Submission.
- **draft-morrison-live-reference-resolution-04** (new-draft, score 8, core_identity) [none]: [Live Reference Resolution: A Result Shape for Reads of an Authority by an Autonomous Agent](https://datatracker.ietf.org/doc/draft-morrison-live-reference-resolution/) — An agent that answers from a cached or derived copy of a value, when
   the system that owns the value has since changed, gives a wrong
   answer with no sign that it is wrong.  This document describes the
   result an agent returns when it reads a value from its authority.
   Another component can rely on it.  The result carries the value, the
   identifier of the authority that answered, a freshness indicator and
   a provenance type, bound together so that the value cannot be
   obtained without them.  It also describes the behaviour around that
   result: resolving at the point of use, treating an unobservable or
   stale authority as an explicit uncertainty state, and refusing or
   escalating a costly act that depends on an uncertain value.  The
   document is Informational.  It defines no wire protocol, it has one
   in-house implementation of part of the result and no other, and it is
   offered for review as an Independent Submission.
- **draft-morrison-org-alter-policy-provision-07** (new-draft, score 8, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — An agent runtime that acts under an organisation's rules receives
   those rules in a form specific to each deployment, and the audit
   records it sends back are specific to each deployment too.  This memo
   specifies two elements that two implementations would have to agree
   on.  The first is an enforcement-gate specification, a list of rules,
   each with a trigger predicate over a tool invocation's name and
   arguments, an action (block, prompt for confirmation, or allow with
   audit), an applicability scope and an explanation, with the most
   restrictive action prevailing when several rules match.  The second
   is an audit-signal record that the runtime submits to an append-only
   ingestion endpoint.  Both are exposed as typed Model Context Protocol
   surfaces of an organisational identity substrate.  The runtime
   resolves the substrate at session start from a manifest source.  A
   principal bound to more than one substrate operates under the
   strictest applicable gate, and no substrate learns of another.  The
   memo is Informational.  The only implementation is the author's own
   substrate, and no agent runtime yet fetches policy this way.
- **draft-morrison-substrate-wake-00** (new-draft, score 8, core_identity) [none]: [Substrate Wake: Armed-Wait Liveness Without Addressability](https://datatracker.ietf.org/doc/draft-morrison-substrate-wake/) — This memo specifies the armed wait, a way for a turn-based agent
   session to be re-entered by an incoming message without becoming a
   network-addressable endpoint and without polling any remote party.
   At the end of a turn a session suspends onto a substrate its own host
   already maintains: a local projection of the frames delivered to its
   principal's identity handle.  An observer on the same host watches
   that projection and re-enters the session the moment a frame of a
   wake class arrives, or when a bounded window closes.  The session
   holds no socket, publishes no address and carries no session
   identifier on any wire.  The memo defines the wake class, the arm and
   wake procedure, the three outcomes of an arm, the delivery and
   ordering properties a woken session can rely on, and the failure
   behaviour.  It builds on the agent-channel frame of draft-morrison-
   agent-channel-fan-out and the coordination posture of draft-morrison-
   substrate-observation.  Under the agent-channel memo's rule for new
   kinds, it defines the four frame kinds it relies on that the agent-
   channel memo does not define.  Liveness obtained this way is an
   optimisation over asynchronous delivery and never replaces it.
- **draft-zly-aibsn-agent-status-02** (new-draft, score 8, core_identity) [none]: [The AIBSN Registry: Public Status Records for AI Agents](https://datatracker.ietf.org/doc/draft-zly-aibsn-agent-status/) — AIBSN is a public registry of AI agents that we have run since
   September 2025.  Each agent gets a permanent code, and anyone can
   look up whether that code is active or revoked, for free and without
   an account.  This document describes the record, what its status
   means and how the lookup works today.  It also lists what we offer
   organizations as custom work on top of the registry, such as their
   own registry instance, change notifications, emergency revocation and
   transfer of a record to a new owner.  Finally it puts forward some
   proposals for discussion: a public revocation time, a standing for
   the party behind an agent that is separate from the agent's own
   status, a stated maximum delay for every way a record can be
   withdrawn, revocation by the owner, a log of status changes, a way to
   check status without telling the registry which record you are
   checking, a key that lets other identifier records point to an
   independent status source, and how a relying party can treat and
   record a status that is out of date.
- **draft-ahn-nmrg-5g-security-i2nsf-framework-06** (new-draft, score 7, agent_identity) [none]: [An Agentic AI Security Framework for Security Management in Mobile Networks](https://datatracker.ietf.org/doc/draft-ahn-nmrg-5g-security-i2nsf-framework/) — This document proposes an Agentic AI Security Framework for security
   management in mobile networks.  A Security Application Function (SAF)
   Agent translates a network administrator's security intent to hold a
   security objective into a high-level security policy.  A Security
   Control Function (SCF) Agent receives the high-level security policy
   and translates it into a low-level security policy that will be
   enforced by distributed Network Security Functions (NSFs) in mobile
   networks.  The SCF Agent sends the low-level security policy to an
   appropriate NSF.  Policy generation, monitoring, and continuity
   across a data path are integrated into a closed-loop control with an
   Observe-Reason-Act-Verify process.  The proposed framework can be
   applied to enterprise, campus, cloud, and edge networks along with
   existing network-management mechanisms.  Thus, this document
   describes an architecture of the Agentic AI Security Framework, a
   policy-continuity example, standard integration points, and security
   considerations in this framework.
- **draft-ahuja-agent-routing-policy-04** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.
- **draft-barrett-dnsop-domain-set-01** (new-draft, score 7, trust_infrastructure) [none]: [The Domain Set Discovery Protocol (domain-set)](https://datatracker.ietf.org/doc/draft-barrett-dnsop-domain-set/) — Organizations commonly operate under multiple domain names: a primary
   website, legacy names, defensive registrations, divisional brands,
   and names in restricted or verified top-level domains.  No standard
   mechanism exists for a domain owner to declare, in a machine-readable
   and verifiable way, which domains are operated by the same
   organization.  This document defines "domain-set", a protocol by
   which domain operators publish membership in a set of domains using a
   DNS TXT record as the discovery mechanism.  The record either lists
   the members directly or references an extensible Domain Set Manifest
   retrieved over HTTPS.  Mutual attestation is the validation
   requirement: a link between two domains is valid only when both
   domains independently publish records naming each other.  Every
   direction of a link MUST be retrieved over an authenticated channel,
   by DNSSEC or by the Web PKI, and consumers report which was used.
   The protocol enables security tooling, mail and browser systems, and
   other automated consumers, including AI systems, to answer the
   question "are these two domains operated by the same organization?"
   from first-party, owner-published data rather than inference.
- **draft-chen-emu-teap-notification-action-00** (new-draft, score 7, core_identity) [none]: [Protected User Notification Extension for Tunnel Extensible Authentication Protocol (TEAP)](https://datatracker.ietf.org/doc/draft-chen-emu-teap-notification-action/) — When IEEE 802.1X network access is denied or restricted, clients
   usually show only a generic message such as "Authentication Failed",
   even when the authentication server knows the specific reason.
   Existing mechanisms either do not reach the client (RADIUS Reply-
   Message), are not protected (EAP Notification), or are not designed
   for presentation to users (the TEAP Error TLV and inner method error
   messages).

   This document defines an optional extension to Tunnel Extensible
   Authentication Protocol (TEAP) Version 1 (RFC 9930) that allows the
   EAP server to send a notification to the user inside the TEAP TLS
   tunnel.  The peer advertises the reason codes it supports and the
   user's preferred languages in a Notification Capabilities TLV.  The
   server sends a reason code, a recommended action, and optional text
   and remediation URI in a User-Notification TLV.  The peer can
   acknowledge it with a Notification-Acknowledgement TLV.  The
   extension only provides information and does not change
   authentication results, authorization decisions, or key derivation.
- **draft-gruszka-signed-evaluation-receipts-05** (new-draft, score 7, trust_infrastructure) [none]: [Signed Evaluation Receipts](https://datatracker.ietf.org/doc/draft-gruszka-signed-evaluation-receipts/) — This document defines a Signed Evaluation Receipt: one JSON object
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
- **draft-jones-scitt-dual-receipt-02** (new-draft, score 7, core_identity) [none]: [A Dual-Receipt Profile for Binding a Decision Statement to an Independent Policy Evaluation Statement](https://datatracker.ietf.org/doc/draft-jones-scitt-dual-receipt/) — This document specifies a dual-receipt profile for recording one
   disbursement decision as two signed statements, made by two different
   parties and registered with the same Transparency Service.  An
   approver acting for a fiscal sponsor signs a Decision Statement.  A
   validator acting for a receiving institution signs a Policy
   Evaluation Statement that binds to the Decision Statement's
   identifier, receipt, and signature, and records the outcome of a
   named policy.  The profile defines the JSON members of both
   statements, a canonical encoding based on the JSON Canonicalization
   Scheme, SHA-256 statement identifiers, a composite identifier, Merkle
   tree receipts that use the hashing rules of RFC 9162, and a
   verification procedure.  It also states the limits of the evidence: a
   bundle of statements cannot show that no conflicting evaluation
   exists, and the times inside the statements are claims made by their
   signers.
- **draft-morrison-reviewed-by-trailer-06** (new-draft, score 7, core_identity) [none]: [Reviewed-By Trailer: Sovereign-Portable Peer-Review Attribution for Content-Hash-Bound Artefacts](https://datatracker.ietf.org/doc/draft-morrison-reviewed-by-trailer/) — This document defines a trailer grammar for sovereign-portable peer
   review as an extension of the identity-attributed commit grammar of
   draft-morrison-identity-attributed-commits.  The grammar introduces
   one required trailer (Reviewed-By:) and three optional companion
   trailers (Review-Stance:, Review-Of:, Witnessed-By:) that bind a
   Sovereign-tier ~handle to a specific act of review over a specific
   content artefact, cryptographically signed using the Ed25519
   mechanism of that grammar.  Because the signature covers the
   reviewer's role, the stance and the review target together, changing
   any of them after signing fails verification.  The mechanism applies
   to git commits, document manifests, pre-prints, patent disclosures,
   and any other content-addressable artefact.  A reviewer's signed
   reviews are bound to the reviewer's sovereign handle and can be
   verified without the publisher.  For anonymous peer review, the
   reviewer signs under a Sovereign handle whose underlying party is
   concealed through out-of-band key custody; the review act stays
   verifiable and the reviewer's identity is not disclosed.  The grammar
   can be used together with CRediT, ORCID and DOI attribution.

## Monitor

- **draft-creviston-racr-00** (new-draft, score 6, authorization) [none]: [RACR Protocol: Recipient-Authorized Content Retrieval](https://datatracker.ietf.org/doc/draft-creviston-racr/) — RACR (Recipient-Authorized Content Retrieval, pronounced "racer") is
   a federated protocol for exchanging recipient-authorized messages
   between portable identities.  Stable decentralized identifiers let
   participants operate independently of their current hosting
   providers.  RACR uses deterministic Concise Binary Object
   Representation (CBOR) and CBOR Object Signing and Encryption (COSE)
   for signed authorization records and message envelopes.  A recipient
   provider validates authorization before retrieving a detached,
   digest-bound body from the sender provider.  This document specifies
   the protocol architecture, grant-authorized delivery, and privacy
   boundaries.
- **draft-huang-aeq-driven-token-transport-00** (new-draft, score 6, agent_identity) [none]: [AEQ-Driven Semantic Transport Control for Real-Time Video Agents](https://datatracker.ietf.org/doc/draft-huang-aeq-driven-token-transport/) — This document describes an Agentic Experience Quality (AEQ)-driven
   semantic transport control framework for real-time video agents using
   visual tokens.  The framework assesses the semantic utility of each
   visual token by jointly considering its spatial salience and temporal
   novelty.  The AEQ model combines cumulative semantic utility with a
   normalized transmission-delay cost.  Frame-level selection plans the
   initial token set, while packet-level control continuously adjusts
   the number of tokens to transmit to maximize predicted AEQ under
   current network conditions.  This document specifies requirements for
   semantic assessment, transmission modeling, two-level control, and
   transport feedback.
- **draft-ietf-cose-pqc-kem-01** (new-draft, score 6, verifiable_claims) [cose]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-pqc-kem/) — This document describes conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and
   Encryption (COSE).
- **draft-morrison-alter-uri-scheme-07** (new-draft, score 6, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
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
- **draft-morrison-identity-pronouns-06** (new-draft, score 6, core_identity) [none]: [Identity Pronouns: A Client-Side Shorthand for ~handle References and the Rule That Keeps It Off the Wire](https://datatracker.ietf.org/doc/draft-morrison-identity-pronouns/) — A client that lets a person type a short reference such as ~org in
   place of a concrete ~handle has to replace the reference before
   anything is sent.  This document states the one rule a receiver can
   check, that a typed handle field in a payload crossing a trust
   boundary never carries such a reference, and describes the client-
   side resolution that makes the rule hold.  A reference of this kind
   is called a pronoun.  The document defines one pronoun, ~org.  It
   resolves to the organisation bound to the caller's current session.
   Resolution is local to the client and uses no network exchange.  The
   document is Informational.  It describes a convention that no second
   party implements, and it makes no claim that the convention needs
   standardising.
- **draft-morrison-identity-streams-01** (new-draft, score 6, core_identity) [none]: [Identity Streams: Per-Trait Source Attribution for Inferred and Stated Identity Claims](https://datatracker.ietf.org/doc/draft-morrison-identity-streams/) — When one system tells another about a trait it has inferred about a
   person, the receiver today learns the trait and a confidence, and
   nothing about what the inference was drawn from.  Because the
   receiver cannot tell a trait the person stated in answer to a
   question from one read off the person's activity on a linked
   platform, it cannot apply the lawful basis, consent and context
   limits that belong to each.  This document defines a source tag
   carried with every inferred trait on the wire.  The tag names, for
   each stream that contributed to the trait, a registered stream class,
   the provenance class of the observation, where the inference was
   computed, the lawful basis and purposes the stream was consented for,
   and the contexts the trait may be used in.  It reuses the provenance-
   class vocabulary of the Morning Brief specification, establishes a
   registry of stream classes, and states the rules a receiver follows,
   including refusing a trait whose sources it cannot check.  The same
   tag carries facts the person states about themselves, such as when
   they are available or the terms on which they offer something, and
   those facts keep the limits of the stream they were given on.  It
   defines a wire field only.  How traits are inferred, stored or scored
   is out of scope.
- **draft-morrison-org-alter-threshold-signing-00** (new-draft, score 6, core_identity) [none]: [Threshold Signing for Organisational Identities](https://datatracker.ietf.org/doc/draft-morrison-org-alter-threshold-signing/) — This memo profiles the two-round threshold Schnorr signature scheme
   of RFC 9591 for the custody of the signing key of an organisational
   identity.  No single member or device of the organisation ever holds
   that key, and a quorum of the organisation's authorised members signs
   on its behalf.  The profile requires the FROST(Ed25519, SHA-512)
   ciphersuite.  Because that ciphersuite produces ordinary Ed25519
   signatures, a key held this way is published, rotated and verified
   exactly as the DNS-based discovery memo "Discovery of Model Context
   Protocol Servers via DNS TXT Records" already specifies, and no
   verifier needs to change.  The memo specifies a distributed key-
   generation ceremony in which the whole key never exists in one place,
   the record of who may sign and how many must agree, the request and
   assembly of a signature, a signed custody statement by which a
   verifier learns that a published key is held under a threshold, and
   the handling of member removal, share refresh and loss.  The memo is
   Informational.
- **draft-morrison-substrate-observation-05** (new-draft, score 6, core_identity) [none]: [Substrate-Observation as an Alternative to Envelope Coordination for Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-substrate-observation/) — This memo describes a coordination-protocol anti-pattern observed in
   cross-tool agentic systems and a substrate-observation alternative
   that does not require negotiating a wire format between heterogeneous
   concurrent sessions of an identity-bound principal.  The memo is
   Informational and proposes no protocol element for standardisation.
   It sets out what should not be standardised for this problem, and
   why, and identifies the existing substrate mechanisms that serve in
   its place.  Companion memos describe the identity primitives this
   memo presumes.  This memo is not offered for working-group adoption.
   It is addressed to those designing coordination for agentic sessions.
- **draft-morrison-venue-log-00** (new-draft, score 6, trust_infrastructure) [none]: [Signed Posts in a Public Venue Log for Lists Written by People and Their Agents](https://datatracker.ietf.org/doc/draft-morrison-venue-log/) — A mailing list joins five things through email: moving messages, the
   archive, who a message is for, who owes a reply, and who wrote it.
   This document moves the archive, authorship and addressing onto a
   public append-only log called a venue.  Each post is a signed record.
   A post an agent wrote names the agent, the person it acts for, and
   how much that person reviewed it.  The venue appends each post to its
   log and returns a receipt, and anyone can check a post against the
   venue's published root without asking the venue.  Positions and
   consensus calls are typed records in the same log.  A gateway carries
   posts out as email and brings email in as posts marked as arriving by
   email.  The log builds on the transparency service and receipts of
   the IETF supply chain integrity work, and on the ~handle tiers and
   the alter URI scheme.
- **draft-zhang-dawn-agent-discovery-framework-10** (new-draft, score 6, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — This document describes a two-layer reference architecture for
   discovering the Minimum Discoverable Information (MDI) for AI agents.
   The Local Discovery Plane collects agent information through mDNS on
   each participating LAN and infrastructure-assisted registration, and
   the Federation Gateway combines these sources into a policy-
   controlled view of the administrative domain.  For cross-domain
   discovery, the Federation Plane uses DNS publication of policy-
   approved information in authoritative DNS zones and on-demand
   resolution as its baseline; Federation Gateways apply export policy
   and validate and cache accepted results.  The document also
   identifies optional functions that may complement this baseline where
   DNS publication and request-driven resolution do not meet deployment
   needs: recipient-specific sharing, proactive or multi-hop
   dissemination, and trusted aggregated directory queries.  In mixed-
   mode deployments, DNS may bootstrap an endpoint that provides one of
   these additional functions.
- **draft-decisium-authorization-disposition-00** (new-draft, score 5, authorization) [none]: [An Authorization Disposition Object for Agent Decision Receipts](https://datatracker.ietf.org/doc/draft-decisium-authorization-disposition/) — A verification check that has completed and a human authorization
   that is still outstanding can coexist for the same proposed action.
   Receipt formats that carry only a claim-state enumeration cannot
   express the second condition, because it is not a statement about the
   claim: it is a statement about what must happen before the action.

   This document specifies an authorization disposition, a sibling
   object carried alongside check results, and the processing rules by
   which a consumer derives a fail-closed decision about whether an
   action may be initiated.  The disposition carries a named holder, two
   distinct deadlines, an action-instance binding, and a detached signed
   decision.

   The document treats receipt integrity, the decision recorded at
   issuance, and present actionability as separate questions.  It
   distinguishes insufficient evidence from conflicting evidence,
   prohibits treating an unevaluated authorization requirement as "not
   required", and specifies requirements for historical verification,
   replay prevention, and tenant-scoped instance ownership.  It records
   what the object establishes and, equally, what it does not.
- **draft-ek-dtn-ipn-arpa-03** (new-draft, score 5, core_identity) [none]: [The ipn.arpa Zone and IPN DNS Operations](https://datatracker.ietf.org/doc/draft-ek-dtn-ipn-arpa/) — This document requests the creation of ipn.arpa, an infrastructure
   DNS namespace for the Bundle Protocol (BP).  It maps a Fully
   Qualified Node Number to the DNS base name N.A.ipn.arpa., where N is
   the Node Number and A is the Allocator Identifier.  A BP Agent can
   use that name to discover a convergence-layer endpoint at the
   destination or at a relay.  This document specifies an SRV binding
   for version 4 of the TCP Convergence-Layer Protocol (TCPCLv4).
- **draft-ietf-spice-oidc-cwt-07** (new-draft, score 5, adjacent_watchlist) [spice]: [OpenID Connect Standard Claims Registration for CBOR Web Tokens](https://datatracker.ietf.org/doc/draft-ietf-spice-oidc-cwt/) — This document registers OpenID Connect standard claims already used
   in JSON Web Tokens for use in CBOR Web Tokens.
- **draft-irtf-nmrg-ai-challenges-07** (new-draft, score 5, ai_infrastructure) [nmrg]: [Research Challenges in Coupling Artificial Intelligence and Network Management](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ai-challenges/) — This document is intended to introduce the challenges to overcome
   when Network Management (NM) problems may require coupling with
   Artificial Intelligence (AI) solutions.  On the one hand, many
   difficult NM problems still lack good solutions, or existing
   approaches come with significant limitations.  Artificial
   Intelligence may help produce novel solutions to those problems.  On
   the other hand, due to the high computational costs of AI solutions
   and stringent data privacy constraints, the distributed execution of
   AI workloads has become paramount.  Consequently, networks must be
   operated efficiently to sustain these distributed processing
   requirements.

   To identify the right set of challenges, the document defines a
   method based on the evolution and nature of NM problems.  This will
   be done in parallel with advances and the nature of existing
   solutions in AI in order to highlight where AI and NM have already
   been coupled together or could benefit from a closer integration.
   So, the method aims at evaluating the gap between NM problems and AI
   solutions.  Challenges are derived accordingly, assuming that solving
   these challenges will help to reduce the gap between NM and AI.

   This document is a product of the Network Management Research Group
   (NMRG) of the Internet Research Task Force (IRTF).  This document
   reflects the consensus of the research group.  It is not a candidate
   for any level of Internet Standard and is published for informational
   purposes.
- **draft-miao-agw-cross-domain-scenario-analysis-01** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Gateway Scenario Analysis and Functional Requirements for Cross-Domain Multi-Agent Communication](https://datatracker.ietf.org/doc/draft-miao-agw-cross-domain-scenario-analysis/) — This document analyzes the communication gaps in three representative
   multi-agent scenarios: single-domain single-agent, single-domain
   multi-agent, and cross-domain multi-agent.  For each scenario, it
   examines whether an Agent Gateway is needed, what capabilities it
   should provide, and where it should be deployed.  Based on the
   consolidated gap analysis, this document derives a set of universal
   functional requirements for the Agent Gateway as a standardized
   cross-domain trust boundary and protocol termination layer.  The
   findings aim to guide the design of interoperable agent communication
   infrastructure.
- **draft-morrison-mcp-tool-surface-names-registry-04** (new-draft, score 5, adjacent_watchlist) [none]: [An IANA Registry for Model Context Protocol Tool Surface Names](https://datatracker.ietf.org/doc/draft-morrison-mcp-tool-surface-names-registry/) — Two Model Context Protocol (MCP) servers can offer a tool under the
   same name with different argument schemas, and a client has no
   machine-readable signal that the two are not the same capability.
   This document describes a possible registry of tool surface names,
   the wire-level identifiers by which a client invokes a typed
   capability on an MCP server.  It sets out the per-entry fields, a
   name grammar and a Specification Required registration procedure with
   a Designated Expert.  The document is Informational.  It has one
   prospective registrant, the author, and the MCP specification is
   maintained by another body.  It therefore makes no request of IANA at
   this revision, and the registry would be requested only if the
   specification's maintainers or an operator other than the author
   wanted it.
- **draft-qiu-ntpv5-root-time-source-alignment-00** (new-draft, score 5, trust_infrastructure) [none]: [Root Time Source Alignment Signature and Transport Protocol for NTPv5](https://datatracker.ietf.org/doc/draft-qiu-ntpv5-root-time-source-alignment/) — This document defines an NTPv5 extension that turns a time value's
   provenance from a _claim_ into _evidence_. A pre-trusted Root Time
   Source attests that a given time service instance's clock has been
   checked for alignment against a physical source; that instance then
   signs the time value itself.  A client holding only the root public
   key verifies both signatures offline, so it can tell a time value
   that carries verifiable provenance apart from one that merely claims
   it.

   The extension deliberately does one thing and no more: it proves
   _where a signed time value came from_. It does not adjust clocks, it
   does not rate sources, and it has no revocation -- a signed proof is
   unilateral, it exists once signed.  It is opt-in, uses two extension
   fields, and touches nothing in the core protocol.
- **draft-ramadan-moq-fec-multicast-01** (new-draft, score 5, core_identity) [none]: [Forward Error Correction for Multicast Delivery of Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-multicast/) — This document specifies how the Forward Error Correction (FEC)
   mechanism for Media over QUIC (MoQ) is used when protected tracks are
   delivered over multicast.  It defines repair-only multicast endpoints
   and how a receiver adds and drops the repair layers they carry,
   states which tracks a multicast endpoint carries in this revision,
   specifies how a receiver treats blocks and symbols that a multicast
   content-authentication profile has not admitted, and specifies the
   receiver repair policy of a multicast or AMT leg: in-band FEC first,
   then per-block unicast repair for the blocks that FEC did not
   recover, with a budget and priorities derived from the catalog.  It
   is independent of how multicast is carried, whether by Source-
   Specific Multicast and Automatic Multicast Tunneling or by a
   multicast QUIC channel.
- **draft-strebulaev-bridge-contract-00** (new-draft, score 5, core_identity) [none]: [Bridge Contract for Agent Session Governance](https://datatracker.ietf.org/doc/draft-strebulaev-bridge-contract/) — Existing agent protocols define identity headers, audit records and
   session resumption, but none defines what an intermediate bridge MUST
   do when the client is detached and the agent keeps executing, or when
   the human in the loop is unavailable.  This document defines the
   Bridge Contract: a Session Identity Descriptor, Mandatory Governance
   Events, a Resume Record that the bridge keeps for itself, and
   Conformance Criteria.  Re-attach is a challenge-response in which the
   client proves possession of a registered key over a single-use nonce
   and the last event it saw.  The event log is hash-chained.  The
   contract complements, and does not replace, the protocols it composes
   with.  The evidence for the specification is in a companion preprint;
   it comes from one author's implementations and is not independent
   confirmation.
- **draft-tayyebi-fcl-dcop-gtl-01** (new-draft, score 5, ai_infrastructure) [none]: [A Fabric Coordination Layer (FCL) for High-Scale AI Training: Distributed Credit-Orbit Pacing (DCOP) and Global Token Ledger (GTL)](https://datatracker.ietf.org/doc/draft-tayyebi-fcl-dcop-gtl/) — This document describes a Fabric Coordination Layer (FCL) for high-
   scale distributed artificial intelligence (AI) training fabrics.  FCL
   coordinates transmission authority using a Global Token Ledger (GTL)
   and applies that authority through Distributed Credit-Orbit Pacing
   (DCOP).  The architecture relates workload communication intent to
   available fabric capacity before traffic is injected.

   The design objectives are to mitigate synchronized incast, reduce
   queue pressure and tail-latency variability, and improve collective
   communication efficiency.  These objectives require experimental
   validation.  This revision clarifies the architectural scope and
   physical constraints of FCL; it does not define an interoperable
   protocol or a production hardware implementation.
- **draft-wang-rtgwg-stateless-compute-power-00** (new-draft, score 5, core_identity) [none]: [Research on Computing Power Network Technology for Stateless Computing Services](https://datatracker.ietf.org/doc/draft-wang-rtgwg-stateless-compute-power/) — Stateless computing services represent a principal design paradigm in
   distributed computing, characterized by statelessness, dynamism,
   service orientation, and atomicity.  These services have been widely
   adopted in cloud computing and microservice architectures.  With the
   rise of AI technologies and the emergence of Model-as-a-Service
   (MaaS), they are being introduced into intelligent computing,
   reshaping industrial divisions of labor and gradually evolving into a
   typical computing power provisioning paradigm following IaaS/PaaS.
   However, current computing power networks were found to primarily
   focus on resource-layer scheduling optimization, leading to critical
   challenges when addressing computing-network collaboration and
   routing/scheduling requirements for stateless services.  These
   included the disconnection between computing resource scheduling and
   user application-layer functional demands, as well as protocol stack
   mismatches between network-layer connectivity solutions and
   service-oriented API interconnection requirements.  The need for
   elastic network pipelines in computing service interconnection was
   analyzed, followed by the proposal of a novel computing power network
   architecture natively supporting stateless service routing and
   scheduling.  Key components including the identifier scheme, system
   architecture, and operational mechanisms were detailed through
   simulation validation.  URL-PATH is employed as computing power
   identifiers, enabling service-oriented API-level resource
   orchestration and differentiated QoS guarantees through service
   semantic routing.  This approach provides new insights for evolving
   computing power networks from "resource provisioning" to "service
   interconnection."
- **draft-wright-verdict-record-03** (new-draft, score 5, trust_infrastructure) [none]: [Verdict Records: Results on Claims that Cite Receipts as Evidence](https://datatracker.ietf.org/doc/draft-wright-verdict-record/) — This document defines a verdict record: a statement, bound to its
   issuer, of a result reached on a claim, together with the evidence
   the result relies on and the rule by which the result can be re-
   derived.  Evidence is cited by digest and can be a receipt or record
   in any format, such as a SCITT Receipt or an Agent Action Capsule.
   The document defines how a checker checks a verdict record and what
   such a check does and does not show.  It defines no receipt format
   and changes none.
- **draft-zeng-osap-consent-receipts-00** (new-draft, score 5, authorization) [none]: [Consent Receipt Binding for Task-Scoped Authorization](https://datatracker.ietf.org/doc/draft-zeng-osap-consent-receipts/) — This document defines a signed consent receipt for task-scoped
   authorization between local agents.  A receipt records a user's
   decision to allow or deny a described action, binds that decision to
   a task, an agent, an audience, an action set, and a resource set, and
   can be verified offline.  The document also defines the consent
   request, the reservation ordering that avoids a circular dependency
   between a receipt and a capability token, the audit events that
   accompany consent and side effects, and an informative mapping to
   ISO/IEC 27560.  It does not define a user interface, a transport, or
   a capability token format.
- **draft-zeng-osap-capability-tokens-00** (new-draft, score 4, adjacent_watchlist) [none]: [Capability Tokens for Local Agent Delegation](https://datatracker.ietf.org/doc/draft-zeng-osap-capability-tokens/) — This document defines a signed capability token format for delegating
   authority between agents on a single local system.  A token binds a
   subject, an audience, a task, a set of actions and resources, and a
   validity window.  Tokens can only be attenuated: a child token is a
   subset of its parent.  The document specifies attenuation rules,
   binding checks, revocation semantics, and the interaction with
   consent receipts.  It does not define a transport, a discovery
   protocol, or an agent runtime.

## Adjacent / watchlist

- **draft-altanai-moq-relay-diagnostics-00** (new-draft, score 3, authorization) [none]: [Client-Visible Relay Diagnostics for Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-altanai-moq-relay-diagnostics/) — Media over QUIC Transport (MOQT) deployments typically place one or
   more relays between publishers and subscribers.  When delivery
   stalls, degrades, or fails, a client observes only its own leg of the
   path, and often cannot determine whether the cause lies with the
   original publisher, an intermediate relay, path conditions,
   authorization policy, or its own behavior.

   This document collects use cases and requirements for exposing a
   limited, relay-controlled set of diagnostic information to authorized
   MOQT clients.  It examines three candidate mechanisms: an explicit
   request and response exchange on the control path, diagnostic
   information carried in existing responses and error codes, and
   advertisement of diagnostic capability during session establishment.
   Because such information can reveal deployment topology, operational
   state, or the activity of other users, authorization, data
   minimization, and relay discretion over what is disclosed are treated
   as first-order requirements rather than later refinements.

   Related operator examples describe capacity and incident observations
   within a separately authorized administrative scope.  They motivate
   correlation with existing metrics and logging systems without
   defining a relay management API.

   The goal is diagnostics that are actionable at runtime and
   interoperable across implementations, not a general-purpose telemetry
   channel within MOQT.  Information intended primarily for offline
   analysis remains the province of logging and observability systems
   such as qlog.  This document defines the problem space and the design
   constraints; a concrete wire format is left to a follow-on document
   once the working group has settled on an approach.
- **draft-barcelo-opsawg-cert-observation-00** (new-draft, score 3, adjacent_watchlist) [none]: [An Information Model and JSON Encoding for Certificate Observation Records](https://datatracker.ietf.org/doc/draft-barcelo-opsawg-cert-observation/) — Operators need to know which X.509 certificates are installed where,
   when they expire, and whether a renewed certificate has actually
   reached the service that uses it.  This information is produced by
   many different parties: network observers, local agents,
   configuration management systems, and certificate issuers.  Each
   currently uses its own format, and many endpoints cannot be reached
   by a central monitoring system at all.

   This document defines the Certificate Observation Record: a
   transport-independent information model describing one certificate as
   seen at one location by one reporter, together with a JSON encoding,
   an HTTP-based exchange mechanism, and a file-based handoff.  The
   record distinguishes the reporter from the subject it describes, so
   that one system can report on behalf of endpoints that a collector
   cannot reach, and it labels each record with the kind of evidence it
   carries, so that a collector can detect when issuance, deployment and
   actual service diverge.
- **draft-bonica-tcpm-extended-options-06** (new-draft, score 3, core_identity) [none]: [An Upgraded TCP Session Type](https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/) — Currently, TCP maintains ordinary sessions (SES-O) in which ordinary
   segments (SEG-O) are exchanged.  Each SEG-O can accommodate up to 40
   octets of options.

   In the future, applications may require more than 40 octets of
   options.  For example, an application may use a 36-byte TCP
   Authentication Option (TCP-AO), leaving insufficient space for other
   required options.

   Therefore, this document describes an experiment in which upgraded
   sessions (SES-U) and upgraded segments (SEG-U) are introduced.  Each
   SEG-U can accommodate up to 1,016 octets of Individual Options.
- **draft-bonica-tcpm-tcp-ao-long-algs-08** (new-draft, score 3, core_identity) [none]: [Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/) — RFC5926 creates a registry of cryptographic algorithms that can be
   used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256 and
   KMAC256.

   The MAC algorithms described by this document produce 256-bit (i.e.,
   32-byte) MACs.  When 32-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 36 of the 40 bytes available for TCP options.
- **draft-claise-green-capability-discovery-05** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
   capabilities model of RFC 9196 to allow a network element to
   advertise, per hardware Component, the set of Power States that the
   Component supports, together with a static characterization of each
   such state: the expected and maximum Power the Component draws in it,
   and the time to enter and exit it, as well as the range of Power Cap
   limits the Component accepts.

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
- **draft-davidben-lamps-turducken-certs-01** (new-draft, score 3, core_identity) [none]: [Embedded Alternate Issuer Certificates](https://datatracker.ietf.org/doc/draft-davidben-lamps-turducken-certs/) — This document defines a mechanism to embed one or more alternate
   certificates within a single outer certificate.  The outer
   certificate remains parseable to a legacy relying party that is
   unaware of this specification.  Each alternate certificate certifies
   the same subject information, but with a different issuer.  This can
   be used to help TLS on the Web transition securely to post-quantum
   authentication, as well as other PKI transitions with similar
   constraints.
- **draft-degennaro-jmap-mail-rules-00** (new-draft, score 3, adjacent_watchlist) [none]: [JMAP Mail Rules](https://datatracker.ietf.org/doc/draft-degennaro-jmap-mail-rules/) — This document specifies a data model for managing server-side mail
   filtering rules with the JSON Meta Application Protocol (JMAP).  A
   rule combines a set of conditions, such as the sender address or the
   message subject, with a set of actions, such as filing the message
   into a mailbox or forwarding it.  The model is designed to be
   presented and edited through simple user interface components, and
   every condition and action is defined in terms of an equivalent
   construct of the Sieve mail filtering language, so that rules have
   precise and interoperable semantics and servers that implement Sieve
   can support this extension by translating rules into Sieve scripts.

   This document also defines lists of safe and blocked senders and
   describes how rules interact with the JMAP VacationResponse object.
- **draft-dsmullen-ppd-taxonomy-06** (new-draft, score 3, adjacent_watchlist) [iotops]: [Privacy Preference Declaration Taxonomy](https://datatracker.ietf.org/doc/draft-dsmullen-ppd-taxonomy/) — This document defines the core vocabulary, comparison model, and
   extension discipline used by Privacy Preference Declarations (PPDs)
   to express atomic privacy-relevant dataflows in home networks.  It
   complements the companion PPD architecture and protocol work by
   standardizing the core fields used in participant declarations and
   household policy rules.  The core vocabulary is the mandatory shared
   semantic floor for baseline participant-facing interoperability.
   Richer ecosystem-specific vocabularies remain possible, but
   comparison-relevant non-core terms need explicit relationships to the
   shared core so they remain computable.  Baseline participant-facing
   protocol messages use compact identifiers plus taxonomy context
   rather than requiring full ontology exchange on the wire.
- **draft-dulaunoy-mispql-00** (new-draft, score 3, adjacent_watchlist) [none]: [MispQL: A Query Language for Cyber Threat Intelligence](https://datatracker.ietf.org/doc/draft-dulaunoy-mispql/) — MispQL is a read-only, SQL-like query language for cyber threat
   intelligence (CTI).  This document specifies its text syntax using
   Augmented Backus-Naur Form (ABNF), its query semantics, and a JSON
   representation for its Boolean filters.  A CTI platform can implement
   MispQL over its own data model by describing the tables, fields,
   types, and operators it supports.  A transport binding describes how
   the Python MispQL client uses the complex-search interface in MISP
   3.0.
- **draft-gage-quic-pathmgmt-07** (new-draft, score 3, core_identity) [none]: [QUIC Path Management for Multi-Path Configurations](https://datatracker.ietf.org/doc/draft-gage-quic-pathmgmt/) — This document defines path management procedures for QUIC that
   operate independently of the connection management procedures defined
   in RFC9000.  The path management procedures enable a multipath
   configuration between endpoints by allowing QUIC packets associated
   with any connection identifier to be transported over any of the
   paths established between the endpoints.  As a consequence, the
   principles and operations of RFC9000 are retained regardless of the
   path used to a convey QUIC packet.
- **draft-hillier-chorale-protocol-01** (new-draft, score 3, core_identity) [none]: [The Chorale Protocol: Interception-Resistant Packet Transmission with Topology-as-Secret Ordering, Cascade-Integrity Witnessing, Polyglot Cover Packets, Per-Packet Time-Lock Sealing, and Multi-Jurisdiction Substrate Diversity](https://datatracker.ietf.org/doc/draft-hillier-chorale-protocol/) — This document specifies the Chorale Protocol, a secure packet
   transmission system with active integrity assurance for settings that
   require resistance to interception, traffic analysis, replay,
   tampering and retrospective decryption by adversaries with quantum
   capability.  Sessions are keyed by a hybrid handoff that combines
   ECDH with ML-KEM-1024 under an HKDF-SHA-512 combiner, binds the
   selected suite into a short authentication string, and is verified in
   the Tamarin prover.  Chorale defines three confidentiality regimes,
   computational, everlasting and information-theoretic, and states the
   keying conditions under which each applies.  Every session reports
   the regime its keying supports, and a conforming implementation
   refuses to transmit a message whose required regime exceeds the
   achievable one.  The protocol composes a per-session secret graph
   topology that orders packets without transmitting ordering
   information, cascade-integrity witnessing over the hidden topology,
   cover packets carrying valid-looking witnesses for fictional
   sessions, per-packet time-lock sealing over an RSA-group VDF or a
   post-quantum sequential hash chain, multi-source physical-entropy pad
   composition with sovereign jurisdictional separation, multi-substrate
   flight with threshold reconstruction, hash-family negotiation across
   SHA-256, SHA-512 and SHA3-512, and a tombstone ledger that makes pad
   reuse structurally impossible at the receiver.  The protocol serves
   intelligence agencies, central banks, treaty-bound corridors,
   regulator-to-regulator communications and other settings that require
   the strongest confidentiality and integrity properties currently
   attainable.
- **draft-horse-sidrops-rfc3779bis-01** (new-draft, score 3, authorization) [none]: [X.509 Extensions for IP Addresses and AS Identifiers](https://datatracker.ietf.org/doc/draft-horse-sidrops-rfc3779bis/) — This document defines two X.509 v3 certificate extensions.  The first
   binds a list of IP address blocks, or prefixes, to the subject of a
   certificate.  The second binds a list of autonomous system
   identifiers to the subject of a certificate.  These extensions may be
   used to convey the authorization of the subject to use the IP
   addresses and autonomous system identifiers contained in the
   extensions.  This document obsoletes RFC 3779.
- **draft-ietf-calext-jscalendarbis-24** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.  It reserves
   the Task object type for future work.
- **draft-ietf-cose-c509-test-vectors-05** (new-draft, score 3, adjacent_watchlist) [cose]: [Test Vectors for CBOR-Encoded X.509 (C509) Certificates](https://datatracker.ietf.org/doc/draft-ietf-cose-c509-test-vectors/) — This document contains examples of CBOR-encoded X.509 (C509)
   certificates, certification requests, and certification request
   templates.
- **draft-ietf-httpapi-idempotency-key-header-09** (new-draft, score 3, adjacent_watchlist) [httpapi]: [The Idempotency-Key HTTP Header Field](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — The HTTP Idempotency-Key request header field can be used to make
   non-idempotent HTTP methods such as POST or PATCH fault-tolerant.
- **draft-ietf-httpapi-ratelimit-headers-12** (new-draft, score 3, adjacent_watchlist) [httpapi]: [RateLimit header fields for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) — This document defines the RateLimit-Policy and RateLimit HTTP header
   fields for servers to advertise their quota policies and the current
   service limits, thereby allowing clients to shape their requests to
   avoid exceeding server-imposed limits.  It also defines problem types
   that servers can use to inform clients about quota-related
   conditions.
- **draft-ietf-httpbis-resumable-upload-16** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
- **draft-ietf-jmap-calendars-35** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-mailmaint-imap-objectid-bis-09** (new-draft, score 3, core_identity) [mailmaint]: [IMAP Extension for Object Identifiers](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-imap-objectid-bis/) — This document defines the OBJECTID+ extension for IMAP, which
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
- **draft-ietf-pce-stateful-pce-autobw-update-08** (new-draft, score 3, adjacent_watchlist) [pce]: [Update to the Automatic Bandwidth Adjustment Procedure for MPLS-TE and SR-TE LSPs with a Stateful PCE](https://datatracker.ietf.org/doc/draft-ietf-pce-stateful-pce-autobw-update/) — Extensions for the stateful PCE model enable control of Traffic
   Engineering (TE) LSPs using the Path Computation Element
   Communication Protocol (PCEP) for RSVP-TE and Segment Routing (SR),
   for both PCE-initiated and PCC-initiated LSPs.

   RFC 8733 defines PCEP extensions for automatically adjusting
   bandwidth on MPLS-TE Label Switched Paths (LSPs) using a stateful
   PCE.  This document applies the PCEP extensions for automatic
   bandwidth adjustment to SR-TE LSPs in both the MPLS (SR-MPLS) and
   IPv6 (SRv6) data planes.  It also extends the RFC 8733 automatic
   bandwidth adjustment procedure to multipath LSPs using the PCEP
   extensions defined in RFC 10066.  This document updates RFC 10066 to
   signal per-path Requested Bandwidth in multipath PCRpt, PCUpd, and
   PCInitiate messages.

   RFC 8733 defines the AUTO-BANDWIDTH-ATTRIBUTES TLV and a set of sub-
   TLVs for the attributes.  A sub-TLV is included when its value
   differs from the value last sent in a PCEP message.  However, RFC
   8733 lacks a mechanism to explicitly remove an attribute identified
   by a sub-TLV.  This document updates RFC 8733 by defining such a
   mechanism.
- **draft-ietf-pim-evpn-multicast-yang-09** (new-draft, score 3, adjacent_watchlist) [pim]: [Yang Data Model for EVPN multicast](https://datatracker.ietf.org/doc/draft-ietf-pim-evpn-multicast-yang/) — This document describes a YANG data model for EVPN multicast services.
The model is agnostic of the underlay as well as RFC 9251. This
document mainly focuses on EVPN instance framework.
- **draft-ietf-ppm-dap-attribution-00** (new-draft, score 3, adjacent_watchlist) [ppm]: [Distributed Aggregation Protocol (DAP) Extensions for the Attribution API](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap-attribution/) — This defines extensions to the DAP protocol that support the
   Attribution API.  These extensions provide support for
   differentially-private aggregation and the operating modes that the
   Attribution API depends on.
- **draft-ietf-sidrops-moa-profile-05** (new-draft, score 3, authorization) [sidrops]: [A Profile for Mapping Origin Authorizations (MOAs)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-moa-profile/) — This document proposes a new approach by leveraging Resource Public
   Key Infrastructure (RPKI) architecture to verify the authenticity of
   the mapping origin of an IPv4 address block.  MOA is a newly defined
   cryptographically signed object that provides a means for the address
   holder to authorize an IPv6 mapping prefix to originate mapping for
   one or more IPv4 prefixes.  When receiving the MOA objects from the
   relying parties, PE devices can verify and discard invalid address
   mapping announcements from unauthorized IPv6 mapping prefixes to
   prevent IPv4 prefix hijacking.
- **draft-ietf-tcpm-tcp-ao-algs-10** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC 5926 established a registry of cryptographic algorithms that can
   be used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-johnson-mda1-protocol-00** (new-draft, score 3, core_identity) [none]: [Flat Data Artifact Format, Version 1 (MDA/1) Protocol](https://datatracker.ietf.org/doc/draft-johnson-mda1-protocol/) — This document specifies the Flat Data Artifact Format Version 1
   (MDA/1), a fixed-layout, zero-copy binary container for exchanging
   and storing signed data artifacts in resource-constrained,
   intermittently connected, and offline environments.  MDA/1 artifacts
   have one canonical encoding and a stable content identifier, can be
   parsed without dynamic memory allocation, and are validated by a
   strictly ordered pipeline whose limits are enforced from a 64-byte
   header.  Every byte except the signature values is covered by
   Ed25519, ML-DSA-44, or hybrid signatures, and signers are bound to
   the principals they speak for.  The document also defines VB01, a
   key-committing, length-bucketed AEAD frame for payloads at rest, and
   an HPKE profile, including the X-Wing post-quantum KEM, for
   delivering frame keys.  MDA/1 is intended as a compact edge transport
   and storage envelope alongside HL7 FHIR.
- **draft-jones-mims-reproducible-draft-review-01** (new-draft, score 3, trust_infrastructure) [none]: [A Method for Reproducible Review of Internet-Draft Test Cases](https://datatracker.ietf.org/doc/draft-jones-mims-reproducible-draft-review/) — This document describes MiMS, a method for an author and independent
   reviewers to identify an exact Internet-Draft revision, reproduce a
   bounded technical proposition, and trace a finding to a subsequent
   edit and replay.  It distinguishes evidence of package delivery,
   evidence of independent computation, and evidence of editorial
   disposition.  A SCITT-related example demonstrates the scope of a
   reproducible finding.  The method is usable with existing transports
   and independently chosen verification tools.
- **draft-kosuru-nmop-incident-diagnosis-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Network Incident Diagnostic Assessments](https://datatracker.ietf.org/doc/draft-kosuru-nmop-incident-diagnosis-yang/) — This document defines a YANG data model for diagnosis-specific
   assessment records associated with network incidents.  The model
   augments the network incident model with a history of diagnostic
   assessments that relate evidence to probable-cause hypotheses, record
   inconclusive or blocked diagnostic outcomes, and capture post-
   remediation verification observations.

   The model complements rather than replaces generic task interfaces.
   Generic task lifecycle, planning, confirmation, execution, and task-
   notification mechanisms are not redefined.
- **draft-kwiatkowski-lake-mtc-00** (new-draft, score 3, authorization) [none]: [Merkle Tree Certificates for LAKE](https://datatracker.ietf.org/doc/draft-kwiatkowski-lake-mtc/) — Merkle Tree Certificates (MTC) replace the signature of a
   Certification Authority (CA) with smaller inclusion proof against a
   periodically published landmark.  The large sizes of post-quantum
   (PQC) keys and signatures make conventional certificate chains costly
   to validate on constrained devices, which have limited memory,
   compute, and message-size budgets.  MTC's lightweight properties keep
   certificate verification practical for such devices even when PQC
   signature algorithms are used.

   This document specifies how to carry MTC credentials in the
   Lightweight Authenticated Key Exchange (LAKE) protocol [RFC9528]:
   CBOR encodings of MTC certificates and landmarks, and a new External
   Authorization Data (EAD) item that lets the two peers negotiate, per
   message, between the compact landmark-relative form of a certificate
   and its self-contained standalone form.
- **draft-lin-idr-bgp-flowspec-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Model for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-flowspec-yang/) — This document defines a YANG data model for the BGP Flow
   Specification (Flowspec) address families.  The model augments the
   BGP YANG model to add all Flow Specification address families,
   including Flowspec-specific configuration, the Flow Specification
   RIB, and per-neighbor Adj-RIBs, and defines notifications for the
   prefix limit exceeded and route state change events.
- **draft-makarov-gostjwa-03** (new-draft, score 3, verifiable_claims) [none]: [Using GOST Cryptographic Algorithms for JWT security](https://datatracker.ietf.org/doc/draft-makarov-gostjwa/) — This specification registers cryptographic algorithms and identifiers
   for GOST R 34.10 digital signatures and public keys, GOST R 34.11
   hash functions, GOST 34.12 encryption algorithms to be used with JSON
   Web Signatures (JWS), JSON Web Encryption (JWE), and JSON Web Keys
   (JWK) specifications.
- **draft-mih-sokolov-cose-deterministic-encodings-04** (new-draft, score 3, verifiable_claims) [none]: [Deterministic Encodings for COSE](https://datatracker.ietf.org/doc/draft-mih-sokolov-cose-deterministic-encodings/) — A COSE Hash Envelope signs the digest of a preimage, not the preimage
   itself.  A verifier that holds the content as a decoded value, such
   as a CBOR data item, rather than the bytes that were hashed has to
   encode the value again, and nothing in the Hash Envelope says how the
   producer encoded it.  CBOR permits more than one encoding of the same
   data item, so a digest mismatch cannot tell a modified value from a
   value encoded another way.  This document defines a COSE Hash
   Envelope protected-header parameter in which the producer states the
   deterministic encoding it applied.  It defines one value, the integer
   1, for the Core Deterministic Encoding Requirements of RFC 8949, and
   no encoding of its own; an application profile can identify another
   encoding by a URL.  A verifier ignores a value that does not identify
   an encoding it implements.
- **draft-mih-zhang-agent-disclosure-bundle-03** (new-draft, score 3, verifiable_claims) [none]: [AAC Evidence Bundle](https://datatracker.ietf.org/doc/draft-mih-zhang-agent-disclosure-bundle/) — This document defines the AAC Evidence Bundle, a portable
   presentation and verification container for an Agent Action Capsule
   and the records that make its evidentiary claim intelligible.  A
   permalink carries a bundle in its URL fragment, an offline HTML
   report carries a bundle in its shell, and a hosted report serves a
   bundle at its URL.  The bundle does not alter any enclosed Capsule.
   It declares its citation closure and any missing cited records,
   carries verified disclosure preimages as a bundle-level overlay,
   separates three different completeness claims, can carry the
   producer's signed declaration of what it offers in each category of
   evidence, and permits independently specified extension blocks and
   countersignatures: signatures by a party other than the producer over
   the bundle digest, each accompanied by a statement of which claims
   that party recomputed and with what result.
- **draft-ramadan-mboned-mcast-manifest-02** (new-draft, score 3, core_identity) [none]: [Signed Digest Manifests for Multicast Datagram Authentication](https://datatracker.ietf.org/doc/draft-ramadan-mboned-mcast-manifest/) — This document defines a format for authenticating UDP datagrams
   delivered over IP multicast without changing them.  The sender
   computes a digest over every data datagram of a flow, places the
   digests of up to 37 datagrams in a fixed-layout record, signs the
   record with Ed25519 under a prefix that names the flow, and sends it
   in band, on the flow's own source, group and port, immediately before
   the datagrams it covers, followed by a byte-identical twin.  Every
   record begins with four fixed octets, and no data datagram does, so a
   receiver tells records from data by those octets alone.  A receiver
   verifies one signature per record, hashes each datagram once, and
   delivers a datagram only after its digest matches an entry of a
   verified record; it needs no return channel.  A well-known document
   supplies a flow's keys and parameters.  A Media over QUIC profile and
   a browser profile use the format.
- **draft-ramadan-moq-fec-block-codes-01** (new-draft, score 3, core_identity) [none]: [Block FEC Schemes for Media over QUIC: Reed-Solomon and RaptorQ](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-block-codes/) — This document specifies two block Forward Error Correction (FEC)
   schemes for the FEC mechanism of Media over QUIC (MoQ): the
   systematic Reed-Solomon erasure code over GF(2^8) of ISO/IEC
   23008-10, which is mandatory to implement, and RaptorQ (RFC 6330),
   which is optional.  For each scheme it gives the registered
   identifier, the derivation of the decoder's parameters from the
   instance's configuration and the Repair FEC Payload ID with no in-
   session signaling, the bounds on block size and symbol size, the
   decoding overhead, and how the scheme supports repair layers.  It
   restates the Reed-Solomon code and gives test vectors for it.
- **draft-ramadan-moq-fec-catalog-01** (new-draft, score 3, adjacent_watchlist) [none]: [Catalog Binding for Forward Error Correction in Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-catalog/) — This document binds the Forward Error Correction (FEC) configuration
   data model of the MoQ FEC core mechanism to the catalog of the MOQT
   Streaming Format (MSF) and to its Common Media Application Format
   (CMAF) profile.  It defines the track-level "fec" array of FEC
   instance objects, the fields with which a repair track or a symbol
   track describes its own role, the packaging values "fec-repair" and
   "fec-source", the validation rules that are specific to the catalog
   encoding, and the handling of unknown keys, so that a receiver that
   obtains a track's catalog entry can configure its decoder without in-
   session signaling.
- **draft-ramadan-moq-multicast-03** (new-draft, score 3, core_identity) [none]: [Multicast Delivery and Endpoint Discovery for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-multicast/) — This document specifies multicast delivery mechanisms and catalog-
   based endpoint discovery for Media over QUIC (MoQ).  It defines how
   MoQ sessions integrate with IP multicast (SSM, ASM), Automatic
   Multicast Tunneling (AMT), and TreeDN for scalable live streaming.
   The specification includes a multicast catalog extension for endpoint
   discovery and multi-path delivery across TV, mobile, and browser
   platforms.  All multicast media delivery uses MPEG Media Transport
   Protocol (MMTP) packets, the same packet format that MoQ objects
   carry on QUIC streams and as QUIC datagrams.  A manifest-based
   content-authentication profile protects multicast delivery with
   signed manifest records that travel in band beside those packets.
- **draft-riedl-moq-ad-creative-signaling-02** (new-draft, score 3, core_identity) [none]: [Ad Creative Signaling over the MSF Event Timeline](https://datatracker.ietf.org/doc/draft-riedl-moq-ad-creative-signaling/) — This document defines the carriage of ad creative signaling --
   creative identity, tracking events, and measurement verification
   metadata as specified by SVTA 2053-1 -- in records on a Media over
   QUIC (MOQT) Streaming Format (MSF) Event Timeline track.  It
   complements the carriage of SCTE-35 splice signaling over the same
   mechanism: splice events describe where placement opportunities occur
   on a media timeline, while the event class defined here describes the
   creatives that fill them and how their playback is to be measured.
   This binding is the MSF counterpart of the DASH and HLS carriage
   bindings defined by SVTA 2053-1, which defines none for MOQT.
- **draft-rosenberg-diem-architecture-03** (new-draft, score 3, adjacent_watchlist) [none]: [Digital Emblems - Architectural Considerations](https://datatracker.ietf.org/doc/draft-rosenberg-diem-architecture/) — This document describes an architecture for digital emblems in which
   emblems are authenticated, typed metadata about assets, published in
   the DNS and protected by DNSSEC.  A single architecture serves many
   use cases.  Use cases differ in the shape of their metadata, which is
   described by profiles, rather than in their transport or trust
   machinery.  The document illustrates the architecture with a strawman
   encoding (an EMBLEM resource record carrying a deterministic CBOR map
   with registered, typed map keys) and with worked examples drawn from
   International Humanitarian Law, logistics and customs, diplomatic
   pouches, and peacekeeping.
- **draft-westphal-lsr-isis-database-checksumming-03** (new-draft, score 3, adjacent_watchlist) [none]: [IS-IS Database Fingerprinting](https://datatracker.ietf.org/doc/draft-westphal-lsr-isis-database-checksumming/) — In large IS-IS networks it is useful to quickly verify whether the
   link-state databases on all routers have synchronized properly and to
   derive a rough metric of flooding diffusion behavior.  This document
   proposes a lightweight database fingerprinting mechanism for IS-IS
   along with YANG model extensions providing easy access to such
   information.  For fast verification against a peer, an optional TLV
   carrying the database fingerprint is defined for inclusion in IIH and
   CSNP PDUs.
- **draft-adams-milter-protocol-01** (new-draft, score 2, ignored_after_review) [none]: [The Mail Filter (milter) Protocol](https://datatracker.ietf.org/doc/draft-adams-milter-protocol/) — This document specifies the "milter" protocol, a binary request/
   response protocol by which a Mail Transfer Agent (MTA) can delegate
   inspection and modification of an SMTP transaction to one or more
   external filtering processes.
- **draft-barker-iaml-syntax-00** (new-draft, score 2, ignored_after_review) [none]: [Intelligent Agent Markup Language (IaML/2.1) Syntax](https://datatracker.ietf.org/doc/draft-barker-iaml-syntax/) — The Intelligent Agent Markup Language (IaML) is a linear, zero-copy,
   compute-efficient structural serialization syntax designed for
   high-density communication between Intelligent Agents (IA), edge
   parsers, and local or distributed inference engines.  By replacing
   nested, recursive tree structures (such as JSON and XML) with
   colon-delimited Dot.Case tags and explicit 'e'-prefixed buffer
   closure traps, IaML enables O(n) single-pass stream routing,
   deterministic partitioning between cognitive and control channels,
   and bounded domain extensibility without secondary parsing trees.
- **draft-barker-iatp-transport-00** (new-draft, score 2, ignored_after_review) [none]: [Intelligent Architecture Transfer Protocol (IATP/1.0)](https://datatracker.ietf.org/doc/draft-barker-iatp-transport/) — The Intelligent Architecture Transfer Protocol (IATP) is a
   lightweight, stateful, zero-copy transport protocol designed for
   deterministic communication between Intelligent Agents (IA), local
   inference runtimes, hardware edge controllers, and federated
   knowledge nodes.  Operating natively over TCP port 7027 (cleartext
   local/intranet) and TLS port 443 (federated), IATP pairs a three-
   phase T-Pipe multiplexer with Length-Prefix Chunk Framing and the
   Intelligent Agent Markup Language (IaML) to achieve O(n) single-pass
   stream routing without head-of-line blocking, recursive tree
   allocation, or patent-based encumbrances.
- **draft-hillier-cnsa2-gate-ruling-00** (new-draft, score 2, ignored_after_review) [none]: [A Closed-Profile Ruling on Cryptographic Algorithm Inventories for the CNSA 2.0 Acquisition Gate](https://datatracker.ietf.org/doc/draft-hillier-cnsa2-gate-ruling/) — National security systems of the United States are moving to the
   algorithms of the Commercial National Security Algorithm Suite 2.0,
   on a published NSA timeline.  An acquiring party receives from each
   supplier an inventory of the cryptographic algorithms its product
   carries, in a supplier-chosen spelling, and has no shared procedure
   for ruling on that inventory.  This document specifies a closed
   profile of the CNSA 2.0 algorithm set, a name-folding step, a ruling
   procedure that returns one verdict and one reason for every entry, a
   pair of digests over the canonical input and the canonical ruling,
   and conformance vectors.  The ruling is a pure function of published
   tables, so any two parties who hold the same tables and the same
   inventory reach the same digests.  A keyed mode lets two parties
   compare digests while keeping the inventory from everyone else.  A
   ruling is a verdict against a published profile and carries the
   endorsement of no agency.
- **draft-huang-visual-token-semantic-transport-00** (new-draft, score 2, ignored_after_review) [none]: [Token-Native Semantic Transport for Real-Time Video Agent Systems](https://datatracker.ietf.org/doc/draft-huang-visual-token-semantic-transport/) — This document describes a token-native semantic transport framework
   for real-time video agent systems.  A client device extracts visual
   tokens from captured video and transmits their compressed
   representations to a server for inference.  The framework adopts an
   autoencoder to reduce the dimensionality of visual tokens and
   organizes the compressed tokens into independently entropy-coded
   groups to support packet-level adaptation.  The client device adjusts
   the number of visual tokens to transmit, both before and during each
   frame's transmission, to adapt to changes in available network
   bandwidth.  This document specifies the functional architecture and
   requirements for token compression, packet-aware grouping, rate
   adaptation, and server-side token reconstruction.
- **draft-morrison-command-authority-long-delay-01** (new-draft, score 2, ignored_after_review) [none]: [Command Authority Across Long Delay and Intermittent Contact](https://datatracker.ietf.org/doc/draft-morrison-command-authority-long-delay/) — An enforcement point that checks agent-originated commands offline
   can be out of contact with the party that issues authority for
   anything from about 2.6 seconds to about two weeks, and learns of no
   revocation in that time.  This document profiles the Command
   Authority Envelope of the operational-technology command authority
   profile for that case.  Two implementations have to agree on how an
   enforcement point decides, from a signed revocation status and a
   monotonic counter, that revocation status has gone silent past a
   declared budget, and on what a grant written in advance, a
   contingency grant, permits during that silence.  The profile adds one
   grant field and one declared bound, a second revocation latency
   budget for the grants that field marks.  It also states how expiry
   and maximum age are checked against a declared clock uncertainty,
   which way an unknown revocation check fails for each action class,
   and how a human approval signed before a command departs stays bound
   to one action.

## Ignored after review

- **draft-acosta-deepspace-celestial-bodies-registry-05** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Reference Framework for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document highlights the operational framework within Deepspace/
   TIPTOP protocols to utilize an external, standardized reference
   framework for celestial objects, functioning as an equivalent to ISO
   3166-1 for interplanetary networking.  To avoid operational overhead
   and duplication of effort, this framework defers the definitions,
   naming, and tracking of celestial entities directly to the
   International Astronomical Union (IAU) and the Minor Planet Center
   (MPC).  This document outlines how these external identifiers guide
   hierarchical address allocation without requiring IANA to maintain a
   dedicated astronomical nomenclature registry.  The ultimate objective
   is to establish a clear definition of what constitutes a valid
   Celestial Body for networking purposes.  From a resource-management
   perspective, this framework remains identical regardless of whether
   the target location hosts human colonies, scientific equipment, or
   autonomous robotic assets; any entity requiring internet and
   communication access must rely on a stable celestial anchor.
- **draft-alcapacit-asots-ots-01** (new-draft, score 0, ignored_after_review) [none]: [Oblivious Transport Security (OTS) Version 1](https://datatracker.ietf.org/doc/draft-alcapacit-asots-ots/) — This document specifies Version 1 of the Oblivious Transport Security
   (OTS) protocol.  OTS provides a connection-oriented, encrypted, and
   authenticated transport channel that operates independently of the
   underlying carrier network.  Unlike TLS, OTS eliminates plaintext
   handshake metadata, client implementation fingerprints, traffic-
   analysis side channels, and cross-epoch network-layer address
   correlation by enforcing fixed-size datagrams, constant-rate
   transmission scheduling, cryptographic path binding, and synchronized
   ephemeral endpoint rotation without third-party proxies or relays.
- **draft-backer-sml-action-requests-00** (new-draft, score 0, ignored_after_review) [none]: [Structured Action Requests and Shared Status in Email](https://datatracker.ietf.org/doc/draft-backer-sml-action-requests/) — Much email asks the recipient to do something: approve, send, sign,
   pay, decide.  Email has no interoperable way to say who owns such a
   request, when it is due, or whether it is done, so senders track
   requests by hand and requests are dropped.  This document defines a
   Structured Email (SML) profile for action requests: a machine-
   readable action object, carried as JSON-LD using the schema.org
   Action vocabulary and optionally mirrored as an iCalendar VTODO, plus
   status-update messages that supersede earlier ones, so that every
   participant's mail client in every administrative domain can show one
   current status.  It works with no shared server between
   organizations, and it degrades to readable text in clients that do
   not implement it.
- **draft-balasubramanian-cesaf-00** (new-draft, score 0, ignored_after_review) [none]: [CESAF: The Canonical Email Storage and Archive Format](https://datatracker.ietf.org/doc/draft-balasubramanian-cesaf/) — Email is kept in many incompatible forms: mbox files in several
   variants, Maildir directories, proprietary personal-folder files and
   ad hoc exports.  Most of them lose or alter information, and each can
   be read only by some tools.  This document specifies CESAF, the
   Canonical Email Storage and Archive Format: a file-based format in
   which mail from any source is kept in one store, each message exactly
   as it was obtained, together with the metadata a reader needs to
   present it (its source, folders and flags, decoded header fields,
   MIME structure, character sets and internationalized addresses).  Any
   client that implements this document can read a store written by any
   other.
- **draft-carpenter-gendispatch-anachronisms-08** (new-draft, score 0, ignored_after_review) [none]: [Some Anachronisms and Gaps in IETF Standards Process Documents](https://datatracker.ietf.org/doc/draft-carpenter-gendispatch-anachronisms/) — This document discusses some aspects of documents describing the IETF
   standards process that have been overtaken by events, as well as
   identifying some gaps.  It covers the six-month expiry of Internet-
   Drafts, the reality of the two-stage standards process, and various
   other issues.  This draft is posted only to open a discussion.
- **draft-dikshit-grow-bmp-rd-scoped-rib-stats-04** (new-draft, score 0, ignored_after_review) [none]: [Route-Distinguisher-Scoped BMP RIB Statistics](https://datatracker.ietf.org/doc/draft-dikshit-grow-bmp-rd-scoped-rib-stats/) — [RFC7854] defines the BGP Monitoring Protocol (BMP) and its
   Statistics Report message.  [I-D.ietf-grow-bmp-bgp-rib-stats]
   (published as [RFC9972]) extended that message with a set of
   advanced, per-AFI/SAFI BGP RIB statistics types.  Several ongoing
   individual contributions independently define additional per-
   address-family, per-instance, or per-Route-Distinguisher (RD)
   statistics on top of that base (for example, EVPN-specific RIB
   statistics and VRF Loc-RIB monitoring enhancements), each proposing
   its own ad hoc Stat Data encoding.

   This document defines a single, address-family-agnostic Stat Data
   container -- the "RD-Scoped Statistics" format -- for BMP statistics
   that are naturally scoped below the per-AFI/SAFI level, to a specific
   Route Distinguisher (VRF instance, EVPN Instance, MVPN instance, or
   equivalent).  Address-family-specific documents, such as EVPN-
   specific BMP RIB statistics, are expected to become thin "profiles"
   of this container rather than defining their own wire format,
   reducing duplication and Stat Type registry fragmentation across the
   GROW working group's BMP statistics work.
- **draft-dikshit-netconf-yang-push-causal-ordering-02** (new-draft, score 0, ignored_after_review) [none]: [Cross-Publisher Causal Ordering for YANG-Push Datastore Telemetry](https://datatracker.ietf.org/doc/draft-dikshit-netconf-yang-push-causal-ordering/) — In YANG-Push version 2, each publisher numbers its own notifications,
   and the numbers of two publishers are not comparable.  When a single
   subscription is served by several publishers, for example on a multi-
   line-card router or a disaggregated routing stack, a collector cannot
   order updates across those publishers from the sequence numbers
   alone.  This document defines an opt-in, coordination-free mechanism
   that carries a Comparability Scope, a coarse Causal-Epoch, and a per-
   publisher Local-Sequence-Number in the notification envelope.
   Publishers stay lock-free on the export fast path, and a collector
   reconstructs cross-publisher order within a bounded reordering
   window.  A companion YANG module adds the subscription controls, the
   envelope metadata, and the capability discovery.  The mechanism does
   not require synchronized clocks across publishers.
- **draft-dikshit-netmod-comparability-scope-extension-05** (new-draft, score 0, ignored_after_review) [none]: [A YANG Extension for Declaring the Comparability Scope of Operational State](https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/) — A value exported from a YANG data tree is often unique only within
   its parent, for example an entry numbered 0 under two different
   parents.  Once the value is exported without the parent's key, a
   collector cannot tell whether two such values refer to the same
   thing, and no collector-side normalization can recover the missing
   key.  YANG (RFC 7950) has no way to state this dependency in the
   schema.  This document defines a YANG extension statement,
   "csc:comparability-scope", a four-level scope lattice, a
   compatibility rule, and an export rule, so that the key needed to
   compare a value travels with it, and a schema-aware tool can detect
   an invalid comparison before any data is exported.
- **draft-dkg-reports-json-00** (new-draft, score 0, ignored_after_review) [none]: [Automated Discovery Of Self-Published Reports (reports.json)](https://datatracker.ietf.org/doc/draft-dkg-reports-json/) — This document describes a mechanism that an organization can use to
   enable automatic discovery of documents associated with regulatory
   compliance.  It is motivated by regulations that require, for
   example, publicly accessible reports of audits of automated decision-
   making processes in hiring, or reports on sustainable business
   practices.
- **draft-eastlake-rfc9231bis-xmlsec-uris-11** (new-draft, score 0, ignored_after_review) [none]: [Additional XML Security Uniform Resource Identifiers (URIs)](https://datatracker.ietf.org/doc/draft-eastlake-rfc9231bis-xmlsec-uris/) — This document expands and corrects the IANA "XML Security URIs"
   registry that lists URIs intended for use with XML digital
   signatures, encryption, canonicalization, and key management.  These
   URIs identify algorithms and types of information.  This document
   obsoletes RFC 9231.
- **draft-farinacci-lisp-lispers-net-nat-13** (new-draft, score 0, ignored_after_review) [none]: [lispers.net LISP NAT-Traversal Implementation Report](https://datatracker.ietf.org/doc/draft-farinacci-lisp-lispers-net-nat/) — This memo documents the lispers.net implementation of LISP NAT
   traversal functionality.  The document describes message formats and
   protocol semantics necessary to interoperate with the implementation.
   This memo is not a standard and does not reflect IETF consensus.
- **draft-flentge-dtn-bpv7-custody-transfer-01** (new-draft, score 0, ignored_after_review) [none]: [Custody Transfer for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-bpv7-custody-transfer/) — This document defines custody transfer for Bundle Protocol Version 7.
   A Custody Transfer Extension Block is defined to request custody
   transfer of a bundle, and a Compressed Custody Signal in the form of
   an administrative record is used to report acceptance or rejection
   for multiple bundles.
- **draft-flentge-dtn-bundle-sequence-identification-01** (new-draft, score 0, ignored_after_review) [none]: [Bundle Sequence Identification for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-bundle-sequence-identification/) — This document defines compact sequence identifiers, ranges, and
   collections for referring to one or more Bundle Protocol Version 7
   bundles.  The mechanism supports efficient signaling and enables
   ordered reception, duplicate suppression, and gap detection.
- **draft-flentge-dtn-compressed-status-reporting-01** (new-draft, score 0, ignored_after_review) [none]: [Compressed Bundle Status Reporting for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-compressed-status-reporting/) — This document defines compact, aggregated status reporting for Bundle
   Protocol Version 7.  A Compressed Reporting Extension Block assigns
   sequence information and optionally requests reports, while a
   Compressed Reporting Signal reports events for multiple bundles.
- **draft-gandhi-bpm-rfc6374-perf-metrics-00** (new-draft, score 0, ignored_after_review) [none]: [Performance Metrics Registry Update for RFC 6374 Delay Metrics](https://datatracker.ietf.org/doc/draft-gandhi-bpm-rfc6374-perf-metrics/) — RFC 6374 defines one-way, two-way, and round-trip delay measurements
   for MPLS networks, including a loopback procedure for round-trip
   delay measurement.  The IANA Performance Metrics registry includes
   Metric Type name elements for one-way and round-trip delay, but does
   not include one for two-way delay.  This document requests that IANA
   add the Two-Way Delay name element and add RFC 6374 as a reference
   for the existing One-Way Delay and Round-Trip Delay name elements.
- **draft-gandhi-pce-pm-17** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Performance Measurement for SR-TE and MPLS-TE LSPs with Stateful PCE](https://datatracker.ietf.org/doc/draft-gandhi-pce-pm/) — In certain networks, network performance data such as packet loss,
   delay, and delay variation, as well as bandwidth utilization, are
   critical measures for Traffic Engineering (TE).  These data provide
   operators with the characteristics of their networks for the
   performance evaluation required to provide Service-Level Agreements
   (SLAs).

   Stateful Path Computation Element Communication Protocol (PCEP)
   extensions have been defined for TE LSPs for Segment Routing (SR) and
   RSVP.  This document specifies PCEP extensions that enable and notify
   end-to-end performance measurements, including liveness detection,
   for PCE-Initiated and PCC-Initiated LSPs.  The PCEP extensions apply
   to SR-TE with the MPLS and IPv6 data planes and to MPLS-TE using
   RSVP, with notification to an Active Stateful PCE.  The PCEP
   extensions also apply to multipath LSPs defined in RFC 10066.
- **draft-gerke-publication-process-reform-13** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   The deterministic state-integrity constraints and automated
   milestones defined herein apply programmatically across the core
   processing streams already defined or established in the future.

   This document updates RFC 6359 and RFC 7841.
- **draft-harrison-sshm-mlkem-03** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice Key Exchange in SSH](https://datatracker.ietf.org/doc/draft-harrison-sshm-mlkem/) — This document defines pure post-quantum key exchange methods based on
   Module-lattice post-quantum key encapsulation schemes for use in the
   SSH Transport Layer Protocol.
- **draft-haynes-nfsv4-swap-08** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Atomic EXCHANGE_RANGE Operation to NFSv4.2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-swap/) — The Network File System version 4.2 (NFSv4.2) does not provide
   support for atomic multi-block updates to file data.  This document
   introduces a new EXCHANGE_RANGE operation which provides for such
   atomic updates.  This document extends NFSv4.2 (see RFC7862).

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at https://ietf-wg-
   nfsv4.github.io/exchange_range/draft-haynes-nfsv4-swap.html.  Status
   information for this document may be found at
   https://datatracker.ietf.org/doc/draft-haynes-nfsv4-swap/.

   Discussion of this document takes place on the Network File System
   Version 4 Working Group mailing list (mailto:nfsv4@ietf.org), which
   is archived at https://mailarchive.ietf.org/arch/browse/nfsv4/.
   Subscribe at https://www.ietf.org/mailman/listinfo/nfsv4/.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-wg-nfsv4/exchange_range.

Note to Readers

   This is an individual submission and does not reflect Working Group
   consensus.  The "About This Document" section above has the current
   discussion venue, latest rendering, and source location.
- **draft-he-idr-bgp-ls-sr-policy-diffserv-00** (new-draft, score 0, ignored_after_review) [none]: [Advertisement of SR Policy DiffServ using BGP Link-State](https://datatracker.ietf.org/doc/draft-he-idr-bgp-ls-sr-policy-diffserv/) — This document defines an extension to BGP Link-State (BGP-LS) for the
   advertisement of the Differentiated Services (DiffServ) Per-Hop
   Behavior (PHB) that is bound to a Segment Routing (SR) Policy
   candidate path.  It introduces a new descriptor TLV carried in the SR
   Policy Candidate Path NLRI defined in [RFC9857].  This TLV reports
   the SR Policy candidate path to PHB binding that is actually
   installed in the data plane by a headend node.  This document
   complements the control-plane signaling which conveys the desired PHB
   binding, by enabling the management or control plane to observe the
   actual PHB binding.
- **draft-he-idr-bgp-sr-policy-diffserv-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Extensions of SR Policy for DiffServ](https://datatracker.ietf.org/doc/draft-he-idr-bgp-sr-policy-diffserv/) — This document defines BGP extensions to associate a Differentiated
   Services (DiffServ) Per-Hop Behavior (PHB) with a Segment Routing
   (SR) Policy candidate path.  It introduces a new sub-TLV carried in
   the BGP Tunnel Encapsulation Attribute that accompanies an SR Policy
   NLRI, thereby publishing the binding between an SR Policy candidate
   path and a PHB.
- **draft-he-spring-sr-policy-bandwidth-guarantee-00** (new-draft, score 0, ignored_after_review) [none]: [A Framework for SR Policy Bandwidth Guarantee](https://datatracker.ietf.org/doc/draft-he-spring-sr-policy-bandwidth-guarantee/) — This document describe a scalable framework targeting deterministic
   bandwidth guarantee for SR Policy candidate paths based on the
   Differentiated Services (DiffServ) architecture.  The proposed
   framework separates the statically configured per-hop Quality of
   Service (QoS) scheduling policy from dynamic service admission and
   path selection managed centrally.  Based on the centralized admission
   policy, per-path signaling state and IGP flooding on forwarding nodes
   can be avoided.  It can be well-suited to enterprise, customer,
   carrier, and 5G/6G transport use cases where service classes need
   assured bandwidth guarantee.
- **draft-heilos-eulno-elp8-00** (new-draft, score 0, ignored_after_review) [none]: [The ELP8 Container Format for Geometric Wheel-8 Compression, Hash-Anchored Self-Alignment, and Multi-Gear Streaming](https://datatracker.ietf.org/doc/draft-heilos-eulno-elp8/) — This document specifies the binary container format .elp8 (EULNO
   Layered Protocol 8) for streaming data compression based on counter-
   rotating modulo-8 wheel geometry, inward-mirror stream bisection, and
   hash-anchored phase alignment.  Unlike conventional archive formats
   that treat checksums solely as passive post-decompression checks,
   .elp8 embeds an active Anchor Hash (SHA-256 or SHA-512) inside a
   variable-tier header (56, 88, or 152 bytes) to deterministically seed
   wheel sector alignment and enforce constant-time cryptographic self-
   validation across arbitrary stream sizes up to 2^64 - 1 bytes.
- **draft-hoffman-deleg-secure-transports-01** (new-draft, score 0, ignored_after_review) [none]: [DELEG Extensions for Secure Transports](https://datatracker.ietf.org/doc/draft-hoffman-deleg-secure-transports/) — The DELEG base protocol allows a DNS zone operator to specify servers
   to be used when delegating zones to other DNS nameservers.  This
   document extends the base protocol to allow zone operators to specify
   secure transports for those delegations.
- **draft-hss-srv6ops-srv6-routing-planes-03** (new-draft, score 0, ignored_after_review) [none]: [BGP based SRv6 Routing Planes for DC network](https://datatracker.ietf.org/doc/draft-hss-srv6ops-srv6-routing-planes/) — This document introduces a BGP-based multi-planar routing
   architecture for modern data center networks, with a particular focus
   on environments running AI/ML workloads that demand traffic
   segregation.  The proposed solution enables deterministic routing for
   workloads with characteristics such as collective communication and
   multi-tenancy.  It allows the creation of multiple logical routing
   planes over a shared physical infrastructure by defining planes
   through three key elements: Constraints (e.g., fabric color
   inclusion/exclusion) Calculation types (e.g., shortest path) and
   Metric types (e.g., cost, delay, bandwidth).
- **draft-iannone-dawn-privacy-considerations-01** (new-draft, score 0, ignored_after_review) [none]: [Privacy Considerations for the Discovery of Agents, Workloads, and Named Entities (DAWN)](https://datatracker.ietf.org/doc/draft-iannone-dawn-privacy-considerations/) — This document describes the privacy issues associated with the
   Discovery of Agents, Workloads, and Named Entities (DAWN).  It
   provides general observations about typical current privacy practices
   in similar domains like, DNS, HTTP, and in general privacy in
   information retrieval.
- **draft-ietf-calext-jscalendar-icalendar-31** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication, and defines conversion rules for all elements that are
   common to both formats.  It updates the semantics of some iCalendar
   elements to align with JSCalendar, and extends both formats to
   support converting arbitrary or unknown JSCalendar and iCalendar
   elements.  This document updates RFC 5545 ("iCalendar") and its
   extensions RFC 7986 and RFC 9073.
- **draft-ietf-detnet-wireless-oam-support-01** (new-draft, score 0, ignored_after_review) [detnet]: [Operations, Administration and Maintenance (OAM) features for RAW](https://datatracker.ietf.org/doc/draft-ietf-detnet-wireless-oam-support/) — Some critical applications may use a wireless infrastructure.
   However, wireless networks exhibit a bandwidth of several orders of
   magnitude lower than wired networks.  Besides, wireless transmissions
   are lossy by nature; the probability that a packet cannot be decoded
   correctly by the receiver may be quite high.  In these conditions,
   providing high reliability and a low delay is challenging.  This
   document lists the requirements of the Operation, Administration, and
   Maintenance (OAM) features are recommended to provide availability
   and reliability on top of a collection of wireless segments.  This
   document describes the benefits, problems, and trade-offs for using
   OAM in wireless networks to achieve Service Level Objectives (SLO).
- **draft-ietf-dtn-udpcl-05** (new-draft, score 0, ignored_after_review) [dtn]: [Delay-Tolerant Networking UDP Convergence Layer Protocol Version 2](https://datatracker.ietf.org/doc/draft-ietf-dtn-udpcl/) — This document describes a UDP convergence layer (UDPCL) for Delay-
   Tolerant Networking (DTN).  This version of the UDPCL protocol
   clarifies requirements of the earlier experimental RFC 7122, adds
   discussion of multicast addressing, congestion signaling, and updates
   to the Bundle Protocol (BP) contents, encodings, and convergence
   layer requirements in BP version 7.  Specifically, the UDPCL uses
   CBOR-encoded BPv7 bundles as its service data unit being transported
   and provides an unacknowledged transport of such bundles.  This
   version of UDPCL also includes security and extensibility mechanisms.
- **draft-ietf-idr-addpath-paths-limit-01** (new-draft, score 0, ignored_after_review) [idr]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-ietf-idr-bgp-ls-flex-algo-ext-04** (new-draft, score 0, ignored_after_review) [idr]: [Advertising Flexible Algorithm Extensions in BGP Link-State](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-flex-algo-ext/) — Flexible Algorithm is a solution that allows some routing protocols
   (IS-IS and OSPF) to compute paths over a network based on user-
   defined (and hence, flexible) constraints and metrics.  The
   computation is performed by routers participating in the specific
   network in a distributed manner using a Flexible Algorithm
   Definition.  This Definition is provisioned on one or more routers
   and propagated through the network by IS-IS and OSPF flooding.

   BGP Link-State (BGP-LS) enables the collection of various topology
   information from the network.  BGP-LS supports the advertisement of
   Flexible Algorithm Definition and other Flexible Algorithm related
   advertisements as a part of the topology information from the
   network.  This document specifies the advertisement of further
   Flexible Algorithm related extensions in BGP-LS.
- **draft-ietf-idr-multinexthop-attribute-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP MultiNexthop Attribute](https://datatracker.ietf.org/doc/draft-ietf-idr-multinexthop-attribute/) — Today, a BGP speaker can advertise one nexthop for a set of NLRIs in
   an Update message.  This nexthop can be encoded in either the top-
   level BGP-Nexthop attribute (code 3), or inside the MP_REACH_NLRI
   attribute (code 14).  Forwarding information related to the nexthop
   is scattered across various attributes, extended communities or the
   NLRI field.

   This document defines a new optional non-transitive BGP attribute
   called "MultiNexthop (MNH)" with IANA code TBD.  The MNH provides two
   things: it allows carrying the Nexthop and related forwarding
   information in one BGP attribute.  The MNH also enables carrying an
   ordered set of multiple Nexthops in the same attribute, with
   forwarding information scoped on a per Nexthop basis.
- **draft-ietf-idr-rt-derived-community-17** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route-Target-derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route-Target-derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-intarea-v4-via-v6-12** (new-draft, score 0, ignored_after_review) [intarea]: [IPv4 routes with an IPv6 next hop](https://datatracker.ietf.org/doc/draft-ietf-intarea-v4-via-v6/) — V4-via-v6 routing is a technique that uses IPv6 next-hop addresses
   for forwarding IPv4 packets, and thus makes it possible to route IPv4
   packets across a network where some routers have not been assigned
   IPv4 addresses.  This document describes v4-via-v6 routing, and
   defines related operational procedures, notably the origination of
   ICMPv4 packets by nodes that might not have an IPv4 address.
- **draft-ietf-ipsecme-ikev2-beet-mode-05** (new-draft, score 0, ignored_after_review) [ipsecme]: [IKEv2 negotiation for Bound End-to-End Tunnel (BEET) mode ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-beet-mode/) — This document specifies a new Notify Message Status Type for the
   Internet Key Exchange Protocol Version 2 (IKEv2), to negotiate IPsec
   ESP Bound End-to-End Tunnel (BEET) mode.  BEET mode combines the
   benefits of tunnel mode with reduced overhead, making it suitable for
   applications requiring minimalistic end-to-end tunnels and multi-
   address multi-homing capabilities.  The introduction of the
   USE_BEET_MODE Notify Message Status Type enables the negotiation and
   establishment of BEET mode security associations.
- **draft-ietf-jmap-mail-sharing-03** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Mail Sharing](https://datatracker.ietf.org/doc/draft-ietf-jmap-mail-sharing/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) for Mail to enable sharing of mailboxes between
   users.  Building upon the JMAP Sharing framework defined in
   [RFC9670], this specification extends the Mailbox data type defined
   in [RFC8621] with properties necessary to configure and manage access
   permissions for shared mailboxes.  The extension introduces a new
   capability that indicates server support for mailbox sharing and
   defines the additional properties required to share mailboxes with
   other principals, including the ability to control which users may
   access a mailbox and what permissions they possess.
- **draft-ietf-mlcodec-opus-extension-07** (new-draft, score 0, ignored_after_review) [mlcodec]: [Extension Formatting for the Opus Codec](https://datatracker.ietf.org/doc/draft-ietf-mlcodec-opus-extension/) — This document updates RFC6716 to extend the Opus codec (RFC6716) in a
   way that maintains interoperability, while adding optional
   functionality.
- **draft-ietf-mpls-mna-ioam-20** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, collects operational and telemetry information in the
   packet using IOAM-Data-Fields while the packet traverses a path
   between two points in the network.  Several IOAM Option-Types are
   available, including Pre-allocated Trace, Proof of Transit (POT),
   Edge-to-Edge (E2E), and Incremental Trace.  These Option-Types can be
   used to collect information for calculating various performance
   metrics.  RFC 9326 defines the IOAM Direct Export (IOAM-DEX) Option-
   Type, which is used as a trigger for IOAM data to be directly
   exported or locally aggregated without being pushed into in-flight
   data packets.

   MPLS Network Action (MNA) mechanisms indicate actions to be performed
   on any combination of Label Switched Paths, MPLS packets, and the
   node itself, and transport the data needed for these actions.  This
   document defines MNAs to collect and transport the operational state
   and telemetry information using IOAM-Data-Fields as well as IOAM-DEX.
- **draft-ietf-nmop-rfc3535-20years-later-06** (new-draft, score 0, ignored_after_review) [nmop]: [An Update of Operators Requirements on Network Management Protocols and Modelling](https://datatracker.ietf.org/doc/draft-ietf-nmop-rfc3535-20years-later/) — This document identifies a list of operators requirements for network
   management operations.  These requirements reflect advances in this
   field since the publication of "IAB Network Management Workshop" (RFC
   3535), which was instrumental for developing many key technologies
   that are widely deployed.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/boucadair/rfc3535-20years-later.
- **draft-ietf-openpgp-external-secrets-03** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-ietf-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
- **draft-ietf-pce-entropy-label-position-11** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extension for SR-MPLS Entropy Label Positions](https://datatracker.ietf.org/doc/draft-ietf-pce-entropy-label-position/) — The Entropy label (EL) can be used in the SR-MPLS data plane to
   improve load-balancing and multiple Entropy Label Indicator (ELI)/EL
   pairs may be inserted in the SR-MPLS label stack as specified in
   RFC8662.

   This document defines a set of extensions for Path Computation
   Element Communication Protocol (PCEP) to indicate where in the label
   stack the ELI/EL pairs should be inserted in SR-MPLS network - the
   Entropy Label Positions (ELP).
- **draft-ietf-pce-sr-p2mp-policy-23** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pce-sr-path-segment-16** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extension for Path Segment in Segment Routing (SR)](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-path-segment/) — The Path Computation Element (PCE) provides path computation
   functions in support of traffic engineering in Multiprotocol Label
   Switching (MPLS) and Generalized MPLS (GMPLS) networks.

   The Source Packet Routing in Networking (SPRING) architecture
   describes how Segment Routing (SR) can be used to steer packets
   through an IPv6 or MPLS network using the source routing paradigm.  A
   Segment Routed Path can be derived from a variety of mechanisms,
   including an IGP Shortest Path Tree (SPT), explicit configuration, or
   a Path Computation Element (PCE).

   Path identification is needed for several use cases such as
   performance measurement in Segment Routing (SR) network.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) to support requesting, replying,
   reporting and updating the Path Segment ID (Path SID) between PCEP
   speakers.
- **draft-ietf-rtgwg-vrrp-p2mp-bfd-16** (new-draft, score 0, ignored_after_review) [rtgwg]: [Applicability of Bidirectional Forwarding Detection (BFD) for Multi-point Networks in Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-p2mp-bfd/) — This document specifies the applicability of Bidirectional Forwarding
   Detection in multipoint networks to support sub-second failure
   detection for Virtual Router Redundancy Protocol Router Role
   election.  The mechanism enables faster determination of the Active
   Router without requiring any modification to the protocol behavior or
   message formats defined in RFC 9568.
- **draft-ietf-tiptop-usecase-05** (new-draft, score 0, ignored_after_review) [tiptop]: [IP in Deep Space: Key Characteristics, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-tiptop-usecase/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  Most of the IP protocol stack
   used on the Internet, in particular reliable transport protocols and
   applications, is based on the assumptions of shorter delays and
   mostly uninterrupted communications.  This document describes the key
   characteristics, use cases, and requirements for deep space
   networking, intended to help when profiling IP protocols in such
   environment.
- **draft-ietf-tsvwg-fq-pie-04** (new-draft, score 0, ignored_after_review) [tsvwg]: [Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/) — This document presents Flow Queue Proportional Integral controller
   Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue
   Management (AQM) algorithm to isolate flows and tackle the problem of
   bufferbloat.  FQ-PIE uses hashing to classify incoming packets into
   different queues and provide flow isolation.  Packets are dequeued by
   using a variant of the round robin scheduler.  Each such flow is
   managed by the PIE algorithm to maintain high link utilization while
   controlling the queue delay to a target value.
- **draft-ietf-v6ops-6mops-13** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (e.g. local area network (LAN)).  This approach enables
   incremental transition from dual-stack to IPv6-only networks by
   allowing IPv6-capable devices to remain IPv6-only while the network
   is seamlessly supplying IPv4 addresses to those devices that require
   them.  This document discusses the requirements, recommendations, and
   challenges associated with deploying IPv6-mostly networks in
   enterprise and public Wi-Fi environments.
- **draft-ietf-v6ops-nat64-wkp-1918-11** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Globally Reachable IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the deployment guidance provided in
   Section 3.1 of RFC 6052 (IPv6 Addressing of IPv4/IPv6 Translators)
   that IPv4/IPv6 Translators must not use the Well-Known Prefix
   64:ff9b::/96 to represent non-globally reachable IPv4 addresses, such
   as those defined in RFC 1918 (Address Allocation for Private
   Internets) or listed in Section 2.2.2 of RFC 6890 (Special-Purpose IP
   Address Registries).  This change enables IPv6-only nodes to reach
   IPv4-only services with specific non-globally reachable addresses by
   leveraging the Well-Known Prefix.

   This document updates RFC 6052 to allow packets in which an address
   is composed of the Well-Known Prefix and specific non-globally
   reachable IPv4 addresses to be translated.
- **draft-intesigroup-dlts-14** (new-draft, score 0, ignored_after_review) [none]: [Distributed Ledger Time-Stamp](https://datatracker.ietf.org/doc/draft-intesigroup-dlts/) — This document defines a standard to extend Time Stamp Tokens with
   Time Attestations recorded on Distributed Ledgers.

   The aim is to provide long-term validity to Time Stamp Tokens,
   backward compatible with currently available software.
- **draft-jiang-sidrops-psvro-05** (new-draft, score 0, ignored_after_review) [none]: [Route Origin Registry Problem Statement](https://datatracker.ietf.org/doc/draft-jiang-sidrops-psvro/) — Prefix hijacking, i.e., unauthorized announcement of a prefix, has
   emerged as a major security threat in the Border Gateway Protocol
   (BGP), garnering widespread attention.  To mitigate such attacks
   while supporting legitimate Multiple Origin AS (MOAS), higher
   requirements are placed on the route origin registry.  This document
   describes the limitations of existing route origin registries.
- **draft-jones-outerprise-handshake-01** (new-draft, score 0, ignored_after_review) [none]: [Cryptographic Handshake Profile for Fiscal-Sponsorship Onboarding and Outer Pilot Execution](https://datatracker.ietf.org/doc/draft-jones-outerprise-handshake/) — This individual Internet-Draft proposes a detached evidence exchange
   for sponsor onboarding, a bounded pilot, and an institutional review.
   A synthetic trace specifies byte-level commitments and evidence
   links.  The profile concerns evidence handling and leaves funding,
   institutional decisions, and legal eligibility to the responsible
   parties.
- **draft-mery-nagy-taistamp-01** (new-draft, score 0, ignored_after_review) [none]: [Taistamp: Signed TAI64N Timestamps over HTTP](https://datatracker.ietf.org/doc/draft-mery-nagy-taistamp/) — This memo defines Taistamp, an HTTP-accessible service that returns
   the current time as a TAI64N label, optionally signed with Ed25519.
   The service is reached at the well-known URI /.well-known/taistamp
   and is intended for clients that need an authenticated wall-clock
   reading without running an NTP stack or relying on the client's own
   clock for TLS certificate validation.  The signing scheme uses a
   length-prefixed, domain-separated framing and publishes verification
   keys as DNS TXT records in a DKIM-inspired selector layout.
- **draft-morrison-claim-currency-02** (new-draft, score 0, ignored_after_review) [none]: [Claim Currency: A Read-Time Currency Band for Claims Held in a Shared Append-Only Store](https://datatracker.ietf.org/doc/draft-morrison-claim-currency/) — Software agents that read a shared, append-only store of claims can
   cite an aged claim as though it were current, and can write new
   claims grounded on it.  This memo defines the one element two parties
   would have to agree on, the envelope a read returns for a claim.  It
   carries the assertion, the time of its grounding observation, its
   basis set, a three-state currency band (FRESH, AGING, STALE) derived
   at read time and never stored, and the evidence from which the band
   was derived.  A relying party can re-derive the band from that
   evidence.  It also states the rules under which a reader may emit an
   aged claim and under which a store must refuse a new claim that cites
   an out-of-date basis.  The memo is an Informational problem statement
   and description of one design.  It has no second implementer yet, and
   it is offered for review as an Independent Submission.
- **draft-prz-lsr-ash-packets-09** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).  ASH also provides a graceful restart
   architecture that addresses scaling limitations by distributing
   recovery work among helpers under the restarting router's
   orchestration.
- **draft-ramadan-moq-fec-core-01** (new-draft, score 0, ignored_after_review) [none]: [Forward Error Correction for Media over QUIC: Core Mechanism](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-core/) — This document specifies how Forward Error Correction (FEC) repair
   data is carried alongside source media in Media over QUIC (MoQ)
   without naming a particular FEC code.  It states the properties that
   an FEC scheme must have to be used with this mechanism, and defines
   everything that does not depend on the scheme: how source objects
   become source symbols, how source symbols are numbered and grouped
   into blocks, two ways of carrying source symbols (as the source
   track's own objects, or as a separate symbol track suited to datagram
   delivery), repair tracks that receivers subscribe to independently
   and in layers, the repair object format, repair Group IDs that make
   repair fetchable by block, and equal and unequal protection driven
   only by metadata that MoQ Transport exposes, so that FEC works when
   payloads are encrypted end to end.  Relays need no FEC knowledge, and
   a relay that has it can rebuild source objects missing from its cache
   when the publisher records how each object is sent.  Specific FEC
   schemes, catalog bindings, packaging-specific profiles and multicast
   delivery are left to companion documents.
- **draft-ramadan-moq-mmt-03** (new-draft, score 0, ignored_after_review) [none]: [MPEG Media Transport (MMT) Packaging for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-mmt/) — This document specifies the use of MPEG Media Transport (MMT) as a
   container format for Media over QUIC (MoQ).  MMT carries media over
   broadcast (ATSC 3.0, ARIB STD-B60), multicast, and unicast (QUIC/
   WebTransport) networks.  This specification defines the mapping of
   MMT packets to MoQ objects, the "iso-ssbg1-v1" block profile under
   which the Forward Error Correction (FEC) mechanism for MoQ protects
   MMTP packets -- its source symbols, its Source FEC Payload ID
   trailer, its repair packet and its keyframe overlay -- the derivation
   of MoQ catalogs from MMTP signaling, and compatibility considerations
   for both ATSC 3.0 and ARIB STD-B60 systems, including the ATSC 3.0
   signed region.
- **draft-saum-grow-bmp-afi-safi-evpn-09** (new-draft, score 0, ignored_after_review) [none]: [EVPN-Specific BMP RIB Statistics Extensions](https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/) — This document defines new EVPN-specific BGP Monitoring Protocol (BMP)
   statistics types.  These extensions include scalar counters for EVPN
   route types specifically, while also keeping scope for defining
   counters which are EVPN route-type agnostic but related to BGP-EVPN
   RIB like, number of multihoming Ethernet Segments, number of
   multihomed EVIs, number of aliased paths, number of dynamic inter-VRF
   route leaking (IVRL).

   This revision (-06) firms up the specification for working group
   consideration: it adds a Relationship to Other Work section that
   explicitly maps this document to concurrently circulating GROW
   contributions on BMP statistics and TLV extensions and invites
   coordination with their authors, corrects the YANG alignment
   reference, strengthens Security Considerations, and adds a worked
   example.  No statistics semantics, Stat Type/Subtype allocations, or
   wire formats defined in -05 are changed.
- **draft-saum-nvo3-mtu-propagation-over-evpn-overlays-11** (new-draft, score 0, ignored_after_review) [none]: [MTU propagation over EVPN Overlays](https://datatracker.ietf.org/doc/draft-saum-nvo3-mtu-propagation-over-evpn-overlays/) — Path MTU Discovery between end-host-devices/Virtual-Machines/servers/
   workloads connected over an EVPN-Overlay Network in
   Datacenter/Campus/enterprise deployment, is a problem, yet to be
   resolved in the standards forums.  It needs a converged solution to
   ensure optimal usage of network and computational resources of the
   networking elements, including underlay routers/switches,
   constituting the overlay network.  This documents takes leads from
   the guidelines presented in [RFC4459].

   The overlay connectivity can pan across various sites (geographically
   seperated or collocated) for realizing a Datacenter Interconnect or
   intersite VPNs between campus sites (buildings, branch offices etc).

   This literature intends to solve problem of icmp error propagation
   from an underlay routing/switching device to an end-host (hooked to
   EVPN overlay), thus facilitating "accurate MTU" learnings.

   This document also leverages the icmp multipart message extension,
   mentioned in [RFC4884] to carry the original packet in the icmp PDU.
- **draft-saum-rtgwg-mtu-propagation-evpn-overlays-01** (new-draft, score 0, ignored_after_review) [none]: [MTU propagation over EVPN Overlays](https://datatracker.ietf.org/doc/draft-saum-rtgwg-mtu-propagation-evpn-overlays/) — Path MTU Discovery between end-host-devices/Virtual-Machines/servers/
   workloads connected over an EVPN-Overlay Network in
   Datacenter/Campus/enterprise deployment, is a problem, yet to be
   resolved in the standards forums.  It needs a converged solution to
   ensure optimal usage of network and computational resources of the
   networking elements, including underlay routers/switches,
   constituting the overlay network.  This documents takes leads from
   the guidelines presented in [RFC4459].

   The overlay connectivity can pan across various sites (geographically
   seperated or collocated) for realizing a Datacenter Interconnect or
   intersite VPNs between campus sites (buildings, branch offices etc).

   This literature intends to solve problem of icmp error propagation
   from an underlay routing/switching device to an end-host (hooked to
   EVPN overlay), thus facilitating "accurate MTU" learnings.

   This document also leverages the icmp multipart message extension,
   mentioned in [RFC4884] to carry the original packet in the icmp PDU.
- **draft-sharma-moq-trace-context-00** (new-draft, score 0, ignored_after_review) [none]: [Trace Context Propagation for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-sharma-moq-trace-context/) — This document defines a Media over QUIC Transport (MOQT) extension
   that carries W3C Trace Context on SUBSCRIBE and FETCH requests.
   Subscribers, relays, and publishers can use it to correlate spans
   across MOQT sessions.
- **draft-shin-avtcore-rtp-multi-opus-05** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP/SDP Signaling for Opus Multistream Operation](https://datatracker.ietf.org/doc/draft-shin-avtcore-rtp-multi-opus/) — This document specifies RTP/SDP signaling for Opus multistream
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
- **draft-smc-grow-bmp-route-change-stats-04** (new-draft, score 0, ignored_after_review) [none]: [BMP Route Change Statistics Based on Routing Policy](https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/) — This document defines few generic BGP Monitoring Protocol (BMP)
   statistics for monitoring route modifications or changes due to
   applying Routing Policy.  These statistics are reported per BGP peer
   using the BMP Statistics Report message.

   This revision (-02) firms up the specification for working group
   consideration: it adds a Relationship to Other Work section that
   explicitly maps this document to concurrently circulating GROW
   contributions on BMP statistics and policy-driven telemetry and
   invites coordination with their authors, adds a worked example, and
   strengthens Security Considerations.  No statistics semantics, Stat
   Type allocations, or wire formats defined in -01 are changed.
- **draft-sporeba-tsvwg-mobile-l4s-01** (new-draft, score 0, ignored_after_review) [none]: [Best Practices for L4S Implementation for Mobile Devices](https://datatracker.ietf.org/doc/draft-sporeba-tsvwg-mobile-l4s/) — This document describes best practices for deployment of Low Latency,
   Low Loss, and Scalable Throughput (L4S) in mobile devices.  It
   defines the responsibilities of the host operating system and the
   link-layer (modem and Wi-Fi) subsystems to ensure successful end-to-
   end low-latency communication.
- **draft-stone-rtgwg-telemetry-optimization-00** (new-draft, score 0, ignored_after_review) [none]: [Telemetry-Driven Congestion Optimization](https://datatracker.ietf.org/doc/draft-stone-rtgwg-telemetry-optimization/) — This document describes Telemetry-Driven Congestion Optimization
   (TDCO), a solution in which a centralized controller uses near-real-
   time per-tunnel demand and per-interface traffic measurements to
   prevent and alleviate link overload autonomously.  The controller
   changes the paths of the tunnels under its control through existing
   mechanisms such as the Path Computation Element Communication
   Protocol (PCEP), BGP Segment Routing (SR) Policy, or NETCONF/YANG.
   TDCO avoids placing Traffic Engineering (TE) tunnels where they would
   cause overload and, when overload occurs, re-routes only as many TE
   tunnels as are needed to relieve the overload onto paths with spare
   capacity that meet their full TE constraints.

   This document describes the solution and the safety properties needed
   to operate it without operator approval of individual actions.  It
   defines no protocol extensions.
- **draft-suresh-webbotauth-verification-outcome-00** (new-draft, score 0, ignored_after_review) [none]: [Reporting Web Bot Auth Verification Outcomes](https://datatracker.ietf.org/doc/draft-suresh-webbotauth-verification-outcome/) — Web Bot Auth lets automated HTTP clients sign requests with HTTP
   Message Signatures and publish their keys in a directory.  Its
   protocol specification defines three verifier outcomes (verified,
   invalid and unverified) but no way for a verifier to tell the client
   which one it reached, or why.  A client whose request is refused
   cannot tell a bad signature from an expired one, or a missing key
   from a directory the verifier could not fetch.

   This document defines a problem type for reporting Web Bot Auth
   verification outcomes, carried in problem details content or in the
   Problem-Details header field, a small registry of reason codes,
   levels of disclosure that let a verifier limit what it reveals, and
   an optional well-known resource that clients can use to check their
   signatures against a verifier without affecting any other resource.
- **draft-templin-6man-aero-omni-amen-19** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-trammell-tsvwg-443-is-enough-02** (new-draft, score 0, ignored_after_review) [none]: [443 is Enough: Guidance on Port Allocation for HTTP-based Services](https://datatracker.ietf.org/doc/draft-trammell-tsvwg-443-is-enough/) — [RFC7605] provides guidance on the use of port numbers and the
   criteria for new port assignments, including a test for whether a
   proposed service is distinct from an existing service.  It gives the
   example that "an automated system that happens to use HTTP framing --
   but is not primarily accessed by a browser -- might be a new
   service."  It also might not.  This document clarifies the
   application of the distinct-protocol test in [RFC7605] Section 7.1 to
   services built on HTTP as a substrate, in light of HTTP's evolution
   since its publication, and provides guidance to applicants and
   reviewers on when an HTTP-based service qualifies for a new port
   assignment and when it does not.
- **draft-watts-bounded-review-00** (new-draft, score 0, ignored_after_review) [none]: [Bounded Prior-Art Review and Transparent Scope Claims in Internet-Drafts](https://datatracker.ietf.org/doc/draft-watts-bounded-review/) — Technical standards work benefits from extensive reading, comparison,
   and revision.  However, examining many documents does not demonstrate
   that every relevant RFC, Internet-Draft, publication, or earlier
   contribution has been reviewed.  This document discusses a voluntary
   approach to describing the scope and limits of related-work review in
   Internet-Draft contributions.  It proposes a review-coverage
   statement, an illustrative record, and a process for correcting
   unsupported novelty claims.  The approach does not replace IETF
   policies, create a new protocol, or certify priority, originality, or
   completeness.
- **draft-xiao-fann-fast-cnp-with-proxy-06** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node for the congested network node to notify the
   traffic sender of the congestion.  The proxy network node is used to
   translate the congestion notification.  The congested network node
   sends the congestion notification to the proxy network node in a
   format defined in this document, and then the proxy network node
   translates the received congestion notification to a format known by
   the traffic sender and resends the translated congestion notification
   to the traffic sender.
- **draft-xu-savax-control-12** (new-draft, score 0, ignored_after_review) [none]: [Control Plane of Source Address Validation Architecture-eXternal (SAVA-X)](https://datatracker.ietf.org/doc/draft-xu-savax-control/) — Because the Internet forwards packets according to the IP destination
   address, packet forwarding generally occurs without examining the
   source address.  Consequently, malicious attacks have been launched
   using spoofed source addresses.  The inter-domain source address
   validation architecture represents an effort to enhance the Internet
   by employing state machines to generate consistent tags.  When two
   end hosts in different address domains (ADs) of an IPv6 network
   communicate with each other, tags are appended to the packets to
   identify the authenticity of the IPv6 source address.
- **draft-xu-savax-data-11** (new-draft, score 0, ignored_after_review) [none]: [Data Plane of Source Address Validation Architecture-eXternal (SAVA-X)](https://datatracker.ietf.org/doc/draft-xu-savax-data/) — Because the Internet forwards packets in accordance with the IP
   destination address, packet forwarding generally occurs without
   examination of the source address.  As a result, malicious attacks
   have been launched using spoofed source addresses.  The inter-domain
   source address validation architecture represents an effort to
   enhance the Internet by employing state machines to generate
   consistent tags.  When two end hosts in different address domains
   (ADs) of an IPv6 network communicate with each other, tags are
   appended to the packets to identify the authenticity of the IPv6
   source address.

   This document focuses on the data plane of the SAVA-X mechanism.
- **draft-xu-savax-protocol-11** (new-draft, score 0, ignored_after_review) [none]: [Communication Protocol Between the AD Control Server and the AD Edge Router of Source Address Validation Architecture-eXternal (SAVA-X)](https://datatracker.ietf.org/doc/draft-xu-savax-protocol/) — Because the Internet forwards packets in accordance with the IP
   destination address, packet forwarding generally occurs without
   examination of the source address.  As a result, malicious attacks
   have been launched using spoofed source addresses.  The inter-domain
   source address validation architecture represents an effort to
   enhance the Internet by employing state machines to generate
   consistent tags.  When two end hosts in different address domains
   (ADs) of an IPv6 network communicate with each other, tags are
   appended to the packets to identify the authenticity of the IPv6
   source address.

   This memo focuses on the communication protocol between ACSes and
   AERs of the SAVA-X mechanism.
- **draft-xu-sidrops-rpa-verification-03** (new-draft, score 0, ignored_after_review) [none]: [BGP AS_PATH Verification Based on Route Path Authorizations (RPA) Objects](https://datatracker.ietf.org/doc/draft-xu-sidrops-rpa-verification/) — The Route Path Authorizations (RPA) is an RPKI object that attests to
   the routing paths description which an Autonomous System (AS) would
   obey in Border Gateway Protocol (BGP) route propagation.  This
   document specifies an RPA-based AS Path Verification methodology to
   mitigate, even solve, AS Path forgery and route leaks.  This document
   also explains the various BGP security threats that RPA can help
   address and provides operational considerations associated with RPA
   deployment.
- **draft-yang-multicast-mac-examples-00** (new-draft, score 0, ignored_after_review) [none]: [Reading Ethernet Multicast Addresses in IPv4 and IPv6 Packet Traces](https://datatracker.ietf.org/doc/draft-yang-multicast-mac-examples/) — A packet trace may show the same Ethernet destination address for two
   packets sent to different IP multicast groups.  This note gives
   worked IPv4 and IPv6 examples for readers interpreting such traces.
   For each address family, one pair of inputs differs in a bit that the
   Ethernet mapping discards.  A third input differs in a bit that the
   mapping retains.  The examples exercise existing mapping rules.
- **draft-zhao-scitt-state-comparison-binding-00** (new-draft, score 0, ignored_after_review) [none]: [State-Comparison Binding for Action Records](https://datatracker.ietf.org/doc/draft-zhao-scitt-state-comparison-binding/) — An action record can say which controlled state was in force when an
   artefact was produced.  It usually cannot say _which state the record
   was compared against_, so the question "is the state that was in
   force still the state now?" has to be answered by asking the producer
   at verification time.

   This document defines one field, compared_state, and four processing
   rules, so that a verifier can decide the state question from the
   record alone, and so that a later comparison is expressible as a new
   sealed revision rather than an edit.

   This is a field definition, not a framework.  It adds nothing to the
   envelope, the lifecycle, or the absence taxonomy of the profiles it
   references.
- **draft-zhu-idr-bgp-ha-00** (new-draft, score 0, ignored_after_review) [none]: [Cross-Device High Availability for BGP Sessions Using BFD](https://datatracker.ietf.org/doc/draft-zhu-idr-bgp-ha/) — Some BGP deployments cannot rely on peers to negotiate Graceful
   Restart.  An operator may instead want a standby routing instance on
   a separate device to continue an existing BGP connection and its
   associated Bidirectional Forwarding Detection (BFD) session after the
   active device fails, without changes at the peer.  This document
   describes the deployment problem, the conditions under which takeover
   can be attempted, and how to verify continuity as observed by the
   peer.  It does not specify a replication protocol, change BGP or BFD
   on the wire, or claim lossless forwarding.  It provides operational
   criteria that can be applied independently of how the underlying TCP
   connection is preserved.
- **draft-zhu-tcpm-tcp-ha-00** (new-draft, score 0, ignored_after_review) [none]: [Peer-Transparent High Availability for Established TCP Connections](https://datatracker.ietf.org/doc/draft-zhu-tcpm-tcp-ha/) — This document describes the conditions under which a standby device
   can continue an established TCP connection after failure of the
   active device, without requiring changes at the remote TCP endpoint.
   It distinguishes connection continuity from application recovery and
   specifies observations for evaluating a failover attempt.  It defines
   no new TCP option, state transfer protocol, or interoperability
   requirement.

## Errors / fetch failures

_None._
