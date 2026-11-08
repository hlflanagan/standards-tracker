# IETF Identity + AI Standards Watch

Date: 2026-11-08

## Read now

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
- **draft-ietf-oauth-sd-jwt-vc-26** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.

   Furthermore, this specification updates RFC7800 to allow for the
   Confirmation Claim (cnf) to be used regardless of the presence or
   absence of other claims.
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
- **draft-agentic-ai-usecases-requirements-07** (new-draft, score 13, core_identity) [agentproto]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
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
- **draft-ietf-rats-network-device-subscription-16** (new-draft, score 9, trust_infrastructure) [rats]: [Attestation Event Stream Subscription](https://datatracker.ietf.org/doc/draft-ietf-rats-network-device-subscription/) — This document defines how to subscribe to YANG Event Streams for
   Remote Attestation Procedures (RATS).  Specifically, this document
   defines a YANG module that augments the YANG module for Trusted
   Platform Module (TPM)-based Challenge-Response Remote Attestation
   (CHARRA), enabling subscription to RATS Conceptual Messages of the
   Evidence type and auxiliary Event Logs as part of that Evidence.  The
   module defined requires at least one Trusted Platform Module (TPM)
   1.2 or TPM 2.0 (or equivalent hardware implementation providing the
   same protected capabilities as a TPM) must be available on the
   Attester on which the YANG server is running.
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
- **draft-wang-agent-gateway-interconnect-usecase-req-00** (new-draft, score 8, agent_identity) [none]: [Agent Gateway Interconnection: Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wang-agent-gateway-interconnect-usecase-req/) — This document defines use cases and requirements for interconnection
   of Agent Gateways (AGWs) across separate administrative domains.  An
   Agent Gateway acts as a trust and protocol boundary for AI agents,
   mediating agent discovery, intent routing, policy enforcement,
   context translation, and secure cross-domain collaboration.  This
   draft does not specify a wire protocol.  Instead, it collects
   representative deployment scenarios and derives functional,
   operational, and interoperability requirements to guide future
   protocol design for AGW-to-AGW interconnection.
- **draft-zhang-rtgwg-multicast-requirements-gaps-aidc-03** (new-draft, score 8, ai_infrastructure) [none]: [Requirements and Gap Analysis of Multicast in AI Data Centers](https://datatracker.ietf.org/doc/draft-zhang-rtgwg-multicast-requirements-gaps-aidc/) — Multicast has the potential to be applied in Artificial Intelligence
   Data Centers (AIDCs) to improve the efficiency of point-to-multipoint
   data transmission during large language model training and inference.
   This document identifies key requirements of multicast in AIDCs, and
   analyzes the gaps between these requirements and the capabilities of
   existing multicast technologies.
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
- **draft-ietf-dance-client-auth-17** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DNS-Based Authentication of Named Entities (DANE) protocol
   describes how to publish Transport Layer Security (TLS) server
   certificates or public keys in the DNS, using the TLSA resource
   record.  This document describes how to use the TLSA record to
   publish client certificates or public keys, and also the rules and
   considerations for using them with TLS.  In addition, it defines a
   new TLS extension, DANE Client Identity, to convey the client's
   domain name identity to the server.
- **draft-ietf-dtn-adm-yang-08** (new-draft, score 6, core_identity) [dtn]: [DTNMA Application Data Model (ADM) YANG Syntax](https://datatracker.ietf.org/doc/draft-ietf-dtn-adm-yang/) — This document defines a concrete syntax for encoding a Delay-Tolerant
   Networking Management Architecture (DTNMA) Application Data Model
   (ADM) using the syntax and modular structure, but not the full data
   model, of YANG.  Extensions to YANG are defined to capture the
   specifics needed to define DTNMA Application Management Model (AMM)
   objects and to use the Application Resource Identifier (ARI) data-
   value syntax.
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
- **draft-skyfire-oauth-amr-values-03** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-03** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
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
- **draft-zhang-seat-selection-02** (new-draft, score 6, trust_infrastructure) [none]: [Balancing Security and Deployability in the Selection of Attested TLS Protocol](https://datatracker.ietf.org/doc/draft-zhang-seat-selection/) — This document analyzes the selection of Attested Transport Layer
   Security (aTLS) protocols, among pre-handshake, intra-handshake, and
   post-handshake aTLS protocols, focusing on the trade-off between
   theoretical security strength and practical deployability.  The goal
   is to enable flexible, context-aware deployment of endpoint
   attestation while maintaining compatibility with existing
   infrastructure.
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
- **draft-gondwana-dkim2-authres-02** (new-draft, score 3, core_identity) [none]: [Reporting DKIM2 Verification Results in Authentication-Results](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-authres/) — DomainKeys Identified Mail Signatures v2 (DKIM2) produces a
   verification result for an email message.  This document defines how
   that result is reported in the Authentication-Results header field,
   registering the "dkim2" authentication method, the result values it
   can take, and two properties which identify the signing domain and
   the point in the chain at which verification failed.  Diagnostic
   detail about each hop is carried in a human-readable comment.
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
- **draft-ietf-cats-oam-fw-02** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections across clients, network paths, and service
   instances within a single domain.  This document does not define
   concrete OAM protocol designs or protocol extensions.
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
- **draft-ietf-lsvr-bgp-ls-yang-05** (new-draft, score 3, adjacent_watchlist) [lsvr]: [A YANG Model for BGP-LS, BGP-LS-VPN, and BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-ietf-lsvr-bgp-ls-yang/) — This document defines a YANG data model for configuration and
   management of BGP-LS, BGP-LS-VPN, and BGP-LS-SPF.
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
- **draft-ietf-opsawg-ipfix-gtpu-19** (new-draft, score 3, core_identity) [opsawg]: [Export of GTP-U Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-gtpu/) — This document specifies IP Flow Information Export (IPFIX)
   Information Elements to report information contained in the Generic
   Packet Radio Service Tunneling Protocol (GTP) User Plane header such
   as Tunnel Endpoint Identifier, and data contained in its session
   container extension header.
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
- **draft-ietf-webtrans-http2-16** (new-draft, score 3, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/2](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http2/) — WebTransport defines a set of low-level communications features
   designed for client-server interactions that are initiated by Web
   clients.  This document describes a protocol that can provide the
   capabilities of WebTransport over HTTP/2.  This protocol enables the
   use of WebTransport when a UDP-based protocol is not available.
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
- **draft-pauly-independent-submission-restructure-00** (new-draft, score 3, adjacent_watchlist) [none]: [Independent Submission Board Model](https://datatracker.ietf.org/doc/draft-pauly-independent-submission-restructure/) — The Independent Submission stream is one of the stream producers that
   create draft RFCs.  This document proposes the creation of the
   Independent Submission Board (ISB), a small board appointed by both
   the IAB and IESG, that acts as the stream approver.  The ISB is
   responsible for activities within the Independent Submission stream,
   works with draft editors and reviewers, and interacts with the RFC
   Production Center and Publisher, and the RFC Series Editor (RSE).

   If approved, this proposal would obsolete RFC 8730, which defines a
   single Independent Submission Editor.
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
- **draft-chen-tsvwg-high-speed-ip-data-express-00** (new-draft, score 2, ignored_after_review) [none]: [High speed data express in IP: Concept, Reference Architecture and Technologies](https://datatracker.ietf.org/doc/draft-chen-tsvwg-high-speed-ip-data-express/) — With the rapid development of AI technology, intelligent computing
   and super-computing services, the demand for wide-area transmission
   of massive data is increasing.  This draft makes full use of the
   advantages of IP network, such as statistical reuse and elastic
   supply, and proposes a reference architecture of high elasticity and
   high throughput data express based on IP network.
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
- **draft-spzzx-bier-in-ai-consideration-00** (new-draft, score 2, ignored_after_review) [none]: [BIER in AI considerations](https://datatracker.ietf.org/doc/draft-spzzx-bier-in-ai-consideration/) — Based on existing industry research, this document outlines
   considerations regarding the application of BIER technology in AIDC.
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

- **draft-ageneau-ccwg-ndtc-03** (new-draft, score 0, ignored_after_review) [none]: [Network Delivery Time Control](https://datatracker.ietf.org/doc/draft-ageneau-ccwg-ndtc/) — This document describes Network Delivery Time Control (NDTC), a rate
   adaptation algorithm for real-time video streaming suited for
   interactive applications like cloud gaming.  NDTC leverages the Frame
   Dithering Available Capacity Estimation (FDACE) heuristic, which
   estimates available path capacity without inducing congestion.  The
   algorithm dynamically adjusts frame sizes and transmission times to
   ensure timely delivery, while also responding to conventional
   congestion signals.
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
- **draft-clayton-dkim-canmodify-00** (new-draft, score 0, ignored_after_review) [none]: [Permitted modifications to DKIM2 messages](https://datatracker.ietf.org/doc/draft-clayton-dkim-canmodify/) — DomainKeys Identified Mail v2 (DKIM2) requires any modifications made
   to email messages by intermediaries to be recorded in "recipes".
   Some originators wish to request that only very limited modifications
   be made to their messages so that the recipient of the message can
   have some assurance that the modifications were benign.  This
   document introduces the CanModify header field into which originator
   requests may be placed.  It then sets out a small set of
   modifications that are commonly applied by intermediaries and
   assesses how benign they may actually be.
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
- **draft-fernandez-dnsop-client-side-adox-signal-00** (new-draft, score 0, ignored_after_review) [none]: [Client-side Request for Encrypted Authoritative DNS Queries](https://datatracker.ietf.org/doc/draft-fernandez-dnsop-client-side-adox-signal/) — This document describes an EDNS0 option that a client can attach to a
   DNS query to signal to a recursive resolver that it SHOULD prefer
   encrypted transports while resolving the query.  The option can also
   be used on the return path by the resolver to signal whether
   encryption was achievable or not.
- **draft-frindell-moq-timestamp-01** (new-draft, score 0, ignored_after_review) [none]: [Timestamp Properties for MOQT](https://datatracker.ietf.org/doc/draft-frindell-moq-timestamp/) — This document defines a set of MOQT Properties for carrying per-
   Object timestamps efficiently.  The encoded timestamp is intended for
   use in MOQT, but can be referenced for application specific purposes.
- **draft-fujiwara-dnsop-dns-upper-limit-values-06** (new-draft, score 0, ignored_after_review) [none]: [Upper limit values for DNS](https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-dns-upper-limit-values/) — DNS was designed to have as few hard upper limits as possible to
   allow for future extensibility.  However, the lack of a clear upper
   limit leads to vulnerabilities, and several attack methods have been
   reported.  This document collects upper limit values implemented by
   DNS software to avoid vulnerabilities.
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
- **draft-gray-plants-mtc-ldp-00** (new-draft, score 0, ignored_after_review) [none]: [Landmark Distribution Point Fetching for Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-gray-plants-mtc-ldp/) — This document specifies a mechanism for a relying party to retrieve
   Merkle-tree subtree consistency proofs needed to validate a landmark-
   relative Merkle Tree Certificate (MTC).  An X.509 certificate
   extension identifies one or more Landmark Distribution Points (LDPs).
   A relying party requests a proof set from an LDP and validates the
   proof chain against a trusted, signed target checkpoint.
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
- **draft-holmgren-at-repository-04** (new-draft, score 0, ignored_after_review) [none]: [Authenticated Transfer: Repository and Synchronization](https://datatracker.ietf.org/doc/draft-holmgren-at-repository/) — This document specifies a repository data structure and
   synchronization mechanisms for public data as part of the
   Authenticated Transfer Protocol (ATP).  It describes encoding formats
   for both individual data records and entire repositories.  The
   repository data structure is content-addressable and
   cryptographically authenticated.  For synchronization, it specifies
   both a low-latency streaming protocol over WebSocket, and a full-
   repository fetch mechanism over HTTP.
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
- **draft-ietf-6lo-rfc8163-bis-01** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of IPv6 over Multidrop Serial Bus/Token Passing (MS/TP) Networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-rfc8163-bis/) — Multidrop Serial Bus/Token Passing (MS/TP) is a medium access control
   method for the RS-485 physical layer and is used primarily in
   building automation networks.  This specification defines the frame
   format for transmission of IPv6 packets and the method of forming
   link-local and statelessly autoconfigured IPv6 addresses on MS/TP
   networks.  It obsoletes RFC 8163.
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
- **draft-ietf-bess-evpn-l3mh-proto-02** (new-draft, score 0, ignored_after_review) [bess]: [EVPN multi-homing support for L3 services](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/) — This document describes the use of EVPN Ethernet Segment Link
   Aggregation Group (ES-LAG) technology to provide multi-homing
   redundancy for Layer 3 services.  The solution synchronizes ARP/ND,
   multicast state, and IGP routes between redundant PEs without
   requiring Layer 2 constructs or proprietary Inter-Chassis
   Communication protocols.
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
- **draft-ietf-idr-rt-derived-community-14** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route-Target-derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route-Target-derived Extended
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
- **draft-ietf-idr-ts-flowspec-srv6-policy-21** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
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
- **draft-ietf-ippm-stamp-cos-ecn-02** (new-draft, score 0, ignored_after_review) [bpm]: [Update of the Simple Two-way Active Measurement Protocol Class-of-Service Extension - ECN](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-cos-ecn/) — The Simple Two-Way Active Measurement Protocol (STAMP) enables one-
   way and round-trip measurement of network metrics between IP hosts,
   and has a facility for defining optional extensions.  This document
   updates the definition of the Class of Service TLV (originally
   defined in RFC 8972) to enable the measurement of manipulation of the
   value of the Explicit Congestion Notification (ECN) field of the IP
   header by middleboxes between two STAMP hosts, and to enable
   discovery and measurement of paths that provide differential
   treatment of packets depending on the value of their ECN field.
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
- **draft-ietf-lsr-pcpps-03** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/) — [I-D.many-teas-power-steering] introduces a Power Conserving Path
   Placement Strategy (PCPPS).  When possible, PCPPS concentrates
   traffic onto a small set of network resources.  When traffic is
   concentrated onto a small set of network resources, other network
   resources become idle and can be powered down until they are needed
   again.  This conserves energy and reduces environmental impact.

   PCPPS uses information that is distributed by an IGP.  This document
   specifies the IS-IS encoding for that information.
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
- **draft-ietf-mls-virtual-clients-02** (new-draft, score 0, ignored_after_review) [mls]: [MLS Virtual Clients](https://datatracker.ietf.org/doc/draft-ietf-mls-virtual-clients/) — This document describes a method that allows multiple MLS clients to
   emulate a virtual MLS client.  A virtual client allows multiple
   emulator clients to jointly participate in an MLS group under a
   single leaf.  Depending on the design of the application, virtual
   clients can help hide metadata and improve performance.
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
- **draft-ietf-opsawg-ipfix-alt-mark-10** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-veloce-yang-01** (new-draft, score 0, ignored_after_review) [opsawg]: [YANG deVELpment PrOCEss and maintenance (VELOCE)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-veloce-yang/) — This document describes a YANG deVELopment PrOCEss and maintenance
   (VELOCE) that is more suitable for the development of YANG modules or
   YANG modules update within the IETF.

   Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-opsawg-wg/veloce/tree/main.
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
- **draft-ietf-savnet-inter-domain-problem-statement-23** (new-draft, score 0, ignored_after_review) [savnet]: [Problem Statement, Gap Analysis, and Requirements for Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/) — This document analyzes the problem space and provides a gap analysis
   of existing inter-domain source address validation (SAV) mechanisms.
   Based on these findings, it outlines the technical requirements for
   future improvements.
- **draft-ietf-schc-architecture-07** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression (SCHC) Architecture](https://datatracker.ietf.org/doc/draft-ietf-schc-architecture/) — The Static Context Header Compression and fragmentation (SCHC)
   framework provides both a header compression mechanism and an
   optional fragmentation mechanism.  This document defines an
   architecture for SCHC deployments, providing guidance for
   implementers and operators on the essential components and their
   interactions required for effective SCHC operation.
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
- **draft-ietf-suit-manifest-38** (new-draft, score 0, ignored_after_review) [suit]: [A Concise Binary Object Representation (CBOR)-based Serialization Format for the Software Updates for Internet of Things (SUIT) Manifest](https://datatracker.ietf.org/doc/draft-ietf-suit-manifest/) — This specification describes the format of a manifest.  A manifest is
   a bundle of metadata about code/data obtained by a recipient (chiefly
   the firmware for an Internet of Things (IoT) device), where to find
   the code/data, the devices to which it applies, and cryptographic
   information protecting the manifest.  Software updates and Trusted
   Invocation both tend to use sequences of common operations, so the
   manifest encodes those sequences of operations, rather than declaring
   the metadata.
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
- **draft-jabley-dnsop-ordered-answer-section-02** (new-draft, score 0, ignored_after_review) [none]: [Ordering of RRSets in CNAME Responses in the DNS](https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/) — In the DNS, recursive resolvers receive queries and formulate
   corresponding responses by reference to data obtained from
   authoritative servers.  In the case where the query name (QNAME) and
   class (QCLASS) in the query matches an owner name in the DNS where a
   canonical name (CNAME) resource record is published, the response
   includes both the CNAME record and the resource record set
   corresponding to the request's query type (QTYPE) published at the
   CNAME target.  The ordering of these two different RRSets has not
   previously been clearly specified, but operational experience based
   on real-world client implementations confirms that the order is
   important.  This document updates RFC 1034 1035 to provide a clearer
   specification, consistent with deployed implementations.
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
- **draft-kbr-teas-mptersvp-06** (new-draft, score 0, ignored_after_review) [none]: [RSVP-TE Extensions for Multipath Traffic Engineered Directed Acyclic Graph Tunnels](https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that facilitates weighted
   load balancing of unicast traffic across a constrained set of paths
   optimized for a specific objective.

   This document describes the provisioning of an MPTED tunnel in a TE
   network using RSVP-TE.
- **draft-kejriwal-scone-scone-qlog-01** (new-draft, score 0, ignored_after_review) [none]: [QUIC Logging for the SCONE Protocol](https://datatracker.ietf.org/doc/draft-kejriwal-scone-scone-qlog/) — This document defines qlog events for the Standard Communication with
   Network Elements (SCONE) protocol.  The events record the sending and
   reception of SCONE packets and changes to throughput advice.
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
- **draft-lampin-schc-voici-01** (new-draft, score 0, ignored_after_review) [none]: [VOICI](https://datatracker.ietf.org/doc/draft-lampin-schc-voici/) — The Static Context Header Compression (SCHC) framework identified the
   need for a minimal transport encapsulation that provides Session
   multiplexing when extrinsic Discriminators are insufficient.  This
   document specifies a Link Multiplexer (VOICI) that addresses those
   SCHC-driven requirements while remaining general enough to
   accommodate other compression mechanisms and uncompressed payloads.
   The encapsulation is designed for minimal overhead, reducing to 1
   byte in the common case (7 inline Session IDs), while supporting
   optional integrity protection and original EtherType/port recovery.
- **draft-lampin-schc-voici-compression-01** (new-draft, score 0, ignored_after_review) [none]: [SCHC Compression of VOICI Headers](https://datatracker.ietf.org/doc/draft-lampin-schc-voici-compression/) — This document describes how to compress VOICI headers using SCHC
   rules at a lower stratum, demonstrating that VOICI provides explicit
   routing metadata that is transparently compressed to minimal on-wire
   size while preserving standardized dispatch semantics.  It is
   intended as a reference for implementers deploying VOICI in SCHC-
   based networks and does not modify the VOICI specification itself.
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
- **draft-lenders-dns-cbor-19** (new-draft, score 0, ignored_after_review) [none]: [A Concise Binary Object Representation (CBOR) of DNS Messages](https://datatracker.ietf.org/doc/draft-lenders-dns-cbor/) — This document specifies a compact data format for DNS messages using
   the Concise Binary Object Representation [RFC8949].  The primary
   purpose is to keep DNS messages small in constrained networks.
- **draft-li-idr-flowspec-redirect-direct-ip-01** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Redirects to Direct IP](https://datatracker.ietf.org/doc/draft-li-idr-flowspec-redirect-direct-ip/) — A bit, D bit, is defined in the Flow-spec Redirect-to-IPv4 Extended
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
- **draft-lin-grow-bmp-cap-notification-02** (new-draft, score 0, ignored_after_review) [none]: [Peer Capability Update Notification in BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-lin-grow-bmp-cap-notification/) — When BGP Dynamic Capability is supported, dynamic updates of
   capabilities are allowed over an established BGP session.  At
   present, after the BGP session is established, the monitored router
   sends a BMP Peer Up Notification message first, containing the
   initial capabilities.  If BGP Dynamic Capability is supported, using
   BMP Peer Up Notification messages to report subsequent capability
   changes for a BGP session becomes inappropriate.  This document
   defines a new Peer Capability Update Notification message type in BMP
   to report peer capability changes.
- **draft-lin-idr-sr-policy-headend-behavior-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extensions of SR Policy for Headend Behavior](https://datatracker.ietf.org/doc/draft-lin-idr-sr-policy-headend-behavior/) — [RFC8986] defines H. Encaps behavior, H. Encaps.Red behavior, H.
   Encaps.L2 behavior, and H. Encaps.L2.Red behavior for SR policy.
   This document defines extensions to Border Gateway Protocol (BGP) to
   distribute SR policies carrying headend behavior.
- **draft-liu-fann-wan-flowctrl-detect-00** (new-draft, score 0, ignored_after_review) [none]: [Proactive Flow Control Point Detection in WAN](https://datatracker.ietf.org/doc/draft-liu-fann-wan-flowctrl-detect/) — This document proposes a proactive detection mechanism that enables
   the flow control notification message generating downstream node to
   be aware of the nearest upstream node capable of processing the
   message . The mechanism operates in the data plane, uses probe
   packets that follow the same path as data traffic, and maintains
   state only where needed.  While proposed for flow control, the same
   mechanism may support other fast notification use cases that require
   distributed recipient node discovery.
- **draft-liu-opsawg-alt-mark-per-packet-01** (new-draft, score 0, ignored_after_review) [none]: [Alternate marking usage for loss location in per-packet load balancing networks](https://datatracker.ietf.org/doc/draft-liu-opsawg-alt-mark-per-packet/) — Many per-packet load balancing schemes have been proposed to mitigate
   network load imbalances.  However, due to the randomness of packet
   paths, loss location is challenging in per-packet load balancing
   networks.  An efficient solution is to leverage the alternate packet
   marking technique.  This draft analyzes the usage and requirements of
   alternate packet marking for packet loss detection and location in
   per-packet load balancing networks.
- **draft-liu-rtgwg-path-aware-remote-protection-06** (new-draft, score 0, ignored_after_review) [none]: [Path-aware Remote Protection Framework](https://datatracker.ietf.org/doc/draft-liu-rtgwg-path-aware-remote-protection/) — This document describes the framework of path-aware remote
   protection.
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
- **draft-many-tiptop-dns-03** (new-draft, score 0, ignored_after_review) [none]: [Deployment and Use of the Domain Name System(DNS) in Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-dns/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  This document lists operational
   methods to enable local DNS name resolving on celestial body networks
   such that there are no real-time query and response flow to name
   servers on (Earth) Internet.
- **draft-marzot-moq-test-tracks-00** (new-draft, score 0, ignored_after_review) [none]: [MOQT Media Test Tracks](https://datatracker.ietf.org/doc/draft-marzot-moq-test-tracks/) — This document specifies moq-test-tracks, a protocol for testing Media
   over QUIC (MOQ) media implementations.  Like moq-test, it carries its
   parameters to the publisher in the Track Namespace.  The parameters
   describe a set of media tracks, including the catalog, packaging,
   codecs and delivery, so that any publisher that implements the
   protocol can generate media of the requested shape.
- **draft-mazilu-tcpm-packet-trimming-01** (new-draft, score 0, ignored_after_review) [none]: [TCP Packet Trimming Extension](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) — This document specifies a TCP extension that enables TCP endpoints in
   data center networks or similarly controlled administrative domains
   to use packet trimming information when it is available.  When switch
   buffers exceed a threshold, rather than silently dropping a packet,
   the switch trims the payload and forwards the header.  This allows
   the destination to issue a deterministic Negative Acknowledgment
   (NACK), enabling faster, more deterministic loss recovery.
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
- **draft-psenak-lsr-igp-dcm-01** (new-draft, score 0, ignored_after_review) [none]: [Distributed Congestion Mitigation](https://datatracker.ietf.org/doc/draft-psenak-lsr-igp-dcm/) — This document describes the Distributed Congestion Mitigation (DCM)
   mechanism using the Interior Gateway Protocols (IGPs) such as IS-IS
   [RFC1195], OSPFv2 [RFC2328], or OSPFv3 [RFC5340].  DCM is a tactical,
   distributed mechanism, designed to mitigate network congestion by
   offloading traffic to an alternate, congestion-free paths.  DCM is
   fully integrated in IGPs.
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
- **draft-seemann-quic-nat-traversal-04** (new-draft, score 0, ignored_after_review) [none]: [Using QUIC to traverse NATs](https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/) — This document specifies a QUIC extension for traversing Network
   Address Translators (NATs).  Endpoints use an existing proxied QUIC
   connection to coordinate path validation attempts that create the NAT
   bindings needed for a direct path and test its connectivity.
   Application data can be exchanged over the proxied path while NAT
   traversal is in progress.  Once a suitable direct path has been
   validated, the connection can migrate to it.
- **draft-sipos-dtn-bp-safe-02** (new-draft, score 0, ignored_after_review) [none]: [Bundle Protocol (BP) Security Associations with Few Exchanges (SAFE)](https://datatracker.ietf.org/doc/draft-sipos-dtn-bp-safe/) — This document defines a protocol for negotiating scoped security
   associations between Bundle Protocol version 7 (BPv7) agents within a
   delay-tolerant network (DTN).  Security associations are used to
   amortize the costs of asymmetric-keyed security operations and allow
   for efficient and high-throughput BPv7 security within a public key
   infrastructure.  This protocol also provides for unilateral re-keying
   of established security associations in a delay-tolerant manner.
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
- **draft-sriram-savnet-intrasav-solution-01** (new-draft, score 0, ignored_after_review) [none]: [IntraSAV - A Solution for Intra-Domain Source Address Validation](https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/) — This document specifies a solution, named IntraSAV, for intra-domain
   source address validation (SAV).  This solution addresses the problem
   stated in the ietf-savnet-intra-domain-problem-statement (RFC-to-be)
   document.  This document updates BCP 38 ([RFC2827]) and BCP 84
   ([RFC3704], [RFC8704]) by providing a more comprehensive solution
   methodology and accommodating prefixes that are not routed but used
   for sourcing traffic originating from an AS.
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
- **draft-vvv-moqt-object-acks-00** (new-draft, score 0, ignored_after_review) [none]: [Media over QUIC Transport (MOQT) Object Acknowledgements](https://datatracker.ietf.org/doc/draft-vvv-moqt-object-acks/) — This document defines an extension to Media over QUIC Transport
   (MOQT) that allows a subscriber to explicitly acknowledge receiving
   and processing an incoming object.  The acknowledgement includes a
   time delta indicating how early or late the object arrived relative
   to an application-specified deadline; the subscriber also provides
   the publisher with the reference window size that can be used to
   interpret the time delta.  A mechanism to negotiate support for the
   extension, both on the connection and the subscription level, is also
   defined.
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
- **draft-zzhang-idr-mpte-signaling-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Signaling for Multipath Traffic Engineering Junction States](https://datatracker.ietf.org/doc/draft-zzhang-idr-mpte-signaling/) — Multi-Path Traffic Engineering (MPTE) combines Traffic Engineering
   with Multi-Path forwarding, offering a much desired TE solution for
   both traditional WAN and new AIML DC/DCI.  MPTE tunnels are based on
   MPTE Directed Acyclic Graph (DAG) and can be signaled with extensions
   to RSVP-TE, PCEP, BGP.  This document specifies the BGP protocol
   extensions and procedures for signaling MPTE DAGs.
- **draft-zzhang-rift-multicast-03** (new-draft, score 0, ignored_after_review) [none]: [Multicast Routing In Fat Trees](https://datatracker.ietf.org/doc/draft-zzhang-rift-multicast/) — This document specifies multicast procedures with RIFT.  Multicast in
   RIFT is similar to Bidirectional Protocol Independent Multicast (PIM-
   Bidir), with the Rendezvous Point Link (RP-Link) simulated by a
   spanning tree of some Top of Fabric (TOF) nodes and sub-TOF nodes.

## Errors / fetch failures

_None._
