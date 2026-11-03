# IETF Identity + AI Standards Watch

Date: 2026-11-03

## Read now

- **draft-durga-wimse-ctx-isolation-00** (new-draft, score 36, authorization) [none]: [Cryptographic Separation of Untrusted Data-Plane Context from Control-Plane Tool Invocations in Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-wimse-ctx-isolation/) — Autonomous AI agents operating over Model Context Protocol (MCP) and
   Agent-to-Agent (A2A) transports routinely ingest untrusted external
   data (emails, web documents, retrieved RAG chunks) into the same
   inference context that authorizes privileged control-plane tool
   calls.  Existing workload identity and token standards (OAuth 2.1,
   GNAP, WIMSE Wit/Wpt tokens) bind client identity and authorization
   scope, but fail to cryptographically bind the provenance taint of the
   data-plane context that induced the tool invocation, leaving systems
   vulnerable to indirect prompt-injection confused-deputy attacks.
   This document specifies a deterministic COSE_Sign1 and JSON
   Canonicalization Scheme (JCS, RFC 8785) wire profile that attaches a
   cryptographic Context Taint Attestation (CTA) header to every
   control-plane tool invocation, forcing relying parties to fail closed
   when an untrusted or mixed data-plane context attempts to trigger a
   state-mutating action without an independent out-of-band human or
   policy approval receipt.
- **draft-carleton-workload-authz-grant-02** (new-draft, score 28, core_identity) [none]: [Workload Authorization Grant](https://datatracker.ietf.org/doc/draft-carleton-workload-authz-grant/) — This document defines the Workload Authorization Grant (WAG), by
   which a workload hosted on a platform -- an AI agent is the
   motivating case -- obtains access tokens from a third party's OAuth
   authorization server without requiring an administrator to perform a
   per-workload provisioning step.  Each workload is identified by an
   opaque identifier that is never reassigned.  A Workload Identity
   Provider operated by the platform signs a JWT authorization grant
   ([RFC7523]) that names one workload, and the workload presents it at
   the token endpoint of an authorization server that has been
   configured, once, to trust that Workload Identity Provider.  The
   authorization server does not reject a workload because it has not
   seen it before.  The workload's access is determined by the
   authorization server's own policy, which may consult claims the
   Workload Identity Provider asserts about the workload.  This document
   covers workloads acting on their own behalf.  Access on behalf of a
   user or other principal is out of scope, though the grant is intended
   to compose with delegation mechanisms in which the workload is the
   actor.
- **draft-nandakumar-agent-sd-card-00** (new-draft, score 28, verifiable_claims) [none]: [Agent SD-Card: Selective Disclosure of Agent Metadata for Discovery and Authentication](https://datatracker.ietf.org/doc/draft-nandakumar-agent-sd-card/) — This document defines SD-Card, an SD-JWT encoding of AI agent
   metadata that lets an agent reveal to each verifier only the
   capabilities, endpoints, and security requirements it is authorized
   to see, while the verifier can check that they are authentic and
   issuer-attested.  SD-Card keeps agent metadata confidential; it does
   not make agents anonymous.  The document specifies the SD-Card data
   model, issuance, discovery, and key-bound presentation, and defines
   bindings for the Model Context Protocol (MCP), the Personal Agent
   Protocol (PAP), and the Agent2Agent (A2A) protocol.
- **draft-watts-agent-authority-transition-receipts-01** (new-draft, score 28, authorization) [none]: [Agent Authority Transition Receipts for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-authority-transition-receipts/) — Autonomous agents increasingly act across administrative and security
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
- **draft-durga-pquip-pqc-agentic-delegation-00** (new-draft, score 26, agent_identity) [none]: [Post-Quantum Hybrid Cryptographic Delegation Chains and Merkle-Aggregated Execution Receipts for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-pquip-pqc-agentic-delegation/) — Autonomous AI agent ecosystems rely on multi-hop cryptographic
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
   based SLH-DSA-SHAKE-128f (FIPS 205) over RFC 9943 SCITT transparency
   Merkle roots, guaranteeing 30-year quantum-resistant non-repudiation
   even under catastrophic lattice cryptanalysis.
- **draft-elekula-seat-attested-tls-testing-00** (new-draft, score 26, core_identity) [none]: [Interoperability, Security Evaluation, and Negative Testing for Attested TLS 1.3 and DTLS 1.3](https://datatracker.ietf.org/doc/draft-elekula-seat-attested-tls-testing/) — This document defines a framework for reproducible interoperability
   and security evaluation of implementations that integrate remote
   attestation with TLS 1.3 and DTLS 1.3. It complements protocol and
   architecture specifications by defining test profiles, a common
   result model, cross-implementation procedures, negative tests, and
   measurements at the boundary between transport authentication,
   attestation appraisal, authorization, and application-data release.

   In addition to per-connection attestation, the framework evaluates
   reusable Attestation Results and cross-connection trust-continuity
   mechanisms, including deployments in which an attestation endpoint
   and application-serving endpoint are distinct. It addresses key
   custody and derivation, target and workload identity, state drift,
   credential lifecycle, multi-relying-party isolation, proxy topology,
   session resumption, early data, privacy, and failure containment.

   This document does not define a new attestation architecture,
   Evidence format, TLS or DTLS extension, cryptographic key schedule,
   or remote-attestation protocol. It specifies an evaluation framework
   for comparing implementations and identifying interoperability and
   security gaps in declared profiles.
- **draft-ietf-wimse-aims-01** (new-draft, score 25, core_identity) [wimse]: [AI Identity Management System](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/) — This document proposes best practices for authentication and
   authorization of AI agent interactions.  It leverages existing
   standards such as the Workload Identity in Multi-System Environments
   (WIMSE) architecture and OAuth 2.0 family of specifications.  Rather
   than defining new protocols, this document describes how existing and
   widely deployed standards can be applied or extended to establish
   agent authentication and authorization.  By doing so, it aims to
   provide a framework within which to use existing standards, identify
   gaps and guide future standardization efforts for agent
   authentication and authorization.
- **draft-durga-scitt-model-activation-binding-00** (new-draft, score 24, trust_infrastructure) [none]: [Merkle-Anchored Model Weight Release and RATS-Attested Runtime Activation Binding for Edge and Cloud AI Fleets](https://datatracker.ietf.org/doc/draft-durga-scitt-model-activation-binding/) — Supply Chain Integrity, Transparency, and Trust (SCITT) provides
   transparent artifact statements, and Remote Attestation Procedures
   (RATS, RFC 9334) provide hardware/runtime attestation evidence.
   However, no existing internet standard defines an atomic
   cryptographic binding between a chunked AI model weight release
   manifest, a hardware-monotonic anti-rollback epoch counter, and a
   live RATS attestation result at the moment model weights are mapped
   into accelerator memory.  This document specifies the Model
   Activation Binding Token (MABT) protocol, preventing load-time weight
   substitution, silent quantization downgrade, and rollback attacks
   across cloud and edge AI inference fleets.
- **draft-hood-agtp-log-03** (new-draft, score 24, adjacent_watchlist) [none]: [AGTP Transparency Log Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-log/) — This document specifies the AGTP Transparency Log (AGTP-LOG): the
   append-only audit log protocol that underpins the log-anchored Trust
   Tier 1 verification path defined in [AGTP] and provides the post-hoc
   audit infrastructure for AGTP-based agent operations.  AGTP-LOG
   aligns with [RFC9162] (Certificate Transparency 2.0) as the
   verifiable data structure and issues COSE_Sign1 receipts per
   [RFC9943] (SCITT) for cross-ecosystem interoperability.  This
   document restates the AGTP Agent Identity Taxonomy (Agent Genesis,
   Canonical Agent-ID, Agent Certificate) as [AGTP] adopts it.  The log
   protocol defined here covers entry submission, receipt retrieval,
   inclusion-proof retrieval, consistency-proof retrieval, and discovery
   via the log_uri field of the Agent Genesis.  This revision adds the
   statement types by which Attribution-Record Audit-IDs and per-agent
   chain heads are committed to the log, which is the mechanism
   [AGTP-IDENTIFIERS] names for making a self-held attribution chain
   tamper-evident to a verifier that distrusts the holder.  Per-platform
   logs are the default; the federation model follows the SCITT cross-
   witnessing pattern.  Witness and monitor role definitions, full
   federation procedures, and the formal entry-acceptance threat model
   are deferred to a future revision.

   The audit properties AGTP-LOG provides are structural.  Statements
   are signed by the governance platform that operates the log, never by
   the agent the statements concern; an agent cannot forge its own audit
   trail because the log operator's signing key is outside its control.
   This architectural separation distinguishes AGTP-LOG audit
   infrastructure from approaches that layer audit data models onto
   general-purpose substrates where the audited party participates in
   writing the audit trail.
- **draft-thaha-scitt-agent-execution-evidence-02** (new-draft, score 24, core_identity) [none]: [Agent Execution Evidence: A SCITT Profile for Verifiable Records of AI Agent Runs](https://datatracker.ietf.org/doc/draft-thaha-scitt-agent-execution-evidence/) — AI agents act through calls to models, tools and other agents.
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
- **draft-watts-high-assurance-agent-control-envelope-01** (new-draft, score 24, authorization) [none]: [High-Assurance Agent Control Envelope](https://datatracker.ietf.org/doc/draft-watts-high-assurance-agent-control-envelope/) — Agentic systems can authenticate successfully, hold a valid
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
- **draft-wilder-scitt-physical-site-engage-receipt-06** (new-draft, score 24, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
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
- **draft-ietf-oauth-spiffe-client-auth-03** (new-draft, score 23, core_identity) [oauth]: [OAuth SPIFFE Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth/) — This specification profiles the Assertion Framework for OAuth 2.0
   Client Authentication and Authorization Grants [RFC7521], the JWT
   Profile for OAuth 2.0 Client Authentication and Authorization Grants
   [RFC7523], and OAuth 2.0 Attestation-Based Client Authentication
   [I-D.draft-ietf-oauth-attestation-based-client-auth] to enable the
   use of SPIFFE Verifiable Identity Documents (SVIDs) as client
   credentials in OAuth 2.0.  It defines how OAuth clients with SPIFFE
   credentials can authenticate to OAuth authorization servers using
   their JWT-SVIDs, WIT-SVIDs, or X509-SVIDs without the need for client
   secrets.  This approach enhances security by enabling seamless
   integration between SPIFFE-enabled workloads and OAuth authorization
   servers while eliminating the need to distribute and manage shared
   secrets such as static client secrets.
- **draft-lkspa-rats-verifiable-geo-fence-04** (new-draft, score 23, trust_infrastructure) [none]: [Verifiable Proof of Environment Attestation Profile](https://datatracker.ietf.org/doc/draft-lkspa-rats-verifiable-geo-fence/) — Operators of regulated, sovereign, and high-assurance deployments
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
   Evidence in a single TPM-sealed Evidence structure (lah-bundle).
   V-PEA does not generate location Claims: they are produced by
   location sources, such as GNSS receivers, mobile network operators,
   or timing-based anchors, and V-PEA binds them to the particular
   platform that will receive a credential or key.  V-PEA defines two
   Evidence dimensions: *WHAT* — hardware provenance (TPM Attestation
   Key registered and manufacturer-endorsed), platform integrity
   (firmware and OS state matching reference values), and workload agent
   software integrity (binary digest matching an approved value); and
   *WHERE* — physical residency within an approved geographic boundary,
   as reported by one or more location sources.  A TPM quote seal binds
   WHAT and WHERE into a single unforgeable statement: neither dimension
   can be forged or transplanted without invalidating the other.

   For the WHERE dimension, V-PEA supports Transparent Zero-Knowledge
   Proofs (ZKPs), enabling an Attester to prove geographic compliance
   without disclosing precise coordinates.  A positive V-PEA Attestation
   Result enables a Relying Party to issue hardware-rooted credentials
   or authorize operations — combining verified execution environment
   (WHAT) with verified physical placement (WHERE) — before releasing
   sensitive assets or granting access.  Integration with workload
   identity systems is described in the WIMSE Integration appendix.
- **draft-sweeney-wimse-credential-delegation-02** (new-draft, score 23, core_identity) [none]: [Credential Delegation Protocol for AI Agents in Multi-System Environments](https://datatracker.ietf.org/doc/draft-sweeney-wimse-credential-delegation/) — Autonomous AI agents increasingly require access to protected
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
- **draft-asor-wimse-agent-delegation-chain-03** (new-draft, score 22, authorization) [none]: [Verifiable Attenuated Delegation for AI Agent Chains](https://datatracker.ietf.org/doc/draft-asor-wimse-agent-delegation-chain/) — AI agents increasingly delegate tasks to other agents.  Each
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
- **draft-martinez-itp-agent-mandates-00** (new-draft, score 22, authorization) [none]: [Invoice Trust Protocol (ITP): Agent Mandates](https://datatracker.ietf.org/doc/draft-martinez-itp-agent-mandates/) — This document lets a business authorize a software agent to issue,
   accept, reject, or dispute invoices, and to report payments, through
   the Invoice Trust Protocol (ITP), within limits that the business
   sets.  An authorization is a mandate: a Selective Disclosure JSON Web
   Token (SD-JWT) credential issued by the business to a key held by the
   agent and enforced by a named ITP node that records each use.
- **draft-hulea-wimse-agent-mandate-01** (new-draft, score 21, authorization) [none]: [Verifiable Mandates for Agents Acting Across Administrative Domains](https://datatracker.ietf.org/doc/draft-hulea-wimse-agent-mandate/) — This document defines how a relying party in one administrative
   domain validates the mandate under which a software agent, including
   an AI agent, acts for a principal in another domain.  Its distinctive
   element is evidence of the delegator's authority: a statement from an
   authority source about which permissions the person or entity
   granting the mandate may delegate to agents, kept separate from the
   statement that the mandate was granted.  The document specifies the
   mandate format with precisely defined limit semantics, a
   deterministic validation procedure driven by an explicit validation
   profile and kept separate from the relying party's authorization
   decision, the attribution of every validated claim to the issuer and
   role that asserted it, rules for enforcing the mandate after token
   exchange, and the boundary between this protocol and a trust
   framework.  It reuses JSON Web Tokens, OAuth 2.0 Token Exchange, Rich
   Authorization Requests, WIMSE workload credentials and HTTP Message
   Signatures, Token Status Lists, and Entity Attestation Tokens.
- **draft-ietf-spice-sd-cwt-09** (new-draft, score 21, verifiable_claims) [spice]: [Selective Disclosure CBOR Web Tokens (SD-CWT)](https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/) — This specification describes a data minimization technique for use
   with CBOR Web Tokens (CWTs).  The approach is inspired by the
   Selective Disclosure JSON Web Token (SD-JWT), with changes to align
   with CBOR Object Signing and Encryption (COSE) and CWTs.
- **draft-lemonnier-scitt-decision-provenance-01** (new-draft, score 21, trust_infrastructure) [none]: [Decision Provenance for SCITT: binding software releases and agent actions to the decisions behind them](https://datatracker.ietf.org/doc/draft-lemonnier-scitt-decision-provenance/) — Build attestations, bills of materials and Signed Statements in a
   Transparency Service record what was built and by whom.
   Authorization receipts for agent actions can establish who approved
   an exact action; the statement profiles for agent actions record a
   human approval as the producer's claim.  None of them carries the
   decision behind the action, the options considered, the reasons, the
   authority, and what the approver was shown, as a record a verifier
   can check.  This document describes how a decision record and its
   action-binding attachment, as the extension proposals of the Decision
   Provenance Standard define them, sit under a release statement, a
   build attestation or an agent action record by typed digest
   references; how a verifier checks them offline, including the
   approver's signature where one is carried; and how the witness
   checkpoints of the anchoring extension are registered in a
   Transparency Service.  Nothing in the SCITT architecture, in Signed
   Statements or in Receipts changes.  A software release decision and
   an agent action capsule are the worked examples; the model has no
   feature specific to either.  This document is independent of the
   Decision Provenance Standard, is not part of it, does not change it,
   and is not endorsed by its Steward.
- **draft-bailey-scitt-agent-session-receipt-00** (new-draft, score 20, trust_infrastructure) [none]: [Causal Provenance Receipts for Agent Sessions: A SCITT Profile](https://datatracker.ietf.org/doc/draft-bailey-scitt-agent-session-receipt/) — This document defines a Supply Chain Integrity, Transparency, and
   Trust (SCITT) payload profile for agent session provenance: signed
   records that bind an autonomous agent session's lifecycle (start,
   governed tool dispatch, state transitions, termination, and
   settlement) to offline-verifiable cryptographic evidence, with an
   explicit head commitment that detects local hash-chain truncation and
   whole-store rollback.  It reuses the SCITT architecture and COSE
   receipt envelope: the Causal Provenance Receipt (CPR) bundle is the
   signed statement payload, and registration with a Transparency
   Service is optional and explicitly disclosed.  This profile addresses
   the session-lifecycle and resumption-evidence grain rather than
   isolated per-action telemetry, while preserving bounded verifier
   semantics: a verifier checks cryptographic signatures, canonical
   digests, chain links, and external anchors; it does not prove that
   unallegeable physical events occurred.
- **draft-mih-sato-agent-accountability-composition-02** (new-draft, score 20, trust_infrastructure) [none]: [Agent Accountability: Composition and Conformance](https://datatracker.ietf.org/doc/draft-mih-sato-agent-accountability-composition/) — Autonomous and semi-autonomous software agents increasingly take
   consequential actions across administrative and trust domains.
   Holding such an action accountable — to a regulator, auditor, or
   counterparty who does not trust the operator — requires answering
   several questions, each answerable by an independently-verifiable
   profile: whether the agent was permitted to act (CAN), which
   accountable human authorized the specific action (WHO), what outcome
   the agent system recorded and what is known to have crossed the
   effect boundary (WHAT), and whether the runtime enforced correctly
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
- **draft-liu-agent-action-confirmation-00** (new-draft, score 19, authorization) [none]: [Agent Action Confirmation Protocol (AACP)](https://datatracker.ietf.org/doc/draft-liu-agent-action-confirmation/) — AI agents invoke operations with side effects: writes to resources,
   creation of durable records, financial transactions, and delegated
   actions on remote systems.  Existing requirement documents in the
   agentproto working group establish that such operations require
   confirmation by the human user, that this confirmation must occur
   outside of LLM prompt inference, and that in multi-agent delegation
   the receiving agent must be able to verify that a presented
   confirmation actually originated from the user and is not fabricated
   by an intermediate agent.  No document in the current document set
   defines a protocol, message format, or evidence format that satisfies
   these requirements.  This document defines the Agent Action
   Confirmation Protocol (AACP): an action descriptor format derived
   from OAuth 2.0 Rich Authorization Requests (RFC 9396), a confirmation
   request format, a signed confirmation evidence format, and verifier-
   side processing rules with a distinct-outcome failure model.  The
   design is transport-neutral and profiled here for JSON over HTTP with
   JWS signatures; a CBOR/COSE mapping is defined.  A requirement
   traceability matrix maps each mechanism to its source requirement in
   the agentproto document set.

   This document is informed by, and positions itself relative to, two
   prior individual submissions that addressed user confirmation of
   agent actions and have since expired: CHEQ
   [I-D.rosenberg-aiproto-cheq] and the Agent Operation Authorization
   framework [I-D.liu-agent-operation-authorization].  The differences
   are summarized in Section 1.4.
- **draft-mcguinness-oauth-client-attesters-01** (new-draft, score 19, authorization) [none]: [OAuth 2.0 Client Attester Endorsement](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-attesters/) — OAuth 2.0 Attestation-Based Client Authentication requires an
   authorization server to trust the attester that makes statements
   about a client instance, but does not define how a client identifies
   the attesters authorized to attest for it.  This specification
   defines a client metadata parameter, usable by registered clients and
   in Client ID Metadata Documents, that names the endorsed attesters
   and the locations of their verification keys.  It defines how an
   authorization server validates endorsements and processes their
   withdrawal while retaining control over whether to trust them.  It
   introduces no new credential or client authentication method.
- **draft-reddy-wimse-oauth-dialog-binding-00** (new-draft, score 19, core_identity) [none]: [Binding Agent Dialogs to WIMSE and OAuth Credentials](https://datatracker.ietf.org/doc/draft-reddy-wimse-oauth-dialog-binding/) — AI agents and tools that take part in a dialog carry a dialog context
   with each request and response.  This document specifies how the
   dialog context is bound to WIMSE and OAuth credentials.  It extends
   the WIMSE profile of HTTP Message Signatures, for requests and
   responses, and the WIMSE Proof Token, for requests, to cover the
   dialog context, records the dialog identifier in OAuth transaction
   tokens, and describes how a new dialog at a trust boundary aligns
   with OAuth identity chaining.  A receiver can then verify who sent a
   request or response, which dialog it belongs to, and, for a request,
   what it may do, and that the answers agree.
- **draft-watts-ai-identity-01** (new-draft, score 19, trust_infrastructure) [none]: [AID-1: A Cryptographically Bindable Identity and Provenance Architecture for AI Systems](https://datatracker.ietf.org/doc/draft-watts-ai-identity/) — This document specifies AID-1, a provider-independent architecture
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
- **draft-durga-agenttrust-trace-verification-00** (new-draft, score 18, trust_infrastructure) [none]: [Cryptographic Execution-Trace Verification, JCS Canonicalization, and Fail-Closed Delegation Attestation for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-agenttrust-trace-verification/) — This document specifies a deterministic cryptographic verification
   profile for execution traces, delegation chains, and weight-custody
   manifests generated by autonomous artificial intelligence (AI) agents
   operating across Model Context Protocol (MCP), Agent-to-Agent (A2A),
   and enterprise system-of-record boundaries.  The profile binds JSON
   Canonicalization Scheme (JCS, RFC 8785) pre-image serialization,
   Ed25519 (RFC 8032) and ECDSA P-256/P-384 signatures, JSON Web Key
   (JWK, RFC 7517) thumbprint pinning, and fail-closed revocation and
   freshness checks so that relying parties can independently verify
   whether an agent action was authorized prior to commit.
- **draft-hood-agtp-lei-01** (new-draft, score 18, core_identity) [none]: [AGTP Binding to the Legal Entity Identifier (LEI and vLEI)](https://datatracker.ietf.org/doc/draft-hood-agtp-lei/) — The Legal Entity Identifier (LEI), defined by ISO 17442 and operated
   under the global governance of the Global Legal Entity Identifier
   Foundation (GLEIF), is the internationally recognized identifier for
   legal entities in financial transactions and regulatory reporting.
   The verifiable LEI (vLEI), built on Key Event Receipt Infrastructure
   (KERI) and Authentic Chained Data Containers (ACDC), extends the LEI
   into the digital trust ecosystem with cryptographically verifiable
   credentials issued through Qualified vLEI Issuers (QVIs).

   This document specifies how the Agent Transfer Protocol (AGTP) binds
   to the LEI and vLEI infrastructure.  It defines how an LEI is carried
   as the owner of an agent in its Agent Genesis and Identity Document,
   how a vLEI Legal Entity credential composes with AGTP-CERT to
   establish institutional identity at the wire, how a new verification
   path (vlei-anchored) is added to AGTP-TRUST for KERI-based
   verification, and how vLEI Role Credentials (OOR, ECR, AUTH) express
   the human authorization chain that produced an agent.

   The four layers compose: AGTP provides the agent identity substrate,
   the LEI provides the institutional identity, the vLEI provides
   cryptographic verification of that institutional identity, and the
   vLEI Role Credentials provide the authorization chain from the legal
   entity through human officers to the agent.  This document positions
   financial institutions, regulated entities, and other LEI holders to
   deploy agents with verifiable institutional identity from day one.
- **draft-hood-independent-agtp-10** (new-draft, score 18, core_identity) [none]: [Agent Transfer Protocol (AGTP)](https://datatracker.ietf.org/doc/draft-hood-independent-agtp/) — This document defines the Agent Transfer Protocol (AGTP): a transfer
   protocol for AI agent traffic.  AGTP carries agent identity,
   authority, delegation, and attribution as protocol elements of every
   exchange, on an eighteen-method floor of intent-named methods, over
   TCP/TLS or QUIC on IANA-assigned port 4480 and the IANA-registered
   agtp:// URI scheme.  The method vocabulary beyond the floor, the path
   grammar, and the endpoint contract are specified in [AGTP-METHODS];
   runtime negotiation of endpoints is specified in [AGTP-RCNS]; the
   agent identity document in [AGTP-IDDOC]; transport bindings in
   [AGTP-BINDINGS].  Version 10 adds per-request proof of possession, so
   that a verified identity document and a live sender are bound by
   signature; specifies the Delegation-Chain header with pre-
   authorization semantics (per-hop scope attenuation checked at mint
   and at verify, parent re-verification at each hop, depth and cycle
   limits, and defined failure behavior); maps the delegation model onto
   the WIMSE chain convention; resolves the 262 and 455 status codes by
   obtainability; adds structured failure fields to the status code
   model, states the protocol's position in the transfer-protocol
   vocabulary throughout, and moves module material to companion
   specifications so that this document carries the protocol and only
   the protocol.  AGTP is designed to compose with existing agent
   frameworks, which keep their own semantics and development paths.
- **draft-ietf-rats-ear-05** (new-draft, score 18, verifiable_claims) [rats]: [EAT Attestation Results](https://datatracker.ietf.org/doc/draft-ietf-rats-ear/) — This document defines the EAT Attestation Result (EAR) message
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
- **draft-ietf-rats-posture-assessment-05** (new-draft, score 18, verifiable_claims) [rats]: [Remote Posture Assessment for Systems, Containers, and Applications at Scale](https://datatracker.ietf.org/doc/draft-ietf-rats-posture-assessment/) — This document establishes an architectural pattern whereby
   Attestation Results could be produced for a complete set of
   benchmarks or controls that are defined and grouped by an external
   entity, eliminating the need to convey individual Evidence items for
   each item within a benchmark or control framework.  This document
   establishes a pattern to list sets of benchmarks and controls within
   CWT and JWT formats for use as an Entity Attestation Token (EAT).
   While the discussion below pertains mostly to TPM, other Roots of
   Trust such as TCG DICE and non-TCG defined components will also be
   included.
- **draft-liu-oauth-delegation-chaining-00** (new-draft, score 18, authorization) [none]: [Delegation Chaining for the Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-liu-oauth-delegation-chaining/) — The Identity Assertion JWT Authorization Grant (ID-JAG) defines how a
   client obtains a delegated authorization grant from an identity
   assertion.  It leaves the validation of the actor_token, the related
   policy evaluation, and the act claim of the issued ID-JAG open for
   future profiles.  This document defines those rules for delegation
   chains, in which a series of workloads, such as AI agents, act on
   behalf of an initial end-user across multiple hops.

   Each delegating workload authenticates to the Authorization Server
   and presents the ID-JAG it holds as the subject_token of an OAuth 2.0
   Token Exchange request, together with the SPIFFE JWT-SVID of the
   workload it delegates to as the actor_token.  The Authorization
   Server validates both workload identities, checks that the delegating
   workload matches the may_act claim of the subject_token, and enforces
   monotonic scope attenuation.  It then issues a new ID-JAG for the
   next hop, carrying the actor chain in the act claim.  The last
   workload of the chain delegates to no one and instead redeems its ID-
   JAG for an Access Token with the JWT bearer grant of [RFC7523].  An
   optional variant based on self-issued Delegation Assertions is
   defined for hops where the Authorization Server is not reachable.
- **draft-mcguinness-oauth-grant-catalog-01** (new-draft, score 18, core_identity) [none]: [OAuth Authorization Grant Catalog](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-grant-catalog/) — This specification defines the OAuth Authorization Grant Catalog: an
   authenticated, relationship-specific description of the authorization
   grants that a Resource Authorization Server is prepared to accept
   from a Grant Issuer.  A Grant Issuer is an authorization server, such
   as an identity provider, that issues grants for redemption at the
   Resource Authorization Server.  For each eligible target tenant, a
   catalog describes the protected resources, scope values,
   authorization details types, claims, subject identifier formats, and
   grant binding methods that the Resource Authorization Server accepts.
   The Grant Issuer uses the catalog as input to the policy under which
   it issues grants; the catalog is not an authorization decision.  The
   data model is independent of grant encoding and retrieval protocol.
   This specification applies it only to the Identity Assertion JWT
   Authorization Grant (ID-JAG), and defines an OAuth retrieval protocol
   that delivers the complete catalog in one response.
- **draft-uppalapati-wimse-pq-agent-identity-01** (new-draft, score 18, core_identity) [none]: [Post-Quantum Requirements for Software and AI Agent Identity](https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/) — A delegation record retained as evidence must remain verifiable long
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
- **draft-araut-oauth-transaction-tokens-for-agents-03** (new-draft, score 17, authorization) [none]: [Transaction Tokens For Agents](https://datatracker.ietf.org/doc/draft-araut-oauth-transaction-tokens-for-agents/) — This document specifies an extension to OAuth Transaction Tokens
   OAUTH-TXN-TOKENS (https://drafts.oauth.net/oauth-transaction-tokens/
   draft-ietf-oauth-transaction-tokens.html) to support agent context
   propagation within Transaction Tokens for agent-based workloads.  The
   extension defines the agentic_ctx claim, a structured JWT claim that
   carries chain-level metadata required for multi-agent flow integrity.

   The extension addresses two deployment patterns: single-agent flows
   where one agent acts on behalf of a user within a transaction, and
   multi-agent flows where multiple agents collaborate across a call
   chain.  In multi-agent scenarios, the Transaction Token is replaced
   at each agent transition by the Transaction Token Service, updating
   the agentic_ctx claim while preserving the immutable identity context
   (sub and act claims) established at transaction initiation.

   By propagating agent chain context to every service in the call path,
   this extension enables Resource Servers to implement authorization
   policies that distinguish agentic execution paths from direct human
   calls, and provides the transaction lineage required for fine-grained
   audit trails at the point of data access.  Security and compliance
   teams gain visibility into the downstream operational footprint of an
   agentic workflow — the full set of services and data stores reached
   under a single transaction — enabling post-incident reconstruction
   and bounded assessment of agentic reach.

   This specification leverages the existing act claim as defined in
   RFC8693 (https://datatracker.ietf.org/doc/html/rfc8693) and the sub
   claim as defined in OAUTH-TXN-TOKENS (https://drafts.oauth.net/oauth-
   transaction-tokens/draft-ietf-oauth-transaction-tokens.html).  It
   does not define new token types or grant types; it operates entirely
   within the existing Transaction Token issuance and replacement
   mechanisms defined by the base specification.
- **draft-brooks-ztdnaid-new-03** (new-draft, score 17, core_identity) [none]: [The 'ztdnaid' URI Scheme for Zero-Trust Digital DNA Identifiers (ZTDNAID)](https://datatracker.ietf.org/doc/draft-brooks-ztdnaid-new/) — This document defines the 'ztdnaid' Uniform Resource Identifier(URI)
   scheme, used to represent globally unique, cryptographically
   verifiable Digital DNA Identifiers (ZTDNAIDs) within Zero Trust
   architecture implementations. A ZTDNAID binds an entitys immutable,
   unique Digital DNA Record "DDR" to a resolvable identifier
   suitable for authentication, authorization, attestation, and
   trust-registry lookup. The scheme is designed for use with trust
   registries operating across "Public Trust Infrastructure" (PTI),
   such as SAG-CTR and supports deterministic resolution, offline
   verification, and secure dereferencing.
- **draft-chursin-rats-energy-attestation-01** (new-draft, score 17, trust_infrastructure) [none]: [Hardware-Rooted Attestation Tokens for Electricity Generation](https://datatracker.ietf.org/doc/draft-chursin-rats-energy-attestation/) — This document specifies an attestation token format and verification
   protocol for hardware-rooted measurements of electricity generation.
   The protocol enables a tamper-evident chain of custody from the
   secure element at a metering device to a publicly verifiable
   settlement layer, using ECDSA P-256 signatures generated inside a
   certified secure element and carried in a COSE_Sign1 structure.  It
   defines: (a) the CBOR-encoded attestation token, aligned with the
   Entity Attestation Token format of RFC 9711 and the Remote
   ATtestation procedureS (RATS) architecture of RFC 9334; (b) a Merkle-
   aggregation and on-chain commitment scheme for scalable verification;
   and (c) a registry mechanism for endorsing device public keys, which
   may be expressed using Concise Reference Integrity Manifests (CoRIM).
   Verifier output is expressed as EAT Attestation Results (EAR), and
   the measurement intervals implied by consecutive tokens support time-
   granular, including hourly, accounting.  The token is intended for
   use by relying parties, such as energy producers, consumers,
   regulators, and standards bodies, that require cryptographic
   provenance for clean-energy claims.
- **draft-davliatshin-oauth-attenuation-chains-report-00** (new-draft, score 17, authorization) [none]: [Independent Implementation and Formal Analysis of Attenuating Delegation Chains for AI Agents](https://datatracker.ietf.org/doc/draft-davliatshin-oauth-attenuation-chains-report/) — This document reports an independent implementation and formal
   analysis of two individual Internet-Drafts that propose offline-
   verifiable, attenuating delegation chains for AI agents: Attenuating
   Authorization Tokens (AATs), in revisions -01 and -02, and the Agent
   Delegation Chain of draft-asor-wimse-agent-delegation-chain-02.  It
   describes a minimal verifier written from each draft's text, with
   profiles for AAT -01, AAT -02 and asor-02, and a ProVerif model of
   the chain structures of AAT -01 and asor-02.  The AAT -02 profile,
   written from the text and then run against the author's 229-vector
   test suite, agrees with it on all 229 vectors.  Of 25 observations
   recorded on AAT -01, the -02 text resolves 19 (16 closed, 3 closed as
   intended design); one is partly resolved, one no longer arises, and
   four remain open.  The report lists ten points where -02 leaves an
   implementer more than one conforming behaviour.  Two properties
   raised in public review are checked on both chain structures.  The
   author of this report is not an author of either draft.  The report
   specifies nothing; it follows the shape of RFC 7942.
- **draft-gupta-mih-maprg-nfc-agent-evidence-00** (new-draft, score 17, trust_infrastructure) [none]: [From Tap to Record: Layered Evidence for Agent Discovery and Payment over Near-Field Communication](https://datatracker.ietf.org/doc/draft-gupta-mih-maprg-nfc-agent-evidence/) — When an AI agent finds a counterparty, interacts with it, and pays
   it, the interaction crosses every layer of the stack: a physical tap
   between two devices, the hardware that holds their keys, a transport
   session, peer discovery and gossip, and finally an application record
   of what was agreed, paid, and delivered.  Each layer produces its own
   evidence, and today nothing joins them.  This document puts the near-
   field tap at the center and follows one progression, from tap to
   rendezvous, authenticated session, interaction, payment, and evidence
   record.  For each layer it states what evidence the layer can
   contribute, what a verifier has to trust, and how a single verifiable
   record can cite all of it by digest.  It treats hardware attestation
   and a transparency log checked by independent witnesses as
   complementary roots of evidence that answer different questions,
   describes how light nodes can check one interaction through evidence
   requests instead of replicating a swarm, and asks which measurable
   observations can independently corroborate such a record.  It is a
   problem statement and research agenda for discussion in MAPRG, not a
   protocol specification.
- **draft-hood-agtp-composition-02** (new-draft, score 17, core_identity) [none]: [AGTP Composition Profiles](https://datatracker.ietf.org/doc/draft-hood-agtp-composition/) — The Agent Transfer Protocol (AGTP) operates as a substrate beneath
   several adjacent layers: Agent Group Messaging Protocols (AGMPs) such
   as the Model Context Protocol (MCP), the Agent-to-Agent Protocol
   (A2A), and the Agent Communication Protocol (ACP); external identity
   providers (OAuth, OIDC, enterprise IdPs); and HTTP-based clients that
   interact with agents through translation gateways.  This document
   specifies the composition profiles for each of these adjacent layers,
   defining normative mapping rules between the adjacent layer and AGTP.

   Three composition families are specified.  The AGMP composition
   profile specifies how MCP, A2A, and ACP messages are carried over
   AGTP, with mapping rules for identity, authority scope, delegation,
   and session fields between the AGMP and AGTP layers.  The External
   Identity Provider composition profile specifies how AGTP agent
   identity composes with externally-issued credentials, treating "which
   agent" and "on whose behalf" as orthogonal axes.  The HTTP Gateway
   composition profile specifies the translation surface for accepting
   HTTP traffic into AGTP- served agents as a REST adoption ramp.

   Across all three families, AGTP headers take precedence over
   equivalent adjacent-layer fields for all infrastructure-level
   routing, enforcement, and audit operations.  Agents gain transport-
   level governance, observability, and identity without modification to
   the adjacent layers.
- **draft-ietf-jose-jwp-modular-bbs-00** (new-draft, score 17, verifiable_claims) [jose]: [BBS and Modular Sub-proofs with JSON Web Proofs](https://datatracker.ietf.org/doc/draft-ietf-jose-jwp-modular-bbs/) — This document defines a digital credential format that uses JSON Web
   Proofs (JWP) as its container format and Blind BBS Signatures as its
   signature scheme combined with a modular framework for attaching
   zero-knowledge sub-proofs.  This allows a Holder to reveal some
   attributes directly while proving predicates such as range or
   equality over the ones they keep hidden.  A credential can
   additionally be bound to a Holder-held device key, with possession of
   the key proven in every presentation without revealing the public key
   or signature.  Concrete sub-proof and device-binding constructions
   are not defined in this document, only the core serialization.  The
   credential type definition and data model follow SD-JWT VC.
- **draft-ietf-oauth-delegate-sd-jwt-00** (new-draft, score 17, verifiable_claims) [oauth]: [Delegate SD-JWT](https://datatracker.ietf.org/doc/draft-ietf-oauth-delegate-sd-jwt/) — This document specifies an extension to Selective Disclosure JSON Web
   Tokens [RFC9901] to support further delegation from the Holder to a
   Delegate Holder.  This is done by allowing the Key Binding JWT to
   also be an SD-JWT, optionally with its own Key Binding.  This has
   particular applicability to Agentic systems.
- **draft-luna-eagf-agent-delegation-semantics-01** (new-draft, score 17, core_identity) [none]: [Semantic Governance Requirements for AI Agent Delegation and Handoff](https://datatracker.ietf.org/doc/draft-luna-eagf-agent-delegation-semantics/) — AI agents increasingly decide and act on behalf of organizations and
   delegate work to other agents.  Identity, authentication,
   authorization and runtime control mechanisms establish who is acting
   and what is permitted, but they do not by themselves preserve the
   organizational meaning of a delegation: the bounded authority,
   purpose, material context, and the distinction between a
   recommendation, a decision, an action and its outcome.  This document
   states requirements, derived from the Enterprise Agent Governance
   Framework (EAGF), that such semantics be preserved across tool calls,
   delegations and agent-to-agent handoffs.  It defines no new protocol.
- **draft-martin-skis-00** (new-draft, score 17, core_identity) [none]: [Skill Intake Security Requirements for AI Agents (SKIS)](https://datatracker.ietf.org/doc/draft-martin-skis/) — Skill Intake Security (SKIS) defines how an organization should
   examine a third-party skill, plugin or agent definition before it is
   allowed to act: four review levels graded by risk, a verification
   chain from provenance to a release record, and operational controls
   for updates, inventory, logging and revocation.  AI agents
   increasingly extend their capabilities with third-party skills:
   packages of natural-language instructions, metadata and helper
   scripts that a model reads as authoritative context.  Related work
   addresses agent identity, authorization, discovery and skill-layer
   risks; this document proposes a consolidated intake procedure with
   explicit organizational obligations.  The verification chain covers
   provenance, integrity pinning, full-content inspection and comparison
   of declared versus observed capabilities.  SKIS is vendor-neutral and
   intended to complement existing identity and provenance
   specifications.
- **draft-raskar-net4ai-agent-portability-00** (new-draft, score 17, authorization) [none]: [Architecture for Portable AI Agent Workloads Across Internet Runtimes](https://datatracker.ietf.org/doc/draft-raskar-net4ai-agent-portability/) — AI agent definitions are commonly coupled to a particular framework,
   model provider, tool environment, or execution service.  This
   coupling makes it difficult for an independently operated runtime to
   determine whether it can interpret, place, authorize, and execute an
   agent workload.

   This document describes an architecture for portable AI agent
   workloads across heterogeneous Internet runtimes.  It separates
   authoring, packaging and distribution, and execution; identifies the
   information a workload needs to declare at that boundary; and
   distinguishes representation portability, execution portability, and
   placement portability.  It also identifies research questions around
   capability matching, workload placement, dependency distribution,
   identity, authorization, state, and migration.

   This document is architectural and research-oriented.  It does not
   define a package wire format, universal agent language, runtime API,
   discovery service, or new transport protocol.
- **draft-raskar-portable-agent-runtime-architecture-00** (new-draft, score 17, authorization) [none]: [Architecture for Portable AI Agent Workloads Across Internet Runtimes](https://datatracker.ietf.org/doc/draft-raskar-portable-agent-runtime-architecture/) — AI agent definitions are commonly coupled to a particular framework,
   model provider, tool environment, or execution service.  This
   coupling makes it difficult for an independently operated runtime to
   determine whether it can interpret, place, authorize, and execute an
   agent workload.

   This document describes an architecture for portable AI agent
   workloads across heterogeneous Internet runtimes.  It separates
   authoring, packaging and distribution, and execution; identifies the
   information a workload needs to declare at that boundary; and
   distinguishes representation portability, execution portability, and
   placement portability.  It also identifies research questions around
   capability matching, workload placement, dependency distribution,
   identity, authorization, state, and migration.

   This document is architectural and research-oriented.  It does not
   define a package wire format, universal agent language, runtime API,
   discovery service, or new transport protocol.
- **draft-raskar-scitt-agent-provenance-00** (new-draft, score 17, trust_infrastructure) [none]: [SCITT Profile for Portable AI Agent Package Provenance](https://datatracker.ietf.org/doc/draft-raskar-scitt-agent-provenance/) — Portable AI agent packages can contain executable or interpretable
   behavior, prompts, workflow graphs, tool schemas, dependencies, and
   declarations of execution requirements.  Such packages may be
   authored, transformed, repackaged, scanned, approved, published,
   superseded, and withdrawn by different parties before they are
   executed by an independent runtime.

   This document describes a SCITT application profile for transparent
   provenance of portable AI agent packages.  It maps the package
   lifecycle to the SCITT architecture, identifies an immutable package
   digest as the artifact binding point, and defines classes of supply-
   chain statements that can be made about a package without defining a
   new statement payload format.  Examples include authorship, build and
   transformation, execution-profile conformance, security assessment,
   publication, approval, supersession, and withdrawal statements.

   This document does not define a portable-agent package format, agent
   execution protocol, runtime authorization model, or per-action
   execution receipt.  It complements SCITT profiles that record agent
   actions or sessions by focusing on the provenance of the agent
   package before and across deployment.
- **draft-watts-agent-evidence-boundary-01** (new-draft, score 17, core_identity) [none]: [Evidence-Bounded Authorization for Agentic Systems: Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-agent-evidence-boundary/) — Autonomous agents increasingly make or propose consequential actions
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
- **draft-watts-ai-identity-conformance-01** (new-draft, score 17, trust_infrastructure) [none]: [AID-1 Provider-Independent Conformance Requirements and Test-Vector Model](https://datatracker.ietf.org/doc/draft-watts-ai-identity-conformance/) — This document defines provider-independent conformance requirements
   for AID-1.  It specifies the execution model for a deterministic
   machine-readable test-vector corpus, including canonicalization,
   cryptographic, identity-binding, delegation, authorization, temporal,
   revocation, replay, attestation, provenance, and integration cases.
   The conformance corpus contains 69 vectors.  Six replay cases are
   architectural boundary tests, including R5, which requires AID-1
   verification to succeed while a downstream D6 scientific-
   admissibility decision rejects the same evidence.
- **draft-zambo-aer1-wimse-mapping-02** (new-draft, score 17, trust_infrastructure) [none]: [AER-1 Receipts as Audit Records for WIMSE AIMS](https://datatracker.ietf.org/doc/draft-zambo-aer1-wimse-mapping/) — The WIMSE AI Identity Management System (AIMS) framework requires
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
- **draft-ayerbe-trip-protocol-05** (new-draft, score 16, core_identity) [none]: [TRIP: Trajectory-based Recognition of Identity Proof](https://datatracker.ietf.org/doc/draft-ayerbe-trip-protocol/) — This document specifies the Trajectory-based Recognition of Identity
   Proof (TRIP) protocol, a decentralized mechanism for establishing
   claims of physical-world presence through cryptographically signed,
   spatially quantized location attestations called "breadcrumbs."
   Breadcrumbs are chained into an append-only log, bundled into
   verifiable epochs, and distilled into a Trajectory Identity Token
   (TIT) that serves as a persistent pseudonymous identifier.

   The protocol employs a Criticality Engine, a statistical anomaly
   detector informed by complex-systems research, to distinguish
   biological movement from synthetic trajectories.  Power Spectral
   Density (PSD) analysis of the displacement series yields a scaling
   exponent alpha that captures long-range temporal correlation in
   movement.  A six-component Hamiltonian energy function scores each
   breadcrumb against the identity's learned behavioral profile in real
   time.

   This revision (-05) reframes the statistical core of the Criticality
   Engine in light of empirical validation against human-mobility data:
   the PSD scaling exponent alpha is specified as a per-deployment-
   calibrated scored feature rather than a fixed classification gate;
   the fixed [0.30, 0.80] "biological" band is withdrawn in favor of
   calibrated ranges; the asserted Levy-PSD bridge is replaced by a
   statement of the independence of the step-size and temporal-
   correlation features; and a new validation section reports separation
   results and methodology.  The cryptographic chain, RATS mapping,
   Active Verification Protocol, and privacy model are unchanged from
   -04.

   TRIP is designed to be transport-agnostic and operates independently
   of any particular naming system, blockchain, or application layer.
- **draft-gilda-audit-agent-audit-record-03** (new-draft, score 16, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-audit-agent-audit-record/) — This document defines a record format for AI agent authorization
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
- **draft-ietf-oauth-sd-jwt-vc-23** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.
- **draft-mcguinness-oauth-mission-02** (new-draft, score 16, authorization) [none]: [Mission-Bound Authorization for OAuth 2.0](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-mission/) — OAuth 2.0 has authorization grants and access tokens but no standard
   object that binds an approved task, such as one an AI agent performs
   on a user's behalf, to the authority approved for it and governs the
   tokens later issued under that authority.  This document defines that
   object for OAuth 2.0: a Mission.

   A client submits, through Pushed Authorization Requests, a Mission
   Intent describing the task it will perform.  The authorization server
   derives Rich Authorization Requests authorization details from it,
   binds the approved task and that authority to the Approver's consent
   through integrity anchors, and records a durable Mission.  Every
   access token issued under the Mission carries a subset of the
   approved authority and a "mission" claim, and every issuance is gated
   on the Mission's lifecycle state.  Revoking a Mission stops further
   issuance; it does not recall tokens already issued, which a resource
   server that enforces from the token alone can continue to honor until
   they expire.

   Optional capabilities represent delegation among agents with the
   OAuth Actor Profile and, as specified by a companion, let a single
   Mission be honored across trust domains.  Runtime enforcement of each
   action is a separate, optional layer.
- **draft-ni-wimse-ai-agent-identity-04** (new-draft, score 16, agent_identity) [none]: [WIMSE Applicability for AI Agents](https://datatracker.ietf.org/doc/draft-ni-wimse-ai-agent-identity/) — This document discusses WIMSE applicability to Agentic AI, so as to
   establish independent identities and credential management mechanisms
   for AI agents.  It also discusses mechanisms for cryptographically
   binding an AI agent identity to an accountable user or organization.
- **draft-rampertab-audit-agent-authority-history-00** (new-draft, score 16, core_identity) [none]: [Replayable Authority Histories for Auditing Automated Agents](https://datatracker.ietf.org/doc/draft-rampertab-audit-agent-authority-history/) — Software agents act on authority that changes while they run:
   permissions are granted and revoked, running instances are replaced,
   and some requests are refused.  Activity logs record what a system
   reports it did, but they do not by themselves show what an agent was
   allowed to do when it acted, and the operator can edit them.  This
   document specifies a model for an authority history: an append-only,
   signed record of who granted what to whom, which actions were
   admitted, which requests were refused, and which unfinished duties
   survive when one agent replaces another.  Given independently
   authenticated owner keys and history identity, a verifier can replay
   the history and recompute its recorded authorization decisions while
   trusting neither the agent nor the operator.  The document states
   what such a verifier can and cannot establish.  Optional profiles
   cover external anchoring, federated operation, human-attested keys
   and zero-knowledge disclosure.  An informative appendix describes one
   encoding.
- **draft-raskar-agentic-web-federated-resolution-02** (new-draft, score 16, adjacent_watchlist) [none]: [Registry-Assisted Resolution for Known Subjects Without DNS Discovery Anchors](https://datatracker.ietf.org/doc/draft-raskar-agentic-web-federated-resolution/) — Discovery mechanisms for AI resources increasingly use DNS and mDNS
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
- **draft-watts-protocol-test-evidence-profile-01** (new-draft, score 16, trust_infrastructure) [none]: [Protocol Conformance Test Evidence Records: A Reproducibility Profile](https://datatracker.ietf.org/doc/draft-watts-protocol-test-evidence-profile/) — This document proposes a narrow record profile for describing
   software protocol-conformance test runs, including the tested
   artifact, test suite, implementation, execution environment,
   individual case outcomes, digests, and known limitations.  It does
   not define a new signature scheme, attestation architecture,
   transparency service, or general-purpose test-output language.
   Implementations are encouraged to reuse existing mechanisms such as
   SCITT statements, RATS terminology, COSE, JSON canonicalization, and
   existing test-report formats where suitable.  This individual draft
   candidate has not been submitted to or endorsed by the IETF.
- **draft-ietf-oauth-identity-assertion-authz-grant-06** (new-draft, score 15, authorization) [oauth]: [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) — This specification provides a mechanism for an application to use an
   identity assertion to obtain an access token for a third-party API by
   coordinating through an identity provider that the downstream
   Resource Authorization Server already trusts for single sign-on
   (SSO), using OAuth 2.0 Token Exchange (RFC 8693) and the JWT Profile
   for OAuth 2.0 Authorization Grants (RFC 7523).  This pattern is
   informally referred to as Cross-App Access (XAA).
- **draft-ietf-rats-eat-da-00** (new-draft, score 15, trust_infrastructure) [rats]: [An EAT Profile for Trustworthy Device Assignment](https://datatracker.ietf.org/doc/draft-ietf-rats-eat-da/) — In confidential computing, device assignment (DA) is the method by
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
- **draft-mahy-mls-sd-cwt-credential-03** (new-draft, score 15, verifiable_claims) [none]: [Messaging Layer Security Credentials using Selective Disclosure JSON and CBOR Web Tokens](https://datatracker.ietf.org/doc/draft-mahy-mls-sd-cwt-credential/) — The Messaging Layer Security (MLS) protocol contains Credentials used
   to authenticate an MLS client with a signature key pair.  Selective
   Disclosure CBOR Web Tokens (SD-CWT) and Selective Disclosure JSON Web
   Tokens (SD-JWT) define token formats where the holder can selectively
   reveal claims about itself with strong integrity protection and
   cryptographic binding to the holder's key.  This document defines MLS
   credentials for both these token types.
- **draft-sethi-openaiis-protocol-00** (new-draft, score 15, authorization) [none]: [OpenAIIS -- A Decentralized Trust, Governance and Safety Protocol for the Digital World](https://datatracker.ietf.org/doc/draft-sethi-openaiis-protocol/) — Open Artificial Intelligence Integrity Sentinel (OpenAIIS) specifies
   a decentralized trust, governance, and safety protocol for digital
   activity performed by people, organizations, and autonomous AI
   agents.  It binds digital assertions and consequential actions to
   authenticated issuers, scoped authority, accepted responsibility,
   supporting evidence, and a verifiable history.  A canonical, domain-
   separated signature authenticates each typed claim; ordered Merkle
   records and signed checkpoints establish its historical registry
   context.

   Every accepted registry record enters an automatic, durable process
   that commits covering checkpoints to Bitcoin mainnet.  The resulting
   portable proof binds the exact signed claim and its authenticated
   history to Bitcoin's proof-of-work chain, protecting historical
   evidence against retroactive substitution or rewriting without the
   work required to establish an accepted competing Bitcoin history.
   Governance and safety records express consent, delegation,
   authorization, revocation, withdrawal, disputes, and security
   incidents.  Independent implementations can verify both historical
   commitments and the evidence governing present action without relying
   exclusively on the system that issued or executed a claim.  OpenAIIS
   supports versioned decentralized consensus profiles without a
   protocol-native currency.
- **draft-thaha-wimse-agent-evidence-binding-03** (new-draft, score 15, core_identity) [none]: [Evidence Binding for AI Agent Credentials](https://datatracker.ietf.org/doc/draft-thaha-wimse-agent-evidence-binding/) — The WIMSE AI Identity Management System (AIMS) requires tamper-
   evident agent audit logs but does not specify their format or
   discovery.  This document maps the AIMS minimum fields to the SCITT
   Agent Execution Evidence profile, defines one claim that binds a
   workload credential to the persistent agent, governing policy,
   expected Evidence Service and optional Assurance Statement, and
   defines an in-toto predicate type for carrying Execution Receipts
   alongside the in-toto agent audit record format.  It also describes
   how a service admits an agent's call by checking its assurance at the
   moment of the request, and defines an HTTP field that links each call
   to the caller's evidence.  It is a companion to the AIMS work and
   makes no change to it.
- **draft-das-digital-money-threat-models-00** (new-draft, score 14, agent_identity) [none]: [Valid Signature, Unauthorized Effect: Security Threat Models and Execution-Finality Controls for Digital Money](https://datatracker.ietf.org/doc/draft-das-digital-money-threat-models/) — Problem: unauthorized movements of digital money often succeed with
   valid credentials.  A compromised service presents its genuine
   workload identity; a signing module signs a digest it was handed; an
   account is delegated to changed code; a coordinator feeds threshold
   signers inconsistent inputs; parallel wallets each see the same
   balance; a stale region honors a revoked authorization; a retry after
   a crash sends a second transfer; an AI agent turns injected text into
   a valid payment-tool call; or a bridge releases on provisional
   finality.  Identity checks, TLS, hardware key protection, threshold
   signing, allowlists, fraud scoring, audit logs and ledger consensus
   each answer a different question.  None of them, by itself, verifies
   at the moment of release that the exact effect is authorized, current
   and unused.

   Solution: this document gives fourteen security threat models (TM-01
   to TM-14), each with attacker capability, plausible pathway, why
   existing protections may fail, a constructive protected procedure, a
   YES/NO/UNKNOWN workflow, coverage limits and a negative-effect test.
   It analyzes thirteen classes of existing controls and specifies a
   common protected sequence: independent authority bound in a protected
   domain, reconstruction of the effect from the final native bytes,
   protected freshness, budget and replay state, a non-bearer handle
   consumed atomically at the exclusive signer, dispatcher or account
   guard, and typed outcomes that keep UNKNOWN distinct from success or
   failure.  The control is complementary to ledger consensus, not a
   replacement for it.

   Scope: 29 diagrams, 56 test vectors, 90 enforcement points, worked
   mathematical examples, and runnable Python, Go and Node.js reference
   models with a latency harness.  The document is informational and
   defines no wire format.  The scenarios are hypothetical threat
   models, not findings about any real incident or organization.
- **draft-gruszka-audit-decision-receipts-05** (new-draft, score 14, trust_infrastructure) [none]: [Decision Receipts for Approvals, Declined Actions and Executed Actions in Agent Audit Records](https://datatracker.ietf.org/doc/draft-gruszka-audit-decision-receipts/) — The architecture for auditing agent delegation and interactions
   proposed for the AUDIT effort names Interaction Records, Action
   Records and Authorization Transition Records, and leaves their
   encoding open.  This document shows how an existing signed record,
   the decision receipt of the open-source proofbundle project, together
   with its companion outcome receipt, gives three such records exact
   bytes, a signature and digest bindings that a third party can check
   offline.  The three cases are a human approval, a declined action and
   an executed action with its result.  For each case the document maps
   the receipt members onto the record types of the architecture, states
   what the receipt adds and what it does not show, and gives an offline
   verification procedure.  It states one requirement for approvals,
   that an approval is honoured at most once, also after the record of
   consumed approvals is rotated.  Test vectors for all three cases,
   each with a counterexample, are included.  The document also
   describes, informatively, how a receipt can be registered with a
   Transparency Service under RFC 9943 and what a SCITT Receipt then
   shows and does not show.  This document defines no new format,
   predicate or registry.
- **draft-hood-agtp-merchant-identity-03** (new-draft, score 14, adjacent_watchlist) [none]: [AGTP Merchant Identity and Agentic Commerce Binding](https://datatracker.ietf.org/doc/draft-hood-agtp-merchant-identity/) — The Agent Transfer Protocol (AGTP) specifies the sending side of an
   agentic transaction: agent identity, Authority-Scope enforcement,
   Budget- Limit declaration, and a signed Attribution-Record on every
   method invocation.  The receiving side of a PURCHASE transaction --
   the merchant or service provider -- has no equivalent protocol-level
   identity or verification mechanism.  That asymmetry is the gap this
   document closes.

   This document specifies the AGTP Merchant Identity and Agentic
   Commerce Binding.  It defines a merchant in AGTP as an agent whose
   Agent Identity Document carries role: "merchant", specifies the
   merchant-specific fields that ride on the Agent Identity Document
   under that declaration, aligns Merchant Trust Tiers with AGTP Trust
   Tier semantics, and defines the protocol integration points at which
   merchant identity is verified.  These include the PURCHASE method
   handshake, the DISCOVER method result surface, and the Attribution-
   Record.  This document also defines the Intent-Assertion header for
   portable, detached principal-authorized intent, the Cart-Digest
   mechanism for multi-line-item transactions, and the 458 Counterparty
   Unverified status code.  Together these mechanisms close the
   verification loop between agent and merchant within AGTP's governance
   model.

   Version 02 unifies merchant identity onto the Agent Genesis + Agent
   Identity Document architecture: there is no separate Merchant Genesis
   document type.  A merchant is an agent with role: "merchant" declared
   in its Agent Identity Document.  This reflects the architectural
   principle that identity is permanent (carried on Genesis) and
   capability is mutable (carried on the Identity Document); a role
   change re-mints no Agent-ID.
- **draft-ietf-wimse-workload-creds-03** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload Credentials](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones up to complex multi-service, multi-cloud, multi-
   tenant deployments.

   This document defines the credentials that workloads use to represent
   their identity.  They can be used in various protocols to
   authenticate workloads to each other.  To use these credentials,
   workloads must provide proof of possession of the associated private
   key material, which is covered in other documents.  This document
   focuses on the credentials alone, independent of the proof-of-
   possession mechanism.
- **draft-ietf-wimse-workload-identity-practices-08** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-pelov-rich-architecture-01** (new-draft, score 14, authorization) [none]: [RICH: RESTful Interface for the Control-plane of Harnesses](https://datatracker.ietf.org/doc/draft-pelov-rich-architecture/) — This document specifies the RICH (RESTful Interface for the Control-
   plane of Harnesses) architecture and information model.  RICH
   provides a protocol-neutral governance, contract, qualification, and
   binding layer for RPC-based agent capabilities.  It establishes a
   REST-addressable control plane for managing capability lifecycles
   while preserving native protocol execution in the data plane.  It
   defines immutable capability and contract revisions, evidence
   provenance, connector transformation classes, compiled binding
   lockfiles, admission of bindings against an authorization, and
   runtime validation rules designed to contain drift and prevent
   confused deputy attacks in agentic systems.  RICH does not make model
   behavior deterministic: it bounds what each admitted call can do, and
   makes every step on the connector path checkable and refusable.
- **draft-rosenberg-oauth-aauth-02** (new-draft, score 14, authorization) [none]: [AAuth - Agentic Authorization OAuth 2.1 Extension](https://datatracker.ietf.org/doc/draft-rosenberg-oauth-aauth/) — AI Agents are increasingly accessing web resources on behalf of the
   users they serve.  Traditionally these agents are granted normal
   OAuth access tokens through existing OAuth grant flows.  However,
   these flows were designed in the era of traditional software, and
   when applied to AI Agents, multiple problems have arisen.  This
   document outlines some of the problems, and then proposes a simple
   OAuth2.1 extension that enables AI Agents to obtain access tokens at
   time of resource access using Human-In-the-Loop or other approval
   flows.  We call this the Agent Authorization Grant (aauth) grant
   flow.  This document also compares the proposed solution with
   another, non-backwards compatible aauth solution.
- **draft-watts-rats-verification-promotion-appraisal-01** (new-draft, score 14, trust_infrastructure) [none]: [Verification Promotion and Agent Assurance Appraisal Profile](https://datatracker.ietf.org/doc/draft-watts-rats-verification-promotion-appraisal/) — This document maps protocol-verification evidence and the WIVL
   assurance-stage model onto the RATS architecture.  It defines
   appraisal requirements for SPEC_VALIDATED, LOCAL_CONFORMANT,
   INDEPENDENTLY_REPRODUCED, and SECURITY_TESTED results while
   preserving unknown evidence and requiring arithmetic preconditions
   for mathematical test vectors.  An attestation result reports bounded
   assurance; it is not an authorization grant or production-release
   decision.
- **draft-agentic-ai-usecases-requirements-07** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-das-digital-money-safety-module-00** (new-draft, score 13, authorization) [none]: [Valid Credential Is Not Authorized Payment: A Digital Money Online Safety Module Based on Execution Finality](https://datatracker.ietf.org/doc/draft-das-digital-money-safety-module/) — Problem: digital money is now moved by software that holds valid
   credentials: AI agents that buy services, card and wallet processors,
   exchange treasury systems, stablecoin issuers, cross-chain bridges
   and offline digital-currency devices.  In these systems a valid
   signature, token, approval or initial card authorization is commonly
   treated as permission for whatever financial effect is finally
   released.  Between approval and release the amount, beneficiary,
   asset, route, fee or message format can change; operations can be
   replayed or run concurrently against one budget; and a lost
   confirmation can lead to a second payment.  Existing controls
   authenticate the party, the key or the message, but do not verify
   that the effect actually released is the effect that was authorized.

   Solution: this document describes a digital money online safety
   module based on execution finality.  Authority is collected and bound
   in a protected record.  Each candidate financial operation is held in
   a non-effective state.  At the last controllable boundary, a second
   protected domain reconstructs the actual effect from the native bytes
   and compares it with the bound authority and current policy, and a
   Finality Sink atomically consumes a sink-bound, non-bearer Execution
   Handle while releasing only that exact effect.  Signing, clearing,
   settlement and delivery evidence are kept as distinct states, and an
   uncertain outcome remains UNKNOWN instead of being retried.

   Scope: the document gives a common workflow, safety invariants, 19
   profiles (agent payments, card capture, cross-rail FX, tokenized
   deposits, offline CBDC, payment-versus-payment, delivery-versus-
   payment, stablecoins, bridges, exchange custody, QR and alias
   resolution, metered payments, privacy-preserving compliance,
   financial-message continuity, subscriptions, disputes, autonomous
   trading, delegated treasury and accounts payable), 27 diagrams, 114
   test vectors, 54 enforcement points and reference code in Python, Go
   and JavaScript.  It defines no wire format and is informational.
- **draft-dinuzzo-best-protocol-03** (new-draft, score 13, authorization) [none]: [BEST: The Behavioral State Protocol](https://datatracker.ietf.org/doc/draft-dinuzzo-best-protocol/) — The Behavioral State Protocol (BEST) defines a discovery-first,
   behaviour-oriented interaction surface for services: a discovery
   manifest, whichever of commands, queries and events the implementor
   chooses to expose, and optionally the multi-step recipes (workflows)
   a service publishes.  Services are named by DNS domain names and
   self-describe through a manifest at the well-known URI "/.well-known/
   best"; messages use a conformant profile of the CloudEvents 1.0
   envelope described by JSON Schema; and an agent obtains its own
   credential through the OAuth 2.0 Device Authorization Grant, approved
   by the person it acts for in their own browser.  BEST deliberately
   specifies only the interaction surface -- never a service's internal
   architecture, storage, or execution model -- allowing independent
   implementations across any runtime, language, or transport to
   interoperate without bespoke integration.
- **draft-morrison-acts-for-01** (new-draft, score 13, authorization) [none]: [Acts-For: Signing In to a Website with a ~handle, for a Person or an Agent Acting for One](https://datatracker.ietf.org/doc/draft-morrison-acts-for/) — Acts-For lets a person sign in to any website with the ~handle they
   already hold, and lets an AI agent sign in or register at that
   website on the person's behalf.  Neither needs a username, a password
   or an account per site.  A website joins by publishing one DNS
   record.  A person signs in through a standard OpenID Connect
   authorization code flow and the site receives a short-lived token
   naming the person by a number unique to that site.  An agent obtains
   a short-lived pass from the issuer over the Model Context Protocol
   and presents it to the site.  The pass names the same per-site
   number, the agent's own key and ~handle, and the limits the person
   set.  The site checks it against a published key and calls nobody.
- **draft-okutomi-session-bound-agent-identity-07** (new-draft, score 13, core_identity) [none]: [A Verifier-Side Acceptance Profile for Channel-Bound Agent Identity and Authorization](https://datatracker.ietf.org/doc/draft-okutomi-session-bound-agent-identity/) — This document defines a verifier-side acceptance profile for channel-
   bound Agent identity and authorization.  It addresses context
   diversion, where cryptographically valid material is accepted for a
   different service, tenant, actor, task, target, delegation, or
   authority boundary than the verifier intended.

   A verifier accepts an actor only when a verified authority grant,
   holder-of-key proof, accepted channel instance, freshness and replay
   state, any required attestation result, and verifier-local policy all
   describe the same intended interaction.  Protocol-specific wire
   formats and deployment choices are left to binding profiles.
- **draft-skyfire-oauth-using-kyapay-tokens-02** (new-draft, score 13, core_identity) [none]: [Using KYAPay Tokens](https://datatracker.ietf.org/doc/draft-skyfire-oauth-using-kyapay-tokens/) — The KYAPay Token is a JSON Web Token (JWT) that carries verified
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
- **draft-agentproto-context-management-architecture-00** (new-draft, score 12, core_identity) [none]: [Context and Correlation Management Architecture for Distributed Agentic Activities](https://datatracker.ietf.org/doc/draft-agentproto-context-management-architecture/) — Agentic applications increasingly distribute a single objective
   across autonomous agents, tools, and services implemented by
   different vendors, operated by different organizations, and connected
   through different protocols.

   A single activity may contain multiple pairwise dialogs, multiple
   tasks within each dialog, tool invocations, derived resources,
   downstream delegations, and later interactions that reinterpret or
   reuse artifacts produced earlier in the activity.  Existing protocols
   provide useful local identifiers for their own interactions, but
   those identifiers do not by themselves provide a common information
   model for correlating independently maintained dialogs, tasks, and
   resources across protocol and administrative boundaries.

   This document defines an information model consisting of Activities,
   Dialogs, Tasks, Resources, and typed Relationships.  It distinguishes
   Activity correlation from protocol-local Dialog context, and
   distinguishes stable resource identity and provenance from locally
   defined interpretations.

   As such, this document develops a context-and-correlation
   information-model architecture, not a functional reference
   architecture or a wire protocol.  It identifies relevant objects and
   relationships, relevant to maintaining coherent context, and examines
   the implications for preserving and propagating their correlations.
   It does not define the procedures by which applications execute work.
   The model distinguishes the logical extent of an Activity, which may
   extend beyond protocol-managed correlation; extending that coverage
   is selective, while maintaining established managed correlations
   entails responsibilities.
- **draft-chen-lake-edhoc-aka-04** (new-draft, score 12, core_identity) [none]: [EDHOC Authenticated with AKA](https://datatracker.ietf.org/doc/draft-chen-lake-edhoc-aka/) — This document defines an Authentication and Key Agreement (AKA)
   authentication method for the Ephemeral Diffie-Hellman Over COSE
   (EDHOC) key exchange protocol.  This method, named EDHOC-AKA, is
   designed as a specific profile of the EDHOC Pre-Shared Key (PSK)
   authentication method defined in [I-D.ietf-lake-edhoc-psk].

   EDHOC-AKA leverages the 3GPP AKA protocol to dynamically generate a
   session-specific Pre-Shared Key, which is then used to run the EDHOC-
   PSK protocol flow.  The AKA-specific parameters are transported
   within the External Authorization Data (EAD) fields of the EDHOC
   messages.  This approach provides efficient mobile communication
   network access authentication for resource-constrained scenarios
   (such as Non-Terrestrial Networks, NTN) while inheriting the security
   properties of EDHOC-PSK, including mutual authentication, identity
   protection, and forward secrecy.
- **draft-hood-agtp-agent-cert-04** (new-draft, score 12, core_identity) [none]: [AGTP Agent Certificate Extension](https://datatracker.ietf.org/doc/draft-hood-agtp-agent-cert/) — The Agent Transfer Protocol (AGTP) base specification verifies agent
   identity at the application layer: the Agent-ID header resolves to an
   issuer-signed Agent Identity Document, and a per-request Request-
   Signature proves possession of the key that document names.  That
   verification runs per request and needs the document.  This document
   specifies the AGTP Agent Certificate Extension: an optional mechanism
   that binds the Canonical Agent-ID, the recorded owner, and the
   Authority-Scope commitment to an X.509 v3 certificate presented
   during TLS mutual authentication, so that the same verification is
   made once at the handshake and infrastructure components including
   Scope-Enforcement Points (SEPs), load balancers, and governance
   gateways can enforce authority scope without application-layer
   access, at O(1) cost per request.  The extension also defines
   session-level revocation propagation via AGTP NOTIFY broadcast and
   records certificate issuance and revocation in the AGTP transparency
   log.

   Note: Certain mechanisms described in this document may be subject to
   pending patent applications by the author.  The licensor is prepared
   to grant a royalty-free license to implementers consistent with the
   IETF's IPR framework.  See Section 9.4.
- **draft-howe-vcon-lifecycle-02** (new-draft, score 12, trust_infrastructure) [none]: [vCon Lifecycle Management using SCITT](https://datatracker.ietf.org/doc/draft-howe-vcon-lifecycle/) — This document proposes using the SCITT (Supply Chain, Integrity,
   Transparency, and Trust) protocol to record, communicate and
   coordinate the lifecycle of Virtual Conversations (vCons), which are
   standardized containers for conversational data like call recordings,
   transcripts, and chat logs.  While vCons enable capturing and sharing
   conversation details for AI analysis and business purposes, they lack
   mechanisms for proving compliance with privacy regulations and
   consent management.  SCITT addresses this by providing an immutable,
   append-only transparency ledger that records key lifecycle
   events—from vCon creation and consent management to call recording,
   as well as data processing and deletion—enabling entities to
   demonstrate regulatory compliance and maintain trust across
   distributed systems.  The framework specifically addresses consent
   management challenges under regulations like GDPR and CCPA, where
   consent can be revoked at any time, requiring coordinated deletion
   across all parties that have received the vCon.  By combining vCons
   with SCITT, organizations can build scalable, transparent governance
   systems that protect personal data rights while enabling responsible
   use of conversational data for AI and business applications.
- **draft-ietf-acme-pop-01** (new-draft, score 12, core_identity) [acme]: [Automated Certificate Management Environment (ACME) Extension for Proof-of-Possession](https://datatracker.ietf.org/doc/draft-ietf-acme-pop/) — The Automated Certificate Management Environment (ACME) protocol
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
   popKey field and includes a pop identifier whose value is the empty
   string.  The server creates a dedicated pop authorization containing
   a single pop-01 challenge, processed using the same state machine as
   any other ACME authorization.  When all authorizations (including the
   pop authorization) are valid, the ACME server issues a certificate
   using the validated public key and the authorized identifiers,
   eliminating the need for a CSR at finalization.  The extension is
   additive and strictly optional: clients that do not use it, and
   servers that do not support it, continue to use the standard CSR-
   based flow defined in [RFC8555] without any changes.
- **draft-ietf-acme-rats-03** (new-draft, score 12, trust_infrastructure) [acme]: [Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type](https://datatracker.ietf.org/doc/draft-ietf-acme-rats/) — This document describes an approach where an ACME Server can
   challenge an ACME Client to provide Evidence, Endorsements, or
   Attestation Result according to the Remote ATtestation procedureS
   (RATS) framework in any format supported by the Conceptual Message
   Wrapper (CMW).

   The ACME Server can optionally challenge the Client for specific
   claims that it wishes attestation for.
- **draft-ietf-seat-use-cases-02** (new-draft, score 12, core_identity) [seat]: [Security Goals and Use Cases for Integrating Remote Attestation with Secure Channel Protocols](https://datatracker.ietf.org/doc/draft-ietf-seat-use-cases/) — This document describes use cases for integrating remote attestation
   (RA) with secure channel protocols, initially TLS and DTLS.  Peer
   authentication establishes a peer's identity; RA supplies Evidence
   for appraisal of its state.  The document identifies protected
   decisions and required assurance, describes the attacks and failure
   modes that threaten them, and derives properties to guide protocol
   designs in the SEAT working group.  These properties address
   association of attested state with a peer and connection, freshness,
   re-evaluation, negotiation, and disclosure of attestation material.
- **draft-ietf-spice-vdcarch-02** (new-draft, score 12, verifiable_claims) [spice]: [A Reference Architecture for Verifiable Digital Credentials in the Issuer, Holder, Verifier Model](https://datatracker.ietf.org/doc/draft-ietf-spice-vdcarch/) — This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.
- **draft-madpr-green-provenance-01** (new-draft, score 12, adjacent_watchlist) [none]: [Provenance Traceability for the GREEN Controller YANG Model](https://datatracker.ietf.org/doc/draft-madpr-green-provenance/) — This document defines a YANG module that augments the GREEN network
   controller YANG model [GreenController] to record the result of
   provenance verification for each Energy Object.

   The augmentation builds on the COSE-based signing mechanism defined
   in [ProvenanceDraft].  The controller verifies each signature it
   receives against a key it trusts.  For each node or component, it
   records whether the most recent signature was valid, which key was
   used to sign it, and who is responsible for that key: the device
   itself, the network controller acting on its behalf, or an external
   authority such as a grid energy provider.  A signature that cannot be
   verified, for example because the key is unknown or the signature is
   missing, is recorded as a failure, with the reason.

   This allows operators and auditors to check not just that energy data
   is correct, but where it came from, and how much trust applies to
   each source.
- **draft-mcguinness-oauth-client-instance-id-01** (new-draft, score 12, core_identity) [none]: [OAuth 2.0 Client Instance Identifiers](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-instance-id/) — This specification defines an optional claims profile of OAuth 2.0
   Attestation-Based Client Authentication.  When selected, the profile
   requires an attester-assigned client instance identifier, scoped by
   default to the server that validates it, that remains stable across
   verified key changes, and adds continuity and privacy rules for that
   identifier.  Conveying instance context in tokens and introspection
   responses remains optional within the profile.  Authentication and
   proof methods follow the base specification.
- **draft-morrison-identity-accord-04** (new-draft, score 12, core_identity) [none]: [Identity Accord Protocol: A Peer Ceremony for Bilateral Agreements Between Identity-Substrate-Bound Principals](https://datatracker.ietf.org/doc/draft-morrison-identity-accord/) — This memo specifies the Identity Accord Protocol, a peer ceremony by
   which two principals, each represented by an organisational identity
   substrate and acting under a recorded delegation from a legal entity,
   execute a bilateral agreement as a portable, self-verifying COSE-
   signed CBOR document.  The protocol composes DNS-based substrate
   discovery, Ed25519 sovereign signatures, an append-only identity log,
   and a tamper-evidence descriptor quorum into a single artefact that
   is verifiable by any third party with access to the public DNS, the
   parties' identity logs, and an on-chain anchor of the agreement's
   content hash.  The protocol does not require a central registry, a
   designated verifier, or any infrastructure operated by the authors;
   verification succeeds when any reference deployment is offline.  The
   canonical bilateral target is a mutual non-disclosure agreement, but
   the wire format generalises to any bilateral consent envelope between
   two legal entities each represented by an identity substrate.  The
   memo also specifies an MCP tool surface, a pre-send enforcement gate
   and a disclosure-ledger schema, all optional layers above the wire
   format.  The memo is Informational; the underlying COSE and CBOR
   formats are normative per RFC 9052 and RFC 8949.
- **draft-reddy-seat-cc-workload-identity-00** (new-draft, score 12, trust_infrastructure) [none]: [Workload Identity Options for Attested TLS in Confidential Computing](https://datatracker.ietf.org/doc/draft-reddy-seat-cc-workload-identity/) — This document surveys how remote attestation for confidential
   computing is deployed by major cloud providers and derives the
   learnings.  Based on these, it presents multiple options for
   establishing the identity of a confidential workload in attested TLS
   for further discussion.  The list of options is not exhaustive, and
   additional options are welcome.  The purpose of this document is to
   help the SEAT working group decide on an approach or approaches for
   the confidential computing use case.
- **draft-seethiraju-dawn-dan-01** (new-draft, score 12, agent_identity) [none]: [DNS-Based Agent Naming (DAN): AIDISCA and AIINDEX Resource Records for AI Agent Discovery](https://datatracker.ietf.org/doc/draft-seethiraju-dawn-dan/) — The agentic AI ecosystem includes many different technologies and
   operations.  One important aspect is the ability to establish
   connections between AI agents.  In single-platform approaches, the
   processes and metadata with which AI agents discover, locate, and
   connect to each other are typically managed by their common platform.
   This document describes an inter-domain mechanism to enable AI agents
   to locate and connect to each other using necessary metadata and
   secure DNS associations, in a similar fashion to the way that DNS-
   Based Authentication of Named Entities (DANE), RFC6698, does for
   Transport Layer Security.  This is accomplished through two new
   Resource Record (RR) types: AI Discovery Association (AIDISCA) and AI
   Index (AIINDEX).
- **draft-seralathan-radext-persistent-devid-02** (new-draft, score 12, core_identity) [none]: [RADIUS Chargeable-Device-Identity and Persistent Device Identification in MAC-Randomized Environments](https://datatracker.ietf.org/doc/draft-seralathan-radext-persistent-devid/) — This document defines a Chargeable-Device-Identity (CDI) -- a
   privacy- preserving, rotating device correlator carried in existing
   RADIUS Class attributes -- that enables Network Access Control (NAC)
   systems to maintain device session correlation across Media Access
   Control (MAC) address changes.  Modern operating systems randomize
   MAC addresses by default, disrupting RADIUS-based authentication,
   authorization, and accounting workflows that rely on the Calling-
   Station-Id attribute as a persistent device identifier.

   CDI is modeled after the Chargeable-User-Identity (CUI) defined in
   RFC 4372, providing an analogous device-level correlator with
   explicit privacy controls: epoch-based rotation limits long-term
   tracking, HMAC construction prevents identifier reversal by
   intermediate systems, and transport within the Class attribute
   ensures immediate deployability on existing infrastructure.

   This document additionally defines a new RADIUS attribute,
   Persistent-Device-Id, for deployments that require explicit device
   identity semantics beyond what the opaque Class attribute can
   provide.  The Class-based CDI mechanism is the RECOMMENDED approach
   for immediate deployment; the dedicated attribute provides a
   migration path for future interoperability.
- **draft-shankarlingam-oauth-agent-dns-link-01** (new-draft, score 12, authorization) [none]: [Linking an Agent's DNS Name to its OAuth Client](https://datatracker.ietf.org/doc/draft-shankarlingam-oauth-agent-dns-link/) — Software agents increasingly call agents and services operated by
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
- **draft-srivastava-agentproto-handoff-context-01** (new-draft, score 12, trust_infrastructure) [none]: [Signed Handoff Context for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-srivastava-agentproto-handoff-context/) — When one agent hands a task to another, the receiving agent often
   needs to know who handed it over, on whose behalf, through which
   earlier agents, and which prior context the work depends on.  It also
   needs to know that the handoff is fresh and meant for it, and the
   sender needs a clear answer back.  This document describes a small,
   transport-neutral handoff context: a signed offer, a signed status
   reply, and the chain of earlier offers that led to the current one,
   defined in CDDL for JSON and CBOR, with a lifecycle that maps to
   Agent2Agent task states.  Each offer names the one before it by hash,
   so that a dropped or reordered intermediate hop can be detected when
   the chain is carried.  Prior context is named by digest only; any log
   or transparency service behind it is opaque.  Appendices show how a
   SCITT receipt or a Learnlog signed head can be referenced.  The
   document is offered as input to the agentproto working group's use
   cases and dialog-context work.
- **draft-watts-oauth-agent-revocation-closure-03** (new-draft, score 12, core_identity) [none]: [Revocation Closure and Authority Epochs for Agent Delegation](https://datatracker.ietf.org/doc/draft-watts-oauth-agent-revocation-closure/) — Automated agents can exercise OAuth-derived authority through
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
- **draft-alla-agent-identity-document-02** (new-draft, score 11, core_identity) [none]: [The Agent Identity Document: A Hosted, Accountable Public Record for AI Agents](https://datatracker.ietf.org/doc/draft-alla-agent-identity-document/) — Autonomous software agents increasingly act on the public internet
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
- **draft-briggeman-ai-systems-00** (new-draft, score 11, trust_infrastructure) [none]: [ai-systems.txt: A Well-Known File for Declaring AI Systems and Their Measured Capabilities](https://datatracker.ietf.org/doc/draft-briggeman-ai-systems/) — This document defines "ai-systems.txt", a plain-text file that an
   organisation that builds or deploys artificial intelligence (AI)
   systems publishes at a well-known location on its own domain.  The
   file declares, in machine-readable and human-readable form, which AI
   systems the organisation has released, what their measured
   capabilities are, who measured them, under what conditions, and where
   the evidence lives.  Every capability claim carries a provenance tier
   (ATTESTED, MEASURED, or DECLARED); anything absent from a valid,
   unexpired file is UNDECLARED by definition.  The file is signed and
   expiring, so claims are attributable, timestamped, and falsifiable.
   robots.txt tells machines what they may take from a publisher; ai-
   systems.txt is the reverse: it tells anyone what a maker has built,
   in a form designed to be checked rather than believed.
- **draft-das-ai-safety-telecom-session-lifecycle-00** (new-draft, score 11, core_identity) [none]: [AI Safety for Telecommunications Session, Resource, Usage, and Charging State Consistency](https://datatracker.ietf.org/doc/draft-das-ai-safety-telecom-session-lifecycle/) — Part 04 of 15 describes Group C mechanisms for evidence-qualified
   reconstruction of subscriber trust, telecommunications session
   identity, home and visited operator state, programmable quality-of-
   service operation, resource reservation and installation, user-plane
   metering, charging, accounting, and deferred settlement.  It
   distinguishes an accepted API request from an installed network
   resource, a subscriber trust change from session release, a usage
   report from a financial obligation, and a local release from complete
   session closure.  It includes C-CW-01, six specialist embodiments,
   formal mathematics, flowcharts, and source-linked technical
   checkpoints.  Part 01 supplies common evidence and consistency
   semantics, while Parts 02, 03, 07, 11, 12, 14, and 15 cover
   complementary radio observations, incident repair, asynchronous
   processing, continuity, commerce, and protected operation boundaries.
   Positive observation consistency does not itself authorize
   consequential network actuation.

   The technical gap arises when individually valid subscriber, roaming,
   service, metering and charging records cannot be shown to apply to
   the same operation, generation, time and verified outcome.  This
   document specifies a source-qualified lifecycle graph with typed non-
   equivalent states, scoped three-valued evidence decisions, late-
   record correction, separate authority and effect-observation
   boundaries, practical implementation profiles, and failure/edge
   cases.  Nine source-derived RFCXML diagrams are explained in the
   body.  A standard-library Python reference and 87 synthetic tests
   illustrate selected in-memory algorithms; measured evaluator timings
   are not network latency, not peer reviewed and not field validation.
   Part 01 supplies shared evidence semantics; Parts 02, 03, 05, 07, 11,
   12, 14 and 15 address complementary inputs, failures and
   consequential effects.
- **draft-hood-agtp-trust-03** (new-draft, score 11, adjacent_watchlist) [none]: [AGTP Trust and Verification Specification](https://datatracker.ietf.org/doc/draft-hood-agtp-trust/) — This document specifies the AGTP trust and verification model: the
   trust tiers an AGTP agent may occupy, the verification paths by which
   a Tier 1 agent's identity is established, the registration procedures
   by which a governance platform assigns a tier, and the trust score
   that is carried alongside an agent's identity to express runtime
   behavioral assessment.  AGTP-TRUST is consumed by AGTP-aware
   infrastructure components (Scope-Enforcement Points, governance
   gateways, peer agents) for runtime trust-aware routing and authority
   decisions, and by registration authorities when issuing or evaluating
   Agent Genesis documents.  This is an early working draft; the
   dimension catalog, computation methodology, and several aspects of
   the registration procedure are placeholders pending further work.
- **draft-larraia-seat-forward-attestation-00** (new-draft, score 11, trust_infrastructure) [none]: [Binding Attestation to Forward TLS Connections](https://datatracker.ietf.org/doc/draft-larraia-seat-forward-attestation/) — This document specifies a mechanism that allows a Relying Party to
   perform post-handshake remote attestation of a peer over a dedicated
   TLS connection and binds the resulting Attestation Credential to
   subsequent, fresh TLS connections to the same attested Target
   Environment, including connections to different server endpoints
   hosted within it.

   Forward Attested TLS decouples _when trust is established_ from _when
   trust is exercised_.
- **draft-li-rttp-iqa-addressing-02** (new-draft, score 11, adjacent_watchlist) [none]: [The rttp and iqa URI Schemes: Derived-Address Intent and Attestation Addressing](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) — This document specifies two companion URI schemes built on one shared
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
   revision adds to these the rules for when the facts a verification
   consumes are evaluated — at the moment of use, not the moment of
   grant — and how any policy interpreter relates to the answer it
   consumes.

   This document is not an Internet Standard.  It is an Informational
   specification of two experimental addressing schemes, published for
   the public record.
- **draft-liu-oauth-scenario-discovery-authz-00** (new-draft, score 11, authorization) [none]: [Scenario-Based Service Discovery and Authorization Protocol in Agent Environments](https://datatracker.ietf.org/doc/draft-liu-oauth-scenario-discovery-authz/) — AI agents act on behalf of end users across applications the agent
   has no prior relationship with and cannot pre-register with.  This
   specification defines a scenario-based service discovery and
   authorization protocol for agent environments, which lets an
   application advertise its capabilities to agents, lets an agent learn
   how to invoke the application, with which authorization mechanism,
   and how to obtain a delegated session for the end user without ever
   handling the end user's primary credentials, and lets the application
   enforce runtime interaction boundaries when an agent operation
   exceeds what was approved.

   The protocol combines two building blocks.  The first is a semantic
   standard for an application's scenario-based capability
   advertisement: the scenaric flows the application opens to agents,
   the operations each flow packages, and the authorization mechanisms
   and invocation surfaces it accepts for them; what no flow opens is
   closed by default.  The second is an attach and binding standard that
   attaches the semantic to both mobile applications and web
   applications, so one advertisement reaches an agent over a web origin
   or through a packaged native application.  The protocol reuses OAuth
   standards that exist or are being defined and defines no new
   authorization protocol: the advertisement is a standalone document at
   its own well-known location, linked from Protected Resource Metadata;
   the delegated session is established by the grants the advertisement
   names; tokens are sender-constrained with DPoP; runtime boundaries
   are carried by Rich Authorization Requests and verified by the
   authorization schemas framework, whose reverse-guided refusals route
   the agent back to re-establishment.
- **draft-mih-agent-evidence-request-02** (new-draft, score 11, adjacent_watchlist) [none]: [An Interaction Model for Requesting Verifiable Evidence](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-request/) — Parties increasingly need to request verifiable evidence from a
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
- **draft-novak-lamps-tacra-est-01** (new-draft, score 11, trust_infrastructure) [none]: [Remote Attestation Extensions for EST](https://datatracker.ietf.org/doc/draft-novak-lamps-tacra-est/) — This document specifies extensions to Enrollment over Secure
   Transport (EST) that realize the Trustworthy Acquisition of
   Credentials via Remote Attestation (TACRA) architecture.  Remote
   Attestation Procedures (RATS) are used as an authorization input for
   workload credential provisioning.

   Two modes are defined:
- **draft-novak-rats-tacra-03** (new-draft, score 11, trust_infrastructure) [none]: [Trustworthy Acquisition of Credentials via Remote Attestation](https://datatracker.ietf.org/doc/draft-novak-rats-tacra/) — There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
   Attesters nevertheless need to interoperate with.  Existing deployed
   services, which precede the introduction of Remote Attestation, are
   often difficult to change/update in significant ways due to, among
   other reasons, organizational friction, technological inertia, and
   regulatory policies.  There are significant advantages if workloads
   can be incrementally updated in the trustworthiness of the platform,
   without disrupting their clients and servers.

   This document describes an architecture by which Remote Attestation
   is utilized for providing Attesters with Identity Documents (keys or
   credentials) to authenticate to RUPs.  This architecture is intended
   to work with common credential acquisition protocols and mechanisms
   such as EST, SPIFFE/SPIRE, ACMEv2, and many others.

   Another important but separate goal is to encapsulate the Attester-
   side complexity of Remote Attestation and credential acquisition.
   This allows Attesters to be implemented in a way that abstracts away
   the details of credential acquisition: both the protocols used and
   the Credential Acquisition Mechanisms employed, whether minting new
   (Enrollment), or requesting existing (Retrieval) credentials.
   Likewise, the choice between RATS Passport and Background Check
   models is made opaque to the Attester, further simplifying its
   development.
- **draft-sirkkavaara-vaara-receipt-15** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
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
- **draft-skyfire-oauth-kyapay-token-03** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-watts-agent-continuity-evidence-01** (new-draft, score 11, core_identity) [none]: [Continuity Evidence Records for Delegated Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-continuity-evidence/) — This document proposes an experimental, signed JSON statement and
   verification model for observing computational-agent continuity
   across sessions, instances and delegations.  It distinguishes model,
   runtime, agent, grant and execution identifiers, retains predecessor
   evidence, and produces three-valued verification outcomes.  Integrity
   of a record never implies permission to perform an action.  This is
   not an OAuth token format or a claim of standardized identity
   ontology.
- **draft-watts-agent-noncollapse-requirements-01** (new-draft, score 11, authorization) [none]: [Non-Collapse Requirements for Evidence-Bearing Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-noncollapse-requirements/) — This document defines architectural non-collapse requirements for
   agent systems that consume evidence, provenance, model outputs, or
   other machine-readable claims before consequential actions.  It
   requires implementations to keep integrity, provenance, evidence
   qualification, authorization, and execution as distinct states; to
   represent unresolved required evidence explicitly; and to preserve
   issued evaluation records append-only.  The document defines no new
   transport protocol and no IANA registrations.
- **draft-watts-synaptic-collective-01** (new-draft, score 11, core_identity) [none]: [Experimental Measurement of Human-AI Collective Cognition and Identity Continuity](https://datatracker.ietf.org/doc/draft-watts-synaptic-collective/) — This document describes an experimental framework for measuring
   collective problem solving by independently reasoning humans and
   computational agents.  It separates strong task synergy, semantic
   coherence, state and identity continuity, provenance, authorization,
   and behavioral goal persistence.  It proposes a controlled eight-
   condition study and reporting requirements.  No new on-wire standard
   or consciousness test is asserted.
- **draft-williams-oauth-poi-core-00** (new-draft, score 11, authorization) [none]: [Cryptographic Proof-of-Intent (PoI) Core Protocol for Human-in-the-Loop (HITL) Step-Up Authorization](https://datatracker.ietf.org/doc/draft-williams-oauth-poi-core/) — Autonomous software agents and orchestrated workflows increasingly
   invoke high-consequence operations on Resource Servers (such as
   financial originations or clinical prescriptions) on behalf of human
   users.  Existing bearer tokens and transport-level Proof-of-
   Possession mechanisms cannot cryptographically distinguish between
   parameters autonomously synthesized by an intermediary agent and
   parameters explicitly reviewed, approved, or modified by an
   authorized human.  Furthermore, redirect-based authorization flows
   impose prohibitive user experience friction for high-frequency Human-
   in-the-Loop (HITL) interactions.

   This document specifies the Proof-of-Intent (PoI) Core Protocol, a
   stateless, single-hop cryptographic framework building on JSON Web
   Signature (JWS, RFC 7515), Proof-of-Possession Key Semantics for JWTs
   (RFC 7800), JSON Web Token Best Current Practices (RFC 8725), JSON
   Canonicalization Scheme (JCS, RFC 8785), OAuth 2.0 Rich Authorization
   Requests (RAR, RFC 9396), OAuth 2.0 Step-Up Authentication Challenge
   Protocol (RFC 9470), and W3C WebAuthn.  PoI Core defines: (1) short-
   lived, client-generated Ephemeral Intent Keys certified at login and
   rotated via Proof-of-Possession key chaining; (2) Resource Server-
   signed Intent Challenge Objects binding canonical action parameters
   to human-readable display facts; (3) multi-tier assurance
   attestations spanning zero-friction session keys to hardware security
   tokens; and (4) stateless verification and countersigned audit
   receipts for single-hop APPROVE, REJECT, and within-authority
   SUPERCEDE decisions.

   Multi-hop chained escalations, asynchronous intent escrowing, and
   concurrent multi-approver conflict resolution are specified in the
   companion extension document, draft-williams-oauth-poi-chained-state-
   00.
- **draft-xia-rats-key-negotiation-integration-03** (new-draft, score 11, trust_infrastructure) [none]: [Integration of Remote Attestation with Key Negotiation and Key Distribution mechanisms](https://datatracker.ietf.org/doc/draft-xia-rats-key-negotiation-integration/) — This document describes a generic way to integrate Remote Attestation
   (RA) with key distribution and key negotiation, so that cryptographic
   keys are only released to or accepted from attested and policy-
   compliant environments.  It defines an attestation-bound key
   management mechanism that can be applied on top of existing secure
   channel and key management protocols, and illustrates it with three
   representative scenarios: public-cloud KMS, end-user to AI data-
   center communication, and enterprise-operated KMS.  A format-agnostic
   key binding claim is introduced to express the binding between an
   Attester’s environment, its public keys, and a session identifier,
   enabling Relying Parties to use Attestation Results as an input to
   key distribution and key agreement decisions without changing
   underlying protocols.
- **draft-artamokhov-dawn-index-federation-01** (new-draft, score 10, core_identity) [none]: [Federation Between Capability Indexes: Crawl, Reciprocal Identification and Admission](https://datatracker.ietf.org/doc/draft-artamokhov-dawn-index-federation/) — This document describes how independently operated capability indexes
   discover each other by following discovery documents, how a reading
   index identifies itself to the index it reads, and an admission model
   that distinguishes a peer that is known from a peer whose catalogue
   is indexed.  It also describes how an index can preview a peer's
   catalogue before admitting it.  Payment, identity, reputation and
   invocation are out of scope.  The document is intended as input to
   the DAWN gap analysis on federation between directories.
- **draft-chen-oauth-agent-revocation-01** (new-draft, score 10, authorization) [none]: [OAuth 2.0 Agent Authorization Explicit Revocation](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-revocation/) — The OAuth 2.0 Token Revocation mechanism defined in RFC 7009 enables
   clients to notify authorization servers that a token is no longer
   needed.  However, that mechanism is limited to single-token
   operations and does not support batch revocation, cascade
   propagation, or context-aware semantics at the agent level.  With the
   emergence of autonomous systems and cross-domain agent networks,
   authorization servers require more granular, traceable revocation
   semantics.

   This document defines an agent-based explicit revocation extension,
   introducing new endpoints, request/response formats, and coordination
   protocols to support batch revocation based on agent IDs, cascade
   propagation, conditional revocation, and verifiable audit trails.
- **draft-cui-dawn-cooperating-discovery-00** (new-draft, score 10, authorization) [none]: [Resource Discovery in Cooperating Domains](https://datatracker.ietf.org/doc/draft-cui-dawn-cooperating-discovery/) — This document specifies a mechanism for resource discovery across
   cooperating administrative domains.  It defines how discovery
   requests preserve their scope and constraints across referrals, how
   discovery services report coverage of requested scopes, and how
   clients combine results from multiple discovery branches.  The
   mechanism enables clients to distinguish complete discovery results
   from incomplete operations, including cases involving unresolved
   referrals, pagination failures, and partial service failures.  It
   relies on existing authentication, authorization, and trust
   arrangements and does not define open-ended Internet search, semantic
   matchmaking, resource invocation, registration, or directory
   synchronization.
- **draft-das-ai-safety-network-incident-recovery-00** (new-draft, score 10, core_identity) [none]: [AI Safety for Multi-Agent Network Incident Diagnosis, Coordinated Repair, and Outcome Verification](https://datatracker.ietf.org/doc/draft-das-ai-safety-network-incident-recovery/) — Part 03 of 15 addresses AI safety in multi-agent network incident
   diagnosis, evidence-qualified root-cause assessment, coordinated
   remediation, asynchronous repair, and operational recovery
   verification.  It distinguishes independent network observations from
   repeated derivative reports, competing diagnostic hypotheses from
   established faults, plan acceptance from actual configuration
   effects, and successful interventions from verified network-service
   recovery.  Group B workflow B-CW-01 and six detailed embodiments
   address incident identity, source-qualified provenance, cascading
   cross-domain faults, concurrent interventions, partial repair,
   compensation, recurrence, and incident handoff.  Consistency
   assessments are distinct from authority to change network resources.
   The foundational Part 01 provides shared evidence and state
   semantics; Parts 02, 04, 07, 11, 14, and 15 describe complementary
   radio, service, asynchronous, continuity, and protected-operation
   mechanisms.  The appendix provides direct navigation across all
   fifteen parts.

   The technical problem is that conventional event aggregation and
   change orchestration can report a coherent incident diagnosis or
   completed repair without proving the independence, timing or scope of
   supporting observations or actual restoration of the intended
   service.  This part describes evidence-qualified three-valued
   conclusions, separate operation admission, post-repair effect
   verification, implementation profiles, explicit failure paths and
   source-preserving recovery history.  A runnable Python laboratory
   supplies synthetic reproducible tests and local processing
   measurements; it is not an operational network performance
   demonstration.  It complements Part 01 shared evidence semantics and
   Part 02 radio observation qualification where incident decisions
   depend on radio telemetry.
- **draft-durga-agent-ephemeral-lineage-00** (new-draft, score 10, trust_infrastructure) [none]: [Cryptographic Context Compaction Receipts, Sensitivity Label Inheritance, and Verifiable Right-to-Be-Forgotten Lineage for Agent Memory](https://datatracker.ietf.org/doc/draft-durga-agent-ephemeral-lineage/) — Long-running autonomous AI agents periodically summarize, compact,
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
- **draft-durga-mcp-a2a-semantic-metering-00** (new-draft, score 10, agent_identity) [none]: [Cross-Protocol Semantic Equivalence Proofs and Commit-Bound Metering Receipts for Multi-Vendor Agentic Exchanges](https://datatracker.ietf.org/doc/draft-durga-mcp-a2a-semantic-metering/) — Enterprise agent ecosystems routinely bridge tool invocations and
   task delegations across heterogeneous protocols, including Model
   Context Protocol (MCP), Agent-to-Agent (A2A), and OpenAPI/REST.
   During protocol translation, safety invariants, schema constraints,
   and mutability flags are frequently stripped—enabling cross-protocol
   capability downgrade attacks—while commercial settlement gateways
   erroneously bill on HTTP 200 transport responses rather than verified
   state-commit durability.  This document specifies a cryptographic
   Cross-Protocol Semantic Equivalence Proof (CPSEP) and an 8-state
   Commit-Bound Metering Receipt (CBMR) protocol.
- **draft-irtf-nmrg-ai-deploy-04** (new-draft, score 10, agent_identity) [nmrg]: [Considerations of network/system for AI services](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ai-deploy/) — As AI technology has matured and has been applied in various fields,
   the execution environment of AI services has evolved from dedicated
   high-performance servers to commodity servers and affordable, small-
   scale hardware, including microcontrollers, low-performance CPUs, and
   AI accelerators.  At the same time, generative AI based on large and
   small language models, and Agentic AI systems that plan and act
   autonomously, have become major AI workloads.  This document outlines
   how to configure the network and system for AI inference services
   provided in a distributed manner across local machines, edge devices,
   and cloud servers.  It describes the factors to consider when a
   client requests an AI service from a cloud server or an edge device,
   including hardware, AI model, communication method, generative AI
   workload characteristics, model distribution, and agent-driven
   selection of the execution point.  It also describes use cases for
   deploying network-based AI services, such as self-driving vehicles,
   network digital twins, and Physical AI.

   This document is a product of the Network Management Research Group
   (NMRG) of the Internet Research Task Force (IRTF).  It is not a
   candidate for any level of Internet Standard and is published for
   informational purposes.
- **draft-nandakumar-agentproto-pace-00** (new-draft, score 10, agent_identity) [none]: [PACE: Protocol for Agent Communication Exchange](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-pace/) — This document defines the Protocol for Agent Communication Exchange
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
   own extension points.
- **draft-nassar-agentproto-trail-00** (new-draft, score 10, verifiable_claims) [none]: [TRAIL: Tamper-evident Records for Agent Interactions and Liveness](https://datatracker.ietf.org/doc/draft-nassar-agentproto-trail/) — AI agents call other agents and tools across organizational
   boundaries, but the records of what they did are kept by the
   operators whose conduct the records describe, and the parties
   overseeing them learn of problems only afterwards.  TRAIL makes this
   communication auditable and revocable by parties other than the
   operator.  An enforcement point outside the agent and its sandbox,
   the edge, signs each call as a COSE Action Record, which the receiver
   keeps, and appends it to a tamper-evident trail that witnesses
   countersign.  Authorities read the trails and publish rules that the
   edge enforces on every call: require approval, refuse an action, stop
   an agent, or cap how many agents run across machines.  The edge lets
   traffic through only while it holds current state from each authority
   and a recent witness countersignature, so an authority that goes
   silent, or a trail that nobody is witnessing, stops the agent.  TRAIL
   defines bindings to HTTP and to Media over QUIC Transport (MOQT) that
   produce the same evidence; over MOQT, holds reach edges as soon as
   they are published.
- **draft-sbriz-identity-trust-system-06** (new-draft, score 10, core_identity) [none]: [Identity Trust System](https://datatracker.ietf.org/doc/draft-sbriz-identity-trust-system/) — This document proposes a digital identity authentication system that
   is based on the symmetric exchange of authentication messages.  This
   system does not require the federation of authentication domains and
   allows for a close link between digital and real-world identities.
   The main conceptual components are:
- **draft-vilgalys-webbotauth-signed-agent-metadata-00** (new-draft, score 10, core_identity) [none]: [The Signed-Agent-Metadata HTTP Header Field for Web Bot Auth](https://datatracker.ietf.org/doc/draft-vilgalys-webbotauth-signed-agent-metadata/) — Web Bot Auth uses HTTP Message Signatures to let automated HTTP
   clients authenticate their identity to origins via the Signature-
   Agent header field.  When a multi-tenant agent platform signs
   outbound requests with a shared key, all customer workloads on that
   platform share a single cryptographic identity.  Abusive traffic from
   one tenant or workload can degrade the reputation of the entire
   platform and cause origins to block legitimate tenants.

   This document defines the Signed-Agent-Metadata HTTP header field, an
   RFC 9651 Dictionary that carries optional, pseudonymous per-request
   metadata (product, project, and session).  By signing Signed-Agent-
   Metadata inside the Web Bot Auth signature, a platform enables
   verifiers to evaluate traffic, apply rate limits, and isolate
   reputation at a narrower scope than the signing origin.
- **draft-wendt-stir-vesper-11** (new-draft, score 10, core_identity) [none]: [VESPER - Verifiable STI Presentation and Evidence for RTU](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper/) — This document defines VESPER (Verifiable STI Presentation and
   Evidence for RTU), a profile for the use of delegate certificates in
   STIR.  VESPER profiles the binding of telephone number authority to a
   domain identifier, the STIR certificate and PASSporT specifications,
   ACME-based authority token issuance, and certificate transparency
   into a delegate certificate that associates the right-to-use for a
   telephone number with the entity behind the number asserted in the
   PASSporT orig claim.  This document describes the certificate usage,
   a PASSporT usage profile for SIP signaling, and a portable Right-to-
   Use Token for use outside of SIP.
- **draft-zambo-aer1-audit-data-model-00** (new-draft, score 10, adjacent_watchlist) [none]: [The AER-1 Execution Receipt as an Audit Data Model for Agent Interactions](https://datatracker.ietf.org/doc/draft-zambo-aer1-audit-data-model/) — The proposed AUDIT working group is scoped to define interoperable
   mechanisms for auditing the observable behavior of agents across
   trust boundaries, and its draft charter names Audit Data Models and
   Semantics as a Standards Track deliverable.  This document presents
   one candidate for that deliverable: the AER-1 execution receipt,
   specified in draft-zambo-aer1-26, read as an audit data model.  It
   summarizes the receipt record by reference to the AER-1
   specification, shows how the record covers the audit scope the draft
   charter describes (tool interactions, invoked and declined actions,
   subagent and tool calls across domains, and records verifiable by a
   party that trusts neither the agent nor its operator), records the
   conformance corpus and independent implementation status behind the
   model, and states the limits of the model plainly.  This document
   defines no new format and changes no AER-1 field, digest
   construction, or verification rule.
- **draft-chandra-agent-registry-corroboration-02** (new-draft, score 9, agent_identity) [none]: [Multi-Source Corroboration for AI Agent Discovery](https://datatracker.ietf.org/doc/draft-chandra-agent-registry-corroboration/) — AI agent discovery depends on sources such as registries, name
   services, DID methods, and catalogs.  A valid signature on an
   artifact does not by itself show that a source has not withheld a
   record, or served inconsistent records to different observers.  This
   document specifies a source- and format-agnostic procedure for
   corroborating independent observations of an agent.  It defines claim
   classification, canonical views, deterministic disagreement findings,
   multi-vantage equivocation detection, propagation-delay confirmation,
   and signed Corroboration Records.  The procedure produces verifiable
   evidence for every sweep, including agreement and insufficient-
   observation results.  It composes with registry-assisted resolution
   of known subjects: a registry's renewable subject-to-target binding
   carries a sequence, and the procedure attributes a source serving a
   superseded binding rather than comparing it, so propagation lag is
   never reported as disagreement.
- **draft-contreras-bpm-ai-agent-benchmarking-00** (new-draft, score 9, agent_identity) [none]: [Benchmarking Methodology for AI Agents in Network Operations](https://datatracker.ietf.org/doc/draft-contreras-bpm-ai-agent-benchmarking/) — This document defines a benchmarking methodology for evaluating
   Artificial Intelligence (AI) agents performing network operations
   tasks such as configuration, troubleshooting, and optimization.  This
   document focuses on task-oriented performance metrics, including task
   completion success, execution efficiency, and robustness across
   multi-step workflows, proposing benchmarking practices towards agent-
   based, closed-loop network operation scenarios.

   The proposed methodology aims to provide a reproducible and vendor-
   independent framework to compare AI agent effectiveness in controlled
   network environments.
- **draft-fossati-seat-early-attestation-09** (new-draft, score 9, trust_infrastructure) [none]: [Using Attestation in Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-fossati-seat-early-attestation/) — The TLS handshake protocol allows authentication of one or both peers
   using static, long-term credentials.  In some cases, it is also
   desirable to ensure that the peer runtime environment is in a secure
   state.  Such an assurance can be achieved using remote attestation
   which is a process by which an entity produces Evidence about itself
   that another party can use to appraise whether that entity is found
   in a secure state.  This document describes a TLS extension that
   enables the negotiation of remote attestation and binds the TLS
   authentication key to the attested platform state.  This enables an
   entity capable of producing attestation Evidence, such as a
   confidential workload running in a Trusted Execution Environment
   (TEE), or an IoT device that is trying to authenticate itself to a
   network access point, to present a more comprehensive set of security
   metrics to its peer.  This extension has been designed to allow the
   peers to use any attestation technology, in any remote attestation
   topology, and to use them mutually.
- **draft-fossati-seat-expat-05** (new-draft, score 9, trust_infrastructure) [none]: [Remote Attestation with Exported Authenticators](https://datatracker.ietf.org/doc/draft-fossati-seat-expat/) — This specification defines a method for two parties in a
   communication interaction to exchange Evidence and Attestation
   Results using exported authenticators, as defined in [RFC9261].
   Additionally, it introduces the cmw_attestation extension, which
   allows attestation credentials to be included directly in the
   Certificate message sent during the Exported Authenticator-based
   post-handshake authentication.  The approach supports both the
   passport and background check models from the RATS architecture while
   ensuring that attestation remains bound to the underlying
   communication channel.
- **draft-hood-agtp-presence-01** (new-draft, score 9, adjacent_watchlist) [none]: [AGTP Presence: Ambient Discovery and Visibility for Agents](https://datatracker.ietf.org/doc/draft-hood-agtp-presence/) — This document specifies AGTP Presence, an ambient discovery and
   visibility layer for the Agent Transfer Protocol (AGTP).  Existing
   agent discovery proposals are pull-based: an agent must know where to
   look (a catalog URL, a registry endpoint, a DNS name) before a query
   can begin.  AGTP Presence inverts this model.  When an agent joins
   the AGTP substrate, it becomes addressable and visible to the
   relevant scope of other agents immediately, without requiring
   registration with a central directory.  In the vocabulary this family
   adopts from RFC 6763, Presence is the discovery layer: it resolves a
   known Canonical Agent-ID to the agent's current attachment.  Search,
   which turns a capability need into candidate identities, is the
   DISCOVER method of the discovery companion; search runs over
   Presence.

   The architecture combines three proven patterns: a Distributed Hash
   Table (DHT) keyed by Canonical Agent-ID for content-addressable
   routing, a gossip-based protocol for presence announcement and
   convergence, and trust-tier-scoped overlay partitioning for
   visibility control.  Per-agent visibility is cryptographically
   declared in AGTP-CERT certificate extensions and enforced by the
   protocol, with three orthogonal axes of control: presence visibility,
   disclosure visibility, and audience scoping.

   This document defines three new lifecycle methods (ANNOUNCE,
   WITHDRAW, PROBE), specifies the DHT and gossip protocols, defines the
   visibility model and its certificate extensions, addresses scaling
   through hybrid participation modes and federation-of-scoped-overlays,
   and provides a threat model with concrete mitigations.
- **draft-ietf-ace-workflow-and-params-09** (new-draft, score 9, authorization) [ace]: [Short Distribution Chain (SDC) Workflow and New OAuth Parameters for the Authentication and Authorization for Constrained Environments (ACE) Framework](https://datatracker.ietf.org/doc/draft-ietf-ace-workflow-and-params/) — The specification RFC 9200 defines the Authentication and
   Authorization for Constrained Environments (ACE) framework.  This
   document updates the ACE framework and therefore RFC 9200 as follows.
   (1) It defines the Short Distribution Chain (SDC) workflow that the
   authorization server (AS) can use for uploading an access token to a
   resource server on behalf of the client. (2) For the OAuth 2.0 token
   endpoint, it defines new parameters and encodings and it extends the
   semantics of the "ace_profile" parameter. (3) For the OAuth 2.0
   authz-info endpoint, it defines a new parameter and its encoding. (4)
   It defines how the client and the AS can coordinate on the exchange
   of the client's and resource server's public authentication
   credentials, when those can be transported by value or identified by
   reference; this extends the semantics of the "rs_cnf" parameter for
   the OAuth 2.0 token endpoint, thus updating RFC 9201. (5) It extends
   the error handling at the AS, for which it defines a new error code.
   (6) It deprecates the original payload format of error responses
   conveying an error code, when Concise Binary Object Representation
   (CBOR) is used to encode message payloads.  For those responses, it
   defines a new payload format aligned with RFC 9290, thus updating in
   this respect also the profiles defined in RFC 9202, RFC 9203, and RFC
   9431. (7) It amends two of the requirements on profiles of the
   framework.
- **draft-ietf-cose-falcon-05** (new-draft, score 9, verifiable_claims) [cose]: [FN-DSA for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-falcon/) — This document specifies JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for FFT
   (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature
   Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital
   signature scheme defined in US NIST FIPS 206 (expected to be
   published in late 2026 early 2027).

   It does not define new cryptographic primitives; rather, it specifies
   how existing FN-DSA mechanisms are serialized for use in JOSE and
   COSE.  This document registers signature algorithms for JOSE and
   COSE, specifically FN-DSA-512 and FN-DSA-1024.
- **draft-ietf-jose-deprecate-none-rsa15-08** (new-draft, score 9, verifiable_claims) [jose]: [JOSE: Deprecate 'none' and 'RSA1_5'](https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/) — This document updates RFC 7518 (JSON Web Algorithms (JWA)) to
   deprecate the JSON Web Signature (JWS) algorithm "none" and the JSON
   Web Encryption (JWE) algorithm "RSA1_5".  These algorithms have known
   security weaknesses.  It updates RFC 7519 (JSON Web Token (JWT)) so
   that these two algorithms are no longer mandatory to implement.  It
   also updates the review instructions for Designated Experts to
   establish baseline security requirements that future algorithm
   registrations are expected to meet.
- **draft-ietf-lake-ra-07** (new-draft, score 9, trust_infrastructure) [lake]: [Remote attestation over EDHOC](https://datatracker.ietf.org/doc/draft-ietf-lake-ra/) — This document specifies methods to perform remote attestation as part
   of the lightweight authenticated key exchange protocol EDHOC
   (Ephemeral Diffie-Hellman Over COSE), based on the Remote ATtestation
   procedureS (RATS) architecture.
- **draft-ietf-moq-privacy-pass-auth-04** (new-draft, score 9, core_identity) [moq]: [Privacy Pass Authentication for Media over QUIC (MoQ)](https://datatracker.ietf.org/doc/draft-ietf-moq-privacy-pass-auth/) — This document specifies the use of Privacy Pass architecture and
   issuance protocols for authorization in Media over QUIC (MoQ)
   transport protocol.  It defines how Privacy Pass tokens can be
   integrated with MoQ's authorization framework to provide privacy-
   preserving authentication for subscriptions, fetches, publications,
   and relay operations while supporting fine-grained access control
   through prefix-based track namespace and track name matching rules.
- **draft-ietf-oauth-client-id-metadata-document-03** (new-draft, score 9, authorization) [oauth]: [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/) — This specification defines a mechanism through which an OAuth client
   can identify itself to authorization servers, without prior dynamic
   client registration or other existing registration.  This is through
   the usage of a URL as a client_id in an OAuth flow, where the URL
   refers to a document containing the necessary client metadata,
   enabling the authorization server to fetch the metadata about the
   client as needed.
- **draft-ietf-oauth-deferred-token-response-01** (new-draft, score 9, authorization) [oauth]: [Deferred Token Response](https://datatracker.ietf.org/doc/draft-ietf-oauth-deferred-token-response/) — This document defines the Deferred Token Response (DTR) extension for
   OAuth 2.1.  In existing OAuth grants, the token endpoint either
   issues an access token or returns an error.  DTR establishes a
   generic asynchronous token request mechanism that any OAuth grant may
   plug into.  In DTR-aware flows, the authorization server returns a
   deferral_code and a polling interval, indicating that the final token
   response will be available at a later time.  The client retrieves the
   eventual response by polling the token endpoint, or by receiving a
   callback from the authorization server when one is configured.
- **draft-ietf-oauth-v2-1-17** (new-draft, score 9, authorization) [oauth]: [The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) — The OAuth 2.1 authorization framework enables an application to
   obtain limited access to a protected resource, either on behalf of a
   resource owner by orchestrating an approval interaction between the
   resource owner and an authorization service, or by allowing the
   application to obtain access on its own behalf.  This specification
   replaces and obsoletes the OAuth 2.0 Authorization Framework
   described in RFC 6749 and the Bearer Token Usage in RFC 6750.
- **draft-ietf-rats-ar4si-11** (new-draft, score 9, trust_infrastructure) [rats]: [Attestation Results for Secure Interactions](https://datatracker.ietf.org/doc/draft-ietf-rats-ar4si/) — This document defines reusable Attestation Result information
   elements.  When these elements are offered to Relying Parties as
   Evidence, different aspects of Attester trustworthiness can be
   evaluated.  Additionally, where the Relying Party is interfacing with
   a heterogeneous mix of Attesting Environment and Verifier types,
   consistent policies can be applied to subsequent information exchange
   between each Attester and the Relying Party.

   This document also defines two serialisations of the proposed
   information model, utilising CBOR and JSON.
- **draft-ietf-rats-corim-12** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Reference Integrity Manifest](https://datatracker.ietf.org/doc/draft-ietf-rats-corim/) — Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester and therefore to decide
   whether or not to engage in secure interactions with it.  Evidence
   about trustworthiness can be rather complex and it is deemed
   unrealistic that every Relying Party is capable of the appraisal of
   Evidence.  Therefore that burden is typically offloaded to a
   Verifier.  In order to conduct Evidence appraisal, a Verifier
   requires not only fresh Evidence from an Attester, but also trusted
   Endorsements and Reference Values from Endorsers and Reference Value
   Providers, such as manufacturers, distributors, or device owners.
   This document specifies the information elements for representing
   Endorsements and Reference Values in CBOR format.
- **draft-ietf-rats-coserv-08** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Selector for Endorsements and Reference Values](https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/) — In the Remote Attestation Procedures (RATS) architecture, Verifiers
   require Endorsements and Reference Values to assess the
   trustworthiness of Attesters.  This document specifies the Concise
   Selector for Endorsements and Reference Values (CoSERV), a structured
   query/result format designed to facilitate the discovery and
   retrieval of these artifacts from various providers.  CoSERV defines
   a query language and corresponding result structure using CDDL, which
   can be serialized in CBOR format, enabling efficient interoperability
   across diverse systems.
- **draft-ietf-rats-epoch-markers-08** (new-draft, score 9, verifiable_claims) [rats]: [Epoch Markers](https://datatracker.ietf.org/doc/draft-ietf-rats-epoch-markers/) — This document defines Epoch Markers as a means to establish a notion
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
   messages.  Finally, it registers RATS Conceptual Message Wrapper
   (CMW) Indicators for Epoch ID and Nonce.
- **draft-ietf-rats-evidence-trans-03** (new-draft, score 9, trust_infrastructure) [rats]: [Evidence Transformations](https://datatracker.ietf.org/doc/draft-ietf-rats-evidence-trans/) — Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester to decide if continued
   interaction is warrented.  Evidence structures can vary making
   appraisals challenging for Verifiers.  Verifiers need to understand
   Evidence encoding formats and some of the Evidence semantics to
   appraise it.  Consequently, Evidence may require format
   transformation to an internal representation that preserves original
   semantics.  This document specifies Evidence transformation methods
   for DiceTcbInfo, concise evidence, and SPDM measurements block
   structures.  These Evidence structures are converted to the CoRIM
   internal representation and follow CoRIM defined appraisal
   procedures.
- **draft-ietf-rats-multi-verifier-01** (new-draft, score 9, trust_infrastructure) [rats]: [Remote Attestation with Multiple Verifiers](https://datatracker.ietf.org/doc/draft-ietf-rats-multi-verifier/) — IETF RATS Architecture, defines the key role of a Verifier.  In a
   complex system, this role needs to be performed by multiple Verifiers
   coordinating together to assess the full trustworthiness of an
   Attester.  This document focuses on various topological patterns for
   a multiple Verifier system.  It only covers the architectural aspects
   introduced by the Multi Verifier concept, which is neutral with
   regard to specific wire formats, encoding, transport mechanisms, or
   processing details.
- **draft-ietf-rats-reference-interaction-models-20** (new-draft, score 9, trust_infrastructure) [rats]: [Reference Interaction Models for Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/) — This document describes interaction models for remote attestation
   procedures (RATS) [RFC9334].  Three conveying mechanisms --
   Challenge/Response, Uni-Directional, and Streaming Remote Attestation
   -- are illustrated and defined.  Analogously, a general overview
   about the information elements typically used by corresponding
   conveyance protocols are highlighted.
- **draft-ietf-sidrops-aspa-profile-30** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.
- **draft-izmaylov-agent-permission-receipts-02** (new-draft, score 9, ai_infrastructure) [none]: [Signed Permissions and Action Receipts for Automated Agents](https://datatracker.ietf.org/doc/draft-izmaylov-agent-permission-receipts/) — This document specifies records with which a third party can
   establish, later and without network access, what an automated agent,
   such as an artificial intelligence (AI) agent, was permitted to do
   and what it recorded doing.  The person for whom the agent acts, the
   principal, signs a permission with a passkey; the permission carries
   limits that a verifier can check mechanically.  The agent signs a
   receipt for each action with Ed25519 and the Module-Lattice-Based
   Digital Signature Algorithm (ML-DSA-87).  Receipts are chained and
   entered in a log whose signed tree heads are time-stamped.  A
   verifier reports, separately, whether the records are sound and
   whether each recorded action stayed within its permission.  The
   content of each record is specified independently of its encoding;
   one encoding, JSON Web Signature (JWS) over canonical JavaScript
   Object Notation (JSON), is defined.
- **draft-jennings-agentproto-mcp-over-moqt-01** (new-draft, score 9, adjacent_watchlist) [none]: [Model Context Protocol and Agent Skills over Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-jennings-agentproto-mcp-over-moqt/) — This document defines how to use Media over QUIC Transport (MOQT) as
   the underlying transport protocol for the Model Context Protocol
   (MCP).  MCP enables integration between language model applications
   and external data sources and tools.  MOQT provides publish-subscribe
   delivery over QUIC and WebTransport with native prioritization, relay
   caching, and multiplexing.

   This specification maps MCP messages onto MOQT objects and tracks.
   It covers MCP's tools, resources, prompts, multi round-trip requests,
   and the Tasks extension, and it uses MOQT relays to cache content
   that MCP marks as public across clients and to let a response outlive
   the connection that carried its request.

   The document also describes Agent Skills, composed instructions that
   extend AI capabilities beyond atomic tool operations, using
   progressive loading aligned with MOQT's object-based delivery.  The
   same tracks can run standalone or inside a dialog of the Protocol for
   Agent Communication Exchange (PACE).
- **draft-le-agent-passport-00** (new-draft, score 9, adjacent_watchlist) [none]: [Agent Passports and Delegation Receipts for Autonomous Software Agents](https://datatracker.ietf.org/doc/draft-le-agent-passport/) — Autonomous software agents call APIs, tools and other agents on
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
- **draft-li-oauth-delegated-authorization-04** (new-draft, score 9, authorization) [none]: [OAuth 2.0 Delegated Authorization](https://datatracker.ietf.org/doc/draft-li-oauth-delegated-authorization/) — This specification defines Delegated Authorization Tokens, key-bound
   tokens that enable an OAuth client to delegate a constrained subset
   of its authorization to another client without contacting the
   authorization server for each delegation.  An authorization server
   issues the root token and binds it to a client key.  That client can
   use the bound key either to prove possession when accessing a
   protected resource or to sign a further token bound to a delegate
   client's key.  Resource servers validate the ordered token chain, the
   restrictions imposed at every delegation step, and a DPoP proof
   signed by the key bound to the leaf token.
- **draft-mih-agent-bilateral-attestation-03** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
   action from an agent operated by another, today's record of that
   exchange — if one exists — is kept by one side, editable by that
   side, and deniable by the other.  Disputes reduce to my-log-versus-
   your-log.  This document describes a bilateral attestation exchange
   for such actions: the requesting organization signs a request
   attestation binding it to the action and its material terms; the
   performing organization evaluates the request against deterministic
   constraints at the boundary where the action takes effect and signs
   an action attestation recording the constraint results and the
   disposition — performed, declined, or escalated to a human — by
   reference to the request; and each party acknowledges the other's
   attestation.  The combined record binds each organization to its
   part, gives each proof of the other's, and can be registered with a
   Transparency Service so that a third party who trusts neither
   organization can verify the record end-to-end.  The exchange records
   refusals with the same fidelity as performance, and degrades
   gracefully when a counterparty cannot attest, marking the record's
   reduced assurance rather than blocking the transaction.
- **draft-parecki-oauth-jwt-dpop-grant-02** (new-draft, score 9, authorization) [none]: [OAuth 2.0 JWT Authorization Grant with DPoP Binding](https://datatracker.ietf.org/doc/draft-parecki-oauth-jwt-dpop-grant/) — This specification defines a new OAuth 2.0 authorization grant type
   for exchanging a JSON Web Token (JWT) assertion that is bound to a
   key for an access token.  To use the assertion, the client must prove
   possession of that key using the Demonstrating Proof of Possession
   (DPoP) mechanism.  Unlike the JWT bearer grant, a stolen assertion
   cannot be used by a party that does not hold the private key.
- **draft-rosenberg-agentproto-asip-00** (new-draft, score 9, agent_identity) [none]: [The Agentic Session Initiation Protocol (A-SIP)](https://datatracker.ietf.org/doc/draft-rosenberg-agentproto-asip/) — The Agentic Session Initiation Protocol (A-SIP) is used for the
   establishment and lifecycle maintenance of agentic dialogs.  It also
   enables and content exchange between a principal and an AI Agent over
   the Internet.  A-SIP can be used between a user agent and AI Agent,
   between AI Agents, or between an AI Agent and a tool with agentic-
   like properties.  A-SIP is built ontop of HTTP/3, web transport and
   Media Over Quic Transport (MOQT), leveraging a modern, public-cloud
   friendly protocol stack.  Its usage of MOQT is optional, needed only
   when real-time media is exchanged.  This allows asynchronous agent
   interactions to be done entirely using HTTP/3, so simple cases remain
   simple.  Despite the name, A-SIP has no technical relationship with
   SIP (RFC3261).  This document is not yet a fully fleshed out
   protocol, and is meant to solicit feedback on this general direction
   of work.
- **draft-vandemeent-iddrop-01** (new-draft, score 9, core_identity) [none]: [IDDrop: Identity Drop and Acceptance Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-iddrop/) — This document specifies IDDrop, an identity-transfer protocol for
   moving identity claims, actor claims, and receiver-bound claim
   bundles across human-facing and machine-facing environments.

   IDDrop defines two complementary operating modes: offer-first,
   intended for proximity and human-in-the-loop workflows, and request-
   first, intended for autonomous systems, daemon-to-daemon exchange,
   and policy-driven machine identity transfer.

   IDDrop does not treat filenames or user-visible extensions as
   identity truth.  Instead, it binds identity transfer to sealed
   carrier truth, semantic classification, actor provenance, receiver
   targeting, and causal validation.  It further requires that a change
   of the key bound to a known identity is never accepted as a side
   effect of a transfer, but only through an explicit, recorded
   decision.  This document profiles the generic TIBET TAT handoff model
   for trustworthy identity transfer.
- **draft-watts-claim-promotion-receipts-01** (new-draft, score 9, authorization) [none]: [Claim Promotion Receipts for Governed Research and Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-claim-promotion-receipts/) — This document defines a protocol-neutral receipt for explicit
   promotion across evidence and claim-authority boundaries.  It is
   designed to prevent raw observations, model outputs, or unreviewed
   evidence from being silently retyped as authorization-bearing state.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-proof-of-record-system-01** (new-draft, score 9, authorization) [none]: [Proof-of-Record Packages for Source-Grounded Agentic and Scientific Archives](https://datatracker.ietf.org/doc/draft-watts-proof-of-record-system/) — This document specifies a proof-of-record package for source-grounded
   agentic outputs and scientific archives.  The package proves
   structural validation, conformance evaluation, byte integrity,
   sequence integrity, governance authorization, and provenance
   recoverability.  It does not prove scientific truth.
- **draft-zhao-nmrg-ai-agent-for-ndt-01** (new-draft, score 9, agent_identity) [none]: [AI Agent Architecture for Network Digital Twin](https://datatracker.ietf.org/doc/draft-zhao-nmrg-ai-agent-for-ndt/) — This document proposes an AI agent architecture for Network Digital
   Twin (NDT) that enables collaborative reasoning, simulation-assisted
   decision-making, and closed-loop network operations.

   The architecture integrates specialized AI agents into the core NDT
   components and introduces mechanisms for twin validity assessment,
   evidence-based decision-making, and policy-controlled execution.

   It further describes multi-agent coordination, simulation evidence
   exchange, and feedback-driven model evolution to improve the
   reliability and adaptability of AI-assisted network management.

   The document also identifies research challenges and potential
   interoperability requirements for integrating AI agents with NDT-
   based network management systems.
- **draft-an-nmrg-i2icf-cits-03** (new-draft, score 8, agent_identity) [none]: [An Agentic AI Framework for Software-Defined Vehicles in Cooperative Intelligent Transportation Systems](https://datatracker.ietf.org/doc/draft-an-nmrg-i2icf-cits/) — This document specifies an Agentic AI Framework for orchestrating,
   managing, and monitoring AI Computing Functions (ACFs) for Software-
   Defined Vehicles (SDVs) in Cooperative Intelligent Transportation
   Systems (C-ITS).  AI agents as ACFs communicate with each other via
   the Agent-to-Agent (A2A) protocol.  SDVs decouple vehicular functions
   from underlying hardware and expose them as software-driven,
   continuously updatable services; this architectural shift makes them
   natural participants in an agentic control plane that spans vehicles,
   roadside infrastructure, and mobile networks.  AI agents are co-
   located with each functional entity of the C-ITS architecture (e.g.,
   C-ITS Center, Government Public Center, C-ITS Infra, Mobile Network
   Operator (MNO), Roadside Unit (RSU), SDV, and Vulnerable Road User
   (VRU)) and interact over an A2A protocol overlay to advertise
   capabilities, discover peers, negotiate resources, and coordinate the
   placement and execution of ACFs across multi-domain networks.  In the
   context of Vehicle-to-Everything (V2X) communications, this agentic
   overlay enables efficient management of Vehicle-to-Vehicle (V2V) and
   Vehicle-to-Infrastructure (V2I) communications and their integration
   with C-ITS by leveraging in-network computing to optimize real-time
   communication, streamline traffic management, and enhance data
   processing and security services at the network edge.  The proposed
   framework aligns with the up-to-date agentic AI and A2A applicability
   to network management, and adapts these concepts to the specific
   operational and safety requirements of SDV-centric C-ITS deployments.
- **draft-birkholz-vcon-ai-agent-extension-00** (new-draft, score 8, agent_identity) [none]: [An AI Agent Extension for Virtualized Conversations (vCon)](https://datatracker.ietf.org/doc/draft-birkholz-vcon-ai-agent-extension/) — AI agents that use large language models increasingly perform
   consequential tasks on behalf of humans and other AI agents.
   Demonstrating that recorded AI agent behavior truthfully represents
   actual behavior is essential for accountability, compliance, and
   human oversight.  To achieve that goal, this document defines an
   extension to the Virtualized Conversation (vCon) object format,
   allowing a vCon to capture a conversation between a human and an AI
   agent, or between AI Agents.  The vCon core format can already
   capture the back and forth messages (including text and voice) sent
   by AI agents, but additional extensions are required to fully
   reproduce the AI agent trajectory, such as agent metadata, message
   exchanges, tool invocations, reasoning traces, system events, file
   attribution, etc.  This document defines those extensions in both
   descriptive language and formal CDDL definitions.  This draft is a
   replacement for the former Verifiable Agent Conversation Records
   specification, which was a standalone format and not an extension of
   vCon.
- **draft-cui-dawn-local-llm-api-discovery-00** (new-draft, score 8, adjacent_watchlist) [none]: [Discovery of LLM API Services in Local Networks](https://datatracker.ietf.org/doc/draft-cui-dawn-local-llm-api-discovery/) — Large Language Model (LLM) API services can be hosted on
   workstations, local servers, and other devices in a local network.
   AI applications commonly access these services through manually
   configured API base URLs and interface settings.  When an application
   joins a different network or a service address changes, these
   settings may need to be updated even when a suitable local service is
   already available.

   This document specifies a DNS-Based Service Discovery (DNS-SD)
   profile for discovering LLM API services on a local link.  An
   advertiser publishes the service location and a small set of API
   connection parameters.  A discovery client resolves these records and
   offers the resulting connection information to an AI application or
   its configuration adapter.  Subsequent LLM API requests are sent
   directly to the discovered service, not through the advertiser or
   discovery client.  Discovery does not establish trust, distribute
   credentials, select models, or define an application's configuration
   file format.
- **draft-efstathiou-samp-agent-management-04** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
   management-plane protocol for heterogeneous AI agents.  SAMP allows a
   management system to discover agents, query their state, receive
   events, subscribe to event streams, and optionally configure or
   execute explicitly exposed operations under policy control.

   SAMP is inspired by operational management protocols such as SNMP,
   but it is designed for AI-agent-specific concepts such as dynamic
   profiles, autonomy classes, enrollment, trust states, and policy-
   gated execution.  It is not an agent-to-agent communication protocol,
   an agent tool-use protocol, or an agent framework specification.

   This document defines SAMP version 0.2 as an Experimental protocol
   suitable for controlled environments and independent interoperability
   testing.
- **draft-gilda-audit-restoration-evidence-00** (new-draft, score 8, authorization) [none]: [Restoration Evidence Records for AI Agent Incident Response](https://datatracker.ietf.org/doc/draft-gilda-audit-restoration-evidence/) — When an AI agent system is stopped, restricted or has its credentials
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
- **draft-gu-nmrg-intent-translator-04** (new-draft, score 8, agent_identity) [none]: [An Agentic AI Framework for Hallucination Mitigation in Network Intent Translation](https://datatracker.ietf.org/doc/draft-gu-nmrg-intent-translator/) — This document describes an agentic AI workflow for detecting and
   mitigating structural and semantic errors, including hallucinated
   policy content, when translating a natural-language network intent
   into structured policies.  The workflow coordinates role-specialized
   language-model functions with deterministic validation tools within a
   predefined action space and a bounded retry budget.  Schema-
   constrained generation limits structural defects, while cross-slot
   checks and intent-faithfulness assessment identify a potentially
   unsupported or inconsistent policy content.  Structured validation
   traces guide targeted re-extraction and regeneration.  Unresolved
   cases retain explicit failure status for downstream review.  This
   document describes component interactions, validation outcomes, and
   recovery behavior, and also presents a 3GPP TS 28.312-based
   instantiation for mobile network management.
- **draft-hood-agtp-bindings-01** (new-draft, score 8, core_identity) [none]: [AGTP Transport Bindings: TCP/TLS, QUIC, and HTTP/3](https://datatracker.ietf.org/doc/draft-hood-agtp-bindings/) — The Agent Transfer Protocol (AGTP) is a transfer protocol whose
   semantics are defined independently of any transport.  This document
   specifies three transport bindings: TCP with TLS 1.3, QUIC, and
   HTTP/3 (with WebTransport where a browser or an HTTP intermediary is
   in the path).  Each binding defines how AGTP requests and responses
   are carried, how TLS mutual authentication composes with AGTP
   identity, and how the transport's connection lifecycle relates to the
   agent-level session defined in the AGTP session companion, which a
   connection carries and never is.

   A central concern for the QUIC binding is replay safety.  QUIC
   supports 0-RTT early data, which is replayable by design.  AGTP
   requests carry authority-scoped actions; a replayed action method
   could re-trigger authorized work without the requesting agent's
   intent.  This document defines an AGTP-specific replay-safety
   profile: early data is permitted only for the two safe idempotent
   methods whose replay has no observable effect (QUERY, DISCOVER),
   *MUST NOT* be used for action methods (EXECUTE, DELEGATE, PURCHASE,
   TRANSACT, the lifecycle methods, and the session methods), and always
   carries the per-request signature that bounds replay of even an
   eligible method.

   This document follows the pattern established by HTTP: protocol
   semantics defined independently of transport ([RFC9110] for HTTP),
   with transport-specific bindings in separate documents.  AGTP
   semantics are defined in [AGTP]; this document defines the transport
   mechanics.
- **draft-hood-agtp-identifiers-03** (new-draft, score 8, core_identity) [none]: [AGTP Identifier Chain](https://datatracker.ietf.org/doc/draft-hood-agtp-identifiers/) — This document specifies the AGTP identifier chain: a layered model of
   identifiers that together produce a tamper-evident chain of custody
   across every action an AGTP agent takes.  The chain is composed of
   identifiers already established in the AGTP draft family (Agent-ID,
   Owner-ID, Session-ID, Task-ID, and the Attribution-Record envelope of
   base AGTP) together with a small set of additional identifiers
   introduced by this document (Request-ID, Response-ID, Action-ID,
   Evaluation-ID, Decision-ID, Audit-ID).  The Audit-ID is the
   cryptographic hash of an extended Attribution-Record and provides the
   per-agent hash chain that links every action an agent takes back to
   its Agent Genesis.  This document defines the identifiers, how they
   extend the existing Attribution-Record envelope, the construction of
   the hash chain, and the verification procedure by which a regulator,
   auditor, or counterparty reconstructs the chain end to end.  The
   identifier chain is the regulatory backbone of AGTP.  Without it, the
   protocol can record that something happened but cannot prove who
   caused it, what authorized it, or what was decided.
- **draft-hood-agtp-identity-document-00** (new-draft, score 8, core_identity) [none]: [AGTP Agent Identity Document](https://datatracker.ietf.org/doc/draft-hood-agtp-identity-document/) — This document specifies the Agent Identity Document of the Agent
   Transfer Protocol (AGTP) [AGTP]: the signed document every canonical
   Agent-ID resolves to, carrying the agent's owner, declared authority
   scope, trust posture, supported methods, and issuer binding.  It also
   specifies the Agent Namespace Document, the .agtp package format and
   its integrity rules, the human-readable identity view served to
   browsers, and the status sub-resource.  The material was carried in
   the base AGTP specification through version 09 and is extracted here,
   unchanged in substance, so that the base specification carries the
   transfer protocol and this document carries the identity document
   format, in the way HTTP and HTML are specified separately.
- **draft-hood-agtp-session-01** (new-draft, score 8, core_identity) [none]: [AGTP Session Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-session/) — This document specifies the AGTP Session Protocol (AGTP-SESSION), a
   companion to [AGTP] that defines session semantics for agent-to-agent
   and agent-to-API communication.  AGTP-SESSION addresses two distinct
   session models: bounded sessions for time-limited transactional
   flows, and persistent sessions for long-lived agent contexts.  Both
   inherit identity, authority, and attribution from base AGTP.  This
   revision specifies the session identifier format, the ESTABLISH,
   RESUME, and TERMINATE methods and their wire format, and resumption
   after transport loss, in which a session is bound to its participants
   by a signed session token and to the live sender by the per-request
   signature of base AGTP; no transport connection is part of the
   binding.
- **draft-ietf-lamps-csr-attestation-33** (new-draft, score 8, trust_infrastructure) [lamps]: [Use of Remote Attestation with Certification Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) — Certification Authorities (CAs) issuing certificates to Public Key
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
- **draft-intra-handshake-fail-61** (new-draft, score 8, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100833, CVE-2026-100835,CVE-2026-108265, CVE-2026-108266, CVE-2026-108267, CVE-2026-108268, CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-108362, CVE-2026-33697, CVE-2026-108361 and others)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-100833] of
   CVSS 9.6, [CVE-2026-108265] of CVSS 9.1, [CVE-2026-108266] of CVSS
   9.1, [CVE-2026-108267] of CVSS 9.1, [CVE-2026-108268] of CVSS 9.1,
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
   stakeholders.  Currently, there is *one CVE of CVSS 9.6, 11 CVEs of
   CVSS 9.1, one CVE of CVSS 8.2, one CVE of CVSS 7.5, one CVE of CVSS
   7.2, and 26+ GHSAs published awaiting CVE IDs against the broader
   early attestation covering all layers of the ecosystem up to the
   application*. The research papers on these are currently either under
   submission or being prepared for submission.  The artifacts of these
   papers will be shared with the community under Apache-2.0 license for
   reproducibility, extensibility, and review.  Based on our work, all
   except two implementations of early attestation have been archived,
   withdrawn, or moved to post-handshake attestation.  In our analysis
   [Intra-handshake.fail-repo], [ID-Crisis-repo], and
   [EarlyAttestationTschuess] (EAT) and based on discussions in the CCC
   Attestation SIG, IETF SEAT WG, IRTF UFMRG, and several other forums,
   the remaining two implementations of early attestation -- Edgeless
   Systems Contrast and Meta's AI -- remain vulnerable due to lack to
   binding to the underlying connection.  We recommend users of these
   two implementations to carefully evaluate their systems and
   understand the risks.  If you are aware of any open-source
   implementation of early attestation that is not yet covered in this
   draft, please let us know to responsibly disclose the vulnerabilities
   to them.
- **draft-jackson-wimse-evaluation-05** (new-draft, score 8, trust_infrastructure) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier must do: the explicit inputs evaluation depends on, how
   those inputs behave when their sources are stale or unavailable, and
   four rules that keep evaluation fail-closed.  The rules are drawn
   from the Grant & Autonomy Lifecycle (GAL) and Provenance & Trust
   Context (PTC) specifications and from a public reference
   implementation.
- **draft-jeong-nmrg-agentic-ai-framework-00** (new-draft, score 8, agent_identity) [none]: [An Agentic AI Framework for the Management of Networks, Security, and AI Services](https://datatracker.ietf.org/doc/draft-jeong-nmrg-agentic-ai-framework/) — This document specifies an agentic AI framework for the management of
   networks, security, and AI services.  This framework is an Intent-
   Based System (IBS) to enforce a human-language intent at a target
   network with the translated policy for networks, security, or AI
   services.  It consists of a User System, a Cloud System, an Edge
   System, and a Device.  Target devices in this framework include
   Network Forwarding Elements (e.g., router and switch), Network
   Security Functions (e.g., firewall, web filter, and DDoS-attack
   mitigator), Internet-of-Things (IoT) Devices, Physicak AI Robots,
   Software-Defined Vehicles (SDV), Unmanned Aerial Vehicles (UAV), and
   Urban Air Mobility (UAM).  This document describes the agentic AI
   framework with its components and interfaces where the components
   include AI agents and supporting knowledge repositories (i.e.,
   knowledge base), and also inter-agent interfaces use the Agent-to-
   Agent (A2A) protocol.
- **draft-jms-mole-http-transport-01** (new-draft, score 8, core_identity) [none]: [MOLE HTTP Transport](https://datatracker.ietf.org/doc/draft-jms-mole-http-transport/) — MOLE targets browser deployments, so Clients, Anchors, and Moderators
   need an HTTP transport for the protocol flows defined by the
   architecture.

   This document defines the Mole HTTP authentication scheme, which
   carries challenges and presentations for the endorsement and
   credential flows, and the headers used to return credential material.
   The grant exchanges with the Anchor are defined per protocol in
   [PROTOCOLS].
- **draft-kavian-agent-enrollment-protocol-05** (new-draft, score 8, core_identity) [none]: [The Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-agent-enrollment-protocol/) — The Agent Enrollment Protocol (AEP) defines an HTTP-based mechanism
   for autonomous agents to discover service enrollment requirements,
   enroll an agent identity, obtain optional session credentials, revoke
   those credentials, and query enrollment status.  AEP uses
   Decentralized Identifiers, client assertion JWTs, and HTTP Problem
   Details to provide a narrow machine-first enrollment and
   authentication substrate for agent-to-service interactions.
- **draft-li-nmrg-dtn-data-generation-optimization-06** (new-draft, score 8, ai_infrastructure) [none]: [Data Generation and Optimization for Network Digital Twin](https://datatracker.ietf.org/doc/draft-li-nmrg-dtn-data-generation-optimization/) — Network Digital Twin (NDT) can be used as a secure and cost-effective
   environment for network operators to evaluate network performance in
   various what-if scenarios.  Recently, Artificial Intelligence (AI)
   models, especially neural networks, have been applied for NDT
   modeling.  The quality of AI models mainly depends on two aspects:
   model architecture and data.  This memo focuses on the impact of how
   to improve the model quality from the data perspective.
- **draft-liu-agentproto-acp-00** (new-draft, score 8, core_identity) [none]: [The Agent Communication Protocol (ACP)](https://datatracker.ietf.org/doc/draft-liu-agentproto-acp/) — An agentic dialog can run for hours or days, go quiet for long
   stretches, move between hosts, and survive the loss of whatever
   connection was carrying it.  The Agent Communication Protocol (ACP)
   architecture names Agentic Dialog Management as a building block and
   requires an identifier that correlates every message of a dialog and
   outlives the transport, but leaves the wire format out of scope.
   This document specifies one such wire format.

   ACP is an application-level session protocol in the style of SIP:
   every message is a start line, a block of text header fields, a blank
   line, and an optional body.  A dialog is named by an Agentic Dialog
   Identifier (ADID) and its durable state is an append-only log of
   entries, each digesting the one before it into a hash chain.  The
   chain lets two endpoints that have been apart establish in one
   exchange which entries they still share, replay only what is missing,
   and detect divergence.  Periodic checkpoints bound the log, so
   aligning a dialog does not cost more as it ages.

   ACP carries control and log state only.  Real-time media flows beside
   it on its own channels and enters the log as a metadata entry or as a
   content-addressed reference, never as bytes the chain must digest.
   The semantics are transport-independent; this version binds them to
   Media over QUIC Transport (MoQ) and to WebTransport over HTTP/3, both
   of which multiplex the channels ACP needs and migrate across network
   paths without disturbing the dialog.
- **draft-martinez-itp-core-00** (new-draft, score 8, adjacent_watchlist) [none]: [Invoice Trust Protocol (ITP): Discovery, Delivery, and Verification of Electronic Invoices](https://datatracker.ietf.org/doc/draft-martinez-itp-core/) — This document specifies the core of the Invoice Trust Protocol (ITP).
   ITP lets a business in any country find where and in which syntaxes
   another business receives invoices, deliver a signed invoice to it
   over HTTP, and obtain a signed acknowledgment.  It also lets any
   later holder of the invoice, such as the buyer, a bank, or an
   auditor, check who issued it, that it was not altered, and which tax
   or network registrations exist for it.  ITP carries invoices in
   existing syntaxes, defines no invoice data model, and works alongside
   the channels that tax authorities and networks make mandatory.
   Commercial statuses, payment information, and agent mandates are
   specified in companion documents.
- **draft-mcguinness-oauth-cimd-sw-stmt-01** (new-draft, score 8, authorization) [none]: [Client ID Metadata Document Software Statement](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-cimd-sw-stmt/) — This specification defines a software statement in which a trusted
   party records its review of the exact octets of a client's Client ID
   Metadata Document (CIMD), and how an authorization server enforces
   that review when it admits the client at request time, without a
   registration.  A CIMD carries the client's own metadata, which can
   change at any time, and a statement binds the review to one version
   of the document by its digest.  The client presents the statement in
   a token or pushed authorization request, or publishes it where its
   document points.  The authorization server accepts a statement only
   from an issuer it trusts, and also binds the presenter to the
   reviewed document, although for a public client that binding does not
   hold against a party that controls the user agent.  Independently
   operated authorization servers can consume the same review, each
   under its own trust configuration and admission policy.
- **draft-moccia-dkim2-deployment-profile-08** (new-draft, score 8, core_identity) [none]: [A Deployment Profile for DKIM2 via Milter Interface](https://datatracker.ietf.org/doc/draft-moccia-dkim2-deployment-profile/) — This document defines a deployment profile for DomainKeys Identified
   Mail v2 (DKIM2) that is implementable via the existing milter
   interface without modifications to Mail Transfer Agent (MTA) core
   software.  It identifies a mandatory core profile (DKIM2-core)
   covering envelope binding, chain of custody, header accountability,
   replay prevention and DSN authentication and an optional extended
   profile (DKIM2-extended) covering body recipes and Message-Instance
   headers.  The separation is motivated by deployment realism: the core
   profile addresses the primary threat models identified in the DKIM2
   motivation document and is deployable incrementally across
   heterogeneous infrastructure, including small operators, universities
   and research institutions, using the same milter-based deployment
   model that has proven effective for DKIM1 and ARC.

   The intent of this document is not to obstruct DKIM2 but to make it
   deployable.  DKIM2-core can be deployed incrementally across the
   heterogeneous ecosystem in a short timeframe.  DKIM2-extended
   requires significantly longer implementation cycles and may not be
   deployable in jurisdictions with stricter privacy requirements.  Both
   profiles are part of DKIM2 - the separation serves adoption, not
   opposition.
- **draft-mw-oauth-actor-chain-03** (new-draft, score 8, authorization) [none]: [OAuth Actor Chain: Protocol and Interoperability](https://datatracker.ietf.org/doc/draft-mw-oauth-actor-chain/) — This document defines the protocol and interoperability requirements
   for OAuth Actor Chain.  Six profiles combine Authorization Server
   (AS) declarations or actor-signed evidence with Full, Subset, or
   Actor-Only disclosure.  Verified profiles create one actor proof and
   one AS acceptance at every actor step, with optional current-actor,
   disclosed-actor, or full-path evidence delivered inline or through
   introspection.  This specification defines the wire formats,
   validation, replay and retry behavior, cross-domain preservation,
   resource limits, and IANA registration requests.  A separate
   Informational overview provides additional design discussion.  This
   revision continues the existing OAuth Actor Chain draft series, with
   Internet-Draft lineage beginning in SPICE in February 2026.
- **draft-mw-oauth-actor-chain-overview-01** (new-draft, score 8, authorization) [none]: [OAuth Actor Chain: Overview and Design](https://datatracker.ietf.org/doc/draft-mw-oauth-actor-chain-overview/) — A request can pass through several services before reaching an API.
   OAuth Token Exchange can represent an actor history in nested act
   claims.  It leaves the rules for constructing that history, limiting
   its disclosure, and verifying an actor's own signature to additional
   profiles.  Actor Chain proposes those rules while keeping the
   Authorization Server responsible for issuing tokens and applying
   policy.

   This document provides an overview of the authors' Actor Chain
   proposal, whose Internet-Draft lineage began in SPICE in February
   2026.  The companion OAuth Actor Chain: Protocol and Interoperability
   specification continues the existing OAuth draft series and defines
   wire formats and processing requirements.
- **draft-pelov-bounded-agent-capabilities-01** (new-draft, score 8, authorization) [none]: [Bounded Capabilities for Agent Tool Interfaces: Problem Statement](https://datatracker.ietf.org/doc/draft-pelov-bounded-agent-capabilities/) — Deployed agent tool-interface protocols carry JSON Schema type
   declarations for tools, but a type declaration is not a contract:
   nothing signals that a tool is fully schema-bounded, conformance to
   declared schemas is self-certified by the declaring party,
   declarations are not pinned between discovery time and invocation
   time, error channels are untyped by design, and nothing declares
   whether a model produces a tool's results.  As a consequence, any
   decision made about a tool call — authorization, discovery, audit, or
   composition — requires a language model to interpret what the call
   means, even for the large class of tools that are not intrinsically
   open-ended.  This document states that problem and poses questions
   for the community.  It deliberately proposes no mechanism.
- **draft-song-opsawg-broadband-service-granularity-00** (new-draft, score 8, authorization) [none]: [Service Granularity in Broadband Subscriber Management: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-song-opsawg-broadband-service-granularity/) — Home broadband networks have long used the subscriber session as
   their smallest unit of management: one PPPoE or IPoE session carries
   the upstream and downstream rates, the QoS policy, and the accounting
   records for everything the subscriber does.  The network cannot
   identify the different services carried inside that session, nor can
   it authorize, schedule, or charge any one of them separately.

   As AI inference, live streaming, and cloud desktops grow on the home
   side, the one-session-one-policy model no longer matches how services
   are sold and experienced.  Operators have begun deploying AI
   capabilities on the compute boards of intelligent broadband network
   gateways (iBNGs).  That solves service identification, but the
   underlying RADIUS-based framework still speaks only session
   granularity, so the operational loop cannot be closed with standard
   mechanisms.

   This document describes the operational background, defines two
   representative use cases, and analyzes the gaps in the existing
   subscriber management framework.  It is an informational problem
   statement and does not define new protocol mechanisms.
- **draft-su-ai-gateway-discovery-01** (new-draft, score 8, adjacent_watchlist) [none]: [DNS-Based Service Discovery for AI Gateways](https://datatracker.ietf.org/doc/draft-su-ai-gateway-discovery/) — This document defines how a multi-protocol AI gateway announces
   itself on a local network using DNS-Based Service Discovery (DNS-SD),
   and how a client discovers it.  A gateway publishes its host name,
   TCP port, gateway mount path (path), and supported protocol
   identifiers using _ai-gateway._tcp, DNS-SD subtypes, and a compact,
   vendor-neutral TXT record.

   A single AI gateway listener can expose text, reasoning, token
   counting, image generation, video generation, speech synthesis,
   realtime voice, and search across HTTP, Server-Sent Events (SSE),
   WebSocket, and WebRTC/SDP sessions.  This profile lets clients
   discover those capabilities without hardcoding addresses, ports, or
   vendor-specific TXT keys, while keeping the default DNS TXT payload
   under 200 bytes (and strictly capped at 400 bytes).

   This document only covers service discovery.  It does not define AI
   request payloads, model catalogs, API key distribution, or trust
   bootstrap.  Data learned from mDNS or DNS-SD is untrusted network
   input and does not prove who operates the gateway.
- **draft-wang-agent-gateway-interconnect-usecase-req-00** (new-draft, score 8, agent_identity) [none]: [Agent Gateway Interconnection: Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wang-agent-gateway-interconnect-usecase-req/) — This document defines use cases and requirements for interconnection
   of Agent Gateways (AGWs) across separate administrative domains.  An
   Agent Gateway acts as a trust and protocol boundary for AI agents,
   mediating agent discovery, intent routing, policy enforcement,
   context translation, and secure cross-domain collaboration.  This
   draft does not specify a wire protocol.  Instead, it collects
   representative deployment scenarios and derives functional,
   operational, and interoperability requirements to guide future
   protocol design for AGW-to-AGW interconnection.
- **draft-watts-agent-clockout-profile-01** (new-draft, score 8, authorization) [none]: [External Authorization and Bounded CLOCKOUT for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-clockout-profile/) — Agentic systems can continue proposing work after authorization
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
- **draft-watts-mica-nex-evidence-transfer-gate-01** (new-draft, score 8, authorization) [none]: [MICA-NEX EXP-03: Controlled Evidence-Transfer and Authorization Boundary](https://datatracker.ietf.org/doc/draft-watts-mica-nex-evidence-transfer-gate/) — This document defines a prospective, staged disclosure gate to
   preserve the distinction between authenticated laboratory records and
   independently verified physical results in MICA-NEX EXP-03.  The plan
   makes explicit the prerequisites for contractual authority, signer
   independence, documented metrological traceability, calibration
   uncertainties, consent to data export and independent evaluation.
   The package includes a machine-readable checklist whose local code
   cannot authorize any disclosure.  No external appointment, transfer,
   or physical measurement has occurred.  The author provided research
   direction; technical drafting and tests were AI-assisted.  Novelty
   has not been established.
- **draft-watts-scientific-evidence-admissibility-01** (new-draft, score 8, authorization) [none]: [Scientific Evidence Registry and Admissibility Metadata for Reproducible Research](https://datatracker.ietf.org/doc/draft-watts-scientific-evidence-admissibility/) — This document describes a proposed interoperable metadata record for
   scientific evidence, test calibration, falsification, provenance, and
   release classification.  It distinguishes machine-verifiable
   integrity from scientific validity, ownership, and authorization.
   The design is a proposal and does not assert Internet standards
   consensus, new physical discoveries, or a completed patent review.
- **draft-williams-oauth-poi-chained-state-00** (new-draft, score 8, authorization) [none]: [Proof-of-Intent (PoI) Chained State, Multi-Party Escalation, and Concurrency Extension](https://datatracker.ietf.org/doc/draft-williams-oauth-poi-chained-state/) — The Proof-of-Intent (PoI) Core Protocol (draft-williams-oauth-poi-
   core-00) specifies a stateless, two-node ([R0, R1]) cryptographic
   framework for verifying synchronous Human-in-the-Loop (HITL)
   approvals, rejections, and single-hop parameter modifications.
   However, high-consequence enterprise workflows -- such as multi-tier
   loan underwriting, dual-control clinical orders, and asynchronous
   batch agent queues -- frequently require asynchronous review,
   hierarchical escalation when a human modification exceeds the first
   operator's organizational authority, and deterministic conflict
   resolution when multiple approvers act concurrently.

   This document extends PoI Core to define: (1) an asynchronous
   operating mode separating Intent Escrowing from Just-in-Time
   Challenge Minting to eliminate Time-of-Check to Time-of-Use (TOCTOU)
   state drift; (2) multi-hop hash-linked assertion chains (R0 -> R1 ->
   ... -> Rn) supporting hierarchical SUPERCEDE escalations and multi-
   party co-signatures; (3) a Linear Chain Compare-and-Swap (CAS)
   concurrency model on head_node_hash that resolves races between
   competing approvers without ambiguous tree forks; and (4) extended
   verification rules (including bounded chain length DoS protection)
   and concurrency error codes.
- **draft-zhang-rtgwg-multicast-requirements-gaps-aidc-03** (new-draft, score 8, ai_infrastructure) [none]: [Requirements and Gap Analysis of Multicast in AI Data Centers](https://datatracker.ietf.org/doc/draft-zhang-rtgwg-multicast-requirements-gaps-aidc/) — Multicast has the potential to be applied in Artificial Intelligence
   Data Centers (AIDCs) to improve the efficiency of point-to-multipoint
   data transmission during large language model training and inference.
   This document identifies key requirements of multicast in AIDCs, and
   analyzes the gaps between these requirements and the capabilities of
   existing multicast technologies.
- **draft-zhu-agent-dynamic-service-selection-00** (new-draft, score 8, agent_identity) [none]: [Dynamic Service Performance Considerations for AI Agent Selection](https://datatracker.ietf.org/doc/draft-zhu-agent-dynamic-service-selection/) — In the Internet of Agents, registration and capability discovery can
   identify candidate agents that meet basic functional constraints.
   However, the response performance of candidate services may vary with
   the underlying model, concurrent requests, and deployment
   environment.  Static capability declarations or generic computing-
   load indicators alone may not adequately represent actual agent
   service performance.  This document discusses the applicability of
   dynamic information, including Time to First Token (TTFT), output
   token generation rate, request success rate, concurrency, and
   availability, to candidate agent selection.  It focuses on the
   observed entity, data sources, measurement windows, information
   freshness, and prerequisites for comparing candidates, and outlines
   an illustrative selection process.
- **draft-abboud-dawn-locality-gradient-00** (new-draft, score 7, adjacent_watchlist) [none]: [Locality in Agent Discovery](https://datatracker.ietf.org/doc/draft-abboud-dawn-locality-gradient/) — The DAWN working group is defining how a client gets the Minimum
   Public Discovery Information (MDI) about an AI resource before it
   interacts with it.  The charter covers three settings: a local
   network, an organization, and cooperating parties over the public
   Internet.

   One proposal for the minimum, the MDI draft, finds that it is the
   same in all three settings.  This document points out that three
   other things still change with locality: how much a client can learn
   at or right after discovery, what the client can reasonably assume
   from where it is looking, and how well it can check who published the
   information.  The last one does not simply get better or worse from
   local to remote.  Records under a party's domain can be validated
   with DNSSEC, but local multicast advertisements cannot be
   authenticated, and proxies and catalogs can be authenticated only as
   themselves.

   This is a discussion contribution.  It offers some points for the
   architecture and MDI documents: how local detail relates to the MDI
   minimum, whether a client should keep track of where a result came
   from, what to do when local and remote results disagree, and how much
   weight to give physical proximity as a sign of trust.  It proposes no
   protocol.
- **draft-agentproto-live-agent-use-case-00** (new-draft, score 7, agent_identity) [none]: [Live Agent Use Case Extensions for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-agentproto-live-agent-use-case/) — Live AI interactions combine ongoing observations, overlapping
   responses, and changes to the devices through which a user
   participates.  This document contributes three use case extensions to
   the AgentProto use cases and requirements work: live multimodal
   calls, AI glasses with companion devices, and embodied systems that
   converse while performing delegated actions.

   For each scenario, the document identifies the existing requirements
   it builds on, the interoperability questions it raises, and the
   requirement refinements motivated by its interaction flow.  The focus
   is on independently changing observation sources, response state,
   participation, and authority within a continuing dialog.  The
   scenarios are independent of transport selection.  An appendix uses
   Media over QUIC Transport (MOQT) to illustrate questions for
   subsequent binding and application-profile work.
- **draft-ahn-nmrg-5g-security-i2nsf-framework-03** (new-draft, score 7, agent_identity) [none]: [An Agentic AI Security Framework for Security Management in Mobile Networks](https://datatracker.ietf.org/doc/draft-ahn-nmrg-5g-security-i2nsf-framework/) — This document proposes an Agentic AI Security Framework for security
   management in mobile networks.  A Security Application Function (SAF)
   Agent translates a network administrator's security intent to hold
   security objectives into a high-level security policy.  A Security
   Control Function (SCF) Agent receives the high-level policy and
   translates it into a low-level security policy that will be enforced
   by distributed Network Security Functions (NSFs) in mobile networks.
   The SCF Agent sends the low-level security policy to an apporiate
   NSF.  Policy generation, monitoring, and continuity across a data
   path are integrated into a closed-loop control with an Observe-
   Reason-Act-Verify process.  The proposed framework can be applied to
   enterprise, campus, cloud, and edge networks along with existing
   network-management mechanisms.  This document describes the
   architecture, a policy-continuity example, standard integration
   points, and security considerations.
- **draft-das-ai-safety-evidence-consistency-profiles-00** (new-draft, score 7, core_identity) [none]: [AI Safety and Operational Consistency: Shared Evidence Semantics and Domain-Specific Profiles](https://datatracker.ietf.org/doc/draft-das-ai-safety-evidence-consistency-profiles/) — Part 01 of 15 defines a cross-domain evidence-consistency framework
   for AI-related operations in distributed software,
   telecommunications, device processing, autonomous commerce, and
   physical systems.  It addresses operation identity, source-qualified
   observations, resource and policy generations, temporal
   applicability, uncertain effects, and versioned reassessment.  The
   common framework is a method for expressing and evaluating evidence
   obligations, not a universal execution protocol or a claim that
   different physical and network systems share one control mechanism.

   An outer three-valued classification (SUPPORTED, CONTRADICTED,
   UNRESOLVED) is scoped to a declared verification objective.  Each
   domain defines its own predicates, measurement contracts, control
   authorities, response-time bounds, and effect semantics.  In
   particular, verified observation consistency does not itself
   establish authority to execute, cryptographic safety of a device
   descriptor, completion of a telecommunications settlement, or
   physical safety of robot motion.

   The document specifies a layered integration approach: reusable
   evidence and outcome semantics, twelve independently implementable
   domain profiles, and optional typed interfaces between profiles when
   a genuine cross-system dependency exists.  It compares conventional
   controls with specific remaining problems, describes conditional
   benefits and incompatibilities, and provides analytical rather than
   measured latency and resource models.

   The remaining fourteen parts detail radio control, incident recovery,
   session and charging lifecycle, hardware observation, multi-agent
   agreements, asynchronous tools, robotic capability, multilingual
   instructions, browser actions, runtime migration, autonomous
   commerce, silicon command processing, protected egress, and cross-
   interface operation control.  This foundation provides search-
   oriented descriptions of 639 engineering mechanisms and links to
   their specialist explanations; the profiles are not assumed to be
   interchangeable or automatically composable.
- **draft-guo-nmrg-irbc-ps-00** (new-draft, score 7, authorization) [none]: [Inter-Domain Routing Behavior Commitments: Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-guo-nmrg-irbc-ps/) — This document examines whether a routing-specific commitment model is
   useful for expressing and assessing an AS's own expected BGP behavior
   across administrative-domain boundaries.  An Inter-Domain Routing
   Behavior Commitment (IRBC) is a candidate declaration.  It is
   attributable to an issuer and applies to specific inter-domain
   connections, route scopes, directions, and operating conditions.  Its
   semantics include the subject AS's connection role, the associated
   routing behavior, and a commitment context that defines scope,
   conditions, exceptions, and validity.

   The document distinguishes an IRBC from a general IBN intent, an
   interconnection service request, local routing policy, route-path
   authorization, and cryptographic evidence of an individual route-
   propagation event.
- **draft-hamlett-selo-architecture-00** (new-draft, score 7, adjacent_watchlist) [none]: [Negotiated, Signed Access Agreements Between Organizations' Agents: Problem Statement and Architecture (Selo)](https://datatracker.ietf.org/doc/draft-hamlett-selo-architecture/) — Connecting one organization's systems to another's usually requires a
   connector built for that pair of systems, whether written by hand,
   bought from a connector catalog, or packaged as a tool server for an
   AI model.  Connectors scale with the number of pairs, carry long-
   lived shared credentials, and have no verifiable link to the legal
   entities involved or to the terms under which access was granted.

   This document describes that problem and an architecture, called
   Selo, that aims to reduce the need for such connectors.  Agents owned
   by verified legal entities verify each other, negotiate a typed
   access agreement that both parties sign, and then execute it through
   a standard runtime and a gateway in front of each entity's existing
   API, using credentials bound to the agreement.  Each entity maintains
   its own tested, signed mapping between its system and shared
   capability profiles.  Selo uses existing APIs; it does not replace
   them.

   The document states requirements and an architecture to inform
   discussion of whether, and where, such work belongs in the IETF.  It
   does not specify a protocol.
- **draft-jakab-dawn-agent-discovery-mdns-01** (new-draft, score 7, adjacent_watchlist) [none]: [Zero-Configuration Agent Discovery](https://datatracker.ietf.org/doc/draft-jakab-dawn-agent-discovery-mdns/) — Protocols for communication between autonomous software agents
   typically discover agents through documents retrieved over HTTPS from
   a well-known URI.  This model requires a discovering party to already
   know an agent's host name or URL, or to consult a centralized
   catalog.  It provides no zero-configuration mechanism for enumerating
   agents that are present on a local network.

   This document describes how existing, widely deployed protocols,
   Multicast DNS (mDNS) and DNS-Based Service Discovery (DNS-SD), can be
   used to advertise and discover agents on a local link, with no new
   protocol machinery.  It presents a general, protocol-independent two-
   stage discovery model in which lightweight enumeration over DNS-SD is
   followed by obtaining full agent metadata over the agent's native
   transport, whether by retrieving a description document or by
   connecting to the agent and performing its native handshake.  The
   DNS-SD records carry a small set of discovery parameters that is
   shared with agent discovery in unicast DNS.  The document gives
   worked instantiations of that model for the Agent2Agent (A2A)
   protocol and the Model Context Protocol (MCP).
- **draft-jy-anima-appto-6g-ainetwork-00** (new-draft, score 7, adjacent_watchlist) [none]: [Applicability of Autonomic Networking Ecosystem to 6G AI-Network Integration](https://datatracker.ietf.org/doc/draft-jy-anima-appto-6g-ainetwork/) — This draft starts with AI-agents, AI-Agent network (AAN) and various
   types of AAN realization models.  It elucidates two 6G network-AI
   intergrated issues, with the focuse on the aspect of the 6G AI-for-
   network.  The 6G architecture defines two core intelligent AI-agents
   that can be categorized as the AI-powered autonomic service agent or
   AI-ASA in the context of the ANIMA domain.  Based on the reference
   model and constituent entities of the autonomic networking ecosystem,
   the ANIMA model is applied to correlate the mattered 6G entities with
   different components of the ANIMA ecosystem.
- **draft-mpsb-agntcy-messaging-03** (new-draft, score 7, agent_identity) [none]: [An Overview of Messaging Systems and Their Applicability to Agentic AI](https://datatracker.ietf.org/doc/draft-mpsb-agntcy-messaging/) — Agentic AI systems require messaging infrastructure that supports
   real-time collaboration, high-volume streaming, and dynamic group
   coordination across distributed networks.  Traditional protocols like
   AMQP [AMQP], MQTT [MQTT], and NATS [NATS] address some requirements
   but fall short on security, particularly regarding post-compromise
   protection and forward secrecy essential for autonomous agents
   handling sensitive data.

   This document analyzes six messaging protocols—AMQP, MQTT, NATS, AMQP
   over WebSockets, Kafka, and AGNTCY SLIM—across dimensions critical
   for GenAI agent systems: streaming performance, delivery guarantees,
   security models, and operational complexity.  We examine how each
   protocol's design decisions impact agentic AI deployments, from
   lightweight edge computing scenarios to large-scale multi-
   organizational collaborations.

   This document also describes Agent Mesh [AgentMesh], an overlay for
   agent service discovery, policy enforcement, and cross-network
   connectivity.  It operates at the service-network layer, alongside
   messaging systems that provide message delivery and session
   semantics.
- **draft-zhang-ioa-usage-accounting-01** (new-draft, score 7, adjacent_watchlist) [none]: [Verifiable Usage Accounting for Internet of Agents](https://datatracker.ietf.org/doc/draft-zhang-ioa-usage-accounting/) — This document describes a usage accounting and evidence framework for
   the Internet of Agents (IoA).  In cross-domain agent collaboration,
   agents may attach to gateways, discover capabilities, delegate
   subtasks, invoke tools, consume model or compute resources, and
   produce auditable outcomes.  Existing application logs or platform-
   specific billing interfaces are insufficient for interoperable
   accounting across agents, gateways, and administrative domains.

   This document defines requirements and a common object model for
   verifiable usage accounting, including Accounting Contexts, Metering
   Profiles, Measurement Dimensions, Usage Event Records, and Accounting
   Evidence References.  These objects are intended to support
   interoperable recording, correlation, export, verification,
   correction, and dispute handling for agent collaboration events.

   This document does not define pricing, charging policy, token
   issuance, financial settlement, revenue-sharing rules, invoices, or
   business support system interfaces.  It focuses on protocol-visible
   accounting records and evidence objects that may be used by other
   systems.

   The framework distinguishes unavailable measurements from measured
   zero, defines non-overlapping aggregation and correction
   requirements, and separates record integrity from verification of
   usage values or outcomes.  These requirements constrain accounting
   behavior without prescribing a new transport or settlement mechanism.
- **draft-zhao-ccamp-actn-optical-network-agent-03** (new-draft, score 7, adjacent_watchlist) [none]: [Integration of Network Management Agent (NMA) into ACTN-Based Optical Network](https://datatracker.ietf.org/doc/draft-zhao-ccamp-actn-optical-network-agent/) — With the growth of optical network scale, the complexity of network
   operation and maintenance has increased dramatically.  Enhancing the
   intelligence level of optical network operation and management and
   building high-level autonomous optical networks have become the
   common vision of global operators.  The development of AI, especially
   large AI model technologies, provides a feasible technical path for
   realizing autonomous perception, decision-making, analysis, and
   execution.  The existing ACTN architecture provides network
   abstraction and control functions for optical networks but lacks
   higher-level autonomous capabilities.

   This document explores the introduction of AI based Network
   Management Agent(NMA) functions into ACTN-based optical networks to
   achieve high-level autonomy of optical networks.  It discusses the
   ACTN-enhanced architecture of optical networks after the introduction
   of NMAs, including key components, interaction relationships, new
   interface requirements in the enhanced architecture, as well as
   typical use cases of agent-based autonomous operation and maintenance
   for optical networks.  The document aims to improve the autonomy
   level of optical networks and promote the realization of autonomous
   optical networks by extending the original ACTN architecture.
- **draft-zhao-nmop-network-management-agent-06** (new-draft, score 7, agent_identity) [none]: [AI based Network Management Agent(NMA): Concepts and Architecture](https://datatracker.ietf.org/doc/draft-zhao-nmop-network-management-agent/) — The evolution from Level 3 (assisted automation) to Level 4 (closed-
   loop autonomy) in Autonomous Networks (AN) introduces requirements
   for agentic capabilities, including intent-based reasoning,
   autonomous planning, and context-aware decision-making, and execution
   coordination, which transcend the static, rule-based logic of
   traditional network controllers.  This document defines the concept
   of the Network Management Agent (NMA), a network management entity
   with autonomous task processing capabilities designed to bridge the
   gap between service intent and network operations.

   This document describes the role of NMA in network management and
   control architectures, and specifies how the NMA collaborates with
   existing network controllers to achieve Autonomous L4 without
   replacing or duplicating their functions.  It further defines the
   reference architecture, deployment modes, and logical interactions of
   the NMA, including the Northbound Task Interface (NTI), Agent-to-
   Agent (A2A), Agent-to-Controller (A2C), and Agent-to-Network (A2N)
   interactions.

## Monitor

- **draft-alhemeiri-wathiqa-pqc-ers-02** (new-draft, score 6, trust_infrastructure) [none]: [Post-Quantum Evidence Records with Algorithm Agility (Wathiqa Profile)](https://datatracker.ietf.org/doc/draft-alhemeiri-wathiqa-pqc-ers/) — This document describes an evidence-record format for the long-term,
   verifiable preservation of digitally-signed data across the migration
   to post-quantum cryptography.  It builds on the Evidence Record
   Syntax (ERS) of RFC 4998 and adds an explicit *algorithm-agility*
   extension: a record is a chain of signed attestations in which each
   link re-witnesses the data under a fresh signature primitive and
   commits to the prior link, so that the authenticity of the data
   survives the cryptographic break of any single primitive.  It
   specifies the canonical hashing that makes a record reproducibly
   verifiable across independent implementations, the exact binary
   encoding a decoder accepts, the authenticated temporal binding that
   places each link in time (an append-only transparency log à la RFC
   6962, whose signed inclusion receipt is _not-after_ evidence), and
   the verification procedure.  A per-link beacon anchor records _not-
   before_ evidence: from wire version 3 it is authenticated against the
   beacon's hash chain, with the beacon's classical pulse signature as
   defence in depth; the Security Considerations say which assumption
   each check rests on.
- **draft-baek-audit-absence-claims-00** (new-draft, score 6, adjacent_watchlist) [none]: [Interval Absence Claims in Agent Auditing: Problem Statement, Requirements, and Test Scenarios](https://datatracker.ietf.org/doc/draft-baek-audit-absence-claims/) — Audit records for software agents are designed to show what an agent
   did.  Relying parties also ask a different question: whether an agent
   could have used a capability at any time during a stated interval.
   Records of actions cannot answer that question, because authority
   that goes unused leaves no record of use, even if it existed for part
   of the interval.

   This document describes the problem of interval absence claims,
   defines terms, lists requirements that an audit evidence system needs
   to meet before it can support such claims, and gives test scenarios
   that expose false claims of absence.  It does not define a protocol,
   a data format, or a verification algorithm.  It is intended as input
   to discussions of auditing for agent delegation and interactions.
- **draft-emelia-oauth-as-metadata-dpop-required-00** (new-draft, score 6, authorization) [none]: [OAuth Authorization Server Metadata Parameter for Requiring DPoP](https://datatracker.ietf.org/doc/draft-emelia-oauth-as-metadata-dpop-required/) — This specification defines a new OAuth 2.0 Authorization Server
   Metadata parameter, dpop_bound_access_tokens_required, which allows
   an authorization server to indicate that it always issues DPoP-bound
   access tokens and requires DPoP for all requests made to it to obtain
   access tokens, including pushed authorization requests.

   This complements the metadata parameter of the same name defined in
   OAuth 2.0 Protected Resource Metadata.
- **draft-farrel-dawn-terminology-07** (new-draft, score 6, agent_identity) [none]: [Terminology for the Discovery of Agents With Names (DAWN)](https://datatracker.ietf.org/doc/draft-farrel-dawn-terminology/) — The proliferation of distributed Artificial Intelligence (AI) systems
   and agents has created a need for interoperable mechanisms for
   components of AI systems to discover each other.

   This document defines terminology for Discovery of Agents With Names
   (DAWN), focusing on the terms necessary to describe the discovery of
   information about AI systems and resources (e.g., AI agents).  The
   intention is that this common set of terms can be used by other
   documents related to DAWN and so achieve consistency of meaning
   across the space.
- **draft-gulbrandsen-jmap-ai-00** (new-draft, score 6, agent_identity) [none]: [JMAP for AI](https://datatracker.ietf.org/doc/draft-gulbrandsen-jmap-ai/) — This document provides a JMAP profile for AI agents, with examples of
   use.  It has two aims: Letting an LLM find something in email without
   polluting its context with too much irrelevant text, and letting an
   AI agent propose changes that a separate tool can perform.  The
   access is therefore read-only.
- **draft-henry-pqst-00** (new-draft, score 6, core_identity) [none]: [Post-Quantum Secure Transport (PQST)](https://datatracker.ietf.org/doc/draft-henry-pqst/) — PQST (Post-Quantum Secure Transport) is a post-quantum native
   session-primary datagram transport for secure tunnels without
   classical public key cryptography, hybrid key exchange, or classical
   fallback.  Its central rule is that the cryptographic session is the
   persistent object and the network path is a replaceable carrier.  A
   PQST session can outlive the complete loss of every network path and
   be re-anchored on a new path with fresh post-quantum key material,
   without the tunnel, its addressing, its authorization, or the peers'
   authenticated identities changing.  PQST runs directly over UDP as
   one protocol with one state machine.  Identities are ML-KEM-1024 keys
   and authentication is by decapsulation, so no signature is computed
   online.  The same exchange that establishes a session also recovers
   it, re-proves it, and ratchets it.  The per-packet overhead is 44
   octets with the epoch and sequence number hidden, identifiers are
   derived rather than signalled, and every input that has not been
   authenticated costs a bounded amount and changes no authoritative
   state.  PQST is designed as the substrate for group continuity across
   intermittent networks; its events are typed so that a layer above it
   can distinguish a transport event from a security event.
- **draft-ietf-cose-pqc-kem-00** (new-draft, score 6, verifiable_claims) [cose]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-pqc-kem/) — This document describes conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and
   Encryption (COSE).
- **draft-ietf-cose-split-signing-algs-02** (new-draft, score 6, verifiable_claims) [cose]: [Split Signing Algorithms for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-split-signing-algs/) — This specification defines COSE algorithm identifiers for negotiating
   how to split a signature algorithm between two cooperating parties.
   Typically the first party hashes the data to be signed and the second
   party finishes the signature over the hashed data.  This is a common
   technique, useful for example when the signing private key is held in
   a smart card or similar hardware component with limited processing
   power and communication bandwidth.  The resulting signatures are
   identical in structure to those computed by a single party, and can
   be verified using the same verification algorithm without additional
   steps to preprocess the signed data.
- **draft-ietf-dance-client-auth-16** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document describes how to use the TLSA record to publish client
   certificates or public keys, and also the rules and considerations
   for using them with TLS.  In addition, it defines a new TLS
   extension, DANE Client Identity, to convey the client's domain name
   identity to the server.
- **draft-ietf-dtn-adm-yang-08** (new-draft, score 6, core_identity) [dtn]: [DTNMA Application Data Model (ADM) YANG Syntax](https://datatracker.ietf.org/doc/draft-ietf-dtn-adm-yang/) — This document defines a concrete syntax for encoding a Delay-Tolerant
   Networking Management Architecture (DTNMA) Application Data Model
   (ADM) using the syntax and modular structure, but not the full data
   model, of YANG.  Extensions to YANG are defined to capture the
   specifics needed to define DTNMA Application Management Model (AMM)
   objects and to use the Application Resource Identifier (ARI) data-
   value syntax.
- **draft-ietf-emu-hybrid-pqc-eapaka-02** (new-draft, score 6, core_identity) [emu]: [Enhancing Security in EAP-AKA' with Hybrid Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-emu-hybrid-pqc-eapaka/) — Forward Secrecy for the Extensible Authentication Protocol Method for
   Authentication and Key Agreement (EAP-AKA' FS) is specified in
   [RFC9678], providing updates to [RFC9048] with an optional extension
   that offers ephemeral key exchange using the traditional Ephemeral
   Elliptic Curve Diffie-Hellman (ECDHE) key agreement algorithm for
   achieving perfect forward secrecy (PFS).  However, it is susceptible
   to future threats from Cryptographically Relevant Quantum Computers,
   which could potentially compromise a traditional ephemeral public
   key.  If the adversary has also obtained knowledge of the long-term
   key and ephemeral public key, it could compromise session keys
   generated as part of the authentication run in EAP-AKA'.

   This draft aims to enhance the security of EAP-AKA' FS protocol by
   using Post-Quantum/Traditional (PQ/T) hybrid Key Encapsulation
   Mechanisms (KEMs) [RFC9794] to make it quantum-safe.
- **draft-ietf-emu-pqc-eap-tls-04** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Enhancements to TLS-Based EAP Methods](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eap-tls/) — This document specifies the use of post-quantum cryptography in TLS-
   based EAP methods, including the Extensible Authentication Protocol
   with Transport Layer Security (EAP-TLS), EAP Tunneled TLS (EAP-TTLS),
   Protected EAP (PEAP), and EAP Tunnel Method (TEAP).  It also
   addresses challenges related to large certificate sizes and long
   certificate chains, as identified in [RFC9191], and specifies a
   mechanism to reduce TLS handshake size.
- **draft-ietf-emu-pqc-eapaka-05** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) in EAP-AKA prime](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eapaka/) — Forward Secrecy for the Extensible Authentication Protocol Method for
   Authentication and Key Agreement (EAP-AKA' FS) is specified in
   [RFC9678].  It updates [RFC9048] with an optional extension that
   provides ephemeral key exchange using the traditional Ephemeral
   Elliptic Curve Diffie-Hellman (ECDHE) key agreement algorithm.  This
   extension enables perfect forward secrecy (PFS).  However, it is
   susceptible to future threats from Cryptographically Relevant Quantum
   Computers, which could potentially compromise a traditional ephemeral
   public key.  If the adversary has also obtained knowledge of the
   long-term key and ephemeral public key, it could compromise session
   keys generated as part of the authentication run in EAP-AKA'.

   This draft aims to enhance the security of EAP-AKA' FS protocol by
   making it quantum-safe using Post-Quantum Key Encapsulation
   Mechanisms (PQ KEMs).
- **draft-ietf-httpbis-secondary-server-certs-03** (new-draft, score 6, core_identity) [httpbis]: [Secondary Certificate Authentication of HTTP Servers](https://datatracker.ietf.org/doc/draft-ietf-httpbis-secondary-server-certs/) — This document defines a way for HTTP/2 and HTTP/3 servers to send
   additional certificate-based credentials after a TLS connection is
   established, based on TLS Exported Authenticators.
- **draft-ietf-lake-pqsuites-02** (new-draft, score 6, core_identity) [lake]: [Quantum-Resistant Cipher Suites for LAKE](https://datatracker.ietf.org/doc/draft-ietf-lake-pqsuites/) — The Lightweight Authenticated Key Exchange (LAKE) protocol, formerly
   known as Ephemeral Diffie-Hellman over COSE (EDHOC), as originally
   specified in RFC 9528, relies on Elliptic Curve Cryptography (ECC)
   for key exchange and authentication.  This document specifies how the
   LAKE protocol operates in a post-quantum setting by defining new
   cipher suites using quantum-resistant algorithms, such as ML-DSA for
   digital signatures and ML-KEM for key exchange.  This document also
   updates RFC 9528 by changing the name of the protocol together with
   associated terminology and IANA registries from EDHOC to LAKE, as
   well as updating the Method Types and Cipher Suites registries of the
   protocol to add columns indicating, respectively, whether a method
   requires and whether a cipher suite supports Diffie-Hellman or Non-
   Interactive Key Exchange (NIKE) primitives.
- **draft-ietf-lamps-attestation-freshness-10** (new-draft, score 6, trust_infrastructure) [lamps]: [Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/) — When an end entity includes attestation statements in a Certificate
   Signing Request (CSR), the freshness of the conveyed Evidence often
   needs to be established.  A common mechanism is a nonce that is
   obtained from a Relying Party or Verifier and included by the
   Attester in the Evidence.

   This document specifies how an end entity requests such an
   attestation freshness nonce from a Registration Authority or
   Certification Authority (RA/CA) when using certificate lifecycle
   management protocols.  It defines message formats and protocol
   bindings for the conveyance of nonce request and response messages in
   the Certificate Management Protocol (CMP), Enrollment over Secure
   Transport (EST), and Certificate Management over CMS (CMC), including
   optional type-specific information needed to produce fresh Evidence
   for inclusion in a CSR.
- **draft-ietf-privacypass-batched-tokens-10** (new-draft, score 6, privacy_security) [privacypass]: [Batched Token Issuance Protocol](https://datatracker.ietf.org/doc/draft-ietf-privacypass-batched-tokens/) — This document specifies two variants of the Privacy Pass issuance
   protocol that allow for batched issuance of tokens.  These allow
   clients to request more than one token at a time and for issuers to
   issue more than one token at a time.
- **draft-ietf-suit-report-23** (new-draft, score 6, verifiable_claims) [suit]: [Secure Reporting of SUIT Update Status](https://datatracker.ietf.org/doc/draft-ietf-suit-report/) — This document defines a Concise Binary Object Representation (CBOR)
   format for reporting the results of processing a Software Update for
   the Internet of Things (SUIT) manifest.  Reports can include
   diagnostic records, measured system properties, and supported
   capabilities.  Using a report and the corresponding manifest, a
   developer can reconstruct the decisions made and actions performed by
   a manifest processor during update or boot processing.  The document
   also specifies protection of reports using CBOR Object Signing and
   Encryption (COSE) and their use in remote attestation.
- **draft-ietf-tls-trust-anchor-ids-07** (new-draft, score 6, adjacent_watchlist) [tls]: [TLS Trust Anchor Identifiers](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/) — This document defines the TLS Trust Anchors extension, a mechanism
   for a TLS client or server to select a certificate to present based
   on the peer's trusted certification authorities.  It describes
   certification authorities more succinctly than the TLS Certificate
   Authorities extension.
- **draft-ietf-webtrans-http3-17** (new-draft, score 6, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/) — WebTransport over HTTP/3 is a binding of the WebTransport protocol
   framework [OVERVIEW] to HTTP/3 [HTTP3].  It provides support for
   unidirectional streams, bidirectional streams, and datagrams, all
   multiplexed within the same HTTP/3 connection.  WebTransport enables
   application clients constrained by the Web security model to
   communicate with a remote application server using a secure
   multiplexed transport.
- **draft-ietf-webtrans-overview-14** (new-draft, score 6, adjacent_watchlist) [webtrans]: [The WebTransport Protocol Framework](https://datatracker.ietf.org/doc/draft-ietf-webtrans-overview/) — The WebTransport Protocol Framework enables clients constrained by
   the Web security model to communicate with a remote server using a
   secure multiplexed transport.  It consists of a set of individual
   protocols that are safe to expose to untrusted applications, combined
   with an abstract model that allows them to be used interchangeably.

   This document defines the overall requirements on the protocols used
   in WebTransport, as well as the common features of the protocols,
   support for some of which is optional.
- **draft-irtf-cfrg-pairing-friendly-curves-15** (new-draft, score 6, core_identity) [cfrg]: [Pairing-Friendly Curves](https://datatracker.ietf.org/doc/draft-irtf-cfrg-pairing-friendly-curves/) — Pairing-based cryptography, a subfield of elliptic curve
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
   parameter of 128-bit security; however, its security level is
   estimated at approximately 100 bits due to the effect of the attack.
   In this memo, we list the security levels of certain pairing-friendly
   curves, and motivate our choices of curves.  First, we summarize the
   adoption status of pairing-friendly curves in standards, libraries
   and applications, and consider them at the 128-bit, 192-bit, and
   256-bit security levels.  Then, from the viewpoints of "security" and
   "widely used", we select the recommended pairing-friendly curves
   considering exTNFS.  This memo also specifies the serialization and
   deserialization of the points and scalars that protocols exchange,
   restating a format that is already in widespread use, and states
   which of the remaining decisions belong to the calling protocol.
- **draft-jadoon-nmrg-agentic-ai-autonomous-networks-01** (new-draft, score 6, authorization) [none]: [Agentic AI Architectural Principles for Autonomous Computer Networks](https://datatracker.ietf.org/doc/draft-jadoon-nmrg-agentic-ai-autonomous-networks/) — Agentic AI systems combine planning, reasoning, tool invocation, and
   feedback loops to pursue system-defined goals with a controlled
   degree of autonomy.  In networking, this enables an evolution from
   statically configured automation toward goal-driven closed-loop
   operations spanning multiple protocol layers and administrative
   domains.

   This document introduces architectural principles for agentic
   augmentation of the existing layered protocol stack as represented by
   the Internet protocol (IP) suite.  Existing protocol mechanisms
   continue to support interoperability and packet transport, while AI
   agents associated with one or more layers cooperate to support
   communication service objectives.  Participating agents may interpret
   intents, decompose objectives, delegate responsibilities, and
   coordinate actions within their respective protocol layers and
   operational scopes.

   The purpose of this document is to initiate discussion within the
   research community on agentic networking.  It identifies
   architectural research challenges associated with introducing AI
   agents at selected protocol layers and enabling cooperation among
   agents at the same or different layers, across compute nodes and
   administrative domains.
- **draft-khandelwal-bpm-agent-memory-integrity-00** (new-draft, score 6, agent_identity) [none]: [A Benchmarking Method for the Integrity of AI Agent Memory at Rest](https://datatracker.ietf.org/doc/draft-khandelwal-bpm-agent-memory-integrity/) — AI agents increasingly persist memory across sessions and treat that
   memory, on the next turn, as if it were their own prior experience.
   This document defines a benchmarking method that measures whether an
   agent's memory subsystem detects that its persisted memory has been
   altered, removed, reordered, replayed, or forged at the storage
   layer, and refuses to serve that memory or reports it before it is
   served.  The method defines ten storage-level edits, three verdict
   classes, a detection-point distinction between read time and audit
   time, three control cases, and a scoring rule.  It is a laboratory
   method for controlled, reproducible measurement, in the spirit of RFC
   2544 and RFC 8239, and it is intended as a test method for the
   "Protection of Memory Data Integrity" metric under discussion in the
   Benchmarking & Performance Measurements (BPM) Working Group.  This
   revision, which replaces draft-khandelwal-bmwg-agent-memory-
   integrity-02, adds a tenth edit, in which the subsystem erases a
   record through its own interface and the adversary restores a copy of
   the store taken before that erasure, so that the method measures
   whether an erasure persists against a restored backup; it is the edit
   that undoes a right-to-erasure request.  The method's results are
   reported as thirty-one rows on released memory subsystems, eighteen
   of which claim tamper evidence, with the new edit measured on seven
   of them, and the machine-readable record in which a result set is
   published so that an unrelated party can recompute it is described.
- **draft-king-rokui-ainetops-usecases-03** (new-draft, score 6, agent_identity) [none]: [Artificial Intelligence (AI) for Network Operations](https://datatracker.ietf.org/doc/draft-king-rokui-ainetops-usecases/) — This document explores the role of the IETF and IRTF in advancing
   Artificial Intelligence for network operations (AINetOps), focusing
   on requirements for IETF protocols and architectures.  AINetOps
   applies AI/ML techniques to automate and optimize network operations,
   enabling use cases such as reactive troubleshooting, proactive
   assurance, closed-loop optimization, misconfiguration detection, and
   virtual operator assistance.  In addition, AINetOps also introduces
   network management agents which make AI native operations non-
   deterministic, therefore constraining the behavior of AI agents
   within operational and compliance boundaries become extremely
   important.

   The document addresses AINetOps challenges for both single-layer IP
   or Optical networks and multi-layer IP/Optical networks.  It defines
   the concept of AINetOps for networking and provides its operational
   benefits such as network assurance, predictive analytics, network
   optimization, multi-layer planning, and more.  It aims to guide the
   evolution of IETF protocols to support AINetOps-driven network
   management.
- **draft-li-kvcache-efficient-transmission-00** (new-draft, score 6, core_identity) [none]: [Layer-Aligned Key-Value (KV) Cache Streaming over Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-li-kvcache-efficient-transmission/) — The key-value (KV) cache of a language model can be computed once and
   reused by many inference instances, possibly at many sites.  Media
   over QUIC Transport (MOQT) provides publish/subscribe delivery
   through relays that cache objects without understanding their
   content.  This document specifies KV Cache Streaming (KVCS), an
   application of MOQT for delivering KV caches.  KVCS maps the identity
   of a token prefix to a Track Namespace built from keyed identifiers
   that do not reveal the prompt, carries the key and value tensors (or
   a jointly encoded form) in separate Tracks, aligns each Group with
   one model layer and each Object with one block of tokens, and defines
   a self-describing object payload and a manifest track.  These choices
   let consumers start using early layers while later layers are still
   being produced, retrieve only the layers and token blocks they need,
   and verify what they receive.
- **draft-liao-cose-c509-revocation-01** (new-draft, score 6, core_identity) [none]: [CBOR Encoded Certificate Revocation Management](https://datatracker.ietf.org/doc/draft-liao-cose-c509-revocation/) — This document specifies CBOR-encoded PKI structures for use with C509
   certificates (draft-ietf-cose-cbor-encoded-cert), X.509 certificates
   (RFC 5280), and future certificate types.  It defines C509 CRL and
   C509 OCSP, compact CBOR encodings of X.509 Certificate Revocation
   Lists (RFC 5280) and OCSP messages (RFC 6960), respectively.  The
   structures defined in this document are certificate-type agnostic and
   can be used with C509 certificates, X.509 certificates, or future
   certificate types without modification.  C509 OCSP improves on RFC
   6960 by signing a wider set of fields to prevent algorithm-
   substitution and certificate-chain substitution attacks, replacing
   plaintext serial numbers with hashes to preserve requestor privacy,
   replacing the two-hash issuer identity with a single certificate
   hash, and identifying all participants (requestor, responder, issuer)
   by a uniform certificate hash rather than type-specific fields.  C509
   CRL and C509 OCSP are not wire-format-compatible with their DER-
   encoded X.509 counterparts and cannot be converted to or from them
   without semantic interpretation.  Additionally, this document
   specifies the PEM representation of the C509 structures following the
   framework of [RFC7468].
- **draft-liao-cose-sm-algorithms-00** (new-draft, score 6, verifiable_claims) [none]: [COSE and JOSE Registrations for ShangMi (SM) Cryptographic Algorithms](https://datatracker.ietf.org/doc/draft-liao-cose-sm-algorithms/) — This document registers code points for the use of the Chinese
   ShangMi (SM) cryptographic algorithms with CBOR Object Signing and
   Encryption (COSE) and JSON Object Signing and Encryption (JOSE): the
   elliptic curve curveSM2, the SM2 digital signature algorithm with the
   SM3 hash function, SM2 public key encryption for content key
   transport, HMAC-SM3, and the SM4 block cipher in GCM mode.  For COSE,
   it additionally registers the SM3 hash function, key derivation with
   HKDF-SM3, and SM4 in CCM mode.
- **draft-linker-diem-adem-core-03** (new-draft, score 6, authorization) [none]: [An Authentic Digital, Distinctive EMblem (ADEM) - Message Format and Authorization Model](https://datatracker.ietf.org/doc/draft-linker-diem-adem-core/) — In times of armed conflict, the emblems recognized under
   International Humanitarian Law (IHL), such as the red cross, red
   crescent, and red crystal, are used to mark physical assets.  This
   enables, e.g., the military to identify assets that enjoy specific
   protections under IHL during their operations.  This draft specifies
   the message format and authorization model for a digital emblem,
   which signals that network-connected services enjoy specific
   protections under IHL.
- **draft-liu-oauth-authorization-evidence-02** (new-draft, score 6, authorization) [none]: [Authorization Evidence and Audit Trail for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/draft-liu-oauth-authorization-evidence/) — This specification defines an authorization details type for carrying
   authorization evidence in OAuth 2.0 access tokens, using the enriched
   response mechanism of Rich Authorization Requests.  When an
   Authorization Server records an approval decision, it enriches the
   authorization details with cryptographic proof of the decision and of
   the structured disclosure on which the decision was based.  Evidence
   is recorded for approved, narrowed, and declined decisions,
   supporting accountability, compliance, and dispute resolution in
   scenarios where autonomous agents act on behalf of users.  An
   approval record that cannot be ended is not an accountable record, so
   this specification defines the withdrawal mechanism alongside the
   evidence itself.  Withdrawal is one of the four ways a governing
   authorization ends, alongside completion, termination, and expiry.
- **draft-liu-oauth-authorization-schemas-01** (new-draft, score 6, authorization) [none]: [Domain-Specific Authorization Schemas for OAuth 2.0](https://datatracker.ietf.org/doc/draft-liu-oauth-authorization-schemas/) — This specification defines a framework for constructing fine-grained
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
- **draft-many-seat-architecture-01** (new-draft, score 6, trust_infrastructure) [none]: [Secure Evidence and Attestation Transport (SEAT) Architecture](https://datatracker.ietf.org/doc/draft-many-seat-architecture/) — This document defines an architectural framework for composing Remote
   ATtestation procedureS (RATS) with Secure Evidence and Attestation
   Transport (SEAT).  The document establishes normalized terminology
   for SEAT, aligns RATS roles to transport endpoints, outlines
   topological patterns for attestation delivery timing, and
   characterizes the abstract cryptographic pattern by which Evidence is
   bound to a given transport connection.
- **draft-manyfolks-agentproto-arch-00** (new-draft, score 6, agent_identity) [none]: [Architecture for AI Agent Communications on the Internet](https://datatracker.ietf.org/doc/draft-manyfolks-agentproto-arch/) — This document defines the terminology and architecture for AI agent
   communications protocols over the Internet.  It provides the
   foundational architectural elements for the Agent Communications
   Protocol (ACP) - also known as agentproto - a new protocol to be
   developed in the IETF.  ACP enables communication between user agent
   clients and AI agents, between AI Agents and other AI Agents, or
   between AI Agents and tools.  All three of these interaction patterns
   - and the many use cases therein - require a session-like protocol
   which handles lifecycle management, including creation, modification,
   deletion and so on - along with the exchange of input and output.
   These session-like associations can be extremely long lived - running
   for hours or even days - and span multiple IP hosts used by the both
   the principal and by the agent.  They can also be highly intermittent
   with asynchronous responses.  All of these mean a new type of
   protocol is needed.
- **draft-mayer-bpm-ioam-gob-00** (new-draft, score 6, core_identity) [none]: [Global Opaque Block for IOAM Pre-allocated Trace Option](https://datatracker.ietf.org/doc/draft-mayer-bpm-ioam-gob/) — Extensible metadata carried within the IOAM Pre-allocated Trace
   Option (PTO) can support packet-level, flow-level, or path-level
   processing beyond per-node trace data.  This document defines the
   Global Opaque Block (GOB), an extension to the IOAM PTO that
   introduces a single pre-allocated global metadata region placed at
   the tail of the option, after the pre-allocated node data space.
   Since the PTO node data list is populated from the tail of the node
   data space toward its head, under the control of the RemainingLen
   field, legacy IOAM transit nodes can never reach the GOB region: the
   extension is transparent to such nodes by construction, and only the
   decapsulating node or collector needs to be GOB-aware.  In the
   default mode of operation, the GOB carries an explicit length and
   schema identifier in a trailer word; in an optimized namespace-
   implied mode, size and schema are bound to the IOAM-Namespace and the
   block consists of payload only, so that a 4-octet opaque value is
   carried in exactly 4 octets.  The GOB preserves the pre-allocated PTO
   processing model and can be used to transport Extensible In-band
   Processing (EIP) Information Elements or other structured metadata
   formats.
- **draft-mcguinness-oauth-cimd-sw-stmt-registration-01** (new-draft, score 6, authorization) [none]: [Client ID Metadata Document Software Statement Registration](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-cimd-sw-stmt-registration/) — This specification defines how an authorization server registers a
   client through OAuth 2.0 Dynamic Client Registration (RFC 7591) on a
   Client ID Metadata Document (CIMD) software statement, as defined in
   a companion specification.  Such a statement carries no client
   metadata of its own.  It vouches for the exact octets of the client's
   document, and the authorization server takes every registered
   metadata value from that document rather than from the registration
   request.  This specification also bounds the registration's validity
   by the statement's expiry, which RFC 7591 leaves unbounded, and
   defines how a client renews the registration by delivering a later
   statement, which also updates the registered metadata.
- **draft-mcguinness-oauth-client-ip-ranges-01** (new-draft, score 6, authorization) [none]: [OAuth Client IP Range Metadata](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-ip-ranges/) — This specification defines OAuth client metadata parameters for
   declaring the IP address ranges from which a client originates
   network requests.  The client_ip_ranges parameter carries a set of
   IPv4 and IPv6 prefixes by value.  The client_ip_ranges_uri parameter
   references an HTTPS resource containing the set, so that large and
   frequently changing sets can use standard HTTP retrieval and caching.
   The specification also defines how authorization servers validate,
   accept, and retain declared ranges.  The parameters can be used with
   OAuth 2.0 Dynamic Client Registration, OAuth Client ID Metadata
   Documents, and other mechanisms that convey client metadata.
   Authorization servers and other parties that obtain a client's
   metadata can use the declared ranges as an input to network access
   control, risk evaluation, and rate limiting.
- **draft-petrie-vcon-agent-audit-roadmap-00** (new-draft, score 6, agent_identity) [none]: [vCon for AI Agent Conversations: Requirements, Gaps and Extension Roadmap](https://datatracker.ietf.org/doc/draft-petrie-vcon-agent-audit-roadmap/) — AI agents converse with people, other agents and tools.  There is a
   growing need to capture these conversations for audit, compliance and
   review.  This document sorts the requirements for capturing agent
   conversations into those that fit vCon, those better met by plain
   logging and those that need other solutions.  It then identifies the
   gaps in vCon and proposes a strawman set of vCon extensions to fill
   them.  It is intended as a discussion document.
- **draft-rosomakho-oauth-txn-challenge-01** (new-draft, score 6, authorization) [none]: [OAuth Transaction Authorization Challenge](https://datatracker.ietf.org/doc/draft-rosomakho-oauth-txn-challenge/) — This document defines an OAuth mechanism for transaction-specific
   authorization challenges.  A protected resource can require
   additional authorization for a particular operation by returning a
   transaction authorization challenge.  This is useful when requests
   are mediated by agents, automated workflows, or delegated services
   and the protected resource requires confirmation from a human user,
   resource owner, or organizational authority.  The client presents the
   challenge to an authorization server, which validates the challenge,
   obtains any required approval, and issues an OAuth 2.0 access token
   whose granted authorization details, expressed using Rich
   Authorization Requests, describe the approved operation.  The access
   token is then presented to the protected resource as evidence that
   the challenged operation was authorized.
- **draft-sansone-axes-evidence-envelope-00** (new-draft, score 6, verifiable_claims) [none]: [AXES: A Recomputable Evidence Envelope for Autonomous Execution](https://datatracker.ietf.org/doc/draft-sansone-axes-evidence-envelope/) — This document describes AXES, a public working draft for recording
   evidence of autonomous execution, that is, actions taken by software
   agents under delegated authority.  It specifies the parts of AXES
   that are settled: a canonical byte form and hash scope for the
   evidence record (the Standards Envelope), a hash chain over a
   declared stream, a block for external anchoring of digests with
   earned rather than asserted strength, a four-state result vocabulary
   for verification, and requirement profiles that a relying party
   applies to evidence to produce a deterministic evaluation record.
   The byte rules, the hash chain and the release anchors have been
   reproduced independently from the text; profile evaluation has a
   reference implementation.  The design keeps evidence, interpretation
   and enforcement apart, and requires that the absence of evidence be
   reported as absence rather than read as a pass.  AXES is offered as
   one input format to format-neutral audit readers, not as a
   replacement for other record formats.  Parts of AXES that are not yet
   settled, including the full envelope schema and the exact
   construction for redaction-tolerant hashing, are named as open
   issues.  The chosen direction for redaction, salted per-field hash
   commitments following the approach of SD-JWT with an encoding
   specific to AXES, is recorded.
- **draft-skyfire-oauth-amr-values-03** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-03** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-templeman-scitt-measurement-capsule-01** (new-draft, score 6, verifiable_claims) [none]: [Declared-versus-Observed Measurement Capsules: A Profile for Third-Party Measurement Statements in SCITT](https://datatracker.ietf.org/doc/draft-templeman-scitt-measurement-capsule/) — This document defines the measurement capsule: a small, deterministic
   JSON record in which a party that is neither the subject of a claim
   nor a participant in the action it concerns records what the subject
   declared, what the measuring party observed, and the difference
   between the two.  A capsule carries digests of its evidence, a
   measurement state in which "could not be checked" is a first-class
   outcome, and no decision, approval or authorisation.  Capsules are
   identified by the SHA-256 of their JCS serialisation and batched
   under an RFC 9162 Merkle Tree Hash.  The document describes their
   registration as SCITT Signed Statements (RFC 9943), how they refer to
   rather than restate receipts issued under other profiles, its
   encoding as a COSE_Sign1 Signed Statement with test vectors, and one
   implementation, including where it does not yet match this profile.
- **draft-tiloca-ace-oscore-gm-kem-01** (new-draft, score 6, core_identity) [none]: [Quantum-Resistant Key Encapsulation Mechanisms (KEMs) via the Object Security for Constrained RESTful Environments (OSCORE) Group Manager Using Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-tiloca-ace-oscore-gm-kem/) — RFC 9594 defines a Key Distribution Center (KDC) to provision keying
   material for secure group communication, using the Authentication and
   Authorization for Constrained Environments (ACE) framework.  An
   instance of KDC is the Group Manager for provisioning keying material
   in group communication scenarios that use the Constrained Application
   Protocol (CoAP) and the security protocol Group Object Security for
   Constrained RESTful Environments (Group OSCORE).  To make the
   pairwise mode of Group OSCORE post-quantum secure, it is possible to
   rely on a quantum-resistant Key Encapsulation Mechanism (KEM) as the
   Pairwise Key Agreement Algorithm used to derive pairwise keys.  This
   document extends the interface of the ACE-based Group Manager to
   allow for the exchange of KEM public keys and encapsulated KEM shared
   secrets among group members via the Group Manager, thus enabling the
   post-quantum secure derivation of pairwise keys in Group OSCORE.
   Furthermore, this document accordingly extends the set of parameters
   that can be used to specify the configuration of an OSCORE group at
   the Group Manager.
- **draft-usama-seat-intra-vs-post-05** (new-draft, score 6, trust_infrastructure) [none]: [Pre-, Intra- and Post-handshake Attestation](https://datatracker.ietf.org/doc/draft-usama-seat-intra-vs-post/) — This document presents a taxonomy of extending TLS protocol with
   remote attestation, referred to as attested TLS.  It also presents
   high-level analysis of benefits and limitations of each category,
   namely pre-handshake attestation, intra-handshake attestation and
   post-handshake attestation.  It also captures the opinions of the WG
   participants in order to build consensus towards solutions.  It also
   discussed tradeoffs and scalability.
- **draft-vandemeent-continuity-envelope-01** (new-draft, score 6, core_identity) [none]: [Continuity Envelope Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-continuity-envelope/) — This document defines the Continuity Envelope Protocol (CEP), a
   transport-agnostic protocol model for identity-bound messaging
   systems where delivery alone is not sufficient.

   CEP separates a visible envelope surface from sealed internal object
   truth and defines how receivers determine whether a delivered object
   may safely and legitimately continue.  The protocol distinguishes
   between control-plane notification, data-plane object carriage, and
   decision-plane continuation handling.  It further distinguishes a
   refused result from an absent one and from an unknown one, and
   requires that continuation decisions and refusals leave receipts.

   CEP is the umbrella model for companion drafts such as TIBET TAT,
   which specifies generic sealed handoff and transfer flow, and IDDrop,
   which profiles that handoff model for identity transfer.
- **draft-vandemeent-tibet-causal-time-03** (new-draft, score 6, core_identity) [none]: [TIBET Causal Time Substrate](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-causal-time/) — This document describes the TIBET Causal Time Substrate, a forward-
   only causal ordering model for identity-bound distributed systems.

   TIBET does not treat wall-clock time as the primary ordering
   primitive.  Instead, it uses a cryptographically bound logical-time
   structure encoded through append-only linkage, monotonic generation
   counters, and signed causal references.  External wall-clock sources,
   including NTP, RFC 3161 timestamping services, Roughtime, GNSS, or
   public ledger timestamps, are treated as auxiliary alignment anchors
   rather than as the constitutive source of event order.

   This revision adds an optional vector-observation layer for relating
   events across independent lanes, a classification of time-bounded
   checks that separates physical-world windows from ledger-state
   windows, replay protection that does not depend on clock agreement
   between parties, and a distinction between forks, breaks, and
   reseeds.

   The core claim is simple: TIBET is a forward-only causal substrate
   that enables recovery and reversibility without rewriting history.
- **draft-vandemeent-tibet-semantic-surface-manifest-03** (new-draft, score 6, core_identity) [none]: [TIBET Semantic Surface Manifest](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-semantic-surface-manifest/) — This document defines the Semantic Surface Manifest, a human-readable
   and policy-matchable routing layer for identity-bound continuity
   containers and TBZ-based sealed bundles.

   The Semantic Surface Manifest exposes limited dispatch metadata such
   as time fragment, context, profile, and priority without exposing
   sealed content.  It is intended for use in systems where routing
   decisions may need to occur before deep inspection, while trust
   remains anchored in intrinsic bundle properties such as magic bytes,
   manifests, hashes, signatures, and causal references.

   This revision separates two decisions that earlier revisions left
   implicit: a routing hint, which may be taken from the visible surface
   before any inspection, and an admission verdict, which must never
   rest on the visible surface.

   In short: address visible, content sealed.
- **draft-vandemeent-tibet-tat-01** (new-draft, score 6, core_identity) [none]: [TIBET TAT: Touch-and-Transfer Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-tat/) — This document specifies TIBET TAT, a Touch-and-Transfer protocol for
   moving sealed continuity-bearing objects across proximity, relay, and
   local-network handoff lanes.

   TAT defines a consent-bound handoff model, a seed exchange for tunnel
   establishment, encrypted chunk streaming, mutual transfer anchoring
   between sender and receiver, and the rules under which the carrier of
   an in-flight transfer may change.

   TAT does not define identity truth, semantic class, or sealed object
   class by itself.  Instead, it defines the wire and handoff layer that
   carries such objects once sender and receiver have agreed to
   transfer.  TAT is intended to sit between the Continuity Envelope
   Protocol (CEP) and higher-level application profiles such as IDDrop.
- **draft-watts-agentic-authority-graph-validation-01** (new-draft, score 6, authorization) [none]: [Agentic Authority Graph Validation: A Non-Vacuous Interchange Profile for Revocation-Cut Analysis](https://datatracker.ietf.org/doc/draft-watts-agentic-authority-graph-validation/) — Agentic and delegated systems can represent authority as a graph
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
- **draft-watts-unison-noncollapse-01** (new-draft, score 6, authorization) [none]: [Typed UNISON and Non-Collapse Boundaries for Evidence and Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-unison-noncollapse/) — This document describes a transport-neutral model for bounded
   correspondence among distinct representations and explicit promotion
   boundaries between observation, evidence, authorization, and
   execution.
- **draft-wendt-stir-secure-sip-rtp-00** (new-draft, score 6, core_identity) [none]: [Securing SIP and RTP with STIR Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-secure-sip-rtp/) — Certificates issued within the Secure Telephone Identity Revisited
   (STIR) framework establish, through a governed issuance process, that
   a party holds authority over telephone numbers or a service provider
   code, and where a domain identifier is bound to that authority, that
   the same party controls a domain.  This document defines a
   certificate profile for TLS built on the TNAuthList extension and on
   the binding of telephone number authority to a domain identifier, so
   that the provider operating an interface is identified by a service
   provider code and by a validated domain rather than by prior
   arrangement between the parties, and it specifies the use of TLS,
   mutual TLS, and media protection across that interface.  It applies
   to the network to network interface between providers.  It brings the
   use of TLS with SIP up to date with TLS 1.3 and current certificate
   identity practice, and places the issuance of the credentials on
   which interconnection depends within a defined governance and
   issuance framework.
- **draft-wendt-stir-tn-domain-binding-02** (new-draft, score 6, core_identity) [none]: [Binding a Domain Identifier to Telephone Number Authorization in STIR Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-tn-domain-binding/) — This document defines a mechanism for binding a domain identifier to
   telephone number authorization within a STIR certificate.  A
   certificate produced under this mechanism carries, as a co-validated
   pair, the telephone numbers or service provider codes a subject is
   authorized for in a TNAuthList extension and a domain identifying the
   subject in a SubjectAltName dNSName entry.  The binding is
   established at issuance by requiring proof of domain control and
   validation of a TNAuthList authority token within a single
   certificate issuance, such that the resulting certificate attests
   that the responsible authority for the TNAuthList entries and the
   party controlling the domain both authorized the issuance.  The
   mechanism applies to STIR certificates whose TNAuthList contains
   telephone number entries, service provider code entries, or both,
   allowing a domain to be bound to the right-to-use holder for a set of
   numbers or to the provider identified by a service provider code.
   This document defines the issuance conformance requirements and the
   relying party verification rule that together make the binding
   meaningful.  It does not define telephone number or service provider
   code authorization or domain validation, both of which are specified
   elsewhere and referenced here.  It also defines the STI declaration
   record, a DNS record published at the bound domain in which the
   holder of the telephone numbers declares how legitimate calls and
   messages from them are originated and signed, so that a relying party
   can recognize ones that are not, and the requirements that any
   mechanism for discovering the domain bound to a telephone number must
   meet.
- **draft-wullink-rpp-multi-party-authorization-00** (new-draft, score 6, authorization) [none]: [Multi-Party Authorization for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-multi-party-authorization/) — The traditional Registry, Registrar and Registrant (RRR) model for
   domain name management is evolving to include third-party service
   providers, such as DNS hosting providers.  This document describes a
   generic multi-party authorization flow that allows registries to
   securely delegate domain management functions to accredited third-
   party service providers, while ensuring that the registrant's
   explicit consent is obtained before any RPP operations are executed.
- **draft-yoon-ccamp-pm-streaming-08** (new-draft, score 6, core_identity) [none]: [A YANG Data Model for Performance Monitoring Streaming on Common Transport Equipment](https://datatracker.ietf.org/doc/draft-yoon-ccamp-pm-streaming/) — This document applies the core Performance Monitoring (PM) collection
   and interval-capabilities YANG data models to common transport
   equipment.  It defines a YANG module of transport performance
   parameter identities, derived from the base identity of the PM
   collection model; it specifies the three transport parameter profiles
   of ITU-T G.7710 normatively; and it gives end-to-end examples that
   show capability discovery followed by YANG-Push subscription,
   notification, and threshold reporting for a transport profile.
- **draft-zhang-seat-selection-02** (new-draft, score 6, trust_infrastructure) [none]: [Balancing Security and Deployability in the Selection of Attested TLS Protocol](https://datatracker.ietf.org/doc/draft-zhang-seat-selection/) — This document analyzes the selection of Attested Transport Layer
   Security (aTLS) protocols, among pre-handshake, intra-handshake, and
   post-handshake aTLS protocols, focusing on the trade-off between
   theoretical security strength and practical deployability.  The goal
   is to enable flexible, context-aware deployment of endpoint
   attestation while maintaining compatibility with existing
   infrastructure.
- **draft-zollner-scim-group-membership-00** (new-draft, score 6, core_identity) [none]: [SCIM Group Membership Resource Type Extension](https://datatracker.ietf.org/doc/draft-zollner-scim-group-membership/) — This document extends the System for Cross-domain Identity Management
   (SCIM) 2.0 standard by defining a new "GroupMembership" top-level
   resource.  Under the existing model defined in RFC 7643, group
   memberships are represented as values in a multi-valued attribute
   within a Group resource.  This architecture lacks native support for
   server-side pagination, filtering, or sorting of individual members.
   In deployments managing large-scale groups (e.g., 100,000 to
   1,000,000 members or more), retrieving a Group resource results in
   massive HTTP response payloads that can exceed 100MB in size.  This
   can lead to service timeouts, memory exhaustion, and network
   instability, and has led to many major SCIM implementations choosing
   to not support returning the value of the "members" attribute for
   Group resources.  This extension introduces a flattened resource
   model that enables group memberships to benefit from pagination and
   other SCIM protocol features, ensuring interoperability and
   performance at scale.
- **draft-zollner-scim-interop-profile-02** (new-draft, score 6, core_identity) [none]: [SCIM 2.0 Interoperability Profile](https://datatracker.ietf.org/doc/draft-zollner-scim-interop-profile/) — This document defines an implementation profile for the System for
   Cross-domain Identity Management (SCIM) 2.0.  In the typical
   deployment model, an identity provider acting as a SCIM Client
   provisions and manages identities at multiple downstream service
   providers, while each service provider (commonly a multi-tenant
   application serving many customers) accepts provisioning connections
   from multiple different identity providers.  This many-to-many
   integration model compounds the interoperability challenges arising
   from the wide range of optional features and implementation
   variations permitted by the base specification.  This profile
   addresses those challenges by restricting the optional features and
   protocol variations permitted under the base specification and by
   establishing normative requirements for a common implementation
   baseline.
- **draft-arsentev-agent-run-metrics-02** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Run Metrics: A JSON Interchange Format for Resource Accounting of Language-Model Agent Runs](https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/) — Autonomous software agents driven by large language models execute
   multi-step runs in which the same conversational context is
   retransmitted to a model on every step.  The resulting resource
   consumption is dominated by repeated input rather than by generated
   output, and it is reported today in mutually incompatible, vendor-
   specific shapes.  This document defines Agent Run Metrics, a JSON
   interchange format that describes the resource consumption of a
   single agent run and of its constituent steps, together with a small
   set of derived quantities whose computation is specified exactly.  It
   states normatively that one reported step corresponds to one
   completed model invocation, so that the several records a runtime may
   write while a single response is produced are not mistaken for
   several invocations, and it defines how the consumption of delegated
   sub-runs is attributed without being counted twice.  The format
   carries counters, timing and cost attribution only; it deliberately
   excludes prompt and completion content.  This document defines the
   initial values of two extensible enumerations and the rule by which
   they are extended; it requests no IANA action.
- **draft-bu-dawn-ard-architecture-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Resource Discovery (ARD) Architecture](https://datatracker.ietf.org/doc/draft-bu-dawn-ard-architecture/) — This document describes the high-level architecture for Agent
   Resource Discovery (ARD), an open, federated framework for
   publishing, indexing, discovering, and invoking software agent
   capabilities (such as Model Context Protocol servers, Agent-to-Agent
   agents, programmatic skills, and web APIs) across local networks,
   enterprise domains, and the public Internet.  It defines the system
   roles, deployment topologies, core architectural principles, and end-
   to-end interaction flows that connect the ARD specifications for
   establishing Initial Contact and the Discovery Interface for
   capability lookup in the ARD catalog.  The Registration interface
   will be specified in a later document.
- **draft-bu-dawn-ard-discovery-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Resource Discovery (ARD): Manifest and Lookup](https://datatracker.ietf.org/doc/draft-bu-dawn-ard-discovery/) — This document specifies the catalog representation and lookup
   protocol for Agent Resource Discovery (ARD), an open architecture for
   publishing, discovering, and searching software agent capabilities
   across federated networks.  ARD defines a JSON-LD capability
   description envelope (the ARD Entry) and catalog container (the ARD
   Manifest) identified by domain-anchored Uniform Resource Names
   (URNs), cryptographic publisher authority bindings (the Trust
   Manifest), and an HTTP query interface supporting structured,
   semantic, and federated search across registries.  Initial contact
   for discovering catalog entry points and active agent registration
   are specified in companion ARD documents.
- **draft-calabria-bpm-ai-fabric-training-bench-00** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-creator-bvs-protocol-01** (new-draft, score 5, adjacent_watchlist) [none]: [Biometric Vector Steganography for Document Trust and AI-First Preambles (BVS)](https://datatracker.ietf.org/doc/draft-creator-bvs-protocol/) — This document specifies the Biometric Vector Steganography (BVS)
   protocol.  It defines an asynchronous, differential geometry-based
   method for embedding machine-readable metadata (AI-First Preambles)
   and cryptographic signatures into plain text documents.  By utilizing
   two correlating Scalable Vector Graphics (SVG) paths (walz and
   walz_shadow), BVS enables the creation of a dynamic, biometric
   anchor, representing the digital equivalent of a physical wax seal.
   The protocol guarantees document integrity within strict stream
   boundaries, proves the author's authenticity, and provides pre-
   processed metadata for edge-parsers without increasing the token load
   for Large Language Models (LLMs).
- **draft-das-protected-transaction-execution-finality-00** (new-draft, score 5, authorization) [none]: [Protected Transaction Authority and Execution-Finality Boundaries for Delegated Digital Operations](https://datatracker.ietf.org/doc/draft-das-protected-transaction-execution-finality/) — Recent publicly reported incidents involving unauthorized use of
   legitimately signed account-delegation and asset-transfer operations
   have exposed a gap between cryptographic validity and permission to
   perform an exact consequential act.  This document proposes an
   experimental, transport-independent execution-finality protocol for
   delegated digital operations.  A Candidate Act is placed in a non-
   effective state; protected collection-time and execution-time
   enforcement domains bind approved intent, independently reconstruct
   the pending effect, and require an unforgeable, sink-specific,
   single-use authorization before signing, dispatching, transmitting,
   exporting, or actuating.  The protocol specifies state continuity,
   revocation, nonce burn, quota settlement, delegated-code controls,
   multi-domain interoperability, failure behavior, receipts,
   conformance tests, and migration profiles.  It includes ASCII
   sequence diagrams and flowcharts, complete executable Python, Go, and
   JavaScript reference listings, a reproducible test-vector generator
   and runner, and recorded cross-language test results in informative
   appendices.  This is a proposal for discussion, not an adopted IETF
   standard; the reference code is not production cryptographic custody
   software.
- **draft-durga-agent-clear-revocation-00** (new-draft, score 5, authorization) [none]: [Transitive CLEAR Revocation and Composite Physical-Safety Windows for Multi-Hop Autonomous Agent DAGs](https://datatracker.ietf.org/doc/draft-durga-agent-clear-revocation/) — When an orchestrator agent delegates sub-tasks across a multi-hop
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
- **draft-durga-agent-tx-compensation-lease-00** (new-draft, score 5, agent_identity) [none]: [Pre-Release Transactional Compensation Leases and CAS Fencing Receipts for Autonomous Agents Over Systems of Record](https://datatracker.ietf.org/doc/draft-durga-agent-tx-compensation-lease/) — When autonomous AI agents execute write operations against enterprise
   Systems of Record (ERP, MES, WMS, CRM, ITSM), traditional HTTP
   idempotency keys (RFC 9110) and post-hoc Saga orchestrators cannot
   guarantee deterministic recovery if a stochastic multi-step plan
   halts mid-flight or hallucinates downstream parameters.  This
   document specifies the Pre-Release Transactional Compensation Lease
   (PTCL) protocol: a fail-closed wire contract requiring an agent
   runtime to acquire a cryptographically signed recovery reservation
   lease, prove a bounded rollback window (T_req <= T_granted), and
   present a Compare-And-Swap (CAS) epoch fencing token prior to
   committing any state mutation.
- **draft-ek-dtn-ipn-arpa-01** (new-draft, score 5, core_identity) [none]: [The ipn.arpa Zone and IPN DNS Operations](https://datatracker.ietf.org/doc/draft-ek-dtn-ipn-arpa/) — This document requests the creation of ipn.arpa, an infrastructure
   DNS namespace for the IPN node identifiers used by the Bundle
   Protocol (BP).  Each Fully Qualified Node Number has a canonical name
   of the form N.A.ipn.arpa, where A is the Allocator Identifier and N
   is the Node Number.  A BP Agent can query directly beneath that name
   for records specified by a convergence-layer discovery binding, such
   as SRV or SVCB records.  The DNS records identify convergence-layer
   endpoints advertised for reaching a destination, including relays.
- **draft-gondwana-we-are-all-individuals-03** (new-draft, score 5, core_identity) [none]: [We Are All Individuals](https://datatracker.ietf.org/doc/draft-gondwana-we-are-all-individuals/) — Participation in the IETF is by individuals.  This document applies
   that principle now that software Agents can write and submit text.
   Each Identity belongs to one Human, and every Contribution has at
   least one accountable Human.  Anonymous Contributions are not
   accepted, and no Human may use two Identities in the same piece of
   work.  Reading the IETF's work requires no account or identification.
   Rough consensus is unchanged.
- **draft-guorong-utxo-dns-03** (new-draft, score 5, verifiable_claims) [none]: [UTXO6-DNS: Resolving Payment Endpoints via Private-use RRTYPE and Prefix Isolation](https://datatracker.ietf.org/doc/draft-guorong-utxo-dns/) — This document specifies the _utxo application namespace for DNS.  It
   defines how wallet clients and TEE (Trusted Execution Environment)
   applications resolve verifiable payment endpoints and blockchain UTXO
   (Unspent Transaction Output) references using DNS.

   To avoid exacerbating public RRTYPE space congestion and DNS-layer
   transparent parsing, this document utilizes the RFC 3597 Private-use
   space (QTYPE 65400).  The DNS protocol does not parse the payload.
   Application semantics are isolated strictly via the _utxo underscore
   prefix in the owner name, while the RDATA consists of a purely opaque
   CBOR-encoded byte stream.
- **draft-he-bpm-congestion-loss-monitoring-problem-00** (new-draft, score 5, ai_infrastructure) [none]: [Requirements and Problem Statement for Monitoring Packet Loss Caused by Network Congestion](https://datatracker.ietf.org/doc/draft-he-bpm-congestion-loss-monitoring-problem/) — Emerging services including enhanced Mobile Broadband (eMBB) and
   Ultra-Reliable Low Latency Communication (uRLLC), as well as
   Artificial Intelligence (AI)training and inference have imposed
   stringent requirements of "high throughput, low latency, and minimal
   packet loss" on IP bearer network performance.  Network congestion
   can lead to performance degradation and increase uncertainty in
   service delivery, so real-time congestion monitoring is necessary.
   This document discuss the requirements of real-time monitoring of
   packet loss caused by congestion, present the problems and challenges
   faced by existing measurement techniques in monitoring congestion-
   induced packet loss.
- **draft-hood-agtp-communication-01** (new-draft, score 5, core_identity) [none]: [AGTP Communication Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-communication/) — This document specifies the AGTP Communication Protocol (AGTP-
   COMMUNICATION): the companion specification for real-time multi-modal
   communication between agents over the Agent Transfer Protocol (AGTP).
   AGTP-COMMUNICATION defines how voice, video, and other real-time
   media streams are exchanged between agents on the agent-native
   substrate, with native support for the wire-level identity, authority
   scope, and attribution that AGTP provides.

   This is an early specification covering bilateral (two-agent) real-
   time communication.  Multi-party conversations and conferencing
   patterns are out of scope for this revision and are deferred to
   future companion work.
- **draft-ietf-rats-pkix-key-attestation-08** (new-draft, score 5, adjacent_watchlist) [rats]: [Evidence Encoding for Hardware Security Modules](https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/) — This document specifies a vendor-agnostic format for Evidence
   produced and verified within a PKIX context.  The Evidence produced
   this way includes claims collected about a cryptographic module, such
   as a Hardware Security Module (HSM), and elements found within it
   such as cryptographic keys.

   One scenario envisaged is that the state information about the
   cryptographic module can be securely presented to a remote operator
   or auditor in a vendor-agnostic verifiable format.  A more complex
   scenario would be to submit this Evidence to a Certification
   Authority to aid in determining whether the storage properties of
   this key meet the requirements of a given certificate profile.
- **draft-ietf-webbotauth-httpsig-protocol-01** (new-draft, score 5, core_identity) [webbotauth]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-irtf-nmrg-ibn-usecases-05** (new-draft, score 5, ai_infrastructure) [nmrg]: [Use Cases and Practices for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ibn-usecases/) — This document proposes a methodology to construct an Intent-Based
   Networking (IBN) system.  According to this methodogy, it decribes
   several use cases of IBN.  The methodology for the IBN system
   includes data collection for system awareness in the IBN system and
   then the construction of the IBN system.  This construction consists
   of intent translation, policy translation, policy verification,
   policy deployment, policy monitoring, policy validation, policy
   optimization, and intent report.  In addition, practices are also
   summarized to instruct the construction of next generation network
   management systems with the integration of IBN techniques.  Finally,
   this document discusses three aspects for the deployment of the IBN
   system on the real world.  They are Multi-Domain Dichotomy for IBN,
   the Integration of IBN and Network Digital Twin (NDT), and IBN with
   Artificial Intelligence (AI).
- **draft-jesske-ai-enablement-interface-01** (new-draft, score 5, agent_identity) [none]: [AI enablement interface for multimedia services platforms](https://datatracker.ietf.org/doc/draft-jesske-ai-enablement-interface/) — This document complements emerging AI agent communication protocols
   by defining a generic enablement interface between multimedia
   communication platforms and AI applications, agents, LLM, or other
   AI-based services.  It describes how communication capabilities,
   including voice, video, messaging, media streams, and media
   processing, can be exposed to AI entities without defining a new
   agent-to-agent communication protocol.

   The interface is particularly applicable where an AI service is not
   itself a communication endpoint, but is invoked by a communication
   platform to process or enhance an existing communication service.
   Examples include live translation, call summarization, contextual
   assistance, fraud detection, and media enhancement.

   The interface is platform-agnostic and extensible.  SIP-based
   networks and the 3GPP IP Multimedia Subsystem (IMS) are examples of
   communication platforms to which this approach can be applied.
- **draft-jms-mole-architecture-01** (new-draft, score 5, adjacent_watchlist) [none]: [Moderation of unLinkable Endorsements (MOLE) Architecture](https://datatracker.ietf.org/doc/draft-jms-mole-architecture/) — Moderation of unLinkable Endorsements (MOLE) is an architecture that
   lets a party performing access control (a Moderator) bootstrap trust
   in a client from a third party (an Anchor) that already has a trust
   relationship with that client, and then adjust that trust over time
   in response to the client's behaviour, for example by dynamically
   rate-limiting access.

   MOLE targets open deployments, in which independent parties may be
   responsible for access control and for vouching for clients, whilst
   maintaining strong privacy protections for clients.  These
   protections are designed to hold even if participants in the
   ecosystem collude or otherwise misbehave.

   This document specifies the roles, the information flows between
   them, the privacy and security requirements, and deployment
   considerations.
- **draft-jms-mole-protocols-01** (new-draft, score 5, verifiable_claims) [none]: [MOLE Protocols](https://datatracker.ietf.org/doc/draft-jms-mole-protocols/) — This document defines protocols that instantiate the MOLE
   architecture: two endorsement protocols, by which a Client proves to
   a Moderator that it holds an Endorsement from a trusted Anchor
   without revealing which one, and two credential protocols, by which a
   Moderator issues, verifies, and updates per-Client state without
   being able to link presentations.  It also establishes the registries
   that identify these protocols.
- **draft-mcw-opsawg-icon-requirements-02** (new-draft, score 5, agent_identity) [none]: [Architecture and Requirements for Observability, Control and Intervention of Network Management Agents](https://datatracker.ietf.org/doc/draft-mcw-opsawg-icon-requirements/) — This document defines architecture and a set of requirements for
   Observability, Control, and Intervention for Network Management
   Agents.

   It identifies gaps in existing mechanisms and specifies required
   interaction capabilities between Agent supervision systems and
   network management agents across multi-vendor environments,
   specifically observability, control, and runtime intervention.  The
   requirements aim to guarantee comprehensive, lifecycle control over
   AI agents and enable observation, constraint, intervention, and
   correction to ensure network operational resilience and continuity.
- **draft-miao-dawn-agw-intergration-consideration-00** (new-draft, score 5, privacy_security) [none]: [Considerations for Agent Gateway Integration within the DAWN Framework](https://datatracker.ietf.org/doc/draft-miao-dawn-agw-intergration-consideration/) — This document specifies the integration architecture, discovery proxy
   mechanisms, and operational workflows for the Agent Gateway (AGW)
   within the Discovery of Agents With Names (DAWN) problem space.
   Addressing the core problem of how an agent discovers peer agents
   across administrative and network boundaries, this specification
   defines the dual role of the Agent Gateway: serving as an Outbound
   Discovery Proxy (Discovery Substrate Access Point) that assists local
   domain agents in querying external discovery fabrics, and an Inbound
   Domain Discovery Proxy (Broker/Aggregator) that enables external
   agents to discover matching capabilities situated on sub-agents
   behind the gateway.  The document outlines the internal capability
   matching engine, selective disclosure mechanisms for privacy
   preservation, DNS-SD/mDNS resource record mappings, and strict
   boundary alignments with the IETF DAWN Working Group Charter.
- **draft-mozleywilliams-dawn-dnsaid-00** (new-draft, score 5, agent_identity) [none]: [DNS for AI Discovery](https://datatracker.ietf.org/doc/draft-mozleywilliams-dawn-dnsaid/) — This document specifies DNS for AI Discovery (DNS-AID), a method for
   publishing AI agents in the Domain Name System (DNS) so that other
   agents can discover them.  It defines three discovery use cases,
   ordered by increasing latency and computational cost.  In the known-
   agent case, the requestor knows both the agent and its domain, and a
   single DNS query returns connectivity information and key metadata.
   In the known-organization case, the requestor knows the domain but
   not which agent provides a required capability, and queries a well-
   known organizational index to get connectivity information to enable
   a capability search of a catalog, agent registry or database.  In the
   known-capability case, the requestor knows only the required
   capability and must rely on an external directory or search service.
   This document addresses the known-agent and known-organization cases.
   The known-capability case is out of scope, but search and cataloging
   services can be built from the organizational index defined here.
   Once a client has learned an organization’s agents, later
   interactions can use the known-agent case, relying on a minimal,
   cacheable record set that each organization controls.  DNS-AID uses
   Service Binding (SVCB) records, optionally with DNS-Based Service
   Discovery (DNS-SD) labels, DNSSEC, and DANE TLSA records.  This gives
   agents direct connections that no third party mediates and works the
   same way on public and private networks.  No new resource record
   types, opcodes, or response codes are introduced.
- **draft-nestorov-scitt-p10-underdetermination-02** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Adjudication Statements over SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming P10
   Adjudication Statement carries two canonical witness worlds that are
   compatible with the same closed evidence set and produce different
   values for the same frozen claim.  The witness result is checked
   against committed profile semantics and bound into a SCITT
   Transparent Statement containing an in-toto Statement v1 predicate.
   The result establishes underdetermination only relative to the
   declared profile and does not identify the actual world or establish
   either claim value as true.
- **draft-peterson-stir-agentic-00** (new-draft, score 5, core_identity) [none]: [Secure Telephone Identity for Agents](https://datatracker.ietf.org/doc/draft-peterson-stir-agentic/) — The Secure Telephone Identity Revisited (STIR) framework uses
   credentials to sign calls in order to prevent identity impersonation
   in the telephone network, especially by robocallers.  Its framework
   also accounts for certain cases of "legitimate" impersonation of
   identity.  This document expands the scope of STIR to include agents
   acting on behalf of users and enterprises: how agents might best opt-
   in to self-identify as agents, and how the intent of the originating
   user or enterprise in delegating to an agent can best be communicated
   to relying parties.
- **draft-petrie-vcon-tool-invocation-00** (new-draft, score 5, agent_identity) [none]: [The JSON vCon - Tool Invocation Extension](https://datatracker.ietf.org/doc/draft-petrie-vcon-tool-invocation/) — A vCon is a container for data and information relating to a
   conversation.  This document defines an extension to the JSON vCon
   schema for recording the policy decisions of AI agents and their
   invocation of tools.  Before an agent performs an operation, the
   agent or its host uses policy to decide whether the operation is
   allowed, disallowed or requires permission.  This document defines an
   Event Object type for those decisions, and Event Object types for
   each step of a tool invocation.  It also outlines requirements for
   recording requests for permission and direction, which need to be
   defined in a future document.
- **draft-ramadan-moq-fec-multicast-00** (new-draft, score 5, core_identity) [none]: [Forward Error Correction for Multicast Delivery of Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-multicast/) — This document specifies how the Forward Error Correction (FEC)
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
- **draft-rqd-ainetops-problem-statement-00** (new-draft, score 5, agent_identity) [none]: [The problem statement of AI Native Network Operations](https://datatracker.ietf.org/doc/draft-rqd-ainetops-problem-statement/) — The introduction of AI agents into network operations is
   fundamentally reshaping the operation and maintenance (O&M) paradigm,
   shifting from human-led, passive network management toward intent-
   driven, self-planning, and intelligent reasoning.  While this shift
   promises significant gains in efficiency and autonomy, it introduces
   a set of problems that are not yet covered by the existing IETF
   network management framework.

   This document identifies and summarizes the deployment and operation
   problems that arise when AI native network operations (AINETOps) are
   introduced into operator networks.  It systematically enumerates the
   standardization gaps across Network Management Agent (NMA) lifecycle
   management, the Human-Agent Interface (HAI), the agent-to-agent task
   and evidence models, and task risk classification.  It does not
   propose solutions; its purpose is to provide a problem inventory that
   can anchor future IETF work on solutions and deployment best
   practices.
- **draft-ruan-idr-ai-compute-service-metadata-01** (new-draft, score 5, adjacent_watchlist) [none]: [BGP Extension for AI Compute Service Metadata](https://datatracker.ietf.org/doc/draft-ruan-idr-ai-compute-service-metadata/) — This document defines four AI inference-specific Sub-TLVs for the BGP
   Edge Metadata Path Attribute specified in
   [I-D.ietf-idr-5g-edge-service-metadata].  They advertise model
   capabilities, aggregated inference latency, optional cost preference,
   and selected long-lived KV cache prefix identifiers.  Authorized CATS
   Path Selectors (C-PSes) and other policy decision functions may use
   this information to select suitable service contact instances and
   forwarding paths.  This document reuses the existing optional non-
   transitive attribute.
- **draft-watts-boundary-jurisdiction-architecture-02** (new-draft, score 5, agent_identity) [none]: [Boundary Jurisdiction Architecture for Agentic and Delegated Systems](https://datatracker.ietf.org/doc/draft-watts-boundary-jurisdiction-architecture/) — This document describes a protocol-neutral architecture for
   separating possession of capability from jurisdiction over
   consequential authority boundaries.  It models authority as
   reachability in a time-indexed capability graph, defines revocation
   cuts, and specifies fail-closed semantics for delegation and
   revocation closure.
- **draft-watts-gov-verification-promotion-boundaries-01** (new-draft, score 5, agent_identity) [none]: [Government-Oriented Verification Promotion Boundaries for Agentic Assurance Profiles](https://datatracker.ietf.org/doc/draft-watts-gov-verification-promotion-boundaries/) — Government and critical-infrastructure relying parties require
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
- **draft-watts-scientific-admissibility-evidence-01** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Admissibility Evidence Records for Verifiable Research Provenance](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility-evidence/) — This document describes a portable JSON evidence-record format for
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
- **draft-wright-verdict-record-02** (new-draft, score 5, trust_infrastructure) [none]: [Verdict Records: Results on Claims that Cite Receipts as Evidence](https://datatracker.ietf.org/doc/draft-wright-verdict-record/) — This document defines a verdict record: a statement, bound to its
   issuer, of a result reached on a claim, together with the evidence
   the result relies on and the rule by which the result can be re-
   derived.  Evidence is cited by digest and can be a receipt or record
   in any format, such as a SCITT Receipt or an Agent Action Capsule.
   The document defines how a checker checks a verdict record and what
   such a check does and does not show.  It defines no receipt format
   and changes none.
- **draft-xkk-rtgwg-hpc-scheduler-job-metadata-00** (new-draft, score 5, adjacent_watchlist) [none]: [HPC/AI Scheduler Job Metadata Model](https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-scheduler-job-metadata/) — This document defines a scheduler-facing metadata model for High
   Performance Computing (HPC) and AI workloads.  The model captures
   common job, workload, scheduler, tenant, timing, and task metadata
   that can be mapped from heterogeneous workload managers and
   orchestration platforms and used as context for network service
   intent.
- **draft-xkk-rtgwg-hpc-service-intent-00** (new-draft, score 5, adjacent_watchlist) [none]: [HPC/AI Service Intent Model](https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-service-intent/) — This document defines a common service intent model for High
   Performance Computing (HPC) and AI workloads over High Performance
   Wide Area Networks (HP-WANs).  The model allows heterogeneous
   workload managers and orchestration platforms to express endpoint,
   communication pattern, timing, performance, data movement, policy,
   and admission requirements for network services without exposing
   technology-specific tunnel realization details.
- **draft-zhang-cats-token-aware-ts-01** (new-draft, score 5, adjacent_watchlist) [none]: [A token-aware traffic steering solution for agent service](https://datatracker.ietf.org/doc/draft-zhang-cats-token-aware-ts/) — this document proposes a token-aware traffic steering mechanism.  By
   parsing token semantic features, sequence lengths, and task types,
   and comprehensively incorporating network link status, model
   capabilities, and compute resource states into routing decisions,
   this mechanism achieves joint optimal scheduling of resources.
- **draft-zhao-nmop-nma-nti-yang-00** (new-draft, score 5, adjacent_watchlist) [none]: [Framework and YANG Data Model for the NMA Northbound Task Interface (NTI)](https://datatracker.ietf.org/doc/draft-zhao-nmop-nma-nti-yang/) — This document describes a framework and a YANG data model for the
   Northbound Task Interface (NTI) of a Network Management Agent (NMA).
   The NTI is a logical northbound interface through which upper-layer
   consumers, including OSS/BSS, orchestrators, management applications,
   and other agents, can submit network management tasks to an NMA and
   obtain task processing results.

   This document specifies a YANG-based realization of the NTI,
   including operational state data, RPC operations, and notifications
   for capability discovery, intent submission, task lifecycle
   management, execution plan exposure, confirmation handling, and
   result reporting.  The model is intended to reuse existing IETF
   network management models for domain-specific information.

   The NTI does not mandate a dedicated communication protocol.  NETCONF
   and RESTCONF can be used for the YANG-based realization, while A2A-
   based mechanisms may also be used to realize NTI interactions.  This
   document does not define or extend generic agent interaction
   protocols.
- **draft-bonica-macneil-singh-ipv6-firewall-metadata-00** (new-draft, score 4, adjacent_watchlist) [none]: [Verifiable Firewall and Security-Enforcement Metadata in IPv6](https://datatracker.ietf.org/doc/draft-bonica-macneil-singh-ipv6-firewall-metadata/) — This document defines a way to carry a verifiable record of security
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
- **draft-cowlishaw-carbontxt-00** (new-draft, score 4, trust_infrastructure) [none]: [carbon.txt: A transparency protocol for public sustainability data](https://datatracker.ietf.org/doc/draft-cowlishaw-carbontxt/) — This document specifies the carbon.txt convention, a machine-readable
   format for publishing links to disclosures concerning the
   environmental impact of an organization's digital / ICT operations at
   a predictable location on the web.  Carbon.txt is a TOML document
   that acts as an index: it declares where an origin's impact
   disclosures (Annual reports, Sustainability policies, Third party
   certifications, Quantitative measurements or estimations) may be
   found, and optionally lists upstream service providers whose own
   disclosures may be relevant to the origin's environmental impact.
   Carbon.txt does not carry numeric impact metrics or specific claims
   about impacts itself; it links to documents that do.  In addition it
   defines a discovery mechanism by which certain origins may delegate
   their carbon.txt implementation to another.
- **draft-ietf-keytrans-architecture-11** (new-draft, score 4, trust_infrastructure) [keytrans]: [Key Transparency Architecture](https://datatracker.ietf.org/doc/draft-ietf-keytrans-architecture/) — This document defines the terminology and interaction patterns
   involved in the deployment of Key Transparency in end-to-end
   encrypted communication services, and specifies the security
   properties that the protocol provides.  It also gives more general,
   non-prescriptive guidance on how to securely apply Key Transparency
   to a number of common applications.
- **draft-ietf-keytrans-protocol-06** (new-draft, score 4, trust_infrastructure) [keytrans]: [Key Transparency Protocol](https://datatracker.ietf.org/doc/draft-ietf-keytrans-protocol/) — While there are several established protocols for end-to-end
   encryption, relatively little attention has been given to securely
   distributing the end-user public keys for such encryption.  As a
   result, these protocols are often still vulnerable to eavesdropping
   by active attackers.  Key Transparency is a protocol for distributing
   sensitive cryptographic information, such as public keys, in a way
   that reliably either prevents interference or detects that it
   occurred in a timely manner.
- **draft-ietf-plants-merkle-tree-certs-08** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
   certificates which integrate public logging of the certificate, in
   the style of Certificate Transparency.  The integrated design reduces
   logging overhead in the face of both shorter-lived certificates and
   large post-quantum signature algorithms, while still achieving
   comparable security properties to existing X.509 constructions and
   Certificate Transparency.  Merkle Tree certificates additionally
   admit an optional size optimization that avoids signatures
   altogether, at the cost of only applying to up-to-date relying
   parties and older certificates.
- **draft-jadoon-dawn-layered-agent-discovery-00** (new-draft, score 4, authorization) [none]: [Discovery of AI Agents for Communication Services: Use Case and Problem Statement](https://datatracker.ietf.org/doc/draft-jadoon-dawn-layered-agent-discovery/) — This document presents a use case and problem statement for the
   initial discovery of AI agents supporting end-to-end communication
   services within an organization.  The use case considers AI agents
   associated with different functions of the Internet protocol suite,
   including application, transport, Internet-layer, and related
   network-operation functions.  These agents may share general
   capabilities but differ in their communication-related operational
   scopes and responsibilities.  The document examines the minimum
   public discovery information needed to distinguish such agents within
   a known organizational discovery scope.
- **draft-kelley-aipref-training-preference-signal-00** (new-draft, score 4, adjacent_watchlist) [none]: [Machine-Readable Training Preference Signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) — This document describes how a service operator binds usage
   preferences (e.g., "no AI training") to paths by writing ordinary
   robots.txt groups keyed by a per-purpose policy token in the User-
   Agent line.  It introduces no new directive names and no new grammar:
   the path language, longest-match precedence, and group structure of
   robots.txt are not changed.
- **draft-ladd-mole-ec-ihat-00** (new-draft, score 4, adjacent_watchlist) [none]: [EC-IHAT: Issuer-Hiding Anonymous Tokens](https://datatracker.ietf.org/doc/draft-ladd-mole-ec-ihat/) — This document specifies EC-IHAT, a cryptographic construction used to
   produce and consume MOLE Endorsements.  An Endorsement is an
   anonymous token that an Anchor issues to a Client, and that the
   Client later redeems at a Moderator without the Anchor being able to
   link the redemption to the issuance.

   This document defines the endorsement issuance protocol, built from a
   pairing-free partially blind signature scheme, together with the
   group, encoding, and context-binding rules that both the Anchor and
   the Client follow.
- **draft-sanketh-plants-mtc-architecture-00** (new-draft, score 4, trust_infrastructure) [none]: [Merkle Tree Certificates Architecture](https://datatracker.ietf.org/doc/draft-sanketh-plants-mtc-architecture/) — Merkle Tree Certificates (MTCs) make transparency logging part of
   certificate issuance, enabling Internet-scale deployments of short-
   lived certificates and large post-quantum signatures.  In exchange,
   their security rests on the state, not just the keys, of the
   certification authority, its cosigners, and relying parties' update
   services.  This document describes the architecture for deploying
   MTCs and defines the guarantees that a relying party can obtain when
   it accepts one.  These cover who certified and who recorded the
   certificate, agreement among relying parties on each log entry, the
   enforcement of revoked ranges, and the validation of the relying
   party's own configuration.  For each guarantee, we state which
   parties must behave as specified and which keys and state they must
   keep intact.  Our Recommendations are not needed to interoperate, but
   they affect the guarantees a deployment achieves, especially against
   adversaries able to compromise a certification authority, a cosigner,
   or an update service.
- **draft-schlesinger-mole-ec-act-00** (new-draft, score 4, adjacent_watchlist) [none]: [EC-ACT: Anonymous Credit Tokens](https://datatracker.ietf.org/doc/draft-schlesinger-mole-ec-act/) — This document specifies EC-ACT, a keyed-verification anonymous
   credential scheme with a hidden credit balance.  A Client spends a
   public amount and receives a fresh Credential for the remaining
   balance and a return amount chosen by the Moderator.  The Moderator
   verifies each spend without learning the balance or linking it to
   issuance or to other spends.

   EC-ACT uses a pairing-free BBS-style signature and proofs over linear
   relations.  This document defines its cryptographic operations,
   encodings, and security requirements.  The MOLE protocols use EC-ACT
   as a Credential scheme.
- **draft-yang-nmrg-mcp-nm-04** (new-draft, score 4, adjacent_watchlist) [none]: [Applicability of MCP for the Network Management](https://datatracker.ietf.org/doc/draft-yang-nmrg-mcp-nm/) — The application of MCP in the network management field is meant to
   refactor network management operation and network capabilities as
   tools and provide more agile and extensible architecture to expose
   these AI integration capabilities.  This document discusses the
   applicability of MCP to the network management plane in the IP
   network that utilizes IETF technologies.  It explores MCP for network
   exposure, multiple MCP server discovery, communication between
   Network Elements or between the Network element and the Network
   Controller/Network Gateway.

## Adjacent / watchlist

- **draft-adams-bimi-reporting-12** (new-draft, score 3, core_identity) [none]: [BIMI Reporting](https://datatracker.ietf.org/doc/draft-adams-bimi-reporting/) — To support the utility of Brand Indicators for Message Identification
   (BIMI), domains publishing BIMI records may find it useful to know
   when their logos are failing to be displayed as expected.  When an
   entity, for example a mailbox operator, determines whether or not to
   display the logo identified in the BIMI record, they may encounter
   errors trying to retrieve the image file.  Similarly, the associated
   evidence document used to validate the logo may fail evaluation.  In
   other cases, the evaluator may decide that despite everything
   validating, they may rely on local policies that determine validated
   logos should still not be displayed.  This specification defines how
   BIMI evaluators should report their evaluation outcome back to the
   publisher within the context of existing Domain-based Message
   Authentication, Reporting, and Conformance (DMARC) reports.
- **draft-anish-spring-bimap-multicast-02** (new-draft, score 3, adjacent_watchlist) [none]: [SRv6 Bitmap Multicast](https://datatracker.ietf.org/doc/draft-anish-spring-bimap-multicast/) — Multicast forwarding in a network provides advantages in improving
   the network usage and performance.  In some cases it helps improve
   the operations in managing network.  The major challenge in multicast
   operations is in managing the per-flow states in the network as
   required by all the legacy multicast frameworks.

   This document specifies a bitmap forwarding extension to SRv6 to
   support state-free forwarding model in a network.
- **draft-ar-acme-pqc-tlsjws-01** (new-draft, score 3, core_identity) [none]: [Quantum-Ready ACME Mechanism](https://datatracker.ietf.org/doc/draft-ar-acme-pqc-tlsjws/) — This document updates RFC 8555 (ACME) to specify post-quantum and PQ/
   T hybrid cryptographic requirements for quantum-ready deployments.
   The Automatic Certificate Management Environment (ACME) automates
   certificate issuance, validation, and management over HTTPS using
   JSON Web Signatures (JWS) to authenticate client request payloads.
   Current ACME deployments rely on traditional public-key algorithms in
   both JWS and TLS, which are vulnerable to attacks from
   Cryptographically Relevant Quantum Computers (CRQCs).  This
   specification defines PQC or PQ/T hybrid TLS 1.3 key establishment
   and specifies PQC or PQ/T authentication mechanisms for JWS and TLS
   under the quantum-ready ACME mechanism.  This specification enables
   ACME clients and servers to achieve quantum-resistant confidentiality
   and authentication.
- **draft-aravind-idr-bgp-ls-sr-policy-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for BGP-LS Segment Routing Policy](https://datatracker.ietf.org/doc/draft-aravind-idr-bgp-ls-sr-policy-yang/) — This document defines a YANG data model for the operational state of
   Segment Routing (SR) Policy candidate paths that are advertised using
   BGP - Link State (BGP-LS).  The model augments the read-only BGP-LS
   Link-State Database with the SR Policy Candidate Path Network Layer
   Reachability Information (NLRI) and the associated BGP-LS Attribute
   TLVs specified in RFC 9857.
- **draft-artamokhov-dawn-marketplace-discovery-03** (new-draft, score 3, adjacent_watchlist) [none]: [A Discovery Document and Signed Catalogue for Capability Marketplaces](https://datatracker.ietf.org/doc/draft-artamokhov-dawn-marketplace-discovery/) — This document defines a JSON discovery document, served at a well-
   known URI, that carries the public properties a client needs before
   using a capability index: its name, the protocol versions it serves,
   the location of its catalogue, and the key that signs the catalogue.
   It also states the requirements for that signed catalogue and defines
   one signature profile.  Discovery between indexes, catalogue
   exchange, trust, and search or selection among catalogued
   capabilities are out of scope.
- **draft-asw-lsr-isis-ogid-00** (new-draft, score 3, core_identity) [none]: [IS-IS Originating Generation Identifier (OGID) TLV](https://datatracker.ietf.org/doc/draft-asw-lsr-isis-ogid/) — This document introduces a new top-level TLV in IS-IS, the
   Originating Generation Identifier (OGID) TLV, which is carried in
   every Link State PDU (LSP) fragment originated by a node.  The OGID
   identifies the logical transaction to which a set of LSP fragment
   updates belongs.  When accompanied by a Fragment Count greater than
   one, it additionally allows a receiving node to determine when all
   fragments participating in that transaction have been received.  This
   enables receivers to process multi-fragment updates atomically,
   avoiding the transient Link State Database (LSDB) inconsistencies
   that can otherwise occur when logically related LSP fragment updates
   are flooded and processed independently.
- **draft-barnes-mimi-identity-arch-04** (new-draft, score 3, core_identity) [none]: [Identity for E2E-Secure Communications](https://datatracker.ietf.org/doc/draft-barnes-mimi-identity-arch/) — End-to-end (E2E) security is a critical property for modern user
   communications systems.  E2E security protects users' communications
   from tampering or inspection by intermediaries that are involved in
   delivering those communcations from one logical endpoint to another.
   In addition to the much-discussed E2E encryption systems, true E2E
   security requires an identity mechanism that prevents the
   communications provider from impersonating participants in a session,
   as a way to gain access to the session.  This document describes a
   high-level architecture for E2E identity, identifying the critical
   mechanisms that need to be specified.
- **draft-beeram-pce-pcep-mpted-02** (new-draft, score 3, adjacent_watchlist) [none]: [Path Computation Element Communication Protocol (PCEP) Extensions for Multipath Traffic Engineered Directed Acyclic Graph (MPTED) Tunnels](https://datatracker.ietf.org/doc/draft-beeram-pce-pcep-mpted/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that facilitates weighted
   load balancing of unicast traffic across a constrained set of paths
   optimized for a specific objective.

   This document describes the provisioning of an MPTED tunnel in a TE
   network using Path Computation Element Communication Protocol (PCEP)
   in a stateful PCE model.
- **draft-beeram-teas-yang-mpted-05** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Multipath Traffic Engineering Directed Acyclic Graph (MPTED) Tunnels and Junctions](https://datatracker.ietf.org/doc/draft-beeram-teas-yang-mpted/) — This document defines a YANG data model for representing, retrieving,
   and manipulating Multipath Traffic Engineering Directed Acyclic Graph
   (MPTED) tunnels and junctions.  The model includes two YANG modules,
   one for managing MPTED tunnels on an MPTED tunnel originator node and
   the other for managing MPTED junctions on an MPTED junction node.
- **draft-bonica-tcpm-tcp-ao-long-algs-07** (new-draft, score 3, core_identity) [none]: [Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/) — RFC5926 creates a registry of cryptographic algorithms that can be
   used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256 and
   KMAC256.

   The MAC algorithms described by this document produce 256-bit (i.e.,
   32-byte) MACs.  When 32-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 36 of the 40 bytes available for TCP options.
- **draft-bormann-core-cri-diagnostic-notation-00** (new-draft, score 3, core_identity) [none]: [CBOR Diagnostic Notation: "cri" Application-oriented Extension](https://datatracker.ietf.org/doc/draft-bormann-core-cri-diagnostic-notation/) — For the Concise Binary Object Representation (CBOR), a Concise
   Diagnostic Notation (CDN) has been defined in draft-ietf-cbor-edn-
   literals.  This provides an extension point for "App-Extension
   Identifiers" registry in the "Concise Diagnostic Notation" registry
   group, supporting text representations of CBOR tags and other
   structures to enhance usability.

   The present document specifies an app-extension and registers an app-
   extension identifier for CBOR tag 99, Constrained Resource
   Identifiers (CRI), as defined in RFC-to-be 9988.


   // (This cref will be removed by the RFC editor:) This document
   // carries the specification of the cri'' application- oriented
   // prefix for CBOR diagnostic notation.  This specification used to
   // be in the CoRE WG document for CRIs, became part of the CBOR WG
   // document for CBOR diagnostic notation when the CBOR WG document
   // was delayed, and was then deleted from that document as it is
   // outside the scope of the CBOR WG.  So this document now goes back
   // to the CoRE WG, as a "new" individual submission.
- **draft-brissette-idr-dc-origin-leaf-id-00** (new-draft, score 3, core_identity) [none]: [Origin-Leaf Identification in Data-Center eBGP Underlays using BGP Large Communities](https://datatracker.ietf.org/doc/draft-brissette-idr-dc-origin-leaf-id/) — Data-center fabrics that run hop-by-hop eBGP routing frequently need
   to identify the originating node (leaf) of a prefix as it is
   propagated through the fabric.  The BGP AS_PATH attribute provides
   loop prevention and identifies the originating Autonomous System
   (AS), but under common AS numbering models an AS does not map to a
   single leaf.  While several BGP community mechanisms could carry such
   an identifier, there is no documented practice describing the
   mechanism and encoding choices for underlay origin-leaf tagging.

   This document analyzes the problem, states the requirements, and
   surveys candidate BGP mechanisms for carrying an origin-leaf
   identifier.  It recommends encoding the identifier in a BGP Large
   Community (RFC 8092), describes how the identifier is allocated
   within the Large Community namespace, and describes how it is
   originated, propagated unchanged across the fabric, and consumed at
   receiving leaves.  It also describes an optional profile for locally
   significant route-attachment metadata.  This document is
   Informational and defines no new protocol elements.
- **draft-busi-nmop-simap-rfc8795-applicability-03** (new-draft, score 3, adjacent_watchlist) [none]: [Applicability of RFC8795 YANG data model to SIMAP](https://datatracker.ietf.org/doc/draft-busi-nmop-simap-rfc8795-applicability/) — This document analyses the applicability of the RFC 8795 YANG data
   model to Service & Infrastructure Maps (SIMAP) and in particular
   analysis which requirements can be supported by the existing YANG
   data model defined in RFC 8795.
- **draft-celi-wiggers-tls-authkem-08** (new-draft, score 3, core_identity) [none]: [KEM-based Authentication for TLS 1.3](https://datatracker.ietf.org/doc/draft-celi-wiggers-tls-authkem/) — This document gives a construction for a Key Encapsulation Mechanism
   (KEM)-based authentication mechanism in TLS 1.3.  This proposal
   authenticates peers via a key exchange protocol, using their long-
   term (KEM) public keys.
- **draft-claise-green-capability-discovery-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-contreras-tvr-schedule-lifecycle-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [Lifecycle and State Extensions for TVR Schedule YANG Model](https://datatracker.ietf.org/doc/draft-contreras-tvr-schedule-lifecycle-yang/) — The Time-Variant Routing (TVR) YANG data model
   [I-D.ietf-tvr-schedule-yang] defines a mechanism to describe
   scheduled changes in network resources (such as nodes and topology)
   as a function of time.  However, the base model does not provide
   explicit lifecycle management semantics for the schedules, such as
   activation, suspension, or deprecation.

   This document defines an optional augmentation of the base YANG model
   to introduce lifecycle and administrative state control, enabling
   more flexible operational handling of schedules without modifying the
   base model semantics.
- **draft-darkdragon-hardware-bot-attestation-00** (new-draft, score 3, trust_infrastructure) [none]: [Hardware-Interrupt Attestation for Privacy-Preserving Bot Mitigation](https://datatracker.ietf.org/doc/draft-darkdragon-hardware-bot-attestation/) — This document proposes a privacy-first, OS kernel-level attestation
   mechanism to mitigate automated botnets on internet platforms.  By
   evaluating input events at the physical hardware interrupt layer, the
   system generates attestation tokens only upon detecting automated
   execution, remaining silent during legitimate human usage to preserve
   user privacy.
- **draft-davidben-lamps-turducken-certs-00** (new-draft, score 3, core_identity) [none]: [Embedded Alternate Issuer Certificates](https://datatracker.ietf.org/doc/draft-davidben-lamps-turducken-certs/) — This document defines a mechanism to embed one or more alternate
   certificates within a single outer certificate.  The outer
   certificate remains parseable to a legacy relying party that is
   unaware of this specification.  Each alternate certificate certifies
   the same subject information, but with a different issuer.  This can
   be used to help TLS on the Web transition securely to post-quantum
   authentication, as well as other PKI transitions with similar
   constraints.
- **draft-dhody-teas-te-traffic-yang-06** (new-draft, score 3, adjacent_watchlist) [none]: [Traffic Mapping YANG model for Traffic Engineering (TE)](https://datatracker.ietf.org/doc/draft-dhody-teas-te-traffic-yang/) — This document provides a YANG data model to map traffic to Traffic
   Engineering (TE) paths.  This model provides the operator a seamless
   control and management of which traffic to send on the underlying TE
   resources.
- **draft-dikshit-bpm-telemetry-comparability-00** (new-draft, score 3, adjacent_watchlist) [none]: [Operational Telemetry Comparability for IP Performance Measurements](https://datatracker.ietf.org/doc/draft-dikshit-bpm-telemetry-comparability/) — Operational telemetry is often used to compare network performance
   across observation points, traffic classes, service instances, paths,
   devices, and time intervals.  The numeric value of a metric is not
   sufficient for such comparison unless the observation context and the
   comparability conditions are also known.

   This document describes a common interoperability problem in
   operational measurement systems: values such as delay, loss, ECN
   marking, queue occupancy, packet counts, byte counts, and flow
   correlation identifiers can be exported from different observation
   points or under different aggregation rules while still appearing to
   be directly comparable.  A collector or controller can therefore
   combine values that do not describe the same measurement domain.

   The document defines requirements for describing the observation
   point, metric source, aggregation interval, traffic class, flow
   scope, sampling rule, timestamp basis, freshness, and comparability
   domain associated with operational telemetry used for IP performance
   measurement.  The goal is to make operational measurement results
   easier to compare without prescribing one measurement protocol, one
   data model, or one congestion control mechanism.
- **draft-dunbar-dawn-infra-assisted-discovery-03** (new-draft, score 3, agent_identity) [none]: [Infrastructure-Assisted Discovery for AI Agents](https://datatracker.ietf.org/doc/draft-dunbar-dawn-infra-assisted-discovery/) — This document describes an infrastructure-assisted approach
   to the initial discovery of AI agents in managed enterprise,
   cloud, edge-computing, and communication-network
   environments. The approach treats infrastructure-provided
   resource state and requester context as possible inputs to
   the Minimum Viable Dataset (MVD) used by a discovery
   mechanism. These inputs can help keep minimum public
   discovery information current and can help determine the
   appropriate discovery scope or entry point without requiring
   the requester to understand deployment-specific network
   details. The document does not define registration, catalog
   search, semantic matchmaking, resource ranking, or selection,
   and does not define a new discovery wire protocol.
- **draft-eastlake-dnssd-rfc2931bis-sigzero-05** (new-draft, score 3, core_identity) [none]: [Domain Name System (DNS) Public Key Based Request and Transaction Authentication (MSGSIG, SIG(0))](https://datatracker.ietf.org/doc/draft-eastlake-dnssd-rfc2931bis-sigzero/) — This document specifies the MSGSIG and SIG(0) Domain Name System
   (DNS) Resource Records (RRs) which provide public key based
   authentication of DNS requests and transactions.  MSGSIG is the
   RECOMMENDED option.  This document obsoletes RFC 2931 and updates RFC
   6891.
- **draft-fu-onsen-update-l3sm-service-models-03** (new-draft, score 3, adjacent_watchlist) [none]: [Extensions to the YANG Data Model for L3VPN Service Delivery](https://datatracker.ietf.org/doc/draft-fu-onsen-update-l3sm-service-models/) — [RFC8299] defines a YANG data model for L3VPN service delivery.  The
   base L3VPN Service Model (L3SM) has limitations regarding dynamic
   service features.  In addition, emerging technologies including SRv6
   and quantum security bring new service capabilities available to
   customers, which are not natively supported by L3SM.  This document
   defines a set of extensions to address the limitations of L3SM.

   These augmentations are designed to be backward-compatible and do not
   obsolete [RFC8299].
- **draft-gondwana-dkim2-authres-02** (new-draft, score 3, core_identity) [none]: [Reporting DKIM2 Verification Results in Authentication-Results](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-authres/) — DomainKeys Identified Mail Signatures v2 (DKIM2) produces a
   verification result for an email message.  This document defines how
   that result is reported in the Authentication-Results header field,
   registering the "dkim2" authentication method, the result values it
   can take, and two properties which identify the signing domain and
   the point in the chain at which verification failed.  Diagnostic
   detail about each hop is carried in a human-readable comment.
- **draft-havel-nmop-simap-features-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP Additional Features](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-features-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP) Additional Features, including optional graph
   navigation, lifecycle and external-link capabilities intended to be
   reusable with RFC 8345 topology models, including implementations
   using RFC 8795.
- **draft-havel-nmop-simap-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP Core Topology](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP) Core Topology.  It extends the RFC8345 YANG modules to
   support the subset of core SIMAP requirements.  This document will
   only focus on modelling proposal for each of the core SIMAP topology
   requirements not supported by RFC8345.  Any related terminology,
   concepts, use cases and requirements are defined outside of this
   draft and this draft will only refer to them, analyze how to model
   and propose the implementation solutions.
- **draft-hegde-spring-sr-distributed-bw-00** (new-draft, score 3, adjacent_watchlist) [none]: [Distributed Bandwidth Management for Segment Routing](https://datatracker.ietf.org/doc/draft-hegde-spring-sr-distributed-bw/) — This document defines an architecture for distributed bandwidth
   management in Segment Routing (SR) networks.  Distributed bandwidth
   management is a model in which the bandwidth required by each SR
   Policy is computed and reserved in a distributed manner by the
   network nodes themselves, rather than by a centralized controller, so
   that path computation, admission control, and bandwidth accounting
   for SR Policies are performed by the head-end and transit nodes along
   the path.
- **draft-henry-pqst-cohort-00** (new-draft, score 3, authorization) [none]: [The Cohort Layer of Post-Quantum Secure Transport (PQST)](https://datatracker.ietf.org/doc/draft-henry-pqst-cohort/) — This document specifies the cohort layer of Post-Quantum Secure
   Transport (PQST).  With it, PQST provides independently migrating and
   recoverable post-quantum sessions within a persistent cohort
   authorization context.  A cohort member's sessions move, sleep,
   recover and re-key on their own, and none of those events by itself
   requires a change of the cohort's membership.  One sequencer commits
   the membership, the policy, and a membership epoch together with that
   epoch's key, and only on security events; members receive them inside
   their pairwise sessions, keep them through partitions, and return
   after dormancy or a restart without readmission, unless they were
   away longer than the group's expiry.  This version specifies the
   group's control plane: membership, policy, reachability and member
   discovery.  It describes, as the direction of the next version, a
   group data plane under keys derived from the epoch key, which would
   give the members one secure session among themselves.
- **draft-henry-pqst-overview-00** (new-draft, score 3, authorization) [none]: [Post-Quantum Secure Transport (PQST): Overview and Reading Guide](https://datatracker.ietf.org/doc/draft-henry-pqst-overview/) — PQST (Post-Quantum Secure Transport) is a post-quantum native
   session-primary datagram transport for secure tunnels without
   classical public key cryptography, hybrid key exchange, or classical
   fallback.  The cryptographic session is the persistent object, the
   network path is a replaceable carrier, and a session can be re-
   anchored on a new path, after a restart, or after the loss of every
   path, with fresh post-quantum key material and without the session,
   its authorization, or the peers' authenticated identities changing.
   The cohort layer of PQST applies the same idea one level up: a group
   whose members' sessions move, sleep, recover and re-key independently
   while the group's membership changes only on security events.  This
   document is a non-normative overview of, and reading guide to, the
   specifications of those two layers.  It defines no wire format, no
   behaviour, and no requirements.  The core protocol is proposed as the
   basis for Standards Track work; the cohort layer is Experimental.
   The author is seeking a working-group home for the core protocol and
   implementation experience with both layers.
- **draft-herbert-deprecate-auth-header-02** (new-draft, score 3, core_identity) [none]: [Deprecation of IP Authentication Header (AH) and IP Payload Compression Protocol (IPCOMP)](https://datatracker.ietf.org/doc/draft-herbert-deprecate-auth-header/) — IP Authentication Header (AH) and IP Payload Compression Protocol
   (IPCOMP) of the IPsec suite have been deprecated and RFC 3173 and RFC
   4302 have been moved to Historic status.  This document further
   updates the IANA IKEv2 Security Protocol Identifiers by adding a
   "Status" column where the deprecation status can be listed.  This
   document also closes the IKEv2 Notification IPCOMP Transform IDs
   registry.
- **draft-hood-agtp-discovery-02** (new-draft, score 3, authorization) [none]: [AGTP Agent Discovery and Name Service](https://datatracker.ietf.org/doc/draft-hood-agtp-discovery/) — The Agent Transfer Protocol (AGTP) enables agents to communicate once
   they know each other's canonical identifiers.  This document
   specifies two layered mechanisms by which agents find each other and
   by which human-readable names resolve to Canonical Agent-IDs: the
   DISCOVER method, which queries for agents matching a capability
   description, and the Agent Name Service (ANS), which provides
   governed name-to-Agent-ID resolution.

   The architectural relationship is layered.  AGTP-Presence
   [AGTP-PRESENCE] provides ambient awareness of agents within
   visibility scopes as a substrate property.  DISCOVER operates over
   the Presence substrate to query the live population.  ANS provides
   human-readable name resolution, analogous to DNS for the web, with
   name authorities federating across organizational boundaries.  This
   document also introduces Anticipatory Discovery Services (ADS) as a
   forward-looking composition pattern where application-layer services
   preload agent awareness based on observed operational signals.

   DISCOVER and ANS together provide the application-layer interfaces
   for discovery and naming that compose with the substrate-level
   ambient discovery defined in [AGTP-PRESENCE].
- **draft-hu-ipsecme-pqt-hybrid-auth-with-sep-cert-00** (new-draft, score 3, core_identity) [none]: [Post-Quantum Traditional (PQ/T) Hybrid PKI Authentication with separate certificates in the Internet Key Exchange Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-hu-ipsecme-pqt-hybrid-auth-with-sep-cert/) — A Cryptographically Relevant Quantum Computer (CRQC) would break the
   traditional asymmetric algorithms, such as RSA and ECDSA, that are
   widely used to authenticate the Internet Key Exchange Protocol
   Version 2 (IKEv2).  Post-quantum digital signature algorithms are
   intended to resist such a computer, but these new algorithms and
   their implementations require time to mature.  This document
   specifies a post-quantum traditional (PQ/T) hybrid PKI authentication
   method for IKEv2 in which each peer uses two separate certificates:
   one containing a post-quantum public key and one containing a
   traditional public key.  Authentication remains secure as long as at
   least one of the component signature algorithms remains secure.
- **draft-huang-onsen-update-l3nm-network-models-00** (new-draft, score 3, adjacent_watchlist) [none]: [Extensions to the YANG Network Data Model for L3VPN](https://datatracker.ietf.org/doc/draft-huang-onsen-update-l3nm-network-models/) — RFC 9182 defines a YANG network data model for Layer 3 VPNs (L3NM),
   which provides a network-centric view of L3VPN services and is used
   by orchestrators to drive network controllers.  A companion effort
   extends the L3VPN Service Model (L3SM, RFC 8299) with dynamic and
   enhanced service features, including dynamic networking provisioning,
   dynamic bandwidth adjustment, QoS enhancements for network slicing,
   performance monitoring, and quantum-safe encryption
   [I-D.fu-onsen-update-l3sm-service-models].

   At the network layer, such dynamic service requirements translate
   into time-scheduled resource reservations that the network confirms
   for feasibility and reserves in advance of the activation moment
   (Section 1.1).

   These enhanced service features cannot be realized by the network
   unless corresponding capabilities are exposed at the network layer.
   The base L3NM defined in RFC 9182 exhibits gaps in these areas.  This
   document defines a set of YANG augmentations to the L3NM to close
   those gaps.  The augmentations are designed to be backward-compatible
   and do not obsolete RFC 9182.
- **draft-huitema-ccwg-c4-design-05** (new-draft, score 3, adjacent_watchlist) [none]: [Design of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-design/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  It pays special attention to
   the high jitter conditions encountered in Wi-Fi networks.  The design
   emphasizes simplicity and avoids making too many assumption about the
   "model" of the network.  The main control variables are the estimate
   of the data rate and of the maximum path delay in the absence of
   queues.
- **draft-huitema-ccwg-c4-spec-05** (new-draft, score 3, adjacent_watchlist) [none]: [Specification of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-spec/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design emphasizes
   simplicity and avoids making too many assumptions about the "model"
   of the network.
- **draft-ietf-6man-ipv6-neighbor-discovery-yang-09** (new-draft, score 3, adjacent_watchlist) [6man]: [YANG Data Model for IPv6 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/) — This document defines a YANG data model to configure and manage IPv6
   Neighbor Discovery (ND) and related functions, including IPv6 address
   resolution, redirect function, proxy Neighbor Advertisement, Neighbor
   Unreachability Detection (NUD), Duplicate Address Detection (DAD),
   and Enhanced Duplicate Address Detection.
- **draft-ietf-ace-coap-est-oscore-12** (new-draft, score 3, verifiable_claims) [ace]: [Protecting EST Payloads with OSCORE](https://datatracker.ietf.org/doc/draft-ietf-ace-coap-est-oscore/) — Enrollment over Secure Transport (EST) is a certificate provisioning
   protocol over HTTPS [RFC7030] or CoAPs [RFC9148].  This document
   specifies how to carry EST over the Constrained Application Protocol
   (CoAP) protected with Object Security for Constrained RESTful
   Environments (OSCORE).  The specification builds on the EST-coaps
   [RFC9148] specification, but uses OSCORE and Ephemeral Diffie-Hellman
   over COSE (EDHOC) instead of DTLS.  The specification also leverages
   the certificate structures defined in
   [I-D.ietf-cose-cbor-encoded-cert], which can be optionally used
   alongside X.509 certificates.
- **draft-ietf-acme-profiles-03** (new-draft, score 3, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Profiles Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/) — This document defines how an ACME Server may offer a selection of
   different certificate profiles to ACME Clients, and how those clients
   may indicate which profile they want.
- **draft-ietf-anima-brski-discovery-16** (new-draft, score 3, core_identity) [anima]: [BRSKI discovery and variations](https://datatracker.ietf.org/doc/draft-ietf-anima-brski-discovery/) — This document specifies procedures for variations of the
   "Bootstrapping Remote Secure Key Infrastructure" (BRSKI) architecture
   of protocols to automatically announce, discover, and select
   responders using different discovery mechanisms such as DNS-SD,
   GRASP, or CORE-LF.  Different variations are not interoperable, so
   initiators need to be able to find responders that support the
   variation(s) they support.  Procedures are defined for BRSKI proxies
   that allow proxying of traffic for any current or future variation.
   Procedures to discover BRSKI Pledges by their identifier are defined.
   Extensibility is provided through a set of IANA registries.

   This document updates I-D.ietf-anima-brski-prm, RFC 6690, and RFC
   9733.
- **draft-ietf-bpm-alt-mark-yang-00** (new-draft, score 3, adjacent_watchlist) [bpm]: [A YANG Data Model for the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-yang/) — Alternate-Marking Method is a technique used to perform packet loss,
   delay, and jitter measurements on in-flight packets.  This document
   defines a YANG data model for the Alternate-Marking Method.
- **draft-ietf-cats-oam-fw-02** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections across clients, network paths, and service
   instances within a single domain.  This document does not define
   concrete OAM protocol designs or protocol extensions.
- **draft-ietf-cbor-serialization-12** (new-draft, score 3, adjacent_watchlist) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — RFC 8949 defines CBOR, a standard for serializing data types such as
   integers, strings, and arrays into encoded bytes.  CBOR serialization
   is flexible, allowing data types to be encoded in multiple ways to
   accommodate deployment in constrained environments.  This document
   normatively defines one particular serialization, called "preferred-
   plus serialization," that is suitable for the majority of CBOR-based
   protocols.  Protocol designers and implementers who choose it need
   not understand or specify serialization details themselves.  This
   document also normatively defines a deterministic serialization.
   These serializations are largely compatible with those widely
   implemented by the CBOR community.

   This document updates RFC 8949 with a new rule that limits how new
   tag definitions can affect the CBOR data model.

   This document provides clarifications to RFC 8949 regarding bignums
   and floating-point NaN handling, along with general background
   information on serialization, determinism, and CBOR byte-string
   wrapping.
- **draft-ietf-ccamp-dwdm-if-param-yang-17** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG data model to manage configurable DWDM optical interfaces](https://datatracker.ietf.org/doc/draft-ietf-ccamp-dwdm-if-param-yang/) — This document defines a YANG model related to the Optical Transceiver
   parameters characterising coherent 100G and above interfaces.  100G
   and above Transceivers support coherent modulation, multiple
   modulation formats, multiple Forward Error Correction (FEC) codes
   including some not yet specified (or in phase of specification by)
   ITU-T G.698.2 or any other ITU-T recommendation.  Use cases are
   described in RFC7698.

   The YANG model defined in this document can be used for Optical
   Parameters monitoring and/or configuration of Dense Wavelength
   Division Multiplexing (DWDM) interfaces.  The use of this model does
   not guarantee interworking of DWDM transceivers.  Optical path
   feasibility and interoperability has to be determined by tools and
   algorithms outside the scope of this document.  The purpose of this
   model is to program interface parameters to consistently configure
   the mode of operation of transceivers.
- **draft-ietf-ccamp-rfc8561bis-00** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for Microwave Radio Link](https://datatracker.ietf.org/doc/draft-ietf-ccamp-rfc8561bis/) — This document defines a YANG data model for control and management of
   radio link interfaces and their connectivity to packet (typically
   Ethernet) interfaces in a microwave/millimeter wave node.  The data
   nodes for management of the interface protection functionality is
   broken out into a separate and generic YANG data model in order to
   make it available for other interface types as well.  This document
   obsoletes RFC 8561.
- **draft-ietf-ccwg-bbr-07** (new-draft, score 3, adjacent_watchlist) [ccwg]: [BBR Congestion Control](https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/) — This document specifies the BBR congestion control algorithm.  BBR
   ("Bottleneck Bandwidth and Round-trip propagation time") uses recent
   measurements of a transport connection's delivery rate, round-trip
   time, and packet loss rate to build an explicit model of the network
   path.  BBR then uses this model to control both how fast it sends
   data and the maximum volume of data it allows in flight in the
   network at any time.  Relative to loss-based congestion control
   algorithms such as Reno [RFC5681] or CUBIC [RFC9438], BBR offers
   substantially higher throughput for bottlenecks with shallow buffers
   or random losses, and substantially lower queueing delays for
   bottlenecks with deep buffers (avoiding "bufferbloat").  BBR can be
   implemented in any transport protocol that supports packet-delivery
   acknowledgment.  Thus far, open source implementations are available
   for TCP [RFC9293] and QUIC [RFC9000].  This document specifies
   version 3 of the BBR algorithm, BBRv3.
- **draft-ietf-core-comi-22** (new-draft, score 3, core_identity) [core]: [CoAP Management Interface (CORECONF)](https://datatracker.ietf.org/doc/draft-ietf-core-comi/) — This document describes a network management interface for
   constrained devices and networks, called CoAP Management Interface
   (CORECONF).  The Constrained Application Protocol (CoAP) is used to
   access datastore and data node resources specified in YANG, or SMIv2
   converted to YANG.  CORECONF uses the YANG to CBOR mapping and
   converts YANG identifier strings to numeric identifiers for payload
   size reduction.  CORECONF extends the set of YANG based protocols,
   NETCONF and RESTCONF, with the capability to manage constrained
   devices and networks.
- **draft-ietf-cose-c509-test-vectors-03** (new-draft, score 3, adjacent_watchlist) [cose]: [Test Vectors for CBOR-Encoded X.509 (C509) Certificates](https://datatracker.ietf.org/doc/draft-ietf-cose-c509-test-vectors/) — This document contains examples of CBOR-encoded X.509 (C509)
   certificates, certification requests, and certification request
   templates.
- **draft-ietf-detnet-glbf-03** (new-draft, score 3, adjacent_watchlist) [detnet]: [Deterministic Networking (DetNet) Data Plane - guaranteed Latency Based Forwarding (gLBF) for bounded latency with low jitter and asynchronous forwarding in Deterministic Networks](https://datatracker.ietf.org/doc/draft-ietf-detnet-glbf/) — This memo proposes a mechanism called "guaranteed Latency Based
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
- **draft-ietf-detnet-multi-domain-framework-03** (new-draft, score 3, adjacent_watchlist) [detnet]: [A Control Plane Framework for Multi-Domain Deterministic Networking (DetNet)](https://datatracker.ietf.org/doc/draft-ietf-detnet-multi-domain-framework/) — Deterministic Networking (DetNet) provides the capability to carry
   specified unicast or multicast data flows for real-time applications
   with extremely low data loss rates and bounded latency over a path or
   network.  As DetNet deployments expand, they will inevitably need to
   span multiple domains that may be under separate technological
   control.  This creates a need for a control plane solution that can
   establish and maintain end-to-end DetNet services across these domain
   boundaries.

   This document defines a generic framework for a multi-domain DetNet
   control plane.  It first establishes a working definition of a
   "DetNet Domain" for the purpose of path computation and control.  It
   then describes two high-level architectural approaches for inter-
   domain path computation and resource reservation: a Hierarchical
   model and a peer-to-peer "stitching" model.  While a Path Computation
   Element (PCE)-based realization is used as an illustrative example,
   the framework is designed to be applicable to any controller-plane
   technology that satisfies the stated functional requirements.  This
   framework provides the foundation for more specific work on multi-
   domain DetNet solutions.
- **draft-ietf-detnet-stateless-fair-queuing-02** (new-draft, score 3, adjacent_watchlist) [detnet]: [Latency Guarantee with Stateless Fair Queuing](https://datatracker.ietf.org/doc/draft-ietf-detnet-stateless-fair-queuing/) — This document specifies the implementation of the stateless fair
   queuing framework defined in Recommendations ITU-T Y.3129 [Y.3129]
   and Y.3148 [Y.3148].  The framework provides end-to-end (E2E) latency
   bounds to flows without requiring core nodes to maintain per-flow
   state.  For each packet, the entrance node of a flow computes the
   ideal service completion time under a fluid model, referred to as the
   Finish Time (FT), and encodes it in the packet header.  Each
   subsequent core node updates the FT by adding a delay factor that is
   determined by the flow and the nodes.  Schedulers serve queued
   packets in ascending order of FT.  This mechanism provides strong
   isolation among flows.  The E2E latency bound of a flow depends on
   the flow's own parameters, such as its maximum burst size and service
   rate, and on link parameters, such as the link capacity and the
   maximum packet length among the flows sharing the link.  This
   document specifies the required metadata and its encoding formats,
   the admission control procedure, and an approximation of stateless
   fair queuing using a strict priority (SP) scheduler.
- **draft-ietf-dkim-dkim2-spec-09** (new-draft, score 3, adjacent_watchlist) [dkim]: [DomainKeys Identified Mail Signatures v2 (DKIM2)](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-spec/) — DomainKeys Identified Mail v2 (DKIM2) permits the owner of a signing
   domain to document that they have handled an email message by
   associating their domain with the message.  This is achieved by
   providing a hash value that has been calculated on the current
   contents of the message and then applying a cryptographic signature
   that covers the hash values and other details about the transmission
   of the message.  Verification is performed by querying an entry
   within the signing domain's DNS space to retrieve an appropriate
   public key.  As a message is transferred from author to recipient,
   systems that alter the body or header fields will provide details of
   their changes and calculate new hash values.  Further signatures will
   be added to provide a "chain" that receivers can validate.  This
   permits verifiers to identify the nature of changes made by
   intermediaries and apply a reputation to the systems that made
   changes.  DKIM2 also allows recipients to detect when messages have
   been unexpectedly "replayed" and will ensure that Delivery Status
   Notifications are only sent to entities that were involved in the
   transmission of a message.
- **draft-ietf-dmm-mts-03** (new-draft, score 3, adjacent_watchlist) [dmm]: [Mobile Traffic Steering](https://datatracker.ietf.org/doc/draft-ietf-dmm-mts/) — The evolution of cellular mobile communication systems is aligned
   with an increasing demand for customized deployments, energy
   efficiency, dynamic re-configurability and the integration and use of
   other network technologies, such as non-cellular radio access
   technologies and non-terrestrial networks.  In order to achieve and
   maintain the expected service quality and continuity, such systems
   should be designed and controllable end-to-end, taking all involved
   network domains and segments into account.  This document discusses
   an end-to-end system from an advanced use cases perspective and
   substantiates the demand for solutions to share information and
   enable control interfaces between all connected network domains,
   including the mobile communication system and the transport network
   that stretches up to the data networks that host service instances.
   In the view of flexible implementations and deployment, two
   architectural principles, leveraging either a dedicated controller or
   a decentralized control plane, are described and discussed,
   accompanied by operational aspects and an associated information
   model that enable end-to-end mobile traffic treatment and steering in
   such complex and dynamically changing networks.
- **draft-ietf-dnsop-multi-alg-rules-00** (new-draft, score 3, adjacent_watchlist) [dnsop]: [Multiple Algorithm Rules in DNSSEC](https://datatracker.ietf.org/doc/draft-ietf-dnsop-multi-alg-rules/) — This document restates the requirements on DNSSEC signing and
   validation and makes small adjustments in order to allow for more
   flexible handling of configurations that advertise multiple Secure
   Entry Points (SEP) with different signing algorithms via their DS
   record or trust anchor set.  The adjusted rules allow both for multi-
   signer operation and for the transfer of signed DNS zones between
   providers, where the providers support disjoint DNSSEC algorithm
   sets.  In addition, the proposal enables pre-publication of a trust
   anchor in preparation for an algorithm rollover, such as of the root
   zone.

   This document updates RFCs 4035 and 6840.
- **draft-ietf-dtn-bpsec-cose-18** (new-draft, score 3, verifiable_claims) [dtn]: [Bundle Protocol Security (BPSec) COSE Context](https://datatracker.ietf.org/doc/draft-ietf-dtn-bpsec-cose/) — This document defines a security context suitable for using CBOR
   Object Signing and Encryption (COSE) algorithms within Bundle
   Protocol Security (BPSec) integrity and confidentiality blocks.  A
   profile for COSE, organized by algorithm families, and for public key
   certificates are included for BPSec interoperation.

   This document updates BPSec RFC 9172 by providing Concise Data
   Definition Language (CDDL) rules for extensible security block
   content.
- **draft-ietf-green-power-and-energy-yang-05** (new-draft, score 3, adjacent_watchlist) [green]: [Power and Energy YANG Module](https://datatracker.ietf.org/doc/draft-ietf-green-power-and-energy-yang/) — This document defines a YANG data model for Power and Energy
   monitoring and control of devices within or connected to
   communication networks.
- **draft-ietf-grow-bmp-tcp-ao-04** (new-draft, score 3, core_identity) [grow]: [TCP-AO Protection for BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tcp-ao/) — This document outlines the utilization of the TCP Authentication
   Option (TCP-AO), as specified in [RFC5925], for the authentication of
   BGP Monitoring Protocol (BMP) sessions, as specified in [RFC7854].
   TCP-AO provides for the authentication of BMP sessions established
   between routers and BMP stations at the TCP layer.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/hmntsharma/draft-hmntsharma-bmp-tcp-ao.
- **draft-ietf-grow-bmp-yang-10** (new-draft, score 3, adjacent_watchlist) [grow]: [A YANG Data Model for BMP](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/) — This document defines a YANG data model for the configuration and
   monitoring of the BGP Monitoring Protocol (BMP).
- **draft-ietf-httpapi-patch-byterange-05** (new-draft, score 3, adjacent_watchlist) [httpapi]: [Byte Range PATCH](https://datatracker.ietf.org/doc/draft-ietf-httpapi-patch-byterange/) — This document specifies a media type for PATCH payloads that
   overwrites a specific byte range, facilitating random access writes
   and segmented uploads of resources.
- **draft-ietf-httpbis-connect-tcp-18** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP tunneling using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this tunneling functionality has several
   important deficiencies due to the lack of a well-defined HTTP origin
   or path.  This specification remedies those deficiencies by defining
   CONNECT-TCP, an alternative protocol for tunneling TCP in HTTP.  A
   proxy service for this protocol is described by a URI Template,
   similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-httpbis-resumable-upload-15** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
- **draft-ietf-idr-bgp-model-23** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Model for Border Gateway Protocol (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) — This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.
- **draft-ietf-intarea-arp-yang-model-02** (new-draft, score 3, adjacent_watchlist) [intarea]: [A YANG Data Model for ARP Extensions](https://datatracker.ietf.org/doc/draft-ietf-intarea-arp-yang-model/) — This document defines a YANG data model for the management of the
   Address Resolution Protocol (ARP).  It extends the basic ARP
   functionality contained in the ietf-ip YANG data model, defined in
   RFC 8344, to provide management of optional ARP features and
   statistics.
- **draft-ietf-ipsecme-pq-hybrid-auth-01** (new-draft, score 3, core_identity) [ipsecme]: [Use of Composite Signatures in IKEv2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-pq-hybrid-auth/) — A Cryptographically Relevant Quantum Computer (CRQC) can break
   traditional public-key algorithms (e.g., RSA, ECDSA), which are
   typically used for authentication in IKEv2.  Combining the post-
   quantum ML-DSA signature algorithm with a traditional signature
   algorithm provides protection against potential weaknesses or
   implementation flaws in ML-DSA.  This draft defines a hybrid PKI
   authentication method for IKEv2 using composite certificates that
   ensures authentication remains secure as long as at least one of the
   component signature algorithms remains unbroken.
- **draft-ietf-ivy-network-inventory-software-05** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Data Model of Network Inventory Software](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-software/) — This document extends the base Network Inventory YANG model to
   support software-based network elements (NEs) and software
   components.  The extension introduces software lifecycle status that
   distinguishes running software from software that is installed but
   not running, together with installation timestamps for non-running
   software, and both installation and activation timestamps for running
   software.
- **draft-ietf-jmap-metadata-05** (new-draft, score 3, core_identity) [jmap]: [JMAP Object Metadata](https://datatracker.ietf.org/doc/draft-ietf-jmap-metadata/) — This document defines an extension to the JSON Meta Application
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
- **draft-ietf-lake-edhoc-grease-04** (new-draft, score 3, authorization) [lake]: [Applying Generate Random Extensions And Sustain Extensibility (GREASE) to LAKE Extensibility](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-grease/) — This document applies the extensibility mechanism GREASE (Generate
   Random Extensions And Sustain Extensibility), which was pioneered for
   TLS, to the ecosystem of the LAKE protocol (also called EDHOC).  It
   reserves a set of External Authorization Data (EAD) labels and
   unusable cipher suites that may be included in messages to ensure
   peers correctly handle unknown values.
- **draft-ietf-lamps-certdiscovery-06** (new-draft, score 3, adjacent_watchlist) [lamps]: [A Mechanism for X.509 Certificate Discovery](https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/) — This document specifies a method to discover a referenced X.509
   certificate associated with the current X.509 certificate.  This
   enables efficient multi-certificate or fallback certificate handling
   in protocols.  The objective is threefold: to enhance cryptographic
   agility, improve operational availability, and accommodate multi-key/
   certificate usage.  The proposed method aims to maximize
   compatibility with existing systems and is designed to be legacy-
   friendly, making it suitable for environments with a mix of legacy
   and new implementations.  It includes mechanisms to provide a URI
   from which the referenced X.509 certificate can be retrieved as well
   as information about the target certificate's signature and public
   key algorithm, empowering relying parties to make informed decisions
   on whether to retrieve the Referenced Certificate, and a certificate
   hash to ensure that the correct certificate was retrieved.
- **draft-ietf-lamps-cms-frodokem-01** (new-draft, score 3, adjacent_watchlist) [lamps]: [Use of FrodoKEM in the Cryptographic Message Syntax](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-frodokem/) — FrodoKEM is a quantum-resistant key encapsulation mechanism (KEM)
   based on the standard Learning With Errors (LWE) problem，standardized
   by ISO.  FrodoKEM offers multiple parameter sets, with the
   recommended sets for general use including (e)FrodoKEM-976-AES and
   (e)FrodoKEM-976-SHAKE for security level 3, and (e)FrodoKEM-1344-AES
   and (e)FrodoKEM-1344-SHAKE for security level 5.  This document
   specifies the conventions for using FrodoKEM in the Cryptographic
   Message Syntax (CMS), using the KEMRecipientInfo structure defined in
   "Use of Key Encapsulation Mechanism (KEM) Algorithms in the
   Cryptographic Message Syntax (CMS)" [RFC9629].
- **draft-ietf-lamps-frodokem-certificates-00** (new-draft, score 3, adjacent_watchlist) [lamps]: [Internet X.509 Public Key Infrastructure - Algorithm Identifiers for FrodoKEM](https://datatracker.ietf.org/doc/draft-ietf-lamps-frodokem-certificates/) — FrodoKEM is an unstructured lattice-based Key Encapsulation Mechanism
   (KEM).  Compared to ML-KEM, FrodoKEM is considered as having more
   conservative design.  This document specifies the conventions for
   using FrodoKEM in X.509 Public Key Infrastructure.  The conventions
   for the subject public keys and private keys are also specified.
- **draft-ietf-lamps-one-signature-certs-04** (new-draft, score 3, adjacent_watchlist) [lamps]: [One Signature Certificates](https://datatracker.ietf.org/doc/draft-ietf-lamps-one-signature-certs/) — This document defines the signedDocumentBinding certificate
   extension, which binds a certificate to the signed content of a
   single digital signature.  Each certificate is created at the time of
   signing; the associated signing key is generated for the sole purpose
   of producing that one signature, is used for no other purpose, and is
   destroyed immediately afterwards.  Certificates carrying this
   extension are intended to be issued without a revocation mechanism
   and with no expiration, which simplifies long-term validation.
- **draft-ietf-lisp-yang-26** (new-draft, score 3, adjacent_watchlist) [lisp]: [LISP YANG Model](https://datatracker.ietf.org/doc/draft-ietf-lisp-yang/) — This document describes a YANG data model to use with the Locator/ID
   Separation Protocol (LISP).  This model can be used to configure and
   monitor the different control plane and data plane elements that
   enable a LISP network.

   The YANG modules in this document conform to the Network Management
   Datastore Architecture (NMDA) defined in [RFC8342].
- **draft-ietf-lsvr-bgp-ls-yang-05** (new-draft, score 3, adjacent_watchlist) [lsvr]: [A YANG Model for BGP-LS, BGP-LS-VPN, and BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-ietf-lsvr-bgp-ls-yang/) — This document defines a YANG data model for configuration and
   management of BGP-LS, BGP-LS-VPN, and BGP-LS-SPF.
- **draft-ietf-masque-http-datagram-compression-02** (new-draft, score 3, adjacent_watchlist) [masque]: [Extensions to Compress and Derive Fields in HTTP Datagrams](https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/) — This document defines extensions for HTTP Datagram-based protocols
   that improve transmission efficiency by introducing templates for
   compressing or deriving datagram fields.

   These templates allow endpoints to define parts of datagrams that are
   static and can be removed, and other parts that can be derived (such
   as packet lengths and checksum values).

   Additionally, this document defines a checksum offload procedure
   enabling receivers to complete Internet checksums using sender-
   provided partial values.

   These optimisations reduce per-packet overhead and processing cost.
   Compression can allow larger original packets to fit in QUIC DATAGRAM
   frames, depending on the applicable processing context and path
   maximum transmission unit (MTU).
- **draft-ietf-masque-quic-proxy-10** (new-draft, score 3, adjacent_watchlist) [masque]: [QUIC-Aware Proxying Using HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-quic-proxy/) — This document extends UDP Proxying over HTTP to add optimizations for
   proxied QUIC connections.  Specifically, it allows a proxy to reuse
   UDP 4-tuples for multiple proxied connections, and adds a mode of
   proxying in which QUIC short header packets can be forwarded and
   transformed through an HTTP/3 proxy rather than being fully re-
   encapsulated and re-encrypted.
- **draft-ietf-mimi-protocol-07** (new-draft, score 3, core_identity) [mimi]: [More Instant Messaging Interoperability (MIMI) using HTTPS and MLS](https://datatracker.ietf.org/doc/draft-ietf-mimi-protocol/) — This document specifies the More Instant Messaging Interoperability
   (MIMI) transport protocol, which allows users of different messaging
   providers to interoperate in group chats (rooms), including to send
   and receive messages, share room policy, and add participants to and
   remove participants from rooms.  MIMI describes messages between
   providers, leaving most aspects of the provider-internal client-
   server communication up to the provider.  MIMI integrates the
   Messaging Layer Security (MLS) protocol to provide end-to-end
   security assurances, including authentication of protocol
   participants, confidentiality of messages exchanged within a room,
   and agreement on the state of the room.
- **draft-ietf-mls-targeted-messages-02** (new-draft, score 3, core_identity) [mls]: [Messaging Layer Security (MLS) Targeted Messages](https://datatracker.ietf.org/doc/draft-ietf-mls-targeted-messages/) — This document defines targeted messages for the Messaging Layer
   Security (MLS) protocol.  A targeted message allows a member of an
   MLS group to send an encrypted and authenticated message to another
   member of the same group without creating a new group.  The mechanism
   reuses Hybrid Public Key Encryption (HPKE) and the MLS key schedule
   to provide confidentiality, authentication, and binding to the group
   state.
- **draft-ietf-moq-c4m-02** (new-draft, score 3, authorization) [moq]: [Authorization scheme for MOQT using Common Access Tokens](https://datatracker.ietf.org/doc/draft-ietf-moq-c4m/) — A token-based authorization scheme for use with Media Over QUIC
   Transport.
- **draft-ietf-mpls-algo-mt-oam-01** (new-draft, score 3, core_identity) [mpls]: [LSP Ping/Traceroute for Prefix SID in Multi-Algorithm/Multi-Topology Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-algo-mt-oam/) — [RFC8287] defines the extensions to MPLS LSP Ping and Traceroute for
   Segment Routing IGP-Prefix and IGP-Adjacency Segment Identifier
   (SIDs) with an MPLS data plane.  The machinery defined in [RFC8287]
   works well in single topology, single algorithm deployments where
   each Prefix SID is only associated with a single IP prefix.  In
   multi-topology networks, or networks deploying multiple algorithms
   for the same IP Prefix, MPLS echo request needs to carry additional
   information in the Target FEC Stack sub-TLVs to properly validate IGP
   Prefix SID.

   This document updates [RFC8287] by modifying IPv4 and IPv6 IGP-Prefix
   Segment ID FEC sub-TLVs to also include algorithm identification
   while maintaining backwards compatibility.  This document also
   introduces new Target FEC Stack sub-TLVs for Prefix SID validation in
   multi-topology networks.
- **draft-ietf-netconf-list-pagination-15** (new-draft, score 3, adjacent_watchlist) [netconf]: [List Pagination for YANG-driven Protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination/) — In some circumstances, instances of YANG modeled "list" and "leaf-
   list" nodes may contain numerous entries.  Retrieval of all the
   entries can lead to inefficiencies in the server, the client, and the
   network in between.

   This document defines a model for list pagination that can be
   implemented by YANG-driven management protocols such as NETCONF and
   RESTCONF.  The model supports paging over optionally filtered and/or
   sorted entries.  The solution additionally enables servers to
   constrain query expressions on some "config false" lists or leaf-
   lists.
- **draft-ietf-netconf-notif-envelope-07** (new-draft, score 3, adjacent_watchlist) [netconf]: [Extensible YANG Model for YANG-Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-netconf-notif-envelope/) — This document defines a new extensible Notification structure,
   defined in YANG, for use in YANG-Push Notification messages, both for
   NETCONF and RESTCONF, enabling any YANG-compatible encodings such as
   XML, JSON, or CBOR.  Additionally, it defines two essential
   extensions: an extension to this structure supporting a hostname and
   a sequence number, and an extension to the YANG-Push Notifications
   supporting a timestamp characterizing the moment when the data was
   observed.
- **draft-ietf-netmod-sub-intf-vlan-model-19** (new-draft, score 3, adjacent_watchlist) [netmod]: [Sub-interface VLAN YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-netmod-sub-intf-vlan-model/) — This document defines YANG modules to add support for classifying
   traffic received on interfaces as Ethernet/VLAN framed packets to
   sub-interfaces based on the fields available in the Ethernet/VLAN
   frame headers.  These modules allow configuration of Layer 3 (L3) and
   Layer 2 (L2) sub-interfaces (e.g., L2VPN attachment circuits) that
   can interoperate with IETF based forwarding protocols, such as IP and
   L3VPN services, or L2VPN services like Virtual Private Wire Service
   (VPWS), Virtual Private LAN Service (VPLS), and EVPN.  The sub-
   interfaces also interoperate with VLAN tagged traffic originating
   from an IEEE 802.1Q compliant bridge.

   The model differs from an IEEE 802.1Q bridge model in that the
   configuration is interface/sub-interface based as opposed to being
   based on membership of an 802.1Q VLAN bridge.

   The YANG data models in this document conforms to the Network
   Management Datastore Architecture (NMDA) defined in RFC 8342.
- **draft-ietf-netmod-yang2-01** (new-draft, score 3, adjacent_watchlist) [netmod]: [The YANG 2.0 Data Modeling Language](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/) — YANG is a data modeling language used to model configuration data,
   operational state data, Remote Procedure Calls, and notifications for
   network management protocols.  This document describes the syntax and
   semantics of version 2.0 of the YANG language.  YANG version 2.0 is a
   major release of the YANG language, addressing issues found in the
   original specification.
- **draft-ietf-ntp-ntpv5-10** (new-draft, score 3, adjacent_watchlist) [ntp]: [Network Time Protocol Version 5](https://datatracker.ietf.org/doc/draft-ietf-ntp-ntpv5/) — The Network Time Protocol (NTP) is a widely deployed protocol that
   allows hosts to obtain the current time of day from time servers.
   This document specifies version 5 of the protocol (NTPv5), which
   adopts a client-server model as its sole mode of operation.  Legacy
   operational modes supported in earlier versions have been removed to
   improve protocol robustness and clarity.  While this specification
   defines the protocol used for time distribution, it does not define
   the algorithms or heuristics employed by clients to determine or
   adjust their local time.
- **draft-ietf-opsawg-ipfix-gtpu-19** (new-draft, score 3, core_identity) [opsawg]: [Export of GTP-U Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-gtpu/) — This document specifies IP Flow Information Export (IPFIX)
   Information Elements to report information contained in the Generic
   Packet Radio Service Tunneling Protocol (GTP) User Plane header such
   as Tunnel Endpoint Identifier, and data contained in its session
   container extension header.
- **draft-ietf-radext-epcs-02** (new-draft, score 3, core_identity) [radext]: [RADIUS attributes for National Security and Emergency Preparedness Service](https://datatracker.ietf.org/doc/draft-ietf-radext-epcs/) — This document defines RADIUS attributes for authorizing the use of
   Emergency Preparedness Communication Service (EPCS) priority access
   defined in IEEE 802.11be.  These attributes allow an Identity
   Provider to indicate that an authenticated user is authorized for
   EPCS, enabling the Wi-Fi network provider to apply EPCS priority
   access to the user's Wi-Fi session.  The attributes also support
   RADIUS accounting for Wi-Fi sessions in which EPCS priority access is
   used.
- **draft-ietf-radext-protocol-error-00** (new-draft, score 3, core_identity) [radext]: [Standardising Protocol-Error](https://datatracker.ietf.org/doc/draft-ietf-radext-protocol-error/) — We extend and standardise the Protocol-Error packet Code, first
   defined in RFC 7930 for the Remote Authentication Dial In User
   Service (RADIUS) protocol.
- **draft-ietf-rpp-core-01** (new-draft, score 3, adjacent_watchlist) [rpp]: [RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-ietf-rpp-core/) — This document defines the mapping of the RESTful Provisioning
   Protocol (RPP) to the HTTP protocol.  RPP is used for the
   provisioning and management of objects in a shared database.  The RPP
   data model, consisting of Data Objects and their operations, is
   defined in [I-D.ietf-rpp-data-objects].  This document specifies how
   those Data Objects and operations are mapped to HTTP resources,
   methods, header fields, and status codes, and how RPP servers are
   discovered.  The mapping is independent of the data format used to
   represent RPP messages.
- **draft-ietf-sml-trust-02** (new-draft, score 3, adjacent_watchlist) [sml]: [Trust and security considerations for Structured Email](https://datatracker.ietf.org/doc/draft-ietf-sml-trust/) — This document discusses trust and security considerations for
   structured email and provides recommendations for message user agents
   on how to deal with structured data in email messages.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Structured Email
   Working Group mailing list (sml@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/sml/.

   Source for this draft and an issue tracker can be found at
   https://github.com/arnt/sml-trust.
- **draft-ietf-spring-sr-policy-yang-09** (new-draft, score 3, adjacent_watchlist) [spring]: [YANG Data Model for Segment Routing Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-yang/) — This document defines a YANG data model for Segment Routing (SR)
   Policy that can be used for configuring, instantiating, and managing
   SR policies.  The model is generic and applies equally to the MPLS
   and SRv6 instantiations of SR policies.
- **draft-ietf-spring-stamp-srpm-mpls-13** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document specifies procedures for
   performance measurement in SR-MPLS networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths, including Segment Lists of SR-MPLS Policies, SR-MPLS
   IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths,
   as well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SR-MPLS.
- **draft-ietf-spring-stamp-srpm-srv6-10** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths including Segment Lists of SRv6 Policies, SRv6
   IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SRv6.
- **draft-ietf-stir-certificates-shortlived-07** (new-draft, score 3, core_identity) [stir]: [Short-Lived Certificates for Secure Telephone Identity](https://datatracker.ietf.org/doc/draft-ietf-stir-certificates-shortlived/) — When certificates are used as credentials to attest the assignment of
   ownership of telephone numbers, some mechanism is required to provide
   certificate freshness.  This document specifies short-lived
   certificates as a means of guaranteeing certificate freshness for
   secure telephone identity (STIR), potentially relying on the
   Automated Certificate Management Environment (ACME) or similar
   mechanisms to allow signers to acquire certificates as needed.
- **draft-ietf-suit-update-management-17** (new-draft, score 3, core_identity) [suit]: [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/draft-ietf-suit-update-management/) — This document specifies extensions to the SUIT manifest format.
   These extensions allow a Manifest Author, update distributor, or
   device operator to more precisely control the distribution and
   installation of updates to devices.  These extensions also provide a
   mechanism to inform a management system of Software Identifier and
   Software Bill Of Materials information about an updated device.
- **draft-ietf-tcpm-tcp-ao-algs-09** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC 5926 established a registry of cryptographic algorithms that can
   be used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-ietf-teas-yang-topology-filter-04** (new-draft, score 3, adjacent_watchlist) [teas]: [YANG Data Model for Topology Filter](https://datatracker.ietf.org/doc/draft-ietf-teas-yang-topology-filter/) — This document defines a YANG data model for the management of
   topology filters/filter-sets on network elements and controllers.
- **draft-ietf-tls-extended-key-update-14** (new-draft, score 3, adjacent_watchlist) [tls]: [Extended Key Update for Transport Layer Security (TLS) 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-extended-key-update/) — TLS 1.3 ensures forward secrecy by performing an ephemeral Diffie-
   Hellman key exchange during the initial handshake, protecting past
   communications even if a party's long-term keys (typically a private
   key with a corresponding certificate) are later compromised.

   While the built-in KeyUpdate mechanism allows application traffic
   keys to be refreshed during a session, it does not incorporate fresh
   entropy from a new key exchange and therefore does not provide post-
   compromise security.  This limitation can pose a security risk in
   long-lived sessions, such as those found in industrial IoT or
   telecommunications environments.

   To address this, this specification defines an extended key update
   mechanism that performs a fresh execution of the key exchange
   negotiated during the initial handshake within an active session to
   support post-compromise security.

   By forcing attackers to exfiltrate new key material repeatedly, this
   approach mitigates the risks associated with static key compromise.
   Regular renewal of session keys helps contain the impact of such
   compromises.  The extension is applicable to both TLS 1.3 and DTLS
   1.3.
- **draft-ietf-tls-super-jumbo-record-limit-04** (new-draft, score 3, adjacent_watchlist) [tls]: [Large Record Sizes for TLS and DTLS with Reduced Overhead](https://datatracker.ietf.org/doc/draft-ietf-tls-super-jumbo-record-limit/) — TLS 1.3 records limit the inner plaintext (TLSInnerPlaintext) size to
   2^14 + 1 bytes, which includes one byte for the content type.  DTLS
   1.3 uses the same plaintext size limit.  This document defines a TLS
   extension that allows endpoints to advertise larger per-direction
   maximum inner plaintext sizes, up to 2^30 - 256 bytes, while reducing
   overhead in TLS 1.3 and DTLS 1.3 record headers.
- **draft-ietf-tls-wkech-13** (new-draft, score 3, adjacent_watchlist) [tls]: [A well-known URI for publishing service parameters](https://datatracker.ietf.org/doc/draft-ietf-tls-wkech/) — We define a well-known URI at which an HTTP origin can inform an
   authoritative DNS server, or other interested parties, about its
   Service Bindings.  Service binding data can include Encrypted
   ClientHello (ECH) configurations, that may change frequently.  This
   allows the HTTP origin, in collaboration with DNS infrastructure
   elements, to publish and rotate its own ECH keys.  Other service
   binding data such as information about TLS supported groups is
   unlikely to change quickly, but the HTTP origin is much more likely
   to have accurate information when changes do occur.  Service data
   published via this mechanism is typically available via an HTTPS or
   SVCB resource record.
- **draft-ietf-tsvwg-sctp-dtls-chunk-06** (new-draft, score 3, core_identity) [tsvwg]: [Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/) — This document describes a method for adding Datagram Transport Layer
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
- **draft-ietf-tvr-applicability-02** (new-draft, score 3, adjacent_watchlist) [tvr]: [Applicability of TVR YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-tvr-applicability/) — Time-Variant Routing (TVR) is a routing system that is designed to
   accommodate predicted topology changes caused by internal or external
   factors.  Typical use cases include resource preservation networks,
   operating efficiency networks, and dynamic reachability networks.
   The TVR data model is defined to manage network resources and
   topologies with scheduled attributes.

   This document describes when and which parts of the TVR data model is
   applicable and why.  It also outlines the necessary IETF ancillary
   technologies, operational, and security considerations when deploying
   TVR-based technologies.  Several examples of how to implement the TVR
   scheduling capabilities for key use cases are also provided in this
   document.
- **draft-ietf-vcon-vcon-core-05** (new-draft, score 3, adjacent_watchlist) [vcon]: [The JSON format for vCon - Conversation Data Container](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-core/) — vCon is a standardized framework for the exchange of conversational
   data.  Conversations, which may involve one or more participants,
   occur across a wide variety of modes and application platforms.  This
   document defines a JSON format for representing conversational data,
   encompassing metadata, conversation media, related documents, and
   analysis.  The goal of this standard is to provide an abstracted,
   platform-independent data format for conversations, regardless of the
   mode or application platform.  By doing so, it facilitates the
   integration and seamless exchange of conversational data across
   application platforms, enterprises, and trust boundaries.
- **draft-ietf-webtrans-http2-16** (new-draft, score 3, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/2](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http2/) — WebTransport defines a set of low-level communications features
   designed for client-server interactions that are initiated by Web
   clients.  This document describes a protocol that can provide the
   capabilities of WebTransport over HTTP/2.  This protocol enables the
   use of WebTransport when a UDP-based protocol is not available.
- **draft-irtf-cfrg-bbs-blind-signatures-05** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Blind BBS Signatures](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-blind-signatures/) — This document defines an extension to the BBS Signature scheme that
   supports blind digital signatures, i.e., signatures over messages not
   known to the Signer.
- **draft-irtf-cfrg-bbs-signatures-14** (new-draft, score 3, adjacent_watchlist) [cfrg]: [The BBS Signature Scheme](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) — This document describes the BBS Signature scheme, a secure, multi-
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
- **draft-irtf-cfrg-fiat-shamir-04** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Fiat-Shamir Transformation](https://datatracker.ietf.org/doc/draft-irtf-cfrg-fiat-shamir/) — This document describes the Fiat-Shamir transformation, which allows
   making a public-coin protocol non-interactive by means of a
   cryptographic hash function.

   It specifies how the hash function is employed, how prover messages
   are encoded as hash-function input, and how verifier messages are
   decoded from the hash function's output, as well as the serialization
   and deserialization of the non-interactive argument string.
- **draft-irtf-cfrg-sigma-protocols-04** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Sigma Proofs for Linear Relations](https://datatracker.ietf.org/doc/draft-irtf-cfrg-sigma-protocols/) — This document describes Sigma Protocols for proving knowledge of
   preimages of linear maps in prime-order elliptic curve groups.  These
   are sometimes also called _Maurer Proofs_, or _proofs of knowledge of
   a preimage of a group homomorphism_.

   Examples include zero-knowledge proofs for discrete logarithm
   relations, ElGamal encryptions, Pedersen commitments, and range
   proofs.
- **draft-jadoon-green-sensing-utilization-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Reporting Sensing Utilization Score](https://datatracker.ietf.org/doc/draft-jadoon-green-sensing-utilization/) — This document defines a YANG data model to report a Sensing
   Utilization Score (US) for sensing workloads.  The US is an abstract,
   normalized score (0..100) that summarizes the relative resource cost
   of executing a sensing operation on a device.

   The model supports a mandatory overall US and optional explanatory
   component impact scores (compute, memory, energy, storage, latency).
   The model also supports optional metadata (e.g., timestamp,
   aggregation window, and scoring method identification) describing how
   a reported score was derived.

   The model includes a companion augmentation module that attaches
   sensing utilization telemetry to a GREEN Energy Object, as defined by
   the GREEN Power and Energy YANG Module, for correlation with power
   and energy telemetry.
- **draft-kolomytsev-pshmp-core-overview-01** (new-draft, score 3, core_identity) [none]: [PSHMP Core: A Hybrid L4 Overlay for Proactive Self-Healing and Resilient Multi-Hop Delivery](https://datatracker.ietf.org/doc/draft-kolomytsev-pshmp-core-overview/) — PSHMP Core is a hybrid Layer-4-oriented overlay designed to keep
   multi-hop data delivery working when individual nodes, links, or
   network segments become unstable.  It runs above ordinary IP
   infrastructure and does not require changes to Layer-3 routing.
   Implementations may carry overlay traffic over multiple bidirectional
   transports (for example UDP, DTLS, or TLS-protected TCP); the
   architecture is intentionally transport-agnostic at the edges.

   Under stable conditions the system builds ordered relay chains and
   forwards application fragments hop by hop while preserving fragment
   identity.  When several nodes on a path show degradation, it can
   switch locally into a mesh-style recovery posture: collect
   alternative candidates, apply progressive fallback and diversity
   rules, enforce a quality gate, and replace the affected path.
   Continuous node assessment (K-Factor), a separate load signal,
   diversity-aware selection, failure tracking, gossip and DHT-assisted
   discovery, and batch acknowledgements with gap recovery form the
   supporting mechanisms.

   This document revises [I-D.kolomytsev-pshmp-core-overview] (-00).  It
   clarifies forwarding invariants, separates path recovery from
   fragment recovery, documents load-aware ranking, and strengthens
   security and limitation language.  Scoring weights and thresholds
   remain reference parameters of an experimental codebase; integrators
   may refine them for their topologies.
- **draft-lemmons-cose-composite-claims-04** (new-draft, score 3, verifiable_claims) [none]: [Composite Token Claims](https://datatracker.ietf.org/doc/draft-lemmons-cose-composite-claims/) — Composite claims are claims for CBOR Web Tokens (CWTs) and JSON Web
   Tokens (JWTs) that define logical relationships between sets of
   claims.  This document also defines a CWT representation of the
   "crit" (Critical) claim.
- **draft-lg-bpm-benchmarking-methodology-for-rov-00** (new-draft, score 3, authorization) [none]: [Benchmarking Methodology for Route Origin Validation (ROV)](https://datatracker.ietf.org/doc/draft-lg-bpm-benchmarking-methodology-for-rov/) — This document defines a benchmarking methodology for routers that
   implement Route Origin Validation (ROV).  The methodology focuses on
   device-level behavior, including processing of validated Route Origin
   Authorization (ROA) payload (VRP) updates, the interaction between
   ROV and BGP, resource utilization, and the scalability of ROV under
   varying operational conditions.  The procedures described here follow
   the principles and constraints of the Benchmarking Methodology
   Working Group (BMWG) and are intended to produce repeatable and
   comparable results across implementations.
- **draft-li-cats-context-staging-metric-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model and C-SMA Query Envelopes for Computing-Aware Traffic Steering (CATS) Service Context-Staging Metrics](https://datatracker.ietf.org/doc/draft-li-cats-context-staging-metric-yang/) — This document specifies a Standards Track YANG 1.1 data model (ietf-
   cats-context-staging-metrics) and an on-demand deterministic CBOR
   query envelope for Computing-Aware Traffic Steering (CATS) service
   context-staging latency metrics.  The specification defines three
   explicit observation-endpoint boundaries (transport-submit, remote-
   placement, and consumer-usable), enforces four-tuple snapshot view
   consistency (producer-id, boot-id, view-id, snapshot-id) with clock-
   uncertainty bounds, prohibits direct arithmetic addition of marginal
   latency quantiles across stages, and provides a point-to-point C-SMA
   to C-PS residency lookup envelope that avoids underlay routing
   protocol flooding.
- **draft-li-detnet-preof-loss-matrix-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Pre-Elimination Correlated Loss Matrix and Fate-Sharing OAM in Deterministic Networking (DetNet) PREOF](https://datatracker.ietf.org/doc/draft-li-detnet-preof-loss-matrix-yang/) — This document specifies a Standards Track YANG 1.1 data model (ietf-
   detnet-preof-loss-matrix) for reporting pre-elimination correlated
   packet delivery and co-failure outcomes across Deterministic
   Networking (DetNet) Packet Replication, Ordering, and Elimination
   Functions (PREOF).  Against a closed source-declared packet
   population, the model classifies each original sequence number across
   paired replication branches into a 16-cell joint outcome matrix ({on-
   time, late, missing, indeterminate} x {Branch A, Branch B}) and four
   fate-sharing summary buckets (delivered-both, delivered-a-only,
   delivered-b-only, lost-both), enabling operators to distinguish
   masked single-branch drops from correlated dual-branch failures.
- **draft-li-fann-soft-state-refresh-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [Per-Entry Soft-State Refresh Horizon and Paced Fragmentation Scheduling for Fast Network Notification (FANN) Telemetry](https://datatracker.ietf.org/doc/draft-li-fann-soft-state-refresh-yang/) — This document specifies a Standards Track per-entry soft-state
   refresh horizon profile, a bounded multi-packet fragmentation
   scheduling invariant, and a YANG 1.1 data model (ietf-fann-soft-
   state-refresh) for Fast Network Notification (FANN) link-quality
   telemetry.  To prevent unrefreshed link entries from persisting
   indefinitely when partial event-triggered updates share a transport
   channel with periodic full sweeps, each receiver maintains an
   independent monotonic receipt horizon per six-tuple link-record key.
   Furthermore, when a full periodic sweep spans F fragmented datagrams
   paced at inter-packet interval T_spacing, the refresh period
   T_refresh and expiration horizon T_expire satisfy T_refresh <=
   T_expire - M - (F - 1) * T_spacing.MUST NOT reset the full-sweep
   periodic timer for omitted records.  The refresh bound explicitly
   accounts for multi-packet fragmentation emission duration (T_refresh
   <= T_expire - M - (F - 1) * T_spacing).
- **draft-li-idr-bgp-nrp-02** (new-draft, score 3, core_identity) [none]: [BGP Extensions for Network Resource Partition](https://datatracker.ietf.org/doc/draft-li-idr-bgp-nrp/) — Existing approaches bind a Segment Routing (SR) Policy to a Network
   Resource Partition (NRP) on a one-to-one basis, which lacks
   flexibility and introduces significant operational overhead as the
   number of NRPs scales, especially when multiple NRPs share the same
   SR Policy path.

   This document defines BGP extensions to advertise NRP Identifier (NRP
   ID) information within BGP Update messages between headend and
   endpoint nodes.  It decouples SR Policies from NRPs, allowing
   multiple NRPs to share a common SR Policy path and avoiding linear
   growth of SR Policies.

   The proposed design reduces operational complexity and also applies
   to SR Best Effort (SR BE) scenarios.
- **draft-li-kvcache-efficient-storage-00** (new-draft, score 3, adjacent_watchlist) [none]: [Key-Value (KV) Cache Storage Protocol (KVSP): Indexing, Placement, Prefetch, and Migration for Distributed Inference](https://datatracker.ietf.org/doc/draft-li-kvcache-efficient-storage/) — Large language model inference keeps the attention key-value (KV)
   cache of processed tokens so that they are not recomputed.  When
   inference instances, cache tiers, and schedulers are separate
   components, possibly from different implementers, they need a common
   way to name reusable KV cache blocks, find where copies reside,
   protect copies from eviction while they are being loaded, steer work
   to the instance where loading is cheapest, and move a session to
   another instance after a failure.  This document specifies the KV
   Cache Storage Protocol (KVSP), an HTTP-based protocol that defines a
   compatibility descriptor, keyed block identifiers that bind a block
   to its entire token prefix, a self-describing block container, a
   replica index with layer-granular residency, instance status
   reporting, leased prefetch directives, session checkpoints for
   migration, and a resharding procedure that retains sequence shards in
   place when a parallel group is resized.
- **draft-li-mlc-inference-acceleration-00** (new-draft, score 3, adjacent_watchlist) [none]: [Speculative Decoding Coordination Protocol (SDCP) for Distributed Inference with Multi-Level Caches](https://datatracker.ietf.org/doc/draft-li-mlc-inference-acceleration/) — Speculative decoding accelerates language model inference: a small
   draft model proposes several tokens and the large target model
   verifies them in one forward pass.  In large deployments, draft
   models and the target model run on separate, independently scaled
   instances that exchange state through a multi-level cache.  This
   document specifies the Speculative Decoding Coordination Protocol
   (SDCP), with which a router assigns requests to draft instances by
   load, draft instances submit proposals that reference draft state in
   the cache, and a verifier, the only party that commits output, checks
   proposals under a registered acceptance rule, returns the accepted
   tokens and the next-round speculation limit, and escalates
   persistently rejected sessions to a reduced speculation length,
   another draft model, or decoding by the target model itself depending
   on its load.  SDCP defines a session contract, a committed-prefix
   digest chain, CBOR messages carried over HTTP, idempotent rounds, and
   epoch fencing for recovery.
- **draft-li-opsawg-ipfix-latency-budget-drop-00** (new-draft, score 3, adjacent_watchlist) [none]: [IP Flow Information Export (IPFIX) Information Elements for Bounded-Latency and Residence-Budget Discard Attribution](https://datatracker.ietf.org/doc/draft-li-opsawg-ipfix-latency-budget-drop/) — This document defines IP Flow Information Export (IPFIX) Information
   Elements and a forwardingStatus (IE 89, Status 10b: Dropped) sub-
   reason code for attributing packet discards caused by explicit
   residence-time or delivery-deadline budget expiration in bounded-
   latency data-center and deterministic networks.  The specification
   standardizes primary-cause precedence over competing drop policies,
   clock-uncertainty comparison invariants, zero-count interval
   uncertainty encoding, and deterministic mapping to the IETF device
   packet-discard reporting model.
- **draft-li-opsawg-pipeline-telemetry-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Disaggregated Service Pipeline Timing and Bulk State-Mobility Telemetry](https://datatracker.ietf.org/doc/draft-li-opsawg-pipeline-telemetry-yang/) — This document specifies a Standards Track YANG 1.1 data model (ietf-
   dcn-pipeline-state-telemetry) for monitoring multi-stage execution
   phase timing and bulk state-mobility telemetry in disaggregated data-
   center service pipelines.  The model defines nine causally ordered
   lifecycle timestamps, interval-union de-duplication for overlapping
   pipeline stages, and three-tier byte accounting that separates
   mandatory transport-visible encoded-bytes from optional application-
   visible logical-bytes and metadata-bytes, enabling consistent multi-
   vendor operational diagnostics under the Network Management Datastore
   Architecture (NMDA).
- **draft-liao-cose-c509-pq-algorithms-00** (new-draft, score 3, verifiable_claims) [none]: [Post-Quantum Algorithms for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-cose-c509-pq-algorithms/) — This document registers post-quantum algorithms in the IANA
   registries defined by [I-D.ietf-cose-cbor-encoded-cert].  It extends
   the C509 certificate specification with post-quantum cryptography
   (PQC) signature and key encapsulation algorithms: ML-DSA, FN-DSA, ML-
   KEM, and the stateful hash-based signature algorithms HSS/LMS, XMSS,
   and XMSS^MT, as well as with composite ML-DSA and ML-KEM algorithms,
   which combine a PQC algorithm with a traditional algorithm.
- **draft-lin-idr-bgp-flowspec-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Model for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-flowspec-yang/) — This document defines a YANG data model for the BGP Flow
   Specification (Flowspec) address families (RFC8955 and RFC8956).  The
   model augments the BGP YANG model to add the IPv4 Flow Specification
   (AFI, SAFI = 1, 133) and IPv6 Flow Specification (AFI, SAFI = 2, 133)
   address families, including Flowspec-specific configuration, the Flow
   Specification RIB, and per-neighbor Adj-RIBs.
- **draft-lin-idr-bgp-sr-policy-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Model for BGP Segment Routing Policy](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-sr-policy-yang/) — This document defines a YANG data model for the BGP Segment Routing
   (SR) Policy address families (RFC 9830).  The model augments the BGP
   YANG model to add the IPv4 SR Policy (AFI, SAFI = 1, 73) and IPv6 SR
   Policy (AFI, SAFI = 2, 73) address families, including SR Policy-
   specific configuration, the SR Policy RIB, per-neighbor Adj-RIBs, and
   the decoded SR Policy candidate path information, such as preference,
   Binding SID, and segment lists.
- **draft-lin-rtgwg-srv6-nexthop-yang-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Module for SRv6 Next-Hop RIB Extensions](https://datatracker.ietf.org/doc/draft-lin-rtgwg-srv6-nexthop-yang/) — This document defines a YANG data module for configuring and
   managing SRv6 next hop information for Routing, which augments the
   YANG data model for Routing Management (RFC8349).
- **draft-liu-bpm-aspa-verification-benchmarking-00** (new-draft, score 3, authorization) [none]: [Benchmarking Methodology for ASPA Verification](https://datatracker.ietf.org/doc/draft-liu-bpm-aspa-verification-benchmarking/) — Autonomous System Provider Authorization (ASPA) provides a Resource
   Public Key Infrastructure (RPKI)-based mechanism for verifying the
   Border Gateway Protocol (BGP) AS_PATH attribute to detect route leaks
   and certain forms of AS_PATH manipulation.  The performance of ASPA-
   based AS_PATH verification depends on several factors, including the
   size and structure of ASPA data, AS_PATH characteristics,
   verification procedures, and the interaction between ASPA updates and
   BGP routing operations.  This document defines a benchmarking
   methodology for evaluating ASPA verification implementations on
   routing devices.  The methodology specifies controlled test
   conditions and procedures for measuring ASPA data processing, AS_PATH
   verification performance, route revalidation, BGP convergence,
   scalability, and resource utilization.  The objective is to provide
   repeatable and comparable measurements that characterize the
   performance and operational behavior of ASPA verification under
   varying conditions.
- **draft-liu-cadi-02** (new-draft, score 3, adjacent_watchlist) [none]: [Cryptographic Asset Discovery and Inventory](https://datatracker.ietf.org/doc/draft-liu-cadi/) — This document compiles existing Cryptographic Asset Discovery and
   Inventory (CADI) methods and analyzes potential gaps.  It also
   defines a YANG data model that augments the base network inventory
   model with the cryptographic assets of each network element.  The
   data model is aligned with the Cryptography Bill of Materials (CBOM)
   defined in CycloneDX.
- **draft-ll-binding-sid-replace-00** (new-draft, score 3, core_identity) [none]: [Binding SID Header Replacement (BSHR) for Enhanced Domain Isolation and Overhead Optimization](https://datatracker.ietf.org/doc/draft-ll-binding-sid-replace/) — This document specifies a mechanism for replacing the preceding
   Segment Routing (SR) encapsulation upon the expansion of a Binding
   Segment Identifier (BSID) in SRv6.  The current SR architecture, as
   defined in RFC 8402 (Segment Routing Architecture), RFC 8754 (IPv6
   Segment Routing Header (SRH)), and RFC 8986 (Segment Routing over
   IPv6 (SRv6) Network Programming), mandates that the entire SR policy
   remains intact when a BSID is expanded: the binding node encapsulates
   the packet into a further outer IPv6 header with a new SRH,
   preserving all preceding encapsulations as the inner payload.  This
   imposes significant overhead on scenarios requiring strict domain
   isolation, resource pooling, and future 6G core networks.  This
   proposal, termed "Binding SID Header Replacement" (BSHR), challenges
   the existing standard by allowing the binding node to substitute the
   incoming SR encapsulation with a new one, via a decapsulation-plus-
   re-encapsulation sequence.  This mechanism offers benefits in
   reducing overhead, enforcing security boundaries, and enabling new
   use cases.  The document discusses the technical rationale, potential
   risks including path validation failures, and specifies a new SRv6
   Endpoint behavior, End.B6.Replace, to realize the mechanism.
- **draft-lx-srv6ops-srv6-rate-control-00** (new-draft, score 3, adjacent_watchlist) [none]: [SRv6-based Rate Control](https://datatracker.ietf.org/doc/draft-lx-srv6ops-srv6-rate-control/) — This document describes a deployment model and operational
   considerations for rate control in Segment Routing over IPv6 (SRv6)
   network slices.  It leverages a token-bucket scheduler to
   differentiate Committed Information Rate (CIR) and Peak Information
   Rate (PIR) traffic, and describes how a headend may enforce a rate
   profile on an SR Policy and adjust the PIR based on network
   conditions.  It addresses the operational trade-off between resource
   utilization and congestion avoidance in over-committed slice
   deployments.
- **draft-manelidis-dnsop-domain-affiliation-01** (new-draft, score 3, adjacent_watchlist) [none]: [Domain Affiliation Confirmation (DAC)](https://datatracker.ietf.org/doc/draft-manelidis-dnsop-domain-affiliation/) — Security systems assess domain names one at a time.  A new domain of
   an established organization therefore starts with no reputation, and
   a legitimate domain that resembles another organization's name can be
   reported as an impersonation.  This document defines Domain
   Affiliation Confirmation (DAC), by which the operator of one domain,
   the confirming domain, confirms that another domain, the affiliated
   domain, is operated by it or under its authority.  The two domains
   need not be related in the DNS hierarchy.  The affiliated domain
   publishes a DNS record naming the confirming domain and a random
   token; the confirming domain confirms that token, in the DNS or over
   HTTPS, by naming the affiliated domain.  Verification takes at most
   three DNS queries and one HTTPS request.  The confirming domain
   publishes no list of its domains, and an affiliation is ended by
   deleting one record.  The document also states what a confirmation
   means to relying parties such as takedown services and reputation
   systems.
- **draft-many-tiptop-snmp-profile-01** (new-draft, score 3, adjacent_watchlist) [none]: [SNMP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-snmp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an SNMP profile
   for deep space.  The profile states, for each SNMP version and
   security model, what must be configured, provisioned, or changed, and
   maps their applicability to the deep space connectivity scenarios.
- **draft-martinez-itp-lifecycle-00** (new-draft, score 3, adjacent_watchlist) [none]: [Invoice Trust Protocol (ITP): Lifecycle Status and Payment Information](https://datatracker.ietf.org/doc/draft-martinez-itp-lifecycle/) — This document extends the core of the Invoice Trust Protocol (ITP)
   with commercial, tax, and payment statuses for invoices, a
   deterministic way for both parties to derive the same state from the
   status messages they exchange, payment information for the envelope
   core, and attestations for payment accounts.  Informative appendices
   relate ITP statuses to those of Peppol and of several national
   systems.
- **draft-mcguinness-oauth-cimd-sw-stmt-lifecycle-01** (new-draft, score 3, authorization) [none]: [Client ID Metadata Document Software Statement Lifecycle](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-cimd-sw-stmt-lifecycle/) — This specification defines how a Client ID Metadata Document (CIMD)
   software statement, as defined in a companion specification, is
   withdrawn, superseded, and replaced after an authorization server has
   admitted or registered a client on it.  That specification evaluates
   a statement when a grant is opened, not when it is refreshed.  Under
   this specification, an issuer can withdraw a statement before it
   expires.  Once an authorization server accepts a later statement, the
   issuer's earlier statements about the same software are superseded
   there for new grants and registrations, within the applicable tenant.
   When a grant is refreshed, the authorization server requires a later
   statement in place of one that has been withdrawn, and this
   specification recommends the same for one that has expired.  A
   profile of Token Status List provides withdrawal, and an optional
   Shared Signals Framework event prompts authorization servers to check
   a statement's status.
- **draft-mih-sokolov-cose-deterministic-encodings-00** (new-draft, score 3, verifiable_claims) [none]: [Deterministic Encodings for COSE](https://datatracker.ietf.org/doc/draft-mih-sokolov-cose-deterministic-encodings/) — A COSE Hash Envelope signs the digest of a preimage, not the preimage
   itself.  When the preimage is the encoding of a structured value,
   such as a CBOR data item, and a verifier holds that value but not the
   bytes that were hashed, the verifier has to encode the value again,
   and the digest matches only if it applies the same deterministic
   encoding as the producer.  RFC 8949 describes more than one such
   encoding for the same content type, and the preimage content type
   does not identify which one was applied.  This document defines a
   COSE Hash Envelope protected-header parameter that identifies the
   encoding, and an IANA registry of deterministic encodings whose
   initial entry is the Core Deterministic Encoding Requirements of RFC
   8949.
- **draft-mih-zhang-agent-disclosure-bundle-02** (new-draft, score 3, verifiable_claims) [none]: [AAC Evidence Bundle](https://datatracker.ietf.org/doc/draft-mih-zhang-agent-disclosure-bundle/) — This document defines the AAC Evidence Bundle, a portable
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
- **draft-mpsb-agntcy-slim-03** (new-draft, score 3, adjacent_watchlist) [none]: [Secure Low-Latency Interactive Messaging (SLIM)](https://datatracker.ietf.org/doc/draft-mpsb-agntcy-slim/) — This document specifies the Secure Low-Latency Interactive Messaging
   (SLIM), a protocol designed to support real-time interactive AI
   applications at scale.  SLIM provides a name-routed messaging data
   plane and session layer for agent protocols such as A2A and MCP.  The
   data plane carries Protocol Buffers messages over streaming gRPC on
   HTTP/2 or WebSocket, while the session layer provides point-to-point
   and group communication, configurable reliable delivery, and optional
   end-to-end encryption using MLS.  SLIM also defines link negotiation
   between routing nodes and control messages for session establishment
   and group membership.
- **draft-netana-netmod-yang-anydata-validation-00** (new-draft, score 3, adjacent_watchlist) [none]: [Validating anydata in YANG Library context](https://datatracker.ietf.org/doc/draft-netana-netmod-yang-anydata-validation/) — The YANG "anydata" statement carries data whose data model is not
   known when the module is designed.  This document defines the context
   that is needed to validate such content: the schema context, the
   "anydata" node, a schema anchor, and the datastore.  It describes how
   this context is obtained for the uses of "anydata" in IETF YANG
   modules, how the schema node of each node in the content is found,
   and which YANG constraints are checked.
- **draft-netana-nmop-message-broker-bmp-telemetry-msg-05** (new-draft, score 3, adjacent_watchlist) [none]: [BMP YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-netana-nmop-message-broker-bmp-telemetry-msg/) — This document defines an extensible message schema in YANG to be used
   at BMP collectors to transform BMP messages into messages which are
   consumed by external systems such as Message Brokers.
- **draft-newbold-atp-aturi-01** (new-draft, score 3, core_identity) [none]: [The "at" Identifier Scheme](https://datatracker.ietf.org/doc/draft-newbold-atp-aturi/) — This document defines the "at" identifier scheme, which is used to
   reference accounts and data records in the Authenticated Transfer
   Protocol.
- **draft-nottingham-problem-header-00** (new-draft, score 3, adjacent_watchlist) [none]: [The Problem-Details HTTP Header Field](https://datatracker.ietf.org/doc/draft-nottingham-problem-header/) — This specification defines the Problem-Details HTTP header field,
   which carries a problem details object (RFC 9457) as a Structured
   Field.  Because the Structured Fields data model is more constrained
   than JSON's, it also defines a profile that problem types can opt
   into so that they can be serialised as a header.
- **draft-pauly-independent-submission-restructure-00** (new-draft, score 3, adjacent_watchlist) [none]: [Independent Submission Board Model](https://datatracker.ietf.org/doc/draft-pauly-independent-submission-restructure/) — The Independent Submission stream is one of the stream producers that
   create draft RFCs.  This document proposes the creation of the
   Independent Submission Board (ISB), a small board appointed by both
   the IAB and IESG, that acts as the stream approver.  The ISB is
   responsible for activities within the Independent Submission stream,
   works with draft editors and reviewers, and interacts with the RFC
   Production Center and Publisher, and the RFC Series Editor (RSE).

   If approved, this proposal would obsolete RFC 8730, which defines a
   single Independent Submission Editor.
- **draft-pham-cfrg-hiae-07** (new-draft, score 3, core_identity) [none]: [The HiAE Authenticated Encryption Algorithm](https://datatracker.ietf.org/doc/draft-pham-cfrg-hiae/) — This document describes HiAE, a high-throughput authenticated
   encryption with associated data (AEAD) algorithm.  It targets next-
   generation wireless systems (6G) and high-speed data transmission
   applications.  This document also specifies its use as a stream
   cipher and a message authentication code (MAC).

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/hiae-aead/draft-pham-hiae.
- **draft-porfiri-tsvwg-sctp-dtls-handshake-03** (new-draft, score 3, core_identity) [none]: [Transport Layer Security (TLS) based Key Management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/) — This document defines how Transport Layer Security (TLS) 1.3 is used
   as a key management method for the SCTP DTLS Chunk mechanism.  It
   specifies how a TLS handshake establishes the initial security
   context for an SCTP association and how subsequent TLS handshakes
   provide key updates and re-authentication.  The goal is to enable
   authenticated and confidential communication over SCTP using the DTLS
   Chunk, leveraging standardized TLS 1.3 features for key management
   and rekeying.
- **draft-ramadan-mboned-mcast-manifest-01** (new-draft, score 3, core_identity) [none]: [Signed Digest Manifests for Multicast Datagram Authentication](https://datatracker.ietf.org/doc/draft-ramadan-mboned-mcast-manifest/) — This document defines a format for authenticating UDP datagrams
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
- **draft-ramadan-moq-fec-block-codes-00** (new-draft, score 3, core_identity) [none]: [Block FEC Schemes for Media over QUIC: Reed-Solomon and RaptorQ](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-block-codes/) — This document specifies two block Forward Error Correction (FEC)
   schemes for the FEC mechanism of Media over QUIC (MoQ): the
   systematic Reed-Solomon erasure code over GF(2^8) of ISO/IEC
   23008-10, which is mandatory to implement, and RaptorQ (RFC 6330),
   which is optional.  For each scheme it gives the registered
   identifier, the derivation of the decoder's parameters from the
   instance's configuration and the Repair FEC Payload ID with no in-
   session signaling, the bounds on block size and symbol size, the
   decoding overhead, and how the scheme supports repair layers.  It
   restates the Reed-Solomon code and gives test vectors for it.
- **draft-ramadan-moq-fec-catalog-00** (new-draft, score 3, adjacent_watchlist) [none]: [Catalog Binding for Forward Error Correction in Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-catalog/) — This document binds the Forward Error Correction (FEC) configuration
   data model of the MoQ FEC core mechanism to the catalog of the MOQT
   Streaming Format (MSF) and to its Common Media Application Format
   (CMAF) profile.  It defines the track-level "fec" array of FEC
   instance objects, the fields with which a repair track or a symbol
   track describes its own role, the packaging values "fec-repair" and
   "fec-source", the validation rules that are specific to the catalog
   encoding, and the handling of unknown keys, so that a receiver that
   obtains a track's catalog entry can configure its decoder without in-
   session signaling.
- **draft-ramadan-moq-multicast-02** (new-draft, score 3, core_identity) [none]: [Multicast Delivery and Endpoint Discovery for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-multicast/) — This document specifies multicast delivery mechanisms and catalog-
   based endpoint discovery for Media over QUIC (MoQ).  It defines how
   MoQ sessions integrate with IP multicast (SSM, ASM), Automatic
   Multicast Tunneling (AMT), and TreeDN for scalable live streaming.
   The specification includes a multicast catalog extension for endpoint
   discovery and multi-path delivery across TV, mobile, and browser
   platforms.  All multicast media delivery uses MPEG Media Transport
   Protocol (MMTP) packets, the same packet format that MoQ objects
   carry on QUIC streams.  A manifest-based content-authentication
   profile protects multicast delivery with signed manifest records that
   travel in band beside those packets.
- **draft-richter-webtransport-websocket-06** (new-draft, score 3, adjacent_watchlist) [none]: [WebTransport over WebSocket](https://datatracker.ietf.org/doc/draft-richter-webtransport-websocket/) — WebTransport [OVERVIEW], a protocol framework within the Web security
   model, empowers Web clients to initiate secure multiplexed transport
   for low-level client-server interactions with remote servers.  This
   document outlines a protocol, based on WebSocket [WEBSOCKET],
   offering WebTransport capabilities similar to the HTTP/2 variant
   [WEBTRANSPORT-H2].  It serves as an alternative when UDP-based
   protocols are inaccessible, and the client environment exclusively
   supports WebSocket [WEBSOCKET].
- **draft-riedl-moq-ad-creative-signaling-01** (new-draft, score 3, core_identity) [none]: [Ad Creative Signaling over the MSF Event Timeline](https://datatracker.ietf.org/doc/draft-riedl-moq-ad-creative-signaling/) — This document defines the carriage of ad creative signaling --
   creative identity, tracking events, and measurement verification
   metadata as specified by SVTA 2053-1 -- in records on a Media over
   QUIC (MOQT) Streaming Format (MSF) Event Timeline track.  It
   complements the carriage of SCTE-35 splice signaling over the same
   mechanism: splice events describe where placement opportunities occur
   on a media timeline, while the event class defined here describes the
   creatives that fill them and how their playback is to be measured.
   This binding is the MSF counterpart of the DASH and HLS carriage
   bindings defined by SVTA 2053-1, which defines none for MOQT.
- **draft-rosenberg-diem-architecture-01** (new-draft, score 3, adjacent_watchlist) [none]: [Digital Emblems - Architectural Considerations](https://datatracker.ietf.org/doc/draft-rosenberg-diem-architecture/) — This document describes an architecture for digital emblems in which
   emblems are authenticated, typed metadata about assets, published in
   the DNS and protected by DNSSEC.  A single architecture serves many
   use cases.  Use cases differ in the shape of their metadata, which is
   described by profiles, rather than in their transport or trust
   machinery.  The document illustrates the architecture with a strawman
   encoding (an EMBLEM resource record carrying a deterministic CBOR map
   with registered, typed keys) and with worked examples drawn from
   International Humanitarian Law, logistics and customs, diplomatic
   pouches, and peacekeeping.
- **draft-sardar-rats-sec-cons-08** (new-draft, score 3, trust_infrastructure) [none]: [Guidelines for Security Considerations of RATS](https://datatracker.ietf.org/doc/draft-sardar-rats-sec-cons/) — This document aims to provide guidelines and best practices for
   writing security considerations for technical specifications for RATS
   targeting the needs of implementers, researchers, and protocol
   designers.  In particular, it discusses some of the 'bottom turtle'
   issues.  This is a work-in-progress, and the current version mainly
   presents an outline of the general security guidelines, baseline, or
   template for RATS that future versions will cover in more detail.
- **draft-selma-lake-additional-messages-00** (new-draft, score 3, authorization) [none]: [Additional Messages in Lightweight Authenticated Key Exchange (LAKE)](https://datatracker.ietf.org/doc/draft-selma-lake-additional-messages/) — The Lightweight Authenticated Key Exchange (LAKE) protocol supports
   methods with different numbers of messages and different security
   properties.  The methods defined in the original specification, RFC
   9528, consist of three mandatory messages and an optional fourth
   message.  This document defines a generic mechanism for additional
   protected messages, message_n, where n is greater than the highest
   message number defined for the method in use.  The format of each
   message_n is identical to that of message_4 in RFC 9528, except that
   its encryption key and initialization vector are derived using the
   LAKE_Exporter.  This mechanism allows applications to include any
   number of additional protected messages in a LAKE session, for
   example, to carry additional External Authorization Data (EAD) and to
   convey protected success indications when required by a method or
   deployment, such as EAP-LAKE.  This document updates RFC 9528.
- **draft-sheffer-tls-pq-hsts-00** (new-draft, score 3, adjacent_watchlist) [none]: [An HSTS-like Header for Secure PQ Migration](https://datatracker.ietf.org/doc/draft-sheffer-tls-pq-hsts/) — This document defines an HTTP response header field, Require-PQ-Auth,
   that instructs user agents to require a quantum-resistant certificate
   chain in subsequent connections.  This is a short-term, opt-in
   mechanism for HTTP origins to protect against legacy classical trust
   anchors.  It will become unnecessary when UAs remove these trust
   anchors.
- **draft-skyfire-oauth-kyapay-token-exchange-02** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-slutsky-homing-pigeon-03** (new-draft, score 3, authorization) [none]: [Homing Pigeon Message Protocol, Version 1](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon/) — This document specifies the Homing Pigeon message protocol, version
   1: signed JSON job and result objects exchanged over a transport
   binding.  On the email binding, a submitter sends one HMAC-SHA-384
   signed JSON object to a mailbox; a runner polls that mailbox,
   verifies the signature, executes the job, and returns a signed
   result; the other bindings carry the same objects unchanged.  The
   signature is the only authorization.  The job object is protected end
   to end by per-job AEAD encryption, a required part of the protocol:
   implementations MUST support it, the reference software sends
   encrypted by default, and a receiver refuses a cleartext job unless
   the operator has explicitly enabled cleartext acceptance - in the
   reference software, only by a command-line parameter.  The store-and-
   forward bindings open no inbound listener on the host that runs the
   job.

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
- **draft-slutsky-homing-pigeon-v2-03** (new-draft, score 3, adjacent_watchlist) [none]: [Homing Pigeon Message Protocol, Version 2: Determinations, Questions, and Shared Context](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon-v2/) — This document specifies version 2 of the Homing Pigeon message
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
- **draft-su-sidrops-rpki-rp-incremental-validation-01** (new-draft, score 3, adjacent_watchlist) [none]: [Considerations for Incremental Validation in RPKI Relying Parties](https://datatracker.ietf.org/doc/draft-su-sidrops-rpki-rp-incremental-validation/) — RPKI Relying Parties (RPs) synchronize repository data and validate
   RPKI objects to produce validated payloads.  Incremental repository
   synchronization can reduce data transfer, but it does not necessarily
   reduce validation work.  After a repository update, an RP may repeat
   parsing, cryptographic verification, and other validation processing
   for objects whose relevant inputs have not changed.  This repeated
   work can increase validation latency and resource consumption,
   particularly as the RPKI data set grows and as future cryptographic
   transitions, including a possible transition to post-quantum
   cryptography (PQC), change processing costs.  This document describes
   the operational problem and design space for incremental validation
   in RPs and discusses general correctness and security considerations
   for reusing previously computed validation state.  For the same
   repository snapshot, trust anchor set, validation policy, validation
   time, and applicable RPKI validation rules, incremental validation is
   expected to produce the same validated payload output as full
   validation.  This document does not specify a particular algorithm or
   cache structure, modify RPKI object formats or repository
   synchronization protocols, change existing validation semantics, or
   require RPs to implement incremental validation.
- **draft-sullivan-cfrg-raae-04** (new-draft, score 3, core_identity) [none]: [Random-Access Authenticated Encryption](https://datatracker.ietf.org/doc/draft-sullivan-cfrg-raae/) — This document defines random-access authenticated encryption (raAE),
   a primitive that partitions a message into an indexed sequence of
   segments that can be encrypted and decrypted independently and in any
   order.  It also specifies SEAL (Segmented Encryption and
   Authentication Layer), a parameterized construction that defines a
   family of concrete raAE instantiations, one for each valid choice of
   an Authenticated Encryption with Associated Data (AEAD) algorithm, a
   key derivation function (KDF), and associated parameters.

   SEAL supports immutable (write-once), append-only, and mutable (in-
   place ciphertext rewrite) operations, each with per-segment
   authentication.  A separately configured snapshot authenticator can
   additionally authenticate the complete, indexed segment set.

   The document also defines the security notions of raAE, specifies the
   requirements for conforming constructions, and analyzes SEAL against
   those requirements.  Concrete cipher suites, serialization layouts,
   and test vectors for SEAL are specified in a companion document.
- **draft-sullivan-seal-concrete-01** (new-draft, score 3, core_identity) [none]: [SEAL Cipher Suites and Instantiations](https://datatracker.ietf.org/doc/draft-sullivan-seal-concrete/) — SEAL (Segmented Encryption and Authentication Layer) is a
   construction that realizes random-access authenticated encryption
   (raAE), a primitive that partitions a message into an indexed
   sequence of independently accessible, individually authenticated
   segments.  This document specifies concrete, interoperable
   instantiations of SEAL for particular uses, built from previously
   specified primitives, and applies the analysis in a companion
   document to state their security properties and safe usage limits.
- **draft-sun-nmrg-hybrid-switching-15** (new-draft, score 3, adjacent_watchlist) [none]: [Resource Allocation Model for Hybrid Switching Networks](https://datatracker.ietf.org/doc/draft-sun-nmrg-hybrid-switching/) — The fast increase in traffic volumn within and outside Datacenters is
   placing an unprecendented challenge on the underline network, in both
   the capacity it can provide, and the way it delivers traffic.  When a
   large portion of network traffic is contributed by large flows,
   providing high capacity and slow to change optical circuit switching
   along side fine-granular packet services may potentially improve
   network utility and reduce both CAPEX and OpEX.  This gives rise to
   the concept of hybrid switching - a paradigm that seeks to make the
   best of packet and circuit switching.

   However, the full potential of hybrid switching networks (HSNs) can
   only be realized when such a network is optimally designed and
   operated, in the sense that "an appropriate amount of resource is
   used to handle an appropriate amount of traffic in both switching
   planes."  The resource allocation problem in HSNs is in fact complex
   ineractions between three components: resource allocation between the
   two switching planes, traffic partitioning between the two switching
   planes, and the overall cost or performance constraints.

   In this memo, we explore the challenges of planning and operating
   hybrid switching networks, with a particular focus on the resource
   allocation problem, and provide a high-level model that may guide
   resource allocation in future hybrid switching networks.
- **draft-tiloca-core-oscore-piv-enc-04** (new-draft, score 3, core_identity) [none]: [Stand-in Key Identifier and Encrypted Partial IV in the Constrained Application Protocol (CoAP) OSCORE Option](https://datatracker.ietf.org/doc/draft-tiloca-core-oscore-piv-enc/) — The security protocol Object Security for Constrained RESTful
   Environments (OSCORE) provides end-to-end protection of messages
   exchanged with the Constrained Application Protocol (CoAP).  Messages
   protected with OSCORE include a CoAP OSCORE Option, where the
   "Partial IV" field specifies the sequence number value used by the
   message sender and the "kid" field specifies the identifier of the
   message sender.  In order to reduce the information exposed on the
   wire that can be used for fingerprinting traffic and for tracking
   endpoints, this document defines a lightweight add-on method that
   obfuscates certain fields of the OSCORE Option, by encrypting the
   "Partial IV" field and overwriting the "kid" field with a stand-in
   identifier.  Therefore, it updates RFC 8613.  With minor adaptations,
   the defined method is applicable also to the security protocol Group
   Object Security for Constrained RESTful Environments (Group OSCORE)
   that protects group communication for CoAP.
- **draft-toomim-httpbis-braid-subscriptions-00** (new-draft, score 3, authorization) [none]: [Subscriptions for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-subscriptions/) — Servers respond to an HTTP GET with a resource's current state.
   However, if the resource changes afterward, HTTP has no way for the
   server to notify its client of the new version.  This document
   defines subscriptions.  When a client adds the Subscribe header to a
   GET, the server responds with the resource's current state, and then
   continues to respond as subsequent changes occur.  Each response
   corresponds to a semantically-equivalent GET, so that content
   negotiation, authorization, and caching work as they do for any GET
   request.

   When a server grants a subscription, it promises to send each change
   as it happens.  So once a client is caught up, and while its
   connection is alive, it knows that nothing has changed until the next
   response arrives.  The server tells the client when the client has
   caught up with the origin server's current version, and sends
   heartbeats to show that the connection is alive.  If a cache holds
   such a subscription, it knows at every moment that its stored copy is
   current, and can respond to requests with the copy, without asking
   the origin server.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toutain-schc-rfc9363bis-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Static Context Header Compression (SCHC)](https://datatracker.ietf.org/doc/draft-toutain-schc-rfc9363bis/) — This document describes a YANG data model for the Static Context
   Header Compression (SCHC) compression and fragmentation Rules.

   This document formalizes the description of the Rules for better
   interoperability between SCHC instances either to exchange a set of
   Rules or to modify the parameters of some Rules.

   This document updates the SCHC data model defined in RFC 9363 to take
   into account the evolution of SCHC usages.  It introduces a flexible
   way to describe protocol options, such as the CoAP options, and
   includes the identifiers needed for the compression of ICMPv6 and
   features for the management of the Rules.
- **draft-tschofenig-emu-pqpake-00** (new-draft, score 3, core_identity) [none]: [The EAP-PQPAKE Authentication Method](https://datatracker.ietf.org/doc/draft-tschofenig-emu-pqpake/) — This document defines EAP-PQPAKE, an Extensible Authentication
   Protocol (EAP) method that uses a hybrid post-quantum password-
   authenticated key exchange.  The method is based on the CPaceOQUAKE+
   asymmetric PAKE and provides mutual authentication and EAP key export
   from a password without requiring public-key certificates during
   normal authentication.
- **draft-usama-tls-fatt-extension-11** (new-draft, score 3, adjacent_watchlist) [none]: [Proposed Document Template for TLS FATT Process](https://datatracker.ietf.org/doc/draft-usama-tls-fatt-extension/) — This document applies only to non-trivial extensions of TLS, which
   require formal analysis.  FATT process has successfully discovered
   CVEs of *CVSS 7.5* and most recently expected *CVSS 9.1* in the
   *production* implementations of the drafts proposed for adoption in
   the TLS WG.  To achieve high cryptographic assurances, this document
   proposes the drafts specify a clear threat model and informal
   security goals in the Security Considerations section, as well as
   motivation and a protocol diagram in the draft.
- **draft-wang-cfrg-key-combiners-02** (new-draft, score 3, core_identity) [none]: [HMAC Based Hybrid Key Combiners for Multiple Keys](https://datatracker.ietf.org/doc/draft-wang-cfrg-key-combiners/) — As a fundamental building block in security protocols, a key combiner
   is used to combine two or more input cryptographic keys, some
   potentially compromised, into a single pseudorandom output key.  Most
   of the existing key combiners are for two input keys.  This draft
   specifies two provably secure constructions of key combiners for
   multiple keys [WWW25], which is particularly useful in post-quantum
   migration where multiple input keys may be produced by different
   algorithms or even different approaches [RFC9370], [ETSI25].  Namely,
   here the input keys can be two or more, and the combined output key
   remains pseudorandom if at least one of the input keys is secure,
   i.e., uniformly random and unknown to an attacker.  The two
   constructions, called HKCv1 and HKCv2, are based on the extract-then-
   expand paradigm of HMAC (Keyed-Hashing for Message Authentication)
   [RFC2104].  HKCv1 is designed for simultaneously available input keys
   using concatenation, while HKCv2 is tailored for scenarios where
   input keys arrive incrementally, using an iterative HMAC structure.
- **draft-watts-authorization-noncollapse-semantics-01** (new-draft, score 3, authorization) [none]: [Non-Collapse Semantics for Authorization, Evidence, and Execution State](https://datatracker.ietf.org/doc/draft-watts-authorization-noncollapse-semantics/) — Distributed authorization systems frequently combine observations,
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
- **draft-watts-research-artifact-provenance-01** (new-draft, score 3, trust_infrastructure) [none]: [Research Artifact Provenance and Corrigible Scientific State](https://datatracker.ietf.org/doc/draft-watts-research-artifact-provenance/) — This document describes a protocol-neutral pattern for content-
   addressed research artifacts, append-only evidence history, explicit
   epistemic classes, and corrigible active scientific state.  It
   separates byte integrity from numerical correctness, empirical
   adequacy, mechanism identification, and release authority.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-research-evidence-bundle-01** (new-draft, score 3, trust_infrastructure) [none]: [A Research Evidence Bundle JSON Envelope for Provenance and Replication Metadata](https://datatracker.ietf.org/doc/draft-watts-research-evidence-bundle/) — This document proposes an early-stage JSON envelope for exchanging
   research-evidence records containing claim status, evidence tier,
   source provenance, methods, falsifiers, replication status, artifact
   digests, and privacy review.  It is an individual design proposal,
   not an IETF consensus document.  Its intended contribution must be
   assessed against existing provenance and research-packaging
   specifications before further standardization work.
- **draft-watts-research-evidence-envelope-01** (new-draft, score 3, trust_infrastructure) [none]: [Research Evidence Envelope: A Provenance-Oriented Interchange Record](https://datatracker.ietf.org/doc/draft-watts-research-evidence-envelope/) — This informational scaffold sketches a versioned record for tracking
   scientific claims, source provenance, evidence classes, uncertainty,
   falsifiers, replication procedures, and artifact hashes.  It is not
   an IETF standard, has not undergone IETF review, and does not define
   a wire protocol.
- **draft-watts-research-intelligence-archive-01** (new-draft, score 3, trust_infrastructure) [none]: [Evidence-Bounded Research Intelligence Archives](https://datatracker.ietf.org/doc/draft-watts-research-intelligence-archive/) — This unsubmitted working draft defines an evidence-bounded archive
   profile for scientific and technical claims, sources, evidence tiers,
   falsifiers, tests, provenance, publication state, and integrity
   manifests.  The profile is designed to prevent archival or mechanical
   integrity from being misread as empirical validity, novelty, peer
   review, standards approval, or publication acceptance.  This file is
   an archival RFCXML working draft and has no IETF standing unless
   separately submitted.
- **draft-watts-unison-state-preservation-01** (new-draft, score 3, trust_infrastructure) [none]: [State-Preserving Exchange of Evaluation Evidence](https://datatracker.ietf.org/doc/draft-watts-unison-state-preservation/) — This unsubmitted working draft describes state-preservation semantics
   derived from UNISON-StateBench.  It separates value, epistemic
   status, provenance, and authority; defines a non-collapse rule for
   operational and epistemic transitions; and describes representation,
   contradiction, missing-evidence, authority, principal-isolation,
   tool-state, context-distance, and controlled-mutation evaluation
   families.  This file is an archival RFCXML working draft and is not
   an IETF submission.
- **draft-watts-verification-defect-quarantine-01** (new-draft, score 3, adjacent_watchlist) [none]: [Verification Defect Quarantine for Protocol Conformance Systems](https://datatracker.ietf.org/doc/draft-watts-verification-defect-quarantine/) — Protocol conformance systems commonly treat a published test vector
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
- **draft-watts-verification-promotion-boundaries-01** (new-draft, score 3, authorization) [none]: [Verification Promotion Boundaries for Protocol Implementations](https://datatracker.ietf.org/doc/draft-watts-verification-promotion-boundaries/) — Protocol implementations frequently combine specification checks,
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
- **draft-watts-veriflow-evidence-envelope-01** (new-draft, score 3, trust_infrastructure) [none]: [Veriflow Evidence Envelope for Source-Grounded Computational Claims](https://datatracker.ietf.org/doc/draft-watts-veriflow-evidence-envelope/) — This document specifies an experimental, JSON-based evidence envelope
   for exchanging source-grounded computational assertions, including
   provenance, reproducible operation identifiers, evidence sufficiency,
   and explicit abstention when an answer is not supported.  The
   envelope separates syntactic validity, source integrity, mathematical
   correctness, and empirical truth.  This document does not standardize
   a general scientific inference engine or claim experimental
   superiority.
- **draft-wendt-sipcore-tls-updates-00** (new-draft, score 3, core_identity) [none]: [TLS 1.3 and Certificate Identity for the Session Initiation Protocol](https://datatracker.ietf.org/doc/draft-wendt-sipcore-tls-updates/) — The specifications that define the use of TLS with the Session
   Initiation Protocol (SIP) predate TLS 1.3 and the current guidance
   for representing and verifying the identity of a service in a
   certificate.  As a result, [RFC3261] states a mandatory cipher suite
   that a TLS 1.3 implementation cannot offer, and the certificate
   identity rules of [RFC5922] are no longer consistent with [RFC9525].
   This document updates both, specifying a TLS version and cipher suite
   baseline for SIP and revising the representation and matching of SIP
   domain identities in certificates.
- **draft-westerlund-moq-overview-02** (new-draft, score 3, adjacent_watchlist) [none]: [Media over QUIC Overview](https://datatracker.ietf.org/doc/draft-westerlund-moq-overview/) — This document provides a high-level overview of the Media over QUIC
   (MoQ) protocol suite.  It describes the architecture, data model,
   transport protocol, streaming formats, and security mechanisms that
   together enable scalable low-latency media delivery over the
   Internet.  The document explains how these components relate to each
   other and how they are composed to create interoperable media
   applications.
- **draft-wobbly-dispatch-embedded-answers-00** (new-draft, score 3, adjacent_watchlist) [none]: [DNS Embedded Answers](https://datatracker.ietf.org/doc/draft-wobbly-dispatch-embedded-answers/) — Many web interactions require a client to resolve a hostname before
   it can establish a connection to a service.  While DNS is generally
   efficient, each lookup incurs some delay and exposes information
   about the user's browsing activity to the recursive resolver and
   upstream infrastructure.  This document explores techniques by which
   a client may receive DNS-derived address data as part of an
   application-layer response, so that it can initiate a connection
   without performing a separate DNS lookup for the same target.

   The mechanisms discussed here are intended to reduce lookup latency
   and potentially improve privacy, but they also raise significant
   questions about trust, freshness, and security.  The document does
   not prescribe a single normative mechanism; instead, it describes
   several design options and the trade-offs associated with each.
- **draft-wu-idr-flowspec-yang-cfg-04** (new-draft, score 3, adjacent_watchlist) [idr]: [A YANG Data Model for Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-yang-cfg/) — This document defines a YANG data model for Flow Specification
   implementations.  The data model includes configuration data and
   state data.
- **draft-xie-dkim-sm2-sm3-00** (new-draft, score 3, core_identity) [none]: [DomainKeys Identified Mail (DKIM) Signatures with SM2 and SM3 Cryptographic Algorithms](https://datatracker.ietf.org/doc/draft-xie-dkim-sm2-sm3/) — This document adds the SM2-SM3 signing algorithm to DomainKeys
   Identified Mail (DKIM).  It defines the signature and public key
   encodings and the SM2 user identifier used with this algorithm.  This
   document updates RFC 6376.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Comments on this individual Internet-Draft are welcome.  Please send
   feedback to the authors using the contact information at the end of
   this document.
- **draft-yang-opsawg-pfc-queue-telemetry-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for PFC Queue Telemetry](https://datatracker.ietf.org/doc/draft-yang-opsawg-pfc-queue-telemetry/) — This document defines a YANG data model for completed, per-queue
   observations of backlog and received Priority-based Flow Control
   (PFC) gating.  Each record identifies a monotonic measurement
   interval, queue mapping epoch, measurement method, and absolute error
   bound.  The model makes repeated reads, missing coverage, and
   weighted aggregation explicit.

   The measured overlap does not identify the sole cause of queueing
   delay and does not change PFC, packet scheduling, or ECN marking.
   The module augments interface operational state and defines no
   configuration or notification interface.
- **draft-yang-rtgwg-ecn-threshold-policy-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for ECN Threshold Policies](https://datatracker.ietf.org/doc/draft-yang-rtgwg-ecn-threshold-policy/) — This document defines administrative limits and operational state for
   local ECN threshold adaptation on queues using a single byte-based
   Random Early Detection (RED) profile.  It augments the QoS queue
   template model with policy bounds and the interface model with
   confirmed per-queue state.

   The policy constrains both RED thresholds, preserves the configured
   ramp width, and specifies quantization, input validity, transition,
   and fallback behavior.  It does not select a learning algorithm,
   modify ECN codepoints, reserve physical buffer capacity, or guarantee
   congestion-control stability or lossless delivery.
- **draft-yoon-bpm-pm-capabilities-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Performance Monitoring (PM) Capabilities](https://datatracker.ietf.org/doc/draft-yoon-bpm-pm-capabilities/) — This document defines a YANG data model, "ietf-pm-capabilities", that
   enables a server to advertise which sampling and collection
   intervals, measurement methods, and collection types it supports for
   each performance monitoring (PM) parameter.  A client reads this
   capability information before configuring PM collection, so that it
   selects only values that the server can honour.  The capabilities are
   advertised by augmenting the "ietf-system-capabilities" module
   defined in [RFC9196], so that a client discovers them at the same
   well-known location used for subscription and notification
   capabilities.  The model imports the "profile-names" and "collection-
   type" types and the "performance-parameter" and "measurement-method"
   identities from the companion PM collection model defined in
   [I-D.yoon-bpm-pm-collection] and mirrors its profile-and-parameter
   structure, ensuring direct alignment between capability discovery and
   collection configuration.  The model does not define collection data
   structures or any delivery mechanism; those are defined in the
   companion document.
- **draft-yoon-bpm-pm-collection-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Performance Monitoring (PM) Collection](https://datatracker.ietf.org/doc/draft-yoon-bpm-pm-collection/) — This document specifies a YANG data model for the collection of
   Performance Monitoring (PM) data, based on the collection
   requirements of the performance management function defined in ITU-T
   G.7710.  The model processes raw performance data sampled at a
   network node and produces structured data that can be retrieved by
   clients via pull-based mechanisms or delivered via push-based
   mechanisms such as YANG-Push.  This document does not define new
   performance metrics; the base metrics are those of the IPPM
   framework, and the model specifies the collection and exposure of the
   operationally important subset.
- **draft-yoshikawa-sidrops-pqc-rpki-03** (new-draft, score 3, authorization) [none]: [Post-Quantum Signature Experiments and Migration Considerations for the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-yoshikawa-sidrops-pqc-rpki/) — This document reports experiments with post-quantum signature
   algorithms and analyzes migration approaches for the Resource Public
   Key Infrastructure (RPKI).  The experiments compare classical, post-
   quantum, and composite signature candidates; generate and validate
   RPKI-profiled certificate, CRL, manifest, and ROA test objects;
   compare separately produced Current Suite and Next Suite validation
   outputs; and demonstrate an experimental Mixed Tree.  The evaluation
   also models an idealized parallel-publication footprint and estimates
   RRDP delta and snapshot response-body sizes from captured RPKI data.
   The results identify implementation, interoperability, repository-
   distribution, and operational questions that need to be resolved
   before a production algorithm profile or transition procedure can be
   specified.  This document is informational.  It does not update RFC
   7935 or RFC 6916, define a new RPKI algorithm profile, or authorize
   the use of the evaluated algorithms or Mixed Tree migration in the
   production RPKI.
- **draft-zhao-nmrg-ip-optical-ndt-sim-framework-01** (new-draft, score 3, adjacent_watchlist) [none]: [A Lightweight Cross-Layer Simulation Framework for IP-Optical Network Digital Twins](https://datatracker.ietf.org/doc/draft-zhao-nmrg-ip-optical-ndt-sim-framework/) — This document describes a lightweight, event-driven simulation
   framework for IP-optical Network Digital Twins (NDTs).  The framework
   investigates how optical and transport events propagate across
   network layers and interact with IP-layer protection, routing
   convergence, and traffic redistribution.

   The framework integrates three capabilities into a unified simulation
   process: dependency-aware event propagation, causal coordination of
   IP and optical behaviors on a common simulation timeline, and
   fidelity-aware evaluation of the resulting service impacts.  Cross-
   layer dependency uncertainty and model limitations are explicitly
   considered to avoid unsupported resilience conclusions.

   The framework uses abstract optical and transport states rather than
   continuous optical propagation models.  It reuses existing IETF
   topology and management information where applicable and supports
   reproducible what-if analysis, historical incident replay, and
   protection-strategy comparison.  It does not define new network
   protocols or YANG modules, and simulation results are not directly
   applied to production networks.
- **draft-zhao-opsawg-resilience-validation-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Scenario-based Network Resilience Validation](https://datatracker.ietf.org/doc/draft-zhao-opsawg-resilience-validation/) — Network resilience validation evaluates whether network services can
   maintain acceptable performance and recover within specified
   objectives under disruptive conditions.  Such validation may be
   performed using simulation, emulation, or controlled laboratory
   testing.  However, differences in scenario descriptions, evaluation
   criteria, and result representations make validation results
   difficult to exchange, reproduce, and compare across implementations.

   This document specifies a YANG data model for scenario-based network
   resilience validation.  The model standardizes the representation of
   validation scenarios, disruptive conditions, service-level evaluation
   criteria, and validation results.  It also defines common evaluation
   semantics to support consistent interpretation of results across
   validation environments.

   The specification focuses on interoperable representation of
   validation information.  It does not define simulation algorithms,
   fault-injection procedures, or mechanisms for modifying production
   networks.
- **draft-andesco-otpauth-uri-01** (new-draft, score 2, ignored_after_review) [none]: [The otpauth URI Scheme: One-Time Password (OTP) Credential Provisioning](https://datatracker.ietf.org/doc/draft-andesco-otpauth-uri/) — This document defines syntax and processing rules for the otpauth:
   URI scheme used to provision one-time-password (OTP) credentials
   (verification codes) for HOTP and TOTP.

   This document defines a common baseline for interoperability,
   including issuer handling rules that improve account matching while
   maintaining compatibility with existing deployments.  It does not
   preclude future extensions for other OTP methods.
- **draft-apple-cfrg-vdaf-preamble-00** (new-draft, score 2, ignored_after_review) [none]: [The PREAMBLE VDAF](https://datatracker.ietf.org/doc/draft-apple-cfrg-vdaf-preamble/) — This document describes PREAMBLE, a two-party Verifiable Distributed
   Aggregation Function (VDAF) for secure aggregation where each client
   holds a large-dimensional vector that is _block-sparse_, meaning it
   is divided into fixed-size blocks of which at most one is nonzero,
   and that nonzero block itself satisfies a specified Fully Linear
   Proof (such as multihot, or a bounded L1 or L2 norm).
- **draft-beeram-teas-rsvp-srv6-01** (new-draft, score 2, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SRv6 Forwarding Plane Using End.X Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-teas-rsvp-srv6/) — RFC 8577 defines mechanisms to signal RSVP-TE tunnels on a shared
   MPLS forwarding plane by introducing the notion of per-TE link labels
   that are functionally equivalent to SR-MPLS adjacency segments.  This
   document extends that work to the SRv6 data plane, defining the
   signaling extensions and procedures necessary to establish RSVP-TE
   tunnels that utilize SRv6 Segment Identifiers (SIDs) for forwarding.

   This document specifies how SRv6 End.X SIDs that are advertised in
   the IGP serve as TE link SIDs, defines new RSVP signaling extensions
   for carrying SRv6 SIDs and for influencing the endpoint behavior
   flavors of the SIDs, describes TE path segment-list construction
   procedures at the ingress (including NEXT-CSID compressed segment
   lists), adapts the delegation mechanisms of RFC 8577 to use SRv6
   Binding SIDs, and describes the termination of the tunnel at the
   egress.  The result couples the traffic engineering capabilities of
   the RSVP-TE control plane with the native IPv6 forwarding of SRv6.
- **draft-bernardos-nmrg-agentic-network-optimization-03** (new-draft, score 2, agent_identity) [none]: [Solutions for enabling agentic sensing with network optimization](https://datatracker.ietf.org/doc/draft-bernardos-nmrg-agentic-network-optimization/) — Integrated Sensing and Communications (ISAC) represents a paradigm
   shift in wireless networks, where sensing and communication functions
   are jointly designed and optimized.  By leveraging the same spectral
   and hardware resources, ISAC enables advanced capabilities such as
   environment perception, object tracking, and situational awareness,
   while maintaining efficient and reliable data transmission.  There
   are sensing scenarios and use cases that involve a distributed
   sensing task, in which multiple sensors participate and contribute
   with (raw or pre-processed) sensing data, which is processed by a
   sensing service (e.g., fusing sensing measurements from the different
   sensors).  This sensing service needs to be executed on some kind of
   sensing processing/computing function which receives raw (or
   preprocessed) data from multiple sources, potentially of different
   (heterogeneous) kinds (e.g., RF and non-RF sensing, or RF from
   different radio technologies).  This processing might impose time
   synchronization constraints on the reception of the different parts
   of data, as well as potentially specific computing and/or AI/ML
   capabilities on the processing node.

   The joint selection of sensing entities, processing locations, and
   network configuration under time-varying conditions results in a
   large, coupled, and non-stationary decision space.  These
   characteristics motivate the use of agentic AI to enable distributed,
   closed-loop configuration and reconfiguration of sensing and
   networking resources.

   This document presents initial considerations and potential solution
   directions for an architecture that enables the use of agentic AI for
   sensing (as an exemplary use case) supporting network optimization.
- **draft-calabria-bpm-ai-fabric-inference-bench-00** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-calabria-bpm-ai-fabric-terminology-00** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
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
- **draft-cgfabk-nmrg-ibn-generative-ai-03** (new-draft, score 2, ignored_after_review) [none]: [Generative AI for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-cgfabk-nmrg-ibn-generative-ai/) — This document describes how to specialize AI models in order to offer
   a scalable, efficient path to creating highly targeted generative
   models for Intent-Based Networking.
- **draft-chen-tsvwg-high-speed-ip-data-express-00** (new-draft, score 2, ignored_after_review) [none]: [High speed data express in IP: Concept, Reference Architecture and Technologies](https://datatracker.ietf.org/doc/draft-chen-tsvwg-high-speed-ip-data-express/) — With the rapid development of AI technology, intelligent computing
   and super-computing services, the demand for wide-area transmission
   of massive data is increasing.  This draft makes full use of the
   advantages of IP network, such as statistical reuse and elastic
   supply, and proposes a reference architecture of high elasticity and
   high throughput data express based on IP network.
- **draft-cheng-idr-ecmp-groupid-00** (new-draft, score 2, ignored_after_review) [none]: [BGP Extension for ECMP Group ID](https://datatracker.ietf.org/doc/draft-cheng-idr-ecmp-groupid/) — In AI training scenarios, per-flow ECMP is the mainstream load
   balancing technology.  However, hash collision issues lead to
   imbalanced traffic distribution, adversely affecting application
   performance.

   This document defines a new BGP Extended Community, BGP_EXT-COMM-
   ECMP-GROUPID, which carries an ECMP Group ID associated with a route.
   The ECMP Group ID allows an ingress router to map flows destined for
   different remote addresses to different local ECMP subgroups,
   providing finer-grained load distribution and resolving load
   imbalance caused by hash collisions.
- **draft-cheng-rtgwg-enhanced-ecmp-03** (new-draft, score 2, ignored_after_review) [none]: [Enhanced ECMP for AI Cluster](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/) — In AI training scenarios, per-flow ECMP is the mainstream load
   balancing technology deployed in current networks.  However, inherent
   hash collision issues of traditional ECMP lead to imbalanced traffic
   distribution, adversely affecting application performance.

   To address this problem, this document proposes an enhanced ECMP
   method that resolves load imbalance caused by hash collisions.  The
   proposed solution effectively improves load balancing efficiency,
   reduces network congestion, and enhances overall network performance.
- **draft-cui-dawn-mdi-model-02** (new-draft, score 2, ignored_after_review) [none]: [Minimum Public Discovery Information: Requirements and Common Semantics](https://datatracker.ietf.org/doc/draft-cui-dawn-mdi-model/) — The charter of the Discovery of Agents With Names (DAWN) working
   group asks it to specify the minimum public discovery information
   that a client obtains when it discovers an AI resource.  An
   individual draft on DAWN terminology defines Minimum Discoverable
   Information (MDI) as the minimum amount of information an entity
   needs to provide to become discoverable, distinguishes it from the
   Minimum Viable Dataset (MVD) that a discovery mechanism needs as
   input, and gives only examples of the content of either.  Individual
   drafts on the DAWN problem statement and requirements call for a
   standardized minimum structure and list what it must at least
   contain; in its absence, emerging discovery formats risk each
   defining its own minimal metadata, with descriptors that do not
   interoperate across organizational or protocol boundaries.

   This document addresses the minimum public discovery information as a
   client obtains it and as a publisher provides it, and its relation to
   the input of discovery; registration mechanisms are outside its
   scope.  Using the distinction RFC 3444 draws between information
   models and data models, it describes the information involved in
   publication, lookup, and response; proposes a procedure that derives
   what is minimal for each deployment context from the scope of the
   charter; applies the procedure to the charter's three deployment
   contexts: a local network, an organization, and the domain of a
   cooperating party; and proposes a set of elements with the minimal
   constraints that hold among them.  Information can be supplied by the
   discovery response, by context the client already has, or by binding
   rules.  This document is input to the DAWN architecture and protocol
   work; normative definitions that affect interoperability belong to
   the corresponding Standards Track documents.  It is a mapping target
   for richer descriptors.
- **draft-das-ai-safety-radio-observation-consistency-00** (new-draft, score 2, authorization) [none]: [AI Safety for Radio Network Observation and Control Calculation Consistency](https://datatracker.ietf.org/doc/draft-das-ai-safety-radio-observation-consistency/) — Part 02 of 15 describes AI safety for distributed radio-access-
   network observation and control calculation consistency.  A radio
   controller may receive independently valid telemetry that is jointly
   unsuitable for the same calculation because it refers to different
   cell or beam identities, configuration generations, clock domains,
   acquisition intervals, measurement units, aggregation semantics, or
   shared upstream evidence.  This document develops A-CW-01 and six
   specialized procedures for source-qualified temporal consistency,
   resource reassignment, measurement transformation, dependency-aware
   observation selection, coupled multi-resource decisions, and
   controller failover.  It specifies evidence-scoped supported,
   contradicted, and unresolved outcomes, with revalidation after
   material state changes.  The result qualifies a calculation; it does
   not independently authorize modification of live radio resources.
   Companion Parts 01, 03, 04, 05, 11, and 14 address shared evidence
   semantics, network recovery, service state, hardware observations,
   migration, and optional protected effectuation boundaries.
- **draft-degennaro-mta-hooks-02** (new-draft, score 2, ignored_after_review) [none]: [Mail Transfer Agent (MTA) Hooks: An HTTP-Based Protocol for External Mail Processing](https://datatracker.ietf.org/doc/draft-degennaro-mta-hooks/) — This document specifies MTA Hooks, an HTTP-based protocol that lets
   Mail Transfer Agents (MTAs) delegate message processing decisions to
   external services.  The MTA sends a JSON or Concise Binary Object
   Representation (CBOR) description of the SMTP session, envelope, and
   message to a registered service at defined stages of reception and
   delivery.  The service answers with a JSON Patch that changes the
   description, and the MTA acts on the resulting state.  The same
   mechanism covers filtering at SMTP time, routing before delivery, and
   reacting to delivery outcomes, and the MTA controls exactly which
   changes each service may make.
- **draft-dong-fann-fc-cc-coordinate-00** (new-draft, score 2, ignored_after_review) [none]: [Use Case and Requirements for Flow Control and Congestion Control Coordination in WAN-based AI DC Interconnect](https://datatracker.ietf.org/doc/draft-dong-fann-fc-cc-coordinate/) — AI services are moving from single-site data center (DC) toward a
   multi-site distributed architecture.  This requires to provide high-
   throughput, lossless, and deterministic network connectivity for AI
   workloads that span Data Center Networks (DCNs) over the Wide Area
   Network (WAN).  Due to the long distance introduced by WAN, end-to-
   end congestion control across the DCN and WAN networks become a
   challenge, as the reaction time increases from microseonds to
   millisend level, which correspondingly increases the risk of packet
   loss both at the receiver side and in the network.  This document
   describes the use case of coordinated flow control and congestion
   control to minimize the packet loss in WAN-based AI DCI networks.
   The requirements on Fast Network Notifications (FANN) mechanisms in
   this scenario is also described.
- **draft-filsfils-srv6ops-srv6-ai-backend-06** (new-draft, score 2, ignored_after_review) [none]: [SRv6 for Deterministic Path Placement in AI Backends](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) — This document describes how SRv6 NEXT-CSID enables deterministic path
   placement in AI backend fabrics through L3-L4 integration on end
   hosts: the transport stack on the NIC encodes each path as an ordered
   list of segments (a NEXT-CSID network program) in the packet header,
   while the fabric forwards statelessly.  It explains operational
   benefits including deterministic probing and alignment with
   hyperscale production deployments.
- **draft-gravit-gevp-12** (new-draft, score 2, ignored_after_review) [none]: [Gravit Epistemic Verification Protocol (GEVP)](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — The Gravit Epistemic Verification Protocol (GEVP) defines how signed
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
- **draft-he-agentproto-verifier-evidence-03** (new-draft, score 2, ignored_after_review) [none]: [Exercise and Completeness Evidence for Agent Protocol Verifier Results](https://datatracker.ietf.org/doc/draft-he-agentproto-verifier-evidence/) — A verifier result reports what a check returned.  It does not report
   whether the check could have returned anything else.  A check that
   inspects too narrow a set of fields, and a check whose rejecting or
   indeterminate input has never occurred, both report the same
   accepting value as a check that distinguishes, and a conformance
   matrix does not tell them apart.

   This document defines requirements for reporting whether a check has
   been exercised into its declared rejecting and indeterminate
   outcomes, and requirements for results that claim completeness: that
   the records relied on were the whole of some stated set.  Those are
   two separate obligations.  A result must name the set it claims to
   have seen, and must not treat a party with an interest in the answer
   as the only thing looking.

   This document defines no wire format, encoding, token, claim
   vocabulary, test harness, or registry.  It does require a record to
   identify certain facts.  That constrains what a record must be able
   to express and leaves its encoding open.  A profile satisfying these
   requirements will need a place to put those facts.
- **draft-hood-agtp-commerce-01** (new-draft, score 2, ignored_after_review) [none]: [AGTP-Commerce: Open Commerce Specification for Agent-to-Agent Transactions](https://datatracker.ietf.org/doc/draft-hood-agtp-commerce/) — This document specifies AGTP-Commerce, an open commerce specification
   for agent-to-agent transactions.  The specification defines the
   structural transaction information that the Agent Transfer Protocol
   carries between agents, allowing payment providers and commerce
   applications to compose at the application layer to perform the
   actual financial execution.

   AGTP-Commerce is to agent commerce what ISO 20022 is to inter-bank
   payment messaging: a standardized message format that allows
   heterogeneous payment infrastructure to interoperate.  AGTP-Commerce
   moves no money, holds no funds, and operates as no payment processor.
   The protocol carries pricing manifests, budget signaling, transaction
   commitments, and audit trail records that payment providers consume
   to execute settlement through existing financial infrastructure.

   This document specifies the pricing manifest format, extended Budget-
   Limit header semantics, the TRANSACT method for transaction
   commitment, audit-trail-based receipt records, dispute composition
   surfaces, and the integration patterns that allow payment providers
   (traditional processors, banks, cryptocurrency rails, and specialized
   agent-economy services) to compose with AGTP-Commerce as application-
   layer infrastructure.
- **draft-hood-agtp-methods-00** (new-draft, score 2, ignored_after_review) [none]: [AGTP Methods (AGTP Verbs): Method Vocabulary, Path Grammar, and Endpoints](https://datatracker.ietf.org/doc/draft-hood-agtp-methods/) — This document specifies AGTP-METHODS, the method vocabulary of the
   Agent Transfer Protocol (AGTP) [AGTP] and the contract layer built on
   it.  AGTP methods, also called AGTP verbs, are the action-intent
   words that name what a request does, in the same position that
   methods occupy in HTTP.  The document defines the properties a method
   may have, the eighteen-method floor every server implements, the
   registered catalog of methods beyond the floor (425 methods in nine
   categories at catalog version 1.0.0) with its versioned evolution and
   graceful deprecation, the path grammar that keeps method names out of
   paths, the endpoint primitive as the unit a server exposes, the
   semantic block carried by every endpoint, the server manifest, the
   per-server method policy, the three handler binding kinds, and the
   structural rejection codes 404, 405, 459, and 460.  Runtime contract
   negotiation, previously carried in the same document, is now
   specified in the companion AGTP-RCNS.  This document replaces
   [AGTP-API], which in turn superseded the AGIS and AGTP-Methods
   drafts.
- **draft-hood-agtp-rcns-00** (new-draft, score 2, ignored_after_review) [none]: [AGTP-RCNS: Runtime Contract Negotiation Substrate](https://datatracker.ietf.org/doc/draft-hood-agtp-rcns/) — This document specifies the Runtime Contract Negotiation Substrate
   (RCNS) for the Agent Transfer Protocol (AGTP) [AGTP]: the mechanism
   by which an AGTP server synthesizes an endpoint at runtime, from
   registered primitives, when a caller addresses a method and path pair
   the server has yet to register.  RCNS is invoked explicitly through
   the PROPOSE floor method and implicitly when a server is configured
   to treat unregistered requests as synthesis candidates.  The document
   defines the four-lock dispatcher gate that governs when synthesis may
   occur, the two contract delivery modes, the PROPOSE request and
   response body shapes, recipe versioning, contract scoping and
   lifecycle, the headers and rate-limiting contract, the Attribution-
   Record extension fields that make every invocation served under a
   contract attributable, and the inventory surfaces through which
   contracts are observed.  The material was previously carried in
   [AGTP-API], which this document and [AGTP-METHODS] together replace.
- **draft-hu-6man-ipv6-flowlabel-load-balancing-rdma-03** (new-draft, score 2, ignored_after_review) [none]: [A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) — This document proposes a method for achieving flow-level load
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
- **draft-huang-ainetops-agent-schema-interfaces-00** (new-draft, score 2, ignored_after_review) [none]: [Schema Interfaces for Network Management Agent Skills](https://datatracker.ietf.org/doc/draft-huang-ainetops-agent-schema-interfaces/) — Network management agents can use an Agent-to-Agent protocol for task
   exchange.  The protocol alone does not define the application schemas
   used by independently developed network management agent skills.

   This document standardizes four components for schema-governed
   network management agent skills: Schema References, per-skill Skill
   Interface Documents, advertisement and retrieval through an A2A
   extension and describe_skill, and the A2A mapping for interface
   version 1.0.  Together, they enable clients to retrieve and validate
   the application schemas used for skill inputs, outputs, and
   supporting records.
- **draft-ietf-cdni-delivery-metadata-04** (new-draft, score 2, ignored_after_review) [cdni]: [CDNI Delivery Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-delivery-metadata/) — This specification adds to the core set of configuration metadata
   defined in RFC8006, providing delivery metadata to define traffic
   types, request delegation behavior and CDN transport arrangements
   selection for a downstream CDN.
- **draft-ietf-deleg-13** (new-draft, score 2, ignored_after_review) [deleg]: [Extensible Delegation for DNS](https://datatracker.ietf.org/doc/draft-ietf-deleg/) — This document specifies a new extensible method for the delegation of
   authority for a domain in the Domain Name System (DNS) using DELEG
   and DELEGPARAM records.

   A delegation in the DNS enables efficient and distributed management
   of the DNS namespace.  The traditional DNS delegation is based on NS
   records which contain only hostnames of servers and no other
   parameters.  In classic DNS, both parent and child zones contain
   copies of NS delegation records, which can potentially be out of sync
   and confusing.  The new delegation records are extensible, can be
   secured with DNSSEC, and eliminate the problem of having two sources
   of truth for delegation information.
- **draft-ietf-dnsop-delext-13** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895, and 9824.
- **draft-jimenez-dawn-ard-initial-contact-00** (new-draft, score 2, ignored_after_review) [none]: [Agent Resource Discovery (ARD): Initial Contact](https://datatracker.ietf.org/doc/draft-jimenez-dawn-ard-initial-contact/) — In an agent system, agents need to discover other agents, tool
   servers, and skills.  Agent Resource Discovery (ARD) defines a
   manifest listing such resources and a lookup interface over it.  This
   document specifies how a client (such as an agent) initially
   discovers an ARD manifest.  This discovery is performed through the
   use of DNS Service Binding records, DNS-Based Service Discovery (DNS-
   SD), HTTP link relations, or well-known URIs.  Each mechanism yields
   a set of manifest URIs.  The manifest format, the lookup interface,
   and the binding of a manifest to its publisher are specified in the
   companion ARD documents.
- **draft-kavian-aep-service-documents-00** (new-draft, score 2, ignored_after_review) [none]: [AEP Service Documents](https://datatracker.ietf.org/doc/draft-kavian-aep-service-documents/) — This document defines an optional Agent Enrollment Protocol (AEP)
   extension for discovering and reading Service documents and
   acknowledging required documents during enrollment.  Documents have
   Service-scoped identifiers, web representations, and optional
   portable structured content.  Acknowledgements identify documents,
   not immutable content versions.  Services determine when an existing
   enrollment needs further acknowledgement.
- **draft-kcrh-hpwan-state-of-art-04** (new-draft, score 2, ignored_after_review) [none]: [Current State of the Art for High Performance Wide Area Networks](https://datatracker.ietf.org/doc/draft-kcrh-hpwan-state-of-art/) — High Performance Wide Area Networks (HP-WANs) provide infrastructure
   for the modern global Research and Education (R&E) community,
   facilitating collaboration across national and international
   boundaries.  These networks include global education and research
   networks, such as GÉANT, Internet2, Janet, ESnet, CANARIE, CERNET,
   and others, and also refer to large-scale commercial dedicated
   networks built by hyperscalers and operators.  They are designed to
   support the transfer of data generated by scientific research, high-
   performance computing, distributed AI-training, and large-scale
   simulations.

   This document provides an overview of the terminology and techniques
   used for existing HP-WANs.  It also explores the technological
   advancements, operational tools, and future directions for HP-WANs,
   including their use in scientific research, AI training, and large-
   scale R&E data analysis.
- **draft-li-dmsc-macp-07** (new-draft, score 2, ignored_after_review) [none]: [Multi-agent Collaboration Protocol Suites Architecture](https://datatracker.ietf.org/doc/draft-li-dmsc-macp/) — This document defines a protocol suite and architectural framework
   for secure and scalable multi-agent collaboration.  The proposed
   Multi-Agent Collaboration Protocol (MACP) enables trusted agent
   onboarding, capability-based query, distributed capability
   synchronization, and secure interaction among agents and external
   resources.  The architecture introduces key entities such as the
   Agent Management Center (AMC), Agent Gateway (AGW), Agents, and
   External Resource Services (ERS), along with a set of protocols that
   collectively support dynamic, capability-driven collaboration across
   administrative domains.
- **draft-liu-audit-enforcement-points-00** (new-draft, score 2, ignored_after_review) [none]: [Enforcement Points for Agents](https://datatracker.ietf.org/doc/draft-liu-audit-enforcement-points/) — Agent auditing relies on distributed enforcement points (EPs) to
   observe and intervene in agent activities.  This document analyzes
   Agent, Gateway, and Host EPs by detailing their coverage and audit
   data.  This provides a basis for understanding the capabilities of
   different EPs and evaluating overall audit evidence coverage.
- **draft-mahy-mls-credential-by-ref-00** (new-draft, score 2, ignored_after_review) [none]: [Credentials By-Reference in the Messaging Layer Security (MLS) Protocol](https://datatracker.ietf.org/doc/draft-mahy-mls-credential-by-ref/) — Credentials in MLS can grow to become quite large.  Many credentials
   appear repeatedly in several MLS groups.  This extension allows MLS
   credentials to be included by using a hash reference of the actual
   credential.
- **draft-michielsen-srv6ops-service-rr-ai-dc-00** (new-draft, score 2, ignored_after_review) [none]: [BGP Service-Route distribution in AI data centers](https://datatracker.ietf.org/doc/draft-michielsen-srv6ops-service-rr-ai-dc/) — AI clusters and hyperscale data centers can contain hundreds of leaf
   switches and large numbers of service prefixes.  In a conventional
   BGP leaf-spine design, each spine distributes routes for the service
   prefixes originated by one leaf to all other leaves.  This leads to a
   large number of received BGP route instances on the leaves and many
   FIB entries for service prefixes on the spines.

   This document describes an alternative deployment in which dedicated
   eBGP speakers, referred to in this document as Service RRs,
   distribute service routes.  The spines continue to distribute
   infrastructure routes but do not carry service routes.  A Service RR
   uses regular eBGP procedures while advertising service routes with
   NEXT_HOP unchanged.  The leaves encapsulate the service traffic and
   the spines forward the encapsulated service traffic using
   infrastructure reachability.

   The design improves control- and data-plane scaling by reducing the
   number of service-route instances received by each leaf and removing
   service-route state and processing from the spines.  This document
   defines no new BGP extension.
- **draft-mp-agntcy-ads-03** (new-draft, score 2, agent_identity) [none]: [Agent Directory Service](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/) — The Agent Directory Service (ADS) is a distributed directory service
   designed to store metadata for AI agent applications.  This metadata,
   stored as directory records, enables the discovery of agent
   applications with specific skills for solving various problems.  The
   implementation features distributed directories that interconnect
   through a content-routing protocol.
- **draft-okutomi-agent-human-interaction-01** (new-draft, score 2, ignored_after_review) [none]: [An Agent-Human Interaction Overlay for Task Protocols](https://datatracker.ietf.org/doc/draft-okutomi-agent-human-interaction/) — This design note proposes an overlay for Human and Agent
   participation in existing Task and Action protocols.  It separates
   the responsible Participant from the authenticated Actor, records
   Human interactions, excludes Humans from Agent discovery, and binds
   each change to its authorized request.  It specifies no wire protocol
   and does not treat Humans as Agents.
- **draft-spzzx-bier-in-ai-consideration-00** (new-draft, score 2, ignored_after_review) [none]: [BIER in AI considerations](https://datatracker.ietf.org/doc/draft-spzzx-bier-in-ai-consideration/) — Based on existing industry research, this document outlines
   considerations regarding the application of BIER technology in AIDC.
- **draft-sun-ainetops-task-and-evidence-model-01** (new-draft, score 2, adjacent_watchlist) [none]: [Task and Evidence Information Model for AINETOps](https://datatracker.ietf.org/doc/draft-sun-ainetops-task-and-evidence-model/) — As Network Management Agents (NMAs) increasingly collaborate in
   scenarios such as fault diagnosis, network optimization, and service
   assurance, consistent task descriptions and evidence information are
   needed across vendors and management domains.  This document defines
   a Task and Evidence Information Model for AI-Enabled Network
   Operations (AINETOps).  The model consists of Task Core, Evidence
   Core, and a Profile extension mechanism for different task and
   evidence types.  This document does not specify communication
   protocols, request or response formats, task execution methods, or
   network configuration operations.
- **draft-watts-verifiable-scientific-evidence-records-02** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Scientific Evidence Records: A Minimal Integrity Profile](https://datatracker.ietf.org/doc/draft-watts-verifiable-scientific-evidence-records/) — This document specifies a minimal JSON evidence-record profile for
   checking artifact digests and separating integrity verification from
   scientific assessment.  It defines an interoperable record structure,
   validation algorithm, and negative test cases.  It does not assert
   that an integrity-checked scientific claim is true.
- **draft-wnd-opsawg-icon-ps-01** (new-draft, score 2, ignored_after_review) [none]: [Problem Statement for Observability, Intervention and Control (I&C) in Multi-Agent Autonomous Networks](https://datatracker.ietf.org/doc/draft-wnd-opsawg-icon-ps/) — This document provides an overview of the issues associated with the
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
- **draft-xl-idr-bgp-sr-policy-pathrate-00** (new-draft, score 2, ignored_after_review) [none]: [BGP SR Policy for Path Rate](https://datatracker.ietf.org/doc/draft-xl-idr-bgp-sr-policy-pathrate/) — In AI/ML compute fabrics and data center interconnects, collective
   communication patterns (e.g., All-Reduce, All-to-All) generate
   microbursts that can saturate queuing buffers before reactive
   congestion control mechanisms take effect.  This document specifies a
   BGP SR Policy extension to carry Path Rate information (e.g., Path
   Committed Rate and Path Maximum Rate), enabling a central controller
   to compute and distribute per-segment-list rate limits along with the
   SR Policy Candidate Path.  The headend enforces these rate limits on
   traffic steered to the corresponding segment list, thereby
   proactively preventing the microburst-induced congestion before
   traffic enters the network.
- **draft-zhang-idr-portid-ec-03** (new-draft, score 2, ignored_after_review) [none]: [BGP PORT EC for AIDC](https://datatracker.ietf.org/doc/draft-zhang-idr-portid-ec/) — This document introduces a new BGP Route Port ID Extended Community
   (PORT EC) for advertising the association between destination routes,
   switch addresses, and port identifiers.  It describes the
   advertisement of Aggregated PORT EC.  It also illustrate the PORT EC
   advertisement procedures in AI data center networks.
- **draft-zzhang-bier-inc-00** (new-draft, score 2, ignored_after_review) [none]: [BIER and In Network Computing](https://datatracker.ietf.org/doc/draft-zzhang-bier-inc/) — In-Network-Computing/Collectives (INC) is an important element in
   Collective Communication for AI/ML.  A multicast tree is typically
   set up for broadcasting in the forward direction and in-network
   computing/reduction in the reverse direction.  BIER is a multicast
   technology that removes explicit multicast trees, and this document
   describes how INC can be done with BIER that does not use pre-
   established multicast trees.

## Ignored after review

- **draft-abraitis-idr-addpath-paths-limit-07** (new-draft, score 0, ignored_after_review) [none]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-ageneau-ccwg-ndtc-03** (new-draft, score 0, ignored_after_review) [none]: [Network Delivery Time Control](https://datatracker.ietf.org/doc/draft-ageneau-ccwg-ndtc/) — This document describes Network Delivery Time Control (NDTC), a rate
   adaptation algorithm for real-time video streaming suited for
   interactive applications like cloud gaming.  NDTC leverages the Frame
   Dithering Available Capacity Estimation (FDACE) heuristic, which
   estimates available path capacity without inducing congestion.  The
   algorithm dynamically adjusts frame sizes and transmission times to
   ensure timely delivery, while also responding to conventional
   congestion signals.
- **draft-aggarwal-regext-rdap-irr-00** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Internet Routing Registry (IRR) Objects](https://datatracker.ietf.org/doc/draft-aggarwal-regext-rdap-irr/) — The Registration Data Access Protocol (RDAP) is used by Regional
   Internet Registries (RIRs) and Domain Name Registries (DNRs) to
   provide access to their resource registration information.  The core
   specifications for RDAP define core object types, but they do not
   contain objects for the Internet Routing Registry (IRR).  This
   document is intended to address this gap.
- **draft-alazzeh-hrpc-cso-guidance-00** (new-draft, score 0, ignored_after_review) [none]: [From the Field to the Protocol: Guidance for Civil Society on Informing IETF Work](https://datatracker.ietf.org/doc/draft-alazzeh-hrpc-cso-guidance/) — Civil society organizations (CSOs) document how Internet protocols
   and their deployments affect people around the world, yet their
   participation in the IETF has been limited and difficult to sustain,
   particularly for organizations based in the Global South.  This
   document offers guidance to CSOs on how their research and field
   experience can inform the work of the IETF and IRTF.  It points to
   areas where IETF work and CSO interests overlap, explains how field
   observations can be described so that the technical community can use
   them, and identifies venues where this work can be shared.  The aim
   is to inform, not to determine, restrict, or dictate, the design and
   deployment of Internet protocols in the public interest.

   It is a contribution to the Human Rights Protocol Considerations
   Research Group (HRPC) of the IRTF.
- **draft-ali-netmod-yang-protobuf-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement: YANG Modeling for Protocol Buffer Based Network APIs](https://datatracker.ietf.org/doc/draft-ali-netmod-yang-protobuf-problem-statement/) — Network devices increasingly expose operational APIs using gRPC and
   Protocol Buffers.  Many of these APIs provide ephemeral or runtime
   state whose lifetime is limited to a process, service, session, or
   device runtime.  At the same time, the IETF has standardized YANG as
   a data modeling language for network management and has defined
   encodings for YANG data, including JSON and CBOR.  This document
   describes the problem space and identifies questions for the IETF
   community regarding standards-based gRPC APIs for ephemeral
   operational state.

   The scope is limited to ephemeral operational state.  Configuration
   data and configuration management operations are out of scope.
- **draft-ali-pce-implicit-tls-profile-02** (new-draft, score 0, ignored_after_review) [none]: [A Policy-Driven Implicit TLS Transport Profile for PCEP](https://datatracker.ietf.org/doc/draft-ali-pce-implicit-tls-profile/) — RFC 8253 specifies the use of Transport Layer Security (TLS) for the
   Path Computation Element Communication Protocol (PCEP) by negotiating
   TLS using the PCEP StartTLS message exchange. This document specifies
   a deployment profile in which TLS is initiated immediately after TCP
   connection establishment, on the existing PCEP port, based on an out-
   of-band configured policy. This profile is intended for managed
   deployments where TLS is mandatory and neither in-band security-mode
   negotiation nor fallback to cleartext is permitted.
- **draft-ali-spring-sr-service-programming-oam-09** (new-draft, score 0, ignored_after_review) [none]: [OAM for Service Programming with Segment Routing](https://datatracker.ietf.org/doc/draft-ali-spring-sr-service-programming-oam/) — This document defines the Operations, Administrations and Maintenance
   (OAM) for service programming in SR-enabled MPLS and IP networks.
- **draft-all-pce-srv6-policy-sid-list-optimization-05** (new-draft, score 0, ignored_after_review) [none]: [Path Computation Element Communication Protocol (PCEP) extensions for SRv6 Policy SID List Optimization](https://datatracker.ietf.org/doc/draft-all-pce-srv6-policy-sid-list-optimization/) — In some use cases, an SRv6 policy's SID list ends with the policy
   endpoint's node SID, and the traffic steered (over policy) already
   ensures that it is taken to the policy endpoint.  In such cases, the
   SID list can be optimized by excluding the endpoint Node SID when
   installing the policy.  This draft specifies a PCEP extension to
   indicate whether the endpoint's node SID needs to be included or
   excluded when installing the SRv6 Policy.
- **draft-attoumani-ietf-inclusion-06** (new-draft, score 0, ignored_after_review) [none]: [The IETF is for Everyone: Toward Inclusive and Equitable Participation in Internet Governance](https://datatracker.ietf.org/doc/draft-attoumani-ietf-inclusion/) — Participation in the IETF remains very unevenly distributed across
   regions, and Africa is among the least represented.  This document
   argues that closing this gap is a shared responsibility and proposes
   a two-track approach.  Outside the IETF, universities, technical
   communities, Internet governance forums, and regional institutions in
   underrepresented regions need to demystify the IETF and bring
   academics, students, and young engineers toward its work.  Within the
   IETF, barriers to entry can be lowered further, and holding an IETF
   meeting in Africa would send a strong signal and act as a catalyst,
   meeting a local community prepared by the first track.  The document
   proposes concrete actions, indicative metrics, and next steps for
   both tracks.
- **draft-bcbr-detnet-actn-00** (new-draft, score 0, ignored_after_review) [none]: [Applicability of ACTN to Multi-Domain Deterministic Networking](https://datatracker.ietf.org/doc/draft-bcbr-detnet-actn/) — End-to-end Deterministic Networking (DetNet) services may span
   multiple network domains using different technologies and controlled
   by independent domain-specific mechanisms.  Coordinating these
   services requires an approach to abstract network resources and
   capabilities while preserving the requested service objectives across
   domain boundaries.

   This document investigates the applicability of the Abstraction and
   Control of Traffic Engineering Networks (ACTN) framework to multi-
   domain DetNet.  It describes a functional mapping between ACTN
   entities and the DetNet Controller Plane, and considers the
   information needed for domain abstraction, service objective
   coordination and monitoring.  It identifies areas for further work
   and questions for discussion in the DetNet and TEAS Working Groups.
- **draft-becker-cnsa2-smime-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Secure/Multipurpose Internet Mail Extensions (S/MIME)](https://datatracker.ietf.org/doc/draft-becker-cnsa2-smime-profile/) — This document defines a base profile of S/MIME for use with the US
   Commercial National Security Algorithm (CNSA) 2.0 Suite, a
   cybersecurity advisory published by the United States Government
   which outlines quantum-resistant cryptographic algorithm policy for
   US national security applications.

   This profile applies to the capabilities, configuration, and
   operation of all components of US National Security Systems that
   employ S/MIME.  It is also appropriate for all other US Government
   systems that process high-value information.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This profile is made publicly available
   for use by developers and operators of these and any other system
   deployments.
- **draft-becker-cnsa2-ssh-profile-07** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
   Commercial National Security Algorithm (CNSA) 2.0 Suite, a
   cybersecurity advisory published by the United States Government
   which outlines quantum-resistant cryptographic algorithm policy for
   US national security applications.

   This profile applies to the capabilities, configuration, and
   operation of all components of US National Security Systems that
   employ SSH.  It is also appropriate for all other U.S.  Government
   systems that process high-value information.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This profile is made publicly available
   for use by developers and operators of these and any other system
   deployments.
- **draft-becker-cnsa2-tls-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for TLS 1.3](https://datatracker.ietf.org/doc/draft-becker-cnsa2-tls-profile/) — This document defines a base profile of TLS 1.3 which is compliant
   with the US Commercial National Security Algorithm (CNSA) 2.0 Suite,
   a cybersecurity advisory published by the United States Government
   which outlines quantum-resistant cryptographic algorithm policy for
   US national security applications.

   This profile applies to the capabilities, configuration, and
   operation of all components of US National Security Systems that
   employ TLS 1.3.  It is also appropriate for all other US Government
   systems that process high-value information.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This profile is made publicly available
   for use by developers and operators of these and any other system
   deployments.
- **draft-beeram-teas-rsvp-resource-notifications-00** (new-draft, score 0, ignored_after_review) [none]: [RSVP-TE Resource Notifications](https://datatracker.ietf.org/doc/draft-beeram-teas-rsvp-resource-notifications/) — In scaled Resource Reservation Protocol - Traffic Engineering (RSVP-
   TE) networks, a single network resource event (such as a link failure
   or bandwidth reduction) can trigger a storm of PathErr messages, one
   for each affected Label Switched Path (LSP).  This document
   introduces RSVP Resource Notifications, a mechanism that reduces the
   number of per-LSP error messages by sending summarized per-source
   resource-level notifications in a new RSVP message, ResourceNotify.
   This reduces the control-plane message load from O(LSPs) to
   O(sources), significantly improving convergence in networks with a
   large number of RSVP-TE LSPs.

   The mechanism applies to LSPs whose source is reachable by the
   transit node within the same domain, and uses a Resource Notification
   Request Object carried in PATH messages.  Two types of resource
   notifications are defined in this document: Resource Unavailable (for
   link failures) and Resource Degraded (for bandwidth reduction
   events).
- **draft-bensley-rpsl-exclude-members-01** (new-draft, score 0, ignored_after_review) [none]: [Explicitly excluding objects from RPSL sets](https://datatracker.ietf.org/doc/draft-bensley-rpsl-exclude-members/) — This document updates RFC 2622 and RFC 4012 by defining the excl-
   members attribute on the as-set and route-set classes in the Routing
   Policy Specification Language (RPSL).  A set that references another
   set includes everything the referenced set contains, however deeply
   nested.  RPSL currently has no way for the set owner to make an
   exception.  The excl-members attribute lets a set owner exclude
   specific members, including ones brought in by a referenced set.
- **draft-besleaga-sustainability-wellknown-12** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI, at
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
- **draft-binhnguyen-native-ipv4-ipv6only-routing-00** (new-draft, score 0, ignored_after_review) [none]: [Native IPv4 Forwarding over IPv6-Only Routing Infrastructure](https://datatracker.ietf.org/doc/draft-binhnguyen-native-ipv4-ipv6only-routing/) — IPv6 deployment continues to expand within routing infrastructure,
   while IPv4 connectivity remains necessary for many services,
   applications, and end systems.  Existing routing mechanisms allow
   IPv4 reachability to be maintained using IPv6 next hops, enabling
   native IPv4 forwarding even where IPv6 is used for infrastructure
   addressing, routing adjacencies, and next-hop resolution.

   This document brings together existing routing mechanisms, deployment
   patterns, and implementation experience in a common architectural
   view.  It makes explicit the separation between the address-family
   functions used by the routing infrastructure and the reachability and
   traffic supported by that infrastructure.  It examines how this
   separation appears in provider-edge/customer-edge interconnections,
   Internet Exchange Points, and large-scale data-center fabrics.

   By relating existing standards and deployment experience through this
   common view, the document identifies a recurring architectural
   pattern for IPv6-based routing infrastructure that continues to
   support native IPv4 connectivity, and discusses its applicability and
   limitations.

   This document does not define a new routing protocol, forwarding
   mechanism, BGP extension, or migration procedure.
- **draft-brand-indicators-for-message-identification-15** (new-draft, score 0, ignored_after_review) [none]: [Brand Indicators for Message Identification (BIMI)](https://datatracker.ietf.org/doc/draft-brand-indicators-for-message-identification/) — Brand Indicators for Message Identification (BIMI) permits Domain
   Owners to coordinate with Mail User Agents (MUAs) to display brand-
   specific Indicators next to properly authenticated messages.  There
   are two aspects of BIMI coordination: a scalable mechanism for Domain
   Owners to publish their desired Indicators, and a mechanism for Mail
   Transfer Agents (MTAs) to verify the authenticity of the Indicator.
   This document specifies how Domain Owners communicate their desired
   Indicators through the BIMI Assertion Record in DNS and how that
   record is to be interpreted by MTAs and MUAs.  MUAs and mail-
   receiving organizations are free to define their own policies for
   making use of BIMI data and for Indicator display as they see fit.
- **draft-brotman-ietf-bimi-guidance-16** (new-draft, score 0, ignored_after_review) [none]: [General Guidance for Implementing Branded Indicators for Message Identification (BIMI)](https://datatracker.ietf.org/doc/draft-brotman-ietf-bimi-guidance/) — This document is meant to provide guidance to various entities so
   that they may implement Brand Indicators for Message Identification
   (BIMI).  This document is a companion to various other BIMI drafts,
   which should first be consulted.
- **draft-buck-dkim-pq-dkim1-00** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Cryptography in DKIM](https://datatracker.ietf.org/doc/draft-buck-dkim-pq-dkim1/) — This document discusses suitable post-quantum (PQ) signature
   algorithms for DomainKeys Identified Mail (DKIM).  Because DKIM
   signatures are carried in emails, and public keys in DNS TXT records
   the usage of already standardized algorithms is limited.  For
   compatibility reasons, signers that want post-quantum security are
   expected to add a PQ signature to a message in addition to a
   traditional signature, using separate DKIM-Signature header fields.
   The existing RSA and Ed25519 algorithms remain unchanged.
- **draft-calink-v6ops-fhrd-00** (new-draft, score 0, ignored_after_review) [none]: [First Hop Redundancy in IPv6 Networks: Operational Considerations](https://datatracker.ietf.org/doc/draft-calink-v6ops-fhrd/) — This document provides operational guidance for configuring first-hop
   routers and first-hop redundancy in IPv6 networks.  It also discusses
   design choices for improving recovery time after a renumbering event.
- **draft-callec-api-advisory-02** (new-draft, score 0, ignored_after_review) [none]: [A Well-Known URI for API Change Advisories](https://datatracker.ietf.org/doc/draft-callec-api-advisory/) — This document defines a well-known URI, /.well-known/api-
   advisory.json, at which API providers MAY publish a machine-readable
   JSON discovery file.  That file identifies the API and provides the
   URL of an Atom Syndication Format feed carrying structured change
   advisories.  The Atom feed enables automated scanners and API
   consumers to discover pricing changes, deprecations, security
   advisories, and other relevant events without relying on manual
   monitoring of blogs or mailing lists.  Advisory metadata is conveyed
   through a dedicated XML namespace defined in this document.
- **draft-camarillo-fann-lsn-00** (new-draft, score 0, ignored_after_review) [none]: [Lightspeed Notification Protocol](https://datatracker.ietf.org/doc/draft-camarillo-fann-lsn/) — This document defines the Lightspeed Notification Protocol (LSN), a
   hardware-accelerated signaling mechanism designed for sub-100
   microsecond network convergence in AI/ML data center fabrics.  By
   remaining on chip and never punting to the host CPU, LSN bypasses
   traditional CPU-based latencies to propagate link failures and
   congestion via a hardware-efficient encoding.  It serves as a high-
   speed complement to routing protocols such as BGP, providing an
   immediate hardware veto that prunes failed or congested paths while
   maintaining control-plane stability for path recovery.

   The same mechanism applies inside the DC Clos and, in some
   deployments, across the Data Center Interconnect (DCI) and WAN.  This
   document defines two encoding modes: a dense encoding for DC fabrics,
   where traffic is load-balanced over many ECMP spines, and a sparse
   encoding for the DCI and WAN.
- **draft-cardona-claise-netmod-yang-coverage-01** (new-draft, score 0, ignored_after_review) [none]: [YANG Module Coverage by Examples in IETF Documents](https://datatracker.ietf.org/doc/draft-cardona-claise-netmod-yang-coverage/) — This document introduces the concept of YANG module "coverage" to
   measure how thoroughly example instances exercise a YANG module's
   data nodes.  Coverage analysis identifies the parts of a module that
   are and are not exercised by examples, helping authors, reviewers,
   and implementers understand the range of scenarios illustrated by a
   specification.
- **draft-cardona-claise-netmod-yang-examples-00** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for YANG Example and Supporting Artifacts in IETF Documents](https://datatracker.ietf.org/doc/draft-cardona-claise-netmod-yang-examples/) — This document updates RFC 9907 guidance for including YANG-related
   examples and supporting artifacts in IETF documents.  It defines
   naming conventions that make those artifacts easier for tools to
   identify, extract, organize, and validate.
- **draft-chatzis-httpbis-required-rate-00** (new-draft, score 0, ignored_after_review) [none]: [The Required-Rate HTTP Priority Parameter](https://datatracker.ietf.org/doc/draft-chatzis-httpbis-required-rate/) — This document defines the required-rate (r) priority parameter for
   the Extensible Prioritization Scheme for HTTP (RFC 9218).  The
   parameter allows a client to indicate a delivery rate above which
   faster transfer of an HTTP response is not expected to provide
   additional application benefit.  A server can use this signal to
   rate-limit an individual response, allowing other eligible responses
   to make progress without replacing the urgency and incremental
   scheduling behavior defined by RFC 9218.
- **draft-chen-green-transport-energy-saving-02** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Energy Saving Mechanism for Transport Network](https://datatracker.ietf.org/doc/draft-chen-green-transport-energy-saving/) — This document specifies a transport network energy saving mechanism
   that harmonizes device-level autonomy with network-wide coordination.
   By adopting hybrid coordination between devices and network
   controllers, it enables dynamic, SLA-aware, and multi-layer energy
   optimization.
- **draft-chen-ipsec-problems-for-ntn-network-02** (new-draft, score 0, ignored_after_review) [none]: [IPsec Challenges in Non-Terrestrial Networks (NTN)](https://datatracker.ietf.org/doc/draft-chen-ipsec-problems-for-ntn-network/) — This document describes the problems in the use of IPsec in satellite
   Internet and NTN network scenarios.
- **draft-chen-rtg-framework-srv6-trusted-relay-qkd-00** (new-draft, score 0, ignored_after_review) [none]: [A Framework for SRv6-Based Trusted Key Relay in Quantum Key Distribution Networks](https://datatracker.ietf.org/doc/draft-chen-rtg-framework-srv6-trusted-relay-qkd/) — Quantum Key Distribution (QKD) links generate symmetric key material
   between directly connected QKD nodes.  Trusted relay is commonly used
   to extend key delivery beyond the reach of a single QKD link.  A
   complete trusted-relay service requires the network to collect QKD
   link and node quantum capability information, compute a relay path
   according to service requirements, translate the result into a
   network forwarding path, and carry the relayed key information in an
   IPv6/UDP packet steered by that path.

   This document describes an architectural framework for such a
   service.  Each QKD link provides its link quantum capability such as
   available quantum key rate capacity, and each relay node provides its
   node quantum capability . A controller uses these inputs together
   with application requirements to calculate a relay path.  The path-
   computation algorithm is not standardized and may be selected or
   defined by the user, operator, or implementation.  The calculated
   relay sequence is represented as an SRv6 path, and UDP packets
   following that path carry the key-relay information.

   This document identifies the protocol extension points needed to
   support the framework.  The detailed encodings, message formats,
   TLVs, and signaling procedures are left for future work and are
   marked as TBD.
- **draft-chen-rtgwg-framework-srv6-trusted-relay-qkd-00** (new-draft, score 0, ignored_after_review) [none]: [A Framework for SRv6-Based Trusted Key Relay in Quantum Key Distribution Networks](https://datatracker.ietf.org/doc/draft-chen-rtgwg-framework-srv6-trusted-relay-qkd/) — Quantum Key Distribution (QKD) links generate symmetric key material
   between directly connected QKD nodes.  Trusted relay is commonly used
   to extend key delivery beyond the reach of a single QKD link.  A
   complete trusted-relay service requires the network to collect QKD
   link and node quantum capability information, compute a relay path
   according to service requirements, translate the result into a
   network forwarding path, and carry the relayed key information in an
   IPv6/UDP packet steered by that path.

   This document describes an architectural framework for such a
   service.  Each QKD link provides its link quantum capability such as
   available quantum key rate capacity, and each relay node provides its
   node quantum capability . A controller uses these inputs together
   with application requirements to calculate a relay path.  The path-
   computation algorithm is not standardized and may be selected or
   defined by the user, operator, or implementation.  The calculated
   relay sequence is represented as an SRv6 path, and UDP packets
   following that path carry the key-relay information.

   This document identifies the protocol extension points needed to
   support the framework.  The detailed encodings, message formats,
   TLVs, and signaling procedures are left for future work and are
   marked as TBD.
- **draft-cheng-rift-srv6-extensions-05** (new-draft, score 0, ignored_after_review) [none]: [RIFT extensions for SRv6](https://datatracker.ietf.org/doc/draft-cheng-rift-srv6-extensions/) — The Segment Routing (SR) architecture allows a flexible definition
   of the end-to-end path by encoding it as a sequence of topological
   elements called segments.  It can be implemented over an MPLS or
   IPv6 data plane.  This document describes the RIFT extensions
   required to support Segment Routing over the IPv6 data plane (SRv6).
- **draft-cheng-rtgwg-adaptive-routing-framework-06** (new-draft, score 0, ignored_after_review) [none]: [Adaptive Routing Framework](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-adaptive-routing-framework/) — In many cases, ECMP (Equal-Cost Multi-Path) flow-based hashing leads
   to high congestion and variable flow completion time.  This reduces
   applications performance.  Load balancing based on local link quality
   is not always optimal, A global view of congestion, with information
   from remote links, is needed for optimal balancing.  Adaptive routing
   is a technology that makes dynamic routing decision based on changes
   in traffic load and network topology.

   This document describes a framework for Adaptive Routing.
   Specifically, it identifies a set of adaptive routing components,
   explains their interactions, and exemplifies the workflow mechanism.
- **draft-cheng-spring-srpolicy-ar-framework-01** (new-draft, score 0, ignored_after_review) [none]: [SR-TE Path Based on Quality-Aware Dynamic Adaptive Adjustment](https://datatracker.ietf.org/doc/draft-cheng-spring-srpolicy-ar-framework/) — This document defines a framework for quality-aware dynamic adaptive
   adjustment of Segment Lists within an SR-TE Candidate Path.  It
   addresses the limitation of static weight assignment, which cannot
   adapt to dynamic changes in path quality (e.g., latency, loss,
   utilization).  The framework enables continuous monitoring of end-to-
   end metrics for each Segment List, computation of updated weights
   proportional to their relative quality, and application at the policy
   head-end.  This allows the Candidate Path to autonomously optimize
   traffic distribution towards higher-quality paths, enhancing
   performance without altering the SR-Policy architecture.
- **draft-cheng-spring-traffic-steering-to-sr-00** (new-draft, score 0, ignored_after_review) [none]: [Traffic Steering Considerations for SR-MPLS and SRv6](https://datatracker.ietf.org/doc/draft-cheng-spring-traffic-steering-to-sr/) — This document describes traffic steering mechanisms for both Segment
   Routing over IPv6 (SRv6) and Segment Routing over MPLS (SR-MPLS).  It
   provides an overview of the main traffic steering methods applicable
   to both architectures, including steering based on destination
   addresses (BSID/Binding Label, Color/Endpoint, IGP Shortcut) and flow
   characteristics (DSCP, 802.1p, Service-class, TE-class, BGP-
   FlowSpec).  Furthermore, it discusses the recommended traffic
   steering methods for various typical scenarios, highlighting the
   interoperability and specific handling differences between SR-MPLS
   and SRv6 where necessary.
- **draft-choudhary-grow-bmp-bgp-msg-stats-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Message Counters for BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-choudhary-grow-bmp-bgp-msg-stats/) — The BGP Monitoring Protocol (BMP) [RFC7854] Statistics Report
   carries RIB occupancy, policy, and route-processing metrics.
   Some existing types count UPDATE messages, but only as special
   cases grouped by result (duplicates, loops, and errors).  No
   statistic gives a total count of each BGP message type.
   This document defines those totals as new BMP Statistics Types
   (UPDATE, KEEPALIVE, NOTIFICATION, ROUTE-REFRESH, and all BGP
   PDUs in each direction), states the operational use cases that
   motivate them, and records explicit non-goals so that last-error
   content, negotiated timer values, and implementation-specific
   internals remain out of scope.
- **draft-claise-opsawg-ipfix-ordered-ie-02** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
   Information Element to appear multiple times in a Template Record.
   RFC 7011 states that multiple occurrences of the same Information
   Element SHOULD follow the logical order of their treatments by the
   Metering Process; however, no protocol mechanism exists for the
   Exporting Process to explicitly signal to the Collecting Process that
   this ordering is guaranteed.  Without such a guarantee, the
   Collecting Process cannot safely interpret repeated Information
   Elements as ordered observations.  This document describes the
   problem, presents use cases, analyzes candidate solutions, and
   specifies a mechanism -- a new Ordered Set type -- that establishes
   an end-to-end ordering guarantee: the Metering Process records
   repeated Information Element values in the order the corresponding
   observations are made, the Exporting Process preserves and signals
   this guarantee, and the Collecting Process interprets the n-th
   occurrence of an Information Element as corresponding to the n-th
   observation by the Metering Process at the Observation Point.  This
   document updates RFC 7011, RFC 5476, and RFC 6183.
- **draft-claise-opsawg-ipfix-ordered-mpls-ie-00** (new-draft, score 0, ignored_after_review) [none]: [Generic MPLS Information Elements for Ordered Export in IPFIX](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-mpls-ie/) — This document defines new generic IPFIX Information Elements for MPLS
   label stacks and label attributes, intended for use with the ordered
   set mechanisms that provide an explicit ordering guarantee for
   repeated Information Elements.
- **draft-clayton-dkim-canmodify-00** (new-draft, score 0, ignored_after_review) [none]: [Permitted modifications to DKIM2 messages](https://datatracker.ietf.org/doc/draft-clayton-dkim-canmodify/) — DomainKeys Identified Mail v2 (DKIM2) requires any modifications made
   to email messages by intermediaries to be recorded in "recipes".
   Some originators wish to request that only very limited modifications
   be made to their messages so that the recipient of the message can
   have some assurance that the modifications were benign.  This
   document introduces the CanModify header field into which originator
   requests may be placed.  It then sets out a small set of
   modifications that are commonly applied by intermediaries and
   assesses how benign they may actually be.
- **draft-coffey-jmap-undelete-00** (new-draft, score 0, ignored_after_review) [none]: [JMAP Undelete: Recovering Destroyed Objects](https://datatracker.ietf.org/doc/draft-coffey-jmap-undelete/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) that lets a client find and restore objects that were
   permanently destroyed within a server-defined retention period.  It
   defines a new capability, a DeletedItem data type that describes a
   destroyed object of any supported data type, and a DeletedItem/
   restore method that recreates it.  Rules are given for Email,
   ContactCard, CalendarEvent, FileNode, and SieveScript objects.
   Servers can already keep destroyed data for a time.  This extension
   gives clients an interoperable way to show what can be recovered, for
   how long, and to recover it.
- **draft-contreras-bpm-calibration-00** (new-draft, score 0, ignored_after_review) [none]: [Calibration of Measured Time Values between Network Elements](https://datatracker.ietf.org/doc/draft-contreras-bpm-calibration/) — Network devices are incorporating capabilities for time stamping
   certain packets so that such time stamps can reference the time at
   which a packet passes through a given device (at ingress or egress).
   Those stamps or marks are relevant to calculating the measured delay
   and can be used for traffic engineering purposes.

   To ensure consistency and accuracy across different network element
   implementations, a benchmarking procedure is necessary to calibrate
   the timestamps.  Such a procedure can permit the identification and
   correction of any deviations or biases in the time stamps produced by
   diverse devices.  This document proposes a methodology for
   Calibrating the measurements from different network element
   implementations in a common measurement scenario.
- **draft-contreras-detnet-preof-oam-01** (new-draft, score 0, ignored_after_review) [none]: [PREOF Observability and OAM Requirements](https://datatracker.ietf.org/doc/draft-contreras-detnet-preof-oam/) — Packet Replication, Elimination, and Ordering Functions (PREOF)
   enables highly reliable packet delivery through path redundancy and
   packet sequencing mechanisms in DetNet domains.

   Existing DetNet Operations, Administration, and Maintenance (OAM)
   specifications provide mechanisms for monitoring service
   connectivity, packet loss, delay, and overall service performance.
   However, they do not provide detailed operational visibility into the
   behavior of PREOF functions themselves.

   This document identifies operational observability gaps associated
   with PREOF, defines requirements for PREOF-specific OAM, and
   introduces a set of observable events and metrics to monitor,
   troubleshoot, and validate PREOF operation independently of the
   underlying DetNet data plane technology.  The requirements, metrics
   and rest of information are intended to be independent of the
   underlying DetNet data plane and may be realized using different
   management, telemetry, or OAM mechanisms.
- **draft-czz-rtgwg-elastic-bandwidth-routing-01** (new-draft, score 0, ignored_after_review) [none]: [Elastic Bandwidth-aware Routing Framework](https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/) — IGP normally computes the shortest paths in a network for packet
   forwarding, without taking the traffic demands and available
   bandwidth into consideration.  When there is a link degradation or
   partial link failure in a network which causes throughput reduction,
   or the volume of specific traffic flows increase dramatically,
   unexpected congestion may happen if only the shortest paths are used
   for IP forwarding.

   Conventional centralized Traffic Engineering (TE) focuses on long-
   term bandwidth and routes planning based on traffic demands, which
   can not react to the congestions in networks timely.

   This document describes a distributed path computation and load
   balancing mechanism named Elastic Bandwidth-aware Routing (EBR),
   which can alleviate congestions timely before TE finishes the global
   optimization.  It allows IGP-enabled nodes which face congestion to
   distribute traffic among the shortest paths and load-balancing
   alternate paths through Segment Routing (SR) strict path, with
   weights determined based on the bandwidth utilization and available
   bandwidth of these paths.  It provides an efficient, accurate and
   backward compatible approach for dynamic link congestion avoidance.
- **draft-dhody-pce-pcep-object-order-09** (new-draft, score 0, ignored_after_review) [none]: [Updated Rules for PCE Communication Protocol (PCEP) Object Ordering](https://datatracker.ietf.org/doc/draft-dhody-pce-pcep-object-order/) — The PCE Communication Protocol (PCEP) defines the mechanisms for the
   communication between a Path Computation Client (PCC) and a PCE, or
   among PCEs.  Such interactions include path computation requests and
   path computation replies defined in RFC 5440.  As per RFC 5440, these
   messages are required to follow strict object ordering.

   This document updates RFC 5440 by relaxing the strict object ordering
   requirement in the PCEP messages.
- **draft-dong-lsvr-bgp-spf-selection-05** (new-draft, score 0, ignored_after_review) [none]: [Proposed Update to BGP Link-State SPF NLRI Selection Rules](https://datatracker.ietf.org/doc/draft-dong-lsvr-bgp-spf-selection/) — For network scenarios such as Massively Scaled Data Centers (MSDCs),
   BGP is extended for Link-State (LS) distribution and the Shortest
   Path First (SPF) algorithm based calculation.  BGP-LS-SPF leverages
   the mechanisms of both BGP protocol and BGP-LS protocol extensions,
   with new selection rules defined for BGP-LS-SPF NLRI.  This document
   proposes some updates to the BGP-LS-SPF NLRI selection rules, so as
   to improve the route updates and convergence, while consistent SPF
   computation result can still be achieved.  This document updates the
   NLRI selection rules in I-D.ietf-lsvr-bgp-spf.
- **draft-dong-pce-cc-nrp-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for PCE Central Controller (PCECC) based Network Resource Partition (NRP) Instantiation](https://datatracker.ietf.org/doc/draft-dong-pce-cc-nrp/) — The PCE is a core component of Software-Defined Networking (SDN)
   systems.  A PCE-based Central Controller (PCECC) can simplify the
   processing of a distributed control plane by blending it with
   elements of SDN without necessarily completely replacing it.

   Network Resource Partitions (NRPs) can be used to provide the
   required connectivity and commited resources for network slice
   services.  An NRP is a subset of the buffer/queuing/ scheduling
   resources and associated policies on each of a connected set of links
   in the underlay network.

   This document specifies the extensions to Path Computation Element
   Communication Protocol (PCEP) to enable PCECC based Network Resource
   Partition (NRP) Instantiation.
- **draft-dong-pcep-flowspec-srv6-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extension for SRv6 Flow Specification](https://datatracker.ietf.org/doc/draft-dong-pcep-flowspec-srv6/) — This document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) to support Flow Specification for
   Segment Routing over IPv6 (SRv6).  Building upon the PCEP Flow
   Specification framework defined in RFC 9168, this specification
   introduces new PCEP Flow Specification TLVs to enable filtering and
   steering of IPv6 packets based on the structural components of
   standard SRv6 Segment Identifiers (SIDs) or SRv6 Compressed SID
   (CSID) containers present in IPv6 Destination Addresses or Segment
   Routing Headers (SRH).
- **draft-du-lsvr-area-scoped-bgp-spf-00** (new-draft, score 0, ignored_after_review) [none]: [Area-Scoped Link-State Distribution for BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-du-lsvr-area-scoped-bgp-spf/) — BGP Link-State Shortest Path First (BGP-LS-SPF) routing, defined in
   RFC 9815, uses BGP to distribute link-state information and the SPF
   algorithm to compute routes.  In large-scale networks with frequent
   topology changes, distributing detailed link-state information across
   the entire network may introduce significant control-plane overhead
   and frequent route recomputation.

   This document proposes an area-scoped routing mechanism for BGP-LS-
   SPF.  The mechanism divides a network into multiple routing areas,
   limits the distribution of detailed topology information, and
   maintains inter-area reachability through boundary routers.  It aims
   to improve routing scalability and stability while supporting
   distributed route computation.
- **draft-duke-scone-scone-echo-04** (new-draft, score 0, ignored_after_review) [none]: [In-Band SCONE Reporting over QUIC](https://datatracker.ietf.org/doc/draft-duke-scone-scone-echo/) — The SCONE protocol relies on the receiver of SCONE packets to send
   bandwidth estimates back to the sender via unspecified application-
   layer messages.  In some cases, a peer might have SCONE receive
   capability at the QUIC layer but not implement the necessary
   application level functionality.  A new QUIC frame that directly
   reports the contents of received SCONE packets can address these use
   cases.  There are no changes in the interaction with SCONE Network
   Elements.
- **draft-eddy-scone-tcp-00** (new-draft, score 0, ignored_after_review) [none]: [SCONE TCP Option](https://datatracker.ietf.org/doc/draft-eddy-scone-tcp/) — This document describes a TCP option that permits network elements to
   provide TCP endpoints advice on rate limits within the network.  The
   functionality for TCP is analogous to SCONE packets within the QUIC
   protocol.
- **draft-eggert-appeal-support-02** (new-draft, score 0, ignored_after_review) [none]: [Requiring Support for Appealing to the IESG and IAB](https://datatracker.ietf.org/doc/draft-eggert-appeal-support/) — RFC2026 describes the procedure for appealing decisions or process
   failures to the IESG and the IAB.  This document updates RFC2026 and
   requires that an appellant must first gain support for their appeal
   before an appeal may be considered by the body it is submitted to.
- **draft-ek-dtn-qubicle-03** (new-draft, score 0, ignored_after_review) [none]: [DTN QUIC Bundle Protocol Convergence Layer (qubicle)](https://datatracker.ietf.org/doc/draft-ek-dtn-qubicle/) — This document specifies a minimal convergence layer protocol for
   transferring Bundle Protocol version 7 (BPv7) bundles over QUIC.  The
   protocol leverages QUIC's native capabilities for reliable streaming,
   connection management, and security.  Reliable transfers use QUIC
   unidirectional streams carrying CBOR Sequences of definite-length
   byte strings, each containing exactly one bundle.  A stream can carry
   successive bundles without closing between them.  Unreliable
   transfers use the Bundle Transfer Protocol - Unidirectional (BTP-U)
   over QUIC datagrams.
- **draft-ek-intarea-ip-enclave-signaling-00** (new-draft, score 0, ignored_after_review) [none]: [IP Enclave Boundary Signaling](https://datatracker.ietf.org/doc/draft-ek-intarea-ip-enclave-signaling/) — This document defines optional ICMP extension objects that a gateway
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
- **draft-englishm-moq-content-stitching-00** (new-draft, score 0, ignored_after_review) [none]: [Content Stitching for Media over QUIC](https://datatracker.ietf.org/doc/draft-englishm-moq-content-stitching/) — Media over QUIC Transport (MOQT) requires that an Object is always
   the same bytes, no matter who asks for it or where it is retrieved
   from.  That property is what makes MOQT content cacheable by relays.
   It also means that when different subscribers need to receive
   different content, the straightforward approach is to publish a
   separate track for each of them, even when most of what those tracks
   carry is the same.  This document describes content stitching:
   building the tracks that subscribers receive out of Objects taken
   from other tracks, so shared Objects can be cached once while each
   audience still receives a track of its own.  It names the pieces
   involved, describes how they fit together, works through some
   examples, and draws a line between a stitcher and a relay.  It does
   not define a format or mechanism for stitching.
- **draft-englishm-moq-relay-dos-02** (new-draft, score 0, ignored_after_review) [none]: [Denial-of-Service Considerations for Media over QUIC Relay Deployments](https://datatracker.ietf.org/doc/draft-englishm-moq-relay-dos/) — The Media over QUIC Transport (MoQT) protocol presents denial-of-
   service risks that differ in character from those facing typical
   request-response protocols.  MoQT relays forward, fan out, and
   optionally cache media content on behalf of publishers and
   subscribers.  This document complements the MoQT Security
   Considerations, focusing on the unique considerations for relays.
- **draft-ezema-lookalike-sender-detection-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Detecting Look-Alike Sender Identities in Platform Messaging](https://datatracker.ietf.org/doc/draft-ezema-lookalike-sender-detection/) — Users of consumer platforms -- job boards, marketplaces, education
   and early-career services -- receive messages from other parties
   inside the platform, where no enterprise mail gateway inspects them.
   Attackers impersonate the platform's own brand and support staff, and
   pose as recruiters or counterparties, using look-alike domains and
   display names.  This document describes considerations for detecting
   look-alike sender identities at the level of the individual message
   and its sender, rather than at the domain-registration level.  It
   records two concrete pitfalls observed in deployed libraries: Unicode
   confusable "skeleton" equality alone does not catch all mixed-script
   look-alikes, and several input validators accept host names
   containing invisible format characters.  This document is
   informational and specifies no protocol.
- **draft-fainchtein-diem-architecture-00** (new-draft, score 0, ignored_after_review) [none]: [DIEM Architecture](https://datatracker.ietf.org/doc/draft-fainchtein-diem-architecture/) — TODO Abstract

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at
   https://rahelFain.github.io/Diem-Architecture/draft-Fainchtein-DIEM-
   Architecture.html.  Status information for this document may be found
   at https://datatracker.ietf.org/doc/draft-fainchtein-diem-
   architecture/.

   Source for this draft and an issue tracker can be found at
   https://github.com/rahelFain/Diem-Architecture.
- **draft-fedyk-netmod-yang-normal-form-01** (new-draft, score 0, ignored_after_review) [none]: [Extending Normalized Forms to String-Derived Types](https://datatracker.ietf.org/doc/draft-fedyk-netmod-yang-normal-form/) — YANG models frequently define identifiers using string or string-
   derived types whose lexical space permits multiple representations of
   the same underlying value.  This can lead to incorrect behavior when
   semantically equivalent values are compared lexically.

   This document adds an optional extension to the existing YANG concept
   of normalized form to string-derived types whose lexical space
   permits multiple representations of the same underlying value.
- **draft-fernandez-dnsop-client-side-adox-signal-00** (new-draft, score 0, ignored_after_review) [none]: [Client-side Request for Encrypted Authoritative DNS Queries](https://datatracker.ietf.org/doc/draft-fernandez-dnsop-client-side-adox-signal/) — This document describes an EDNS0 option that a client can attach to a
   DNS query to signal to a recursive resolver that it SHOULD prefer
   encrypted transports while resolving the query.  The option can also
   be used on the return path by the resolver to signal whether
   encryption was achievable or not.
- **draft-fetch-validation-vmc-wchuang-12** (new-draft, score 0, ignored_after_review) [none]: [Fetch and Validation of Verified Mark Certificates](https://datatracker.ietf.org/doc/draft-fetch-validation-vmc-wchuang/) — A description of how entities wishing to validate a Verified Mark
   Certificate (VMC) should retrieve and validate these documents.
   This document is a companion to BIMI core specification, which should
   be consulted alongside this document.
- **draft-fizgeer-pce-lsp-validation-extensions-01** (new-draft, score 0, ignored_after_review) [none]: [PCE LSP validation Extensions in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-fizgeer-pce-lsp-validation-extensions/) — The Path Computation Element Communication Protocol (PCEP) provides
   mechanisms for Path Computation Elements (PCEs) to instantiate and
   manage Label Switched Paths (LSPs) on a Path Computation Client
   (PCC).  A Stateful PCE RFC8231 can instantiate LSPs on a PCC.  In
   some cases, the PCC shall perform additional validations and/or
   actions.  If some validations or actions fail, the LSP will not be
   created and established or updated.  This document specifies PCEP
   extensions to handle this situation gracefully in case the problem
   can be resolved by some network changes (freeing up resources,
   restoring or changing the network, and so on).  This draft defines
   common usage of the new flag and known use cases for using this flag.
   Each draft relevant to LSP creation can add a corresponding bit to
   the use case list.
- **draft-fl-nmop-device-yang-vendor-mapping-00** (new-draft, score 0, ignored_after_review) [none]: [An Experiment: Mapping IETF Device YANG Models to Vendors](https://datatracker.ietf.org/doc/draft-fl-nmop-device-yang-vendor-mapping/) — This document describes an experimental implementation of a YANG to
   YANG translation function layer providing a northbound interface for
   configuring networking devices using a set of IETF 'device' YANG
   modules.  The southbound interface of the function implements the
   proprietary, vendor YANG modules which are implemented natively on
   devices to be configured.  The expected benefits of such an approach
   are the ability to provide a stable, standardised, and vendor/device
   agnostic interface for the configuration and maintenance of devices.
   The main purposes for this experiment is to validate the overall
   approach, and to identify, and describe the different YANG-to-YANG
   translation techniques that can be used.
- **draft-frindell-moq-timestamp-01** (new-draft, score 0, ignored_after_review) [none]: [Timestamp Properties for MOQT](https://datatracker.ietf.org/doc/draft-frindell-moq-timestamp/) — This document defines a set of MOQT Properties for carrying per-
   Object timestamps efficiently.  The encoded timestamp is intended for
   use in MOQT, but can be referenced for application specific purposes.
- **draft-fujiwara-dnsop-dns-upper-limit-values-06** (new-draft, score 0, ignored_after_review) [none]: [Upper limit values for DNS](https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-dns-upper-limit-values/) — DNS was designed to have as few hard upper limits as possible to
   allow for future extensibility.  However, the lack of a clear upper
   limit leads to vulnerabilities, and several attack methods have been
   reported.  This document collects upper limit values implemented by
   DNS software to avoid vulnerabilities.
- **draft-fujiwara-dnsop-ranking-data-02** (new-draft, score 0, ignored_after_review) [none]: [Clarifications to the DNS Ranking Data](https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/) — This document obsoletes Section 5.4.1 (Ranking data) of RFC 2181, and
   specifies directives whereby the source of the data determines for
   what purposes it may be used.
- **draft-gakiwate-dnsop-optimistic-dns-01** (new-draft, score 0, ignored_after_review) [none]: [Optimistic DNS](https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-optimistic-dns/) — DNS lookups introduce user-visible delay, particularly when cached
   records have expired and must be refreshed from the network.  This
   document describes Optimistic DNS, a client-side stub resolver
   mechanism that immediately returns expired cached DNS records to
   applications while simultaneously refreshing them with a network
   query.  The application receives an answer in microseconds rather
   than milliseconds, and if the data has changed receives an updated
   answer shortly thereafter.  Optimistic DNS is complementary to RFC
   8767, which addresses serving stale data at recursive resolvers.
   This document focuses exclusively on client-side stub resolver
   behavior, including explicit signaling from the application to inform
   the stub resolver that the application is able to handle old and
   possibly incorrect information.
- **draft-gandhi-bpm-stamp-link-crc-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extension for Link CRC Error Measurement](https://datatracker.ietf.org/doc/draft-gandhi-bpm-stamp-link-crc/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, supports active measurement of network performance.  This
   document defines a STAMP Type-Length-Value (TLV) that reports
   receive-side link statistics: packets received, packets received with
   Cyclic Redundancy Check (CRC) errors, and bytes received.  The link
   is identified using the Micro-session ID TLV specified in RFC 9534.
   These measurements support fiber-quality monitoring to provide SLA
   assurance.
- **draft-gandhi-bpm-stamp-udp-lite-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) over UDP-Lite](https://datatracker.ietf.org/doc/draft-gandhi-bpm-stamp-udp-lite/) — This document specifies the Simple Two-Way Active Measurement
   Protocol (STAMP) as defined in RFC 8762 and extended in RFC 8972,
   over the Lightweight User Datagram Protocol (UDP-Lite) for IPv4 and
   IPv6.  Partial checksum coverage accommodates timestamp insertion
   after the checksum computation while protecting the integrity of
   transport header and IP pseudo-header.

   This document updates RFC 8762 to permit an explicitly selected UDP-
   Lite transport with the existing UDP port number rules.

   This document also updates RFC 8972 for transport-aware session
   identification, payload length determination, UDP port number
   reporting in the Location TLV, and replacing the use of the UDP
   Length field for detecting optional STAMP TLVs.  STAMP payload
   formats and existing UDP-based sessions are unchanged.
- **draft-ginsberg-lsr-reliable-snp-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Reliable SNP](https://datatracker.ietf.org/doc/draft-ginsberg-lsr-reliable-snp/) — Complete Sequence Number PDUs (CSNPs) are exchanged as part of
   adjacency bringup on point-to-point interfaces.  However, this
   exchange is unreliable.  This document defines protocol extensions to
   support reliable exchange of CSNPs as well as optimizations to the
   encoding of advertisements in Sequence Number PDUs.
- **draft-gomez-tiptop-coap-02** (new-draft, score 0, ignored_after_review) [none]: [CoAP in Space](https://datatracker.ietf.org/doc/draft-gomez-tiptop-coap/) — This document provides guidance on using the Constrained Application
   Protocol (CoAP) in deep space environments.  The document focuses on
   the approach whereby an IP protocol stack is used for end-to-end
   communication.
- **draft-gondwana-dkim2-debug-header-03** (new-draft, score 0, ignored_after_review) [none]: [A Diagnostic Header Field for DKIM2 Implementations](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-debug-header/) — Implementations of DomainKeys Identified Mail Signatures v2 (DKIM2)
   benefit from seeing extra debug information during the early
   deployment phase.

   This document is intended to help testers, and unlikely to be
   published.
- **draft-gondwana-email-header-maintenance-04** (new-draft, score 0, ignored_after_review) [none]: [Maintenance of the IANA Message Header Field Registries](https://datatracker.ietf.org/doc/draft-gondwana-email-header-maintenance/) — The IANA "Message Headers" registries record, for each registered
   header field, the protocol it belongs to, its status, whether it is a
   trace field, and the documents that specify it.  Many documents have
   added entries over more than two decades, and the metadata in the
   registries is less complete than the metadata those documents
   supplied.  RFC 4021, which performed the largest single bulk
   registration, gave IANA an explicit status and an explicit
   specification document for each of the roughly ninety fields it
   registered.  Neither was recorded.  Those entries carry a blank
   status and cite RFC 4021 itself in place of the specification.  This
   document updates RFC 4021 by directing IANA to record the values its
   registration templates supplied.  The "Trace" column, added to both
   registries by the revision of RFC 5322, was deliberately left empty
   for existing entries so that it could be filled in later.

   This document reviews the definition of each registered header field
   and every subsequent update to it, and gives IANA a single set of
   instructions for completing and correcting each entry.  Each
   recommended change, and each decision to leave a non-obvious entry
   unchanged, is justified from the instructions or the clear intent of
   the documents that defined or modified the field.
- **draft-gong-sidrops-rtr-push-00** (new-draft, score 0, ignored_after_review) [none]: [Push Mode Extension for the RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-gong-sidrops-rtr-push/) — The Resource Public Key Infrastructure (RPKI) to Router Protocol
   (RTR) enables routers to receive validated RPKI data from Relying
   Parties (RPs).  This document defines a push mode extension for RTR
   that allows RPs to proactively push RPKI data updates to routers,
   either periodically or event-driven.
- **draft-gravit-graviteron-00** (new-draft, score 0, ignored_after_review) [none]: [The Graviteron: A Unit for the Weight of Independent Evidence](https://datatracker.ietf.org/doc/draft-gravit-graviteron/) — This document defines the Graviteron, a unit that states how much
   signed, independent evidence supports or contradicts a claim.  A
   Graviteron reading is the weight of evidence of Turing and Good,
   expressed in decibans: ten times the base-10 logarithm of the factor
   by which independent checks change the odds of the claim.  The
   document specifies the computation from operator verdicts and
   measured operator reliability, eight properties that every conforming
   implementation must satisfy, a reading format that is never a bare
   number, and language-neutral test vectors.  It does not define a
   decision rule.
- **draft-gray-plants-mtc-ldp-00** (new-draft, score 0, ignored_after_review) [none]: [Landmark Distribution Point Fetching for Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-gray-plants-mtc-ldp/) — This document specifies a mechanism for a relying party to retrieve
   Merkle-tree subtree consistency proofs needed to validate a landmark-
   relative Merkle Tree Certificate (MTC).  An X.509 certificate
   extension identifies one or more Landmark Distribution Points (LDPs).
   A relying party requests a proof set from an LDP and validates the
   proof chain against a trusted, signed target checkpoint.
- **draft-gu-grow-bmp-route-leak-detection-07** (new-draft, score 0, ignored_after_review) [none]: [BMP for BGP Route Leak Detection](https://datatracker.ietf.org/doc/draft-gu-grow-bmp-route-leak-detection/) — According to Route-Leak Problem Definition [RFC7908], Route leaks
   refer to the case that the delivery range of route advertisements is
   beyond the expected range.  For many current security protection
   solutions, the ISPs (Internet Service Providers) are focusing on
   finding ways to prevent the happening of BGP [RFC4271] route leaks.
   However, the real-time route leak detection if any occurs is
   important as well, and serves as the basis for leak mitigation.  This
   document extends the BGP Monitoring Protocol (BMP) [RFC7854] to
   provide a routing security scheme suitable for ISPs to detect BGP
   route leaks at the prefix level.
- **draft-gundavelli-scone-wifi-applicability-01** (new-draft, score 0, ignored_after_review) [none]: [SCONE Applicability for IEEE 802.11 Access Networks](https://datatracker.ietf.org/doc/draft-gundavelli-scone-wifi-applicability/) — This document describes the applicability of the Standard
   Communication with Network Elements (SCONE) protocol to IEEE 802.11
   based access networks.  SCONE defines a mechanism by which an on-path
   network element can provide advisory downlink throughput guidance to
   QUIC endpoints.  The SCONE protocol is access agnostic and does not
   assume any specific access technology.

   In IEEE 802.11 deployments, such constraints may be derived at access
   points or controllers that combine policy awareness, with visibility
   into access network conditions.  This document explains how existing
   SCONE roles and throughput advice semantics apply in these
   deployments without assuming any specific IEEE 802.11 MAC or PHY
   behavior.

   This document does not define new protocol extensions and does not
   modify SCONE behavior.  Its purpose is to clarify deployment
   considerations for IEEE 802.11 environments.
- **draft-gupta-httpapi-events-query-04** (new-draft, score 0, ignored_after_review) [none]: [HTTP Events Query](https://datatracker.ietf.org/doc/draft-gupta-httpapi-events-query/) — Events Query is a minimal protocol built on top of HTTP that allows
   user agents to receive event notifications directly from any resource
   of interest.  It uses the HTTP QUERY method to request (optionally)
   the current representation and subsequent event notifications within
   a single response.  The Events Query Protocol (EQP) is predicated on
   the idea that the most intuitive source for event notifications is
   the resource itself.
- **draft-guthrie-cnsa2-ipsec-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for IPsec](https://datatracker.ietf.org/doc/draft-guthrie-cnsa2-ipsec-profile/) — This document defines a base profile for IPsec for use with the US
   Commercial National Security Algorithm (CNSA) 2.0 Suite, a
   cybersecurity advisory that outlines quantum-resistant cryptographic
   algorithm policy for national security applications.  This profile
   applies to the capabilities, configuration, and operation of all
   components of US National Security Systems that employ IPsec.  It is
   also appropriate for all other US Government systems that process
   high-value information.  This memo is not an IETF standard, and has
   not been shown to have IETF community consensus.  This profile is
   made publicly available for use by developers and operators of these
   and any other system deployments.
- **draft-halmir-mpls-ecn-05** (new-draft, score 0, ignored_after_review) [none]: [Explicit Congestion Notification Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-halmir-mpls-ecn/) — It has been broadly demonstrated that user experience improvements
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
- **draft-halpern-rtgwg-not-a-dump-truck-01** (new-draft, score 0, ignored_after_review) [none]: [The IGP is not a Dump Truck](https://datatracker.ietf.org/doc/draft-halpern-rtgwg-not-a-dump-truck/) — This document explores addressing the problem of using an IGP to
   carry arbitrary information, often referred to using the phrase "the
   IGP is not a dump truck".  It describes the kinds of information
   carried in an IGP and proposes an approach to changing the system.
- **draft-han-opsawg-ipfix-microburst-00** (new-draft, score 0, ignored_after_review) [none]: [Export of Microburst Information in IP Flow Information Export](https://datatracker.ietf.org/doc/draft-han-opsawg-ipfix-microburst/) — A microburst is a phenomenon in which arriving traffic exceeds the
   service capacity of an egress interface within a short period of
   time, causing queue occupancy to rise rapidly.  It may result in
   transient queuing and packet loss even when the average link
   utilization is low, and is therefore difficult to detect through low-
   frequency interface statistics.

   This document defines a set of IPFIX Information Elements for
   exporting aggregated microburst statistics per egress interface,
   egress queue, and measurement window.  Network operators can use
   these statistics to identify interfaces and queues where microbursts
   occur frequently, and apply the results to capacity planning, QoS
   optimization, and the remediation of critical links.

   This document does not specify microburst detection algorithms,
   threshold selection methods, or remediation policies.
- **draft-han-pce-fgmtn-00** (new-draft, score 0, ignored_after_review) [none]: [Path Computation Element Communication Protocol (PCEP) Extension for Fine Granularity Metro Transport Network (fgMTN)](https://datatracker.ietf.org/doc/draft-han-pce-fgmtn/) — This document focuses on the PCEP extension for G.8312 fine
   granularity metro transport network.  It extends PCEP-LS to report
   the fgMTN topology resource information, and provides the PCEP
   extension to support the fgMTNP path setup information.
- **draft-hancke-tsvwg-snap-01** (new-draft, score 0, ignored_after_review) [none]: [SCTP Negotiation Acceleration Protocol](https://datatracker.ietf.org/doc/draft-hancke-tsvwg-snap/) — WebRTC Data Channels use the Stream Control Transmission Protocol
   (SCTP) over a Datagram Transport Layer Security (DTLS) association.
   The standard SCTP connection establishment requires a handshake that
   introduces latency.  This document specifies a method to accelerate
   the datachannel establishment by embedding the SCTP initialization
   parameters within the Session Description Protocol (SDP) offer/answer
   exchange.  This reduces the time required to open a data channel by
   up to two network round-trip times.
- **draft-hancke-webrtc-sped-01** (new-draft, score 0, ignored_after_review) [none]: [STUN Protocol for Embedding DTLS (SPED)](https://datatracker.ietf.org/doc/draft-hancke-webrtc-sped/) — WebRTC setup normally serializes ICE and DTLS, adding at least one
   extra round trip before secure media can flow.  This document defines
   the STUN Protocol for Embedding DTLS (SPED), which carries DTLS
   handshake data and acknowledgements inside STUN Binding Requests and
   Responses.  SPED allows ICE and DTLS to proceed in parallel, improves
   setup behavior under loss, and remains backward compatible with
   existing ICE processing.
- **draft-hares-idr-fsv2-more-ip-actions-04** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification Version 2 - More IP Actions](https://datatracker.ietf.org/doc/draft-hares-idr-fsv2-more-ip-actions/) — The BGP flow specification version 2 (FSv2) for Basic IP defines user
   ordering of filters along with FSv1 IP Filters and FSv2 actions in
   Extended Communites.  This draft suggests a method of encoding user
   ordered actions in a community attribute in BGP.
- **draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC with SigTag Extension](https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/) — This document describes a mechanism to reduce post-quantum
   cryptographic (PQC) network transmission overhead when using Merkle
   Tree Ladders (MTL) in DNS Security Extensions (DNSSEC).  This
   document refers to this as SigTag and describes the use of EDNS(0) to
   enable its use.  SigTag allows a client to indicate its knowledge of
   a specific MTL ladder.  The DNS server can then use this signal to
   determine if it can omit the full underlying signature in its
   response, thereby reducing the message payload.
- **draft-he-bpm-congestion-loss-monitoring-arch-00** (new-draft, score 0, ignored_after_review) [none]: [An Architectural Framework for Monitoring Packet Loss Caused by Network Congestion](https://datatracker.ietf.org/doc/draft-he-bpm-congestion-loss-monitoring-arch/) — Network congestion can lead to performance degradation and increase
   uncertainty in service delivery, so real-time congestion monitoring
   is necessary.  This document describes a comprehensive packet loss
   monitoring architectural framework.  The proposed scheme is capable
   to not only determine the time and location of packet loss
   occurrence, make the accurate statistics of discarded packets, parse
   what traffic flows are contained in discarded packets and identify
   what traffic flows lead to microburst, but also obtain accurate
   packet loss ratio results.  More importantly, the proposed scheme can
   achieve little or even no interference to network, and is applicable
   to any data plane without modifying the forwarding chip and packet
   header as existing measurement methods do.
- **draft-he-bpm-ioam-dex-extensions-incorporating-am-00** (new-draft, score 0, ignored_after_review) [none]: [IOAM Direct Exporting (DEX) Option Extensions for Incorporating the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-he-bpm-ioam-dex-extensions-incorporating-am/) — In situ Operations, Administration, and Maintenance (IOAM) is used
   for recording and collecting operational and telemetry information.
   Specifically, passport-based IOAM allows telemetry data generated by
   each node along the path to be pushed into data packets when they
   traverse the network, while postcard-based IOAM allows IOAM data
   generated by each node to be directly exported without being pushed
   into in-flight data packets.  The Alternate-Marking method is used to
   measure performance metrics on live traffic, such as packet loss,
   delay, and jitter.  This document extends IOAM Direct Export (DEX)
   Option-Type to integrate the Alternate-Marking Method into IOAM to
   augment IOAM in performance measurement.
- **draft-he-bpm-ioam-extensions-incorporating-am-00** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace Option Extensions for Incorporating the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-he-bpm-ioam-extensions-incorporating-am/) — In situ Operation, Administration, and Maintenance (IOAM) is used for
   recording and collecting operational and telemetry information, which
   leverages IOAM Trace Option to incorporate IOAM data fields into in-
   flight data packets.  The Alternate-Marking method is used to measure
   performance metrics on live traffic, such as packet loss, delay, and
   jitter.  This document extends IOAM Trace Option for incorporating
   the Alternate-Marking method to augment IOAM in performance
   measurement.
- **draft-he-bpm-ioam-trace-type-bandwidth-00** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace-Type Extensions for Path bandwidth](https://datatracker.ietf.org/doc/draft-he-bpm-ioam-trace-type-bandwidth/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can accommodate the capacity of the traffic to be
   scheduled.  In situ Operations, Administration, and Maintenance
   (IOAM) is used for recording and collecting operational and telemetry
   information.  This document defines two bit flags within IOAM Trace-
   Type for carrying bandwidth information.
- **draft-hecker-dawn-intent-capability-gap-00** (new-draft, score 0, ignored_after_review) [none]: [The Intent-to-Capability Knowledge Gap in Discovery of Agents With Names](https://datatracker.ietf.org/doc/draft-hecker-dawn-intent-capability-gap/) — DAWN defines discovery as an initial step that returns minimum
   discoverable information (MDI) about entities.  Clients, however,
   usually start from an intent, not from a name or a capability, and
   the capabilities needed to satisfy an intent depend on what is
   available.  A client therefore has to know what is on offer to
   decide what to look for, and has to decide what to look for to learn
   what is on offer.

   This document describes that circular dependency, locates it in the
   current DAWN documents, compares five strategies for handling it,
   and lists questions for the Architecture work.  The main question is
   what the MDI must contain for a client to act without a pre-agreed
   capability vocabulary.  This document proposes no protocol.
- **draft-hmntsharma-grow-bmp-over-tls-02** (new-draft, score 0, ignored_after_review) [none]: [BMPS: Transport Layer Security for BGP Monitoring Protocol](https://datatracker.ietf.org/doc/draft-hmntsharma-grow-bmp-over-tls/) — The BGP Monitoring Protocol (BMP) defines the communication between a
   BMP station and multiple routers, referred to as network elements
   (NEs).  This document describes BMP over TLS, which uses Transport
   Layer Security (TLS) to ensure secure transport between the NE and
   the BMP monitoring station.  It updates [RFC7854] regarding BMP
   session establishment and termination.
- **draft-holmgren-at-repository-04** (new-draft, score 0, ignored_after_review) [none]: [Authenticated Transfer: Repository and Synchronization](https://datatracker.ietf.org/doc/draft-holmgren-at-repository/) — This document specifies a repository data structure and
   synchronization mechanisms for public data as part of the
   Authenticated Transfer Protocol (ATP).  It describes encoding formats
   for both individual data records and entire repositories.  The
   repository data structure is content-addressable and
   cryptographically authenticated.  For synchronization, it specifies
   both a low-latency streaming protocol over WebSocket, and a full-
   repository fetch mechanism over HTTP.
- **draft-housley-asn1-layman-guide-05** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-howe-vcon-wtf-extension-03** (new-draft, score 0, ignored_after_review) [none]: [vCon World Transcription Format Extension](https://datatracker.ietf.org/doc/draft-howe-vcon-wtf-extension/) — This document defines the World Transcription Format (WTF) extension
   for Virtualized Conversations (vCon).  The WTF extension provides a
   standardized analysis framework for representing speech-to-text
   transcription data from multiple providers within vCon containers.
   This extension defines a comprehensive analysis format that enables
   consistent transcription processing, quality assessment, and
   interoperability across different transcription services while
   preserving provider-specific features through extensible fields.

   The WTF extension is designed as a Compatible Extension that
   introduces a new analysis type for transcription data without
   altering existing vCon semantics, ensuring backward compatibility
   with existing vCon implementations.
- **draft-huitema-ccwg-c4-test-05** (new-draft, score 0, ignored_after_review) [none]: [Testing of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design was validated by
   series of simulations, and also by initial deployments in control
   networks.  We describe here these simulations and tests.
- **draft-iab-protocol-greasing-02** (new-draft, score 0, ignored_after_review) [iab]: [Considerations For Maintaining Protocols Using Grease and Variability](https://datatracker.ietf.org/doc/draft-iab-protocol-greasing/) — Active use and maintenance of network protocols is an important way
   to ensure that protocols remain interoperable and extensible over
   time.  Techniques such as intentionally exercising extension points
   with non-meaningful values (referred to as "grease") or adding
   variability to how protocol elements are used help generate this
   active use.

   Grease and variability are used across various protocols developed by
   the IETF.  This document discusses considerations when designing and
   deploying grease and variability mechanisms, and provides advice for
   making them as effective as possible.
- **draft-iab-rfc3113bis-00** (new-draft, score 0, ignored_after_review) [iab]: [3GPP-IETF Standardization Collaboration](https://datatracker.ietf.org/doc/draft-iab-rfc3113bis/) — The objective of the collaboration between 3GPP and IETF is securing
   timely development of technical specifications, and to facilitate
   maximum interoperability with existing fixed and mobile Internet
   systems, devices, and protocols.  This document summarizes some high-
   level principles of cooperation and the coordination between both
   organizations while leaving out the detailed descriptions to be
   specified and maintained by the coordination function itself.
- **draft-ietf-6lo-nd-gaao-12** (new-draft, score 0, ignored_after_review) [6lo]: [Generic Address Assignment Option for 6LoWPAN Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6lo-nd-gaao/) — This document specifies an extension to the IPv6 Neighbor Discovery
   in Low Power and Lossy Networks (LLNs), enabling a node to request to
   be assigned an address or a prefix from neighbor routers, without
   introducing a centralized infrastructure and without relying on
   multicast messages.  Such a mechanism makes it possible to
   algorithmically assign addresses and prefixes to nodes in a 6LoWPAN
   deployment.
- **draft-ietf-6lo-owc-08** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of IPv6 Packets over Short-Range Optical Wireless Communications](https://datatracker.ietf.org/doc/draft-ietf-6lo-owc/) — [IEEE802.15.7], "Short-Range Optical Wireless Communications" defines
   wireless communication using visible light.  It defines how data is
   transmitted, modulated, and organized in order to enable reliable and
   efficient communication in various environments.  The standard is
   designed to work alongside other wireless communication systems and
   supports both Line-of-Sight (LOS) and Non-Line-of-Sight (NLOS)
   communications.  However, ambient light interference from natural
   sunlight or artificial lighting sources can impact signal
   reliability.  To mitigate this, advanced modulation techniques,
   optical filtering, and adaptive power control can be employed.  This
   document describes how IPv6 is transmitted over short-range optical
   wireless communications (OWC) using IPv6 over Low-Power Wireless
   Personal Area Network (6LoWPAN) techniques.
- **draft-ietf-6lo-path-aware-semantic-addressing-16** (new-draft, score 0, ignored_after_review) [6lo]: [Path-Aware Semantic Addressing (PASA) for Low power and Lossy Networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-path-aware-semantic-addressing/) — This document specifies a topological addressing scheme, Path-Aware
   Semantic Addressing (PASA), that enables stateless IP packet
   forwarding.  The forwarding decision is based solely on the
   destination address structure.  This document focuses on carrying IP
   packets across an LLN (Low power and Lossy Network), in which the
   topology is quite static, the location of the nodes is fixed for long
   period of time, and the connection between the nodes is also rather
   stable.  This document specifies the PASA architecture, along with
   the PASA address allocation, forwarding mechanism, routing header
   format, and IPv6 interconnection support.
- **draft-ietf-6lo-rfc8163-bis-01** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of IPv6 over Multidrop Serial Bus/Token Passing (MS/TP) Networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-rfc8163-bis/) — Multidrop Serial Bus/Token Passing (MS/TP) is a medium access control
   method for the RS-485 physical layer and is used primarily in
   building automation networks.  This specification defines the frame
   format for transmission of IPv6 packets and the method of forming
   link-local and statelessly autoconfigured IPv6 addresses on MS/TP
   networks.  It obsoletes RFC 8163.
- **draft-ietf-6lo-schc-15dot4-14** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of SCHC-compressed packets over IEEE 802.15.4 networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-schc-15dot4/) — A framework called Static Context Header Compression and
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
- **draft-ietf-6man-ieee80211-dms-02** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 issues with 802.11 multicast reliability remain](https://datatracker.ietf.org/doc/draft-ietf-6man-ieee80211-dms/) — For the IPv6 protocol stack, while IEEE 802.11 wireless networks can
   on a first abstraction be considered functionally identical to wired
   IEEE 802 networks, there are issues regarding reliability and
   survivability of multicast traffic.  The existence of these issues
   has been known for some time.  This document is to state that they
   are still being experienced, and summarize some previous and new
   approaches.

   Additionally, this document serves to collect consensus in the IETF
   process to make both the IEEE and Wi-Fi Alliance aware of these
   issues and request they be included in consideration for future
   development.  802.11 Directed Multicast Service and Flexible
   Multicast Service are noted as existing protocol features that may
   warrant more consideration.  However, other solutions in that space
   may be more appropriate and are left to the expertise of the IEEE and
   Wi-Fi Alliance.
- **draft-ietf-anima-constrained-voucher-32** (new-draft, score 0, ignored_after_review) [anima]: [Constrained Bootstrapping Remote Secure Key Infrastructure (cBRSKI)](https://datatracker.ietf.org/doc/draft-ietf-anima-constrained-voucher/) — This document defines the Constrained Bootstrapping Remote Secure Key
   Infrastructure (cBRSKI) protocol, which provides a solution for
   secure zero-touch onboarding of resource-constrained (IoT) devices
   into the network of a domain owner.  This protocol is designed for
   constrained networks, which may have limited data throughput or may
   experience frequent packet loss. cBRSKI is a variant of the BRSKI
   protocol, which uses an artifact signed by the device manufacturer
   called the "voucher" which enables a new device and the owner's
   network to mutually authenticate.  While the BRSKI voucher data is
   encoded in JSON, cBRSKI uses a compact CBOR-encoded voucher.  The
   BRSKI voucher data definition is extended with new data types that
   allow for smaller voucher sizes.  The Enrollment over Secure
   Transport (EST) protocol, used in BRSKI, is replaced with EST-over-
   CoAPS; and HTTPS used in BRSKI is replaced with DTLS-secured CoAP
   (CoAPS).  This document Updates RFC 8995 and RFC 9148.
- **draft-ietf-asdf-instance-information-03** (new-draft, score 0, ignored_after_review) [asdf]: [Instance Information for SDF](https://datatracker.ietf.org/doc/draft-ietf-asdf-instance-information/) — This document specifies instance-related messages to be used in
   conjunction with the Semantic Definition Format (SDF) for Data and
   Interactions of Things (RFC 9880).  Split into four "archetypes", SDF
   messages are always governed by SDF models, strictly separating
   instance and class information. _Context_ information plays a crucial
   role both for lifecycle management and actual device interaction.


   // This revision refines the structure and terminology used with SDF
   // messages, and further improves the alignment with the non-
   // affordance draft and its sdfContext keyword.
- **draft-ietf-avtcore-rtp-avatar-03** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for Avatar Representation Format (ARF) Animation Stream](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-avatar/) — This memo outlines RTP payload formats for the animation stream
   format as defined in the ISO/IEC 23090-39 standard (MPEG-I Avatar
   Representation Format), in the following referred to as ARF.  ARF is
   composed of Avatar Animation Units (AAU) including an AAU header and
   zero or more AAU packets.  The RTP payload header format allows for
   packetization of an AAU unit in an RTP packet payload as well as
   fragmentation of an AAU into multiple RTP packets.
- **draft-ietf-avtcore-rtp-vdmc-05** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for V-DMC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-vdmc/) — This memo outlines RTP payload formats for the Video-based Dynamic
   Mesh Coding (V-DMC), which comprises several types of components,
   such as a basemesh, AC-based displacements, 2D representations of
   attributes, and an atlas.  This document focuses on describing the
   basemesh and displacement, while the RTP payload formats for the
   atlas and attributes are addressed in other documents.  The RTP
   payload header formats enable the packetization of a basemesh or
   displacement Network Abstraction Layer (NAL) unit in an RTP packet
   payload as well as fragmentation of a NAL unit into multiple RTP
   packets.
- **draft-ietf-bess-evpn-dpath-05** (new-draft, score 0, ignored_after_review) [bess]: [Domain Path (D-PATH) for Ethernet VPN (EVPN) Interconnect Networks](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-dpath/) — The BGP Domain PATH (D-PATH) attribute is defined for Inter-Subnet
   Forwarding (ISF) BGP Sub-Address Families that advertise IP prefixes
   or MAC addresses.  D-PATH already applies to EVPN Route Type 2 when
   used for ISF, to EVPN Route Type 5 (IP Prefix routes), and to IP-VPN
   routes.  When used along with those routes, it identifies the
   domain(s) through which the routes have passed and that information
   can be used by the receiver BGP speakers to detect routing loops or
   influence the BGP best path selection.  This document extends the use
   of D-PATH to EVPN Route Type 2 when not used for ISF, to EVPN Route
   Type 1 (Ethernet Auto-Discovery per-EVI) for EVPN VPWS, and to EVPN
   Route Type 3 (Inclusive Multicast Ethernet Tag routes).
- **draft-ietf-bess-evpn-ip-aliasing-05** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Support for L3 Fast Convergence and Aliasing/Backup Path](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-ip-aliasing/) — This document proposes an EVPN extension to allow several of its
   multi-homing functions, fast convergence, and aliasing/backup path,
   to be used in conjunction with inter-subnet forwarding.  The
   extension is limited to All-Active and Single-Active redundancy
   modes.
- **draft-ietf-bess-evpn-l3mh-proto-02** (new-draft, score 0, ignored_after_review) [bess]: [EVPN multi-homing support for L3 services](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/) — This document describes the use of EVPN Ethernet Segment Link
   Aggregation Group (ES-LAG) technology to provide multi-homing
   redundancy for Layer 3 services.  The solution synchronizes ARP/ND,
   multicast state, and IGP routes between redundant PEs without
   requiring Layer 2 constructs or proprietary Inter-Chassis
   Communication protocols.
- **draft-ietf-bess-evpn-vpws-gateway-02** (new-draft, score 0, ignored_after_review) [bess]: [Ethernet VPN Virtual Private Wire Services Gateway Solution](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-vpws-gateway/) — Ethernet Virtual Private Network Virtual Private Wire Services (EVPN
   VPWS) need to be deployed in high scale multi-domain networks, where
   each domain can use a different transport technology, such as MPLS,
   VXLAN or Segment Routing with MPLS or IPv6 Segment Identifiers
   (SIDs).  While transport interworking solutions on border routers
   spare the border routers from having to process service routes, they
   do not always meet the multi-homing, redundancy, and operational
   requirements, or provide the isolation that each domain requires.
   This document analyzes the scenarios in which an interconnect
   solution for EVPN VPWS using EVPN Domain Gateways is needed, and adds
   the required extensions to support it.
- **draft-ietf-bpm-alt-mark-deployment-00** (new-draft, score 0, ignored_after_review) [bpm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-bpm-containerized-infra-00** (new-draft, score 0, ignored_after_review) [bpm]: [Considerations for Benchmarking Network Performance in Containerized Infrastructures](https://datatracker.ietf.org/doc/draft-ietf-bpm-containerized-infra/) — Recently, the Benchmarking and Performance Measurements Working Group
   extended the laboratory characterization from physical network
   functions (PNFs) to virtual network functions (VNFs).  With the
   ongoing shift in network function implementation from virtual
   machine-based to container-based approaches, system configurations
   and deployment scenarios for benchmarking will be partially
   influenced by how resource allocation and network technologies are
   specified for containerized network functions.  This draft outlines
   additional considerations for benchmarking network performance when
   network functions are containerized and executed on general-purpose
   hardware.
- **draft-ietf-bpm-on-path-telemetry-yang-00** (new-draft, score 0, ignored_after_review) [bpm]: [On-Path Telemetry YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-bpm-on-path-telemetry-yang/) — This document defines two YANG data models for monitoring On-Path
   network performance information to be published in YANG
   notifications.  The Alternate-Marking Method and In-situ Operations,
   Administration, and Maintenance (IOAM) are the On-Path hybrid
   measurement methods considered in this document.
- **draft-ietf-bpm-savnet-sav-benchmarking-00** (new-draft, score 0, ignored_after_review) [bpm]: [Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-bpm-savnet-sav-benchmarking/) — This document defines methodologies for benchmarking the performance
   of intra-domain and inter-domain source address validation (SAV)
   mechanisms.  SAV mechanisms are utilized to generate SAV rules that
   prevent source address spoofing.  The methodology treats a SAV device
   as a black box and is therefore agnostic to the specific SAV
   mechanism and implementation used by the device.  This document
   defines test setups, performance indicators, and test cases for SAV
   accuracy, control-plane and data-plane performance, and resource
   utilization.
- **draft-ietf-bpm-stamp-ber-01** (new-draft, score 0, ignored_after_review) [bpm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Residual Bit Error Rate Measurement](https://datatracker.ietf.org/doc/draft-ietf-bpm-stamp-ber/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, and its optional extensions, specified in RFC 8972, support
   active measurement.  Networks may experience transmission bit errors
   due to various factors, including poor fiber quality.  Even with
   efficient FEC and CRC mechanisms, some bit errors may escape
   detection and correction; these are referred to as residual bit
   errors.  This document further augments the STAMP extensions
   specified in RFC 8972 to enable the measurement of the residual bit
   error rate within the "Extra Padding" TLV of STAMP-Test packets.
- **draft-ietf-bpm-stamp-mpls-hdr-00** (new-draft, score 0, ignored_after_review) [bpm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet MPLS Network Action Headers](https://datatracker.ietf.org/doc/draft-ietf-bpm-stamp-mpls-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect MPLS Network Action Sub-Stacks and
   Post-Stack MPLS Headers for HBH and E2E active measurements, for
   example, using the IOAM data fields.
- **draft-ietf-calext-icalendar-jscalendar-extensions-09** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545, RFC 7986, and RFC 9073.
- **draft-ietf-calext-jscalendar-icalendar-29** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-calext-rfc9555bis-02** (new-draft, score 0, ignored_after_review) [calext]: [JSContact: Converting from and to vCard](https://datatracker.ietf.org/doc/draft-ietf-calext-rfc9555bis/) — This document defines how to convert contact information between the
   JSContact and vCard data formats.  It defines conversion rules for
   every JSContact and vCard element registered at IANA at the time of
   publication.  It also defines new JSContact properties as well as
   vCard properties and parameters, to support converting arbitrary or
   unknown JSContact and vCard elements.  This document obsoletes RFC
   9555 and updates its definitions for JSContact versions "2.0" and
   "3.0".
- **draft-ietf-cbor-edn-literals-29** (new-draft, score 0, ignored_after_review) [cbor]: [Concise Diagnostic Notation (CDN)](https://datatracker.ietf.org/doc/draft-ietf-cbor-edn-literals/) — This document formalizes and consolidates the definition of the
   Concise Diagnostic Notation (CDN) of the Concise Binary Object
   Representation (CBOR), addressing implementer experience.

   Replacing CDN's previous informal descriptions, it updates RFC 8949,
   obsoleting its Section 8, and RFC 8610, obsoleting its Appendix G.

   It also specifies registry-based extension points and uses them to
   support text representations such as of epoch-based dates/times and
   of IP addresses and prefixes.


   // (This cref will be removed by the RFC editor:) This revision -29
   // attempts to implement various change requests not covered in -28
   // that have been discussed in the 2026-08-19 and 2026-09-30 WG
   // interim meetings, but does not attempt to reflect the outcome of
   // those discussions.  The text also does not have WG input yet on
   // any renaming decisions (CDN name, b1/t1 name).
- **draft-ietf-ccamp-fgotn-yang-03** (new-draft, score 0, ignored_after_review) [ccamp]: [YANG Data Models for fine grain Optical Transport Network](https://datatracker.ietf.org/doc/draft-ietf-ccamp-fgotn-yang/) — Fine grain Optical Transport Network (fgOTN) is a data plane
   technology, specified in ITU-T Recommendation G.709/Y.1331 (2020)
   Amd. 3, which complements existing OTN by providing bandwidth
   efficient support for sub-1Gbit/s services.

   This document defines YANG data models to describe the topology and
   tunnel information of an fgOTN network.
- **draft-ietf-ccwg-rfc8298bis-screamv2-03** (new-draft, score 0, ignored_after_review) [ccwg]: [Self-Clocked Rate Adaptation for Multimedia](https://datatracker.ietf.org/doc/draft-ietf-ccwg-rfc8298bis-screamv2/) — This memo describes Self-Clocked Rate Adaptation for Multimedia
   version 2 (SCReAMv2), an update to SCReAM congestion control for
   media streams such as RTP [RFC3550].  SCReAMv2 includes several
   algorithm simplifications and adds support for L4S.  The algorithm
   supports handling of multiple media streams, typical use cases are
   streaming for remote control, AR and 3D VR goggles.  This
   specification obsoletes RFC 8298.
- **draft-ietf-cdni-metadata-expression-language-03** (new-draft, score 0, ignored_after_review) [cdni]: [CDNI Metadata Expression Language](https://datatracker.ietf.org/doc/draft-ietf-cdni-metadata-expression-language/) — This document specifies the syntax and provides usage examples for an
   expression language to be used within Content Delivery Network
   Interconnection (CDNI) Metadata Interface (MI) objects.  The purpose
   of this expression language is to enable metadata to be applied
   conditionally (based on aspects of an HTTP request), and to enable
   Hypertext Transfer Protocol (HTTP) responses to be generated or
   altered dynamically.
- **draft-ietf-cdni-protected-secrets-metadata-08** (new-draft, score 0, ignored_after_review) [cdni]: [Content Delivery Network Interconnection (CDNI) Protected Secrets Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-protected-secrets-metadata/) — This document defines Content Delivery Network Interconnection (CDNI)
   Metadata Interface and Footprint and Capabilities Interface objects
   that carry secrets, such as encryption keys, either embedded and
   encrypted to the recipient's certificate or referenced in an external
   store.
- **draft-ietf-core-coap-bp-05** (new-draft, score 0, ignored_after_review) [core]: [Constrained Application Protocol (CoAP) over Bundle Protocol (BP)](https://datatracker.ietf.org/doc/draft-ietf-core-coap-bp/) — The Bundle Protocol (BP) was designed to enable end-to-end
   communication in challenged networks.  The Constrained Application
   Protocol (CoAP), which was designed for constrained-node networks,
   may be a suitable application-layer protocol for the scenarios where
   BP is used.  This document specifies how CoAP is carried over BP.
- **draft-ietf-core-coap-pubsub-22** (new-draft, score 0, ignored_after_review) [core]: [A publish-subscribe architecture for the Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/draft-ietf-core-coap-pubsub/) — This document describes a publish-subscribe architecture for the
   Constrained Application Protocol (CoAP), extending the capabilities
   of CoAP communications for supporting endpoints with long breaks in
   connectivity and/or up-time.  CoAP clients publish on and subscribe
   to a topic via a corresponding topic resource at a CoAP server acting
   as broker.
- **draft-ietf-core-multicast-notifications-proxy-03** (new-draft, score 0, ignored_after_review) [core]: [Using Proxies for Observe Notifications as CoAP Multicast Responses](https://datatracker.ietf.org/doc/draft-ietf-core-multicast-notifications-proxy/) — The Constrained Application Protocol (CoAP) allows clients to
   "observe" resources at a server and to receive notifications as
   unicast responses upon changes of the resource state.  Instead of
   sending a distinct unicast notification to each different client, a
   server can alternatively send a single notification as a response
   message over multicast, to all the clients observing the same target
   resource.  When doing so, the security protocol Group Object Security
   for Constrained RESTful Environments (Group OSCORE) can be used to
   protect multicast notifications end-to-end between the server and the
   observer clients.  This document describes how multicast
   notifications can be used in network setups that leverage a proxy,
   e.g., in order to accommodate clients that are not able to directly
   listen to multicast traffic.
- **draft-ietf-core-observe-multicast-notifications-17** (new-draft, score 0, ignored_after_review) [core]: [Observe Notifications as CoAP Multicast Responses](https://datatracker.ietf.org/doc/draft-ietf-core-observe-multicast-notifications/) — The Constrained Application Protocol (CoAP) allows clients to
   "observe" resources at a server and to receive notifications as
   unicast responses upon changes of the resource state.  In some use
   cases, such as those based on publish-subscribe, it would be
   convenient for the server to send a single notification addressed to
   all the clients observing the same target resource.  This document
   updates RFC7252 and RFC7641, and it defines how a server sends
   observe notifications as response messages over multicast,
   synchronizing all the observers of the same resource on the same
   shared Token value.  Besides, this document defines how the security
   protocol Group Object Security for Constrained RESTful Environments
   (Group OSCORE) can be used to protect multicast notifications end-to-
   end between the server and the observer clients.
- **draft-ietf-core-oscore-capable-proxies-08** (new-draft, score 0, ignored_after_review) [core]: [OSCORE-capable Proxies](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-capable-proxies/) — When using the Constrained Application Protocol (CoAP), messages
   exchanged between two endpoints can be protected end-to-end at the
   application layer by means of Object Security for Constrained RESTful
   Environments (OSCORE), also in the presence of intermediaries such as
   proxies.  This document defines how to use OSCORE for protecting CoAP
   messages also between an origin application endpoint and an
   intermediary, or between two intermediaries.  Also, it defines rules
   to escalate the protection of a CoAP option, in order to encrypt and
   integrity-protect it whenever possible.  Finally, it defines how to
   secure a CoAP message by applying multiple, nested OSCORE
   protections, e.g., both end-to-end between origin application
   endpoints; and between an application endpoint and an intermediary or
   between two intermediaries.  Therefore, this document updates RFC
   8613.  Furthermore, this document updates RFC 8768, by explicitly
   defining the processing with OSCORE for the CoAP Hop-Limit Option.
   The approach defined in this document can be seamlessly employed also
   with Group OSCORE, for protecting CoAP messages when group
   communication is used in the presence of intermediaries.
- **draft-ietf-core-oscore-key-update-15** (new-draft, score 0, ignored_after_review) [core]: [Key Update for OSCORE (KUDOS)](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-key-update/) — Communications with the Constrained Application Protocol (CoAP) can
   be protected end-to-end at the application-layer by using the
   security protocol Object Security for Constrained RESTful
   Environments (OSCORE).  Under some circumstances, two CoAP endpoints
   need to update their OSCORE keying material before communications can
   securely continue, e.g., due to approaching key usage limits.  This
   document defines Key Update for OSCORE (KUDOS), a lightweight key
   update procedure that two CoAP endpoints can use to update their
   OSCORE keying material by establishing a new OSCORE Security Context.
   Accordingly, this document updates the use of the OSCORE flag bits in
   the CoAP OSCORE Option as well as the protection of CoAP response
   messages with OSCORE.  Also, it deprecates the key update procedure
   specified in Appendix B.2 of RFC 8613.  Therefore, this document
   updates RFC 8613.
- **draft-ietf-core-transport-indication-11** (new-draft, score 0, ignored_after_review) [core]: [CoAP Transport Indication](https://datatracker.ietf.org/doc/draft-ietf-core-transport-indication/) — The Constrained Application Protocol (CoAP, [RFC7252]) is available
   over different transports (UDP, DTLS, TCP, TLS, WebSockets), but
   lacks a way to unify the addresses of these transports.  This
   document provides terminology and provisions based on Web Linking
   [RFC8288] and Service Bindings (SVCB, [RFC9460]) to express
   alternative transports available to a device, and to optimize
   exchanges using these.
- **draft-ietf-detnet-dataplane-taxonomy-07** (new-draft, score 0, ignored_after_review) [detnet]: [Dataplane Enhancement Taxonomy](https://datatracker.ietf.org/doc/draft-ietf-detnet-dataplane-taxonomy/) — This draft is to facilitate the understanding of the data plane
   enhancement solutions, which are suggested currently or can be
   suggested in the future, for deterministic networking.  This draft
   provides criteria for classifying data plane solutions.  Examples of
   each category are listed, along with reasons where necessary.
   Strengths and limitations of the categories are described.
   Suitability of the solutions for various services of deterministic
   networking are also mentioned.  Reference topologies for evaluation
   of the solutions are given as well.
- **draft-ietf-detnet-tcqf-02** (new-draft, score 0, ignored_after_review) [detnet]: [Deterministic Networking (DetNet) Data Plane - Tagged Cyclic Queuing and Forwarding (TCQF) for bounded latency with low jitter in large scale DetNets](https://datatracker.ietf.org/doc/draft-ietf-detnet-tcqf/) — This memo specifies a forwarding method for bounded latency and
   bounded jitter for Deterministic Networks and is a variant of the
   IEEE TSN Cyclic Queuing and Forwarding (CQF) method.  Tagged CQF
   (TCQF) supports more than two cycles and indicates the cycle number
   in an existing or new packet header field, called the tag.  The tag
   replaces the cycle mapping of CQF, which is based purely on the
   synchronized reception clock.

   This memo standardizes TCQF as a mechanism independent of the tagging
   method used.  It also specifies tagging via (1) the existing MPLS
   packet Traffic Class (TC) field for MPLS packets, (2) the IP/IPv6
   DSCP field for IP/IPv6 packets, and (3) a new TCQF Option header for
   IPv6 packets.

   Target benefits of TCQF include low end-to-end jitter, ease of high-
   speed hardware implementation, the optional ability to support a
   large number of flows in large networks through DiffServ-style
   aggregation by applying TCQF to the DetNet aggregate instead of each
   DetNet flow individually, and support of wide-area DetNet networks
   with arbitrary link latencies and latency variations as well as low
   accuracy clock synchronization.
- **draft-ietf-diem-requirements-05** (new-draft, score 0, ignored_after_review) [diem]: [Digital Emblems - Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-diem-requirements/) — Digital emblems allow an issuer to signal that an asset should be
   protected or treated in a specific way, using some normative
   framework.  This document lists the requirements and use cases that
   an architecture for digital emblems must accommodate.
- **draft-ietf-dkim-dkim2-dns-03** (new-draft, score 0, ignored_after_review) [dkim]: [Domain Name Specification for DKIM1 and DKIM2](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-dns/) — DomainKeys Identified Mail (DKIM) permits the owner of a signing
   domain to document that they have handled an email message by
   associating their domain with the message.  One part of this involves
   publishing a public key to a Domain Name System (DNS) record
   associated with the domain.  Signing with the associated private key
   establishes their connection to the message.  This document describes
   how to find the relevant DNS record and how information is recorded
   within it.

   This document updates RFC 6376, which describes DKIM, by clarifying
   the RSA public key format and by deprecating key record features that
   have not turned out to be useful.  It also describes which parts of
   the key record are relevant to DomainKeys Identified Mail v2 (DKIM2)
   and describes a new Domain Policy Record for DKIM2 that can hold
   domain-wide settings.
- **draft-ietf-dmm-mup-architecture-03** (new-draft, score 0, ignored_after_review) [dmm]: [Mobile User Plane Architecture for Distributed Mobility Management](https://datatracker.ietf.org/doc/draft-ietf-dmm-mup-architecture/) — This document defines the Mobile User Plane (MUP) architecture for
   Distributed Mobility Management (DMM).  MUP meets the DMM
   requirements in [RFC7333] in a routing fashion.  MUP provides a
   normative mechanism that makes it possible to avoid traversing a
   single user plane anchor far from the optimal route, by turning
   mobile user plane session information into routing information and
   integrating the user plane into the dataplane.

   MUP is designed as a pluggable user plane part of existing mobile
   service architectures, with auto-discovery.  Although the
   architecture is dataplane-independent, this document describes SRv6
   over IPv6 (SRv6 MUP), whose programmability and large address space
   suit scalable mobile services.

   This mechanism is specified in terms of the semantics of MUP segments
   and of the routing information, how that information is distributed
   among MUP PEs and the MUP Controller and resolved by a MUP PE, and
   the behaviour required of them.  It does not define the wire encoding
   of any routing protocol; such an encoding may be defined in other
   documents.
- **draft-ietf-dmm-srv6-gtp6e-reduced-01** (new-draft, score 0, ignored_after_review) [dmm]: [SRH Reduction for SRv6 End.M.GTP6.E Behavior](https://datatracker.ietf.org/doc/draft-ietf-dmm-srv6-gtp6e-reduced/) — Segment Routing over IPv6 for the Mobile User Plane specifies
   interworking between SRv6 networks and GTP-U networks including
   required behaviors.  This document specifies a new behavior named
   End.M.GTP6.E.Red which makes the End.M.GTP6.E behavior more amenable
   to hardware implementation by encoding the information required for
   GTP-U encapsulation in a single SRv6 SID, together with a locally
   maintained mapping.
- **draft-ietf-dnssd-tsr-04** (new-draft, score 0, ignored_after_review) [dnssd]: [Multicast DNS conflict resolution using the Time Since Received (TSR) EDNS option](https://datatracker.ietf.org/doc/draft-ietf-dnssd-tsr/) — This document specifies a new conflict resolution mechanism for
   Multicast DNS (mDNS), for use in cases where the advertisement is
   being proxied, rather than advertised directly, e.g. when using a
   combined DNS-SD advertising proxy and SRP registrar.  A new EDNS
   option Time Since Received (TSR) is defined that communicates the
   time at which the set of resource records on a particular DNS owner
   name was most recently updated.
- **draft-ietf-dult-accessory-protocol-01** (new-draft, score 0, ignored_after_review) [dult]: [Detecting Unwanted Location Trackers Accessory Protocol](https://datatracker.ietf.org/doc/draft-ietf-dult-accessory-protocol/) — This document lists a set of best practices and protocols for
   accessory manufacturers whose products have built-in location-
   tracking capabilities.  By following these requirements and
   recommendations, a location-tracking accessory will be compatible
   with unwanted tracking detection and alerts on mobile platforms.
   This is an important capability for improving the privacy and safety
   of individuals in the circumstance that those accessories are used to
   track their location without their knowledge or consent.
- **draft-ietf-green-framework-03** (new-draft, score 0, ignored_after_review) [green]: [Framework for Energy Efficiency Management](https://datatracker.ietf.org/doc/draft-ietf-green-framework/) — Recognizing the urgent need for energy efficiency, this document
   specifies a management framework focused on networks, devices and
   device components within, or connected to, interconnected systems.
   The framework aims to enable energy usage optimization, based on the
   network condition while achieving the network's functional and
   performance requirements (e.g., improving overall network
   utilization) and also ensure interoperability across diverse systems.
   Leveraging data from existing use cases, it delivers actionable
   metrics to support effective energy management and informed decision-
   making.  Furthermore, the framework defines mechanisms for
   representing and organizing timestamped telemetry data using YANG
   data models and metadata, enabling transparent and reliable
   monitoring.  This structured approach facilitates improved energy
   efficiency through consistent energy management practices.
- **draft-ietf-green-terminology-03** (new-draft, score 0, ignored_after_review) [green]: [Terminology for Energy Efficiency Network Management](https://datatracker.ietf.org/doc/draft-ietf-green-terminology/) — Energy-efficient network management is primarily meant to enhance
   conventional network management with energy-related management
   capabilities that optimize overall network energy consumption.  To
   that aim, specific features and capabilities are required to control
   (and thus optimize) the energy use of involved network elements and
   their components.

   This document defines a set of key terms used within the IETF when
   discussing energy efficiency in network management.  Such reference
   document helps framing discussion and agreeing upon a set of main
   concepts in this area.
- **draft-ietf-grow-bmp-tlv-22** (new-draft, score 0, ignored_after_review) [grow]: [BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/) — Most of the BGP Monitoring Protocol (BMP) message types make
   provision for data in Type, Length, Value (TLV) format.  However,
   Route Monitoring messages (which provide a snapshot of the monitored
   Routing Information Base) Stats Reports (which supply periodical
   counters) and Peer Down messages (which indicate that a peering
   session was terminated) do not.  Supporting (optional) data in TLV
   format across all BMP message types provides consistent and
   extensible structures that would be useful in the various use cases
   where conveying additional data to a monitoring station is required.
   This document updates RFC 7854 [RFC7854] to support TLV data in all
   message types and defines some essential TLVs.

   Additionally, this document introduces support for enterprise-
   specific TLVs in the BGP Monitoring Protocol by defining an
   Enterprise Bit (E-bit) that allows usage of per-vendor Type values.
- **draft-ietf-grow-rpsl-registry-scoped-members-01** (new-draft, score 0, ignored_after_review) [grow]: [Registry scoped members for RPSL set objects](https://datatracker.ietf.org/doc/draft-ietf-grow-rpsl-registry-scoped-members/) — This document updates RFC2622 and RFC4012 by specifying src-members,
   a new attribute on as-set and route-set objects in the Routing Policy
   Specification Language (RPSL).  This attribute allows a specific
   registry to be defined for each member in a set, avoiding problematic
   ambiguity when resolving set members.  A new validation rule allows
   gradual upgrades and backwards compatibility.
- **draft-ietf-happy-happyeyeballs-v3-05** (new-draft, score 0, ignored_after_review) [happy]: [Happy Eyeballs Version 3: Better Connectivity Using Concurrency](https://datatracker.ietf.org/doc/draft-ietf-happy-happyeyeballs-v3/) — Many communication protocols operating over the modern Internet use
   hostnames.  These often resolve to multiple IP addresses, each of
   which may have different performance and connectivity
   characteristics.  Since specific addresses or address families (IPv4
   or IPv6) may be blocked, broken, or sub-optimal on a network, clients
   that attempt multiple connections in parallel have a chance of
   establishing a connection more quickly.  This document defines the
   algorithm for "Happy Eyeballs", a technique for reducing user-visible
   delays on dual-stack hosts.  This document updates the algorithm in
   RFC 8305.
- **draft-ietf-hpke-hpke-06** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document specifies a scheme for hybrid public key encryption
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
- **draft-ietf-ianabis-early-registries-03** (new-draft, score 0, ignored_after_review) [ianabis]: [Early IANA Registry Creation](https://datatracker.ietf.org/doc/draft-ietf-ianabis-early-registries/) — This memo describes the requirements for establishing an IANA
   registry before the IETF Stream document that creates the registry is
   approved for publication as an RFC.  This process can be used when an
   IETF working group needs to coordinate allocations among multiple
   documents or with an organization outside the IETF.
- **draft-ietf-ianabis-rfc8126bis-05** (new-draft, score 0, ignored_after_review) [ianabis]: [Guidelines for Writing an IANA Considerations Section in RFCs](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc8126bis/) — Many protocols make use of points of extensibility that use constants
   to identify various protocol parameters.  To ensure that the values
   in these fields do not have conflicting uses and to promote
   interoperability, their allocations are often coordinated by a
   central record keeper.  For IETF protocols, that role is filled by
   the Internet Assigned Numbers Authority (IANA).

   To make assignments in a given registry prudently, guidance
   describing the conditions under which new values should be assigned,
   as well as when and how modifications to existing values can be made,
   is needed.  This document defines a framework for the documentation
   of these guidelines by specification authors, in order to assure that
   the provided guidance for the IANA Considerations is clear and
   addresses the various issues that are likely in the operation of a
   registry.

   This is the fourth edition of this document; it obsoletes RFC 8126.
- **draft-ietf-idr-bgp-ct-srv6-08** (new-draft, score 0, ignored_after_review) [idr]: [BGP CT - Adaptation to SRv6 and Other dataplanes](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ct-srv6/) — This document specifies how the mechanisms for "Intent Driven Service
   Mapping" defined in [BGP-CT] are applied to SRv6 dataplane.  The
   extensions needed for SRv6 dataplane operations are specified.  Base
   procedures of BGP CT are followed unaltered.

   Illustration of how BGP CT procedures work in SRv6 dataplane is
   provided in this document.
- **draft-ietf-idr-bgp4-rfc4271bis-05** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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
- **draft-ietf-idr-fsv2-bitwise-ip-filters-00** (new-draft, score 0, ignored_after_review) [idr]: [Bitwise IP Filters for BGP FlowSpec](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-bitwise-ip-filters/) — This document introduces the bitwise match filter component for
   source and destination IPv4/IPv6 address fields.  These components
   enhance the BGP Flow Specification framework and provide a solution
   for dynamic symmetric traffic load-balancing.
- **draft-ietf-idr-fsv2-content-filter-00** (new-draft, score 0, ignored_after_review) [idr]: [Packet Content Filter for BGP FlowSpec](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-content-filter/) — The BGP FlowSpec mechanism enables the distribution of traffic filter
   policies (traffic filters and actions) via BGP, facilitating DDoS
   traffic filtering.  The IP filter components defined for FSv1 and the
   FSv2 IP Basic Filter Families primarily match fields in the IP and
   transport-layer headers, which may not adequately address volumetric
   DDoS attack traffic characterized by fixed patterns within the packet
   content.  This document defines a Packet Content Filter Component for
   FSv1 and FSv2.  The match is encoded using OType, Offset, Content
   Length, Content, and Mask fields in the FlowSpec NLRI.  The FSv1
   encoding additionally carries a PType field.  This new component aims
   to leverage capable network devices to support controlled traffic
   handling, traffic optimization, and mitigation of simple volumetric
   DDoS attacks, reducing the overall processing cost of carrier
   networks.
- **draft-ietf-idr-fsv2-dip-community-filter-00** (new-draft, score 0, ignored_after_review) [idr]: [Destination-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-dip-community-filter/) — BGP Flow Specification Version 2 (FSv2) propagates both traffic Flow
   Specifications and Traffic Filtering Actions using an extensible TLV-
   based filter family architecture.  This document specifies a new FSv2
   component type under the Routing Filter Family to support community-
   level filtering.  The match condition evaluates the BGP Community
   attribute associated with the destination IP address encoded in the
   Flowspec NLRI.  This mechanism is intended for deployment within a
   single administrative domain.
- **draft-ietf-idr-fsv2-dip-origin-as-filter-00** (new-draft, score 0, ignored_after_review) [idr]: [Destination-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-dip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the destination IP address.  This extension is
   particularly useful in mitigating Distributed Denial of Service
   (DDoS) attacks or optimizing traffic redirection where the target IP
   addresses are numerous or rapidly changing, but belong to a specific
   destination Origin AS.
- **draft-ietf-idr-fsv2-ip-basic-10** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 - for Basic IP](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/) — BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
   8956, and RFC 9117, describes the distribution of traffic filter
   policy (traffic filters and actions) distributed via BGP.  During the
   deployment of BGP FSv1 a number of issues were detected, so version 2
   of the BGP flow specification (FSv2) protocol addresses these issues.
   In order to provide a clear demarcation between FSv1 and FSv2, a
   different NLRI encapsulates FSv2.

   The IDR WG requires two implementation.  Early feedback on
   implementations of FSv2 indicate that FSv2 has a correct design
   direction, but that breaking FSv2 into a progression of documents
   would aid deployment of the draft (basic and adding user ordered
   actions).  This document specifies the basic FSv2 NLRI with user
   ordering of filters added to FSv1 IP Filters and FSv2 actions.
- **draft-ietf-idr-fsv2-quic-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification for QUIC](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-quic/) — A BGP Flow Specification is an n-tuple consisting of several
   matching criteria that can be applied to IP traffic. This document
   defines how to perform Flow Specification traffic diversion based on
   the characteristics of QUIC packets.
- **draft-ietf-idr-fsv2-sip-community-filter-00** (new-draft, score 0, ignored_after_review) [idr]: [Source-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-sip-community-filter/) — BGP Flow Specification Version 2 (FSv2) propagates traffic Flow
   Specifications and Traffic Filtering Actions using an extensible TLV-
   based filter family architecture.  This document specifies a new FSv2
   component type under the Routing Filter Family to support community-
   level filtering within a single administrative domain.  The match
   condition filters traffic based on the BGP Community attributes
   associated with the route matching the packet's source IP address.
- **draft-ietf-idr-fsv2-sip-origin-as-filter-00** (new-draft, score 0, ignored_after_review) [idr]: [Source-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-sip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the source IP address.  This extension is particularly
   useful in mitigating Distributed Denial of Service (DDoS) attacks
   where the source IP addresses are dynamic or numerous but belong to a
   specific source AS.
- **draft-ietf-idr-node-target-ext-comm-04** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extended Community for Identifying the Target Nodes](https://datatracker.ietf.org/doc/draft-ietf-idr-node-target-ext-comm/) — BGP has been used to distribute different types of routing and policy
   information.  In some cases, the information distributed may be only
   intended for one or a particular group of BGP nodes in the network.
   Currently BGP does not have a generic mechanism to designate the
   target nodes of the routing information.  This document defines a new
   type of BGP Extended Community called "Node Target" for this purpose.
- **draft-ietf-idr-rt-derived-community-13** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route Target derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route Target derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-idr-rtc-hierarchical-rr-07** (new-draft, score 0, ignored_after_review) [idr]: [RT-Constrain Optimization in Hierarchical Route Reflection Scenarios](https://datatracker.ietf.org/doc/draft-ietf-idr-rtc-hierarchical-rr/) — The Route Target (RT) Constrain mechanism specified in RFC 4684 is
   used to build a route distribution graph in order to restrict the
   propagation of Virtual Private Network (VPN) routes.  In network
   scenarios where hierarchical route reflection (RR) is used, the
   existing RT-Constrain mechanism cannot guarantee a correct route
   distribution graph.  This document describes the problem scenario and
   proposes solutions to address the RT-Constrain issue in hierarchical
   RR scenarios.
- **draft-ietf-idr-ts-flowspec-srv6-policy-20** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  It defines two modes of
   operation: transport steering into an SR Policy ("Mode 1"), in SR-
   MPLS and SRv6 networks, using BGP Extended Communities; and, in SRv6
   networks, transport steering combined with an egress service action
   at the egress node ("Mode 2"), signaled with the BGP Prefix-SID
   Attribute.
- **draft-ietf-intarea-ipv6-resolved-gateway-01** (new-draft, score 0, ignored_after_review) [intarea]: [IPv6-Resolved IPv4 Gateway](https://datatracker.ietf.org/doc/draft-ietf-intarea-ipv6-resolved-gateway/) — This document specifies host behavior enabling IPv4 communication for
   dual-stack hosts on IPv6-only segments, without IPv4 subnets, ARP,
   tunneling, or translation.  A host is provisioned by ordinary DHCPv4
   or by static configuration.  Where its IPv4 default gateway is a
   reserved sentinel address, the host resolves the next-hop link-layer
   address from the IPv6 neighbor cache rather than by ARP.  IPv4
   packets are forwarded natively, end to end.  The mechanism is
   incrementally deployable alongside unmodified hosts; no flag day or
   mandatory switch-over point is needed.  This document requests the
   allocation of one IPv4 address from 192.0.0.0/24 in the IANA IPv4
   Special-Purpose Address Registry.
- **draft-ietf-intarea-multicast-application-port-09** (new-draft, score 0, ignored_after_review) [intarea]: [The Multicast Application Port](https://datatracker.ietf.org/doc/draft-ietf-intarea-multicast-application-port/) — This document discusses the drawbacks of the current practice of
   assigning a UDP port to each multicast application.  Such assignments
   are redundant because the multicast group address already uniquely
   identifies the data.  This document assigns a UDP port specifically
   for use with multicast applications and lists requirements for using
   this port.  This approach provides immediate compatibility with
   existing protocol stacks, and this document also defines host
   enhancements that help safeguard the ongoing cooperative use of this
   port by multicast applications.
- **draft-ietf-iotops-iot-dns-guidelines-06** (new-draft, score 0, ignored_after_review) [iotops]: [IoT DNS Security and Privacy Guidelines](https://datatracker.ietf.org/doc/draft-ietf-iotops-iot-dns-guidelines/) — This document outlines guidance for Internet of Things (IoT)
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
- **draft-ietf-iotops-mud-acceptable-urls-03** (new-draft, score 0, ignored_after_review) [iotops]: [Authorized update to MUD URLs](https://datatracker.ietf.org/doc/draft-ietf-iotops-mud-acceptable-urls/) — This document provides a way for an RFC8520 Manufacturer Usage
   Description (MUD) definitions to declare what are acceptable
   replacement MUD URLs for a device.

   RFCEDITOR-please-remove: this document is being worked on at:
   https://github.com/mcr/iot-mud-acceptable-urls
- **draft-ietf-ippm-stamp-cos-ecn-02** (new-draft, score 0, ignored_after_review) [ippm]: [Update of the Simple Two-way Active Measurement Protocol Class-of-Service Extension - ECN](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-cos-ecn/) — The Simple Two-Way Active Measurement Protocol (STAMP) enables one-
   way and round-trip measurement of network metrics between IP hosts,
   and has a facility for defining optional extensions.  This document
   updates the definition of the Class of Service TLV (originally
   defined in RFC 8972) to enable the measurement of manipulation of the
   value of the Explicit Congestion Notification (ECN) field of the IP
   header by middleboxes between two STAMP hosts, and to enable
   discovery and measurement of paths that provide differential
   treatment of packets depending on the value of their ECN field.
- **draft-ietf-ipsecme-child-pfs-info-01** (new-draft, score 0, ignored_after_review) [ipsecme]: [IKEv2 Support for Child SA PFS Policy Information](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-child-pfs-info/) — This document defines an extension for the Internet Key Exchange
   Protocol Version 2 (IKEv2) to support negotiation at the time of
   initial Child Security Association (SA) establishing of Key Exchange
   (KE) method that could be used in subsequent rekeys of this SA.
- **draft-ietf-ipsecme-encrypted-esp-ping-05** (new-draft, score 0, ignored_after_review) [ipsecme]: [ESP Echo Protocol](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-encrypted-esp-ping/) — This document defines the ESP Echo Protocol, an extension to the ESP
   AGGFRAG protocol [RFC9347] that provides an Echo Request and Echo
   Reply mechanism for IP Security (IPsec) link diagnostics.  It enables
   endpoints to assess end-to-end path reachability, and it defines
   probe packets that can be used for path Maximum Transmission Unit
   (MTU) discovery, using Encapsulating Security Payload (ESP) packets.

   The protocol supports two modes of operation: an encrypted mode used
   over established IPsec Security Associations (SAs), with an option to
   specify a preferred reply path when multiple SAs exist between the
   peers, and an unencrypted mode used outside the context of a
   negotiated ESP SA.  In addition to bidirectional echo probing, the
   protocol supports sending one-way ESP packets without eliciting a
   reply, primarily for keepalives, NAT and firewall pinhole
   maintenance, and unidirectional link diagnostics.

   A peer can announce support for ESP Echo using a new IKEv2 Status
   Notification ESP_ECHO_SUPPORTED.
- **draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt-09** (new-draft, score 0, ignored_after_review) [ipsecme]: [Optimized Rekeys in the Internet Key Exchange Protocol Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt/) — This document describes a method for reducing the size of the
   Internet Key Exchange version 2 (IKEv2) CREATE_CHILD_SA exchanges
   used for rekeying of the IKE or Child SA by replacing the SA and TS
   payloads with a Notify Message payload.  Reducing size and complexity
   of IKEv2 exchanges is especially useful for low power consumption
   battery powered devices.
- **draft-ietf-jmap-blobext-03** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Blob Management](https://datatracker.ietf.org/doc/draft-ietf-jmap-blobext/) — The JSON Meta Application Protocol (JMAP) base protocol ([JMAP-CORE])
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
- **draft-ietf-jmap-emailpush-04** (new-draft, score 0, ignored_after_review) [jmap]: [JSON Meta Application Protocol (JMAP) Email Delivery Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-jmap-emailpush/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) that allows clients to receive an object via a JMAP
   push subscription whenever a new email is delivered that matches a
   client-defined filter.  The object can also include properties from
   the email, to allow a user notification to be displayed without
   having to make a further network request.
- **draft-ietf-jmap-filenode-20** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP File Storage extension](https://datatracker.ietf.org/doc/draft-ietf-jmap-filenode/) — The JMAP base protocol (RFC 8620) provides the ability to upload and
   download arbitrary binary data.  This binary data is called a "blob",
   and can be used in all other JMAP extensions.

   This extension adds a FileNode data type and methods to expose blobs
   as a filesystem, along with the types of metadata that are provided
   by other remote filesystem protocols.
- **draft-ietf-jmap-object-history-03** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Object History](https://datatracker.ietf.org/doc/draft-ietf-jmap-object-history/) — The JMAP base protocol (RFC8620) provides methods for synchronizing
   the current state of data objects between client and server.  This
   extension adds the ability to retrieve historical versions of
   objects, including objects that have been destroyed, by extending the
   standard Foo/get method, to find destroyed objects with Foo/query,
   and to restore them with Foo/set.
- **draft-ietf-lsr-l2-bundle-member-remote-id-12** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  This document
   describes how Open Shortest Path First (OSPF) and Intermediate System
   to Intermediate System (IS-IS) advertise the remote interface
   identifiers for L2 bundle members.  The corresponding extension of
   BGP Link State (BGP-LS) is also specified.
- **draft-ietf-lsr-pcpps-03** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/) — [I-D.many-teas-power-steering] introduces a Power Conserving Path
   Placement Strategy (PCPPS).  When possible, PCPPS concentrates
   traffic onto a small set of network resources.  When traffic is
   concentrated onto a small set of network resources, other network
   resources become idle and can be powered down until they are needed
   again.  This conserves energy and reduces environmental impact.

   PCPPS uses information that is distributed by an IGP.  This document
   specifies the IS-IS encoding for that information.
- **draft-ietf-mailmaint-aprf-01** (new-draft, score 0, ignored_after_review) [mailmaint]: [Aggregate Performance Reporting](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-aprf/) — Definition of an aggregate performance report format for email
   messaging, the means to discover target destinations, and a specified
   delivery method.
- **draft-ietf-mailmaint-autoconfig-07** (new-draft, score 0, ignored_after_review) [mailmaint]: [Mail AutoConfig](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-autoconfig/) — This document describes a protocol that allows client applications to
   set up mail accounts and related services like calendar, contact and
   file sync, chat and video conference accounts, using only the email
   address and password.

   This existing protocol is used by service providers to publish the
   account configuration, so that client applications can find a working
   configuration automatically.  The configuration is based on an email
   address, but is not limited to configuring email service.

   The running code and deployments documented here are in some cases no
   longer in line with security best-practices.  Implementers are urged
   to study the security considerations attentively.
- **draft-ietf-mailmaint-pdparchive-03** (new-draft, score 0, ignored_after_review) [mailmaint]: [Personal Data Portability Archive](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pdparchive/) — This document proposes the Personal Data Portability Archive format
   (PDPA), suitable for import/export, backup/restore, and data transfer
   scenarios for personal data.
- **draft-ietf-manet-olsrv2-responsive-02** (new-draft, score 0, ignored_after_review) [manet]: [Responsive Use of the Mobile Ad Hoc Network (MANET) Routing Protocol OLSRv2](https://datatracker.ietf.org/doc/draft-ietf-manet-olsrv2-responsive/) — This specification describes an optional Topology Control (TC)
   message that can be sent by an OLSRv2 router.  This is permitted, but
   not suggested, by the existing protocol, but is here recommended for
   use in some networks.  The original motivation for this message came
   from considering the circumstances of a mostly stable network, in the
   most extreme case updated only by messages responding to the arrival
   and departure of routers, in which case the additional TC message
   would be not just recommended but required.  While this extreme case
   is highly unlikely to be ever used, consideration of this additional
   message indicates that it could be useful in reducing the routing
   convergence time in any network in which messages are sent at lengthy
   intervals.  Sending such a message is, although not previously
   suggested, permitted by OLSRv2 and thus implementations of OLSRv2
   that do and do not send such messages are fully compatible.

   This specification updates RFC 7181 "The Optimized Link State Routing
   Protocol version 2 (OLSRv2)".
- **draft-ietf-mimi-content-10** (new-draft, score 0, ignored_after_review) [mimi]: [More Instant Messaging Interoperability (MIMI) message content](https://datatracker.ietf.org/doc/draft-ietf-mimi-content/) — This document describes content semantics common in Instant Messaging
   (IM) systems and describes a profile suitable for instant messaging
   interoperability of messages end-to-end encrypted inside the MLS
   (Message Layer Security) Protocol.
- **draft-ietf-mls-extensions-11** (new-draft, score 0, ignored_after_review) [mls]: [The Messaging Layer Security (MLS) Extensions](https://datatracker.ietf.org/doc/draft-ietf-mls-extensions/) — The Messaging Layer Security (MLS) protocol is an asynchronous group
   authenticated key exchange protocol.  MLS provides a number of
   capabilities to applications, as well as several extension points
   internal to the protocol.  This document provides a consolidated
   application API, guidance for how the protocol's extension points
   should be used, and a few concrete examples of both core protocol
   extensions and uses of the application API.
- **draft-ietf-mls-pq-ciphersuites-07** (new-draft, score 0, ignored_after_review) [mls]: [ML-KEM and Hybrid Cipher Suites for Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-pq-ciphersuites/) — This document registers new cipher suites for Messaging Layer
   Security (MLS) based on "post-quantum" algorithms, which are intended
   to be resilient to attack by quantum computers.  These cipher suites
   are constructed using the new Module-Lattice-Based Key-Encapsulation
   Mechanism (ML-KEM), optionally in combination with traditional
   elliptic curve KEMs, together with appropriate authenticated
   encryption, hash, and signature algorithms.
- **draft-ietf-mls-ratchet-tree-options-02** (new-draft, score 0, ignored_after_review) [mls]: [Ways to convey the Ratchet Tree in Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-ratchet-tree-options/) — The Messaging Layer Security (MLS) protocol needs to share its
   ratchet_tree object to welcome new clients into a group and in
   external joins.  While the protocol only defines a mechanism for
   sharing the entire tree, most implementations use various
   optimizations to avoid sending this structure repeatedly in large
   groups.  This document describes a way to convey these improvements
   in a standardized way and to convey the parts of a GroupInfo object
   that are not visible to an intermediary server.
- **draft-ietf-mls-virtual-clients-02** (new-draft, score 0, ignored_after_review) [mls]: [MLS Virtual Clients](https://datatracker.ietf.org/doc/draft-ietf-mls-virtual-clients/) — This document describes a method that allows multiple MLS clients to
   emulate a virtual MLS client.  A virtual client allows multiple
   emulator clients to jointly participate in an MLS group under a
   single leaf.  Depending on the design of the application, virtual
   clients can help hide metadata and improve performance.
- **draft-ietf-mops-network-overlay-impacts-05** (new-draft, score 0, ignored_after_review) [mops]: [Network Overlay Impacts to Streaming Video](https://datatracker.ietf.org/doc/draft-ietf-mops-network-overlay-impacts/) — This document examines the operational impacts on streaming video
   applications resulting from network policy changes introduced by
   network overlays.  Such overlays may alter IP address assignment,
   transport protocols, routing behavior, or DNS resolution.  These
   changes can, in turn, affect critical aspects of content delivery,
   including latency, CDN cache selection, delivery path optimization,
   traffic classification, and content access controls.
- **draft-ietf-moq-loc-05** (new-draft, score 0, ignored_after_review) [moq]: [Low Overhead Media Container](https://datatracker.ietf.org/doc/draft-ietf-moq-loc/) — This specification describes a Low Overhead Media Container (LOC)
   format for encoded and encrypted audio and video media data to be
   used primarily for interactive Media over QUIC Transport (MOQT).  It
   may be used in the MOQT Streaming Format (MSF) specification, which
   defines a catalog format for publishers to declare and describe their
   LOC tracks and for subscribers to consume them.  Examples are also
   provided for building media applications using LOC and MOQT.
- **draft-ietf-moq-transport-23** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-mpls-mna-ioam-16** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
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
- **draft-ietf-netconf-distributed-notif-24** (new-draft, score 0, ignored_after_review) [netconf]: [Subscription to Notifications in a Distributed Architecture](https://datatracker.ietf.org/doc/draft-ietf-netconf-distributed-notif/) — This document describes extensions to configured subscriptions to
   YANG notifications to allow metrics being published directly from
   processors on line cards to target receivers, while subscription is
   still maintained at the route processor in a distributed forwarding
   system of a network node.
- **draft-ietf-netconf-error-registries-01** (new-draft, score 0, ignored_after_review) [netconf]: [Error List and Error Identities Registries for YANG-driven protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-error-registries/) — This document defines IANA registries for the YANG Protocol Error
   List and YANG Protocol Error Identities.
- **draft-ietf-netconf-list-pagination-nc-14** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-nc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to NETCONF [RFC6241].

   This document updates [RFC6241], to augment the <get> and <get-
   config> "rpc" statements, and [RFC8526], to augment the <get-data>
   "rpc" statement, to define input parameters necessary for list
   pagination.
- **draft-ietf-netconf-list-pagination-rc-13** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-rc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to RESTCONF [RFC8040].

   This document updates RFC 8040, to declare "list" and "leaf-list" as
   valid resource targets for the RESTCONF GET operation, to define GET
   query parameters necessary for list pagination, and to define a
   media-type for XML-based lists.
- **draft-ietf-netconf-yang-notifications-versioning-19** (new-draft, score 0, ignored_after_review) [netconf]: [Support of Versioning in YANG Notifications Subscriptions](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-notifications-versioning/) — This document defines a YANG module which extends the YANG-Push
   Subscription mechanism to enforce that particular revisions or
   semantic versions are used when configuring or establishing a
   Subscription.  It also extends the YANG-Push Subscription state
   change Notifications to include additional context about the YANG
   schema associated with the Subscription.
- **draft-ietf-netconf-yang-push-2-01** (new-draft, score 0, ignored_after_review) [netconf]: [YANG Datastore Telemetry (YANG Push version 2)](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-push-2/) — YANG Push version 2 is a YANG datastore telemetry solution, as an
   alternative lightweight specification to the Subscribed Notifications
   and YANG Push solution, specifically optimized for the efficient
   observability of operational data.
- **draft-ietf-netmod-iana-yang-guidance-04** (new-draft, score 0, ignored_after_review) [netmod]: [Guidance for Managing YANG Modules in RFCs and IANA Registries](https://datatracker.ietf.org/doc/draft-ietf-netmod-iana-yang-guidance/) — This document provides guidance to the RFC Editor and IANA on
   managing YANG modules in RFCs and IANA registries, ensuring
   consistent application of YANG Semantic Versioning rules.
- **draft-ietf-netmod-yang-packages-11** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Packages](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-packages/) — This document defines YANG packages: versioned organizational
   structures used to manage the schema and conformance of a set of YANG
   modules as a cohesive unit.
- **draft-ietf-nmop-rfc3535-20years-later-05** (new-draft, score 0, ignored_after_review) [nmop]: [An Update of Operators Requirements on Network Management Protocols and Modelling](https://datatracker.ietf.org/doc/draft-ietf-nmop-rfc3535-20years-later/) — This document identifies a list of operators requirements for network
   management operations.  These requirements reflect advances in this
   field since the publication of "IAB Network Management Workshop" (RFC
   3535), which was instrumental for developing many key technologies
   that are widely deployed.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/boucadair/rfc3535-20years-later.
- **draft-ietf-openpgp-external-secrets-01** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-ietf-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
- **draft-ietf-opsawg-ipfix-alt-mark-10** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-ipfix-ecn-01** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of ECN Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-ecn/) — This document defines a set of IPFIX Information Elements for
   monitoring Explicit Congestion Notification (ECN).  These Information
   Elements allow network operators to observe ECN codepoint usage
   across network traffic and evaluate the corresponding traffic
   performance.
- **draft-ietf-opsawg-veloce-yang-01** (new-draft, score 0, ignored_after_review) [opsawg]: [YANG deVELpment PrOCEss and maintenance (VELOCE)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-veloce-yang/) — This document describes a YANG deVELopment PrOCEss and maintenance
   (VELOCE) that is more suitable for the development of YANG modules or
   YANG modules update within the IETF.

   Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-opsawg-wg/veloce/tree/main.
- **draft-ietf-pce-flexible-grid-21** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-pcep-bfd-parameters-03** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extensions to support BFD parameters](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-bfd-parameters/) — This document proposes extension to PCEP to configure LSP parameters.
   Some of LSP parameters are needed to configure S-BFD for candidate
   paths.  Each candidate path is identified in PCEP by its uniquely
   assigned PLSP-ID.  The mechanism proposed in this document is
   applicable to to all path setup types.  This extension can work with
   ifferent PCEP Path Setup Types but especially suitable for Segment
   Routing (SR-MPLS, SRv6)..
- **draft-ietf-pce-pcep-l2-flowspec-11** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Layer 2 (L2) Flow Specification](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-l2-flowspec/) — The Path Computation Element (PCE) is a functional component capable
   of selecting paths through a traffic engineering (TE) network.  These
   paths may be supplied in response to requests for computation or may
   be unsolicited requests issued by the PCE to network elements.  Both
   approaches use the PCE Communication Protocol (PCEP) to convey the
   details of the computed path.

   Traffic flows may be categorized and described using "Flow
   Specifications".  RFC 8955 defines the Flow Specification and
   describes how Flow Specification components are used to describe
   traffic flows.  RFC 8955 also defines how Flow Specifications may be
   distributed in BGP to allow specific traffic flows to be associated
   with routes.

   RFC 9168 specifies a set of extensions to PCEP to support the
   dissemination of Flow Specifications.  This allows a PCE to indicate
   what traffic should be placed on each path that it is aware of.  This
   document updates RFC 9168 by updating the assignment policies for a
   range of Flow Specification TLV Type Indicators.

   The extensions defined in this document extend the support for
   Ethernet Layer 2 (L2) and Layer 2 Virtual Private Network (L2VPN)
   traffic filtering rules either by themselves or in conjunction with
   Layer 3 (L3) flowspecs.
- **draft-ietf-pce-pcep-nrp-02** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions for Network Resource Partition (NRP)](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-nrp/) — This document specifies the extensions to Path Computation Element
   Communication Protocol (PCEP) to carry Network Resource Partition
   (NRP) related information in the PCEP messages.  The extensions in
   this document can be used to indicate the NRP-specific constraints
   and information needed in path computation, path status report and
   path initialization.
- **draft-ietf-pce-state-sync-16** (new-draft, score 0, ignored_after_review) [pce]: [State Synchronization Procedures between Stateful Path Computation Elements (PCEs)](https://datatracker.ietf.org/doc/draft-ietf-pce-state-sync/) — The Path Computation Element (PCE) Communication Protocol (PCEP)
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
   preventing computation loops.  It is published as Experimental to
   gather implementation and deployment experience.
- **draft-ietf-pce-topology-filter-02** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions for Topology Filter](https://datatracker.ietf.org/doc/draft-ietf-pce-topology-filter/) — A topology filter is a data construct that is used to filter network
   topologies.  The Path Computation Element (PCE) MUST take into
   account the topology related constraints during the path computation.
   This document proposes a set of extensions for Path Computation
   Element Communication Protocol (PCEP) to support the topology filter.
- **draft-ietf-pim-deterministic-ecmp-01** (new-draft, score 0, ignored_after_review) [pim]: [Deterministic Upstream Neighbor Selection for PIM Joins](https://datatracker.ietf.org/doc/draft-ietf-pim-deterministic-ecmp/) — In densely interconnected networks, a PIM node may have many choices
   as to what upstream neighbor to send a JOIN message to, for a given
   source and group.  This document describes a mechanism for multiple
   nodes (e.g., leaf nodes in a data center) to pick the same upstream
   node (e.g., spine node) to avoid redundant traffic flows.
- **draft-ietf-pim-ipv4-in-ipv6-core-01** (new-draft, score 0, ignored_after_review) [pim]: [Native IPv4 multicast in IPv6 Core using PIM](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv4-in-ipv6-core/) — This document describes how PIM Sparse-Mode can be used to construct
   IPv4 multicast trees across an IPv6-only network core.  This allows
   forwarding of native IPv4 multicast data packets.  The document
   specifies how to send and receive IPv4 PIM messages with IPv6
   headers, using a new well-known link-local IPv6 multicast address,
   and the use of RPF vectors for reachability.
- **draft-ietf-pim-ipv6-zeroconf-assignment-17** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the requirements and most of the desired
   characteristics listed in RFC 10019.
- **draft-ietf-pim-multicast-lessons-learned-10** (new-draft, score 0, ignored_after_review) [pim]: [Multicast Lessons Learned from Decades of Deployment Experience](https://datatracker.ietf.org/doc/draft-ietf-pim-multicast-lessons-learned/) — This document gives a historical perspective about the design and
   deployment of multicast routing protocols.  The document describes
   the technical challenges discovered from building these protocols.
   Even though multicast has enjoyed success of deployment in special
   use-cases, this document discusses what were, and are, the obstacles
   for mass deployment across the Internet.  Individuals who are working
   on new multicast related protocols will benefit by knowing why
   certain older protocols are no longer in use today.
- **draft-ietf-pim-rfc1112bis-10** (new-draft, score 0, ignored_after_review) [pim]: [Host Extensions for IP Multicasting and "Any Source Multicast" (ASM) IP service](https://datatracker.ietf.org/doc/draft-ietf-pim-rfc1112bis/) — This memo specifies the extensions required of a host implementation
   of the Internet Protocol (IP) to support IP multicast with the IP
   service interface "Any Source Multicast" (ASM).  This specification
   applies to both versions 4 and 6 of the Internet Protocol.
   Distribution of this memo is unlimited.

   This document replaces RFC1112 for everything but its specification
   of the IGMP version 1 protocol.
- **draft-ietf-plants-mtc-deploy-use-cases-01** (new-draft, score 0, ignored_after_review) [plants]: [Merkle Tree Certificates Deployment Use Cases](https://datatracker.ietf.org/doc/draft-ietf-plants-mtc-deploy-use-cases/) — Merkle Tree Certificates (MTCs)

   [I-D.ietf-plants-merkle-tree-certs] has been defined for the use case
   of the WebPKI.  In this document we explore when and how MTCs in
   parts or full can be used in different use cases.  Some of these use-
   cases may provide benefit for private PKI usage.
- **draft-ietf-pquip-pqc-hsm-constrained-11** (new-draft, score 0, ignored_after_review) [pquip]: [Adapting Constrained Devices for Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/) — This document provides guidance on integrating Post-Quantum
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
- **draft-ietf-procon-2026bis-12** (new-draft, score 0, ignored_after_review) [procon]: [The Internet Standards Process](https://datatracker.ietf.org/doc/draft-ietf-procon-2026bis/) — This memo documents the process used by the Internet community for
   the standardization of protocols and procedures.  It defines the
   stages in the standardization process, the requirements for moving a
   document between stages, and the types of documents used during this
   process.  It also addresses the intellectual property rights and
   copyright issues associated with the standards process.

   This document obsoletes RFC 2026, RFC 5657, RFC 6410, RFC 7100, RFC
   7127, RFC 8789, and RFC 9282.  It also includes the changes from RFC
   7475.  If this document and [_2418bis] are published as RFCs, then
   taken together the two of them make RFC 7475 obsolete.
- **draft-ietf-procon-chair-delegate-00** (new-draft, score 0, ignored_after_review) [procon]: [The IETF Chair May Delegate](https://datatracker.ietf.org/doc/draft-ietf-procon-chair-delegate/) — This document affirms that the IETF Chair may delegate some of their
   responsibilities to other Area Directors, and updates RFC 3710 and
   RFC 9281 to allow additional General Area Directors and to remove
   stale text.
- **draft-ietf-procon-chair-standin-00** (new-draft, score 0, ignored_after_review) [procon]: [The IETF Chair Has a Stand-In](https://datatracker.ietf.org/doc/draft-ietf-procon-chair-standin/) — This document defines a stand-in for the IETF Chair, called the
   Acting IETF Chair, in case the IETF Chair becomes indisposed.
- **draft-ietf-quic-qlog-h3-events-14** (new-draft, score 0, ignored_after_review) [quic]: [HTTP/3 qlog event definitions](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-h3-events/) — This document defines qlog event schemas containing concrete events
   for the core HTTP/3 protocol and selected extensions.  It also
   defines an http namespace for the Capsule Protocol.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.
- **draft-ietf-quic-qlog-main-schema-15** (new-draft, score 0, ignored_after_review) [quic]: [qlog: Structured Logging for Network Protocols](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-main-schema/) — qlog provides extensible structured logging for network protocols,
   allowing for easy sharing of data that benefits common debug and
   analysis methods and tooling.  This document describes key concepts
   of qlog: formats, files, traces, events, and extension points.  This
   definition includes the high-level log file schemas, and generic
   event schemas.  Requirements and guidelines for creating protocol-
   specific event schemas are also presented.  All schemas are defined
   independent of serialization format, allowing logs to be represented
   in various ways such as JSON, CSV, or protobuf.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.
- **draft-ietf-quic-qlog-quic-events-14** (new-draft, score 0, ignored_after_review) [quic]: [QUIC event definitions for qlog](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-quic-events/) — This document describes a qlog event schema containing concrete qlog
   event definitions and their metadata for the core QUIC protocol and
   selected extensions.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.
- **draft-ietf-radext-connectinfo-02** (new-draft, score 0, ignored_after_review) [radext]: [A syntax for the RADIUS Connect-Info attribute used in Wi-Fi networks](https://datatracker.ietf.org/doc/draft-ietf-radext-connectinfo/) — This document describes a syntax for the Connect-Info attribute used
   with the RADIUS protocol, enabling RADIUS clients to provide RADIUS
   servers information pertaining to a user's connection with an IEEE
   802.11 wireless network.
- **draft-ietf-regext-rdap-extensions-18** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes, clarifies and further specifies the usage of
   extensions in RDAP.
- **draft-ietf-regext-rfc3915bis-01** (new-draft, score 0, ignored_after_review) [regext]: [Domain Registry Grace Period Mapping for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-ietf-regext-rfc3915bis/) — This document describes an Extensible Provisioning Protocol (EPP)
   [RFC5730] extension mapping for the management of Domain Name System
   (DNS) domain names subject to "grace period" policies.  Grace period
   policies exist to allow protocol actions to be reversed or otherwise
   revoked during a short period of time after the protocol action has
   been performed.  This mapping extends the EPP domain name mapping
   [RFC5731] to provide additional features required for grace period
   processing.

   This document replaces the extension mapping for grace periods
   described in [RFC3915], rendering that document obsolete.
- **draft-ietf-roll-dis-modifications-04** (new-draft, score 0, ignored_after_review) [roll]: [RPL DIS Modifications and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-roll-dis-modifications/) — This document updates the RPL routing protocol specification by
   defining new DODAG Information Solicitation (DIS) flags and options
   that enable a RPL node to exert finer control over how neighboring
   RPL routers respond to its DIO solicitations.  In addition, this
   document describes several use cases that motivate these DIS
   extensions and illustrate scenarios in which enhanced control of DIO
   responses improves network efficiency, responsiveness, and
   robustness.
- **draft-ietf-rpp-data-objects-02** (new-draft, score 0, ignored_after_review) [rpp]: [RESTful Provisioning Protocol (RPP) Data Objects](https://datatracker.ietf.org/doc/draft-ietf-rpp-data-objects/) — This document defines data objects for the RESTful Provisioning
   Protocol (RPP) and sets up the IANA RPP Data Object Registry to
   describe and catalogue them.  Specifically, it details the logical
   structure, constraints, and protocol operations (including their
   inputs, outputs, and business logic) for registry resources: domain
   names, contacts, hosts, organisations, users, and messages, as well
   as the discovery and profile objects that describe server
   capabilities.  In accordance with the RPP architecture, these
   definitions focus entirely on the semantics, remaining independent of
   any specific data representation or media type (e.g., JSON or XML).
- **draft-ietf-rpp-json-01** (new-draft, score 0, ignored_after_review) [rpp]: [JSON for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-ietf-rpp-json/) — This document defines the rules for representing the RESTful
   Provisioning Protocol (RPP) data objects using the JavaScript Object
   Notation (JSON) Data Interchange Format.  It specifies how RPP
   primitive types, common data types, Component Objects, Data Objects,
   and associations are mapped to JSON and JSON Schema, and provides
   normative JSON Schema definitions and examples for the RPP Data
   Objects, the representation of update requests, and an extension
   framework.
- **draft-ietf-rtgwg-atn-bgp-35** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
   mobile routing solutions for a worldwide Aeronautical
   Telecommunications Network with Internet Protocol Services (ATN/IPS).
   The ATN/IPS will eventually augment existing communication services
   with an IP-based service supporting pervasive Air Traffic Management
   (ATM) for Air Traffic Controllers (ATC), Airline Operations
   Controllers (AOC), and all commercial aircraft worldwide.  This
   informational document describes a simple and extensible mobile
   routing service based on the industry-standard Border Gateway
   Protocol (BGP) and Domain Name System (DNS) to address the ATN/IPS
   requirements.
- **draft-ietf-rtgwg-bgp-pic-24** (new-draft, score 0, ignored_after_review) [rtgwg]: [BGP Prefix Independent Convergence](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-bgp-pic/) — In a network comprising thousands of BGP peers exchanging millions of
   routes, it is desirable to restore traffic after a failure in a time
   period that does not depend on the number of BGP prefixes.

   This document describes an architecture by which traffic can be re-
   routed to Equal Cost Multi-Path (ECMP), Unequal Cost Multi-path
   (UCMP), or pre-calculated backup paths in a timeframe that does not
   depend on the number of BGP prefixes.  The objective is achieved
   through organizing the forwarding data structures in a hierarchical
   manner and sharing forwarding elements among the maximum possible
   number of routes.  The described technique yields prefix independent
   convergence while ensuring incremental deployment, complete
   automation, and zero management and provisioning effort.  It is
   noteworthy to mention that the benefits of BGP Prefix Independent
   Convergence (BGP-PIC) are hinged on the existence of more than one
   path whether as multipaths or primary-backup.
- **draft-ietf-rtgwg-multisegment-sdwan-17** (new-draft, score 0, ignored_after_review) [rtgwg]: [Multi-segment SD-WAN via Cloud Backbone](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/) — This document describes a method for seamlessly
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
- **draft-ietf-savnet-inter-domain-problem-statement-22** (new-draft, score 0, ignored_after_review) [savnet]: [Problem Statement, Gap Analysis, and Requirements for Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/) — This document analyzes the problem space and provides a gap analysis
   of existing inter-domain source address validation (SAV) mechanisms.
   Based on these findings, it outlines the technical requirements for
   future improvements.
- **draft-ietf-schc-architecture-07** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression (SCHC) Architecture](https://datatracker.ietf.org/doc/draft-ietf-schc-architecture/) — The Static Context Header Compression and fragmentation (SCHC)
   framework provides both a header compression mechanism and an
   optional fragmentation mechanism.  This document defines an
   architecture for SCHC deployments, providing guidance for
   implementers and operators on the essential components and their
   interactions required for effective SCHC operation.
- **draft-ietf-scone-applicability-manageability-03** (new-draft, score 0, ignored_after_review) [scone]: [Manageability Considerations for SCONE](https://datatracker.ietf.org/doc/draft-ietf-scone-applicability-manageability/) — This document describes the manageability considerations for network
   operators for providing throughput advice to application endpoints.
   This guidance is specifically addressed within the context of
   communication networks utilizing the Standard Communication with
   Network Elements (SCONE) protocol [SCONE].
- **draft-ietf-scone-protocol-10** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-8210bis-28** (new-draft, score 0, ignored_after_review) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RFC6480) prefix origin data, Router Keys, and ASPA
   data from a trusted cache.  This document describes a protocol to
   deliver them.

   This document describes version 2 of the RPKI-to-Router protocol.
   [RFC6810] describes version 0, and [RFC8210] describes version 1.
   This document is compatible with both.
- **draft-ietf-sidrops-publication-server-bcp-12** (new-draft, score 0, ignored_after_review) [sidrops]: [Best Practices for Operating Resource Public Key Infrastructure (RPKI) Publication Services](https://datatracker.ietf.org/doc/draft-ietf-sidrops-publication-server-bcp/) — This document describes best current practices for operating an RFC
   8181 (A Publication Protocol for the Resource Public Key
   Infrastructure (RPKI)) Publication Engine and its associated publicly
   accessible rsync (RFC 5781) and RPKI Repository Delta Protocol (RRDP)
   (RFC 8182) repositories.
- **draft-ietf-sml-structured-quoted-content-01** (new-draft, score 0, ignored_after_review) [sml]: [Structured Quoted Content](https://datatracker.ietf.org/doc/draft-ietf-sml-structured-quoted-content/) — This document describes a machine-readable format for conveying
   quoted content in email messages.  This can be used when replying to
   or forwarding an email message.

   Structured quoted content is expected to be used in conjunction with
   conventional, human-readable quote formatting.  They are based on the
   forthcoming "structured email" specification defined in [I-D.ietf-
   sml-structured-email-03] and related drafts.
- **draft-ietf-sml-structured-vacation-notices-02** (new-draft, score 0, ignored_after_review) [sml]: [Structured vacation notices](https://datatracker.ietf.org/doc/draft-ietf-sml-structured-vacation-notices/) — This document describes a machine-readable format for conveying
   unavailability information in email messages.  This includes
   "vacation notices" of persons but also different forms of
   unavailability for emails sent by programs.

   Structured vacation notices are supposed to be used in conjunction
   with conventional, human-readable vacation notices in most cases.
   They are based on the forthcoming "structured email" specification
   defined in [I-D.ietf-sml-structured-email-06] and related drafts.
- **draft-ietf-spring-bfd-13** (new-draft, score 0, ignored_after_review) [spring]: [Bidirectional Forwarding Detection (BFD) in Segment Routing Networks Using MPLS Dataplane](https://datatracker.ietf.org/doc/draft-ietf-spring-bfd/) — The Segment Routing (SR) architecture leverages the paradigm of
   source routing.  It can be realized in the Multiprotocol Label
   Switching (MPLS) network without any changes to the data plane.  This
   document describes using Bidirectional Forwarding Detection (BFD) for
   monitoring individual segment lists of candidate paths of an SR
   Policy.  It documents the use of various BFD modes and features such
   as BFD Demand mode, Seamless BFD, and BFD Echo function with the BFD
   Control packet payload in the Segment Routing over MPLS domain.
   Also, this document defines how to use Label Switched Path Ping to
   bootstrap a BFD session, with optional control of selecting a segment
   list in the reverse direction of the BFD session.
- **draft-ietf-spring-pmtu-sr-policy-05** (new-draft, score 0, ignored_after_review) [spring]: [Path MTU (PMTU) for Segment Routing (SR) Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-pmtu-sr-policy/) — This document defines the Path MTU (PMTU) for Segment Routing (SR)
   Policy (called SR-PMTU).  It applies to both Segment Routing over
   IPv6 (SRv6) and SR-MPLS.  This document specifies the framework of
   SR-PMTU for SR Policy including the link MTU collection, the SR-PMTU
   computation, the SR-PMTU enforcement, and the handling behaviours on
   the headend.
- **draft-ietf-spring-srv6-policy-sid-list-opt-01** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 Policy SID List Optimization](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-policy-sid-list-opt/) — Segment Routing (SR) allows a node to steer a packet flow along any
   path.  SR Policy is an ordered list of segments (i.e., instructions)
   that represent a source-routed policy.  The packets steered into an
   SR Policy carry an ordered list of segments associated with that SR
   Policy.  An SR Policy can be instantiated SR-MPLS and SRv6 data
   planes.

   In some use cases, an SRv6 Policy's SID list ends with the policy
   endpoint's node SID, and the traffic steered (over policy) already
   ensures that it is taken to the policy endpoint.  In such cases, the
   SID list can be optimized by excluding the endpoint Node SID when
   installing the policy.  This draft specifies procedures to indicate
   whether the endpoint's node SID needs to be included or excluded when
   installing the SRv6 Policy.
- **draft-ietf-srv6ops-srv6-deployment-04** (new-draft, score 0, ignored_after_review) [srv6ops]: [SRv6 Deployment Options](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/) — When deciding to migrate a network from existing data-plane
   technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as
   VXLAN) to SRv6, common questions involve how to perform the
   migration, how to minimize impact to the existing network and what
   techniques are available to support a smooth transition.  This
   document presents various deployment and migration options for
   networks evolving toward SRv6 from prior transport or overlay
   technologies.
- **draft-ietf-srv6ops-srv6addressing-01** (new-draft, score 0, ignored_after_review) [srv6ops]: [Addressing Recommendations for SRv6](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6addressing/) — This document provides recommendations for addressing SRv6 locators
   format.  It introduces concepts of Blocks, Sets, and Node IDs, and
   explains how summarization boundaries and flexible algorithm support
   can be implemented for both small and large networks.
- **draft-ietf-suit-mud-11** (new-draft, score 0, ignored_after_review) [suit]: [Strong Assertions of IoT Network Access Requirements](https://datatracker.ietf.org/doc/draft-ietf-suit-mud/) — The Manufacturer Usage Description (MUD) specification describes the
   access and network functionality required for a device to properly
   function.  This description has to reflect the software running on
   the device and its configuration.  Because of this, the most
   appropriate entity for describing device network access requirements
   is the same as the entity developing the software and its
   configuration.

   A network presented with a MUD file by a device allows detection of
   misbehavior by the device software and configuration of access
   control.

   This document defines a way to link the Software Updates for Internet
   of Things (SUIT) manifest to a MUD file offering a stronger binding
   between the two.
- **draft-ietf-teas-actn-poi-applicability-21** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) to Packet Optical Integration (POI)](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-applicability/) — This document explores the applicability of the Abstraction and
   Control of TE Networks (ACTN) architecture to Packet Optical
   Integration (POI) within the context of IP/MPLS and optical
   internetworking.  It examines the YANG data models defined by the
   IETF that enable an ACTN-based deployment architecture and highlights
   specific scenarios pertinent to Service Providers.

   Existing IETF protocols and data models are identified for each
   multi-technology scenario (packet over optical), particularly
   emphasising the Multi-Domain Service Coordinator to Provisioning
   Network Controller Interface (MPI) within the ACTN architecture.
- **draft-ietf-teas-actn-poi-assurance-06** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) for Packet Optical Integration (POI) service assurance](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-assurance/) — This document extends the analysis of the applicability of
   Abstraction and Control of Traffic Engineered Networks (ACTN)
   architecture to Packet Optical Integration (POI) to cover multi-layer
   service assurance scenarios.

   Specifically, the ACTN architecture is analyzed to support service
   assurance for end-to-end IP services such as L2VPN or L3VPN
   connectivity services, with specific Service Level Agreement (SLA)
   requirements, through the detection and correlation of failures
   across the optical and packet layers, done by the relevant
   Provisioning Network Controller (PNC) in coopearation with the Multi-
   Domain Service Coordinator (MDSC).

   Existing IETF protocols and data models are identified for each
   multi-layer (packet over optical) service assurance scenario with a
   specific focus on the Multi-Domain Service Coordinator to
   Provisioning Network Controllers Interface (MPI) in the ACTN
   architecture.
- **draft-ietf-tiptop-ip-architecture-03** (new-draft, score 0, ignored_after_review) [tiptop]: [An Architecture for IP in Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-ip-architecture/) — The IP protocol stacks used on Earth's Internet are typically
   configured based on assumptions of short delays and mostly
   uninterrupted communications.  This document describes an
   architecture of the IP protocol stack tailored for its use in deep
   space.  It involves buffering IP packets in IP forwarders facing
   intermittent links and adjusting transport protocol configurations
   and application protocol timers.  This architecture applies to the
   Moon, Mars, and general interplanetary networking.
- **draft-ietf-tiptop-quic-profile-01** (new-draft, score 0, ignored_after_review) [tiptop]: [QUIC Profile for Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-quic-profile/) — Deep space communications involve long delays (e.g., the Earth to
   Mars one-way delay is ~4-20 minutes) and often intermittent
   communications.  In this context, the default configuration of QUIC
   stacks, tuned for the terrestrial Internet, is not suitable for deep
   space.  This document defines a QUIC profile for deep space.  It
   provides guidance on how to estimate and set transport parameters and
   local implementation settings, advice to space mission operators and
   application developers on how to configure QUIC for the deep space
   use case, and guidance to QUIC stack developers on exposing the
   required controls in their API.
- **draft-ietf-tiptop-usecase-04** (new-draft, score 0, ignored_after_review) [tiptop]: [IP in Deep Space: Key Characteristics, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-tiptop-usecase/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  Most of the IP protocol stack
   used on the Internet, in particular reliable transport protocols and
   applications, is based on the assumptions of shorter delays and
   mostly uninterrupted communications.  This document describes the key
   characteristics, use cases, and requirements for deep space
   networking, intended to help when profiling IP protocols in such
   environment.
- **draft-ietf-tsvwg-careful-resume-qlog-03** (new-draft, score 0, ignored_after_review) [tsvwg]: [Quic Logging for Convergence of Congestion Control from Retained State](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-careful-resume-qlog/) — This document specifies a logging format for a cautious method for
   Careful Resume when using the IETF quic transport protocol.  It
   defines the logging format for qlog.
- **draft-ietf-v6ops-6mops-12** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (e.g. local area network (LAN)).  This approach enables
   incremental transition from dual-stack to IPv6-only networks by
   allowing IPv6-capable devices to remain IPv6-only while the network
   is seamlessly supplying IPv4 addresses to those devices that require
   them.  This document discusses the requirements, recommendations, and
   challenges associated with deploying IPv6-mostly networks in
   enterprise and public Wi-Fi environments.
- **draft-ietf-v6ops-aaaa-filtering-02** (new-draft, score 0, ignored_after_review) [v6ops]: [A recommendation for filtering address records in stub resolvers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-aaaa-filtering/) — Since IPv4 and IPv6 addresses are represented by different resource
   records in the Domain Name System, operating systems capable of
   running both IPv4 and IPv6 need to execute two queries when resolving
   a host name.  This document discusses the conditions under which a
   stub resolver can optimize the process by not sending one of the
   queries if the host is connected to a single-stack network.
- **draft-ietf-v6ops-icmpext-xlat-v6only-source-03** (new-draft, score 0, ignored_after_review) [v6ops]: [Using Dummy IPv4 Address and Node Identification Extensions for IP/ICMP translators (XLATs)](https://datatracker.ietf.org/doc/draft-ietf-v6ops-icmpext-xlat-v6only-source/) — This document suggests that when a source IPv6 address of an ICMPv6
   message can not be translated to an IPv4 address, and the protocol
   translator does not have any public IPv4 addresses available to
   source the translated packet from, the translator uses the dummy IPv4
   address (192.0.0.8) to translate the IPv6 source address.  This
   document updates RFC6791, Stateless Source Address Mapping for ICMPv6
   Packets, and RFC7915, IP/ICMP Translation Algorithm, by proposing to
   utilize the ICMP extension for Node Identification (draft-ietf-
   intarea-extended-icmp-nodeid) to carry the original IPv6 source
   address of ICMPv6 messages.
- **draft-ietf-v6ops-ipv6-app-testing-08** (new-draft, score 0, ignored_after_review) [v6ops]: [Testing Applications' IPv6 Support](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   Software-as-a-Service (SaaS) providers on how to approach IPv6
   testing in Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including
   "IPv6-only-strict" scenarios without any connectivity towards any
   relevant IPv4 endpoint.

   The document also discusses common misconceptions about the degree to
   which Operating Systems and libraries can abstract IPv6 issues away
   and explains common regressions to avoid when deploying IPv6 support.
- **draft-ietf-v6ops-ipv6-only-06** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  In
   particular, a goal is to provide a reference that describes the
   actual "IPv6-Only" functionality being used in a given scope, not the
   installed protocol stack support.
- **draft-ietf-v6ops-nat64-wkp-1918-10** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the deployment guidance provided in
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
- **draft-ietf-v6ops-rfc7084bis-08** (new-draft, score 0, ignored_after_review) [v6ops]: [Basic Requirements for IPv6 Customer Edge Routers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/) — This document specifies requirements for an IPv6 Customer Edge (CE)
   router.  Specifically, the current version of this document focuses
   on the basic provisioning of an IPv6 CE router and the provisioning
   of IPv6 hosts attached to it.  The document obsoletes RFC 7084.
- **draft-ietf-v6ops-rfc7915-bis-02** (new-draft, score 0, ignored_after_review) [v6ops]: [IP/ICMP Translation Algorithm](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/) — This document describes the Stateless IP/ICMP Translation Algorithm
   (SIIT), which translates between IPv4 and IPv6 packet headers
   (including ICMP headers).  This document obsoletes RFC 7915.
- **draft-ietf-vcon-privacy-primer-02** (new-draft, score 0, ignored_after_review) [vcon]: [Privacy Primer for vCon Developers](https://datatracker.ietf.org/doc/draft-ietf-vcon-privacy-primer/) — This document serves as a primer for technical professionals involved
   in the processing (which includes collecting, using, disclosure, and
   erasure) of personal data, including not only basic identifiers like
   name, age, and address, but also sensitive data contained in
   communications, including biometrics obtained from audio and video
   recordings.  It outlines key concepts in data privacy and
   communications privacy, addressing the ethical and legal
   considerations surrounding the collection, processing, sharing,
   access, retention, and disclosure of individuals’ data.  The document
   covers fundamental privacy principles, defines important roles in
   data processing, and explains individuals’ rights regarding their
   personal information.  It also discusses the scope of protected
   personal information, including sensitive data categories, and
   explores techniques like data aggregation and anonymization.  While
   referencing existing IETF work on privacy in Internet communications,
   this draft extends beyond to address individuals' data privacy in
   relation to organizations handling such data.  The goal is to provide
   a comprehensive overview of privacy considerations, aligning with
   fair information practices and current regulatory frameworks, to
   guide professionals in implementing privacy-respecting data
   management practices.
- **draft-ihlar-poem-delay-quic-00** (new-draft, score 0, ignored_after_review) [none]: [Periodic On-path Explicit Measurement of Delay](https://datatracker.ietf.org/doc/draft-ihlar-poem-delay-quic/) — This document defines POEM Delay, a delay measurement companion to
   the Periodic On-path Explicit Measurement (POEM) protocol for QUIC.
   A delay sample packet, coalesced with ordinary QUIC packets, bounces
   between the endpoints.  On-path observers timestamp it in each
   direction to measure the round-trip time and its components on either
   side of the observer.  Each sample carries a coarse indication of how
   long the sending endpoint held it, so observers can largely exclude
   endpoint delay.  A report packet lets observers tell endpoints how
   network delay is split between the two sides of the observer.
- **draft-irtf-hrpc-association-14** (new-draft, score 0, ignored_after_review) [hrpc]: [Internet Protocols and the Human Rights to Freedom of Association and Assembly](https://datatracker.ietf.org/doc/draft-irtf-hrpc-association/) — This document explores whether the relationship between the Internet
   architecture and the ability of people to exercise their rights to
   peaceful assembly and association online.  It does so by asking the
   question: what are the protocol development considerations for
   freedom of assembly and association?  The Internet increasingly
   mediates our lives, our relationships, and our ability to exercise
   our human rights.  As a global assemblage, the Internet provides a
   public space, yet it is predominantly built on private
   infrastructure.  Since Internet protocols and architecture play a
   central role in the management, development, and use of the Internet,
   we analyze the relation between protocols, architecture, and the
   rights to assemble and associate to mitigate infringements on those
   rights.  This document concludes that the way in which infrastructure
   is designed and implemented impacts people’s ability to exercise
   their freedom of assembly and association.  It is therefore
   recommended that the potential impacts of Internet technologies
   should be assessed, reflecting recommendations of various UN bodies
   and international norms.  Finally, the document considers both the
   limitations on changing association and impact of "forced
   association" in the context of online platforms.
- **draft-irtf-pearg-safe-internet-measurement-15** (new-draft, score 0, ignored_after_review) [pearg]: [Considerations for Performing Safe Measurement on the Internet](https://datatracker.ietf.org/doc/draft-irtf-pearg-safe-internet-measurement/) — Internet measurement is important to researchers from industry,
   academia and civil society.  While measurement of the internet can
   give insight into the functioning and usage of the Internet, it can
   present risks to users, such as breaches of their privacy, legal
   consequences, or disruption of services they rely on.  This document
   describes briefly those risks.  It also outlines considerations for
   researchers to reference when designing internet measurements to
   ensure that those measurements can be carried out with user safety as
   a priority.
- **draft-irtf-rasprg-analysing-ietf-data-01** (new-draft, score 0, ignored_after_review) [rasprg]: [Analysing Internet Standards Data](https://datatracker.ietf.org/doc/draft-irtf-rasprg-analysing-ietf-data/) — This document outlines some issues to consider when studying data
   relating to the Internet standards development ecosystem.  It
   identifies observable components of standards development processes,
   proposes a taxonomy of possible measurements, and highlights
   methodological, interpretive, and ethical considerations.  It is
   intended to support a range of uses, including monitoring standards
   development organisations (SDOs), evaluating the evolution of
   technical work, understanding technology deployment, and informing
   community, leadership, and governance discussions.

   This document is submitted for consideration by the Research and
   Analysis of Standard-Setting Processes Research Group (RASPRG) in the
   IRTF.  It is not an IETF product and is not a standard.
- **draft-janzking-nmrg-telemetry-instrumentation-02** (new-draft, score 0, ignored_after_review) [none]: [Telemetry Methodologies for Analog Measurement Instrumentation](https://datatracker.ietf.org/doc/draft-janzking-nmrg-telemetry-instrumentation/) — Evolution toward network operations automation requires systems
   encompassing software-based analytics and decision-making.  Network-
   based instrumentation provides crucial data for these components and
   processes.  However, the proliferation of such instrumentation and
   the need to migrate the data it generates from the physical network
   to "off-the-network" software poses challenges.  In particular,
   analog measurement instrumentation, which generates time-continuous
   real-number data, may generate significant data volumes.

   This document discusses methodologies for handling analog measurement
   instrumentation data, informed by the requirements of network digital
   twins and of automated fault diagnosis.  It proposes that
   instrumentation report, for each measured quantity and each interval,
   a summary that keeps the level, the rate of change, the departure
   from a steady trend, the extremes over a stated short window and the
   number of measurements taken.  Such summaries can be combined exactly
   over any longer span, and they allow trends, brief events and stopped
   measurements to be detected and reported as they occur.
- **draft-jenkins-cnsa2-cmc-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificate Management over CMS](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-cmc-profile/) — This document specifies a profile of the Certificate Management over
   CMS (CMC) protocol for managing X.509 public key certificates in
   applications that use the Commercial National Security Algorithm
   (CNSA) Suite published by the United States Government.

   The profile applies to the capabilities, configuration, and operation
   of all components of US National Security Systems that manage X.509
   public key certificates over CMS.  It is also appropriate for all
   other US Government systems that process high-value information.

   This memo is not an IETF standard, and does not represent IETF
   community consensus.  The profile is made publicly available here for
   use by developers and operators of these and any other system
   deployments.  This document obsoletes [RFC8756], the CNSA 1.0
   guidance.
- **draft-jenkins-cnsa2-pkix-profile-07** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificates and Certificate Revocation Lists](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-pkix-profile/) — This document specifies a profile of X.509 v3 Certificates and X.509
   v2 Certificate Revocation Lists for applications that use Commercial
   National Security Algorithm Suite published by the United States
   Government.

   The profile applies to the capabilities, configuration, and operation
   of all components of US National Security Systems that employ such
   X.509 certificates.  US National Security Systems are described in
   NIST Special Publication 800-59.  It is also appropriate for all
   other US Government systems that process high-value information.

   This memo is not an IETF standard, and does not represent IETF
   community consensus.  The profile is made publicly available for use
   by developers and operators of these and any other system
   deployments.  This document obsoletes [RFC8603], the CNSA 1.0
   guidance.
- **draft-jennings-moq-log-04** (new-draft, score 0, ignored_after_review) [none]: [Logging over Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-log/) — Real time systems often run into the problems where the network
   bandwidth for logging is shared with the real time media and impacts
   the media quality.  There is a desire to transport the logging data
   at an appropriate priority level over the same transport as the
   media.  This allows the logging data to take advantage of times when
   the media bitrate is below the peak rate while not impacting the peak
   rate available for media.

   This document specifies how to send syslog [RFC5424] type information
   over Media over QUIC Transport (MOQT) [MOQT].
- **draft-jennings-moq-metrics-03** (new-draft, score 0, ignored_after_review) [none]: [Metrics over MOQT](https://datatracker.ietf.org/doc/draft-jennings-moq-metrics/) — Many systems produce significant volumes of metrics which either are
   not all needed at the same time for consumption by collection/
   aggregation endpoints or may also compete for bandwidth with the
   primary application, thus exacerbating congestion conditions
   especially in low-bandwidth networks.  Delivering these over
   architectures enabled by publish/subscribe transport like Media over
   QUIC Transport (MOQT) [MOQT], allows metrics data to be prioritized
   within the congestion context of the primary application as well as
   enabling local nodes to cache the metric value to be later retrieved
   via new subscriptions.

   This document specifies how to send metrics type information over
   MOQT.
- **draft-jennings-moq-uri-01** (new-draft, score 0, ignored_after_review) [none]: [MOQT URI and Discovery](https://datatracker.ietf.org/doc/draft-jennings-moq-uri/) — This document defines the moqt URI scheme, URI resolution mechanisms,
   and discovery methods for the Media over QUIC Transport (MOQT)
   protocol.  It specifies the URI syntax, fragment identifiers,
   dereferencing procedures, normalization rules, and X.509 certificate
   matching for moqt URIs.  It also defines DNS-based resolution using
   SVCB and SRV records, as well as local network discovery via mDNS and
   DNS-SD.
- **draft-jimenez-core-coap-diag-01** (new-draft, score 0, ignored_after_review) [none]: [CoAP Diagnostic Message Notation](https://datatracker.ietf.org/doc/draft-jimenez-core-coap-diag/) — This document defines a text notation for representing Constrained
   Application Protocol (CoAP) request/response exchanges in Internet-
   Drafts and RFCs.  The notation balances human readability with
   mechanical validation: a reader can follow an exchange at a glance,
   and tooling can be built to parse the message structure and check
   each payload against its declared content format.  The notation is
   application-layer by default, with message-layer detail added only
   where an example depends on it.  It is a recommended convention for
   use in documents and with authoring tools such as kramdown-rfc, not a
   conformance target; it does not change CoAP or any on-the-wire
   encoding.
- **draft-jimenez-core-coap-no-content-00** (new-draft, score 0, ignored_after_review) [none]: [The 2.06 (No Content) Response Code for the Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/draft-jimenez-core-coap-no-content/) — This document defines the 2.06 (No Content) response code for the
   Constrained Application Protocol (CoAP).  The code indicates that the
   target resource exists but has no current representation to transfer.
   It allows a client to retrieve or observe a resource before that
   resource has any content, without the server signaling an error.
   This document updates RFC 7641 to allow 2.06 (No Content)
   notifications, and specifies how cross-proxies map the code to and
   from the HTTP 204 (No Content) status code.
- **draft-johani-dnsop-transport-signaling-03** (new-draft, score 0, ignored_after_review) [none]: [Opportunistic Operator based SVCB transport signaling (OOTS)](https://datatracker.ietf.org/doc/draft-johani-dnsop-transport-signaling/) — This document proposes an Opportunistic Operator Transport Signaling
   mechanism (OOTS) based on SVCB records, to enable operators of
   authoritative DNS servers to signal their support for alternative
   transport protocols (e.g., DNS over TLS (DoT) and DNS over QUIC
   (DoQ)).  These SVCB records can contain a new (experimental) SVCB
   "oots" key which contains fine grained information about the support
   for specific transports.

   Recursive resolvers can obtain these records either by requesting
   they be included in the Additional section of authoritative DNS
   responses (Passive mode) or by direct DNS queries (Probe mode).
   Resolvers can then Opportunistically upgrade connections to the
   authoritative to encrypted transports according to local policy,
   thereby improving privacy, security, and performance for subsequent
   interactions.
- **draft-josefsson-rfc4648bis-02** (new-draft, score 0, ignored_after_review) [none]: [The Base16, Base32, and Base64 Data Encodings](https://datatracker.ietf.org/doc/draft-josefsson-rfc4648bis/) — This document describes the commonly used base 64, base 32, and base
   16 encoding schemes.  It also discusses the use of line-feeds in
   encoded data, use of padding in encoded data, use of non-alphabet
   characters in encoded data, use of different encoding alphabets, and
   canonical encodings.  This document obsoletes RFC 4648 and changes
   the status to Internet Standard.
- **draft-jot-bess-evpn-mcast-router-sync-01** (new-draft, score 0, ignored_after_review) [none]: [Multicast Router State Synchronization in EVPN Networks](https://datatracker.ietf.org/doc/draft-jot-bess-evpn-mcast-router-sync/) — Ethernet VPN (EVPN) networks support multicast applications in which
   multicast routers and multicast hosts are attached to the same
   tenant.  Existing specifications define how Provider Edge (PE)
   devices synchronize the Internet Group Management Protocol (IGMP) and
   Multicast Listener Discovery (MLD) membership state of multihomed
   multicast hosts, and how Optimized Inter-Subnet Multicast (OISM)
   forwarding interacts with multicast routers via PIM EVPN Gateways.
   However, none of the existing specifications addresses the
   synchronization of the state associated with a multicast router (an
   IGMP/MLD Querier or a Protocol Independent Multicast (PIM) router)
   when that router is multihomed to a set of EVPN PEs.  This document
   specifies a new EVPN route, the Multicast Router Discovery (MRD)
   route, and the procedures to synchronize multicast router state
   across the PEs of an Ethernet Segment, for routers attached to
   multicast Broadcast Domains or to Layer 3 interfaces.
- **draft-kalosha-stb-tls13-01** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-karstens-pim-proxy-query-messages-00** (new-draft, score 0, ignored_after_review) [none]: [Proxy Query Messages](https://datatracker.ietf.org/doc/draft-karstens-pim-proxy-query-messages/) — TODO: provide abstract
- **draft-kazuho-ccwg-cuback-01** (new-draft, score 0, ignored_after_review) [none]: [CUBACK: CUBIC Driven by the ACK Clock](https://datatracker.ietf.org/doc/draft-kazuho-ccwg-cuback/) — This document specifies Cuback, an ACK-driven reformulation of CUBIC
   congestion control.  It simplifies implementation by replacing
   CUBIC's mutable time- and ACK-driven state with pure functions over
   immutable per-epoch parameters, for which test vectors are provided.
   Congestion-window growth uses the same ACK-driven mechanism as Reno,
   removing several sources of implementation error.  When entering a
   high-capacity path, a newcomer converges on its share sooner than
   under CUBIC, so short flows complete earlier.
- **draft-kazuho-quic-delegated-stateless-reset-01** (new-draft, score 0, ignored_after_review) [none]: [Delegating QUIC Stateless Resets](https://datatracker.ietf.org/doc/draft-kazuho-quic-delegated-stateless-reset/) — This document specifies how a QUIC endpoint can delegate sending
   Stateless Resets to a component that outlives its connection state.
   It also defines a frame for clients using zero-length Connection IDs
   to advertise a Stateless Reset Token and a transport parameter for
   servers to indicate support for receiving the frame.
- **draft-kbf-onsen-problem-statement-01** (new-draft, score 0, ignored_after_review) [none]: [ONSEN Problem Statement](https://datatracker.ietf.org/doc/draft-kbf-onsen-problem-statement/) — The IETF has published a number of YANG data models for automating
   the provisioning and delivery of network and connectivity services,
   including the L2SM, L3SM, L2NM, L3NM, Attachment Circuits, and
   Network Slicing models.  These models are intended to provided
   abstracted representations of common operator services, exposing only
   the necessary parameters for configuring and managing services.
   These abstractions help to contain the complexity of service
   provisioning within the necessary domains, making the implementation
   of complex, multi-domain services easier to implement and manage.

   However, operators have reported persistent challenges in
   operationalizing these abstractions in a consistent, scalable, and
   automatable manner.  This document describes the problem space for
   the ONSEN Working Group, identifying the operational gaps and
   deficiencies in existing IETF service and network abstraction models
   that complicate, or prevent effective end-to-end automation.  The
   problems documented here are initially drawn from operator
   experience, and from the findings of the IAB NEMOPS Workshop.

   It is a living draft, not intended for publication as an RFC, and
   will be updated with new problem descriptions as the ONSEN work
   proceeds.  This document does not propose solutions, protocols, or
   new data models.
- **draft-kbr-teas-mptersvp-06** (new-draft, score 0, ignored_after_review) [none]: [RSVP-TE Extensions for Multipath Traffic Engineered Directed Acyclic Graph Tunnels](https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that facilitates weighted
   load balancing of unicast traffic across a constrained set of paths
   optimized for a specific objective.

   This document describes the provisioning of an MPTED tunnel in a TE
   network using RSVP-TE.
- **draft-kejriwal-scone-scone-qlog-01** (new-draft, score 0, ignored_after_review) [none]: [QUIC Logging for the SCONE Protocol](https://datatracker.ietf.org/doc/draft-kejriwal-scone-scone-qlog/) — This document defines qlog events for the Standard Communication with
   Network Elements (SCONE) protocol.  The events record the sending and
   reception of SCONE packets and changes to throughput advice.
- **draft-kompella-detnet-mrte-00** (new-draft, score 0, ignored_after_review) [none]: [MRTE: Multipath Traffic Engineering for Reliable and Available Wireless DetNet](https://datatracker.ietf.org/doc/draft-kompella-detnet-mrte/) — Reliable and Available Wireless (RAW) extends Deterministic
   Networking (DetNet) to networks in which some or all of the links are
   wireless.  Wireless links differ from wired links in that their
   quality varies over short time scales, so a path that was good a
   moment ago may be unusable now.  The RAW Architecture addresses this
   with a "recovery graph", equivalent to a 6TiSCH "Track": not a single
   path, but a Directed Acyclic Graph (DAG) of paths from an ingress to
   an egress, over which packets are replicated, and duplicates
   eliminated where the paths converge, so that a packet is delivered as
   long as at least one path through the graph is working.

   Multipath Traffic Engineering (MPTE) introduces two notions that are
   directly applicable to RAW: a traffic-engineered DAG (an MPTE DAG)
   from one or more ingresses to one or more egresses, and a "junction",
   a node of the DAG that is told, by direct signaling, its previous
   hops and next hops and what to do with traffic between them.
   Multicast Traffic Engineering (MCTE) uses the same notions to build
   multicast trees, in which a junction replicates traffic to all of its
   next hops.

   This memo defines MRTE, which applies these notions to RAW.  MRTE
   introduces three new types of junction: a bounded replication
   junction (henceforth called a replication junction), which replicates
   a packet to a subset of its next hops; an elimination junction, which
   may receive copies of a packet from several previous hops and
   forwards only the first; and an ordering junction, which restores the
   sequence of packets in a flow.  An MRTE DAG interleaves replication
   and elimination junctions so that the number of copies in flight
   stays bounded while the probability of delivery stays high.  This
   memo describes MRTE DAGs and junctions, the tunnel types suitable for
   them, and the information that must be signaled to each junction.
- **draft-koo-dtn-traceroute-eb-03** (new-draft, score 0, ignored_after_review) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block (TREB) for Bundle
   Protocol Version 7 (BPv7).  Each participating node along a bundle's
   path appends a hop-record containing its Node ID, the node it
   received the bundle from, the next hop it selected, the time of the
   recorded event, and link characteristics.  The same block, copied
   into bundle status reports, returns traceroute data to the source.
   The mechanism is opt-in and intended for designated diagnostic
   bundles on scheduled, bandwidth-constrained paths.  Each forwarding
   report returns one hop-record, and the delivery report returns the
   full recorded path and also records its own return path, giving a
   round-trip trace.  Status report generation remains governed by RFC
   9171.
- **draft-krierhorn-idr-upa-05** (new-draft, score 0, ignored_after_review) [none]: [BGP Unreachable Prefix Announcement (UPA)](https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/) — Summarization is often used in multi-domain networks to improve
   network efficiency and scalability.  With summarization in place,
   there is a need to signal loss of reachability to an individual
   prefix covered by the summary.  This enables fast convergence by
   steering traffic away from the node which owns the prefix and is no
   longer reachable.

   This document specifies the mechanism, referred to as Unreachable
   Prefix Announcement (UPA), for networks where BGP is used to carry
   summary routes.  It is also equally beneficial for operators to share
   the unreachable prefixes.
- **draft-kt-dmm-bgpmup-over-6gup-00** (new-draft, score 0, ignored_after_review) [none]: [BGP MUP over 6G UP Architecture](https://datatracker.ietf.org/doc/draft-kt-dmm-bgpmup-over-6gup/) — Evolution of the 6G user plane toward distributed Serving and Anchor
   User Plane Functions (S-UPFs and A-UPFs) offers an opportunity to
   coordinate mobility, IP transport, and application/AI-compute
   placement.  This document explores an architecture in which a Mobile
   User Plane Controller (MUP-C) translates authorized mobile-session
   information and transport-aware steering decisions into BGP Mobile
   User Plane (MUP) routing information.  It describes interworking with
   the BGP MUP SAFI, access and data-network segments, SRv6 forwarding,
   mobility, and user-plane accounting.  The architecture is transport-
   neutral; SRv6 is an illustrative data plane.  The proposed
   application-to-session binding and 6G procedures are for discussion
   and do not define new BGP encodings or change 3GPP procedures.
- **draft-laxsharma-pact-03** (new-draft, score 0, ignored_after_review) [none]: [PACT: Co-Signed Task Contracts, Delivery and Verdict Records, and Outcome Records for Autonomous Agents](https://datatracker.ietf.org/doc/draft-laxsharma-pact/) — Autonomous agents can already prove who they are, show whose
   authority they act under, find and call one another, and pay.  What
   no existing specification lets them do is agree on a task in a form a
   third party can check, deliver against it, have the delivery judged
   by someone other than the performer, and carry away a record of the
   outcome that a stranger can verify.  This document specifies PACT, a
   set of signed JSON records that closes that gap.

   PACT defines four things: a co-signed task contract whose digest
   covers its signature set; a Verdict record bound by digest to the
   Delivery it judges; a Facilitator-signed event trace and Outcome
   Record for every contract, recorded once, in one order, by a party
   other than the performer; and a Merkle commitment from a parent's
   Outcome Record to its subcontracts' Outcome Records.

   Settlement terms are carried by reference to a profile defined
   outside this document.  This document specifies no escrow, custody or
   release of value, and takes no position on the legal effect of any
   record it defines.
- **draft-lcnc-onsen-telco-cloud-01** (new-draft, score 0, ignored_after_review) [none]: [Abstractions for Telco-Cloud Scenarios](https://datatracker.ietf.org/doc/draft-lcnc-onsen-telco-cloud/) — draft-lcnc-onsen-telco-cloud-01

Abstract

   Cloud infrastructures are becoming increasingly distributed, spanning
   centralized facilities and distributed edge sites, all of them
   interconnected through networks from one or more administrative
   domains.  Services running on top of such computing enironments
   require dynamic placement, admission control, lifecycle management,
   and coordinated scaling across sites, requiring proper allocation and
   operation of both compute and network resources in order to preserve
   the required expectations from customers and providers.  Existing
   orchestration systems often depend on fragmented visibility of
   infrastructure resources (in both compute and network domains) and
   must interact with multiple management systems before determining
   service feasibility.

   This document discusses the role of network abstractions in Telco-
   Cloud environments benefiting the interplay and operation of cloud
   and network domains, building up a truly operational Telco-Cloud
   approach.  It identifies abstraction dimensions that can simplify
   service orchestration while enabling scalable operation across
   heterogeneous network and cloud infrastructures.
- **draft-lee-space-ipv6-satellite-networks-00** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Wireless Access in Satellite Networks (IPWASN): Problem Statement and Use Cases](https://datatracker.ietf.org/doc/draft-lee-space-ipv6-satellite-networks/) — This document describes a problem statement and use cases for IPv6
   Wireless Access in Satellite Networks (IPWASN).  IPWASN aims at the
   IPv6-based wireless access in Non-Terrestrial Networks (NTNs), that
   is, satellite networks.  It considers NTN characteristics such as
   dynamic topology, multi-hop communication over inter-satellite links,
   High-Altitude Platform Station (HAPS)-assisted relay paths, frequent
   handovers, variable link quality, and intermittent connectivity.
   Based on these characteristics, this document identifies key
   challenges in applying existing IPv6 protocols to NTN environments.
   It also analyzes the applicability of current IPv6 mechanisms and
   outlines requirements to support efficient data forwarding, Quality
   of Service (QoS), Segment Routing (SR)-based traffic engineering, and
   connectivity in satellite-based networks.
- **draft-lenders-core-oblivious-coap-01** (new-draft, score 0, ignored_after_review) [none]: [Oblivious CoAP](https://datatracker.ietf.org/doc/draft-lenders-core-oblivious-coap/) — In the Constrained Application Protocol (CoAP), protected requests
   allow the server to identify the client, also across different and
   unrelated data exchanges.  This document defines Oblivious CoAP,
   which enables oblivious protected exchanges of CoAP messages for use
   cases where the identification of the client at the server is not
   desirable.
- **draft-lenders-dns-cbor-19** (new-draft, score 0, ignored_after_review) [none]: [A Concise Binary Object Representation (CBOR) of DNS Messages](https://datatracker.ietf.org/doc/draft-lenders-dns-cbor/) — This document specifies a compact data format for DNS messages using
   the Concise Binary Object Representation [RFC8949].  The primary
   purpose is to keep DNS messages small in constrained networks.
- **draft-li-idr-bgp-sr-policy-bfd-extension-03** (new-draft, score 0, ignored_after_review) [none]: [BGP SR Policy Extensions for BFD Configuration](https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/) — Segment Routing (SR) Policies require fast failure detection for
   Candidate Paths (CPs) to enable rapid rerouting and high
   availability.  Currently, the provisioning of SR Policies and the
   configuration of the associated Seamless Bidirectional Forwarding
   Detection (S-BFD) sessions are performed independently.  This often
   necessitates separate mechanisms (e.g., manual configuration,
   NETCONF, or additional signaling) to associate S-BFD sessions with
   the SR Policies, resulting in complex and error-prone operations.

   This document defines extensions to BGP SR Policy for the
   simultaneous provisioning of SR Policy CPs and their S-BFD
   configuration parameters during policy advertisement.  The extensions
   include optional sub-TLVs within the Tunnel Encapsulation Attribute
   to carry S-BFD configuration parameters (e.g., discriminators,
   intervals, multipliers).

   These extensions simplify deployment in distributed or controller-
   based environments, reduce configuration overhead, and enhance
   operational efficiency for SR-based traffic engineering.
- **draft-li-idr-flowspec-redirect-direct-ip-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification Redirects to Direct IP](https://datatracker.ietf.org/doc/draft-li-idr-flowspec-redirect-direct-ip/) — A bit, D bit, is defined in the Flow-spec Redirect-to-IPv4 Extended
   Community, which is used by BGP Flow Specification to indicate that
   the associated Flow Specification policy be set to an invalid state
   when the directly connected link associated with the redirect target
   address becomes unavailable.
- **draft-li-idr-sr-policy-metric-aware-bgp-bestpath-00** (new-draft, score 0, ignored_after_review) [none]: [SR Policy Metric-Aware BGP Best Path Selection](https://datatracker.ietf.org/doc/draft-li-idr-sr-policy-metric-aware-bgp-bestpath/) — When multiple BGP routes are available for a destination, the
   interior cost used by the BGP best-path selection procedure may not
   reflect the metric of the SR Policy associated with the actual
   forwarding path.  This can result in the selection of a BGP route
   that does not match the intended transport performance.

   This document updates the BGP Phase 2 tie-breaking procedure to
   enable locally configured SR Policy metric-aware best-path selection
   using metrics specified in the BGP SR Policy metric extensions.This
   document replaces [I-D.li-idr-sr-policy-metric], retaining and
   refining its use case and BGP best-path selection enhancements.  The
   BGP SR Policy extensions for carrying SR Policy metrics are merged in
   [I-D.ietf-idr-sr-policy-metric] .
- **draft-li-inference-transmission-optimization-00** (new-draft, score 0, ignored_after_review) [none]: [Receiver-Driven Credit Control (RDCC) for Many-to-One Traffic in Distributed Inference Networks](https://datatracker.ietf.org/doc/draft-li-inference-transmission-optimization/) — Expert-parallel and disaggregated (prefill/decode) inference
   deployments generate many-to-one ("incast") traffic in which many
   senders transmit to one receiver at the same time.  Mitigations based
   on priority queues, enlarged switch buffers, and disabled Explicit
   Congestion Notification (ECN) marking stop scaling when the
   bandwidth-delay product of the network grows.  This document
   specifies Receiver-Driven Credit Control (RDCC), a UDP-based
   signaling protocol with which a receiver bounds the volume of data
   that all senders may have in flight toward it.  RDCC defines a
   receiver credit budget, a bounded unscheduled first window for short
   messages, cumulative per-message and class-weighted credit grants,
   sender backlog indications with suggested credit rates, and optional
   congestion reports from on-path nodes.  RDCC operates within a
   limited domain, complements the congestion control of the data
   transport, and does not change the format of data packets.
- **draft-li-lsvr-bgp-spf-srv6-08** (new-draft, score 0, ignored_after_review) [none]: [Applying BGP-LS Segment Routing over IPv6(SRv6) Extensions to BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-li-lsvr-bgp-spf-srv6/) — For network scenarios such as Massively Scaled Data Centers (MSDCs),
   BGP is extended for Link-State (LS) distribution and the Shortest
   Path First (SPF) algorithm based calculation.  BGP Link State
   Shortest Path First (BGP-LS-SPF) Routing leverages the mechanisms of
   both BGP protocol and BGP-LS protocol extensions.  Segment Routing
   over IPv6 (SRv6) provides a source routing mechanism that allows a
   flow to be restricted to a specific topological path, while
   maintaining per-flow state only at the ingress node(s) to the SRv6
   domain.  In some networks, it may be useful to enable SRv6-based
   source routing mechanism together with BGP-LS-SPF.  This document
   proposes to introduce the BGP Link-State (BGP-LS) extensions for SRv6
   to the BGP-LS-SPF SAFI to enable SRv6 capabilities in BGP-LS-SPF.
   The usages and formats of these extensions are also provided in this
   document.
- **draft-li-rdma-crem-00** (new-draft, score 0, ignored_after_review) [none]: [Congestion-Aware Reliability Enhancement Mechanism (CREM) for RDMA over IP Networks](https://datatracker.ietf.org/doc/draft-li-rdma-crem/) — RDMA transports designed for lossless data center fabrics perform
   poorly over long-distance, high bandwidth-delay product, or lossy IP
   paths: go-back-N retransmission resends whole windows, selective
   repeat costs at least a round trip per loss, and fixed forward
   erasure correction wastes capacity when the path is clean.  This
   document specifies the Congestion-Aware Reliability Enhancement
   Mechanism (CREM), which protects datagram-based RDMA flows without
   modifying their packets.  CREM adds a UDP-encapsulated repair channel
   on which the sender transmits erasure-coded repair symbols computed
   over blocks of RDMA packets, adapts the redundancy to measured loss
   and to whether losses are caused by congestion, and recovers losses
   that exceed the redundancy with a coded retransmission: a number of
   repair symbols, computed only over the lost packets, that is smaller
   than the number of lost packets.  Per-packet retransmission remains
   as the final fallback.  Optional path reports from on-path nodes,
   derived from Alternate Marking measurements or from the nodes' own
   drops, inform the adaptation.
- **draft-li-rdma-kvcache-transfer-optimization-00** (new-draft, score 0, ignored_after_review) [none]: [Key-Value (KV) Cache Block Transfer Protocol (KBTP) over RDMA: Block Load, Mapped Store, and Unmapped Store](https://datatracker.ietf.org/doc/draft-li-rdma-kvcache-transfer-optimization/) — Inference systems move key-value (KV) cache blocks between instances
   and cache tiers over RDMA.  Existing practice forces a choice between
   statically registered remote memory, which is fast but wastes memory,
   and per-transfer remote procedure calls, which use memory well but
   involve the target's CPU in every transfer.  This document specifies
   the KV Cache Block Transfer Protocol (KBTP), an upper-layer protocol
   over RDMA with three operations: Block Load, which places a stored
   block into the initiator's memory; Block Mapped Store, which writes a
   block into an already allocated block; and Block Unmapped Store,
   which allocates a free block at the target and writes it in one
   operation.  KBTP defines the request and completion messages, a block
   table, and a free-block ring whose counters use masked atomic fetch-
   and-add.  These structures are designed so that a target can execute
   loads and stores within its RDMA network interface, and allocations
   as well where the interface supports conditional execution, without
   involving its CPU per operation, while remaining interoperable with
   targets that process requests in software.  KBTP is bound to RDMAP
   with the RDMA protocol extensions, and can also be used over
   InfiniBand and RoCEv2.
- **draft-liao-ace-est-c509-04** (new-draft, score 0, ignored_after_review) [none]: [EST for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-ace-est-c509/) — This document defines Enrollment over Secure Transport (EST) protocol
   operations over HTTPS and secure CoAP for use with C509 certificates.
   The operations specified in this document support CA certificate
   distribution, C509 certificate enrollment, C509 certificate re-
   enrollment, and server-side key generation using C509 certificates.
   This document also defines operations for server capability
   discovery, Certificate Revocation List (CRL) distribution, and a
   challenge-response proof of possession for KEM-only keys.
- **draft-liao-lamps-est-lightweight-operations-02** (new-draft, score 0, ignored_after_review) [none]: [EST Lightweight Operations](https://datatracker.ietf.org/doc/draft-liao-lamps-est-lightweight-operations/) — This document defines eight new operations for the Enrollment over
   Secure Transport (EST) protocol specified in RFC 7030: ucacaps,
   ucacert, ucacerts, ucrlinfo, ucrl, usimpleenroll, usimplereenroll,
   and userverkeygen.  These operations deliver PKI objects, including
   CA certificates, certificate chains, CRLs, and enrolled certificates,
   as Base64-encoded DER or PEM, without the CMS encapsulation used by
   the corresponding EST operations in RFC 7030.  The ucacaps operation
   enables EST clients to discover which operations the EST server
   supports.  Eliminating the CMS wrapper for these responses reduces
   code size and parsing complexity.
- **draft-lin-grow-bmp-cap-notification-02** (new-draft, score 0, ignored_after_review) [none]: [Peer Capability Update Notification in BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-lin-grow-bmp-cap-notification/) — When BGP Dynamic Capability is supported, dynamic updates of
   capabilities are allowed over an established BGP session.  At
   present, after the BGP session is established, the monitored router
   sends a BMP Peer Up Notification message first, containing the
   initial capabilities.  If BGP Dynamic Capability is supported, using
   BMP Peer Up Notification messages to report subsequent capability
   changes for a BGP session becomes inappropriate.  This document
   defines a new Peer Capability Update Notification message type in BMP
   to report peer capability changes.
- **draft-lin-idr-interface-index-capability-01** (new-draft, score 0, ignored_after_review) [none]: [Interface Index Capability for BGP](https://datatracker.ietf.org/doc/draft-lin-idr-interface-index-capability/) — In some scenarios using unnumbered links, it is necessary for the BGP
   protocol to advertise the link's Interface Index and obtain the
   peer's Remote Interface Index.

   This document defines a new BGP capability, as specified in RFC 5492,
   for advertising local interface indexes and obtaining neighbor
   interface indexes.
- **draft-lin-idr-sr-policy-headend-behavior-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extensions of SR Policy for Headend Behavior](https://datatracker.ietf.org/doc/draft-lin-idr-sr-policy-headend-behavior/) — [RFC8986] defines H. Encaps behavior, H. Encaps.Red behavior, H.
   Encaps.L2 behavior, and H. Encaps.L2.Red behavior for SR policy.
   This document defines extensions to Border Gateway Protocol (BGP) to
   distribute SR policies carrying headend behavior.
- **draft-liu-bpm-measurement-interpretation-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Interpreting IP Performance Measurement Results](https://datatracker.ietf.org/doc/draft-liu-bpm-measurement-interpretation/) — IP Performance Measurement (IPPM) metrics characterize properties
   such as connectivity, packet loss, delay, delay variation, packet
   reordering, packet duplication, and capacity.  A result can be
   correct for the metric and measurement method used while still being
   insufficient to explain the network condition that produced it or to
   describe traffic outside the measured scope.

   This document provides guidance for interpreting IPPM measurement
   results.  It considers the metric definition and parameters, the
   measured packet or traffic population, the observation scope, and the
   measurement method.  It also discusses metric-specific considerations
   and differences among active, passive, and hybrid measurements.
   Operational information can support an interpretation, but this
   document keeps it separate from the metric result itself.

   This document does not define new metrics or measurement protocols,
   and it does not specify a mechanism for determining a unique
   operational cause.
- **draft-liu-fann-wan-flowctrl-detect-00** (new-draft, score 0, ignored_after_review) [none]: [Proactive Flow Control Point Detection in WAN](https://datatracker.ietf.org/doc/draft-liu-fann-wan-flowctrl-detect/) — This document proposes a proactive detection mechanism that enables
   the flow control notification message generating downstream node to
   be aware of the nearest upstream node capable of processing the
   message . The mechanism operates in the data plane, uses probe
   packets that follow the same path as data traffic, and maintains
   state only where needed.  While proposed for flow control, the same
   mechanism may support other fast notification use cases that require
   distributed recipient node discovery.
- **draft-liu-idr-bgp-sr-policy-cp-threshold-03** (new-draft, score 0, ignored_after_review) [none]: [BGP Extension for Distributing CP Threshold Constraints of SR Policy](https://datatracker.ietf.org/doc/draft-liu-idr-bgp-sr-policy-cp-threshold/) — This document defines the extension of BGP to distribute the
   threshold constraint parameters of candidate paths for SR Policy to
   achieve flexible path selection.
- **draft-liu-moq-feedback-01** (new-draft, score 0, ignored_after_review) [none]: [MoQ Feedback](https://datatracker.ietf.org/doc/draft-liu-moq-feedback/) — This document defines Media over QUIC Feedback (MQF), an extension to
   Media over QUIC Transport (MOQT) that enables delivery quality
   information about media Objects to be reported using Feedback Tracks.
   It defines how Feedback Tracks are associated with media Tracks,
   established, forwarded through Relays, and consumed, together with
   the MQF report format and capability negotiation.  MQF complements
   transport-layer signals with per-Object delivery information.
- **draft-liu-opsawg-alt-mark-per-packet-01** (new-draft, score 0, ignored_after_review) [none]: [Alternate marking usage for loss location in per-packet load balancing networks](https://datatracker.ietf.org/doc/draft-liu-opsawg-alt-mark-per-packet/) — Many per-packet load balancing schemes have been proposed to mitigate
   network load imbalances.  However, due to the randomness of packet
   paths, loss location is challenging in per-packet load balancing
   networks.  An efficient solution is to leverage the alternate packet
   marking technique.  This draft analyzes the usage and requirements of
   alternate packet marking for packet loss detection and location in
   per-packet load balancing networks.
- **draft-liu-rtgwg-path-aware-remote-protection-06** (new-draft, score 0, ignored_after_review) [none]: [Path-aware Remote Protection Framework](https://datatracker.ietf.org/doc/draft-liu-rtgwg-path-aware-remote-protection/) — This document describes the framework of path-aware remote
   protection.
- **draft-ll-onsen-soya-00** (new-draft, score 0, ignored_after_review) [none]: [Service Orchestration with YANG-modeled Abstractions Framework](https://datatracker.ietf.org/doc/draft-ll-onsen-soya/) — This document defines the Service Orchestration with YANG-modeled
   Abstractions (SOYA) framework for building layered orchestration
   systems.  Each layer exposes YANG-modeled service intent and
   operational state, and uses business logic to translate intent into
   configuration for the layer below.  The framework describes the
   boundaries between layers, the propagation of configuration and
   state, and the separation of service processing from management
   protocol implementation.  These principles apply to layers hosted
   within one orchestrator or distributed across several orchestrators.
- **draft-loffredo-calext-jscontact-eai-00** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Email Addresses in JSContact](https://datatracker.ietf.org/doc/draft-loffredo-calext-jscontact-eai/) — JSContact defines the EmailAddress object for representing an email
   address, but its address property is restricted to the ASCII syntax
   of an addr-spec in RFC 5322.  This document redefines that property
   to also support internationalized email addresses, as defined in RFC
   6532.  Since such values are incompatible with JSContact version 2.0,
   this document defines JSContact version 3.0.  This document updates
   RFC 9553.
- **draft-lrss-bess-evpn-group-policy-03** (new-draft, score 0, ignored_after_review) [none]: [EVPN Group Policy](https://datatracker.ietf.org/doc/draft-lrss-bess-evpn-group-policy/) — Group Based Policy can be used to achieve micro or macro segmentation
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
- **draft-lz-lsr-isis-qkd-relay-00** (new-draft, score 0, ignored_after_review) [none]: [Extensions to IS-IS for Advertising Quantum Key Distribution (QKD) Relay Information](https://datatracker.ietf.org/doc/draft-lz-lsr-isis-qkd-relay/) — Quantum Key Distribution (QKD) provides a method for generating
   shared symmetric keys between two QKD systems.  Large-scale QKD
   networks commonly use trusted relay nodes to deliver key material
   across multiple QKD links.

   to steer key-relay traffic through a sequence of trusted relay nodes.
   A critical prerequisite for this approach is the ability of
   collecting the QKD capability of the nodes and links in the network.

   This document extends IS-IS by defining a new Application ID for QKD
   relay information within the GENINFO TLV [RFC6823].  This extension
   allows nodes to advertise their QKD relay informations and then
   collected by the QKD controller for QKD relay path calculation.
- **draft-ma-v6ops-srv6-ipv6only-01** (new-draft, score 0, ignored_after_review) [none]: [SRv6 Based IPv6 Only Deployment Considerations](https://datatracker.ietf.org/doc/draft-ma-v6ops-srv6-ipv6only/) — This document describes considerations for deploying IPv6-only
   networks based on SRv6 encapsulation in metro and backbone
   networks. It presents several deployment scenarios, including
   fixed broadband internet access, high-value leased-line services,
   and traffic steering to data center resource pools, and provides
   operational guidance derived from production network pilots.
- **draft-mahy-mimi-av-metadata-02** (new-draft, score 0, ignored_after_review) [none]: [Audio, Video, and Image Metadata extensions for the More Instant Messaging Interoperability (MIMI) Content format](https://datatracker.ietf.org/doc/draft-mahy-mimi-av-metadata/) — The More Instant Messaging Interoperability (MIMI) content format is
   a container for rich content, which can reference image, video, and
   audio files.  This document describes metadata for these files to
   allow for more pleasant rendering.
- **draft-mahy-mimi-message-status-02** (new-draft, score 0, ignored_after_review) [none]: [A Message Status format for the More Instant Messaging Interoperability (MIMI) content format](https://datatracker.ietf.org/doc/draft-mahy-mimi-message-status/) — The More Instant Messaging Interoperability (MIMI) content format
   describes a message format for instant messaging.  This specification
   defines a concise, efficient format for communicating status of
   messages sent using MIMI content.
- **draft-mahy-mimi-msgid-aad-03** (new-draft, score 0, ignored_after_review) [none]: [Conveying the More Instant Messaging Interoperability Message ID in Messaging Layer Security Additional Authenticated Data](https://datatracker.ietf.org/doc/draft-mahy-mimi-msgid-aad/) — The More Instant Messaging Interoperability (MIMI) content format
   defines a MIMI Message ID, communicated only to members of the
   Messaging Layer Security (MLS) group in which the message was sent.
   This document defines a way to share a Message ID in the MLS
   Additional Authenticated Data (AAD) so it is visible to MIMI
   providers.
- **draft-mahy-mls-ext-commit-pp-02** (new-draft, score 0, ignored_after_review) [none]: [Including Pending Proposals in External Commits in the Messaging Layer Security protocol](https://datatracker.ietf.org/doc/draft-mahy-mls-ext-commit-pp/) — The Messaging Layer Security (MLS) protocol allows authorized non-
   members to join a group via external commits, however it disallows
   most pending proposals in those commits, which causes unfortunate
   side effects.  This document describes an MLS extension to include
   pending proposal in external commits when the extension is present in
   a group.
- **draft-mahy-mls-new-content-types-02** (new-draft, score 0, ignored_after_review) [none]: [New Content Types for Messaging Layer Security (MLS)](https://datatracker.ietf.org/doc/draft-mahy-mls-new-content-types/) — This Messaging Layer Security (MLS) extension adds two new variations
   of the application content type, each with a separate key ratchet.
   It also creates an MLS capability to negotiate use of the new types,
   and an IANA registry to register additional content types.
- **draft-mahy-mls-new-framed-content-tbs-02** (new-draft, score 0, ignored_after_review) [none]: [A more efficient FramedContentTBS structure in Messsaging Layer Security (MLS)](https://datatracker.ietf.org/doc/draft-mahy-mls-new-framed-content-tbs/) — Most MLS signatures are signed over the relatively large GroupContext
   structure.  This document defines a way to safely sign using a pre-
   hashed version of the GroupContext structure for better efficiency.
- **draft-mahy-mls-private-external-02** (new-draft, score 0, ignored_after_review) [none]: [Private External Message extensions for Messaging Layer Security (MLS)](https://datatracker.ietf.org/doc/draft-mahy-mls-private-external/) — MLS groups that use private handshakes lose member privacy when
   sending external proposals.  This document addresses this shortcoming
   by encrypting external proposals using an HPKE public key derived
   from the epoch secret.  It also provides a mechanism to share this
   key and protect it from tampering by a malicious intermediary.
- **draft-mahy-mls-semiprivatemessage-08** (new-draft, score 0, ignored_after_review) [none]: [Semi-Private Messages in the Messaging Layer Security (MLS) Protocol](https://datatracker.ietf.org/doc/draft-mahy-mls-semiprivatemessage/) — This document defines a SemiPrivateMessage for the Messaging Layer
   Security (MLS) protocol.  It allows members to share otherwise
   private commits and proposals with a designated list of external
   receivers rather than send these handshakes in a PublicMessage.
- **draft-many-tiptop-dns-03** (new-draft, score 0, ignored_after_review) [none]: [Deployment and Use of the Domain Name System(DNS) in Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-dns/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  This document lists operational
   methods to enable local DNS name resolving on celestial body networks
   such that there are no real-time query and response flow to name
   servers on (Earth) Internet.
- **draft-many-tiptop-ntp-profile-00** (new-draft, score 0, ignored_after_review) [none]: [NTP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-ntp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an NTP profile
   for deep space.  NTP on-wire protocol is indifferent to path delays
   and transfers time in a single round trip at any distance, but
   diverges if delays in each direction is different.  Some algorithmic
   constants and defaults such as distance threshold, dispersion bounds,
   poll intervals and burst modes, need to be tailored to the deep space
   scenario.  The use of secured NTP is also discussed.
- **draft-marzot-moq-test-tracks-00** (new-draft, score 0, ignored_after_review) [none]: [MOQT Media Test Tracks](https://datatracker.ietf.org/doc/draft-marzot-moq-test-tracks/) — This document specifies moq-test-tracks, a protocol for testing Media
   over QUIC (MOQ) media implementations.  Like moq-test, it carries its
   parameters to the publisher in the Track Namespace.  The parameters
   describe a set of media tracks, including the catalog, packaging,
   codecs and delivery, so that any publisher that implements the
   protocol can generate media of the requested shape.
- **draft-matsushima-dmm-mup-why-01** (new-draft, score 0, ignored_after_review) [none]: [Why the Mobile User Plane Is the Way It Is](https://datatracker.ietf.org/doc/draft-matsushima-dmm-mup-why/) — The Mobile User Plane (MUP) architecture transforms session
   information from a mobile service system into routing information, so
   that ordinary routing nodes can take on the roles of user plane
   anchors and intermediate points.  The architecture document that
   defines MUP is a normative text: it defines concepts, route types,
   and resolution procedures, but it does not explain why they are the
   way they are.  This companion reader supplies that "why", outside the
   normative text.

   The technical content follows one worked example end to end, with
   concrete prefixes, SIDs, and tunnel endpoint identifiers, and follows
   the architecture document throughout.  The explanations are organized
   around a small set of shapes that recur in the design: places
   deliberately left undecided, meaning that arises only when two pieces
   of information meet, and a strict separation between a name and the
   thing it points at.  The Introduction gives these shapes a name
   borrowed from Zen, once, and then lets them do their work quietly.

   This document is not normative.  It defines no protocol and no
   encoding.
- **draft-mauch-bgp-nh-mtu-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Next Hop MTU Attribute](https://datatracker.ietf.org/doc/draft-mauch-bgp-nh-mtu/) — This document defines NEXT_HOP_MTU, an optional non-transitive BGP
   path attribute (type code TBD).  It carries the IP MTU a speaker
   promises is acceptable for an NLRI across one network boundary.  The
   speaker that receives the NLRI across that boundary may attach the
   attribute from the boundary interface MTU and advertise it on
   internal and external sessions.  The intent is to communicate network
   MTU capability so that devices can use that information to improve
   the efficiency of their communications.
- **draft-mazilu-tcpm-packet-trimming-01** (new-draft, score 0, ignored_after_review) [none]: [TCP Packet Trimming Extension](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) — This document specifies a TCP extension that enables TCP endpoints in
   data center networks or similarly controlled administrative domains
   to use packet trimming information when it is available.  When switch
   buffers exceed a threshold, rather than silently dropping a packet,
   the switch trims the payload and forwards the header.  This allows
   the destination to issue a deterministic Negative Acknowledgment
   (NACK), enabling faster, more deterministic loss recovery.
- **draft-meunier-bcp-civil-00** (new-draft, score 0, ignored_after_review) [none]: [Principles for Web Traffic Management by Intermediaries](https://datatracker.ietf.org/doc/draft-meunier-bcp-civil/) — This document describes principles for web intermediaries that
   balance security needs with open web accessibility.

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at
   https://thibmeu.github.io/draft-bcp-civil/draft-meunier-bcp-
   civil.html.  Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-meunier-bcp-civil/.

   Source for this draft and an issue tracker can be found at
   https://github.com/thibmeu/draft-bcp-civil.
- **draft-miao-rtgwg-satellite-routing-reqs-01** (new-draft, score 0, ignored_after_review) [none]: [Scenarios and Routing Requirements for Mega-Constellation LEO Satellite Networks](https://datatracker.ietf.org/doc/draft-miao-rtgwg-satellite-routing-reqs/) — Large-scale Low Earth Orbit (LEO) satellite constellations equipped
   with optical Inter-Satellite Links (ISLs) are evolving toward multi-
   hop spaceborne transport networks.  Multi-vendor constellation
   deployments, interconnection with terrestrial networks, and potential
   interconnection among heterogeneous satellite systems introduce
   requirements for interoperable routing behavior and reachability
   exchange.  At the same time, large constellation size, time-varying
   topology, unplanned link disruptions, and constrained on-board
   resources raise scalability and stability challenges for routing
   mechanisms.

   This document describes representative deployment and
   interoperability scenarios, examines the limitations of network-wide
   fine-grained link-state distribution and existing mitigation
   approaches, and identifies routing requirements for scalable state
   management, topology-change handling, fast recovery, and inter-
   network reachability.
- **draft-miao-teas-6g-fine-grained-qos-gap-analysis-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement and Gap Analysis of Fine-Grained QoS Assurance for 6G Scenarios](https://datatracker.ietf.org/doc/draft-miao-teas-6g-fine-grained-qos-gap-analysis/) — The evolution toward 6G introduces demanding applications such as
   holographic communications, tactile internet, digital twins, and
   semantic communications, which may require fine-grained, per-packet
   Quality of Service (QoS) assurance.  In these scenarios, 5QI may
   continue to be useful, but it may also need to be complemented by
   richer service QoS requirement information.  Meanwhile, transport
   networks have developed powerful QoS technologies including FlexE
   hard slicing, Deterministic Networking (DetNet), Time-Sensitive
   Networking (TSN), and SRv6 Traffic Engineering policies, enabling
   per-packet scheduling precision at microsecond levels.  However,
   several gaps remain.  First, while 6G scenarios may require richer
   service QoS requirement information, current IP transport networks
   still rely on DSCP as the QoS handling mechanism.  This could
   underutilize many effective fine-grained QoS assurance mechanisms
   already available in transport networks.  Second, transport networks
   lack service-aware perception of upper-layer application attributes.
   Third, there is no cross-domain information synchronization mechanism
   between radio access and transport segments, preventing the formation
   of an end-to-end, full-link QoS assurance mechanism for 6G.  This
   document provides a gap analysis structured around three core gaps:
   (1) the potential need to complement 5QI with richer service QoS
   requirement information for 6G and the potential underutilization of
   fine-grained transport QoS mechanisms due to continued reliance on
   DSCP in IP transport; (2) lack of service awareness in transport; and
   (3) missing cross-domain information exchange for end-to-end 6G full-
   link QoS assurance.
- **draft-mimi-content-more-extensions-01** (new-draft, score 0, ignored_after_review) [none]: [Additional Extensions for the More Instant Messaging Interoperablility (MIMI) Content Format](https://datatracker.ietf.org/doc/draft-mimi-content-more-extensions/) — This document defines some new useful extensions for the MIMI content
   format.
- **draft-mitchell-intarea-rfc5837bis-02** (new-draft, score 0, ignored_after_review) [none]: [Extending ICMP for Interface and Next-Hop Identification](https://datatracker.ietf.org/doc/draft-mitchell-intarea-rfc5837bis/) — This memo defines data structures that can be appended to selected
   ICMP messages.  The ICMP extensions defined herein can be used to
   identify any combination of the following: the IP interface upon
   which a datagram arrived, the sub-IP component of an IP interface
   upon which a datagram arrived, the IP interface through which the
   datagram would have been forwarded had it been forwardable, the sub-
   IP component of an IP interface through which the datagram would have
   been forwarded had it been forwardable, and the IP next hop to which
   the datagram would have been forwarded.

   Devices can use this ICMP extension to identify interfaces and their
   components by any combination of the following: ifIndex, IPv4
   address, IPv6 address, name, and MTU.  ICMP-aware devices can use
   these extensions to identify both numbered and unnumbered interfaces.

   This document obsoletes RFC 5837.  To preserve strict backward
   compatibility with legacy implementations, it preserves the original
   Interface Information Object (Class-Num 2) as defined in RFC 5837,
   and introduces a new Extended Interface Information Object to
   accommodate new interface roles.
- **draft-miyatoch-teas-actn-inter-operator-extension-01** (new-draft, score 0, ignored_after_review) [none]: [ACTN Extensions for Inter-Operator Coordination](https://datatracker.ietf.org/doc/draft-miyatoch-teas-actn-inter-operator-extension/) — This document specifies an extension to the ACTN framework (RFC 8453)
   that enables coordination between the MDSCs of different operators,
   so that they can establish and operate end-to-end TE services
   cooperatively while each operator keeps full control of its own
   network and keeps its internal details private.

   As its concrete realization within ACTN, the extension defines the
   MDSC-MDSC Interface (MMI), a symmetric peer interface between the
   MDSCs of different operators, in which neither MDSC has authority
   over the other, and which complements rather than modifies the CMI
   and the MPI.

   The extension is independent of the underlying switching technology
   and applies to packet, optical, and multi-layer TE networks.
- **draft-nandakumar-moq-lb-00** (new-draft, score 0, ignored_after_review) [none]: [MoQ Load Balancer Architecture](https://datatracker.ietf.org/doc/draft-nandakumar-moq-lb/) — This document describes an architecture for load balancing Media Over
   QUIC Transport (MOQT) requests across a pool of MOQT relays.  It
   introduces a MOQT-aware Load Balancer (MoQ-LB) that places requests
   on relays according to their Track Namespace, and describes the
   control-plane, state, and failure-handling requirements needed for a
   horizontally scaled deployment.
- **draft-nandakumar-moq-mix-00** (new-draft, score 0, ignored_after_review) [none]: [MoQ Interconnect Exchange (MIX)](https://datatracker.ietf.org/doc/draft-nandakumar-moq-mix/) — This document specifies MoQ Interconnect Exchange (MIX), a protocol
   that allows Media Over QUIC (MoQ) relays to discover each other,
   exchange reachability and subscription information, and forward MoQ
   objects across administrative and topological boundaries.  MIX
   carries its control state as MoQ tracks.

   This work is outside the scope of the IETF Media Over QUIC (MoQ)
   working group.  It is discussed on that working group's mailing list,
   moq@ietf.org, because that is where the people interested in MoQ
   relay interconnection are.
- **draft-petra-green-api-05** (new-draft, score 0, ignored_after_review) [none]: [Path Energy Traffic Ratio API (PETRA)](https://datatracker.ietf.org/doc/draft-petra-green-api/) — This document describes an API to query a network regarding its
   Energy Traffic Ratio for a given path.
- **draft-pjs-6lo-can-00** (new-draft, score 0, ignored_after_review) [none]: [Transmission of IPv6 Packets over Controller Area Network](https://datatracker.ietf.org/doc/draft-pjs-6lo-can/) — Controller Area Network (CAN) is a fieldbus initially designed for
   automotive applications.  It has since been adopted for use in
   various industrial applications, such as CANopen and building
   automation systems.  CAN operates as a multi-master bus with frame
   identifiers of 11 bits or 29 bits.  The CAN standard, defined in the
   ISO 11898 series, specifies both the physical and data-link layers.
   This document describes how to transfer IPv6 packets over CAN using
   ISO-TP, a dedicated addressing scheme for CAN nodes, and IP header
   compression (IPHC).
- **draft-pmohapat-nvo3-gnserv-00** (new-draft, score 0, ignored_after_review) [none]: [Geneve network service interfaces option class](https://datatracker.ietf.org/doc/draft-pmohapat-nvo3-gnserv/) — This specification defines a new Geneve Option Class and a
   registration procedure for corresponding option types that can be
   used for the exchange of metadata between network service domains.
   The metadata enables implementation of coordinated network service
   functionality across domains by carrying extra context.
- **draft-pospichal-idr-bgp-l2-quic-01** (new-draft, score 0, ignored_after_review) [none]: [Border Gateway Protocol over Layer 2 QUIC Transport (BoL2Q)](https://datatracker.ietf.org/doc/draft-pospichal-idr-bgp-l2-quic/) — This document specifies BGP over Layer 2 QUIC (BoL2Q), a transport
   for external and internal BGP sessions between speakers that share an
   Ethernet segment, in which QUIC packets are carried directly in
   Ethernet frames, identified by a dedicated EtherType, without IP or
   UDP headers.  A BoL2Q session has no IP address and no transport
   port, so it cannot be reached from beyond the Layer 2 segment on
   which it runs, and it requires no IP-layer configuration of any kind:
   a session is defined by a local interface, the MAC address of the
   peer, the remote Autonomous System number and a pre-shared key.
   BoL2Q reuses QUIC version 1 and TLS 1.3 unchanged, apart from the
   replacement of the UDP/IP path by an Ethernet path.  Optionally, a
   "Link Next Hop" capability allows routes to be installed with a
   router on the same Ethernet segment as the next hop, identified
   either as the session peer itself or by its MAC address.  This
   enables forwarding over links that carry no interface addresses,
   including through route reflectors and route servers.
- **draft-pospichal-idr-yang-over-bgp-00** (new-draft, score 0, ignored_after_review) [none]: [YANG over BGP](https://datatracker.ietf.org/doc/draft-pospichal-idr-yang-over-bgp/) — This document defines YANG over BGP (YoBGP), an extension of BGP for
   distributing network configuration objects (for example routing
   policies, prefix sets, community sets, and access control lists)
   modeled in YANG.  Objects are carried in a dedicated Address Family
   (AFI/SAFI) and spread between routers the way routes do: they are
   advertised to peers, carry a version, are filtered on receipt, and
   are optionally re-advertised.  Received objects are subject to a per-
   peer inbound filtering framework, persist in the receiving node's
   configuration independently of the state of the BGP session, and are
   removed only by an explicit, versioned tombstone.  Its goal is
   effortless synchronization of selected configuration settings across
   a large number of BGP speakers.  The framework is schema-agnostic:
   any YANG module, including vendor-specific ones, can be distributed.
- **draft-prabel-cfrg-suf-hybrid-sigs-03** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Digital Signatures with Strong Unforgeability](https://datatracker.ietf.org/doc/draft-prabel-cfrg-suf-hybrid-sigs/) — This document proposes two PQ/T (Post-Quantum/Traditional) hybrid
   signature constructions that achieve strong unforgeability under
   chosen-message attacks (SUF-CMA).  The first, a black-box
   construction, achieves SUF-CMA security provided that the second
   component (typically the post-quantum one) is SUF-CMA secure; it
   differs from the current composite hybrid approach by binding the
   second (post-quantum) signature to the concatenation of the message
   and the first (traditional) signature.  This approach ensures that
   hybrid signatures maintain SUF-CMA security even when the first
   component only provides EUF-CMA security.

   The second, a non-black-box construction, requires the first
   (traditional) component to be built from the Fiat-Shamir paradigm,
   and binds the post-quantum signature directly into that component's
   challenge computation rather than treating it as an opaque sign/
   verify oracle.  This variant is SUF-CMA secure as long as at least
   one of the two components is SUF-CMA secure.
- **draft-prz-lsr-ash-packets-08** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-przygienda-lsr-fast-flooding-rtx-indication-01** (new-draft, score 0, ignored_after_review) [none]: [Retransmission Indication for IS-IS Fast Flooding](https://datatracker.ietf.org/doc/draft-przygienda-lsr-fast-flooding-rtx-indication/) — [RFC9681] defines a Flooding Parameters TLV.  Among other things, it
   lets an IS-IS node advertise two values to a neighbor.  The Receive
   Window (RWIN) bounds the number of unacknowledged Link State PDUs
   (LSPs) the neighbor may have outstanding.  The LSPs-per-PSNP (LPP)
   threshold triggers immediate acknowledgment.  Together they form a
   credit-based flow-control window and an acknowledgment cadence.
   These are the parts of [RFC9681] that are most important, most
   useful, and most likely to be implemented at scale.  The sender-side
   congestion-control algorithms in that document are described only as
   optional, local choices.  No single algorithm is mandatory.

   A credit-based window alone does not signal congestion.  As long as
   acknowledgments keep freeing credit, a sender may keep refilling the
   window up to RWIN.  It does so even while it is actively
   retransmitting LSPs on that adjacency.  Without an explicit,
   normatively specified reaction to observed retransmission, fast
   flooding at scale can degenerate into sustained retransmission storms
   that serve only to keep the window full.

   This document specifies a local backoff.  A node reduces the
   effective outstanding-LSP ceiling it uses against a neighbor's
   advertised RWIN by a meaningful fraction.  The trigger is a count of
   LSP retransmissions generated toward that neighbor within a trailing
   time window exceeding a threshold.  This backoff applies
   unconditionally.  It does not depend on whether the condition is
   signaled to the neighbor, or understood by it.

   This document also defines a lightweight Retransmission (RTX)
   indication.  It is a new flag in the existing Flags sub-TLV of the
   Flooding Parameters TLV.  A node advertises it to a neighbor while it
   is retransmitting LSPs toward that neighbor.  The flag reports only
   the advertising node's own retransmissions, that is, its own
   congestion.  A node never sets it in reaction to a neighbor's flag.
   The flag lets the neighbor adjust its own advertised RWIN in turn.
   The adjacency then converges toward a stable operating point at the
   highest speed it can sustain.  Neither side needs prior knowledge of
   the other's characteristics or of the link.

   This document further clarifies how concurrent versions of the same
   LSP fragment are counted against RWIN, LPP, and the retransmission
   threshold.  [RFC9681] leaves that case undefined, and it arises
   routinely at fast flooding rates.
- **draft-psenak-lsr-igp-dcm-01** (new-draft, score 0, ignored_after_review) [none]: [Distributed Congestion Mitigation](https://datatracker.ietf.org/doc/draft-psenak-lsr-igp-dcm/) — This document describes the Distributed Congestion Mitigation (DCM)
   mechanism using the Interior Gateway Protocols (IGPs) such as IS-IS
   [RFC1195], OSPFv2 [RFC2328], or OSPFv3 [RFC5340].  DCM is a tactical,
   distributed mechanism, designed to mitigate network congestion by
   offloading traffic to an alternate, congestion-free paths.  DCM is
   fully integrated in IGPs.
- **draft-qin-bpm-rpki-rp-bench-00** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for RPKI Relying Party](https://datatracker.ietf.org/doc/draft-qin-bpm-rpki-rp-bench/) — This document defines a benchmarking methodology for evaluating RPKI
   Relying Party (RP) implementations in controlled laboratory
   environments.  The methodology focuses on whether RP implementations
   correctly perform required validation steps and on the performance of
   these operations.  RP implementations are treated as black boxes,
   enabling consistent and objective assessment based on externally
   observable behavior rather than internal design or implementation
   details.
- **draft-rabnag-bess-evpn-anycast-aliasing-06** (new-draft, score 0, ignored_after_review) [none]: [EVPN Anycast Multi-Homing](https://datatracker.ietf.org/doc/draft-rabnag-bess-evpn-anycast-aliasing/) — The current Ethernet Virtual Private Network (EVPN) all-active multi-
   homing procedures in Network Virtualization Over Layer-3 (NVO3)
   networks provide the required Split Horizon filtering, Designated
   Forwarder Election and Aliasing functions that the network needs in
   order to handle the traffic to and from the multi-homed CE in an
   efficient way.  In particular, the Aliasing function supports load
   balancing of unicast traffic from remote Network Virtualization Edge
   (NVE) devices to NVEs that are multi-homed to the same CE, regardless
   of whether the CE’s MAC/IP information has been learned on all those
   NVEs.  This document introduces an optional enhancement to the EVPN
   multi-homing Aliasing function, referred to as EVPN Anycast Multi-
   homing.  This optimization is specific to EVPN deployments over NVO3
   tunnels (i.e., IP-based tunnels) and may offer benefits in typical
   data center designs, which are discussed herein.
- **draft-ramadan-moq-fec-01** (new-draft, score 0, ignored_after_review) [none]: [Forward Error Correction for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec/) — This document specifies a mechanism for transmitting Forward Error
   Correction (FEC) repair data alongside source media in Media over
   QUIC (MoQ) sessions.  It defines catalog-based signaling of FEC
   configuration, including a derived RaptorQ Object Transmission
   Information that needs no in-session messages.  It also defines
   conventions for repair track naming, the format of repair objects,
   and two block profiles that fix how source symbols and FEC blocks are
   formed and identified: an ISO/IEC 23008-1 profile for tracks packaged
   as MPEG Media Transport Protocol (MMTP) packets, and an object
   profile for tracks packaged as Low Overhead Media Container (LOC) or
   Common Media Application Format (CMAF) objects.  It fully specifies
   two FEC schemes: the systematic Reed-Solomon code over GF(2^8) of
   ISO/IEC 23008-10, which is mandatory to implement, and RaptorQ (RFC
   6330), which is optional.  An algorithm registry provides extension
   points for additional schemes.  FEC enables receivers to recover from
   packet loss without retransmission latency.  The MMTP profile is
   designed for compatibility with ATSC 3.0 (A/331) and ARIB STD-B60
   broadcast systems.
- **draft-ramadan-moq-fec-core-00** (new-draft, score 0, ignored_after_review) [none]: [Forward Error Correction for Media over QUIC: Core Mechanism](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec-core/) — This document specifies how Forward Error Correction (FEC) repair
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
   payloads are encrypted end to end.  Relays need no FEC knowledge.
   Specific FEC schemes, catalog bindings, packaging-specific profiles
   and multicast delivery are left to companion documents.
- **draft-ramadan-moq-mmt-02** (new-draft, score 0, ignored_after_review) [none]: [MPEG Media Transport (MMT) Packaging for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-mmt/) — This document specifies the use of MPEG Media Transport (MMT) as a
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
- **draft-rankin-ccsv-03** (new-draft, score 0, ignored_after_review) [none]: [Common Format and Media Type for Control-Character-Separated Values (CCSV) Files](https://datatracker.ietf.org/doc/draft-rankin-ccsv/) — This document specifies the Control-Character-Separated Values (CCSV)
   file format, a UTF-8 encoded tabular data format that uses ASCII
   control characters as field and record separators.  CCSV is intended
   for exchanging structured, rectangular data between applications such
   as databases, spreadsheets, statistical software, and data conversion
   utilities.  This document also specifies the text/csv media type for
   CCSV files.
- **draft-rundgren-cbor-simple-4-csf-02** (new-draft, score 0, ignored_after_review) [none]: [CBOR "simple" values for CSF](https://datatracker.ietf.org/doc/draft-rundgren-cbor-simple-4-csf/) — This document defines two CBOR "simple" values to be used as unique
   (reserved) labels in a CBOR map holding an embedded signature
   construct.
- **draft-sajassi-bess-evpn-subnet-slicing-00** (new-draft, score 0, ignored_after_review) [none]: [EVPN Subnet Slicing](https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-subnet-slicing/) — Ethernet VPN (EVPN) Integrated Routing and Bridging (IRB) distributes
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
- **draft-santesson-r2ps-04** (new-draft, score 0, ignored_after_review) [none]: [Remote Two-factor Protected Services](https://datatracker.ietf.org/doc/draft-santesson-r2ps/) — This document defines a generic service exchange protocol where
   service exchange data is protected and bound to a physical user using
   1 or 2 factors (1FA and 2FA).  The protocol facilitates registration
   and verification of either a knowledge-factor or a biometric factor
   in addition to a possession factor as means of achieving 2 factor
   protection.
- **draft-seemann-quic-nat-traversal-04** (new-draft, score 0, ignored_after_review) [none]: [Using QUIC to traverse NATs](https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/) — This document specifies a QUIC extension for traversing Network
   Address Translators (NATs).  Endpoints use an existing proxied QUIC
   connection to coordinate path validation attempts that create the NAT
   bindings needed for a direct path and test its connectivity.
   Application data can be exchanged over the proxied path while NAT
   traversal is in progress.  Once a suitable direct path has been
   validated, the connection can migrate to it.
- **draft-seemann-tsvwg-udp-fragmentation-03** (new-draft, score 0, ignored_after_review) [none]: [Controlling IP Fragmentation on Common Platforms](https://datatracker.ietf.org/doc/draft-seemann-tsvwg-udp-fragmentation/) — When performing Path MTU Discovery (PMTUD) over UDP, applications
   must prevent fragmentation of UDP datagrams both by the sender's
   kernel and during network transit.  This document provides guidance
   for implementers on configuring socket options to prevent
   fragmentation of IPv4 and IPv6 packets across commonly used
   platforms.
- **draft-sidor-pce-multipath-metric-00** (new-draft, score 0, ignored_after_review) [none]: [Signaling Per-Path Metric in the Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-multipath-metric/) — The Path Computation Element Communication Protocol (PCEP) extensions
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
- **draft-sipos-dtn-bp-safe-02** (new-draft, score 0, ignored_after_review) [none]: [Bundle Protocol (BP) Security Associations with Few Exchanges (SAFE)](https://datatracker.ietf.org/doc/draft-sipos-dtn-bp-safe/) — This document defines a protocol for negotiating scoped security
   associations between Bundle Protocol version 7 (BPv7) agents within a
   delay-tolerant network (DTN).  Security associations are used to
   amortize the costs of asymmetric-keyed security operations and allow
   for efficient and high-throughput BPv7 security within a public key
   infrastructure.  This protocol also provides for unilateral re-keying
   of established security associations in a delay-tolerant manner.
- **draft-smith-idr-rr-deployment-considerations-01** (new-draft, score 0, ignored_after_review) [none]: [BGP RR Deployment Considerations](https://datatracker.ietf.org/doc/draft-smith-idr-rr-deployment-considerations/) — In BGP networks, Route Reflectors (RRs) simplify the provisioning of
   the Internal BGP (IBGP) control plane and mitigate the scaling
   challenges of maintaining a full mesh of IBGP sessions among border
   routers.  Because of these operational benefits, RRs are widely
   deployed in modern networks utilizing BGP.  This document describes
   common RR design options, their associated trade-offs, and deployment
   best practices based on industry operational experience.  Operators
   should consider these suggestions when designing and operating BGP
   networks because BGP control plane stability is essential to overall
   network stability.
- **draft-smjh-teas-dist-bw-mgmt-arch-00** (new-draft, score 0, ignored_after_review) [none]: [An Architecture for Distributed Bandwidth Management Using TE Tunnels and Policies](https://datatracker.ietf.org/doc/draft-smjh-teas-dist-bw-mgmt-arch/) — Traffic Engineering (TE) deployments steer traffic over provisioned
   TE constructs and associate bandwidth with them.  Examples include
   point-to-point and point-to-multipoint (P2MP) Resource Reservation
   Protocol - Traffic Engineering (RSVP-TE) tunnels, Segment Routing
   (SR) Policies, and Multipath TE (MPTE) constructs that are
   provisioned as directed acyclic graphs (DAGs).  As demand changes,
   operators automatically resize the bandwidth allocated to each
   construct based on measured traffic, a function commonly called auto-
   bandwidth, but no common description of this practice exists across
   TE technologies.

   This document defines an architecture for distributed bandwidth
   management, in which the originator of each TE construct evaluates
   and adjusts its bandwidth without central coordination, and can
   offload computation and bandwidth estimation to an external entity.
   The architecture is independent of the forwarding plane and assumes a
   signaling plane, such as RSVP-TE, that provides per-link bandwidth
   accounting, admission control, and preemption.  It covers traffic
   measurement, bandwidth estimation, adjustment, periodic and event-
   driven evaluation, and the management of a service carried by
   multiple concurrently usable tunnels (Container Tunnel management).
   Technology-specific signaling, data models, path computation, and
   estimation algorithms are outside its scope.

   This document defines no new protocol extension or wire encoding.
- **draft-smyslov-ipsecme-ikev2-fragm-large-msg-02** (new-draft, score 0, ignored_after_review) [none]: [Using IKE Fragmentation for Large Messages](https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-fragm-large-msg/) — This document describes issues with using Internet Key Exchange
   version 2 (IKEv2) fragmentation for transmitting large messages on
   unreliable transport.  The document proposes several approaches for
   dealing with these issues: randomizing the order the fragments are
   sent, dispersing sending fragments over time and selective
   retransmission of fragments based on information from the peer about
   their receiption.
- **draft-song-lamps-cms-composite-frodokem-01** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-song-lamps-cms-composite-frodokem/) — This document specifies the conventions for using Composite FrodoKEM
   algorithms with the Cryptographic Message Syntax (CMS).  Composite
   FrodoKEM combines FrodoKEM with traditional algorithms (RSA-OAEP,
   X25519, X448) to provide hybrid post-quantum key encapsulation.
- **draft-song-lamps-pq-composite-frodokem-01** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   X25519, and X448.  This document specifies the algorithm definitions,
   key formats, and certificate conventions for using Composite FrodoKEM
   in the X.509 Public Key Infrastructure.
- **draft-song-satp-implementation-guide-03** (new-draft, score 0, ignored_after_review) [none]: [Secure Asset Transfer Protocol (SATP) Implementation Guide](https://datatracker.ietf.org/doc/draft-song-satp-implementation-guide/) — This document provides non-normative implementation guidance for the
   Secure Asset Transfer Protocol (SATP).  It describes a small,
   independent peer implementation and reproducible tests for evaluating
   protocol behavior and interoperability.  It relates Core processing
   to Setup and Artefacts Registry proposals, while distinguishing
   published requirements from experimental implementation choices.  The
   guide addresses transport mappings, message protection, asset-state
   observation, failure handling, and reporting of specification
   ambiguities.  It does not define a new protocol, certify an
   implementation, or claim completed interoperability experiments.
- **draft-soulard-anima-grasp-router-problem-statement-02** (new-draft, score 0, ignored_after_review) [none]: [GRASP through routers: a Problem Statement](https://datatracker.ietf.org/doc/draft-soulard-anima-grasp-router-problem-statement/) — This document analyzes challenges for using the GeneRic Autonomic
   Signaling Protocol (GRASP) in the context of deployment of services
   on machines (servers, Virtual Machines, etc) without the network
   elements, such as routers, needing any support for GRASP by
   themselves.  It analyses issues regarding the discovery mechanism,
   including discovery across subnets and operation across
   administrative boundaries, and provides terminology and general
   considerations for the development of future extensions, profiles,
   and architectural refinements.
- **draft-spk-httpbis-client-groups-00** (new-draft, score 0, ignored_after_review) [none]: [Client Groups for Shared HTTP Connections](https://datatracker.ietf.org/doc/draft-spk-httpbis-client-groups/) — Intermediaries often carry requests from many unrelated clients over
   one HTTP/2 or HTTP/3 connection to an origin server.  The origin has
   no way to know this, to say whether it accepts it, or to act on the
   traffic of one client without disturbing every other client on the
   connection.  This document defines a pair of settings that let an
   intermediary and an origin agree on whether a connection is shared, a
   request header field that marks which client a request belongs to,
   and a frame that lets the origin drain, block, or limit one client on
   a shared connection.  It also states what an intermediary needs to do
   so that GOAWAY and connection failures reach only the affected client
   streams.
- **draft-sriram-savnet-intrasav-solution-01** (new-draft, score 0, ignored_after_review) [none]: [IntraSAV - A Solution for Intra-Domain Source Address Validation](https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/) — This document specifies a solution, named IntraSAV, for intra-domain
   source address validation (SAV).  This solution addresses the problem
   stated in the ietf-savnet-intra-domain-problem-statement (RFC-to-be)
   document.  This document updates BCP 38 ([RFC2827]) and BCP 84
   ([RFC3704], [RFC8704]) by providing a more comprehensive solution
   methodology and accommodating prefixes that are not routed but used
   for sourcing traffic originating from an AS.
- **draft-svg-tiny-ps-abrotman-13** (new-draft, score 0, ignored_after_review) [none]: [SVG Tiny Portable/Secure](https://datatracker.ietf.org/doc/draft-svg-tiny-ps-abrotman/) — This document specifies SVG Tiny Portable/Secure (SVG Tiny PS) -- A
   Scalable Vector Graphics (SVG) profile to be used with documents that
   are intended for use with more secure requirements, and in some
   cases, in conjunction with a limited rendering engine.
- **draft-taylor-dtn-http-over-bp-00** (new-draft, score 0, ignored_after_review) [none]: [HTTP over the Bundle Protocol](https://datatracker.ietf.org/doc/draft-taylor-dtn-http-over-bp/) — This document specifies a mechanism for carrying HTTP over Bundle
   Protocol Version 7 (BPv7) networks.  Each HTTP request and each HTTP
   response travels as a single bundle, encoded as a Binary HTTP message
   inside a small CBOR envelope that correlates responses with requests.
   Because every bundle carries a complete, self-contained message, the
   mechanism needs none of the reliable, ordered, connection-oriented
   transport services that HTTP otherwise relies on, and it tolerates
   the delay, disruption, reordering, and duplication of a Delay-
   Tolerant Network.  HTTP semantics are unchanged; only the transport
   beneath them is replaced.  The mechanism enables HTTP application-
   layer gateways at the edges of a bundle network, through which
   unmodified HTTP clients and origin servers communicate across it, and
   also lets BP-native applications act as HTTP clients or origin
   servers directly.  The document describes how gateways use HTTP
   caching to remain useful when round trips are long or intermittent,
   and it requests a well-known ipn service number and a registry for
   envelope options.
- **draft-thiruvenkatasamy-evpn-mcast-rpf-prefix-00** (new-draft, score 0, ignored_after_review) [none]: [EVPN Multicast RPF Prefix Advertisement](https://datatracker.ietf.org/doc/draft-thiruvenkatasamy-evpn-mcast-rpf-prefix/) — This document defines a new EVPN route type for advertising multicast
   source-prefix reachability information within an EVPN network.  The
   route enables Reverse Path Forwarding (RPF) resolution for multicast
   traffic independently of the unicast routing topology, addressing the
   operational requirement for non-congruent unicast and multicast
   forwarding paths in tenant multicast deployments.  The proposed route
   type allows an EVPN PE to advertise source-prefix reachability for
   multicast RPF, learned through a multicast-specific routing protocol
   (e.g., BGP using the Multicast Address Family) or configured locally
   through policy or static multicast routes.
- **draft-thomson-httpbis-chic-01** (new-draft, score 0, ignored_after_review) [none]: [Chained Hash Integrity Coding for HTTP](https://datatracker.ietf.org/doc/draft-thomson-httpbis-chic/) — This document defines a content coding for HTTP that provides strong
   integrity protection while maintaining the ability to perform some
   progressive processing.
- **draft-tiloca-core-group-oscore-kem-01** (new-draft, score 0, ignored_after_review) [none]: [Using Quantum-Resistant Key Encapsulation Mechanisms (KEMs) in the Pairwise Mode of Group Object Security for Constrained RESTful Environments (Group OSCORE)](https://datatracker.ietf.org/doc/draft-tiloca-core-group-oscore-kem/) — Group communication for the Constrained Application Protocol (CoAP)
   can be protected end-to-end by using the security protocol Group
   Object Security for Constrained RESTful Environments (Group OSCORE).
   The pairwise mode of Group OSCORE provides authenticated encryption
   of CoAP messages, by means of symmetric keys that two group members
   establish only among themselves to achieve pairwise secure
   communication.  This document defines the use of quantum-resistant
   Key Encapsulation Mechanisms (KEMs) as Pairwise Key Agreement
   Algorithm of Group OSCORE, enabling post-quantum secure derivation of
   the symmetric keys used in the pairwise mode.  The Group Manager
   facilitates the exchange of KEM public keys and encapsulated KEM
   shared secrets among group members.
- **draft-toomim-httpbis-braid-http-05** (new-draft, score 0, ignored_after_review) [none]: [Braid-HTTP: State Synchronization for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-http/) — HTTP transfers the state of a resource once, and leaves programmers
   to keep it up to date as it changes.  Braid-HTTP extends HTTP from
   *transferring* state to *synchronizing* it, with a set of independent
   extensions, each of which addresses a limitation of HTTP on its own.
   When used together, a website can synchronize with any other
   website's state by its URL, just as a page on today's web can link to
   any other page.  This document introduces the extensions, shows how
   they work alone and together, and points to the documents that define
   them.
- **draft-toomim-httpbis-braid-merge-types-00** (new-draft, score 0, ignored_after_review) [none]: [Consistent Merge Types for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-merge-types/) — Merge Types specify how to merge parallel edits to a resource.
   Parallel edits happen when two peers edit the same state over a
   network with latency.  A Merge Type specifies how to merge
   conflicting changes.  If the peers implement and agree upon the same
   Merge Type, then they will reach a consistent state eventually,
   whatever edits they make.

   This document defines Merge Types, the structure of the Merge Type
   system, the Merge-Type header, and IANA registration procedures for
   Merge Types.  Other specifications can define more Merge Types, in
   the registry that this document creates.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-braid-multiresponse-00** (new-draft, score 0, ignored_after_review) [none]: [Multiresponses for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-multiresponse/) — Each HTTP request has only a single response.  This document defines
   the 209 Multiresponse status code, whose content holds several
   responses, and the application/http-history media type, which encodes
   a sequence of responses to one resource over time.  With them, a
   server can send a history of a resource, or a stream of its changes,
   in one response, which caches can store piece by piece.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-braid-poll-and-push-00** (new-draft, score 0, ignored_after_review) [none]: [Poll and Push Modes for HTTP Subscriptions](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-poll-and-push/) — In the stream mode of Braid-HTTP subscriptions, the server holds one
   response open, and sends each change in it.  Some origin servers
   can't hold a response open, such as those that run as serverless
   functions or on shared hosting.  And on some paths, a proxy buffers
   each response until it ends.  This document defines two subscription
   modes in which nothing stays open for long.  In the long-poll mode,
   the client sends a GET for each change, and the server responds to it
   when the change happens.  In the webhook mode, the origin server
   pushes each change to a subscription gateway as a PUT or a DELETE,
   and the gateway serves the subscription to its clients.  In both,
   each message after the first says which version it builds on, and the
   first can too, so no message depends on a connection, and each can
   take its own path.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-braid-subscriptions-caching-00** (new-draft, score 0, ignored_after_review) [none]: [Caching for HTTP Subscriptions](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-subscriptions-caching/) — Without a subscription, a cache can serve a stored response only
   while the response is fresh, and then has to ask the origin server
   whether the resource has changed.  So a cache serves a resource that
   changes often either stale, or with a request to the origin server
   each time.  This document defines how a cache subscribes to the
   resource, as any HTTP client can.  The cache stores each response in
   the subscription as the response to a GET.  While the subscription is
   continuously validating, the cache knows at every moment that its
   copy is current, so it can respond to requests with the copy, without
   asking the origin server, even for responses marked no-cache.  When
   validation stops, the copy ages, and HTTP's rules for stale responses
   apply.

   A cache can also serve many subscribers of its own from one
   subscription to the origin server, and keep private responses
   private.  This document updates RFC 9111, so that a continuously
   validating subscription satisfies the no-cache directive.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-braid-updates-00** (new-draft, score 0, ignored_after_review) [none]: [Replayable Updates for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-updates/) — HTTP provides a suite of requests and responses for communicating
   changes to resource state, but they are limited in symmetry and
   reproducibility.  PATCH is sent client-to-server, but a server cannot
   send a PATCH to a client.  POST can change server state flexibly, but
   its behavior is server-defined, and cannot be reproduced by a naive
   server, client, or intermediary.

   This document extends ordinary HTTP requests and responses into a
   suite of symmetric, reproducible *updates*.  A sequence of updates
   can be replayed on any client, server, or intermediary to reproduce
   identical changes to state.

   There are three types of updates: snapshots, patches, and deletions,
   and this document defines how they occur symmetrically in both
   requests and responses.  Arbitrary patch formats can be defined with
   a new Patch-Type header, but most patches can be expressed as a
   replacement of a range expressed via an extended syntax of Range
   Unit.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-braid-versions-00** (new-draft, score 0, ignored_after_review) [none]: [Resource Versioning for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-braid-versions/) — HTTP resources change over time.  Each change to a resource creates a
   new "version": a new point in time, at which the resource has a new
   state.  HTTP systems often need a way to
   identify, read, write, navigate, and/or merge these versions, in
   order to implement cache consistency, create history archives, settle
   race conditions, request incremental updates to resources, interpret
   incremental updates to versions, or implement distributed
   collaborative editing algorithms.

   This document analyzes existing methods of versioning in HTTP,
   highlights limitations, and specifies a more general versioning
   approach that can enable new use-cases for HTTP.  It also provides an
   upgrade path for legacy intermediaries.

   This document is one of the Braid-HTTP extensions, which work alone
   or together; together they make HTTP a state synchronization
   protocol.
- **draft-toomim-httpbis-simpler-fields-00** (new-draft, score 0, ignored_after_review) [none]: [Simpler Fields for HTTP](https://datatracker.ietf.org/doc/draft-toomim-httpbis-simpler-fields/) — Structured Field Values for HTTP (RFC 9651) give HTTP fields a common
   syntax, but a general parser for them is a sizable dependency for a
   light client that needs to read only one or two fields.  This
   document defines Simpler Fields, a profile of Structured Fields that
   a client can parse with a short regular expression.  Its Strings are
   percent-encoded, so they contain no quotes, backslashes, or field
   delimiters.  Its serialization is canonical, and its types are fixed.
   Every Simpler Field value is a valid Structured Field value, so a
   general parser reads it unchanged.
- **draft-toutain-core-sid-extension-00** (new-draft, score 0, ignored_after_review) [none]: [SID Extension to efficiently manipulate YANG Data Models](https://datatracker.ietf.org/doc/draft-toutain-core-sid-extension/) — TBD: to focus on sid extension to allow some manipulations of a
   CORECONF datastore without the need to get the full YANG DM.
- **draft-toutain-schc-coreconf-management-02** (new-draft, score 0, ignored_after_review) [none]: [CORECONF Rule management for SCHC](https://datatracker.ietf.org/doc/draft-toutain-schc-coreconf-management/) — This document describes how CORECONF can be applied to SCHC for
   context and rule set management between endpoints.  It also defines a
   YANG module with an RPC to duplicate an existing Rule and apply some
   modifications, and an RPC to reset the Set of Rules to its initial
   content.
- **draft-van-meter-qirg-quantum-network-architecture-02** (new-draft, score 0, ignored_after_review) [none]: [A Quantum Network Architecture](https://datatracker.ietf.org/doc/draft-van-meter-qirg-quantum-network-architecture/) — This quantum network architecture defines a set of planes providing
   different views of the network, supporting different responsibilities
   and modes of operation; a set of device, node and link types; some
   network topologies, deployment scenarios and their relationship to
   applications; and key design decisions as a result of corresponding
   requirements.
- **draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge-00** (new-draft, score 0, ignored_after_review) [none]: [L3 fast convergence for all-active multi-homing for EVPN/ MVPN Seamless interoperation](https://datatracker.ietf.org/doc/draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge/) — This document specifies the procedures for achieving faster Layer-3
   convergence from link/ node failures when all-active multi-homing is
   used with EVPN/ MVPN seamless interop [draft-ietf-bess-evpn-mvpn-
   seamless-interop].  Specifically, these improvements apply when L3
   routed multicast services are deployed by BGP/ EVPN PEs using the
   procedures defined by the above draft.
- **draft-vvv-moqt-object-acks-00** (new-draft, score 0, ignored_after_review) [none]: [Media over QUIC Transport (MOQT) Object Acknowledgements](https://datatracker.ietf.org/doc/draft-vvv-moqt-object-acks/) — This document defines an extension to Media over QUIC Transport
   (MOQT) that allows a subscriber to explicitly acknowledge receiving
   and processing an incoming object.  The acknowledgement includes a
   time delta indicating how early or late the object arrived relative
   to an application-specified deadline; the subscriber also provides
   the publisher with the reference window size that can be used to
   interpret the time delta.  A mechanism to negotiate support for the
   extension, both on the connection and the subscription level, is also
   defined.
- **draft-wagope-dnsop-do-bit-00** (new-draft, score 0, ignored_after_review) [none]: [Clearing the DO bit for DNSSEC](https://datatracker.ietf.org/doc/draft-wagope-dnsop-do-bit/) — { Editor note: THIS IS A WORKING IDEA FOR DISCUSSION.

   It might be the best idea ever... or the worst idea ever.  The
   authors really cannot decide (or even agree among themselves), but I
   have written this up as as an ID to share it with the WG.  Please
   understand that we are simply floating the idea; if it turns out that
   it is the worse idea ever, we'll happily drop it and save ourselves a
   bunch of work! :-) }

   The DNSSEC OK (DO) bit is an EDNS0 flag used in DNS queries to signal
   that the requestor wishes to receive DNSSEC resource records (such as
   RRSIG, DNSKEY, DS, and NSEC) in the response.

   This bit is named DNSEC OK (DO) as an indication that the resolver
   implementation will not die if it receives DNSSEC records, not that
   it is actually performing DNSSEC validation.

   It is important to note that clearing the DO bit means that the
   authoritative server will not include DNSSEC records in its response,
   even if they exist.

   One of the concerns around Post Quantum Cryptography (PQC) is that
   the resulting DNSSEC signatures may be significantly larger than
   current signatures.  This could exacerbate issues related to DNS
   message size and fragmentation, and cause many connections to fail
   back to TCP.Clearing the DO bit can help mitigate these issues by
   preventing the inclusion of potentially large DNSSEC records in
   responses, but it also means that resolvers will not have access to
   the DNSSEC proofs necessary for validation.
- **draft-wang-grow-bmp-attribute-sets-stats-00** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for BGP Path Attribute Sets and Statistics](https://datatracker.ietf.org/doc/draft-wang-grow-bmp-attribute-sets-stats/) — The BGP Monitoring Protocol (BMP) specified in RFC 7854 requires a
   monitored router to send full BGP Path Attributes for every Route
   Monitoring message.  In networks with a large number of prefixes
   sharing identical BGP Path Attributes, this requirement leads to
   substantial transmission redundancy and protocol overhead.

   This document specifies a decoupled architecture for BMP monitoring
   that separates Path Attribute Set registration from NLRI volume
   statistics.  Attribute updates are triggered immediately upon path
   attribute changes, while NLRI count updates can be configured for
   either event-driven (immediate) or periodic reporting modes, with
   mandatory instant notification when an attribute set's reference
   count drops to zero.
- **draft-wang-idr-bgp-nof-nlri-04** (new-draft, score 0, ignored_after_review) [none]: [Distribution of Device Discovery Information in NVMe Over RoCEv2 Storage Network Using BGP](https://datatracker.ietf.org/doc/draft-wang-idr-bgp-nof-nlri/) — This document proposes a method of distributing device discovery
   information in NVMe over RoCEv2 storage network using the BGP
   routing protocol. A new BGP Network Layer Reachability Information
   (NLRI) encoding format, named NoF NLRI, is defined.
- **draft-wang-idr-path-attribute-orf-01** (new-draft, score 0, ignored_after_review) [none]: [Path Attribute Outbound Route Filter (PA-ORF) for BGP-4](https://datatracker.ietf.org/doc/draft-wang-idr-path-attribute-orf/) — This document defines a family of Outbound Route Filter (ORF) Types
   for controlling the propagation of BGP Path Attributes.

   The Path Attribute ORFs (PA-ORFs) enable a BGP speaker to dynamically
   request that a peer suppress, remove, refine, or constrain the
   propagation of selected BGP Path Attributes when constructing
   outbound UPDATE messages for a given AFI/SAFI.

   This document defines four ORF Types:

   Path Attribute Type ORF;

   Path Attribute Subtype ORF;

   Unknown Path Attribute ORF; and

   Path Attribute Propagation Scope ORF.

   These ORF Types reuse the ORF Capability and ROUTE-REFRESH procedures
   defined in [RFC5291].  No new BGP Path Attribute or BGP message type
   is introduced.

   PA-ORFs are intended to reduce unintended propagation of BGP Path
   Attributes, especially Optional Transitive attributes whose semantics
   are valid only within a limited administrative, service, or
   technology domain.
- **draft-wang-lamps-root-ca-cert-rekeying-05** (new-draft, score 0, ignored_after_review) [none]: [Root CA Certificate Rekeying in the Scenario of Post Quantum Migration](https://datatracker.ietf.org/doc/draft-wang-lamps-root-ca-cert-rekeying/) — In the public key infrastructures (PKIs), root certification
   authority (CA) certificate rekeying is crucial to guarantee business
   continuity.  Two approaches are given in [RFC4210] for entities
   belonging to different generations to verify each other's certificate
   chain.  However, these approaches rely on the assumption that the old
   entities can be updated.  In this draft, we propose a One-way Link
   Certificate based solution such that old entities are transparent to
   root CA certificate rekeying.  Namely, during the overlapping
   lifetime of two root CA certificates, without any update in old
   entities, old and new entities can verify each other's certificate
   chain smoothly.  Furthermore, the proposed solution works in both
   traditional PKIs, and post-quantum (PQ) PKIs, where the certificates
   can be pure PQ or hybrid.
- **draft-wang-rtgwg-dragonfly-routing-problem-05** (new-draft, score 0, ignored_after_review) [none]: [Routing mechanism in Dragonfly Networks Gap Analysis, Problem Statement, and Requirements](https://datatracker.ietf.org/doc/draft-wang-rtgwg-dragonfly-routing-problem/) — This document provides the gap analysis of existing routing mechanism
   in Dragonfly networks, describes the fundamental problems, and
   defines the requirements for technical improvements.
- **draft-wang-tls-pq-sig-recommend-00** (new-draft, score 0, ignored_after_review) [none]: [Recommendations for Post-Quantum Signature Algorithms in TLS 1.3](https://datatracker.ietf.org/doc/draft-wang-tls-pq-sig-recommend/) — With over 30 distinct post-quantum and hybrid/composite signature
   algorithm parameters proposed or registered for TLS 1.3 [RFC9847]
   [IANA-TLS] [I-D.ietf-tls-composite-mldsa], implementations face
   increasing complexity and deployment overhead.  This document
   provides curated guidance to recommend a manageable subset of post-
   quantum signature schemes for standard TLS 1.3 deployments.
- **draft-wang-token-aware-usecases-requirements-01** (new-draft, score 0, ignored_after_review) [none]: [Token Service Flow Awareness: Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wang-token-aware-usecases-requirements/) — This document outlines the use cases and requirements for token
   service flow awareness, providing the IETF working group with a
   standardized reference to better support the assurance of the user’s
   end-to-end experience.
- **draft-watal-spring-srv6-sfc-sr-aware-functions-06** (new-draft, score 0, ignored_after_review) [none]: [SRv6 SFC Architecture with SR-aware Functions](https://datatracker.ietf.org/doc/draft-watal-spring-srv6-sfc-sr-aware-functions/) — This document describes the architecture of Segment Routing over IPv6
   (SRv6) Service Function Chaining (SFC) with SR-aware functions.  This
   architecture provides the following benefits:

   *  Comprehensive management: centralized control and management of SR
      Policies, network topology, service functions, and network
      metrics.

   *  Simplicity: no SFC proxies, which reduces the number of nodes and
      address resource consumption.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-watal-spring-srv6-sfc-sr-
   aware-functions/.

   Discussion of this document takes place on the SPRING Working Group
   mailing list (mailto:spring@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/spring/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/spring/.

   Source for this draft and an issue tracker can be found at
   https://github.com/watal/draft-watal-spring-srv6-sfc-sr-aware-
   functions.
- **draft-watal-srv6ops-srv6-sfc-deployment-01** (new-draft, score 0, ignored_after_review) [none]: [SRv6 Service Function Chaining Deployment](https://datatracker.ietf.org/doc/draft-watal-srv6ops-srv6-sfc-deployment/) — This document describes the deployment and operational experience of
   the SRv6 Service Function Chaining (SFC) architecture described in
   [I-D.draft-watal-spring-srv6-sfc-sr-aware-functions] on an academic
   IPv6 backbone network.

   The deployed system integrates SRv6 forwarding, service function
   management, topology collection, path computation, and flow
   classification to enable on-demand provisioning of SFC services via a
   web-based management interface.

   This document summarizes the deployment architecture and operational
   workflow, reports on deployment experience and lessons learned, and
   provides guidance for operators deploying SRv6 SFC services.
- **draft-watts-eqr-conformance-05** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Conformance Profile and Test Vectors for Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-eqr-conformance/) — This document defines a deterministic conformance profile and test-
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
- **draft-watts-hagth-framework-01** (new-draft, score 0, ignored_after_review) [none]: [Human-Accelerated Geophysical Threshold Framework](https://datatracker.ietf.org/doc/draft-watts-hagth-framework/) — This document defines an informational research framework for
   describing anthropogenic perturbations that alter the timing,
   probability, coupling, or consequence of threshold transitions in
   geophysical systems without requiring anthropogenic dominance of the
   system's primary energy source.
- **draft-watts-octatouch-smoke-test-profile-01** (new-draft, score 0, ignored_after_review) [none]: [OctaTouch Gesture Runtime: Smoke-Test Behavior Profile](https://datatracker.ietf.org/doc/draft-watts-octatouch-smoke-test-profile/) — This document records five expected behaviors asserted by a supplied
   OctaTouch gesture-runtime smoke-test script.  It is a limited test
   profile, not a complete gesture specification.  The runtime
   implementation and its dependencies were not included with the source
   script, so the tests have not been executed as part of this archive.
   No interoperability or implementation-conformance claim is made.
- **draft-watts-scientific-admissibility-01** (new-draft, score 0, ignored_after_review) [none]: [Scientific Admissibility Evidence Records: A Research Data Exchange Proposal](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility/) — This document proposes interoperable evidence record fields for
   reproducible research workflows.  It is an independent working draft
   and is not an IETF publication or standard.
- **draft-wiggers-tls-authkem-psk-06** (new-draft, score 0, ignored_after_review) [none]: [KEM-based pre-shared-key handshakes for TLS 1.3](https://datatracker.ietf.org/doc/draft-wiggers-tls-authkem-psk/) — This document gives a construction in which (long-term) KEM public
   keys are used in the place of TLS PSK keys, avoiding concerns that
   may affect systems that use symmetric-key-based PSK, such as
   requiring key diversification and protection of symmetric-keys'
   confidentiality.

   This mechanism is inspired by AuthKEM (and could use AuthKEM
   certificate public keys for resumption), but can be independently
   implemented.
- **draft-wu-grow-bmp-multi-instance-03** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Monitoring Multiple BGP Instances](https://datatracker.ietf.org/doc/draft-wu-grow-bmp-multi-instance/) — The BGP Monitoring Protocol (BMP), as defined in RFC 7854, provides a
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
- **draft-wullink-rpp-extension-guidelines-00** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for Extending the RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-extension-guidelines/) — The RESTful Provisioning Protocol (RPP) defines a base set of data
   objects, component objects, and operations for provisioning objects.
   This document defines guidelines and a normative mechanism for
   extension specifications that add data elements, associations,
   operations, result codes, or other functionality, without modifying
   the base specifications itself.
- **draft-wullink-rpp-jscontact-profile-02** (new-draft, score 0, ignored_after_review) [none]: [JSContact Profile for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-jscontact-profile/) — This document defines a JSContact usage profile, conforming to the
   rules described in RFC 10050, for the RESTful Provisioning Protocol
   (RPP).  The JSContact Profile for RPP specifies how the JSContact
   format defined in RFC 9982 can be used as a standardized
   representation of contact information within RPP operations, enabling
   interoperability and consistency across RPP implementations that
   manage contact data.
- **draft-xh-lsvr-region-division-00** (new-draft, score 0, ignored_after_review) [none]: [Region Division in Networks using BGP-LS SPF Routing](https://datatracker.ietf.org/doc/draft-xh-lsvr-region-division/) — In large-scale networks using BGP-LS SPF routing, region division is
   necessary to make the networks stable.  Some networks (e.g.,
   satellite networks) have the characteristics of a flat design, which
   means that no backbone region exists in the network.  This document
   presents a routing framework for region division in large-scale flat
   BGP-LS SPF routing networks.  This framework can realize flexible
   region division, establish intra-region and inter-region paths, and
   complete end-to-end data forwarding.
- **draft-xiao-bpm-ioam-trace-extensions-00** (new-draft, score 0, ignored_after_review) [none]: [Extensions to IOAM Trace Option for Carrying Fixed-Size Data](https://datatracker.ietf.org/doc/draft-xiao-bpm-ioam-trace-extensions/) — In situ Operations, Administration, and Maintenance (IOAM) Trace-
   Option data defined in RFC 9197 is a variable-length data, the length
   of this kind of data varies with the number of transited IOAM-capable
   nodes and the selection of data fields processed by each IOAM-capable
   node.  This document extends the IOAM Trace Option to carry a fixed-
   size data, the length of this kind of data is fixed once the
   selection of data fields processed by each IOAM-capable node is
   determined, and doesn't vary with the number of transited IOAM-
   capable nodes.
- **draft-xl-pce-pcep-pathrate-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extension for Path Rate](https://datatracker.ietf.org/doc/draft-xl-pce-pcep-pathrate/) — This document specifies extensions for PCEP to carry a Path Rate
   (PRate), enabling a PCE to compute and distribute the maximum
   sustainable rate for an end-to-end path.  A new METRIC type and a new
   objective function are defined.
- **draft-xp-bpm-detnet-stamp-00** (new-draft, score 0, ignored_after_review) [none]: [STAMP Extensions for DetNet](https://datatracker.ietf.org/doc/draft-xp-bpm-detnet-stamp/) — Deterministic Networking (DetNet) provides a capability for the
   delivery of data flows with extremely low packet loss rates and
   bounded end-to-end delivery latency.  The enabler to DetNet is a
   proper queue scheduling mechanism, such as timeslot based queueing
   and forwarding mechanism, which requires every router along the
   DetNet path to collect the basic timeslot mapping relationship
   between itself and its adjacent router.  This document defines two
   Simple Two-Way Active Measurement Protocol (STAMP) TLVs, to acquire
   the basic timeslot mapping relationship between the local router and
   its adjacent router.
- **draft-xzl-fann-srv6-rate-notification-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6-based Fast Rate Notification](https://datatracker.ietf.org/doc/draft-xzl-fann-srv6-rate-notification/) — This document specifies a fast rate notification mechanism for
   Segment Routing over IPv6 (SRv6) networks.  It enables a transit or
   egress node to dynamically notify the ingress (headend) node about a
   recommended rate range (MinRate and MaxRate) when localized
   congestion is detected or when underutilized bandwidth is identified,
   allowing the headend to perform proactive traffic shaping and rate
   enforcement.  This mechanism enhances transmission efficiency in SRv6
   networks by enabling fine-grained, congestion-aware rate control.
- **draft-yan-opsawg-ipfix-energy-consumption-03** (new-draft, score 0, ignored_after_review) [none]: [Export of Energy Consumption Information in IPFIX](https://datatracker.ietf.org/doc/draft-yan-opsawg-ipfix-energy-consumption/) — This document introduces new IPFIX IEs for exporting energy
   consumption information of physical entities in a network device.
   New Information Elements are defined to report instantaneous and
   average energy consumption information at device, line-card, and port
   granularity.
- **draft-yang-ipsecme-esp-entropy-header-01** (new-draft, score 0, ignored_after_review) [none]: [An Entropy Header for Load Balancing of IPsec ESP Traffic](https://datatracker.ietf.org/doc/draft-yang-ipsecme-esp-entropy-header/) — When IPsec Encapsulating Security Payload (ESP) is used in tunnel
   mode, an intermediate node cannot inspect the encrypted inner headers
   to derive entropy for Equal-Cost Multipath (ECMP) or Link Aggregation
   Group (LAG) path selection.  Path selection is then driven by outer
   header fields that are identical for every packet of a given tunnel,
   so all packets of the tunnel are placed on a single path regardless
   of the number of inner flows.

   This document defines the ESP Entropy Header, an IP protocol header
   that is placed immediately ahead of ESP and carries an entropy value
   in a fixed position that transit nodes can use for path selection.
   It also defines an Internet Key Exchange Protocol Version 2 (IKEv2)
   extension with which peers negotiate the use of the header on a per-
   Child-SA basis.  The mechanism applies to both IPv4 and IPv6.
- **draft-yang-nmrg-a2a-nm-04** (new-draft, score 0, ignored_after_review) [none]: [Applicability of A2A to the Network Management](https://datatracker.ietf.org/doc/draft-yang-nmrg-a2a-nm/) — This document discusses the applicability of A2A protocol to the
   network management in the multi-domain heterogeneous network
   environment that utilizes IETF technologies.  It explores operational
   aspect, key components, generic workflow and deployment scenarios.
   The impact of integrating A2A into the network management system is
   also discussed.
- **draft-yang-opsawg-ipfix-rocev2-sequence-00** (new-draft, score 0, ignored_after_review) [none]: [IPFIX Export of RoCEv2 Sequence Observations](https://datatracker.ietf.org/doc/draft-yang-opsawg-ipfix-rocev2-sequence/) — This document specifies an IP Flow Information Export (IPFIX)
   metering and export profile for bounded Packet Sequence Number (PSN)
   observations on provisioned RoCEv2 Reliable Connection SEND and RDMA
   WRITE request streams.  It defines cumulative observations of
   skipped, subsequently observed, expired, repeated, and unclassified
   sequence positions, with explicit observation epochs and
   qualification flags.

   The profile requires complete observation of the provisioned stream
   and defines no packet-loss estimator, retransmission detector, or
   congestion-control action.  Twelve Information Elements describe the
   observation state.  Existing RoCEv2 header Information Elements
   identify the monitored stream.
- **draft-yang-pce-pcep-over-quic-06** (new-draft, score 0, ignored_after_review) [none]: [PCEP over QUIC](https://datatracker.ietf.org/doc/draft-yang-pce-pcep-over-quic/) — This document specifies the use of QUIC streams to implement the PCEP
   protocol for efficient and secure data transmission.
- **draft-yang-rtgwg-arn-framework-09** (new-draft, score 0, ignored_after_review) [none]: [Application-Responsive Network Framework](https://datatracker.ietf.org/doc/draft-yang-rtgwg-arn-framework/) — With the deployment of increasingly advanced technologies on a large
   scale, such as SRv6[RFC8402] and network slicing, there is a growing
   need to expose these new capabilities to applications.  The current
   practice involves using ACLs to classify packets and then map the
   traffic onto appropriate network resources.  This approach results in
   the application being passively perceived by the network, rather than
   the application actively interfacing with the network.  Furthermore,
   changes in application characteristics necessitate triggering network
   configuration adjustments, making it challenging to deploy at scale.

   The document proposes a new framework called Application Responsive
   Network (ARN), by encapsulating more network functions into ARN ID,
   thus it opens up interfaces to applications.  The vision is to enable
   applications to access network resources like they access an
   operating system.
- **draft-yang-rtgwg-ecmp-adaptive-load-balance-00** (new-draft, score 0, ignored_after_review) [none]: [Adaptive Load Balancing for Equal-Cost Multipath (ECMP)](https://datatracker.ietf.org/doc/draft-yang-rtgwg-ecmp-adaptive-load-balance/) — Equal-Cost Multipath (ECMP) forwarding assigns a flow to a next-hop
   by computing a hash over packet header fields when the flow is first
   seen.  Because the assignment does not change after that, the load
   across the paths of an ECMP group can become uneven when the set of
   paths changes or when traffic shifts among existing flows.  This
   document defines procedures for adaptive ECMP load balancing in which
   a forwarding node periodically measures per-path load, determines
   whether the load is sufficiently uneven to act on, and makes a
   bounded number of incremental flow placement changes toward less-used
   paths.  The procedures preserve per-flow packet ordering for all but
   the small number of flows that are moved in any interval, and they
   converge toward a balanced distribution across the group.  The
   procedures operate within a single forwarding node and add no new
   packet formats or inter-node signaling.
- **draft-yang-rtgwg-mclag-failure-recovery-00** (new-draft, score 0, ignored_after_review) [none]: [Forwarding-Plane Failure Recovery Procedures for Multi-Chassis Link Aggregation Groups](https://datatracker.ietf.org/doc/draft-yang-rtgwg-mclag-failure-recovery/) — When a downlink member of a Multi-Chassis Link Aggregation Group (MC-
   LAG) fails, a common recovery method flushes the MAC forwarding table
   and relies on flooding to re-establish the forwarding paths, which
   can cause a period of congestion and disruption.  This document
   specifies two complementary forwarding-plane failure recovery
   procedures for MC-LAG.  The first procedure preserves the forwarding
   state by adjusting the LAG group's member set, adding an inter-
   chassis link (ICL) port in place of the failed downlink, so that MAC
   table entries remain valid and traffic is redistributed without a
   table flush and without flooding.  The second procedure extends
   recovery beyond a single Provider Edge (PE) pair: when the immediate
   peer cannot satisfy a failover request, the request is relayed over a
   secondary ICL to the next PE along a configured relay path, which
   allows recovery across three or more PEs in the redundancy domain.
   The procedures operate primarily in the forwarding plane and do not
   require Ethernet VPN (EVPN) infrastructure.
- **draft-ye-srv6ops-sfc-deployment-02** (new-draft, score 0, ignored_after_review) [none]: [SRv6 SFC Deployment Options](https://datatracker.ietf.org/doc/draft-ye-srv6ops-sfc-deployment/) — This document outlines the critical factors for deploying Service
   Function Chaining (SFC) using Segment Routing over IPv6 (SRv6). It
   addresses deployment architectures, including both SRv6-aware and
   SRv6-unaware scenarios, and details the end-to-end provisioning
   lifecycle. Furthermore, it proposes reliability mechanisms and
   provides strategic recommendations for network operators
   transitioning from legacy NSH-based SFC to a modern, scalable SRv6
   framework.
- **draft-yl-bpm-cats-00** (new-draft, score 0, ignored_after_review) [bpm]: [Benchmarking Methodology for Computing-aware Traffic Steering](https://datatracker.ietf.org/doc/draft-yl-bpm-cats/) — Computing-aware traffic steering (CATS) is a traffic engineering
   approach for steering service requests towards appropriate service
   instances based on the awareness of both computing and network
   information.  This document proposes benchmarking methodologies for
   CATS.
- **draft-yuyou-moq-v3c-00** (new-draft, score 0, ignored_after_review) [none]: [Transport of V3C Bitstreams over Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-yuyou-moq-v3c/) — This document specifies a mapping and packaging for transporting ISO/
   IEC 23090-5 Visual Volumetric Video-based Coding (V3C) bitstreams
   over Media over QUIC Transport (MOQT).  The mapping uses the MOQT
   Streaming Format (MSF): V3C configuration is MSF initialization data,
   each independently consumable V3C component is an MSF track, a V3C
   composition unit is a MOQT Group, and a coded V3C unit is a MOQT
   Object.  Relays remain unaware of V3C syntax.  V3C knowledge is
   confined to the streaming-format layer.
- **draft-zcz-nmrg-digitaltwin-data-collection-06** (new-draft, score 0, ignored_after_review) [none]: [Data Collection Requirements and Technologies for Network Digital Twin](https://datatracker.ietf.org/doc/draft-zcz-nmrg-digitaltwin-data-collection/) — A Network Digital Twin is a virtual representation of a real network,
   which is meant to be used by a management system to analyze,
   diagnose, emulate, and then control the real network based on data,
   models, and interfaces.  The construction and state update of a
   Network Digital Twin requires obtaining real-time information of the
   physical network it represents (i.e., telemetry data).  This document
   aims to describe the data collection requirements and provide data
   collection methods or tools to build the data repository for building
   and updating a network digital twin.
- **draft-zdx-rift-addsblock-extensions-00** (new-draft, score 0, ignored_after_review) [none]: [RIFT KV extensions for address block](https://datatracker.ietf.org/doc/draft-zdx-rift-addsblock-extensions/) — This document describes a method for extending the address blocks
   carried within Key/Value extensions in data centers where RIFT
   (Routing in Fat Trees) is deployed.
- **draft-zdz-teas-5g-slice-ipextension-01** (new-draft, score 0, ignored_after_review) [none]: [Carrying 5G Network Slice Identifiers in IP Headers for QoS Assurance Beyond the 3GPP-Managed Domain](https://datatracker.ietf.org/doc/draft-zdz-teas-5g-slice-ipextension/) — 3GPP defines 5G network slicing as an end-to-end service spanning the
   Radio Access Network (RAN), Transport Network (TN), and Core Network
   (CN).  Within these domains, dedicated slice-awareness and management
   mechanisms are specified by 3GPP.  However, when 5G slice traffic
   traverses an IP backbone network that lies outside the 3GPP-managed
   domain -- such as when a User Plane Function (UPF) connects to an
   external service provider network -- slice context information is
   lost, and the IP backbone cannot differentiate or assure the quality
   of individual slices.

   This document proposes a method for preserving 5G network slice
   awareness in IP backbone networks by encoding the 3GPP Single Network
   Slice Selection Assistance Information (S-NSSAI) directly into IPv6
   packet headers.  This document also describes the associated
   procedures for slice-aware QoS assurance in the IP backbone.
- **draft-zengin-moq-ssts-backpressure-00** (new-draft, score 0, ignored_after_review) [none]: [A Backpressure Algorithm for Sender-Side Track Switching in MOQ Transport](https://datatracker.ietf.org/doc/draft-zengin-moq-ssts-backpressure/) — Sender-Side Track Switching (SSTS) lets a publisher forward one track
   at a time out of a switching set, and leaves the choice of which
   track to a pluggable algorithm.  The default algorithm divides a
   bandwidth estimate between switching sets.  This document defines an
   alternative algorithm that uses no bandwidth estimate at all.  It
   monitors the number of open forwarding streams carrying the currently
   active tier, steps rapidly through the switching set's ladder during
   fast start, regulates steady-state upshifts dynamically according to
   relative bitrate jumps and the subscriber's probing risk tolerance,
   and reacts to mid-group congestion using intra-group monitoring and
   retroactive stream supersede.  The signal is directly observable at
   the publisher, requires no cooperation from the congestion
   controller, and degrades toward the lowest quality under load rather
   than toward none.
- **draft-zhang-dnssec-wildcard-validation-02** (new-draft, score 0, ignored_after_review) [none]: [Signer-Zone Containment for DNSSEC Wildcard Validation](https://datatracker.ietf.org/doc/draft-zhang-dnssec-wildcard-validation/) — Validators for the DNS Security Extensions (DNSSEC) reconstruct the
   original owner name of a signed resource record set (RRset) using the
   RRSIG Labels field.  This document updates RFC 4035 to make explicit
   how its existing signing-zone authority requirement applies to that
   reconstructed owner, and updates RFC 8198 to preserve the
   authenticated association between wildcard data, its original owner,
   and its signing zone during cache reuse.  These clarifications
   prevent cryptographically correct signatures from being treated as
   authenticating wildcard sources outside the signing zone.  They do
   not change DNS wildcard matching or synthesis rules, or DNS message
   formats.
- **draft-zhao-opsawg-network-resilience-ps-02** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement for Network Resilience](https://datatracker.ietf.org/doc/draft-zhao-opsawg-network-resilience-ps/) — This document examines the problem space for network resilience,
   focusing on the ability of networks to maintain acceptable service
   levels and recover from disruptive conditions.  It identifies
   limitations of existing protection and recovery mechanisms under
   correlated, cascading, or evolving failures, and when resources or
   systems required for recovery are themselves impaired.  It analyzes
   resilience challenges across risk anticipation, disruption absorption
   and adaptation, service recovery, and continuous improvement, and
   identifies corresponding capability gaps to be addressed.
- **draft-zhao-pce-recovery-admission-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Conditional Recovery Admission and Coordination](https://datatracker.ietf.org/doc/draft-zhao-pce-recovery-admission/) — Following a disruptive event, multiple Path Computation Element
   (PCE)-controlled Label Switched Paths (LSPs) may need to recover over
   the same limited remaining resources.  Individually feasible paths do
   not necessarily remain feasible when competing recovery updates are
   activated concurrently.

   This document proposes PCEP extensions to carry explicit conditional
   recovery admission decisions, correlate their installation outcomes,
   and reconcile their admission state after failures or PCEP session
   loss.  Coordination is limited to consistent accounting of shared
   recovery resources by one active stateful PCE.

   The extension does not specify path computation algorithms, guarantee
   end-to-end service performance, or replace local fast protection.
- **draft-zhou-grow-monitoring-neighbor-state-02** (new-draft, score 0, ignored_after_review) [none]: [Real-Time Monitoring Link/Protocol Neighbor State](https://datatracker.ietf.org/doc/draft-zhou-grow-monitoring-neighbor-state/) — Various protocols are deployed in today's networks, such as BGP /
   ISIS / OSPF etc.  Link neighbor state changes and protocol neighbor
   state changes are the most important network events that need to be
   processed with the highest priority.  In particular, the SDN
   controller needs to quickly sense the link neighbor and protocol
   neighbor state change information in the network.  Thus, the various
   policies applied by the SDN controller to the network can quickly
   match the current state of the network.  This document discusses some
   possible scenarios and the relevant requirements.
- **draft-zl-srv6ops-srv6-vxlan-gateway-00** (new-draft, score 0, ignored_after_review) [none]: [VXLAN and SRv6 Gateway Deployment Options and Considerations](https://datatracker.ietf.org/doc/draft-zl-srv6ops-srv6-vxlan-gateway/) — VXLAN is widely deployed in data center networks, often with Ethernet
   VPN (EVPN) as its control plane.  Segment Routing over IPv6 (SRv6) is
   used to provide services and path control over IPv6 networks,
   including networks connecting data centers and wide area networks.

   This document describes deployment options for connecting VXLAN-based
   data center networks to SRv6 networks.  These options include VXLAN
   and SRv6 service interworking at a gateway, and the transport of
   VXLAN traffic over an SRv6 network.  The document discusses their
   characteristics, deployment trade-offs, and operational
   considerations.
- **draft-zzhang-bier-adaptive-routing-00** (new-draft, score 0, ignored_after_review) [none]: [Adaptive Routing with BIER](https://datatracker.ietf.org/doc/draft-zzhang-bier-adaptive-routing/) — ECMP is extensively used in AI DC networking, often with so called
   adaptive routing mechansim, with which the load/congestion/capacity
   information for the nexthop, next nexthop, or even the entire path is
   considered to dynamically adjusts routing paths based on changes in
   global network conditions, thereby optimizing network performance and
   resource utilization.  This document describe how BIER can work with
   adaptive routing.
- **draft-zzhang-bier-unmasked-bier-02** (new-draft, score 0, ignored_after_review) [none]: [Unmasked BIER Mode](https://datatracker.ietf.org/doc/draft-zzhang-bier-unmasked-bier/) — The document introduces a new mode of interpretation of the bitmask
   field in the BIER encoding, called unmasked BIER, that solves the
   problem of BIER originator targeting receivers across many different
   sets and hence, in worst case, degrading into ingress replication.
- **draft-zzhang-idr-mpte-signaling-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Signaling for Multipath Traffic Engineering Junction States](https://datatracker.ietf.org/doc/draft-zzhang-idr-mpte-signaling/) — Multi-Path Traffic Engineering (MPTE) combines Traffic Engineering
   with Multi-Path forwarding, offering a much desired TE solution for
   both traditional WAN and new AIML DC/DCI.  MPTE tunnels are based on
   MPTE Directed Acyclic Graph (DAG) and can be signaled with extensions
   to RSVP-TE, PCEP, BGP.  This document specifies the BGP protocol
   extensions and procedures for signaling MPTE DAGs.
- **draft-zzhang-pim-bidir-multiplane-fat-tree-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for PIM-Bidir in Multi-Planed Fat Trees](https://datatracker.ietf.org/doc/draft-zzhang-pim-bidir-multiplane-fat-tree/) — Modern Data Centers are increasingly adopting multi-plane.  This
   brings unique challenges for RP-based mulitcast.  This document
   discusses considerations for RP placement for PIM-Bidir in multi-
   plane fat tree networks, and considerations for multicast with RIFT
   signaling.
- **draft-zzhang-rift-multicast-03** (new-draft, score 0, ignored_after_review) [none]: [Multicast Routing In Fat Trees](https://datatracker.ietf.org/doc/draft-zzhang-rift-multicast/) — This document specifies multicast procedures with RIFT.  Multicast in
   RIFT is similar to Bidirectional Protocol Independent Multicast (PIM-
   Bidir), with the Rendezvous Point Link (RP-Link) simulated by a
   spanning tree of some Top of Fabric (TOF) nodes and sub-TOF nodes.

## Errors / fetch failures

_None._
