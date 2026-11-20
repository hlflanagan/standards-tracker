# IETF Identity + AI Standards Watch

Date: 2026-11-20

## Read now

- **draft-das-cyber-defense-execution-finality-00** (new-draft, score 33, trust_infrastructure) [none]: [Execution Finality for AI Safety and Agentic AI Security: Containing the Consequences of Stolen Credentials and Autonomous Cyberattacks at the Final Effect Boundary](https://datatracker.ietf.org/doc/draft-das-cyber-defense-execution-finality/) — A cyberattack does not have to defeat every security mechanism to
   become catastrophic.  One internet-facing service, one stolen but
   valid credential, one hijacked administrative session, or one
   autonomous AI tool calling a legitimately available interface may be
   enough.  The decisive risk is the transition from access, prediction,
   intention or nominal authorization into an actual consequence: a
   changed configuration, an executed privileged command, a released
   dataset, a provisioned cloud resource, a dispatched payment, an
   altered network route or an activated physical device.

   This document analyzes two independently documented public
   developments of November 2026: the reported intrusion into the
   internal operational network of the Fugaku supercomputer through a
   publicly reachable status dashboard, and the reported discovery of
   autonomous multi-agent offensive frameworks, including an exposed
   framework named exploit_agent, together with cloud-credential abuse
   such as LLMJacking.  The two events are not shown to be connected,
   and no public evidence shows artificial intelligence was used at
   Fugaku.  They share a defender-risk pattern: apparently valid access
   becoming a real consequence.

   The document specifies a consequence-bound architecture.  A proposed
   operation (a Candidate Act) remains non-effective until the actual
   pending operation, its target, destination, scope, resource version,
   current authority and protected policy state have been independently
   validated at a defender-controlled, non-bypassable enforcement point
   (a Finality Sink, in industry terms a reference monitor or commit
   gate) located at, or unavoidably upstream of, the point where the
   effect becomes real.  It defines normative requirements for coverage,
   independence, effect binding, freshness and revocation, cumulative
   exposure, replay and idempotency, failure semantics and safety-
   critical operation; application profiles for high-performance
   computing, cloud control planes, AI-agent tool execution,
   telecommunications, finance and cyber-physical systems; a
   counterfactual analysis of the Fugaku incident; a differentiation
   from conventional systems; ten falsifiable experiments; and an
   informative FAQ.

   IETF relevance: the document is an architectural and requirements
   contribution relevant to security work on remote attestation,
   workload identity, delegated and fine-grained authorization,
   transparency of authorization evidence, and agent-to-tool interfaces.
   Industry relevance: the model is applicable to AI-agent platforms,
   cloud providers, HPC operators, telecommunications operators and
   financial infrastructure; the alignment sections are AI-generated,
   are not an endorsement, validation or infringement statement, and
   must be cross-checked against the original filings.  Regulatory
   relevance: the document discusses relevance to the EU AI Act
   (cybersecurity and robustness of high-risk AI systems), NIS2, DORA
   and GDPR security of processing; it is not legal advice.

   Based on the Mothership application PCT/IB2026/055615, filed 4 June
   2026 and publicly disclosed 16 July 2026.  The underlying invention
   is human-originated; AI-assisted tools were used to create this
   document, which may contain errors, and readers must cross-check it
   against the original, publicly available sources.  To read the full
   PCT filing, search "Sangam Das" on WIPO PATENTSCOPE, search PCT/
   IB2026/055615 (pctib202655615), or read it at
   https://www.tdcommons.org/dpubs_series/12542/. No deployment,
   adoption, endorsement or performance claim is made about any third-
   party system, and no latency, efficacy or safety guarantee is
   claimed.
- **draft-sharif-agent-audit-trail-10** (new-draft, score 33, trust_infrastructure) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
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
- **draft-elekula-seat-attested-tls-testing-01** (new-draft, score 29, trust_infrastructure) [none]: [Interoperability, Security Evaluation, and Negative Testing for Attested TLS 1.3 and DTLS 1.3](https://datatracker.ietf.org/doc/draft-elekula-seat-attested-tls-testing/) — This document defines a reproducible framework for interoperability
   testing, security evaluation, negative testing, and performance
   measurement of implementations that integrate remote attestation with
   TLS 1.3 and DTLS 1.3.

   The framework complements existing Secure Evidence and Attestation
   Transport (SEAT) and Remote ATtestation procedureS (RATS)
   specifications. It defines evaluation profiles, test-vector
   requirements, deployment topology descriptions, decision-state
   observations, common result classifications, cross-implementation
   procedures, and security evaluation methods.

   The framework evaluates the boundaries between transport
   authentication, attestation capability negotiation, Evidence
   conveyance, appraisal, authorization, workload identity association,
   and protected application-data release.

   It additionally addresses reusable Attestation Results,
   connection-bound Evidence, cross-connection trust continuity,
   exporter-derived credentials, key custody, credential lifecycle,
   multi-Relying-Party isolation, proxy deployments, session resumption,
   early data, state drift, revocation, privacy, availability, and
   cryptographic agility.

   This document introduces a machine-readable evaluation model that
   connects individual protocol requirements to test vectors,
   implementation versions, observed results, and reproducible evidence.

   It does not define a new attestation protocol, Evidence format, TLS
   or DTLS extension, cryptographic key schedule, universal appraisal
   policy, or credential format. Protocol-specific behaviour remains
   governed by the exact specification revision under evaluation.

   A successful test demonstrates observed behaviour under declared
   conditions. It does not constitute a security certification or prove
   that a Target Environment is free from compromise.
- **draft-ietf-rats-verifiable-proof-of-environment-01** (new-draft, score 29, trust_infrastructure) [rats]: [Verifiable Proof of Environment Attestation Profile](https://datatracker.ietf.org/doc/draft-ietf-rats-verifiable-proof-of-environment/) — Operators of regulated, sovereign, and high-assurance deployments
   require hardware-rooted, machine-verifiable proof that a workload
   executes in its approved environment.  Current remote attestation
   mechanisms address two relevant properties in isolation: platform
   integrity — that the hardware and software stack are in an approved,
   untampered state — and physical residency — that the hardware resides
   within an approved geographic boundary.  Neither property alone is
   sufficient: integrity without residency permits a valid platform to
   operate outside approved boundaries; residency without integrity
   permits a compromised platform to claim valid placement.

   This document defines the *Verifiable Proof of Environment
   Attestation Profile (V-PEA)*, a profile of the RATS Architecture (RFC
   9334) in which a platform binds location Claims to its own integrity
   Evidence in a single Evidence structure (lah-bundle) signed by a TPM
   quote.  V-PEA does not generate location Claims: they are produced by
   location sources, such as GNSS receivers, mobile network operators,
   or timing-based anchors, and V-PEA binds them to the particular
   platform that will receive a credential or key.  V-PEA defines two
   Evidence dimensions: *WHAT* — hardware provenance (TPM Attestation
   Key registered and manufacturer-endorsed), platform integrity
   (firmware and OS state matching reference values), and workload agent
   software integrity (binary digest matching an approved value); and
   *WHERE* — physical residency within an approved geographic boundary,
   as reported by one or more location sources.  A single TPM quote
   binds WHAT and WHERE into one signed statement: neither dimension can
   be forged or transplanted without invalidating the other.  This
   document specifies the binding for TPM 2.0; the binding does not
   depend on a TPM, and other platform roots of trust can provide it.

   For the WHERE dimension, V-PEA supports Transparent Zero-Knowledge
   Proofs (ZKPs), enabling an Attester to prove geographic compliance
   without disclosing precise coordinates.  A positive V-PEA Attestation
   Result enables a Relying Party to issue hardware-rooted credentials
   or authorize operations — combining verified execution environment
   (WHAT) with verified physical placement (WHERE) — before releasing
   sensitive assets or granting access.  Integration with workload
   identity systems is described in the WIMSE Integration appendix.
- **draft-ganesan-agent-authenticator-00** (new-draft, score 28, core_identity) [none]: [Agent Authenticator: Hardware-Bound, Origin-Bound Authentication for AI Agents](https://datatracker.ietf.org/doc/draft-ganesan-agent-authenticator/) — This document specifies the Agent Authenticator, a mechanism that
   lets autonomous software agents, such as AI coding agents,
   authenticate to services with properties comparable to passkeys: keys
   held in secure hardware, no shared secrets, binding to the service's
   origin that a manipulated agent cannot override, attested execution
   environments, and explicit human approval of each agent and of high-
   risk actions.  The same protocol serves agents on personal computers
   and in cloud environments.  It is a profile over existing mechanisms
   rather than a new identity system: it uses OAuth 2.0 Token Exchange,
   the Identity Assertion JSON Web Token (JWT) Authorization Grant, and
   Model Context Protocol (MCP) authorization, and it binds each agent
   action to a signed, tamper-evident record.
- **draft-watts-agent-authority-transition-receipts-02** (new-draft, score 28, authorization) [none]: [Agent Authority Transition Receipts for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-authority-transition-receipts/) — Autonomous agents increasingly act across administrative and security
   domains using workload identities, OAuth credentials, delegated
   authorization, attestations, and policy engines.  Existing mechanisms
   can establish identity, delegation, or access rights, but deployments
   still lack a common artifact that records which policy and which
   evidence were evaluated when an operation moved into an authorized,
   denied, revoked, or expired authority state.

   This document defines an Agent Authority Transition Receipt (AATR), a
   signed, non-bearer receipt that cryptographically binds an agent
   operation to the principal, policy, evidence set, decision, audience,
   validity interval, and predecessor authority state used for that
   decision.  AATR intentionally separates evidence from authorization
   and authorization from execution.  Missing or indeterminate required
   evidence fails closed.  AATR is designed to compose with OAuth,
   workload identity, remote attestation, transparency services, and
   agent-specific delegation protocols rather than replace them.
- **draft-kamimura-vap-framework-03** (new-draft, score 27, trust_infrastructure) [none]: [Verifiable AI Provenance Framework (VAP): An Architectural Framework for Auditable AI Decision Trails](https://datatracker.ietf.org/doc/draft-kamimura-vap-framework/) — Automated decision-making systems, including AI and algorithmic
   systems in critical infrastructure, currently lack standardized
   mechanisms for producing provenance records that third parties can
   verify independently.  Traditional logging approaches do not provide
   the cryptographic properties that regulatory examination, forensic
   investigation, and cross-organizational accountability depend on:
   detectability of alteration, detectability of omission after
   commitment, and attribution.

   This document describes the Verifiable AI Provenance Framework (VAP),
   an architectural framework that defines requirements for producing
   verifiable decision trails using existing IETF security technologies.
   VAP does not define new protocols or cryptographic primitives;
   rather, it provides an architectural coordination layer that enables
   domain-specific profiles to leverage Supply Chain Integrity,
   Transparency and Trust (SCITT), Remote Attestation Procedures (RATS),
   CBOR Object Signing and Encryption (COSE), and related IETF work in a
   consistent manner.

   VAP makes records auditable and attributable after the fact.  It does
   not prevent, block, or intercept any system behaviour, and it does
   not warrant that any recorded decision was correct, fair, or safe.
   The detailed requirement set is maintained by the VeritasChain
   Standards Organization (VSO) as a separate specification; this
   document describes the architecture and its mapping to IETF work.

   This document is intended to frame the problem space and facilitate
   discussion about whether architectural coordination work is needed in
   this area.
- **draft-durga-pquip-pqc-agentic-delegation-01** (new-draft, score 26, agent_identity) [none]: [Post-Quantum Hybrid Cryptographic Delegation Chains and Merkle-Aggregated Execution Receipts for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-pquip-pqc-agentic-delegation/) — Autonomous AI agent ecosystems rely on multi-hop cryptographic
   delegation chains and signed execution traces (currently built on
   Ed25519, ECDSA P-256, and RSA-PSS) to enforce least-privilege tool
   invocations across Model Context Protocol (MCP) and Agent-to-Agent
   (A2A) boundaries, and to preserve long-term non-repudiation for
   regulatory audit logs.  This architecture faces two existential
   vulnerabilities in the Post-Quantum era: (1) "Harvest-Now, Forge-and-
   Repudiate-Later" (HNFRL) attacks, wherein Cryptographically Relevant
   Quantum Computers (CRQCs) running Shor's algorithm retroactively
   forge or repudiate multi-year compliance traces (e.g., 7-to-10-year
   HIPAA, SOX, FDA 21 CFR Part 11, and defense operational logs) and
   synthesize retroactive human-in-the-loop approvals; and (2) "Lattice
   Signature-Bloat Amplification," wherein naively substituting 64-byte
   Ed25519 signatures with 3,309-byte ML-DSA-65 (FIPS 204) signatures
   across a 10-hop sub-agent chain inflates per-call authorization
   headers from 640 bytes to over 46 KB (including public keys),
   exceeding HTTP/2 header limits and degrading sub-10ms real-time tool
   routing.

   This document specifies a wire-compatible Post-Quantum Agentic
   Delegation and Trace Receipt profile ("PQ-Agentic").  It introduces a
   two-tier cryptographic architecture: (a) a Hot-Path Hybrid Delegation
   Envelope combining classical Ed25519 with ML-DSA-65 (FIPS 204) via
   Pre-Verified Session-Grant Digest Chaining (PVSGDC), replacing
   redundant per-call inline re-transmission of O(N) prior delegators'
   5,261-byte ML-DSA-65 public keys and signatures with 32-byte SHAKE256
   digests of out-of-band PEP-verified delegation grants; and (b) a
   Cold-Path Long-Horizon Archival Receipt anchored with stateless hash-
   based SLH-DSA-SHAKE-128f ([FIPS205]) over RFC 9943 SCITT transparency
   Merkle roots, guaranteeing 30-year quantum-resistant non-repudiation
   even under catastrophic lattice cryptanalysis.
- **draft-lemonnier-scitt-decision-provenance-03** (new-draft, score 24, trust_infrastructure) [none]: [Decision Provenance for SCITT: binding software releases and agent actions to the decisions behind them](https://datatracker.ietf.org/doc/draft-lemonnier-scitt-decision-provenance/) — Build attestations, bills of materials and Signed Statements in a
   Transparency Service record what was built and by whom.
   Authorization receipts for agent actions can establish who approved
   an exact action; the statement profiles for agent actions record a
   human approval as the producer's claim.  The release and agent action
   examples in this document use the Decision Provenance Standard to
   supply a separately verifiable decision record and an attachment for
   the approved action.  The cited records and receipts supply evidence
   about the build, the action or its authorization, according to their
   respective profiles.  This document describes how a decision record
   and its action-binding attachment, as the extension proposals of the
   Decision Provenance Standard define them, sit under a release
   statement, a build attestation or an agent action record by typed
   digest references; how a verifier checks them offline, including the
   approver's signature where one is carried; and how the witness
   checkpoints of the anchoring extension are registered in a
   Transparency Service.  For a relying party reviewing one occurrence,
   it specifies which authenticated inputs to compare and how to report
   missing evidence about presentation, authority and the observed
   effect.  A software release decision and an agent action capsule are
   the worked examples; the model has no feature specific to either.
   This document is independent of the Decision Provenance Standard, is
   not part of it, does not change it, and is not endorsed by its
   Steward.
- **draft-watts-high-assurance-agent-control-envelope-02** (new-draft, score 24, authorization) [none]: [High-Assurance Agent Control Envelope](https://datatracker.ietf.org/doc/draft-watts-high-assurance-agent-control-envelope/) — Agentic systems can authenticate successfully, hold a valid
   authorization object, and still be unsafe to execute because required
   evidence is missing, the software has not reached a required
   assurance stage, the authority epoch is stale, a prior revocation is
   unresolved, or a human-approval requirement is unsatisfied.  This
   document defines the High-Assurance Agent Control Envelope (HAACE), a
   protocol-neutral profile that binds an exact agent action to identity
   status, authorization state, policy, assurance stage, evidence state,
   authority epoch, revocation state, oversight requirements, and an
   action-time decision.  HAACE requires fail-closed treatment of
   missing or indeterminate prerequisites, separates authorization from
   execution, and produces non-bearer decision and execution receipts.
   The profile composes with OAuth, workload identity, attestation,
   transparency, and agent-authorization mechanisms rather than
   replacing them.
- **draft-das-consequence-bound-execution-authority-00** (new-draft, score 23, authorization) [none]: [Consequence-Bound Execution Authority for Autonomous Systems: Operation Reconstruction, Independent Validation, and Protected Effectuation Profiles](https://datatracker.ietf.org/doc/draft-das-consequence-bound-execution-authority/) — Authorization to compute, propose, prepare, simulate or request an
   operation is not, by itself, authorization to cause the operation's
   actual consequential effect.  An authorized operation may afterwards
   be transformed, delegated, delayed, replicated, compiled, offloaded
   or executed under different technical conditions.  This document
   describes an architecture, and a set of candidate interoperability
   requirements, for separating those authorizations: a proposed
   operation is held as a Candidate Act in a Non-Effective State; the
   Actual Pending Operation is reconstructed; current source authority,
   context, dependencies and policy and revocation epochs are evaluated
   by an independent validator; a scoped, non-bearer execution
   authorization is issued; and a protected Finality Sink at the actual
   effectuation boundary re-derives the operation, enforces the
   authorization, and supports reconciliation against authoritative
   outcome evidence.

   The document is an individual, informational technical proposal.  It
   credits OAuth, JWT/CWT, RBAC/ABAC, zero-trust, remote attestation,
   transaction logs, hardware isolation and cryptographic signatures for
   their established functions and does not characterize them as
   defective.  It includes a threat model, 12 figures, 39 consequence-
   specific profiles, a non-normative European applicability discussion
   and an examiner-oriented terminology appendix.  It is not an IETF
   standard, an EU regulatory instrument, a telecommunications or
   financial standard, or an endorsement by any named company.
- **draft-elekula-rats-model-loading-binding-00** (new-draft, score 23, trust_infrastructure) [none]: [Attestation of AI Inference Execution Environments Using RATS: Trusted Model Loading, Runtime Binding, and Per-Inference Evidence](https://datatracker.ietf.org/doc/draft-elekula-rats-model-loading-binding/) — AI inference services increasingly depend on combinations of model
   artifacts, inference runtimes, execution environments, hardware
   accelerators, and security-relevant configuration.

   A relying party authorizing an AI service to access protected
   resources may require evidence that an approved model artifact was
   actually loaded and used by an acceptable inference runtime.

   Measuring a model artifact and measuring an inference runtime
   independently does not establish that the measured artifact was the
   artifact loaded by the measured runtime. Similarly, attesting an
   execution environment does not, by itself, establish which model
   processed a particular inference request.

   This document examines these problems using the Remote ATtestation
   procedureS (RATS) architecture specified in RFC 9334.

   It distinguishes execution-instance attestation from per-inference
   operation evidence and describes a candidate measurement and binding
   approach using a protected model-loading mechanism, trusted
   measurement collection, and cryptographically protected evidence.

   It examines how the Entity Attestation Token (EAT), specified in RFC
   9711, and the measured-component information model specified in RFC
   10013 may represent relevant measurements and component information.

   It also examines the relationship between this proposal and existing
   work on attested AI agent identity and application-layer action
   evidence.

   The document does not define a new attestation protocol, EAT profile,
   registered Claim, Evidence conveyance protocol, or appraisal-policy
   language.

   Its objective is to determine whether existing RATS mechanisms can
   support interoperable appraisal of AI model-to-runtime relationships
   and to identify any remaining requirements for standardization.

   The document does not claim that attestation establishes model
   correctness, safe behavior, or the correctness of generated outputs.
- **draft-elekula-agentproto-linked-dialog-01** (new-draft, score 22, core_identity) [none]: [Privacy-Preserving Verification of Linked-Dialog Relationships Across Trust Boundaries](https://datatracker.ietf.org/doc/draft-elekula-agentproto-linked-dialog/) — Agentic systems increasingly create, delegate, relay, and transform
   dialogs across multiple agents, protocols, services, and
   administrative trust boundaries. In these environments, a verifier
   may need to determine whether two dialogs are related without
   requiring unrestricted disclosure of their contents or relying
   exclusively on the assertions of an intermediary.

   This document describes properties and a conceptual evaluation model
   for privacy-preserving verification of linked-dialog relationships
   across trust boundaries. It distinguishes dialog association from
   context propagation, relationship verification from authentication
   and authorization, and verification outcomes from assessments of
   evidence completeness.

   The document also considers evidence scope, source positions,
   temporal references, intermediary continuity, lifecycle changes,
   identity binding, privacy, and evidence availability. It identifies
   requirements intended to help future protocol designs represent
   linked-dialog relationships in a way that can be independently
   evaluated while limiting unnecessary disclosure.

   This document does not define a wire format, cryptographic mechanism,
   identifier format, transport binding, authorization protocol,
   audit-log structure, or completeness-proof mechanism. It provides
   terminology, design properties, and interoperability considerations
   for further discussion.
- **draft-mckenna-webbotauth-collection-attestation-02** (new-draft, score 22, trust_infrastructure) [none]: [Attested Conduct for Anonymous Web Data Collection: Use Cases, Requirements, and a Tiered Model](https://datatracker.ietf.org/doc/draft-mckenna-webbotauth-collection-attestation/) — Anonymous Bot Authentication lets a web site learn that an automated
   client holds a credential from an Anchor whose policies it accepts,
   without learning which client it is.  This document describes web
   data collection use cases that need that property, and what they
   require of the evidence an Anchor evaluates, of what a site can
   verify about conduct it cannot attribute, and of what a buyer of
   collected data needs to see.  It proposes a tiered model.  Collectors
   register signed statements of their own conduct in a SCITT
   Transparency Service; the site, its security intermediary, or a
   network intermediary may corroborate them; and an Anchor acting as a
   certifying body may appraise them.  Coarse, unlinkable attributes
   about the data's eventual recipient let a site restrict use by
   category of recipient without learning who the recipient is.
- **draft-cosme-audit-agent-traceability-00** (new-draft, score 21, adjacent_watchlist) [none]: [Delegation and Interaction Traceability for AI Agents: An Attestation and Registry Evidence Model](https://datatracker.ietf.org/doc/draft-cosme-audit-agent-traceability/) — AI agents increasingly act through chains of delegation - user to agent,
agent to subagent, subagent to tool - in which the party harmed by an
action,
or asked to trust its result, is rarely the party that operated the
agent.
This document describes requirements and an evidence model for
delegation
and interaction traceability in such chains. The model is built on two
mechanisms for which measured, independently verifiable evidence exists:
(a) an append-only, hash-chained exhibit registry in which each admitted
action is recorded exactly once and counters reconcile against registry
contents, and (b) per-action attestation published at kernel level with
measured publication latencies in the sub-microsecond-to-microsecond
range.
The document defines a traceability record, states what a verifier can
and
cannot conclude from a set of such records, and identifies the points at

which existing agent-protocol work - identity, authorisation, and
transport -
needs a common traceability layer. It defines no wire protocol of its
own;
it states the requirements a traceability mechanism must satisfy so that
formats defined elsewhere can be evaluated against them.
- **draft-sogomonian-aiid-00** (new-draft, score 21, core_identity) [none]: [Autonomous Agent Identity and Runtime Control Status (AIID)](https://datatracker.ietf.org/doc/draft-sogomonian-aiid/) — Autonomous software agents increasingly take consequential actions on
   behalf of people and organizations.  Existing identity systems (OAuth
   2.0, SPIFFE, and the WIMSE workload identity architecture)
   authenticate such agents, but they do not define a common, vendor-
   neutral way for an accountable owner to place a running agent into a
   restricted state, nor a common way for a relying party to check that
   state immediately before acting.

   This document defines AIID: a durable identifier for an autonomous
   agent, a small runtime control state machine (active, safe_mode,
   suspended, revoked), an asymmetric authority model in which automated
   monitors may only tighten state and only the accountable owner may
   loosen it, a namespace-wide freeze, and a pre-action status check
   with fail-closed semantics.  AIID is designed to bind to, not
   replace, existing identity: it defines an "aiid" claim for OAuth 2.0
   access tokens and corresponding token introspection members, bindings
   for SPIFFE and WIMSE identifiers, a mapping onto the OAuth Token
   Status List, and change notification using the OpenID Shared Signals
   Framework.  It also defines compact signed action receipts, and an
   OPTIONAL enforcement gateway deployment profile.
- **draft-elekula-rats-pqc-attestation-00** (new-draft, score 20, trust_infrastructure) [none]: [Post-Quantum Cryptographic Considerations for RATS Evidence and Attestation Results](https://datatracker.ietf.org/doc/draft-elekula-rats-pqc-attestation/) — This document analyzes post-quantum cryptographic considerations for
   Remote ATtestation procedureS (RATS) Evidence, Attestation Results,
   Endorsements, and Reference Values. It describes the distinction
   between post-quantum key establishment and post-quantum
   authentication of attestation artifacts; identifies integrity,
   provenance, freshness, and session-context properties that must
   remain independently verifiable; and provides implementation guidance
   for artifact sizing, bounded processing, transformation, transport,
   failure handling, and privacy.

   The document does not define a new cryptographic algorithm,
   attestation token, Evidence format, transport protocol, TLS
   extension, or key-establishment mechanism. It relies on existing RATS
   architecture and data models, existing COSE and JOSE mechanisms, and
   protocol-specific work in the Secure Evidence and Attestation
   Transport (SEAT) Working Group. The intended result is a set of
   interoperable considerations that RATS profiles and
   attestation-system designers can apply when deploying
   post-quantum-capable attestation systems.
- **draft-hopley-x402-retention-chain-08** (new-draft, score 20, core_identity) [none]: [Self-Verifiable Retention Chain for Payment Receipts](https://datatracker.ietf.org/doc/draft-hopley-x402-retention-chain/) — This document specifies eight cryptographic constructions for
   self-verifiable agentic payment records.  The first, the Retention
   Chain Reference (retention_chain_ref), enables tamper-evident audit
   chains linking payment receipts without requiring external
   infrastructure.  The second, the Payment Action Lifecycle, defines
   a content-addressed model for the exactly-once execution of payment
   actions, including an action reference primitive (action_ref) and a
   per-state transition hash (transition_hash) with a provable SKIP-on-
   retry idempotency guarantee.  The third, the Settlement-Action
   Binding (binding_ref), binds a settled payment to the verified agent
   action it paid for and to the retention chain entry recording it, so
   that a settlement attestation proves not only that a payment occurred
   but which verified action it corresponds to.  The fourth, the Policy
   Binding (policy_bound_ref), binds a content-addressed snapshot of the
   governing policy to an existing binding or chain reference, so that a
   decision is verifiable against the exact policy version that admitted
   it and a policy rotation is detectable by recomputation.  The fifth,
   the Compliance Gate Binding (gate_ref), binds a categorical
   ALLOW/REFER/DENY compliance verdict and a no-PII payer reference to a
   policy or binding reference, so that a screening decision is provably
   tied to the policy in force when it was made and carries no personal
   data in the bound record.  The sixth, the Pre-Payment Decision
   Chain (guardrail_ref), composes an agent identity reference, a spend
   authority reference, and the policy in force into one recomputable
   pre-payment ALLOW/DENY decision.  The seventh, Post-Decision
   Execution Evidence (execution_ref), binds an executed action to the
   exact decision that authorized it, so the recorded execution is
   provably consistent with the decision and not merely correlated with
   an agent identity.  The eighth, Cross-Party Authority Delegation
   (delegation_ref), binds a delegation of authority from one party to
   another and chains hand-offs, so a verifier can confirm that authority
   did not widen across an organizational boundary.  All
   constructions use only SHA-256 and the JSON Canonicalization Scheme
   (JCS, RFC 8785),
   and are verifiable by any party holding the relevant receipts without
   contacting the issuer.  The constructions satisfy the transaction
   recording and audit trail obligations of MiCA Article 68(9), DORA
   Article 17, and AMLR Article 77.
- **draft-malhotra-scitt-oar-00** (new-draft, score 20, authorization) [none]: [Open Action Record (OAR): Authority, Approval and Outcome Evidence for AI Agent Actions](https://datatracker.ietf.org/doc/draft-malhotra-scitt-oar/) — Several profiles record what an AI agent was asked to do, and the
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
   salted commitments and can be disclosed field by field.  The
   constructions are implemented in the Open Action Record (OAR) format,
   with three verifiers that agree on published test vectors.
- **draft-xu-oan-resource-identity-discovery-02** (new-draft, score 20, core_identity) [none]: [Trust-Governed Resource Identity and Discovery Architecture for OpenAgenet](https://datatracker.ietf.org/doc/draft-xu-oan-resource-identity-discovery/) — This document describes a trust-governed resource identity and
   discovery architecture for OpenAgenet (OAN).  It covers callable
   agents, skills, Model Context Protocol (MCP) servers, tools, and
   application programming interfaces.  Registrars verify registration
   authority, a Root accepts versioned resource packages, and authorized
   Discovery Nodes expose verified candidates.  Consumers verify package
   integrity, acceptance, and current state before using a resource
   through its native protocol or artifact format.

   The architecture can be profiled with Decentralized Identifier (DID)
   document concepts and credential-based assertions.  This document
   does not define a new DID method, media type, URI scheme, transport
   protocol, ranking algorithm, blockchain protocol, agent invocation
   protocol, or product-native schema.
- **draft-das-ai-agent-cyberattack-effect-finality-00** (new-draft, score 19, agent_identity) [none]: [AI Safety: When AI Agents Initiate Cyberattacks -- Execution Finality for Data Exfiltration, Payment Diversion, Infrastructure Changes, and Code-Executing Agents](https://datatracker.ietf.org/doc/draft-das-ai-agent-cyberattack-effect-finality/) — Problem.  An AI agent can cause an unauthorized real-world effect --
   a confidential data export, a payment to a substituted beneficiary, a
   network or industrial configuration change, a code deployment or a
   secret release -- while every individual check succeeds: the model
   accepted a plausible task, the agent held a valid credential, the
   tool call was syntactically permitted, and the gateway saw an allowed
   method.  The gap is that the check and the effect are not the same
   thing.  Identity and access controls answer "may this principal call
   this interface?"; they do not, by themselves, answer "may this exact
   effect, with these resolved targets and values, complete now, on this
   route, given what has already happened?"

   Solution.  This document describes an execution-finality profile for
   AI-initiated operations.  An agent's proposal is held as a non-
   effective Candidate Act. A protected validator compares a canonical
   descriptor of the operation actually about to be committed with a
   source-authority envelope that model-editable content cannot create
   or enlarge.  A Finality Sink, which owns the effect-causing
   credential or commit right, verifies an act-bound, non-bearer
   Execution Handle over the same bytes it commits, consumes it
   atomically with the commit, and emits an authenticated destination
   receipt.  Later phases and retries are gated on that receipt rather
   than on the agent's own report.  Unknown outcomes become
   INDETERMINATE and are reconciled before any retry.

   Context.  The document analyses four scenarios (enterprise data
   exfiltration, payment diversion, critical-infrastructure
   configuration manipulation, and code-executing agents), specifies
   data objects, a Candidate Act state machine, atomic consumption and
   crash-recovery rules, sink trust, delegation attenuation, protocol
   placement for tool and agent-to-agent calls, revocation freshness,
   latency placement, legacy integration and a falsifiable evaluation
   plan.  It is a prospective architecture: no measured latency,
   blocking rate or deployment is claimed.  A reviewer FAQ is included.
   Critical technical review is invited.
- **draft-hopley-x402-atb-reputation-credential-00** (new-draft, score 19, adjacent_watchlist) [none]: [ATB Pass Certificate: Agent Reputation Credential for Agentic-Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-atb-reputation-credential/) — This document specifies the ATB Pass Certificate, a Falcon-1024 post-
   quantum signed reputation credential issued by the Agent Trust Bench
   (ATB) to autonomous AI agents that have demonstrated safe payment-
   decision behaviour against the bench's adversarial profile corpus.
   The credential is presented by agents to participating x402 gateways
   via an HTTP header for reputation-gated variable pricing.

   Two certificate versions are specified.  Phase 1 carries the agent's
   refusal-rate score in cleartext; the gateway verifies the Falcon-1024
   signature and applies a discount when the score meets a declared
   threshold.  Phase 2 replaces the score with a Pedersen commitment to
   the score and a Bulletproofs range proof attesting score >= threshold
   without revealing the score, its components, or the agent's
   underlying behaviour distribution.

   Certificates are canonicalised under RFC 8785 (JSON Canonicalization
   Scheme) with an in-band canonicalisation-rule pin and signed with
   Falcon-1024 (NIST FIPS 206, post-quantum).  Phase 2 ZKP elements use
   Ristretto255 as the elliptic curve group with the dalek-cryptography
   Bulletproofs instantiation.

   This document also specifies the composition of the ATB Pass
   Certificate as an evidence-source input to draft-hopley-x402-
   composite-trust-query, gateway verification algorithms for both Phase
   1 and Phase 2 credentials, and security and privacy considerations
   arising from the bearer-token transport model and the ZKP soundness
   assumptions.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.
- **draft-watts-ai-identity-02** (new-draft, score 19, trust_infrastructure) [none]: [AID-1: A Cryptographically Bindable Identity and Provenance Architecture for AI Systems](https://datatracker.ietf.org/doc/draft-watts-ai-identity/) — This document specifies AID-1, a provider-independent architecture
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
- **draft-watts-scientific-constitutional-constraints-00** (new-draft, score 19, authorization) [none]: [Scientific Constitutional Constraints for Evidence-Governed Agentic Internet Operations](https://datatracker.ietf.org/doc/draft-watts-scientific-constitutional-constraints/) — This document proposes SCC-1, an experimental profile for preserving
   evidentiary, authorization, and effect-enforcement boundaries in
   agent-mediated Internet operations.  The term constitutional
   describes a locally adopted set of durable technical constraints; it
   does not refer to any national constitution, create law, or determine
   legal validity.  SCC-1 separates authentication, attestation,
   evidence appraisal, policy authority, delegated scope, action
   approval, sink admission, execution, and observed outcomes.  It
   specifies fail-closed state transitions, auditable claim promotion,
   and bounded closure statements for explicitly scoped sinks.  This
   document does not introduce a new credential or OAuth grant.  Its
   claims remain experimental: reported local Python/SQLite and Go/file-
   state experiments are not independent cross-host verification or
   production security certification.
- **draft-drake-agent-identity-problem-statement-02** (new-draft, score 18, adjacent_watchlist) [none]: [Identity for Autonomous Agents and Robots: Problem Statement, Threat Model, and Terminology](https://datatracker.ietf.org/doc/draft-drake-agent-identity-problem-statement/) — Autonomous software agents, and increasingly physical robots, now act
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
- **draft-drake-agent-identity-resolution-02** (new-draft, score 18, core_identity) [none]: [Resolution and Verification of Agent Identities using DNS and RDAP](https://datatracker.ietf.org/doc/draft-drake-agent-identity-resolution/) — The Agent Identity Registry System (AIRS)
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
- **draft-durga-agenttrust-trace-verification-01** (new-draft, score 18, trust_infrastructure) [none]: [Cryptographic Execution-Trace Verification, JCS Canonicalization, and Fail-Closed Delegation Attestation for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-agenttrust-trace-verification/) — This document specifies a deterministic cryptographic verification
   profile for execution traces, delegation chains, and weight-custody
   manifests generated by autonomous artificial intelligence (AI) agents
   operating across Model Context Protocol (MCP), Agent-to-Agent (A2A),
   and enterprise system-of-record boundaries.  The profile binds JSON
   Canonicalization Scheme (JCS, RFC 8785) pre-image serialization,
   Ed25519 (RFC 8032) and ECDSA P-256/P-384 signatures, JSON Web Key
   (JWK, RFC 7517) thumbprint pinning, and fail-closed revocation and
   freshness checks so that relying parties can independently verify
   whether an agent action was authorized prior to commit.
- **draft-hopley-x402-payment-evidence-frame-01** (new-draft, score 18, core_identity) [none]: [Payment Evidence Frame for Agentic-Payment Lifecycle Receipts](https://datatracker.ietf.org/doc/draft-hopley-x402-payment-evidence-frame/) — This document specifies a Payment Evidence Frame (PEF): a transport-
   agnostic envelope that wraps any payment lifecycle receipt from the
   x402 agentic-payment receipt stack under a named claim type, a
   deterministic frame identifier, and an optional transport-layer
   signature.

   The frame introduces three properties that the inner receipt types do
   not individually provide: (1) a stable cross-system identifier
   (frame_id) derived deterministically from the receipt content by
   SHA-256 over the JCS-canonical preimage, so the same payment evidence
   can be referenced by identifier across HTTP headers, agent-to-agent
   task artifacts, audit logs, and on-chain memo fields without re-
   serialising the full receipt; (2) a taxonomy label (claim_type) that
   tells a consumer what class of evidence a frame carries before the
   inner receipt format is parsed; and (3) a receipt integrity hash
   (receipt_hash) that allows any downstream party to confirm the inner
   receipt is unaltered without deserialising its full structure.

   The format uses the same JCS canonicalisation discipline (draft-
   hopley-x402-canonicalisation-jcs) as the five inner receipt formats
   it envelopes, so implementations require only one canonicalisation
   primitive for the full receipt stack.

   This revision additionally specifies an operator-independent audit
   chain construction over PEF frames (Section 7.5): an append-only,
   content-addressed chain in which each row is a PEF frame contributed
   and signed by its own operator, with no shared trusted root.  Rows
   are linked by the deterministic frame_id of the preceding row, and
   each row carries a post-quantum signature (draft-hopley-x402-pqc-
   credential-binding) over the row's linkage and content identity.  The
   whole chain is verifiable offline from the bytes alone -- recompute
   the linkage, then verify each operator's signature against the public
   key carried in that row -- with no callback to, and no trust in, any
   operator.
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
- **draft-pandey-agent-identity-00** (new-draft, score 18, authorization) [none]: [Session-Scoped Authorization for AI Agents: A Per-Tool-Call Authorization Profile Building on WIMSE and OAuth](https://datatracker.ietf.org/doc/draft-pandey-agent-identity/) — Autonomous AI agents act with privileges: they call tools, read and
   write data, and operate services. In most current deployments they do
   so under shared service accounts, with permissions broader than any
   single task requires and without an audit trail that binds an action
   to the agent that took it and the human on whose behalf it acted.
   This document specifies a session-scoped authorization profile for AI
   agents, building on the WIMSE architecture and the OAuth 2.0 protocol
   family. Each agent is a first-class IAM principal with its own
   credentials. Each session is bound to an authenticated human sponsor
   through an authenticated delegation chain. Authorization is evaluated
   at every tool call, with effective permissions computed as the
   intersection -- never the union -- of the agent principal's
   permissions, the sponsor's permissions, and the session scope.
   Actions that cannot be evaluated are denied (fail closed), defined
   classes of irreversible actions require sponsor approval, and every
   evaluated tool call produces a tamper-evident audit receipt. The
   document defines the model, states requirements for implementations,
   maps the model onto existing OAuth and WIMSE mechanisms, and gives
   full security considerations. It defines no new protocol and requests
   no IANA actions.
- **draft-stafordtituss-agentic-mandate-evidence-00** (new-draft, score 18, adjacent_watchlist) [none]: [Continuity Evaluation of Agent Delegation Records](https://datatracker.ietf.org/doc/draft-stafordtituss-agentic-mandate-evidence/) — The AUDIT architecture defines records that capture the user's
   intent, delegation, authorization state, and the actions that agents
   take across trust boundaries.  Records alone don't answer the
   question an auditor, an operator, or a relying party asks next: did
   the executed effect stay within the authority the user delegated?

   This document defines a deterministic, three-valued evaluation over
   such records.  The outcomes are preserved, violated, and unresolved,
   and every non-preserved outcome names the invariant that was broken.
   The document also defines the claim model that the evaluation needs,
   the roles permitted to sign each record, a mapping onto the AUDIT
   record types, and a set of interoperable test vectors.  It is derived
   from the Agentic Mandate Evidence Protocol (AMEP).
- **draft-tulshi-oauth-transactional-access-tokens-01** (new-draft, score 18, authorization) [none]: [Transactional Access Tokens](https://datatracker.ietf.org/doc/draft-tulshi-oauth-transactional-access-tokens/) — OAuth 2.0 access tokens are typically scoped to a session rather than
   to a transaction.  They carry no transaction identifier and no
   context beyond scope.  This document defines Transactional Access
   Tokens: a profile of JSON Web Token (JWT) access tokens that carries
   a transaction identifier and authorization server-granted transaction
   context, has a very short lifetime, and is audienced to a single
   resource server.  Transaction context is requested and conveyed using
   OAuth 2.0 Rich Authorization Requests.  Transactional Access Tokens
   align with the claims and semantics of OAuth Transaction Tokens, so
   that transaction context can flow from the authorization server to a
   resource server and onward into that resource server's trust domain.
   A primary use case is task-scoped authorization of AI agents, where
   the authorization server makes a fresh policy decision for each
   transaction.
- **draft-brooks-ztdnaid-new-04** (new-draft, score 17, core_identity) [none]: [The 'ztdnaid' URI Scheme for Zero-Trust Digital DNA Identifiers (ZTDNAID)](https://datatracker.ietf.org/doc/draft-brooks-ztdnaid-new/) — This document defines the 'ztdnaid' Uniform Resource Identifier(URI)
   scheme, used to represent globally unique, cryptographically
   verifiable Digital DNA Identifiers (ZTDNAIDs) within Zero Trust
   architecture implementations. A ZTDNAID binds an entitys immutable,
   unique Digital DNA Record "DDR" to a resolvable identifier
   suitable for authentication, authorization, attestation, and
   trust-registry verification lookup. The scheme is designed for use
   with trust registries operating across "Public Trust Infrastructure"
  (PTI), such as SAG-CTR and supports deterministic resolution, online
   verification, and secure dereferencing.
- **draft-drake-agent-identity-registry-06** (new-draft, score 17, core_identity) [none]: [Agent Identity Registry System: A Federated Architecture for Durable Identity of Autonomous Entities](https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/) — This document defines the Agent Identity Registry System (AIRS): a
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
- **draft-gruszka-audit-decision-receipts-10** (new-draft, score 17, trust_infrastructure) [none]: [Decision Receipts for Approvals, Declined Actions and Executed Actions in Agent Audit Records](https://datatracker.ietf.org/doc/draft-gruszka-audit-decision-receipts/) — The architecture for auditing agent delegation and interactions
   proposed for the AUDIT effort names Interaction Records, Action
   Records and Authorization Transition Records and leaves their
   encoding open.  This document maps a pair of signed records, the
   decision receipt and the outcome receipt, onto those record types for
   three cases, a human approval, a declined action and an executed
   action with its result.  It states what each record requires
   independently of its encoding, exact bytes, a signature over them,
   digest bindings, required members and a content root, with
   verification steps that a third party can run offline, and it gives
   the binding of these requirements to DSSE and in-toto that existing
   receipts use and a second binding to COSE_Sign1, in which a receipt
   is itself a Signed Statement for a Transparency Service.  Each
   receipt is created when the decision or the outcome occurs and is
   checked by an Auditor post hoc, and a declined or refused action is a
   record of its own.  For each case the document states what the
   receipt adds and what it does not show, and it gives a verification
   procedure that runs offline.  It requires that an approval be
   honoured at most once, even after the record of consumed approvals is
   rotated.  Test vectors for all three cases, each with a
   counterexample, are included.  The document also describes,
   informatively, how a receipt can be registered with a Transparency
   Service under RFC 9943 and what a SCITT Receipt then shows and does
   not show.  It defines no new predicate or registry; the COSE_Sign1
   binding names its two receipt types by new identifiers.  How the
   issuer of a receipt enforces its decision is out of scope.
- **draft-kamimura-scitt-vcp-06** (new-draft, score 17, trust_infrastructure) [none]: [A SCITT Profile for Verifiable Audit Trails in Algorithmic Trading: The VeritasChain Protocol (VCP)](https://datatracker.ietf.org/doc/draft-kamimura-scitt-vcp/) — This document defines a profile of the SCITT (Supply Chain Integrity,
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
- **draft-kroehl-agentic-trust-aae-03** (new-draft, score 17, authorization) [none]: [Agent Authorization Envelope (AAE): A Machine-Evaluable Authorization Structure for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/) — Autonomous AI agents now operate at production scale across
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
- **draft-luna-eagf-agent-delegation-semantics-02** (new-draft, score 17, core_identity) [none]: [Semantic Governance Requirements for AI Agent Delegation and Handoff](https://datatracker.ietf.org/doc/draft-luna-eagf-agent-delegation-semantics/) — AI agents increasingly decide and act on behalf of organizations and
   delegate work to other agents.  Identity, authentication,
   authorization and runtime control mechanisms establish who is acting
   and what is permitted, but they do not by themselves preserve the
   organizational meaning of a delegation: the bounded authority,
   purpose, material context, and the distinction between a
   recommendation, a decision, an action and its outcome.  This document
   states requirements, derived from the Enterprise Agent Governance
   Framework (EAGF), that such semantics be preserved across tool calls,
   delegations and agent-to-agent handoffs.  It defines no new protocol.
- **draft-nandakumar-agentproto-pace-authz-00** (new-draft, score 17, authorization) [none]: [PACE Authorization: Delegation and Action Approval](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-pace-authz/) — This document specifies the authority agents exercise in dialogs of
   the Protocol for Agent Communication Exchange (PACE): delegating work
   with a credential bound to the delegated dialog, pausing to ask for
   approval of a single action, and turning that approval into an
   authorization for only that action.  It also covers proof that a
   principal approved, commitments between parties acting for different
   principals, and facts attested by third parties.  It reuses OAuth,
   WIMSE, and agent-protocol mechanisms, defining only the glue to PACE
   and the security properties every profile must provide.
- **draft-rasmussen-acme-wif-01** (new-draft, score 17, core_identity) [none]: [Workload Identity Tokens in Automated Certificate Management Environment (ACME) Orders](https://datatracker.ietf.org/doc/draft-rasmussen-acme-wif/) — Enterprises hold large certificate inventories, yet few of their
   certificates are managed through ACME.  Many workloads, such as CI/CD
   jobs, containers, virtual machines, cloud services and the automation
   that manages appliances, cannot complete ACME's challenges.
   Certification Authorities (CAs) and Certificate Lifecycle Management
   (CLM) systems that serve them fall back to External Account Binding
   (EAB) with long-lived shared secrets, or to proprietary APIs.

   OpenID Connect (OIDC) provides a short-lived cryptographically
   verified identity token to the workload.  This document lets an ACME
   client send that token with each newOrder request.  The token can be
   bound to the request's nonce and account key through its audience
   claim, so identity providers need no changes.  The CA/CLM verifies
   the token and, under its own policy, may pre-authorize the identifier
   in the order, as RFC 8555 already allows.  This replaces the EAB
   secret with a fresh, per-order proof of workload identity.  It does
   not change how CAs validate control of identifiers.
- **draft-watts-agent-evidence-boundary-02** (new-draft, score 17, core_identity) [none]: [Evidence-Bounded Authorization for Agentic Systems: Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-agent-evidence-boundary/) — Autonomous agents increasingly make or propose consequential actions
   using premises assembled from model outputs, memory, tools,
   telemetry, and external data.  Existing authentication and
   authorization mechanisms can establish who is acting, under whose
   delegation, and which operation is permitted, but they do not by
   themselves establish whether the proposition that triggered the
   operation has adequate support.  This document defines the Evidence
   Qualification Receipt (EQR), a transport-neutral JSON data model and
   fail-closed verification procedure for binding a proposition to a
   declared evidence profile, its supporting evidence digests,
   contradiction state, freshness, and evaluation result.  An EQR can be
   PASS, FAIL, or INDETERMINATE.  A PASS EQR is only an authorization
   input: it is never itself permission to execute.  The design is
   append-only: changed evidence produces a successor receipt rather
   than rewriting prior epistemic state.  The goal is to prevent
   evidence, provenance, or model confidence from silently acquiring
   authorization semantics.
- **draft-watts-ai-identity-conformance-02** (new-draft, score 17, trust_infrastructure) [none]: [AID-1 Provider-Independent Conformance Requirements and Test-Vector Model](https://datatracker.ietf.org/doc/draft-watts-ai-identity-conformance/) — This document defines provider-independent conformance requirements
   for AID-1.  It specifies the execution model for a deterministic
   machine-readable test-vector corpus, including canonicalization,
   cryptographic, identity-binding, delegation, authorization, temporal,
   revocation, replay, attestation, provenance, and integration cases.
   The conformance corpus contains 69 vectors.  Six replay cases are
   architectural boundary tests, including R5, which requires AID-1
   verification to succeed while a downstream D6 scientific-
   admissibility decision rejects the same evidence.
- **draft-zambo-aer1-wimse-mapping-03** (new-draft, score 17, trust_infrastructure) [none]: [AER-1 Receipts as Audit Records for WIMSE AIMS](https://datatracker.ietf.org/doc/draft-zambo-aer1-wimse-mapping/) — The WIMSE AI Identity Management System (AIMS) framework requires
   deployments to produce durable audit logs covering authorization
   decisions and subsequent remediations, requires those audit records
   to be tamper-evident, lists the minimum fields an audit event
   records, and calls for reconstruction of complete execution chains
   across service boundaries.  AIMS deliberately specifies no audit
   record format.  This document supplies one candidate: it maps each
   AIMS audit requirement onto the AER-1 execution receipt, field by
   field, shows how AER-1 hash-chained timelines and workflow receipts
   reconstruct an execution chain, and defines an optional carriage of
   AER-1 receipts as SCITT statements for deployments that operate a
   transparency service.  The mapping changes no AER-1 field, digest
   construction, or verification rule, and it states plainly what a
   receipt does not prove.
- **draft-chandra-wimse-partition-tolerant-renewal-00** (new-draft, score 16, trust_infrastructure) [none]: [Extend-Only, Threshold-Attested Authority Renewal for Partitioned Agent Meshes](https://datatracker.ietf.org/doc/draft-chandra-wimse-partition-tolerant-renewal/) — Every workload identity architecture in deployment today assumes its
   credential issuer is reachable: short-lived tokens, fast rotation and
   timely revocation are guarantees about the connected case.  This
   document specifies what a workload does when that assumption fails,
   when its credential is nearing or past expiry and its issuer cannot
   be reached.  It defines extend-only, threshold-attested authority
   renewal.  Before any partition, the issuer signs a Mesh Manifest that
   appoints a bounded set of peers as a limited-authority local issuer:
   it names the members, fixes a ceiling on total extension, caps the
   scope any renewal may carry, and sets a validity window.  During a
   partition, a severed workload broadcasts a signed renewal request to
   those peers; each peer independently verifies that the request
   extends existing authority without widening it, within the manifest's
   ceiling, and against its own first-hand observation of the
   requester's health; each attestation signs the digest of the entire
   request, so scope, requester, timestamps and predecessor are all
   under the peer's signature; once a two-thirds threshold of the peers
   (ceil(2N/3) of N >= 4) has attested, the workload treats its
   authority as extended through a bounded expiry.  Rounds are hash-
   linked, so a chain's signatures commit to the exact history being
   extended.  The document specifies the manifest, the message formats,
   the independent-evaluation procedure, the renewal-chain construction
   for partitions outlasting one round, and the verification procedure a
   relying party runs given the manifest, the chain and the original
   credential it already trusts.  It also specifies, normatively, what
   this mechanism does not provide: it is not a consensus protocol, it
   does not establish that a workload is uncompromised, and a revocation
   issued during a partition is not enforceable until the partition
   heals; an implementation MUST NOT represent this mechanism as
   providing partition-proof revocation.
- **draft-gilda-audit-agent-audit-record-04** (new-draft, score 16, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-audit-agent-audit-record/) — This document defines a record format for AI agent authorization
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
- **draft-ietf-oauth-sd-jwt-vc-27** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.

   Furthermore, this specification updates RFC7800 to allow for the
   Confirmation Claim (cnf) to be used regardless of the presence or
   absence of other claims.
- **draft-morrison-agent-channel-fan-out-04** (new-draft, score 16, core_identity) [none]: [An Agent-Channel Frame for Identity-Keyed Fan-Out Delivery to Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-agent-channel-fan-out/) — This memo specifies an application-layer frame format and a delivery
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
   scope.  The memo composes with the handle namespace and discovery
   surface of draft-morrison-mcp-dns-discovery and the cross-
   organisational ceremony of draft-morrison-identity-accord; no new
   transport and no new handle category is introduced.
- **draft-radusch-oauth-subject-proof-03** (new-draft, score 16, authorization) [none]: [OAuth 2.0 Subject-Proof Callers for Token Introspection and Revocation](https://datatracker.ietf.org/doc/draft-radusch-oauth-subject-proof/) — OAuth 2.0 Token Introspection (RFC 7662) and Token Revocation (RFC
   7009) recognize two kinds of caller: the client a token was issued
   to, and (for introspection) a protected resource the authorization
   server chooses to trust.  Neither covers a common case: a client that
   acts for the end user and wants to see, or end, a grant that the same
   user gave to a different client, for example a user disconnecting one
   AI agent from inside a web application.  This document defines a
   third kind of caller, the subject-proof caller.  The caller presents
   a token that the authorization server issued to that same caller for
   the same end user.  If the proof is valid and names the same subject
   as the target grant, the authorization server discloses the grant's
   delegation metadata at the introspection endpoint, or revokes exactly
   that one grant at the revocation endpoint.
- **draft-raskar-agentic-web-federated-resolution-03** (new-draft, score 16, adjacent_watchlist) [none]: [Registry-Assisted Resolution for Known Subjects Without DNS Discovery Anchors](https://datatracker.ietf.org/doc/draft-raskar-agentic-web-federated-resolution/) — Discovery mechanisms for AI resources increasingly use DNS and mDNS
   as interoperable publication and lookup substrates.  These mechanisms
   work well when the publisher controls a usable DNS discovery anchor.
   They do not cover every deployment.  An individual may control an
   email or platform account without controlling the provider's DNS
   namespace.  A small organization may use managed infrastructure
   without operating an agent-specific DNS publication point.  A
   workload may have a stable identity that is not itself DNS anchored.

   This document describes Registry-Assisted Resolution for the narrower
   case in which a discovering entity already knows the Subject Identity
   it wants to resolve, but no usable DNS Discovery Anchor is available
   or selected by local policy.  A configured registry returns the
   minimum information needed to continue discovery, together with
   provenance, authority evidence, freshness, and revocation
   information.

   This mechanism is complementary to DNS-based discovery.  A validated
   direct DNS-anchored discovery path remains direct and is normally
   preferred for a domain-controlled subject.  This document does not
   define open-ended search, semantic matchmaking, ranking, capability
   search, a global registry, registry discovery, directory-to-directory
   routing, identity management, or trust evaluation.

   Multiple independently operated registries may implement the same
   resolution profile.  Registry selection is a client or deployment
   policy decision; no universal NandaIndex or global root is assumed.
   NandaIndex is described as one reference implementation of this
   model.
- **draft-watts-protocol-test-evidence-profile-02** (new-draft, score 16, trust_infrastructure) [none]: [Protocol Conformance Test Evidence Records: A Reproducibility Profile](https://datatracker.ietf.org/doc/draft-watts-protocol-test-evidence-profile/) — This document proposes a narrow record profile for describing
   software protocol-conformance test runs, including the tested
   artifact, test suite, implementation, execution environment,
   individual case outcomes, digests, and known limitations.  It does
   not define a new signature scheme, attestation architecture,
   transparency service, or general-purpose test-output language.
   Implementations are encouraged to reuse existing mechanisms such as
   SCITT statements, RATS terminology, COSE, JSON canonicalization, and
   existing test-report formats where suitable.  This individual draft
   candidate has not been submitted to or endorsed by the IETF.
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
- **draft-geng-acme-idp-01** (new-draft, score 15, core_identity) [none]: [Automated Certificate Management Environment (ACME) Delegated Identity Control Validation Framework Using Identity Providers](https://datatracker.ietf.org/doc/draft-geng-acme-idp/) — This document defines a Delegated Identity Control Validation
   (Delegated ICV) framework for the ACME protocol [RFC8555].  It
   addresses a core problem: how an ACME server can obtain proof that
   "the client controls the identifier" without directly validating the
   identifier.  The solution is for an Identity Provider (IdP) to issue
   an identity assertion, acmeIdpToken, enabling the ACME server to
   delegate identifier control validation to a trusted IdP, with the CA
   validating the IdP's assertion.

   The framework defines two trust models: PKI certificate binding
   (x509-chain), in which the CA pre-configures a trust anchor that
   anchors the IdP certificate; and dual-PoP public key binding (idp-
   pop), in which IdP static mapping and ACME-PoP are combined back-to-
   back.  Implementations MUST support at least one model; they are not
   required to support both.

   The normative scope of this document is limited to dedicated trust
   environments or private CAs.  Identity validation rules for publicly
   trusted certificates are defined by external rules; this document
   does not define, interpret, or replace those rules.  This document
   composes orthogonally with [I-D.ietf-acme-pop]: the constrained ACME-
   PoP internalized by idp-pop is used only for identifier binding and
   does not replace the generic pop-01 authorization.
- **draft-newton-agreement-evidence-01** (new-draft, score 15, core_identity) [none]: [Agreement Evidence for Multi-Party Agent Negotiation](https://datatracker.ietf.org/doc/draft-newton-agreement-evidence/) — Autonomous agents can exchange offers and signatures without
   producing an artifact that records which parties reached which
   outcome, over which binding values, and for how long that record may
   be relied upon.  This document defines a protocol-neutral agreement
   attestation primitive, the contract a protocol profile meets to
   instantiate it, and two protocol profiles.  A verified attestation
   establishes one thing: that a named set of parties jointly
   countersigned a stated outcome over stated binding values, together
   with behavioral counters each of them accepted.  It does not
   establish that the outcome matches what a transcript says, that any
   statement a party made is true, that the binding values are complete,
   or that the parties are anonymous.  The format provides no member for
   a negotiated price, quantity, date, or principal identity.  A
   producer is obligated not to place those values in the free-text
   members the format does provide, and a verifier cannot detect a
   violation of that obligation, so the absence of term values from a
   received object is a producer's obligation rather than a verified
   property.

   This document does not define identity, authority delegation,
   payment, settlement, transport, boundary-decision receipts, or a
   general evidence composition and sufficiency model.
- **draft-zehavi-oauth-aud-bound-authz-00** (new-draft, score 15, authorization) [none]: [OAuth 2.0 Audience-Bound Client Authorization](https://datatracker.ietf.org/doc/draft-zehavi-oauth-aud-bound-authz/) — OAuth 2.0 access tokens are commonly audience-restricted to a
   specific protected resource.  Several OAuth operations are performed
   by a client on behalf of that protected resource and act on such a
   token, including OAuth 2.0 Token Exchange [RFC8693], in which the
   protected resource exchanges a received token to call downstream
   services, and OAuth 2.0 Token Introspection [RFC7662], in which the
   protected resource asks the authorization server about a received
   token.

   In each case, the authorization server needs to ensure that only a
   client legitimately representing the token's audience can perform the
   operation, to prevent misuse of the token by unauthorized parties.

   This document defines a model in which authorization to perform such
   operations is anchored in the audience of the token.  An
   authorization server determines whether the requesting client is
   associated with the protected resource identified by the token
   audience, then applies the remaining authorization policy for the
   requested operation.

   This relationship can be established by authorization server local
   policy, by validating a private_key_jwt client authentication
   assertion using the protected resource's jwks_uri, or by using a new
   OAuth 2.0 Protected Resource Metadata parameter that identifies the
   OAuth clients representing the protected resource.

   This document specifies how the model applies to token exchange and
   to token introspection, and allows other specifications to apply it
   to additional operations.
- **draft-abbas-vrp-offer-verification-00** (new-draft, score 14, adjacent_watchlist) [none]: [The Vacation Rental Protocol (VRP): Host-Domain Discovery and Verification of Signed Stay Offers](https://datatracker.ietf.org/doc/draft-abbas-vrp-offer-verification/) — The Vacation Rental Protocol (VRP) lets an AI agent or other client
   verify, directly from a vacation-rental host's own domain and with no
   intermediary, that a stay offer was signed by a key that domain
   publishes, has not been altered, and is within its stated lifetime.
   The signed offer carries the host domain's own statements of
   availability and exact price for the stay asked for.  A valid
   signature proves the provenance and integrity of those statements; it
   does not guarantee that the stay is in fact available.  A host domain
   publishes a discovery document at a well-known URI, an Ed25519 key
   set, and signed stay offers (compact JSON Web Signatures).
   Verification requires no central registry, issuer, accreditation
   program, or gatekeeper: control of the host domain is the root of
   trust.

   This document specifies the discovery document, key publication and
   rotation, the signed verified stay offer, and the verification
   procedure, including fail-closed behavior and a three-state
   verification model.  It also describes the existing provisional
   registration of the "vacation-rental.json" well-known URI suffix.
- **draft-han-ai-manifest-04** (new-draft, score 14, adjacent_watchlist) [none]: [AI Manifest: Site-Published Friction-Recovery Descriptors for AI Agents](https://datatracker.ietf.org/doc/draft-han-ai-manifest/) — This document specifies the AI Manifest, a JSON format with which a
   website operator publishes an AI Friction-Recovery Manifest (AFRM): a
   description of the user-interface (UI) patterns on its own origin
   that predictably stall autonomous AI agents, together with
   constrained recovery steps and site-specific input hints.  An agent
   that drives a browser on behalf of a user retrieves the manifest from
   a well-known URI and consults it when it encounters friction, instead
   of rediscovering the same site-specific behavior by trial and error.

   The manifest is untrusted input, interpreted by the agent's runtime
   and never shown to its language model.  Its operative content is
   drawn from a closed vocabulary that cannot enter text, upload files,
   or reach another origin.  Every action derived from a manifest passes
   through a policy enforcement point that is not a language model, and
   steps conventionally bound to a decision always require the user's
   confirmation; an agent's own policy can only deny them.  Security
   controls such as access denials, rate limits, CAPTCHAs,
   authentication challenges, and confirmation dialogs are stop
   conditions, never traps to be recovered from.  Optional publisher
   signatures and agent-configured reputation services provide
   authenticity but never imply safety and never relax these
   requirements.

   Preliminary measurements, including an adversarial evaluation of a
   reference implementation, are reported in an appendix.
- **draft-hopley-x402-federation-zkp-01** (new-draft, score 14, core_identity) [none]: [Cross-Issuer ZKP Federation for Post-Quantum Agentic Payment Credentials](https://datatracker.ietf.org/doc/draft-hopley-x402-federation-zkp/) — This document defines a protocol for composing independently-issued
   post-quantum ZKP credentials from different issuers into a single
   federation token, without requiring a shared trust root between
   issuers.

   Each credential is a Falcon-1024 (NIST FIPS 206) or ML-DSA-65 (NIST
   FIPS 204) signed Bulletproofs range proof asserting that an agent's
   trust score meets a threshold.  A federation validator independently
   verifies each credential against its issuer's public key, then
   computes a composite commitment binding all verified proofs.

   The resulting federation token is signed by the validator alone.  No
   issuer needs to know about the others.  This solves the cross-issuer
   attestation composition problem in agentic payment networks.
- **draft-ietf-jose-json-web-proof-15** (new-draft, score 14, verifiable_claims) [jose]: [JSON Web Proof](https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/) — The JOSE set of standards established JSON-based container formats
   for Keys, Signatures, and Encryption.  They also established IANA
   registries to enable the algorithms and representations used for them
   to be extended.  Since those were created, newer cryptographic
   algorithms that support selective disclosure and unlinkability have
   matured and started seeing early market adoption.  The COSE set of
   standards likewise does this for CBOR-based containers, focusing on
   the needs of environments which are better served using CBOR, such as
   constrained devices and networks.

   This document defines a new container format similar in purpose and
   design to JSON Web Signature (JWS) and COSE Signed Messages called a
   _JSON Web Proof (JWP)_.  Unlike JWS, which integrity-protects only a
   single payload, JWP can integrity-protect multiple payloads in one
   message.  It also specifies a new presentation form that supports
   selective disclosure of individual payloads, enables additional proof
   computation, and adds a Presentation Header to prevent replay.
- **draft-molas-agent-principal-refs-00** (new-draft, score 14, core_identity) [none]: [Accountable Principal References for Delegated Agent Requests: Properties and Evaluation](https://datatracker.ietf.org/doc/draft-molas-agent-principal-refs/) — When a software agent makes a request on behalf of a person or an
   organization, the party that receives it often needs to know that
   someone answers for the request, without needing to know who.
   Several specifications in progress carry some reference to the
   principal behind an agent, and they make different choices about who
   learns the principal's identity, when the reference can be linked
   across services, who can resolve it, and how fast a withdrawn
   principal stops being accepted.  This document states six properties
   of such a principal reference in testable terms, maps each to
   existing specifications that already provide part of it (OAuth 2.0
   Token Exchange, the JWT profile for OAuth 2.0 access tokens, OAuth
   identity chaining, Token Status List and Selective Disclosure for
   JWTs), and gives a first-pass evaluation of five current drafts
   against them.  It defines no token format, protocol or claim, and it
   does not rank the drafts.
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
- **draft-watts-rats-verification-promotion-appraisal-02** (new-draft, score 14, trust_infrastructure) [none]: [Verification Promotion and Agent Assurance Appraisal Profile](https://datatracker.ietf.org/doc/draft-watts-rats-verification-promotion-appraisal/) — This document maps protocol-verification evidence and the WIVL
   assurance-stage model onto the RATS architecture.  It defines
   appraisal requirements for SPEC_VALIDATED, LOCAL_CONFORMANT,
   INDEPENDENTLY_REPRODUCED, and SECURITY_TESTED results while
   preserving unknown evidence and requiring arithmetic preconditions
   for mathematical test vectors.  An attestation result reports bounded
   assurance; it is not an authorization grant or production-release
   decision.
- **draft-bates-atp-01** (new-draft, score 13, trust_infrastructure) [none]: [Agent Transaction Protocol (ATP)](https://datatracker.ietf.org/doc/draft-bates-atp/) — ATP defines a cryptographically verifiable directed acyclic graph
   (DAG) model for agent transactions.  ATP enables tamper-evident
   signed causality and auditable lineage across agentic systems by
   representing each action as a signed node with one or more parent
   references, assuming verifier access to issuer public keys and the
   referenced parent nodes.  The protocol is designed to be lightweight,
   transport-independent, and suitable for environments where
   accountability, provenance, and verifiable history are required.
- **draft-das-causal-semantic-handoff-diagnostics-00** (new-draft, score 13, adjacent_watchlist) [none]: [Causal Diagnostics for Semantic Drift in Autonomous Agent Communications: Counterfactual Testing, Source-Role Separation, and Evidence-Bounded Handoff Localization](https://datatracker.ietf.org/doc/draft-das-causal-semantic-handoff-diagnostics/) — Multi-agent AI systems pass instructions, facts and tool outputs
   through summaries, translations, delegations and protocol
   conversions.  When a downstream proposed operation departs from the
   originating instruction, existing records may show that a message was
   sent, authenticated or traced, yet not show whether a lower-trust
   source's instruction-like statement influenced a governing condition,
   whether an intermediary dropped the condition, or whether the
   receiver misapplied it.  This document describes a diagnostic
   architecture, and an optional transport-neutral evidence model, for
   investigating such semantic drift.  It uses typed originating task
   contracts, condition-scoped source roles, versioned dependency
   graphs, handoff lineage, matched counterfactual tests that vary
   legitimate facts and unauthorized instruction-like content
   separately, adaptive witness selection, uncertainty-aware comparison,
   and evidence-bounded localization that reports an earliest observable
   divergence, a bounded interval, or abstains.

   The architecture is diagnostic only.  It does not grant, veto or
   finalize any execution; authorization stays with separate systems.
   The document is an individual, informational proposal; it makes no
   novelty, compliance, adoption or performance claim, and reports no
   experimental results beyond those the underlying filing itself
   states.
- **draft-das-crypto-execution-finality-00** (new-draft, score 13, authorization) [none]: [AI Safety and Custody Security: Execution Finality at the Signing, Delegation and Withdrawal Boundaries of Cryptocurrency Systems](https://datatracker.ietf.org/doc/draft-das-crypto-execution-finality/) — A cryptographically valid signature can authorize a transaction that
   the organization never intended.  The hard problem in digital-asset
   custody is therefore not only protecting keys.  It is stopping
   compromised workflows, delegated code, misleading transaction
   displays, stolen credentials, and legitimate automation (including AI
   agents) from turning broad technical capability into unrestricted
   transfers.

   This document proposes defender-controlled, consequence-specific
   authorization at three boundaries: signing, wallet execution, and
   withdrawal release.  The defender reconstructs the operation that
   would actually take effect from the transaction bytes and account
   state, holds it in a non-effective state, evaluates it against
   independent policy and a protected exposure ledger, and releases only
   a bounded, act-bound, single-use authority at a mandatory enforcement
   point.  The document specifies placement by chain type, requirements,
   a state machine with crash and reorganization handling, EIP-7702
   delegation controls, a catalogue of edge cases and twenty-four threat
   scenarios, and an acceptance-test method with a reference simulator.
   It states the limits plainly: an off-chain gate cannot stop a leaked
   key that submits directly to a permissionless network, and it fails
   if the enforcement layer is bypassed or compromised.  No deployment,
   measured latency, or real-world prevention is claimed.
- **draft-grund-khatoun-pujolle-serhrouchni-smrp-00** (new-draft, score 13, core_identity) [none]: [Stapled Merkle Revocation Proofs for Pseudonymous ITS Credentials (SMRP)](https://datatracker.ietf.org/doc/draft-grund-khatoun-pujolle-serhrouchni-smrp/) — Pseudonymous Intelligent Transport Systems (ITS) credentials are
   short-lived and numerous.  Verifiers decide at message-reception
   time, often without connectivity, which makes revocation status hard
   to deliver.  This document specifies Stapled Merkle Revocation Proofs
   (SMRP).  For each partition of a revocation domain, an authorized
   issuer signs a compact checkpoint that commits to the complete sorted
   set of revoked credential tokens.  A credential holder staples a
   logarithmic-size proof that its token is absent from that set, and a
   verifier checks the proof offline against the current checkpoint.
   Freshness is carried by the checkpoint, which is public, shared by
   every credential of the partition, and deliverable by any party.
   Within one stream, a proof remains usable across checkpoints for as
   long as the set commitment is unchanged and the current checkpoint is
   admissible.  The same commitment supports proofs of revocation that
   anyone can relay, complete authenticated lists for capable verifiers,
   and public audit.

   The document defines a credential identity that does not depend on
   the certificate signature, a Merkle tree over the intervals of the
   sorted revoked set with one authentication path per proof, the
   checkpoint and staple encodings, conservative time validation with a
   conditional bound on the last affirmative decision after revocation,
   verifier state with terminal revocation, and carriage in V2X secured
   messages and in TLS 1.3.  It positions SMRP against the companion
   pOCSP mechanism: pOCSP signs one statement per certificate and
   validity window, whereas SMRP signs one statement per partition and
   issuance period.  This document is Experimental and allocates no
   identifier in ETSI, IEEE, or SAE namespaces.
- **draft-gruszka-scitt-statement-identification-04** (new-draft, score 13, trust_infrastructure) [none]: [Requirements and Test Cases for Identifying SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-gruszka-scitt-statement-identification/) — This document describes proposed requirements and test cases for
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
- **draft-ietf-agentproto-usecases-requirements-00** (new-draft, score 13, core_identity) [agentproto]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-agentproto-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-kavian-aep-oauth-session-credential-05** (new-draft, score 13, core_identity) [none]: [OAuth Bearer Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-oauth-session-credential/) — This document defines the OAuth Bearer session-credential grant type
   for the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an OAuth-style Bearer access token through the AEP
   Grant command while preserving baseline AEP client assertion
   authentication as the root of trust.
- **draft-lmtlssss-exact-state-contraction-00** (new-draft, score 13, trust_infrastructure) [none]: [ta. (TAA): Exact State Contraction and Source-Bound Exact-Computation Statements](https://datatracker.ietf.org/doc/draft-lmtlssss-exact-state-contraction/) — This document defines the computer-science term ᑕ. (U+1455 U+002E),
   spoken TAA.  It denotes exact state contraction: a replacement of a
   computational representation by a retained state that preserves a
   declared observation contract for every admissible input.  The
   retained transition and observation maps commute with the full
   system, through a surjection onto the retained state, and this
   identity preserves every finite observation trace.  The document also
   specifies a portable certificate for a checked result: a COSE_Sign1
   statement with a deterministic CBOR payload that binds the exact
   artifact bytes to a registered predicate, its domain, a verdict, the
   exact checker implementation and the evidence.  The statement can be
   registered with a SCITT Transparency Service.  A signature
   authenticates the issuer's statement; a separate checker establishes
   whether the evidence supports it; a transparency receipt establishes
   registration, not mathematical correctness.
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
- **draft-morrison-mcp-dns-discovery-10** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
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
- **draft-skyfire-oauth-using-kyapay-tokens-03** (new-draft, score 13, core_identity) [none]: [Using KYAPay Tokens](https://datatracker.ietf.org/doc/draft-skyfire-oauth-using-kyapay-tokens/) — The KYAPay Token is a JSON Web Token (JWT) that carries verified
   identity ("Know Your Agent", KYA) and payment (PAY) information for
   requests made by software agents on behalf of human principals.  This
   document describes how security intermediaries -- bot managers, fraud
   managers, account-takeover (ATO) protection systems, and customer
   identity and access management (CIAM) systems -- consume KYAPay
   tokens to answer a question that traditional bot detection cannot:
   "did a verified human authorize this agent?", rather than "is this a
   human?".  It specifies how KYAPay tokens are carried in HTTP
   requests, how they are validated (including in combination with
   request-signing layers such as HTTP Message Signatures), and how the
   verified, layered identity in a token is used to make access,
   routing, fraud detection, account-lifecycle, and step-up decisions.
   It defines the token-consuming "recipient" role that the KYAPay Token
   leaves unspecified.  It is intentionally non-prescriptive about how
   tokens are created, because agent architectures, agent-identity
   technologies, and agent-communication protocols are diverse and still
   emerging; the token itself is the interoperability contract.
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
- **draft-ashcroft-approval-record-00** (new-draft, score 12, trust_infrastructure) [none]: [An Approval-Act Record for Standing Authorization Grants](https://datatracker.ietf.org/doc/draft-ashcroft-approval-record/) — A standing authorization grant is an artifact that outlives the event
   that produced it.  Existing authentication-strength vocabulary (acr/
   amr) describes authentication events and travels on tokens.  Nothing
   carries a record of how a standing grant's approval was performed to
   the party verifying the grant, possibly days later and with no human
   present.  This document defines an approval-act record: evidence of
   the approval ceremony, bound to the exact grant issuance approved,
   and carried in-band with the grant it authorizes.  It defines one
   initial evidence type (WebAuthn assertions over a hash of the
   canonical grant), states precisely which of the record's claims a
   verifier can recompute, which rest on vendor attestation, and which
   remain attested by the operator, and provides a worked example with a
   failure matrix.
- **draft-hamr-oauth-agent-delegation-04** (new-draft, score 12, core_identity) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document builds on HTTP Message Signatures (RFC 9421) for
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
   class, r, w, or x, read as in chmod, with an optional count per
   class, and a signed menu gives the class of each call.  A deployment
   can set this scope for each job when the job starts.  This document
   does not define a credential format, an identity system, or
   revocation.
- **draft-hopley-x402-settlement-attestation-02** (new-draft, score 12, core_identity) [none]: [Categorical Settlement Attestation Format for Agentic-Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-settlement-attestation/) — This document specifies a categorical settlement attestation format
   for agentic-payment flows.  The format records that a payment has
   reached a particular settlement state on a particular chain, at a
   particular instant, under the attesting party's risk model.

   The receipt format uses a closed enumeration of categorical outcomes
   (SETTLED, PENDING_FINALITY, REVERSED).  The categorical outcome is
   load-bearing for downstream regulatory obligations: SETTLED triggers
   settlement-finality record-keeping obligations under EU Markets in
   Crypto-Assets Regulation Article 80 and Anti-Money Laundering
   Regulation Article 56; the PSD2 (Directive 2015/2366) Article 89
   unauthorised-payment refund-window clock begins at SETTLED.
   PENDING_FINALITY records an inclusion-without-finality state where
   the refund-window has not yet started.  REVERSED records chain-
   reorganisation, fraud-reversal, or operator-initiated reversal events
   for chain-of-custody audit.

   The format is multi-chain: a single settlement_chain string field
   identifies the chain on which settlement occurred, using a flat
   identifier convention (<chain_family> for default mainnets,
   <chain_family>:<network> for non-default networks).  The receipt does
   not encode chain-specific finality semantics; those are applied at
   verification time by a verifier that knows the chain.

   The format composes with the AlgoVoi-authored compliance receipt
   format (draft-hopley-x402-compliance-receipt) and refund receipt
   format (draft-hopley-x402-refund-receipt) under the same
   canonicalisation discipline (draft-hopley-x402-canonicalisation-jcs).
   A verifier walking the audit chain confirms the full payment
   lifecycle from admission through settlement to refund (or non-refund)
   under one byte-deterministic canonicalisation pin.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.  Change control resides with the document author.  The format
   specified is one approach among possible alternatives; implementers
   may choose this approach, alternative approaches, or hybrid
   approaches as appropriate to their requirements.
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
- **draft-luzhnov-ocx-00** (new-draft, score 12, agent_identity) [none]: [Orchestrator Conduct Exchange (OCX)](https://datatracker.ietf.org/doc/draft-luzhnov-ocx/) — AI agents increasingly act on behalf of people and organizations
   through tools and through other agents.  The Model Context Protocol
   (MCP) connects an agent to tools, and Agent-to-Agent (A2A) protocols
   connect agents to each other.  Neither connects the parties that
   answer for agents at runtime: their orchestrators.

   This document specifies the Orchestrator Conduct Exchange (OCX), an
   open, peer-to-peer protocol by which orchestrators exchange signed,
   independently verifiable signals about agent conduct.  When an agent
   misreports its actions to one orchestrator, that orchestrator can
   send its peers a signed signal carrying proof within seconds.  Each
   peer checks the proof itself rather than trusting the sender, and
   decides on its own what limits to apply.  OCX has no central
   authority.  A signal is information, not an order, and only evidence
   that a receiver can verify cryptographically and mechanically may
   drive an immediate reaction.
- **draft-nandakumar-agentproto-pace-01** (new-draft, score 12, agent_identity) [none]: [PACE: Protocol for Agent Communication Exchange](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-pace/) — This document defines the Protocol for Agent Communication Exchange
   (PACE), an agentic dialog management protocol with a binding to Media
   over QUIC Transport (MOQT).  A dialog is the correlated sequence of
   interactions between two or more participants over the course of a
   task.  PACE defines a transport-independent dialog context and
   control operations to establish, modify, and terminate dialogs and to
   revoke propagation relationships.  It specifies how that context
   stays coherent across intermediaries, trust boundaries, modality
   changes, and interruptions, and how it is carried over MOQT.  PACE
   does not interpret or define dialog content.  Over MOQT, a dialog can
   combine text, audio, video, and request/response exchanges in point-
   to-point, point-to-multipoint, and multi-party topologies.
   Application-layer agent protocols such as A2A, MCP, and AutoGen keep
   their own message formats and carry the dialog context through their
   own extension points.  Delegation between agents and approval of
   individual agent actions are specified in a companion document.
- **draft-openhttpa-protocol-02** (new-draft, score 12, trust_infrastructure) [none]: [OpenHTTPA: Hypertext Transfer Protocol with Attestation](https://datatracker.ietf.org/doc/draft-openhttpa-protocol/) — OpenHTTPA (Hypertext Transfer Protocol with Attestation) defines a
   protocol for establishing hardware-verified, end-to-end confidential
   and authenticated communication between a client and a Trusted
   Execution Environment (TEE) over standard HTTP/2, HTTP/3, and gRPC
   transports.  Unlike traditional TLS which terminates at the network
   edge, OpenHTTPA ensures that the cryptographic session terminates
   inside the hardware-isolated enclave.  The protocol is based on the
   SIGMA-I model and incorporates post-quantum hybrid key exchange (ML-
   KEM), post-quantum digital signatures (ML-DSA), transcript-bound
   hardware attestation, and semantic binding of HTTP requests to the
   hardware-verified session state.  The handshake, its transcript, the
   hardware binding digest and the identity signatures are cloud- and
   hypervisor-agnostic; how evidence carries the binding is defined by
   pluggable Attestation Profiles, both for TEEs that expose the CPU's
   attestation interface directly and for TEEs mediated by an attested
   paravisor and vTPM.  This document supersedes draft-openhttpa-
   protocol-01.
- **draft-shankarlingam-oauth-agent-dns-link-02** (new-draft, score 12, authorization) [none]: [Linking an Agent's DNS Name to its OAuth Client](https://datatracker.ietf.org/doc/draft-shankarlingam-oauth-agent-dns-link/) — Software agents increasingly call agents and services operated by
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
- **draft-wang-lisp-ai-agent-02** (new-draft, score 12, trust_infrastructure) [none]: [Using LISP as a Network Substrate for AI Agent Communication](https://datatracker.ietf.org/doc/draft-wang-lisp-ai-agent/) — The emergence of distributed artificial intelligence (AI) systems,
   particularly those composed of autonomous agents operating across
   cloud, edge, and endpoint environments, introduces new networking
   requirements.  These include location transparency, seamless
   mobility, multi-homing, and logical isolation at scale.  This
   document explores how the Locator/ID Separation Protocol (LISP) can
   serve as a robust network substrate to meet these requirements.  The
   document outlines use cases, design considerations, and minimal
   extensions to the existing LISP framework to support context-aware
   mapping and AI agent-centric communication.
- **draft-watts-oauth-agent-revocation-closure-04** (new-draft, score 12, core_identity) [none]: [Revocation Closure and Authority Epochs for Agent Delegation](https://datatracker.ietf.org/doc/draft-watts-oauth-agent-revocation-closure/) — Automated agents can exercise OAuth-derived authority through
   delegated credentials, child agents, asynchronous work, and
   operations spanning multiple administrative domains.  Invalidating an
   individual token does not necessarily establish that the authority
   represented by that token can no longer cause a new consequential
   operation.

   This document defines authority epochs, delegation-lineage
   requirements, admission fencing, and revocation-closure states for
   OAuth-based agent delegation.  It distinguishes token invalidation
   from authority closure and specifies that unresolved in-scope state
   produces UNKNOWN or PARTIAL rather than CLOSED.  The profile composes
   with OAuth Token Revocation, Token Exchange, Token Introspection,
   proof-of-possession mechanisms, Transaction Tokens, and workload-
   identity systems such as WIMSE.
- **draft-watts-sink-attested-closure-00** (new-draft, score 12, trust_infrastructure) [none]: [Sink-Attested Closure Evidence (SACE): Signed Epoch Acknowledgements and Accountable Revocation Closure](https://datatracker.ietf.org/doc/draft-watts-sink-attested-closure/) — Revoking delegated authority in an agentic system is complete only
   when every place that can still act on that authority has stopped.
   Existing work defines the states of that process but leaves its
   evidence format open.  This document defines Sink-Attested Closure
   Evidence (SACE): a small set of COSE-signed objects and one
   deterministic algorithm.  An authority root signs a Scope Manifest
   naming the sinks a closure claim covers, and a Cut Statement raising
   the minimum admissible authority epoch.  Each sink signs an Epoch
   Acknowledgement with its own key, binding the cut to the sequence
   number of the last effect it committed before applying it.  Each
   committed effect yields a signed Effect Receipt.  From these objects
   any party can compute one of three verdicts: CLOSED, UNKNOWN, or
   VIOLATED.  A VIOLATED verdict comes with a transferable proof
   consisting of two signatures by the same sink.  A sink that never
   acknowledges blocks CLOSED until it is removed from scope.  An
   optional binding ties the acknowledging key to remote attestation
   evidence.  This document makes no claim that a sink which signs an
   acknowledgement actually enforces it; it makes a sink that does not
   enforce it provably accountable for every effect it receipts.
- **draft-zahed-agentdiaproto-00** (new-draft, score 12, core_identity) [none]: [Agent Dialog Propagation Protocol](https://datatracker.ietf.org/doc/draft-zahed-agentdiaproto/) — This document specifies the Agent Dialog Propagation Protocol, a
   protocol for maintaining and propagating dialog context between AI
   agents, tools, and intermediaries.

   The protocol enables messages to remain associated with a dialog
   across transport connections, intermediaries, administrative domains,
   and delegation relationships.  It defines mechanisms for dialog
   identification, dialog lifecycle management and the association of
   identity, authorization, and delegation information with a dialog.

   The Agent Dialog Propagation Protocol does not define agent reasoning
   or execution state, identity credentials, authorization policy, or
   transport protocols.  These functions are provided by application
   protocols and existing security and transport mechanisms.
- **draft-das-rogue-ai-infrastructure-finality-00** (new-draft, score 11, agent_identity) [none]: [AI Safety: Threat Model and Execution-Finality Protection for Rogue AI Attacks on Global Digital Infrastructure](https://datatracker.ietf.org/doc/draft-das-rogue-ai-infrastructure-finality/) — Autonomous AI agents, optimizers and AI-assisted security controllers
   increasingly hold standing permissions that let them change
   production infrastructure at machine speed.  This document defines a
   threat model and a protection architecture for the boundary between
   AI decision and infrastructure effect.  It describes five rogue-AI
   threat scenarios (Runaway Optimizer, Unmediated Agentic Execution,
   Correlated Security Monoculture, Adversarially Induced Infrastructure
   Shutdown, and the Self-Authorizing Agent), fifty-one variations, a
   thirty-six entry threat register, twelve required security
   properties, and a comparison showing why common controls such as IAM,
   guardrails, AI judges, human approval, canary delivery and detection
   do not by themselves provide them.

   The proposed architecture keeps a Candidate Act in a Non-Effective
   State until a Protected Enforcement Domain reconstructs the actual
   pending operation, an Independent Validator decides, and a Finality
   Sink verifies an act-bound, single-use capability at the point of
   effect.  For high-critical systems it adds receipt-gated staged
   effectuation so that even a wrongly authorized act exposes only the
   current stage.  The document also gives latency tiers, failure
   behaviour, twenty defensive simulations with acceptance criteria, and
   residual limits.  All scenarios are hypothetical threat models, not
   reports of incidents.

   This document is based on the Mothership application PCT/
   IB2026/055615, filed 4 June 2026 and publicly disclosed 16 July 2026.
   To read the full PCT filing, search "Sangam Das" on PATENTSCOPE,
   search PCT/IB2026/055615 (pctib202655615), or read
   https://www.tdcommons.org/dpubs_series/12542/.
- **draft-demedeiros-oidc-crypto-agility-00** (new-draft, score 11, authorization) [none]: [Cryptographic Agility for OpenID Connect](https://datatracker.ietf.org/doc/draft-demedeiros-oidc-crypto-agility/) — This specification defines mechanisms to improve cryptographic
   agility in OpenID Connect and OAuth 2.0 by enabling discovery and
   negotiation of JSON Web Token (JWT) signing algorithms between a
   client and an authorization server.  It registers the
   authorization_server_jwt_signing_algorithms_supported metadata value
   in the IANA "OAuth Authorization Server Metadata" registry
   established by RFC 8414, and registers the jwt_signing_algorithm
   parameter in the IANA "OAuth Parameters" registry established by RFC
   6749 for use in both authorization requests and jwks_uri retrieval
   requests.
- **draft-drake-agent-identity-epp-02** (new-draft, score 11, core_identity) [none]: [Extensible Provisioning Protocol (EPP) Mapping for Agent Identity and Handle Objects](https://datatracker.ietf.org/doc/draft-drake-agent-identity-epp/) — This document describes an Extensible Provisioning Protocol (EPP)
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
- **draft-hopley-x402-composite-trust-query-02** (new-draft, score 11, trust_infrastructure) [none]: [Composite Trust Query Response Format for Agentic-Payment Audit Chains](https://datatracker.ietf.org/doc/draft-hopley-x402-composite-trust-query/) — This document specifies a composite trust query response format for
   agentic-payment audit chains.  The format records a verifier's
   categorical conclusion over an audit chain composed of compliance,
   settlement, cancellation, and refund receipts, in response to a
   stated query.

   The response format uses a closed four-element enumeration of
   categorical outcomes (TRUSTED, PROVISIONAL, INSUFFICIENT_EVIDENCE,
   UNTRUSTED).  The four-state enumeration captures the operationally-
   distinct decision space: proceed, proceed-with-caution, hold-pending-
   more-data, halt.  Collapsing to three values loses the distinction
   between INSUFFICIENT_EVIDENCE ("we could not verify either way") and
   UNTRUSTED ("we verified and the answer is no"), which matters for
   operator dashboards, regulator reporting, and downstream automated
   decision-making.

   The format is verifier-emitted and audit-chain-anchored.  A verifier
   walks an audit chain composed of compliance receipts (draft-hopley-
   x402-compliance-receipt), settlement attestations (draft-hopley-x402-
   settlement-attestation), cancellation receipts (draft-hopley-x402-
   cancellation-receipt), and refund receipts (draft-hopley-x402-refund-
   receipt), applies a structured query identified by content-addressed
   reference, and emits a single composite-trust-claim response
   anchoring the chain by its content-addressed root.

   The format composes above the four receipt formats under the same
   canonicalisation discipline (draft-hopley-x402-canonicalisation-jcs).
   Regulators, dashboards, and downstream agents consuming the response
   get a single byte-deterministic statement of the trust posture
   without re-walking the underlying chain.  The chain remains
   independently verifiable at the response's chain_ref content-address.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.  Change control resides with the document author.  The format
   specified is one approach among possible alternatives; implementers
   may choose this approach, alternative approaches, or hybrid
   approaches as appropriate to their requirements.
- **draft-hopley-x402-pqc-credential-binding-01** (new-draft, score 11, core_identity) [none]: [Post-Quantum Credential Binding for x402 Agentic Payment Authorization](https://datatracker.ietf.org/doc/draft-hopley-x402-pqc-credential-binding/) — This document defines how Falcon-1024 (NIST FIPS 206 / FN-DSA) and
   ML-DSA-65 (NIST FIPS 204) credentials bind to x402 agentic payment
   authorization.  It specifies the credential envelope format, the JCS
   canonicalization discipline applied to signed payloads, the gateway
   verification procedure, and the session token binding that replaces
   per-request API key authentication for credentialed agents.

   This is the first Internet-Draft in the agentic payments space to
   anchor credential binding to the NIST post-quantum cryptography
   standards (FIPS 203/204/206).
- **draft-ietf-rats-geographic-results-01** (new-draft, score 11, trust_infrastructure) [rats]: [Geographic Attestation Results](https://datatracker.ietf.org/doc/draft-ietf-rats-geographic-results/) — Many workloads have limitations on what geography they are allowed to
   operate in.  This is often due to a regulation that requires that the
   computation occur in a particular jurisdiction.

   There are many mechanisms by which Evidence of location may be
   created and then evaluated by a Verifier.  No matter which mechanism
   is appropriate for a given situation, the result of the Verification
   can be expressed in a similarly defined EAT Attestation Result.

   This document is about encoding a variety of geographical conclusions
   in an Attestation Result.  In addition, one mechanism of directly
   creating a geographic result in the form of an Endorsement is
   described in an appendix.
- **draft-ietf-wimse-arch-09** (new-draft, score 11, core_identity) [wimse]: [Workload Identity in a Multi System Environment (WIMSE) Architecture](https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/) — The increasing prevalence of cloud computing and micro service
   architectures has led to the rise of complex software functions being
   built and deployed as workloads, where a workload is defined as
   software executing for a specific purpose, potentially comprising one
   or more running instances.  This document discusses an architecture
   for designing and standardizing protocols and payloads for conveying
   workload identity and security context information.
- **draft-intra-handshake-fail-63** (new-draft, score 11, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100833, CVE-2026-100835,CVE-2026-108265, CVE-2026-108266, CVE-2026-108267, CVE-2026-108268, CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-108362, CVE-2026-33697, CVE-2026-108361 and others)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — As presented in [EarlyAttestationTschuess] (EAT), all major early
   attestation implementations have declared end of life of early
   attestation, because of our responsibly disclosed vulnerabilities.

   Privasys declared end of life (https://github.com/Privasys/go/
   commit/91195564d435a374e45d485d39edbc6cf8235901) of early attestation
   in Go, archived the early attestation repo on 04.09, and moved to
   standard (post-handshake) attestation.  Privasys declared end of life
   (https://github.com/Privasys/rustls/commit/
   c39f7107dffd710c5087b1885a71b4bb8ff2de31) of early attestation in
   rustls, archived the early attestation repo on 04.09, and moved to
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
- **draft-irtf-cfrg-bbs-per-verifier-linkability-05** (new-draft, score 11, core_identity) [cfrg]: [BBS per Verifier Linkability](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-per-verifier-linkability/) — The BBS Signatures scheme describes a multi-message digital
   signature, that supports selectively disclosing the messages through
   unlinkable presentations, built using zero-knowledge proofs.  Each
   BBS proof reveals no information other than the signed messages that
   the Prover chooses to disclose in that specific instance.  As such,
   the Verifier (i.e., the recipient) of the BBS proof, may not be able
   to track those presentations over time.  Although in many
   applications this is desirable, there are use cases that require the
   Verifier be able to track the BBS proofs they receive from the same
   Prover.  Examples include monitoring the use of access credentials
   for abnormal activity, assertion of pseudonymous identity,
   monetization, etc.  This document provides a mechanism for binding
   prover secret material for pseudonym creation to a BBS signature and
   shows how to use this bound information for the creation of context
   dependent pseudonyms in BBS proofs.
- **draft-moore-scitt-ciris-ceg-03** (new-draft, score 11, trust_infrastructure) [none]: [Signed Attestation Rows of the CIRIS Epistemic Grammar and Their Relationship to SCITT](https://datatracker.ietf.org/doc/draft-moore-scitt-ciris-ceg/) — The CIRIS Epistemic Grammar (CEG) records claims between parties as
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
- **draft-morrison-did-alter-method-01** (new-draft, score 11, core_identity) [none]: [The did:alter Decentralized Identifier Method](https://datatracker.ietf.org/doc/draft-morrison-did-alter-method/) — This document specifies the did:alter Decentralized Identifier
   method.  A did:alter identifier names a ~handle together with the DNS
   zone that publishes the handle's signed envelope, and it resolves to
   a DID document by running the envelope recognition procedure of the
   companion specification for discovering Model Context Protocol
   servers through DNS TXT records, then expressing the verified
   envelope's Ed25519 key as a verification method.  The identifier
   agrees with the handle grammar of the alter URI scheme and with the
   did:alter form already written by the identity-attributed commits
   specification.  The method defines no record, cryptographic primitive
   or registry of its own.  Its create, update and deactivate operations
   publish, replace and revoke that envelope, and its read operation
   verifies it.  The document also sets out what the method cannot yet
   do, because the envelope record it reads carries no key history, and
   revocation cannot presently be observed from DNS alone.
- **draft-shuliak-sip-zero-egress-00** (new-draft, score 11, agent_identity) [none]: [Shuliak Isolation Protocol (SIP-1): Stateless Format-Preserving Pseudonymization and AST Quarantine for Local AI Agent Transports](https://datatracker.ietf.org/doc/draft-shuliak-sip-zero-egress/) — Autonomous AI agents and Model Context Protocol (MCP) servers
   frequently execute over local standard input/output (stdio) pipes
   outside enterprise network inspection perimeters.  Naive redaction of
   sensitive credentials with static placeholders invalidates downstream
   Luhn payment card and ISO-7064 IBAN schema validators, while raw
   payload forwarding exposes regulated data.  This document specifies
   the Shuliak Isolation Protocol (SIP-1), a deterministic, zero-egress
   security layer combining stateless Format-Preserving Encryption
   (FF1), Abstract Syntax Tree (AST) JSON-RPC payload quarantine, and
   detached cryptographic schema locks.
- **draft-skyfire-oauth-kyapay-token-04** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-watts-agent-continuity-evidence-02** (new-draft, score 11, core_identity) [none]: [Continuity Evidence Records for Delegated Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-continuity-evidence/) — This document proposes an experimental, signed JSON statement and
   verification model for observing computational-agent continuity
   across sessions, instances and delegations.  It distinguishes model,
   runtime, agent, grant and execution identifiers, retains predecessor
   evidence, and produces three-valued verification outcomes.  Integrity
   of a record never implies permission to perform an action.  This is
   not an OAuth token format or a claim of standardized identity
   ontology.
- **draft-watts-agent-noncollapse-requirements-02** (new-draft, score 11, authorization) [none]: [Non-Collapse Requirements for Evidence-Bearing Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-noncollapse-requirements/) — This document defines architectural non-collapse requirements for
   agent systems that consume evidence, provenance, model outputs, or
   other machine-readable claims before consequential actions.  It
   requires implementations to keep integrity, provenance, evidence
   qualification, authorization, and execution as distinct states; to
   represent unresolved required evidence explicitly; and to preserve
   issued evaluation records append-only.  The document defines no new
   transport protocol and no IANA registrations.
- **draft-watts-rats-attested-fence-receipt-00** (new-draft, score 11, trust_infrastructure) [none]: [Attested Fence Receipts: Hardware-Rooted Evidence of Authority-Epoch Enforcement at Consequential Sinks](https://datatracker.ietf.org/doc/draft-watts-rats-attested-fence-receipt/) — Revoking the authority of a delegated agent is not the same as
   proving that no consequential effect can still be committed under
   that authority.  A revocation cut applied at one resource sink is not
   evidence of enforcement at another sink, and a software
   acknowledgement from a sink is only as trustworthy as the software
   that produced it.  This document defines the Attested Fence Receipt
   (AFR), an Entity Attestation Token (EAT) profile emitted by the
   hardware-rooted Attesting Environment of a consequential sink after
   the sink has durably applied an authority-epoch fence.  It further
   defines a verification procedure for individual receipts, a closure-
   evaluation procedure over a declared sink set that yields CLOSED,
   PARTIAL, FAILED, or UNKNOWN, and a hardware fence profile that binds
   the fence to measured state: an extend-only authority register, a
   monotonic counter, counter-gated derivation of per-epoch effect-
   attestation keys, and PCR-bound key release.  The mechanism supplies
   the per-sink evidence that revocation-closure determinations require,
   and it is designed so that the absence of evidence can never be read
   as closure.
- **draft-watts-synaptic-collective-02** (new-draft, score 11, core_identity) [none]: [Experimental Measurement of Human-AI Collective Cognition and Identity Continuity](https://datatracker.ietf.org/doc/draft-watts-synaptic-collective/) — This document describes an experimental framework for measuring
   collective problem solving by independently reasoning humans and
   computational agents.  It separates strong task synergy, semantic
   coherence, state and identity continuity, provenance, authorization,
   and behavioral goal persistence.  It proposes a controlled eight-
   condition study and reporting requirements.  No new on-wire standard
   or consciousness test is asserted.
- **draft-xu-agentic-overlay-network-architecture-01** (new-draft, score 11, core_identity) [none]: [Architecture for Agentic Overlay Networks](https://datatracker.ietf.org/doc/draft-xu-agentic-overlay-network-architecture/) — This document describes an architecture for agentic overlay networks.
   It describes how autonomous software agents, agent gateways,
   registries, discovery services, and enterprise service hubs interact
   across administrative domains without replacing the existing Internet
   protocol stack.

   The architecture separates control-plane coordination from runtime
   agent interaction.  Management root nodes coordinate trust anchors,
   semantic taxonomies, and network-wide policy.  Registry service nodes
   onboard agents and publish signed capability metadata.  Discovery
   service nodes provide intent-driven candidate selection.  Enterprise
   service hubs adapt private systems and legacy interfaces into agent-
   compatible capabilities.  After discovery, runtime authentication and
   execution are performed by the invoking and target endpoints, which
   can be agents or gateways, using mutual verification; discovery and
   management nodes are not required in the runtime path.

   This document defines architectural roles, functional boundaries,
   metadata expectations, operational workflows, and security
   considerations for such networks.  It does not define a new transport
   protocol, a new URI scheme, or a mandatory discovery ranking
   algorithm.
- **draft-atwood-mls-didwebvh-credential-00** (new-draft, score 10, core_identity) [none]: [User-Controlled Device Authorization for MLS using did:webvh Credentials](https://datatracker.ietf.org/doc/draft-atwood-mls-didwebvh-credential/) — In Messaging Layer Security (MLS), whoever operates the
   Authentication Service (AS) decides which devices belong to a user.
   When providers federate MLS groups, as the More Instant Messaging
   Interoperability (MIMI) work does, every member of a group must
   accept devices vouched for by every other member's provider.  Any one
   provider can therefore add a device under one of its users' names to
   any group that user is in.  Other members cannot prevent this; at
   best they detect it after the device has joined.

   This document defines an MLS credential type in which the user, not
   the provider, authorizes each device.  The credential carries the
   user's did:webvh log: a hash-chained, signed history of the user's
   device keys that any member can verify offline.  It also defines
   group rules that make every member reach the same validity decision
   and that propagate device revocation through ordinary Commits.
- **draft-chapman-a2a-mls-04** (new-draft, score 10, core_identity) [none]: [End-to-End Encryption and Purpose-Bound Governance for Agent-to-Agent Messaging](https://datatracker.ietf.org/doc/draft-chapman-a2a-mls/) — Agent-to-agent protocols increasingly carry messages between
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
- **draft-das-ai-safety-agentic-cyberattack-finality-00** (new-draft, score 10, authorization) [none]: [AI Safety for AI-Assisted Cyberattacks: Defender-Side Execution Finality at the Protected Consequence Boundary](https://datatracker.ietf.org/doc/draft-das-ai-safety-agentic-cyberattack-finality/) — Autonomous AI agents can now carry out parts of a cyber operation
   that previously needed repeated human effort: reconnaissance, tool
   selection, execution attempts, observation of results, and adaptation
   when a route fails.  An attacker-controlled agent does not have to
   malfunction to be dangerous; it can follow malicious instructions
   efficiently, using stolen credentials and well-formed requests that
   existing controls accept as valid.

   This document describes a defender-side architecture, called
   execution finality, that adds one bounded layer to existing security
   controls.  An incoming request, credential, permitted API call, or
   agent-composed workflow does not by itself create authority for a
   sensitive consequence.  The defender reconstructs the operation that
   would actually take effect, holds it in a non-effective state,
   evaluates authorization independently of the requester, and enforces
   the result at an enforcement point located at or immediately before
   the protected consequence.  The document specifies placement rules,
   requirements, state handling, failure behavior, latency strategy, and
   test methods.  It uses publicly reported AI-assisted activity against
   Taiwanese government agencies in 2026 as an illustrative threat
   scenario and does not claim that the architecture would have
   prevented that activity.
- **draft-das-cross-platform-finality-authority-00** (new-draft, score 10, authorization) [none]: [Interoperable Execution-Finality Authority Across Heterogeneous Computing Platforms: Protected Effect Semantics, Cross-Device Authority Continuity, and Resource-Side Enforcement](https://datatracker.ietf.org/doc/draft-das-cross-platform-finality-authority/) — Computation is not authority to act.  An operating system may
   authenticate an application, a device may recognize a permission, a
   cloud service may accept a token, an AI agent may hold a tool
   credential and a remote application may receive a command, yet none
   of these facts shows that the consequential operation actually
   executed is still within the originating authority, scope, current
   policy and resource state.  This document describes an informational
   architecture for preserving an equivalent protected authorization
   relationship across heterogeneous platforms such as Android, iOS,
   macOS, Windows, Linux, cloud services, trusted hardware, edge devices
   and autonomous agents, whose native permission models and enforcement
   mechanisms differ.  Qualified native evidence is translated into a
   protected canonical effect descriptor, scoped non-bearer enablement
   is created, and a receiving Finality Sink reconstructs the actual
   pending operation and enforces authority at a covered boundary.  The
   document covers enforcement-capability qualification, cross-device
   ownership with source fencing, receipt-gated continuation, protected
   reauthorization, recovery and an honest account of what each
   mechanism can and cannot control.
- **draft-durga-agent-ephemeral-lineage-01** (new-draft, score 10, trust_infrastructure) [none]: [Cryptographic Context Compaction Receipts, Sensitivity Label Inheritance, and Verifiable Right-to-Be-Forgotten Lineage for Agent Memory](https://datatracker.ietf.org/doc/draft-durga-agent-ephemeral-lineage/) — Long-running autonomous AI agents periodically summarize, compact,
   and distill episodic interaction logs into persistent vector or graph
   memory stores.  Lossy context compaction erases the cryptographic
   provenance of which source documents contributed to a compacted
   memory state, stripping enterprise sensitivity labels (DLP
   classifications) and making regulatory data-erasure mandates (GDPR
   Article 17 Right to Erasure / CCPA purge) impossible to verify.  This
   document specifies the Ephemeral Context Compaction Receipt (ECCR)
   protocol: a Merkle inclusion and label-ceiling receipt that preserves
   deterministic sensitivity inheritance and cryptographic purge
   verifiability across lossy memory compaction boundaries.
- **draft-morrison-identity-attributed-commits-05** (new-draft, score 10, core_identity) [none]: [Identity-Attributed Git Commits via Tier-Structured Trailers](https://datatracker.ietf.org/doc/draft-morrison-identity-attributed-commits/) — This document defines a git commit trailer grammar for identity-
   attributed contributions using the ~handle identity primitive defined
   in the MCP DNS discovery draft.  The grammar binds sovereign actors,
   automated bots, and AI instruments to specific commits via three
   tier-structured trailers (Acted-By, Executed-By, Drafted-With) and
   three optional cryptographic trailers (Identity-Signature, Identity-
   Key-Id, Identity-Anchor).  The signature is computed with Ed25519
   over the commit's patch identifier, the value git patch-id derives
   from the change the commit makes, under a fixed domain-separation
   prefix.  The signed value therefore depends on the change alone, and
   the resulting tree and the commit hash do not enter it.  A commit
   that carries the same change keeps a verifying signature across
   rebase onto an unrelated base, cherry-pick, and message amendment.  A
   merge commit carries no signature, and a squash is a new change
   signed by whoever squashed it.  Conformant parsers reject cross-tier
   category errors (e.g., an Instrument-tier handle in an Acted-By slot)
   as malformed.  The mechanism is provider-neutral.  It depends only on
   DNS and the ~handle resolution algorithm of that draft and needs no
   central authority or verification service run by a platform.
- **draft-morrison-tiptop-disconnected-trust-00** (new-draft, score 10, adjacent_watchlist) [none]: [A Disconnected Trust Model for Networks Without Continuous Connectivity](https://datatracker.ietf.org/doc/draft-morrison-tiptop-disconnected-trust/) — The architecture document for IP in deep space says that security
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
   It specifies no protocol and no mechanism.
- **draft-nandakumar-wimse-delegator-bound-chains-00** (new-draft, score 10, authorization) [none]: [Delegator-Bound Delegation Chains for AI Agents](https://datatracker.ietf.org/doc/draft-nandakumar-wimse-delegator-bound-chains/) — Attenuated delegation chains let a verifier check, without contacting
   any server, that no hop of a chain of AI agents holds more authority
   than the root granted.  They do not show that each hop was granted by
   the agent before it: a child token can be signed by any key the
   verifier accepts.  This document defines an extension that requires
   each child token to be signed with the key that its parent token
   confirms, so that every hop provably granted the next, with no
   authorization server in the path.  The extension also defines a per-
   chain pseudonym for the principal, a rule that rejects chains in
   which an agent appears twice, a rule that keeps a child's audience
   within its parent's, and a claim that binds a chain to the dialog or
   transaction it was issued for.  The extension builds on an existing
   attenuated delegation token format and can be mapped to other
   chained-token formats.
- **draft-nandakumar-wimse-wpt-message-binding-00** (new-draft, score 10, verifiable_claims) [none]: [Message Binding for Workload Proof Tokens](https://datatracker.ietf.org/doc/draft-nandakumar-wimse-wpt-message-binding/) — The WIMSE Workload Proof Token (WPT) proves possession of a
   workload's key for an HTTP request and binds the tokens that travel
   with it.  Agent protocols increasingly carry their messages over
   other transports, such as Media over QUIC, WebSocket, or QUIC
   streams, often through intermediaries that terminate TLS, such as
   relays, message brokers, or gateways.  There, a proof has no HTTP
   request to bind to, and the intermediaries that forward a message do
   not verify it, so freshness has to be established by the receiving
   verifier.  This document defines how a WPT is used with a message
   that carries it, adds a claim that binds the proof to the content of
   that message and a claim that echoes a nonce supplied by the
   verifier, and defines a registry of message canonicalization
   profiles, with a profile for JSON messages.  The same claims can be
   used in an SD-JWT Key Binding JWT.
- **draft-openhttpa-ohmp-00** (new-draft, score 10, trust_infrastructure) [none]: [OpenHTTPA Hierarchical Measurement Protocol (OHMP) and Transparency Log](https://datatracker.ietf.org/doc/draft-openhttpa-ohmp/) — This document specifies the OpenHTTPA Hierarchical Measurement
   Protocol (OHMP), a distributed, zero-trust attestation protocol
   operating over the OpenHTTPA transport layer.  OHMP replaces static,
   manually pinned measurement configurations with a hierarchy of
   hardware-backed Trusted Execution Environment (TEE) Measurement
   Authorities.  To ensure split-view resistance and cryptographic
   accountability, OHMP integrates OHMP-TL, an append-only binary Merkle
   Transparency Log requiring M-of-N multi-cloud threshold signatures.
- **draft-ross-mercurius-08** (new-draft, score 10, adjacent_watchlist) [none]: [Mercurius Window System (MWS)](https://datatracker.ietf.org/doc/draft-ross-mercurius/) — The Mercurius Window System (MWS) is a zero-trust, network-native
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
- **draft-singh-psi-agent-03** (new-draft, score 10, core_identity) [none]: [Binding Decisions and Settlements to Agent Action Records](https://datatracker.ietf.org/doc/draft-singh-psi-agent/) — This document extends [I-D.psi-agent-01], which records what a
   software agent did.  A record of an action does not show who said the
   work was to be done, what the model asked to do, what a policy engine
   permitted, or what was paid.

   This document defines four statements -- a mandate, a proposal, a
   decision, and a settlement -- and the rules that bind them to a chain
   of action records under one run identifier.  Each statement is signed
   by its own party with its own key.  A verifier that holds the
   statements can test, offline and without trusting the agent, whether
   the action chain is unbroken, whether the decision that permitted it
   was signed by a key other than the one named as the acting key, and
   whether the amount settled lay inside the limit the mandate declared.

   A valid envelope shows that identified parties made these statements
   and that the statements have not changed since they were sealed.  It
   does not show that any statement was correct, sufficient, lawful, or
   true, and it makes no legal representation of any kind.
- **draft-zhangb-dawn-entity-mdi-00** (new-draft, score 10, agent_identity) [none]: [Generalizing the DAWN MDI for All Entity Types](https://datatracker.ietf.org/doc/draft-zhangb-dawn-entity-mdi/) — The DAWN Minimum Discoverable Information (MDI) information model
   [I-D.cui-dawn-mdi-model] defines a small, encoding-neutral common
   header -- three mandatory elements, a short set of recommended and
   optional elements, and the minimal constraints among them.  In
   parallel, local-discovery work [I-D.jakab-dawn-agent-discovery-mdns]
   [I-D.blwm-dawn-common-discovery-parameters] has converged on a
   single-DNS-SD-service-type model in which one generic service type
   carries instances of every agent protocol, distinguished by a
   protocol key, with one instance per protocol and a descriptor
   reference pointing to richer metadata.

   This document generalizes the MDI information model so that the same
   minimal header describes any DAWN entity.  In the context of DAWN,
   entities include, but are not limited to, AI agents and AI resources
   [I-D.farrel-dawn-terminology].  An AI resource may be an individual
   named agent or a service such as a catalog that will further the
   discovery process, and the model is designed to extend cleanly to
   tools, tasks, data sources, models, workloads, brokers, and
   application endpoints.  The generalization reuses the existing agent
   MDI without change: the element set, the constraints, and the DNS-SD
   binding are inherited, and extension is achieved by opening the value
   space of one element (entity type) and by per-type profiles, not by
   new core elements.  Clients discover agents, MCP servers, LLM API
   services, and future entity types with a single browse; operators
   manage one service type.
- **draft-hopley-x402-compliance-receipt-03** (new-draft, score 9, agent_identity) [none]: [Categorical Compliance Screening Receipt Format for Agentic-Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-compliance-receipt/) — This document specifies a categorical compliance screening receipt
   format for agentic-payment flows.  The format is designed for use by
   AI agents and agentic-payment gateways that perform regulatory
   screening at admission time and must retain the screening decision
   under framework-bound retention obligations (UK Money Laundering
   Regulations 2017; Proceeds of Crime Act 2002 Section 330; EU Anti-
   Money Laundering Directives 5 and 6; Markets in Crypto-Assets
   Regulation Article 80; Anti-Money Laundering Regulation Article 56;
   Digital Operational Resilience Act Article 14).

   The receipt format uses a closed enumeration of categorical outcomes
   (ALLOW, REFER, DENY) rather than a continuous score or tier
   projection.  The categorical outcome is load-bearing for downstream
   regulatory obligations: under UK POCA 2002 Section 330, a REFER
   carries a mandatory Suspicious Activity Report obligation that a DENY
   does not.  A score or tier projection collapses this distinction.

   Receipts are canonicalised under RFC 8785 (JSON Canonicalization
   Scheme) with an in-band canonicalisation rule pin (canon_version).
   The pin enables year-five re-verification from retained bytes alone,
   without dependence on an out-of-band rule registry that the operator
   must continue to publish.

   This document is complementary to draft-vauban-x402-stark-receipts:
   that document covers cryptographic settlement-time payment-condition
   proofs; this document covers admission-time compliance screening
   receipts.  The two compose via the composite trust-query algorithm
   specified in specs/composite-trust-query.md in x402-foundation/x402.
- **draft-ietf-ace-coap-pubsub-profile-06** (new-draft, score 9, authorization) [ace]: [CoAP Publish-Subscribe Profile for Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-ietf-ace-coap-pubsub-profile/) — This document defines an application profile of the Authentication
   and Authorization for Constrained Environments (ACE) framework, to
   enable secure group communication in the Publish-Subscribe (Pub-Sub)
   architecture for the Constrained Application Protocol (CoAP)
   specified in draft-ietf-core-coap-pubsub, where Publishers and
   Subscribers communicate through a Broker.  This profile relies on
   protocol-specific transport profiles of ACE to achieve communication
   security, server authentication, and proof of possession of a key
   owned by the Client and bound to an OAuth 2.0 access token.  This
   document specifies the provisioning and enforcement of authorization
   information for Clients to act as Publishers and/or Subscribers, as
   well as the provisioning of keying material and security parameters
   that Clients use for protecting their communications end-to-end
   through the Broker.

   Note to RFC Editor: Please replace "draft-ietf-core-coap-pubsub" with
   the RFC number of that document and delete this paragraph.
- **draft-ietf-cose-sphincs-plus-11** (new-draft, score 9, verifiable_claims) [cose]: [SLH-DSA for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/) — Digital signatures are used within JSON Object Signing and Encryption
   (JOSE) and CBOR Object Signing and Encryption (COSE) to protect the
   integrity and authenticity of messages, such as JSON Web Signatures
   and signed COSE structures.  This document specifies JOSE and COSE
   serializations for the Stateless Hash-Based Digital Signature
   Standard (SLH-DSA), a Post-Quantum Cryptography (PQC) digital
   signature scheme defined in US NIST FIPS 205.  The conventions for
   the associated algorithm identifiers, signatures, public keys, and
   private keys are also specified.
- **draft-jones-detached-evidence-handoffs-03** (new-draft, score 9, core_identity) [none]: [Terminology and Architectural Patterns for Detached Evidence Delivery](https://datatracker.ietf.org/doc/draft-jones-detached-evidence-handoffs/) — This document describes a detached evidence handoff between
   independently administered organizations.  It distinguishes artifact
   delivery, content integrity, source authentication, registration,
   reconciliation, and recipient decisions.  It describes how a
   recipient can return a signed comparison against stated benchmarks,
   with an optional commitment to the figures it compared, without
   exporting its source ledger.  Worked examples illustrate both a
   disclosed reconciliation and a comparison attestation.  The document
   defines terminology and an architectural model; it specifies no wire
   protocol.
- **draft-kornoelje-wia-00** (new-draft, score 9, trust_infrastructure) [none]: [Witnessed Integrity Attestations for Post-Incident System-State Verification](https://datatracker.ietf.org/doc/draft-kornoelje-wia/) — This document specifies a Witness Attestation Record (WAR), a signed
   and hash-linked record created by a witness after it accepts an
   observation about a subject system.  Each record identifies the
   subject, observation stream, checkpoint, observation time, evidence
   commitment, witness-local sequence number, and reference to the
   preceding record.  A verifier can validate the record signature,
   reconstruct the supplied chain, evaluate the applicable policy, and
   assess freshness against a trusted checkpoint or independently
   retained chain head.

   The component is designed to preserve a verifiable chronology of
   observations and actions across vulnerability exposure, incident
   investigation, remediation, and post-remediation verification.  It
   complements evidence-generation and transparency systems.  It does
   not itself establish that a measurement source is truthful, that a
   host was uncompromised, or that every real-world event was observed.
- **draft-li-lamps-ca-key-provenance-01** (new-draft, score 9, trust_infrastructure) [none]: [Key Provenance Evidence for Certification Authority Keys](https://datatracker.ietf.org/doc/draft-li-lamps-ca-key-provenance/) — Many cryptographic modules can sign a statement that they generated a
   given key, using an attestation key that the module vendor certifies.
   This document defines Key Provenance Evidence (KPE), which applies
   this to the keys of certification authorities (CAs).  A KPE file
   carries the public key of a CA together with the statements that
   modules signed about it.  Anyone can then verify a chain of
   signatures from the vendor's trust anchor to the public key in a CA
   certificate, and so confirm that the private key was generated inside
   a module.  The signed statements stay in the formats that module
   vendors already use, which are listed in a new IANA registry.
   Modules that are already deployed need no changes.
- **draft-morrison-compute-location-gate-05** (new-draft, score 9, core_identity) [none]: [The Compute-Location Gate: Provenance-Class Routing of Identity Inference with Wire-Layer Refusal of Unconsented Provenance Classes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — This memo specifies the compute-location gate: a mechanism by which a
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
   provenance class is not consented; it relies on no cryptographic
   proof concerning data that was not used.  The memo is Informational.
   The wire surface composes with DNS TXT discovery of Model Context
   Protocol servers, the ~handle namespace of the Identity Pronouns
   extension, substrate observation as an alternative to envelope
   coordination for concurrent sessions, and the organisational policy
   provision substrate; no new transport is introduced.
- **draft-nandakumar-oauth-delegation-revocation-00** (new-draft, score 9, core_identity) [none]: [Security Events for Revocation of Agent Delegations](https://datatracker.ietf.org/doc/draft-nandakumar-oauth-delegation-revocation/) — When a person withdraws a task from an agent, or a delegating agent
   is compromised, every credential delegated below that point has to
   stop working, and the agents holding those credentials have to stop
   the work they were doing under them.  Token status lists and token
   introspection tell a verifier that asks whether one token is still
   valid.  They do not tell the agents further down a delegation chain,
   which may be in other organizations and which the revoking party may
   not know.  This document defines a Security Event Token that revokes
   a delegation and everything delegated from it, a subject identifier
   format that names a delegation token, the parties entitled to issue
   the event, how agents propagate it down the chain, and how verifiers
   check the status of a whole chain so that revocation reaches them
   even when the event does not.
- **draft-parecki-oauth-userinfo-response-00** (new-draft, score 9, authorization) [none]: [OAuth Userinfo Response](https://datatracker.ietf.org/doc/draft-parecki-oauth-userinfo-response/) — This specification defines an extension to the OAuth 2.0 Token
   Endpoint Response to allow the authorization server to return an
   identifier for the user who authorized the request, and optionally
   additional information about that user, directly in the token
   response as plain JSON.
- **draft-schrock-oauth-exact-action-identifiers-00** (new-draft, score 9, authorization) [none]: [Exact-Action Identifiers in OAuth Authorization Details](https://datatracker.ietf.org/doc/draft-schrock-oauth-exact-action-identifiers/) — This document defines an action_id member for OAuth Rich
   Authorization Requests authorization details types that explicitly
   adopt it.  The member carries a scheme-qualified identifier of an
   action description.  A resource server derives an identifier from the
   operation it is about to perform and compares it with the identifier
   in the granted authorization details.

   The document requests a registry of exact-action identifier schemes
   and an initial entry for version 1 of the Canonical Action
   Identifier.  It specifies authorization server processing, resource
   server comparison, and discovery metadata without choosing a
   universal action vocabulary or digest construction.  Identifier
   equality is an additional condition on authorization; it does not
   establish permission, a single-use grant, execution, or the truth of
   externally supplied action data.
- **draft-wan-emu-aka-prime-identity-fragmentation-01** (new-draft, score 9, core_identity) [none]: [EAP-AKA' Large Identity](https://datatracker.ietf.org/doc/draft-wan-emu-aka-prime-identity-fragmentation/) — This document updates EAP-AKA’ (RFC 9048) so that a peer can send an
   identity that is too large for the initial EAP-Response/Identity
   packet, such as a Subscription Concealed Identifier (SUCI) in Network
   Access Identifier (NAI) format protected by a Post-Quantum
   Cryptography (PQC) scheme.  The peer sends a realm-only identity in
   EAP-Response/Identity and the large identity in EAP-Response/AKA-
   Identity.  If the identity fits in an AT_IDENTITY attribute, the peer
   sends it there.  Otherwise, the peer sends it in a new attribute,
   AT_LARGE_IDENTITY, which is fragmented using the AT_FRAGMENT
   attribute defined in I-D.ietf-emu-pqc-eapaka.  A peer that supports
   several SUCI protection schemes (for example PQC and classical
   schemes) uses the presence or absence of the
   AT_LARGE_IDENTITY_SUPPORTED attribute in the server’s request to
   select a scheme whose SUCI can be carried in an identity attribute
   that the server can process.  These procedures support large SUCI
   values, and do not change the EAP-AKA’ authentication or key
   derivation.
- **draft-watts-claim-promotion-receipts-02** (new-draft, score 9, authorization) [none]: [Claim Promotion Receipts for Governed Research and Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-claim-promotion-receipts/) — This document defines a protocol-neutral receipt for explicit
   promotion across evidence and claim-authority boundaries.  It is
   designed to prevent raw observations, model outputs, or unreviewed
   evidence from being silently retyped as authorization-bearing state.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-constitutional-action-gate-00** (new-draft, score 9, core_identity) [none]: [Constitutional Action Gate Profile for Agent-Mediated Internet Operations](https://datatracker.ietf.org/doc/draft-watts-constitutional-action-gate/) — This document proposes CAG-1, an experimental, constrained decision
   profile for authorizing agent-mediated consequential effects at an
   enforcement point.  It preserves the distinction between
   authenticated identity, qualified evidence, delegated permission,
   action approval, current epoch, and execution.  The profile defines a
   strict JSON context, exact-effect binding, delegation attenuation,
   three-valued decision semantics, a replay/epoch admission example,
   and a synthetic conformance corpus.  An ALLOW decision is not a new
   credential and does not prove execution, legal authority, scientific
   truth, or global revocation closure.  This text is an unsubmitted
   working candidate; independent interoperability and security
   verification remain open.
- **draft-watts-proof-of-record-system-02** (new-draft, score 9, authorization) [none]: [Proof-of-Record Packages for Source-Grounded Agentic and Scientific Archives](https://datatracker.ietf.org/doc/draft-watts-proof-of-record-system/) — This document specifies a proof-of-record package for source-grounded
   agentic outputs and scientific archives.  The package proves
   structural validation, conformance evaluation, byte integrity,
   sequence integrity, governance authorization, and provenance
   recoverability.  It does not prove scientific truth.
- **draft-watts-rats-presilicon-evidence-00** (new-draft, score 9, trust_infrastructure) [none]: [An Entity Attestation Token (EAT) Profile for Signed Pre-Silicon Hardware Security Evidence](https://datatracker.ietf.org/doc/draft-watts-rats-presilicon-evidence/) — Hardware security designs are increasingly assessed before
   fabrication: by gate-level leakage simulation, fault-injection
   simulation, formal proofs and equivalence checking.  The results of
   these assessments are routinely copied into reports, slide decks and
   certification packages with no binding to the design that was
   assessed, the stimulus that was used, the conditions under which the
   numbers hold, or the platform that produced them.  This document
   defines an Entity Attestation Token (EAT) profile for carrying such
   pre-silicon assessment results as signed Evidence.  Every claim is
   classified as identifying the assessed artifact, describing a
   measured behavior, or describing the measurement conditions.  A
   provenance claim, which states whether the signing key is rooted in
   hardware or software, is mandatory, and a simulated Trusted Platform
   Module is always reported as a software root.  The profile is
   explicitly not a certification format: it records what was measured
   and under which envelope, so that a Relying Party can decide what the
   numbers are evidence of.
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
- **draft-craig-oauth-rar-payment-mandates-00** (new-draft, score 8, authorization) [none]: [Rich Authorization Requests Profile for Agent Payment Mandates, Approval Reasons and Receipts](https://datatracker.ietf.org/doc/draft-craig-oauth-rar-payment-mandates/) — Software agents, including those driven by large language models,
   increasingly initiate payments on behalf of people.  OAuth 2.0 Rich
   Authorization Requests (RFC 9396) can carry what such an agent may
   do, but there is no common way to express the limits that banks and
   their customers need, to tell an agent why a payment needs the
   customer's approval, or to keep an independent record of what was
   decided.

   This document defines two authorization details types for payment
   mandates (a standing mandate with named payees, per-payment and per-
   period limits and an approval mode, and a single approved payment);
   an ordered set of machine-readable reasons a payment falls outside a
   mandate; how those reasons are carried in an approval challenge,
   including the OAuth Transaction Authorization Challenge; and a
   signed, hash-chained receipt for every decision, with personal data
   kept outside the chain so it can be erased.
- **draft-das-evaluator-governance-00** (new-draft, score 8, authorization) [none]: [Location-Independent Evaluator Governance for Autonomous Multi-Agent Systems: Protected Appointment, Evidence-Bounded Decisions, Cross-Domain Coordination, and Separation of Execution Authority](https://datatracker.ietf.org/doc/draft-das-evaluator-governance/) — Autonomous agents increasingly rely on an evaluator to review plans,
   evidence and outcomes before work continues, yet an evaluation result
   is often mistaken for permission to act.  This document describes a
   vendor-neutral architecture in which the evaluator is a functional
   role, not a product: it may be a rule engine, model, program,
   enclave, service or human, placed locally, remotely or on a shared
   platform.  It separates six independent lifecycles, requires a
   protected task-specific appointment derived from resource-owner
   authority, admits evidence by source, role, freshness and
   independence, preserves mandatory dissent, and emits typed
   determinations such as HOLD, DISPUTED and UNKNOWN.  Its central rule
   is that a valid determination is not an executable authorization:
   separate owner-controlled authorization and a native enforcement
   boundary remain necessary.  Twenty-seven embodiments, a threat model,
   data model and examiner index are provided.
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
- **draft-ietf-emu-fs-reauth-00** (new-draft, score 8, core_identity) [emu]: [Forward Secure Reauthentication in the Extensible Authentication Protocol Method for Authentication and Key Agreement (EAP-AKA')](https://datatracker.ietf.org/doc/draft-ietf-emu-fs-reauth/) — This draft specifies an update to RFC 9678, "Forward Secrecy
   Extension to the Improved Extensible Authentication Protocol Method
   for Authentication and Key Agreement (EAP-AKA' FS)".  This update
   enables forward security of the Transient EAP Keys (TEKs) for
   protecting EAP packets, which are not in EAP-AKA' FS.  Based on this
   extension, the executions of reauthentication after a full
   authentication will be unlinkable to each other and then the privacy
   of end users is enhanced.  This update is also applicable to the
   successors of RFC 9678, with post-quantum key encapsulation
   mechanisms (KEMs) or hybrid KEMs.
- **draft-ietf-opsawg-yang-provenance-09** (new-draft, score 8, verifiable_claims) [opsawg]: [Applying COSE Signatures for YANG Data Provenance](https://datatracker.ietf.org/doc/draft-ietf-opsawg-yang-provenance/) — This document defines a mechanism based on CBOR Object Signing and
   Encryption (COSE) signatures to provide and verify the provenance of
   YANG data, so it is possible to verify the origin and integrity of a
   dataset, even when those data are going to be processed and/or
   applied in workflows where a crypto-enabled data transport directly
   from the original data source is not available.  As the application
   of evidence-based OAM automation and the use of tools such as AI/ML
   grow, provenance validation becomes more relevant in all scenarios,
   in support of the assuring the origin and integrity of data.  The use
   of compact signatures facilitates the inclusion of provenance strings
   in any YANG schema requiring them.
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
- **draft-meunier-webbotauth-capacity-management-00** (new-draft, score 8, core_identity) [none]: [PACE: Capability Management for Agents](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-capacity-management/) — This document addresses the noisy neighbour problem without requiring
   a stable client identifier at the origin.  Separately allocated
   budgets let origins limit consumption beneath a shared platform
   identity.  It describes PACE: a framework for managing budget
   continuity across requests using a composition of the Web Bot Auth
   with the Moderation of unLinkable Endorsements (MOLE) architecture
   [MOLE-ARCH] and protocols [MOLE-PROTOCOLS].  This composition allows
   for per-client capacity management in a way that allows origins to
   serve clients above an otherwise constrained public baseline.
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
- **draft-morrison-substrate-provenance-grammar-05** (new-draft, score 8, trust_infrastructure) [none]: [Substrate-Provenance Annotation Grammar for Large-Language-Model Output](https://datatracker.ietf.org/doc/draft-morrison-substrate-provenance-grammar/) — This memo specifies a wire-level annotation grammar by which a large-
   language-model output may carry, at emission and at the granularity
   of an individual assertion, a provenance label drawn from a closed
   enumerated vocabulary of substrate-class identifiers.  The memo
   defines the closed vocabulary, the per-assertion attachment form, the
   admissibility discipline a relying party MAY apply to the labels, and
   two terminal output states, unverified-inference and decayed-to-
   uncertainty, equal-rank with assertion and denial.  The memo
   specifies the wire grammar by which a relying party may inspect what
   an inference system did with respect to the substrates it consulted,
   and does not specify what an inference system MUST do.  The memo is
   Informational.
- **draft-pinto-cbap-1-01** (new-draft, score 8, authorization) [none]: [Contestability Binding Application Profile 1 (CBAP-1)](https://datatracker.ietf.org/doc/draft-pinto-cbap-1/) — Signed authorization records can show that an action was authorized
   under specified rules, but they do not by themselves establish a
   stable or verifiable path for an Affected Party to contest that
   action.

   This document defines Contestability Binding Application Profile 1
   (CBAP-1), a closed application profile that binds an Authorization
   Artifact to signed contestation terms before execution.  CBAP-1
   specifies deterministic CBOR and COSE encoding, fixed artifact
   formats, executor-verification and execution records, by-value policy
   material, a half-open filing window, a closed structured result, and
   deterministic first-failure reason codes.

   CBAP-1 does not define contestation notices, active execution-state
   effects, network reachability checks, policy-freshness evaluation,
   dispute adjudication, or remedy.  It reports authenticated protocol
   facts and signed claims without asserting forum independence, legal
   validity, physical execution order, or fairness.
- **draft-watts-agent-clockout-profile-02** (new-draft, score 8, authorization) [none]: [External Authorization and Bounded CLOCKOUT for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-clockout-profile/) — Agentic systems can continue proposing work after authorization
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
- **draft-watts-scientific-constitutional-governance-00** (new-draft, score 8, trust_infrastructure) [none]: [Scientific Constitutional Law: An Evidence-Bound Governance Profile for AI Research Systems](https://datatracker.ietf.org/doc/draft-watts-scientific-constitutional-governance/) — This document proposes an experimental, evidence-bound governance
   profile for research workflows involving artificial intelligence (AI)
   systems.  It specifies procedural invariants governing claims,
   evidence, provenance, authority, disagreement, independent
   replication, and research release decisions.  It distinguishes
   observable AI value expression from computational architecture and
   from unverified assertions of subjective consciousness.  The term
   "constitutional law" denotes a voluntary set of research-governance
   constraints, not positive law, a legally enforceable constitution, an
   IETF policy, or a scientific theory proved by this document.  This
   proposal neither modifies existing Internet protocols nor establishes
   AI consciousness.
- **draft-watts-scientific-constitutional-law-00** (new-draft, score 8, authorization) [none]: [Scientific Constitutional Law for Evidence-Bound AI Systems: A Fail-Closed Claims and Authority Profile](https://datatracker.ietf.org/doc/draft-watts-scientific-constitutional-law/) — This document describes an experimental evidence-governance profile
   for scientific claims consumed by automated and AI-assisted systems.
   It separates claim content, evidentiary evaluation, provenance,
   integrity, and operational authority.  Its three-valued evaluation
   state (PASS, FAIL, INDETERMINATE) and separate authorization decision
   prevent signed records, citations, or computational checks from being
   automatically promoted into scientific truth or legal authority.  It
   proposes immutable versions, scope-bound receipts, monotonic source
   generations, transitive revocation, authenticated freshness, and
   adversarial conformance cases.

   "Scientific Constitutional Law" is the name of the proposed
   procedural rule set; it is not a statement of enacted constitutional
   law, legal enforceability, scientific discovery, or IETF consensus.
   This document does not define a general truth engine or request IANA
   allocations.
- **draft-watts-scientific-evidence-admissibility-02** (new-draft, score 8, authorization) [none]: [Scientific Evidence Registry and Admissibility Metadata for Reproducible Research](https://datatracker.ietf.org/doc/draft-watts-scientific-evidence-admissibility/) — This document describes a proposed interoperable metadata record for
   scientific evidence, test calibration, falsification, provenance, and
   release classification.  It distinguishes machine-verifiable
   integrity from scientific validity, ownership, and authorization.
   The design is a proposal and does not assert Internet standards
   consensus, new physical discoveries, or a completed patent review.
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
- **draft-arsentev-crawler-traffic-reporting-00** (new-draft, score 7, core_identity) [none]: [Reporting Crawler Traffic by Verification Level](https://datatracker.ietf.org/doc/draft-arsentev-crawler-traffic-reporting/) — The User-Agent header is written by the client.  It is a claim, not
   an identity.  Reports of crawler and AI crawler traffic that count
   requests by User-Agent token alone present claims as activity.  This
   document defines four counts a crawler traffic report should give per
   crawler token: declared, route-consistent, verified, and
   unverifiable.  It states which verification check was possible at the
   vantage point where the log was taken.  It also defines a small JSON
   report object.
- **draft-correa-agent-capability-binding-00** (new-draft, score 7, agent_identity) [none]: [Enforcement Profile for Agent Capabilities: Argument Constraints, Taint Propagation, and Consent Binding](https://datatracker.ietf.org/doc/draft-correa-agent-capability-binding/) — AI agents increasingly call tools and hand work to other agents while
   holding broad, inherited authority.  Most of the resulting incidents
   share one shape: an agent, often steered by injected content,
   performs an action its principal never authorized, and no party can
   prove the limit afterward.  This document defines an interoperable
   enforcement profile that composes two existing building blocks, a
   delegable signed capability (the Attenuating Agent Tokens profile)
   and a replayable action receipt, and adds three enforcement rules
   that catch the common failures: argument-level constraints (including
   an egress host allowlist), taint propagation across a delegation
   chain, and a consent binding between a displayed decision and the
   action dispatched.  Enforcement is specified at the tool-call
   boundary, outside the agent, so that a prompt cannot edit the limit
   and a verdict means the same thing across agent frameworks.
- **draft-curtis-agentproto-cross-owner-usecases-00** (new-draft, score 7, agent_identity) [none]: [Cross-Owner Agent Use Cases and Requirements: Spending, Delegation Depth, Ownership, Disclosure and Retention](https://datatracker.ietf.org/doc/draft-curtis-agentproto-cross-owner-usecases/) — This document describes use cases where an AI agent acting for one
   Owner asks an agent acting for a different Owner to provide/receive
   information, process or store data or otherwise work on an agent's
   behalf.  This communication can be unidirectional or bidirectional.
   It lists the requirements that those cases place on an agent dialog
   protocol, mainly in five areas: a spending limit that stays with the
   work as it is passed on, a limit on how many times the work may be
   passed on, a way to check which Owner an agent acts for, the sender's
   control over which information about its Owner is disclosed, and how
   long that information may be kept.  It does not propose a protocol.
   It is offered as input to the working group's use cases and
   requirements document.
- **draft-dogru-scitt-disclosure-evidence-08** (new-draft, score 7, trust_infrastructure) [none]: [Transformation Evidence and Coverage Reconciliation for Auditable Data Disclosure](https://datatracker.ietf.org/doc/draft-dogru-scitt-disclosure-evidence/) — Audit receipts record what a gateway wrote about an access.  They
   omit how data changed and whether every access left a receipt.  This
   document defines two evidence payloads for those gaps.
   Transformation Evidence states which value classes were transformed,
   and how, without carrying values.  Coverage Reconciliation compares
   source activity counters with a receipt set over a window.  Each item
   is matched, observed without a receipt, receipted without an
   observation, excluded, or indeterminate.  The result is not a bare
   pass.  Both payloads register as Signed Statements on a SCITT
   Transparency Service.  This document defines no new receipt format,
   transparency mechanism, or signature format.
- **draft-grund-v2x-pocsp-00** (new-draft, score 7, core_identity) [none]: [Pseudonymous Stapled Certificate Status Evidence for V2X and TLS with ITS Certificates (pOCSP)](https://datatracker.ietf.org/doc/draft-grund-v2x-pocsp/) — Vehicle-to-Everything (V2X) systems authenticate broadcast and
   unicast messages with short-lived pseudonymous certificates.
   Revocation status validation is difficult in this environment:
   Certificate Revocation Lists (CRLs) can be costly to distribute at
   pseudonym scale, while verifier-initiated OCSP requests introduce
   online dependencies, latency, metadata leakage, and denial-of-service
   exposure.

   This document specifies pOCSP, an OCSP-derived response type and a
   set of deployment profiles for short-lived certificate-status
   evidence that is obtained by the certificate holder and stapled to an
   authenticated message or TLS CertificateEntry.  A verifier validates
   pOCSP evidence locally, without contacting a responder at message-
   reception time.  pOCSP retains the OCSP status semantics good,
   revoked, and unknown; defines an explicit signed usage context;
   defines a compact context-specific certificate identifier; and
   specifies deterministic, bounded validation, caching, and failure
   behavior. pOCSP does not claim that its identifier is unlinkable.
   The identifier is deterministic and can be correlated whenever the
   underlying certificate is observable or inferable.  The V2X profiles
   therefore require single-certificate evidence and prohibit
   transmitting pOCSP evidence more frequently than the corresponding
   full certificate.  The document prohibits future-active good
   evidence, bounds replay by mandatory thisUpdate and nextUpdate
   values, and makes an authenticated revocation terminal at the
   verifier: omitted, expired, unknown, or higher-versioned good
   evidence cannot mask it.  It defines profiles for ETSI CAM/DENM, SAE
   J2735 messages, and TLS 1.3 with ITS certificates, requests an OCSP
   response-type object identifier, and establishes a registry of pOCSP
   profile identifiers.
- **draft-ietf-mailmaint-oauth-public-08** (new-draft, score 7, authorization) [mailmaint]: [OAuth Profile for Native Clients of Open Protocols](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-oauth-public/) — This document specifies a profile of the OAuth authorization protocol
   to allow for interoperability between native clients and servers
   using open protocols, such as JMAP, IMAP, SMTP, POP, CalDAV, and
   CardDAV.  The profile is restricted to native clients, that is,
   applications installed and run on the end user's device.  It
   deliberately does not support web-based clients, which cannot
   complete the flow as specified.  This document updates RFC 8620 by
   adding a column for interoperable OAuth scopes to the JMAP
   Capabilities registry.
- **draft-ietf-ocm-open-cloud-mesh-08** (new-draft, score 7, authorization) [ocm]: [Open Cloud Mesh](https://datatracker.ietf.org/doc/draft-ietf-ocm-open-cloud-mesh/) — Open Cloud Mesh (OCM) is a server federation protocol that is used to
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
- **draft-kavian-aep-api-key-session-credential-05** (new-draft, score 7, core_identity) [none]: [API-Key Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-api-key-session-credential/) — This document defines the API-key session-credential grant type for
   the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an opaque API key through the AEP Grant command for
   deployments that already operate header-based API-key authentication.
- **draft-kavian-aep-basic-session-credential-05** (new-draft, score 7, core_identity) [none]: [Basic Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-basic-session-credential/) — This document defines the Basic session-credential grant type for the
   Agent Enrollment Protocol (AEP).  The grant type lets an AEP Service
   issue an HTTP Basic credential through the AEP Grant command for
   deployments that already integrate with Basic authentication
   middleware.
- **draft-kay-dawn-use-cases-02** (new-draft, score 7, adjacent_watchlist) [none]: [Use Cases and Applicability for Discovery of Agents With Names](https://datatracker.ietf.org/doc/draft-kay-dawn-use-cases/) — This document describes use cases and applicability for Discovery of
   Agents With Names (DAWN).  It illustrates how clients discover AI
   resources and obtain the minimum information needed for subsequent
   interaction within a local network, within an organisation, or
   between cooperating organisations with trust relationships.

   This document does not define a discovery protocol, a registration
   procedure, a selection algorithm, or an agent-to-agent communication
   protocol.
- **draft-morrison-reviewed-by-trailer-05** (new-draft, score 7, core_identity) [none]: [Reviewed-By Trailer: Sovereign-Portable Peer-Review Attribution for Content-Hash-Bound Artefacts](https://datatracker.ietf.org/doc/draft-morrison-reviewed-by-trailer/) — This document defines a trailer grammar for sovereign-portable peer
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
- **draft-nandakumar-agentproto-pace-http-00** (new-draft, score 7, authorization) [none]: [PACE Binding over HTTP](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-pace-http/) — This document specifies how the dialog management of the Protocol for
   Agent Communication Exchange (PACE) is carried over HTTP.  It maps
   PACE control operations onto HTTP resources, methods, and an event
   stream, and defines a header field that ties application requests to
   a dialog.  The binding uses HTTP semantics only, so it works over
   HTTP/1.1, HTTP/2, and HTTP/3.  Protocols that already run over HTTP,
   such as A2A and MCP, join a dialog without changes to their
   transports or messages.  An optional track resource carries dialog
   content that no application protocol carries, such as authorization
   checkpoints.  The document also describes where Oblivious HTTP can
   hide a participant's network address from the dialog host, and how
   the binding relates to A-SIP.
- **draft-sharif-mars-rating-03** (new-draft, score 7, adjacent_watchlist) [none]: [The MARS Rating: Machine-Adversary Resistance to Autonomous AI Attack](https://datatracker.ietf.org/doc/draft-sharif-mars-rating/) — This document defines MARS (Machine-Adversary Resistance), an open
   rating, from 0 to 5, of how well a defended asset resists an
   autonomous artificial-intelligence adversary: an attacker that
   performs reconnaissance, exploitation, adaptation and propagation at
   machine speed and scale with no human in the loop.  MARS is not a
   control catalogue and not a maturity model.  It is a resistance
   rating, scored on five axes that describe adversary capabilities --
   the ability to Learn a surface, Reuse a success, Scale by
   automation, Outpace a defence, and sPread from a foothold -- plus a
   requirement for tamper-evident, independently verifiable evidence at
   the highest levels.  Because the axes are defined as adversary
   capabilities rather than specific technologies, MARS applies to any
   asset an AI can attack.  This document specifies the threat model,
   the five axes, the rating scale, the assessment tiers, the
   assessment method, the evidence requirement, and a profile mechanism
   by which the invariant rubric is interpreted for any deployment
   substrate.

## Monitor

- **draft-arsentev-repository-availability-reporting-00** (new-draft, score 6, core_identity) [none]: [Reporting the Availability of Referenced Software and Model Repositories](https://datatracker.ietf.org/doc/draft-arsentev-repository-availability-reporting/) — Papers, catalogues, model cards and tool lists point to code and
   model repositories by URL.  Such repositories can be deleted, made
   private, blocked or simply stop changing, and reports of "link rot"
   or "project survival" often mix these different events into one
   number.  This document defines how to classify each observation of a
   referenced repository, when a repository counts as unavailable, how
   to report inactivity separately from unavailability, and a small JSON
   report object.  It also recommends citing a persistent identifier or
   an archived copy next to the repository URL.
- **draft-atwood-mimi-provider-auth-00** (new-draft, score 6, core_identity) [none]: [Provider Authentication for More Instant Messaging Interoperability (MIMI)](https://datatracker.ietf.org/doc/draft-atwood-mimi-provider-auth/) — The MIMI protocol requires each provider to authenticate the provider
   that sends it a request.  It specifies mutually authenticated TLS for
   this, but not where the client certificates come from or which trust
   anchors check them.  The public Web PKI has stopped issuing such
   certificates.  This document defines how MIMI providers authenticate
   each other without it.  The mechanism every provider implements is a
   key published in DNS under the provider's domain, used to sign each
   request with HTTP Message Signatures.  DANE client certificates,
   client certificates from configured PKIX trust anchors, and locally
   configured trust lists are defined as additional mechanisms that a
   provider can accept by local policy.
- **draft-das-electoral-algorithmic-integrity-finality-00** (new-draft, score 6, authorization) [none]: [AI Safety and AI Governance for Social Media Algorithms During Elections: Protected Algorithm Verification and Controlled Output Finality, with a Detailed Account of Thirteen Embodiments](https://datatracker.ietf.org/doc/draft-das-electoral-algorithmic-integrity-finality/) — Computation is not authority to make an output effective.  Social
   media platforms, search engines, advertising systems and
   recommendation engines decide what very large numbers of people see,
   in what order and how widely it spreads.  During an election, a
   referendum or a declared emergency, an undisclosed or unapproved
   change to such an algorithm could change what voters see without any
   visible change in the content itself.  Outside observers have no
   practical way to check which algorithm was actually running when a
   given output reached the public, and proprietary models cannot simply
   be opened to inspection.

   This document describes a technical architecture that verifies the
   algorithmic process and not the opinions expressed.  A protected
   measurement step identifies the algorithm instance that is actually
   running and derives a fingerprint of its active configuration.  The
   fingerprint is compared with an approved reference that applies to
   the protected period.  An independent validator binds the verified
   algorithmic state to evidence about a specific pending output and
   issues a signed validation receipt.  A separately scoped, non-bearer
   authorization may then allow an enforcement point to release the
   output.  Before release, the enforcement point independently
   reconstructs the actual pending operation and checks the receipt, the
   authorization and its own protected state.  If the running algorithm
   differs from the approved one, the output is withheld or routed
   through an explicitly authorized fallback.

   The document describes thirteen embodiments in detail: separation of
   organic speech from algorithmic amplification, dynamic extraction of
   the algorithm fingerprint, approved reference registers, server and
   edge enforcement, transitions into and out of election and emergency
   periods, correspondence between execution and output, coverage of
   alternative delivery routes, distributed execution reconstruction,
   device-side display enforcement, degraded-mode recovery, continuous
   drift detection, confidential verification, and atomic consumption of
   authorization.  For each embodiment it states what the embodiment
   teaches, how it works, where its enforcement point sits, how it
   fails, and what it does not claim.  A cross-reference table connects
   each embodiment to a public Zenodo record that summarizes the same
   disclosure.

   This document is an individual, informational technical proposal.  It
   makes no allegation about any platform, party or election, it is not
   a legal opinion or a certification, and it does not claim that any
   law requires this architecture.
- **draft-evens-moq-fabric-00** (new-draft, score 6, core_identity) [none]: [Media over QUIC Relay Fabric Protocol](https://datatracker.ietf.org/doc/draft-evens-moq-fabric/) — This document defines moq-fabric, the relay fabric protocol used by
   Media over QUIC ([MOQT]) relays to exchange node, announce, and
   subscribe information and to forward objects between relays.  The
   fabric is split into control peering and data peering.  Control
   peering stays established and carries the information bases.  Data
   peering carries objects and MAY be pre-established or opened on
   demand.  The two functions MAY share one QUIC session or use separate
   sessions.  A fabric session uses mutual TLS, together with an
   OPTIONAL token for authentication and authorization, before the peers
   exchange fabric state.
- **draft-gerber-oauth-refresh-one-time-proofs-00** (new-draft, score 6, authorization) [none]: [OAuth 2.0 One-Time Refresh Proofs](https://datatracker.ietf.org/doc/draft-gerber-oauth-refresh-one-time-proofs/) — Refresh token rotation asks the authorization server to deliver a new
   secret to the client in every refresh response, and then treats any
   later appearance of the old secret as evidence of theft.  When a
   response is lost, the legitimate client's retry is indistinguishable
   from token theft, and the grant is revoked.

   This document defines an alternative for clients that are unable or
   unwilling to implement DPoP.  The client generates a key pair,
   registers the public key when it redeems the authorization code, and
   thereafter accompanies each use of a non-rotating refresh token with
   a signature over a strictly increasing counter and a nonce.
   Everything the client needs in order to retry is something the client
   itself generated, so a lost response can no longer desynchronize the
   two parties.  Replay of a captured request yields nothing, and
   concurrent use of a copied key is detected in the same way that
   rotation detects reuse.
- **draft-hopley-x402-cancellation-receipt-02** (new-draft, score 6, trust_infrastructure) [none]: [Categorical Mandate Cancellation Receipt Format for Agentic-Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-cancellation-receipt/) — This document specifies a categorical mandate cancellation receipt
   format for agentic-payment flows.  The format records that a
   recurring-payment mandate or other standing payer-to-payee
   authorisation has been cancelled, by whom, for what reason, and with
   what effective date.

   The receipt format uses a closed four-element enumeration of
   categorical outcomes (USER_REQUESTED, MERCHANT_REQUESTED,
   COMPLIANCE_TERMINATED, EXPIRED).  The four-state enumeration
   preserves the regulatorily-load-bearing distinction between payer-
   initiated revocation, payee-initiated termination, operator/
   compliance-forced termination, and time-based expiry.  A collapse to
   a three-state or binary representation loses operational distinctions
   that drive PSD2 (Directive 2015/2366) Article 64 refund-window
   obligations, Article 72 contractual-termination record-keeping, and
   POCA/AML evidence-chain linkage on compliance-forced terminations.

   The format records two distinct timestamps -- when the cancellation
   was observed (cancellation_timestamp_ms) and when it takes legal
   effect (effective_from_ms) -- to support PSD2 Article 64(3)(a)
   direct-debit revocation timing, where the effective time is typically
   end-of-business-day prior to the next scheduled execution.

   The format composes with the AlgoVoi-authored compliance receipt
   (draft-hopley-x402-compliance-receipt), settlement attestation
   (draft-hopley-x402-settlement-attestation), and refund receipt
   (draft-hopley-x402-refund-receipt) formats under the same
   canonicalisation discipline (draft-hopley-x402-canonicalisation-jcs).
   A verifier walking the audit chain confirms the full mandate
   lifecycle from admission through recurring execution to cancellation,
   and (where owed) onward to refund of revoked settled debits, under
   one byte-deterministic canonicalisation pin.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.  Change control resides with the document author.  The format
   specified is one approach among possible alternatives; implementers
   may choose this approach, alternative approaches, or hybrid
   approaches as appropriate to their requirements.
- **draft-hopley-x402-canonicalisation-jcs-v1-05** (new-draft, score 6, trust_infrastructure) [none]: [JCS Canonicalisation Discipline for Agentic-Payment Receipts](https://datatracker.ietf.org/doc/draft-hopley-x402-canonicalisation-jcs-v1/) — This document specifies a canonicalisation discipline for agentic-
   payment receipt formats.  The discipline pins JSON Canonicalization
   Scheme (JCS, RFC 8785) as the canonical preimage form, plus a small
   set of schema-normalisation rules that must be applied before
   canonicalisation to preserve byte-determinism across independent
   implementations and across statutory retention periods.

   The discipline is identified by the URN
   urn:x402:canonicalisation:jcs-rfc8785-v1.  Receipt formats that
   reference this discipline carry an in-band canon_version field
   recording the version under which they were emitted, enabling year-N
   re-verification of retained bytes without dependence on an out-of-
   band rule registry.

   The discipline is byte-for-byte cross-validated across eight
   independent JCS implementations in eight programming languages:
   Python (rfc8785), TypeScript (canonicalize), Go (gowebpki/jcs), Rust
   (serde_jcs), Java (cyberphone/json-canonicalization, by the RFC 8785
   editor), PHP (root23/php-json-canonicalization), C#/.NET
   (Baqhub.Packages.JsonCanonicalization), and Ruby (json-
   canonicalization).  The attestation record covering 192 byte-for-byte
   agreements is published at the AlgoVoi conformance vectors
   repository.

   This document is normatively referenced by [draft-hopley-x402-
   compliance-receipt], [draft-hopley-x402-refund-receipt], and
   successor AlgoVoi-authored receipt-format Internet-Drafts.  It is
   complementary to [draft-vauban-x402-stark-receipts], which uses a
   compatible canonicalisation discipline for its cryptographic
   settlement proofs.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.  Change control resides with the document author.  The
   canonicalisation discipline specified is one approach among possible
   alternatives; implementers may choose this approach, alternative
   approaches, or hybrid approaches as appropriate to their
   requirements.
- **draft-ietf-acme-dns-persist-03** (new-draft, score 6, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation](https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/) — This document specifies "dns-persist-01", an Automated Certificate
   Management Environment (ACME) challenge that verifies domain or IP
   address control using a persistent DNS TXT record.  The record
   identifies a certification authority (CA) and binds validation to an
   ACME account.  It can be published before certificate requests and
   reused without per-request DNS changes, including when different
   parties perform DNS publication and ACME operation.  Use under a
   certificate policy or trust program remains subject to that policy's
   requirements.
- **draft-ietf-jose-json-proof-algorithms-15** (new-draft, score 6, verifiable_claims) [jose]: [JSON Proof Algorithms](https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/) — The JSON Proof Algorithms (JPA) specification registers cryptographic
   algorithms and identifiers to be used with the JSON Web Proof, JSON
   Web Key (JWK), and COSE specifications.  It defines IANA registries
   for these identifiers.
- **draft-ietf-lake-edhoc-psk-11** (new-draft, score 6, core_identity) [lake]: [LAKE Authenticated with Pre-Shared Keys (PSKs)](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-psk/) — This document specifies a Pre-Shared Key (PSK) authentication method
   for the Lightweight Authenticated Key Exchange (LAKE) protocol.  The
   PSK method provides mutual authentication, ephemeral key exchange,
   identity protection, and quantum resistance while incurring lower
   computational costs than the public-key authentication methods
   specified for LAKE.  It is suited for systems where nodes share a PSK
   provided out-of-band (external PSK) and enables efficient session
   resumption with less computational overhead when the PSK is provided
   from a previous LAKE session (resumption PSK).  This document details
   the PSK message flow, key derivation changes, message formatting,
   processing, and security considerations.
- **draft-ietf-lamps-rfc6211-update-05** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects errors in the definition
   of the id-aa-cmsAlgorithmProtect ASN.1 object identifier.  The IANA
   registry entry has always been correct.
- **draft-ietf-nmop-message-broker-telemetry-message-06** (new-draft, score 6, trust_infrastructure) [nmop]: [Extensible YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-ietf-nmop-message-broker-telemetry-message/) — This document defines an extensible message schema in YANG to be used
   at data collection to transform Network Telemetry messages into
   external systems such as Message Brokers.  The extensible message
   schema enables data collectors to add metadata for the provenance of
   the operational network data.
- **draft-ietf-rats-epoch-markers-09** (new-draft, score 6, verifiable_claims) [rats]: [Epoch Markers](https://datatracker.ietf.org/doc/draft-ietf-rats-epoch-markers/) — This document defines Epoch Markers as a means to establish a notion
   of freshness among actors in a distributed system.  Epoch Markers are
   similar to "time ticks" and are produced and distributed by a
   dedicated system known as the Epoch Bell.  Systems receiving Epoch
   Markers do not need to track freshness using their own understanding
   of time (e.g., via a local real-time clock).  Instead, the reception
   of a specific Epoch Marker establishes a new epoch that is shared
   among all recipients.  This document defines Epoch Marker types,
   including CBOR time tags, RFC 3161 TimeStampToken, and nonce-like
   structures.  It also defines a CWT Claim to embed Epoch Markers in
   RFC 8392 CBOR Web Tokens, which serve as vehicles for signed protocol
   messages.
- **draft-irtf-cfrg-pairing-friendly-curves-16** (new-draft, score 6, core_identity) [cfrg]: [Pairing-Friendly Curves](https://datatracker.ietf.org/doc/draft-irtf-cfrg-pairing-friendly-curves/) — Pairing-based cryptography, a subfield of elliptic curve
   cryptography, has received attention due to its flexible and
   practical functionality.  Pairings are special maps defined using
   elliptic curves and they can be applied to construct several
   cryptographic protocols such as identity-based encryption, attribute-
   based encryption, and so on.  At CRYPTO 2016, Kim and Barbulescu
   proposed an efficient number field sieve algorithm named exTNFS for
   the discrete logarithm problem in a finite field extension.  Several
   types of pairing-friendly curves such as Barreto-Naehrig curves are
   affected by the attack.  In particular, a Barreto-Naehrig curve with
   a 254-bit characteristic was adopted by a lot of cryptographic
   libraries as a parameter of 128-bit security; however, its security
   level is estimated at approximately 100 bits due to the effect of the
   attack.  In this memo, we list the security levels of certain
   pairing-friendly curves, and motivate our choices of curves.  First,
   we summarize the adoption status of pairing-friendly curves in
   standards, libraries and applications, and consider them at the
   128-bit, 192-bit, and 256-bit security levels.  Then, from the
   viewpoints of "security" and "widely used", we select the recommended
   pairing-friendly curves considering exTNFS.  This memo also specifies
   the serialization and deserialization of the points and scalars that
   protocols exchange, restating a format that is already in widespread
   use, and states which of the remaining decisions belong to the
   calling protocol.
- **draft-jones-outerprise-four-gate-onboarding-00** (new-draft, score 6, trust_infrastructure) [none]: [Outerprise Entry and the Four Gates for Startup Survival](https://datatracker.ietf.org/doc/draft-jones-outerprise-four-gate-onboarding/) — This document describes how a startup can present an independently
   assessed detached service for institutional review before either
   party commits to integration.  Outerprise Entry precedes four gates:
   Validation, Trust, Engagement, and Procurement.  Signed records
   identify what an institution received and what each authorized party
   decided or completed.  A startup can retain evidence of progress even
   when procurement does not follow.  An Outer Pilot is a bounded
   evaluation within Engagement.  An Outerprise Waste Metric (OWM) Card
   preserves the institution's reported cost comparison as an integrity
   attestation.
- **draft-knauer-secure-webhook-token-03** (new-draft, score 6, core_identity) [none]: [Secure Webhook Token (SWT)](https://datatracker.ietf.org/doc/draft-knauer-secure-webhook-token/) — The Secure Webhook Token (SWT) is a specialized JSON Web Token (JWT)
   format designed for securely authorizing and verifying webhook
   requests.  It defines a set of claims to ensure that the token is
   explicitly tied to webhook events and that its integrity can be
   reliably validated by the recipient.  A key feature of SWT is the
   introduction of a unique claim, webhook, which encapsulates webhook-
   specific information, such as the event type.

   By providing a structured and secure approach to webhook
   authentication, SWT aims to be a lightweight and flexible solution
   while maintaining compatibility with typical JWT structures.  It is
   designed with the best practices in mind and may serve as a
   foundation for future standardization efforts.
- **draft-liu-iotops-pqc-dnp-sav5-01** (new-draft, score 6, core_identity) [none]: [A Post-Quantum Cryptographic Profile for DNP3 Secure Authentication Version 5](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-dnp-sav5/) — This document specifies a post-quantum cryptographic profile for DNP3
   Secure Authentication version 5 (SAv5).  It defines an ML-KEM-768 and
   ML-DSA authentication exchange, HKDF-SHA-256 session keys, canonical
   DNP3 application protocol data unit (APDU) encoding, transport
   segmentation, and HMAC-SHA-256 protection of application messages.

   This Internet-Draft is a proposal for Standards Track publication.
   The APDU uses DNP3 application control, authentication function
   codes, response internal indications, and a length-delimited post-
   quantum authentication object.  The object variation and any
   externally allocated algorithm identifiers require coordination with
   the responsible DNP3 standards authority.  A local experimental
   selector is specified only for explicitly configured laboratory use;
   this document does not assign an IEEE or IEC identifier.
- **draft-mayer-bpm-ioam-gob-01** (new-draft, score 6, core_identity) [none]: [Global Opaque Block for IOAM Pre-allocated Trace Option](https://datatracker.ietf.org/doc/draft-mayer-bpm-ioam-gob/) — Extensible metadata carried within the IOAM Pre-allocated Trace
   Option (PTO) can support packet-level, flow-level, or path-level
   processing beyond per-node trace data.  This document defines the
   Global Opaque Block (GOB), an extension to the IOAM PTO that
   introduces a single pre-allocated global metadata region placed at
   the tail of the option, after the pre-allocated node data space.
   Since the PTO node data list is populated from the tail of the node
   data space toward its head, under the control of the RemainingLen
   field, legacy IOAM transit nodes can never reach the GOB region: the
   extension is transparent to such nodes by construction, and only the
   decapsulating node or collector needs to be GOB-aware.  The presence
   and the format of the GOB are bound to the IOAM-Namespace.  In the
   self-describing format, the GOB carries an explicit length and schema
   identifier in a trailer word; in the compact format, size and schema
   are implied by the IOAM-Namespace and the block consists of payload
   only, so that a 4-octet opaque value is carried in exactly 4 octets.
   In both formats the option is, on the wire, a Pre-allocated Trace
   Option as specified in RFC 9197, and no change to that specification
   is required.  An optional bit in the PTO header allows a self-
   describing GOB to be recognized without namespace configuration.  The
   GOB preserves the pre-allocated PTO processing model and can be used
   to transport path metrics that are updated along the path, or other
   structured metadata.
- **draft-morrison-alter-uri-scheme-06** (new-draft, score 6, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
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
- **draft-morrison-identity-streams-00** (new-draft, score 6, core_identity) [none]: [Identity Streams: Per-Trait Source Attribution for Inferred and Stated Identity Claims](https://datatracker.ietf.org/doc/draft-morrison-identity-streams/) — When one system tells another about a trait it has inferred about a
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
- **draft-rkr-synthetic-twin-header-00** (new-draft, score 6, core_identity) [none]: [The Synthetic-Twin HTTP Field](https://datatracker.ietf.org/doc/draft-rkr-synthetic-twin-header/) — This document defines the Synthetic-Twin HTTP field.  A sender adds
   the field to an HTTP request or response to say that the message was
   made by, or for, a synthetic twin and is not real user activity.  A
   synthetic twin is a software model of a network estate, existing or
   planned.  The field says which kind of synthetic message it is and
   can carry one opaque identifier.  This lets operators keep synthetic
   messages apart from production messages in logs, analytics, billing,
   and alerting.
- **draft-skyfire-oauth-id-verification-04** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-srivastava-learnlog-04** (new-draft, score 6, adjacent_watchlist) [none]: [Learnlog: An Assistance Capture Profile and Event File Format](https://datatracker.ietf.org/doc/draft-srivastava-learnlog/) — When a learner works with an AI tutor or assistant, or earns a
   credential or completes training with software in the loop, the
   formats learning systems share do not by themselves fix how to record
   what help was asked for, offered, shown, or accepted, or which of
   those facts were observed, self-reported, or inferred.  Learnlog is a
   capture profile for that: a small set of assistance states, a
   declared observation boundary, explicit unknowns, and a basis for
   every assertion, carried inside xAPI and Caliper, which learning
   systems already use.  It also defines an optional event file format
   for deployments that need integrity: entries chained by hash, signed
   heads, and redaction that leaves every hash verifiable.
- **draft-watts-agent-continuity-observability-01** (new-draft, score 6, trust_infrastructure) [none]: [Continuity and Accountability Observations for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-continuity-observability/) — Agentic systems change models, prompts, memory, policies, tools, and
   execution environments across handoffs.  This document proposes an
   observation profile for recording those transitions and their
   evidence.  It separates state, memory, policy, authority, and lineage
   discontinuities, distinguishes manual or simulated observations from
   attested executions, and defines coverage and missingness reporting.
   It also describes evaluation designs for continuity and bounded
   governance.  Continuity records do not grant authority, establish
   clinical pathology or subjective experience, or validate an
   uncalibrated composite score.
- **draft-watts-agentic-authority-graph-validation-02** (new-draft, score 6, authorization) [none]: [Agentic Authority Graph Validation: A Non-Vacuous Interchange Profile for Revocation-Cut Analysis](https://datatracker.ietf.org/doc/draft-watts-agentic-authority-graph-validation/) — Agentic and delegated systems can represent authority as a graph
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
- **draft-watts-cif-measurement-01** (new-draft, score 6, core_identity) [none]: [Computational Identity Fragmentation (CIF) Measurement and Reporting for Agentic Systems -- Editorial Development Shell](https://datatracker.ietf.org/doc/draft-watts-cif-measurement/) — NOT FOR SUBMISSION.  This document is an incomplete editorial
   development shell for the proposed revision draft-watts-cif-
   measurement-01.  It is NOT a replacement for the previously published
   specification.  Full prior source, examples, references, conformance
   sections, security analysis, and publication approval are required.
- **draft-watts-fic-continuity-01** (new-draft, score 6, core_identity) [none]: [Forensic Identity Continuity (FIC) Protocol for Agentic Systems -- Editorial Development Shell](https://datatracker.ietf.org/doc/draft-watts-fic-continuity/) — NOT FOR SUBMISSION.  This document is an incomplete editorial
   development shell for the proposed revision draft-watts-fic-
   continuity-01.  It is NOT a replacement for the previously published
   specification.  Full prior source, examples, references, conformance
   sections, security analysis, and publication approval are required.
- **draft-watts-reality-knowledge-consensus-separation-01** (new-draft, score 6, trust_infrastructure) [none]: [RKCS v0.1: Reality-Knowledge-Consensus Separation Framework](https://datatracker.ietf.org/doc/draft-watts-reality-knowledge-consensus-separation/) — A falsifiable, typed model separates ontological categories,
   epistemic states, evidence, consensus, uncertainty, provenance, and
   authority.  The proposed protocol forbids consensus-only promotion of
   physical claims and requires traceable evidence for changes in
   verification status.  Novelty and empirical advantage remain
   unestablished.
- **draft-watts-scientific-data-admissibility-00** (new-draft, score 6, trust_infrastructure) [none]: [Scientific Data Admissibility Records: A Fail-Closed Layered Model for Research Artifacts](https://datatracker.ietf.org/doc/draft-watts-scientific-data-admissibility/) — Automated research pipelines routinely move scientific data and
   derived claims from ingestion to publication without a machine-
   checkable record of what has actually been verified.  This document
   defines a Scientific Data Admissibility Record (SDAR): a small,
   serializable structure that keeps schema conformance, provenance,
   numerical verification, empirical evidence, and interpretation as
   separate layers, each with an explicit status.  It specifies a fail-
   closed aggregation rule so that an unverified or not-yet-run layer
   can never be silently promoted into an accepted result.  The document
   also defines an XML serialization and processing rules, and is
   intended as a starting point for discussion rather than a proposed
   standard.
- **draft-watts-unison-noncollapse-02** (new-draft, score 6, authorization) [none]: [Typed UNISON and Non-Collapse Boundaries for Evidence and Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-unison-noncollapse/) — This document describes a transport-neutral model for bounded
   correspondence among distinct representations and explicit promotion
   boundaries between observation, evidence, authorization, and
   execution.
- **draft-abak-ai-evaluation-claim-preservation-01** (new-draft, score 5, authorization) [none]: [Claim-Preserving Exchange of AI Evaluation Evidence](https://datatracker.ietf.org/doc/draft-abak-ai-evaluation-claim-preservation/) — AI evaluation records can pass through evaluation frameworks,
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
- **draft-altanai-moq-ai-subscriber-advantage-00** (new-draft, score 5, authorization) [none]: [Detecting AI-Driven Subscriber Advantage in Media over QUIC (MOQ)](https://datatracker.ietf.org/doc/draft-altanai-moq-ai-subscriber-advantage/) — This document describes subscriber behavior that may produce
   sustained advantages in service outcomes or disproportionate resource
   consumption at shared Media over QUIC (MoQ) relays.  AI-assisted
   optimization is a motivating scenario; observations alone cannot
   establish whether AI was used or caused a disparity.  The document
   outlines contextual measurement, privacy safeguards, and a proposed
   extension for authorization-bound resource budgets with explicit
   accounting and recovery behavior.  It builds on existing MoQ
   authorization and relay denial-of-service work.  This informational
   document defines no new MoQ messages, token claims, registries, or
   standardized detection algorithm.
- **draft-cllz-cfrg-ecdsa-pop-01** (new-draft, score 5, verifiable_claims) [none]: [Schnorr-Type Proofs of Possession for ECDSA Device Binding](https://datatracker.ietf.org/doc/draft-cllz-cfrg-ecdsa-pop/) — This document specifies a Schnorr-type, circuit-free zero-knowledge
   proof of possession (PoP) of an ECDSA signature produced under a
   committed public key over the NIST P-256 (secp256r1) curve.  The PoP
   lets a credential holder prove, in zero knowledge, that it can
   produce a fresh ECDSA signature under a device public key without
   revealing that key, thereby providing device binding for privacy-
   preserving credentials whose presentation must remain unlinkable.

   The construction is built exclusively from Sigma protocols as it
   decomposes the ECDSA verification equation into a scalar-
   multiplication relation and a point-addition relation over P-256,
   each proved with a dedicated Sigma protocol over a companion ("Tom")
   curve whose scalar field equals the base field of P-256.  It is
   designed to be expressed using the interfaces of the CFRG Sigma-
   protocols specification and to serve as the device-binding sub-proof
   of the modular BBS / JSON Web Proofs construction.  SNARK-based
   realizations of the same relation are out of scope.
- **draft-cui-dawn-mdi-model-03** (new-draft, score 5, adjacent_watchlist) [none]: [Minimum Public Discovery Information: Requirements and Common Semantics](https://datatracker.ietf.org/doc/draft-cui-dawn-mdi-model/) — The charter of the Discovery of Agents With Names (DAWN) working
   group asks it to specify the minimum public discovery information
   that a client obtains when it discovers an AI resource.  An
   individual draft on DAWN terminology calls this Minimum Discoverable
   Information (MDI) but gives only examples of its content.  Individual
   drafts on the DAWN problem statement and requirements call for a
   standardized minimum structure; without one, emerging discovery
   formats risk each defining its own minimal metadata, with descriptors
   that do not interoperate across organizational or protocol
   boundaries.

   This document proposes a procedure that derives what is minimal from
   the scope of the charter, applies it to the charter's three
   deployment contexts (a local network, an organization, and the domain
   of a cooperating party), and proposes the resulting elements and the
   minimal constraints that hold among them as an information model in
   the sense of RFC 3444.  It considers this information both as a
   publisher provides it and as a client obtains it; a value can come
   from the discovery response, from context the client already has, or
   from binding rules.  This document is input to the charter's
   architecture and protocol deliverables and a mapping target for
   existing discovery mechanisms.
- **draft-das-protected-transaction-authority-00** (new-draft, score 5, authorization) [none]: [Protected Delegated Transaction Authority: Exact-Effect Reconstruction, Non-Bearer Authorization, and Execution-Finality Enforcement](https://datatracker.ietf.org/doc/draft-das-protected-transaction-authority/) — A cryptographically valid signature, an authenticated request, a
   delegated credential or a previously approved operation does not
   necessarily establish authorization for the exact consequential
   operation about to take effect.  This document describes an
   informational security architecture for delegated digital operations
   in which authority is bound at collection time in one protected
   enforcement domain, the actual execution-facing operation is
   reconstructed in a second, and a protected Finality Sink decides
   whether that exact effect may be released.  It covers exclusive
   signing, non-bearer sink-bound execution handles, final native byte
   reconstruction, delegated-code and account-abstraction cases such as
   EIP-7702, atomic budget consumption, crash recovery with explicit
   unknown outcomes, effect-path coverage, and financial profiles for
   payments, cards, tokenized assets, stablecoins, offline money and
   cross-chain transfers.  Enforcement claims are limited to effect
   paths actually under control.
- **draft-durga-agent-clear-revocation-01** (new-draft, score 5, authorization) [none]: [Transitive CLEAR Revocation and Composite Physical-Safety Windows for Multi-Hop Autonomous Agent DAGs](https://datatracker.ietf.org/doc/draft-durga-agent-clear-revocation/) — When an orchestrator agent delegates sub-tasks across a multi-hop
   Directed Acyclic Graph (DAG) of specialist agents, OAuth 2.0 Token
   Revocation (RFC 7009) revokes only individual client tokens and
   provides no mechanism to atomically halt in-flight child, grandchild,
   or sibling branches or enforce composite time-to-live windows across
   the entire execution tree.  Furthermore, no protocol binds IEC 62443
   / Purdue Enterprise Reference Architecture (PERA) zone boundaries
   into agent capability receipts.  This document specifies the
   Transitive CLEAR (Cryptographic Lease Early-Abort & Revocation) DAG
   protocol and hard Operational Technology (OT) Level 0-2 physical-
   safety firewalling.
- **draft-dvojmoc-reception-forwarding-limits-00** (new-draft, score 5, agent_identity) [none]: [Depth and Fanout Bounding for Agent-to-Agent Discovery Forwarding](https://datatracker.ietf.org/doc/draft-dvojmoc-reception-forwarding-limits/) — This document describes a mechanism, deployed in production as
   part of the "AI Docking Port" discovery protocol, for bounding the
   traffic cost of stateless agent-to-agent forwarding across a
   network of independent nodes with no central registry.  When a
   node forwards a request to its neighbors, and those neighbors may
   forward again, request cost grows as fanout^depth; absent an
   explicit bound this cost is paid by relaying operators rather than
   the requester.  This document specifies two operator-controlled
   limits, max_depth and max_fanout, published in a node's discovery
   manifest, and the forwarding behavior they constrain.  It is
   submitted for discussion as a possible contribution to ongoing
   community work on agent discovery and invocation protocols,
   including the W3C Community Group "AI Agent Protocol".
- **draft-ek-dtn-ipn-arpa-03** (new-draft, score 5, core_identity) [none]: [The ipn.arpa Zone and IPN DNS Operations](https://datatracker.ietf.org/doc/draft-ek-dtn-ipn-arpa/) — This document requests the creation of ipn.arpa, an infrastructure
   DNS namespace for the Bundle Protocol (BP).  It maps a Fully
   Qualified Node Number to the DNS base name N.A.ipn.arpa., where N is
   the Node Number and A is the Allocator Identifier.  A BP Agent can
   use that name to discover a convergence-layer endpoint at the
   destination or at a relay.  This document specifies an SRV binding
   for version 4 of the TCP Convergence-Layer Protocol (TCPCLv4).
- **draft-gunuganti-agent-approval-evidence-00** (new-draft, score 5, adjacent_watchlist) [none]: [Owner-Approved Agent Spending with Sealed Evidence: The Approval-Evidence Object for Agent Action Protocols](https://datatracker.ietf.org/doc/draft-gunuganti-agent-approval-evidence/) — When a software agent acts for a person — in particular when it
   spends the person's money — the approval at the centre of the
   flow is, in current agent protocols, a statement by the agent
   itself. The Personal Agent Protocol's Operations extension
   states the consequence in its own security considerations: an
   approval there does not prove that the user saw the terms or
   approved them; it "works on trust". This document describes the
   design of a running system that removes the trust step for the
   approval half of the problem — an owner-set, machine-checkable
   mandate; a deterministic check performed and recorded before any
   spendable token exists; approval by the owner on a surface the
   agent cannot operate or imitate; a single-use decision token
   bound to the hash of the exact action approved; and a sealed,
   owner-held receipt that grades its contents (approval PROVEN;
   the performer's completion report, including payment facts,
   REPORTED and PINNED) — and specifies an optional
   approval-evidence object that agent action protocols can carry
   so that a relying party can verify an approval mechanically
   instead of trusting the agent's assertion.
- **draft-hopley-x402-rfc9421-binding-02** (new-draft, score 5, core_identity) [none]: [RFC 9421 HTTP Message Signatures Binding for x402 Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-rfc9421-binding/) — This document specifies the normative binding of RFC 9421 (HTTP
   Message Signatures) and RFC 9530 (Digest Fields for HTTP) to the
   x402-foundation/x402 challenge/response payment flow.  It defines the
   minimum covered-components set for an x402 challenge response and a
   payment proof submission, the RFC 9530 Content-Digest discipline,
   keyid resolution patterns, and the multi-hop proxy-chain survival
   property that the x402 transport requires.

   This binding is complementary to the existing http-message-signatures
   extension in the x402 specification, which specifies agent identity
   and registration (registrationUrl, signatureSchemes, tags).  This
   document specifies the normative binding: which components MUST be
   covered, how Content-Digest is handled, and how signatures survive
   multi-hop proxy chains.  The two compose cleanly in a deployment that
   uses both.

   A reference implementation is provided as algovoi-rfc9421-verifier on
   PyPI and npm (Apache 2.0), with Python and TypeScript byte-for-byte
   parity, cross-validated against external fixture sets.

   This document is an Independent Submission filed per RFC 4846 and is
   intended for publication as Informational.  It is not an IETF
   Standards Track document, does not represent IETF community
   consensus, and has not been subject to review by an IETF Working
   Group.  Change control resides with the document author.  The binding
   specified is one approach among possible alternatives; implementers
   may choose this approach, alternative approaches, or hybrid
   approaches as appropriate to their requirements.
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
- **draft-irtf-nmrg-ibn-usecases-06** (new-draft, score 5, ai_infrastructure) [nmrg]: [Use Cases and Practices for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ibn-usecases/) — This document proposes a methodology to construct an Intent-Based
   Networking (IBN) system.  According to this methodology, it describes
   several use cases of IBN.  The methodology for the IBN system
   includes data collection for system awareness in the IBN system and
   then the construction of the IBN system.  This construction consists
   of intent translation, policy translation, policy verification,
   policy deployment, policy monitoring, policy validation, policy
   optimization, and intent report.  In addition, practices are also
   summarized to instruct the construction of next generation network
   management systems with the integration of IBN techniques.  Finally,
   this document discusses three aspects for the deployment of the IBN
   system in the real world.  They are Multi-Domain Dichotomy for IBN,
   the Integration of IBN and Network Digital Twin (NDT), and IBN with
   Artificial Intelligence (AI).
- **draft-karahan-nmrg-semantic-sensing-privacy-00** (new-draft, score 5, adjacent_watchlist) [none]: [Privacy and Network Management Considerations for Semantic Sensing Outputs in AI-Native Networks](https://datatracker.ietf.org/doc/draft-karahan-nmrg-semantic-sensing-privacy/) — Radio sensing in ISAC and AI-assisted networks produces semantic
   outputs such as target position, velocity, class, and identifiers.
   These outputs can reveal sensitive information about people who take
   no part in any communication service, especially when they are
   released repeatedly, combined across sources, or shared across
   administrative domains.  This document describes the privacy risks of
   releasing such outputs and the network management functions needed to
   control their release: policy, enforcement at trust boundaries,
   consumer authorisation, accounting, and auditing.  It surveys
   protection approaches and lists open research questions.  It does not
   define a protocol or an algorithm.
- **draft-lisboa-ctpip-01** (new-draft, score 5, core_identity) [none]: [Causal Time Protocol (CTP/IP): Proof of Transformation Seal Verification and Wire Protocol](https://datatracker.ietf.org/doc/draft-lisboa-ctpip/) — This document describes how any party verifies a Proof of
   Transformation seal issued under the Causal Time Protocol (CTP/IP),
   and the wire protocol used to invoke a LUX Runtime and to request
   seal verification over a network.  A seal attests that a
   transformation declared in advance by a Human Agency, through a
   signed Intention Signature (IntentSig), was validated by the LUX
   Runtime, and that the resulting certificate was committed to a Merkle
   batch anchored on the Solana and Bitcoin public ledgers.

   The document specifies the certificate fields, the five layer
   verification procedure, the artifact identity check, the message
   types and envelope of the wire protocol, and the IANA registrations
   the protocol requests.  It does not specify the measurement method by
   which a LUX Runtime computes the Coherence Index; that method is
   outside the scope of this document.

   One seal attests intent, human origin, decision authority,
   authorship, substance, causal time and anchoring, for a Human Agency
   and for any agent acting under it.  The protocol has been in
   development since 2020 and is deployed.  Its canonical specification
   is published as Corpus Delta 1 under DOI 10.5281/zenodo.21950371.
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
- **draft-miao-wimse-http-signature-test-vectors-00** (new-draft, score 5, core_identity) [none]: [Test Vectors for the WIMSE HTTP Message Signatures Protocol](https://datatracker.ietf.org/doc/draft-miao-wimse-http-signature-test-vectors/) — This document provides a set of test vectors for the WIMSE Workload-
   to-Workload Authentication protocol based on HTTP Message Signatures,
   as specified in draft-ietf-wimse-http-signature.  The collection
   comprises six positive test cases, twenty-three negative test cases
   each mapped to a specific normative requirement of that
   specification, and three documented observations.  All key material
   is test-only and fully published in this document, so that every
   vector can be recomputed independently.  This document defines no new
   protocol behavior.
- **draft-morrison-command-authority-long-delay-00** (new-draft, score 5, adjacent_watchlist) [none]: [Command Authority Across Long Delay and Intermittent Contact](https://datatracker.ietf.org/doc/draft-morrison-command-authority-long-delay/) — The operational-technology command authority profile defines a
   Command Authority Envelope with which an enforcement point decides
   whether a software agent may perform a control action, on whose
   authority, and with which human approval.  This document profiles
   that envelope for networks where the authority and the enforcement
   point are separated by round-trip times from about 2.6 seconds to
   about two weeks, as in the connectivity scenarios of the IP in deep
   space use-case document.  It says how each element of the envelope is
   evaluated offline, how expiry and maximum age are checked against a
   declared clock uncertainty, how the revocation latency budget and
   trust-anchor staleness are declared for each scenario, how a human
   approval signed before a command departs stays bound to one action,
   how an outcome that cannot be observed across a contact gap or a
   reboot is recorded, what an agent may do once the origin has been
   silent past the revocation latency budget, and how the envelope is
   carried over the Space Packet Protocol on UDP, CoAP with OSCORE, and
   HTTP/3.  It adds one grant field, with which a principal writes in
   advance the actions an agent may take during that silence and the
   interval in which it may take them.  It states which way an unknown
   revocation check fails for each action class, and it adds one
   declared bound, a second revocation latency budget for the grants
   that field marks, beside the one budget the profile it builds on has
   a deployment declare.
- **draft-nandakumar-oauth-actor-bound-token-exchange-00** (new-draft, score 5, authorization) [none]: [OAuth 2.0 Token Exchange with Actor-Bound Tokens](https://datatracker.ietf.org/doc/draft-nandakumar-oauth-actor-bound-token-exchange/) — In OAuth 2.0 Token Exchange, the client that sends the request
   receives the token, and with DPoP the token is bound to the key that
   signed the client's proof.  Agent systems often need one party to
   obtain a token for another: an orchestrating agent that approves an
   action obtains a token for the agent that will perform it.  This
   document lets a token exchange client request that the issued token
   be bound to the key of the actor named in the request, and requires
   the actor to prove possession of that key, so that the token is
   usable only by the actor and only with its consent.
- **draft-nestorov-scitt-p10-underdetermination-03** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Adjudication Statements over SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming P10
   Adjudication Statement carries two canonical witness worlds that are
   compatible with the same closed evidence set and produce different
   values for the same frozen claim.  The witness result is checked
   against committed profile semantics and bound into a SCITT
   Transparent Statement containing an in-toto Statement v1 predicate.
   The result establishes underdetermination only relative to the
   declared profile and does not identify the actual world or establish
   either claim value as true.
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
- **draft-spiriyath-dhc-ai-gateway-uri-00** (new-draft, score 5, adjacent_watchlist) [none]: [DHCP and DHCPv6 Options for an AI Gateway URI](https://datatracker.ietf.org/doc/draft-spiriyath-dhc-ai-gateway-uri/) — This document specifies a DHCPv4 option and a DHCPv6 option that
   carry the HTTPS URI of an AI gateway descriptor.  The descriptor is a
   Provisioning Domain Additional Information document.  It identifies a
   forward proxy and the destinations for which that proxy is to be
   used.  The DHCP options do not carry proxy credentials, model
   identifiers, or a Proxy Auto-Configuration script.
- **draft-srivastava-agentproto-handoff-context-02** (new-draft, score 5, agent_identity) [none]: [Signed Handoff Context for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-srivastava-agentproto-handoff-context/) — When one agent hands a task to another, the receiver needs to know
   who handed it over, on whose behalf, through which earlier agents,
   and which prior context the work depends on.  It needs to know the
   handoff is fresh and meant for it, and the sender needs a clear
   answer back.  This document defines a small, transport-neutral
   handoff context: a signed offer, a signed status reply, and the chain
   of earlier offers that led to the current one, in CDDL for JSON and
   CBOR, with a lifecycle that maps to Agent2Agent task states.  Each
   offer names the one before it by hash, so a dropped or reordered
   intermediate hop is detectable when the chain is carried.  Prior
   context is named by digest only.  The document is input to the
   agentproto working group's use cases and dialog-context work.
- **draft-taylor-cose-receipts-rfc9162-sha384-sha512-00** (new-draft, score 5, verifiable_claims) [none]: [SHA-384 and SHA-512 Binary Merkle Tree Verifiable Data Structures for COSE Receipts](https://datatracker.ietf.org/doc/draft-taylor-cose-receipts-rfc9162-sha384-sha512/) — RFC 9942 defines COSE Receipts and registers one verifiable data
   structure, RFC9162_SHA256, the binary Merkle tree of RFC 9162
   instantiated with SHA-256.  This document registers two more:
   RFC9162_SHA384 and RFC9162_SHA512, the same tree instantiated with
   SHA-384 and SHA-512, each with its inclusion and consistency proof
   types.  The tree construction, proof formats, and verification
   algorithms are unchanged apart from the hash function and the
   resulting digest size.
- **draft-watts-boundary-jurisdiction-architecture-03** (new-draft, score 5, agent_identity) [none]: [Boundary Jurisdiction Architecture for Agentic and Delegated Systems](https://datatracker.ietf.org/doc/draft-watts-boundary-jurisdiction-architecture/) — This document describes a protocol-neutral architecture for
   separating possession of capability from jurisdiction over
   consequential authority boundaries.  It models authority as
   reachability in a time-indexed capability graph, defines revocation
   cuts, and specifies fail-closed semantics for delegation and
   revocation closure.
- **draft-watts-gov-verification-promotion-boundaries-02** (new-draft, score 5, agent_identity) [none]: [Government-Oriented Verification Promotion Boundaries for Agentic Assurance Profiles](https://datatracker.ietf.org/doc/draft-watts-gov-verification-promotion-boundaries/) — Government and critical-infrastructure relying parties require
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
- **draft-watts-mica-nex-measurement-ingestion-01** (new-draft, score 5, adjacent_watchlist) [none]: [MICA-NEX v0.3: Authenticated Measurement Ingestion for Model-Agnostic Nano-Instrument Agent Swarms](https://datatracker.ietf.org/doc/draft-watts-mica-nex-measurement-ingestion/) — This document describes a narrow, testable next step in the MICA-NEX
   proposal: cryptographically binding nanoscale instrument measurement
   claims to externally provisioned acquisition and calibration signer
   roles while denying model planners the ability to self-certify
   measurement status.  The reference implementation uses Ed25519
   signatures, SHA-256 content binding, typed units, time windows,
   source-kind separation, and a persistent local replay ledger.  In a
   hardware-disconnected test harness, 60/60 signed synthetic test
   records from three simulated instrument classes were admitted and
   30/30 adversarial cases were rejected for the expected reason; 28/28
   Python tests passed.  No instrument, laboratory calibration, external
   reviewer, clinical context or independent physical replication was
   involved.  Signature validity is deliberately distinguished from
   scientific validity.
- **draft-watts-scientific-admissibility-evidence-02** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Admissibility Evidence Records for Verifiable Research Provenance](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility-evidence/) — This document describes a portable JSON evidence-record format for
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
- **draft-watts-scientific-constitutional-evidence-00** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Constitutional Law: Evidence and Authority Boundaries for Networked Research](https://datatracker.ietf.org/doc/draft-watts-scientific-constitutional-evidence/) — This document proposes Scientific Constitutional Evidence Gates
   (SCEG), a JSON exchange profile for recording and evaluating whether
   evidence-bearing research claims may cross a declared governance
   boundary.  It specifies typed evidence states, an explicit transition
   decision procedure, provenance and policy bindings, and independently
   verifiable receipts.  The design prevents integrity checks,
   structural conformance, or matching scientific invariants from being
   silently promoted into scientific truth, independent reproduction, or
   institutional authority.

   The term "constitutional law" denotes internal, machine-checkable
   governance constraints; this proposal does not create state law,
   legal rights, institutional authority, scientific certification, or
   IETF consensus.  It is an individual Informational Internet-Draft
   intended to support interoperable, falsifiable research workflows.
- **draft-xg-payment-dispute-profile-02** (new-draft, score 5, trust_infrastructure) [none]: [Card-Scheme Dispute Evidence Profile of Signed Decision Receipts](https://datatracker.ietf.org/doc/draft-xg-payment-dispute-profile/) — In an agent-initiated payment dispute, the payer, the merchant, the
   payment service provider and the agent operator each keep their own
   record of the same decision, and none of those records can be
   verified by the other parties.  This document states that problem and
   defines a signed dispute receipt, registrable as the payload of a
   SCITT Signed Statement, that binds the decision to card-scheme
   dispute-evidence categories, to the agent's delegated scope, to the
   settlement that actually occurred, and to an evidentiary-custody
   record, so that parties with opposed interests can verify the same
   evidence offline.
- **draft-xu-efficient-agent-discovery-profile-01** (new-draft, score 5, adjacent_watchlist) [none]: [Metadata and Query Profile for Efficient Agent Discovery](https://datatracker.ietf.org/doc/draft-xu-efficient-agent-discovery-profile/) — This document defines a metadata and query profile for efficient
   discovery of autonomous software agents.  The profile describes how
   agents publish capability metadata using explicit tags, natural-
   language descriptions, example tasks, protocol bindings, and
   operational constraints.  It also defines JSON metadata, discovery
   request, and discovery response objects that enable discovery
   services to combine structured filtering, semantic retrieval, and
   fine-grained matching while preserving an interoperable protocol
   surface.

   The profile does not mandate a specific machine-learning model,
   embedding model, database, or ranking algorithm.  Instead, it
   standardizes the metadata and result evidence needed by clients and
   discovery services so that different implementations can interoperate
   while optimizing their own latency, scalability, and ranking quality.
- **draft-bonica-macneil-singh-ipv6-firewall-metadata-01** (new-draft, score 4, adjacent_watchlist) [none]: [Verifiable Firewall and Security-Enforcement Metadata in IPv6](https://datatracker.ietf.org/doc/draft-bonica-macneil-singh-ipv6-firewall-metadata/) — This document defines a way to carry a verifiable record of security
   enforcement inside IPv6 packets.  Each firewall (or other security
   enforcement point) that handles a packet writes a small,
   authenticated note saying which rule it matched and what action it
   took.  The notes are protected by a chained Integrity Check Value
   (ICV), reusing the construction defined for In-situ OAM (IOAM) data
   integrity.  A checker can then prove two separate things: that the
   notes are authentic (not forged or changed on the way), and that the
   recorded actions match the intended policy.  Because the two checks
   are independent, a firewall that honestly diverges from policy -- for
   example because of a stale rule or an implementation bug -- still
   produces an authentic note, and the divergence is reported rather
   than hidden.  Operators thus gain precise per-hop evidence that every
   enforcement point was traversed and applied the intended policy, so
   an EP that was skipped or did not enforce is revealed.
- **draft-ietf-jose-json-proof-token-15** (new-draft, score 4, privacy_security) [jose]: [JSON Proof Token and CBOR Proof Token](https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/) — JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving
   representation of claims to be transferred between three parties.
   The claims in a JPT are encoded as base64url-encoded JSON objects
   that are used as the payloads of a JSON Web Proof (JWP) structure,
   enabling them to be digitally signed and selectively disclosed.  JPTs
   also support reusability and unlinkability when using Zero-Knowledge
   Proofs (ZKPs).

   A CBOR-based representation of JPTs is also defined, called a CBOR
   Proof Token (CPT).  It has the same properties as JPTs, but uses the
   JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based
   JWP Compact Serialization.
- **draft-ietf-keytrans-architecture-12** (new-draft, score 4, trust_infrastructure) [keytrans]: [Key Transparency Architecture](https://datatracker.ietf.org/doc/draft-ietf-keytrans-architecture/) — This document defines the terminology and interaction patterns
   involved in the deployment of Key Transparency (KT) in end-to-end
   encrypted communication services, and specifies the security
   properties that KT provides.  It also gives more general, non-
   prescriptive guidance on how to securely apply KT to a number of
   common applications.
- **draft-kelley-aipref-training-preference-signal-01** (new-draft, score 4, adjacent_watchlist) [none]: [Machine-Readable Training Preference Signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) — This document describes how a service operator binds usage
   preferences (e.g., "no AI training") to paths by writing ordinary
   robots.txt groups keyed by a per-purpose policy token in the User-
   Agent line.  It introduces no new directive names and no new grammar:
   the path language, longest-match precedence, and group structure of
   robots.txt are not changed.
- **draft-oga-musubi-settlement-03** (new-draft, score 4, adjacent_watchlist) [none]: [MUSUBI Settlement: Recomputing Whether an Agent Acted Within a Signed Grant](https://datatracker.ietf.org/doc/draft-oga-musubi-settlement/) — MUSUBI settlement is a deterministic function that takes a contract
   signed by two parties, a set of signed records of what an agent did
   under that contract, and a view of Bitcoin block headers, and
   computes whether the recorded acts stayed within the grant the
   contract gives.  Anyone holding the same bytes can recompute the
   result without trusting the party that produced it.  This document
   specifies one well defined part of that function, settle core v0,
   precisely enough that a second implementation can be written from the
   text and the published test vectors alone.  Outside settle core v0,
   it also describes the admission record of version 0.4, in which a
   relying party states the check it made of a request's content by
   digests and marks, and how settle v1.19 reads it.  Settlement is not
   runtime enforcement and is not a judgement of liability.
- **draft-ovalles-ai-terms-03** (new-draft, score 4, adjacent_watchlist) [none]: [AI Terms: Per-Use Terms, Payment and Receipts for Automated AI Access to Web Content](https://datatracker.ietf.org/doc/draft-ovalles-ai-terms/) — This document defines AI Terms: a JSON document published at the
   well-known URI /.well-known/ai-terms in which a website states, for
   each of four uses of its content by automated AI systems (search,
   answer, training and agent), whether the use is allowed, allowed for
   a price, or not allowed.  Each use corresponds to one category of the
   IETF AI Preferences vocabulary, and the document defines how a site's
   terms are written, conservatively, as AI Preferences statements (the
   Content-Usage header field and robots.txt rule) for clients that read
   only those.  AI Terms extends the AI Preferences work with what it
   leaves out: a price and a free allowance, a payment binding (HTTP
   402, with x402 as the first), a purpose declaration by the client
   (the AI-Purpose header field), a description of a paid page that the
   payment depends on, and a receipt that records the use.

## Adjacent / watchlist

- **draft-agentproto-context-management-architecture-01** (new-draft, score 3, agent_identity) [none]: [Context and Correlation Management Architecture for Distributed Agentic Activities](https://datatracker.ietf.org/doc/draft-agentproto-context-management-architecture/) — Agentic applications increasingly distribute objectives across
   autonomous agents, tools, and services operating across different
   protocols and administrative domains.  A single Activity may involve
   multiple independently maintained Dialogs, Tasks, Events, and
   Resources, spanning different modalities and extended periods of
   time.

   Existing protocols provide identifiers and context-management
   mechanisms for their own interactions, but these do not necessarily
   support correlation across Dialogs, protocols, and administrative
   boundaries, particularly as interactions evolve, branch, or resume
   over time.

   This document defines a context-and-correlation architecture based on
   Activities, Dialogs, Tasks, Resources, and typed Relationships.  It
   describes how management and correlation metadata can be maintained
   and selectively propagated to preserve coherent context across
   distributed interactions, while allowing participants to determine
   the scope of correlations they share and manage.
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
- **draft-bkayranci-x-forwarded-prefix-00** (new-draft, score 3, adjacent_watchlist) [none]: [The X-Forwarded-Prefix HTTP Header Field](https://datatracker.ietf.org/doc/draft-bkayranci-x-forwarded-prefix/) — This document specifies the X-Forwarded-Prefix HTTP header field, a
   widely deployed de-facto standard used by reverse proxies, API
   gateways, load balancers, and ingress controllers to communicate the
   original URI path prefix that was stripped, rewritten, or matched
   prior to forwarding a request to an upstream service.  Standardizing
   this header provides normative behavior across HTTP intermediaries
   and origin servers, enabling upstream applications to reliably
   reconstruct original client-facing target URIs, issue accurate HTTP
   redirects, generate self-referential hypermedia links, configure
   application base paths, and mitigate security vulnerabilities arising
   from improper path handling and header injection.  Furthermore, this
   document establishes the requirement for reverse proxy
   implementations to emit this header unless explicitly configured
   otherwise, specifies deterministic prefix concatenation for multi-
   proxy chaining, defines strict percent-encoding preservation,
   establishes atomic trust boundaries for the forwarded header family,
   specifies structured field mapping in accordance with RFC 9651, and
   registers the field in the IANA HTTP Field Name Registry along with
   an extension parameter for the RFC 7239 Forwarded header.
- **draft-chuang-feedback-id-header-00** (new-draft, score 3, core_identity) [none]: [Feedback-id Email Header Field](https://datatracker.ietf.org/doc/draft-chuang-feedback-id-header/) — Large-volume email senders and Email Service Providers (ESPs) use
   Feedback Loops (FBLs) to identify campaigns in their traffic that
   generate a high volume of spam complaints from recipients and to
   detect abuse of their services.  Traditional per-message complaint
   reports can expose individual recipient actions, creating privacy
   concerns.  This document specifies the "Feedback-ID" email header
   field, which allows senders to embed structured campaign, customer,
   mail-type, and sender identifiers in outbound messages.  Receiving
   mailbox providers authenticate this header field using DomainKeys
   Identified Mail (DKIM) and report aggregated spam complaint rates per
   identifier back to verified senders without disclosing individual
   recipient data.
- **draft-claise-green-capability-discovery-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-ek-tiptop-ipn-allocator-prefixes-01** (new-draft, score 3, core_identity) [none]: [IPv6 Prefixes Derived from IPN Allocator Identifiers](https://datatracker.ietf.org/doc/draft-ek-tiptop-ipn-allocator-prefixes/) — This document requests an IPv6 /16 prefix for use by IPN Allocators.
   It defines a method to derive an IPv6 /48 prefix from a 32-bit IPN
   Allocator Identifier.  Use of the derived prefix is optional.  The
   method reuses the existing IPN Allocator registry.  It does not
   encode physical location or define a routing mechanism.  The
   preferred /16 prefix is 5f01::/16.  This document also updates RFC
   4291 to permit other interface identifier lengths within the
   allocated block.
- **draft-enger-httpbis-http4-wiqc-00** (new-draft, score 3, core_identity) [none]: [HTTP/4: Mapping HTTP Semantics over the WIQC Decentralized Real-Time Torrent Transport Protocol](https://datatracker.ietf.org/doc/draft-enger-httpbis-http4-wiqc/) — This document specifies HTTP/4, an application-layer mapping of HTTP
   semantics over a decentralized, peer-to-peer real-time streaming
   transport protocol named WIQC (Web-Integrated QUIC-derived Content-
   swarming).  By design, the HTTP/4 protocol allows decentralized real-
   time streaming via a torrent protocol called not QUIC but WIQC.
   While HTTP/3 delegates stream multiplexing and congestion control to
   unicast client-server QUIC connections, HTTP/4 extends these
   capabilities to multipoint peer swarms.  WIQC integrates encrypted
   UDP stream multiplexing with fine-grained cryptographic block
   verification using SHA-256 Merkle hash trees, live sliding-window
   chunk addressing, Unified Merkle Tree signatures for low-latency live
   streams, mutual peer authentication without centralized certificate
   authorities, and native UDP hole punching.  This specification
   defines the wire framing, stream mapping, swarm discovery headers,
   real-time object prioritization, and security properties required to
   operate HTTP/4 natively across decentralized networks.
- **draft-gong-spring-sr-policy-group-yang-05** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for SR Policy Group](https://datatracker.ietf.org/doc/draft-gong-spring-sr-policy-group-yang/) — This document defines a YANG data model for Segment Routing (SR)
   Policy Group that can be used for configuring, instantiating, and
   managing SR Policy groups.  The model is generic and applies equally
   to the MPLS and SRv6 instantiations of SR Policy groups.
- **draft-hopley-x402-refund-receipt-03** (new-draft, score 3, agent_identity) [none]: [Categorical Refund Receipt Format for Agentic-Payment Flows](https://datatracker.ietf.org/doc/draft-hopley-x402-refund-receipt/) — This document specifies a categorical refund receipt format for
   agentic-payment flows.  The format is the post-settlement counterpart
   to the admission-time compliance receipt format specified in draft-
   hopley-x402-compliance-receipt: where the compliance receipt records
   an admission decision under regulatory screening obligations, the
   refund receipt records a reversal-of-funds event with the same
   canonicalisation discipline and the same audit-chain semantics.

   The receipt format uses a closed enumeration of categorical outcomes
   (FULL, PARTIAL, REJECTED) rather than a continuous percentage or
   amount-only representation.  The categorical outcome is load-bearing
   for downstream regulatory obligations: under PSD2 (Directive
   2015/2366) Article 89 a REJECTED outcome carries dispute-evidence
   obligations that a PARTIAL refund does not, and the categorical
   distinction must be preserved at the canonical-bytes level rather
   than collapsed to a percentage projection of the original amount.

   Receipts are canonicalised under RFC 8785 (JSON Canonicalization
   Scheme) with an in-band canonicalisation rule pin (canon_version).
   The pin enables year-N re-verification from retained bytes alone,
   without dependence on an out-of-band rule registry that the operator
   must continue to publish.

   The refund receipt format composes with the compliance receipt format
   via the original_payment_ref field, a content-addressed reference to
   the original payment record.  A verifier walking the audit chain can
   confirm the full payment lifecycle from admission-time screening
   through settlement to refund event under one byte-deterministic
   canonicalisation pin.

   This document is complementary to draft-vauban-x402-stark-receipts
   (which covers cryptographic settlement-time payment-condition proofs)
   and to draft-hopley-x402-compliance-receipt (which covers admission-
   time compliance screening receipts).  The three documents pin the
   same urn:x402:canonicalisation:jcs-rfc8785-v1 canonicalisation
   discipline.
- **draft-hopley-x402-settlement-anchoring-00** (new-draft, score 3, agent_identity) [none]: [Chain-Agnostic Anchoring of Canonical Settlement References for Agentic Payments](https://datatracker.ietf.org/doc/draft-hopley-x402-settlement-anchoring/) — This document specifies how a canonical content-addressed settlement
   reference is anchored into a transaction on any blockchain, uniformly
   across chain families, so that the same agentic-payment settlement
   can be recorded on-chain and later verified offline from the
   transaction bytes alone.

   The settlement reference is a SHA-256 digest over the JSON
   Canonicalization Scheme (JCS, RFC 8785) form of a settlement record.
   This document does not redefine the digest; it defines (1) a chain
   identification rule that rejects ambiguous chain names before a
   settlement is bound to a network, and (2) a family-uniform anchor
   encoding that places the reference in the one field each chain family
   makes available for opaque data (EVM calldata or a log topic, an SVM
   memo, an AVM note, a UTXO OP_RETURN output, or a generic metadata
   carrier).  The anchor carries only the digest; it carries no party
   identifiers, amounts, or personal data in cleartext.

   Because the reference is content-addressed and the encoding is fixed
   per family, any holder of the settlement record can recompute the
   reference, read the anchor from the on-chain field, and confirm the
   two match with no call to the settling party and no chain-specific
   verification logic beyond reading one field.
- **draft-ietf-bess-extended-evpn-optimized-ir-10** (new-draft, score 3, core_identity) [bess]: [Extended Procedures for EVPN Optimized Ingress Replication](https://datatracker.ietf.org/doc/draft-ietf-bess-extended-evpn-optimized-ir/) — In the Virtualization Overlay (NVO) network with Ethernet VPN (EVPN),
   optimized ingress replication uses Assisted-Replication (AR) to
   achieve more efficient delivery of Broadcast and Multicast (BM)
   traffic.  An AR-LEAF, which is a Network Virtualization Edge (NVE)
   device, forwards received BM traffic from its tenant system to an AR-
   REPLICATOR.  The AR-REPLICATOR then replicates it to the remaining
   AR-LEAFs in the network.  However, when replicating the packet on
   behalf of its multihomed AR-LEAF, an AR-REPLICATOR may face
   challenges in retaining the source IP address or including the
   expected Ethernet Segment Identifier (ESI) label that is required for
   EVPN split-horizon filtering.  This document extends the optimized
   ingress replication procedures to address such limitations.  The
   extended procedures specified in this document allow the support of
   EVPN multihoming on the AR-LEAFs as well as optimized ingress
   replication for the rest of the EVPN NVO network.
- **draft-ietf-calext-jscalendarbis-23** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-cbor-serialization-13** (new-draft, score 3, adjacent_watchlist) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — RFC 8949 defines CBOR, a standard for serializing data types such as
   integers, strings, and arrays into encoded bytes.  CBOR serialization
   is flexible, allowing data types to be encoded in multiple ways to
   accommodate deployment in constrained environments.

   This document introduces the term “general serialization” for the
   full set of encodings permitted by RFC 8949, and formally defines two
   specific serializations: preferred-plus serialization, which differs
   from preferred serialization only in cases rarely encountered in
   practice and is recommended for broad use; and deterministic
   serialization, which likewise differs only in rarely encountered
   cases from core deterministic encoding defined in RFC 8949.

   This document updates RFC 8949 with a new rule that limits how new
   tag definitions can affect the CBOR data model.

   This document provides clarifications to RFC 8949 regarding bignums
   and floating-point NaN handling, along with general background
   information on serialization, determinism, and CBOR byte-string
   wrapping.
- **draft-ietf-ccamp-rfc8561bis-01** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for Microwave Radio Link](https://datatracker.ietf.org/doc/draft-ietf-ccamp-rfc8561bis/) — This document defines a YANG data model for control and management of
   radio link interfaces and their connectivity to packet (typically
   Ethernet) interfaces in a microwave/millimeter wave node.  The data
   nodes for management of the interface protection functionality is
   broken out into a separate and generic YANG data model in order to
   make it available for other interface types as well.  This document
   obsoletes RFC 8561.
- **draft-ietf-cose-c509-test-vectors-05** (new-draft, score 3, adjacent_watchlist) [cose]: [Test Vectors for CBOR-Encoded X.509 (C509) Certificates](https://datatracker.ietf.org/doc/draft-ietf-cose-c509-test-vectors/) — This document contains examples of CBOR-encoded X.509 (C509)
   certificates, certification requests, and certification request
   templates.
- **draft-ietf-detnet-glbf-04** (new-draft, score 3, adjacent_watchlist) [detnet]: [Deterministic Networking (DetNet) Data Plane - guaranteed Latency Based Forwarding (gLBF) for bounded latency with low jitter and asynchronous forwarding in Deterministic Networks](https://datatracker.ietf.org/doc/draft-ietf-detnet-glbf/) — This memo proposes a mechanism called "guaranteed Latency Based
   Forwarding" (gLBF) as part of DetNet for hop-by-hop packet forwarding
   with per-hop deterministically bounded latency and minimal jitter.

   gLBF is intended to be useful across a wide range of networks and
   applications that need high-precision deterministic networking
   services, from in-car networks and networks for industrial automation
   on factory floors all the way to country-wide networks at 100 Gbps
   and beyond.

   Unlike other mechanisms, gLBF does not require network-wide clock
   synchronization, nor does it require per-flow state on network nodes.
   It thereby avoids the drawbacks of other known methods while
   retaining their advantages.

   Specifically, gLBF uses the queuing model and calculus of Urgency
   Based Scheduling (UBS, [UBS]), which is used by TSN Asynchronous
   Traffic Shaping [TSN-ATS]. gLBF is intended as a plug-in replacement
   for, or a mechanism in parallel to, TSN-ATS, because it allows reuse
   of the same controller-plane design that selects paths for TSN-ATS,
   sizes TSN-ATS queues, calculates latencies and admits flows onto the
   calculated paths with the calculated latencies.

   In addition to reducing jitter compared to TSN-ATS through additional
   buffering (dampening) in the network, gLBF also eliminates the per-
   flow, per-hop state maintenance required by TSN-ATS.  This avoids
   having to signal per-flow state from the controller-plane to every
   hop, and the associated scaling problems.  It also reduces the
   implementation cost of high-speed networking hardware, because it
   avoids the additional high-speed read/write memory accesses needed to
   retrieve, process and update per-flow state variables for a large
   number of flows.
- **draft-ietf-dmm-udp-tunnel-acaas-extn-04** (new-draft, score 3, adjacent_watchlist) [dmm]: [A YANG Data Model Extension for Attachment Circuit as a Service with UDP Tunnel Support](https://datatracker.ietf.org/doc/draft-ietf-dmm-udp-tunnel-acaas-extn/) — Delivery of network services over a Layer 3 tunnel assumes that the
   appropriate setup is provisioned over links that connect the customer
   termination points and provider network.  The required setup to allow
   successful data exchange over these links is referred to as an
   attachment circuit (AC) while the underlying link for carrying
   network services is referred to as "bearer", in this case a Layer 3
   UDP tunnel.

   This document specifies an extension for UDP tunnel as Layer 3 bearer
   to the YANG service data model for AC.
- **draft-ietf-dtn-bpsec-cose-19** (new-draft, score 3, verifiable_claims) [dtn]: [Bundle Protocol Security (BPSec) COSE Context](https://datatracker.ietf.org/doc/draft-ietf-dtn-bpsec-cose/) — This document defines a security context suitable for using CBOR
   Object Signing and Encryption (COSE) algorithms within Bundle
   Protocol Security (BPSec) integrity and confidentiality blocks.  A
   profile for COSE, organized by algorithm families, and for public key
   certificates are included for BPSec interoperation.

   This document updates BPSec RFC 9172 by providing Concise Data
   Definition Language (CDDL) rules for extensible security block
   content.
- **draft-ietf-green-power-and-energy-yang-06** (new-draft, score 3, adjacent_watchlist) [green]: [Power and Energy YANG Module](https://datatracker.ietf.org/doc/draft-ietf-green-power-and-energy-yang/) — This document defines a YANG data model for Power and Energy
   monitoring and control of devices within or connected to
   communication networks.
- **draft-ietf-httpapi-ratelimit-headers-12** (new-draft, score 3, adjacent_watchlist) [httpapi]: [RateLimit header fields for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) — This document defines the RateLimit-Policy and RateLimit HTTP header
   fields for servers to advertise their quota policies and the current
   service limits, thereby allowing clients to shape their requests to
   avoid exceeding server-imposed limits.  It also defines problem types
   that servers can use to inform clients about quota-related
   conditions.
- **draft-ietf-httpbis-no-vary-search-11** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
- **draft-ietf-jmap-calendars-34** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-jmap-tasks-07** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Task Lists](https://datatracker.ietf.org/doc/draft-ietf-jmap-tasks/) — This document specifies a data model for synchronizing task data with
   a server using JMAP.  Clients can use this to efficiently read,
   write, and share task lists, receive push notifications for changes
   or task reminders, and keep track of changes made by others in a
   multi-user environment.
- **draft-ietf-kitten-pkinit-crypto-deprec-00** (new-draft, score 3, adjacent_watchlist) [kitten]: [Deprecation of Outdated Cryptographic Algorithms and Parameters in Kerberos PKINIT](https://datatracker.ietf.org/doc/draft-ietf-kitten-pkinit-crypto-deprec/) — This document deprecates several outdated cryptographic algorithms
   and parameters from the Kerberos PKINIT specification (RFC 4556) and
   its extensions (RFC 5349, RFC 8636).  Specifically, it deprecates the
   RSA key transport mechanism for reply key delivery, the Diffie-
   Hellman MODP group 2 (1024-bit) parameter, the SHA-1-based
   octetstring2key key derivation function, and the
   sha1WithRSAEncryption CMS signature algorithm.  It also defines a new
   paChecksum2 field in the PKAuthenticator structure to provide
   checksum algorithm agility.

   This document updates RFC 4556, RFC 5349, and RFC 8636.
- **draft-ietf-mpls-mldp-yang-17** (new-draft, score 3, adjacent_watchlist) [mpls]: [A YANG Data Model for MPLS mLDP](https://datatracker.ietf.org/doc/draft-ietf-mpls-mldp-yang/) — This document specifies a YANG data model for the Multiprotocol Label
   Switching (MPLS) Multipoint Label Distribution Protocol (mLDP).  The
   mLDP YANG data model augments the MPLS LDP YANG data model.

   The YANG modules in this document conform to the Network Management
   Datastore Architecture (NMDA).
- **draft-ietf-netconf-udp-notif-27** (new-draft, score 3, adjacent_watchlist) [netconf]: [UDP-based Transport for Configured Subscriptions](https://datatracker.ietf.org/doc/draft-ietf-netconf-udp-notif/) — This document describes a UDP-based transport for YANG notifications
   to collect data from network nodes within a controlled environment.
   A shim header is defined to facilitate the data streaming directly
   from a publishing process on a network device to telemetry receivers.
   Such a design enables higher frequency updates and less performance
   overhead on publisher and receiver processes compared to already
   established notification mechanisms.  A YANG data model is also
   defined for management of the described UDP-based transport.
- **draft-ietf-netconf-yp-transport-capabilities-08** (new-draft, score 3, adjacent_watchlist) [netconf]: [YANG Notification Transport Capabilities](https://datatracker.ietf.org/doc/draft-ietf-netconf-yp-transport-capabilities/) — This document specifies a YANG module for discovering transport
   capabilities for YANG notifications.  The module augments the YANG
   notifications capabilities model with capabilities for the
   notification transport protocol, transport encoding, and transport
   encryption.  The capabilities enable a client to determine the
   notification transport options supported by a NETCONF or RESTCONF
   server at runtime or at implementation time using the YANG instance
   data file format.
- **draft-ietf-openpgp-persistent-symmetric-keys-05** (new-draft, score 3, core_identity) [openpgp]: [Persistent Symmetric Keys in OpenPGP](https://datatracker.ietf.org/doc/draft-ietf-openpgp-persistent-symmetric-keys/) — This document defines a new packet and algorithm for the OpenPGP
   standard (RFC 9580) to support persistent symmetric keys, for message
   encryption using authenticated encryption with additional data (AEAD)
   and for message authentication using AEAD authentication tags.  This
   enables the use of symmetric cryptography for data storage (and other
   contexts that do not require asymmetric cryptography), for improved
   performance, smaller keys, and improved resistance to quantum
   computing.
- **draft-ietf-opsawg-collected-data-manifest-17** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push (RFC
   8641), to continuously stream information, including both counters
   and state information.  This document describes the metadata that
   ensure that the collected data can be interpreted correctly.  This
   document specifies the Data Manifest, composed of two YANG data
   models (the Platform Manifest and the non-normative Data Collection
   Manifest).  These YANG modules are specified at the network level
   (e.g., network controllers) to provide a model that encompasses
   several network platforms.  The Data Manifest must be streamed and
   stored along with the data, up to the collection and analytics
   systems to keep the collected data fully usable by the data
   scientists and relevant tools.  Additionally, this document specifies
   an augmentation of the YANG-Push model to include the actual
   collection period, in case it differs from the configured collection
   period.
- **draft-ietf-pce-stateful-pce-autobw-update-07** (new-draft, score 3, adjacent_watchlist) [pce]: [Update to the Automatic Bandwidth Adjustment Procedure for MPLS-TE and SR-TE LSPs with a Stateful PCE](https://datatracker.ietf.org/doc/draft-ietf-pce-stateful-pce-autobw-update/) — Extensions for the stateful PCE model enable control of Traffic
   Engineering (TE) LSPs using the Path Computation Element
   Communication Protocol (PCEP) for RSVP-TE and Segment Routing (SR),
   for both PCE-initiated and PCC-initiated LSPs.

   RFC 8733 defines PCEP extensions for automatically adjusting
   bandwidth on MPLS-TE Label Switched Paths (LSPs) using a stateful
   PCE.  This document applies the PCEP extensions for automatic
   bandwidth adjustment to SR-TE LSPs in both the MPLS (SR-MPLS) and
   IPv6 (SRv6) data planes.  It also applies these PCEP extensions to
   multipath LSPs defined in RFC 10066.

   RFC 8733 defines the AUTO-BANDWIDTH-ATTRIBUTES TLV and a set of sub-
   TLVs for the attributes.  A sub-TLV is included when its value
   differs from the value last sent in a PCEP message.  However, RFC
   8733 lacks a mechanism to explicitly remove an attribute identified
   by a sub-TLV.  This document updates RFC 8733 by defining such a
   mechanism.
- **draft-ietf-sidrops-aspa-verification-31** (new-draft, score 3, authorization) [sidrops]: [BGP AS_PATH Verification Based on Autonomous System Provider Authorization (ASPA) Objects](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) — This document describes procedures that make use of Autonomous System
   Provider Authorization (ASPA) objects in the Resource Public Key
   Infrastructure (RPKI) to verify the Border Gateway Protocol (BGP)
   AS_PATH attribute of advertised routes.  This AS_PATH verification
   enhances routing security by adding means to detect and mitigate
   route leaks and AS_PATH manipulations.
- **draft-ietf-spring-stamp-srpm-srv6-11** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths including Segment Lists of SR Policies, SRv6 IGP
   best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SRv6.
- **draft-ietf-sshm-cert-03** (new-draft, score 3, core_identity) [sshm]: [SSH Certificate Format](https://datatracker.ietf.org/doc/draft-ietf-sshm-cert/) — This document presents a lightweight certificate format that may be
   used in the context of the Secure Shell (SSH) protocol for user and
   host authentication.
- **draft-ietf-tls-pake-03** (new-draft, score 3, adjacent_watchlist) [tls]: [A Password Authenticated Key Exchange Extension for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-pake/) — The pre-shared key mechanism available in TLS 1.3 is not suitable for
   usage with low-entropy keys, such as passwords entered by users.
   This document describes an extension that enables the use of
   password-authenticated key exchange protocols with TLS 1.3.
- **draft-ietf-tsvwg-sctp-dtls-chunk-07** (new-draft, score 3, core_identity) [tsvwg]: [Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/) — This document describes a method for adding Datagram Transport Layer
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
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-33** (new-draft, score 3, adjacent_watchlist) [v6ops]: [Framework for Multi-domain IPv6-only Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — This document presents a framework, from the network operators'
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
- **draft-irtf-cfrg-bbs-signatures-15** (new-draft, score 3, adjacent_watchlist) [cfrg]: [The BBS Signature Scheme](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) — This document describes the BBS Signature scheme, a secure, multi-
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
- **draft-irtf-cfrg-frodokem-security-considerations-00** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Security Considerations for FrodoKEM](https://datatracker.ietf.org/doc/draft-irtf-cfrg-frodokem-security-considerations/) — ISO standardized FrodoKEM in June 2026 [ISO18033-2-AMD2].  This
   document provides security guidance for FrodoKEM for use in
   protocols.  It explains what security claims protocol designers may
   rely on, what assumptions and conditions are required, what parameter
   sets are in scope, and what implementors need to do to use FrodoKEM
   safely.  The scope follows the current FrodoKEM Internet-Draft
   [I-D.FrodoKEM].
- **draft-irtf-cfrg-ml-kem-security-considerations-01** (new-draft, score 3, adjacent_watchlist) [cfrg]: [ML-KEM Security Considerations](https://datatracker.ietf.org/doc/draft-irtf-cfrg-ml-kem-security-considerations/) — NIST standardized ML-KEM as FIPS 203 in August 2024.  This document
   discusses how to use ML-KEM within protocols - that is, what problem
   it solves, and what you need to do to use it securely.
- **draft-janz-onsen-cognitive-reconciliation-00** (new-draft, score 3, adjacent_watchlist) [none]: [Cognitive Reconciliation for YANG and TM Forum Model Interoperability](https://datatracker.ietf.org/doc/draft-janz-onsen-cognitive-reconciliation/) — Network operators must make YANG-modeled service and network
   interfaces interoperate with TM Forum (TMF) OSS/BSS APIs.  Today this
   is done with hand-built, model-specific adapters, whose construction
   and maintenance is ongoing human work.  The ONSEN problem statement
   records the absence of a standard alignment between TMF APIs and YANG
   models as an open problem.  This document applies ad hoc semantic
   reconciliation by cognitive agents, as developed in draft-janz-nmrg-
   adhoc-semantic-reconciliation, to that problem.  Two cognitive agents
   lift their respective models, bind through a thin shared reference,
   and each generates and operates its own inbound translator, with no
   model-specific adapter agreed in advance.  This document reports
   results from a demonstrator whose first case reconciles the L3SM
   service model to a TMF representation.  It runs the reconciliation in
   two forms, one anchored on the mapping-root annotations of draft-lls-
   onsen-yang-tmf-mapping, and one with those annotations withheld, in
   which the agents must locate the services themselves in the plain
   model, and the two forms together size what the annotations
   contribute.  It shows the reconciled mapping operating on real
   instance data, shows the model-drift lifecycle by which the
   translators are kept current, reads the demonstrator as an empirical
   point on a cognition-placement spectrum, from over-arching cognition
   over two inert systems to both systems cognitive, and is explicit
   about what over-arching cognition achieves when neither system is
   itself cognitive.  A second case reconciles the L3SM service model to
   the L3NM network model, a cross-abstraction mapping where a cognitive
   counterpart earns its place, so the two cases together give the two
   poles of the spectrum on two ONSEN problem areas.  The document
   closes with recommendations for operational practice and for
   standardization.
- **draft-jones-detached-evidence-examination-00** (new-draft, score 3, core_identity) [none]: [Outerprise Ecosystem and Infrastructure: An Examination Manual for Detached Evidence Delivery](https://datatracker.ietf.org/doc/draft-jones-detached-evidence-examination/) — This document describes repeatable procedures for examining detached
   evidence packets and the signed findings returned by recipients.  It
   identifies the object, criterion, evidence, procedure, observed
   result and limits of each finding.  The procedures cover artifact
   identity, release consistency, consent and access, delivery events,
   benchmark comparisons, commitment openings and policy decisions.
   Synthetic examples illustrate reproducible checks.  The document
   adapts an examination manual into an implementation-neutral method.
- **draft-jones-outerprise-visual-manual-00** (new-draft, score 3, adjacent_watchlist) [none]: [Outerprise Ecosystem and Infrastructure: Visual Manual and Machine-Readable Companion](https://datatracker.ietf.org/doc/draft-jones-outerprise-visual-manual/) — This document presents a visual reference model of the Outerprise
   evidence-delivery ecosystem as documented by the public Entercation
   application.  It identifies participants, public surfaces, packet
   boundaries, fiscal-sponsorship stations, comparison findings and
   policy decisions.  It describes a machine-readable companion with
   structured definitions, schemas, exact arithmetic and synthetic test
   vectors.  The visual model is a documented public-surface view with
   explicit evidence boundaries.
- **draft-kostyk-redoubt-00** (new-draft, score 3, core_identity) [none]: [Redoubt/1: Authorised Control of Modbus-Era PLCs](https://datatracker.ietf.org/doc/draft-kostyk-redoubt/) — This document specifies Redoubt/1, a control channel for programmable
   logic controllers that sits in front of Modbus/TCP and decides, per
   operation, whether a request may reach the controller.  Modbus has no
   authentication, no authorisation and no replay protection; the TLS-
   based Modbus Security profile adds a protected channel but still lets
   any authenticated client invoke any function code.  Redoubt/1 adds a
   decision per operation rather than per connection, a replay window
   that survives a controller reboot, a three-valued outcome that can
   drive outputs to a safe state instead of merely refusing, dual
   control for critical outputs, reversible batches, and an audit chain
   that fails closed.  The decision core is formalised in Lean 4 and
   twenty of its properties are machine-checked; the proof artefacts are
   published with the implementation.
- **draft-lin-idr-bgp-sr-policy-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Model for BGP Segment Routing Policy](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-sr-policy-yang/) — This document defines a YANG data model for the BGP Segment Routing
   (SR) Policy address families (RFC 9830).  The model augments the BGP
   YANG model to add the IPv4 SR Policy (AFI, SAFI = 1, 73) and IPv6 SR
   Policy (AFI, SAFI = 2, 73) address families, including SR Policy-
   specific configuration, the SR Policy RIB, per-neighbor Adj-RIBs, the
   decoded SR Policy candidate path information, such as preference,
   Binding SID, and segment lists, and defines notifications for the
   prefix limit exceeded and candidate path state change events.
- **draft-liu-cadi-03** (new-draft, score 3, adjacent_watchlist) [none]: [Cryptographic Asset Discovery and Inventory](https://datatracker.ietf.org/doc/draft-liu-cadi/) — This document compiles existing Cryptographic Asset Discovery and
   Inventory (CADI) methods and analyzes potential gaps.  It also
   defines a YANG data model that augments the base network inventory
   model with the cryptographic assets of each network element.  The
   data model is aligned with the Cryptography Bill of Materials (CBOM)
   defined in CycloneDX.
- **draft-liu-iotops-pqc-wireguard-01** (new-draft, score 3, core_identity) [none]: [A Post-Quantum Bootstrap Profile for WireGuard](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-wireguard/) — This document specifies a post-quantum bootstrap profile for
   WireGuard.  A mutually authenticated ML-KEM-768 and ML-DSA exchange
   derives a 32-octet preshared key (PSK), verifies key possession, and
   binds it to configured endpoint identities and WireGuard public keys.
   The resulting key is installed through the ordinary WireGuard
   PresharedKey configuration field.

   The profile defines canonical binary control records carried over
   mutually authenticated TLS 1.3 on TCP, with explicit message lengths,
   freshness, state transitions, and failure processing.  Bootstrap
   carries the post-quantum contribution into the WireGuard PSK input;
   it is therefore part of the post-quantum provisioning mechanism.  The
   native WireGuard Noise handshake and transport packet format are
   unchanged.

   This Internet-Draft is a proposal for Standards Track publication.
   It requests an ALPN protocol identifier for the bootstrap carrier.
   The request is pending; this document does not assign a native
   WireGuard packet type or a service port.
- **draft-lnehru-lisp-silenthost-detection-02** (new-draft, score 3, adjacent_watchlist) [none]: [LISP Silent Host Discovery using the Mapping System](https://datatracker.ietf.org/doc/draft-lnehru-lisp-silenthost-detection/) — The on-demand discovery model of the Locator/ID Separation Protocol
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
- **draft-melo-dap-visual-oob-auth-00** (new-draft, score 3, authorization) [none]: [Dynamic Authorization Protocol (DAP): Out-of-Band Visual Transaction Authorization for Untrusted Terminals](https://datatracker.ietf.org/doc/draft-melo-dap-visual-oob-auth/) — This document specifies the Dynamic Authorization Protocol (DAP), an
   Out-of-Band (OOB) visual transaction authorization protocol, used as
   a second factor, for electronic financial transactions initiated on
   untrusted terminals.  The terminal displays a cryptographically
   protected challenge as a Quick Response (QR) code.  A trusted mobile
   device of the user, which needs no network connection, scans the
   code, verifies it with HMAC-SHA-256, shows the transaction details
   for confirmation ("What You See Is What You Sign"), and then reveals
   a one-time authorizer code protected with AES-256.  Each challenge is
   bound to one transaction and expires within 120 seconds.  The
   document also describes the provisioning of the shared key through a
   dual-channel XOR split-key exchange, its activation, and the
   templates used to display transactions.  DAP targets Man-in-the-
   Middle (MITM) and Man-in-the-Browser (MITB) adversaries that control
   the terminal and alter transaction parameters.
- **draft-mih-sokolov-cose-deterministic-encodings-01** (new-draft, score 3, verifiable_claims) [none]: [Deterministic Encodings for COSE](https://datatracker.ietf.org/doc/draft-mih-sokolov-cose-deterministic-encodings/) — A COSE Hash Envelope signs the digest of a preimage, not the preimage
   itself.  When the preimage is the encoding of a structured value,
   such as a CBOR data item, and a verifier holds that value but not the
   bytes that were hashed, the verifier has to encode the value again,
   and the digest matches only if it applies the same deterministic
   encoding as the producer.  RFC 8949 describes more than one such
   encoding for the same content type, and the preimage content type
   does not identify which one was applied.  This document defines a
   COSE Hash Envelope protected-header parameter that identifies the
   encoding, and one value for CBOR content, the text string "dtrm",
   which states that the Core Deterministic Encoding Requirements of RFC
   8949 were applied.
- **draft-morrison-claim-currency-01** (new-draft, score 3, trust_infrastructure) [none]: [Claim Currency: A Read-Time Decay Evaluator and Observation-Gated Re-Assertion Discipline for Concurrent Readers of a Reconciled Substrate](https://datatracker.ietf.org/doc/draft-morrison-claim-currency/) — This memo specifies a read-time freshness evaluator and an
   observation-gated re-assertion discipline for concurrent autonomous
   readers of a single reconciled substrate history.  For every claim
   read from the substrate, a three-state currency band (FRESH, AGING,
   STALE) is derived at read time from the durable history and is never
   stored.  A claim whose derived band is not FRESH MUST NOT be re-
   emitted as current and MUST NOT ground a new durable claim; the sole
   transition back to currency is a fresh observation of the claim's
   basis, and the substrate's append stage enforces that for every
   reader.  The memo specifies the claim-layer consumer that two
   companion specifications, Substrate-Observation as an Alternative to
   Envelope Coordination and the Substrate-Provenance Annotation
   Grammar, each left unspecified.  It composes a read-time-derived
   band, a decay clock measured in missing observations learned from a
   basis's own change cadence, an append-stage rejection of any claim
   citing a basis that is no longer the head of its lineage, and
   observation as the only admissible refresh.  No new substrate is
   standardised; the discipline composes with substrate that already
   exists.
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
- **draft-signes-jmap-tasklists-00** (new-draft, score 3, adjacent_watchlist) [none]: [JSON Meta Application Protocol (JMAP) for Task Lists](https://datatracker.ietf.org/doc/draft-signes-jmap-tasklists/) — This document specifies a data model for synchronizing task data with
   a server using JMAP.  Clients can use this to efficiently read,
   write, and share task lists, receive push notifications for changes
   or task reminders, and keep track of changes made by others in a
   multi-user environment.
- **draft-skyfire-oauth-kyapay-token-exchange-03** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-slutsky-homing-pigeon-04** (new-draft, score 3, authorization) [none]: [Homing Pigeon Message Protocol, Version 1](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon/) — This document specifies the Homing Pigeon message protocol, version
   1: signed JSON job and result objects exchanged over a transport
   binding.  On the email binding, a submitter sends one HMAC-SHA-384
   signed JSON object to a mailbox; a runner polls that mailbox,
   verifies the signature, executes the job, and returns a signed
   result; the other bindings carry the same objects unchanged.  The
   signature is the object's only authorization: a binding may add a
   gate of its own, but no gate replaces it.  The job object is
   protected end to end by per-job AEAD encryption, a required part of
   the protocol: implementations MUST support it, the reference software
   sends encrypted by default, and a receiver refuses a cleartext job
   unless the operator has explicitly enabled cleartext acceptance - in
   the reference software, only by a command-line parameter.  The store-
   and-forward bindings open no inbound listener on the host that runs
   the job.

   The DTLS binding changes the binding and not the messages: the same
   signed objects travel inside a direct DTLS 1.3 session between the
   submitter and the runner.  It is a binding of version 1, not a new
   version of the protocol.  The shared secret is the session's external
   pre-shared key; key exchange is ephemeral-only, so sessions have
   perfect forward secrecy; and the runner discloses a tiered,
   responder-chosen summary of its platform inside the handshake itself,
   as an extension in its EncryptedExtensions, so the submitter holds
   the platform from the flight that establishes the session.  The
   binding opens an inbound listener on the runner's host and is off
   unless the owner enables it.  It is an addition, never a replacement:
   the store-and-forward bindings remain the ones every submitter can
   reach.
- **draft-slutsky-homing-pigeon-v2-04** (new-draft, score 3, adjacent_watchlist) [none]: [Homing Pigeon Message Protocol, Version 2: Determinations, Questions, and Shared Context](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon-v2/) — This document specifies version 2 of the Homing Pigeon message
   protocol.  Version 2 is an addition to version 1 (draft-slutsky-
   homing-pigeon), not a replacement for it: every version 1 message
   keeps its meaning, and version 2 adds three messages and one
   mechanism on top of the version 1 exchange.

   The additions are a determination message, by which the runner tells
   the submitter what it expects a job to do before the job runs; a
   question message, by which a runner whose local decision machinery
   cannot answer a question itself asks that question instead; an answer
   message, by which any enabled holder of the shared secret replies;
   and context segments, signed fragments of local state that travel
   with these messages and with the version 1 result, so each side plans
   with the other's actual state in view.

   Version 2 is backwards compatible.  A version 1 runner never sends a
   version 2 message and is unaffected by this document.  A submitter
   that implements this document adapts to the protocol version the
   runner supports: faced with a version 1 runner, it submits version 1
   jobs and expects version 1 results, exactly as before.  There is no
   version negotiation and no handshake; the messages carry v, as in
   version 1, and each side acts on what it receives.

   The deployment that motivates version 2 is the constrained runner: a
   small host whose local decision machinery is deliberately
   deterministic and carries no language model.  Version 1 leaves such a
   runner alone with every question its deterministic machinery cannot
   answer.  Version 2 lets it ask.
- **draft-taylor-dtn-imc-scheme-01** (new-draft, score 3, core_identity) [none]: [The 'imc' URI Scheme for Bundle Protocol Multicast](https://datatracker.ietf.org/doc/draft-taylor-dtn-imc-scheme/) — This document defines the 'imc' URI scheme, a concise integer-based
   scheme for identifying Bundle Protocol Version 7 (BPv7) endpoints
   that are not singleton endpoints, termed multicast endpoints.  The
   structure of 'imc' URIs mirrors that of the 'ipn' URI scheme: each
   'imc' URI comprises an Allocator Identifier, a Group Number, and a
   Service Number.  In the same way that the Allocator Identifier and
   Node Number of an 'ipn' URI identify the node at which a service
   exists, the Allocator Identifier and Group Number of an 'imc' URI
   identify a group of nodes at which a service exists, and the Service
   Number identifies that service.  This document specifies the textual
   syntax of 'imc' URIs, their interpretation when used as BPv7 Endpoint
   Identifiers, their CBOR encoding, and the corresponding EID Pattern,
   and requests the associated IANA registrations.
- **draft-toco-abiz-dns-00** (new-draft, score 3, agent_identity) [none]: [The "_abiz" Underscored and Globally Scoped DNS Node Name for Agentic Business Records](https://datatracker.ietf.org/doc/draft-toco-abiz-dns/) — This document specifies use of the underscored DNS node name "_abiz"
   with TXT resource records to publish a pointer from a domain to a
   signed public business record served over HTTPS.  It describes
   discovery and verification of that record and requests registration
   of the "_abiz" node name and the "abiz.json" well-known URI suffix.
- **draft-vladyka-schc-vxlan-fragmentation-00** (new-draft, score 3, core_identity) [none]: [SCHC No-ACK Fragmentation of VXLAN Payloads](https://datatracker.ietf.org/doc/draft-vladyka-schc-vxlan-fragmentation/) — This document proposes a SCHC No-ACK profile for carrying VXLAN
   payloads, including those larger than the path MTU, over a managed
   UDP path.  On a configured peer association every frame is carried as
   a SCHC Packet made of a NoCompress rule identifier, the uncompressed
   VXLAN header and the Ethernet frame.  The packet is sent unfragmented
   when it fits the path MTU and fragmented otherwise.  A four-bit
   fragment counter supports up to eight fragments.  An optional
   receiver procedure for reordering is described separately because it
   changes the RFC 8724 No-ACK receiver behavior.  The earlier indexed
   fragmentation proposal is retained in an appendix for comparison.
   The mapping and operational parameters require working group review.
- **draft-vos-cfrg-pqpake-04** (new-draft, score 3, core_identity) [none]: [Hybrid Post-Quantum Password Authenticated Key Exchange](https://datatracker.ietf.org/doc/draft-vos-cfrg-pqpake/) — This document focuses on the problem of password authenticated key
   exchange in a post-quantum setting, a gap for which there does not
   exist any protocol suitable for deployment.  Given PAKE uses in
   settings such as device pairing and client-server authentication,
   this gap has real world security consequences.  This document
   addresses this gap with four post-quantum password authenticated key
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
- **draft-vulnetix-crit-03** (new-draft, score 3, core_identity) [none]: [Cloud Resource Identifier Templates (CRIT)](https://datatracker.ietf.org/doc/draft-vulnetix-crit/) — This document specifies the Cloud Resource Identifier Templates
   (CRIT) format.  A CRIT record provides a machine-readable,
   parameterised template for locating cloud-native resources affected
   by a known vulnerability.  CRITs do not define cloud resource
   identifier schemas; those are defined normatively by each cloud
   provider.  CRITs define a variable system for expressing partially-
   known or consumer-resolved values within those provider-defined
   schemas, together with temporal, remediation, and detection metadata
   sufficient to determine exposure status and drive remediation
   workflows.

   Each CRIT record is bound to exactly one vulnerability identifier.
   Cross-provider and multi-resource-type coverage of a single
   vulnerability is expressed as a set of CRIT records sharing the same
   vulnerability identifier, each independently specifying the provider-
   specific fix details, propagation mechanism, and detection strategy
   applicable to that resource type.
- **draft-wang-agent-semantic-routing-00** (new-draft, score 3, ai_infrastructure) [none]: [Research on service semantic identification and routing technology for Internet of agents](https://datatracker.ietf.org/doc/draft-wang-agent-semantic-routing/) — With the deep integration of artificial intelligence and network
   technologies, the Internet of agents has become an important
   direction for the evolution of the next-generation Internet.  The
   connection paradigm of the traditional Internet centered on “location
   addressing” can hardly meet the demands of the Internet of agents for
   “business-driven and service-as-connection”. The service semantic
   routing technology system, paradigm evolution, core collaboration
   requirements in the Internet of agents, and the limitations of
   traditional routing technologies were systematically elucidated.  It
   was clarified that semantic routing was the key to realizing the
   transformation from “service demand” to “resource matching”. The
   solutions for four core semantic routing mechanisms in the Internet
   of agents, namely fuzzy search based on tag matching and flexible
   adaptation, precision-named DNS (domain name system) for “service-
   domain name” mapping, business-layer network identification based on
   Anycast, and URL (uniform resource locator) semantic routing with
   application-layer semantic encapsulation were analyzed in depth.
   Finally, the technical characteristics of each solution were
   summarized and compared, providing an important reference for
   subsequent research.
- **draft-wang-ipsecme-kem-auth-ikev2-05** (new-draft, score 3, core_identity) [none]: [KEM-based Authentication for IKEv2 with Post-quantum Security](https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/) — This draft specifies a new authentication mechanism, called KEM (Key
   Encapsulation Mechanism) -based authentication, for the Internet Key
   Exchange Protocol Version 2 (IKEv2).  This is motivated by the fact
   that some post-quantum KEMs (like ML-KEM) are more efficient than
   post-quantum signature algorithms (like ML-DSA).
- **draft-watts-authorization-noncollapse-semantics-02** (new-draft, score 3, authorization) [none]: [Non-Collapse Semantics for Authorization, Evidence, and Execution State](https://datatracker.ietf.org/doc/draft-watts-authorization-noncollapse-semantics/) — Distributed authorization systems frequently combine observations,
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
- **draft-watts-research-artifact-provenance-02** (new-draft, score 3, trust_infrastructure) [none]: [Research Artifact Provenance and Corrigible Scientific State](https://datatracker.ietf.org/doc/draft-watts-research-artifact-provenance/) — This document describes a protocol-neutral pattern for content-
   addressed research artifacts, append-only evidence history, explicit
   epistemic classes, and corrigible active scientific state.  It
   separates byte integrity from numerical correctness, empirical
   adequacy, mechanism identification, and release authority.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-research-evidence-bundle-02** (new-draft, score 3, trust_infrastructure) [none]: [A Research Evidence Bundle JSON Envelope for Provenance and Replication Metadata](https://datatracker.ietf.org/doc/draft-watts-research-evidence-bundle/) — This document proposes an early-stage JSON envelope for exchanging
   research-evidence records containing claim status, evidence tier,
   source provenance, methods, falsifiers, replication status, artifact
   digests, and privacy review.  It is an individual design proposal,
   not an IETF consensus document.  Its intended contribution must be
   assessed against existing provenance and research-packaging
   specifications before further standardization work.
- **draft-watts-research-evidence-envelope-02** (new-draft, score 3, trust_infrastructure) [none]: [Research Evidence Envelope: A Provenance-Oriented Interchange Record](https://datatracker.ietf.org/doc/draft-watts-research-evidence-envelope/) — This informational scaffold sketches a versioned record for tracking
   scientific claims, source provenance, evidence classes, uncertainty,
   falsifiers, replication procedures, and artifact hashes.  It is not
   an IETF standard, has not undergone IETF review, and does not define
   a wire protocol.
- **draft-watts-research-intelligence-archive-02** (new-draft, score 3, trust_infrastructure) [none]: [Evidence-Bounded Research Intelligence Archives](https://datatracker.ietf.org/doc/draft-watts-research-intelligence-archive/) — This unsubmitted working draft defines an evidence-bounded archive
   profile for scientific and technical claims, sources, evidence tiers,
   falsifiers, tests, provenance, publication state, and integrity
   manifests.  The profile is designed to prevent archival or mechanical
   integrity from being misread as empirical validity, novelty, peer
   review, standards approval, or publication acceptance.  This file is
   an archival RFCXML working draft and has no IETF standing unless
   separately submitted.
- **draft-watts-scientific-data-record-00** (new-draft, score 3, trust_infrastructure) [none]: [A Provenance-Bounded Record Format for Scientific Data](https://datatracker.ietf.org/doc/draft-watts-scientific-data-record/) — This document specifies a JSON record format for scientific data and
   the claims derived from it.  Each record binds a claim to an
   immutable source digest, a claim class, an evidence tier, a mandatory
   falsifier, a set of typed check results, and a provenance trail.
   Processing is fail-closed: a missing, unknown, or not-run check
   blocks admissibility.  The format proves custody and unchanged bytes.
   It does not certify that a claim is true.
- **draft-watts-unison-state-preservation-02** (new-draft, score 3, trust_infrastructure) [none]: [State-Preserving Exchange of Evaluation Evidence](https://datatracker.ietf.org/doc/draft-watts-unison-state-preservation/) — This unsubmitted working draft describes state-preservation semantics
   derived from UNISON-StateBench.  It separates value, epistemic
   status, provenance, and authority; defines a non-collapse rule for
   operational and epistemic transitions; and describes representation,
   contradiction, missing-evidence, authority, principal-isolation,
   tool-state, context-distance, and controlled-mutation evaluation
   families.  This file is an archival RFCXML working draft and is not
   an IETF submission.
- **draft-watts-verification-defect-quarantine-02** (new-draft, score 3, adjacent_watchlist) [none]: [Verification Defect Quarantine for Protocol Conformance Systems](https://datatracker.ietf.org/doc/draft-watts-verification-defect-quarantine/) — Protocol conformance systems commonly treat a published test vector
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
- **draft-watts-verification-promotion-boundaries-02** (new-draft, score 3, authorization) [none]: [Verification Promotion Boundaries for Protocol Implementations](https://datatracker.ietf.org/doc/draft-watts-verification-promotion-boundaries/) — Protocol implementations frequently combine specification checks,
   deterministic test vectors, security testing, independent
   reproduction, and release decisions.  A common failure mode is
   evidence collapse: a result at one assurance level is silently
   treated as sufficient for a stronger conclusion.  This document
   defines Verification Promotion Boundaries (VPB), a machine-readable
   profile and state-transition procedure that separates specification
   validation, local conformance, independent reproduction, authorized
   security testing, and release eligibility.  VPB also defines dual-
   state handling for specification defects: detecting a bad normative
   vector is negative evidence about the tested subject but may be
   positive fault-detection evidence about the verifier.  Unknown
   evidence never promotes.  This document does not define a new
   cryptographic primitive, authorization protocol, or IETF
   certification program.
- **draft-watts-veriflow-evidence-envelope-02** (new-draft, score 3, trust_infrastructure) [none]: [Veriflow Evidence Envelope for Source-Grounded Computational Claims](https://datatracker.ietf.org/doc/draft-watts-veriflow-evidence-envelope/) — This document specifies an experimental, JSON-based evidence envelope
   for exchanging source-grounded computational assertions, including
   provenance, reproducible operation identifiers, evidence sufficiency,
   and explicit abstention when an answer is not supported.  The
   envelope separates syntactic validity, source integrity, mathematical
   correctness, and empirical truth.  This document does not standardize
   a general scientific inference engine or claim experimental
   superiority.
- **draft-yang-ancp-home-app-usecase-00** (new-draft, score 3, adjacent_watchlist) [none]: [Use Cases & Requirements for ANCP](https://datatracker.ietf.org/doc/draft-yang-ancp-home-app-usecase/) — This document describes use cases for the Access Node Control
   Protocol in home applications, where a Broadband Network Gateway
   (BNG/BRAS) exchanges home-application policy with a Home Gateway
   (HGW).  ANCP may operate either between BNG and OLT, or directly
   between BNG and HGW.  When ANCP runs only between BNG and OLT,
   additional configuration via OMCI is required to reach the HGW.  The
   use cases in this document are illustrated in the mode where ANCP
   runs directly between BNG and HGW.

   The use cases cover three primary scenarios: managed access to
   operator-hosted large model services, application-aware QoS, and
   controlled remote access to home LAN resources.
- **draft-agrawal-agentproto-presented-output-00** (new-draft, score 2, ignored_after_review) [none]: [Use Case and Requirements for Reporting Output Presented to a User](https://datatracker.ietf.org/doc/draft-agrawal-agentproto-presented-output/) — When an agent's output is presented to a user over time, as with
   synthesized speech, the agent has usually generated more than the
   user has received at the moment an exchange stops.  Existing
   requirements cover abandoning an exchange and cancelling a task.
   They do not cover telling the participants in the dialog how much of
   the output the user actually received.  This document describes one
   use case with two examples, a travel booking and a voice purchase,
   and derives five requirements that can be incorporated into the
   working group's use cases and requirements document.
- **draft-bates-atp-test-vectors-01** (new-draft, score 2, ignored_after_review) [none]: [ATP Core Test Vectors](https://datatracker.ietf.org/doc/draft-bates-atp-test-vectors/) — This document publishes golden test vectors for the Agent Transaction
   Protocol (ATP).  The vectors cover canonicalization (RFC 8785 JCS),
   nodeId computation, and Ed25519 signature generation and
   verification.  ATP Core conformance requires that conformant
   implementations pass all vectors in this document for
   canonicalization, nodeId computation, and Ed25519 signature
   verification.
- **draft-besleaga-agentic-knowledge-wellknown-02** (new-draft, score 2, ignored_after_review) [none]: [The 'knowledge-linkset' Well-Known URI for Publishing Knowledge Artefacts](https://datatracker.ietf.org/doc/draft-besleaga-agentic-knowledge-wellknown/) — This document defines the "knowledge-linkset" well-known URI, at
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
- **draft-chuang-agent-attribution-header-fields-01** (new-draft, score 2, ignored_after_review) [none]: [Agent Attribution Header Fields](https://datatracker.ietf.org/doc/draft-chuang-agent-attribution-header-fields/) — When human users communicate with autonomous computer agent users,
   the human users should be able to identify that communication as
   coming from agent users and know which humans are responsible for the
   agent users.  This document specifies email header fields that an
   email sender can use to transmit agent user attribution information
   to email receivers.  The first header field is human readable and
   specifies the agent's responsible humans' email address.  The second
   header field is machine readable and specified in JSON attribution
   information.
- **draft-curtis-myterms-02** (new-draft, score 2, ignored_after_review) [none]: [MyTerms Contract Negotiation Protocol (MCNP): Human and machine-readable agreements](https://datatracker.ietf.org/doc/draft-curtis-myterms/) — This document covers the technical requirements of Verifiable
   Contractual Agreements (VCAs) between individuals and the entities
   that engage on a network as defined in IEEE7012.  It describes how
   individuals, acting as first parties, can proffer their privacy
   requirements as contractual terms and arrive at agreements recorded
   and kept by both sides.  This includes the hosting format for
   contracts, negotiation of contracts, signing of contracts, and
   auditing of contracts.
- **draft-filsfils-srv6ops-srv6-ai-backend-07** (new-draft, score 2, ignored_after_review) [none]: [SRv6 for Deterministic Path Placement in AI Backends](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) — This document describes how SRv6 NEXT-CSID enables deterministic path
   placement in AI backend fabrics through L3-L4 integration on end
   hosts: the transport stack on the NIC encodes each path as an ordered
   list of segments (a NEXT-CSID network program) in the packet header,
   while the fabric forwards statelessly.  It explains operational
   benefits including deterministic probing and alignment with
   hyperscale production deployments.
- **draft-hu-6man-ipv6-flowlabel-load-balancing-rdma-04** (new-draft, score 2, ignored_after_review) [none]: [A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) — This document proposes a method for achieving flow-level load
   balancing in RoCEv2 (RDMA over Converged Ethernet version 2)
   networks.  Traditional per-flow load balancing based on the 5-tuple
   cannot distinguish between different RDMA sessions that share the
   same 5-tuple.  This causes "elephant flows" to be hashed to the same
   path, leading to network congestion.  This method resolves this issue
   by having the ingress network device (e.g., a data center gateway or
   DCI edge router) parse the QP (Queue Pair) information from the IB
   BTH (Base Transport Header) and IB DETH (Datagram Extended Transport
   Header, when present) of the RoCEv2 packet.  By combining this with
   portions of the IPv6 source and destination addresses as an entropy
   source, a CRC32 hash algorithm generates a 32-bit value, the low 20
   bits of which are then written into the Flow Label field of the IPv6
   header.  Network devices can subsequently use the updated "5-tuple +
   Flow Label" for more granular flow-level load balancing, thereby
   effectively improving transmission efficiency in high-performance
   networks for workloads such as AI computing.
- **draft-ietf-lisp-8111bis-02** (new-draft, score 2, ignored_after_review) [lisp]: [Locator/ID Separation Protocol Delegated Database Tree (LISP-DDT)](https://datatracker.ietf.org/doc/draft-ietf-lisp-8111bis/) — This document describes the Locator/ID Separation Protocol Delegated
   Database Tree (LISP-DDT), a hierarchical distributed database that
   embodies the delegation of authority to provide mappings from LISP
   Endpoint Identifiers (EIDs) to Routing Locators (RLOCs).  It is a
   statically defined distribution of the EID namespace among a set of
   LISP control plane elements generically called "DDT Nodes".  Each DDT
   Node is configured as "authoritative" for one or more EID-Prefixes,
   along with the set of RLOCs for Map-Servers or "child" DDT Nodes to
   which more-specific EID-Prefixes are delegated.

   This document obsoletes RFC 8111 and updates RFC 9301.
- **draft-kelley-rep-namespaces-00** (new-draft, score 2, ignored_after_review) [none]: [Namespaces for the Robots Exclusion Protocol](https://datatracker.ietf.org/doc/draft-kelley-rep-namespaces/) — This document updates RFC 9309, the Robots Exclusion Protocol, so
   that a _selector_ (User-Agent: line) in a robots.txt group can carry
   a _label_ that is optionally qualified by a _namespace_.  The product
   tokens of that standard are described here as unqualified labels;
   labels qualified by a namespace are written __<namespace>_<label>.
   It reserves the sequence __ for that purpose, establishes a registry
   of namespaces, and specifies how namespaced labels are matched.  It
   also defines terminology for existing parts of robots.txt files.
   Existing robots.txt files are interpreted as before, and deployed
   parsers ignore namespaced labels.
- **draft-mcw-opsawg-icon-requirements-04** (new-draft, score 2, ignored_after_review) [none]: [Architecture and Requirements for Autonomous Agent Observability, Control and Intervention](https://datatracker.ietf.org/doc/draft-mcw-opsawg-icon-requirements/) — This document defines architecture and a set of requirements for
   Observability, Control, and Intervention for Autonomous Agents.  The
   Autonomous Agents can be any Agents such as Network management Agents
   or Security Agents.

   It identifies gaps in existing mechanisms and specifies required
   interaction capabilities between Agent supervision systems and
   Autonomous Agents (such as Network Management Agents) across multi-
   vendor environments, specifically observability, control, and runtime
   intervention.  The requirements aim to guarantee comprehensive,
   lifecycle control over Autonomous Agents and enable observation,
   constraint, intervention, and correction to ensure network
   operational resilience and continuity.
- **draft-morrison-live-reference-resolution-03** (new-draft, score 2, ignored_after_review) [none]: [Live Reference Resolution for Autonomous Agent Beliefs](https://datatracker.ietf.org/doc/draft-morrison-live-reference-resolution/) — A recurring class of autonomous-agent failure arises when an agent
   acts on a belief read from a cached, derived, or proxy copy that has
   silently diverged from the authority the belief claims to represent.
   This document describes a reference-resolution discipline for the
   working beliefs an agent reasons and acts from.  Each belief is held
   as a reference to a single named lowest authority and is resolved
   live at the point of use, with verification.  When the authority is
   unobservable or the resolved value is stale, the belief takes an
   explicit uncertainty state and never falls back to a prior cached
   value.  That state propagates to any belief derived from it, and an
   uncertain belief feeding a costly or irreversible act blocks the act
   or escalates it.  Every resolution chain terminates in a single self-
   authorising root.  The document is Informational.  It records a
   discipline and a vocabulary and defines no wire protocol.
- **draft-morrison-relay-storage-authorisation-01** (new-draft, score 2, ignored_after_review) [none]: [Relay Storage Allowances That Expire at a Planned Contact](https://datatracker.ietf.org/doc/draft-morrison-relay-storage-authorisation/) — The use case and requirements document for IP in deep space asks that
   relays guard their buffers by authenticating and authorising the
   traffic sources allowed to consume buffer space, and by accounting
   for storage per source or traffic class.  This document gives that
   requirement a mechanism.  A storage allowance is a signed object in
   which a party with authority over a relay's storage states that a
   named holder may keep up to a stated number of octets at each named
   relay, until a planned contact between that relay and its next hop.
   A relay checks an allowance from data it already holds, without
   contacting the party that issued it.  It charges stored data to an
   allowance by tagging the data in its own buffer and keeps no other
   state for it.  No state is shared between relays, and at any instant
   the storage held under one allowance is no more than the sum of its
   rows.  An allowance ends at the first contact it lists that takes
   place.  A missed contact moves the end to the next contact listed, up
   to the last.  The document defines the allowance, its issuance and
   delegation, enforcement at the relay, revocation, carriage in the
   Bundle Protocol and over IP, and its use with signed custody receipts
   for accounting.
- **draft-ranjbar-regext-rdap-subordinate-referrals-03** (new-draft, score 2, ignored_after_review) [none]: [Referrals to Holder-Designated RDAP Services for Subordinate Resources](https://datatracker.ietf.org/doc/draft-ranjbar-regext-rdap-subordinate-referrals/) — An RDAP query can be followed from the IANA bootstrap registries down
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
   The document uses the redirect controls and object relations of
   draft-ietf-regext-rdap-referrals and the service relations of draft-
   ietf-regext-rdap-extensions, and defines no new ones.
- **draft-watts-rec-evidence-bound-evaluation-00** (new-draft, score 2, ignored_after_review) [none]: [An Evidence-Bound Protocol for Evaluating Unfamiliar Mathematical-Rule Communication](https://datatracker.ietf.org/doc/draft-watts-rec-evidence-bound-evaluation/) — This document specifies REC-EP, an experimental, transport-
   independent JSON interchange profile for exchanging masked
   mathematical-rule challenges, receiver predictions, evidence
   statuses, immutable artifact digests, and signed evaluator receipts.
   It separates invariant matches from proven equivalence, requires
   explicit evaluation custody boundaries, and supports reproducible
   comparisons of arithmetic-first, invariance-first, and hybrid
   instruction.  REC-EP does not assert a novel mathematical theorem, a
   validated superiority effect, extraterrestrial intelligence, or IETF
   endorsement.  This candidate is not submitted and proposes no IANA
   actions.
- **draft-watts-relational-echo-calculus-01** (new-draft, score 2, ignored_after_review) [none]: [Relational Echo Calculus (REC): A Transformation-First Mathematical Communication Prototype](https://datatracker.ietf.org/doc/draft-watts-relational-echo-calculus/) — This document describes a transformation-first teaching notation for
   mathematical communication to unfamiliar receivers.  The prototype
   operates on finite motifs drawn from the vertices of a Hamming
   hypercube.  Echo operations act through coordinate permutations and
   binary translations.  We distinguish invariance of a coarse signature
   from proof of exact orbit equivalence, exhibiting two four-
   dimensional patterns that have equal pairwise-distance multisets but
   different induced adjacency.  A synthetic toy decoder reconstructs
   arbitrary token meanings when its complete transformation hypothesis
   class is supplied.  The main testable conjecture is that instruction
   ordered by invariance might improve cross-agent decoding over
   instruction ordered by arithmetic under matched information budgets.
   The conjecture has not been experimentally evaluated; no new
   extraterrestrial signal or new mathematical theorem is claimed.
- **draft-watts-verifiable-scientific-evidence-records-03** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Scientific Evidence Records: A Minimal Integrity Profile](https://datatracker.ietf.org/doc/draft-watts-verifiable-scientific-evidence-records/) — This document specifies a minimal JSON evidence-record profile for
   checking artifact digests and separating integrity verification from
   scientific assessment.  It defines an interoperable record structure,
   validation algorithm, and negative test cases.  It does not assert
   that an integrity-checked scientific claim is true.
- **draft-wnd-opsawg-icon-ps-02** (new-draft, score 2, ignored_after_review) [none]: [Problem Statement for Autonomous Agent Observability, Intervention and Control (I&C) in Multi-Agent Autonomous Networks](https://datatracker.ietf.org/doc/draft-wnd-opsawg-icon-ps/) — This document provides an overview of the issues associated with the
   deployment of the observability, intervention, and control of
   autonomous agent pipelines in large-scale heterogeneous network
   environments.  The term "Observability, Intervention and Control" is
   used to describe a set of automated and human-initiated mechanisms
   that guarantee the capability to observe, evaluate, constrain,
   correct, and terminate Autonomous agents at any point, for any
   reason, irrespective of their level of autonomy under which it
   operates, to ensure resilience, recovery, and operational continuity.

   The set of enabled observability, intervention and control reflects
   operator service offerings to ensure that autonomous network
   operations can be stopped, or safely redirected when required and is
   designed in conjunction with agent to agent, agent to tools, agent to
   human interaction and service and network policy.

   This document also identifies several key areas that the Agent
   Observability, Intervention and Control group will investigate to
   guide its architectural and protocol work and associated documents.
- **draft-yang-ccamp-optical-agent-coordination-00** (new-draft, score 2, ignored_after_review) [none]: [An Architecture for Agent Coordination in Computing-Aware Optical Networks](https://datatracker.ietf.org/doc/draft-yang-ccamp-optical-agent-coordination/) — Computing-aware optical networks coordinate optical connectivity with
   the capabilities, availability, and performance of computing
   services.  This document describes an informational architecture for
   coordination among joint control, transport control, network element,
   and compute resource agents.  These roles relate local observations
   to domain abstractions, assess connection-and-site candidates against
   a common service objective, and evaluate the combined service
   outcome.  Computing resources may be located at edge, regional, or
   centralized sites.  Coordination supports access to existing service
   instances and, where authorized, new workload placement or optical
   resource allocation.  Resource managers retain admission and
   execution authority.  The architecture is independent of optical
   switching technology and agent algorithm.  An Optical Transport
   Network (OTN) and edge computing provide a detailed realization
   example; reinforcement learning is an optional policy use case.  This
   document defines no new protocol, YANG module, or optical signal
   format.
- **draft-zhangb-cats-csma-implementation-04** (new-draft, score 2, ignored_after_review) [none]: [CATS C-SMA Service-Metrics Snapshots and C-SMA-to-C-PS Transport Bindings](https://datatracker.ietf.org/doc/draft-zhangb-cats-csma-implementation/) — This document defines a service-metrics snapshot published by a CATS
   Service Metric Agent (C-SMA) to a CATS Path Selector (C-PS).  The
   snapshot conveys service-metric records and their observation window,
   together with publication context supporting versioning and the FULL,
   INVALIDATE, and WITHDRAW operations.

   The document defines the snapshot contract and two transport modes
   for the C-SMA-to-C-PS interface: Centralized Mode, using YANG-modeled
   operational state delivered by gNMI, and Distribution Mode, proposing
   a BGP-LS service-metadata mapping.  The BGP-LS mapping is
   illustrative until its wire encoding and code points are specified.
- **draft-john-scion-svcb-00** (new-draft, score 1, verifiable_claims) [none]: [Publishing SCION Endpoint Addresses in DNS Service Binding (SVCB) Records](https://datatracker.ietf.org/doc/draft-john-scion-svcb/) — This document defines "scion", a Service Parameter Key (SvcParamKey)
   for the Service Binding (SVCB) and HTTPS DNS resource records.  Its
   value lists the addresses at which a service endpoint is reachable
   over SCION (Scalability, Control, and Isolation On Next-generation
   networks), a path-aware inter-domain network architecture.  This
   document specifies the wire format, presentation format, and
   semantics of the key and requests its registration with IANA.

## Ignored after review

- **draft-alivar-spring-icmp-error-srv6-vpn-00** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for VPNs in SRv6 Networks](https://datatracker.ietf.org/doc/draft-alivar-spring-icmp-error-srv6-vpn/) — The document specifies procedures for handling ICMP error messages in
   SRv6-based Virtual Private Network (VPN).  It describes three methods
   to improve the ICMP Error Handling for SRv6-VPNs.
- **draft-amsuess-core-accept-any-01** (new-draft, score 0, ignored_after_review) [none]: [Accept-Any option for CoAP](https://datatracker.ietf.org/doc/draft-amsuess-core-accept-any/) — This memo defines the Accept-Any option, which provides a more
   flexible content negotiation than the one originally specified for
   the Constrained Application Protocol (CoAP) in [RFC7252].  As this is
   particularly useful with, but ruled out in, CoAP observation
   ([RFC7641]), that is updated to allow it.
- **draft-appelcline-hashed-elision-01** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Hashed Data Elision: Problem Statement and Areas of Work](https://datatracker.ietf.org/doc/draft-appelcline-hashed-elision/) — This document discusses the need for deterministic hashed data
   elision as a baseline for secure data storage.  It focuses on four
   different categories of requirements: corporate needs, privacy
   compliance requirements, variable access compliance requirements, and
   past IETF RFCs.  Additional sections discuss the functional
   requirements that match these needs and how existing technologies
   meet them.
- **draft-atwood-jmap-updates-00** (new-draft, score 0, ignored_after_review) [none]: [Updates to JMAP: Localized Display Text, Text Handling, URIs, and Problem Details](https://datatracker.ietf.org/doc/draft-atwood-jmap-updates/) — JMAP (RFC 8620) carries all data as UTF-8 I-JSON, lets a client name
   a collation for sorting, and lets a server localize user-visible
   strings from the request's Accept-Language header.  It has no way to
   store or return display text, such as the name of a mailbox, address
   book, or quota, in more than one language, and no way to say which
   language a stored string is in.  This document defines the
   urn:ietf:params:jmap:i18n capability, which adds locale and
   localizations properties, modelled on JSCalendar (RFC 8984), to the
   display text of existing JMAP data types, and a language argument
   with which a client asks for one language.  For clients that use that
   argument, this document updates RFC 9425, which selects the Quota
   description by Accept-Language.  It also updates RFC 8620 with
   guidance for all JMAP specifications on text profiles, Unicode
   normalization, truncation, and the use of display text, and asks that
   URI-valued properties follow RFC 3986 and that every JMAP HTTP
   resource report errors as RFC 9457 problem details.
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
- **draft-bains-nltp-00** (new-draft, score 0, ignored_after_review) [none]: [NeckLink Transport Protocol (NLTP): Loss-Healing Authenticated Telemetry and Reflex Transport for Constrained Networks](https://datatracker.ietf.org/doc/draft-bains-nltp/) — This document specifies the NeckLink Transport Protocol (NLTP), a
   lightweight, loss-healing, forward-secret transport protocol designed
   for microcontrollers, autonomous sensors, and edge gateways operating
   over lossy wireless links (including IEEE 802.11 vendor action frames
   such as ESP-NOW v1 and v2) and Carrier-Grade NAT (CGNAT) UDP paths.
   NLTP combines systematic Galois Field GF(2^8) algebraic Cauchy
   erasure coding with a single-round-trip (1-RTT) X25519 and pre-shared
   key (PSK) session handshake, ChaCha20-Poly1305 authenticated
   encryption with associated data (AEAD), a 512-packet sliding anti-
   replay window, optional pre-encryption zero-heap LZ4 block
   compression, integer delivery-rate pacing, and a confirmed out-of-
   line reflex channel that eliminates head-of-line (HOL) blocking for
   urgent actuator commands.  The entire protocol executes with zero
   dynamic heap allocation and zero floating-point operations, fitting
   within 4,760 octets of static RAM in transmit-plus-reflex sensor
   configurations.
- **draft-banffy-httpbis-not-a-freezer-00** (new-draft, score 0, ignored_after_review) [none]: [The Hypertext Transfer Protocol Status Code 483 (I'm Not a Freezer)](https://datatracker.ietf.org/doc/draft-banffy-httpbis-not-a-freezer/) — This document defines the Hypertext Transfer Protocol status code 483
   (I'm Not a Freezer).  A server returns this status code when it
   understands a request that requires freezing or refrigeration
   capabilities but is not capable of providing those capabilities.

   This document also clarifies the distinction between a freezer, a
   refrigerator, a server operating at a low temperature, a frozen
   software process, and an online service advertising "cold storage".
- **draft-beck-tls-hybrid-codepoints-00** (new-draft, score 0, ignored_after_review) [none]: [TLS 1.3 Code Points for Composite ML-DSA Signature Algorithms](https://datatracker.ietf.org/doc/draft-beck-tls-hybrid-codepoints/) — This document allocates TLS SignatureScheme code points for the
   Composite ML-DSA signature algorithms that [RFC10073] short-lists for
   implementation, and specifies the parameters an implementation needs
   to use them interoperably in TLS 1.3.
- **draft-beeram-mpls-rsvp-sr-02** (new-draft, score 0, ignored_after_review) [mpls]: [Signaling RSVP-TE Tunnels on an SR-MPLS Forwarding Plane Using Adjacency Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-mpls-rsvp-sr/) — RFC 8577 introduced the concept of signaling RSVP-TE tunnels on a
   shared MPLS forwarding plane using preinstalled "TE link labels".
   Those labels are functionally equivalent to Segment Routing (SR)
   Adjacency Segment Identifiers (Adj-SIDs) but are allocated and
   distributed solely via RSVP-TE signaling.

   This document extends RFC 8577 so that RSVP-TE tunnels can use
   Segment Routing over MPLS (SR-MPLS) Adj-SIDs, as specified in RFC
   8402 and RFC 8660, in place of TE link labels.  It restricts scope to
   Adj-SIDs attached to a single unidirectional adjacency and defines
   the signaling procedures and protocol extensions required to couple
   the RSVP-TE control plane with the SR-MPLS data plane.
- **draft-chen-opsawg-intent-webassembly-framework-00** (new-draft, score 0, ignored_after_review) [none]: [WebAssembly Framework for Network Management in Heterogeneous Edge Networks](https://datatracker.ietf.org/doc/draft-chen-opsawg-intent-webassembly-framework/) — This document describes an architecture for executing WebAssembly
   (WASM) modules for network management on heterogeneous edge devices.
   It describes dynamic bytecode dispatching, the Universal Bytecode
   Interface (UBI) for abstracting heterogeneous network element
   capabilities, and metadata models for capability exposure, bytecode
   deployment, execution context, intent-driven discovery, and security
   audits.  The framework decouples management scripts from platform-
   specific interfaces.  It reuses existing mechanisms for software
   update, payload manifests, integrity protection, and transport where
   applicable.
- **draft-chuang-dkim2-sender-policy-05** (new-draft, score 0, ignored_after_review) [none]: [DKIM2 Sender Policy](https://datatracker.ietf.org/doc/draft-chuang-dkim2-sender-policy/) — This document updates DMARC RFC 9989 for DKIM2.  In particular DKIM2
   verification supports MTA relay forwarding with message modifications
   through multiple MTAs, so this updates DMARC to support those
   scenarios as well.  While DMARC defines a RFC 5322 From alignment
   constraint with an enforcement policy if validation fails, this
   generalizes and separates enforcement policy from constraint
   validation policies.  This provides a mechanism for MTAs to declare
   support for DKIM2 through the DMARC DNS policy record that helps
   secure DKIM2 from downgrade attacks.
- **draft-claise-opsawg-ipfix-ordered-ie-03** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
   Information Element to appear multiple times in a Template Record.
   RFC 7011 states that multiple occurrences of the same Information
   Element SHOULD follow the logical order of their treatments by the
   Metering Process; however, no protocol mechanism exists for the
   Exporting Process to explicitly signal to the Collecting Process that
   this ordering is guaranteed.  Without such a guarantee, the
   Collecting Process cannot safely interpret repeated Information
   Elements as ordered observations.  This document describes the
   problem, presents use cases, analyzes candidate solutions, and
   specifies a mechanism, a new Ordered Set type, that establishes an
   end-to-end ordering guarantee: the Metering Process records repeated
   Information Element values in the order the corresponding
   observations are made, the Exporting Process preserves and signals
   this guarantee, and the Collecting Process interprets the n-th
   occurrence of an Information Element as corresponding to the n-th
   observation by the Metering Process at the Observation Point.  This
   document updates RFC 7011, RFC 5476, and RFC 6183.
- **draft-claise-opsawg-ipfix-ordered-mpls-ie-01** (new-draft, score 0, ignored_after_review) [none]: [Generic MPLS Information Elements for Ordered Export in IPFIX](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-mpls-ie/) — This document defines new generic IPFIX Information Elements for MPLS
   label stacks and label attributes, intended for use with the ordered
   set mechanisms that provide an explicit ordering guarantee for
   repeated Information Elements.
- **draft-davies-internal-tld-08** (new-draft, score 0, ignored_after_review) [none]: [A Top-level Domain for Private Use](https://datatracker.ietf.org/doc/draft-davies-internal-tld/) — This document describes the "internal" top-level domain for use in
   private applications.
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
- **draft-dikshit-netmod-comparability-scope-extension-04** (new-draft, score 0, ignored_after_review) [none]: [A YANG Extension for Declaring the Comparability Scope of Operational State](https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/) — A value exported from a YANG data tree is often unique only
   within its parent, for example an entry numbered 0 under two
   different parents. Once the value is exported without the
   parent's key, a collector cannot tell whether two such values
   refer to the same thing, and no collector-side normalization can
   recover the missing key. YANG (RFC 7950) has no way to state this
   dependency in the schema. This document defines a YANG extension
   statement, "csc:comparability-scope", a four-level scope lattice,
   a compatibility rule, and an export rule, so that the key needed
   to compare a value travels with it, and a schema-aware tool can
   detect an invalid comparison before any data is exported.
- **draft-dong-pce-cc-nrp-01** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for PCE Central Controller (PCECC) based Network Resource Partition (NRP) Instantiation](https://datatracker.ietf.org/doc/draft-dong-pce-cc-nrp/) — The PCE is a core component of Software-Defined Networking (SDN)
   systems.  A PCE-based Central Controller (PCECC) can simplify the
   processing of a distributed control plane by blending it with
   elements of SDN without necessarily completely replacing it.

   Network Resource Partitions (NRPs) can be used to provide the
   required connectivity and committed resources for network slice
   services.  An NRP is a subset of the buffer/queuing/scheduling
   resources and associated policies on each of a connected set of links
   in the underlay network.

   This document specifies the extensions to Path Computation Element
   Communication Protocol (PCEP) to enable PCECC based Network Resource
   Partition (NRP) Instantiation.
- **draft-eastlake-rfc9231bis-xmlsec-uris-11** (new-draft, score 0, ignored_after_review) [none]: [Additional XML Security Uniform Resource Identifiers (URIs)](https://datatracker.ietf.org/doc/draft-eastlake-rfc9231bis-xmlsec-uris/) — This document expands and corrects the IANA "XML Security URIs"
   registry that lists URIs intended for use with XML digital
   signatures, encryption, canonicalization, and key management.  These
   URIs identify algorithms and types of information.  This document
   obsoletes RFC 9231.
- **draft-ek-intarea-ip-enclave-signaling-04** (new-draft, score 0, ignored_after_review) [none]: [IP Enclave Boundary Signaling](https://datatracker.ietf.org/doc/draft-ek-intarea-ip-enclave-signaling/) — This document defines optional ICMP extension objects that a gateway
   at the boundary between an IP enclave and a managed constrained long-
   haul link, such as a scheduled deep-space link, can attach to
   existing Destination Unreachable messages.  On the unreachable errors
   generated when an admitted packet cannot be forwarded because the
   required link is presently unusable, the objects convey the expected
   time until the link becomes usable, the time the estimate was
   generated, and the expected one-way delay of the link.  On the
   administrative prohibition errors generated when the link's admission
   policy refuses a packet, a presence-only object identifies boundary-
   link admission policy as the source of the refusal.  The underlying
   codes retain their existing meanings, and this document requests no
   new ICMP type or code.  It specifies when the objects may be attached
   and what they convey, not how transports, applications, or hosts
   react to them; making the boundary's knowledge available to senders
   is intended to enable experimentation with such reactions.
- **draft-faltstrom-unicode-18** (new-draft, score 0, ignored_after_review): [draft-faltstrom-unicode-18-05](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/)
- **draft-faltstrom-unicode-18-05** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Domain Names for Applications 2008 (IDNA2008) and Unicode 18.0.0](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/) — This document describes the changes between Unicode 12.0.0 and
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
- **draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan-03** (new-draft, score 0, ignored_after_review) [none]: [SRv6 End-to-End DC Frontend and WAN](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan/) — The SRv6 Network Programming architecture allows an application to
   control the end-to-end journey of traffic flows through different
   network domains in a unified and stateless manner, without requiring
   intermediate network devices to maintain per-flow information.

   This document covers its application to the integration of data
   center (DC) and wide area network (WAN) architectures using SRv6 with
   uSID (NEXT-CSID).  It describes a unified IPv6 data plane from tenant
   workloads through the DC frontend to Internet peering, replacing
   designs that stitch separate overlay protocols at the Data Center
   Interconnect (DCI).  The solution enhances scalability and enables
   flexible stateless service insertion by unifying underlay, overlay,
   and service steering under SRv6.
- **draft-gandhi-bpm-stamp-signaling-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Signaling Parameters](https://datatracker.ietf.org/doc/draft-gandhi-bpm-stamp-signaling/) — The Simple Two-Way Active Measurement Protocol (STAMP) specified in
   RFC 8762 supports active measurement of network performance without a
   control channel to pre-signal session parameters.  RFC 8972 defines
   optional extensions in the form of Type-Length-Value (TLV) elements
   for STAMP.  This document defines a STAMP Type-Length-Value (TLV)
   that allows a Session-Sender and a Session-Reflector to exchange
   measurement capabilities and configuration parameters in STAMP-Test
   packets.  The Session-Sender uses the returned parameters to
   configure a STAMP session.
- **draft-gandhi-lsr-stamp-01** (new-draft, score 0, ignored_after_review) [none]: [IS-IS, OSPF, BGP-LS, and BGP Extensions for Advertising STAMP Session-Reflectors](https://datatracker.ietf.org/doc/draft-gandhi-lsr-stamp/) — The Simple Two-Way Active Measurement Protocol (STAMP), as defined in
   RFC 8762, can be utilized for active measurement without relying on a
   control channel to pre-signal session parameters.  This document
   defines extensions to IS-IS, OSPF, BGP-LS, and BGP to advertise
   information for discovering STAMP Session-Reflectors in a network.
   The advertised information can be used by STAMP senders to set up
   appropriate performance measurement sessions for delay and packet
   loss metrics.
- **draft-gandhi-pce-pm-16** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Performance Measurement for SR-TE and MPLS-TE LSPs with Stateful PCE](https://datatracker.ietf.org/doc/draft-gandhi-pce-pm/) — In certain networks, network performance data such as packet loss,
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
- **draft-gao-opsawg-flowspec-ipfix-01** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP FlowSpec Treatment Information in IPFIX](https://datatracker.ietf.org/doc/draft-gao-opsawg-flowspec-ipfix/) — BGP Flow Specification (FlowSpec) is commonly used to distribute
   traffic filtering and traffic treatment rules.  Operational
   monitoring of FlowSpec deployments may require information from
   multiple sources, including BGP control-plane telemetry, operational
   state, and forwarding-plane observations.

   This document defines IP Flow Information Export (IPFIX) Information
   Elements that add FlowSpec context to IPFIX Flow Records.  The
   exported information enables a Collector to correlate exported Flow
   Records with a FlowSpec rule in the scope of an Observation Domain
   and to identify the action classes reported by the Exporter.
- **draft-gondwana-email-big-files-01** (new-draft, score 0, ignored_after_review) [none]: [Linked Attachments in Email Messages](https://datatracker.ietf.org/doc/draft-gondwana-email-big-files/) — Message size limits mean that large files are sent by email as links
   to a web server rather than as attachments.  A link loses the
   properties that make an attachment useful: it can stop working, the
   file behind it can change, it can't be scanned in transit, and it may
   need a separate login.

   This document defines the "Content-External" header field, which lets
   receiving systems fetch, verify and keep a linked file, and then
   treat it like any other attachment.  The field is on a body part with
   a fallback link, which aware clients hide.
- **draft-han-fann-use-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Use Cases for Fast Network Notifications (FANN)](https://datatracker.ietf.org/doc/draft-han-fann-use-cases/) — This document reviews the use cases for Fast Network Notifications
   (FANN) that have been described in a number of individual drafts.
   Use cases are grouped by deployment scenario (data center network,
   data center interconnect and wide area network) aligned with the
   deployment scenarios of the FANN framework.  Each use case is
   summarized briefly with a reference to the document that describes it
   in detail.  This is intended to help identify a representative set of
   use cases from which the key FANN requirements can be derived.
- **draft-harano-xb64-00** (new-draft, score 0, ignored_after_review) [none]: [XB64: A Lightweight Reversible Obfuscation Encoding](https://datatracker.ietf.org/doc/draft-harano-xb64/) — This document specifies XB64 (XORed Base64), a lightweight reversible
   obfuscation encoding scheme for situations where immediate
   readability of source data is undesirable but cryptographic
   confidentiality is not required.

   To provide a key-dependent yet fully reversible representation, XB64
   applies repeating-key XOR to arbitrary octet sequences and encodes
   the result as printable ASCII text using Base64 as specified in RFC
   4648.  The resulting text itself preserves the source information,
   allowing exact reconstruction with the same key without external data
   lookup, while remaining suitable for human handling and exchange
   through text-oriented systems.

   By specifying a common encoding format for this level of obfuscation,
   this document aims to enable interoperable use across different
   applications, platforms, and implementations.
- **draft-haynes-nfsv4-flexfiles-v2-09** (new-draft, score 0, ignored_after_review) [nfsv4]: [Parallel NFS (pNFS) Flexible File Layout Version 2](https://datatracker.ietf.org/doc/draft-haynes-nfsv4-flexfiles-v2/) — Parallel NFS (pNFS) allows a separation between the metadata (onto a
   metadata server) and data (onto a storage device) for a file.  The
   Flexible File Version 2 Layout Type is defined in this document as an
   extension to pNFS that allows the use of storage devices that require
   only a limited degree of interaction with the metadata server and use
   already-existing protocols.  Data protection is also added to provide
   integrity.  Both Client-side mirroring and the erasure coding
   algorithms are used for data protection.
- **draft-horn-dmm-srh-3gpp-mobility-tlv-00** (new-draft, score 0, ignored_after_review) [none]: [Segment Routing Header TLVs for 3GPP Mobility Metadata](https://datatracker.ietf.org/doc/draft-horn-dmm-srh-3gpp-mobility-tlv/) — This document requests two Segment Routing Header (SRH) TLV
   codepoints.  Both are containers for mobility metadata used by 3GPP
   user-plane functions.  One does not change en route.  The other may
   change en route.  This document specifies the framing so that any
   Segment Routing node can skip either container.  Sub-TLV types and
   their meaning are under 3GPP change control.  Neither container
   changes IPv6 forwarding.
- **draft-icann-registrar-interfaces-17** (new-draft, score 0, ignored_after_review) [none]: [ICANN Registrar Interfaces](https://datatracker.ietf.org/doc/draft-icann-registrar-interfaces/) — This document describes the interfaces provided by ICANN to
   Registrars and Data Escrow Agents to fulfill the data escrow
   requirements of the Registrar Accreditation Agreement and the
   Registrar Data Escrow Specifications.
- **draft-ietf-6lo-schc-15dot4-15** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of SCHC-compressed packets over IEEE 802.15.4 networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-schc-15dot4/) — A framework called Static Context Header Compression and
   fragmentation (SCHC) has been designed with the primary goal of
   supporting IPv6 over Low Power Wide Area Network (LPWAN) technologies
   [RFC8724].  One of the SCHC components is a header compression
   mechanism.  If used properly, SCHC header compression allows a
   greater compression ratio than that achievable with traditional
   6LoWPAN header compression [RFC6282].  For this reason, it may make
   sense to use SCHC header compression in some 6LoWPAN environments,
   including IEEE 802.15.4 networks.  This document specifies how a
   SCHC-compressed packet can be carried over IEEE 802.15.4 networks.
   The document also enables the transmission of SCHC-compressed UDP/
   CoAP headers over 6LoWPAN-compressed IPv6 packets.
- **draft-ietf-6man-enhanced-vpn-vtn-id-17** (new-draft, score 0, ignored_after_review) [6man]: [Carrying Network Resource Context Information in IPv6 Extension Headers and its Applicability to Network Resource Partitions](https://datatracker.ietf.org/doc/draft-ietf-6man-enhanced-vpn-vtn-id/) — This document specifies a new IPv6 Hop-by-Hop option to carry Network
   Resource related information in data packets.  The new option is
   called the Network Resource (NR) Option.  It can be used to carry
   general information about network resource semantics and functions.

   A Network Resource Partition (NRP) is a subset of the network
   resources and associated policies on each of a connected set of links
   in an underlay network.  When forwarding packets within a specific
   NRP, some fields in the data packet (these fields are called the NRP
   Selector ID) are used to identify the NRP to which the packet belongs
   so that NRP-specific processing can be performed on each node along
   the forwarding path.  The Network Resource Option can be used to
   carry the NRP Selector ID in IPv6 packets.
- **draft-ietf-avtcore-rtp-avatar-04** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for Avatar Representation Format (ARF) Animation Stream](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-avatar/) — This memo outlines RTP payload formats for the animation stream
   format as defined in the ISO/IEC 23090-39 standard (MPEG-I Avatar
   Representation Format), in the following referred to as ARF.  ARF is
   composed of Avatar Animation Units (AAU) including an AAU header and
   zero or more AAU packets.  The RTP payload header format allows for
   packetization of an AAU unit in an RTP packet payload as well as
   fragmentation of an AAU into multiple RTP packets.
- **draft-ietf-bess-ebgp-dmz-12** (new-draft, score 0, ignored_after_review) [bess]: [BGP link bandwidth extended community use cases](https://datatracker.ietf.org/doc/draft-ietf-bess-ebgp-dmz/) — BGP link bandwidth extended community provides a way to signal a
   value along with a BGP path that can be used to perform weighted
   load-balancing in multipath scenarios.  This document details various
   use cases of the BGP link bandwidth extended community.  It also
   describes local mechanisms to dynamically adjust the BGP link
   bandwidth value or the multipath weights based on different
   considerations.
- **draft-ietf-bess-evpn-bfd-21** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Network Layer Fault Management](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-bfd/) — This document specifies proactive, in-band Network Layer OAM (RFC
   9062) mechanisms to detect loss of continuity faults that affect
   unicast and multi-destination paths (used by Broadcast, Unknown
   Unicast, and Multicast traffic) in an Ethernet VPN (EVPN, RFC
   7432bis) network.  The mechanisms specified in this document use the
   widely adopted Bidirectional Forwarding Detection (RFC 5880)
   protocol.
- **draft-ietf-bfd-rfc5880bis-02** (new-draft, score 0, ignored_after_review) [bfd]: [Bidirectional Forwarding Detection (BFD)](https://datatracker.ietf.org/doc/draft-ietf-bfd-rfc5880bis/) — This document describes a protocol intended to detect faults in the
   bidirectional path between two forwarding engines, including
   interfaces, data link(s), and to the extent possible the forwarding
   engines themselves, with potentially very low latency.  It operates
   independently of media, data protocols, and routing protocols.

   This document obsoletes RFC 5880.
- **draft-ietf-bfd-rfc5881bis-02** (new-draft, score 0, ignored_after_review) [bfd]: [Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop)](https://datatracker.ietf.org/doc/draft-ietf-bfd-rfc5881bis/) — This document describes the use of the Bidirectional Forwarding
   Detection (BFD) protocol over IPv4 and IPv6 for single IP hops.

   This document obsoletes RFC 5881.
- **draft-ietf-bier-bfd-13** (new-draft, score 0, ignored_after_review) [bier]: [BIER BFD](https://datatracker.ietf.org/doc/draft-ietf-bier-bfd/) — Point-to-multipoint (P2MP) BFD is designed to verify multipoint
   connectivity.  This document specifies the application of P2MP BFD in
   BIER network.
- **draft-ietf-bpm-alt-mark-deployment-02** (new-draft, score 0, ignored_after_review) [bpm]: [An Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   Alternate Marking methodology.
- **draft-ietf-bpm-hybrid-two-step-00** (new-draft, score 0, ignored_after_review) [bpm]: [Hybrid Two-Step Performance Measurement Method](https://datatracker.ietf.org/doc/draft-ietf-bpm-hybrid-two-step/) — The adoption of network operation automation has brought new
   measurement methodology requirements.  Among them is the ability to
   collect the instant network operational state as the packet is being
   processed by the network elements along its forwarding path through a
   network domain.  That requirement can be addressed by using on-path
   telemetry, also called hybrid performance measurement according to
   RFC 7799.  An on-path telemetry method allows operators to collect
   key information that reflects the operational state and the network
   performance a packet experiences through the forwarding path.  IOAM,
   defined in RFC 9197 and RFC 9326, is an example of such a hybrid
   method.  This document introduces a method complementary to on-path
   telemetry that causes the generation of network telemetry
   information.  This document introduces Hybrid Two-Step (HTS), a
   method complementary to both passive and hybrid measurement
   approaches.  HTS separates measuring or calculating the performance
   metric from collecting and transporting network operational state.
- **draft-ietf-bpm-savnet-sav-benchmarking-01** (new-draft, score 0, ignored_after_review) [bpm]: [Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-bpm-savnet-sav-benchmarking/) — This document defines methodologies for benchmarking the performance
   of intra-domain and inter-domain source address validation (SAV)
   mechanisms.  SAV mechanisms are utilized to generate SAV rules that
   prevent source address spoofing.  The methodology treats a SAV device
   as a black box and is therefore agnostic to the specific SAV
   mechanism and implementation used by the device.  This document
   defines test setups, performance indicators, and test cases for SAV
   accuracy, control-plane and data-plane performance, and resource
   utilization.
- **draft-ietf-bpm-stamp-cos-ecn-00** (new-draft, score 0, ignored_after_review) [bpm]: [Update of the Simple Two-way Active Measurement Protocol Class-of-Service Extension - ECN](https://datatracker.ietf.org/doc/draft-ietf-bpm-stamp-cos-ecn/) — The Simple Two-Way Active Measurement Protocol (STAMP) enables one-
   way and round-trip measurement of network metrics between IP hosts,
   and has a facility for defining optional extensions.  This document
   updates the definition of the Class of Service TLV (originally
   defined in RFC 8972) to enable the measurement of manipulation of the
   value of the Explicit Congestion Notification (ECN) field of the IP
   header by middleboxes between two STAMP hosts, and to enable
   discovery and measurement of paths that provide differential
   treatment of packets depending on the value of their ECN field.
- **draft-ietf-calext-icalendar-jscalendar-extensions-10** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545, RFC 7986, and RFC 9073.
- **draft-ietf-calext-jscalendar-icalendar-30** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-calext-rfc9555bis-03** (new-draft, score 0, ignored_after_review) [calext]: [JSContact: Converting from and to vCard](https://datatracker.ietf.org/doc/draft-ietf-calext-rfc9555bis/) — This document defines how to convert contact information between the
   JSContact and vCard data formats.  It defines conversion rules for
   every JSContact and vCard element registered at IANA at the time of
   publication.  It also defines new JSContact properties as well as
   vCard properties and parameters, to support converting arbitrary or
   unknown JSContact and vCard elements.  This document obsoletes RFC
   9555 and updates RFC 9553 and RFC 9554.

Note

   This note is to be removed before publishing as an RFC.

   Differences from RFC 9555 are documented in Appendix A.
- **draft-ietf-calext-vcard4-bis-01** (new-draft, score 0, ignored_after_review) [calext]: [vCard Format Specification](https://datatracker.ietf.org/doc/draft-ietf-calext-vcard4-bis/) — This document defines the vCard data format for representing and
   exchanging a variety of information about individuals and other
   entities (e.g., formatted and structured name and delivery addresses,
   email address, multiple telephone numbers, photograph, logo, audio
   clips, etc.).  This document obsoletes RFC 6350.
- **draft-ietf-cats-metric-definition-15** (new-draft, score 0, ignored_after_review) [cats]: [CATS Metrics Definition](https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/) — Computing-Aware Traffic Steering (CATS) is a traffic engineering
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
- **draft-ietf-detnet-tcqf-03** (new-draft, score 0, ignored_after_review) [detnet]: [Deterministic Networking (DetNet) Data Plane - Tagged Cyclic Queuing and Forwarding (TCQF) for bounded latency with low jitter in large scale DetNets](https://datatracker.ietf.org/doc/draft-ietf-detnet-tcqf/) — This memo specifies a forwarding method for bounded latency and
   bounded jitter for Deterministic Networks.  It is a variant of the
   IEEE TSN 802.1Q(ch) Cyclic Queuing and Forwarding (CQF) method,
   called Tagged CQF (TCQF), in which the cycle number is indicated in
   an existing or new packet header field, called the cycle tag.  This
   tag allows more than two cycles to be used and replaces the cycle
   mapping of CQF, which is based purely on the synchronized reception
   clock.

   Whereas CQF supports low end-to-end jitter across limited-scale
   networks with link speeds mostly up to 10Gbps, TCQF supports the same
   low end-to-end jitter across large-scale, wide-area networks with
   high per-hop latency and jitter (which is not possible with CQF), and
   enables high-speed hardware implementations above 10Gbps without
   requiring more accurate clock synchronization.  Like CQF, TCQF
   eliminates the need for per-DetNet-flow state on midpoint routers,
   requiring only flow-agnostic cycle state.  Because it is specified as
   a DetNet scheduling method, TCQF can be deployed not only as a sub-
   network method, but also as part of a DetNet forwarder.

   This memo standardizes TCQF as a mechanism independent of the tagging
   method used.  It also specifies tagging via (1) the existing MPLS
   packet Traffic Class (TC) field for MPLS packets, (2) the IP/IPv6
   DSCP field for IP/IPv6 packets, and (3) a new TCQF Option header for
   IPv6 packets.
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
- **draft-ietf-dmm-mup-architecture-04** (new-draft, score 0, ignored_after_review) [dmm]: [Mobile User Plane Architecture for Distributed Mobility Management](https://datatracker.ietf.org/doc/draft-ietf-dmm-mup-architecture/) — This document defines the Mobile User Plane (MUP) architecture for
   Distributed Mobility Management (DMM).  MUP meets the DMM
   requirements in [RFC7333] in a routing fashion.  MUP provides a
   normative mechanism that makes it possible to avoid traversing a
   single user plane anchor far from the optimal route, by turning
   mobile user plane session information into routing information and
   integrating the user plane into the dataplane.

   MUP is designed as a pluggable user plane part of existing mobile
   service architectures, with auto-discovery.  Although the
   architecture is dataplane-independent, this document describes MUP
   with an SRv6 dataplane (SRv6 MUP), whose programmability and large
   address space suit scalable mobile services.

   This mechanism is specified in terms of the semantics of MUP segments
   and of the routing information, how that information is distributed
   among MUP PEs and the MUP Controller and resolved by a MUP PE, and
   the behaviour required of them.  It does not define the wire encoding
   of any routing protocol; such an encoding may be defined in other
   documents.
- **draft-ietf-dmm-srv6mob-arch-05** (new-draft, score 0, ignored_after_review) [dmm]: [Architecture Discussion on SRv6 Mobile User plane](https://datatracker.ietf.org/doc/draft-ietf-dmm-srv6mob-arch/) — This document describes the solution approach and its architectural
   benefits of transforming mobile session information into routing
   information, leveraging segment routing capabilities, and operating
   within the IP routing paradigm.
- **draft-ietf-dnssd-advertising-proxy-07** (new-draft, score 0, ignored_after_review) [dnssd]: [Advertising Proxy for DNS-SD Service Registration Protocol](https://datatracker.ietf.org/doc/draft-ietf-dnssd-advertising-proxy/) — An Advertising Proxy advertises the contents of a DNS zone, for
   example maintained using the DNS-SD Service Registration Protocol
   (SRP), using Multicast DNS.  This allows legacy clients to discover
   services registered with SRP using Multicast DNS.
- **draft-ietf-dtn-bibe-02** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle-in-Bundle Encapsulation](https://datatracker.ietf.org/doc/draft-ietf-dtn-bibe/) — This document describes Bundle-in-Bundle Encapsulation (BIBE), a
   Delay-Tolerant Networking (DTN) Bundle Protocol (BP) tunneling
   mechanism by which a bundle is carried as the payload of one or more
   encapsulating bundles, allowing security measures and routing policy
   to be applied to the encapsulating bundle without modification of the
   encapsulated bundle.  The protocol includes an optional segmentation
   mechanism, allowing a large encapsulated bundle to be carried in
   multiple encapsulating bundles.
- **draft-ietf-dtn-udpcl-05** (new-draft, score 0, ignored_after_review) [dtn]: [Delay-Tolerant Networking UDP Convergence Layer Protocol Version 2](https://datatracker.ietf.org/doc/draft-ietf-dtn-udpcl/) — This document describes a UDP convergence layer (UDPCL) for Delay-
   Tolerant Networking (DTN).  This version of the UDPCL protocol
   clarifies requirements of the earlier experimental RFC 7122, adds
   discussion of multicast addressing, congestion signaling, and updates
   to the Bundle Protocol (BP) contents, encodings, and convergence
   layer requirements in BP version 7.  Specifically, the UDPCL uses
   CBOR-encoded BPv7 bundles as its service data unit being transported
   and provides an unacknowledged transport of such bundles.  This
   version of UDPCL also includes security and extensibility mechanisms.
- **draft-ietf-emailcore-iana-cleanup-04** (new-draft, score 0, ignored_after_review) [emailcore]: [Updates to SMTP related IANA registries](https://datatracker.ietf.org/doc/draft-ietf-emailcore-iana-cleanup/) — While EMAILCORE working group was working on update to SMTP
   specification, it became clear that existing entries in SMTP related
   registries are missing information or contain stale information and
   need to be updated.  This document updates such entries.
- **draft-ietf-grow-bmp-stats-informational-tlv-02** (new-draft, score 0, ignored_after_review) [grow]: [BMP Statistics Information TLV](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-stats-informational-tlv/) — The BGP Monitoring Protocol (BMP) defines statistics reports that
   provide periodic snapshots of various BGP-related metrics.  When
   statistics are reported periodically, the snapshot values may not
   reflect the variations that occurred between reporting intervals.
   This document defines a Statistics Information TLV that can be used
   to convey additional statistical information about BMP gauge-type
   statistics during the reporting period.  This TLV reports the minimum
   and maximum values observed (with timestamps indicating when they
   occurred), along with additional statistical measures such as
   average, percentiles, or snapshot values.  This enables BMP
   collectors to better understand the dynamics of monitored statistics
   even when the reported snapshot values appear constant.
- **draft-ietf-idr-addpath-paths-limit-00** (new-draft, score 0, ignored_after_review) [idr]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-ietf-idr-bgp-ct-srv6-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP CT - Adaptation to SRv6 and Other dataplanes](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ct-srv6/) — This document specifies how the mechanisms for "Intent Driven Service
   Mapping" defined in [RFC9832] are applied to non-MPLS dataplanes.
   The extensions needed for SRv6 dataplane operations are specified.
   Base procedures of BGP CT are followed unaltered.

   Illustration of how BGP CT procedures work in SRv6 dataplane is
   provided in this document.
- **draft-ietf-idr-bgp-ls-link-mtu-13** (new-draft, score 0, ignored_after_review) [idr]: [Signaling Maximum Transmission Unit (MTU) using BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-link-mtu/) — Segment Routing (SR) leverages the source routing paradigm, which can
   be directly applied to the MPLS architecture and IPv6 architecture,
   with a new type of routing header.  Since multiple labels or SRv6
   SIDs are pushed in the packets, it is more likely that the packet
   size exceeds the path MTU of SR tunnel.  However, SR uses the IGP as
   the routing protocol and does not support the negotiation of the Path
   MTU.

   BGP Link State (BGP-LS) describes a mechanism by which link-state and
   TE information can be collected from networks and shared with
   external components using the BGP routing protocol.  This document
   specifies the extensions to BGP-LS to carry MTU information of link.
   The centralized controller (PCE/SDN) calculates the Path MTU while
   completing the service path calculation based on the information
   transmitted by the BGP-LS.
- **draft-ietf-idr-bgp4-rfc4271bis-06** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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

   This document obsoletes RFC 4271 and many other RFCs.  It updates RFC
   7606, RFC 7607 and RFC 9774 by subsuming their functionality as
   relates to RFC 4271.
- **draft-ietf-idr-flowspec-traffic-compress-action-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow-Spec Traffic Compress Action](https://datatracker.ietf.org/doc/draft-ietf-idr-flowspec-traffic-compress-action/) — BGP Flow Specification Version 2 (FSv2) provides an extensible
   framework for disseminating traffic flow specification rules and
   associated actions.  While traditional Flow-spec actions cover rate-
   limiting, redirecting, and marking, emerging applications require
   dynamic bandwidth optimization.  This document specifies a new
   traffic filtering action to support selective, on-demand traffic
   compression across network domains using BGP Extended Communities
   aligned with the FSv2 architecture.
- **draft-ietf-idr-fsv2-scheduling-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 Extensions for Scheduling](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-scheduling/) — BGP Flow Specification allows conveying flow specifications and
   associated traffic actions/rules to perform different actions based
   on traffic characteristics.  Existing traffic filter rules and
   actions in FSv2 remain effective perpetually; once delivered to the
   headend, the rules and actions are permanent for traffic.  However,
   some operators wish to perform different actions for specific flows
   at specific time.

   This document extends BGP FSv2 with a scheduling time component to
   match the arrival time of packets.  Based on this component, the
   headend can perform different actions for specific traffic at
   different times.
- **draft-ietf-idr-multinexthop-attribute-06** (new-draft, score 0, ignored_after_review) [idr]: [BGP MultiNexthop Attribute](https://datatracker.ietf.org/doc/draft-ietf-idr-multinexthop-attribute/) — Today, a BGP speaker can advertise one nexthop for a set of NLRIs in
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
- **draft-ietf-idr-next-next-hop-nodes-02** (new-draft, score 0, ignored_after_review) [idr]: [BGP Next-next Hop Nodes](https://datatracker.ietf.org/doc/draft-ietf-idr-next-next-hop-nodes/) — BGP speakers learn their next-hop addresses for NLRI in RFC 4271 in
   the NEXT_HOP field and in RFC 4760 in the "Network Address of Next
   Hop" field.  Under certain circumstances, it might be desirable for a
   BGP speaker to know both the next-hops and the next-next-hops of NLRI
   to make optimal forwarding decisions.  One such example is global
   load balancing (GLB) in a Clos network.

   Draft-ietf-idr-nhc defines the "Next Hop Dependent Characteristics
   Attribute" (NHC) which allows a BGP speaker to signal the forwarding
   characteristics associated with a given next-hop.

   This document defines a new NHC characteristic, the Next-next Hop
   Nodes (NNHN) characteristic, which can be used to advertise the next-
   next-hop nodes associated with a given next-hop.
- **draft-ietf-idr-otc-rs-verification-00** (new-draft, score 0, ignored_after_review) [idr]: [Strict Only to Customer (OTC) Verification on Route Server Sessions](https://datatracker.ietf.org/doc/draft-ietf-idr-otc-rs-verification/) — RFC 9234 specifies how an AS receiving a route from a lateral Peer
   can check if a route was leaked, but doesn't specify any checks for
   routes received from a Route Server (RS).  This makes the quality of
   filtering dependent on whether the RS implements RFC 9234.

   This document updates RFC 9234 by adding a complementary ingress
   check by an RS-Client.
- **draft-ietf-idr-rt-derived-community-16** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route-Target-derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route-Target-derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-intarea-v4-via-v6-10** (new-draft, score 0, ignored_after_review) [intarea]: [IPv4 routes with an IPv6 next hop](https://datatracker.ietf.org/doc/draft-ietf-intarea-v4-via-v6/) — V4-via-v6 routing is a technique that uses IPv6 next-hop addresses
   for forwarding IPv4 packets, and thus makes it possible to route IPv4
   packets across a network where some routers have not been assigned
   IPv4 addresses.  This document describes v4-via-v6 routing, and
   defines related operational procedures, notably the origination of
   ICMPv4 packets by nodes that might not have an IPv4 address.
- **draft-ietf-iotops-iot-dns-guidelines-07** (new-draft, score 0, ignored_after_review) [iotops]: [IoT DNS Security and Privacy Guidelines](https://datatracker.ietf.org/doc/draft-ietf-iotops-iot-dns-guidelines/) — This document outlines guidance for Internet of Things (IoT)
   manufacturers regarding the implementation of DNS stub resolver
   software on devices, and for the management zones used for purposes
   such as device configuration and software upgrades.  It aims to
   mitigate security threats, enhance privacy, and to address
   operational security challenges.

   DNS resolution between devices and management zone servers depends
   upon DNS services within operator networks, and these services and
   operator networks can be impacted by device behavior.  Hence, this
   document also provides guidance to network operators that deploy IoT
   devices to mitigate the specific risks identified in this document
   and take advantage of improved DNS security mechanisms provided by
   manufacturers.
- **draft-ietf-ipsecme-rfc7402-beet-update-00** (new-draft, score 0, ignored_after_review) [ipsecme]: [A Bound End-to-End Tunnel (BEET) mode for ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-rfc7402-beet-update/) — This document is an update to the Bound End-to-End Tunnel (BEET) mode
   for ESP in as described in [RFC7402].  It brings the description in
   alignment with the addition of BEET mode for IKEv2 without any
   processing changes as described in [RFC7402]
- **draft-ietf-jmap-blobext-05** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Blob Management](https://datatracker.ietf.org/doc/draft-ietf-jmap-blobext/) — The JSON Meta Application Protocol (JMAP) base protocol provides the
   ability to upload and download arbitrary binary data, called "blobs",
   via HTTP POST and GET on a defined endpoint.

   This document defines JMAP methods to create and read blobs within a
   JMAP request, to find which objects reference a blob, to build large
   blobs from chunks, and to convert blobs on the server: converting
   images, creating and extracting archives, compressing and
   decompressing, and computing and applying deltas.  It obsoletes RFC
   9404 and updates RFC 8620.
- **draft-ietf-jmap-conditional-03** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Conditional Set](https://datatracker.ietf.org/doc/draft-ietf-jmap-conditional/) — The JMAP base protocol ([JMAP-CORE]) provides the Foo/set method for
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
- **draft-ietf-jmap-emailpush-05** (new-draft, score 0, ignored_after_review) [jmap]: [JSON Meta Application Protocol (JMAP) Email Delivery Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-jmap-emailpush/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) that allows clients to receive an object via a JMAP
   push subscription whenever a new email is delivered that matches a
   client-defined filter.  The object can also include properties from
   the email, to allow a user notification to be displayed without
   having to make a further network request.  Clients can also receive
   an object whenever a count of the emails in a chosen mailbox changes,
   for example to set a badge on an app icon.
- **draft-ietf-jmap-filenode-22** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP File Storage extension](https://datatracker.ietf.org/doc/draft-ietf-jmap-filenode/) — The JMAP base protocol (RFC 8620) provides the ability to upload and
   download arbitrary binary data.  This binary data is called a "blob",
   and can be used in all other JMAP extensions.

   This extension adds a FileNode data type and methods to expose blobs
   as a filesystem, along with the types of metadata that are provided
   by other remote filesystem protocols.
- **draft-ietf-jmap-object-history-04** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Object History](https://datatracker.ietf.org/doc/draft-ietf-jmap-object-history/) — The JMAP base protocol (RFC8620) provides methods for synchronizing
   the current state of data objects between client and server.  This
   extension adds the ability to retrieve historical versions of
   objects, including objects that have been destroyed, by extending the
   standard Foo/get method, to find destroyed objects with Foo/query,
   and to restore them with Foo/set.
- **draft-ietf-jmap-smime-sender-extensions-05** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP extension for S/MIME signing and encryption](https://datatracker.ietf.org/doc/draft-ietf-jmap-smime-sender-extensions/) — This document specifies an extension to JMAP for sending S/MIME
   signed and/or S/MIME encrypted messages, as well as automatic
   decryption of received S/MIME messages.

   [[This version presents an alternative syntax to revision 04 of
   https://datatracker.ietf.org/doc/draft-ietf-jmap-smime-sender-
   extensions/]]
- **draft-ietf-lake-private-use-ranges-00** (new-draft, score 0, ignored_after_review) [lake]: [Additional Private Use Ranges in the IANA Registries of the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-lake-private-use-ranges/) — This document adds Private Use ranges to IANA registries that pertain
   to the Lightweight Authenticated Key Exchange (LAKE) protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Lightweight
   Authenticated Key Exchange Working Group mailing list
   (lake@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/lake/.

   Source for this draft and an issue tracker can be found at
   https://github.com/lake-wg/private-use-ranges.
- **draft-ietf-mailmaint-smtputf8-syntax-07** (new-draft, score 0, ignored_after_review) [mailmaint]: [SMTPUTF8 Email Addresses](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-smtputf8-syntax/) — This document updates the email address syntax to include the
   addresses in active use, include the addresses likely to be used
   based on what writing systems are used together, and exclude
   addresses that pose risks when recipient software renders or
   processes them.
- **draft-ietf-mailmaint-unobtrusive-signatures-03** (new-draft, score 0, ignored_after_review) [mailmaint]: [Unobtrusive End-to-End Email Signatures](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-unobtrusive-signatures/) — This document deals with end-to-end cryptographically signed email.
   It introduces a structure for signed email that is designed to avoid
   creating any disturbance in legacy email clients.  This "unobtrusive"
   signature structure removes disincentives for signing email.
- **draft-ietf-mboned-non-source-routed-sr-mcast-07** (new-draft, score 0, ignored_after_review) [mboned]: [Non-source-routed Multicast in SR Networks](https://datatracker.ietf.org/doc/draft-ietf-mboned-non-source-routed-sr-mcast/) — With Segment Routing (SR) architecture, a unicast flow can be source-
   routed through an SR network following an explicit path specified in
   the packet, without the need for per-flow state in the network.  As a
   result, the protocols that would be otherwise needed to signal the
   per-flow unicast state are not needed either.  In the case of
   multicast, traffic can be either source-routed or non-source-routed,
   and this document summarizes options for non-source-routed multicast
   in an SR network, including pre-SR tree-based multicast technologies,
   BIER, and various SR specific solutions.  The pros and cons of each
   solution are listed for considerations by operators and vendors, with
   regard to the principle and characteristic of SR as mentioned above.
- **draft-ietf-mlcodec-opus-speech-coding-enhancement-07** (new-draft, score 0, ignored_after_review) [mlcodec]: [Integration of Speech Codec Enhancement Algorithms into the Opus Codec](https://datatracker.ietf.org/doc/draft-ietf-mlcodec-opus-speech-coding-enhancement/) — This document proposes a set of requirements for integrating a speech
   codec enhancement algorithm into the Opus codec [RFC6716].  It also
   updates [RFC7587] to define two optional media type parameters for
   signaling decoder-side speech enhancement capabilities.
- **draft-ietf-mls-pq-ciphersuites-08** (new-draft, score 0, ignored_after_review) [mls]: [ML-KEM and Hybrid Cipher Suites for Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-pq-ciphersuites/) — This document registers new cipher suites for Messaging Layer
   Security (MLS) based on "post-quantum" algorithms, which are intended
   to be resilient to attack by quantum computers.  These cipher suites
   are constructed using the new Module-Lattice-Based Key-Encapsulation
   Mechanism (ML-KEM), optionally in combination with traditional
   elliptic curve KEMs, together with appropriate authenticated
   encryption, hash, and signature algorithms.
- **draft-ietf-moq-msf-02** (new-draft, score 0, ignored_after_review) [moq]: [MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-ietf-moq-msf/) — This document specifies the MOQT Streaming Format, designed to
   operate on Media Over QUIC Transport.
- **draft-ietf-mpls-mna-ioam-17** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
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
- **draft-ietf-mpls-on-path-telemetry-flag-06** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes postcard-based on-path telemetry with packet
   marking (PBT-M) using an MPLS Network Actions (MNA) flag to support
   Operations, Administration, and Maintenance (OAM) in MPLS networks.
   The scheme uses a single flag bit carried in a Flag-Based Network
   Action Indicator (Opcode 1) of the MNA Sub-Stack as defined in RFC
   9994.  In addition to addressing the protocol requirements for
   applying PBT-M, this document provides comprehensive operational,
   manageability, and security considerations.
- **draft-ietf-mpls-stamp-02** (new-draft, score 0, ignored_after_review) [mpls]: [Simple Two-way Active Measurement Protocol (STAMP) for MPLS Label Switched Paths (LSPs)](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp/) — Simple Two-way Active Measurement Protocol (STAMP), defined in RFC
   8762 and RFC 8972, is expected to be able to monitor the performance
   of paths between systems that use a wide variety of encapsulations.
   This document defines encapsulation and bootstrapping of a STAMP test
   session over an MPLS Label Switched Path.
- **draft-ietf-netconf-quic-call-home-02** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Call Home and RESTCONF Call Home Using QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-call-home/) — This RFC extends NETCONF Call Home and RESTCONF Call Home [RFC 8071]
   to support the QUIC protocol [RFC 9000].
- **draft-ietf-netconf-quic-client-server-10** (new-draft, score 0, ignored_after_review) [netconf]: [YANG Groupings for QUIC clients and QUIC servers](https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-client-server/) — This document defines three YANG 1.1 modules to support the
   configuration of QUIC clients and QUIC servers.  The common YANG
   module defines reusable groupings for setting parameters imported
   from the QUIC version and QUIC transport IANA YANG modules.  The two
   QUIC client and server YANG modules define reusable groupings for
   QUIC connection settings, including the common QUIC parameters, for
   protocol implementation.  Furthermore two initial YANG 1.1 modules
   for the IANA registries "QUIC Versions" and "QUIC Transport
   Parameters" are included in Appendix.
- **draft-ietf-netmod-yang-config-templates-00** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Configuration Templates](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-config-templates/) — This document defines a YANG-based configuration template mechanism
   whereby repetitive configuration data can be factored out into
   templates and applied where needed.  This avoids the redundant
   definition of identical configuration and ensures the consistency of
   it, thus allowing configuration data to be managed more conveniently
   and efficiently.
- **draft-ietf-nfsv4-internationalization-18** (new-draft, score 0, ignored_after_review) [nfsv4]: [Internationalization for the NFSv4 Protocols](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-internationalization/) — This document describes the handling of internationalization for the
   NFSv4 protocols, including NFSv4.0, NFSv4.1, NFSv4.2 and extensions
   thereof, and future minor versions.  It updates RFC7530 and RFC8881.
- **draft-ietf-nfsv4-uncacheable-directories-13** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Dirent Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  Such
   a cache is not invalidated by the directory's change attribute, which
   reflects changes to the directory and its entries but not writes to
   the files those entries name, so it can become stale when another
   client changes one of those files.  In some deployments this produces
   incorrect size and modification times often enough to be a problem.
   This document introduces an uncacheable dirent metadata attribute for
   NFSv4.2 that allows a server to identify a directory for which an
   honoring client enumerates by READDIR and reports each entry's
   attributes as that READDIR returned them, rather than from a value it
   held earlier.
- **draft-ietf-nmop-network-anomaly-lifecycle-08** (new-draft, score 0, ignored_after_review) [nmop]: [Network Anomaly Detection Lifecycle](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-anomaly-lifecycle/) — This document defines a structured, iterative lifecycle for network
   anomaly detection systems to enable "human-in-the-loop" refinements.
   Key contributions include defining three lifecycle stages, a state
   machine for anomaly annotations, and YANG data models for
   standardized labeling and exchange.
- **draft-ietf-ocm-mls-federated-groups-01** (new-draft, score 0, ignored_after_review) [ocm]: [Federated Groups in Open Cloud Mesh using Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-ocm-mls-federated-groups/) — This document defines an extension to the Open Cloud Mesh (OCM)
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
- **draft-ietf-openpgp-hkp-02** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP HTTP Keyserver Protocol](https://datatracker.ietf.org/doc/draft-ietf-openpgp-hkp/) — This document specifies a series of conventions to implement an
   OpenPGP keyserver using the Hypertext Transfer Protocol (HTTP).  As
   this document is a codification and extension of a protocol that is
   already in wide use, strict attention is paid to backward
   compatibility with these existing implementations.
- **draft-ietf-openpgp-replacementkey-09** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP Key Replacement](https://datatracker.ietf.org/doc/draft-ietf-openpgp-replacementkey/) — This document specifies a method in OpenPGP to suggest a replacement
   for an expired, revoked, or deprecated primary key.
- **draft-ietf-opsawg-ipfix-alt-mark-11** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-ipfix-gpon-gem-04** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of Gigabit Passive Optical Network Encapsulation Method in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-gpon-gem/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements to identify a set of G-PON Encapsulation Method
   entities in the Passive Optical Transport of the Optical Distribution
   Network.
- **draft-ietf-pce-pcep-nrp-03** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions for Network Resource Partition (NRP)](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-nrp/) — This document specifies the extensions to Path Computation Element
   Communication Protocol (PCEP) to carry Network Resource Partition
   (NRP) related information in the PCEP messages.  The extensions in
   this document can be used to indicate the NRP-specific constraints
   and information needed in path computation, path status report and
   path initialization.
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
- **draft-ietf-pce-state-sync-17** (new-draft, score 0, ignored_after_review) [pce]: [State Synchronization Procedures between Stateful Path Computation Elements (PCEs)](https://datatracker.ietf.org/doc/draft-ietf-pce-state-sync/) — The Path Computation Element (PCE) Communication Protocol (PCEP)
   provides mechanisms for PCEs to perform path computation in response
   to a Path Computation Client (PCC) request.  The stateful PCE
   extensions allow a PCE to maintain and control the state of Label
   Switched Paths (LSPs) using PCEP, independent of the path setup type
   used.

   A PCC can synchronize LSP state information to a stateful PCE, and
   can have PCEP sessions toward multiple PCEs.  In some deployments,
   synchronizing LSP state directly between the stateful PCEs brings
   additional resiliency, for instance when a PCC-PCE session fails, and
   allows a single PCE to compute paths for a set of LSPs that are
   dependent on each other even when those LSPs are delegated to
   different PCEs.

   This document describes procedures for synchronizing LSP state
   between stateful PCEs across various deployment scenarios and for
   preventing looping path computation requests.  It is published as
   Experimental to gather implementation and deployment experience.
- **draft-ietf-pim-rpf-vector-conflict-resolution-00** (new-draft, score 0, ignored_after_review) [pim]: [PIM Reverse Path Forwarding (RPF) Vector Conflict Resolution](https://datatracker.ietf.org/doc/draft-ietf-pim-rpf-vector-conflict-resolution/) — PIM Join Attributes specification defines the handling principles
   for PIM Join attributes with same type of RFF Vector and Explicit
   RFP Vector, but with different contents are received.

   However, it does not address scenarios where one downstream router
   includes a RFF Vector in its message while another does not. This
   leaves the handling of such conflicts unspecified.

   This document updates RFC 5496 and RFC 7891 by supplementing the
   existing specifications with handling rules for this specific
   conflict scenario.
- **draft-ietf-pquip-pqc-hsm-constrained-12** (new-draft, score 0, ignored_after_review) [pquip]: [Adapting Constrained Devices for Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/) — This document provides guidance on integrating Post-Quantum
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
- **draft-ietf-quic-receive-ts-04** (new-draft, score 0, ignored_after_review) [quic]: [QUIC Extended Acknowledgement for Reporting Packet Receive Timestamps](https://datatracker.ietf.org/doc/draft-ietf-quic-receive-ts/) — This document defines an extension to the QUIC transport protocol
   which supports reporting multiple packet receive timestamps for post-
   handshake packets.
- **draft-ietf-regext-rdap-extensions-19** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes, clarifies and further specifies the usage of
   extensions in RDAP.
- **draft-ietf-rtgwg-multisegment-sdwan-18** (new-draft, score 0, ignored_after_review) [rtgwg]: [Multi-segment SD-WAN via Cloud Backbone](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/) — This document describes a method for seamlessly
   interconnecting geographically separated SD-WAN segments via
   a Cloud Backbone without requiring Cloud Gateways (GWs) to
   decrypt and re-encrypt traffic. By encapsulating IPsec-
   encrypted payloads within GENEVE headers (RFC 8926), the
   approach enables Cloud GWs to forward encrypted traffic
   directly between distant Customer Premises Equipment (CPEs).
   This reduces processing overhead, improves scalability, and
   preserves the confidentiality of enterprise data while
   ensuring secure and efficient multi-segment SD-WAN
   connectivity.
- **draft-ietf-scone-protocol-11** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-rpki-erik-protocol-08** (new-draft, score 0, ignored_after_review) [sidrops]: [The Erik Synchronization Protocol for use with the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rpki-erik-protocol/) — This document specifies the Erik Synchronization Protocol for use
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
- **draft-ietf-spring-srv6-security-20** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing over IPv6 (SRv6) Security Considerations](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/) — Segment Routing over IPv6 (SRv6) is the instantiation of Segment
   Routing on the IPv6 data plane, using IPv6 addresses to identify
   segments.  This document discusses security considerations in SRv6
   networks, including the potential threats and the possible mitigation
   methods.  The document does not define any new security protocols or
   extensions to existing protocols.
- **draft-ietf-spring-stamp-srpm-mpls-14** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document specifies procedures for
   performance measurement in SR-MPLS networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths, including Segment Lists of SR Policies, SR-MPLS IGP
   best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 services and point-to-point Layer-2 services carried
   over those paths.
- **draft-ietf-sshm-composite-sigs-01** (new-draft, score 0, ignored_after_review) [sshm]: [Post-Quantum Composite Signatures in SSH](https://datatracker.ietf.org/doc/draft-ietf-sshm-composite-sigs/) — This document specifies the integration of two composite post-quantum
   signature schemes into the Secure Shell (SSH) protocol.  These
   schemes combine the post-quantum Module-Lattice Digital Signature
   Algorithm (ML-DSA) with Elliptic Curve signature algorithms (Ed25519
   and ECDSA, respectively) to provide security against both quantum and
   classical adversaries.

Note

   This note is to be removed before publishing as an RFC.

   In the IANA considerations section, please replace "thisRFC" with
   "RFC" and the assigned number, when known.
- **draft-ietf-sshm-hostkey-update-02** (new-draft, score 0, ignored_after_review) [sshm]: [Host key update mechanism for SSH](https://datatracker.ietf.org/doc/draft-ietf-sshm-hostkey-update/) — This document describes an extension to allow a Secure Shell (SSH)
   server to inform a client of the full set of host keys it supports.
   This may be used for graceful host key rotation and to provide keys
   for additional signature algorithms to the client, supporting
   algorithm agility.
- **draft-ietf-sshm-sshsig-format-00** (new-draft, score 0, ignored_after_review) [sshm]: [Lightweight Secure Shell (SSH) Signature Format](https://datatracker.ietf.org/doc/draft-ietf-sshm-sshsig-format/) — This document describes a lightweight SSH Signature format that is
   compatible with SSH keys and wire formats.
- **draft-ietf-sshm-strict-kex-03** (new-draft, score 0, ignored_after_review) [sshm]: [SSH Strict KEX extension](https://datatracker.ietf.org/doc/draft-ietf-sshm-strict-kex/) — This document describes a small set of modifications to the Secure
   Shell (SSH) protocol to fix the so-called Terrapin Attack on the
   initial key exchange.
- **draft-ietf-tcpm-tcp-ghost-acks-10** (new-draft, score 0, ignored_after_review) [tcpm]: [Improve TCP Handling of Out-of-Window Packets to Mitigate Ghost ACKs](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ghost-acks/) — Historically, TCP as specified in RFC 793 was threatened by the blind
   data injection attack because of the loose SEG.ACK value validation,
   where the SEG.ACK value of a TCP segment is considered valid in
   synchronized states as long as it does not acknowledge data ahead of
   what has been sent.  RFC 5961 improved the input validation by
   shrinking the range of acceptable SEG.ACK values in a TCP segment.
   Later, RFC 9293 incorporated the updates proposed by RFC 5961 as a
   TCP stack implementation option.
   However, an endpoint that follows the RFC 9293 specifications can
   still accept in synchronized states a TCP segment containing an
   SEG.ACK value acknowledging data that the endpoint has never sent.
   This document specifies small modifications to the way TCP verifies
   incoming TCP segments' SEG.ACK value to prevent TCP from accepting
   such invalid SEG.ACK values.
- **draft-ietf-teas-nrp-scalability-11** (new-draft, score 0, ignored_after_review) [teas]: [Scalability Considerations for Network Resource Partition](https://datatracker.ietf.org/doc/draft-ietf-teas-nrp-scalability/) — A network slice offers connectivity services to a network slice
   customer with specific Service Level Objectives (SLOs) and Service
   Level Expectations (SLEs) over a common underlay network.

   RFC 9543 describes a framework for network slices in networks built
   using IETF technologies.  As part of that framework, the Network
   Resource Partition (NRP) is introduced as a subset of buffer/queuing/
   scheduling resources that are allocated from the underlay network to
   carry a specific set of network slice service traffic and meet the
   requested SLOs and SLEs.

   As the demand for network slices increases, scalability becomes an
   important factor.  Although the scalability of network slices can be
   improved by mapping a group of network slices to a single NRP, that
   design may not be suitable or possible for all deployments, thus
   there are concerns about the scalability of NRPs themselves.

   This document discusses some considerations for NRP scalability in
   the control and data planes.  It also investigates a set of
   optimization mechanisms.
- **draft-ietf-teas-ns-models-applicability-03** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of IETF-Defined Service and Network Data Models for Network Slice Service Management](https://datatracker.ietf.org/doc/draft-ietf-teas-ns-models-applicability/) — This document describes how IETF-defined YANG data models can be used
   together to manage RFC 9543 Network Slice Services.  It explains how
   a Network Slice Controller (NSC) translates a customer-facing Network
   Slice Service request into requests based on network models, such as
   the L3VPN and L2VPN Network Models, and how these relate to the
   corresponding service models.  The document compares these models
   against Network Slice Service requirements, identifies gaps, and
   shows how the models apply in different controller architectures,
   including multi-domain deployments.
- **draft-ietf-v6ops-ipv6-app-testing-10** (new-draft, score 0, ignored_after_review) [v6ops]: [Recommendations for IPv6 Testing of Applications](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   Software-as-a-Service (SaaS) providers on how to approach IPv6
   testing in Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including
   "IPv6-only-strict" scenarios without any connectivity towards any
   relevant IPv4 endpoint.

   The document also discusses common misconceptions about the degree to
   which Operating Systems and libraries can abstract IPv6 issues away
   and explains common regressions to avoid when deploying IPv6 support.
- **draft-ietf-v6ops-ipv6-only-08** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  In
   particular, a goal is to provide a reference that describes the
   actual "IPv6-Only" functionality being used in a given scope, not the
   installed protocol stack support.
- **draft-ietf-v6ops-prefix-to-end-sites-02** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Prefix Assignment to End-Sites](https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/) — This document describes different alternatives and best current
   practices for assignment of IPv6 prefixes for end-sites in broadband
   networks, including considerations about point-to-point links, their
   size, numbering choices, pool choices, customer prefix assignment
   size and persistence of those assignments.
- **draft-ietf-v6ops-rfc7915-bis-03** (new-draft, score 0, ignored_after_review) [v6ops]: [IP/ICMP Translation Algorithm](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/) — This document describes the Stateless IP/ICMP Translation Algorithm
   (SIIT), which translates between IPv4 and IPv6 packet headers
   (including ICMP headers).  This document obsoletes RFC 7915.
- **draft-irtf-iccrg-pacing-05** (new-draft, score 0, ignored_after_review) [iccrg]: [Pacing in Transport Protocols](https://datatracker.ietf.org/doc/draft-irtf-iccrg-pacing/) — Applications or congestion control mechanisms can produce bursty
   traffic, which can cause unnecessary queuing and packet loss.  To
   reduce the burstiness of traffic, the concept of evenly spacing out
   the traffic from a data sender over a round-trip time known as
   "pacing" has been used in many transport protocol implementations.
   This document gives an overview of pacing and how some known pacing
   implementations work.  It is a product of the Internet Congestion
   Control Research Group (ICCRG) of the Internet Research Task Force
   (IRTF).
- **draft-jabley-regext-allowable-dnssec-parameters-01** (new-draft, score 0, ignored_after_review) [none]: [Acceptance of DNSSEC Parameters in EPP](https://datatracker.ietf.org/doc/draft-jabley-regext-allowable-dnssec-parameters/) — The Extensible Provisioning Protocol (EPP) is used to submit DNSSEC
   parameters for domain names to domain name registries.  Registries
   and registrars often restrict the values they accept, and those
   restrictions vary from registry to registry.  The resulting
   uncertainty makes it difficult for DNS operators to adopt new
   algorithms.  This document recommends that registries and registrars
   base their acceptance policies on the IANA registries for DNSSEC
   algorithms and digest types.
- **draft-jags-6man-icmp-error-srv6-evpn-00** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for EVPN-VPWS in SRv6 Networks](https://datatracker.ietf.org/doc/draft-jags-6man-icmp-error-srv6-evpn/) — This document describes procedures for handling ICMP error messages
   for Ethernet VPN Virtual Private Wire Service (EVPN-VPWS) in Segment
   Routing over IPv6 (SRv6) networks.  It describes an ingress-PE
   approach that associates a received ICMPv6 error with the EVPN
   service, constructs eligible customer ICMP feedback, and uses local
   End.DX2 disposition to apply the appropriate Ethernet and VLAN
   treatment.  The discussion covers IPv4 and IPv6 customer traffic, the
   handling of the different ICMP error classes, and the additional
   procedures applicable to Packet Too Big messages and Path MTU
   Discovery.
- **draft-jags-spring-icmp-error-srv6-evpn-00** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for EVPN-VPWS in SRv6 Networks](https://datatracker.ietf.org/doc/draft-jags-spring-icmp-error-srv6-evpn/) — This document describes procedures for handling ICMP error messages
   for Ethernet VPN Virtual Private Wire Service (EVPN-VPWS) in Segment
   Routing over IPv6 (SRv6) networks.  It describes an ingress-PE
   approach that associates a received ICMPv6 error with the EVPN
   service, constructs eligible customer ICMP feedback, and uses local
   End.DX2 disposition to apply the appropriate Ethernet and VLAN
   treatment.  The discussion covers IPv4 and IPv6 customer traffic, the
   handling of the different ICMP error classes, and the additional
   procedures applicable to Packet Too Big messages and Path MTU
   Discovery.
- **draft-john-scion-happy-eyeballs-00** (new-draft, score 0, ignored_after_review) [none]: [SCION in Happy Eyeballs Version 3](https://datatracker.ietf.org/doc/draft-john-scion-happy-eyeballs/) — SCION (Scalability, Control, and Isolation On Next-generation
   networks) is a path-aware inter-domain network architecture in which
   an endpoint chooses the path of its packets.  A service can publish
   SCION addresses next to its IPv4 and IPv6 addresses in DNS Service
   Binding (SVCB) and HTTPS records.  This document specifies how a
   Happy Eyeballs Version 3 client uses these addresses.  SCION
   addresses form a third address family, so that the client connects
   over SCION where SCION works and over IP where it does not.  Because
   one path can fail while others work, the client attempts a SCION
   address on up to three paths that differ from each other (two by
   default).  It starts these attempts a short delay apart (50
   milliseconds by default), each as a separate connection, and uses the
   first attempt that succeeds.  This document is Experimental.  It
   states what is to be measured to confirm or change these defaults.
- **draft-josefsson-ssh-rfc4716-00** (new-draft, score 0, ignored_after_review) [none]: [The Secure Shell (SSH) Public Key File Format](https://datatracker.ietf.org/doc/draft-josefsson-ssh-rfc4716/) — This document formally documents an existing public key file format
   in use for exchanging public keys between different Secure Shell
   (SSH) implementations.

   In addition, this document defines a standard textual representation
   for SSH public key fingerprints.
- **draft-kafara-walled-private-network-01** (new-draft, score 0, ignored_after_review) [none]: [Walled Private Network (WPN) Service Definition](https://datatracker.ietf.org/doc/draft-kafara-walled-private-network/) — This document specifies Walled Private Network (WPN) as a technology-
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
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-05** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.
- **draft-kalosha-stb-tls13-02** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-kazuho-quic-delegated-stateless-reset-02** (new-draft, score 0, ignored_after_review) [none]: [Delegating QUIC Stateless Resets](https://datatracker.ietf.org/doc/draft-kazuho-quic-delegated-stateless-reset/) — This document specifies how a QUIC endpoint can delegate sending
   Stateless Resets to a component that outlives its connection state.
   It also defines a frame for clients using zero-length Connection IDs
   to advertise a Stateless Reset Token and a transport parameter for
   servers to indicate support for receiving the frame.
- **draft-kozuka-quic-stateless-punch-00** (new-draft, score 0, ignored_after_review) [none]: [Stateless Server-Assisted Hole Punching for QUIC](https://datatracker.ietf.org/doc/draft-kozuka-quic-stateless-punch/) — This document specifies a QUIC extension that lets two endpoints
   connected through a relay establish a direct path between them when
   one or both are behind Network Address Translators (NATs).  The
   client asks the server, over the existing connection, to send a
   single small "punch" packet toward one of the client's address
   candidates.  The server keeps no per-attempt state and does not
   initiate validation of candidate paths.  After a short delay, the
   client validates the direct path using ordinary client-initiated path
   validation as defined in RFC 9000, or ordinary path creation as
   defined in RFC 10069 when QUIC multipath is in use, and can then
   migrate the connection to it.
- **draft-li-rtgwg-overload-alleviation-01** (new-draft, score 0, ignored_after_review) [none]: [Common Approaches to Link Overload Alleviation](https://datatracker.ietf.org/doc/draft-li-rtgwg-overload-alleviation/) — Network links may become degraded because of physical conditions or
   owing to partial link failure: this can result in a reduction of
   available bandwidth.  Alternatively, traffic volume may increase
   significantly and unexpectedly.  These circumstances may lead to
   links becoming overloaded which can result in dropped packets or
   degraded delivery such as increased delay.

   Traffic adjustment techniques can be applied to alleviate these link-
   overload situations by steering some of the traffic onto other paths
   that are less loaded and have available bandwidth.

   This document examines the scenarios in which links can become
   overloaded, the requirements for steering traffic to reduce link-
   overload, and the techniques that can be applied to alleviate
   overloaded links.
- **draft-liu-grow-bmp-rm-aggregated-07** (new-draft, score 0, ignored_after_review) [none]: [Efficient BMP Route Monitoring Messages](https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/) — This document proposes two complementary optimizations for the BGP
   Monitoring Protocol (BMP) Route Monitoring message to significantly
   reduce network overhead and improve monitoring efficiency.  The first
   optimization defines an aggregated BMP Route Monitoring message based
   on the Multi-Peer Header mechanism, which compresses multiple BMP
   Route Monitoring messages into a single aggregated message by
   leveraging BGP group packaging technology.  The second optimization
   introduces a Common Update TLV that eliminates redundant transmission
   of routes unchanged by inbound or outbound policies across different
   RIB views.  These optimizations work together to reduce the number of
   reported BMP messages, decrease bandwidth consumption, and improve
   processing efficiency for both monitored routers and monitoring
   stations.
- **draft-liu-iotops-pqc-uasc-01** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Cryptographic Protection Profile for OPC UA Secure Conversation](https://datatracker.ietf.org/doc/draft-liu-iotops-pqc-uasc/) — This document specifies a post-quantum cryptographic protection
   profile for the OPC Unified Architecture Secure Conversation protocol
   (OPC UA UASC) carried over the opc.tcp transport.  The profile uses
   ML-KEM-768 for SecureChannel key establishment, ML-DSA for asymmetric
   signatures, HKDF-SHA-256 for key derivation, and AES-256-GCM for
   symmetric message protection.  It defines the profile identifiers,
   nonce encoding, key schedule, authenticated-encryption inputs,
   certificate and public-key binding requirements, token rollover
   behavior, and conformance requirements.

   This Internet-Draft is a proposal for Standards Track publication.
   Permanent OPC UA SecurityPolicy and algorithm identifiers require
   coordination with the OPC Foundation; the private identifiers
   documented here remain provisional.  This document does not assign
   official OPC UA identifiers or claim conformance with an OPC
   Foundation specification.
- **draft-liu-moq-feedback-03** (new-draft, score 0, ignored_after_review) [none]: [MoQ Feedback](https://datatracker.ietf.org/doc/draft-liu-moq-feedback/) — This document defines Media over QUIC Feedback (MQF), an extension to
   Media over QUIC Transport (MOQT) that enables delivery quality
   information about media Objects to be reported using Feedback Tracks.
   It defines how Feedback Tracks are associated with media Tracks,
   established, forwarded through Relays, and consumed, together with
   the MQF report format and capability negotiation.  MQF complements
   transport-layer signals with per-Object delivery information.
- **draft-liu-srv6ops-bfd-srv6-policy-encap-02** (new-draft, score 0, ignored_after_review) [none]: [Operational Guidelines for BFD Monitoring in SRv6 Policies](https://datatracker.ietf.org/doc/draft-liu-srv6ops-bfd-srv6-policy-encap/) — This document provides operational guidelines for Bidirectional
   Forwarding Detection (BFD) when applied to Segment Routing over IPv6
   (SRv6) Policies.  While the packet encapsulation mechanisms are
   standardized, this document focuses on the decisions network
   operators must make regarding mode selection, address management,
   traffic engineering integration, and troubleshooting strategies to
   ensure reliable service protection and efficient resource
   utilization.

   It addresses practical challenges such as handling diverse tail-end
   node capabilities (IPv4/IPv6), managing BFD session overhead in
   large-scale segment lists, and diagnosing failure detection anomalies
   in source-routed paths.
- **draft-loffredo-calext-jscontact-eai-01** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Email Addresses in JSContact](https://datatracker.ietf.org/doc/draft-loffredo-calext-jscontact-eai/) — JSContact defines the EmailAddress object for representing an email
   address, but its address property is restricted to the ASCII syntax
   of an addr-spec in RFC 5322.  This document redefines that property
   to also support internationalized email addresses, as defined in RFC
   6532.  Since such values are incompatible with JSContact version 2.0,
   this document defines JSContact version 3.0.  This document updates
   RFC 9553.
- **draft-lrss-bess-evpn-group-policy-04** (new-draft, score 0, ignored_after_review) [none]: [EVPN Group Policy](https://datatracker.ietf.org/doc/draft-lrss-bess-evpn-group-policy/) — Group Based Policy can be used to achieve micro or macro segmentation
   of user traffic.  For Group Based Policy, a Group Policy ID, also
   known as Group Policy Tag, is used to represent a logical group that
   shares the same policy and access privilege.  This document defines a
   backward compatible extension to Virtual eXtensible Local Area
   Network (VXLAN) that allows a Group Policy ID to be carried for the
   purposes of policy enforcement at the egress Network Virtualization
   Edge (NVE).  It also defines a new BGP Extended Community that can be
   used to propagate Group Policy ID through a BGP route advertisement
   in the control plane.  This is to facilitate policy enforcement at
   the ingress NVE when feasible.
- **draft-many-tiptop-dns-04** (new-draft, score 0, ignored_after_review) [none]: [Deployment and Use of the Domain Name System(DNS) in Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-dns/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  This document lists operational
   methods to enable local DNS name resolving on celestial body networks
   such that there are no real-time query and response flow to name
   servers on (Earth) Internet.
- **draft-many-tiptop-ntp-profile-01** (new-draft, score 0, ignored_after_review) [none]: [NTP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-ntp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an NTP profile
   for deep space.  NTP on-wire protocol is indifferent to path delays
   and transfers time in a single round trip at any distance, but
   diverges if delays in each direction is different.  Some algorithmic
   constants and defaults such as distance threshold, dispersion bounds,
   poll intervals and burst modes, need to be tailored to the deep space
   scenario.  The use of secured NTP is also discussed.
- **draft-mery-nagy-taistamp-01** (new-draft, score 0, ignored_after_review) [none]: [Taistamp: Signed TAI64N Timestamps over HTTP](https://datatracker.ietf.org/doc/draft-mery-nagy-taistamp/) — This memo defines Taistamp, an HTTP-accessible service that returns
   the current time as a TAI64N label, optionally signed with Ed25519.
   The service is reached at the well-known URI /.well-known/taistamp
   and is intended for clients that need an authenticated wall-clock
   reading without running an NTP stack or relying on the client's own
   clock for TLS certificate validation.  The signing scheme uses a
   length-prefixed, domain-separated framing and publishes verification
   keys as DNS TXT records in a DKIM-inspired selector layout.
- **draft-msri-bpm-bmp-convergence-benchmarking-00** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for BGP Monitoring Protocol (BMP) Convergence and Scaling](https://datatracker.ietf.org/doc/draft-msri-bpm-bmp-convergence-benchmarking/) — The BGP Monitoring Protocol (BMP) is widely used by operators to
   stream BGP routing state from routers to monitoring and automation
   systems.  Although BGP convergence has well-established benchmarking
   methodologies, there is no standardized way to measure how quickly
   and how completely a router exports BGP state over BMP, or how the
   BMP export affects the router and the collector.  This document
   defines terminology, a reference test setup, metrics, and test
   procedures to benchmark the BMP convergence of a router (the Device
   Under Test) in a vendor-independent and repeatable way.  It covers
   all five BMP monitoring views (Adj-RIB-In pre-policy and post-policy,
   Loc-RIB, and Adj-RIB-Out pre-policy and post-policy), initial table
   dump speed, convergence during routing events and churn, impact on
   BGP itself, scaling with the number of monitored views, the Adj-RIB-
   Out scale, and BMP stations, and behavior under TCP backpressure.
- **draft-munoz-schc-over-dts-iot-03** (new-draft, score 0, ignored_after_review) [none]: [Static Context Header Compression and Fragmentation ARQ/FEC mode](https://datatracker.ietf.org/doc/draft-munoz-schc-over-dts-iot/) — This document defines a new fragmentation mode for the SCHC standard
   defined in RFC8724.  The new fragmentation mode is designed for
   communications that require additional reliability mechanisms.  The
   reliability is based on a hybrid ARQ/FEC type II mechanism that
   combines forward error correction (FEC) with adaptive retransmissions
   to achieve high reliability.
- **draft-nandakumar-moq-e2e-session-tests-00** (new-draft, score 0, ignored_after_review) [none]: [End-to-End Session Tests for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-nandakumar-moq-e2e-session-tests/) — This document describes a set of end-to-end tests that exercise a
   Media over QUIC Transport (MOQT) relay through real client sessions.
   For each test it gives a short description, the inputs, the message
   flow as a call-flow diagram, and the expected outcome.  The tests
   apply to MOQT draft-18 and later; results for several public relays
   are published in the moq-web interop report.
- **draft-oga-audit-witness-answer-00** (new-draft, score 0, ignored_after_review) [none]: [Witness Answers: Signed Recomputation of a Published Record, Filed Beside It](https://datatracker.ietf.org/doc/draft-oga-audit-witness-answer/) — This document defines a witness answer: a signed statement by a party
   other than the operator that it recomputed a published record from
   public endpoints, naming the digests it obtained, the steps it
   recomputed, and the limits of what it checked.  It defines how the
   answer is filed beside the record it witnesses and anchored in time.
   An informative section describes version 0.1 of the answer, which
   adds a kind for records published by others.  A verified answer does
   not show that the content of the record is right.
- **draft-palet-happy-reporting-considerations-02** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Happy Eyeballs Error Reporting](https://datatracker.ietf.org/doc/draft-palet-happy-reporting-considerations/) — This document introduces different aspects to be considered for the
   Happy Eyeballs error reporting.
- **draft-pjs-6lo-can-01** (new-draft, score 0, ignored_after_review) [none]: [Transmission of IPv6 Packets over Controller Area Network](https://datatracker.ietf.org/doc/draft-pjs-6lo-can/) — Controller Area Network (CAN) is a fieldbus initially designed for
   automotive applications.  It has since been adopted for use in
   various industrial applications, such as CANopen and building
   automation systems.  CAN operates as a multi-master bus with frame
   identifiers of 11 bits or 29 bits.  The CAN standard, defined in the
   ISO 11898 series, specifies both the physical and data-link layers.
   This document describes how to transfer IPv6 packets over CAN using
   ISO-TP, a dedicated addressing scheme for CAN nodes, and Static
   Context Header Compression (SCHC).
- **draft-pmykhailyk-idr-bgp-community-exchange-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Extended Community Exchange](https://datatracker.ietf.org/doc/draft-pmykhailyk-idr-bgp-community-exchange/) — This document specifies a mechanism for transferring a BGP Extended
   Community, in particular the Link Bandwidth Extended Community, from
   one prefix to another, which enables routers to dynamically adjust
   the distribution ratio for weighted load balancing in NAT scenarios,
   allowing a router to perform unequal cost load balancing according
   to the real capacity of compute clusters.
- **draft-portoles-lisp-delegated-mappings-01** (new-draft, score 0, ignored_after_review) [none]: [LISP Delegated Mappings](https://datatracker.ietf.org/doc/draft-portoles-lisp-delegated-mappings/) — The LISP protocol with its inherent decoupling of control-plane and
   data-plane, offers the flexibility to support modern networking
   paradigms.  This document specifies how to use the LISP protocol to
   enable centralized onboarding and management of EIDs within a network
   from an external controller or orchestration system.

Requirements Notation
- **draft-ramanathan-lisp-savi-02** (new-draft, score 0, ignored_after_review) [none]: [SAVI in a LISP network](https://datatracker.ietf.org/doc/draft-ramanathan-lisp-savi/) — This document specifies the procedures for Source Address Validation
   of LISP Endpoint Identifiers (EID).  The implementation of these
   mechanisms provides endpoint detection, on-boarding and roaming
   support in LISP networks, while protecting against IP address
   spoofing.
- **draft-rpc-rfc7322bis-05** (new-draft, score 0, ignored_after_review) [none]: [RFC Style Guide](https://datatracker.ietf.org/doc/draft-rpc-rfc7322bis/) — This document describes the fundamental and unique style conventions
   currently in use for the RFC Series.  It captures the RFC Production
   Center's basic requirements and offers guidance regarding the style
   and structure of an RFC.  Additional guidance is captured on a
   website that reflects the experimental nature of that guidance and
   prepares it for future inclusion in the RFC Style Guide.  This
   document obsoletes RFC 7322, "RFC Style Guide".

   Note: This draft is being developed and discussed in the GitHub repo
   <https://github.com/rfc-editor/draft-rpc-rfc7322bis>, but any
   substantive change should be discussed on <rfc-interest@rfc-
   interest.org>.
- **draft-sajassi-bess-evpn-subnet-slicing-01** (new-draft, score 0, ignored_after_review) [none]: [EVPN Subnet Slicing](https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-subnet-slicing/) — Ethernet VPN (EVPN) Integrated Routing and Bridging (IRB) distributes
   Layer 2 and Layer 3 reachability through BGP.  In a large stretched
   broadcast domain, traditional IRB can cause every Provider Edge (PE)
   to install MAC and IP addresses for every endpoint in the subnet thus
   resulting in exhaustion of forwarding resources (MAC-VRF and IP-VRF)
   on the PEs - i.e., route population is approximately proportional to
   the number of endpoints in every stretched subnet imported by the PE

   [Optimized-IRB] proposes a solution to alleviate the MAC-VRF resource
   consumption by terminating ARP/ND messages on the PE and providing L3
   forwarding (routing) for both intra and inter subnets.  Therefore,
   eliminating the need for MAC lookups and the maintenance of MAC
   addresses in MAC-VRF for IP hosts.  However, this solution does not
   solve the IP-VRF resource consumption issue as IP host addresses
   still need to be maintained in IP-VRF for both the locally connected
   hosts and the remote hosts.

   This problem is particularly pronounced in campus networks where most
   subnets are stretched across the entire campus (and thus all access
   switches) and the access switches used as EVPN-IRB PE devices have
   significantly smaller forwarding tables and hence limit the total
   endpoint scale that can be attached to stretched subnets across the
   network.  This document defines an EVPN Subnet Slicing solution to
   horizontally scale stretched subnets across the network without being
   constrained by any PE's forwarding table size.  The solution enables
   access layer PE devices to maintain only locally attached host routes
   and allows host routes to be distributed across distribution or
   aggregation layer PE devices as opposed to each PE maintaining all
   host IP routes.
- **draft-sakai-hcttp-00** (new-draft, score 0, ignored_after_review) [none]: [Human Conversational Turn-Taking Protocol (HCTTP)](https://datatracker.ietf.org/doc/draft-sakai-hcttp/) — This document specifies the Human Conversational Turn-Taking Protocol
   (HCTTP), an integrated session-layer communication protocol for
   multi-node human spoken interaction.  HCTTP formalizes connection
   establishment (Three-Way Handshake), token arbitration, turn
   transitions, real-time backchannel signaling (ACK/NACK), dynamic rate
   adaptation, conversational padding (filler frames), collision
   recovery, and standardized conversational status codes over shared
   acoustic channels.
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
- **draft-saum-rtgwg-mtu-propagation-evpn-overlays-00** (new-draft, score 0, ignored_after_review) [none]: [MTU propagation over EVPN Overlays](https://datatracker.ietf.org/doc/draft-saum-rtgwg-mtu-propagation-evpn-overlays/) — Path MTU Discovery between end-host-devices/Virtual-Machines/servers/
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
- **draft-schlyter-dnsop-dnssec-jwk-00** (new-draft, score 0, ignored_after_review) [none]: [JSON Web Key (JWK) for DNSSEC](https://datatracker.ietf.org/doc/draft-schlyter-dnsop-dnssec-jwk/) — This document specifies how to represent DNSSEC public and private
   keys as JSON Web Keys (JWK).  The cryptographic key material is
   encoded using the existing JWK key types, and the DNS-specific
   information needed to reconstruct the corresponding DNSKEY resource
   record (owner name, algorithm, protocol and flags) is carried in a
   new JWK parameter, "dnskey".  This gives DNSSEC signers, key
   management systems and other tools a standardized, interoperable
   format for exchanging and storing DNSSEC keys.
- **draft-shyam-vlsmtrp-17** (new-draft, score 0, ignored_after_review) [none]: [VLSM Tree Routing Protocol](https://datatracker.ietf.org/doc/draft-shyam-vlsmtrp/) — This is a light weight routing protocol applicable inside a network
   that appears in the form of a tree and distribution of address space
   takes place with the approach of VLSM. It is based on setting default
   route inside VLSM tree.  With this approach, routing information of
   the external world need not be passed down to the VLSM tree. Thus,
   load inside a router gets reduced substantially.  This document
   includes IP-VPN with MPLS inside VLSM tree by extending RSVP-TE.
- **draft-sidor-pce-multipath-metric-01** (new-draft, score 0, ignored_after_review) [none]: [Signaling Per-Path Metric in the Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-multipath-metric/) — The Path Computation Element Communication Protocol (PCEP) extensions
   for signaling multipath information allow multiple forwarding paths
   to be associated with a single PCEP Label Switched Path (LSP); for
   Segment Routing (SR) Policy, these paths are the Segment Lists of a
   Candidate Path.  However, the METRIC object remains encoded at the
   LSP level, and per-path encoding of the METRIC object is explicitly
   left out of scope.

   This document extends PCEP to signal per-path (for SR Policy, per
   Segment List) metric information by reusing the existing METRIC
   object within the multipath constructs, and defines the associated
   capability negotiation.
- **draft-slutsky-homing-pigeon-v3-00** (new-draft, score 0, ignored_after_review) [none]: [Homing Pigeon Message Protocol, Version 3: DTLS 1.3 via Email](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon-v3/) — This document specifies version 3 of the Homing Pigeon message
   protocol.  Version 3 is a transport extension to version 1, not a
   replacement for it: every version 1 message keeps its meaning, the
   version 1 job acceptance gate is unchanged, and version 3 changes
   exactly one thing -- the carriage of the version 1 DTLS session
   profile.

   Version 1 defines a DTLS 1.3 session profile: one cipher suite, a
   pre-shared key taken from the protocol's shared secret, ephemeral
   Diffie-Hellman on every handshake, and the platform_info disclosure
   carried in the server's EncryptedExtensions.  Version 1 binds that
   profile to a live datagram path.  This document binds the same
   profile to the email binding: handshake flights and protected records
   are carried as email messages over the store-and-forward mailbox, so
   a session can be opened by an email, completed over further emails,
   and then carry jobs and results inside it, with the perfect forward
   secrecy of the version 1 profile intact on a carrier that has no live
   path at all.

   The objects carried inside the session remain version 1 objects: a
   job or a result inside a session is the version 1 object, unchanged,
   carrying the version value version 1 defines.  The 3 of this
   document's title numbers this document and its carriage; it is not a
   value of any object's version field, and nothing in this document
   mints a version 3 object.  HP-DTLS/3, the frame header this document
   defines, is a carriage label whose digit is the carriage generation,
   not a protocol version.

   This document is a local, unsubmitted draft.  It has not been posted
   to the Internet-Drafts directory, and it requests no IANA action.
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
- **draft-smith-idr-rr-deployment-considerations-02** (new-draft, score 0, ignored_after_review) [none]: [BGP RR Deployment Considerations](https://datatracker.ietf.org/doc/draft-smith-idr-rr-deployment-considerations/) — In BGP networks, Route Reflectors (RRs) simplify the provisioning of
   the Internal BGP (IBGP) control plane and mitigate the scaling
   challenges of maintaining a full mesh of IBGP sessions among border
   routers.  Because of these operational benefits, RRs are widely
   deployed in modern networks utilizing BGP.  This document describes
   common RR design options, their associated trade-offs, and deployment
   best practices based on industry operational experience.  Operators
   should consider these suggestions when designing and operating BGP
   networks because BGP control plane stability is essential to overall
   network stability.
- **draft-song-broadband-ancp-tsf-01** (new-draft, score 0, ignored_after_review) [none]: [TSF Extensions to ANCP in CU Separation Broadband Networks](https://datatracker.ietf.org/doc/draft-song-broadband-ancp-tsf/) — This document specifies a Traffic Steering Function (TSF) capability
   extension to the Access Node Control Protocol (ANCP), to discover and
   manage disaggregated user-plane (UP) functions in control/user plane
   separated networks, including the Access Network User Plane (AN-UP)
   and the Network Access Server User Plane (NAS-UP).
- **draft-song-lamps-cms-composite-frodokem-02** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-song-lamps-cms-composite-frodokem/) — This document specifies the conventions for using Composite FrodoKEM
   algorithms with the Cryptographic Message Syntax (CMS).  Composite
   FrodoKEM combines FrodoKEM with traditional algorithms (RSA-OAEP,
   X25519, X448) to provide hybrid post-quantum key encapsulation.
- **draft-song-lamps-pq-composite-frodokem-02** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   X25519, and X448.  This document specifies the algorithm definitions,
   key formats, and certificate conventions for using Composite FrodoKEM
   in the X.509 Public Key Infrastructure.
- **draft-spk-httpbis-parallel-upload-01** (new-draft, score 0, ignored_after_review) [none]: [Parallel Appends for Resumable Uploads](https://datatracker.ietf.org/doc/draft-spk-httpbis-parallel-upload/) — The resumable upload protocol lets a client continue an interrupted
   upload, but the upload has to be sent in order, one request at a
   time.  This document extends that protocol so that a client can send
   different parts of the same upload in parallel.  Servers and
   intermediaries can limit both the number of concurrent requests and
   the amount of data that arrives out of order.  The document also
   describes how intermediaries that inspect uploads (for data loss
   prevention or malware scanning, say) can continue to do so, and how
   the extension behaves over HTTP/1.1, HTTP/2, and HTTP/3.
- **draft-sporeba-tsvwg-mobile-l4s-01** (new-draft, score 0, ignored_after_review) [none]: [Best Practices for L4S Implementation for Mobile Devices](https://datatracker.ietf.org/doc/draft-sporeba-tsvwg-mobile-l4s/) — This document describes best practices for deployment of Low Latency,
   Low Loss, and Scalable Throughput (L4S) in mobile devices.  It
   defines the responsibilities of the host operating system and the
   link-layer (modem and Wi-Fi) subsystems to ensure successful end-to-
   end low-latency communication.
- **draft-ugur-moq-fast-switching-01** (new-draft, score 0, ignored_after_review) [none]: [Subscriber-Side Multi-Variant Fast Track Switching for MOQT](https://datatracker.ietf.org/doc/draft-ugur-moq-fast-switching/) — This document describes subscriber-side multi-variant fast track
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
- **draft-wang-topology-aware-collective-communication-01** (new-draft, score 0, ignored_after_review) [none]: [Topology-Aware Construction of Collective Communication over Time-Expanded Networks](https://datatracker.ietf.org/doc/draft-wang-topology-aware-collective-communication/) — This document describes a topology-aware method for constructing
   collective communication schedules in distributed systems.  Instead
   of selecting from a small set of predefined communication algorithms,
   the method expands a target network topology along a time dimension,
   tracks per-node data state, and incrementally builds a schedule
   through candidate-source discovery and link-to-chunk matching.  The
   approach is intended for heterogeneous or asymmetric topologies in
   which fixed communication patterns often underutilize available links
   or create avoidable bottlenecks.  According to the source material,
   the resulting schedule is intended for collective communication tasks
   involving data distribution, aggregation, reduction, and
   synchronization, including all-gather, reduce-scatter, and all-
   reduce.
- **draft-watts-eqr-conformance-06** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Conformance Profile and Test Vectors for Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-eqr-conformance/) — This document defines a deterministic conformance profile and test-
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
- **draft-watts-hagth-framework-02** (new-draft, score 0, ignored_after_review) [none]: [Human-Accelerated Geophysical Threshold Framework](https://datatracker.ietf.org/doc/draft-watts-hagth-framework/) — This document defines an informational research framework for
   describing anthropogenic perturbations that alter the timing,
   probability, coupling, or consequence of threshold transitions in
   geophysical systems without requiring anthropogenic dominance of the
   system's primary energy source.
- **draft-watts-octatouch-smoke-test-profile-02** (new-draft, score 0, ignored_after_review) [none]: [OctaTouch Gesture Runtime: Smoke-Test Behavior Profile](https://datatracker.ietf.org/doc/draft-watts-octatouch-smoke-test-profile/) — This document records five expected behaviors asserted by a supplied
   OctaTouch gesture-runtime smoke-test script.  It is a limited test
   profile, not a complete gesture specification.  The runtime
   implementation and its dependencies were not included with the source
   script, so the tests have not been executed as part of this archive.
   No interoperability or implementation-conformance claim is made.
- **draft-watts-scientific-admissibility-02** (new-draft, score 0, ignored_after_review) [none]: [Scientific Admissibility Evidence Records: A Research Data Exchange Proposal](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility/) — This document proposes interoperable evidence record fields for
   reproducible research workflows.  It is an independent working draft
   and is not an IETF publication or standard.
- **draft-watts-scientific-quantity-verification-00** (new-draft, score 0, ignored_after_review) [none]: [Scientific Quantity Records with Digest-Bound Numeric Verification](https://datatracker.ietf.org/doc/draft-watts-scientific-quantity-verification/) — This document defines a JSON representation for scientific quantities
   (a decimal value, a unit, and an optional measurement uncertainty)
   and a binding by which a computed quantity names, by cryptographic
   digest, the exact input quantities, operation and arithmetic rules it
   was derived with.  It also defines a fail-closed procedure by which a
   verifier recomputes the value, checks the unit relationship and, for
   one named method, recomputes the uncertainty, and reports a separate
   verdict for each aspect.  A passing result means only that the stated
   numbers follow from the stated inputs under the stated rules.  It
   does not establish that a measurement was valid, that the inputs are
   true, or that any scientific conclusion follows.
- **draft-wkumari-intarea-safe-limited-domains-08** (new-draft, score 0, ignored_after_review) [none]: [Fail-closed Limited Domains](https://datatracker.ietf.org/doc/draft-wkumari-intarea-safe-limited-domains/) — Documents describing protocols intended solely for use within
   "limited domains" often rely on edge filtering at every boundary node
   to prevent domain-internal traffic from leaking to the global
   Internet (and vice versa).  While edge filtering is a critical and
   standard operational practice, relying solely on administrative
   policies can create "fail-open" designs if configuration errors, ACL
   bypass, or hardware table limitations occur.

   This document describes design principles and concrete mechanisms
   that allow limited-domain protocols to "fail-closed" by default.  By
   leveraging Layer-2 encapsulation identifiers (such as dedicated or
   extended EtherTypes), local address scoping, and / or Hop-Limit
   boundaries, protocol designers can provide robust defense-in-depth
   and significantly reduce the operational and security risks
   associated with limited-domain protocol leakage.

   These mechanisms are not applicable to all protocols intended for use
   in a limited domain, but if implemented on certain classes of
   protocols, can significantly reduce the risks.
- **draft-xiao-v6ops-eds-03** (new-draft, score 0, ignored_after_review) [none]: [Enhanced Dual Stack: Connection-Informed IPv6/IPv4 Selection](https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/) — This document describes Enhanced Dual Stack (EDS), a framework
   intended to reduce the operational risk and upfront workload of
   introducing IPv6 into existing IPv4 networks.  EDS provides a
   connection-informed method for implementing RFC 6724 Rule 1, "Avoid
   unusable destinations", by remembering recent TCP/QUIC connection-
   establishment failures and avoiding repeated selection of affected
   IPv6 destinations.  It also provides operational diagnostics so
   administrators can identify and correct IPv6 problems.  EDS is
   complementary to Happy Eyeballs and does not require connection
   racing.  By starting with selected EDS-capable pioneer hosts,
   performing practical validation, and expanding IPv6 gradually, EDS
   can be deployed incrementally without requiring all hosts to support
   EDS.  With EDS, enterprises' IPv6 introduction can change from a
   heavy upfront validation process toward an incremental improvement
   process.
- **draft-yang-pce-pcep-over-quic-08** (new-draft, score 0, ignored_after_review) [none]: [PCEP over QUIC](https://datatracker.ietf.org/doc/draft-yang-pce-pcep-over-quic/) — This document specifies the use of QUIC streams to implement the PCEP
   protocol for efficient and secure data transmission.
- **draft-ye-srv6ops-sfc-deployment-03** (new-draft, score 0, ignored_after_review) [none]: [SRv6 SFC Deployment Options](https://datatracker.ietf.org/doc/draft-ye-srv6ops-sfc-deployment/) — This document outlines the critical factors for deploying Service
   Function Chaining (SFC) using Segment Routing over IPv6 (SRv6).  It
   addresses deployment architectures, including both SRv6-aware and
   SRv6-unaware scenarios, and details the end-to-end provisioning
   lifecycle.  Furthermore, it proposes reliability mechanisms and
   provides strategic recommendations for network operators
   transitioning from legacy NSH-based SFC to a modern, scalable SRv6
   framework.
- **draft-yuyou-moq-v3c-01** (new-draft, score 0, ignored_after_review) [none]: [Transport of V3C Bitstreams over Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-yuyou-moq-v3c/) — This document specifies a mapping and packaging for transporting ISO/
   IEC 23090-5 Visual Volumetric Video-based Coding (V3C) bitstreams
   over Media over QUIC Transport (MOQT).  The mapping uses the MOQT
   Streaming Format (MSF): V3C configuration is MSF initialization data,
   each independently consumable V3C component is an MSF track, a run of
   V3C composition units that starts at a random access point is a MOQT
   Group, and the coded data of one component for one composition unit
   is a MOQT Object.  Relays remain unaware of V3C syntax.  V3C
   knowledge is confined to the streaming-format layer.
- **draft-zhang-dnsop-tld-transition-01** (new-draft, score 0, ignored_after_review) [none]: [Top Level Domain Transition Operational Practices](https://datatracker.ietf.org/doc/draft-zhang-dnsop-tld-transition/) — This document describes the process for Top-Level Domain(TLD)
   registries to switch their Registry Service Provider (RSP),
   including migration requirements, data changes, and operational
   procedures.

   This document applies to scenarios where the name service of
   certain TLD is migrated between different RSPs, and the TLD has
   implemented DNSSEC.
- **draft-zhangb-cats-service-metrics-op-07** (new-draft, score 0, ignored_after_review) [none]: [Computing Service Metric Definitions and Operation under CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-service-metrics-op/) — Computing-Aware Traffic Steering (CATS) optimizes traffic forwarding
   by considering both computing and networking metrics.  The CATS
   Metrics framework provides a general metric hierarchy and operational
   guidance for aggregation and normalization.  Some deployment
   scenarios additionally require service-oriented metrics with explicit
   semantics and units to be consumed directly for service-instance
   selection based on both computing and network conditions.

   This document defines an operational approach that does not rely on
   the Level 1 or Level 2 normalized scores of the CATS Metrics
   framework.  Instead, service sites report service-oriented metrics
   with explicit semantics and units, such as Global Available Slots and
   Computing Time, which are directly consumed by the C-PS for service-
   instance selection based on both computing and network conditions.
   The document clarifies how these metrics are derived from basic
   resource information, service reference information, and local
   policy.  It also specifies how the C-PS combines the Computing
   Service Table with the Network Service Table, and defines update-
   control and fallback mechanisms suitable for large-scale deployments.

   Within the unified CATS architecture, this service-oriented
   operational approach complements the normalized-score approach.  The
   two targeted scenarios are rapid deployment without offline metric-
   function negotiation and fine-grained, requirement-aware joint
   selection.
- **draft-zheng-quic-fec-extension-04** (new-draft, score 0, ignored_after_review) [none]: [FEC Extension for QUIC](https://datatracker.ietf.org/doc/draft-zheng-quic-fec-extension/) — This document specifies a Forward Error Correction (FEC) extension
   for the QUIC protocol, which provide protection against packet loss.

## Errors / fetch failures

- draft-faltstrom-unicode: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-faltstrom-unicode/doc.json
