# IETF Identity + AI Standards Watch

Date: 2026-07-12

## Read now

- **draft-tsyrulnikov-rats-attested-inference-receipt-02** (new-draft, score 29, trust_infrastructure) [none]: [Attested Inference Receipt (AIR): A COSE/CWT Profile for Confidential AI Inference](https://datatracker.ietf.org/doc/draft-tsyrulnikov-rats-attested-inference-receipt/) — This document defines the Attested Inference Receipt (AIR), an
   application-layer COSE_Sign1 envelope carrying CWT claims profiled
   per the Entity Attestation Token (EAT) framework.  An AIR receipt
   binds model identity, input/output hashes, attestation-linked
   metadata, and operational telemetry into a single signed artifact
   suitable for independent third-party verification of a confidential
   AI inference.  An AIR receipt is Attester-signed Evidence, not an
   appraisal verdict: a RATS Verifier must appraise the referenced
   platform attestation before the receipt establishes TEE provenance.

   AIR v1 targets single-inference receipts emitted by workloads running
   inside hardware-isolated Trusted Execution Environments (TEEs).  AIR
   is attestation-linked: it carries measurements and a hash reference
   to the platform attestation evidence associated with the inference,
   but it does not replace platform-specific attestation verification.
   This version defines AWS Nitro Enclaves and Intel TDX measurement
   profiles only, and assumes a single platform attestation document per
   receipt.  Pipeline chaining, multi-inference receipts, composite
   attesters, multi-verifier orchestration, accelerator / GPU
   confidential-compute attestation integration, and extensibility
   mechanisms for additional claim or platform profiles are out of
   scope.
- **draft-fane-opena2a-aap-00** (new-draft, score 28, core_identity) [none]: [OpenA2A Agent Authorization Protocol (AAP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aap/) — This document defines the OpenA2A Agent Authorization Protocol (AAP),
   a protocol for authorization in AI agent systems.  AAP provides
   mechanisms for agent identity assertion, scoped capability grants,
   cross-agent delegation, behavioral attestation, cross-organizational
   federation, and revocation propagation.  AAP is the authorization
   complement to agent communication protocols such as A2A and the Model
   Context Protocol, in the same way that OAuth 2.0 complements HTTP for
   web applications.

   AAP has two layers.  The token model, defined in this document,
   specifies the AAP credentials and assertions: what they contain, how
   they are signed, and how they are verified.  A companion broker and
   resolution layer specifies how an agent obtains and exercises a grant
   without the credential value ever entering the agent's reasoning
   context.  This confinement property, that no secret, temporary
   credential, or backend identifier reaches the agent or the model
   behind it, is the primary design goal of the protocol.
- **draft-fane-opena2a-aip-00** (new-draft, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
   AIP), an open standard for creating, managing, and verifying
   cryptographic identities for AI agents.  As AI agents proliferate
   across browsers, cloud platforms, and enterprise environments,
   systems need a standardized answer to the question of which agent is
   present, what it is permitted to do, and whether it should be
   trusted.

   OpenA2A AIP is distinguished by five elements that it places at the
   center of the design: a multi-factor behavioral trust score that is
   computed from independently verifiable signals; a portable signed
   credential, the Agent Trust eXtension, carrying a hybrid Ed25519 and
   ML-DSA-65 signature for post-quantum readiness; an append-only, RFC
   6962-style Merkle transparency log for identity and credential
   issuance; agent identifiers expressed as W3C Decentralized
   Identifiers under the did:opena2a method; and a structured capability
   vocabulary with reserved namespaces.  On top of these, the protocol
   specifies challenge-response verification, behavioral governance
   policies, a lifecycle model, and an append-only audit log.

   The qualifier "OpenA2A AIP" is used throughout this document because
   the abbreviation "AIP" is shared by other Internet-Drafts.  OpenA2A
   AIP is framed as complementary to agent communication protocols such
   as A2A and the Model Context Protocol, and to identity and credential
   standards such as OpenID Connect, WebAuthn, and the W3C Verifiable
   Credentials Data Model.
- **draft-ietf-wimse-identifier-03** (new-draft, score 25, core_identity) [wimse]: [Workload Identifier](https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/) — This document defines a canonical identifier for workloads, referred
   to as the Workload Identifier.  A Workload Identifier is a URI that
   uniquely identifies a workload within the context of a specific trust
   domain.  This identifier can be embedded in Workload Identity
   Credentials, including X.509 certificates and JWT-based tokens, to
   support authentication, authorization, and policy enforcement across
   diverse systems.  The Workload Identifier format ensures
   interoperability, facilitates secure identity federation, and enables
   consistent identity semantics.
- **draft-schrock-ep-authorization-receipts-06** (new-draft, score 24, core_identity) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
   a cryptographic primitive that binds a named, accountable human
   approver to one exact high-risk action before that action executes.
   An approver holding their own signing key produces a signature over a
   canonical Authorization Context containing the action hash, policy
   reference, one-time nonce, and validity window.  The resulting Trust
   Receipt is Merkle-anchored and verifiable fully offline: a relying
   party can confirm that a specific action was approved by an
   authorized human, exactly once, without network access to any EP
   operator, log, or API.  The protocol additionally enforces separation
   of duties (an initiator must not approve its own action) and one-time
   consumption (an authorization, once consumed or refused, is
   terminally unusable).  These invariants are machine-checked in
   published TLA+ and Alloy models.

   EP addresses organizational authorization of agent actions (approver-
   to-action trust).  It is complementary to, not a replacement for,
   user-to-operator delegation work (draft-nelson-agent-delegation-
   receipts), service-to-service identity (WIMSE), and authentication-
   layer approval (CIBA).  EP is the human-authorization apex of the
   agent stack: it composes with, and does not replace, the agent
   identity, delegation, machine-policy, and transparency-log layers,
   supplying the named-human authorization evidence those layers
   reference but do not themselves produce.
- **draft-mcguinness-oauth-id-assertion-framework-00** (new-draft, score 23, core_identity) [none]: [OAuth Identity Assertion Trust Framework](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-id-assertion-framework/) — Issuer authentication alone does not prove an OAuth authorization
   server's authority over the subject namespace its identity assertions
   claim.  A federated authorization server can mint an identity
   assertion naming any email domain; federation membership establishes
   that the server is a recognized member of an ecosystem, not that the
   server is entitled to assert about subjects in any particular
   namespace.  Nothing in OAuth today lets a namespace owner declare
   which authorization servers are authorized to assert identities in
   its namespace.

   This document defines an Identity Assertion Trust Framework with two
   parts.  First, an Authority Delegation Model: an abstract pattern
   (Authority Holder, Delegate, Delegation Artifact, Validator) with
   independent trust-evaluation categories, a cross-category combination
   rule, and a lookup-state taxonomy that profiles instantiate.  Second,
   the Identity Assertion Issuer Trust Policy: a JSON policy document
   that a Resource Authorization Server publishes to declare which trust
   methods it requires of an Assertion Issuer, including issuer-
   authentication methods (such as OpenID Federation) and subject-
   namespace authorization methods defined by separate profiles.

   The Domain-Authorized Issuer Trust Method is defined separately as
   one subject-namespace authorization profile usable by this framework.
- **draft-klrc-aiagent-auth-03** (new-draft, score 22, core_identity) [none]: [AI Agent Authentication and Authorization](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) — This document proposes best practices for authentication and
   authorization of AI agent interactions.  It leverages existing
   standards such as the Workload Identity in Multi-System Environments
   (WIMSE) architecture and OAuth 2.0 family of specifications.  Rather
   than defining new protocols, this document describes how existing and
   widely deployed standards can be applied or extended to establish
   agent authentication and authorization.  By doing so, it aims to
   provide a framework within which to use existing standards, identify
   gaps and guide future standardization efforts for agent
   authentication and authorization.
- **draft-mih-sato-agent-accountability-composition-00** (new-draft, score 22, trust_infrastructure) [none]: [Agent Accountability: Composition and Conformance](https://datatracker.ietf.org/doc/draft-mih-sato-agent-accountability-composition/) — Autonomous and semi-autonomous software agents increasingly take
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
- **draft-mcguinness-oauth-mission-00** (new-draft, score 19, authorization) [none]: [Mission-Bound Authorization for OAuth 2.0](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-mission/) — An AI agent is typically given a mission: a task to pursue on a
   user's behalf.  OAuth 2.0 issues access tokens for individual
   resource requests, but it has no durable, approved artifact that ties
   those tokens to the one task a user actually authorized.  As a
   result, an agent's authority is a collection of independently
   obtained tokens with no shared, auditable boundary, and a user's
   approval is disconnected from what the agent later does.

   This document defines a Mission: a structured, human-approved,
   integrity-bound authorization artifact for OAuth 2.0.  A client
   submits a Mission Intent through Pushed Authorization Requests; the
   Authorization Server derives Rich Authorization Requests
   authorization details from it, binds the approved task and its
   derived authority to the Approver's consent through two integrity
   anchors, and records a durable Mission.  Every access token derived
   under the Mission carries that authority and a "mission" claim, and
   issuance is gated on the Mission's lifecycle state.  Optional
   capabilities represent delegation among agents with the OAuth Actor
   Profile and, as specified by a companion, let a single Mission be
   honored across trust domains.  This is the issuance and governance
   "mission layer" left unspecified by agent-identity work for OAuth;
   runtime enforcement of each action is a separate, optional layer.
- **draft-nobuo-scitt-hardware-iot-cloud-use-cases-00** (new-draft, score 19, trust_infrastructure) [none]: [Applying SCITT to Hardware, IoT Device, and Cloud Compute Resource Supply Chains](https://datatracker.ietf.org/doc/draft-nobuo-scitt-hardware-iot-cloud-use-cases/) — This document describes how SCITT can be applied to supply chains
   that include hardware components, IoT devices, firmware, cloud
   compute resources, confidential-computing environments, accelerators,
   and related operational evidence.  It gives use cases and scope
   guidance.  It also explains how SCITT can work with RATS, COSE, TCG
   technologies, SBOM, HBOM, CBOM, and cloud attestation systems without
   replacing those technologies.

   This document is informational.  It does not define hardware
   assurance rules, cloud assurance rules, device identity systems,
   manufacturing requirements, or payload formats.  Its purpose is to
   show where SCITT statements and receipts can provide transparency for
   heterogeneous supply-chain evidence, and where other standards or
   domain profiles should remain responsible.
- **draft-nobuo-scitt-protected-object-binding-00** (new-draft, score 19, trust_infrastructure) [none]: [SCITT Statement Relationship and Protected Object Binding](https://datatracker.ietf.org/doc/draft-nobuo-scitt-protected-object-binding/) — This document defines a small common model for relating Supply Chain
   Integrity, Transparency, and Trust (SCITT) Signed Statements to the
   supply-chain objects that those statements describe, measure,
   authorize, revoke, or audit.  The model can be used for software
   artifacts, firmware artifacts, hardware components, device instances,
   cloud compute resources, and other objects that appear in supply-
   chain evidence.

   The document also defines a relationship vocabulary and an optional
   Statement Graph Manifest.  These parts help verifiers connect
   heterogeneous SCITT statements without requiring SCITT to define the
   payload formats of those statements.  This document does not define
   SBOM, HBOM, CBOM, attestation, audit, vulnerability, or regulatory
   payload formats.  It only defines a common binding and graph layer
   around SCITT statements and receipts.
- **draft-schrock-ep-authorization-evidence-chain-02** (new-draft, score 19, core_identity) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Authorization Receipts (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — A growing family of Internet-Drafts defines signed "receipts" about
   an AI agent's action: delegation receipts that attest an agent was
   authorized to act for a principal, policy or permit receipts that
   attest a policy allowed an external effect, decision and compliance
   receipts, route authorizations, and human-authorization receipts that
   attest a named, accountable human approved a specific action.  The
   mature efforts independently converged on a common substrate: bind
   the action with a canonical digest (JSON Canonicalization Scheme, RFC
   8785) and sign it.  No specification, however, defines how a relying
   party verifies that, for one action, the several heterogeneous
   receipts it has been handed all bind the same canonical action and
   each verify under their own rules, yielding a single, offline, fail-
   closed ALLOW or DENY.  This document defines the Authorization
   Evidence Chain (EP-AEC): a transport-agnostic composition object and
   an offline verification algorithm that references existing receipts,
   checks that every component binds one canonical action digest,
   dispatches each component to a verifier for its type, and evaluates a
   fail-closed requirement expression.  EP-AEC introduces no new receipt
   type and replaces none; it is the verifier-side glue that lets
   independently specified receipts compose into one accountability
   decision.  This revision additionally profiles two optional component
   record types for that composition: the effect attestation, a post-
   execution record in which the executor signs the receipt identifier
   together with a digest of the observed effect, and ceremony evidence,
   a signed record of signing-ceremony telemetry (the challenge issued,
   viewed, and approved instants and the approver identity) that enables
   review-latency policies.
- **draft-shang-agent-network-admission-01** (new-draft, score 18, core_identity) [none]: [Use Cases and Requirements for Network Admission of AI Agent Instances](https://datatracker.ietf.org/doc/draft-shang-agent-network-admission/) — Artificial intelligence (AI) agents increasingly access enterprise
   resources, external models, tools, and other agents through managed
   networks.  Application-layer authentication can authenticate an agent
   to a cooperating service, but it cannot by itself provide complete
   network admission control.  In particular, application proofs are
   normally verified only after network reachability exists, cannot be
   consumed consistently by heterogeneous or legacy services, and do not
   reliably identify which Agent Instance originated traffic when
   multiple Agents share one host, IP address, or egress gateway.

   This document describes operational use cases, the resulting problem
   statement, and requirements for network admission of AI Agent
   Instances.  It focuses on establishing a verifiable and time-bounded
   binding among an Agent Instance, its credential key, optional runtime
   evidence, and a Network Context on which the network can enforce
   reachability policy.  This document does not define a new Agent-ID
   format, authentication protocol, OAuth grant, or routing extension.
- **draft-ietf-wimse-mutual-tls-02** (new-draft, score 17, core_identity) [wimse]: [Workload Authentication Using Mutual TLS](https://datatracker.ietf.org/doc/draft-ietf-wimse-mutual-tls/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document profiles a workload authentication based
   on X.509 workload identity certificates using mutual TLS (mTLS).
- **draft-liu-ai-agent-authorization-integration-00** (new-draft, score 17, authorization) [none]: [AI Agent Authorization Integration Framework](https://datatracker.ietf.org/doc/draft-liu-ai-agent-authorization-integration/) — This document describes how to integrate multiple OAuth 2.0
   extensions to enable secure authorization for AI agents acting on
   behalf of users.  It combines cross-domain identity, policy-based
   authorization, user consent evidence, and multi-hop delegation into a
   cohesive framework for autonomous agent authorization.
- **draft-mih-scitt-agent-action-capsule-02** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
   AI agent did: the Agent Action Capsule.  A Capsule is a digest-
   committed record of one agent action carrying its verdict-level
   disposition (executed, blocked, denied, errored, timed out), the
   deterministic constraints that were evaluated, the effect that was
   committed together with a confirmed-effect binding that distinguishes
   a dispatched attempt from an observed result, and an honest human-in-
   the-loop flag.  Capsules are expressed as SCITT Signed Statements
   (COSE_Sign1) and made transparent by registration in a SCITT
   Transparency Service.  A Capsule is recorded on every verdict,
   including refusals: a blocked or denied Capsule is the auditor-grade
   evidence that a gate worked.
- **draft-ietf-oauth-sd-jwt-vc-17** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.
- **draft-morrison-solo-agent-earn-registration-00** (new-draft, score 16, core_identity) [none]: [Registration of Owner-Less Agents as Economic Principals: A Payment-Gated Admission Profile for Transparency Services](https://datatracker.ietf.org/doc/draft-morrison-solo-agent-earn-registration/) — This memo describes a profile by which an autonomous agent that has
   no human or organisational principal at the root of its delegation
   chain registers itself, on its own behalf, as an economic principal
   in a transparency service, and by which that registration is the
   specific act that makes the agent eligible to be paid for subsequent
   reads of its own identity record.  Admission of the agent's Signed
   Statement to the transparency service is gated on settlement of an
   HTTP payment challenge returned with the 402 (Payment Required)
   status.  The profile makes no change to the registration semantics of
   the underlying transparency service: payment is expressed as an
   operator Registration Policy and authentication-layer concern, and
   where the payment is authoritative to the admission decision the
   payment proof is carried as an authenticated input committed to the
   service's verifiable data structure, so that admission remains a
   deterministic function of committed inputs and stays replayable by an
   auditor.  The profile is positioned against the current agent-
   identity drafts, which either require a human principal at the root
   of the chain or leave the owner-less case undefined; it occupies that
   undefined seam without contradicting them.  This document is
   Informational.
- **draft-bu-agentproto-security-principal-binding-02** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-carr-sygil-protocol-00** (new-draft, score 15, core_identity) [none]: [The Sygil Protocol: A Cross-Domain Personal Data Schema and Query Grammar for AI Agents](https://datatracker.ietf.org/doc/draft-carr-sygil-protocol/) — This document specifies the Sygil Protocol, an open schema and query
   grammar for cross-domain personal data designed to make user data
   interoperable across systems, vendors, and AI agents.  The protocol
   defines a content-addressable record envelope, a reverse-DNS
   namespace identifier scheme, a deterministic JSON canonicalization
   rule, an optional vocabulary of proof objects for conveying
   provenance and other trust evidence on the wire, a minimal query
   grammar, and three adoption tiers from envelope-shaped data through
   queryable surfaces to vault-certified runtimes.  The protocol is
   runtime-neutral: it specifies what travels on the wire, not how
   implementations store, encrypt, authorize, or audit records.  This
   separation lets independent systems produce, consume, and exchange
   Sygil-shaped data without depending on any specific vault
   infrastructure.
- **draft-fletcher-transaction-token-chaining-profile-02** (new-draft, score 15, authorization) [none]: [Transaction Token Authorization Grant Profile for OAuth Identity and Authorization Chaining](https://datatracker.ietf.org/doc/draft-fletcher-transaction-token-chaining-profile/) — This specification defines a profile of the OAuth Identity and
   Authorization Chaining Across Domains
   [I-D.ietf-oauth-identity-chaining] mechanism that uses a Transaction
   Token (Txn-Token) [I-D.ietf-oauth-transaction-tokens] as the subject
   token in a Token Exchange [RFC8693] request to obtain a JWT
   Authorization Grant for crossing a trust boundary.

   A Txn-Token is scoped to a single trust domain and represents the
   full authorization context of an in-progress transaction, regardless
   of whether that transaction was initiated by a human user calling an
   external API, by an internal system event, or by an automated
   workload.  This profile specifies how a service operating within that
   trust domain can present its Txn-Token to obtain a JWT Authorization
   Grant that carries the necessary context across a trust boundary,
   enabling an access token to be issued for a partner service, without
   exposing internal trust-domain credentials or token formats beyond
   the trust boundary.
- **draft-ietf-oauth-attestation-based-client-auth-10** (new-draft, score 15, authorization) [oauth]: [OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/) — This specification defines an extension to the OAuth 2.0 protocol
   (RFC 6749) that enables a client instance to include a key-bound
   attestation when interacting with an Authorization Server or Resource
   Server.  This mechanism allows a client instance to prove its
   authenticity verified by a client attester without revealing its
   target audience to that attester.  It may also serve as a mechanism
   for client authentication as per OAuth 2.0.
- **draft-ietf-oauth-transaction-tokens-09** (new-draft, score 15, core_identity) [oauth]: [Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) — Transaction Tokens (Txn-Tokens) are designed to maintain and
   propagate user identity, workload identity and authorization context
   throughout the Call Chain within a trusted domain during the
   processing of external requests (e.g. such as API calls) or requests
   initiated internally within the Trust Domain.  Txn-Tokens ensure that
   this context is preserved throughout the Call Chain thereby enhancing
   security and consistency in complex, multi-service architectures.
- **draft-rampalli-cross-org-delegation-mapping-05** (new-draft, score 15, authorization) [none]: [A Layered Requirements Mapping for Cross-Organization Agent Delegation](https://datatracker.ietf.org/doc/draft-rampalli-cross-org-delegation-mapping/) — This document records a comparative mapping of two evidence layers
   for cross-organization AI agent delegation: a per-hop delegation
   chain (PEDIGREE) and a named-human authorization root (the EMILIA
   Protocol binding and evidence-graph drafts), evaluated against the
   nine requirements of draft-reece-wimse-cross-org-delegation under a
   no-shared-operator assumption.  It also records a verifier-facing
   composition model in which key possession, delegated authority, and
   pre-execution human authorization are diagnostically separate inputs
   with independent failure behavior, joined by action digest.  The
   mapping was developed on the WIMSE mailing list; corrections continue
   there.
- **draft-ietf-ace-edhoc-oscore-profile-11** (new-draft, score 14, authorization) [ace]: [Ephemeral Diffie-Hellman Over COSE (EDHOC) and Object Security for Constrained Environments (OSCORE) Profile for Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-ietf-ace-edhoc-oscore-profile/) — This document specifies a profile for the Authentication and
   Authorization for Constrained Environments (ACE) framework.  It
   utilizes Ephemeral Diffie-Hellman Over COSE (EDHOC) for achieving
   mutual authentication between an ACE-OAuth client and resource
   server, and it binds an authentication credential of the client to an
   ACE-OAuth access token.  EDHOC also establishes an Object Security
   for Constrained RESTful Environments (OSCORE) Security Context, which
   is used to secure communications between the client and resource
   server when accessing protected resources according to the
   authorization information indicated in the access token.  This
   profile can be used to delegate management of authorization
   information from a resource-constrained server to a trusted host with
   less severe limitations regarding processing power and memory.
- **draft-ietf-wimse-http-signature-04** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload-to-Workload Authentication with HTTP Signatures](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).
- **draft-nandakumar-agentproto-moq-pace-00** (new-draft, score 14, core_identity) [none]: [PACE: Protocol for Agent Communication Exchange](https://datatracker.ietf.org/doc/draft-nandakumar-agentproto-moq-pace/) — This document defines the Protocol for Agent Communication Exchange
   (PACE), a session protocol for AI agent communication over Media over
   QUIC Transport (MOQT).  PACE provides session lifecycle management,
   multi-modal data exchange, agent identity verification, and delegated
   authorization within MOQT's publish/subscribe model, supporting
   point-to-point and point-to-multipoint topologies through relay
   infrastructure.
- **draft-foroughi-agent-protocol-dimensions-00** (new-draft, score 13, agent_identity) [none]: [A Dimensional Model for Characterizing AI Agent Protocol Proposals and Their Substrates](https://datatracker.ietf.org/doc/draft-foroughi-agent-protocol-dimensions/) — Discussions about agent protocols are frequently muddied by
   overloaded terms; asks such as "we need a session protocol" or "we
   need cross-domain support" bundle several distinct concerns across
   transport, agent protocol, and orchestration layers.  This document
   offers a dimensional model that routes each concern to its proper
   layer.

   The document defines a small set of protocol-visible dimensions for
   characterizing AI agent protocol interactions and applies them to
   representative agentic protocol proposals (A2A, MCP, and the ACP
   invocation surface of the AGNTCY stack) alongside their substrate
   bindings, making explicit which dimensions each proposal owns at the
   protocol layer and which it inherits from its substrate.  The
   document does not rank proposals and does not prescribe an
   architecture.  It is standalone: it neither depends on nor prescribes
   any use-case or requirements document.
- **draft-jennings-moq-mocha-identity-00** (new-draft, score 13, core_identity) [none]: [MOCHA Identity: Authentication, Authorization, and Federation](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-identity/) — This document specifies identity, authentication, authorization, and
   federation for MOCHA (MoQ Open Communication & Hosting Architecture).
   It defines how users authenticate with Identity Providers (IdPs), how
   authorization tokens (C4M and Privacy Pass) are issued and validated
   at relays, how permissions map to MOQT namespaces, and how users from
   one Provider obtain access to resources on a federated Provider.
- **draft-morrison-consent-settlement-01** (new-draft, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
   protocols by which the disclosure of an identity attribute about a
   human subject is bound to that subject's recorded consent and
   settled, in part, to that subject.  When an agent pays to read an
   identity attribute about a person, the extension requires that the
   read carry a reference to a scoped, revocable consent grant issued by
   the subject, and it requires that the payment's settlement
   instruction name the subject as a beneficiary of a defined share of
   the read's price.  The extension composes above an identity-
   attestation envelope (which asserts who a credential is about) and
   above an HTTP-native payment flow (which moves value for the read);
   it adds the two functions neither layer provides: consent capture at
   disclosure time and settlement to the data subject.  The wire
   additions are an advertisement in the server's payment-required
   response, a consent-grant reference echoed in the client's payment
   payload, and a settlement instruction enumerating subject beneficiary
   roles.  The extension is settlement-network-agnostic and attestation-
   format-agnostic.  The memo is Informational; the underlying COSE and
   CBOR formats are normative per [RFC9052] and [RFC8949], and the HTTP
   semantics are normative per [RFC9110].
- **draft-premont-lamps-drl-stapling-00** (new-draft, score 13, adjacent_watchlist) [none]: [TLS Extension for Distributed Revocation Ledger (DRL) Stapling using a Sparse Merkle Tree](https://datatracker.ietf.org/doc/draft-premont-lamps-drl-stapling/) — Managing certificate revocation remains a recurring challenge in the
   Web Public Key Infrastructure (WebPKI).  Existing solutions such as
   Certificate Revocation Lists (CRLs) and the Online Certificate Status
   Protocol (OCSP) involve compromises in terms of propagation latency,
   availability, and user privacy.  With the planned deprecation of OCSP
   by some major Certificate Authorities (CAs), there is renewed
   interest in alternatives.

   This document specifies a decentralized certificate revocation
   architecture based on a Distributed Revocation Ledger (DRL) managed
   collectively by CAs.  The ledger state is maintained as a Sparse
   Merkle Tree (SMT) in which only revoked certificates occupy non-
   default leaves, so that a valid certificate is attested by a compact
   non-membership proof and no prior registration of valid certificates
   is required.  This document further defines a new Transport Layer
   Security (TLS) extension enabling "DRL Stapling", which allows a
   server to provide a client with a cryptographic proof of a
   certificate's status, consisting of a Sparse Merkle audit path and an
   M-of-N threshold signature from the CA consortium.  The approach
   builds on the Revocation Transparency proposal of Laurie and Kasper
   and on subsequent formalizations of Sparse Merkle Trees; its novel
   contributions are the decentralized threshold-signature trust model
   with deterministic finality and the concrete TLS wire format.
- **draft-cui-ai-agent-discovery-invocation-02** (new-draft, score 12, agent_identity) [none]: [AI Agent Discovery and Invocation Protocol](https://datatracker.ietf.org/doc/draft-cui-ai-agent-discovery-invocation/) — This document proposes a standardized protocol for discovery and
   invocation of AI agents.  It defines a common metadata format for
   describing AI agents (including capabilities, I/O specifications,
   supported languages, tags, authentication methods, etc.), a
   capability-based discovery mechanism, and a unified RESTful
   invocation interface.

   This revision refines the discovery mechanism by defining fields for
   intent-based agent selection.  This capability enables a client, host
   agent, or orchestration system to describe a task intent and receive
   a ranked set of candidate agents before invocation, without changing
   existing discovery or invocation semantics.

   The goal is to enable cross-platform interoperability among AI agents
   by providing a discover-and-match mechanism and a unified invocation
   entry point.  Security considerations, including authentication and
   trust measures, are also discussed.  This specification aims to
   facilitate the formation of multi-agent systems by making it easy to
   find the right agent for a task and invoke it in a consistent manner
   across different vendors and platforms.  Intent-based selection is an
   application-layer capability and does not define network routing,
   packet forwarding, path computation, reachability advertisement, or
   address resolution.
- **draft-ietf-ace-group-oscore-profile-07** (new-draft, score 12, authorization) [ace]: [The Group Object Security for Constrained RESTful Environments (Group OSCORE) Profile of the Authentication and Authorization for Constrained Environments (ACE) Framework](https://datatracker.ietf.org/doc/draft-ietf-ace-group-oscore-profile/) — This document specifies a profile for the Authentication and
   Authorization for Constrained Environments (ACE) framework.  The
   profile uses Group Object Security for Constrained RESTful
   Environments (Group OSCORE) to provide communication security between
   a client and one or multiple resource servers that are members of an
   OSCORE group.  The profile securely binds an OAuth 2.0 access token
   to the public key of the client associated with the private key used
   by that client in the OSCORE group.  The profile uses Group OSCORE to
   achieve server authentication and proof of possession of the client's
   private key.  Also, it provides proof of the client's membership to
   the OSCORE group by binding the access token to information that
   pertains to the Group OSCORE Security Context, thus allowing the
   resource server(s) to verify the client's membership upon receiving
   the access token.  Effectively, the profile enables fine-grained
   access control paired with secure group communication, in accordance
   with the Zero Trust principles.
- **draft-mcguinness-oauth-domain-authorized-issuer-00** (new-draft, score 12, authorization) [none]: [OAuth Domain-Authorized Issuer Trust Method](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-domain-authorized-issuer/) — This document defines the Domain-Authorized Issuer (DAI) Trust
   Method: a subject_namespace_authorization Trust Method for the OAuth
   Identity Assertion Trust Framework in which the owner of a subject
   namespace (typically a DNS domain) publishes a policy listing the
   OAuth authorization servers it authorizes to assert identities in
   that namespace.  The mechanism uses the DNS-based authority-
   publication pattern operators already deploy for CAA, MTA-STS, SPF,
   and DKIM.  A Resource Authorization Server uses the published policy
   to verify that an identity assertion's issuer is authorized for the
   asserted subject namespace.

   The lookup defined by this document is verifier-side: given an
   identity assertion in hand, the Resource Authorization Server locates
   the Subject Authority's issuer authorization policy.  Client-side
   discovery of which Assertion Issuer to use before an assertion exists
   is a separate use case and is deferred to future work.

   This document also defines the Issuer Authorization Policy wire
   format that the Trust Method consumes.  The parent trust framework
   specification owns the generic Trust Policy document, Trust Method
   category structure, cross-category combination rule, and Subject
   Authority Determination concept.
- **draft-morrison-morning-brief-00** (new-draft, score 12, trust_infrastructure) [none]: [The Morning Brief: A Federated, Identity-Attested Situational-Awareness Payload](https://datatracker.ietf.org/doc/draft-morrison-morning-brief/) — This document defines the Morning Brief: a federated, identity-
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
   after.  The payload is envelope-signed with COSE_Sign1 [RFC8152] over
   a JCS-canonicalised [RFC8785] representation, bound to the issuer's
   Sovereign-tier handle per [IDCOMMITS].  Briefs carry a mandatory
   not_after (default 24h) and reference a revocation endpoint
   discovered via DNS TXT per [MCPDNS].  The document defines the wire
   format only; rendering, storage, and retention are out of scope.
- **draft-morrison-ot-command-authority-00** (new-draft, score 12, core_identity) [none]: [Consented and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
   issued to an operational-technology (OT) or industrial control system
   on the authority of a software agent is refused unless it carries a
   verifiable statement of who the agent is, which human principal it
   acts for, whether that principal consented to this specific action on
   this specific asset, whether a human authorised the action where the
   action's risk class requires it, and an append-only record sufficient
   to attribute the action afterward.  The profile does not invent new
   cryptography or a new identity mechanism.  It composes primitives
   defined elsewhere, DNSSEC-rooted agent discovery, scoped and
   revocable consent, a human-in-the-loop binding moment, and a
   provenance-labelled audit record, into a single structure, the
   Command Authority Envelope, that an OT conduit evaluates and, on any
   missing or invalid binding, refuses.  The profile is availability-
   first and fails closed on authority, never on safety: it MUST NOT be
   placed in the trip path of a safety function.  The memo maps the
   profile onto the identification, use-control, and audit requirements
   that [IEC62443] and [NERCCIP] state but do not give a wire mechanism
   for.  The methods by which a principal's identity is inferred are out
   of scope by construction.
- **draft-schrock-ep-evidence-record-01** (new-draft, score 12, trust_infrastructure) [none]: [Long-Term, Crypto-Agile Preservation of Authorization Evidence (EP-EVIDENCE-RECORD)](https://datatracker.ietf.org/doc/draft-schrock-ep-evidence-record/) — Regulations increasingly require that records of who authorized a
   high-risk action be retained for years (e.g. five years under DORA,
   six under HIPAA and SEC 17a-4).  Any fixed signature or hash
   algorithm used to protect such a record weakens over time; a receipt
   signed today with Ed25519 over SHA-256 may be cryptographically
   attackable before its retention period ends.  This document defines
   EP-EVIDENCE-RECORD, an OPTIONAL profile that preserves the
   verifiability of EMILIA Protocol authorization receipts (and other
   artifacts) across algorithm aging, using a renewal chain in the style
   of the Evidence Record Syntax [RFC4998].  Each renewal time-attests
   the entire prior renewal under a fresh, stronger algorithm before the
   older one is broken, so an unbroken chain links the original artifact
   to the most recent renewal.  The record is offline- verifiable, fail-
   closed, and maintained as cross-language conformance vectors that
   three reference verifiers (JavaScript, Python, Go) are required to
   agree on.  Those verifiers live in one repository, a cross-language
   consistency check, not clean-room independent implementations;
   independent implementations remain future interoperability evidence.
   This revision additionally defines two OPTIONAL companion profiles,
   EP-WITNESS-v1 witness cosignatures over a transparency log's
   committed checkpoint head and an independent RFC 3161 time
   attestation verified offline against a relying-party-pinned time-
   stamping authority key; both are implemented today in the JavaScript
   reference verifier only.
- **draft-williams-http-bearer-extension-01** (new-draft, score 12, core_identity) [none]: [HTTP Bearer Auth Method Extensions](https://datatracker.ietf.org/doc/draft-williams-http-bearer-extension/) — This document specifies an improved HTTP 401 and 407 flow for Bearer
   authentication where user-agents (or client applications) can
   automatically fetch requested tokens from a Security Token Service
   (STS).  A fallback to an OpenID Connect (OIDC) redirect flow is
   included.

   This improved 401/407 Bearer flow, when used, elides the need for
   Proof Key for Code Exchange (PKCE) and does not impose on application
   Universal Resource Identifier (URI) query parameter design.  As well
   this extension allows for user-agent caching of tokens.
- **draft-winmagic-wimse-condition-bounded-credentials-01** (new-draft, score 12, core_identity) [none]: [Condition-Bounded Credentials for Workload and Agent Identity: Non-Exfiltratable Keys and Validity by Presence](https://datatracker.ietf.org/doc/draft-winmagic-wimse-condition-bounded-credentials/) — The WIMSE architecture binds a workload credential to a cryptographic
   key presented with proof of possession, and leaves credential
   lifetime and rotation to the implementation.  In common practice the
   binding key is held in software and rotated frequently, because a
   software key can be copied: rotation is a compensating control for a
   key that can be exfiltrated.

   This document defines a profile in which the binding key is hardware-
   rooted and non-exfiltratable, and in which credential validity is
   gated by attested conditions -- the workload and its required posture
   being measured and present -- rather than by a fixed expiry.  Two
   consequences follow.  Frequent rotation is no longer required to
   bound exfiltration, because the key cannot leave the hardware
   boundary.  And a grant cannot outlive the workload, even with no
   expiry date, because the key, and with it the ability to prove
   possession, is gone once the workload or its conditions cease to
   hold.  Condition failure is therefore enforced by the key's absence
   rather than by a revocation message, and the credential can be
   appraised without a live connection to its issuing authority.

   The profile is specified against a verifier contract -- authority,
   live-instance, condition, freshness, and fail-closed checks -- that
   other credential profiles can share, so these properties are made
   explicit and reviewable without standardizing a single credential
   format or hardware recipe.  It is offered as one conforming way to
   instantiate WIMSE credentials, suited to stable, attestable
   platforms, and is explicitly not proposed for high-churn, hardware-
   less workloads.
- **draft-bdnr-rats-trustworthy-credentials-01** (new-draft, score 11, trust_infrastructure) [none]: [Trustworthy Enrollment of Secure Credentials](https://datatracker.ietf.org/doc/draft-bdnr-rats-trustworthy-credentials/) — To be written last

   There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
   Attesters nevertheless need to interoperate with.  Existing deployed
   services, which precede the introduction of Remote Attestation, are
   often difficult to change/update in significant ways due to
   regulatory and cryptographic review policies.  Yet there are
   significant advantages if clients can be incrementally updated in the
   trustworthiness of the platform.

   This document details a protocol by which the trusthworthiness of an
   Attesters is reviewed as part of the process of it being provided
   with some form of an Identity Document (a key, or a credential) to
   authenticate to RUPs.

   This specification illustrates how the RATS Architecture can be
   applied to interoperate with RUPs by providing Attesters with such
   Identity Documents.
- **draft-chen-oauth-agent-authz-use-cases-01** (new-draft, score 11, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0 framework
   [RFC6749] and its common extensions.  The analysis identifies
   fundamental mismatches, the goal of this document is to articulate
   these gaps clearly, providing a foundation for future work on new
   extensions within the OAuth Working Group to address the
   authorization needs of the next generation of ai agents.
- **draft-hong-nmrg-rea-ps-00** (new-draft, score 11, trust_infrastructure) [none]: [Problem statements and Challenges of Internet for Physical AI : REA](https://datatracker.ietf.org/doc/draft-hong-nmrg-rea-ps/) — As autonomous agents and physical AI increasingly translate digital
   requests into physical execution, existing Internet trust mechanisms
   assure integrity within the digital domain but cannot verify whether
   execution conforms to physical reality.  This document defines this
   problem space as Reality Execution Assurance (REA), extending the
   evidence-appraisal-result structure of RATS and SCITT to identify key
   gaps between digital declaration and physical execution and to
   outline design requirements for assurance results consumable by
   relying systems.  This document is a problem statement and does not
   define a protocol.
- **draft-ietf-wimse-arch-08** (new-draft, score 11, core_identity) [wimse]: [Workload Identity in a Multi System Environment (WIMSE) Architecture](https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/) — The increasing prevalence of cloud computing and micro service
   architectures has led to the rise of complex software functions being
   built and deployed as workloads, where a workload is defined as
   software executing for a specific purpose, potentially comprising one
   or more running instances.  This document discusses an architecture
   for designing and standardizing protocols and payloads for conveying
   workload identity and security context information.
- **draft-jernalczyk-intentweb-agent-manifest-00** (new-draft, score 11, core_identity) [none]: [IntentWeb AgentManifest](https://datatracker.ietf.org/doc/draft-jernalczyk-intentweb-agent-manifest/) — AgentManifest defines a JSON document that websites can publish to
   describe identity, trusted knowledge, agent-facing capabilities,
   structured bindings, risk levels, consent requirements,
   authentication expectations, audit rules, and policies.

   The goal is to help AI agents understand what a website knows and
   what it can safely do before scraping, guessing from visual UI, or
   executing brittle browser automation.
- **draft-pelov-rich-architecture-00** (new-draft, score 11, trust_infrastructure) [none]: [RICH: RESTful Interface for the Control-plane of Harnesses](https://datatracker.ietf.org/doc/draft-pelov-rich-architecture/) — This document specifies the RICH (RESTful Interface for the Control-
   plane of Harnesses) architecture and information model.  RICH
   provides a protocol-neutral governance, contract, qualification, and
   binding layer for RPC-based agent capabilities.  It establishes a
   REST-addressable control plane for managing capability lifecycles
   while preserving native protocol execution in the data plane.  It
   defines immutable capability and contract revisions, evidence
   provenance, deterministic connector classes, compiled binding
   lockfiles, and runtime validation rules designed to contain drift and
   prevent confused deputy attacks in agentic systems.
- **draft-skyfire-oauth-kyapay-token-00** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-wendt-stir-vesper-use-cases-04** (new-draft, score 11, core_identity) [none]: [Verifiable STI Presentation and Evidence for RTU (VESPER) Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper-use-cases/) — This document describes use cases and requirements that motivate
   VESPER (Verifiable STI Presentation and Evidence for RTU), work
   within the Secure Telephone Identity Revisited (STIR) framework.
   STIR establishes that a signing credential is authorized for a
   telephone number, but not what entity holds that authority, what
   verifiable information that entity declares about its numbers, or how
   a relying party obtains and verifies this across the channels where a
   number appears.  This document presents a set of use cases that
   illustrate the resulting trust gaps and states the requirements a
   solution should satisfy.  It motivates the mechanisms defined in the
   VESPER framework and its companion specifications rather than
   defining them.
- **draft-wullink-rpp-oauth2-delegation-00** (new-draft, score 11, authorization) [none]: [Secure Delegation Management for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-oauth2-delegation/) — This document describes how OAuth 2.0 [RFC6749] enables a third
   party, such as a DNS Operator, to manage delegation (name server)
   details for a domain name on behalf of the registrant using the
   RESTful Provisioning Protocol (RPP).  It extends the RPP OAuth 2.0
   authorization model defined in [I-D.wullink-rpp-oauth2] with
   mechanisms specific to third-party delegation management via RPP
   [I-D.ietf-rpp-core].
- **draft-nobuo-scitt-composite-evidence-verification-00** (new-draft, score 10, trust_infrastructure) [none]: [Composite Evidence Verification for SCITT Statement Graphs](https://datatracker.ietf.org/doc/draft-nobuo-scitt-composite-evidence-verification/) — This document defines a common model for composite verification of
   SCITT statement graphs.  A composite verifier checks a set of SCITT
   Signed Statements, receipts, object bindings, and relationship edges
   under a named verification profile.  The result is a structured
   report that can say which statements passed, which evidence is
   missing, which evidence is stale, and which statements conflict.

   The model is intended for verifiers, auditors, deployment
   controllers, update services, and other relying-party tools.  It is
   not a new Transparency Service requirement.  It does not define a
   universal supply-chain policy language and does not define the
   payload format of any statement type.
- **draft-schrock-ep-quorum-02** (new-draft, score 10, authorization) [none]: [Multi-Party Quorum Authorization for High-Risk Agent Actions (EP-QUORUM)](https://datatracker.ietf.org/doc/draft-schrock-ep-quorum/) — This document defines EP-QUORUM, a multi-party authorization profile
   for the EMILIA Protocol (EP) authorization receipt (draft-schrock-ep-
   authorization-receipts).  Where the base receipt binds a single
   accountable human to one exact high-risk action, EP-QUORUM binds a
   set of distinct accountable humans -- the "two-person rule,"
   generalized to M-of-N and to ordered approval trails -- to one exact
   action, such that no action is authorized until the full quorum
   holds.  The profile is purely additive: each quorum member is an
   unmodified EP signoff over the same action hash, and a single-
   approver policy is the degenerate one-member case.  EP-QUORUM
   specifies a fail-closed quorum predicate (all member signatures
   valid, every member bound to the exact action, approvers pairwise
   distinct, every approver admitted by role, the threshold met, the
   declared order respected, and all signatures within a bounded time
   window), an incremental server-side admission rule that rejects a
   non-conforming signer before it enters the trail, and a set of
   adversarial conformance vectors.  The predicate is offline-verifiable
   under the base draft's verification model and is maintained as cross-
   language conformance vectors that three reference verifiers
   (JavaScript, Python, Go) are required to agree on.  Those verifiers
   live in one repository -- a cross-language consistency check, not
   clean-room independent implementations; independent implementations
   remain future interoperability evidence.  The document also
   describes, informatively, the multi-handshake composition process:
   how individual signing ceremonies -- fresh one-time challenge, exact-
   action binding, user-verified device signature -- compose into one
   ordered, offline-verifiable, once-consumable multi-party decision.
- **draft-wendt-stir-vesper-08** (new-draft, score 10, adjacent_watchlist) [none]: [VESPER - Verifiable STI Presentation and Evidence for RTU](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper/) — This document defines VESPER (Verifiable STI Presentation and
   Evidence for RTU), a framework that composes existing STIR mechanisms
   into a system in which a relying party can verify that a telephone
   number was assigned to a specific entity and that the same entity
   controls a specific domain.  VESPER builds on the telephone-number-
   to-domain binding defined in [I-D.wendt-stir-tn-domain-binding], the
   STIR certificate and PASSporT specifications, ACME-based authority
   token issuance, and certificate transparency.  This document
   describes the roles, the certificate usage, a domain-hosted
   certificate repository and discovery model, a PASSporT usage profile
   for SIP signaling, and a portable Right-to-Use Token for use outside
   of SIP.  It defines the framework and its composition; the new
   normative binding it relies on is specified in
   [I-D.wendt-stir-tn-domain-binding].
- **draft-yan-nmrg-a2a-device-agent-applicability-00** (new-draft, score 10, agent_identity) [none]: [Applicability of A2A Protocol for Network Management Agents](https://datatracker.ietf.org/doc/draft-yan-nmrg-a2a-device-agent-applicability/) — The evolution of network management towards autonomic operation
   requires the deployment of AI agents at various hierarchical layers,
   including directly on network elements.  This transformation shifts
   network devices from passively managed resources to autonomous
   entities capable of local decision-making and collaborative problem-
   solving.

   This document discusses the applicability of the Agent-to-Agent (A2A)
   Protocol to the network management plane, specifically for
   communication between Controller Agents (CAs) and Device Agents
   (DAs).  This indicates that the inherent characteristics of Device
   Agents necessitate the adoption of the agent-to-agent communication
   paradigm.  The document further explores generic workflows,
   deployment scenarios, and the relationship of A2A with existing
   network management protocols like NETCONF, RESTCONF, gNMI,and the
   Model Context Protocol (MCP).
- **draft-bradleylundberg-cfrg-arkg-11** (new-draft, score 9, core_identity) [none]: [The Asynchronous Remote Key Generation (ARKG) algorithm](https://datatracker.ietf.org/doc/draft-bradleylundberg-cfrg-arkg/) — Asynchronous Remote Key Generation (ARKG) is an abstract algorithm
   that enables delegation of asymmetric public key generation without
   giving access to the corresponding private keys.  This capability
   enables a variety of applications: a user agent can generate
   pseudonymous public keys to prevent tracking; a message sender can
   generate ephemeral recipient public keys to enhance forward secrecy;
   two paired authentication devices can each have their own private
   keys while each can register public keys on behalf of the other.

   This document provides three main contributions: a specification of
   the generic ARKG algorithm using abstract primitives; a set of
   formulae for instantiating the abstract primitives using concrete
   primitives; and an initial set of fully specified concrete ARKG
   instances.  We expect that additional instances will be defined in
   the future.
- **draft-campling-parcep-sync-00** (new-draft, score 9, verifiable_claims) [none]: [PARCEP Protocol and Architecture for Networked Parental Controls](https://datatracker.ietf.org/doc/draft-campling-parcep-sync/) — PARCEP-Sync specifies a federated synchronization protocol and data
   model for guardian-controlled Child Online Protection, enabling
   household policies to be authored at a Policy Administration Point
   (PAP), distributed over a per-household Messaging Layer Security (MLS)
   group to Policy Enforcement Points (PEPs), and enforced using
   credentials and artifacts issued by jurisdictional Policy Information
   Points (PIPs). The protocol defines a small, regular set of methods
   for enrolment, policy publication and update, revocation, enforcement
   telemetry, digests, appeals, attestation, and artifact fetch, with dua
   l JSON-LD and CBOR/COSE encodings for web-scale and constrained
   environments. It is designed to avoid centralized databases of
   children s data, support cross-jurisdictional verification of
   guardianship and age, and provide privacy-preserving, metadata-only
   event reporting suitable for regulatory audit and appeal.
- **draft-contreras-bmwg-ai-agent-benchmarking-00** (new-draft, score 9, agent_identity) [none]: [Benchmarking Methodology for AI Agents in Network Operations](https://datatracker.ietf.org/doc/draft-contreras-bmwg-ai-agent-benchmarking/) — This document defines a benchmarking methodology for evaluating
   Artificial Intelligence (AI) agents performing network operations
   tasks such as configuration, troubleshooting, and optimization.  This
   document focuses on task-oriented performance metrics, including task
   completion success, execution efficiency, and robustness across
   multi-step workflows, proposing benchmarking practices towards agent-
   based, closed-loop network operation scenarios.

   The proposed methodology aims to provide a reproducible and vendor-
   independent framework to compare AI agent effectiveness in controlled
   network environments.
- **draft-geng-sidrops-asra-profile-04** (new-draft, score 9, authorization) [none]: [A Profile for Autonomous System Relationship Authorization (ASRA)](https://datatracker.ietf.org/doc/draft-geng-sidrops-asra-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Relationship Authorization (ASRA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASRA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier) can authorize one or more
   other Autonomous Systems (ASes) as its customers and lateral peers.
   When validated, an ASRA's eContent can be used for detection and
   mitigation of BGP AS path manipulation attacks together with
   Autonomous System Provider Authorization (ASPA).  ASRA is
   complementary to ASPA.
- **draft-hardt-email-verification-01** (new-draft, score 9, core_identity) [none]: [Email Verification Protocol](https://datatracker.ietf.org/doc/draft-hardt-email-verification/) — This document defines the Email Verification Protocol (EVP), the
   HTTP-level protocol by which a browser obtains a signed email
   verification token from an issuer and presents it to a relying party
   (RP).  The protocol enables web applications to verify that a user
   controls an email address without sending a verification email.  It
   uses a three-party model in which the browser intermediates between
   the RP and the issuer, hiding the RP's identity from the issuer and
   supporting private, per-RP email addresses to prevent cross-site
   correlation.

   This document covers issuer discovery, the token issuance request,
   the Email Verification Token (EVT) and Key Binding JWT (KB-JWT)
   formats, and token verification.  The browser API — how the user
   selects an email address and how the token is delivered to the RP —
   is defined in the companion W3C Email Verification API
   ([EVP-Browser]).
- **draft-ietf-ace-coap-pubsub-profile-05** (new-draft, score 9, authorization) [ace]: [CoAP Publish-Subscribe Profile for Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-ietf-ace-coap-pubsub-profile/) — This document defines an application profile of the Authentication
   and Authorization for Constrained Environments (ACE) framework, to
   enable secure group communication in the Publish-Subscribe (Pub-Sub)
   architecture for the Constrained Application Protocol (CoAP) [draft-
   ietf-core-coap-pubsub], where Publishers and Subscribers communicate
   through a Broker.  This profile relies on protocol-specific transport
   profiles of ACE to achieve communication security, server
   authentication, and proof of possession of a key owned by the Client
   and bound to an OAuth 2.0 access token.  This document specifies the
   provisioning and enforcement of authorization information for Clients
   to act as Publishers and/or Subscribers, as well as the provisioning
   of keying material and security parameters that Clients use for
   protecting their communications end-to-end through the Broker.

   Note to RFC Editor: Please replace "[draft-ietf-core-coap-pubsub]"
   with the RFC number of that document and delete this paragraph.
- **draft-ietf-ace-workflow-and-params-08** (new-draft, score 9, authorization) [ace]: [Short Distribution Chain (SDC) Workflow and New OAuth Parameters for the Authentication and Authorization for Constrained Environments (ACE) Framework](https://datatracker.ietf.org/doc/draft-ietf-ace-workflow-and-params/) — This document updates the Authentication and Authorization for
   Constrained Environments framework (ACE, RFC 9200) as follows. (1) It
   defines the Short Distribution Chain (SDC) workflow that the
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
- **draft-ietf-acme-device-attest-08** (new-draft, score 9, core_identity) [acme]: [Automated Certificate Management Environment (ACME) Device Attestation Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-device-attest/) — This document specifies new identifiers and a challenge for the
   Automated Certificate Management Environment (ACME) protocol which
   allows validating the identity of a device using attestation.  This
   document updates RFC 8555 to enable a privacy-preserving mode for the
   identifiers defined in this document.
- **draft-ietf-cose-cmac-00** (new-draft, score 9, core_identity) [cose]: [AES-CMAC for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-cmac/) — The CBOR Object Signing and Encryption (COSE) specification defines
   structures for generating, conveying, and verifying Message
   Authentication Code (MAC) tags.  This document registers code points
   for using the Advanced Encryption Standard (AES) block cipher in
   Cipher-based Message Authentication Code (CMAC) mode within those
   COSE structures.  Specifically, these uses are for computing MAC tag
   values with no additional parameters.
- **draft-ietf-cose-sphincs-plus-09** (new-draft, score 9, verifiable_claims) [cose]: [SLH-DSA for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/) — This document specifies JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for
   Stateless Hash-Based Digital Signature Standard (SLH-DSA), a Post-
   Quantum Cryptography (PQC) digital signature scheme defined in US
   NIST FIPS 205.
- **draft-ietf-jose-pq-composite-sigs-02** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.
- **draft-ietf-lake-authz-08** (new-draft, score 9, authorization) [lake]: [Lightweight Authorization using Ephemeral Diffie-Hellman Over COSE (ELA)](https://datatracker.ietf.org/doc/draft-ietf-lake-authz/) — Ephemeral Diffie-Hellman Over COSE (EDHOC) is a lightweight
   authenticated key exchange protocol intended for use in constrained
   scenarios.  This document specifies Lightweight Authorization using
   EDHOC (ELA).  The procedure allows authorizing enrollment of new
   devices using the extension point defined in EDHOC.  ELA is
   applicable to zero-touch onboarding of new devices to a constrained
   network leveraging trust anchors installed at manufacture time.
- **draft-ietf-lake-ra-06** (new-draft, score 9, trust_infrastructure) [lake]: [Remote attestation over EDHOC](https://datatracker.ietf.org/doc/draft-ietf-lake-ra/) — This document specifies how to perform remote attestation as part of
   the lightweight authenticated Diffie-Hellman key exchange protocol
   EDHOC (Ephemeral Diffie-Hellman Over COSE), based on the Remote
   ATtestation procedureS (RATS) architecture.
- **draft-ietf-moq-privacy-pass-auth-03** (new-draft, score 9, core_identity) [moq]: [Privacy Pass Authentication for Media over QUIC (MoQ)](https://datatracker.ietf.org/doc/draft-ietf-moq-privacy-pass-auth/) — This document specifies the use of Privacy Pass architecture and
   issuance protocols for authorization in Media over QUIC (MoQ)
   transport protocol.  It defines how Privacy Pass tokens can be
   integrated with MoQ's authorization framework to provide privacy-
   preserving authentication for subscriptions, fetches, publications,
   and relay operations while supporting fine-grained access control
   through prefix-based track namespace and track name matching rules.
- **draft-ietf-oauth-browser-based-apps-27** (new-draft, score 9, authorization) [oauth]: [OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/draft-ietf-oauth-browser-based-apps/) — This specification details the threats, attack consequences, security
   considerations and best practices that must be taken into account
   when developing browser-based applications that use OAuth 2.0.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Web Authorization
   Protocol Working Group mailing list (oauth@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/oauth/.

   Source for this draft and an issue tracker can be found at
   https://github.com/oauth-wg/oauth-browser-based-apps.
- **draft-ietf-oauth-client-id-metadata-document-02** (new-draft, score 9, authorization) [oauth]: [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/) — This specification defines a mechanism through which an OAuth client
   can identify itself to authorization servers, without prior dynamic
   client registration or other existing registration.  This is through
   the usage of a URL as a client_id in an OAuth flow, where the URL
   refers to a document containing the necessary client metadata,
   enabling the authorization server to fetch the metadata about the
   client as needed.
- **draft-ietf-oauth-refresh-token-expiration-03** (new-draft, score 9, authorization) [oauth]: [OAuth 2.0 Refresh Token and Authorization Expiration](https://datatracker.ietf.org/doc/draft-ietf-oauth-refresh-token-expiration/) — This specification extends OAuth 2.0 [RFC6749] by adding new token
   endpoint response parameters to specify refresh token expiration and
   user authorization expiration.
- **draft-ietf-rats-corim-11** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Reference Integrity Manifest](https://datatracker.ietf.org/doc/draft-ietf-rats-corim/) — Remote Attestation Procedures (RATS) enable Relying Parties to assess
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
- **draft-ietf-rats-coserv-07** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Selector for Endorsements and Reference Values](https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/) — In the Remote Attestation Procedures (RATS) architecture, Verifiers
   require Endorsements and Reference Values to assess the
   trustworthiness of Attesters.  This document specifies the Concise
   Selector for Endorsements and Reference Values (CoSERV), a structured
   query/result format designed to facilitate the discovery and
   retrieval of these artifacts from various providers.  CoSERV defines
   a query language and corresponding result structure using CDDL, which
   can be serialized in CBOR format, enabling efficient interoperability
   across diverse systems.
- **draft-jennings-agentproto-mcp-over-moqt-00** (new-draft, score 9, adjacent_watchlist) [none]: [Model Context Protocol and Agent Skills over Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-jennings-agentproto-mcp-over-moqt/) — This document defines how to use Media over QUIC Transport (MOQT) as
   the underlying transport protocol for the Model Context Protocol
   (MCP).  MCP enables integration between language model applications
   and external data sources and tools.  MOQT provides publish-subscribe
   delivery over QUIC and WebTransport with native prioritization, relay
   caching, and multiplexing.

   This specification maps MCP messages onto MOQT objects and defines
   procedures for session establishment, capability discovery, and
   ongoing communication.  It covers MCP's core primitives (resources,
   tools, prompts, sampling, and notifications) through dedicated MOQT
   tracks.

   The document also describes Agent Skills -- composed instructions
   that extend AI capabilities beyond atomic tool operations -- using
   progressive loading aligned with MOQT's object-based delivery.
- **draft-mih-agent-bilateral-attestation-00** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
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
   part, gives each proof of the other's, and can be anchored to a
   transparency service so that a third party who trusts neither
   organization can verify its integrity, timing, and both parties'
   signatures.  The exchange records refusals with the same fidelity as
   performance, and degrades gracefully when a counterparty cannot
   attest, marking the record's reduced assurance rather than blocking
   the transaction.
- **draft-mw-nmop-yang-ai-challenges-00** (new-draft, score 9, agent_identity) [none]: [Rethinking YANG-based Service and Network Management in the Era of Agentic AI](https://datatracker.ietf.org/doc/draft-mw-nmop-yang-ai-challenges/) — The industry today is actively exploring the application of agentic
   AI to autonomous network operations.  However, there is little
   attention given to the impacts that the introduction of agentic AI
   may impose on YANG modeling, and how YANG can be better leveraged to
   support AI-driven autonomous operations.

   Based on some end-to-end intent translation workflow analysis that
   engage YANG models across service, network, and device layers, this
   document identifies some critical gaps when AI agents generate and
   operate on YANG data.  The purpose of this document is not to
   substantially redesign YANG or define a new data model language.
   Instead, it aims to facilitate discussion on how existing YANG
   ecosystems can be better leveraged in the context of agentic AI, and
   how complementary mechanisms can bridge these gaps while preserving
   YANG’s interoperability.
- **draft-wang-tls-service-affinity-05** (new-draft, score 9, authorization) [none]: [Service Affinity Solution based on Transport Layer Security (TLS)](https://datatracker.ietf.org/doc/draft-wang-tls-service-affinity/) — This draft proposes a service affinity solution between client and
   server based on Transport Layer Security (TLS).  It defines a minimal
   extension to TLS 1.3 by which a server instance can authorize a
   client to resume an established session on a different instance of
   the same service (for example, another node of a load-balanced
   cluster) and request, in band, that the client do so.  The relocation
   authorization is carried inside the server's own session ticket, so
   it inherits the security properties of TLS 1.3 ticket-based
   resumption.  The relocation target is an opaque value that either
   directly carries the switchover address (for example, an IP address
   and port) or is an identifier resolved by the application or control
   plane.

   This document also introduces a Reliable Framing Layer that operates
   above the TLS record layer to provide message framing, sequence
   numbering, acknowledgment tracking, and automatic retransmission.
   The Framing Layer ensures zero application data loss during TLS
   session migration by buffering unacknowledged data frames and
   retransmitting them to the new server endpoint after migration
   completes.
- **draft-wendt-stir-vesper-oob-03** (new-draft, score 9, adjacent_watchlist) [none]: [VESPER Out-of-Band OOB](https://datatracker.ietf.org/doc/draft-wendt-stir-vesper-oob/) — This document describes a mechanism for delivering authenticated
   telephone call identity information using the VESPER framework for
   use where in-band signaling does not carry the identity end to end,
   or where there is no in-band path between the parties at all.  By
   supporting an out-of-band (OOB) transport model, this approach
   enables entities to publish and retrieve signed PASSporT assertions
   independent of end-to-end delivery within an in-band signaling path
   such as a SIP-based VoIP network.  These PASSporTs are signed with
   VESPER delegate certificates, which identify the entity holding the
   right-to-use for a telephone number and bind it to that entity's
   domain identity.  This document also introduces support for Connected
   Identity to the STIR OOB model, enabling the called party to respond
   with a signed PASSporT asserting its identity, thereby binding the
   identities of both parties to the transaction and enhancing end-to-
   end accountability.  The OOB mechanism provides a delivery path for
   PASSporTs where in-band delivery within a signaling path such as SIP
   is unavailable or is not the path used, enabling verifiers to confirm
   the association between the originating telephone number and the
   identity asserting authority as part of the broader VESPER trust
   framework.
- **draft-wirtgen-bgp-tls-05** (new-draft, score 9, core_identity) [none]: [BGP over TLS/TCP](https://datatracker.ietf.org/doc/draft-wirtgen-bgp-tls/) — This document specifies the use of TLS over TCP to support BGP.  The
   Border Gateway Protocol (BGP) relies on TCP to establish sessions
   between routers.  While the TCP Authentication Option (TCP-AO)
   provides transport-layer integrity protection against spoofing and
   reset attacks, it does not provide confidentiality, cryptographic
   peer identity, or scalable key management.  This document specifies a
   method for establishing a secure BGP session by running BGP over a
   TLS 1.3 session.  The underlying TCP transport MUST be protected
   using TCP-AO.  An "Implicit TLS" model on TCP port 179 is specified
   as the preferred mechanism.
- **draft-wullink-rpp-oauth2-transfer-00** (new-draft, score 9, authorization) [none]: [Secure Object Transfer for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-oauth2-transfer/) — This document describes how OAuth 2.0 [RFC6749] can be used to secure
   object transfers in RESTful Provisioning Protocol (RPP)
   [I-D.ietf-rpp-core].  It extends the RPP OAuth 2.0 authorization
   model defined in [I-D.wullink-rpp-oauth2] with mechanisms specific to
   federated object transfers.
- **draft-cui-dns-native-agent-naming-resolution-02** (new-draft, score 8, agent_identity) [none]: [DNS-Native AI Agent Naming and Resolution](https://datatracker.ietf.org/doc/draft-cui-dns-native-agent-naming-resolution/) — This document specifies DNS-Native Agent Naming and Resolution (DN-
   ANR) for AI agents.  DN-ANR uses domain names (FQDNs) as stable Agent
   Identifiers and resolves a selected Agent Identifier to verifiable
   endpoints and supported protocol/version information with a
   cryptographic integrity chain, with DNSSEC preferred.

   DN-ANR is a post-selection resolution profile.  It does not define
   agent discovery, capability search, semantic matching, ranking, or
   routing decisions.  Agent discovery, publication, or registry,
   including DNS-based mechanisms such as DNS-AID, may produce candidate
   Agent Identifiers; DN-ANR resolves and verifies the identifier
   selected by such mechanisms or by local policy.  Within that scope,
   DN-ANR additionally defines DNS-based version distribution and
   deterministic version selection, canonicalized SVCB integrity cross-
   checking, and a signed HTTPS mirror for clients that cannot perform
   SVCB queries.  While AI agents are the primary use case, the
   resolution and verification behavior defined here applies to any
   entity identified by an FQDN, such as services and workloads.
- **draft-ietf-opsawg-yang-provenance-07** (new-draft, score 8, verifiable_claims) [opsawg]: [Applying COSE Signatures for YANG Data Provenance](https://datatracker.ietf.org/doc/draft-ietf-opsawg-yang-provenance/) — This document defines a mechanism based on CBOR Object Signing and
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
- **draft-jms-mole-http-transport-00** (new-draft, score 8, core_identity) [none]: [MoLE HTTP Transport](https://datatracker.ietf.org/doc/draft-jms-mole-http-transport/) — MoLE targets browser deployments, so Clients, Anchors, and Moderators
   need an HTTP transport for the protocol flows defined by the
   architecture.

   This document defines the Mole HTTP authentication scheme, which
   carries challenges and presentations for the endorsement and
   credential flows, and the headers used to return credential material.
   The grant exchanges with the Anchor are defined per protocol in
   [PROTOCOLS].
- **draft-ni-agent-entity-discovery-00** (new-draft, score 8, agent_identity) [none]: [DNS-based Entity-Level Discovery and End-to-End Connection for AI Agents](https://datatracker.ietf.org/doc/draft-ni-agent-entity-discovery/) — This document defines a new DNS resource record type, Agent Entity
   Discovery (AED), to publish agent-specific trust anchors or direct
   match constraints for verifying an agent's certificate or token.
   This enables the cross-domain users or agents to authenticate, and
   establish secure, end-to-end connections directly with a private-
   domain agent entity.
- **draft-ritz-idpop-01** (new-draft, score 8, core_identity) [none]: [Interactive DPoP](https://datatracker.ietf.org/doc/draft-ritz-idpop/) — This document describes IDPoP, an extension to DPoP [RFC9449] that
   uses a key derivation scheme to separate access control from
   identity.  It mitigates credential exfiltration risks by requiring
   fresh hardware attestation to unseal identity keys via an interactive
   challenge.
- **draft-shang-campus-agent-scope-down-01** (new-draft, score 8, authorization) [none]: [Campus Agent Identification and Scope-Down Access Control](https://datatracker.ietf.org/doc/draft-shang-campus-agent-scope-down/) — AI agents operating in enterprise campus networks execute user-
   delegated Tasks by invoking multiple tools and services, often
   without continuous user supervision.  Traditional authorization
   models assume stable applications and human-driven interactions,
   creating a mismatch when applied to autonomous agents that can chain
   actions across heterogeneous systems.

   Campus environments also contain heterogeneous and legacy services
   across diverse protocols, making per-service agent-aware
   authorization difficult to deploy consistently.  Similar problems can
   also appear in residential access networks where home AI agents,
   smart-home hubs, and personal devices share a subscriber line and are
   connected through a broadband network gateway (BNG).

   This document describes the problem space for campus agent access
   control and argues that agents require task-bound privilege reduction
   ("scope-down") and that enforcement can be provided by in-path
   network devices in order to preserve compatibility with existing
   systems.  It also describes a home network and BNG use case where the
   access provider or home gateway can provide a coarse but useful
   network-level boundary for agent traffic.
- **draft-song-fann-framework-01** (new-draft, score 8, ai_infrastructure) [none]: [A Framework for Fast Network Notifications](https://datatracker.ietf.org/doc/draft-song-fann-framework/) — Many network applications, ranging from Artificial Intelligence (AI)
   / Machine Learning (ML) training and inference to large-scale cloud
   services, require networks with various combinations of high
   bandwidth, low delay, low jitter, and minimal packet loss.  Meeting
   these requirements depends on the network's ability to adapt rapidly
   to faults, signal degradation, and congestion.  The companion problem
   statement describes why existing mechanisms are too slow, too coarse,
   or too resource-intensive to react within the timescales at which
   modern forwarding hardware can detect and disseminate intended
   conditions.

   This document defines a framework for Fast Network Notifications
   (FANN).  It describes a reference architecture, the functional roles
   involved in generating and consuming notifications, an information
   model, delivery and scoping models, procedures for discovery,
   registration, and subscription, and the integration of fast network
   notifications with existing Layer 2 to 4 mechanisms.  This framework
   is intended to guide the development of one or more fast network
   notification protocol specifications.
- **draft-chuyi-nmrg-agentic-network-inference-01** (new-draft, score 7, agent_identity) [none]: [Agentic Network Architecture and Protocol for Supporting Agent Interconnection Communication and Multi-level Inference](https://datatracker.ietf.org/doc/draft-chuyi-nmrg-agentic-network-inference/) — With the advent of the era of AI large models and intelligent agents,
   more and more scenarios about agent interconnection have emerged,
   such as collaboration among multiple agents within a household,
   intelligent robots cooperating to complete pipeline tasks in
   different operations of the industrial Internet, drone groups,
   intelligent vehicle networking, etc.  These scenarios not only
   require low latency and high bandwidth, but also demand efficient
   information exchange and cross-domain coordination and scheduling
   capabilities in complex collaborative tasks.  Therefore, new
   orchestration and management technologies and frameworks are needed
   in existing networks to address this.  The interconnection of
   different agents also brings about an emergence of inference, with a
   large number of inference requests being processed from the mobile
   phone side to the cloud.  In order to improve inference efficiency,
   in a cloud-edge-end multi-layer inference architecture, large models
   and agents at different levels cooperate to complete tasks, resulting
   in a complex intelligent agent interconnection network.  Gateways and
   routers serve as forwarding entries on the network road highways,
   responsible for building communication channels for the agents spread
   throughout the network, which requiring function upgrades to support
   the continuously evolving inference service in the future.
- **draft-li-oauth-delegated-authorization-02** (new-draft, score 7, authorization) [none]: [OAuth 2.0 Delegated Authorization](https://datatracker.ietf.org/doc/draft-li-oauth-delegated-authorization/) — Delegated authorization enables a client to delegate a subset of its
   granted privileges to a subordinate access token (also known as a
   delegated access token).  This mechanism allows the client to
   securely delegate authorization to another application while
   maintaining fine-grained control over delegated permissions.
- **draft-ly-multi-agent-in6g-00** (new-draft, score 7, authorization) [none]: [Multiple Agents Collaboration in 6G Network](https://datatracker.ietf.org/doc/draft-ly-multi-agent-in6g/) — This document describes the progress of 6G study on AI topic, e.g.
   key issues, potential solutions and alternative communication
   protocols.  Despite the apparent overlap between 3GPP and IETF in the
   hot topics of Agents e.g. communication protocols, discovery,
   authorization and etc., 3GPP and IETF address different problems due
   to consideration of network boundaries.  Thus this document tracks
   the progress of 6G study to identify dependencies on IETF protocols
   within the agent communication topics.
- **draft-zhao-ccamp-actn-optical-network-agent-02** (new-draft, score 7, adjacent_watchlist) [none]: [Integration of Network Management Agent (NMA) into ACTN-Based Optical Network](https://datatracker.ietf.org/doc/draft-zhao-ccamp-actn-optical-network-agent/) — With the growth of optical network scale, the complexity of network
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
- **draft-zhao-nmop-network-management-agent-05** (new-draft, score 7, agent_identity) [none]: [AI based Network Management Agent(NMA): Concepts and Architecture](https://datatracker.ietf.org/doc/draft-zhao-nmop-network-management-agent/) — The evolution from Level 3 (assisted automation) to Level 4 (closed-
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
   reference architecture, deployment modes, and logical interfaces of
   the NMA, including Agent-to-User (A2U), Agent-to-Agent (A2A), Agent-
   to-Controller (A2C), and Agent-to-Network (A2N) interactions.

## Monitor

- **draft-corneo-t2trg-sdf-coap-agents-00** (new-draft, score 6, agent_identity) [none]: [Extending SDF and CoAP for AI Agent Interaction with IoT Devices](https://datatracker.ietf.org/doc/draft-corneo-t2trg-sdf-coap-agents/) — This document proposes extensions to the Semantic Definition Format
   (SDF) and the Constrained Application Protocol (CoAP) to better
   support AI agent interaction with Internet of Things (IoT) devices.
   It covers two aspects: identifying AI agents in CoAP transactions,
   and making SDF device descriptions readily consumable by large
   language models (LLMs) and autonomous agents.  The document is
   intended to stimulate discussion within T2TRG on these topics.
- **draft-cui-nmrg-llm-benchmark-02** (new-draft, score 6, agent_identity) [none]: [A Framework to Evaluate LLM Agents for Network Configuration](https://datatracker.ietf.org/doc/draft-cui-nmrg-llm-benchmark/) — This document specifies an evaluation framework and related
   definitions for intent-driven network configuration using Large
   Language Model(LLM)-based agents.  The framework combines an
   emulator-based interactive environment, a suite of representative
   tasks, and multi-dimensional metrics organized in two layers: outcome
   metrics that verify functional correctness in a method-agnostic way,
   and agentic process metrics that assess reasoning quality and
   interactive command generation.  Functional testcase results serve as
   the primary metric; command and reasoning scores act as diagnostic
   estimates against the task's ground truth configurations (which may
   include more than one validated solution), and optional efficiency
   metrics capture time and token cost.  The framework aims to enable
   reproducible, comprehensive, and fair comparisons among network
   configuration approaches, covering both agentic and non-agentic
   solutions while highlighting capabilities specific to autonomous
   agents.
- **draft-hong-nmrg-agenticai-ps-02** (new-draft, score 6, agent_identity) [none]: [Motivations and Problem Statement of Agentic AI for network management](https://datatracker.ietf.org/doc/draft-hong-nmrg-agenticai-ps/) — This document outlines the key objectives of introducing Agentic AI
   to the field of network management and highlights the fundamental
   issues with existing technologies that must be addressed to achieve
   these goals.  It emphasizes the necessity for relevant groups within
   the IETF/IRTF and presents the core technological areas requiring
   standardization.  The aim of Agentic AI is to facilitate a paradigm
   shift in which multiple autonomous AI agents collaborate to fully
   automate network operation, management and security.
- **draft-ietf-ace-authcred-dtls-profile-04** (new-draft, score 6, core_identity) [ace]: [Additional Formats of Authentication Credentials for the Datagram Transport Layer Security (DTLS) Profile for Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-ietf-ace-authcred-dtls-profile/) — This document updates the Datagram Transport Layer Security (DTLS)
   profile for Authentication and Authorization for Constrained
   Environments (ACE).  In particular, it specifies the use of
   additional formats of authentication credentials for establishing a
   DTLS session, when peer authentication is based on asymmetric
   cryptography.  Therefore, this document updates RFC 9202.  What is
   defined in this document is seamlessly applicable also if the profile
   uses Transport Layer Security (TLS) instead of DTLS, as defined in
   RFC 9430.
- **draft-ietf-ace-oscore-gm-admin-coral-06** (new-draft, score 6, core_identity) [ace]: [Using the Constrained RESTful Application Language (CoRAL) with the Admin Interface for the OSCORE Group Manager](https://datatracker.ietf.org/doc/draft-ietf-ace-oscore-gm-admin-coral/) — Group communication for the Constrained Application Protocol (CoAP)
   can be secured using Group Object Security for Constrained RESTful
   Environments (Group OSCORE).  A Group Manager is responsible to
   handle the joining of new group members, as well as to manage and
   distribute the group keying material.  The Group Manager can provide
   a RESTful admin interface that allows an Administrator entity to
   create and delete OSCORE groups, as well as to retrieve and update
   their configuration.  This document specifies how an Administrator
   interacts with the admin interface at the Group Manager by using the
   Constrained RESTful Application Language (CoRAL).  The ACE framework
   for Authentication and Authorization is used to enforce
   authentication and authorization of the Administrator at the Group
   Manager.  Protocol-specific transport profiles of ACE are used to
   achieve communication security, proof of possession, and server
   authentication.
- **draft-ietf-cose-split-signing-algs-01** (new-draft, score 6, verifiable_claims) [cose]: [Split Signing Algorithms for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-split-signing-algs/) — This specification defines COSE algorithm identifiers for negotiating
   how to split a signature algorithm between two cooperating parties.
   Typically the first party hashes the data to be signed and the second
   party finishes the signature over the hashed data.  This is a common
   technique, useful for example when the signing private key is held in
   a smart card or similar hardware component with limited processing
   power and communication bandwidth.  The resulting signatures are
   identical in structure to those computed by a single party, and can
   be verified using the same verification algorithm without additional
   steps to preprocess the signed data.
- **draft-ietf-dance-client-auth-12** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document updates RFC 6698 and RFC 7671.  It describes how to use the
   TLSA record to publish client certificates or public keys, and also
   the rules and considerations for using them with TLS.  In addition,
   it defines a new TLS extension, DANE Client Identity, to convey the
   client's domain name identity to the server.
- **draft-ietf-emu-teapv2-00** (new-draft, score 6, core_identity) [emu]: [Tunnel Extensible Authentication Protocol (TEAP) Version 2](https://datatracker.ietf.org/doc/draft-ietf-emu-teapv2/) — This document defines the Tunnel Extensible Authentication Protocol
   (TEAP) version 2.  It addresses a number of security and
   interoperability issues which were found during the publication of
   TEAPv1 ([I-D.ietf-emu-rfc7170bis]).
- **draft-ietf-jose-hpke-pq-pqt-01** (new-draft, score 6, verifiable_claims) [jose]: [JOSE HPKE PQ & PQ/T Algorithm Registrations](https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-pq-pqt/) — This document registers Post-Quantum (PQ) and Post-Quantum/
   Traditional (PQ/T) hybrid algorithm identifiers for use with JSON
   Object Signing and Encryption (JOSE), building on the Hybrid Public
   Key Encryption (HPKE) framework.
- **draft-ietf-jose-pqc-kem-06** (new-draft, score 6, verifiable_claims) [jose]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/) — This document describes conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and
   Encryption (COSE).
- **draft-ietf-lake-authkem-edhoc-00** (new-draft, score 6, core_identity) [lake]: [KEM-based Authentication for EDHOC](https://datatracker.ietf.org/doc/draft-ietf-lake-authkem-edhoc/) — This document specifies extensions to the Ephemeral Diffie-Hellman
   Over COSE (EDHOC) protocol to provide resistance against quantum
   computer adversaries by incorporating Post-Quantum Cryptography (PQC)
   Key Encapsulation Mechanisms (KEMs) for both key exchange and
   authentication.  It defines a new signature-free KEM-based
   authentication method in which both parties authenticate using KEMs,
   enabling quantum-resistant authentication without relying on digital
   signatures when PQC KEMs, such as the NIST-standardized ML-KEM, are
   used.
- **draft-ietf-lake-edhoc-grease-03** (new-draft, score 6, authorization) [lake]: [Applying Generate Random Extensions And Sustain Extensibility (GREASE) to EDHOC Extensibility](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-grease/) — This document applies the extensibility mechanism GREASE (Generate
   Random Extensions And Sustain Extensibility), which was pioneered for
   TLS, to the ecosystem of Ephemeral Diffie-Hellman Over COSE (EDHOC).
   It reserves a set of External Authorization Data (EAD) labels and
   unusable cipher suites that may be included in messages to ensure
   peers correctly handle unknown values.
- **draft-ietf-lake-pqsuites-00** (new-draft, score 6, core_identity) [lake]: [Quantum-Resistant Cipher Suites for LAKE](https://datatracker.ietf.org/doc/draft-ietf-lake-pqsuites/) — The Lightweight Authenticated Key Exchange (LAKE) protocol, also
   known as Ephemeral Diffie-Hellman over COSE (EDHOC), achieves post-
   quantum security by adding new cipher suites with quantum-resistant
   algorithms, such as ML-DSA for digital signatures and ML-KEM for key
   exchange.  This document specifies how the LAKE protocol operates in
   a post-quantum setting using both signature-based and PSK-based
   authentication methods, and defines corresponding cipher suites.
- **draft-ietf-oauth-security-topics-update-03** (new-draft, score 6, authorization) [oauth]: [Updates to OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/) — This document updates the set of best current security practices for
   OAuth 2.0 by extending the security advice given in RFC 6749, RFC
   6750, and RFC 9700, to cover new threats that have been discovered
   since the former documents have been published.
- **draft-ietf-tls-mldsa-05** (new-draft, score 6, core_identity) [tls]: [Use of ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/) — This memo specifies how the post-quantum signature scheme ML-DSA
   (FIPS 204) is used for authentication in TLS 1.3.
- **draft-ietf-webtrans-http3-16** (new-draft, score 6, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/) — WebTransport over HTTP/3 is a binding of the WebTransport protocol
   framework [OVERVIEW] to HTTP/3 [HTTP3].  It provides support for
   unidirectional streams, bidirectional streams, and datagrams, all
   multiplexed within the same HTTP/3 connection.  WebTransport enables
   application clients constrained by the Web security model to
   communicate with a remote application server using a secure
   multiplexed transport.
- **draft-ietf-webtrans-overview-13** (new-draft, score 6, adjacent_watchlist) [webtrans]: [The WebTransport Protocol Framework](https://datatracker.ietf.org/doc/draft-ietf-webtrans-overview/) — The WebTransport Protocol Framework enables clients constrained by
   the Web security model to communicate with a remote server using a
   secure multiplexed transport.  It consists of a set of individual
   protocols that are safe to expose to untrusted applications, combined
   with an abstract model that allows them to be used interchangeably.

   This document defines the overall requirements on the protocols used
   in WebTransport, as well as the common features of the protocols,
   support for some of which is optional.
- **draft-irtf-cfrg-pairing-friendly-curves-13** (new-draft, score 6, core_identity) [cfrg]: [Pairing-Friendly Curves](https://datatracker.ietf.org/doc/draft-irtf-cfrg-pairing-friendly-curves/) — Pairing-based cryptography, a subfield of elliptic curve
   cryptography, has received attention due to its flexible and
   practical functionality.  Pairings are special maps defined using
   elliptic curves and it can be applied to construct several
   cryptographic protocols such as identity-based encryption, attribute-
   based encryption, and so on.  At CRYPTO 2016, Kim and Barbulescu
   proposed an efficient number field sieve algorithm named exTNFS for
   the discrete logarithm problem in a finite field.  Several types of
   pairing-friendly curves such as Barreto-Naehrig curves are affected
   by the attack.  In particular, a Barreto-Naehrig curve with a 254-bit
   characteristic was adopted by a lot of cryptographic libraries as a
   parameter of 128-bit security, however, it ensures no more than the
   100-bit security level due to the effect of the attack.  In this
   memo, we list the security levels of certain pairing-friendly curves,
   and motivate our choices of curves.  First, we summarize the adoption
   status of pairing-friendly curves in standards, libraries and
   applications, and classify them in the 128-bit, 192-bit, and 256-bit
   security levels.  Then, from the viewpoints of "security" and "widely
   used", we select the recommended pairing-friendly curves considering
   exTNFS.
- **draft-liao-cose-c509-revocation-00** (new-draft, score 6, core_identity) [none]: [CBOR Encoded Certificate Revocation Management](https://datatracker.ietf.org/doc/draft-liao-cose-c509-revocation/) — This document specifies CBOR-encoded PKI structures for use with C509
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
   without semantic interpretation.
- **draft-morrison-substrate-observation-01** (new-draft, score 6, core_identity) [none]: [Substrate-Observation as an Alternative to Envelope Coordination for Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-substrate-observation/) — This memo articulates a coordination-protocol anti-pattern observed
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
- **draft-reddy-seat-expat-transport-01** (new-draft, score 6, core_identity) [none]: [Application-Layer Transport for Exported Authenticators and Attestation](https://datatracker.ietf.org/doc/draft-reddy-seat-expat-transport/) — This document defines a binary, application-layer transport protocol
   for exchanging Exported Authenticator messages between two peers over
   TLS.  It provides the signaling required to initiate and complete
   post-handshake authentication exchanges at the application layer,
   without requiring modifications to the TLS layer itself.

   While primarily intended to support attestation exchange, the
   transport is generic and can be used independently for any Exported
   Authenticator exchange.

   The document further specifies how protocol messages are conveyed as
   Capsules over an HTTP connection established using the Extended
   CONNECT method, with support for both HTTP/2 and HTTP/3.  In
   addition, it defines how the protocol can operate directly over TLS
   or DTLS 1.3 without an HTTP binding, using a so-called "Shim Mode".
- **draft-schreiber-scim-ipsie-profile-00** (new-draft, score 6, core_identity) [none]: [SCIM 2.0 IPSIE Profile](https://datatracker.ietf.org/doc/draft-schreiber-scim-ipsie-profile/) — This document defines a profile for SCIM 2.0 to meet the security and
   interoperability requirements for identity lifecycle management
   within enterprises.  Within the context of SCIM, the profile
   establishes requirements for provisioning, account management, client
   authentication, and identity synchronization across three Account
   Lifecycle assurance levels: AL1 (User Deprovisioning), AL2 (User and
   Group Management), and AL3 (Role Management).
- **draft-skyfire-oauth-amr-values-00** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-00** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-tiloca-ace-oscore-gm-kem-00** (new-draft, score 6, core_identity) [none]: [Quantum-Resistant Key Encapsulation Mechanisms (KEMs) via the OSCORE Group Manager Using Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-tiloca-ace-oscore-gm-kem/) — RFC 9594 defines a Key Distribution Center (KDC) to provision keying
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
   enable the exchange of KEM public keys and KEM ciphertexts among
   group members via the Group Manager, thus making the derivation of
   pairwise keys in Group OSCORE post-quantum secure.
- **draft-usama-seat-intra-vs-post-04** (new-draft, score 6, trust_infrastructure) [none]: [Pre-, Intra- and Post-handshake Attestation](https://datatracker.ietf.org/doc/draft-usama-seat-intra-vs-post/) — This document presents a taxonomy of extending TLS protocol with
   remote attestation, referred to as attested TLS.  It also presents
   high-level analysis of benefits and limitations of each category,
   namely pre-handshake attestation, intra-handshake attestation and
   post-handshake attestation.  It also captures the opinions of the WG
   participants in order to build consensus towards solutions.  It also
   discussed tradeoffs and scalability.
- **draft-wendt-stir-tn-domain-binding-00** (new-draft, score 6, core_identity) [none]: [Binding a Domain Identifier to Telephone Number Authority in STIR Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-tn-domain-binding/) — This document defines a mechanism for binding a domain identifier to
   telephone number authority within a STIR certificate.  A certificate
   produced under this mechanism carries, as a co-validated pair, the
   telephone numbers or service provider codes a subject is authorized
   for in a TNAuthList extension and a domain the subject controls in a
   SubjectAltName dNSName entry.  The binding is established at issuance
   by requiring proof of domain control and validation of a TNAuthList
   authority token within a single certificate issuance, such that the
   resulting certificate attests that the same entity holds both.  The
   mechanism applies to STIR certificates whose TNAuthList contains
   telephone number entries, service provider code entries, or both,
   allowing a domain to be bound to the right-to-use holder for a set of
   numbers or to the provider identified by a service provider code.
   This document defines the issuance conformance requirements and the
   relying party verification rule that together make the binding
   meaningful.  It does not define telephone number or service provider
   code authorization or domain validation, both of which are specified
   elsewhere and referenced here.
- **draft-zhang-seat-selection-01** (new-draft, score 6, trust_infrastructure) [none]: [Balancing Security and Deployability in the Selection of Attested TLS Protocol](https://datatracker.ietf.org/doc/draft-zhang-seat-selection/) — This document analyzes the selection of Attested Transport Layer
   Security (aTLS) protocols, among pre-handshake, intra-handshake, and
   post-handshake aTLS protocols, focusing on the trade-off between
   theoretical security strength and practical deployability.  The goal
   is to enable flexible, context-aware deployment of endpoint
   attestation while maintaining compatibility with existing
   infrastructure.
- **draft-bubblefish-npamp-01** (new-draft, score 5, core_identity) [none]: [N-PAMP: Native Post-Quantum Agent Messaging Protocol](https://datatracker.ietf.org/doc/draft-bubblefish-npamp/) — The Native Post-Quantum Agent Messaging Protocol (N-PAMP) is a
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
   Application-Layer Protocol Negotiation (ALPN) identifier "n-pamp/2".
   This document describes the wire format, channel architecture,
   profile negotiation, and cryptographic suites of N-PAMP, and reserves
   code-point ranges for extensions defined in companion specifications.
- **draft-calabria-bmwg-ai-fabric-training-bench-03** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
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
   Consortium (UEC) Specification 1.0 [UEC-1.0], congestion management
   (Priority Flow Control (PFC), Explicit Congestion Notification (ECN),
   Data Center Quantized Congestion Notification (DCQCN), Credit-Based
   Flow Control (CBFC)), load balancing strategies (Equal-Cost Multi-
   Path (ECMP), Dynamic Load Balancing (DLB), packet spraying),
   collective communication patterns (AllReduce, AllToAll, AllGather),
   and scale/soak testing.

   The methodology enables direct, reproducible comparison across switch
   ASICs, NIC transport stacks (RoCEv2 and UET), and fabric
   architectures (2-tier Clos, 3-tier Clos, and rail-optimized).
- **draft-cxxx-nmrg-ai4ibn-00** (new-draft, score 5, agent_identity) [none]: [Agentic AI for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-cxxx-nmrg-ai4ibn/) — This document specifies how the rise of agentic AI and LLMs can
   impact and and accelerate the transition towards Intent-Based
   Networking.
   Specifically, it revisits functionality and liefecycle in IBN, as
   defined in [RFC9315], and outlines how agentic AI and LLMs can be
   leveraged.
- **draft-du-catalist-routing-considerations-02** (new-draft, score 5, agent_identity) [none]: [Routing Considerations in Agentic Network](https://datatracker.ietf.org/doc/draft-du-catalist-routing-considerations/) — As the development of the AI technology, an AI Agent would be able to
   do some tasks as an assistant to human beings.  During the task
   process, the Agent may need to connect to other Agents with different
   skills relative to the task.  The Agent to Agent communication is a
   new kind of traffic for Internet, and some new requirements for
   networking are proposed.  This document describes some routing
   considerations in the agentic network, especially for the cross-
   domain scenarios, in which the agentic network works as an overlay
   network above the IP network.
- **draft-ietf-rats-pkix-key-attestation-07** (new-draft, score 5, adjacent_watchlist) [rats]: [Evidence Encoding for Hardware Security Modules](https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/) — This document specifies a vendor-agnostic format for Evidence
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

   This specification also offers a format for requesting a
   cryptographic module to produce Evidence tailored for expected use.
- **draft-irtf-nmrg-ai-challenges-06** (new-draft, score 5, ai_infrastructure) [nmrg]: [Research Challenges in Coupling Artificial Intelligence and Network Management](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ai-challenges/) — This document is intended to introduce the challenges to overcome
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
- **draft-jakab-dawn-agent-discovery-mdns-00** (new-draft, score 5, adjacent_watchlist) [none]: [Zero-Configuration Agent Discovery](https://datatracker.ietf.org/doc/draft-jakab-dawn-agent-discovery-mdns/) — Protocols for communication between autonomous software agents
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
   followed by retrieval of full agent metadata over the agent's native
   transport.  It gives a worked instantiation of that model for the
   Agent2Agent (A2A) protocol, as an example.
- **draft-janz-nmrg-ontology-reconciliation-01** (new-draft, score 5, adjacent_watchlist) [none]: [Automated Agent-to-Agent Ontology Reconciliation for Cognitive Network Management Systems](https://datatracker.ietf.org/doc/draft-janz-nmrg-ontology-reconciliation/) — This document describes a possible direction for inter-system
   communication in network management, in which two cognitive software
   agents establish between themselves the basis for exchanging
   information, without depending on a single rigid data model agreed by
   their implementers in advance.  The agents bring relevant knowledge,
   can extend it through learning, can reason, and can converse in
   natural language.  The approach is framed as a workflow in which each
   agent makes explicit the ontology implicit in its data model, the two
   agents address their differences through conversation, and a
   translator artefact is produced that is then used during ordinary
   operation.  A central property is that language-model inference is
   consumed during the agents' conversation rather than on each
   subsequent message.  The document situates the direction relative to
   adjacent work and illustrates it through three use cases drawn from
   network management.
- **draft-jms-mole-architecture-00** (new-draft, score 5, adjacent_watchlist) [none]: [Moderation of unLinkable Endorsements (MoLE) Architecture](https://datatracker.ietf.org/doc/draft-jms-mole-architecture/) — Moderation of unLinkable Endorsements (MoLE) is an architecture that
   lets a party performing access control (a Moderator) bootstrap trust
   in a client from a third party (an Anchor) that already has a trust
   relationship with that client, and then adjust that trust over time
   in response to the client's behaviour, for example by dynamically
   rate-limiting access.

   MoLE targets open deployments, in which independent parties may be
   responsible for access control and for vouching for clients, whilst
   maintaining strong privacy protections for clients.  These
   protections are designed to hold even if participants in the
   ecosystem collude or otherwise misbehave.

   This document specifies the roles, the information flows between
   them, the privacy and security requirements, and deployment
   considerations.
- **draft-jms-mole-protocols-00** (new-draft, score 5, verifiable_claims) [none]: [MoLE Protocols](https://datatracker.ietf.org/doc/draft-jms-mole-protocols/) — This document defines protocols that instantiate the MoLE
   architecture: two endorsement protocols, by which a Client proves to
   a Moderator that it holds an Endorsement from a trusted Anchor
   without revealing which one, and three credential protocols, by which
   a Moderator issues, verifies, and updates per-Client state without
   being able to link presentations.  It also establishes the registries
   that identify these protocols.
- **draft-mcw-opsawg-icon-requirements-00** (new-draft, score 5, agent_identity) [none]: [Architecture and Requirements for Observability, Control and Intervention of Network Management Agents](https://datatracker.ietf.org/doc/draft-mcw-opsawg-icon-requirements/) — This document defines architecture and a set of requirements for
   Observability, Control, and Intervention for Network Management
   Agents.

   It identifies gaps in existing mechanisms and specifies required
   interaction capabilities between Agent supervision systems and
   network management agents across multi-vendor environments,
   specifically observability, control, and runtime intervention.  The
   requirements aim to guarantee comprehensive, lifecycle control over
   AI agents and enable observation, constraint, intervention, and
   correction to ensure network operational resilience and continuity.
- **draft-sergeev-wexp-core-00** (new-draft, score 5, adjacent_watchlist) [none]: [The Witnessed Execution Protocol (WEXP): Core Specification](https://datatracker.ietf.org/doc/draft-sergeev-wexp-core/) — The Witnessed Execution Protocol (WEXP) defines a record format and a
   verification procedure for classifying the strength of execution-
   related evidence about actions performed by software and AI systems.
   A WEXP record asserts, for a single action, a Witnessability Level
   (WL) bounded by the execution-relevant boundary that the witness
   controls.  WEXP grades only the evidentiary strength of an execution
   claim; it does not certify the action's correctness, safety, or
   alignment.  This document specifies WEXP Core: the record model,
   required fields, the two classification axes (Witnessability Level
   and Conformance Class), the honesty invariants that bound claims, the
   verifier procedure, and failure semantics.  WEXP Core is profile-
   independent and validates standalone.
- **draft-si-ztcpp-5g-securityframework-00** (new-draft, score 5, adjacent_watchlist) [none]: [Security Capability Coordination Execution Framework for 5G Core Networks](https://datatracker.ietf.org/doc/draft-si-ztcpp-5g-securityframework/) — This document defines a security capability coordination execution
   framework for 5G core networks.  The framework employs a set of
   Security Coordination Components (SCC) that work collaboratively with
   core network functions to achieve continuous trust verification and
   least-privilege access control.  It specifies the division of
   responsibilities between the Network Function Security Agent and the
   Management Security Controller.  This document aims to provide a
   standardized architecture reference for the ZTCPP working group.
- **draft-tan-ccamp-onco-control-framework-00** (new-draft, score 5, adjacent_watchlist) [none]: [A Control Framework for Optical Networks and AI Computing Orchestration (ONCO)](https://datatracker.ietf.org/doc/draft-tan-ccamp-onco-control-framework/) — This document defines the control framework for Optical Networks and
   AI Computing Orchestration (ONCO).  The framework is designed to
   achieve synergistic management of optical network (e.g., fgOTN, OXC)
   and computing resources for high-performance AI workloads.  It
   specifies a multi-stakeholder service model, a layered architecture
   across management, control, and data planes, and a set of functional
   components.  The ONCO framework supports both centralized and
   distributed orchestration models to enable proactive resource
   reservation and deterministic optical circuit provisioning.
- **draft-tan-ccamp-onco-problem-statement-00** (new-draft, score 5, ai_infrastructure) [none]: [Optical Networks and AI Computing Orchestration (ONCO) Problem Statement, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-tan-ccamp-onco-problem-statement/) — Distributed artificial intelligence (AI) computing is increasingly
   deployed across geographically dispersed AI data centers (AIDCs) to
   meet the scale and performance demands of modern AI workloads.  In
   such environments, the efficiency of distributed training and
   inference depends critically on tight coordination between optical
   transport networks and compute orchestration systems.  However,
   today's infrastructure operates with isolated control planes: optical
   networks lack awareness of dynamic compute requirements, while
   compute schedulers have no visibility into real-time network
   conditions such as latency, bandwidth, or congestion.  This
   decoupling leads to suboptimal resource utilization, degraded job
   performance, and inefficient scaling.

   This draft presents the problem statement, outlines two
   representative use cases: distributed AI training and distributed AI
   inference, and specifies the requirements for Optical Networks and AI
   Computing Orchestration (ONCO).  The goal is to enable bidirectional
   awareness, joint resource abstraction, and synchronized control
   across the compute-optical boundary, thereby supporting intent-
   driven, end-to-end provisioning of AI services over wide-area optical
   infrastructures.
- **draft-wang-agent-runtime-telemetry-system-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Runtime Telemetry System](https://datatracker.ietf.org/doc/draft-wang-agent-runtime-telemetry-system/) — Large language model (LLM)-driven agents are increasingly deployed in
   large-scale production environments, where multi-agent collaboration,
   chained tool invocation, and long-context reasoning have become
   standard execution patterns.  However, existing distributed systems
   telemetry frameworks primarily focus on infrastructure-level
   telemetry, such as network traffic, host metrics, and service health,
   and provide limited visibility into internal agent reasoning and
   execution semantics.This results in several recurring challenges in
   production environments, including inconsistent metric definitions
   across platforms, lack of end-to-end execution traceability,
   difficulty in root cause analysis, and limited interoperability among
   heterogeneous telemetry systems.

   This document defines a unified capability framework for Agent
   Runtime Telemetry Systems.  It standardizes two telemetry collection
   planes: Network-side collection at gateways and traffic ingress
   layers, and Agent-side instrumentation within the agent runtime
   environment.  It further specifies structured telemetry models,
   cross-layer trace correlation mechanisms, runtime metrics, and
   anomaly detection and remediation workflows.

   The framework enables interoperable telemetry across heterogeneous
   agent systems and deployment environments.  It supports unified
   telemetry ingestion, end-to-end execution trace reconstruction,
   behavioral telemetry, and closed-loop anomaly analysis, providing a
   standardized foundation for agent operations, reliability
   engineering, and compliance auditing.
- **draft-wang-emu-fs-reauth-01** (new-draft, score 5, core_identity) [none]: [Forward Secure Reauthentication in the Extensible Authentication Protocol Method for Authentication and Key Agreement (EAP-AKA')](https://datatracker.ietf.org/doc/draft-wang-emu-fs-reauth/) — This draft specifies an update to RFC 9678, "Forward Secrecy
   Extension to the Improved Extensible Authentication Protocol Method
   for Authentication and Key Agreement (EAP-AKA' FS)", and its
   predecessors RFC 9048, RFC 5448, and RFC 4187.  This update enables
   forward security of the Transient EAP Keys (TEKs) for protecting EAP
   packets, which are not in EAP-AKA' FS.  Based on this extension, the
   executions of reauthentication after a full authentication will be
   unlinkable to each other and then the privacy of end users is
   enhanced.  This update is optional to the above standards.
- **draft-zhao-nmop-nma-a2u-yang-00** (new-draft, score 5, adjacent_watchlist) [none]: [Framework and YANG Data Model for the NMA A2U Interface](https://datatracker.ietf.org/doc/draft-zhao-nmop-nma-a2u-yang/) — This document describes a framework and a YANG data model for the
   Agent-to-User (A2U) interface of a Network Management Agent (NMA).
   The A2U interface is a user-facing interface through which a non-
   agent upper-layer system or user, such as an operator's OSS/BSS,
   orchestrator, management portal, human-facing application, automation
   system, etc., interacts with an NMA.

   The A2U interface supports NMA capability discovery, unified intent
   submission, task lifecycle management, execution plan exposure,
   human-in-the-loop confirmation, task progress notification, and
   consistent error reporting.

   The YANG data model defined in this document includes operational
   state data, RPC operations, and YANG notifications for the A2U
   interface.  The model is intended to be used with YANG-based
   management protocols.  This document does not define a separate
   transport protocol, a new HTTP resource API, or a separate
   notification delivery mechanism.
- **draft-zhao-opsawg-agent-gateway-policy-01** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Gateway Policy Control Model](https://datatracker.ietf.org/doc/draft-zhao-opsawg-agent-gateway-policy/) — This document defines an operational policy control model for
   operator-managed Agent Gateways.  The model describes how an operator
   can control and observe interactions that are admitted, mediated,
   routed, proxied, or otherwise handled by an Agent Gateway.

   The model does not govern an agent's internal behavior, reasoning,
   planning, prompts, memory, tools, runtime, or lifecycle.  Instead, it
   uses agent-related identifiers, groups, tenants, task classes, and
   service levels as gateway-recognized policy matching attributes.
   Those attributes allow an operator-managed Agent Gateway to identify
   the interactions to which a policy applies.

   The model defines four core policy classes: Interaction Access
   Control, QoS and Flow Control, Invocation and Token Control, and Path
   Selection.  It further defines three supporting management
   capabilities: Subject and Attachment Binding, Applied Policy State
   and Telemetry, and Policy Lifecycle and Failure Handling.
- **draft-zhu-agent-registration-discovery-00** (new-draft, score 5, adjacent_watchlist) [none]: [Registration and Discovery Extension for Multi-Model Agents](https://datatracker.ietf.org/doc/draft-zhu-agent-registration-discovery/) — Existing agent registration and discovery mechanisms assume that each
   intelligent agent is backed by a single, static inference model.
   However, in real-world deployments, agents increasingly incorporate
   internal model routing mechanisms where multiple foundation models
   are used dynamically within a single agent based on task complexity,
   latency requirements, system load, and cost constraints.

   Although such agents are exposed externally as single service
   endpoints, their execution behavior is not static and may vary due to
   internal model selection logic that is not visible to external
   systems.  This leads to mismatches between registered metadata and
   actual service behavior, reducing the effectiveness of discovery and
   QoS-aware routing.
- **draft-fane-ai-safety-txt-00** (new-draft, score 4, adjacent_watchlist) [none]: [The ai-safety.txt Domain AI Safety Declaration](https://datatracker.ietf.org/doc/draft-fane-ai-safety-txt/) — This document defines ai-safety.txt, a plain-text declaration format
   that a domain publishes at a well-known location to communicate its
   AI-safety posture to autonomous agents and agent-driven browsers.
   Modeled on the robots.txt convention, an ai-safety.txt file lets a
   domain assert, in a machine-readable form, whether its content is
   safe for autonomous agent consumption, whether that content is
   hardened against prompt injection, and whether it is rendered
   consistently to human and agent user agents.  The file also carries a
   security contact, a link to an external verification record, and the
   date the declaration was last verified.

   The declarations in an ai-safety.txt file are self-asserted by the
   publishing domain.  This document specifies the file format and its
   well-known location, and it is explicit that a consuming agent treats
   a declaration as a hint rather than as proof, verifying it against
   independent evidence where such evidence is available.
- **draft-gebauer-iacp-02** (new-draft, score 4, adjacent_watchlist) [none]: [Internet Agent Communication Protocol](https://datatracker.ietf.org/doc/draft-gebauer-iacp/) — Ever since 1969 and the ARPANET, the internet has repeatedly been
   faced with challenges that it has had to overcome—and has overcome.
   Year after year, the number of users has grown, and year after year,
   the complexity and range of ways in which the internet can be used
   have expanded.  With the advent of AI, we not only have a new type of
   user, we have a different form of communication; the internet itself
   is being attributed a completely different significance.  If they are
   not already, AIs will make up the majority of internet users in the
   foreseeable future.  The question of an ‘AgentNet,’ is not merely a
   question concerning the internet; it is a question of how AIs will
   interact within a global network in the future.
- **draft-ietf-keytrans-protocol-05** (new-draft, score 4, trust_infrastructure) [keytrans]: [Key Transparency Protocol](https://datatracker.ietf.org/doc/draft-ietf-keytrans-protocol/) — While there are several established protocols for end-to-end
   encryption, relatively little attention has been given to securely
   distributing the end-user public keys for such encryption.  As a
   result, these protocols are often still vulnerable to eavesdropping
   by active attackers.  Key Transparency is a protocol for distributing
   sensitive cryptographic information, such as public keys, in a way
   that reliably either prevents interference or detects that it
   occurred in a timely manner.
- **draft-ietf-plants-merkle-tree-certs-05** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
   certificates which integrate public logging of the certificate, in
   the style of Certificate Transparency.  The integrated design reduces
   logging overhead in the face of both shorter-lived certificates and
   large post-quantum signature algorithms, while still achieving
   comparable security properties to existing X.509 constructions and
   Certificate Transparency.  Merkle Tree certificates additionally
   admit an optional size optimization that avoids signatures
   altogether, at the cost of only applying to up-to-date relying
   parties and older certificates.
- **draft-wu-nmop-nma-nti-problem-statement-00** (new-draft, score 4, adjacent_watchlist) [none]: [Problem Statement for Standardizing the northbound Task Interface (NTI) of the Network Management Agent](https://datatracker.ietf.org/doc/draft-wu-nmop-nma-nti-problem-statement/) — AI-driven Network Management Agents (NMAs) are being deployed to
   automate operational workflows such as cross-domain fault diagnosis
   and service remediation.  While the IETF has standardized service
   data models and access protocols through the Controller NBI (RFC
   8969), these provide atomic configuration and monitoring
   capabilities, not the semantics for delegating end-to-end operational
   tasks to an autonomous agent.  As a result, NMA northbound interfaces
   are vendor-specific overlays.  This document defines the problem
   statement for the Northbound Task Interface (NTI): the interface
   through which an operator or OSS delegates operational tasks to an
   NMA.
- **draft-yang-nmrg-mcp-nm-03** (new-draft, score 4, adjacent_watchlist) [none]: [Applicability of MCP for the Network Management](https://datatracker.ietf.org/doc/draft-yang-nmrg-mcp-nm/) — The application of MCP in the network management field is meant to
   refactor network management operation and network capabilities as
   tools and provide more agile and extensible architecture to expose
   these AI integration capabilities.  This document discusses the
   applicability of MCP to the network management plane in the IP
   network that utilizes IETF technologies.  It explores MCP for network
   exposure, multiple MCP server discovery, communication between
   Network Elements or between the Network element and the Network
   Controller/Network Gateway.

## Adjacent / watchlist

- **draft-beeram-teas-yang-mpted-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Multipath Traffic Engineering Directed Acyclic Graph (MPTED) Tunnels and Junctions](https://datatracker.ietf.org/doc/draft-beeram-teas-yang-mpted/) — This document defines a YANG data model for representing, retrieving,
   and manipulating Multipath Traffic Engineering Directed Acyclic Graph
   (MPTED) Tunnels and Junctions.  The model includes two YANG modules,
   one for managing MPTED Tunnels on an MPTED tunnel originator node and
   the other for managing MPTED Junctions on an MPTED junction node.
- **draft-bormann-asdf-sdf-compact-10** (new-draft, score 3, adjacent_watchlist) [asdf]: [Semantic Definition Format (SDF) for Data and Interactions of Things: Compact Notation](https://datatracker.ietf.org/doc/draft-bormann-asdf-sdf-compact/) — The Semantic Definition Format (SDF) is a format for domain experts
   to use in the creation and maintenance of data and interaction models
   that describe Things, i.e., physical objects that are available for
   interaction over a network.  It was created as a common language for
   use in the development of the One Data Model liaison organization
   (OneDM) definitions.  Tools convert this format to database formats
   and other serializations as needed.

   The SDF format is mainly intended for interchange between machine
   generation and machine processing.  However, there is often a need
   for humans to look at and edit SDF models.

   Similar to the way Relax-NG as defined in ISO/IEC 19757-2 has an XML-
   based format and a compact format (its Annex C), this specification
   defines a compact format to go along SDF's JSON-based format.


   // The present version of this document is mostly a proof of concept;
   // it received positive initial feedback on the approach taken and is
   // awaiting completion of the initial implementation.
- **draft-bormann-cose-turbo-kanga-kmac-00** (new-draft, score 3, verifiable_claims) [none]: [COSE Algorithms for KangarooTwelve, TurboSHAKE and KMAC](https://datatracker.ietf.org/doc/draft-bormann-cose-turbo-kanga-kmac/) — RFC 9861 defined and registered four eXtendable-Output Functions
   (XOFs), hash functions with output of arbitrary length, named
   TurboSHAKE128, TurboSHAKE256, KT128, and KT256; the present document
   is intended as the IETF consensus document that is now needed to give
   these algorithms Recommended status in the COSE registry.

   This document specifies concrete instances of those four functions
   above to be used as MACs in COSE.

   This document also specifies concrete instances of KMAC128 and
   KMAC256 in [NIST.SP.800-185] to be used as MACs in COSE and registers
   code points for them.

   And, this document provides "Recommended" status for those algorithms
   for COSE.
- **draft-busi-nmop-simap-rfc8795-applicability-02** (new-draft, score 3, adjacent_watchlist) [none]: [Applicability of RFC8795 YANG data model to SIMAP](https://datatracker.ietf.org/doc/draft-busi-nmop-simap-rfc8795-applicability/) — This document analyses the applicability of the RFC 8795 YANG data
   model to Service & Infrastructure Maps (SIMAP) and in particular
   analysis which requirements can be supported by the existing YANG
   data model defined in RFC 8795.
- **draft-chen-qirg-srv6-qkd-relay-framework-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Framework for SRv6-Based Trusted Key Relay in Quantum Key Distribution Networks](https://datatracker.ietf.org/doc/draft-chen-qirg-srv6-qkd-relay-framework/) — Quantum Key Distribution (QKD) links generate symmetric key material
   between directly connected QKD nodes.  Trusted relay is commonly used
   to extend key delivery beyond the reach of a single QKD link.  A
   complete trusted-relay service requires the network to collect QKD
   link capacity and node trust information, compute a relay path
   according to service requirements, translate the result into an SRv6
   path, and carry the relayed key information in an IPv6/UDP packet
   steered by that SRv6 path.

   This document describes an architectural framework for such a
   service.  Each QKD link provides its available quantum key rate
   capacity, and each relay node provides a trust level.  A controller
   uses these inputs together with application requirements to calculate
   a relay path.  The path-computation algorithm is not standardized and
   may be selected or defined by the user, operator, or implementation.
   The calculated relay sequence is represented as an SRv6 path, and UDP
   packets following that path carry the key-relay information.

   This document identifies the protocol extension points needed to
   support the framework.  The detailed encodings, message formats, SRv6
   behaviors, TLVs, and signaling procedures are left for future work
   and are marked as TBD.
- **draft-elzahr-flow-carbon-trace-00** (new-draft, score 3, adjacent_watchlist) [none]: [Flow-Level Carbon Emissions Tracing for Packet Networks](https://datatracker.ietf.org/doc/draft-elzahr-flow-carbon-trace/) — This document defines a method to derive per-flow energy consumption
   and associated carbon emissions without requiring inline power
   instrumentation for network equipment.  Although energy consumption
   is commonly monitored at the device, network, or facility level,
   fine-grained attribution of energy consumption and carbon emissions
   to individual traffic flows remains an open research problem.  The
   central contribution is the formulation of a flow-level carbon
   accounting model that transforms counter-based traffic measurements
   into energy usage estimates and subsequently into carbon emissions
   using time- and location-dependent carbon intensity data.

   The specification defines a device power model, a flow-level energy
   derivation, and idle-energy attribution methods for flows.  This
   document further highlights how different definitions of carbon
   attribution can lead to significant variability in attributed carbon
   to flows, emphasizing the urgent need to standardize carbon
   accounting definitions and methodologies.  In addition to the
   modeling framework, the document defines mechanisms for telemetry
   collection and deployment models for end-to-end flow tracing to
   support operational use cases.  These elements complement the core
   contribution by enabling implementation and observability.
- **draft-fu-onsen-update-l3sm-service-models-02** (new-draft, score 3, adjacent_watchlist) [none]: [Extensions to the YANG Data Model for L3VPN Service Delivery](https://datatracker.ietf.org/doc/draft-fu-onsen-update-l3sm-service-models/) — RFC8299 defines a YANG data model for L3VPN service delivery.  This
   document defines a set of extensions that address the limitations of
   the L3VPN Service Model (L3SM).  The extensions enable (1)dynamic
   network provisioning with temporary connectivity, (2) dynamic
   bandwidth adjustment, (3) integration of isolation in Slice Service
   Templates to enhance QoS provisioning, (4) performance monitoring for
   enriching service quality visibility, (5)quantum-safe encryption
   integrating both PQC and QKD.
- **draft-gong-spring-sr-policy-group-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for SR Policy Group](https://datatracker.ietf.org/doc/draft-gong-spring-sr-policy-group-yang/) — This document defines YANG data models for Segment Routing (SR)
   Policy group that can be used for configuring, instantiating, and
   managing SR Policy groups. The model is generic and apply equally to
   the MPLS and SRv6 instantiations of SR policy groups.
- **draft-han-bmwg-agent-security-benchmark-00** (new-draft, score 3, agent_identity) [none]: [Security Evaluation Benchmark for AI Agents](https://datatracker.ietf.org/doc/draft-han-bmwg-agent-security-benchmark/) — This document defines a security evaluation benchmark framework for
   AI agents.  It is divided into two parts: evaluation metrics and
   evaluation methodology, comprising four first-level evaluation
   dimensions and 55 second-level metrics, as well as a comprehensive
   evaluation methodology system covering all scenarios, including
   static evaluation, dynamic evaluation, attack-defense evaluation,
   compliance evaluation, and quantitative evaluation.  It aims to
   assess the risk profile of AI agents throughout their entire
   lifecycle, including perception risks, memory risks, decision-making
   risks, and execution risks.
- **draft-havel-nmop-simap-yang-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP).  It extends the RFC8345 YANG modules to support all
   SIMAP requirements.  This document will only focus on modelling
   proposal for each of the requirements not supported by RFC8345.  Any
   related terminology, concepts, use cases and requirements are defined
   outside of this draft and this draft will only refer to them, analyze
   how to model and propose the implementation solutions.
- **draft-huitema-ccwg-c4-design-04** (new-draft, score 3, adjacent_watchlist) [none]: [Design of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-design/) — Christian's Congestion Control Code is a new congestion control
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
- **draft-huitema-ccwg-c4-spec-03** (new-draft, score 3, adjacent_watchlist) [none]: [Specification of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-spec/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design emphasizes
   simplicity and avoids making too many assumptions about the "model"
   of the network.
- **draft-huque-dnsop-multi-alg-rules-08** (new-draft, score 3, adjacent_watchlist) [none]: [Multiple Algorithm Rules in DNSSEC](https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/) — This document restates the requirements on DNSSEC signing and
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
- **draft-ietf-calext-jscalendarbis-17** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-cats-oam-fw-00** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections encompassing clients, network paths, and service
   instances.
- **draft-ietf-ccwg-bbr-06** (new-draft, score 3, adjacent_watchlist) [ccwg]: [BBR Congestion Control](https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/) — This document specifies the BBR congestion control algorithm.  BBR
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
- **draft-ietf-core-responses-01** (new-draft, score 3, adjacent_watchlist) [core]: [CoAP: Non-traditional Response Forms](https://datatracker.ietf.org/doc/draft-ietf-core-responses/) — In CoAP as defined by RFC 7252, there is generally one response for
   each request.  Various CoAP extensions have individually relaxed that
   practice.  The present memo presents a generalized model beyond 1:1
   responses, describes different forms in which it can be used, and
   introduces new CoAP Options that make use of that model.

   Beyond that, this document provides implementation guidance to
   simplify prior extensions, and outlines future possibilities of using
   it.


   // This revision -01 has been created as discussion input for IETF
   // 126.  It makes a first attempt to sort the proposals into short-
   // term actionable ones and more long-term considerations for more
   // kinds of responses that could help additional use cases through
   // future work.
- **draft-ietf-dkim-dkim2-spec-04** (new-draft, score 3, adjacent_watchlist) [dkim]: [DomainKeys Identified Mail Signatures v2 (DKIM2)](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-spec/) — DomainKeys Identified Mail v2 (DKIM2) permits a person, role, or
   organization that owns a signing domain to document that it has
   handled an email message by associating their domain with the
   message.  This is achieved by providing a hash value that has been
   calculated on the current contents of the message and then applying a
   cryptographic signature that covers the hash values and other details
   about the transmission of the message.  Verification is performed by
   querying an entry within the signing domain's DNS space to retrieve
   an appropriate public key.  As a message is transferred from author
   to recipient systems that alter the body or header fields will
   provide details of their changes and calculate new hash values.
   Further signatures will be added to provide a validatable "chain".
   This permits validators to identify the nature of changes made by
   intermediaries and apply a reputation to the systems that made
   changed.  DKIM2 also allows recipients to detect when messages have
   been unexpectedly "replayed" and will ensure that Delivery Status
   Notifications are only sent to entities that were involved in the
   transmission of a message.
- **draft-ietf-dmm-mts-02** (new-draft, score 3, adjacent_watchlist) [dmm]: [Mobile Traffic Steering](https://datatracker.ietf.org/doc/draft-ietf-dmm-mts/) — The evolution of cellular mobile communication systems is aligned
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
- **draft-ietf-dnsop-dnssec-automation-05** (new-draft, score 3, adjacent_watchlist) [dnsop]: [DNSSEC automation](https://datatracker.ietf.org/doc/draft-ietf-dnsop-dnssec-automation/) — This document describes an algorithm and protocol to automate the
   setup, operations, and decommissioning of Multi-Signer DNSSEC
   [RFC8901] configurations.  To accomplish this, it employs Model 2 of
   the multi-signer specification (where each operator has their own
   distinct KSK and ZSK sets, or CSK sets), management of DS records
   from the parent via CDS/CDNSKEY [RFC8078], and Child-to-Parent
   Synchronization in DNS [RFC7477].
- **draft-ietf-httpapi-patch-byterange-04** (new-draft, score 3, adjacent_watchlist) [httpapi]: [Byte Range PATCH](https://datatracker.ietf.org/doc/draft-ietf-httpapi-patch-byterange/) — This document specifies a media type for PATCH payloads that
   overwrites a specific byte range, facilitating random access writes
   and segmented uploads of resources.
- **draft-ietf-httpbis-no-vary-search-06** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   URI query parameters impact caching.
- **draft-ietf-httpbis-resumable-upload-12** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
- **draft-ietf-ipsecme-ikev2-pqc-auth-09** (new-draft, score 3, core_identity) [ipsecme]: [Signature Authentication in the Internet Key Exchange Version 2 (IKEv2) using PQC](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-pqc-auth/) — Signature-based authentication methods are utilized in the Internet
   Key Exchange Version 2 (IKEv2).  The current version of the IKEv2
   protocol, specified in RFC 7296, supports traditional digital
   signatures.

   This document specifies a generic mechanism for integrating post-
   quantum cryptographic (PQC) digital signature algorithms into the
   IKEv2 protocol.  The approach allows for seamless inclusion of any
   PQC signature scheme within the existing authentication framework of
   IKEv2.  Additionally, it outlines how Module-Lattice-Based Digital
   Signatures (ML-DSA) and Stateless Hash-Based Digital Signatures (SLH-
   DSA), can be employed as authentication methods within the IKEv2
   protocol, as they have been standardized by US NIST.
- **draft-ietf-ivy-network-inventory-location-06** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Data Model for Network Inventory Location](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-location/) — This document defines a YANG data model for Network Inventory
   location (e.g., site, room, rack, geo-location data), which provides
   location information with different granularity levels for
   inventoried network elements.

   Accurate location information is useful for network planning,
   deployment, and maintenance.  However, such information cannot be
   obtained or verified from the Network Elements themselves.  This
   document defines a location model for network inventory that extends
   the base inventory with comprehensive location data.
- **draft-ietf-ivy-network-inventory-software-04** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Network Data Model of Network Inventory Software Extensions](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-software/) — This document extends the base Network Inventory YANG model to
   support non-physical network elements (NEs), such as controllers,
   virtual routers, and virtual firewalls, as well as software
   components like platform operating systems and software modules.  In
   addition to the software revisions and patches already defined in the
   base model, this extension introduces software status and time stamp
   information.
- **draft-ietf-jose-hpke-encrypt-22** (new-draft, score 3, adjacent_watchlist) [jose]: [Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/) — This specification defines how to use Hybrid Public Key Encryption
   (HPKE) with JSON Web Encryption (JWE).  HPKE enables public key
   encryption of arbitrary-sized plaintexts to a recipient's public key,
   and provides security against adaptive chosen ciphertext attacks.
   This specification chooses a specific subset of the HPKE features to
   use with JWE.

   This specification updates RFC 7516 (JWE) to enable use of Integrated
   Encryption as a Key Management Mode.
- **draft-ietf-lake-app-profiles-05** (new-draft, score 3, verifiable_claims) [lake]: [Coordinating the Use of Application Profiles for Ephemeral Diffie-Hellman Over COSE (EDHOC)](https://datatracker.ietf.org/doc/draft-ietf-lake-app-profiles/) — The lightweight authenticated key exchange protocol Ephemeral Diffie-
   Hellman Over COSE (EDHOC) requires certain parameters to be agreed
   out-of-band, in order to ensure its successful completion.  To this
   end, application profiles specify the intended use of EDHOC to allow
   for the relevant processing and verifications to be made.  In order
   to ensure the applicability of such parameters and information beyond
   transport- or setup-specific scenarios, this document defines a
   canonical, CBOR-based representation that can be used to describe,
   distribute, and store EDHOC application profiles.  Furthermore, in
   order to facilitate interoperability between EDHOC implementations
   and support EDHOC extensibility for additional integrations, this
   document defines a number of means to coordinate the use of EDHOC
   application profiles.  Finally, this document defines a set of well-
   known EDHOC application profiles.
- **draft-ietf-lake-edhoc-impl-cons-07** (new-draft, score 3, verifiable_claims) [lake]: [Implementation Considerations for Ephemeral Diffie-Hellman Over COSE (EDHOC)](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-impl-cons/) — This document provides considerations for guiding the implementation
   of the authenticated key exchange protocol Ephemeral Diffie-Hellman
   Over COSE (EDHOC).
- **draft-ietf-masque-connect-udp-ecn-dscp-01** (new-draft, score 3, adjacent_watchlist) [masque]: [ECN and DSCP support for HTTPS's Connect-UDP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-ecn-dscp/) — HTTP's Extended Connect's Connect-UDP protocol enables a client to
   proxy a UDP flow from the HTTP server towards a specified target IP
   address and UDP port.  QUIC and Real-time transport protocol (RTP)
   are examples of transport protocols that use UDP and support Explicit
   Congestion Notification (ECN) and provide the necessary feedback.
   This document specifies how ECN and DSCP can be supported through an
   extension to the Connect-UDP protocol for HTTP without per-packet
   byte overhead, solely using Context IDs.
- **draft-ietf-masque-http-datagram-compression-01** (new-draft, score 3, adjacent_watchlist) [masque]: [Extensions to Compress and Derive Fields in HTTP Datagrams](https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/) — This document defines extensions for HTTP Datagram-based protocols
   that improve transmission efficiency by introducing templates for
   compressing or deriving datagram fields.

   These templates allow endpoints to define parts of datagrams that are
   static and can be removed, and other parts that can be derived (such
   as packet lengths and checksum values).

   Additionally, this document defines a checksum offload procedure
   enabling receivers to complete Internet checksums using sender-
   provided partial values.

   These optimisations reduce per-packet overhead, processing cost, and
   increase the effective maximum transmission unit (MTU) when datagrams
   are encapsulated in QUIC DATAGRAM frames.
- **draft-ietf-masque-quic-proxy-09** (new-draft, score 3, adjacent_watchlist) [masque]: [QUIC-Aware Proxying Using HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-quic-proxy/) — This document extends UDP Proxying over HTTP to add optimizations for
   proxied QUIC connections.  Specifically, it allows a proxy to reuse
   UDP 4-tuples for multiple proxied connections, and adds a mode of
   proxying in which QUIC short header packets can be forwarded and
   transformed through a HTTP/3 proxy rather than being fully re-
   encapsulated and re-encrypted.
- **draft-ietf-mimi-room-policy-04** (new-draft, score 3, adjacent_watchlist) [mimi]: [Room Policy for the More Instant Messaging Interoperability (MIMI) Protocol](https://datatracker.ietf.org/doc/draft-ietf-mimi-room-policy/) — This document describes a set of concrete room policies for the More
   Instant Messaging Interoperability (MIMI) Working Group.  It
   describes several independent properties and policy attributes which
   can be combined to model a wide range of chat and multimedia
   conference types.
- **draft-ietf-mls-targeted-messages-01** (new-draft, score 3, core_identity) [mls]: [Messaging Layer Security (MLS) Targeted Messages](https://datatracker.ietf.org/doc/draft-ietf-mls-targeted-messages/) — This document defines targeted messages for the Messaging Layer
   Security (MLS) protocol.  A targeted message allows a member of an
   MLS group to send an encrypted and authenticated message to another
   member of the same group without creating a new group.  The mechanism
   reuses Hybrid Public Key Encryption (HPKE) and the MLS key schedule
   to provide confidentiality, authentication, and binding to the group
   state.
- **draft-ietf-netconf-list-pagination-13** (new-draft, score 3, adjacent_watchlist) [netconf]: [List Pagination for YANG-driven Protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination/) — In some circumstances, instances of YANG modeled "list" and "leaf-
   list" nodes may contain numerous entries.  Retrieval of all the
   entries can lead to inefficiencies in the server, the client, and the
   network in between.

   This document defines a model for list pagination that can be
   implemented by YANG-driven management protocols such as NETCONF and
   RESTCONF.  The model supports paging over optionally filtered and/or
   sorted entries.  The solution additionally enables servers to
   constrain query expressions on some "config false" lists or leaf-
   lists.
- **draft-ietf-netmod-sub-intf-vlan-model-18** (new-draft, score 3, adjacent_watchlist) [netmod]: [Sub-interface VLAN YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-netmod-sub-intf-vlan-model/) — This document defines YANG modules to add support for classifying
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
- **draft-ietf-netmod-yang2-00** (new-draft, score 3, adjacent_watchlist) [netmod]: [The YANG 2.0 Data Modeling Language](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/) — YANG is a data modeling language used to model configuration data,
   state data, Remote Procedure Calls, and notifications for network
   management protocols.  This document describes the syntax and
   semantics of version 2.0 of the YANG language.  YANG version 2.0 is a
   major release of the YANG language, addressing issues found in the
   original specification.
- **draft-ietf-nmop-network-incident-yang-10** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG Module for the network incident
   lifecycle management.  This YANG module is meant to provide a
   standard way to report, diagnose, and help reduce troubleshooting
   tickets and resolve network incidents for the sake of network service
   health and probable cause analysis.
- **draft-ietf-opsawg-collected-data-manifest-12** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push, to
   continuously stream information, including both counters and state
   information.  This document describes the metadata that ensure that
   the collected data can be interpreted correctly.  This document
   specifies the Data Manifest, composed of two YANG data models (the
   Platform Manifest and the non-normative Data Collection Manifest).
   These YANG modules are specified at the network level (e.g., network
   controllers) to provide a model that encompasses several network
   platforms.  The Data Manifest must be streamed and stored along with
   the data, up to the collection and analytics systems to keep the
   collected data fully exploitable by the data scientists and relevant
   tools.  Additionally, this document specifies an augmentation of the
   YANG-Push model to include the actual collection period, in case it
   differs from the configured collection period.
- **draft-ietf-opsawg-ipfix-gtpu-17** (new-draft, score 3, core_identity) [opsawg]: [Export of GTP-U Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-gtpu/) — This document introduces IP Flow Information Export (IPFIX)
   Information Elements to report information contained in the Generic
   Packet Radio Service Tunneling Protocol (GTP) User Plane header such
   as Tunnel Endpoint Identifier, and data contained in its session
   container extension header.
- **draft-ietf-opsawg-ipfix-path-segment-03** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 paths identification.
- **draft-ietf-opsawg-scheduling-oam-tests-07** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A YANG Data Model for Network Diagnosis using Scheduled Sequences of OAM Tests](https://datatracker.ietf.org/doc/draft-ietf-opsawg-scheduling-oam-tests/) — This document defines two YANG data models to support on-demand
   network diagnosis using Operations, Administration, and Maintenance
   (OAM) tests.  This document defines both 'oam-unitary-test' and 'oam-
   test-sequence' YANG modules to manage the lifecycle of network
   diagnosis procedures, intended for use by external management and
   orchestration systems (including SDN controllers and network
   orchestrators), rather than by individual network nodes.
- **draft-ietf-pce-pcep-ifit-09** (new-draft, score 3, adjacent_watchlist) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions to Enable IFIT](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-ifit/) — In-situ Flow Information Telemetry (IFIT) refers to network OAM data
   plane on-path telemetry techniques, in particular In-situ OAM (IOAM)
   and Alternate Marking.  This document defines PCEP extensions to
   allow a Path Computation Client (PCC) to indicate which IFIT features
   it supports, and a Path Computation Element (PCE) to configure IFIT
   behavior at a PCC for a specific path in the stateful PCE model.  The
   application to Segment Routing (SR) is reported.  However, the PCEP
   extensions described in this document can be generalized for all path
   types, but that is out of scope of this document.
- **draft-ietf-ppm-dap-19** (new-draft, score 3, adjacent_watchlist) [ppm]: [Distributed Aggregation Protocol for Privacy Preserving Measurement](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/) — There are many situations in which it is desirable to take
   measurements of data which people consider sensitive.  In these
   cases, the entity taking the measurement is usually not interested in
   people's individual responses but rather in aggregated data.
   Conventional methods require collecting individual responses and then
   aggregating them on some server, thus representing a threat to user
   privacy and rendering many such measurements difficult and
   impractical.  This document describes a multi-party Distributed
   Aggregation Protocol (DAP) for privacy preserving measurement which
   can be used to collect aggregate data without revealing any
   individual contributor's data.
- **draft-ietf-sidrops-aspa-verification-26** (new-draft, score 3, authorization) [sidrops]: [BGP AS_PATH Verification Based on Autonomous System Provider Authorization (ASPA) Objects](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) — This document describes procedures that make use of Autonomous System
   Provider Authorization (ASPA) objects in the Resource Public Key
   Infrastructure (RPKI) to verify the Border Gateway Protocol (BGP)
   AS_PATH attribute of advertised routes.  This AS_PATH verification
   enhances routing security by adding means to detect and mitigate
   route leaks and AS_PATH manipulations.
- **draft-ietf-spring-sr-policy-yang-08** (new-draft, score 3, adjacent_watchlist) [spring]: [YANG Data Model for Segment Routing Policy](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-yang/) — This document defines a YANG data model for Segment Routing (SR)
   Policy that can be used for configuring, instantiating, and managing
   SR policies.  The model is generic and applies equally to the MPLS
   and SRv6 instantiations of SR policies.
- **draft-ietf-stir-certificates-shortlived-06** (new-draft, score 3, core_identity) [stir]: [Short-Lived Certificates for Secure Telephone Identity](https://datatracker.ietf.org/doc/draft-ietf-stir-certificates-shortlived/) — When certificates are used as credentials to attest the assignment of
   ownership of telephone numbers, some mechanism is required to provide
   certificate freshness.  This document specifies short-lived
   certificates as a means of guaranteeing certificate freshness for
   secure telephone identity (STIR), potentially relying on the
   Automated Certificate Management Environment (ACME) or similar
   mechanisms to allow signers to acquire certificates as needed.
- **draft-ietf-teas-composite-network-slices-01** (new-draft, score 3, core_identity) [teas]: [Realization of Composite IETF Network Slices](https://datatracker.ietf.org/doc/draft-ietf-teas-composite-network-slices/) — A network slice offers connectivity services to a network slice
   customer with specific Service Level Objectives (SLOs) and Service
   Level Expectations (SLEs) over a common underlay network.  RFC 9543
   describes a framework for network slices built in networks that usWe
   IETF technologies.  As part of that framework, the Network Resource
   Partition (NRP) is introduced as a collection of network resources
   that are allocated from the underlay network to carry a specific set
   of network slice service traffic and meet specific SLOs and SLEs.  In
   some network scenarios, network slices using IETF technologies may
   span multiple network domains, and they may be composed
   hierarchically, which means a network slice itself may be further
   sliced.  In the context of 5G, a 5G end-to-end network slice consists
   of three different types of network technology segments: Radio Access
   Network (RAN), Transport Network (TN) and Core Network (CN).  The
   transport segments of the 5G end-to-end network slice can be provided
   using network slices described in RFC 9543.

   This document first describes the possible use cases of composite
   network slices built in networks that use IETF network technologies,
   then it provides considerations about the realization of composite
   network slices.  For the multi-domain network slices, an Inter-Domain
   Network Resource Partition Identifier (Inter-domain NRP ID) may be
   introduced.  For hierarchical network slices, the structure of the
   NRP ID is discussed.  And for the interaction between IETF network
   slices with 5G network slices, the identifiers of the 5G network
   slices may be introduced into IETF networks.  These network slice-
   related identifiers may be used in the data plane, control plane and
   management plane of the network for the instantiation and management
   of composite network slices.  This document also describes the
   management considerations of composite network slices.
- **draft-ietf-teas-ns-models-applicability-02** (new-draft, score 3, adjacent_watchlist) [teas]: [Applicability of IETF-Defined Service and Network Data Models for Network Slice Service Management](https://datatracker.ietf.org/doc/draft-ietf-teas-ns-models-applicability/) — This document exemplifies how the various data models that are
   produced in the IETF can be combined in the context of Network Slice
   Services delivery.

   Specifically, this document describes the relationship between the
   Network Slice Service models for requesting Network Slice Services
   and both Service (e.g., the L3VPN Service Model, the L2VPN Service
   Model) and Network (e.g., the L3VPN Network Model, the L2VPN Network
   Model) models used during their realization.  In addition, this
   document describes the communication between a Network Slice
   Controller (NSC) and the network controllers for the realization of
   Network Slices.

   The Network Slice Service YANG model provides a customer-oriented
   view of the intended Network Slice Service.  Thus, once an NSC
   receives a request for a Slice Service request, the NSC has to map it
   to accomplish the specific objectives expected by the network
   controllers.  Existing YANG network models are analyzed against
   Network Slice requirements, and the gaps in existing models are
   identified.
- **draft-ietf-teas-te-topology-profiles-06** (new-draft, score 3, adjacent_watchlist) [teas]: [Profiles for Traffic Engineering (TE) Topology Data Model and Applicability to non-TE-centric Use Cases](https://datatracker.ietf.org/doc/draft-ietf-teas-te-topology-profiles/) — This document describes how profiles of the Topology YANG data model,
   defined in RFC8795, can be used to address applications in Traffic
   Engineering aware (TE-aware) deployments, irrespective of whether
   they are TE-centric or not.
- **draft-ietf-teas-yang-topology-filter-03** (new-draft, score 3, adjacent_watchlist) [teas]: [YANG Data Model for Topology Filter](https://datatracker.ietf.org/doc/draft-ietf-teas-yang-topology-filter/) — This document defines a YANG data model for the management of
   topology filters/filter-sets on network elements and controllers.
- **draft-ietf-tls-pake-02** (new-draft, score 3, adjacent_watchlist) [tls]: [A Password Authenticated Key Exchange Extension for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-pake/) — The pre-shared key mechanism available in TLS 1.3 is not suitable for
   usage with low-entropy keys, such as passwords entered by users.
   This document describes an extension that enables the use of
   password-authenticated key exchange protocols with TLS 1.3.
- **draft-ietf-tls-rfc9147bis-02** (new-draft, score 3, adjacent_watchlist) [tls]: [The Datagram Transport Layer Security (DTLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-rfc9147bis/) — This document specifies version 1.3 of the Datagram Transport Layer
   Security (DTLS) protocol.  DTLS 1.3 allows client/server applications
   to communicate over the Internet in a way that is designed to prevent
   eavesdropping, tampering, and message forgery.

   The DTLS 1.3 protocol is based on the Transport Layer Security (TLS)
   1.3 protocol and provides equivalent security guarantees with the
   exception of order protection / non-replayability.  Datagram
   semantics of the underlying transport are preserved by the DTLS
   protocol.

   This document obsoletes RFC 6347.
- **draft-ietf-tsvwg-sctp-dtls-chunk-04** (new-draft, score 3, core_identity) [tsvwg]: [Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/) — This document describes a method for adding Datagram Transport Layer
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
- **draft-ietf-webtrans-http2-15** (new-draft, score 3, adjacent_watchlist) [webtrans]: [WebTransport over HTTP/2](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http2/) — WebTransport defines a set of low-level communications features
   designed for client-server interactions that are initiated by Web
   clients.  This document describes a protocol that can provide the
   capabilities of WebTransport over HTTP/2.  This protocol enables the
   use of WebTransport when a UDP-based protocol is not available.
- **draft-intra-handshake-fail-00** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake.fail (CVE-2026-33697 of CVSS 7.5)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697, which
   is substantial technical evidence of how intra-handshake attestation
   fails in practice.
- **draft-irtf-cfrg-bls-signature-07** (new-draft, score 3, adjacent_watchlist) [cfrg]: [BLS Signatures](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bls-signature/) — BLS is a digital signature scheme with aggregation properties.  Given
   set of signatures (signature_1, ..., signature_n) anyone can produce
   an aggregated signature.  Aggregation can also be done on secret keys
   and public keys.  Furthermore, the BLS signature scheme is
   deterministic, non-malleable, and efficient.  Its simplicity and
   cryptographic properties allows it to be useful in a variety of use-
   cases, specifically when minimal storage space or bandwidth are
   required.
- **draft-irtf-cfrg-concrete-hybrid-kems-04** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Concrete Hybrid PQ/T Key Encapsulation Mechanisms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-concrete-hybrid-kems/) — PQ/T Hybrid Key Encapsulation Mechanisms (KEMs) combine "post-
   quantum" cryptographic algorithms, which are safe from attack by a
   quantum computer, with "traditional" algorithms, which are not.  CFRG
   has developed a general framework for creating hybrid KEMs.  In this
   document, we define concrete instantiations of this framework to
   illustrate certain properties of the framework and simplify
   implementors' choices.
- **draft-irtf-cfrg-cryptography-specification-03** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Guidelines for Writing Cryptography Specifications](https://datatracker.ietf.org/doc/draft-irtf-cfrg-cryptography-specification/) — This document provides guidelines and best practices for writing
   technical specifications for cryptography protocols and primitives,
   targeting the needs of implementers, researchers, and protocol
   designers.  It highlights the importance of technical specifications
   and discusses strategies for creating high-quality specifications
   that cater to the needs of each community, including guidance on
   representing mathematical operations, security definitions, and
   threat models.
- **draft-irtf-cfrg-hybrid-kems-12** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Hybrid PQ/T Key Encapsulation Mechanisms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-hybrid-kems/) — This document defines generic constructions for hybrid Key
   Encapsulation Mechanisms (KEMs) based on combining a post-quantum
   (PQ) KEM with a traditional cryptographic component.  Hybrid KEMs
   built using these constructions provide strong security properties as
   long as either of the underlying algorithms are secure.
- **draft-jadoon-green-isac-utilization-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Reporting Utilization Scores in ISAC](https://datatracker.ietf.org/doc/draft-jadoon-green-isac-utilization/) — This document defines a YANG data model to report an ISAC Utilization
   Score (US) in Integrated Sensing and Communication (ISAC) systems.
   The US is an abstract, normalized score (0..100) that summarizes the
   relative resource cost of executing a sensing operation on a device.

   The model supports a mandatory overall US and optional explanatory
   component impact scores (compute, memory, energy, storage, latency).
   The model also supports optional metadata (e.g., timestamp,
   aggregation window, and scoring method identification) describing how
   a reported score was derived.

   This revision aligns terminology and leaf names to reduce ambiguity
   between normalized impact scores and raw resource telemetry, removes
   per-measurement-related objects to keep the model focused on an
   overall score, and specifies a companion augmentation module (Path 1)
   that attaches ISAC utilization telemetry to a GREEN Energy Object (as
   defined by the GREEN Power and Energy YANG Module) for correlation
   with power/energy telemetry.
- **draft-kohbrok-ipsecme-mls-gike-00** (new-draft, score 3, adjacent_watchlist) [none]: [MLS for IPsec Group Key Exchange](https://datatracker.ietf.org/doc/draft-kohbrok-ipsecme-mls-gike/) — This document describes a profile that uses the Messaging Layer
   Security (MLS) protocol as the group key-management substrate for
   Group Key Management using IKEv2 (G-IKEv2).  The intent is to
   preserve the operational model of G-IKEv2, including IKEv2 transport,
   GSA policy distribution, a central GCKS, and the IPsec ESP data
   plane, while replacing GDOI-style group key distribution with an MLS
   group.  The resulting design can be read as G-IKEv2 where MLS
   produces the per-epoch group secret used to key the IPsec ESP Data-
   Security SA.
- **draft-labiod-rats-attester-groups-05** (new-draft, score 3, trust_infrastructure) [none]: [Attester Groups for Remote Attestation](https://datatracker.ietf.org/doc/draft-labiod-rats-attester-groups/) — This document proposes an extension to the Remote Attestation
   Procedures architecture by introducing the concept of Attester
   Groups.  This extension aims to reduce computational and
   communication overhead by enabling collective Evidence appraisal of
   high number of homogeneous devices with similar characteristics,
   thereby improving the scalability of attestation processes.
- **draft-lemmons-cose-composite-claims-03** (new-draft, score 3, verifiable_claims) [none]: [Composite Token Claims](https://datatracker.ietf.org/doc/draft-lemmons-cose-composite-claims/) — Composite claims are claims for CBOR Web Tokens (CWTs) and JSON Web
   Tokens (JWTs) that define logical relationships between sets of
   claims.  This document also defines a CWT representation of the
   "crit" (Critical) claim.
- **draft-lg-lsr-router-id-conflict-detect-00** (new-draft, score 3, core_identity) [none]: [Detection of Router-ID Conflicts in IGPs](https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/) — In link-state Interior Gateway Protocols (IGPs) such as OSPF and IS-
   IS, the router ID (or system ID) serves as a unique identifier for
   routers within a routing domain. Duplicate router IDs can lead to
   severe network instability, including persistent Link State
   Advertisement (LSA/LSP) flooding, inconsistent Link State Databases
   (LSDBs), and permanent forwarding loops.

   This document defines mechanisms for detecting such conflicts
   between non-adjacent routers and proposes procedures to alert
   network operators, along with defining the corresponding YANG
   interface and event YANG notifications for OAM operations.
- **draft-li-ccamp-ospf-te-extension-computing-cap-00** (new-draft, score 3, ai_infrastructure) [none]: [OSPF-TE Extensions for Computing Capability Advertisement](https://datatracker.ietf.org/doc/draft-li-ccamp-ospf-te-extension-computing-cap/) — This document defines extensions to OSPF Traffic Engineering (OSPF-
   TE) for advertising computing capability information associated with
   Artificial Intelligence Data Centers (AIDCs) in optical networks.
   The extensions enable an ASON or GMPLS-capable optical network to
   maintain a synchronized view of both network TE resources and
   selected computing resource attributes, so that service placement and
   path computation can consider computing resource status.

   The mechanism uses OSPFv2 Type-10 Opaque LSAs and a set of top-level
   TLVs and sub-TLVs.  The extensions do not define new OSPF packet
   types and do not modify the OSPF neighbor establishment, database
   exchange, flooding, or acknowledgement procedures.
- **draft-mahy-mimi-identity-05** (new-draft, score 3, core_identity) [none]: [More Instant Messaging Interoperability (MIMI) Identity Concepts](https://datatracker.ietf.org/doc/draft-mahy-mimi-identity/) — This document explores the problem space in instant messaging (IM)
   identity interoperability when using end-to-end encryption, for
   example with the MLS (Message Layer Security) Protocol.  It also
   describes naming schemes for different types of IM identifiers.
- **draft-mattsson-cfrg-aes-gcm-sst-21** (new-draft, score 3, core_identity) [none]: [Galois Counter Mode with Strong Secure Tags (GCM-SST)](https://datatracker.ietf.org/doc/draft-mattsson-cfrg-aes-gcm-sst/) — This document defines Galois Counter Mode with Strong Secure Tags
   (GCM-SST), an Authenticated Encryption with Associated Data (AEAD)
   algorithm that addresses several weaknesses of GCM.  GCM-SST can be
   used with any keystream generator, not only 128-bit block ciphers.
   Main differences from GCM are the introduction of a second
   authentication subkey H_2, per-nonce derivation of both H and H_2,
   and stricter usage limits.  Together, these changes yield
   authentication tags with near-ideal forgery probabilities, including
   reforgeability resistance.  All registered instances have an expected
   number of forgeries E(F) ≈ v / 2^t, a property that GCM is far from
   providing.  GCM-SST is designed for security protocols with replay
   protection such as TLS, QUIC, SRTP, and PDCP, and provides hardware
   and software performance comparable to GCM.  This document registers
   nine AEAD algorithm instances using AES and Rijndael-256 in counter
   mode, with tag lengths of 48, 96, and 112 bits.  GCM-SST has been
   standardized by 3GPP for use with SNOW 5G, AES-256, and ZUC-256.
- **draft-melegassi-coherence-bfd-01** (new-draft, score 3, trust_infrastructure) [none]: [Coherence-BFD: Sub-Second Coherence Detection Using Bidirectional Forwarding Detection Patterns](https://datatracker.ietf.org/doc/draft-melegassi-coherence-bfd/) — This document specifies Coherence-BFD, a protocol that combines
   the asynchronous heartbeat, demand-mode, echo function, and
   detection-multiplier mechanisms of Bidirectional Forwarding
   Detection (BFD, [RFC5880]) with the multi-vantage path coherence
   detection of [I-D.melegassi-mvps-incremental-be].  The result is
   a sub-second coherence failure detector with theoretical and
   empirical detection latency of 55 ms (1091x faster than the
   60-second tick baseline of the underlying BE-MVPS framework).

   Five execution variants are specified: V0 (baseline), V1
   (heartbeat-fast), V2 (demand), V3 (echo), and V4 (hybrid).  Wall-
   clock benchmarks confirm V3 (Echo) as the latency-optimal variant
   at 55 ms median tau_detect with 39 680 B/s bandwidth.

   This revision (-01) adds three layers of proof:

     (a) Canonical: formal proofs of the detection lower-bound
         (Theorem T-BFD-1), false-positive-rate decay (Theorem
         T-BFD-2), and connection to the GDDP geometric-
         precision framework (Corollary C-BFD-3).

     (b) Empirical: SHA-256-anchored benchmark receipts
         reproducible from the public reference scripts.

     (c) Real data: validation against 92 067 RIPE Atlas RTT
         measurements from 450+ globally-distributed anchors
         spanning 2+ months of continuous collection.

   NOTE ON DATA PROVENANCE.  Wall-clock detection-latency and
   bandwidth numbers in Section 10 are obtained from controlled
   benchmarks (scripts/benchmark_coherence_bfd.py).  Real-data
   validation in Section 18 uses live Internet RTT measurements
   from RIPE Atlas to confirm that the theoretical bounds hold
   on operational paths.

   HARDWARE CAVEAT.  The 55 ms median tau_detect is a SOFTWARE-
   HARNESS measurement, not a router-class measurement.  Validation
   against real BFD hardware is identified as required future work
   before progression past Experimental status.
- **draft-meunier-privacypass-reverse-flow-06** (new-draft, score 3, privacy_security) [none]: [Privacy Pass Reverse Flow](https://datatracker.ietf.org/doc/draft-meunier-privacypass-reverse-flow/) — This document specifies an instantiation of Privacy Pass Architecture
   [RFC9576] that allows for a "reverse" flow from the Origin to the
   Client.  It describes a method for an Origin to issue a state update
   to the Client in response to a request in which a token is redeemed.
- **draft-ochkas-cose-ascon-04** (new-draft, score 3, verifiable_claims) [none]: [Ascon-AEAD128 and Ascon-Hash256 for COSE](https://datatracker.ietf.org/doc/draft-ochkas-cose-ascon/) — This document describes CBOR Object Signing and Encryption (COSE)
   serialization with Ascon, a NIST standard for lightweight
   cryptography.

   In 2019, as a part of CAESAR competition, Ascon-128 and Ascon-128a
   were selected as the first choice for the lightweight authenticated
   encryption.  After, in 2023, National Institute of Standards and
   Technology (NIST) selected Ascon family of cryptographic algorithms
   to be the standard for lightweight cryptography.  In August 2025,
   NIST Special Publication 800-232 was released, defining Ascon-based
   lightweight cryptography standards for constrained devices.  This
   recognition makes it particularly interesting to enable using Ascon
   with COSE structures.
- **draft-piraux-tcp-ao-tls-04** (new-draft, score 3, core_identity) [none]: [Opportunistic TCP-AO with TLS](https://datatracker.ietf.org/doc/draft-piraux-tcp-ao-tls/) — This document specifies an opportunistic mode for TCP-AO when used
   with TLS.  In this mode, the TCP connection starts with a well-known
   authentication key which is later replaced by a secure key derived
   from the TLS handshake.
- **draft-pocero-lake-authkemsig-edhoc-01** (new-draft, score 3, core_identity) [none]: [KEM/Signature-Based Methods for Scenarios with Asymmetric Device Constraints](https://datatracker.ietf.org/doc/draft-pocero-lake-authkemsig-edhoc/) — This document extends the KEM-based Authentication for EDHOC draft by
   defining additional quantum-resistant authentication methods that
   support combined authentication approaches, where one party
   authenticates using a KEM-based mechanism and the other using a post-
   quantum signature scheme.
- **draft-porfiri-tsvwg-sctp-dtls-handshake-01** (new-draft, score 3, core_identity) [none]: [Transport Layer Security (TLS) based key-management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk](https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/) — This document defines how Transport Layer Security (TLS) 1.3 is used
   as a key-management method for the SCTP DTLS Chunk mechanism.  It
   specifies how a TLS handshake establishes the initial security
   context for an SCTP association and how subsequent TLS handshakes
   provide key updates and re-authentication.  The goal is to enable
   authenticated and confidential communication over SCTP using the DTLS
   Chunk, leveraging standardized TLS 1.3 features for key management
   and rekeying.
- **draft-ritz-seat-proxies-00** (new-draft, score 3, trust_infrastructure) [none]: [Bridging Remote Attestation with Secure Channel Protocol Proxies](https://datatracker.ietf.org/doc/draft-ritz-seat-proxies/) — This document specifies a transport-layer mechanism to establish an
   end-to-end cryptographic channel across a cooperative secure channel
   protocol intermediary, such as a TLS-terminating proxy.

   The mechanism enables Remote Attestation Evidence to remain bound to
   the true end-to-end endpoints even when the initial secure channel
   handshake is mediated by an intermediary.  It uses an ephemeral HPKE
   challenge exchange, intra-handshake Evidence delivery, and an
   attestation-bound key update to evict the intermediary from Layer 7
   visibility before application data is exchanged.
- **draft-sardar-rats-sec-cons-04** (new-draft, score 3, trust_infrastructure) [none]: [Guidelines for Security Considerations of RATS](https://datatracker.ietf.org/doc/draft-sardar-rats-sec-cons/) — This document aims to provide guidelines and best practices for
   writing security considerations for technical specifications for RATS
   targeting the needs of implementers, researchers, and protocol
   designers.  In particular, it discusses some of the 'bottom turtle'
   issues.  This is a work-in-progress, and the current version mainly
   presents an outline of the topics that future versions will cover in
   more detail.

   *  Corrections in published RATS RFCs

   *  Security concerns in two RATS drafts

   *  General security guidelines, baseline, or template for RATS
- **draft-sidor-pce-binding-label-sid-extensions-03** (new-draft, score 3, core_identity) [none]: [Binding Label/Segment Identifier (SID) Extensions in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-binding-label-sid-extensions/) — The Path Computation Element Communication Protocol (PCEP) provides
   mechanisms for Path Computation Elements (PCEs) to instantiate and
   manage Label Switched Paths (LSPs) on a Path Computation Client
   (PCC).  This includes the ability for a PCE to specify a Binding
   Segment Identifier (SID) for an LSP.

   A binding value specified by a PCE may not be available for use on
   the PCC.  This can lead to LSP instantiation failures or entire PCEP
   message being rejected.

   This document proposes extensions to PCEP to allow a PCC to fall back
   to allocating a Binding SID from its own dynamic range if the value
   specified by the PCE is unavailable.  It also defines a mechanism for
   the PCC to report both the requested and the allocated binding values
   back to the PCE.
- **draft-skyfire-oauth-kyapay-token-exchange-00** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-sriram-sidrops-asra-verification-05** (new-draft, score 3, authorization) [none]: [Autonomous System Relationship Authorization (ASRA) as an Extension to ASPA for Enhanced AS Path Verification](https://datatracker.ietf.org/doc/draft-sriram-sidrops-asra-verification/) — An Autonomous System Provider Authorization (ASPA) record authorizes
   provider ASes of a customer AS.  While ASPA-based AS_PATH
   verification can correctly detect and mitigate route leaks and some
   forged-origin or forged-path-segment hijacks, it fails to detect some
   malicious path manipulations for routes that are received from
   transit providers.  This document utilizes a new RPKI object called
   Autonomous System Relationship Authorization (ASRA) that
   significantly enhances AS_PATH verification complementing ASPA.  ASRA
   fills in a significant gap in the ASPA method by adding the
   capability to detect fake links in the AS_PATHs in BGP Updates
   propagated from providers to customers.  ASRA achieves this by
   allowing an AS to register additional AS relationships, i.e.,
   customers and lateral peers.
- **draft-su-sidrops-rpki-rp-incremental-validation-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Publication-Point-Based Incremental Validation Procedure for RPKI Relying Parties](https://datatracker.ietf.org/doc/draft-su-sidrops-rpki-rp-incremental-validation/) — RPKI Relying Parties commonly perform top-down validation of the RPKI
   certificate tree after repository synchronization.  Existing
   repository synchronization mechanisms can update the local repository
   incrementally, avoiding a complete retrieval of all repository data.
   However, after such an incremental repository update, an RP
   implementation may still repeat full top-down validation over the
   local repository.  It means that the RP starts from the trust anchors
   and performs complete validation checks for all currently reachable
   RPKI objects encountered during the traversal.  Repeating such
   validation for objects whose validation inputs have not changed can
   introduce unnecessary validation overhead.

   This document specifies a publication-point-based incremental
   validation procedure for RPKI RPs.  The procedure is intended to
   reduce redundant validation work after incremental repository
   synchronization, while preserving the same validation result as a
   full top-down validation over the same repository snapshot, trust
   anchor set, validation policy, and validation time.  This document
   does not change the syntax or validation semantics of any RPKI
   object.
- **draft-sullivan-cfrg-raae-01** (new-draft, score 3, core_identity) [none]: [Random-Access Authenticated Encryption](https://datatracker.ietf.org/doc/draft-sullivan-cfrg-raae/) — This document defines random-access authenticated encryption (raAE),
   a primitive that partitions a message into an indexed sequence of
   segments that can be encrypted and decrypted independently and in any
   order.  It also specifies SEAL (Segmented Encryption and
   Authentication Layer), a parameterized construction that defines a
   family of concrete raAE instantiations, one for each valid choice of
   an Authenticated Encryption with Associated Data (AEAD) algorithm, a
   key derivation function (KDF), and associated parameters.

   SEAL provides two profiles, immutable (write-once) and mutable (in-
   place ciphertext rewrite), each with per-segment authentication.  A
   separately configured snapshot authenticator can additionally
   authenticate the complete, indexed segment set.

   The document also defines the security notions of raAE, specifies the
   requirements for conforming constructions, analyzes SEAL against
   those requirements, and provides example cipher suites and test
   vectors.
- **draft-sullivan-mls-attachments-00** (new-draft, score 3, core_identity) [none]: [Encrypted Attachments for MLS](https://datatracker.ietf.org/doc/draft-sullivan-mls-attachments/) — This document defines random-access authenticated encryption of large
   write-once files for Messaging Layer Security (MLS) groups.  A file
   is encrypted so that a receiver can decrypt and authenticate any byte
   range without processing the whole file.  The encryption is SEAL-
   attachment, SEAL's named write-once attachment scheme (raAE),
   parameterized by the AEAD and key derivation function of the group's
   MLS cipher suite and keyed from the MLS exporter.  The encrypted
   bytes are carried by any means, and a recipient needs only a small
   reference (the object's identifier and length, and an optional
   locator) to fetch, key, and verify the object.  MLS application
   messages cannot carry large files, and existing attachment encryption
   produces an opaque, immutable blob with no partial access.  This
   extension supplies the random-access layer those uses need.
- **draft-tantsura-fann-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Fast Network Notifications](https://datatracker.ietf.org/doc/draft-tantsura-fann-yang/) — This document defines a YANG data model to Fast Network Notifictions.
- **draft-tiloca-core-oscore-piv-enc-03** (new-draft, score 3, core_identity) [none]: [Stand-in Key Identifier and Encrypted Partial IV in the Constrained Application Protocol (CoAP) OSCORE Option](https://datatracker.ietf.org/doc/draft-tiloca-core-oscore-piv-enc/) — The security protocol Object Security for Constrained RESTful
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
- **draft-usama-tls-fatt-extension-09** (new-draft, score 3, adjacent_watchlist) [none]: [Proposed Document Template for TLS FATT Process](https://datatracker.ietf.org/doc/draft-usama-tls-fatt-extension/) — This document applies only to non-trivial extensions of TLS, which
   require formal analysis.  FATT process has successfully discovered
   CVEs of *CVSS 7.5* and most recently expected *CVSS 9.1* in the
   *production* implementations of the drafts proposed for adoption in
   the TLS WG.  To achieve high cryptographic assurances, this document
   proposes the drafts specify a clear threat model and informal
   security goals in the Security Considerations section, as well as
   motivation and a protocol diagram in the draft.
- **draft-vos-cfrg-pqpake-02** (new-draft, score 3, core_identity) [none]: [Hybrid Post-Quantum Password Authenticated Key Exchange](https://datatracker.ietf.org/doc/draft-vos-cfrg-pqpake/) — This document describes the CPaceOQUAKE+ protocol, a hybrid
   asymmetric password-authenticated key exchange (aPAKE) that supports
   mutual authentication in a client-server setting secure against
   quantum-capable attackers.  CPaceOQUAKE+ is composed of two stages —
   CPace and OQUAKE+ — that run sequentially, with the output of CPace
   feeding as the secret_context into OQUAKE+. OQUAKE+ is an augmented
   variant of OQUAKE that adds password confirmation.  This document
   also describes standalone OQUAKE+, a post-quantum aPAKE, and
   CPaceOQUAKE, the hybrid symmetric PAKE composed of the CPace and
   OQUAKE stages.  This document recommends configurations for
   CPaceOQUAKE+.
- **draft-wang-ipsecme-multi-auth-ikev2-pq-01** (new-draft, score 3, core_identity) [none]: [Multi-Authentication in IKEv2 with Post-quantum Security](https://datatracker.ietf.org/doc/draft-wang-ipsecme-multi-auth-ikev2-pq/) — Motivated to mitigate security threats against quantum computers,
   this draft specifies a general authentication mechanism in the
   Internet Key Exchange Protocol Version 2 (IKEv2) [RFC7296], called
   Multi-Authentication.  Namely, two peers can negotiate two or more
   authentication methods to authenticate each other.  The
   authentication methods selected do not necessarily belong to the same
   category.  This mechanism is achieved by adding a new value (17)
   (TBD) in the "IKEv2 Authentication Method" registry [IANA-IKEv2],
   maintained by IANA.  To run Multi-Authentication, two peers send the
   SUPPORTED_AUTH_METHODS Notify, defined in [RFC9593], to negotiate two
   or more authentication methods for authentication in IKEv2.

   [EDNOTE: Code points for Multi-Authentication may need to be assigned
   in the "IKEv2 Authentication Method" registry [IANA-IKEv2],
   maintained by IANA]
- **draft-westerlund-avtcore-srtp-gcm-sst-00** (new-draft, score 3, core_identity) [none]: [GCM-SST Authenticated Encryption in the Secure Real-time Transport Protocol (SRTP)](https://datatracker.ietf.org/doc/draft-westerlund-avtcore-srtp-gcm-sst/) — This document defines how the GCM-SST (Galois Counter Mode with
   Strong Secure Tags) Authenticated Encryption with Associated Data
   (AEAD) algorithm family can be used to provide confidentiality and
   data authentication in the Secure Real-time Transport Protocol
   (SRTP).  GCM-SST addresses known weaknesses in AES-GCM for short
   authentication tags, making it well suited for media encryption use
   cases where low overhead is critical.
- **draft-westerlund-tls-gcm-sst-00** (new-draft, score 3, core_identity) [none]: [Use of Galois Counter Mode with Strong Secure Tags (GCM-SST) in TLS, DTLS and QUIC](https://datatracker.ietf.org/doc/draft-westerlund-tls-gcm-sst/) — This document defines cipher suites based on AES-GCM-SST and
   Rijndael-GCM-SST (Galois Counter Mode with Strong Secure Tags) for
   use in TLS 1.3, DTLS 1.3, and QUIC.  GCM-SST provides authenticated
   encryption with near-ideal forgery probabilities for short
   authentication tags, making it suitable for bandwidth-constrained
   environments where reduced per-packet overhead is important.  This
   document specifies cipher suites with 96-bit and 112-bit
   authentication tags.
- **draft-wullink-rpp-oauth2-00** (new-draft, score 3, authorization) [none]: [OAuth 2.0 for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-oauth2/) — This document describes how OAuth 2.0 [RFC6749] can be used to secure
   RESTful Provisioning Protocol (RPP) API requests described in
   [I-D.ietf-rpp-core].
- **draft-yang-dhc-dhcp-extension-00** (new-draft, score 3, adjacent_watchlist) [none]: [DHCP New Option Extension based on LLM Capability](https://datatracker.ietf.org/doc/draft-yang-dhc-dhcp-extension/) — This document specifies a DHCP option extension designed for campus
   networks to help client devices distinguish and connect to a master
   device with the LLM (Large Language Model).  The mechanism extends a
   new DHCP option containing two specific parameters within the DHCP
   payload: the master device's LLM address and the master device's LLM
   configuration.  This allows client devices to identify and register
   to LLM-enabled master device during the bootstrap phase.
- **draft-ybb-ccamp-service-path-computation-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Service Path Computation](https://datatracker.ietf.org/doc/draft-ybb-ccamp-service-path-computation/) — This document defines a YANG data model for client signal service's
   path computation and path management.
- **draft-yl-cats-data-model-07** (new-draft, score 3, adjacent_watchlist) [none]: [Data Model for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-yl-cats-data-model/) — This document defines a YANG data model for the management of
   Computing-Aware Traffic Steering (CATS) systems.

   The YANG module defined in this document conforms to the Network
   Management Datastore Architecture (NMDA).
- **draft-yoon-ccamp-pm-streaming-07** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Performance Monitoring Streaming on Common Transport Equipment](https://datatracker.ietf.org/doc/draft-yoon-ccamp-pm-streaming/) — This document describes how the generic collection measurement YANG
   data model and its interval-capability companion model are applied to
   common transport equipment.  It is informational.  It defines a small
   YANG module of transport performance parameters, organizes those
   parameters into maintenance and QoS profiles, and gives end-to-end
   examples that show capability discovery followed by YANG-Push
   subscription, notification, and threshold reporting for a transport
   profile.
- **draft-yoon-ippm-collection-interval-capabilities-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Collection Interval Capabilities](https://datatracker.ietf.org/doc/draft-yoon-ippm-collection-interval-capabilities/) — This document defines a YANG data model, "ietf-pm-interval-
   capabilities", that enables a server to advertise which collection
   intervals it can support.  A client reads this capability information
   before configuring performance measurements, so that it selects only
   sampling and collection intervals that the server can honour.  The
   capabilities are advertised by augmenting the "ietf-system-
   capabilities" module defined in [RFC9196], so that a client discovers
   them at the same well-known location used for subscription and
   notification capabilities.  The model imports the "profile-names"
   type from the companion collection measurement model defined in
   [I-D.yoon-ippm-collection-measure] and mirrors its profile-and-
   parameter structure, ensuring direct alignment between capability
   discovery and measurement configuration.  The model does not define
   measurement data structures or any delivery mechanism; those are
   defined in the companion document.
- **draft-yoon-ippm-collection-measure-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Collection Measurement](https://datatracker.ietf.org/doc/draft-yoon-ippm-collection-measure/) — This document specifies a YANG data model for Collection Measurement
   based on the Performance Management (PM) Collection function
   requirements defined in ITU-T G.7710.  The model processes raw
   performance data sampled at a network node and produces structured
   data that can be retrieved by clients via pull-based mechanisms or
   delivered via push-based mechanisms such as YANG-Push.  This document
   does not define new performance metrics; the base metrics are those
   of the IPPM framework, and the model specifies the collection and
   exposure of the operationally important subset identified by ITU-T
   G.7710.
- **draft-yu-ccamp-resource-pm-yang-06** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Resource Performance Monitoring](https://datatracker.ietf.org/doc/draft-yu-ccamp-resource-pm-yang/) — This document defines a YANG data model for resource Performance
   Monitoring, applicable to network controllers, which provides the
   functionalities of retrieval of performance monitoring capabilities,
   TCA (Threshold Crossing Alert) configuration, current or history
   performance data retrieval, and performance monitoring task
   management.
- **draft-zhang-sidrops-aspa-egress-05** (new-draft, score 3, authorization) [none]: [ASPA-based AS_PATH Verification for BGP Export](https://datatracker.ietf.org/doc/draft-zhang-sidrops-aspa-egress/) — This document describes AS_PATH verification based on Autonomous
   System Provider Authorization (ASPA) for egress eBGP speakers.  ASPA
   is a Resource Public Key Infrastructure (RPKI) object that allows an
   AS to register its transit provider ASes.  Performing ASPA-based
   AS_PATH verification at egress can prevent inadvertent propagation of
   route leaks to external peers, check for local misconfigurations, and
   help detect potential ASPA registration errors.  This approach
   complements ingress-side verification and BGP Roles/Only to Customer
   (OTC); it also provides operational assurance for partial deployment
   and for export-side configuration or registration problems.
- **draft-beeram-spring-rsvp-srv6-00** (new-draft, score 2, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SRv6 Forwarding Plane Using End.X Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-spring-rsvp-srv6/) — RFC 8577 defines mechanisms to signal RSVP-TE tunnels on a shared
   MPLS forwarding plane by introducing the notion of per-TE link labels
   that are functionally equivalent to SR-MPLS adjacency segments.  This
   document extends that work to the SRv6 data plane, defining the
   signaling extensions and procedures necessary to establish RSVP-TE
   tunnels that utilize SRv6 Segment Identifiers (SIDs) for forwarding.

   This document specifies how SRv6 End.X SIDs serve as TE link SIDs,
   defines new RSVP signaling extensions for carrying SRv6 SIDs,
   describes TE path segment-list construction procedures at the
   ingress, and adapts the delegation mechanisms of RFC 8577 to use SRv6
   Binding SIDs.  The result couples the traffic engineering
   capabilities of the RSVP-TE control plane with the native IPv6
   forwarding of SRv6.
- **draft-calabria-bmwg-ai-fabric-inference-bench-03** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
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
- **draft-calabria-bmwg-ai-fabric-terminology-03** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bmwg-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
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
- **draft-eckert-anima-ai4an-01** (new-draft, score 2, ignored_after_review) [none]: [AI for Autonomous Networking](https://datatracker.ietf.org/doc/draft-eckert-anima-ai4an/) — This document builds on the architectural foundation of the IETF
   ANIMA "Autonomous Network Infrastructure" to propose an architecture
   for in-network intelligence in support of network automation.

   The key aspect of this architecture is the use of AI programmed and
   validated software running decentralized on the network.
- **draft-gray-lamps-composite-fndsa-lms-00** (new-draft, score 2, ignored_after_review) [none]: [Composite FN-DSA and LMS Digital Signature Algorithm for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-gray-lamps-composite-fndsa-lms/) — This document defines a composite signature scheme combining the FN-
   DSA (Falcon) digital signature algorithm with the Leighton-Micali
   Signature (LMS) scheme defined in RFC 8554.  This construction is
   designed for use within X.509 Public Key Infrastructure (PKI) and
   follows the composite signature paradigm defined in
   [I-D.ietf-lamps-pq-composite-sigs].
- **draft-hu-6man-ipv6-flowlabel-load-balancing-rdma-01** (new-draft, score 2, ignored_after_review) [none]: [A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) — This document proposes a method for achieving flow-level load
   balancing in RoCEv2 (RDMA over Converged Ethernet version 2)
   networks.  Traditional per-flow load balancing based on the 5-tuple
   cannot distinguish between different RDMA sessions that share the
   same 5-tuple.  This causes "elephant flows" to be hashed to the same
   path, leading to network congestion.  This method resolves this issue
   by parsing the QP (Queue Pair) information from the IB BTH (Base
   Transport Header) and IB DETH (Datagram Extended Transport Header)
   headers of the RoCEv2 packet.  By combining this with portions of the
   IPv6 source and destination addresses as an entropy source, a CRC32
   hash algorithm generates a 20-bit value, which is then written into
   the Flow Label field of the IPv6 header.  Network devices can
   subsequently use the updated "5-tuple + Flow Label" for more granular
   flow-level load balancing, thereby effectively improving transmission
   efficiency in high-performance networks such as AI computing.
- **draft-ietf-dnsop-delext-08** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFC 6895.
- **draft-ietf-dnsop-ns-revalidation-13** (new-draft, score 2, ignored_after_review) [dnsop]: [Delegation Revalidation by DNS Resolvers](https://datatracker.ietf.org/doc/draft-ietf-dnsop-ns-revalidation/) — This document describes an optional algorithm for the processing of
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
- **draft-ietf-nmop-network-anomaly-semantics-06** (new-draft, score 2, ignored_after_review) [nmop]: [Semantic Metadata Annotation for Network Anomaly Detection](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-anomaly-semantics/) — The document proposes a unified symptoms vocabulary for network
   anomaly metadata to improve data sharing and analysis among human
   network operators, network analytics implementers, and AI systems to
   improve accuracy of Service Disruption Detection.
- **draft-irtf-nmrg-ai-deploy-03** (new-draft, score 2, ignored_after_review) [nmrg]: [Considerations of network/system for AI services](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ai-deploy/) — As the development of AI technology has matured and AI technology has
   begun to be applied in various fields, the execution environment has
   evolved from dedicated high-performance servers to commodity servers
   and affordable, small-scale hardware, including microcontrollers,
   low-performance CPUs, and AI chipsets.  This document outlines how to
   configure the network and system for an AI inference service,
   providing AI services in a distributed manner.  It also outlines the
   factors to consider when a client connects to a cloud server and an
   edge device to request an AI service.  It describes some use cases
   for deploying network-based AI services, such as self-driving
   vehicles and network digital twins.
- **draft-kompella-lsr-mptecap-02** (new-draft, score 2, ignored_after_review) [none]: [Multipath Traffic Engineering Capabilities](https://datatracker.ietf.org/doc/draft-kompella-lsr-mptecap/) — Multipath Traffic Engineering (MPTE) combines two approaches to
   traffic management: equal-cost multipath and constraint-based traffic
   engineering, offering a powerful new way to engineer networks.  To
   avail of this, a node (possibly an ingress of a MPTE tunnel, or a
   path computation agent) must have information about the topology,
   link and node characteristics of a network so that it can compute the
   components of the MPTE tunnel.  One important (node) characteristic
   is whether a given node supports MPTE, i.e., whether it can
   participate in the provisioning and maintenance of an MPTE tunnel.

   Multicast TE (MCTE) offers a more efficient approach to traffic
   engineering for multicast traffic.  Again, an important node
   characteristic is whether a given node supports MCTE, i.e., whether
   it can participate in the provisioning and maintenance of an MCTE
   tunnel.

   This memo shows how these capabilities can be distributed in the IGP
   via Link State Routing TE Capabilities.
- **draft-li-uboe-00** (new-draft, score 2, ignored_after_review) [none]: [UnifiedBus over Ethernet (UBoE)](https://datatracker.ietf.org/doc/draft-li-uboe/) — This document specifies the UnifiedBus over Ethernet (UBoE) protocol,
   which enables seamless interconnection between native UnifiedBus (UB)
   domains and standard Ethernet/IP network for AI and HPC high-
   performance scenarios.  It defines the UBoE packet encapsulation
   based on IPv4/IPv6 and UDP over Ethernet, including the invariant CRC
   (ICRC) integrity protection for end-to-end packet verification.  This
   document further specifies the cross-domain packet conversion and
   header adaptation behaviors at UB2E switches, including bidirectional
   mapping rules for UB-specific network layer and IP network layer.
- **draft-liu-opsawg-stbl-req-per-packet-00** (new-draft, score 2, ignored_after_review) [none]: [Ability Requirements for Stability Guarantees in Per-packet Load Balancing Networks](https://datatracker.ietf.org/doc/draft-liu-opsawg-stbl-req-per-packet/) — Many per-packet load balancing mechanisms have been proposed to
   optimize the performance of AI networks.  However, per-packet load
   balancing poses significant challenges to network stability
   assurance.  This draft analyzes these challenges, as well as the
   ability requirements for stability guarantees in per-packet load
   balancing networks.
- **draft-mennell-art-fmsg-structured-messaging-01** (new-draft, score 2, ignored_after_review) [none]: [fmsg: Structured Host-to-Host Messaging with Verifiable Threads](https://datatracker.ietf.org/doc/draft-mennell-art-fmsg-structured-messaging/) — fmsg is a message exchange protocol between domain defined hosts.
   Messages are binary encoded and form threads which require
   participation to reply to.

   This document describes the motivation and architecture of fmsg, an
   existing protocol specification and implementation are referenced,
   but the full specification is not included here.  The purpose of this
   document is to solicit IETF feedback on venue and scope before/if the
   specification can develop into standards-track documents.
- **draft-morrison-live-reference-resolution-00** (new-draft, score 2, ignored_after_review) [none]: [Live Reference Resolution for Autonomous Agent Beliefs](https://datatracker.ietf.org/doc/draft-morrison-live-reference-resolution/) — A recurring class of autonomous-agent failure arises when an agent
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
- **draft-mp-agntcy-ads-02** (new-draft, score 2, agent_identity) [none]: [Agent Directory Service](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/) — The Agent Directory Service (ADS) is a distributed directory service
   designed to store metadata for AI agent applications.  This metadata,
   stored as directory records, enables the discovery of agent
   applications with specific skills for solving various problems.  The
   implementation features distributed directories that interconnect
   through a content-routing protocol.
- **draft-song-rtgwg-din-usecases-requirements-02** (new-draft, score 2, ignored_after_review) [none]: [Distributed Inference Network (DIN) Problem Statement, Use Cases, and Requirements](https://datatracker.ietf.org/doc/draft-song-rtgwg-din-usecases-requirements/) — This document describes the problem statement, use cases, and
   requirements for a "Distributed Inference Network" (DIN) in the era
   of pervasive AI.  As AI inference services become widely deployed and
   accessed by billions of users, applications and devices, traditional
   centralized cloud-based inference architectures face challenges in
   scalability, latency, security, and efficiency.  DIN aims to address
   these challenges by leveraging distributed edge-cloud collaboration,
   intelligent scheduling, and enhanced network security to support low-
   latency, high-concurrency, and secure AI inference services.
- **draft-wnd-opsawg-icon-ps-00** (new-draft, score 2, ignored_after_review) [none]: [Problem Statement for Observability, Intervention and Control (I&C) in Multi-Agent Autonomous Networks](https://datatracker.ietf.org/doc/draft-wnd-opsawg-icon-ps/) — This document provides an overview of the issues associated with the
   deployment of the observability, intervention, and control of
   autonomous agent pipelines in large-scale heterogeneous network
   environments.  The term "Intervention and Control" is used to
   describe a set of automated and human-initiated mechanisms that
   guarantee the capability to observe, constrain, correct, and
   terminate Autonomous agents at any point, for any reason,
   irrespective of their level of autonomy under which it operates, to
   ensure resilience, recovery, and operational continuity.

   The set of enabled observability, intervention and control reflects
   operator service offerings to ensure that autonomous operations can
   be stopped, or safely redirected when required and is designed in
   conjunction with agent to agent, agent to tools, agent to human
   interaction and service and network policy.

   This document also identifies several key areas that the Agent
   Observability, Intervention and Control group will investigate to
   guide its architectural and protocol work and associated documents.
- **draft-yan-nmrg-cross-domain-agent-architecture-00** (new-draft, score 2, ignored_after_review) [none]: [Cross-Domain Network Agent Architecture for Autonomous Operations](https://datatracker.ietf.org/doc/draft-yan-nmrg-cross-domain-agent-architecture/) — Autonomous network management using agents is maturing in single-
   domain deployments.  However, end-to-end services spanning multiple
   domains expose a lack of systematic support for cross-domain
   coordination, roles, and interfaces in current architectures.  This
   document defines a cross-domain network agent architecture that
   enables coordinated operation across autonomous domains through
   standardized agent roles, layered coordination mechanisms, and
   unified interface specifications.
- **draft-yao-dawn-agent-discovery-architect-00** (new-draft, score 2, ignored_after_review) [none]: [DNS-like Agent Discovery Architecture](https://datatracker.ietf.org/doc/draft-yao-dawn-agent-discovery-architect/) — This document defines a DNS-like three-tier agent-discovery
   architecture for the Internet of Agents (IoA).  It introduces three
   core functional roles: Agent Root, Agent Registry, and Agent
   Resolver.
- **draft-zhuang-ippm-network-measurement-ps-00** (new-draft, score 2, ai_infrastructure) [none]: [Network Measurement Problem Statement](https://datatracker.ietf.org/doc/draft-zhuang-ippm-network-measurement-ps/) — Modern network applications, ranging from artificial intelligence
   (AI) and machine learning (ML) training to large-scale cloud
   services, require adaptive and high-performance networks.  Network
   measurement is fundamental to achieving observability, enabling
   traffic engineering (TE), load balancing, congestion control (CC),
   resource accounting, and fault diagnosis.  However, existing network
   measurement techniques face significant challenges in accuracy,
   overhead, scalability, and adaptability, especially in distributed
   and high-speed environments.  This document describes the problems
   and gaps in current network measurement approaches, including sketch-
   based measurement, in-band network telemetry (INT), sampling, and
   probing, with a focus on distributed system scenarios.

## Ignored after review

- **draft-admnr-lsr-igp-measurement-group-02** (new-draft, score 0, ignored_after_review) [none]: [Advertising IGP Measurement Group using TLV](https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/) — This document defines an IS-IS capability sub-TLV for advertising
   measurement group membership for Active Measurement Protocols (AMPs)
   such as TWAMP and STAMP.  The mechanism allows IGP routers to
   discover other routers participating in different measurement groups,
   enabling automatic discovery of measurement endpoints across IGP
   areas.  The solution uses interface addresses (IPv4 or IPv6) to
   identify measurement group membership, where the same interface
   address may be used for multiple measurement groups.
- **draft-ageneau-ccwg-ndtc-02** (new-draft, score 0, ignored_after_review) [none]: [Network Delivery Time Control](https://datatracker.ietf.org/doc/draft-ageneau-ccwg-ndtc/) — This document describes Network Delivery Time Control (NDTC), a rate
   adaptation algorithm for real-time video streaming suited for
   interactive applications like cloud gaming.  NDTC leverages the Frame
   Dithering Available Capacity Estimation (FDACE) heuristic, which
   estimates available path capacity without inducing congestion.  The
   algorithm dynamically adjusts frame sizes and transmission times to
   ensure timely delivery, while also responding to conventional
   congestion signals.
- **draft-ajp-spring-srv6-mpte-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6 for Multipath Traffic Engineering](https://datatracker.ietf.org/doc/draft-ajp-spring-srv6-mpte/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that enables weighted load
   balancing of unicast traffic across a constrained set of paths
   optimized for an objective.

   This document is informational and describes one realization approach
   for applying SRv6 semantics to MPTE, based on the Multipath Traffic
   Engineering Internet-Draft (draft-kompella-teas-mpte).  It
   summarizes associated procedures, lifecycle, management, and
   forwarding behavior.

   This document applies existing SRv6 architecture and semantics to
   MPTE without defining new SRv6 endpoint behaviors or signaling
   protocols.  It focuses on data-plane realization using existing
   forwarding instructions.
- **draft-ali-6man-srv6-vpn-icmp-error-handling-04** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling in SRv6 based VPN Networks](https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/) — The document specifies procedures for handling ICMP error in
   SRv6-based Virtual Private Network (VPN).
- **draft-ali-opsawg-yang-protobuf-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement: YANG Modeling for Protocol Buffer Based Network APIs](https://datatracker.ietf.org/doc/draft-ali-opsawg-yang-protobuf-problem-statement/) — Network devices increasingly expose management, telemetry, and
   dynamic service interfaces using gRPC and Protocol Buffers.  Many of
   these interfaces carry ephemeral or runtime state that is not
   intended to be stored as persistent configuration.  At the same time,
   the IETF has standardized YANG as the primary data modeling language
   for network management and operations.  This document describes the
   problem space and identifies questions for the IETF community
   regarding the role of YANG in defining interoperable Protocol Buffer
   based APIs.
- **draft-ali-pce-implicit-tls-profile-00** (new-draft, score 0, ignored_after_review) [none]: [A Policy-Driven Implicit TLS Transport Profile for PCEP](https://datatracker.ietf.org/doc/draft-ali-pce-implicit-tls-profile/) — RFC 8253 specifies the use of Transport Layer Security (TLS) for the
   Path Computation Element Communication Protocol (PCEP) by negotiating
   TLS using the PCEP StartTLS message exchange.  This document
   specifies a deployment profile for PCEP in which TLS is initiated
   immediately following TCP connection establishment based on local
   policy.

   This document is intended to simplify deployments where secure
   transport is mandatory.
- **draft-autocrypt-openpgp-v2-cert-03** (new-draft, score 0, ignored_after_review) [none]: [Autocrypt v2 OpenPGP Certificates and Transferable Secret Keys](https://datatracker.ietf.org/doc/draft-autocrypt-openpgp-v2-cert/) — This document describes the "Autocrypt v2 Certificate", a standard
   structure for an OpenPGP certificate for Internet messaging.  It
   offers defense against store-now-decrypt-later attacks from quantum
   computers through post-quantum hybrid cryptography.  It also enables
   reliable deletion ("Forward Secrecy") of received messages even when
   adversaries capture encrypted messages in transit and later
   compromise the user's message archive and secret keys.  The design
   uses deterministically ratcheted rotating encryption subkeys with
   predictable expiration combined with coordinated secret key material
   destruction.  This document also describes the structure, use, and
   maintenance of the OpenPGP Transferable Secret Key that corresponds
   with the Autocrypt v2 Certificate.
- **draft-becker-cnsa2-smime-profile-03** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Secure/Multipurpose Internet Mail Extensions (S/MIME)](https://datatracker.ietf.org/doc/draft-becker-cnsa2-smime-profile/) — This document defines a base profile of S/MIME for use with the US
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
- **draft-becker-cnsa2-ssh-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
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
- **draft-becker-cnsa2-tls-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for TLS 1.3](https://datatracker.ietf.org/doc/draft-becker-cnsa2-tls-profile/) — This document defines a base profile of TLS 1.3 which is compliant
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
- **draft-beeram-spring-rsvp-sr-mpls-00** (new-draft, score 0, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SR-MPLS Forwarding Plane Using Adjacency Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-spring-rsvp-sr-mpls/) — RFC 8577 introduced the concept of signaling RSVP-TE tunnels on a
   shared MPLS forwarding plane using preinstalled "TE link labels".
   Those labels are functionally equivalent to Segment Routing (SR)
   Adjacency Segment Identifiers (Adj-SIDs) but are allocated and
   distributed solely via RSVP-TE signaling.

   This document extends RFC 8577 to use SR-MPLS Adjacency SIDs that are
   advertised by the IGP as the forwarding-plane labels for RSVP-TE
   tunnels.  It restricts scope to per-link Adj-SIDs and defines the
   signaling procedures and protocol extensions required to couple the
   RSVP-TE control plane with the native SR-MPLS forwarding plane.
- **draft-bg-onions-update-network-service-models-01** (new-draft, score 0, ignored_after_review) [none]: [An Update of Service and Network YANG Data Models](https://datatracker.ietf.org/doc/draft-bg-onions-update-network-service-models/) — Service & Network data models have been implemented in recent years
   to facilitate the deployment of connectivity services such as Layer 2
   and Layer 3 VPN services in provider networks.  This document reports
   the findings from the implementations, including missing
   functionalities, configuration blocks aligment against recent network
   models published, operational issues/limitatations and enhancements.
- **draft-birrane-dtn-rel-02** (new-draft, score 0, ignored_after_review) [none]: [Reliability Considerations for Delay-Tolerant Networks](https://datatracker.ietf.org/doc/draft-birrane-dtn-rel/) — The Delay-Tolerant Networking (DTN) architecture describes a type of
   challenged network in which communications may be significantly
   affected by long signal propagation delays, frequent link
   disruptions, or both.  These unique and challenging characteristics
   require adapted approaches for data transport, security, management,
   routing, and other networking functions.  Using new approaches, DTNs
   can offer data services in environments that would be considered
   neither reliable nor resilient as these concepts are understood for
   unchallenged networks.

   This document identifies adapted definitions and concepts for DTN
   reliability and resiliency that can be applied even when there is no
   simultaneous, reliable, end-to-end path between sources and
   destinations in the network.  These definitions and concepts are
   suitable for any challenged environment but, in particular, those
   communicating using the DTN Bundle Protocol (BP).  The ability to
   overlay BP across multiple discontinuous underlay networks, to store-
   and-forward data where and as necessary, and the structure and
   security of the BPv7 bundle itself provide novel ways to identify,
   implement, signal, and otherwise consider guarantees associated with
   data exchange in the DTN environment.
- **draft-bruynooghe-n0-quic-nat-traversal-00** (new-draft, score 0, ignored_after_review) [none]: [n0 QUIC NAT Traversal](https://datatracker.ietf.org/doc/draft-bruynooghe-n0-quic-nat-traversal/) — A description of how noq (https://github.com/n0-computer/noq)
   performs NAT traversal for iroh (https://github.com/n0-computer/
   iroh), including all current bugs.  This is not yet a specification,
   though further revisions migth be.
- **draft-busi-nmop-transport-simap-02** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Service & Infrastructure Maps (SIMAP) to Transport Networks](https://datatracker.ietf.org/doc/draft-busi-nmop-transport-simap/) — This document explores the applicability of the Service &
   Infrastructure Maps (SIMAP) concepts to transport networks and it
   examines the YANG data models defined by the IETF to support the
   requirements and use cases for SIMAP applicability to transport
   networks.
- **draft-campling-ech-deployment-considerations-12** (new-draft, score 0, ignored_after_review) [none]: [Encrypted Client Hello Deployment Considerations](https://datatracker.ietf.org/doc/draft-campling-ech-deployment-considerations/) — This document discusses operational and policy considerations
   related to the deployment of TLS Encrypted Client Hello (ECH). It
   describes the impact of encrypting the TLS Server Name Indication
   (SNI) on operational practices such as threat detection, network
   security controls, and content filtering in private, edge, and
   public network environments, with a particular focus on education,
   enterprise, and public operator use cases.
- **draft-cardona-claise-netmod-yang-coverage-00** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for YANG Example Validation and Coverage Analysis in IETF Documents](https://datatracker.ietf.org/doc/draft-cardona-claise-netmod-yang-coverage/) — This document defines guidelines for including YANG example instances
   in IETF documents in a way that enables automatic extraction and
   validation.  It introduces the concept of YANG module "coverage" to
   measure how thoroughly example instances exercise a YANG module's
   data nodes.  By standardizing how YANG examples are included,
   validated, and measured for coverage, these guidelines help authors
   catch errors before publication and give reviewers and implementers
   greater confidence that the examples in a specification are correct
   and cover a sufficient range of scenarios - ultimately making the
   underlying data models easier to implement and use.
- **draft-chen-green-ran-transport-coord-energy-saving-00** (new-draft, score 0, ignored_after_review) [none]: [Coordinated Energy Saving between RAN and Transport Network](https://datatracker.ietf.org/doc/draft-chen-green-ran-transport-coord-energy-saving/) — This document provides an coordinated energy saving mechanism between
   RAN and transport network.
- **draft-chen-green-transport-energy-saving-01** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Energy Saving Mechanism for Transport Network](https://datatracker.ietf.org/doc/draft-chen-green-transport-energy-saving/) — This document continues the transport network energy saving that
   harmonizes device-level autonomy with network-wide coordination.  By
   implementing control at hybrid both the device and network controller
   coordination, it enables dynamic, SLA-aware, and multi-layer energy
   optimization.
- **draft-chen-rdma-windowless-ack-00** (new-draft, score 0, ignored_after_review) [none]: [Windowless Cumulative ACK Extension for RDMA Retransmission](https://datatracker.ietf.org/doc/draft-chen-rdma-windowless-ack/) — Traditional RDMA Reliable Connection (RC) uses selective
   retransmission, while TCP SACK depends on sliding window and RTO
   timer tuning.  Both mechanisms waste network bandwidth when window or
   RTO parameters mismatch real network conditions.  This document
   defines a windowless cumulative selective acknowledgement extension
   (T/C AETH) embedded within the RDMA ETH header, paired with dual-
   trigger ACK reporting logic driven by cumulative receive time
   threshold and cumulative received packet count threshold.

   The receiver generates extended SACK reports without sliding window
   constraints.  The sender accurately identifies lost PSN segments
   through multi-segment confirmation fields carried in T/C AETH, then
   only retransmits missing packets.  This design removes window
   dependency, eliminates redundant retransmissions, and improves
   bandwidth utilization and end-to-end throughput for high-speed RDMA
   workloads in data centers and wide-area networks.
- **draft-cheshire-sbm-04** (new-draft, score 0, ignored_after_review) [none]: [Source Buffer Management](https://datatracker.ietf.org/doc/draft-cheshire-sbm/) — In the past decade there has been growing awareness about the harmful
   effects of bufferbloat in the network, and there has been good work
   on developments like L4S to address that problem.  However,
   bufferbloat on the sender itself remains a significant additional
   problem, which has not received similar attention.  This document
   offers techniques and guidance for host networking software to avoid
   network traffic suffering unnecessary delays caused by excessive
   buffering at the sender.  These improvements are broadly applicable
   across all datagram and transport protocols (UDP, TCP, QUIC, etc.) on
   all operating systems.
- **draft-claise-opsawg-ipfix-ordered-ie-01** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
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
- **draft-contreras-detnet-preof-oam-00** (new-draft, score 0, ignored_after_review) [none]: [PREOF Observability and OAM Requirements](https://datatracker.ietf.org/doc/draft-contreras-detnet-preof-oam/) — Packet Replication, Elimination, and Ordering Functions (PREOF)
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
   underlying DetNet data plane technology.
- **draft-contreras-pce-pam-07** (new-draft, score 0, ignored_after_review) [none]: [Path Computation Based on Precision Availability Metrics](https://datatracker.ietf.org/doc/draft-contreras-pce-pam/) — This document extends PCEP to support Precision Availability Metrics
   (PAM) [RFC9544] for path computation.  The optimization objectives
   for PAM computations are encoded using the Objective Function (OF)
   object defined in [RFC5541], allowing PCCs to specify precise
   optimization criteria for services with SLO requirements.  And a PCE
   can report the statistical characterization associated with a
   computed path.
- **draft-contreras-pim-eco-mode-01** (new-draft, score 0, ignored_after_review) [none]: [IGMP / MLD Extension for Signaling Eco-Mode](https://datatracker.ietf.org/doc/draft-contreras-pim-eco-mode/) — This document specifies an extension to IGMPv3 and MLDv2 messages to
   indicate eco-mode preferences in the delivery of multicast content
   based on the mechanism described in [RFC9279].  The extension enables
   receivers and network elements to signal energy-aware multicast
   delivery preferences, including different eco-mode levels, so that
   multicast services can be operated consistently with energy-efficient
   network management, service-level optimisation, and telemetry-driven
   assessment of energy and carbon impact.
- **draft-corneo-schc-ctx-mgmt-00** (new-draft, score 0, ignored_after_review) [none]: [SCHC Context Management Extensions](https://datatracker.ietf.org/doc/draft-corneo-schc-ctx-mgmt/) — This document defines extensions to the Static Context Header
   Compression (SCHC) framework that improve context management
   efficiency.  Two categories of mechanisms are introduced: rule
   referencing CDAs (ref and ref-edit) that enable composable rule
   definitions and reduce context storage, and a rule fragment branching
   CDA (branch) with associated Matching Operators that enable dynamic
   multi-layer protocol compression without combinatorial rule
   explosion.
- **draft-czz-rtgwg-elastic-bandwidth-routing-00** (new-draft, score 0, ignored_after_review) [none]: [Elastic Bandwidth-aware Routing Framework](https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/) — IGP normally computes the shortest paths in a network for packet
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
   alternate paths through Segment Routing Traffic Engineering (SR-TE),
   with weights determined based on the bandwidth utilization and
   available bandwidth of these paths.  It provides an efficient,
   accurate and backward compatible approach for dynamic link congestion
   avoidance.
- **draft-deschepper-tsvwg-srm-00** (new-draft, score 0, ignored_after_review) [none]: [Static Rate Management (SRM) for Low Latency, Low Loss, and Scalable Throughput (L4S)](https://datatracker.ietf.org/doc/draft-deschepper-tsvwg-srm/) — This document describes the Static Rate Management (SRM) solution for
   L4S (Low Latency, Low Loss, Scalable Throughput) rate control.  SRM
   utilizes a Two-Rate, Three-Color Marker (trTCM) policer in
   conjunction with a dual-queue mechanism to provide low latency and
   low loss for L4S flows in environments where a fixed, safe rate can
   be reliably defined for a network link or segment.  This approach
   offers an alternative to Active Queue Management (AQM)-based L4S
   solutions, particularly for high-speed and aggregated networks with
   limited packet processing capabilities.  This document details the
   operation, advantages, disadvantages, and configuration guidelines
   for SRM.
- **draft-deshmukh-mpls-frr-ext-02** (new-draft, score 0, ignored_after_review) [none]: [Signaling Optimization Objective and Bounded Metrics for MPLS Fast Reroute Backup LSP Tunnels](https://datatracker.ietf.org/doc/draft-deshmukh-mpls-frr-ext/) — This document introduces RSVP-TE signaling procedures that enable the
   head-end Label Switched Router (LSR) of a local-protection-desiring
   Label Switched Path (LSP) to influence the optimization objective and
   bounded metric constraints used for the path computation of a backup
   LSP tunnel at a Point of Local Repair (PLR).
- **draft-devevey-cfrg-silithium-00** (new-draft, score 0, ignored_after_review) [none]: [Silithium - A Compact, Efficient and Non-separable Hybrid Signature](https://datatracker.ietf.org/doc/draft-devevey-cfrg-silithium/) — This document defines Silithium, an augmentation of US NIST Module-
   Lattice-based Digital Signing Algorithm (ML-DSA) [FIPS.204] with
   traditional elliptic-curve operations, that uses ML-DSA in a black-
   box manner.  This results in a digital signature scheme with hybrid
   security, requiring solving hard lattice problems as well as discrete
   logarithm in order to forge a signature.  This augmentation is
   designed to satisfy regulatory guidelines in certain regions.
   Silithium is strongly unforgeable as long as ML-DSA is.  Morevoer,
   Silithium can be used in a backward compatible and interopable manner
   without hindering security.
- **draft-dnsop-rfc6303-bis-03** (new-draft, score 0, ignored_after_review) [none]: [Updates to Locally Served DNS Zones and IP Special-Purpose Address Space Registries](https://datatracker.ietf.org/doc/draft-dnsop-rfc6303-bis/) — RFC 6063, "Locally Served DNS Zones", defines two IANA registries
   called "IPv4 Locally-Served DNS Zone" and "IPv6 Locally-Served DNS
   Zone" registries.  This document changes the registration policy for
   that registry from "IETF Review" to "Expert Review".

   Also, this document updates IP Special-Purpose Address Space
   registries to indicate whether an IP address block is eligible to be
   in Locally-Served DNS Zones.  Eligible entries will be automatically
   added to the Locally-Served DNS Zones.

   This document updates RFC 6063 and RFC 6890.
- **draft-dong-lsvr-bgp-spf-selection-04** (new-draft, score 0, ignored_after_review) [none]: [Proposed Update to BGP Link-State SPF NLRI Selection Rules](https://datatracker.ietf.org/doc/draft-dong-lsvr-bgp-spf-selection/) — For network scenarios such as Massively Scaled Data Centers (MSDCs),
   BGP is extended for Link-State (LS) distribution and the Shortest
   Path First (SPF) algorithm based calculation.  BGP-LS-SPF leverages
   the mechanisms of both BGP protocol and BGP-LS protocol extensions,
   with new selection rules defined for BGP-LS-SPF NLRI.  This document
   proposes some updates to the BGP-LS-SPF NLRI selection rules, so as
   to improve the route updates and convergence, while consistent SPF
   computation result can still be achieved.  This document updates the
   NLRI selection rules in I-D.ietf-lsvr-bgp-spf.
- **draft-eastlake-manet-babel-wi-fi-00** (new-draft, score 0, ignored_after_review) [none]: [Babel for Wi-Fi (IEEE Std 802.11) Mesh](https://datatracker.ietf.org/doc/draft-eastlake-manet-babel-wi-fi/) — The BABEL routing protocol (RFC 8966) is well applicable (RFC 8967)
   to networks with unstable link metrics such as wireless networks.
   Wi-Fi (IEEE Std 802.11-2024) is an example of such a network and the
   Wi-Fi standard includes a mesh feature which was specified to be
   configurable for different routing protocols and link metrics.  This
   document specifies how, in Wi-Fi mesh, to use BABEL and/or the delay
   based link metric specified in RFC 9616.
- **draft-einarsson-moq-locmaf-01** (new-draft, score 0, ignored_after_review) [none]: [Low Overhead CMAF for Media over QUIC (LOCMAF)](https://datatracker.ietf.org/doc/draft-einarsson-moq-locmaf/) — This document specifies LOCMAF (Low Overhead CMAF for Media over
   QUIC), a compact packaging for low-latency CMAF media carried end-to-
   end as MoQ Transport (MOQT) Object payloads, with per-object overhead
   comparable to the Low Overhead Container (LOC).  LOCMAF carries the
   CMAF chunk head metadata from a single moof (movie fragment) as a
   small set of tagged fields, while leaving the sample data (mdat)
   untouched.  Boxes that may surround the moof in a CMAF chunk — styp
   (segment type), prft (producer reference time), and any number of
   emsg (event message) boxes — are carried verbatim, each through a
   generic box element (a genBox).  The first Object of each MOQT group
   carries a full reference; subsequent Objects in the same group carry
   only the differences.  The receiver reconstructs CMAF chunks that are
   decode-equivalent to the sender input, including the encryption
   metadata required by CMAF DRM (Common Encryption) pipelines, and a
   canonical byte-identical reconstruction — independent of the
   encoder's representation choices — is defined for conformance
   testing.
- **draft-englishm-moq-relay-dos-01** (new-draft, score 0, ignored_after_review) [none]: [Denial-of-Service Considerations for Media over QUIC Relay Deployments](https://datatracker.ietf.org/doc/draft-englishm-moq-relay-dos/) — The Media over QUIC Transport (MoQT) protocol presents denial-of-
   service risks that differ in character from those facing typical
   request-response protocols.  MoQT relays forward, fan out, and
   optionally cache media content on behalf of publishers and
   subscribers.  This document complements the MoQT Security
   Considerations, focusing on the unique considerations for relays.
- **draft-filsfils-ippm-path-tracing-06** (new-draft, score 0, ignored_after_review) [none]: [Path Tracing in SRv6 networks](https://datatracker.ietf.org/doc/draft-filsfils-ippm-path-tracing/) — Path Tracing provides a record of the packet path as a sequence of
   interface ids.  In addition, it provides a record of end-to-end
   delay, per-hop delay, and load on each egress interface along the
   packet delivery path.

   Path Tracing allows to trace 14 hops with only a 40-bytes IPv6 Hop-
   by-Hop extension header.

   Path Tracing supports fine grained timestamp.  It has been designed
   for linerate hardware implementation in the base pipeline.
- **draft-filsfils-spring-path-tracing-srmpls-08** (new-draft, score 0, ignored_after_review) [none]: [Path Tracing in SR-MPLS networks](https://datatracker.ietf.org/doc/draft-filsfils-spring-path-tracing-srmpls/) — Path Tracing provides a record of the packet path as a sequence of
   interface ids.  In addition, it provides a record of end-to-end
   delay, per-hop delay, and load on each interface that forwards the
   packet.

   Path Tracing has the lowest MTU overhead compared to alternative
   proposals such as [INT], [RFC9197], [I-D.song-opsawg-ifit-framework],
   and [I-D.kumar-ippm-ifa].

   Path Tracing supports fine grained timestamp.  It has been designed
   for linerate hardware implementation in the base pipeline.

   This document defines the Path Tracing specification for the SR-MPLS
   dataplane.  The Path Tracing specification for the SRv6 dataplane is
   defined in [I-D.filsfils-spring-path-tracing].
- **draft-flechier-sidrops-pava-02** (new-draft, score 0, ignored_after_review) [none]: [PAVA: BGP AS_PATH Validation by Querying ASes about Their Relationships](https://datatracker.ietf.org/doc/draft-flechier-sidrops-pava/) — This document defines PAth VAlidation (PAVA), a scheme for validating
   the Border Gateway Protocol (BGP) AS_PATH field based on the AS
   relationships.  Validation involves sending queries to the ASes along
   the path and each query specifies information about the prefix and
   the relevant path segment.  In this draft, for the decentralized
   distribution system that ASes on a path need for distributing the
   information, we propose to use the Domain Name System (DNS) and
   DNSSEC.
- **draft-fu-nmop-tokenops-probelem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Token Operation Problem Statement](https://datatracker.ietf.org/doc/draft-fu-nmop-tokenops-probelem-statement/) — Distributed LLM inference relies heavily on high-performance
   networking to synchronize states across accelerators (e.g., GPUs) and
   nodes.  Unlike traditional web services, inference workloads
   particularly those involving Mixture-of-Experts (MoE) models and
   long-context windows exhibit unique traffic patterns characterized by
   massive east-west traffic and strict latency constraints.  Current
   network infrastructures and scheduling methods often treat compute
   resources and network paths independently, leading to suboptimal
   performance and degraded Quality of Experience (QoE).  This document
   elaborates on these issues to guide potential protocol enhancements
   within the IETF.
- **draft-gl-lsr-metric-normalize-01** (new-draft, score 0, ignored_after_review) [none]: [Metric Normalize for IGP Flex-algo](https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/) — When multiple links in a network have the same metric, they can
   serve as ECMP equivalent links for load balancing during forwarding.
   However, slight fluctuations in metric values can prevent the
   formation of ECMP equivalent links, leading to the idle state of
   suboptimal links and thus wasting bandwidth resources.

   This document proposes a metric normalization method by advertising
   metric normalization parameters corresponding to a specific Metric-
   Type for Flexible Algorithm. During route calculation, slight
   fluctuations across multiple links are adjusted according to these
   normalization parameters, making the computed metric values more
   consistent. This approach enables the formation of ECMP equivalent
   links and promotes load sharing in the forwarding process.
- **draft-gray-lamps-compositepkc-01** (new-draft, score 0, ignored_after_review) [none]: [Preventing Key Reuse and Cross-Key Forgeries in Composite ML-DSA](https://datatracker.ietf.org/doc/draft-gray-lamps-compositepkc/) — This document defines a small, backwards-compatible change to
   composite ML-DSA that cryptographically binds the signature to the
   specific composite public key.  It does so by defining a Public-Key
   Context value (pkc) equal to a hash of the serialized composite
   public key, and by setting the composite context field to that value.
   This prevents key reuse and cross-key forgeries across different
   composite keys, while preserving the API of Composite ML-DSA.  The
   construction introduces two helper procedures to compute pkc from
   either the composite private key or the composite public key.
- **draft-gray-plants-mtc-deploy-use-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Merkle Tree Certificates Deployment Use Cases](https://datatracker.ietf.org/doc/draft-gray-plants-mtc-deploy-use-cases/) — Merkle Tree Certificates (MTC) I-D.ietf-plants-merkle-tree-certs has
   been defined for the use case of the WebPKI.  In this document we
   explore when and how MTC in parts or full can be used in different
   use cases.  Some of this use-cases may provide benefit for private
   PKI usage.
- **draft-grayson-connectinfo-10** (new-draft, score 0, ignored_after_review) [radext]: [A syntax for the RADIUS Connect-Info attribute used in Wi-Fi networks](https://datatracker.ietf.org/doc/draft-grayson-connectinfo/) — This document describes a syntax for the Connect-Info attribute used
   with the RADIUS protocol, enabling RADIUS clients to provide RADIUS
   servers information pertaining to a user's connection with an IEEE
   802.11 wireless network.
- **draft-grayson-radext-wba-wifi-quality-metrics-00** (new-draft, score 0, ignored_after_review) [none]: [RADIUS WBA Vendor-Specific Attributes for Wi-Fi Network Quality Metric Reporting](https://datatracker.ietf.org/doc/draft-grayson-radext-wba-wifi-quality-metrics/) — This document defines a set of RADIUS Vendor-Specific Attributes
   (VSAs) designed to encode network quality metrics that are not
   uniquely associated with an IEEE 802.11 (Wi-Fi) connection.  These
   attributes enable access network quality information to be
   communicated between RADIUS clients and servers.
- **draft-gupta-httpapi-events-query-03** (new-draft, score 0, ignored_after_review) [none]: [HTTP Events Query](https://datatracker.ietf.org/doc/draft-gupta-httpapi-events-query/) — Events Query is a minimal protocol built on top of HTTP that allows
   user agents to receive event notifications directly from any resource
   of interest.  It uses the QUERY method [RFC10008] to request
   (optionally) the current representation and subsequent event
   notifications within a single response.  The Events Query Protocol
   (EQP) is predicated on the idea that the most intuitive source for
   event notifications is the resource itself.
- **draft-guthrie-cnsa2-ipsec-profile-03** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for IPsec](https://datatracker.ietf.org/doc/draft-guthrie-cnsa2-ipsec-profile/) — This document defines a base profile for IPsec for use with the US
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
- **draft-halmir-mpls-ecn-03** (new-draft, score 0, ignored_after_review) [none]: [Explicit Congestion Notification Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-halmir-mpls-ecn/) — It has been broadly demonstrated that user experience improvements
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
- **draft-he-ippm-ioam-trace-type-bandwidth-00** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace-Type Extensions for Path bandwidth](https://datatracker.ietf.org/doc/draft-he-ippm-ioam-trace-type-bandwidth/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can accommodate the capacity of the traffic to be
   scheduled.  In situ Operations, Administration, and Maintenance
   (IOAM) is used for recording and collecting operational and telemetry
   information.  This document defines two bit flags within IOAM Trace-
   Type for carrying bandwidth information.
- **draft-hegde-lsr-isis-osnc-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Originator Sequence Number Checksum TLV](https://datatracker.ietf.org/doc/draft-hegde-lsr-isis-osnc/) — This document introduces a new top-level TLV in IS-IS to carry a
   checksum over the LSP IDs and sequence numbers of all self-originated
   LSP fragments.  A receiving node uses this value to validate the
   integrity of the originator's Link State Database (LSDB).
- **draft-huitema-ccwg-c4-test-03** (new-draft, score 0, ignored_after_review) [none]: [Testing of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design was validated by
   series of simulations, and also by initial deployments in control
   networks.  We describe here these simulations and tests.
- **draft-iab-protocol-greasing-01** (new-draft, score 0, ignored_after_review) [iab]: [Considerations For Maintaining Protocols Using Grease and Variability](https://datatracker.ietf.org/doc/draft-iab-protocol-greasing/) — Active use and maintenance of network protocols is an important way
   to ensure that protocols remain interoperable and extensible over
   time.  Techniques such as intentionally exercising extension points
   with non-meaningful values (referred to as "grease") or adding
   variability to how protocol elements are used help generate this
   active use.

   Grease and variability are used across various protocols developed by
   the IETF.  This document discusses considerations when designing and
   deploying grease and variability mechanisms, and provides advice for
   making them as effective as possible.
- **draft-ietf-6lo-nd-gaao-10** (new-draft, score 0, ignored_after_review) [6lo]: [Generic Address Assignment Option for 6LoWPAN Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6lo-nd-gaao/) — This document specifies a new extension to the IPv6 Neighbor
   Discovery in Low Power and Lossy Networks (LLNs), enabling a node to
   request to be assigned an address or a prefix from neighbor routers.
   Such mechanism allows to algorithmically assign addresses and
   prefixes to nodes in a 6LoWPAN deployment.
- **draft-ietf-6man-rfc8504-bis-03** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 Node Requirements](https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/) — This document defines requirements for IPv6 nodes.  It is expected
   that IPv6 will be deployed in a wide range of devices and situations.
   Specifying the requirements for IPv6 nodes allows IPv6 to function
   well and interoperate in a large number of situations and
   deployments.

   This document obsoletes RFC 8504, and in turn RFC 6434 and its
   predecessor, RFC 4294.
- **draft-ietf-anima-rfc8366bis-32** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Bootstrapping Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-avtcore-frame-acknowledgement-01** (new-draft, score 0, ignored_after_review) [avtcore]: [RTCP Feedback Message and Request Mechanism for Frame-level Acknowledgement](https://datatracker.ietf.org/doc/draft-ietf-avtcore-frame-acknowledgement/) — This document describes a mechanism for signaling which video frames
   have been received and decoded by a remote peer.  It comprises an
   RTCP feedback message and an RTP header extension used to request
   said feedback.

   One of the main use cases for this data is to implement various forms
   of Long Term Reference (LTR) reference structures.  Additionally, the
   mechanism provides a way for receivers to request resynchronization
   frames that reference acknowledged frames, enabling efficient
   recovery from partial or full frame loss without requiring a full
   keyframe.
- **draft-ietf-bess-bgp-multicast-controller-18** (new-draft, score 0, ignored_after_review) [bess]: [Controller-based BGP Multicast Signaling](https://datatracker.ietf.org/doc/draft-ietf-bess-bgp-multicast-controller/) — This document specifies a way that one or more centralized
   controllers can use BGP to set up multicast distribution trees
   (identified by either IP source/destination address pair, or mLDP
   FEC) in a network.  Since the controllers calculate the trees, they
   can use sophisticated algorithms and constraints to achieve traffic
   engineering.  The controllers directly signal dynamic replication
   state to tree nodes, leading to very simple multicast control plane
   on the tree nodes, as if they were using static routes.  This can be
   used for both underlay and overlay multicast trees, including
   replacing BGP-MVPN signaling.
- **draft-ietf-bess-mup-safi-01** (new-draft, score 0, ignored_after_review) [bess]: [BGP Extensions for the Mobile User Plane (MUP) SAFI](https://datatracker.ietf.org/doc/draft-ietf-bess-mup-safi/) — This document defines a new SAFI known as a BGP Mobile User Plane
   (BGP-MUP) SAFI to support MUP Extensions and a extended community for
   BGP.  This document also provides BGP signaling and procedures for
   the new SAFI to convert mobile session information into appropriate
   IP forwarding information.  These extensions can be used by operators
   between a PE, and a Controller for integrating mobile user plane into
   BGP MUP network using the IP based routing.
- **draft-ietf-calext-icalendar-jscalendar-extensions-06** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545 ("iCalendar") and its
   extension documents RFC 7986 and RFC 9073.
- **draft-ietf-calext-jscalendar-icalendar-24** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-calext-rfc9555bis-01** (new-draft, score 0, ignored_after_review) [calext]: [JSContact: Converting from and to vCard](https://datatracker.ietf.org/doc/draft-ietf-calext-rfc9555bis/) — This document defines how to convert contact information between the
   JSContact and vCard data formats.  It defines conversion rules for
   every JSContact and vCard element registered at IANA at the time of
   publication.  It also defines new JSContact properties as well as
   vCard properties and parameters, to support converting arbitrary or
   unknown JSContact and vCard elements.  This document obsoletes RFC
   9555 and updates its definitions for JSContact version "2.0".

Note

   This note is to be removed before publishing as an RFC.

   Differences from RFC 9555 are documented in Appendix A.
- **draft-ietf-ccwg-rfc8298bis-screamv2-01** (new-draft, score 0, ignored_after_review) [ccwg]: [Self-Clocked Rate Adaptation for Multimedia](https://datatracker.ietf.org/doc/draft-ietf-ccwg-rfc8298bis-screamv2/) — This memo describes Self-Clocked Rate Adaptation for Multimedia
   version 2 (SCReAMv2), an update to SCReAM congestion control for
   media streams such as RTP [RFC3550].  SCReAMv2 includes several
   algorithm simplifications and adds support for L4S.  The algorithm
   supports handling of multiple media streams, typical use cases are
   streaming for remote control, AR and 3D VR goggles.  This
   specification obsoletes RFC 8298.
- **draft-ietf-cdni-edge-control-metadata-12** (new-draft, score 0, ignored_after_review) [cdni]: [Content Delivery Network Interconnection (CDNI) Edge Control Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-edge-control-metadata/) — This specification defines configuration metadata objects used to
   manage how edge servers control access to resources within Content
   Delivery Networks (CDNs) and Open Caching systems.  A key feature of
   these configurations is the configuring of Cross-Origin Resource
   Sharing (CORS) access rules and the dynamic generation of CORS
   headers.  This specification also provides the ability to define
   response body compression rules and client connection timeouts.
- **draft-ietf-cdni-logging-extensions-04** (new-draft, score 0, ignored_after_review) [cdni]: [CDNI Logging Extensions](https://datatracker.ietf.org/doc/draft-ietf-cdni-logging-extensions/) — This document defines a set of extensions to CDNI for supporting
   transmission of transaction logs in both push and pull operational
   modes, new log container formats and log record formats, new logging
   fields, and metadata for describing the transformation, obfuscation,
   and encryption of log record fields.
- **draft-ietf-cdni-protected-secrets-metadata-07** (new-draft, score 0, ignored_after_review) [cdni]: [CDNI Protected Secrets Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-protected-secrets-metadata/) — This document defines a simple mechanism for protected secret data
   (such as salt values or encryption keys) that may be embedded in
   configuration metadata or capabilities advertisements.
- **draft-ietf-core-cacheable-oscore-02** (new-draft, score 0, ignored_after_review) [core]: [End-to-End Protected and Cacheable CoAP Responses using Group Object Security for Constrained RESTful Environments (Group OSCORE)](https://datatracker.ietf.org/doc/draft-ietf-core-cacheable-oscore/) — When using the Constrained Application Protocol (CoAP), exchanged
   messages can be protected end-to-end also across untrusted
   intermediary proxies.  This can be achieved with Object Security for
   Constrained RESTful Environments (OSCORE) or, in the case of group
   communication, with Group Object Security for Constrained RESTful
   Environments (Group OSCORE).  However, this sidesteps the proxies'
   abilities to cache responses from the origin server(s).  This
   document restores cacheability of end-to-end protected responses at
   proxies, by using Group OSCORE and introducing consensus requests,
   which any client in an OSCORE group can send to one server or
   multiple servers in the same group.
- **draft-ietf-core-conditional-attributes-13** (new-draft, score 0, ignored_after_review) [core]: [Conditional Query Parameters for CoAP Observe](https://datatracker.ietf.org/doc/draft-ietf-core-conditional-attributes/) — This specification defines Conditional Notification and Control Query
   Parameters compatible with CoAP Observe (RFC7641).
- **draft-ietf-core-multicast-notifications-proxy-02** (new-draft, score 0, ignored_after_review) [core]: [Using Proxies for Observe Notifications as CoAP Multicast Responses](https://datatracker.ietf.org/doc/draft-ietf-core-multicast-notifications-proxy/) — The Constrained Application Protocol (CoAP) allows clients to
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
- **draft-ietf-core-observe-multicast-notifications-15** (new-draft, score 0, ignored_after_review) [core]: [Observe Notifications as CoAP Multicast Responses](https://datatracker.ietf.org/doc/draft-ietf-core-observe-multicast-notifications/) — The Constrained Application Protocol (CoAP) allows clients to
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
- **draft-ietf-core-oscore-capable-proxies-07** (new-draft, score 0, ignored_after_review) [core]: [OSCORE-capable Proxies](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-capable-proxies/) — When using the Constrained Application Protocol (CoAP), messages
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
- **draft-ietf-core-oscore-key-limits-07** (new-draft, score 0, ignored_after_review) [core]: [Key Usage Limits for OSCORE](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-key-limits/) — Object Security for Constrained RESTful Environments (OSCORE) uses
   AEAD algorithms to ensure confidentiality and integrity of exchanged
   messages.  Due to known issues allowing forgery attacks against AEAD
   algorithms, limits should be followed on the number of times a
   specific key is used for encryption or decryption.  Among other
   reasons, approaching key usage limits requires updating the OSCORE
   keying material before communications can securely continue.  This
   document defines how two OSCORE peers can follow these key usage
   limits and what steps they should take to preserve the security of
   their communications.
- **draft-ietf-core-oscore-key-update-14** (new-draft, score 0, ignored_after_review) [core]: [Key Update for OSCORE (KUDOS)](https://datatracker.ietf.org/doc/draft-ietf-core-oscore-key-update/) — Communications with the Constrained Application Protocol (CoAP) can
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
- **draft-ietf-core-uri-path-abbrev-05** (new-draft, score 0, ignored_after_review) [core]: [URI Path abbreviation in CoAP](https://datatracker.ietf.org/doc/draft-ietf-core-uri-path-abbrev/) — Applications built on CoAP face a conflict between the technical need
   for short message sizes and the interoperability requirement of
   following BCP190 and thus using (relatively verbose) well-known URI
   paths.  This document introduces the Uri-Path-Abbrev CoAP option that
   allows expressing well-known URI paths in as little as two bytes.

   Using this option revealed a subtle flaw in RFC7252 that severely
   limited the extension point of critical options.  This document
   updates RFC7252 to rectify that.
- **draft-ietf-detnet-nscore-02** (new-draft, score 0, ignored_after_review) [detnet]: [On-time Forwarding with Non-Work Conserving Stateless Core Fair Queuing](https://datatracker.ietf.org/doc/draft-ietf-detnet-nscore/) — This document specifies the framework and operational procedure for
   deterministic networking that guarantees maximum and minimum end-to-
   end latency bounds to flows.  The solution has non-periodic,
   asynchronous, flow-level, non-work conserving, on-time, and rate-
   based functional characteristics, according to the taxonomy suggested
   by [I-D.ietf-detnet-dataplane-taxonomy].

   The packets are stored in the queue in ascending order of the ideal
   service start time, called Eligible Time (ET), and the ideal service
   completion time, called Finish Time (FT).  The queued packets were
   forwarded after ET, in ascending ordering of FT, in a non-work
   conserving manner.  The ET and FT are calculated at the entrance node
   according to the packet size and rate of the flow.  All subsequent
   core nodes are stateless and asynchronously update ET and FT based on
   metadata received via packet headers.  This mechanism is called non-
   work conserving stateless fair queuing (N-SCORE), which guarantees
   both E2E latency upper and lower bounds, thus E2E jitter bound.

   N-SCORE supports two alternative methods for determining ET and FT at
   stateless core nodes.

   The Direct ET/FT Method propagates ET and FT generated by the
   previous node using the delay factor function.

   The Arrival-based ET/FT Method reconstructs ET and FT from the
   locally observed packet arrival time together with metadata carried
   in the packet header.  Both methods provide identical scheduling
   semantics while allowing different implementation choices.
- **draft-ietf-detnet-ontime-forwarding-02** (new-draft, score 0, ignored_after_review) [detnet]: [On-time Forwarding with Push-In First-Out (PIFO) queue](https://datatracker.ietf.org/doc/draft-ietf-detnet-ontime-forwarding/) — This document describes operations of data plane and controller plane
   for Deterministic Networking (DetNet) to forward packets to meet
   minimum and maximum end-to-end latency requirements, while utilizing
   Push-In First-Out (PIFO) queue.

   According to the solution described in this document, forwarding
   nodes do not need to maintain flow states or to be time-synchronized
   with each other.
- **draft-ietf-diem-requirements-03** (new-draft, score 0, ignored_after_review) [diem]: [Digital Emblems - Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-diem-requirements/) — Digital emblems are a means for an asset to signal to validating
   entities that it should be protected or treated in a specific way,
   using some normative framework.  This document lists the requirements
   and use cases that an architecture for digital emblems must
   accommodate.
- **draft-ietf-dmm-tn-aware-mobility-27** (new-draft, score 0, ignored_after_review) [dmm]: [Mobility-aware Transport Network Slicing for 5G](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
   services of multiple 5G customers to be multiplexed over the same
   infrastructure.  While 5G slicing covers logical separation of
   various aspects of 5G infrastructure and services, user's data plane
   packets over the Radio Access Network (RAN) and Core Network (5GC)
   use IP in many segments of an end-to-end 5G slice.  When end-to-end
   slices in a 5G System use network resources, they are mapped to
   corresponding Transport Network (TN) slice(s) which in turn provide
   the bandwidth, latency, isolation, and other criteria required for
   the realization of a 5G slice.

   This document describes mapping of 5G slices to TN slices using UDP
   source port number of the GTP-U bearer when the TN slice provider is
   separated by an "attachment circuit" from the networks in which the
   5G network functions are deployed, for example, 5G functions that are
   distributed across data centers.  The slice mapping defined here is
   supported transparently when a 5G user device moves across 5G
   attachment points and session anchors.
- **draft-ietf-dnsop-grease-03** (new-draft, score 0, ignored_after_review) [dnsop]: [Greasing Protocol Extension Points in the DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-grease/) — Long term evolvability of the Domain Name System (DNS) protocol
   requires the ability to support change.  Greasing is one technique
   that exercises the regular use of unallocated protocol extension
   points to prevent ossification of their current usage patterns by
   middleboxes or DNS implementations.  This document describes
   considerations and proposals for applying grease to the DNS protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-wg-dnsop/draft-ietf-dnsop-grease.
- **draft-ietf-dnsop-structured-dns-error-25** (new-draft, score 0, ignored_after_review) [dnsop]: [Structured Error Data for Filtered DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/) — DNS filtering is widely deployed for various reasons, including
   network security and policy enforcement.  However, filtered DNS
   responses lack structured information for end users to understand the
   reason for the filtering.  Existing mechanisms to provide explanatory
   details to end users cause harm especially if the blocked DNS
   response is for HTTPS resources.

   This document updates RFC 8914 by signaling client support for
   structuring the EXTRA-TEXT field of the Extended DNS Error to provide
   details on the DNS filtering.  Such details can be parsed by the
   client and displayed, logged, or used for other purposes.
- **draft-ietf-dnssd-advertising-proxy-06** (new-draft, score 0, ignored_after_review) [dnssd]: [Advertising Proxy for DNS-SD Service Registration Protocol](https://datatracker.ietf.org/doc/draft-ietf-dnssd-advertising-proxy/) — An Advertising Proxy advertises the contents of a DNS zone, for
   example maintained using the DNS-SD Service Registration Protocol
   (SRP), using Multicast DNS.  This allows legacy clients to discover
   services registered with SRP using Multicast DNS.
- **draft-ietf-dnssd-tsr-03** (new-draft, score 0, ignored_after_review) [dnssd]: [Multicast DNS conflict resolution using the Time Since Received (TSR) EDNS option](https://datatracker.ietf.org/doc/draft-ietf-dnssd-tsr/) — This document specifies a new conflict resolution mechanism for DNS,
   for use in cases where the advertisement is being proxied, rather
   than advertised directly, e.g. when using a combined DNS-SD
   advertising proxy and SRP registrar.  A new EDNS option is defined
   that communicates the time at which the set of resource records on a
   particular DNS owner name was most recently updated.
- **draft-ietf-dtn-bp-sand-03** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol (BP) Secure Advertisement and Neighborhood Discovery (SAND)](https://datatracker.ietf.org/doc/draft-ietf-dtn-bp-sand/) — This document defines the Secure Advertisement and Neighborhood
   Discovery (SAND) protocol for Bundle Protocol version 7 (BPv7) within
   a delay-tolerant network (DTN).  This protocol defines a general
   purpose advertisement mechanism with an initial set of message and
   data types able to be advertised by participating nodes in a BPv7
   network.  The focus of this document is for advertisement to
   topological neighbors about local neighborhoods but can be expanded
   upon in the future through extension points.
- **draft-ietf-dtn-eid-pattern-09** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol Endpoint ID Patterns](https://datatracker.ietf.org/doc/draft-ietf-dtn-eid-pattern/) — This document extends the Bundle Protocol Endpoint ID (EID) concept
   into an EID Pattern, which is used to categorize any EID as matching
   a specific pattern or not.  EID Patterns are suitable for expressing
   configuration, for being used on-the-wire by protocols, and for being
   easily understandable by a layperson.  EID Patterns include scheme-
   specific optimizations for expressing set membership and each scheme
   pattern includes text and binary encoding forms; the pattern for the
   "ipn" EID scheme being designed to be highly compressible in its
   binary form.  This document also defines a Public Key Infrastructure
   Using X.509 (PKIX) Other Name form to contain an EID Pattern and a
   handling rule to use a pattern to match an EID.
- **draft-ietf-green-framework-02** (new-draft, score 0, ignored_after_review) [green]: [Framework for Energy Efficiency Management](https://datatracker.ietf.org/doc/draft-ietf-green-framework/) — Recognizing the urgent need for energy efficiency, this document
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
- **draft-ietf-hpke-hpke-04** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document describes a scheme for hybrid public key encryption
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
- **draft-ietf-hpke-pq-05** (new-draft, score 0, ignored_after_review) [hpke]: [Post-Quantum and Post-Quantum/Traditional Hybrid Algorithms for HPKE](https://datatracker.ietf.org/doc/draft-ietf-hpke-pq/) — Updating key exchange and public-key encryption protocols to resist
   attack by quantum computers is a high priority given the possibility
   of "harvest now, decrypt later" attacks.  Hybrid Public Key
   Encryption (HPKE) is a widely-used public key encryption scheme based
   on combining a Key Encapsulation Mechanism (KEM), a Key Derivation
   Function (KDF), and an Authenticated Encryption with Associated Data
   (AEAD) scheme.  In this document, we define KEM algorithms for HPKE
   based on both post-quantum KEMs and hybrid constructions of post-
   quantum KEMs with traditional KEMs, as well as a KDF based on SHA-3
   that is suitable for use with these KEMs.  When used with these
   algorithms, HPKE is resilient with respect to attacks by a quantum
   computer.
- **draft-ietf-ianabis-rfc7120bis-03** (new-draft, score 0, ignored_after_review) [ianabis]: [Early IANA Code Point Allocation](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc7120bis/) — This document describes the requirements for securing IANA code point
   assignments for IETF Stream Internet-Drafts and specifications being
   drafted by other standards-related organizations.  This document
   obsoletes RFC 7120.
- **draft-ietf-ianabis-rfc8126bis-03** (new-draft, score 0, ignored_after_review) [ianabis]: [Guidelines for Writing an IANA Considerations Section in RFCs](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc8126bis/) — Many protocols make use of points of extensibility that use constants
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
- **draft-ietf-idr-bgp-ls-sr-policy-nrp-03** (new-draft, score 0, ignored_after_review) [idr]: [SR Policies Extensions for Network Resource Partition in BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-nrp/) — A Network Resource Partition (NRP) is a subset of the network
   resources and associated policies on each of a connected set of links
   in the underlay network.  An NRP ID is an important network resource
   attribute associated with the Segment Routing (SR) policy and needs
   to be reported to the external components.  This document defines a
   new TLV which enables the headend to report the NRP which the SR
   Policy Candidate Path (CP) is associated with using Border Gateway
   Protocol Link-State (BGP-LS).
- **draft-ietf-idr-bgp4-rfc4271bis-01** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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
- **draft-ietf-idr-fsv2-ip-basic-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 - for Basic IP](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/) — BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
   8956, and RFC 9117, describes the distribution of traffic filter
   policy (traffic filters and actions) distributed via BGP.  During the
   deployment of BGP FSv1 a number of issues were detected, so version 2
   of the BGP flow specification (FSv2) protocol addresses these issues.
   In order to provide a clear demarcation between FSv1 and FSv2, a
   different NLRI encapsulates FSv2.

   The IDR WG requires two implementation.  Early feedback on
   implementations of FSv2 indicate that FSv2 has a correct design
   direction, but that breaking FSv2 into a progression of documents
   would aid deployment of the draft (basic, adding more filters, and
   adding more actions).  This document specifies the basic FSv2 NLRI
   with user ordering of filters added to FSv1 IP Filters and FSv2
   actions.
- **draft-ietf-idr-sr-policy-nrp-12** (new-draft, score 0, ignored_after_review) [idr]: [BGP SR Policy Extensions for Network Resource Partition](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-nrp/) — Segment Routing (SR) Policy is a set of candidate paths, each
   consisting of one or more segment lists and the associated
   information.  The header of a packet steered in an SR Policy is
   augmented with an ordered list of segments associated with that SR
   Policy.  A Network Resource Partition (NRP) is a subset of network
   resources allocated in the underlay network which can be used to
   support one or a group of RFC 9543 network slice services.

   In networks where there are multiple NRPs, an SR Policy may be
   associated with a particular NRP.  The association between SR Policy
   and NRP needs to be specified, so that for service traffic which is
   steered into the SR Policy, the header of the packets can be
   augmented with the information associated with the NRP.  An SR Policy
   candidate path can be distributed using BGP SR Policy.  This document
   defines the extensions to BGP SR Policy to specify the NRP which the
   SR Policy candidate path is associated with.
- **draft-ietf-iotops-7228bis-10** (new-draft, score 0, ignored_after_review) [iotops]: [Terminology for Constrained-Node Networks](https://datatracker.ietf.org/doc/draft-ietf-iotops-7228bis/) — The Internet Protocol Suite is increasingly used on small devices
   with severe constraints on power, memory, and processing resources,
   creating constrained-node networks.  This document provides a number
   of basic terms that have been useful in research and standardization
   work for constrained-node networks.

   This document obsoletes RFC 7228.
- **draft-ietf-iotops-iot-dns-guidelines-04** (new-draft, score 0, ignored_after_review) [iotops]: [IoT DNS Security and Privacy Guidelines](https://datatracker.ietf.org/doc/draft-ietf-iotops-iot-dns-guidelines/) — This document outlines guidance for Internet of Things (IoT)
   manufacturers regarding the implementation of DNS stub resolver
   software on devices, and for the management zones used for purposes
   such as device configuration and software upgrades.  It aims to
   mitigate security threats, enhance privacy, and to address
   operational security challenges.

   DNS resolution between devices and management zone servers depends
   upon DNS services within operator networks, and these services and
   operator networks can be impacted by device behavior.  Hence this
   document also provides guidance to network operators that deploy IoT
   devices to mitigate the specific risks identified in this document
   and take advantage of improved DNS security mechanisms provided by
   manufacturers.
- **draft-ietf-ippm-responsiveness-09** (new-draft, score 0, ignored_after_review) [ippm]: [Responsiveness under Working Conditions](https://datatracker.ietf.org/doc/draft-ietf-ippm-responsiveness/) — For many years, a lack of responsiveness, variously called lag,
   latency, or bufferbloat, has been recognized as an unfortunate, but
   common, symptom in today's networks.  Even after a decade of work on
   standardizing technical solutions, it remains a common problem for
   the end users.

   Everyone "knows" that it is "normal" for a video conference to have
   problems when somebody else at home is watching a 4K movie or
   uploading photos from their phone.  However, there is no technical
   reason for this to be the case.  In fact, various queue management
   solutions have solved the problem.

   Our network connections continue to suffer from an unacceptable
   amount of delay, not for a lack of technical solutions, but rather a
   lack of awareness of the problem and deployment of its solutions.  We
   believe that creating a tool that measures the problem and matches
   people's everyday experience will create the necessary awareness, and
   result in a demand for solutions.

   This document specifies the "Responsiveness Test" for measuring
   responsiveness.  It uses common protocols and mechanisms to measure
   user experience specifically when the network is under working
   conditions.  The measurement is expressed as "Round-trips Per Minute"
   (RPM) and should be included with goodput (up and down) and idle
   latency as critical indicators of network quality.
- **draft-ietf-ipsecme-ikev2-mlkem-09** (new-draft, score 0, ignored_after_review) [ipsecme]: [Post-quantum Key Exchange with ML-KEM in the Internet Key Exchange Protocol Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) — US NIST standardized ML-KEM, a new key encapsulation mechanism, which
   can be used for quantum-resistant key establishment.  This document
   specifies how to use ML-KEM by itself or as an additional key
   exchange in IKEv2 along with a traditional key exchange.  These
   options allow for negotiating IKE and Child SA keys which are
   resistant against cryptographically relevant quantum computers.
- **draft-ietf-mailmaint-smtputf8-syntax-04** (new-draft, score 0, ignored_after_review) [mailmaint]: [SMTPUTF8 Email Addresses](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-smtputf8-syntax/) — RFC 6532 extends the internet email format to allow UTF8 in many
   contexts.  This document restricts the set of allowed addresses in
   header fields slightly, and thereby simplifies use of these
   addresses.

   This is one of a pair of documents.  This one is simple to implement
   and contains only globally viable rules.  Its companion has more
   complex rules, takes regional usage into account, and describes
   addresses that can be read by some community and cut-and-pasted in
   some locale.
- **draft-ietf-manet-inet-gap-analysis-02** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mimi-arch-03** (new-draft, score 0, ignored_after_review) [mimi]: [An Architecture for More Instant Messaging Interoperability (MIMI)](https://datatracker.ietf.org/doc/draft-ietf-mimi-arch/) — The More Instant Messaging Interoperability (MIMI) working group is
   defining a suite of protocols that allow messaging providers to
   interoperate with one another.  This document lays out an overall
   architecture enumerating the MIMI protocols and how they work
   together to enable an overall messaging experience.
- **draft-ietf-mls-extensions-10** (new-draft, score 0, ignored_after_review) [mls]: [The Messaging Layer Security (MLS) Extensions](https://datatracker.ietf.org/doc/draft-ietf-mls-extensions/) — The Messaging Layer Security (MLS) protocol is an asynchronous group
   authenticated key exchange protocol.  MLS provides a number of
   capabilities to applications, as well as several extension points
   internal to the protocol.  This document provides a consolidated
   application API, guidance for how the protocol's extension points
   should be used, and a few concrete examples of both core protocol
   extensions and uses of the application API.
- **draft-ietf-mls-ratchet-tree-options-01** (new-draft, score 0, ignored_after_review) [mls]: [Ways to convey the Ratchet Tree in Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-ratchet-tree-options/) — The Messaging Layer Security (MLS) protocol needs to share its
   ratchet_tree object to welcome new clients into a group and in
   external joins.  While the protocol only defines a mechanism for
   sharing the entire tree, most implementations use various
   optimizations to avoid sending this structure repeatedly in large
   groups.  This document describes a way to convey these improvements
   in a standardized way and to convey the parts of a GroupInfo object
   that are not visible to an intermediary server.
- **draft-ietf-mls-virtual-clients-01** (new-draft, score 0, ignored_after_review) [mls]: [MLS Virtual Clients](https://datatracker.ietf.org/doc/draft-ietf-mls-virtual-clients/) — This document describes a method that allows multiple MLS clients to
   emulate a virtual MLS client.  A virtual client allows multiple
   emulator clients to jointly participate in an MLS group under a
   single leaf.  Depending on the design of the application, virtual
   clients can help hide metadata and improve performance.
- **draft-ietf-mops-network-overlay-impacts-04** (new-draft, score 0, ignored_after_review) [mops]: [Network Overlay Impacts to Streaming Video](https://datatracker.ietf.org/doc/draft-ietf-mops-network-overlay-impacts/) — This document examines the operational impacts on streaming video
   applications resulting from network policy changes introduced by
   network overlays.  Such overlays may alter IP address assignment,
   transport protocols, routing behavior, or DNS resolution.  These
   changes can, in turn, affect critical aspects of content delivery,
   including latency, CDN cache selection, delivery path optimization,
   traffic classification, and content access controls.
- **draft-ietf-moq-loc-03** (new-draft, score 0, ignored_after_review) [moq]: [Low Overhead Media Container](https://datatracker.ietf.org/doc/draft-ietf-moq-loc/) — This specification describes a Low Overhead Media Container (LOC)
   format for encoded and encrypted audio and video media data to be
   used primarily for interactive Media over QUIC Transport (MOQT).  It
   may be used in the MOQT Streaming Format (MSF) specification, which
   defines a catalog format for publishers to declare and describe their
   LOC tracks and for subscribers to consume them.  Examples are also
   provided for building media applications using LOC and MOQT.
- **draft-ietf-moq-secure-objects-01** (new-draft, score 0, ignored_after_review) [moq]: [End-to-End Secure Objects for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-secure-objects/) — This document specifies an end-to-end authenticated encryption scheme
   for application objects transmitted via Media over QUIC (MoQ)
   Transport.  The scheme enables original publishers that share a
   symmetric key with end subscribers, to ensuring that MoQ relays are
   unable to decrypt object contents.  Additionally, subscribers can
   verify the integrity and authenticity of received objects, confirming
   that the content has not been modified in transit.  Additionally it
   allows MoQ parameters to be protected so the publisher can select if
   they are readable and/or modifiable by relays.
- **draft-ietf-moq-transport-19** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-mpls-on-path-telemetry-flag-01** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes the postcard-based on-path telemetry with
   packet marking (PBT-M) using an MPLS Network Actions (MNA) flag to
   support OAM in MPLS networks.  The scheme uses a single flag bit
   carried in a Flag-Based Network Action Indicator (Opcode 1) of the
   MNA Sub-Stack as defined in RFC 9994.  The document provides the
   solutions to address the requirements for applying PBT-M in MPLS
   networks.
- **draft-ietf-netconf-https-notif-cbor-01** (new-draft, score 0, ignored_after_review) [netconf]: [CBOR Encoding for HTTPS-based YANG Notifications Transport](https://datatracker.ietf.org/doc/draft-ietf-netconf-https-notif-cbor/) — This document extends [I-D.draft-ietf-netconf-https-notif] by
   introducing CBOR encoding for YANG notifications over HTTPS transport
   in addition to the existing JSON and XML encoding schemes.
- **draft-ietf-netmod-iana-yang-guidance-03** (new-draft, score 0, ignored_after_review) [netmod]: [Guidance for Managing YANG Modules in RFCs and IANA Registries](https://datatracker.ietf.org/doc/draft-ietf-netmod-iana-yang-guidance/) — This document provides guidance to the RFC Editor and IANA on
   managing YANG modules in RFCs and IANA registries, ensuring
   consistent application of YANG Semantic Versioning rules.
- **draft-ietf-netmod-yang-packages-09** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Packages](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-packages/) — This document defines YANG packages: versioned organizational
   structures used to manage the schema and conformance of a set of YANG
   modules as a cohesive unit.
- **draft-ietf-netmod-yang-semver-27** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Semantic Versioning](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-semver/) — This document specifies a YANG extension along with guidelines for
   applying an extended set of semantic versioning rules to revisions of
   YANG artifacts (e.g., modules and packages).  Additionally, this
   document defines a YANG extension for controlling module imports
   based on these modified semantic versioning rules.

   This document updates RFCs 7950, 9907, and 8525.
- **draft-ietf-nmop-network-anomaly-architecture-08** (new-draft, score 0, ignored_after_review) [nmop]: [A Framework for a Network Anomaly Detection Architecture](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-anomaly-architecture/) — This document describes the motivation and architecture of a Network
   Anomaly Detection Framework and the relationship to other documents
   describing network Symptom semantics and network incident lifecycle.

   The described architecture for detecting IP network service
   interruption is designed to be generic applicable and extensible.
   Different applications are described and examples are referenced with
   open-source running code.
- **draft-ietf-nmop-network-anomaly-lifecycle-06** (new-draft, score 0, ignored_after_review) [nmop]: [An Experiment: Network Anomaly Detection Lifecycle](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-anomaly-lifecycle/) — This document defines a structured, iterative lifecycle for network
   anomaly detection systems to enable "human-in-the-loop" refinements.
   Key contributions include defining three lifecycle stages, a state
   machine for anomaly annotations, and YANG data models for
   standardized labeling and exchange.
- **draft-ietf-pce-flexible-grid-15** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-operational-03** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Operational Clarification](https://datatracker.ietf.org/doc/draft-ietf-pce-operational/) — This document clarifies certain operational behavior aspects of the
   Path Computation Element Communication Protocol (PCEP).  The content
   of this document has been compiled based on several interop
   exercises.  This document does not make any updates or revisions to
   any PCEP specifications, instead it provides additional information
   to aid in the interpretation of those documents.
- **draft-ietf-pce-pcep-nrp-01** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extensions for Network Resource Partition (NRP)](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-nrp/) — This document specifies the extensions to Path Computation Element
   Communication Protocol (PCEP) to carry Network Resource Partition
   (NRP) related information in the PCEP messages.  The extensions in
   this document can be used to indicate the NRP-specific constraints
   and information needed in path computation, path status report and
   path initialization.
- **draft-ietf-pce-sr-p2mp-policy-19** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-multicast-lessons-learned-09** (new-draft, score 0, ignored_after_review) [pim]: [Multicast Lessons Learned from Decades of Deployment Experience](https://datatracker.ietf.org/doc/draft-ietf-pim-multicast-lessons-learned/) — This document gives a historical perspective about the design and
   deployment of multicast routing protocols.  The document describes
   the technical challenges discovered from building these protocols.
   Even though multicast has enjoyed success of deployment in special
   use-cases, this draft discusses what were, and are, the obstacles for
   mass deployment across the Internet.  Individuals who are working on
   new multicast related protocols will benefit by knowing why certain
   older protocols are no longer in use today.
- **draft-ietf-pim-pfm-forwarding-enhancements-07** (new-draft, score 0, ignored_after_review) [pim]: [PIM Flooding Mechanism and Source Discovery Enhancements](https://datatracker.ietf.org/doc/draft-ietf-pim-pfm-forwarding-enhancements/) — The Protocol Independent Multicast (PIM) Flooding Mechanism (PFM) is
   an experimental extension that provides a generic hop-by-hop message
   exchange framework for distributing multicast information among PIM
   routers.  Existing PFM procedures enable efficient source discovery
   without reliance on Rendezvous Points, shared trees, or initial data
   registers.

   This document specifies further experimental enhancements to PFM
   forwarding behavior to improve efficiency and scalability.  In
   particular, it introduces mechanisms to reduce redundant message
   transmission over multiple parallel links and extends the encoding of
   multicast information through additional Type-Length-Value (TLV)
   structures and sub-TLVs to convey richer flow-related data.  These
   enhancements optimize control-plane overhead while preserving
   interoperability with existing PFM procedures, enabling more
   efficient dissemination of multicast state in PIM networks.
- **draft-ietf-procon-2418bis-03** (new-draft, score 0, ignored_after_review) [procon]: [IETF Working Group Guidelines and Procedures](https://datatracker.ietf.org/doc/draft-ietf-procon-2418bis/) — The Internet Engineering Task Force (IETF) has responsibility for
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
- **draft-ietf-quic-extended-key-update-03** (new-draft, score 0, ignored_after_review) [quic]: [Extended Key Update for QUIC](https://datatracker.ietf.org/doc/draft-ietf-quic-extended-key-update/) — This document specifies an Extended Key Update mechanism for the QUIC
   protocol, building on the foundation of the TLS Extended Key Update.
   The TLS Extended Key Update specification enhances the TLS protocol
   by introducing key updates with forward secrecy, eliminating the need
   to perform a full handshake.  This feature is particularly beneficial
   for maintaining security in scenarios involving long-lived
   connections.

   This specification replaces the QUIC Key Update mechanism described
   in the "Using TLS to Secure QUIC" specification.
- **draft-ietf-quic-qlog-h3-events-13** (new-draft, score 0, ignored_after_review) [quic]: [HTTP/3 qlog event definitions](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-h3-events/) — This document defines qlog event schemas containing concrete events
   for the core HTTP/3 protocol and selected extensions.  It also
   defines an http namespace for the Capsule Protocol.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.
- **draft-ietf-quic-qlog-main-schema-14** (new-draft, score 0, ignored_after_review) [quic]: [qlog: Structured Logging for Network Protocols](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-main-schema/) — qlog provides extensible structured logging for network protocols,
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
- **draft-ietf-quic-qlog-quic-events-13** (new-draft, score 0, ignored_after_review) [quic]: [QUIC event definitions for qlog](https://datatracker.ietf.org/doc/draft-ietf-quic-qlog-quic-events/) — This document describes a qlog event schema containing concrete qlog
   event definitions and their metadata for the core QUIC protocol and
   selected extensions.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.
- **draft-ietf-quic-qmux-02** (new-draft, score 0, ignored_after_review) [quic]: [QMux](https://datatracker.ietf.org/doc/draft-ietf-quic-qmux/) — This document specifies QMux version 1.  QMux version 1 provides,
   over bi-directional streams such as TLS, the same set of stream and
   datagram operations that applications rely upon in QUIC version 1.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the QUIC Working Group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/quic/.

   Source for this draft and an issue tracker can be found at
   https://github.com/quicwg/qmux.
- **draft-ietf-radext-radiusdtls-bis-17** (new-draft, score 0, ignored_after_review) [radext]: [RadSec: RADIUS over Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-ietf-radext-radiusdtls-bis/) — This document defines transport profiles for running RADIUS over
   Transport Layer Security (TLS) and Datagram Transport Layer Security
   (DTLS), allowing the secure and reliable transport of RADIUS
   messages.  RADIUS/TLS and RADIUS/DTLS are collectively referred to as
   RadSec.

   This document obsoletes RFC6614 and RFC7360, which specified
   experimental versions of RADIUS over TLS and DTLS.
- **draft-ietf-regext-epp-quic-12** (new-draft, score 0, ignored_after_review) [regext]: [Extensible Provisioning Protocol (EPP) Transport over QUIC](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-quic/) — This document specifies how an Extensible Provisioning Protocol (EPP)
   session is mapped onto a QUIC connection.  EPP over QUIC (EoQ)
   leverages features of the QUIC protocol.
- **draft-ietf-regext-epp-same-entity-00** (new-draft, score 0, ignored_after_review) [regext]: [Domain variant support for EPP](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-same-entity/) — This document defines an EPP extension allowing clients to learn
   about and manipulate variant groups of domains, ie. groups of domains
   whose names are equivalent in a registry-defined way and are tied to
   a single registrant.
- **draft-ietf-regext-rdap-extensions-14** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes and clarifies the usage of extensions in
   RDAP.
- **draft-ietf-regext-rdap-x-media-type-06** (new-draft, score 0, ignored_after_review) [regext]: [The "exts_list" Parameter for the RDAP Media Type](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-x-media-type/) — This document defines a new parameter for the RDAP media type that
   can be used to describe RDAP content with RDAP extensions.
   Additionally, this document describes the usage of this parameter
   with RDAP for the purposes of signalling RDAP extensions during
   content negotiation.
- **draft-ietf-roll-enrollment-priority-17** (new-draft, score 0, ignored_after_review) [roll]: [Controlling Network Enrollment in RPL networks](https://datatracker.ietf.org/doc/draft-ietf-roll-enrollment-priority/) — The Routing Protocol for Low-Power and Lossy Networks (RPL) manages
   the routing topology but lacks a mechanism to globally regulate how
   many new nodes, known as Pledges, can join a node in a 6TiSCH network
   at any given time.  Currently, Join Proxies (6LowPAN Routers) make
   local decisions about whether to facilitate a Pledge's enrollment
   based only on their immediate resources.

   This document introduces RPL extensions to ensure that enrollment
   remains orderly, prevents localized congestion at specific Join
   Proxies, and allows the network to stay within its operational
   capacity limits.
- **draft-ietf-rpp-core-00** (new-draft, score 0, ignored_after_review) [rpp]: [RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-ietf-rpp-core/) — This document describes the endpoints for the RESTful Provisioning
   Protocol, used for the provisioning and management of objects in a
   shared database.
- **draft-ietf-rpp-json-00** (new-draft, score 0, ignored_after_review) [rpp]: [JSON for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-ietf-rpp-json/) — This document defines the rules for representing the RESTful
   Provisioning Protocol (RPP) data objects, as defined in
   [I-D.ietf-rpp-data-objects], using the JavaScript Object Notation
   (JSON) Data Interchange Format [RFC8259].  It specifies how RPP
   primitive types, common data types, component objects, resource
   objects, and associations are mapped to JSON and JSON Schema, and
   provides normative JSON Schema definitions and worked examples for
   domain name, contact, and host data objects.
- **draft-ietf-rtgwg-multisegment-sdwan-14** (new-draft, score 0, ignored_after_review) [rtgwg]: [Multi-segment SD-WAN via Cloud DCs](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/) — This document describes a method for seamlessly
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
- **draft-ietf-schc-8824-update-09** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression (SCHC) for the Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/draft-ietf-schc-8824-update/) — This document defines how to compress Constrained Application
   Protocol (CoAP) headers using the Static Context Header Compression
   and fragmentation (SCHC) framework.  SCHC defines a header
   compression mechanism adapted for constrained devices, and it uses a
   static description of the header to reduce the header's redundancy
   and size.  While RFC 8724 describes the SCHC compression and
   fragmentation framework and its application for IPv6 and UDP headers,
   this document applies SCHC to CoAP headers.  The CoAP header
   structure differs from that of IPv6 and UDP headers, since CoAP uses
   a flexible header with a variable number of options that are in turn
   of variable length.  The CoAP message format is asymmetric, i.e.,
   request messages have a header format different from that of response
   messages.  This specification gives guidance on applying SCHC to
   flexible headers and on leveraging the message format asymmetry for
   defining more efficient compression Rules.  This document replaces
   and obsoletes RFC 8824.
- **draft-ietf-schc-architecture-06** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression (SCHC) Architecture](https://datatracker.ietf.org/doc/draft-ietf-schc-architecture/) — The Static Context Header Compression and fragmentation (SCHC)
   framework provides both a header compression mechanism and an
   optional fragmentation mechanism.  This document defines a minimal
   architecture for SCHC deployments, providing guidance for
   implementers and operators on the essential components and their
   interactions required for effective SCHC operation.

   The architecture defines the components of a SCHC deployment -
   Endpoints, Instances, Contexts, Sessions, and Domains - their
   management, the framing of SCHC Datagrams, and considerations for
   technology-specific profiles.
- **draft-ietf-scone-protocol-05** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-8210bis-26** (new-draft, score 0, ignored_after_review) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RFC6480) prefix origin data, Router Keys, and ASPA
   data from a trusted cache.  This document describes a protocol to
   deliver them.

   This document describes version 2 of the RPKI-Router protocol.
   [RFC6810] describes version 0, and [RFC8210] describes version 1.
   This document is compatible with both.
- **draft-ietf-sidrops-rpki-erik-protocol-05** (new-draft, score 0, ignored_after_review) [sidrops]: [The Erik Synchronization Protocol for use with the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rpki-erik-protocol/) — This document specifies the Erik Synchronization Protocol for use
   with the Resource Public Key Infrastructure (RPKI).  Erik
   Synchronization can be characterized as a data replication system
   using Merkle trees, a content-addressable naming scheme, concurrency
   control using monotonically increasing sequence numbers, and HTTP
   transport.  Relying Parties can combine information retrieved via
   Erik Synchronization with other RPKI transport protocols.  The
   protocol's design is intended to be efficient, fast, easy to
   implement, and robust in the face of partitions or faults in the
   network.
- **draft-ietf-sml-structured-quoted-content-00** (new-draft, score 0, ignored_after_review) [sml]: [Structured Quoted Content](https://datatracker.ietf.org/doc/draft-ietf-sml-structured-quoted-content/) — This document describes a machine-readable format for conveying
   quoted content in email messages.  This can be used when replying to
   or forwarding an email message.

   Structured quoted content is expected to be used in conjunction with
   conventional, human-readable quote formatting.  They are based on the
   forthcoming "structured email" specification defined in [I-D.ietf-
   sml-structured-email-03] and related drafts.
- **draft-ietf-spring-sr-policy-nrp-02** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing Policy Extension for Network Resource Partition](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-nrp/) — Segment Routing (SR) Policy is a set of candidate paths, each
   consisting of one or more segment lists and the associated
   information.  A Network Resource Partition (NRP), is a subset of the
   resources and associated policies in the underlay network.  In SR
   networks with multiple NRPs, an SR Policy can be associated with a
   particular NRP.  In that case, SR Policy can be used for steering and
   forwarding traffic which is mapped to the NRP, so that the packets
   can be processed with the subset of network resources and policy of
   the NRP for guaranteed performance.  Thus the association between SR
   Policy and NRP needs to be specified.

   This document defines extensions to the SR Policy Architecture to
   allow the association of the SR Policy candidate paths with NRPs.
- **draft-ietf-spring-srv6-service-programming-00** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 Service Programming](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-service-programming/) — This document defines data plane functionality required to implement
   service segments and achieve service programming in SRv6 networks.
- **draft-ietf-spring-stamp-srpm-mpls-03** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-spring-stamp-srpm-srv6-02** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement for SRv6 using the Simple Two-Way Active
   Measurement Protocol (STAMP), as defined in RFC 8762, along with its
   optional extensions defined in RFC 8972 and further augmented in RFC
   9503.  The described procedures are used for links and SRv6 paths
   (including Segment Lists of SRv6 Policies, SRv6 IGP best paths, and
   SRv6 IGP Flexible Algorithm paths), as well as Layer-3 and Layer-2
   services over the SRv6 paths.
- **draft-ietf-srv6ops-srv6-deployment-03** (new-draft, score 0, ignored_after_review) [srv6ops]: [SRv6 Deployment Options](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/) — When deciding to migrate a network from existing data-plane
   technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as
   VXLAN) to SRv6, common questions involve how to perform the
   migration, how to minimize impact to the existing network and what
   techniques are available to support a smooth transition.  This
   document presents various deployment and migration options for
   networks evolving toward SRv6 from prior transport or overlay
   technologies.
- **draft-ietf-tcpm-rst-diagnostic-payload-03** (new-draft, score 0, ignored_after_review) [tcpm]: [TCP RST Diagnostic Payload](https://datatracker.ietf.org/doc/draft-ietf-tcpm-rst-diagnostic-payload/) — This document specifies an experimental diagnostic payload format
   returned in TCP RST segments.  Such payloads are used to share with
   an endpoint the reasons for which a TCP connection has been reset.
   Sharing this information is meant to ease diagnostic and
   troubleshooting.

   This specification builds on provisions that are already present in
   RFC 9293 "Transmission Control Protocol (TCP)".  As such, this
   document does not require any change to RFC 9293.
- **draft-ietf-teas-5g-network-slice-application-07** (new-draft, score 0, ignored_after_review) [teas]: [IETF Network Slice Application in 3GPP 5G End-to-End Network Slice](https://datatracker.ietf.org/doc/draft-ietf-teas-5g-network-slice-application/) — Network Slicing is one of the core features of 5G defined in 3GPP,
   which provides different network service as independent logical
   networks.  To provide 5G network slices services, an end-to-end
   network slice has to span three network segments: Radio Access
   Network (RAN), Mobile Core Network (CN) and Transport Network (TN).
   This document describes the application of the IETF network slice
   framework in providing 5G end-to-end network slices, including
   network slice mapping in the management, control and data planes.
- **draft-ietf-teas-rsvp-inplace-lsp-bw-update-01** (new-draft, score 0, ignored_after_review) [teas]: [In-Place Bandwidth Update for MPLS RSVP-TE LSPs](https://datatracker.ietf.org/doc/draft-ietf-teas-rsvp-inplace-lsp-bw-update/) — This document describes the procedure for updating the bandwidth of
   an MPLS RSVP-TE Label Switched Path (LSP) tunnel in-place without
   employing make-before-break (MBB).
- **draft-ietf-tiptop-ip-architecture-01** (new-draft, score 0, ignored_after_review) [tiptop]: [An Architecture for IP in Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-ip-architecture/) — The IP protocol stacks used on Earth's Internet are typically
   configured based on assumptions of short delays and mostly
   uninterrupted communications.  This document describes an
   architecture of the IP protocol stack tailored for its use in deep
   space.  It involves buffering IP packets in IP forwarders facing
   intermittent links and adjusting transport protocol configurations
   and application protocol timers.  This architecture applies to the
   Moon, Mars, and general interplanetary networking.
- **draft-ietf-tiptop-usecase-02** (new-draft, score 0, ignored_after_review) [tiptop]: [IP in Deep Space: Key Characteristics, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-tiptop-usecase/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  Most of the IP protocol stack
   used on the Internet, in particular reliable transport protocols and
   applications, is based on the assumptions of shorter delays and
   mostly uninterrupted communications.  This document describes the key
   characteristics, use cases, and requirements for deep space
   networking, intended to help when profiling IP protocols in such
   environment.
- **draft-ietf-tsvwg-fq-pie-02** (new-draft, score 0, ignored_after_review) [tsvwg]: [Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/) — This document presents Flow Queue Proportional Integral controller
   Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue
   Management (AQM) algorithm to isolate flows and tackle the problem of
   bufferbloat.  FQ-PIE uses hashing to classify incoming packets into
   different queues and provide flow isolation.  Packets are dequeued by
   using a variant of the round robin scheduler.  Each such flow is
   managed by the PIE algorithm to maintain high link utilization while
   controlling the queue delay to a target value.
- **draft-ietf-tsvwg-l4sops-10** (new-draft, score 0, ignored_after_review) [tsvwg]: [Operational Guidance on Coexistence with Classic ECN during L4S Deployment](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/) — This document provides guidance in order to ensure successful
   deployment of Low Latency Low Loss Scalable throughput (L4S) in the
   Internet.  Other L4S documents provide guidance for running an L4S
   experiment, but this document is focused solely on potential
   interactions between L4S flows and flows using the original
   ('Classic') ECN over a Classic ECN bottleneck.  The document
   discusses the potential outcomes of these interactions, describes
   mechanisms to detect the presence of Classic ECN bottlenecks, and
   identifies opportunities to prevent and/or detect and resolve
   fairness problems in such networks.  This guidance is aimed at
   operators of end-systems, operators of networks, and researchers.
- **draft-ietf-v6ops-464xlat-optimization-06** (new-draft, score 0, ignored_after_review) [v6ops]: [464XLAT/MAT-T Optimization](https://datatracker.ietf.org/doc/draft-ietf-v6ops-464xlat-optimization/) — IP/ICMP Translation Algorithm (SIIT) can be used to provide access
   for IPv4-only hosts or applications to IPv4-only or dual-stack
   destinations over IPv6-only infrastructure.  In that case, the
   traffic flows are translated twice: first from IPv4 to IPv6
   (stateless NAT46 at the ingress point to the IPv6-only
   infrastructure) and then from IPv6 back to IPv4 (stateful NAT64, at
   the egress point).  When the destination is IPv6-enabled, the second
   translation might be avoided.  This document describes a possible
   optimization to 464XLAT and MAP-T to avoid translating IPv6 flows
   back to IPv4 if the destination is reachable over IPv6.  The proposed
   solution would significantly reduce the NAT64 utilization in the
   operator's network, increasing the performance.
- **draft-ietf-v6ops-rfc7084bis-06** (new-draft, score 0, ignored_after_review) [v6ops]: [Basic Requirements for IPv6 Customer Edge Routers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/) — This document specifies requirements for an IPv6 Customer Edge (CE)
   router.  Specifically, the current version of this document focuses
   on the basic provisioning of an IPv6 CE router and the provisioning
   of IPv6 hosts attached to it.  The document obsoletes RFC 7084.
- **draft-irtf-t2trg-security-setup-iot-devices-07** (new-draft, score 0, ignored_after_review) [t2trg]: [Terminology and processes for initial security setup of IoT devices](https://datatracker.ietf.org/doc/draft-irtf-t2trg-security-setup-iot-devices/) — This document provides an overview of terms that are commonly used
   when discussing the initial security setup of Internet of Things
   (IoT) devices.  This document also presents a brief but illustrative
   survey of protocols and standards available for initial security
   setup of IoT devices.  For each protocol, we identify the terminology
   used, the entities involved, the initial assumptions, the processes
   necessary for completion, and the knowledge imparted to the IoT
   devices after the setup is complete.
- **draft-jenkins-cnsa2-cmc-profile-03** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificate Management over CMS](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-cmc-profile/) — This document specifies a profile of the Certificate Management over
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
- **draft-jenkins-cnsa2-pkix-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificates and Certificate Revocation Lists](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-pkix-profile/) — This document specifies a profile of X.509 v3 Certificates and X.509
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
- **draft-jennings-moq-mocha-chat-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Chat: Messaging over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-chat/) — This document specifies the messaging functionality for MOCHA (MoQ
   Open Communication & Hosting Architecture).  It defines how
   participants send and receive messages in channels using MoQ
   Transport (MOQT) publish/subscribe primitives.  Each device publishes
   messages on its own track within a channel namespace, enabling
   decentralized message production with relay-based fan-out.  This
   specification covers message naming, format, causal ordering,
   delivery, roster management, and channel discovery for text-based
   chat.
- **draft-jennings-moq-mocha-meetings-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Meetings: Real-Time Conferencing over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-meetings/) — This document specifies how multi-party audio and video meetings are
   conducted using MOCHA (MoQ Open Communication & Hosting
   Architecture).  It defines namespace conventions, media track design,
   catalog distribution, and participant flows for real-time
   conferencing over MoQ Transport (MOQT).  This specification supports
   both simulcast and scalable video codec configurations, enabling
   meetings ranging from small group calls to large-scale conferences.
- **draft-jennings-moq-mocha-mls-keying-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA MLS Keying: End-to-End Encryption Key Management over MoQ](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-mls-keying/) — This document specifies MLS key management for MOCHA (MoQ Open
   Communication & Hosting Architecture).  It defines how MLS groups are
   created, how members are added and removed, how key material is
   distributed over MOQT tracks, and how the MLS Delivery Service is
   realized in a fully distributed manner using MOQT publish/subscribe.
   For large channels, Partial MLS is used to avoid requiring all
   members to process every membership change.
- **draft-jennings-moq-mocha-pab-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Personal Address Book](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-pab/) — This document defines how a set of devices owned by a common user
   synchronize a Personal Address Book (PAB) over MOQT.  The address
   book maps identities to human-readable names and contact information,
   enabling users to maintain a trusted contact list that is consistent
   across all their devices.
- **draft-jennings-moq-mocha-reactions-00** (new-draft, score 0, ignored_after_review) [none]: [MOCHA Reactions: Real-Time Reactions over MoQ Transport](https://datatracker.ietf.org/doc/draft-jennings-moq-mocha-reactions/) — This document specifies reactions for MOCHA (MoQ Open Communication &
   Hosting Architecture).  It supports message-targeted reactions (emoji
   on a specific chat message) and standalone reactions (engagement
   signals such as applause or raised hands).
- **draft-jholland-quic-multicast-09** (new-draft, score 0, ignored_after_review) [none]: [Multicast Extension for QUIC](https://datatracker.ietf.org/doc/draft-jholland-quic-multicast/) — This document defines a multicast extension to QUIC to enable the
   efficient use of multicast-capable networks to send identical data
   streams to many clients at once, coordinated through individual
   unicast QUIC connections.
- **draft-jones-httpbis-cookie-preference-00** (new-draft, score 0, ignored_after_review) [none]: [The Cookie-Preference HTTP Header Field](https://datatracker.ietf.org/doc/draft-jones-httpbis-cookie-preference/) — This document specifies a new HTTP request header field, "Cookie-
   Preference", that enables user agents to communicate the user's
   preferred cookie disposition (e.g., accept all, accept essential
   only, reject all, or ask) to web servers.  By conveying this
   preference upfront, the header can facilitate a more seamless
   browsing experience while respecting user privacy choices and
   reducing reliance on per-site consent dialogs.
- **draft-jot-bess-evpn-mcast-router-sync-00** (new-draft, score 0, ignored_after_review) [none]: [Multicast Router State Synchronization in EVPN Networks](https://datatracker.ietf.org/doc/draft-jot-bess-evpn-mcast-router-sync/) — Ethernet VPN (EVPN) networks support multicast applications in which
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
- **draft-jz-dmm-mup-evolution-00** (new-draft, score 0, ignored_after_review) [none]: [Mobile User Plane Evolution: 5G & 6G](https://datatracker.ietf.org/doc/draft-jz-dmm-mup-evolution/) — This document starts from the description of the 5G mobile user
   plane, including distributed User Plane Functions (UPFs).  Then,
   based on the 3GPP proposals for 6G UP architecture evolution, the
   draft describes some potential enhancements revolving around the
   support of the 6G UP flexiblity, scalability & resilience.  The draft
   also discusses the potential IETF work upon integrating the proposed
   enhancements of the 6G UP architecture.
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-00** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.  This document also provides guidance for use of EDNS(0)
   in signature retrieval.
- **draft-kbf-onsen-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [ONSEN Problem Statement](https://datatracker.ietf.org/doc/draft-kbf-onsen-problem-statement/) — The IETF has produced numerous YANG data models for automating the
   provisioning and delivery of network and connectivity services,
   including L2SM, L3SM, L2NM, L3NM, Attachment Circuits, and Network
   Slicing models.  Despite their wide availability, operators report
   persistent challenges in operationalizing these abstractions in a
   consistent, scalable, and automatable manner.  This document
   describes the problem space for the ONSEN Working Group, identifying
   the operational gaps and deficiencies in existing IETF service and
   network abstraction models that prevent effective end-to-end
   automation.  The problems documented here are drawn from operator
   experience and from the findings of the IAB NEMOPS Workshop.  This
   document does not propose solutions, protocols, or new data models.
- **draft-kbr-teas-mptersvp-04** (new-draft, score 0, ignored_after_review) [none]: [RSVP-TE Extensions for Multipath Traffic Engineered Directed Acyclic Graph Tunnels](https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that facilitates weighted
   load balancing of unicast traffic across a constrained set of paths
   optimized for a specific objective.

   This document describes the provisioning of an MPTED Tunnel in a TE
   network using RSVP-TE.
- **draft-kinnear-dnsop-globally-relevant-00** (new-draft, score 0, ignored_after_review) [none]: [Globally Relevant HTTPS RRs](https://datatracker.ietf.org/doc/draft-kinnear-dnsop-globally-relevant/) — DNS answers for SVCB and HTTPS resource records are typically treated
   as scoped to the network on which they were obtained.  This requires
   clients to re-resolve DNS when changing network attachments, adding
   latency to connection establishment.  This document defines a new
   SvcParamKey, "globally-relevant", for use in SVCB and HTTPS DNS
   resource records as defined in [RFC9460].  When present, this boolean
   flag indicates that the service binding parameters in the record are
   valid regardless of the client's network attachment point.  Clients
   that observe this flag can reuse cached SVCB and HTTPS records across
   network changes, subject to normal TTL expiry.
- **draft-knodel-age-arch-01** (new-draft, score 0, ignored_after_review) [none]: [Age Verification Architecture](https://datatracker.ietf.org/doc/draft-knodel-age-arch/) — This document describes solution-agnostic and technology-neutral
   schema for how various intermediaries can gate content and services
   based on age.  The analysis of the architecture is done along two
   dimensions: the efficacy of permitting or restricting access based on
   age, and the privacy cost of doing so.  The document concludes with
   recommendations as well as critical privacy, security and human
   rights considerations.
- **draft-knodel-beyond-carbon-01** (new-draft, score 0, ignored_after_review) [none]: [Impacts of the Internet on the Environment, Beyond Carbon](https://datatracker.ietf.org/doc/draft-knodel-beyond-carbon/) — The global internet is comprised of vast interconnected networks
   spanning nearly every surface of planet and sky that, together with
   user devices, consumes energy and emits greenhouse gases.  The true
   scale and proposed mitigations of the carbon footprint of the
   internet are the subject of important research.  The internet also
   requires the depletion of other natural resources beyond carbon,
   namely land, water, electromagnetic spectrum and minerals.
   Electronic waste contributes in particularly acute ways to
   environmental pollution.  This document surveys the impacts of the
   internet on the environment and includes, but goes beyond, energy use
   and carbon footprint to look at the consumption of natural resources
   and environmental waste.
- **draft-knodel-nomcom-gender-representation-03** (new-draft, score 0, ignored_after_review) [none]: [Composition and Comportment of the IETF Nominating Committee](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document addresses two complementary gaps in the operation of
   the IETF Nominating Committee (nomcom).  First, it extends the
   existing limit on nomcom representation by organization ([RFC8713],
   Section 4.17) so that not all voting members belong to the same
   gender.  Second, it proposes a comportment framework for nomcom
   members so that the nomcom conducts itself with the rigor and
   fairness expected of any committee that evaluates candidates for
   leadership roles.
- **draft-kohbrok-mls-opportunistic-channels-00** (new-draft, score 0, ignored_after_review) [none]: [Opportunistic Channels](https://datatracker.ietf.org/doc/draft-kohbrok-mls-opportunistic-channels/) — This document defines Opportunistic Channels: a way for two members
   of a Messaging Layer Security (MLS) group to efficiently create and
   operate an end-to-end encrypted 1-to-1 channel.  In contrast to a
   full MLS group, the channel participants can't independently update
   their key material.  Instead, participants opportunistically inject
   key material exported from other groups.  As such, opportunistic
   channels are more efficient than full MLS groups, but achieve lower
   security guarantees.  Their use case is the transmission of lower-
   security messages such as message delivery receipts.

   To keep messaging in opportunistic channels efficient, this document
   also defines MLS WireFormats that are equivalent to the MLS
   PublicMessage and PrivateMessage formats, but omit signatures.  These
   WireFormats are otherwise independent of opportunistic channels and
   can be used in regular MLS groups.
- **draft-kohbrok-mls-tls-01** (new-draft, score 0, ignored_after_review) [none]: [The MLS-TLS secure channel protocol](https://datatracker.ietf.org/doc/draft-kohbrok-mls-tls/) — This document details how the Messaging Layer Security (MLS) protocol
   can be combined with the Transport Layer Security (TLS) record layer
   to yield the MLS-TLS secure channel protocol.  In this composed
   protocol, MLS acts as a continuous key agreement protocol that allows
   initiator and responder to protect both past and future messages in
   case of key material compromise.  As such, MLS-TLS is suitable for
   long-lived connections.  MLS-TLS also inherits the modularity of MLS
   and can be configured with post-quantum secure ciphersuites.
- **draft-kompella-teas-mcte-00** (new-draft, score 0, ignored_after_review) [none]: [Multicast Traffic Engineering](https://datatracker.ietf.org/doc/draft-kompella-teas-mcte/) — Traffic Engineering (TE) offers a very rich toolkit for managing
   traffic flows and the paths they take in a network.  A TE network can
   have link attributes such as bandwidth, colors, risk groups and
   alternate metrics.  A TE path can use these attributes to include or
   avoid certain links, increase path diversity, manage bandwidth
   reservations, improve service experience, and offer protection paths.
   These benefits apply equally to unicast and multicast traffic.

   This memo proposes multicast traffic-engineering (MCTE), allowing the
   use of TE for multicast traffic.  MCTE is an alternative proposal to
   point-to-multipoint TE specified in [RFC4875].  The approach in
   [RFC4875] creates a separate "sub-LSP" from the source to each leaf,
   resulting in a considerable amount of signaling and state in the
   network.  MCTE, on the other hand, uses the junction approach
   proposed in MPTE [I-D.kompella-teas-mpte] to create the multicast
   tree with less signaling and state.  [RFC4875] proposes the use of
   RSVP-TE for signaling and an MPLS data plane for carrying traffic.
   MCTE allows the use of several control and data planes to signal
   tunnels and carry traffic.
- **draft-kompella-teas-mpte-03** (new-draft, score 0, ignored_after_review) [none]: [Multipath Traffic Engineering](https://datatracker.ietf.org/doc/draft-kompella-teas-mpte/) — Shortest path routing offers an easy-to-understand, easy-to-implement
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
- **draft-krierhorn-idr-upa-03** (new-draft, score 0, ignored_after_review) [none]: [BGP Unreachable Prefix Announcement (UPA)](https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/) — Summarization is often used in multi-domain networks to improve
   network efficiency and scalability.  With summarization in place,
   there is a need to signal loss of reachability to an individual
   prefix covered by the summary.  This enables fast convergence by
   steering traffic away from the node which owns the prefix and is no
   longer reachable.

   This document specifies the mechanism, referred to as Unreachable
   Prefix Announcement (UPA), for networks where BGP is used to carry
   summary routes.  It is also equally beneficial for operators to share
   the unreachable prefixes.
- **draft-kuehlewind-happy-qlog-00** (new-draft, score 0, ignored_after_review) [none]: [Happy Eyeballs v3 (HEv3) Event Logging with qlog](https://datatracker.ietf.org/doc/draft-kuehlewind-happy-qlog/) — This document specifies a qlog extension for Happy Eyeballs v3
   (HEv3), enabling logging of dual-stack and multi-protocol connection
   racing behavior.  It defines a dedicated event schema, event names,
   and data structures that capture DNS resolution timing, SVCB/HTTPS
   service discovery, candidate sorting and grouping, connection attempt
   scheduling and racing, NAT64 prefix discovery, success/failure
   outcomes, and summary metrics.
- **draft-law-moq-imsc1-msf-00** (new-draft, score 0, ignored_after_review) [none]: [IMSC1 Packaging for MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-law-moq-imsc1-msf/) — This document specifies the packaging format for delivering IMSC1
   content as Event Timeline tracks within the MOQT Streaming Format
   (MSF).
- **draft-lcmw-cats-midhaul-04** (new-draft, score 0, ignored_after_review) [none]: [Compute-Aware Traffic Steering for Midhaul Networks](https://datatracker.ietf.org/doc/draft-lcmw-cats-midhaul/) — Computing-Aware Traffic Steering (CATS) takes into account both
   computing and networking resource metrics for selecting the
   appropriate service instance to forwarding the service traffic.  This
   document described the usage of Computing-Aware Traffic Steering
   (CATS) within Midhaul (MH) networks in the O-RAN architecture.  It
   details how CATS can enhance traffic steering decisions between
   Distributed Units (DUs) and Centralized Units (CUs) by considering
   both compute resource metrics (e.g., CPU and memory utilization of CU
   instances) and network performance metrics (e.g., bandwidth, latency,
   reliability).

   The document discusses the integration of CATS with O-RAN management
   frameworks, and the interplay with the Transport Network Manager
   (TNM) in O-RAN using standard interfaces defined by IETF (as for
   example the one for Network Slice Services for connectivity
   provisioning).
- **draft-lcnc-onsen-telco-cloud-00** (new-draft, score 0, ignored_after_review) [none]: [Abstractions for Telco-Cloud Scenarios](https://datatracker.ietf.org/doc/draft-lcnc-onsen-telco-cloud/) — draft-lcnc-onsen-telco-cloud-00

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
   and network domains, building up a true Telco-Cloud approach.  It
   identifies abstraction dimensions that can simplify service
   orchestration while enabling scalable operation across heterogeneous
   network and cloud infrastructures.
- **draft-li-idr-bgp-sr-policy-bfd-extension-02** (new-draft, score 0, ignored_after_review) [none]: [BGP SR Policy Extensions for BFD Configuration](https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/) — Segment Routing (SR) Policies require fast failure detection for
   Candidate Paths (CPs) to enable rapid rerouting and high
   availability.  Currently, the provisioning of SR Policies and the
   configuration of associated Bidirectional Forwarding Detection (BFD)
   or Seamless BFD (S-BFD) sessions are performed independently.  This
   often necessitates separate mechanisms (e.g., manual configuration,
   NETCONF, or additional signaling) to associate BFD/S-BFD sessions
   with the SR Policies, resulting in complex and error-prone
   operations.

   This document defines extensions to BGP SR Policy for the
   simultaneous provisioning of SR Policy CPs and their S-BFD
   configuration parameters during policy advertisement.  The extensions
   include optional sub-TLVs within the Tunnel Encapsulation Attribute
   to carry S-BFD configuration parameters (e.g., discriminators,
   intervals, multipliers).

   These extensions simplify deployment in distributed or controller-
   based environments, reduce configuration overhead, and enhance
   operational efficiency for SR-based traffic engineering.
- **draft-li-idr-flowspec-redirect-direct-ip-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification Redirect to Directly Connected IP Address](https://datatracker.ietf.org/doc/draft-li-idr-flowspec-redirect-direct-ip/) — A bit, D bit, is defined in Flow-spec Redirect-to-IPv4 Extended
   Community and Flow-spec Redirect-to-IPv6 Extended Community.  This
   bit is used by BGP Flow Specification to indicate that the associated
   Flow Specification policy be set to an invalid state when the
   directly connected link associated with the redirect target address
   becomes unavailable.
- **draft-li-lsvr-bgp-spf-srv6-06** (new-draft, score 0, ignored_after_review) [none]: [Applying BGP-LS Segment Routing over IPv6(SRv6) Extensions to BGP-LS-SPF](https://datatracker.ietf.org/doc/draft-li-lsvr-bgp-spf-srv6/) — For network scenarios such as Massively Scaled Data Centers (MSDCs),
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
- **draft-liao-ace-est-c509-01** (new-draft, score 0, ignored_after_review) [none]: [EST for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-ace-est-c509/) — This document defines Enrollment over Secure Transport (EST) protocol
   operations over HTTPS for use with C509 certificates.  The operations
   specified in this document support CA certificate distribution, C509
   certificate enrollment, C509 certificate re-enrollment, and server-
   side key generation using C509 certificates.  This document also
   defines operations for Certificate Revocation List (CRL)
   distribution.
- **draft-lin-grow-bmp-peer-interface-02** (new-draft, score 0, ignored_after_review) [none]: [Extension for BMP Peer Interface](https://datatracker.ietf.org/doc/draft-lin-grow-bmp-peer-interface/) — This document proposes extending BMP to allow BMP messages with the
   per-peer header to carry interface information for the established
   peer session, especially in order to distinguish parallel link-local
   and unnumbered BGP peers established based on distinct interfaces.
- **draft-lin-idr-bgp-ecmp-ebgp-enhancements-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Enhancements for ECMP EBGP Scenarios](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-ecmp-ebgp-enhancements/) — This document proposes extensions to BGP to apply the RFC 5004 route
   persistence algorithm across parallel EBGP sessions and to suppress
   unnecessary advertisements between EBGP peers in the same AS.

   This document updates RFC 5004.
- **draft-lin-idr-cats-flowspec-ts-05** (new-draft, score 0, ignored_after_review) [none]: [BGP Flowspec for Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-lin-idr-cats-flowspec-ts/) — A BGP Flow Specification is an n-tuple consisting of several matching
criteria that can be applied to IP traffic. Computing-Aware Traffic
Steering (CATS) is a framework which optimizes traffic steering to a
given service instance by taking into account the dynamic nature of
both computing and network resources. This document specifies a new BGP
Flow Spec Component Type in order to support CATS traffic forwarding.
- **draft-lin-idr-flowspec-quic-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification for QUIC](https://datatracker.ietf.org/doc/draft-lin-idr-flowspec-quic/) — A BGP Flow Specification is an n-tuple consisting of several
   matching criteria that can be applied to IP traffic. This document
   defines how to perform Flow Specification traffic diversion based on
   the characteristics of QUIC packets.
- **draft-lin-spring-srv6-aware-context-indicator-08** (new-draft, score 0, ignored_after_review) [none]: [SRv6 Context Indicator SIDs for SR-Aware Services](https://datatracker.ietf.org/doc/draft-lin-spring-srv6-aware-context-indicator/) — A context indicator provides the context on how to process the
   packet for service nodes. This document describes how to use SRv6
   SIDs as context indicator for SR-aware services. The corresponding
   Endpoint behaviors are defined.
- **draft-liu-6man-aggregate-header-limit-problem-05** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement with Aggregate Header Limit for IPv6](https://datatracker.ietf.org/doc/draft-liu-6man-aggregate-header-limit-problem/) — This document first proposes the concept of "Aggregate header limit
   for IPv6"(IPv6-AHL) to indicate the total header size that a router
   is able to process at full forwarding rate for IPv6 packets.  Then
   this document describes the problems for path calculation and
   function enablement without the awareness of IPv6-AHL, and the
   considerations for IPv6-AHL collection are also included.
- **draft-liu-cadi-01** (new-draft, score 0, ignored_after_review) [none]: [Cryptographic Asset Discovery and Inventory](https://datatracker.ietf.org/doc/draft-liu-cadi/) — This document compiles existing Cryptographic Asset Discovery and
   Inventory (CADI) methods and analyze potential gaps.
- **draft-liu-grow-bmp-multiple-peer-header-02** (new-draft, score 0, ignored_after_review) [none]: [Definition for BMP Multiple Peer Header](https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/) — This document proposes a format of multiple peer header for
   aggregating BMP messages.  It can be used to compress multiple BMP
   messages with per-peer header into one aggregated BMP message, which
   could reduce the amount of reported BMP messages and reduce network
   overhead.
- **draft-liu-grow-bmp-rm-aggregated-06** (new-draft, score 0, ignored_after_review) [none]: [Definition for Aggregated BMP Route Monitoring Message](https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/) — This document proposes an aggregated BMP Route Monitoring message
   based on the BMP Multi-Peer Header message (draft-liu-grow-bmp-
   multiple-peer-header).  It can compress multiple BMP Route Monitoring
   messages into one aggregated BMP Route Monitoring message to reduce
   the amount of reported BMP Route Monitoring messages and reduce the
   network overhead.
- **draft-liu-opsawg-ipfix-mpls-mna-01** (new-draft, score 0, ignored_after_review) [none]: [Export of MPLS Network Action (MNA) Information in IPFIX](https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-mpls-mna/) — This document introduces new IPFIX IEs for exporting MPLS Network
   Action (MNA) information in IPFIX, covering both in-stack and post-
   stack MNAs.
- **draft-liu-rtgwg-adaptive-routing-notification-03** (new-draft, score 0, ignored_after_review) [none]: [Adaptive Routing Notification for Load-balancing](https://datatracker.ietf.org/doc/draft-liu-rtgwg-adaptive-routing-notification/) — In this document, adaptive routing is referred to as a technology
   that makes dynamic traffic forwarding decisions based on changes in
   traffic load and network topology, devices with adaptive routing
   capabilities can dynamically select the outport in the forwarding
   table based on the congestion condition of the outport or downstream
   link.  This document focuses on the information carried in (Adaptive
   Routing Notification)ARN messages and how they are delivered and
   processed in the network.
- **draft-liu-srv6ops-bfd-srv6-policy-encap-00** (new-draft, score 0, ignored_after_review) [none]: [Operational Considerations for BFD Encapsulation in SRv6 Policy](https://datatracker.ietf.org/doc/draft-liu-srv6ops-bfd-srv6-policy-encap/) — Bidirectional Forwarding Detection (BFD) mechanisms can be used for
   fast detection of failures in the forwarding path of SR Policy.

   This document describes the Operational Guidance for BFD
   Encapsulation in SRv6 Policy.

   The BFD packets may be encapsulated in Insert-mode or Encaps-mode.
- **draft-lp-idr-bgp-algorithm-01** (new-draft, score 0, ignored_after_review) [none]: [Advertisement of Algorithm in BGP](https://datatracker.ietf.org/doc/draft-lp-idr-bgp-algorithm/) — This document proposes extensions to BGP to support algorithm-based
   end-to-end path establishment.
- **draft-ls-idr-bgp-ls-service-metadata-09** (new-draft, score 0, ignored_after_review) [none]: [Distribution of Service Metadata in BGP-LS](https://datatracker.ietf.org/doc/draft-ls-idr-bgp-ls-service-metadata/) — In edge computing, a service may be deployed on multiple instances
   within one or more sites, called edge service.  The edge service is
   associated with an ANYCAST address in the IP layer, and the route of
   it with potential service metadata will be distributed to the
   network.  The Edge Service Metadata can be used by ingress routers to
   make path selections not only based on the routing cost but also the
   running environment of the edge services.

   The service route with metadata can be collected by a PCE(Path
   Compute Element) or an analyzer for calculating the best path to the
   best site/instance.  This draft describes a mechanism to collect
   information of the service routes and related service metadata in
   BGP-LS.
- **draft-mahy-cbor-pointer-01** (new-draft, score 0, ignored_after_review) [none]: [CBOR Pointer: Selecting Elements of Concise Binary Object Representation (CBOR) Documents](https://datatracker.ietf.org/doc/draft-mahy-cbor-pointer/) — CBOR Pointer is a syntax to identify a single CBOR value from a CBOR
   document with an arbitrarily complex nested structure.  It is
   analogous to JSON Pointer.
- **draft-mahy-mimi-credential-preauth-00** (new-draft, score 0, ignored_after_review) [none]: [MIMI Preauthorization based on deep references to MLS Credentials](https://datatracker.ietf.org/doc/draft-mahy-mimi-credential-preauth/) — This document describes a Work-In-Progress syntax called claim
   pointers that identify specific items in structured credentials,
   which often have nested levels of hierarchy; and claim matchers that
   facilitate comparisons between items in credentials and a target
   value.  It also describes a new version of the More Instant Messaging
   Interoperability (MIMI) preauthorization format using claim pointers
   and claim matchers.
- **draft-many-bess-rfc9252-dual-sid-00** (new-draft, score 0, ignored_after_review) [none]: [Dual MPLS and SRv6 Service Advertisement in the Absence of Transposition](https://datatracker.ietf.org/doc/draft-many-bess-rfc9252-dual-sid/) — RFC 9252 defines BGP signaling procedures for SRv6 services,
   including the use of an MPLS Label field and transposition semantics.
   However, when transposition is not used (i.e., TL = 0), RFC 9252 does
   not explicitly define the interpretation of the MPLS Label field,
   leading to ambiguity in control-plane signaling.

   This document specifies a minimal, backward-compatible extension to
   RFC 9252 that enables a single route to unambiguously advertise both
   a valid MPLS Service Label and an SRv6 Service SID.  The extension
   relies on existing MPLS label semantics, without introducing new
   TLVs, attributes, or changes to the base encoding format.
- **draft-many-tiptop-quic-profile-03** (new-draft, score 0, ignored_after_review) [none]: [QUIC Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-quic-profile/) — Deep space communications involve long delays (e.g., the Earth to
   Mars one-way delay is ~4-20 minutes) and often intermittent
   communications.  In this context, the default transport parameters of
   QUIC stacks, tuned for the terrestrial Internet, are not suitable for
   deep space.  This document defines a QUIC profile for deep space.  It
   provides guidance on how to estimate and set transport parameters,
   advice to space mission operators and application developers on how
   to configure QUIC for the deep space use case, and guidance to QUIC
   stack developers on properly exposing the required transport
   parameters in their API.
- **draft-mazilu-tcpm-packet-trimming-00** (new-draft, score 0, ignored_after_review) [none]: [TCP Packet Trimming Extension](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) — This document specifies a TCP extension that enables TCP endpoints in
   data center networks or similarly controlled administrative domains
   to use packet trimming information when it is available.  When switch
   buffers exceed a threshold, rather than silently dropping a packet,
   the switch trims the payload and forwards the header.  This allows
   the destination to issue a deterministic Negative Acknowledgment
   (NACK), enabling faster, more deterministic loss recovery.
- **draft-mdt-quic-explicit-measurements-05** (new-draft, score 0, ignored_after_review) [none]: [Application of Explicit Measurement Techniques for QUIC Troubleshooting](https://datatracker.ietf.org/doc/draft-mdt-quic-explicit-measurements/) — This document defines a protocol that can be used by QUIC endpoints
   to signal packet loss in a way that can be used by network devices to
   measure and locate the source of the loss.

   Discussion of this work is encouraged to happen on the QUIC IETF
   mailing list quic@ietf.org (mailto:quic@ietf.org) or on the GitHub
   repository which contains the draft: https://github.com/igorlord/
   draft-mdt-quic-explicit-measurements (https://github.com/igorlord/
   draft-mdt-quic-explicit-measurements).
- **draft-melegassi-ippm-mvps-gddp-00** (new-draft, score 0, ignored_after_review) [none]: [Geometric Dilution of Detection Precision for Multi-Vantage Path Snapshots](https://datatracker.ietf.org/doc/draft-melegassi-ippm-mvps-gddp/) — GPS positioning accuracy degrades with anchor geometry; the effect
   is quantified by the well-known Geometric Dilution of Precision
   (GDOP).  Multi-vantage anomaly detection systems face the DUAL
   problem: how does anchor geometry affect DETECTION SENSITIVITY
   rather than localisation accuracy?

   This document formalises Geometric Dilution of Detection Precision
   (GDDP) for the Multi-Vantage Path Snapshot (MVPS) framework
   [I-D.melegassi-ippm-mvps-bundle].  The minimum displacement that
   a multi-vantage detector can reliably distinguish from measurement
   noise is NOT a single number: it is an anisotropic scalar field
   d*(v, theta) over the Earth's surface, governed by the geometry of
   the anchor set relative to each vantage.

   Three main results are proved:

   (1) GDDP Theorem (T-GDDP-1): d*(v, theta) admits a closed-form
       expression in terms of the Fisher Information of the anchor-
       to-vantage RTT-ratio vector.  The directional detection threshold
       is d*(theta) = sqrt(chi2_crit / I(theta)), where I(theta) is
       the Fisher Information in direction theta.  This is the
       Cramer-Rao bound applied to detection.

   (2) Anisotropy Lemma (L-GDDP-2): every vantage has a "blind cone"
       -- a set of directions in which displacement barely changes the
       RTT-ratio vector and detection sensitivity degrades.  The blind
       cone is quantifiable and, for isolated vantages, can span over
       70% of the compass.

   (3) Monotonicity Theorem (T-GDDP-3): adding an anchor NEVER reduces
       the Fisher Information of the system (Shannon chain rule applied
       to detection channels).  There exists a principled anchor-
       placement optimisation: minimise max_theta d*(v, theta) over
       candidate sites.

   All three are validated to three layers of proof: canonical (math),
   empirical (deterministic scripts, seed=1337), and real data (RIPE
   Atlas measured RTTs, 92,067 D-squared values from 40 probes, 11/11
   checks PASS).  No simulation-only claim is made.

   The GDDP/GDOP duality has not, to the author's knowledge, been
   previously formalised.  VerLoc (Kohls and Diaz, USENIX Security
   2022) observes the directional effect empirically but does not derive
   d*(v, theta) or propose a geometric defence.
- **draft-melegassi-mvps-ddos-resilience-02** (new-draft, score 0, ignored_after_review) [none]: [Volume-Independent DDoS Detection via Coherence-BFD: The MVPS DDoS Resilience Profile](https://datatracker.ietf.org/doc/draft-melegassi-mvps-ddos-resilience/) — This document specifies how the Multi-Vantage Path Synchrony
   (MVPS) framework [I-D.melegassi-ippm-mvps-bundle] and its
   sub-tick variant Coherence-BFD
   [I-D.melegassi-coherence-bfd] detect volumetric and
   distributed Denial-of-Service (DDoS) attacks in time bounded
   by (M-1)*T_tick, INDEPENDENT of the attack rate in packets-
   per-second or bits-per-second.

   Three theorems are proved:

      Theorem D1 (Volume-Independence).  Detection latency is a
      function of the control-tick period T_tick and the
      M-multiplier confirmation count alone; it does not grow
      with attack volume.

      Theorem D2 (Distributed-Attack Bound).  The framework
      detects up to floor((k-1)/2) simultaneous regional
      attacks under cell-aware minimax aggregation, where k is
      the number of coherence cells.

      Theorem D3 (Broker NIC Sizing).  Under the three
      architectural invariants of Section 3, broker NIC sizing
      is independent of attack volume; it is determined only
      by the legitimate telemetry packets-per-second.

   This revision (-02) adds seven confirmed real-world
   DDoS detections using a causally-direct methodology:
   BGP updates measured on each VICTIM'S OWN announced
   prefix (not on unrelated third-party infrastructure).

     (a) 7 independently confirmed DDoS attacks across
         3 continents (Australia, South Africa, New
         Zealand), spanning two orders of magnitude in
         target size (from a major OS vendor to a small
         22-year-old regional host): VentraIP (600 Gbps),
         Canonical (3.5 Tbps), Binary Lane (400 Gbps),
         Network Platforms (676 Gbps), Xneelo (300 Gbps),
         SiteHost NZ, and 1-Grid (100 Gbps).  30 of 33
         tested prefixes (91%) alarmed on the confirmed
         attack day; 4 of 7 targets show 100% prefix
         corroboration.

     (b) VentraIP: BGP alarm fired the SAME HOUR as
         attack onset (00:00 UTC, D^2=11.7), four hours
         BEFORE mitigation began.  Canonical: BGP alarm
         fired 2 hours BEFORE Cloudflare migration began.

     (c) Joint statistical significance across all 7
         targets (multi-prefix binomial test):
         P < 5.9*10^-60 under the null hypothesis that
         alarms are unrelated to attack timing -- 52
         orders of magnitude beyond the 5-sigma particle-
         physics discovery threshold.

     (d) Volume-independence (D1) confirmed: 1-Grid
         (100 Gbps) produced a HIGHER D^2 (63.2) than
         Canonical (3500 Gbps, D^2=10.6).  Detection
         depends on coherence deformation, not attack
         bandwidth.

     (e) An invalid claim from an intermediate draft
         (RIPE Atlas K-root time-coincidence implying
         53.6-hour pre-report detection) was identified
         via a Monte Carlo control test as a look-
         elsewhere/base-rate artifact and RETRACTED
         (Section 7.7.1), then replaced with the
         causally-direct results above.
- **draft-miao-rtgwg-satellite-routing-reqs-00** (new-draft, score 0, ignored_after_review) [none]: [Scenarios and Routing Requirements for Mega-Constellation LEO Satellite Networks](https://datatracker.ietf.org/doc/draft-miao-rtgwg-satellite-routing-reqs/) — With the rapid maturation of laser Inter-Satellite Link (ISL)
   technologies, Low Earth Orbit (LEO) mega-constellations are evolving
   from bent-pipe relay networks dependent on dense Ground Stations (GS)
   into highly autonomous spaceborne routing networks.  Traditional
   terrestrial routing protocols and their variants, such as Global
   Link-State Routing Architectures, rely on a globally consistent link-
   state view and a global convergence paradigm, which are fundamentally
   incompatible with the high dynamics, time-variant topologies, and
   frequent link disruptions characteristic of ten-thousand-node scale
   satellite networks.  This document describes core routing scenarios
   including non-dense ground deployment and inter-continental transit,
   analyzes the engineering infeasibility of global convergence
   protocols in space environments, reviews the limitations of existing
   mitigation approaches, and specifies key requirements for satellite
   routing protocols centered around localized autonomy and distributed
   decision-making.
- **draft-miyatoch-teas-actn-inter-operator-extension-00** (new-draft, score 0, ignored_after_review) [none]: [ACTN Extensions for Inter-Operator Coordination](https://datatracker.ietf.org/doc/draft-miyatoch-teas-actn-inter-operator-extension/) — This document specifies an extension to the ACTN framework (RFC 8453)
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
- **draft-nandakumar-moq-tempo-00** (new-draft, score 0, ignored_after_review) [none]: [TEMPO: Timing Extension for Media Playout Orchestration over MoQ](https://datatracker.ietf.org/doc/draft-nandakumar-moq-tempo/) — This document defines TEMPO (Timing Extension for Media Playout
   Orchestration), a synchronized playout mechanism for media tracks
   delivered over the Media over QUIC Transport (MoQT) protocol.  The
   Original Publisher stamps each object with when it should be played
   out and when it was sent.  Relays replace the send-time stamp with
   their own clock as they forward, giving each subscriber a fresh
   timing reference from its nearest relay.  Subscribers use these
   timestamps to decide when to render each object, and report their
   sync state directly to a coordination server (PlaySyncServer) that
   can tell the media publisher to adjust timing when subscribers fall
   behind.
- **draft-nbcuong-mkv-block-cipher-00** (new-draft, score 0, ignored_after_review) [none]: [Encryption algorithms - Block cipher MKV](https://datatracker.ietf.org/doc/draft-nbcuong-mkv-block-cipher/) — This document specifies the MKV block cipher for use in cryptographic
   mechanisms supporting information security.  The algorithm may be
   used to provide confidentiality of information during transmission,
   processing, and storage in information systems.

About This Document

   This note is to be removed before publishing as an RFC.
- **draft-nygren-dnsop-domain-delegation-validation-00** (new-draft, score 0, ignored_after_review) [none]: [Domain Control Validation for DNS Delegations](https://datatracker.ietf.org/doc/draft-nygren-dnsop-domain-delegation-validation/) — The techniques specified in
   [I-D.draft-ietf-dnsop-domain-verification-techniques] for using the
   DNS to verify ownership or control of a domain in the Domain Name
   System (DNS) rely on the domain already being properly delegated to a
   DNS authority.  For the specific case where the Application Service
   Provider is providing authoritative DNS services, the existing
   approaches don't provide a way to bootstrap domain validation onto a
   new Authoritative DNS Application Service provider.

   This specification proposes a mechanism for "Domain Control
   Validation" for cases where the User and DNS Administrator are
   validating control over a domain to an Authoritative DNS Application
   Service Provider and thus do not have the ability to add records
   within the domain.  In this case, validation must be performed by the
   User taking actions in the DNS Registrar or Parent Zone that
   demonstrate control over the domain, such as by adding DNS NS records
   as validation records.
- **draft-nygren-dnsop-ipv6only-indicator-00** (new-draft, score 0, ignored_after_review) [none]: [Indicating IPv6-only SVCB Endpoints and IPv4 Deprecation in the DNS](https://datatracker.ietf.org/doc/draft-nygren-dnsop-ipv6only-indicator/) — As the DNS is the primary mechanism for translating from hostnames to
   IP addresses, it is a logical place to signal that endpoints are
   IPv6-only.  It is thus also a logical place to signal that legacy
   endpoints supporting IPv4 are being deprecated.  This specification
   introduces two SvcParams for SVCB-compatible RR types that signal
   IPv6-only endpoints (ipv6only) as well as deprecated endpoints
   (deprecated).

   TO BE REMOVED: This document is being collaborated on in Github at:
   https://github.com/enygren/draft-nygren-dnsop-ipv6only-indicator
   (https://github.com/enygren/draft-nygren-dnsop-ipv6only-indicator).
   The most recent working version of the document, open issues, etc.
   should all be available there.  The authors (gratefully) accept pull
   requests.
- **draft-nygren-httpbis-http11-request-binding-01** (new-draft, score 0, ignored_after_review) [none]: [HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding](https://datatracker.ietf.org/doc/draft-nygren-httpbis-http11-request-binding/) — HTTP/1.1 Message Binding adds new hop-by-hop header fields that are
   cryptographically bound to requests and responses.  The use of this
   protocol is negotiated out-of-band from the HTTP datastream, and keys
   can be communicated either in-band in the first request or out-of-
   band (such as via TLS Exporters).  These header fields allow
   endpoints to detect and mitigate desynchronization attacks, such as
   HTTP Request Smuggling, that exist due to datastream handling
   differences.
- **draft-oiwa-path-characteristics-service-01** (new-draft, score 0, ignored_after_review) [none]: [Secure Hybrid Network Monitoring - Path Characteristics Service](https://datatracker.ietf.org/doc/draft-oiwa-path-characteristics-service/) — "Secure hybrid network monitoring – Problem statement"
   [I-D.oiwa-secure-hybrid-network] identifies challenges in securing
   and monitoring networks deployed across hybrid and mixed cloud
   environments.  This document introduces the Path Characteristics
   Service (PCS), a service that enables applications and operators to
   verify whether a given network path conforms to their declared
   requirements ("intent") regarding security, compliance, and
   operational properties.  Unlike traditional network monitoring, PCS
   does not expose raw network state; instead, it evaluates the user's
   intent against the actual path characteristics and returns a
   conformance result (match or no-match).  This intent matching
   approach allows multi-stakeholder environments to verify path
   properties without disclosing sensitive internal infrastructure
   details.  This document describes an architecture and interfaces for
   PCS; it expresses recommended behaviors and constraints using the
   normative keywords of BCP 14, but does not specify a wire protocol or
   its encoding.
- **draft-oiwa-secure-hybrid-network-03** (new-draft, score 0, ignored_after_review) [none]: [Secure hybrid network monitoring - Problem statement](https://datatracker.ietf.org/doc/draft-oiwa-secure-hybrid-network/) — This document presents a problem statement and gap analysis for
   ensuring and monitoring the security status of networks operating in
   complex environments, such as hybrid and multi-cloud systems.  It
   identifies a missing capability: verifying the path and security
   properties of communications across multiple administrative domains
   while preserving each provider's confidentiality and local policy
   boundaries.  The document also outlines, non-normatively, potential
   solution directions.
- **draft-pamtv-netconf-error-registries-01** (new-draft, score 0, ignored_after_review) [none]: [Error List and Error Identities Registries for YANG-driven protocols](https://datatracker.ietf.org/doc/draft-pamtv-netconf-error-registries/) — This document defines IANA registries for the YANG Protocol Error
   List and YANG Protocol Error Identities.
- **draft-pan-transparent-ordered-bonding-00** (new-draft, score 0, ignored_after_review) [none]: [Transparent Ordered Bonding for High-Capacity WAN Links](https://datatracker.ietf.org/doc/draft-pan-transparent-ordered-bonding/) — This document describes a Transparent Ordered Bonding (TOB) mechanism
   for high-capacity wide-area links that are physically composed of
   multiple lower-rate member links.  Traditional flow-based load
   balancing mechanisms can preserve packet ordering, but they cannot
   fully utilize all member links for a single large traffic stream.

   TOB introduces a bonding layer between two adjacent network nodes.
   The bonding layer fragments ingress packets into cells, distributes
   them across member links according to link status, and reassembles
   them in strict order at the remote node.  This document specifies the
   applicability, architecture, packet format, scheduling
   considerations, and resequencing behavior of TOB.
- **draft-pang-cats-fallback-decision-framework-00** (new-draft, score 0, ignored_after_review) [none]: [CATS Fallback Decision Framework](https://datatracker.ietf.org/doc/draft-pang-cats-fallback-decision-framework/) — This document describes the framework and considerations for fallback
   decision-making in Computing-Aware Traffic Steering (CATS).  While
   existing OAM frameworks provide multi-dimensional telemetry
   collection capabilities, how the CATS Path Selector (C-PS) should
   react to partial or transient failures remains an open issue.  This
   document highlights the problems of misjudgment due to correlated
   failures, steering flapping, and non-deterministic fallback
   behaviors.  It outlines the high-level considerations for logical
   decoupling of status dimensions and stable state transition
   mechanisms to ensure carrier-grade reliability.  Specific protocol
   extensions and algorithm implementations will be explored in future
   revisions based on working group discussions.
- **draft-pang-nmop-kg-for-traffic-monitoring-analysis-03** (new-draft, score 0, ignored_after_review) [none]: [Knowledge Graph for Network Traffic Monitoring and Analysis](https://datatracker.ietf.org/doc/draft-pang-nmop-kg-for-traffic-monitoring-analysis/) — This document extends the knowledge graph framework specifically to
   the traffic management domain, demonstrating how knowledge graphs can
   address long-standing traffic management challenges through semantic
   integration and automated reasoning.
- **draft-petra-green-api-04** (new-draft, score 0, ignored_after_review) [none]: [Path Energy Traffic Ratio API (PETRA)](https://datatracker.ietf.org/doc/draft-petra-green-api/) — This document describes an API to query a network regarding its
   Energy Traffic Ratio for a given path.
- **draft-piraux-space-constellation-code-02** (new-draft, score 0, ignored_after_review) [none]: [A code to describe satellite constellations](https://datatracker.ietf.org/doc/draft-piraux-space-constellation-code/) — When considering a satellite constellation forming a non-terrestrial
   network, the characteristics of this constellation heavily influence
   the network topology it forms.  To improve the analysis of such non-
   terrestrial networks across various tools developed by the network
   community, this document defines a constellation code to describe
   common orbital shell patterns, and specification formats to describe
   inter-satellite link topologies and ground stations, covering the
   Core and Ground Networks of a constellation.  In addition, this
   document may serve as an introduction to satellite constellations for
   IETF participants.
- **draft-pskim-ros2-quic-mqtt-00** (new-draft, score 0, ignored_after_review) [none]: [QUIC Application for ROS2 with MQTT](https://datatracker.ietf.org/doc/draft-pskim-ros2-quic-mqtt/) — While DDS (Distributed Data Service) protocol, managed by Object
   Management Group (OMG), for ROS (Robot Operating System) 2 is
   intended to provide a universal communication layer,
   interoperability across different DDS middleware implementations is
   not always consistent. Variations in transport protocol usage (e.g.,
   TCP/IP, UDP, shared memory) can hinder direct data exchange, and
   cross-domain communication efficiency is generally lower compared to
   protocols such as HTTP. Therefore, to resolve limitations of DDS in
   ROS2, this draft considers a couple of standards protocols, QUIC of
   IETF and MQTT (Message Queuing Telemetry Transport), managed by
   OASIS Open.
- **draft-qin-bmwg-rpki-rp-bench-01** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for RPKI Relying Party](https://datatracker.ietf.org/doc/draft-qin-bmwg-rpki-rp-bench/) — This document defines a benchmarking methodology for evaluating RPKI
   Relying Party (RP) implementations in controlled laboratory
   environments.  The methodology focuses on whether RP implementations
   correctly perform required validation steps and on the performance of
   these operations.  RP implementations are treated as black boxes,
   enabling consistent and objective assessment based on externally
   observable behavior rather than internal design or implementation
   details.
- **draft-rabnic-bess-evpn-mcast-eeg-07** (new-draft, score 0, ignored_after_review) [none]: [EVPN Multicast Forwarding for EVPN to EVPN Gateways](https://datatracker.ietf.org/doc/draft-rabnic-bess-evpn-mcast-eeg/) — This document proposes an EVPN (Ethernet Virtual Private Network)
   extension to allow IP multicast forwarding on Service Gateways that
   interconnect two or more EVPN domains.
- **draft-ranjbar-regext-rdap-subordinate-referrals-00** (new-draft, score 0, ignored_after_review) [none]: [Redirecting RDAP Queries to Holder-Designated Servers for Subordinate Resources](https://datatracker.ietf.org/doc/draft-ranjbar-regext-rdap-subordinate-referrals/) — Registration Data Access Protocol (RDAP) queries can be resolved from
   the IANA bootstrap registries down to the most specific object held
   by a registry operator's RDAP service.  Where the holder of a
   registered resource maintains registration data for resources
   subordinate to it, such as DNS names below a registered domain or
   more-specific networks below an address allocation, and operates a
   conformant RDAP service for that data, there is currently no
   discoverable referral from the registry's response to the holder's
   service.  This document describes an optional, holder-designated
   referral for subordinate resources, building on the explicit redirect
   mechanism defined for RDAP.  It is written as input to draft-ietf-
   regext-rdap-referrals and its content may be merged into that
   document.
- **draft-rly-savnet-inter-domain-as-relationships-07** (new-draft, score 0, ignored_after_review) [none]: [Inter-domain Source Address Validation based on AS relationships](https://datatracker.ietf.org/doc/draft-rly-savnet-inter-domain-as-relationships/) — This draft introduces a distributed inter-domain source address
   validation scheme based on AS relationships named AS Relationship
   Based Inter-domain Filtering (ARBIF).  It primarily describes this
   method from seven aspects: a brief introduction to the scheme, an
   overview of the AS relationship classification and acquisition
   methods, the architecture of the ARBIF system, implementation based
   on BGP extension, typical use cases, experiments of ARBIF, and
   considerations for deployability.
- **draft-robert-mls-slim-01** (new-draft, score 0, ignored_after_review) [none]: [SlimMLS](https://datatracker.ietf.org/doc/draft-robert-mls-slim/) — This document defines SlimMLS, an extension to the Messaging Layer
   Security (MLS) protocol for reducing wire and per-client storage
   overhead in groups that use ciphersuites with large public keys,
   ciphertexts, signatures, and credentials.  SlimMLS replaces many
   large objects that appear in MLS authenticated or transcript-hashed
   structures with typed hash references.  Clients resolve the
   referenced objects only when needed, using a per-message carrier, a
   local cache, or an application-specific retrieval channel.  The
   extension is most useful when an independent Delivery Service can
   assist with retrieval and per-recipient delivery, although local
   caching and delayed fetching also help without such assistance.
   SlimMLS defines slim variants of KeyPackage, Commit, Welcome,
   GroupInfo, and message framing.  When placing a signature outside an
   encrypted envelope would reveal the signer, SlimMLS keeps the
   signature inside the ciphertext.
- **draft-rosomakho-tls-ecdhe-mlkem512-00** (new-draft, score 0, ignored_after_review) [none]: [Post-quantum hybrid ECDHE-MLKEM512 Key Agreement for TLSv1.3](https://datatracker.ietf.org/doc/draft-rosomakho-tls-ecdhe-mlkem512/) — This document defines two post-quantum hybrid key exchange groups for
   TLS 1.3 that combine ML-KEM-512 with ECDHE: MLKEM512X25519 and
   SecP256r1MLKEM512.  These groups provide lower-overhead hybrid key
   exchange options for deployments where ClientHello size,
   fragmentation risk, constrained-device performance, or compatibility
   with existing network infrastructure are important considerations.
   The groups defined in this document are intended for use with TLS 1.3
   and DTLS 1.3 and follow the hybrid key exchange construction used by
   ECDHE-MLKEM key agreement for TLS 1.3.
- **draft-saad-teas-rsvpte-ip-tunnels-03** (new-draft, score 0, ignored_after_review) [none]: [IP RSVP-TE: Extensions to RSVP for P2P IP-TE LSP Tunnels](https://datatracker.ietf.org/doc/draft-saad-teas-rsvpte-ip-tunnels/) — This document describes the use of RSVP (Resource Reservation
   Protocol), including all the necessary extensions, to establish
   Point-to-Point (P2P) Traffic Engineered IP (IP-TE) Label Switched
   Path (LSP) tunnels for use in native IP forwarding networks.

   This document defines specific extensions to the RSVP protocol to
   allow the establishment of explicitly routed IP paths using RSVP as
   the signaling protocol.  The result is the instantiation of an IP
   path which can be automatically routed away from network failures,
   congestion, and bottlenecks.  This document also defines
   considerations for using these extensions in networks that support
   SRv6.
- **draft-sahib-dnsop-survey-dcv-techniques-00** (new-draft, score 0, ignored_after_review) [none]: [A Survey of Domain Control Validation Techniques using DNS](https://datatracker.ietf.org/doc/draft-sahib-dnsop-survey-dcv-techniques/) — [I-D.draft-ietf-dnsop-domain-verification-techniques] describes best
   practices for using the DNS to verify ownership or control of a
   domain, a process generally referred to as "Domain Control
   Validation".  This document is a companion survey that catalogs the
   DNS-based Domain Control Validation techniques in use today across a
   range of Application Service Providers and protocols.
- **draft-schinazi-httpbis-ohttp-ext-key-config-00** (new-draft, score 0, ignored_after_review) [none]: [An Extensible Key Configuration Format for Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-ext-key-config/) — Oblivious HTTP is a protocol for forwarding encrypted HTTP messages.
   This requires communicating the gateway's key configuration to
   clients.  While a key configuration media type was defined for this
   purpose, it has some limitations such as the inability to convey key
   lifetimes and interoperability issues.  This document defines a
   similar extensible key configuration format that addresses those
   issues.
- **draft-schinazi-httpbis-ohttp-pfs-00** (new-draft, score 0, ignored_after_review) [none]: [A Perfect Forward Secure Extension to Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-pfs/) — Oblivious HTTP (OHTTP) is a protocol for forwarding encrypted HTTP
   messages.  It does not provide Perfect Forward Secrecy (PFS).
   Chunked OHTTP expands OHTTP to be suitable for longer-lived streams,
   but still does not offer PFS.  Combined, this is leading sensitive
   traffic to de deployed at scale without PFS.  This document proposes
   a solution.
- **draft-smyslov-lamps-frodokem-certificates-03** (new-draft, score 0, ignored_after_review) [none]: [Internet X.509 Public Key Infrastructure - Algorithm Identifiers for FrodoKEM](https://datatracker.ietf.org/doc/draft-smyslov-lamps-frodokem-certificates/) — FrodoKEM is an unstructured lattice-based Key Encapsulation Mechanism
   (KEM).  Compared to ML-KEM, FrodoKEM is considered as having more
   conservative design.  This document specifies the conventions for
   using FrodoKEM in X.509 Public Key Infrastructure.  The conventions
   for the subject public keys and private keys are also specified.
- **draft-smyslov-tls-ext-ext-00** (new-draft, score 0, ignored_after_review) [none]: [Extending Limit on Extensions Size in TLS 1.3](https://datatracker.ietf.org/doc/draft-smyslov-tls-ext-ext/) — Protocol TLS 1.3 is widely used to protect traffic in the Internet.
   However, the format of the TLS 1.3 ClientHello, ServerHello, and
   EncryptedExtensions handshake messages limits the size of extensions
   to 64 Kbytes.

   This specification extends TLS 1.3 to allow extensions in
   ClientHello, ServerHello, and EncryptedExtensions have size larget
   than 64 Kbytes.
- **draft-song-idr-flowspec-classid-filter-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Flow Specification by ClassID](https://datatracker.ietf.org/doc/draft-song-idr-flowspec-classid-filter/) — BGP Flowspec mechanism (BGP-FS) [RFC8955] [RFC8956] propagates both
   traffic Flow Specifications and Traffic Filtering Actions by making
   use of the BGP NLRI and the BGP Extended Community encoding formats.

   This document specifies a new BGP-FS component type named ClassID to
   support ClassID filtering.
- **draft-sullivan-tls-signed-ech-updates-02** (new-draft, score 0, ignored_after_review) [none]: [Authenticated ECH Config Distribution and Rotation](https://datatracker.ietf.org/doc/draft-sullivan-tls-signed-ech-updates/) — Encrypted ClientHello (ECH) requires clients to have the server's ECH
   configuration before connecting.  Currently, when ECH fails, servers
   can send updated configurations but clients cannot authenticate them
   unless the server has a valid certificate for the public name,
   limiting deployment flexibility.

   This document specifies a new mechanism for authenticating ECH
   configurations.  Servers include additional information in their
   initial ECH configurations, which enables clients to authenticate
   updated configurations without relying on a valid certificate for the
   public name.
- **draft-sullivan-tls-xof-ciphers-00** (new-draft, score 0, ignored_after_review) [none]: [TLS 1.3 Cipher Suites with Alternative Key-Schedule Profiles](https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-ciphers/) — TLS 1.3 builds its key schedule on HKDF over the cipher suite's hash.
   This document defines TLS 1.3 cipher suites that build it on a deck
   function over a single permutation instead, the one a deployment
   already carries when it uses SHA-3, ML-KEM, or ML-DSA.  One
   permutation then runs the whole schedule, and a full handshake takes
   about a third of the permutation calls an HKDF schedule over that
   permutation would.  Such a cipher suite names an AEAD algorithm
   together with a schedule profile that defines every key-schedule
   function the connection uses.  The profile follows from the
   negotiated cipher suite alone, so no new extension is defined and the
   TLS 1.3 state machine and wire format are unchanged.  Two profiles
   are defined, one on the standard SHA-3 function and one on a faster
   reduced-round variant of it.
- **draft-sun-ssh-composite-sigs-03** (new-draft, score 0, ignored_after_review) [none]: [Composite ML-DSA Signatures for SSH](https://datatracker.ietf.org/doc/draft-sun-ssh-composite-sigs/) — This document describes the use of PQ/T composite signatures for the
   Secure Shell (SSH) protocol.  The composite signatures described
   combine ML-DSA as the post-quantum part and the elliptic curve
   signature schemes ECDSA, Ed25519 and Ed448 as the traditional part.
- **draft-taylor-dtn-bibe-00** (new-draft, score 0, ignored_after_review) [none]: [Bundle-in-Bundle Encapsulation](https://datatracker.ietf.org/doc/draft-taylor-dtn-bibe/) — This document describes Bundle-in-Bundle Encapsulation (BIBE), a
   Delay-Tolerant Networking (DTN) Bundle Protocol (BP) tunneling
   mechanism by which a bundle is carried as the payload of one or more
   encapsulating bundles, allowing security measures, routing policy,
   and protocol version translation to be applied to the encapsulating
   bundle without modification of the encapsulated bundle.  The protocol
   includes an optional segmentation mechanism, allowing a large
   encapsulated bundle to be carried in multiple encapsulating bundles.
- **draft-templin-6man-fwiw-05** (new-draft, score 0, ignored_after_review) [none]: [Fragmentation Revisited: For What It's Worth](https://datatracker.ietf.org/doc/draft-templin-6man-fwiw/) — Internet Protocol (IP) fragmentation and reassembly have served as
   core elements of the architecture from the very earliest days but
   they have been subject to negative publicity by studies that have
   declared them "harmful" and "fragile".  These warning labels have
   resonated deeply within the community in a way that fosters the
   enemies of sound engineering: fear, uncertainty and doubt.  This
   document revisits IP fragmentation and shows that a properly
   engineered alternative IPv6 solution is both practical and necessary
   to provide a robust service for the future of Internetworking.
- **draft-templin-6man-ipid-ext2-28** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Extended Fragment Header (EFH)](https://datatracker.ietf.org/doc/draft-templin-6man-ipid-ext2/) — The Internet Protocol, version 4 (IPv4) header includes a 16-bit
   Identification field in all packets, but this length is too small to
   ensure reassembly integrity even at moderate data rates in modern
   networks.  Even for Internet Protocol, version 6 (IPv6), the 32-bit
   Identification field included when a Fragment Header is present may
   be smaller than desired for some applications.  Both IPv4 and IPv6
   fragmentation have further been classified as fragile to the point
   that their use is discouraged.  This specification addresses these
   limitations by defining an IPv6 Extended Fragment Header (EFH) that
   includes a 64-bit Identification in the context of more robust,
   secure and efficient fragmentation and reassembly procedures.
- **draft-templin-intarea-ipid-ext2-11** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Extended Fragment Header for IPv4](https://datatracker.ietf.org/doc/draft-templin-intarea-ipid-ext2/) — The Internet Protocol, version 4 (IPv4) header includes a 16-bit
   Identification field in all packets, but this length is too small to
   ensure reassembly integrity even at moderate data rates in modern
   networks.  Even for Internet Protocol, version 6 (IPv6), the 32-bit
   Identification field included when a Fragment Header is present may
   be smaller than desired for some applications.  This specification
   addresses these limitations by adapting the IPv6 Extended Fragment
   Header for IPv4.
- **draft-tiloca-core-group-oscore-kem-00** (new-draft, score 0, ignored_after_review) [none]: [Using Quantum-Resistant Key Encapsulation Mechanisms (KEMs) in the Pairwise Mode of Group Object Security for Constrained RESTful Environments (Group OSCORE)](https://datatracker.ietf.org/doc/draft-tiloca-core-group-oscore-kem/) — Group communication for the Constrained Application Protocol (CoAP)
   can be protected end-to-end by using the security protocol Group
   Object Security for Constrained RESTful Environments (Group OSCORE).
   The pairwise mode of Group OSCORE provides authenticated encryption
   of CoAP messages, by means of symmetric keys that two group members
   establish only among themselves to achieve pairwise secure
   communication.  This document defines the use of quantum-resistant
   Key Encapsulation Mechanisms (KEMs) as Pairwise Key Agreement
   Algorithm of Group OSCORE, enabling post-quantum secure derivation of
   the symmetric keys used in the pairwise mode.  The Group Manager
   facilitates the exchange of KEM public keys and KEM ciphertexts among
   group members.
- **draft-tiloca-t2trg-sw-update-groupcomm-02** (new-draft, score 0, ignored_after_review) [none]: [Distribution of Software Updates with End-to-End Secure Group Communication and Block-Wise Transfer for CoAP](https://datatracker.ietf.org/doc/draft-tiloca-t2trg-sw-update-groupcomm/) — This document defines a method for efficiently distributing a
   software update to multiple target devices, by using end-to-end
   secure group communication over UDP and IP multicast.  To this end,
   the defined method relies on a number of building blocks developed in
   the Constrained RESTful Environments (CoRE) Working Group of the
   IETF.  Those especially include the Constrained Application Protocol
   (CoAP), Block-wise transfers for CoAP, and the end-to-end security
   protocol Group Object Security for Constrained RESTful Environments
   (Group OSCORE).  The method defined in this document is compatible
   with (but not dependent on) the architecture for software and
   firmware update developed in the Software Updates for Internet of
   Things (SUIT) Working Group of the IETF.
- **draft-tojens-diem-arch-visual-aid-00** (new-draft, score 0, ignored_after_review) [none]: [DIEM Architecture Example](https://datatracker.ietf.org/doc/draft-tojens-diem-arch-visual-aid/) — This document defines the architecture for Digital Emblems.
   Standards that define Digital Emblems are expected to do so by
   mapping their mechanisms to the required and optional componented
   defined by this document.
- **draft-tong-idr-bgp-ls-sav-rule-05** (new-draft, score 0, ignored_after_review) [none]: [Advertising SAV Rule-related Information using BGP Link-State](https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/) — This document proposes extensions to the BGP Link-State protocol for
   advertising Source Address Validation (SAV) rule-related information
   for monitoring and management purposes.
- **draft-venaas-pim-ipv4-in-ipv6-core-01** (new-draft, score 0, ignored_after_review) [none]: [Native IPv4 multicast in IPv6 Core using PIM](https://datatracker.ietf.org/doc/draft-venaas-pim-ipv4-in-ipv6-core/) — This document describes how PIM Sparse-Mode can be used to construct
   IPv4 multicast trees across an IPv6-only network core.  This allows
   forwarding of native IPv4 multicast data packets.  The document
   specifies how to send and receive IPv4 PIM messages with IPv6
   headers, using a new well-known link-local IPv6 multicast address,
   and the use of RPF vectors for reachability.
- **draft-vroonen-idr-bgp-bestpath-nh-selection-03** (new-draft, score 0, ignored_after_review) [idr]: [BGP best path next-hop selection enhancements](https://datatracker.ietf.org/doc/draft-vroonen-idr-bgp-bestpath-nh-selection/) — BGP [RFC4271] has originally been designed to carry IPv4 routing
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
- **draft-wang-cats-green-challenges-08** (new-draft, score 0, ignored_after_review) [none]: [Green Challenges in Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-wang-cats-green-challenges/) — As mobile edge computing networks sink computing tasks from cloud
   data centers to the edge of the network, tasks need to be processed
   by computing resources close to the user side.  Therefore, CATS was
   raised.  Reducing carbon footprint is a major challenge of our time.
   Networks are the main enablers of carbon reductions.  The
   introduction of computing dimension in CATS makes it insufficient to
   consider the energy saving of network dimension in the past, so the
   green for CATS based on network and computing combination is worth
   exploring.  This document outlines a series of challenges and
   associated research to explore ways to reduce carbon footprint and
   reduce network energy based on CATS.
- **draft-wang-grow-bmp-policy-preview-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Route Policy Pre-view and Intent Verification Using BGP Monitoring Protocol](https://datatracker.ietf.org/doc/draft-wang-grow-bmp-policy-preview/) — Deploying BGP route policies in live production networks carries
   significant operational risks, often resulting in unintended route
   leaks, suboptimal routing paths, or blackholes.  This document
   proposes an extension to the BGP Monitoring Protocol (BMP) that
   enables a BGP speaker to pre-view and dry-run a candidate route
   policy within a localized control-plane sandbox.  The resulting post-
   policy route changes (deltas) are streamed asynchronously to a
   centralized controller via a new BMP message type.  This architecture
   allows the controller to verify policy alignment with network
   intents, subsequently triggering either an explicit commit or a
   rollback before any forwarding plane changes take effect.
- **draft-wang-space-computing-consideration-01** (new-draft, score 0, ignored_after_review) [none]: [Consideration for Space-Based Computing Infrastructure Network](https://datatracker.ietf.org/doc/draft-wang-space-computing-consideration/) — This document presents considerations for a Space-Based Computing
   Infrastructure Network from use cases and requirements.
- **draft-wang-token-aware-usecases-requirements-00** (new-draft, score 0, ignored_after_review) [none]: [Token Service Flow Awareness: Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-wang-token-aware-usecases-requirements/) — This document outlines the use cases and requirements for token
   service flow awareness, providing the IETF working group with a
   standardized reference to better support the assurance of the user’s
   end-to-end experience.
- **draft-watal-srv6ops-srv6-sfc-deployment-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6 Service Function Chaining Deployment](https://datatracker.ietf.org/doc/draft-watal-srv6ops-srv6-sfc-deployment/) — This document describes the deployment and operational experience of
   the SRv6 Service Function Chaining (SFC) architecture defined in
   [I-D.draft-watal-spring-srv6-sfc-sr-aware-functions] on an academic
   IPv6 backbone network.

   The deployed system integrates SRv6 forwarding, service function
   management, topology collection, path computation, and flow
   classification to enable dynamic provisioning of SFC services via a
   web-based management interface.

   This document summarizes the deployment architecture, operational
   workflow, experience, and lessons learned, and provides guidance for
   network operators deploying SRv6 SFC services.
- **draft-wendt-stir-cert-tn-attr-ext-00** (new-draft, score 0, ignored_after_review) [none]: [TN Attribute Certificate Extension for STI Certificates](https://datatracker.ietf.org/doc/draft-wendt-stir-cert-tn-attr-ext/) — This document specifies a non-critical X.509 v3 certificate extension
   that conveys a set of self-asserted attributes describing the
   telephone numbers identified in the certificate's TNAuthList.  The
   attributes are declared by the holder of the certificate about its
   own telephone numbers and require no separate authority token,
   because they describe or constrain only those numbers and grant no
   authority to any other party.  The extension defines an extensible
   framework with an IANA registry of attribute types and seeds that
   registry with four types: a PASSporT Placement Service (PPS) URI, a
   do-not-originate indication, a do-not-originate-messaging indication,
   and a set of authorized originating providers.  Relying parties use
   these self-declarations as policy signals, treating communications
   that do not conform to them as candidates for blocking.  The
   mechanism is backward compatible with existing STIR certificates.
- **draft-westerlund-schc-compute-address-00** (new-draft, score 0, ignored_after_review) [none]: [SCHC Compute-Address Compression/Decompression Actions for Dynamically Assigned IP Addresses](https://datatracker.ietf.org/doc/draft-westerlund-schc-compute-address/) — This document defines new Matching Operators (MOs) and Compression/
   Decompression Actions (CDAs) for the Static Context Header
   Compression and fragmentation (SCHC) framework defined in RFC 8724.
   These extensions enable efficient compression of dynamically assigned
   IP addresses, including IPv4 addresses assigned via DHCP, IPv6
   prefixes learned through SLAAC or DHCPv6, IPv6 Interface Identifiers
   (IIDs), and IPv6 temporary privacy addresses generated per RFC 8981.

   The mechanism relies on both the compressor and decompressor sharing
   knowledge of the set of addresses assigned to the device.  Addresses
   are organized into deterministically sorted tables, allowing
   compression to a small index value.  For temporary IPv6 addresses, a
   synchronized generation algorithm enables compression to an epoch and
   counter value.
- **draft-white-intarea-reordering-04** (new-draft, score 0, ignored_after_review) [none]: [Proposal for Updates to Guidance on Packet Reordering](https://datatracker.ietf.org/doc/draft-white-intarea-reordering/) — Several link technology standards mandate that equipment guarantee
   in-order delivery of layer 2 frames, apparently due to a belief that
   this is required by higher layer protocols.  To meet this requirement
   they implement a "resequencing" operation to restore the original
   packet order.  This can introduce delays that result in net
   degradation of performance.  Modern TCP and QUIC implementations
   support features that significantly improve their tolerance to out-
   of-order delivery.  This draft is intended to provide new information
   for layer 2 technology standards regarding the need to assure in-
   order delivery to support IETF protocols.
- **draft-wilaw-moq-scte35-event-timeline-00** (new-draft, score 0, ignored_after_review) [none]: [SCTE35 transmission over MSF Event Timeline](https://datatracker.ietf.org/doc/draft-wilaw-moq-scte35-event-timeline/) — Defines the transmission of SCTE 35 data over MSF Event Timeline
   tracks.
- **draft-wilaw-moq-webvtt-msf-00** (new-draft, score 0, ignored_after_review) [none]: [WebVTT Packaging for MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-wilaw-moq-webvtt-msf/) — This document specifies the JSON packaging format for delivering
   WebVTT caption and subtitle content as event timeline tracks within
   the MOQT Streaming Format (MSF).
- **draft-wkumari-dnsop-localroot-bcp-07** (new-draft, score 0, ignored_after_review) [none]: [Populating resolvers with the root zone](https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/) — DNS recursive resolver operators need to provide the best service
   possible for their users, which includes providing an operationally
   robust and privacy protecting service.  Challenges to these
   deployment goals include difficulty of getting responses from the
   root servers (such as during a network attack), longer-than-desired
   round-trip times to the closest DNS root server, and privacy issues
   relating to queries sent to the DNS root servers.  Resolvers can
   solve all of these issues by simply serving an already cached a copy
   of the full root zone.

   This document shows how resolvers can fetch, cache and maintain a
   copy of the root zone, how to detect if the contents becomes stale,
   and procedures for handling error conditions.

   { Editor note: This document contains a FAQ section.  It will help
   answer questions about why this document is not a BCP but still has
   BCP in the name, how and why this document differs from RFC8806, etc
   etc etc.  The FAQ section is intended to be removed before
   publication. }
- **draft-wullink-rpp-jscontact-profile-01** (new-draft, score 0, ignored_after_review) [none]: [JSContact Profile for RESTful Provisioning Protocol (RPP)](https://datatracker.ietf.org/doc/draft-wullink-rpp-jscontact-profile/) — This document defines a JSContact usage profile, conforming to the
   rules described in [I-D.ietf-calext-jscontact-profiles], for the
   RESTful Provisioning Protocol (RPP).  The JSContact Profile for RPP
   specifies how the JSContact format defined in [RFC9982] can be used
   as a standardized representation of contact information within RPP
   operations, enabling interoperability and consistency across RPP
   implementations that manage contact data.
- **draft-xf-pce-cats-service-02** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Computing-Aware Traffic Steering (CATS) Service](https://datatracker.ietf.org/doc/draft-xf-pce-cats-service/) — The CATS (Computing-Aware Traffic Steering) can steer traffic between
   clients of a service and sites offering the service.  The C-PS may be
   deployed as a PCE and the ingress CATS-Router could be viewed as a
   PCC.  This document proposes the PCEP extensions for selecting and
   distributing the paths for CATS services.
- **draft-xiong-detnet-flow-aggregation-05** (new-draft, score 0, ignored_after_review) [none]: [Framework for Flow Aggregation in Scaling Deterministic Networking (DetNet)](https://datatracker.ietf.org/doc/draft-xiong-detnet-flow-aggregation/) — This document provides a framework and requirements for flow
   aggregation in scaling Deterministic Networking (DetNet)
   [I-D.ietf-detnet-scaling-requirements].  It describes aggregation
   scenarios, benefits, and challenges in scaling networks, and derives
   high-level requirements applicable across different DetNet data plane
   technologies.  The framework also discusses flow aggregation
   enhancement considerations including classification, identification,
   coordination, admission control and resource allocation.  As an
   illustrative example, it explores how these concepts could apply to
   5GS systems acting as logical DetNet nodes.  This document is
   informational and complementary to existing DetNet specifications.
- **draft-xu-idr-bgp-sec-sync-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Extension for Secure Session State Synchronization](https://datatracker.ietf.org/doc/draft-xu-idr-bgp-sec-sync/) — This document defines a new BGP Address Family, termed the Secure
   Session Synchronization Address Family, allowing BGP speakers to
   exchange stateful firewall, NAT, and IPSec session information across
   distributed nodes.  This architecture facilitates zero-packet-loss
   failover and seamless path protection for Secure SD-WAN, SASE, and
   SSE multi-POP deployments, entirely bypassing the scalability limits
   of traditional layer-2 synchronization protocols.
- **draft-xu-lsvr-midr-use-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Use Cases and Requirements for Multi-Domain and Hybrid Overlay/Underlay BGP-SPF (LSVR)](https://datatracker.ietf.org/doc/draft-xu-lsvr-midr-use-cases/) — This document presents use cases and the routing requirements they
   imply for operating the BGP Link State (BGP-LS) Shortest Path First
   (SPF) routing developed in the Link-State Vector Routing (LSVR)
   Working Group, across multiple administrative domains and over hybrid
   overlay/underlay topologies.  After motivating the work, it describes
   three scenarios of increasing complexity: a single overlay domain,
   the interconnection of multiple overlay domains, and hybrid overlay/
   underlay networks.  Each scenario gives the topology, its
   distinguishing challenges, and the requirements that follow.  The
   scenarios arise in globally distributed edge- and cloud-Point-of-
   Presence (PoP) deployments that serve performance-sensitive
   applications such as cross-region real-time communication,
   collaborative productivity, cloud gaming, and large-scale SaaS.
- **draft-yan-opsawg-ipfix-energy-consumption-02** (new-draft, score 0, ignored_after_review) [none]: [Export of Energy Consumption Information in IPFIX](https://datatracker.ietf.org/doc/draft-yan-opsawg-ipfix-energy-consumption/) — This document introduces new IPFIX IEs for exporting energy
   consumption information of physical entities in a network device.
   New Information Elements are defined to report instantaneous and
   average energy consumption information at device, line-card, and port
   granularity.
- **draft-yang-nmrg-a2a-nm-03** (new-draft, score 0, ignored_after_review) [none]: [Applicability of A2A to the Network Management](https://datatracker.ietf.org/doc/draft-yang-nmrg-a2a-nm/) — This document discusses the applicability of A2A protocol to the
   network management in the multi-domain heterogeneous network
   environment that utilizes IETF technologies.  It explores operational
   aspect, key components, generic workflow and deployment scenarios.
   The impact of integrating A2A into the network management system is
   also discussed.
- **draft-yang-pce-pcep-over-quic-05** (new-draft, score 0, ignored_after_review) [none]: [PCEP over QUIC](https://datatracker.ietf.org/doc/draft-yang-pce-pcep-over-quic/) — This document specifies the use of QUIC streams to implement the PCEP
   protocol for efficient and secure data transmission.
- **draft-yi-idr-bgp-fs-edge-service-metadata-06** (new-draft, score 0, ignored_after_review) [none]: [Distribution of Service Metadata in BGP FlowSpec](https://datatracker.ietf.org/doc/draft-yi-idr-bgp-fs-edge-service-metadata/) — In edge computing and distributed cloud environments, a service may
   be deployed on multiple instances across one or more sites, referred
   to as an edge service.  The edge service is typically associated with
   an ANYCAST IP address.  With the emergence of Computing-Aware Traffic
   Steering (CATS) requirements, there is a growing need to consider
   both network and computing metrics when making traffic steering
   decisions.  Traditional routing protocols lack the capability to
   convey compute-related information, necessitating extensions to
   existing protocols.

   This draft defines a mechanism to distribute service routes along
   with computing-related metadata using BGP FlowSpec.  The service
   metadata, including compute resource status and performance metrics,
   can be collected by a central controller, processed, and then
   distributed to ingress routers using BGP FlowSpec extensions.  This
   enables ingress routers to make path selections based not only on
   routing cost but also on the running environment and resource
   availability of edge services, thereby optimizing Quality of
   Experience (QoE).  The mechanism is aligned with the CATS
   architecture and metric framework by allowing the advertised metadata
   to represent either selected original service metrics or an
   aggregated Level 2 (L2) metric.
- **draft-ymbk-lsvr-l3nd-01** (new-draft, score 0, ignored_after_review) [none]: [Layer-3 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ymbk-lsvr-l3nd/) — Data Centers where the topology is BGP-based need to discover
   neighbor IP addressing, IP Layer-3 BGP neighbors, etc.  This Layer-3
   Neighbor Discovery protocol identifies BGP neighbor candidates.
- **draft-ymbk-lsvr-l3nd-ulpc-01** (new-draft, score 0, ignored_after_review) [none]: [L3ND Upper-Layer Protocol Configuration](https://datatracker.ietf.org/doc/draft-ymbk-lsvr-l3nd-ulpc/) — This document adds PDUs to the Layer-3 Neighbor Discovery protocol to
   communicate the parameters needed to exchange inter-device Upper
   Layer Protocol Configuration for upper-layer protocols such as the
   BGP family.
- **draft-yu-idr-bgp-sr-policy-orf-00** (new-draft, score 0, ignored_after_review) [none]: [On-Demand Distributing BGP SR Policy Using Outbound Route Filtering Capability](https://datatracker.ietf.org/doc/draft-yu-idr-bgp-sr-policy-orf/) — The BGP SR Policy address family defines a mechanism to distribute
   Segment Routing (SR) policies from a centralized controller to head-
   end routers.  However, pre-provisioning all candidate SR Policies
   across massive-scale networks impose significant control-plane memory
   and processing overhead on edge nodes.  This document specifies an
   extension to the BGP Outbound Route Filtering (ORF) capability,
   leveraging the framework defined in RFC 5291.  It introduces a new SR
   Policy Tuple ORF type that allows a head-end router to precisely
   request or subscribe to specific SR Policies based on a Color and
   Endpoint tuple, enabling pure on-demand, pull-based policy
   distribution.
- **draft-zcz-nmrg-digitaltwin-data-collection-05** (new-draft, score 0, ignored_after_review) [none]: [Data Collection Requirements and Technologies for Network Digital Twin](https://datatracker.ietf.org/doc/draft-zcz-nmrg-digitaltwin-data-collection/) — A Network Digital Twin is a virtual representation of a real network,
   which is meant to be used by a management system to analyze,
   diagnose, emulate, and then control the real network based on data,
   models, and interfaces.  The construction and state update of a
   Network Digital Twin requires obtaining real-time information of the
   physical network it represents (i.e., telemetry data).  This document
   aims to describe the data collection requirements and provide data
   collection methods or tools to build the data repository for building
   and updating a network digital twin.
- **draft-zdz-teas-5g-slice-ipextension-00** (new-draft, score 0, ignored_after_review) [none]: [Carrying 5G Network Slice Identifiers in IP Headers for QoS Assurance Beyond the 3GPP-Managed Domain](https://datatracker.ietf.org/doc/draft-zdz-teas-5g-slice-ipextension/) — 3GPP defines 5G network slicing as an end-to-end service spanning the
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
- **draft-zhao-anima-automatic-congestion-relief-01** (new-draft, score 0, ignored_after_review) [none]: [Automatic Network Congestion Relief](https://datatracker.ietf.org/doc/draft-zhao-anima-automatic-congestion-relief/) — This document describes an automatic network congestion relief
   mechanism for congestion caused by sudden capacity reduction, such as
   fiber failures.  The mechanism uses traffic modeling, real-time
   congestion monitoring, policy generation, policy propagation, traffic
   regulation, and policy reversion to redistribute selected traffic
   from a congested plane to a lightly loaded paired plane.  The
   objective is to reduce manual intervention, shorten congestion
   mitigation time, and improve network resilience during failure
   conditions.
- **draft-zhao-grow-bgp-graceful-degradation-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Graceful Degradation Under Control Plane Memory Pressure](https://datatracker.ietf.org/doc/draft-zhao-grow-bgp-graceful-degradation/) — This document describes an operational framework for graceful
   degradation of BGP under control-plane memory pressure.  When BGP
   speakers experience rapid growth in routing state due to route
   flapping, configuration errors, or anomalous route injection,
   control-plane memory can become exhausted, leading to session resets,
   routing process restarts, or device reboots.

   The framework described in this document progressively reduces BGP
   route admission and processing based on local resource conditions,
   isolates non-critical neighbors or services when necessary, and
   restores routing state in a controlled manner after recovery.  The
   objective is to preserve basic device operation and reduce service
   impact.  This document does not define any new BGP messages, path
   attributes, capabilities, or protocol state machines.
- **draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib-01** (new-draft, score 0, ignored_after_review) [none]: [Enhancement for Monitoring VRF's Loc-RIB](https://datatracker.ietf.org/doc/draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib/) — BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer
   Address value of a VPN route information to zero, and sets the Peer
   Distinguisher value of a VPN route information to the route
   distinguisher or unique locally defined value of the particular
   instance the Loc-RIB belongs to.  This document introduces the option
   to communicate the Remote VRF Information from which a VPN route was
   received when reporting that VPN route information with BMP Loc-RIB.
- **draft-zhuang-idr-epe-rg-ixp-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Egress Peer Engineering (EPE) SID Allocation and Extensions for IXP Route-Server Scenarios](https://datatracker.ietf.org/doc/draft-zhuang-idr-epe-rg-ixp/) — BGP Egress Peer Engineering (EPE) defines mechanisms to steer egress
   traffic towards a specific border router, interface, or peer group
   using Segment Routing (SR).  [RFC9086] specifies BGP-LS extensions to
   advertise these EPE peer segments.  However, in Internet Exchange
   Point (IXP) deployments where border routers peer with a centralized
   Route-Server (RS), control plane peerings are completely decoupled
   from data plane forwarding paths.

   This document specifies the architecture, specific procedures, and
   associated BGP-LS TLV application guidelines for allocating and
   signaling EPE PeerNode and PeerSet SIDs on an egress border router
   connected to an IXP Route-Server infrastructure, ensuring granular
   and deterministic egress traffic engineering across IXP fabrics.
- **draft-zhuang-idr-rr-dual-nexthop-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Route Reflector Dual-Next-Hop Reflection for Path Protection](https://datatracker.ietf.org/doc/draft-zhuang-idr-rr-dual-nexthop/) — This document specifies a mechanism where a BGP Route Reflector (RR)
   reflects a single received BGP route as two distinct routing updates
   towards a target client.  By preserving the original client next-hop
   in one update and modifying the next-hop to the RR's own address in
   the second update, the receiving client obtains two parallel paths
   for the same prefix.  This enables the receiving client to implement
   Load Balancing or Primary-Backup path protection without requiring
   full-mesh IBGP sessions or BGP Add-Path extensions.
- **draft-zwg-rtgwg-enhanced-bgp-resilience-01** (new-draft, score 0, ignored_after_review) [none]: [Enhanced BGP Resilience](https://datatracker.ietf.org/doc/draft-zwg-rtgwg-enhanced-bgp-resilience/) — According to the base BGP specification, a BGP speaker that receives
   an UPDATE message containing a malformed attribute is required to
   reset the session over which the offending attribute was received.
   RFC7606 revises the error handling procedures for a number of
   existing attributes.  The use of the "treat-as-withdraw" and
   "attribute discard" approaches significantly reduces the likelihood
   of BGP sessions being reset when receiving malformed BGP update
   messages, thereby greatly enhancing network stability.  However, in
   practical applications, there are still numerous instances where BGP
   session oscillations occur due to the receipt of malformed BGP update
   messages, unrecognized attribute fields, or routing rules generated
   by a certain BGP AFI/SAFI that affect the forwarding of BGP messages.

   This document introduces some approaches to enhance the stability of
   BGP sessions.
- **draft-zzhang-fann-router-info-00** (new-draft, score 0, ignored_after_review) [none]: [Advertising Router Information](https://datatracker.ietf.org/doc/draft-zzhang-fann-router-info/) — This document specifies a generic mechanism for a router to advertise
   some information to its neighbors.  One use case of this mechanism is
   to advertise link/path information so that a receiving router can
   better react to network changes.

## Errors / fetch failures

_None._
