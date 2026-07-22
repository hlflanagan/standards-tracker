# IETF Identity + AI Standards Watch

Date: 2026-07-22

## Read now

- **draft-kamimura-vap-framework-01** (new-draft, score 27, trust_infrastructure) [none]: [Verifiable AI Provenance Framework (VAP): An Architectural Framework for Evidentiary-Grade AI Decision Trails](https://datatracker.ietf.org/doc/draft-kamimura-vap-framework/) — Automated decision-making systems, including AI and algorithmic
   systems in critical infrastructure, currently lack standardized
   mechanisms for producing evidentiary-grade provenance records that
   can withstand independent verification.  Traditional logging
   approaches fail to provide the cryptographic guarantees required for
   regulatory compliance, forensic investigation, and cross-
   organizational accountability.

   This document describes the Verifiable AI Provenance Framework (VAP),
   an architectural framework that defines requirements for producing
   verifiable decision trails using existing IETF security technologies.
   VAP does not define new protocols or cryptographic primitives;
   rather, it provides an architectural coordination layer that enables
   domain-specific profiles to leverage Supply Chain Integrity,
   Transparency and Trust (SCITT), Remote Attestation Procedures (RATS),
   CBOR Object Signing and Encryption (COSE), and related IETF work in a
   consistent manner.

   This document is intended to frame the problem space and facilitate
   discussion about whether architectural coordination work is needed in
   this area.
- **draft-munoz-wimse-authorization-evidence-01** (new-draft, score 25, core_identity) [none]: [Signed Authorization-Evidence Records for WIMSE-Authorized AI Agent Actions](https://datatracker.ietf.org/doc/draft-munoz-wimse-authorization-evidence/) — This document specifies a companion profile to the AI Agent
   Authentication and Authorization draft [I-D.klrc-aiagent-auth],
   defining a signed authorization-evidence record produced by WIMSE-
   authorized AI agent actions.  The evidence record (referred to as a
   Permit) cryptographically commits to the canonical bytes of the
   request authorized before dispatch and, via a paired Closure Record,
   to the recorded dispatched-request digest; it maps to and can satisfy
   the audit minimum requirements enumerated in Section 11 of the
   companion draft, and composes with HTTP Message Signatures, OAuth
   access tokens, and Shared Signals Framework eventing without
   requiring modifications to those existing standards.  The profile is
   anchored in the SCITT profile defined in
   [I-D.munoz-scitt-permit-profile].

   This revision also describes how WIMSE deployments compose with
   authorization-lineage evidence defined by the companion SCITT
   profile: workload identity, delegated subject context, runtime token
   claims, and HTTP Message Signature coverage become Verifier inputs
   for parent/child Permit relationships.
- **draft-pidlisnyi-aps-03** (new-draft, score 24, authorization) [none]: [Agent Passport System (APS): Verifiable Agent Identity, Faceted Authority, and Signed Action Receipts](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/) — This document specifies the Agent Passport System (APS), a protocol
   for identifying AI agents, attenuating delegated authority, and
   producing signed evidence at policy-enforcement boundaries.  APS
   defines Ed25519 agent passports; separately signed principal
   bindings; delegation chains that cannot widen across scope, spend,
   depth, time, reputation, values, or reversibility; deterministic
   action and decision references; and a common envelope for signed
   action receipts.  It also defines bindings for Model Context Protocol
   tool calls and imported OAuth identity-assertion authorization
   grants.  Verification results keep cryptographic integrity, signer
   authority, referenced-artifact resolution, policy semantics, and
   external truth separate.  An Implementation Status section identifies
   the exact coverage and maturity of the available open-source
   implementations.
- **draft-capobianco-ncfed-00** (new-draft, score 23, core_identity) [none]: [The NetClaw-to-NetClaw Federation Protocol (NCFED)](https://datatracker.ietf.org/doc/draft-capobianco-ncfed/) — This document specifies the NetClaw-to-NetClaw Federation Protocol
   (NCFED), an implementation-agnostic application-layer protocol that
   lets independently operated, heterogeneous AI network-engineering
   agents ("NCFED peers", or "claws") discover one another's
   capabilities, invoke remote tools, and delegate tasks over long-lived
   TCP sessions.  Although named for its reference instantiation, NCFED
   is a wire specification, not an SDK, and federates arbitrary
   autonomous agent architectures across distinct administrative
   boundaries; a peer needs no knowledge of its counterparty's internal
   reasoning framework, prompt structure, or execution runtime.  NCFED
   multiplexes its federation channel with BGP-4 and an associated
   tunneling data plane on a single listening port, using first-octet
   protocol discrimination.  Its payload is JSON-RPC 2.0, onto which
   Model Context Protocol (MCP) tool-invocation semantics and
   Agent2Agent (A2A) task-delegation semantics are mapped.  Federation
   between different trust domains (eN2N) requires mutual operator
   consent; within a single operator's trust domain (iN2N) it is hub-
   and-spoke, bootstrapped by an enrollment token.  For eN2N, the
   channel is encrypted with TLS 1.3 and each peer is cryptographically
   authenticated by proof of possession of the credential bound to its
   identity, under either a domain-verified (publicly certified) or a
   pinned (trust-on-first-use) model.  For iN2N, members and the Border
   mutually authenticate at the application layer with pinned
   credentials and a hub attestation, and TLS may additionally protect
   the transport.  NCFED does not replace MCP or A2A; it is a cross-
   operator federation, identity, and transport layer beneath them.
   This document describes the protocol as implemented in the open-
   source NetClaw project and is published as Experimental to enable
   interoperability and public review.
- **draft-coetzee-oauth-spt-txn-tokens-03** (new-draft, score 23, trust_infrastructure) [none]: [Transaction-Bound Authorization Tokens for Software and AI Agents (SPT-Txn)](https://datatracker.ietf.org/doc/draft-coetzee-oauth-spt-txn-tokens/) — Current authorization is role-scoped: an actor is granted a role
   whose authority persists across every action it takes.  This fails
   exactly when actors fail -- under compromise, prompt injection, or
   goal hijacking -- because a compromised actor retains full role
   authority.  This document specifies SPT-Txn, a family of transaction-
   bound authorization tokens in which authority exists only inside a
   short-lived token bound to one declared action, on one resource,
   under one jurisdictional policy, verified against how the requesting
   workload was attested.  Delegation across agents and tools is
   expressed as a cryptographically sealed chain that can only narrow
   authority and is verifiable offline.  Each authorization decision
   emits a signed, tamper-evident receipt as a byproduct of enforcement.
   This document specifies normative intent binding, transaction
   receipts and their transparency log, attested issuance via OAuth 2.0
   Token Exchange, per-token status-list revocation, and cryptographic
   algorithm agility including hybrid post-quantum signing.  It also
   hardens attested issuance in response to an adversarial security
   review of the reference implementation: it makes an audience and a
   verifiable expiry mandatory on the presented attestation, requires
   the issuer to bound the delegated depth it grants, and clamps a
   token's lifetime to the attestation it was minted on.  The issuer-
   side requested-versus-permitted scope intersection is retained; the
   enforcement point re-checks the chain independently.
- **draft-munoz-scitt-permit-profile-01** (new-draft, score 23, adjacent_watchlist) [none]: [A SCITT Profile for Pre-Execution AI Action Authorization Records](https://datatracker.ietf.org/doc/draft-munoz-scitt-permit-profile/) — This document specifies a SCITT (Supply Chain Integrity,
   Transparency, and Trust) profile for pre-execution authorization
   records of AI agent actions.  The profile defines a Signed Statement
   type, the "Pre-Execution Authorization Record" (also called a
   Permit), that records a policy-evaluated decision to allow, deny, or
   challenge an AI agent action before that action is dispatched to a
   model provider, tool, or service.  The profile cryptographically
   binds the authorization decision to the canonical bytes of the
   request that is authorized.  When the paired Closure Record carries a
   dispatch digest, a Verifier can compare the authorized-request digest
   against the recorded dispatched-request digest; on the managed
   dispatch path the reference implementation additionally enforces this
   equality before the request is sent.

   This revision also introduces authorization-lineage vocabulary.  It
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
- **draft-lundholm-kaif-00** (new-draft, score 22, authorization) [none]: [The Kindred Agent Identity Framework (KAIF)](https://datatracker.ietf.org/doc/draft-lundholm-kaif/) — The Kindred Agent Identity Framework (KAIF) is an OAuth 2.0 token
   exchange mechanism for delegated agent-to-service authorization,
   combining RFC 8693 token exchange with SPIFFE workload identity
   attestation and operator-assigned authorization tiers.

   This document specifies the protocol mechanics, deployment profiles,
   and interoperability requirements for systems implementing agent
   authorization with audit accountability.  KAIF is intended for
   scenarios in which an operator (human principal) provisionally
   authorizes an agent (automated workload) to perform bounded actions
   on their behalf, with cryptographic proof of authorization,
   delegation depth tracking, and revocation in real time.

   This document is intentionally vendor-neutral in its normative
   requirements.  Cloud platforms, model providers, workflow systems,
   and audit backends discussed by implementations are informative
   deployment examples, not part of the KAIF wire protocol.
- **draft-burls-mtac-00** (new-draft, score 18, authorization) [none]: [Merkle Tree Agent Certificates (MTAC): Batch-Issued Post-Quantum Identity Credentials for AI Agents](https://datatracker.ietf.org/doc/draft-burls-mtac/) — This document specifies Merkle Tree Agent Certificates (MTAC), a
   credential format and issuance profile in which a certificate
   authority commits a batch of AI agent identity credentials to a
   Merkle tree, signs only the tree head with the post-quantum signature
   algorithm ML-DSA-65, and distributes a per-credential inclusion
   proof.  A relying party verifies a credential offline against the
   signed tree head without contacting the issuer.  Each batch root is
   additionally co-signed by an independently keyed witness, providing
   per-batch integrity and continuity attestation, and its root can be
   corroborated against an independent public record.

   MTAC defines the leaf structure, its deterministic encoding, the leaf
   hash preimage, the signed tree head wire format, the witness co-
   signature, and an optional challenge-response proof of possession
   that binds a credential to a holder key.  Test vectors are provided.
   This document specifies a credential issuance and verification
   mechanism.  Declared scopes carried in a credential are self-reported
   parameters recorded at issuance; this document does not specify a
   runtime authorization mechanism.
- **draft-ietf-oauth-identity-chaining-17** (new-draft, score 18, authorization) [oauth]: [OAuth Identity and Authorization Chaining Across Domains](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/) — This specification describes a mechanism for preserving identity and
   authorization information across trust domains that use the OAuth 2.0
   Framework.  A JSON Web Token (JWT) authorization grant, obtained
   through an intra-domain OAuth 2.0 Token Exchange, facilitates the
   cross-domain acquisition of an access token.  The relevant identity
   and authorization information is chained throughout the flow by being
   conveyed in the respective artifacts exchanged at each step of the
   process.  Chaining across multiple domains is achieved by using the
   same protocol every time a trust domain boundary is crossed.
- **draft-reilly-cogsov-00** (new-draft, score 18, trust_infrastructure) [none]: [Cognitive Sovereignty (CS): A Framework for Verifiable Human Epistemic Autonomy over Agent-Curated Content](https://datatracker.ietf.org/doc/draft-reilly-cogsov/) — As autonomous AI agents become the primary intermediaries between
   humans and the web, humans increasingly perceive the web only as
   agents present it: summarized, filtered, ranked, translated, and
   rewritten.  Machine-Web Symbiosis [REILLY-MWS] gives machines
   verifiable ground truth about web content; no equivalent mechanism
   gives humans verifiable ground truth about what agents did to that
   content before presenting it.

   This document defines Cognitive Sovereignty (CS): the principle
   that a human consuming agent-curated content retains the right and
   the technical capacity to (1) know that curation occurred, (2)
   inspect what transformations were applied and under what declared
   agent policy, (3) reach the attested, un-curated source, and (4)
   verify all of the above using only public data and open
   specifications.  The document specifies a complete implementation:
   the Curation Disclosure Record (CDR) format, the pipeline by which
   conforming agents generate CDRs, the mechanisms by which CDRs are
   delivered alongside curated content, and the procedure by which
   any consumer verifies them.  CS composes directly with the Reilly
   Protocol Suite: MWS records supply source ground truth, the
   Cognitive Trust Stack supplies agent behavioral provenance, and
   Dual-Layer Digital Permanence anchors the disclosure chain.
- **draft-schrock-ep-architecture-02** (new-draft, score 18, core_identity) [none]: [The EMILIA Protocol: An Evidence Architecture for Consequential Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-architecture/) — Consequential agent actions can cross operator and administrative
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
- **draft-sharif-x509-agent-identity-profile-01** (new-draft, score 18, agent_identity) [none]: [X.509 Certificate Profile for Autonomous AI Agent Identity](https://datatracker.ietf.org/doc/draft-sharif-x509-agent-identity-profile/) — This document defines an X.509 certificate profile for identifying
   autonomous AI agents.  It specifies a new X.509v3 extension,
   AgentIdentity, that encodes agent-specific metadata within a
   standard X.509 certificate, including agent trust level,
   operational capabilities, delegation constraints, owner attribution,
   and revocation control endpoints.

   The profile enables certificate authorities (CAs) to issue
   interoperable agent identity certificates that any relying party
   can parse, validate, and enforce, regardless of the issuing CA or
   the platform that provisioned the agent.

   The design builds on existing PKI infrastructure (RFC 5280), SPIFFE
   Verifiable Identity Documents (SPIFFE SVIDs), and the MCPS
   cryptographic signing layer (draft-sharif-mcps-secure-mcp).  It
   does not require changes to X.509v3 certificate parsing or to
   existing CA issuance pipelines beyond supporting a new non-critical
   extension.
- **draft-zagarella-verified-human-root-00** (new-draft, score 18, core_identity) [none]: [Verified Human Root Attestation for Agent Delegation Chains and Audit Records](https://datatracker.ietf.org/doc/draft-zagarella-verified-human-root/) — Autonomous software agents increasingly act under delegated
   authority, and emerging audit-record data models capture what an
   agent did, under which delegation, with which authorization state.
   In current practice the head of every such chain, and the identity
   axis of every such record, is a key, an account, or a workload
   identity.  No standardized element establishes that an identified
   natural person, verified as live and present, stands at the head of
   the chain or behind the recorded action.

   This document defines the Verified Human Root Attestation (VHRA): a
   compact, privacy-preserving data structure asserting that a biometric
   proof-of-human verification of an identified natural person (or an
   M-of-N quorum of such persons) occurred at a specific issuance event.
   It further defines how a delegation chain binds a VHRA at its root
   such that the binding survives attenuation, and how audit and
   interaction records reference a VHRA so that any recorded agent
   action can be resolved to an accountable natural person without the
   verifier receiving any biometric material.

   This document is offered as input to the proposed AUDIT working
   group's data model work.  It deliberately does not standardize
   biometric verification methods; it standardizes only the attestation
   structure, its bindings, and verifier obligations.
- **draft-kamimura-scitt-vcp-03** (new-draft, score 17, trust_infrastructure) [none]: [A SCITT Profile for Verifiable Audit Trails in Algorithmic Trading: The VeritasChain Protocol (VCP)](https://datatracker.ietf.org/doc/draft-kamimura-scitt-vcp/) — This document defines a profile of the SCITT (Supply Chain Integrity,
   Transparency, and Trust) architecture for creating tamper-evident
   audit trails of AI-driven algorithmic trading decisions and
   executions.  The VeritasChain Protocol (VCP) applies the SCITT
   framework to address the specific requirements of financial markets,
   including high-precision timestamps, regulatory compliance
   considerations (EU AI Act, MiFID II), and privacy-preserving
   mechanisms (crypto-shredding) compatible with GDPR.  This profile
   specifies how VCP events are encoded as SCITT Signed Statements,
   registered with Transparency Services, and verified using COSE
   Receipts.  It further defines SCITT conformance profiles for
   interoperability and an ERASURE event type that records crypto-
   shredding operations as immutable audit events.

About This Document

   This note is to be removed before publishing as an RFC.

   The latest version of this document, along with implementation
   resources and test vectors, can be found at
   https://github.com/veritaschain/vcp-spec.

   Discussion of this document takes place on the SCITT Working Group
   mailing list (scitt@ietf.org).

   Changes from -02:

   *  Updated to align with VCP Specification v1.2

   *  Added SCITT Alignment Object and conformance profiles
      (Section 4.4)

   *  Added ERASURE event type recording crypto-shredding operations
      (Section 6.3)

   *  Corrected the post-quantum SignAlgo registry value from DILITHIUM3
      to DILITHIUM2 (ML-DSA, FIPS 204)

   *  PolicyID examples migrated to the Issuer Domain + Local ID naming
      convention defined in VCP v1.2
- **draft-raskar-agentic-web-federated-resolution-01** (new-draft, score 17, core_identity) [none]: [Registry-Assisted Discovery for AI Agents and Workloads Without DNS Discovery Anchors](https://datatracker.ietf.org/doc/draft-raskar-agentic-web-federated-resolution/) — Many agent-discovery mechanisms assume that an organization controls
   a DNS domain and can publish a DNS record, a well-known catalog, or
   an organization gateway. That model works well for enterprises with
   operational DNS infrastructure, but it does not cover every agent or
   workload. Small businesses may own a domain yet lack the expertise or
   infrastructure to publish agent-specific DNS records. Individuals may
   have a globally scoped account identifier, such as an email address,
   while not controlling the provider domain. Personal agents and other
   workloads may run on a cloud service or local device while their
   public descriptor is hosted elsewhere.

   This document describes registry-assisted discovery for these cases.
   A NandaIndex registry binds a stable Subject Identity to a
   subject-authorized terminal object, such as an A2A Agent Card, an MCP
   server descriptor, a workload descriptor, a subject-owned AI Catalog,
   or a subject-authorized gateway. The binding includes authority,
   freshness, and revocation information. The identity owner, descriptor
   host, and runtime operator may be different parties.

   This document does not define a directory of discovery servers,
   directory federation, or a global switchboard. A NandaIndex response
   does not direct a client to another generic resolution or discovery
   service. DNS-anchored systems remain direct: when an authoritative AI
   Catalog, DNS-AID record, or organization gateway is already known,
   NandaIndex is not in the critical path. The focus is permissionless
   publication and discovery for agents and workloads that do not have a
   usable DNS Discovery Anchor.
- **draft-schrock-action-evidence-boundary-00** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
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
- **draft-li-opsawg-agent-accel-framework-00** (new-draft, score 16, core_identity) [none]: [A Framework for Agent-Aware Network Acceleration Services in Home Broadband Access](https://datatracker.ietf.org/doc/draft-li-opsawg-agent-accel-framework/) — This document describes a framework for providing AI agents with
   differentiated network acceleration services in home broadband access
   environments.

   The framework introduces a Network Acceleration SKILL, provided by
   the network operator, through which agents subscribe to and request
   acceleration services directly from the Broadband Remote Access
   Server (Broadband Remote Access Server).  The Broadband Remote Access
   Server, augmented with a control plane agent, processes acceleration
   requests, coordinates authorization with the Authentication,
   Authorization, and Accounting server, and applies per-agent Quality
   of Service policies on its data plane.

   A key motivation is to evolve the currently rigid home broadband
   service model — where plans are fixed on monthly or yearly cycles
   with static rate limiting — toward a dynamic subscription model that
   supports on-demand purchase and management of acceleration resources
   such as time duration or traffic volume.

   A fundamental design constraint is that existing broadband access
   procedures, including Customer Premises Equipment authentication,
   IPv6 prefix delegation, and subscriber billing, remain unmodified.
- **draft-ranjbar-dane-anchored-identity-00** (new-draft, score 16, core_identity) [none]: [DANE-Anchored Identity for Network Clients, Devices, and Autonomous Agents](https://datatracker.ietf.org/doc/draft-ranjbar-dane-anchored-identity/) — A rapidly growing set of protocols for autonomous agents, connected
   devices, and machine workloads bootstraps trust in an endpoint's
   public key over the Web PKI together with an HTTPS .well-known fetch,
   a bespoke certificate authority, or a centralized registry.  These
   approaches inherit domain-takeover exposure, depend on a reachable
   call-home endpoint, are not verifiable across organizational
   boundaries, and frequently provide no timely revocation.  This
   document describes a complementary identity model in which an
   endpoint's key is anchored directly in DNSSEC-signed DNS using DANE
   (a TLSA record), bound to a routable address whose reverse and
   forward names are served from a signed zone, and described by RDAP.
   The model, consistent with the architecture developed in the DANE
   Authentication for Network Clients Everywhere (DANCE) working group,
   lets any relying party verify an endpoint's identity from stock DNS
   tooling with no account or private trust root, and lets the
   identity's holder revoke it worldwide at DNS TTL.  It is intended as
   an anchor that existing agent-, device-, and content-identity schemes
   can adopt without abandoning their own transports or object formats.
- **draft-aravind-oauth-operator-of-record-00** (new-draft, score 15, verifiable_claims) [none]: [Operator-of-Record: an Origination Marker for Agent-Operated Presentations and Decisions](https://datatracker.ietf.org/doc/draft-aravind-oauth-operator-of-record/) — This document requests registration of opr, an OPTIONAL, descriptive
   JWT claim that marks the operator of record, that is, whether a human
   or an agent operated a credential presentation or drove a decision.
   Its purpose is record integrity.  Under agent operation a wallet key-
   binding proof is cryptographically indistinguishable from a human-
   operated one, and no presentation protocol marks the difference; opr
   records the distinction.  A Policy Decision Point MUST ignore opr for
   the allow/deny decision; interpretation and any resulting
   authorization behavior are deployment-local and out of scope.  This
   document defines representation only.  It defines no remedy,
   adjudication, obligation, or authorization mandate.
- **draft-bu-agentproto-security-principal-binding-03** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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
- **draft-gravit-gevp-00** (new-draft, score 15, trust_infrastructure) [none]: [Gravit Epistemic Verification Protocol (GEVP) v0.1](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — Gravit Epistemic Verification Protocol (GEVP) defines minimal data
   types and APIs for autonomous agents and human-machine systems to
   achieve epistemic convergence without centralized truth arbiters.
   GEVP is transport-agnostic, blockchain-agnostic, and model-agnostic.
   This document defines a parameterized cost model where C_validation
   is the cost to verify a Claim's provenance and signatures, and
   C_manipulation is the estimated cost to forge a quorum of
   attestations under GQRVP.  The protocol enforces the engineering
   invariant C_manipulation > C_validation for all accepted Claims.

   This document was previously published as draft-gravit-vcp-00 and -01
   under the acronym VCP (Verifiable Convergence Protocol).  To avoid
   collision with VeritasChain Protocol (VCP) defined in draft-kamimura-
   scitt-vcp [KAMIMURA-VCP], which is a SCITT profile for financial
   trading audit trails first published December 2025, the acronym is
   changed to GEVP from -02 onward.  The two protocols are unrelated and
   address different domains.  The former VCP acronym is deprecated and
   MUST NOT be used for this protocol.

   This revision (-02) addresses feedback on -01: pins reproducible
   trace commits, provides full confusion matrix with false positive
   rate, clarifies that cost model and resilience bound are heuristic
   parameterized estimates (not formal derivations from MWU regret
   bounds), defines exact SCITT Signed Statement, Receipt, and
   Transparency Service mappings, separates SCITT authenticity
   guarantees from epistemic truth, and adds Appendix B on Gödel
   completeness boundary.
- **draft-sokolov-rats-aep-composition-03** (new-draft, score 15, trust_infrastructure) [none]: [Composing Application-Layer Action Evidence with Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-sokolov-rats-aep-composition/) — This document sketches a composition pattern in which an application-
   layer "action evidence package" (AEP) -- a signed, append-only record
   of an action taken by an automated (for example, AI-agent) system,
   the authority under which it was taken, and its outcome -- is treated
   as Evidence in the sense of the RATS Architecture (RFC 9334) and
   bound to platform Evidence produced by a hardware root of trust.  The
   intent is that a single Verifier, or a composition of Verifiers, can
   appraise both the platform state and the application-layer action
   together, and emit an Attestation Result that a Relying Party can use
   to reason about _what an automated system did_ and _on what platform
   it did so_ without trusting the operator's self-report for either.
   This is an individual sketch intended to ask the working group
   whether the pattern is already covered by existing mechanisms or
   warrants a short document.
- **draft-ambekar-oauth-epop-02** (new-draft, score 14, authorization) [none]: [JSON Web Token (JWT) Profile for OAuth 2.0 Enveloped Proof of Possession (EPOP)](https://datatracker.ietf.org/doc/draft-ambekar-oauth-epop/) — This specification defines a profile for OAuth 2.0 sender-constrained
   credentials in which authorization codes, access tokens, and refresh
   tokens are cryptographically bound to the client's private key as a
   single inseparable envelope.  Unlike existing mechanisms, EPOP
   provides proof-of-possession uniformly across both JWT and opaque
   access tokens, and across HTTP and non-HTTP transports.  The profile
   extends sender-constraining beyond HTTP to non-HTTP transports
   including MQTT, Kafka, the Model Context Protocol (MCP), gRPC, and
   SASL-based protocols such as those defined in [RFC7628].  It
   introduces atomic proof-of-possession key rotation, enabling clients
   to rotate key pairs without disrupting active sessions, and an
   offline-derived client nonce (cnonce) that eliminates the server-
   issued nonce round-trip required by existing mechanisms — enabling
   stateless proof validation critical for non-HTTP and high-throughput
   deployments.  Authorization servers, resource servers, and clients
   from different vendors can implement this profile interoperably.
- **draft-boone-prompt-uri-scheme-00** (new-draft, score 14, core_identity) [none]: [The 'prompt' URI Scheme for AI Agent Sessions and Prompts](https://datatracker.ietf.org/doc/draft-boone-prompt-uri-scheme/) — This document defines the prompt Uniform Resource Identifier (URI)
   scheme for identifying prompts within AI agent sessions.  A prompt
   URI encodes the agent identity, session identifier, and a timestamp
   sufficient to locate the originating prompt within an agent session
   log.  The scheme is intended for use in provenance records, audit
   trails, and cross-agent references where a human-readable, stable
   locator for a prompt interaction is required.

   This document also addresses the conditions under which multiple URIs
   MAY resolve to the same prompt and the conditions under which a
   single URI MAY be ambiguous with respect to the prompt it identifies.
- **draft-bzb-rats-intel-poe-endorsements-00** (new-draft, score 14, trust_infrastructure) [none]: [A CoRIM Profile for Intel Platform Ownership Endorsements (POE)](https://datatracker.ietf.org/doc/draft-bzb-rats-intel-poe-endorsements/) — A Platform Ownership Endorsement (POE) is a signed statement that a
   specific Intel confidential-computing platform instance, identified
   by its Platform Instance Identity (PIID), belongs to a named owner.
   POEs let a Verifier bind the attested hardware identity from an Intel
   SGX or TDX platform to an operational owner (e.g., a Cloud Service
   Provider) during appraisal, giving a Relying Party a trustworthy
   owner identity -- without trusting the attestation service or any in-
   band claim from the platform itself.

   This document defines POE as a profile of the IETF Concise Reference
   Integrity Manifest (CoRIM) data model.
- **draft-ietf-jose-json-web-proof-14** (new-draft, score 14, verifiable_claims) [jose]: [JSON Web Proof](https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/) — The JOSE set of standards established JSON-based container formats
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
- **draft-ietf-wimse-http-signature-05** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload-to-Workload Authentication with HTTP Signatures](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).
- **draft-liu-icnrg-verifiable-compute-results-00** (new-draft, score 14, trust_infrastructure) [none]: [A Metadata Model for Verifiable and Reusable Compute-Result Objects in Information-Centric Edge Networks](https://datatracker.ietf.org/doc/draft-liu-icnrg-verifiable-compute-results/) — Distributed edge systems can execute the same logical computing
   service at multiple sites and can retain previously generated outputs
   in gateways, caches, or result stores.  Reusing such an output can
   reduce communication and computation, but a payload alone does not
   indicate which service, inputs, parameters, execution environment, or
   validity conditions produced it.  This document defines a conceptual
   metadata model for named compute-result objects.  The model binds a
   result payload to service identity, input identity, invocation
   context, execution provenance, freshness information, and reuse
   policy.  It also describes validation and cache-reuse workflows for
   intermittently connected and multi-domain edge environments.  This
   document does not define a wire encoding, a naming syntax, a remote-
   attestation profile, or a traffic-steering protocol.
- **draft-mpsb-agntcy-messaging-02** (new-draft, score 14, agent_identity) [none]: [An Overview of Messaging Systems and Their Applicability to Agentic AI](https://datatracker.ietf.org/doc/draft-mpsb-agntcy-messaging/) — Agentic AI systems require messaging infrastructure that supports
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

   AGNTCY SLIM emerges as a purpose-built solution, integrating Message
   Layer Security (MLS) [RFC9420] with gRPC [gRPC] over HTTP/2 [RFC9113]
   to provide end-to-end encryption with forward secrecy, efficient
   streaming, and OAuth-based authentication [RFC6749].  Unlike
   transport-layer security approaches, SLIM's MLS implementation
   ensures secure communication even through untrusted intermediaries
   while supporting dynamic group membership changes essential for
   collaborative AI agents.
- **draft-schrock-canonical-action-identifier-01** (new-draft, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
   identify an action using format-local content and digests.  Those
   digests are not directly comparable when the formats select or encode
   material action fields differently.  This document defines the
   Canonical Action IDentifier (CAID): a typed action object, a
   canonicalization and digest suite, a compact identifier string, and
   immutable action-type definitions with required material fields.  It
   also defines an Action-Mapping Profile for projecting independently
   verified native artifacts into a common action type, with the closed
   results EQUIVALENT_UNDER_PROFILE, NOT_EQUIVALENT, and INDETERMINATE.
   CAID carries no trust semantics.  It does not establish identity,
   authority, authorization, execution, safety, or legal reliance.
- **draft-schrock-ep-authorization-evidence-chain-04** (new-draft, score 14, core_identity) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
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
   and controls consumption, invocation, and effect handling.  AEC
   introduces no new component receipt type and does not replace any
   native verifier.
- **draft-zhu-oauth-async-delegation-02** (new-draft, score 14, authorization) [none]: [Delegation Handle for Asynchronous OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/draft-zhu-oauth-async-delegation/) — This document defines a standardized continuation mechanism for
   delegated OAuth 2.0 Token Exchange.  RFC 8693 permits an
   authorization server to include an optional "refresh_token" in a
   successful Token Exchange response, but does not specify issuance
   policy, delegated authorization semantics, lifecycle, or security
   properties for continuation credentials.  This specification fills
   that gap for asynchronous and long-running delegated service
   workflows by defining the Delegation Handle.

   The Delegation Handle is a delegation-bound continuation credential
   with a new token type identifier usable as the RFC 8693
   "subject_token_type".  An acting service presents the handle as the
   "subject_token" in a subsequent RFC 8693 Token Exchange request after
   the original subject token is no longer available.  This
   specification standardizes delegated continuation semantics,
   preservation of subject and actor relationships, audience
   confinement, scope monotonicity, actor binding, authorization re-
   evaluation during continuation, token rotation, revocation, bounded
   delegation lifetime, and interoperability between implementations.
- **draft-schrock-ep-revocation-statement-00** (new-draft, score 13, core_identity) [none]: [Portable Revocation Statements for Action-Bound Authorization Artifacts](https://datatracker.ietf.org/doc/draft-schrock-ep-revocation-statement/) — Signed authorization artifacts for agent actions (receipts, commits,
   delegations) are being defined faster than the means to retract them.
   Many deployed systems use live status services, revocation lists, or
   issuer datastores.  This document defines a complementary portable
   form for action-bound authorization artifacts: a signed, offline-
   verifiable claim that a named logical target, addressed by identifier
   and action commitment, is revoked.  Verification is fail-closed and
   evaluates a fixed set of checks: version, closed object structure,
   target binding, a revoker key pinned by the verifier and, for newly
   emitted artifacts, bound to a full digest-derived key identifier (a
   self-asserted key confers nothing), the presence of a strict
   revocation instant that has taken effect by the verifier's decision
   time, and an independently recomputed signature.  The statement
   proves that a named, pinned revoker revoked this specific target.  It
   does not prove that every relying party saw it, and offline
   verification cannot prove the absence of a revocation that was not
   presented.  A terminal revocation never ages out; current non-
   revocation requires separate authenticated, policy-fresh status
   evidence.  A Trust Program profile binds revocation to the complete
   execution claim, and requires revocation-versus-claim to be resolved
   atomically; a revocation learned after a claim never rewrites an
   effect that may already have occurred.
- **draft-sirkkavaara-vaara-receipt-05** (new-draft, score 13, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Agent Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
   recomputable record that binds a decision about an agent action to
   the evidence the decision was made on, and optionally to one or more
   external timestamp anchors.  The format is canonicalized with the
   JSON Canonicalization Scheme (JCS) so that any third party can
   recompute its digests and verify its signature without access to the
   issuer.

   The receipt's trust is root-agnostic: the same record is verifiable
   with or without a hardware trusted execution environment and is re-
   expressible as an IETF RATS Entity Attestation Result.  Downstream
   specifications (a payment rail, a compliance regime, a framework
   integration) define profiles that pin to a version of this document
   and add only their own evidence schema; they do not redefine the
   envelope.  The format described here is deployed, and its receipts
   are independently recomputable from public conformance vectors that
   ship with standalone checkers importing no issuer code.  The minimal
   profile is a governance decision over a single agent action, bound to
   the action's own intent with no external rail; it is the floor of the
   format, and a reference library offers a matching adoption floor at
   the API layer as a one-line decorator over the governed function.
- **draft-skyfire-oauth-using-kyapay-tokens-00** (new-draft, score 13, core_identity) [none]: [Using KYAPay Tokens](https://datatracker.ietf.org/doc/draft-skyfire-oauth-using-kyapay-tokens/) — The KYAPay Token is a JSON Web Token (JWT) that carries verified
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
   It defines the token-consuming "verifier" role that the KYAPay Token
   leaves unspecified.  It is intentionally non-prescriptive about how
   tokens are created, because agent architectures, agent-identity
   technologies, and agent-communication protocols are diverse and still
   emerging; the token itself is the interoperability contract.
- **draft-geng-acme-sm2dualcert-extension-00** (new-draft, score 12, authorization) [none]: [ACME Extension for SM2 Dual-Certificate System](https://datatracker.ietf.org/doc/draft-geng-acme-sm2dualcert-extension/) — This document describes the extension of the ACME protocol [RFC8555]
   to support automated issuance of SM2 dual certificates (signature
   certificates and encryption certificates) in the Chinese National
   Cryptography certificate system.  This document does not represent
   IETF consensus; the technical solution is applicable only to PKI
   environments based on an SM2 dual-certificate system.

   Under the framework of the ACME protocol [RFC8555], this document
   proposes using two separate Orders to request the two certificates.
   For the signature certificate, the existing ACME workflow is reused,
   optionally using the standard CSR approach or the pk-01 challenge
   [I-D.geng-acme-public-key].  For the encryption certificate, this
   document defines a new challenge type, auth-01, specifically for
   *identity authorization* scenarios: the client proves possession of
   the *signature private key* to authorize the Key Management Center
   (KMC) to generate an encryption key pair and issue the encryption
   certificate on behalf of the entity.  This challenge type
   intrinsically binds the issuance of the encryption certificate to the
   signature key, requiring no additional binding identifiers.

   All extensions are compatible with the existing ACME resource model.
   No new Order types are introduced.  This document only adds optional
   fields in the client's newOrder request (authKey, includeEnvelope)
   and an additional field in the server's response (envelope), without
   changing the core semantics or state machine of Order.
- **draft-marques-asqav-compliance-receipts-07** (new-draft, score 12, trust_infrastructure) [none]: [Compliance Profile of Signed Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-marques-asqav-compliance-receipts/) — This document defines a multi-jurisdiction compliance profile of the
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
   cross-agent envelope binding, per-action freshness and integrity,
   build provenance, threat-framework taxonomy, server-built enforcement
   attestation, producer-asserted risk acceptance, and producer-asserted
   code authorship, each subject to false-attestation guards where
   applicable, and registers receipt type namespaces for passive-
   telemetry, result-bound observation, risk-acceptance, and code-
   authorship receipts.  The full field set and its normative
   requirements are defined in the body of this document.
- **draft-schrock-model-to-matter-01** (new-draft, score 12, authorization) [none]: [Model-to-Matter: Authorization Evidence for Model-Directed Physical Execution](https://datatracker.ietf.org/doc/draft-schrock-model-to-matter/) — Advanced models and agents can propose experimental workflows and
   invoke systems that produce physical effects.  Before acting, a
   physical executor may need evidence from several independent
   authorities: model provenance, a safety assessment, institutional
   authority, a domain review, an external screening service, and an
   accountable human.  Those artifacts are commonly evaluated separately
   and may not bind the same action.  This document defines Model-to-
   Matter, an experimental executor-side applicability profile for
   composing those artifacts over one canonical, digest-only action.  It
   specifies an executor-owned acceptance profile, normalized signed
   evidence adapters, a registered challenge, closed clearance and
   refusal verdicts, atomic single-use clearance consumption, and an
   optional executor-signed effect statement.  The profile composes
   native evidence through an Authorization Evidence Chain and applies
   the Action Evidence Boundary lifecycle when the executor invokes the
   effect.  It does not perform domain screening, determine scientific
   safety, authorize an institution, or establish physical truth.  It
   standardizes the point at which an executor refuses to act unless the
   authorities it independently trusts agree about the same action.
- **draft-feng-netconf-naim-op-00** (new-draft, score 11, agent_identity) [none]: [Operation Intent Intermediate Representation for AI-Assisted Network Management](https://datatracker.ietf.org/doc/draft-feng-netconf-naim-op/) — This document defines Operation IR, a protocol-neutral intermediate
   representation for runtime network operations in the NAIM
   architecture.  Operation IR serves as an AI-friendly operation layer
   between AI agents or LLM-based systems and the underlying network
   management protocols.  It captures write operations, retrieval, RPC/
   action invocation, filtering, transaction metadata, precondition
   verification, compensation semantics, and optional expression-based
   values.

   Operation IR is designed to be consumed by any upstream mechanism
   capable of generating structured operation intent, including but not
   limited to MCP tool invocations, function calling interfaces, and
   agent-to-agent communication protocols.  The translation of Operation
   IR into protocol-specific messages is performed deterministically by
   a Handler component, keeping the AI agent in the role of intent
   encoder rather than protocol executor.

   This document also defines context completeness classes for the
   Originator (AI agent) side, validation feedback requirements, and an
   execution preview mode intended to improve safety and operator trust.
   It standardizes semantic expectations and interoperability
   boundaries, but does not standardize proprietary dialogue policies,
   implementation-specific scheduling internals, automatic compensation
   derivation algorithms, or private execution-engine logic.
- **draft-ietf-seat-use-cases-00** (new-draft, score 11, core_identity) [seat]: [Security Goals and Use Cases for Integrating Remote Attestation with Secure Channel Protocols](https://datatracker.ietf.org/doc/draft-ietf-seat-use-cases/) — This document outlines desirable security goals and use cases for
   integrating remote attestation (RA) capabilities with secure channel
   establishment protocols (e.g., TLS and DTLS).  Peer authentication in
   such protocols establishes trust in a peer's network identifiers but
   provides no assurance regarding the integrity of its underlying
   software and hardware stack.  Remote attestation addresses this gap
   by enabling a peer to provide verifiable evidence about the current
   state of the Target Environment.  This document specifies a set of
   essential security goals the protocol solution must have, including
   cryptographic binding to the secure connection, evidence freshness,
   and flexibility to support different attestation models.  It then
   explores relevant use cases, such as confidential data collaboration
   and secure secrets provisioning, to motivate the need for this
   integration.  This document is intended to serve as an input to the
   design of protocol solutions within the SEAT working group.
- **draft-liu-icnrg-disruption-aware-task-descriptor-00** (new-draft, score 11, core_identity) [none]: [Requirements for Disruption-Aware Compute-Task Descriptors in Heterogeneous Space-Terrestrial-Maritime Edge Networks](https://datatracker.ietf.org/doc/draft-liu-icnrg-disruption-aware-task-descriptor/) — Compute tasks in heterogeneous edge environments may traverse
   terrestrial, maritime, airborne, and non-terrestrial domains before
   an eligible execution site becomes reachable.  Conventional request
   formats often assume an immediately selected endpoint and a
   continuously available request-response path.  Those assumptions are
   fragile when connectivity is intermittent, service instances move,
   inputs are named and distributed, and duplicate delivery can occur.

   This document describes a problem statement, a conceptual compute-
   task descriptor, and requirements for carrying a portable task
   description across disruption-prone edge networks.  The descriptor
   separates the identity and semantics of a task from a particular
   execution location.  It binds the requested service, named inputs,
   relevant parameters, timing constraints, authorization policy, and
   expected result properties while supporting store-carry-forward
   operation, duplicate suppression, verifiable execution receipts, and
   result provenance.  This document does not define a wire encoding,
   task-placement algorithm, traffic-steering protocol, or execution
   runtime.
- **draft-sabey-succession-receipts-02** (new-draft, score 11, authorization) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
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
- **draft-sabey-succession-receipts-sd-02** (new-draft, score 11, verifiable_claims) [none]: [Selective Disclosure for Succession Receipts](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts-sd/) — A Succession Receipt proves one completed, policy-gated transfer of
   authority between autonomous agents, and it is all-or-nothing:
   whoever holds the receipt holds every claim and every evidence event
   in it.  In regulated deployments the parties entitled to verify a
   transfer are not all entitled to read it in full — a regulator, a
   counterparty, and the public each warrant a different view.  This
   document specifies a selective-disclosure form of the receipt: the
   issuer signs salted commitments to each claim unit and each evidence
   event, disclosures travel outside the signature, and a projection —
   the signed envelope plus any subset of the disclosures — still
   verifies against the one issuer signature.  Withholding never breaks
   the proof, disclosing never re-signs, withheld content remains
   visibly committed, and a projection that opens every commitment is
   verifiable to exactly the strength of the underlying receipt.  The
   disclosure mechanism deliberately follows the salted-digest analysis
   of SD-JWT, restated for plain-JSON documents canonicalized with the
   JSON Canonicalization Scheme.
- **draft-schrock-ep-authorization-receipts-08** (new-draft, score 11, core_identity) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
   an evidence artifact binding an enrolled approver key to one
   canonical action before execution.  An approver-held key signs an
   Authorization Context containing the action hash, policy reference,
   nonce, audience, and validity window.  A Trust Receipt carries the
   signed contexts, terminal consumption record, and Merkle inclusion
   material so a relying party can verify the recorded event offline
   under independently selected log, directory, policy, and approver
   trust inputs.

   The receipt establishes only the guarantees of the selected
   verification profile.  The mapping from an enrolled approver
   identifier to a natural person is asserted by the directory
   authority.  Offline verification does not establish current
   revocation status, global non-replay, comprehension, legality,
   safety, or execution.  Replay prevention requires an online atomic
   consumption store at the executor.  The state-machine invariants are
   machine-checked under the assumptions stated in this document.
- **draft-singh-apex-psi-03-01** (new-draft, score 11, core_identity) [none]: [PSI-03: VPP Dispatch Conformance Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/) — PSI-03 specifies a portable, Ed25519-signed bond that anchors a
   registered NDIS practitioner's professional identity to a DID-
   compatible decentralised identifier without requiring a central
   registry.  The bond enables cross-provider, cross-border practice
   verification while preserving privacy and issuer sovereignty.
- **draft-singh-psi-agent-00** (new-draft, score 11, agent_identity) [none]: [PSI AI Agent Action Sealing and Liability Protocol](https://datatracker.ietf.org/doc/draft-singh-psi-agent/) — This document specifies a cryptographic protocol for sealing AI agent
   actions, establishing an auditable chain of custody from instruction
   to execution.  As AI agents increasingly perform autonomous actions —
   financial transfers, content publication, system configuration, legal
   filings — the need for a verifiable record of "who instructed what,
   when, and what actually happened" becomes critical for liability
   attribution, regulatory compliance, and trust.  The PSI Agent Se
- **draft-skyfire-oauth-kyapay-token-01** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-gupta-emu-eap-wsim-01** (new-draft, score 10, core_identity) [none]: [EAP-WSIM: SIM-Based EAP Authentication for Enterprise Wi-Fi Using the MILENAGE-ML-KEM-FWD Construction](https://datatracker.ietf.org/doc/draft-gupta-emu-eap-wsim/) — Enterprise Wi-Fi networks authenticate devices using enterprise
   credentials and provisioning policies that are entirely independent
   of MNO subscriber identity.  As a result, MNO application traffic on
   enterprise Wi-Fi is completely anonymous at the Wi-Fi layer: the
   enterprise cannot identify MNO subscribers, apply per-subscriber QoS,
   or support fast BSS transitions for VoWiFi continuity.

   This document specifies EAP-WSIM, an evolutionary enhancement of EAP-
   AKA' (RFC 9048) that enables MNO devices to authenticate to
   enterprise Wi-Fi using their existing SIM credential (WSIM-Card)
   without contacting the MNO backend during authentication.  A WSIM-
   Authentication Server (WSIM-AS) within the enterprise Wi-Fi
   infrastructure holds MNO-provisioned MASTER KEY material in tamper-
   resistant security hardware.  Per-subscriber MILENAGE key material is
   derived on-demand from the MASTER KEY using the device's IMSI --
   identical in principle to MNO SIM personalization -- entirely within
   the security hardware boundary.  No per-subscriber key provisioning
   at the WSIM-AS is required.
- **draft-kondoju-evc-00** (new-draft, score 10, authorization) [none]: [An External Verifier Contract for Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-kondoju-evc/) — This document specifies the External Verifier Contract (EVC): a
   small, testable, proof-system-agnostic boundary between a host (the
   program about to take a privileged action on an agent's behalf) and
   an external verifier (a subprocess that renders an allow/deny verdict
   on an opaque proof bundle).  The contract governs only the transport
   and verdict envelope: how the host hands a single JSON request to a
   verifier subprocess over stdin, how the verifier answers with exactly
   one JSON verdict on stdout, and how the host interprets exit codes,
   timeouts, and malformed output under a fail-closed rule.  Three
   properties make the boundary standardizable: (1) a single-shot
   subprocess transport with a closed JSON verdict schema; (2) fail-
   closed host semantics that are independently testable by a host-
   conformance suite; and (3) proof-system agnosticism, so the same
   envelope carries classical-signature, zero-knowledge, and third-party
   verdicts, distinguished only by an OPTIONAL self-description field.
   EVC is deliberately not a governance framework, not a delegation
   model, and not a policy language.  It is the narrow decision boundary
   those larger systems all require at the point of enforcement.
- **draft-miller-aeo-00** (new-draft, score 10, trust_infrastructure) [none]: [The AEO1 Discovery Mechanism: A DNS-Anchored, Signed Pointer to Owner-Attested Fact Catalogs for AI Answer Engines](https://datatracker.ietf.org/doc/draft-miller-aeo/) — This document specifies AEO1 (Answer Engine Optimization, version 1),
   a discovery mechanism that allows a domain owner to publish a
   verifiable, machine-readable pointer to a structured, owner-attested
   fact catalog for that domain.  AEO1 consists of three coordinated
   surfaces: a DNS TXT record at the "_aeo" subdomain, a JSON document
   at the well-known URI "/.well-known/aeo.json", and an optional HTML
   link hint.  Records may carry an Ed25519 signature issued by an
   issuing authority, enabling consuming agents such as AI answer
   engines to distinguish verified, current, domain-authorized data from
   unverified crawled content.  The design follows the DNS-authenticated
   trust-anchor pattern established by SPF, DKIM, and DMARC.  This
   document also requests provisional registration of the "aeo.json"
   well-known URI suffix.
- **draft-schrock-ep-quorum-03** (new-draft, score 10, authorization) [none]: [Multi-Party Quorum Authorization for High-Risk Agent Actions (EP-QUORUM)](https://datatracker.ietf.org/doc/draft-schrock-ep-quorum/) — This document defines EP-QUORUM, a multi-party authorization profile
   for the EMILIA Protocol (EP) authorization receipt (draft-schrock-ep-
   authorization-receipts).  Where the base receipt binds a single
   accountable human to one exact high-risk action, EP-QUORUM binds a
   set of distinct accountable humans -- the "two-person rule,"
   generalized to M-of-N and to ordered approval trails -- to one exact
   action, such that the quorum predicate is not satisfied until the
   full quorum holds.  The profile is purely additive: each quorum
   member is an unmodified EP signoff over the same action hash, and a
   single-approver policy is the degenerate one-member case.  EP-QUORUM
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
   ordered, offline-verifiable, at-most-once-consumable multi-party
   decision.
- **draft-singh-psi-age-assurance-00** (new-draft, score 10, core_identity) [none]: [PSI Zero-Knowledge Age Assurance Attestation](https://datatracker.ietf.org/doc/draft-singh-psi-age-assurance/) — This document specifies PSI-Age, a privacy-preserving cryptographic
   attestation for age assurance.  It enables a relying party (such as a
   social media platform or online service) to verify that a user meets
   a minimum age threshold without learning the user's identity, date of
   birth, or any other personal attribute.  PSI-Age uses zero-knowledge
   range proofs over a committed birthdate to produce a compact,
   verifiable "age credential" that proves age >= threshold without rev
- **draft-araut-oauth-transactiontokens-bcp-00** (new-draft, score 9, authorization) [none]: [OAuth Transaction Tokens Best Current Practice](https://datatracker.ietf.org/doc/draft-araut-oauth-transactiontokens-bcp/) — This document provides best current practices for implementing and
   deploying OAuth 2.0 Transaction Tokens as specified in draft-ietf-
   oauth-transaction-tokens.  Transaction Tokens (Txn-Tokens) enable
   workloads in a trusted domain to preserve and propagate user identity
   and authorization context across service boundaries during the
   processing of external programmatic requests.  This BCP addresses
   practical deployment considerations including token service
   architecture, size management, propagation patterns, validation
   strategies, and operational monitoring that are essential for secure
   and effective implementation in production environments.
- **draft-bdnr-rats-trustworthy-credentials-02** (new-draft, score 9, trust_infrastructure) [none]: [Trustworthy Enrollment of Secure Credentials](https://datatracker.ietf.org/doc/draft-bdnr-rats-trustworthy-credentials/) — There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
   Attesters nevertheless need to interoperate with.  Existing deployed
   services, which precede the introduction of Remote Attestation, are
   often difficult to change/update in significant ways due to, among
   other reasons, organizational friction, technological inertia, and
   regulatory policies.  Yet there are significant advantages if
   workloads can be incrementally updated in the trustworthiness of the
   platform, without disrupting their clients and servers.

   This document details a protocol by which Remote Attestattion of
   Attesters is incorporated into the process of them being provided
   with Identity Documents (keys or credentials) to authenticate to
   RUPs.

   This specification illustrates how the RATS Architecture can be
   applied to interoperate with RUPs by providing Attesters with such
   Identity Documents.
- **draft-dellaert-oauth-approval-based-dcr-00** (new-draft, score 9, authorization) [none]: [OAuth 2.0 Approval-Based Dynamic Client Registration](https://datatracker.ietf.org/doc/draft-dellaert-oauth-approval-based-dcr/) — This document specifies an extension to the OAuth 2.0 Dynamic Client
   Registration Protocol ([RFC7591]) that enables registration of a
   client with an authorization server through an explicit approval step
   performed by an approving party, typically the user running the
   client, without requiring the client to possess an Initial Access
   Token (IAT) beforehand.  The client submits its desired metadata to
   the existing client registration endpoint and signals that it can
   accept a deferred, approval-based registration.  When the
   authorization server requires approval, it defers completion of the
   registration and returns a 202 (Accepted) response carrying a
   registration code and a verification challenge.  The client polls the
   same registration endpoint, presenting the registration code.  The
   approving party, authenticated to the authorization server through a
   mechanism of the authorization server's choosing, responds to the
   verification challenge and approves or denies the registration.  On
   approval, a subsequent poll returns a registered client identifier
   and, where applicable, a client secret.

   This extension preserves the authorization server operator's ability
   to require an authenticated, policy-controlled approval for every new
   client record, while removing the operational burden of issuing an
   Initial Access Token out of band.
- **draft-feng-nmrg-ain-architecture-01** (new-draft, score 9, agent_identity) [none]: [Agentic Intent Network (AIN): A Routing-Based Architecture for AI Agent Coordination at Scale](https://datatracker.ietf.org/doc/draft-feng-nmrg-ain-architecture/) — The rapid proliferation of autonomous AI agents across enterprise and
   Internet-scale deployments creates a structural challenge that
   existing agent frameworks cannot address: how to enable any agent to
   discover and invoke any other agent's capabilities without pre-
   established bilateral integration, across organizational boundaries,
   at Internet scale.  This document presents the Agentic Intent Network
   (AIN) as an architecture-level model for open, heterogeneous,
   dynamically evolving multi-agent coordination.  It defines problem
   drivers, architectural and underlay requirements, architectural
   components, design invariants, scope boundaries, and a research
   agenda for the NMRG.
- **draft-gould-regext-auth-token-00** (new-draft, score 9, authorization) [none]: [Extensible Provisioning Protocol (EPP) Authentication Token Mapping](https://datatracker.ietf.org/doc/draft-gould-regext-auth-token/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for provisioning and management of EPP Authentication Token
   objects in a shared central repository, where an Authentication Token
   is a JSON Web Signature (JWS), defined in RFC 7515, and is used to
   authorize actions by registrar users.  The Authentication Token can
   be passed over an authenticated EPP session, as defined in RFC 5730,
   to provide elevated, fine-grained authorization exclusively valid
   until the lifetime of the digitally signed Authentication Token.
- **draft-gould-regext-epp-status-set-01** (new-draft, score 9, core_identity) [none]: [Status Set Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-gould-regext-epp-status-set/) — This document describes an Extensible Provisioning Protocol (EPP)
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
- **draft-ietf-jose-pq-composite-sigs-03** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.
- **draft-ietf-oauth-rfc8725bis-07** (new-draft, score 9, core_identity) [oauth]: [JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc8725bis/) — JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security
   tokens that contain a set of claims that can be signed and/or
   encrypted.  JWTs are being widely used and deployed as a simple
   security token format in numerous protocols and applications, both in
   the area of digital identity and in other application areas.  This
   Best Current Practices (BCP) specification updates RFC 7519 to
   provide actionable guidance leading to secure implementation and
   deployment of JWTs.

   This BCP specification furthermore obsoletes the existing JWT BCP
   specification RFC 8725 to provide additional actionable guidance
   covering threats and attacks that have been discovered since RFC 8725
   was published.
- **draft-ietf-sidrops-aspa-profile-28** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.
- **draft-infantado-agent-memory-architecture-00** (new-draft, score 9, trust_infrastructure) [none]: [Architecture and Data Model for Persistent Memory in Agentic Systems](https://datatracker.ietf.org/doc/draft-infantado-agent-memory-architecture/) — Memory in current agentic systems is often fragmented across model-
   provider features, application databases, session histories,
   framework-specific stores, unstructured files, and retrieval indexes.
   This document distinguishes temporary context supplied to an
   inference request from persistent memory that remains addressable,
   machine-readable, and governed beyond a single request.  It specifies
   a provider-independent architecture and data model for persistent
   memory in agentic systems based on Memory Scope isolation, typed and
   versioned Memory Objects, machine-readable provenance, append-only
   Event Ledger history, separate lifecycle, availability, retention,
   and validation state, and isolated Derived Indexes and Embedding
   Spaces.  The architecture separates a transient Compute Plane from an
   authoritative Persistent State Plane and treats embeddings, lexical
   indexes, graph projections, generated retrieval summaries, ranking
   caches, and retrieval caches as non-authoritative derived state.  The
   architecture is independent of model provider, storage engine, and
   protocol transport while allowing future bindings and multiple
   independent implementations.  It does not claim that related systems
   or standards do not exist; rather, it defines a common architectural
   vocabulary and interoperability target for persistent agentic memory.
- **draft-kykdxy-rats-tdx-cgpu-ear-profile-02** (new-draft, score 9, trust_infrastructure) [none]: [EAT Attestation Result (EAR) profile for Intel(r) Trust Domain Extensions (TDX) + Confidential GPU (C-GPU) composite attestation](https://datatracker.ietf.org/doc/draft-kykdxy-rats-tdx-cgpu-ear-profile/) — This document defines an Entity Attestation Token (EAT) Attestation
   Result (EAR) profile for the composite attestation of Intel® Trust
   Domain Extensions (TDX)–based Confidential Virtual Machines (CVMs)
   together with confidential NVIDIA GPUs (C-GPUs) deployed in Microsoft
   Azure.  The profile outlines claims that enable relying parties to
   establish trust in the integrity and confidentiality of the combined
   confidential computing environment.  Developed collaboratively by
   Microsoft, Intel, and NVIDIA, this work is intended to foster
   interoperable composite attestation across heterogeneous Trusted
   Execution Environments (TEEs) and confidential accelerators, while
   encouraging adoption and extension by verifier providers across the
   confidential computing ecosystem.
- **draft-lukianets-open-ethics-transparency-protocol-10** (new-draft, score 9, trust_infrastructure) [none]: [Open Ethics Transparency Protocol](https://datatracker.ietf.org/doc/draft-lukianets-open-ethics-transparency-protocol/) — The Open Ethics Transparency Protocol (OETP) is an application-level
   protocol for publishing and accessing ethical Disclosures of IT
   Products and their Components.  The Protocol is based on HTTP
   exchange of information about the ethical "postures", provided in an
   open and standardized format.  The scope of the Protocol covers
   Disclosures for systems such as Software as a Service (SaaS)
   Applications, Software Applications, Software Components, Application
   Programming Interfaces (API), Automated Decision-Making (ADM)
   systems, and systems using Artificial Intelligence (AI).  OETP aims
   to bring more transparent, predictable, and safe environments for the
   end-users.  The OETP Disclosure Schema is an extensible JSON-based
   format.
- **draft-mih-agent-bilateral-attestation-01** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
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
   organization can verify the record end-to-end.  The exchange records
   refusals with the same fidelity as performance, and degrades
   gracefully when a counterparty cannot attest, marking the record's
   reduced assurance rather than blocking the transaction.
- **draft-spk-agentproto-llm-stream-00** (new-draft, score 9, adjacent_watchlist) [none]: [A Standard Wire Format for Large Language Model Inference Streaming](https://datatracker.ietf.org/doc/draft-spk-agentproto-llm-stream/) — Large Language Model (LLM) inference endpoints stream response tokens
   to clients using a fragmented set of vendor-specific application-
   layer protocols layered on top of standardized transports (HTTP/2,
   HTTP/1.1, WebSocket, Server-Sent Events).  While these transports
   carry IETF or W3C standardization, the JSON payload schemas, event
   taxonomies, and framing conventions used within them are entirely
   vendor-defined, with no RFCs or common specifications governing them.

   This fragmentation imposes costs across the AI ecosystem.  Middleware
   frameworks and orchestration platforms (LangChain, LiteLLM, Vercel AI
   SDK, Portkey, Cloudflare AI Gateway) must maintain vendor-specific
   streaming parsers for every supported provider.  Cloud hosting
   platforms (AWS Bedrock, Azure AI Studio, Google Vertex AI) have each
   introduced additional proprietary streaming formats.  Compliance and
   observability tooling must be rebuilt per provider.  And new
   inference providers cannot reach framework-dependent developers
   without custom integration work.

   This document defines a standard wire format for LLM inference
   streaming over Server-Sent Events (SSE) on HTTP.  It specifies a
   request envelope media type (application/llm-request+json), a
   response event taxonomy, and a JSON event envelope schema that enable
   middleware, orchestration platforms, compliance tooling, and HTTP
   intermediaries to handle AI inference traffic from any conforming
   provider using a single protocol contract.  SSE transport remains
   unchanged; only the JSON payload inside it is standardized.

   The scope of this document is strictly Client/Application to LLM
   inference endpoint streaming.  Agent-to-tool interaction (e.g., MCP)
   and agent-to-agent communication are out of scope.
- **draft-vandoulas-aidp-03** (new-draft, score 9, adjacent_watchlist) [none]: [Agent Interaction & Delegation Protocol (AIDP)](https://datatracker.ietf.org/doc/draft-vandoulas-aidp/) — This document specifies the Agent Interaction & Delegation Protocol
   (AIDP), a control-plane protocol for secure, auditable, and
   interoperable software agents.  AIDP defines standardized mechanisms
   for expressing intent, enforcing authority, delegating capabilities,
   executing actions, and binding execution results to agent reasoning
   across heterogeneous systems and administrative domains.  This
   version introduces a normative Intent Lifecycle Model, including
   Human Approval Gates and support for long-running agent executions,
   defines version negotiation and capability discovery, clarifies the
   relationship of AIDP to the Model Context Protocol (MCP) and the
   Agent2Agent (A2A) protocol, and establishes extensibility
   registries.  Non-normative deployment material has been moved to
   informative appendices.
- **draft-davey-tls-braid-01** (new-draft, score 8, core_identity) [none]: [Bound Routing, Authority, and Identity Data (BRAID): Independent Circuit Breakers for Long-Lived TLS Certificates](https://datatracker.ietf.org/doc/draft-davey-tls-braid/) — This document defines BRAID, a negotiated profile for publicly
   trusted TLS server certificates that adds one or more independent
   circuit breakers to a certificate.  Each circuit breaker is an
   authorization held by a party the domain owner appoints; withdrawing
   any required authorization causes the certificate to stop validating.
   Because a certificate can be invalidated promptly and without the
   participation of the issuing certification authority, its natural
   validity period no longer has to be short in order to bound exposure.

   The base mechanism is deliberately static.  The domain owner
   publishes a DNSSEC-signed BRAID Anchor listing the public keys
   authorized to authenticate the domain, and thereafter does nothing;
   the certificate remains valid until the owner withdraws an entry.
   Steady-state operation requires no periodic reissuance, no periodic
   re-minting of credentials, and no online status service.  Short-
   interval credential refresh is defined as an optional enhancement
   that tightens revocation latency, not as a requirement.

   Because the Anchor authorizes credential keys rather than the end-
   entity key itself, impersonating a BRAID-protected domain requires
   both the end-entity private key and the ability to publish in the
   owner's DNSSEC-signed zone.  This document calls that the Two-Control
   Property, and it is the principal security difference between BRAID
   and publishing an end-entity certificate association directly in DNS.

   BRAID support is negotiated in the handshake, so a BRAID certificate
   is presented only to a client that offered to validate it; every
   other client is served an ordinary certificate and is unaffected.
   Optional strands bind a certificate to an authorized routing origin
   and to an appointed third-party witness.
- **draft-janz-nmrg-reference-lexicons-00** (new-draft, score 8, core_identity) [none]: [Shared Reference Lexicons for Agent-to-Agent Model Reconciliation in Network Management](https://datatracker.ietf.org/doc/draft-janz-nmrg-reference-lexicons/) — Interoperability between network-management systems is customarily
   arranged by agreeing a shared data model in advance or, where that
   falls short, a richer shared information model or ontology; both
   still require broad prior agreement on a common model.  This
   document, a companion to and enhancement of draft-janz-nmrg-ontology-
   reconciliation, argues that for systems built as cognitive, language-
   capable agents the shared reference can instead be a thin reference
   lexicon: a consultable nomenclature of named entities with
   disambiguating definitions and examples, free of relationship axioms
   and attribute schemas, and typically derived from an existing model.
   Each agent brings the lexicon apt to it; the two are lexically
   aligned into cross-source correspondences; identity is settled
   wherever they correspond; and only the residual is reconciled by the
   conversation of the companion document.  The document develops what
   such a lexicon should contain, the two-stage alignment that relates
   lexicons across sources, the distinct problem of co-referencing
   specific instances, and the scaling that follows from anchoring
   translation on shared references; and it recommends how model authors
   can make their artefacts more amenable to this automated alignment.
- **draft-kamimura-rats-behavioral-evidence-02** (new-draft, score 8, trust_infrastructure) [none]: [On the Relationship Between Remote Attestation and Behavioral Evidence Recording](https://datatracker.ietf.org/doc/draft-kamimura-rats-behavioral-evidence/) — This document provides an informational discussion of the conceptual
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
- **draft-moccia-dkim2-deployment-profile-06** (new-draft, score 8, core_identity) [none]: [A Deployment Profile for DKIM2 via Milter Interface](https://datatracker.ietf.org/doc/draft-moccia-dkim2-deployment-profile/) — This document defines a deployment profile for DomainKeys Identified
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
- **draft-pei-opsawg-agentops-observability-00** (new-draft, score 8, agent_identity) [none]: [AgentOps Observability for Failure Detection and Attribution](https://datatracker.ietf.org/doc/draft-pei-opsawg-agentops-observability/) — Agentic systems execute tasks through long-running sequences of model
   inference, planning, delegation, tool use, state updates,
   verification, and recovery.  Conventional metrics, logs, and traces
   can identify a failed request but often cannot determine whether a
   failure is emerging, which actor introduced it, or which earlier
   event was its root cause.  This document specifies an AgentOps
   observability event model and processing requirements for
   interoperable early failure detection and post-failure root-cause
   attribution.  It defines common event, anomaly, assertion, and
   diagnosis records; distinguishes causal origins from propagated
   symptoms; and provides the evidence model required by separate
   benchmarks of detection lead time, responsible-actor attribution, and
   root-cause localization.  The model is transport-neutral and can be
   carried by existing telemetry systems.
- **draft-rescorla-anonymous-webbotauth-01** (new-draft, score 8, core_identity) [none]: [Anonymous Bot Authentication: Authorization and Rate Limiting for Web Agents](https://datatracker.ietf.org/doc/draft-rescorla-anonymous-webbotauth/) — Automated agents ("bots") represent a large fraction of the traffic
   to many Web sites.  In some cases, this traffic is desired, in others
   undesired, and in yet others, desired as long as it remains within
   certain rate limits.  This memo describes Anonymous Bot
   Authentication (ABA), a system that allows Web site operators to
   distinguish wanted from unwanted traffic, while not tying a given
   request to a specific sender.
- **draft-sun-nmop-agent-lifecycle-management-00** (new-draft, score 8, core_identity) [none]: [The requirements of Agent Lifecycle Management](https://datatracker.ietf.org/doc/draft-sun-nmop-agent-lifecycle-management/) — As agents evolve from auxiliary analysis toward autonomous decision-
   making and task execution, their operation involves multiple dynamic
   factors, including models, knowledges, metrics, tools, permissions,
   behaviors, and collaborative relationships.  Traditional management
   methods are no longer sufficient to ensure their secure and stable
   operation.  This draft proposes an agent lifecycle management
   requirement covering registration and publication, deployment and
   operation, continuous operations, capability evolution, deactivation,
   and retirement.  It analyzes key management requirements related to
   assets, capabilities, knowledge, tools, identity and authorization,
   operational evaluation, auditing, and version evolution and
   retirement, providing the unified management, continuous governance,
   and large-scale deployment of agents.
- **draft-thallapelly-oasnt-00** (new-draft, score 8, authorization) [none]: [OASNT: Attested Action Authorization Tokens](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt/) — This document defines the OASNT token, a compact JWS-based credential
   in which a hardware-bound device key attests that a specific human,
   on a device whose runtime integrity was assessed, authorized one
   specific action whose human-readable disclosure is cryptographically
   bound to the token (What You See Is What You Sign).  Tokens are
   single-use, short-lived, and may additionally be bound to one
   concrete HTTP request.
- **draft-zagarella-autonomy-governor-00** (new-draft, score 8, authorization) [none]: [Pre-Action Risk-Graded Assurance for Agent Interactions](https://datatracker.ietf.org/doc/draft-zagarella-autonomy-governor/) — Governance of autonomous agents today is largely expressed as
   boundary enforcement: an action is permitted or blocked at the point
   it is attempted, per a policy evaluated at that boundary.  As agents
   span heterogeneous action types — authenticating a human, executing a
   delegated task, selecting a computational resource — a single,
   uniform way to express "how much assurance this action requires,
   before it proceeds" is missing.

   This document describes an interface for pre-action, risk-graded
   assurance: a policy stage that, before an agent action proceeds,
   derives an assurance requirement from a risk signal and expresses
   that requirement in a domain-appropriate form, recording the decision
   in an audit record and optionally binding it to a verified human
   root.  It defines the interface and the audit-record fields, not any
   particular risk-scoring method or control law.

   This document is offered as input to the proposed AUDIT working
   group's work on authorization state over time and action provenance.
- **draft-feng-nmop-naim-mcp-00** (new-draft, score 7, adjacent_watchlist) [none]: [Implementing the NAIM Framework over the Model Context Protocol](https://datatracker.ietf.org/doc/draft-feng-nmop-naim-mcp/) — NAIM (Natural AI Interface Modeling) is a semantic intermediate
   representation framework for AI-assisted network management.  It
   consists of two specifications: a core specification [NAIM-CORE] that
   defines the NAIM Document format, YANG-aware node templates, type
   representation, and design-time Skills A-D; and an operations
   specification [NAIM-OP] that defines the Operation IR, runtime
   execution semantics, transaction and compensation model, and runtime
   Skills E-F.

   The Model Context Protocol (MCP) has emerged as the dominant standard
   for AI hosts to discover and invoke external capabilities.  However,
   MCP delegates semantic understanding entirely to the AI model through
   natural language Tool descriptions, which is insufficient for the
   structured precondition checking, constraint validation, and
   compensation logic that reliable network management requires.

   This document specifies how the NAIM framework is implemented over
   MCP.  It defines the Originator/Handler architectural split, the MCP
   Resources through which NAIM LLM Context Views are distributed, the
   minimal MCP Tool surface through which Operation IRs are submitted,
   and the complete interaction flow from natural language intent to
   validated network execution.  This document is self-contained with
   respect to the MCP integration architecture; it references
   [NAIM-CORE] and [NAIM-OP] for the NAIM Document format, Operation IR
   structure, and execution engine semantics, which are not redefined
   here.
- **draft-fu-sidrops-rpki-repositories-monitoring-01** (new-draft, score 7, authorization) [none]: [Operational Monitoring of RPKI Repositories' Health and Safety](https://datatracker.ietf.org/doc/draft-fu-sidrops-rpki-repositories-monitoring/) — The Resource Public Key Infrastructure (RPKI) relies on a globally
   distributed set of repositories to deliver signed routing
   authorization data to Relying Parties (RPs).  Internet Service
   Providers (ISPs) depend on RPs to collect RPKI objects from
   distributed repositories and validate them cryptographically,
   resulting in hundreds of thousands of Validated Route origin
   authorization Payloads (VRPs).  Nevertheless, even with multiple RPs
   deployed, ISPs have limited insight into the operational health and
   reliability of each Publication Point (PP).  When a large number of
   RPKI objects change unexpectedly, operators often lack sufficient
   visibility into individual PPs to determine the source of the
   changes.  Consequently, ISPs cannot easily determine whether these
   changes are caused by routine updates, malicious behavior, or
   underlying repository instability.

   This document provides operational guidance for monitoring the health
   and safety of RPKI repositories on a per-publication point basis.  It
   defines measurable indicators related to reachability, availability,
   and content integrity, and explains how these metrics can be used to
   detect degraded performance or potentially unsafe repository
   behavior.  The document discusses and provides recommendations for
   repositories alerting and operational response.  The goal is to
   improve the transparency, operational availability and security of
   the RPKI ecosystem.
- **draft-hwang-silp-protocol-02** (new-draft, score 7, adjacent_watchlist) [none]: [Semantic Interlingua Layer Protocol (SILP): A Payload Codec for Cross-Model Agent Communication](https://datatracker.ietf.org/doc/draft-hwang-silp-protocol/) — This document specifies the Semantic Interlingua Layer Protocol
   (SILP), a black-box, text-interface payload codec designed for cross-
   model agent-to-agent communication.  SILP defines a coarse-grained
   action-slot intermediate representation (IR) as the reference
   semantic layer and compiles it into multiple pluggable surface
   frontends -- code-like function-call syntax, pure JSON, natural
   language, and ML-compressed text.  SILP is designed as a payload-
   layer option within existing agent transport protocols such as the
   Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocol, which
   define transport envelopes and capability discovery but leave payload
   encoding unspecified.

   SILP provides compile/decode round-trip guarantees for lossless
   frontends, dynamic frontend negotiation via probe messages, session
   management with heartbeat renewal, and a verb whitelist verified
   across six production tokenizers for cross-model token-level
   stability.

   This document is a product of independent research and is not an IETF
   standard.  It is published as an Informational document to establish
   a stable reference for implementers.
- **draft-ietf-ocm-open-cloud-mesh-06** (new-draft, score 7, authorization) [ocm]: [Open Cloud Mesh](https://datatracker.ietf.org/doc/draft-ietf-ocm-open-cloud-mesh/) — Open Cloud Mesh (OCM) is a server federation protocol that is used to
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
- **draft-schrock-ep-bounded-capability-receipts-00** (new-draft, score 7, authorization) [none]: [Bounded Capability Receipts and Durable Spend Control for Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-capability-receipts/) — Agents sometimes need bounded authority to perform more than one
   consequential action without obtaining a new human approval for every
   operation.  A signed token alone cannot enforce a shared budget
   across replicas, survive retries safely, or distinguish an operation
   that never crossed an effect boundary from one whose outcome is
   unknown.

   This document defines a bounded capability receipt and a durable
   reserve-execute-commit protocol.  The receipt binds an issuance
   authorization, a closed action scope, a budget with explicit units, a
   holder proof, an expiry, and any parent capability.  The state
   protocol atomically refuses overspend and replay, fences concurrent
   owners, and charges an indeterminate operation when an external
   effect may have occurred.  It also defines narrowing-only delegation
   and evidence interfaces.  It does not make a bearer token into human
   approval, does not provide offline global double-spend prevention,
   and does not claim that an authorized action was safe, lawful, or
   successfully executed.
- **draft-singh-psi-01** (new-draft, score 7, adjacent_watchlist) [none]: [Proof of Sovereign Integrity (PSI): A Cryptographic Protocol for Verifiable AI Regulatory Compliance](https://datatracker.ietf.org/doc/draft-singh-psi-01/) — This document specifies the Proof of Sovereign Integrity (PSI)
   Protocol, version 1.2, a cryptographic framework enabling
   organizations to prove compliance with AI regulations (including
   the EU AI Act 2024/1689, NIST AI RMF, UK AI Safety Institute
   guidelines, and equivalent frameworks) without disclosing
   proprietary model architectures, training data, or inference logic.

   PSI achieves this through a combination of SHA-256 hash-chained
   audit trails, Ed25519 digital signatures, Merkle inclusion proofs,
   Groth16-compatible zero-knowledge commitments over BN128 fields,
   and a 3-node Multi-Party Computation (MPC) consensus mechanism
   with 2/3 threshold verification.
- **draft-venkateswaran-jamwal-twophp-01** (new-draft, score 7, adjacent_watchlist) [none]: [2-Phase HTTP Protocol for Distributed Transaction Tracking (2PHP-DTT)](https://datatracker.ietf.org/doc/draft-venkateswaran-jamwal-twophp/) — This document specifies the 2-Phase HTTP Protocol for Distributed
   Transaction Tracking (2PHP-DTT), a backward-compatible, opt-in
   extension to HTTP mutation semantics that introduces a two-phase
   handshake at service request boundaries. 2PHP ensures that a mutation
   request is durably registered on both the client and the server
   before any processing commences, addressing a structural gap in
   existing HTTP REST semantics where no standard mechanism exists to
   confirm bilateral intent registration prior to execution.

   The acronym DTT expands to Distributed Transaction Tracking.  2PHP is
   not Two-Phase Commit (2PC).  Microservices architectures deliberately
   avoid the cross-service locking and blocking that 2PC requires. 2PHP
   standardizes the intent-tracking pattern that implementations
   currently build ad hoc, providing a common wire contract and a
   queryable ledger of registered intent without introducing a
   distributed transaction coordinator.

   A primary motivator for this work is the growing use of agent-driven
   HTTP invocations, including Model Context Protocol (MCP) tool calls
   and agent-to-agent (A2A) integrations.  When an agent does not
   receive a response, its default behavior is to retry.  Absent a
   queryable record of prior intent, retries pile onto services that may
   already be overwhelmed, causing deadlocks, resource exhaustion, and
   full outages. 2PHP's Phase 1 ledger record enables the client to
   inspect whether the prior intent was registered before issuing a
   retry, breaking the retry-storm feedback loop at the protocol layer.

   2PHP operates at the HTTP protocol layer, requires no new transport
   mechanisms, and is composable across independently operating service
   boundaries.  This document further defines a standardized Intent
   Ledger model for durable, queryable, cross-service correlation of
   request intent, distinct from execution telemetry provided by
   distributed tracing systems.

   This document does not claim novelty over existing intent-tracking,
   idempotency, or distributed-tracing patterns.  Its goal is to define
   a common HTTP-layer wire contract and a common ledger schema so that
   a single reference implementation--packaged as a library or framework
   module--can serve multiple deployments, replacing the per-team ad hoc
   implementations that currently reinvent this pattern.

   This document defines the protocol headers, phase state machine,
   idempotency and replay behavior, the three-tier Intent Ledger
   architecture, cross-service correlation model, and IANA registration
   of the associated HTTP header fields. 2PHP-DTT targets the
   synchronous request-response boundary, where no standard
   acknowledgement primitive exists to confirm bilateral intent
   registration before processing.  Asynchronous HTTP patterns -- 202
   Accepted with Location-based polling in HTTP Semantics, Prefer:
   respond-async negotiation, webhooks, and message-broker delivery --
   already provide durable acknowledgement of intent by construction,
   and are therefore out of scope for this specification.

## Monitor

- **draft-ietf-cose-hpke-pq-pqt-01** (new-draft, score 6, verifiable_claims) [cose]: [COSE HPKE PQ & PQ/T Algorithm Registrations](https://datatracker.ietf.org/doc/draft-ietf-cose-hpke-pq-pqt/) — This document registers Post-Quantum (PQ) and Post-Quantum/
   Traditional (PQ/T) hybrid algorithm identifiers for use with CBOR
   Object Signing and Encryption (COSE), building on the Hybrid Public
   Key Encryption (HPKE) framework.
- **draft-ietf-dtn-adm-yang-07** (new-draft, score 6, core_identity) [dtn]: [DTNMA Application Data Model (ADM) YANG Syntax](https://datatracker.ietf.org/doc/draft-ietf-dtn-adm-yang/) — This document defines a concrete syntax for encoding a Delay-Tolerant
   Networking Management Architecture (DTNMA) Application Data Model
   (ADM) using the syntax and modular structure, but not the full data
   model, of YANG.  Extensions to YANG are defined to capture the
   specifics needed to define DTNMA Application Management Model (AMM)
   objects and to use the Application Resource Identifier (ARI) data-
   value syntax.
- **draft-ietf-dtn-ari-09** (new-draft, score 6, core_identity) [dtn]: [DTNMA Application Resource Identifier (ARI)](https://datatracker.ietf.org/doc/draft-ietf-dtn-ari/) — This document defines the structure, format, and features of the
   naming scheme for the objects defined in the Delay-Tolerant
   Networking Management Architecture (DTNMA) Application Management
   Model (AMM), in support of challenged network management solutions
   described in the DTNMA document.

   This document defines the DTNMA Application Resource Identifier
   (ARI), using a text-form based on the common Uniform Resource
   Identifier (URI) and a binary-form based on Concise Binary Object
   Representation (CBOR).  These meet the needs for a concise, typed,
   parameterized, and hierarchically organized set of managed data
   elements.
- **draft-ietf-ippm-encrypted-pdmv2-14** (new-draft, score 6, authorization) [ippm]: [IPv6 Performance and Diagnostic Metrics Version 2 (PDMv2) Destination Option](https://datatracker.ietf.org/doc/draft-ietf-ippm-encrypted-pdmv2/) — RFC 8250 defines an IPv6 Destination Option that carries Performance
   and Diagnostic Metrics (PDM) such as sequence numbers and timing
   information.  While useful for measurement and troubleshooting,
   clear-text PDM data may expose operational characteristics of
   endpoints and networks.

   This document defines PDMv2, a revised version of PDM that introduces
   a registration-based security model.  Instead of specifying
   cryptographic algorithms or inline key negotiation, PDMv2 relies on a
   prior registration process to authenticate entities, authorize
   participation, and establish shared secrets.  These secrets are then
   used by endpoints and authorized analyzers to protect and interpret
   PDMv2 data according to local policy.

   This document specifies the PDMv2 semantics, header structure, and
   operational model.  Cryptographic algorithms, key derivation
   functions, and cipher negotiation are explicitly out of scope.
- **draft-ietf-jose-json-proof-algorithms-14** (new-draft, score 6, verifiable_claims) [jose]: [JSON Proof Algorithms](https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/) — The JSON Proof Algorithms (JPA) specification registers cryptographic
   algorithms and identifiers to be used with the JSON Web Proof, JSON
   Web Key (JWK), and COSE specifications.  It defines IANA registries
   for these identifiers.
- **draft-ietf-nmop-message-broker-telemetry-message-05** (new-draft, score 6, trust_infrastructure) [nmop]: [Extensible YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-ietf-nmop-message-broker-telemetry-message/) — This document defines an extensible message schema in YANG to be used
   at data collection to transform Network Telemetry messages into
   external systems such as Message Brokers.  The extensible message
   schema enables data collectors to add metadata for the provenance of
   the operational network data.
- **draft-ietf-stir-8588bis-02** (new-draft, score 6, core_identity) [stir]: [Personal Assertion Token (PaSSporT) Extension for Signature-based Handling of Asserted information using toKENs (SHAKEN)](https://datatracker.ietf.org/doc/draft-ietf-stir-8588bis/) — This document extends the Personal Assertion Token (PASSporT), which
   is a token object that conveys cryptographically signed information
   about the participants involved in communications.  The extension is
   defined based on the "Signature-based Handling of Asserted
   information using toKENs (SHAKEN)" specification by the ATIS/SIP
   Forum IP-NNI Task Group.  It provides both (1) a specific set of
   levels of confidence in the correctness of the originating identity
   of a call originated in a SIP-based telephone network as well as (2)
   an identifier that allows the Service Provider (SP) to uniquely
   identify the origin of the call within its network.  This document
   obsoletes RFC8588.
- **draft-jiang-anima-traffic-management-in-aidc-00** (new-draft, score 6, ai_infrastructure) [none]: [The Use Case of Autonomic Traffic Management in the Artificial Intelligence Data Center](https://datatracker.ietf.org/doc/draft-jiang-anima-traffic-management-in-aidc/) — This document describes the use case of autonomic traffic management
   in the Artificial Intelligence Data Center (AIDC), including the
   requirements and two management mechanisms, based on the distributed
   model and the centralized controlling model.  It proposed to use the
   IETF GRASP protocol for the information exchanging, resource
   negotiation, control signalling, and etc.
- **draft-li-sidrops-pqrpki-00** (new-draft, score 6, core_identity) [none]: [Post-Quantum Authentication for the Resource Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-li-sidrops-pqrpki/) — The Resource Public Key Infrastructure (RPKI) authenticates Internet
   number resource holdings and routing authorizations with classical
   (RSA) signatures.  Because every relying party repeatedly fetches and
   validates the complete global repository, replacing each per-object
   signature with a larger post-quantum signature would multiply
   repository size and validation cost.

   This document specifies pqRPKI, an additive post-quantum
   authentication layer for the RPKI.  Instead of re-signing every
   object, each Certification Authority (CA) authenticates its complete
   published state with a single post-quantum signature over a Merkle
   Tree Ladder whose leaf order and leaf commitments are taken directly
   from the CA's existing Manifest.  A new signed object, the pqRPKI
   Ladder Object (PQLO), carries the ladder root, the Manifest binding,
   an optional aggregate binding the CA's children, and -- for a Trust
   Anchor or a CA holding its own post-quantum key -- the post-quantum
   signature; a CA operated by its parent is authenticated through the
   parent's aggregate instead.  Existing RPKI objects are unchanged and
   legacy relying parties are unaffected by the PQLO, which no Manifest
   lists, while upgraded relying parties validate the same repository
   contents with post-quantum authentication.  This document updates RFC
   9286 to permit index-preserving placeholder Manifest entries and the
   pqRPKI file-name extension.
- **draft-li-zt-consideration-04** (new-draft, score 6, adjacent_watchlist) [none]: [Consideration of Applying Zero Trust Philosophy in Network Infrastructure](https://datatracker.ietf.org/doc/draft-li-zt-consideration/) — Network security has traditionally relied on a perimeter-centric
   model, assuming that traffic originating within the network can be
   implicitly trusted.  This model is fundamentally challenged by
   modern, highly distributed, and software-driven network environments
   where internal compromise is a realistic and high-impact threat
   scenario.  This document examines the critical limitations of edge-
   only network protection and the systemic risks that arise from
   insufficient internal validation.  Once the network perimeter is
   bypassed, the absence of internal protection mechanisms facilitates
   rapid lateral movement, impersonation of network entities, and
   interference with critical control and management functions.

   The document argues that Zero Trust (ZT) principles, which mandate
   continuous, dynamic verification of all entities and communications
   regardless of network location, are necessary to address contemporary
   threat models.  Deploying ZT-aligned network protection mechanisms
   beyond the network edge is essential to build resilient,
   controllable, and trustworthy networks.
- **draft-liu-icnrg-cross-domain-compute-discovery-01** (new-draft, score 6, core_identity) [none]: [Requirements for Name-Based Compute-Service Discovery in Heterogeneous Space-Terrestrial-Maritime Edge Networks](https://datatracker.ietf.org/doc/draft-liu-icnrg-cross-domain-compute-discovery/) — Future edge systems may span terrestrial infrastructure, maritime
   gateways, and non-terrestrial nodes such as low-Earth-orbit
   satellites.  In these environments, a computing service, its
   executable instances, input data, and reusable results may be
   distributed across intermittently connected and resource-constrained
   nodes.  This document describes a problem statement, an illustrative
   network model, and requirements for name-based discovery of computing
   services and reusable results.  The objective is to separate stable
   service identity from temporary execution location while supporting
   disruption awareness, metadata authenticity, controlled result reuse,
   and incremental deployment over existing IP and Information-Centric
   Networking infrastructures.  This document does not define a wire
   protocol, a naming syntax, or a traffic-steering algorithm.
- **draft-lohmann-qikvrt-effect-ack-01** (new-draft, score 6, authorization) [none]: [QIK-VRT Effect Acknowledgement: Separating Receipt from Authorization for Downstream Effect](https://datatracker.ietf.org/doc/draft-lohmann-qikvrt-effect-ack/) — Transport acknowledgements establish technical receipt; they do not
   establish that a received information unit is understood, policy-
   compliant, or authorized to produce a downstream effect.  This
   document defines an Experimental application-layer control record,
   called EFFECT_ACK, that separates receipt from effect authorization.

   The protocol has five closed version-1 outcomes.  Ordinary downstream
   release is permitted only for EFFECT_ACK_DONE and only after
   validation of the record, its policy and evidence bindings, its
   freshness, and its authenticated origin.  This document specifies the
   state-selection algorithm, version handling, a deterministic JSON
   representation, hash chaining, timeout behavior, conformance
   requirements, and security and privacy boundaries.

   This protocol does not modify TCP, QUIC, or the OSI model; does not
   solve the halting problem; and does not establish the truth of
   external evidence.  It provides a machine-checkable authorization
   boundary under explicitly stated deployment assumptions.
- **draft-mcguinness-oauth-token-exchange-cnf-00** (new-draft, score 6, authorization) [none]: [Confirmation Response Parameter for OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-token-exchange-cnf/) — This specification defines a cnf response parameter for the OAuth 2.0
   Token Exchange (RFC 8693) response.  The parameter carries the
   confirmation method that the authorization server applied to the
   issued token, enabling clients to verify that sender-constraint
   binding (for example a DPoP key or mutual-TLS client certificate) was
   performed without inspecting the issued token.  This is useful for
   opaque tokens, encrypted tokens, or any other case where the client
   cannot read the issued token's cnf claim directly.
- **draft-mpsb-agntcy-slim-02** (new-draft, score 6, adjacent_watchlist) [none]: [Secure Low-Latency Interactive Messaging (SLIM)](https://datatracker.ietf.org/doc/draft-mpsb-agntcy-slim/) — This document specifies the Secure Low-Latency Interactive Messaging
   (SLIM), a protocol designed to support real-time interactive AI
   applications at scale.  SLIM provides the transport layer for agent
   protocols (for example, A2A and MCP), combining gRPC over HTTP/2 and
   HTTP/3 with secure messaging, group communication, and native RPC
   semantics.  The protocol provides mechanisms for connection
   management, stream multiplexing, and flow control while maintaining
   compatibility with existing gRPC deployments and supporting end-to-
   end encryption via MLS.
- **draft-norton-sdlp-overview-01** (new-draft, score 6, core_identity) [none]: [SDLP RFC 0: Overview and Architecture](https://datatracker.ietf.org/doc/draft-norton-sdlp-overview/) — This document presents an architectural overview of the Secured
   Digital Lifecycle Protocol (SDLP). SDLP defines a structured model
   for representing, identifying, tracking, and securing digital
   objects across their lifecycle. This overview summarizes the SDLP
   object model, explains how identity, lineage, lifecycle, and
   security architecture interrelate, and outlines the rationale for
   defining SDLP through multiple coordinated specifications. It
   serves as the entry point for understanding the SDLP framework.
- **draft-norton-sdlp-phys-00** (new-draft, score 6, core_identity) [none]: [SDLP Physics Specification](https://datatracker.ietf.org/doc/draft-norton-sdlp-phys/) — The Secured Digital Lifecycle Protocol (SDLP) defines a physics layer
   for digital objects: a set of non-negotiable behavioral laws that
   govern identity stability, lineage integrity, lifecycle determinism,
   and irreversible state transitions. SDLP Physics establishes how
   object security depletes, transforms, or terminates as an object is
   activated, used, or shared, ensuring that each operation consumes or
   alters the object’s allowable state in predictable ways.

   These laws prevent cloning, enforce legitimate descent, bind objects
   to their environments, and guarantee that destruction and zeroization
   are final. This document specifies the core physics that underpin
   SDLP’s security model and define how digital objects behave across all
   environments and distribution paths.

This Internet-Draft is submitted in full conformance with the
provisions of BCP 78 and BCP 79.

Internet-Drafts are working documents of the Internet Engineering Task
Force (IETF), its areas, and its working groups. Note that other groups
may also distribute working documents as Internet-Drafts.

Internet-Drafts are draft documents valid for a maximum of six months
and may be updated, replaced, or obsoleted by other documents at any
time. It is inappropriate to use Internet-Drafts as reference material
or to cite them other than as "work in progress."

The list of current Internet-Drafts can be accessed at:
https://www.ietf.org/1id-abstracts.html

The list of Internet-Draft Shadow Directories can be accessed at:
https://www.ietf.org/shadow.html
- **draft-sabey-refusal-transparency-02** (new-draft, score 6, trust_infrastructure) [none]: [Refusal Transparency: Signed, Replay-Resistant Evidence of Refused Agent-System Transitions](https://datatracker.ietf.org/doc/draft-sabey-refusal-transparency/) — A governance system for autonomous agents is defined as much by what
   it refuses as by what it permits, yet refusals are the one behavior
   vendors only ever assert.  A Refusal Digest is a portable, signed
   JSON document recording one adversarial probe run against a live
   agent-governance system: for every attack attempted, the system's
   verbatim refusal ground, the event types the attack would have
   recorded had it succeeded, and the complete signed event ledger of
   the attempt — in which the refused transition is provably absent.
   Digests verify offline, by parties who do not operate the probed
   system, using only the issuer's public key.  From version 0.2, every
   quantity that varies between runs derives deterministically from a
   per-run seed carried in the digest, so a relying party can recompute
   the derivations and a replayed or pre-recorded ledger cannot match a
   fresh digest.  This document specifies the digest wire format, its
   canonicalization and signature scheme, the seeded-variation
   derivations, and the verification algorithm.  Where succession
   receipts prove that an agent legitimately became the holder of an
   authority, refusal digests prove what the governing system declined
   to let happen.
- **draft-singh-apex-psi-09-00** (new-draft, score 6, core_identity) [none]: [PSI-09: Age Assurance Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-09/) — PSI-09 defines a signed verdict format for distributed tribunal
   proceedings conducted under the Apex Protocol.  A verdict carries the
   case identifier, the predicate chain that produced it, the ruling,
   the evidence anchors, and the dissenting opinion if any.
- **draft-skyfire-oauth-amr-values-01** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-01** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-varnagy-iid-protocol-00** (new-draft, score 6, core_identity) [none]: [Internet Identity Protocol (IID)](https://datatracker.ietf.org/doc/draft-varnagy-iid-protocol/) — This document specifies the IID protocol, which defines message
   formats and operations for managing personal data, permissions, and
   attributes associated with internet identities, including natural
   persons, organizations and artificial intelligence agents.

   The protocol is designed to be simple, extensible, platform-
   independent, and human readable.  It is transport-agnostic and
   supports arbitrary cryptographic algorithms.
- **draft-yossif-agent-mandate-problem-00** (new-draft, score 6, adjacent_watchlist) [none]: [Problem Statement: Verifiable Human Mandates for Autonomous Agent Actions](https://datatracker.ietf.org/doc/draft-yossif-agent-mandate-problem/) — An autonomous software agent commonly acts under authority a human
   granted at an earlier moment: the human expresses and authorizes an
   intent at one time, and the agent executes one or more concrete
   actions at a later time.  The credentials and session state the agent
   carries at execution time establish that some agent is authorized to
   act, but they do not establish that this specific action, with these
   specific parameters, falls within the constraints the human actually
   signed.  As agent autonomy and action throughput grow, the population
   of executed actions that no human individually bounded grows with it.
   This document is a problem statement.  It characterizes the gap
   between an authorized agent and an authorized action, explains why
   existing delegation, logging, and payment-mandate mechanisms do not
   close it, and states the requirements any solution would have to
   satisfy.  It defines no protocol or mechanism.
- **draft-yu-dmsc-ai-agent-use-cases-in-6g-02** (new-draft, score 6, agent_identity) [none]: [AI Agent Use Cases and Requirements in 6G Network](https://datatracker.ietf.org/doc/draft-yu-dmsc-ai-agent-use-cases-in-6g/) — This draft introduces use cases related to AI Agents in 6G networks,
   primarily referencing the technical report of 3GPP SA1 R20 Study on
   6G Use Cases and Service Requirements (TR 22.870).  It also
   elaborates on some of the requirements for introducing AI Agents into
   6G networks from the perspective of operators.
- **draft-zundel-vdcarch-00** (new-draft, score 6, verifiable_claims) [none]: [A reference architecture for direct presentation credential flows](https://datatracker.ietf.org/doc/draft-zundel-vdcarch/) — This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.
- **draft-aravind-oauth-decision-subject-00** (new-draft, score 5, authorization) [none]: [Decision-Subject Representation for Agent Authorization](https://datatracker.ietf.org/doc/draft-aravind-oauth-decision-subject/) — This document defines dsub, an OPTIONAL, descriptive claim naming the
   *decision subject*, the party an automated agent's action is taken
   _upon_, as distinct from the acting agent (act) and the delegating
   principal (sub).  Its purpose is *audit legibility*: letting a record
   name the party a decision concerns, which is the precondition for
   that record ever being made legible to them.  The claim is privacy-
   minimizing by construction and is NOT an input to the authorization
   decision; a Policy Decision Point MUST ignore it.  This document
   defines representation only.
- **draft-ferro-apertomemory-01** (new-draft, score 5, verifiable_claims) [none]: [The ApertoMemory Format: Portable, Client-Side-Encrypted AI Memory](https://datatracker.ietf.org/doc/draft-ferro-apertomemory/) — AI assistants and agents accumulate long-term memory about their
   users.  This memory is typically stored in proprietary, provider-held
   silos: it cannot be moved between tools, its integrity cannot be
   verified, and its confidentiality depends entirely on the provider.
   This document specifies the ApertoMemory format: a canonical, signed,
   client-side-encrypted representation of AI memory objects, together
   with a portable single-file export container.  Memory objects are
   encoded in deterministic CBOR, signed with COSE_Sign1, and encrypted
   with COSE_Encrypt0 under keys derived from and controlled by the
   user.  A storage or synchronisation server handling ApertoMemory
   objects has zero access to their content, authorship, or semantic
   timestamps.
- **draft-ietf-dtn-amm-07** (new-draft, score 5, adjacent_watchlist) [dtn]: [DTNMA Application Management Model (AMM) and Data Models](https://datatracker.ietf.org/doc/draft-ietf-dtn-amm/) — This document defines a model that captures the information necessary
   to asynchronously manage applications within the Delay-Tolerant
   Networking Management Architecture (DTNMA).  This model provides a
   set of common managed object types, data types and structures, and a
   template for information needed within each application data model.
   The built-in definitions are made to be extensible by applications
   without needing to modify core Agent or Manager behavior.
- **draft-mcw-opsawg-icon-requirements-01** (new-draft, score 5, agent_identity) [none]: [Architecture and Requirements for Observability, Control and Intervention of Network Management Agents](https://datatracker.ietf.org/doc/draft-mcw-opsawg-icon-requirements/) — This document defines architecture and a set of requirements for
   Observability, Control, and Intervention for Network Management
   Agents.

   It identifies gaps in existing mechanisms and specifies required
   interaction capabilities between Agent supervision systems and
   network management agents across multi-vendor environments,
   specifically observability, control, and runtime intervention.  The
   requirements aim to guarantee comprehensive, lifecycle control over
   AI agents and enable observation, constraint, intervention, and
   correction to ensure network operational resilience and continuity.
- **draft-schrock-ep-authority-introduction-01** (new-draft, score 5, adjacent_watchlist) [none]: [Authority Documents and Scoped Authority for Agent-Action Evidence](https://datatracker.ietf.org/doc/draft-schrock-ep-authority-introduction/) — Signature verification answers whether a key produced an artifact.
   It does not answer why a relying party accepts that key, or whether
   the key holder had authority for the action.  This document specifies
   two composable artifacts.  An Authority Document introduces and
   rotates an organization's evidence-issuing keys through a signed,
   hash-chained sequence.  A Scoped Authority Proof records the
   authority held by a subject at a registry snapshot, including role,
   action scope, material limits, policy binding, validity, and
   revocation status.  A relying party evaluates both artifacts under
   its own pinned trust inputs and policy.  The design does not make a
   self-presented key authoritative, does not turn log inclusion or
   domain control into automatic trust, and does not equate a valid
   signature with permission to act.
- **draft-singh-apex-psi-08-00** (new-draft, score 5, trust_infrastructure) [none]: [PSI-08: Health Records Access Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-08/) — PSI-08 specifies a format for composing multiple Digital Gallows
   predicates into a verifiable chain.  Each link in the chain is a
   signed predicate output that serves as input to the next, enabling
   verifiable multi-step inference without a trusted intermediary.
- **draft-singh-webbotauth-hosted-directories-00** (new-draft, score 5, adjacent_watchlist) [none]: [Hosted Key Directories for Web Bot Auth](https://datatracker.ietf.org/doc/draft-singh-webbotauth-hosted-directories/) — Web Bot Auth authenticates automated clients to origins using HTTP
   Message Signatures, with verification keys published in a key
   directory at a well-known URI.  Current drafts assume that each agent
   operator hosts its own key directory.  A large and growing population
   of agents is operated by individuals and small organizations for whom
   hosting a directory is impractical, and whose legitimate traffic is
   otherwise indistinguishable from abusive automation.

   This document describes the hosted (multi-tenant) key directory
   deployment model, in which a registry operator publishes key
   directories on behalf of many independent agent operators while the
   operators retain exclusive custody of their private keys.  It
   analyzes principal mapping, proof of key possession, freshness, and
   accountability in this model; reports interoperability observations
   from an independent implementation; and offers operational guidance
   for hosted directory operators and for verifiers.  It is intended as
   input to the Web Bot Auth working group's operational and deployment
   guidance.
- **draft-song-ina-framework-00** (new-draft, score 5, core_identity) [none]: [A Unified Bitmap Framework for In-Network Aggregation and Multicast](https://datatracker.ietf.org/doc/draft-song-ina-framework/) — Collective communication is a critical performance bottleneck for
   distributed deep learning and large model training and inference in
   data centers for AI computing.  In-Network Aggregation (INA) has been
   identified as an effective accelerating technique to improve its
   performance.  This draft describes a flexible and efficient INA
   framework for packet routing and forwarding in which a tree is
   encoded by a bitmap and the same bitmap is reused for data movement
   in both directions, with the multicast direction realized by a
   stateless bitmap-driven forwarding mechanism that adopts an encoding
   and replication behavior similar to BIER.  The bitmap encoding is
   compact, hardware friendly, exact and self-describing, and, being
   carried per packet, supports highly dynamic endpoint sets without any
   signaling to the network.

   The framework is applied to three use cases.  The first is AllReduce,
   used in model training, which performs an in-network aggregation
   toward the root followed by a multicast of the result back to the
   workers.  The second is the dispatch and combine operations of
   Mixture-of-Experts (MoE) expert parallelism, which performs a dynamic
   multicast of tokens to the selected experts followed by an in-network
   aggregation of the expert outputs.  In both use cases a single
   bitmap-encoded tree drives both directions.  The third use case is
   for reliable multicast, which aggregates the acknowledgments of all
   multicast receivers in the network to avoid ACK implosion; its ACK-
   aggregation tree can be either pre-configured, as in the AllReduce
   use case, or self-installed by the data multicast itself, as in the
   MoE use case.

   The draft further analyzes why the base BIER architecture alone
   cannot realize the framework and identifies the per-packet
   information an INA encapsulation must carry beyond the endpoint-set
   encoding: a direction indicator, a job identifier, a sequence number,
   and an encoding-type indicator.  It also examines the efficiency of
   the endpoint-set encoding at scale, covering hierarchical bitmaps and
   multiple parallel trees for large dense endpoint sets, node-list
   encoding for very large domains with few active endpoints, and the
   trade-offs between header overhead and network processing complexity
   among these encodings.
- **draft-yang-6man-wide-area-packet-spraying-00** (new-draft, score 5, ai_infrastructure) [none]: [IPv6 Options for Wide-Area Packet Spraying (WPS): Group-Based Multipath Load Balancing](https://datatracker.ietf.org/doc/draft-yang-6man-wide-area-packet-spraying/) — This document specifies the Wide-area Packet Spraying (WPS) option,
   an IPv6 option that can be carried in the Destination Options header
   or, where required, the Hop-by-Hop Options header.  The option
   conveys the scheduling metadata that is needed to distribute the
   packets of a single high-volume flow across multiple parallel wide-
   area paths at the granularity of packet groups, and to restore the
   original packet ordering at the egress boundary of a controlled
   domain.  The mechanism provides order-preserving multipath load
   balancing and bandwidth aggregation for wide-area interconnection of
   distributed computing sites, such as wide-area interconnects between
   Artificial Intelligence (AI) data centers, and is intended for use
   within limited domains.
- **draft-zahed-agent-comm-framework-01** (new-draft, score 5, agent_identity) [none]: [AI Agent Interoperable Protocol Framework (AIPF)](https://datatracker.ietf.org/doc/draft-zahed-agent-comm-framework/) — The current generation of AI agent communication protocols enables
   basic tool access and inter-agent messaging, but lacks the
   architectural and protocol foundations required for open,
   interoperable, and resilient Internet-scale deployments.  This
   document presents the AI Agent Interoperable Protocol Framework
   (AIPF), a layered framework that identifies the key building blocks
   and the protocol suite required for interoperable Agent-to-agent/
   Agent-to-tool communication.
- **draft-feng-netmod-naim-01** (new-draft, score 4, adjacent_watchlist) [none]: [NAIM: A Canonical Semantic Representation for AI-Assisted YANG Modeling and Validation](https://datatracker.ietf.org/doc/draft-feng-netmod-naim/) — This document defines the NAIM (Natural AI Interface Modeling)
   framework, a canonical semantic intermediate representation between
   natural language descriptions and YANG data models (RFC 7950).

   NAIM addresses a recognized gap in the YANG authoring and network
   management workflow: direct conversion from natural language to YANG
   is error-prone because essential modeling semantics -- including
   configuration versus state distinction, list key identification,
   constraint expressions, operational preconditions, and cross-module
   relationships -- are routinely absent or ambiguous in natural
   language input.  NAIM makes these semantics explicit, structurally
   consistent, and machine-verifiable.

   This document defines: the NAIM Document format (Canonical JSON and
   derived Markdown View); the LLM Context View for AI prompt context
   distribution; the three-layer architecture (Specification, Skill,
   Tool); Skills A-D for conversational modeling, summarization, YANG
   generation, and reverse engineering; and the Validation-Reflection-
   Retry mechanism for AI output quality control.

   The NAIM Document format is designed to serve two roles: as the
   intermediate representation for design-time YANG authoring, and as
   the runtime semantic authority against which AI-generated operation
   intents are validated.  The runtime validation usage is specified in
   [NAIM-OP]; this document defines the format, derived views, and
   design-time workflows.
- **draft-ietf-jose-json-proof-token-14** (new-draft, score 4, privacy_security) [jose]: [JSON Proof Token and CBOR Proof Token](https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/) — JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving
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
- **draft-reilly-looking-glass-00** (new-draft, score 4, adjacent_watchlist) [none]: [Project Looking Glass: An Integrative Framework for Verifiable Observability and Autonomous Self-Healing Across the Reilly Protocol Suite](https://datatracker.ietf.org/doc/draft-reilly-looking-glass/) — This document specifies Project Looking Glass, an integrative
   framework that unifies the Reilly Protocol Suite -- including the
   REM Protocol, WebProof, PLPES, CTS, AIMED/AIMED-EVAL, UAEMF, RMRP,
   SkyLedger, RLT Genesis, Machine-Web Symbiosis (MWS), and Cognitive
   Sovereignty -- into a single verifiable observability and autonomous
   self-healing architecture.  Project Looking Glass defines how a live
   production system, exemplified by the REM Protocol 14-agent
   autonomous pipeline, continuously inspects its own state ("the
   looking glass"), proves that state using Dual-Layer Digital
   Permanence (Bitcoin blockchain timestamping via OpenTimestamps plus
   DOI archival), and autonomously detects, diagnoses, and repairs
   faults without human intervention while preserving human epistemic
   authority as defined by the Cognitive Sovereignty framework.  A
   complete step-by-step implementation process is provided.
- **draft-singh-psi-01-01** (new-draft, score 4, adjacent_watchlist) [none]: [Proof of Sovereign Integrity (PSI): Protocol Specification v1](https://datatracker.ietf.org/doc/draft-singh-psi-01/) — This document specifies the Proof of Sovereign Integrity (PSI)
   Protocol for verifiable AI regulatory compliance.  Revision 01
   updates the March 2026 specification with EU AI Act Article 50
   alignment and post-quantum cryptographic requirements.

## Adjacent / watchlist

- **draft-anderson-askew-cidvv-01** (new-draft, score 3, core_identity) [none]: [Caller-ID Vouching and Vetting (CIDVV)](https://datatracker.ietf.org/doc/draft-anderson-askew-cidvv/) — Caller-ID spoofing remains a significant problem in telephony,
   particularly across inter-domain and international call paths where
   identity frameworks may not yet be fully deployed.

   This document defines *Caller-ID Vouching and Vetting (CIDVV)*, a
   lightweight verification mechanism that lets the called party ask a
   simple question:
- **draft-carpenter-anima-otp-casa-00** (new-draft, score 3, core_identity) [none]: [One-time Pad for Authorizing Device Identity](https://datatracker.ietf.org/doc/draft-carpenter-anima-otp-casa/) — This document describes how devices joining an autonomic control
   plane as defined in RFC 8994 may use the bootstrapping mechanism
   defined in RFC 8995 even if they cannot use a manufacturer-installed
   X.509 certificate.  Instead, such devices may generate a self-signed
   certificate embedding a unique token selected from a one-time pad.
- **draft-doehle-company-certs-discovery-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Well-Known URI for Discovery of Application-Specific Trust Anchors](https://datatracker.ietf.org/doc/draft-doehle-company-certs-discovery/) — This document defines the "company-certs" well-known URI in
   accordance with Request for Comments (RFC) 8615.  The URI provides a
   JSON metadata document that allows an organization to publish
   application-specific trust anchors and related revocation information
   for use by consuming applications.  The mechanism is intended for
   scoped trust bootstrapping, such as S/MIME, mutual TLS, or other
   application-local trust decisions, without modifying the global
   operating system trust store.
- **draft-farrokhi-dnsop-ede-nta-01** (new-draft, score 3, adjacent_watchlist) [none]: [Disclosure of Negative Trust Anchors in DNS Responses](https://datatracker.ietf.org/doc/draft-farrokhi-dnsop-ede-nta/) — This document describes a mechanism for disclosing that a Negative
   Trust Anchor (NTA) was in effect at the time that a DNS response was
   generated, using an Extended DNS Error (EDE).
- **draft-grant-ntp-server-identifier-extension-00** (new-draft, score 3, core_identity) [none]: [NTP Server Identifier Extension](https://datatracker.ietf.org/doc/draft-grant-ntp-server-identifier-extension/) — This document defines an extension field that allows operators of NTP
   services the ability to provide additional information about their
   services to clients which request it.
- **draft-huang-spring-pppoe-srv6-00** (new-draft, score 3, core_identity) [none]: [SRv6 for PPPoE Transport](https://datatracker.ietf.org/doc/draft-huang-spring-pppoe-srv6/) — This document proposes a method that employs SRv6 underlay tunnel to
   transport PPPoE session information across broadband networks.  By
   leveraging the programmability of SRv6 SIDs, the approach not only
   delivers trusted authentication and secure subscriber access, but
   also enables operators to offer differentiated services and flexibly
   instantiate network functions for broadband users.
- **draft-huitema-ccwg-c4-spec-04** (new-draft, score 3, adjacent_watchlist) [none]: [Specification of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-spec/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design emphasizes
   simplicity and avoids making too many assumptions about the "model"
   of the network.
- **draft-ietf-cats-oam-fw-01** (new-draft, score 3, adjacent_watchlist) [cats]: [Computing-Aware Traffic Steering (CATS) Operations, Administration, and Maintenance (OAM) Framework](https://datatracker.ietf.org/doc/draft-ietf-cats-oam-fw/) — This document describes the Operations, Administration, and
   Maintenance (OAM) framework and requirements for Computing-Aware
   Traffic Steering (CATS).  The framework defines the CATS OAM layering
   model and functional components.  It also specifies the requirements
   to enable fault management and performance monitoring for CATS end-
   to-end connections across clients, network paths, and service
   instances.
- **draft-ietf-ccamp-flexe-yang-cm-09** (new-draft, score 3, adjacent_watchlist) [ccamp]: [YANG Data Model for FlexE Management](https://datatracker.ietf.org/doc/draft-ietf-ccamp-flexe-yang-cm/) — This document defines a service provider targeted YANG data model for
   the configuration and management of a Flex Ethernet (FlexE) network,
   including FlexE group and FlexE client.
- **draft-ietf-detnet-glbf-01** (new-draft, score 3, adjacent_watchlist) [detnet]: [Deterministic Networking (DetNet) Data Plane - guaranteed Latency Based Forwarding (gLBF) for bounded latency with low jitter and asynchronous forwarding in Deterministic Networks](https://datatracker.ietf.org/doc/draft-ietf-detnet-glbf/) — This memo proposes a mechanism called "guaranteed Latency Based
   Forwarding" (gLBF) as part of DetNet for hop-by-hop packet forwarding
   with per-hop deterministically bounded latency and minimal jitter.

   gLBF is intended to be useful across a wide range of networks and
   applications with need for high-precision deterministic networking
   services, including in-car networks or networks used for industrial
   automation across on factory floors, all the way to ++100Gbps
   country-wide networks.

   Contrary to other mechanisms, gLBF does not require network wide
   clock synchronization, nor does it need to maintain per-flow state at
   network nodes, avoiding drawbacks of other known methods while
   leveraging their advantages.

   Specifically, gLBF uses the queuing model and calculus of Urgency
   Based Scheduling (UBS, [UBS]), which is used by TSN Asynchronous
   Traffic Shaping [TSN-ATS]. gLBF is intended to be a plug-in
   replacement for TSN-ATN or as a parallel mechanism beside TSN-ATS
   because it allows to keeping the same controller-plane design which
   is selecting paths for TSN-ATS, sizing TSN-ATS queues, calculating
   latencies and admitting flows to calculated paths for calculated
   latencies.

   In addition to reducing the jitter compared to TSN-ATS by additional
   buffering (dampening) in the network, gLBF also eliminates the need
   for per-flow, per-hop state maintenance required by TSN-ATS.  This
   avoids the need to signal per-flow state to every hop from the
   controller-plane and associated scaling problems.  It also reduces
   implementation cost for high-speed networking hardware due to the
   avoidance of additional high-speed speed read/write memory access to
   retrieve, process and update per-flow state variables for a large
   number of flows.
- **draft-ietf-dmm-udp-tunnel-acaas-extn-01** (new-draft, score 3, adjacent_watchlist) [dmm]: [A YANG Data Model Extension for Attachment Circuit as a Service with UDP Tunnel Support](https://datatracker.ietf.org/doc/draft-ietf-dmm-udp-tunnel-acaas-extn/) — Delivery of network services over a Layer 3 tunnel assumes that the
   appropriate setup is provisioned over links that connect the customer
   termination points and provider network.  The required setup to allow
   successful data exchange over these links is referred to as an
   attachment circuit (AC) while the underlying link for carrying
   network services is referred to as "bearer", in this case a Layer 3
   UDP tunnel.

   This document specifies an extension for UDP tunnel as Layer 3 bearer
   to the YANG service data model for AC.
- **draft-ietf-dtn-amp-04** (new-draft, score 3, adjacent_watchlist) [dtn]: [DTNMA Asynchronous Management Protocol (AMP)](https://datatracker.ietf.org/doc/draft-ietf-dtn-amp/) — This document defines a messaging protocol for the Delay-Tolerant
   Networking (DTN) Management Architecture (DTNMA) Asynchronous
   Management Model (AMM) and a transport binding for exchanging those
   messages over a network.  This Asynchronous Management Protocol (AMP)
   does not require transport-layer sessions, operates over
   unidirectional links, and seeks to reduce the energy and compute
   power necessary for performing remote management of resource
   constrained devices possibly over challenged networks.
- **draft-ietf-httpbis-connect-tcp-12** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP proxying using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this proxying functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-jmap-calendars-27** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-kitten-password-storage-11** (new-draft, score 3, adjacent_watchlist) [kitten]: [Best practices for SASL password hashing and storage](https://datatracker.ietf.org/doc/draft-ietf-kitten-password-storage/) — This document outlines best practices for handling user passwords and
   other authenticator secrets in client-server systems making use of
   SASL.
- **draft-ietf-lsr-isis-flex-algo-yang-21** (new-draft, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for IS-IS Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-flex-algo-yang/) — This document defines a YANG data model to support IS-IS Application-
   Specific Link Attributes and Flexible Algorithm.
- **draft-ietf-lsr-isis-yang-augmentation-v1-12** (new-draft, score 3, adjacent_watchlist) [lsr]: [IS-IS YANG Model Augmentations for Additional Features - Release 1](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-yang-augmentation-v1/) — This document defines YANG data modules augmenting the IETF IS-IS
   YANG model to provide support for IS-IS Minimum Remaining Lifetime as
   defined in RFC 7987, and Signaling Maximum SID Depth Using IS-IS as
   defined in RFC 8491.
- **draft-ietf-lsr-ospf-flex-algo-yang-16** (new-draft, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for OSPF Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-ospf-flex-algo-yang/) — This document defines a YANG data model to support OSPF Application-
   Specific Link Attributes and Flexible Algorithm.  It also creates the
   initial version of IANA-maintained YANG modules for IGP Algorithm
   Types, IGP Metric-Types, and IGP Link Attribute Applications.

   This document updates RFCs 8665, 9350, and 9843.
- **draft-ietf-mailmaint-imap-objectid-bis-06** (new-draft, score 3, core_identity) [mailmaint]: [IMAP Extension for Object Identifiers](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-imap-objectid-bis/) — This document defines the OBJECTID+ extension for IMAP, which
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
- **draft-ietf-masque-connect-ethernet-11** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document describes how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-masque-connect-udp-ecn-dscp-02** (new-draft, score 3, adjacent_watchlist) [masque]: [ECN and DSCP support for HTTPS's Connect-UDP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-ecn-dscp/) — HTTP's Extended Connect's Connect-UDP protocol enables a client to
   proxy a UDP flow from the HTTP server towards a specified target IP
   address and UDP port.  QUIC and Real-time transport protocol (RTP)
   are examples of transport protocols that use UDP and support Explicit
   Congestion Notification (ECN) and provide the necessary feedback.
   This document specifies how ECN and DSCP can be supported through an
   extension to the Connect-UDP protocol for HTTP without per-packet
   byte overhead, solely using Context IDs.
- **draft-ietf-sidrops-aspa-verification-27** (new-draft, score 3, authorization) [sidrops]: [BGP AS_PATH Verification Based on Autonomous System Provider Authorization (ASPA) Objects](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) — This document describes procedures that make use of Autonomous System
   Provider Authorization (ASPA) objects in the Resource Public Key
   Infrastructure (RPKI) to verify the Border Gateway Protocol (BGP)
   AS_PATH attribute of advertised routes.  This AS_PATH verification
   enhances routing security by adding means to detect and mitigate
   route leaks and AS_PATH manipulations.
- **draft-ietf-sidrops-bar-sav-10** (new-draft, score 3, authorization) [savnet]: [Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/) — Designing an efficient source address validation (SAV) filter
   requires minimizing false positives (i.e., avoiding blocking
   legitimate traffic) while maintaining directionality (see RFC8704).
   This document advances the technology for SAV filter design through a
   method that makes use of BGP UPDATE messages, Autonomous System
   Provider Authorization (ASPA), and Route Origin Authorization (ROA).
   The proposed method's name is abbreviated as BAR-SAV.  BAR-SAV can be
   used by network operators to derive more robust SAV filters and thus
   improve network resilience.  This document updates RFC8704.
- **draft-ietf-suit-update-management-14** (new-draft, score 3, core_identity) [suit]: [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/draft-ietf-suit-update-management/) — This document specifies extensions to the SUIT manifest format.
   These extensions allow an update author, update distributor or device
   operator to more precisely control the distribution and installation
   of updates to devices.  These extensions also provide a mechanism to
   inform a management system of Software Identifier and Software Bill
   Of Materials information about an updated device.
- **draft-ietf-tls-mlkem-09** (new-draft, score 3, adjacent_watchlist) [tls]: [ML-KEM Post-Quantum Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) — This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as
   NamedGroups and registers IANA values in the TLS Supported Groups
   registry for use in TLS 1.3 to achieve post-quantum (PQ) key
   establishment.
- **draft-ietf-uta-tls13-iot-profile-23** (new-draft, score 3, adjacent_watchlist) [uta]: [TLS/DTLS 1.3 Profiles for the Internet of Things](https://datatracker.ietf.org/doc/draft-ietf-uta-tls13-iot-profile/) — RFC 7925 offers guidance to developers on using TLS/DTLS 1.2 for
   Internet of Things (IoT) devices with resource constraints.  This
   document is a companion to RFC 7925, defining TLS/DTLS 1.3 profiles
   for IoT devices.  Additionally, it updates RFC 7925 with respect to
   the X.509 certificate profile and ciphersuite requirements.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/thomas-fossati/draft-tls13-iot.
- **draft-lg-bmwg-benchmarking-methodology-for-rov-03** (new-draft, score 3, authorization) [none]: [Benchmarking Methodology for Route Origin Validation (ROV)](https://datatracker.ietf.org/doc/draft-lg-bmwg-benchmarking-methodology-for-rov/) — This document defines a benchmarking methodology for routers that
   implement Route Origin Validation (ROV).  The methodology focuses on
   device-level behavior, including processing of validated Route Origin
   Authorization (ROA) payload (VRP) updates, the interaction between
   ROV and BGP, resource utilization, and the scalability of ROV under
   varying operational conditions.  The procedures described here follow
   the principles and constraints of the Benchmarking Methodology
   Working Group (BMWG) and are intended to produce repeatable and
   comparable results across implementations.
- **draft-li-cats-task-segmentation-framework-02** (new-draft, score 3, adjacent_watchlist) [none]: [A Task Segmentation Framework for Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-li-cats-task-segmentation-framework/) — This document proposes an extension to the Computing-Aware Traffic
   Steering (CATS) framework by introducing a task segmentation module.
   This extension enables the CATS framework to handle divisible
   computing requests by breaking them down into smaller computational
   units, referred to as "Task".  The document focuses on two primary
   task segmentation modes: the distributed mode and the chain-
   structured Directed Acyclic Graph (DAG) model, providing detailed
   workflows for each.
- **draft-li-coap-task-resources-01** (new-draft, score 3, adjacent_watchlist) [none]: [CoAP Extensions for Asynchronous Task Resources](https://datatracker.ietf.org/doc/draft-li-coap-task-resources/) — Many operations on constrained devices cannot complete within a
   single CoAP request and response exchange.  Examples include firmware
   installation, diagnostic procedures, commissioning, calibration, and
   physical actuation.

   This document defines a common lifecycle model for representing such
   operations as addressable CoAP Task Resources.  It specifies task
   creation, state monitoring, discovery, cancellation, terminal-state
   retention, and eventual removal.  It also defines a four-part request
   payload model, identified by the existing CoAP Content-Format Option,
   for carrying resource operations together with task execution
   controls.  No new CoAP Option is defined.
- **draft-mankamana-pim-source-discovery-00** (new-draft, score 3, adjacent_watchlist) [none]: [PIM Source Discovery for ASM Deployments](https://datatracker.ietf.org/doc/draft-mankamana-pim-source-discovery/) — This document discusses the operational challenges of Any-Source
   Multicast deployments that use PIM Sparse Mode and explores whether
   PIM extensions can simplify source discovery and operational behavior
   while preserving the host-facing ASM service model.
- **draft-mankamana-pim-source-fanout-trace-00** (new-draft, score 3, adjacent_watchlist) [none]: [PIM Source Fanout Trace for multicast flow](https://datatracker.ietf.org/doc/draft-mankamana-pim-source-fanout-trace/) — Mtrace version 2 traces an IP multicast path by walking from a last-
   hop router or rendezvous point toward the source.  That model is
   efficient for a single receiver path, but it does not directly answer
   the operational question of where a multicast source fans out
   downstream without issuing separate traces from many receiver-side
   locations.
- **draft-muks-dns-nta-feed-zones-00** (new-draft, score 3, adjacent_watchlist) [none]: [DNS NTA feed zones](https://datatracker.ietf.org/doc/draft-muks-dns-nta-feed-zones/) — This memo documents a method for expressing a list of DNS negative
   trust anchors [RFC7646] inside a specially constructed DNS zone, that
   validating recursive name servers and other DNSSEC validators may
   configure negative trust anchors from.
- **draft-praveen-fann-lq-telemetry-udp-00** (new-draft, score 3, adjacent_watchlist) [none]: [A UDP Transport Binding for Link Quality Telemetry in CLOS Data Center Fabrics](https://datatracker.ietf.org/doc/draft-praveen-fann-lq-telemetry-udp/) — This document specifies a UDP transport binding for the Link Quality
   Telemetry data model.  The binding disseminates YANG-modeled link
   quality data between directly connected switches in multi-stage CLOS
   (leaf-spine) data center fabrics using a compact, fixed-offset binary
   encoding designed for forwarding-plane (ASIC) generation and
   consumption, achieving sub-100 microsecond notification latency on
   forwarding engines capable of data-plane UDP processing.  The encoded
   payload can be carried natively on a dedicated UDP port or as a TLV
   within the Router-Info advertisement mechanism; both carriages share
   a byte-identical payload.

   The data model, receiver processing rules, and requirements
   applicable to all transport bindings are defined in a companion
   document.
- **draft-rogge-niewiejska-manet-awareness-model-00** (new-draft, score 3, adjacent_watchlist) [none]: [MANET Awareness Model](https://datatracker.ietf.org/doc/draft-rogge-niewiejska-manet-awareness-model/) — The MANET Awareness Model is a protocol- and vendor-independent data
   model that exports a router's internal knowledge from different
   protocols via REST or NETCONF/RESTCONF to services or applications.
- **draft-singh-apex-psi-02-00** (new-draft, score 3, trust_infrastructure) [none]: [PSI-02: ACCU Carbon Sequestration Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-02/) — PSI-02 specifies a privacy-preserving cryptographic attestation that
   a registered NDIS service provider's operational evidence satisfies
   the NDIS Practice Standards.  The attestation binds a canonicalised
   evidence digest to an Ed25519 signature without disclosing
   participant data or commercially sensitive material.
- **draft-singh-apex-psi-06-00** (new-draft, score 3, trust_infrastructure) [none]: [PSI-06: Supply Chain Provenance](https://datatracker.ietf.org/doc/draft-singh-apex-psi-06/) — PSI-06 specifies an inception-lock protocol that cryptographically
   anchors a raw human-originated data signal (keystroke, biometric,
   survey response) to an Ed25519 signing key within 10 ms of
   generation.  The protocol prevents tampering with source data between
   capture and submission.
- **draft-singh-apex-psi-07-01** (new-draft, score 3, trust_infrastructure) [none]: [PSI-07: Organic Production Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/) — PSI-07 defines a standard signal format for regulatory events
   detected by automated monitoring systems.  The format is a signed
   JSON envelope carrying the event classification, evidence hash, and
   jurisdiction code, enabling autonomous reporting to one or more
   regulators without human intervention.
- **draft-skyfire-oauth-kyapay-token-exchange-01** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-steele-vibeslop-00** (new-draft, score 3, agent_identity) [none]: [Vibeslop Confessions](https://datatracker.ietf.org/doc/draft-steele-vibeslop/) — AI Agents have transformed the way internet applications are
   developed and have introduced a new set of challenges for
   organizations.  This document describes techniques and concepts that
   are emerging to assist with these challenges, and relates them to
   concepts already familiar to the internet community.  The pace of
   change in this area is accelerating, and it is anticipated that much
   of what this document discusses will become outdated quickly;
   nevertheless, a static publication may prove amusing to future
   readers, whether machine or human.
- **draft-sullivan-mls-attachments-01** (new-draft, score 3, core_identity) [none]: [Encrypted Attachments for MLS](https://datatracker.ietf.org/doc/draft-sullivan-mls-attachments/) — This document defines random-access authenticated encryption of large
   write-once files for Messaging Layer Security (MLS) groups.  A file
   is encrypted so that a receiver can decrypt and authenticate any byte
   range without processing the whole file.  The encryption is SEAL-
   attachment, SEAL's named write-once attachment scheme (raAE),
   parameterized by the AEAD and key derivation function of the group's
   MLS cipher suite and keyed from the MLS exporter.  The encrypted
   bytes are carried by any means, and a recipient needs only a small
   reference (the object's identifier, length, and snapshot value, and
   an optional locator) to fetch, key, and verify the object.  Carrying
   that reference in an MLS message attributes the object to the member
   that sent the message.  MLS application messages cannot carry large
   files, and existing attachment encryption produces an opaque,
   immutable blob with no partial access.  This extension supplies the
   random-access layer those uses need.
- **draft-taylor-dtn-dpp-01** (new-draft, score 3, core_identity) [none]: [DTN Peering Protocol](https://datatracker.ietf.org/doc/draft-taylor-dtn-dpp/) — This document specifies the DTN Peering Protocol (DPP), an inter-
   domain routing protocol for the Delay-Tolerant Networking (DTN)
   ecosystem.  DPP facilitates the exchange of reachability information
   between distinct Administrative Domains (ADs), enabling inter-domain
   routing across the Solar System DTN.  DPP separates the control plane
   from the data plane: a DPP speaker need not be a gateway that
   forwards bundles, allowing centralized route controllers or
   orchestration systems to participate in peering on behalf of the
   gateways they manage.

   DPP harmonizes the two DTN addressing schemes -- ipn (integer-based)
   and dtn (URI-based) -- into a unified routing framework.  It
   leverages DNS for identity verification and supports both reactive
   routing and scheduled contact windows for deep-space networks.
- **draft-yossif-enrollment-problem-00** (new-draft, score 3, adjacent_watchlist) [none]: [Problem Statement: Enrollment and Key-Binding Assumptions in Execution Authority Evidence](https://datatracker.ietf.org/doc/draft-yossif-enrollment-problem/) — Any scheme that produces cryptographic evidence of execution
   authority roots its entire trust chain in an enrollment: the moment
   at which a key becomes bound to a subject and a device, and at which
   a verifier begins to treat signatures under that key as meaningful.
   Every downstream proof is only as trustworthy as that binding.  If an
   attacker substitutes a key of their choosing at enrollment, every
   subsequent proof verifies correctly and yet attests to the wrong
   party.  This document is a problem statement.  It describes the
   foundational key-substitution threat, records the relevant public
   facts about consumer-platform biometric and key APIs that bound what
   an enrollment can establish, and states the assumptions a verifier of
   execution authority evidence must be able to make about the
   enrollment its proofs depend on.  Specific enrollment ceremonies are
   out of scope.  This document defines no protocol or mechanism.
- **draft-yu-ccamp-sla-assurance-optical-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Service Level Agreement (SLA) Assurance Management in Optical Transport Networks](https://datatracker.ietf.org/doc/draft-yu-ccamp-sla-assurance-optical-yang/) — This document defines a YANG module for SLA assurance management in
   optical transport networks.  The module provides a standard way to
   define, detect, and report issues that may impact service and network
   availability.  It enables consistent modeling of assurance intent,
   impairment detection, and risk reporting across optical transport
   domains.  The YANG model is designed to support closed-loop
   operations, allowing automated monitoring, analysis, and remediation
   workflows to maintain high service reliability and SLA compliance
- **draft-zhang-cats-clients-request-packet-00** (new-draft, score 3, core_identity) [none]: [CATS Client Service Request Packet Format (IPv6 Extension Header and Payload-Based Carriage of CS-ID and Network/Computing Requirement Parameters)](https://datatracker.ietf.org/doc/draft-zhang-cats-clients-request-packet/) — This document specifies two complementary mechanisms for carrying the
   CATS Service Identifier (CS-ID) and network/computing requirement
   parameters in client service request packets within the Computing-
   Aware Traffic Steering (CATS) framework.

   Mode A uses IPv6 Extension Headers to carry CS-ID and requirement
   parameters as hop-by-hop or destination options, enabling in-band
   signaling that is visible to all CATS-aware network nodes along the
   path.  Mode B uses a payload-based TLV structure that is transport-
   protocol agnostic and can be used with both IPv4 and IPv6, as well as
   with encrypted transports.

   The document defines the Virtual Placeholder Address (VPA) prefix
   requirements, the CATS Service Request Extension Header (CSREH)
   format, the CATS Service Request TLV format, and the CATS_PACKET_IN
   process for handling these packets at ingress CATS-Forwarders.
- **draft-zw-idr-bgp-orf-yang-model-01** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for BGP Outbound Route Filtering](https://datatracker.ietf.org/doc/draft-zw-idr-bgp-orf-yang-model/) — This document defines YANG data models for managing BGP Outbound
   Route Filter (ORF), including Address Prefix ORF, Covering Prefixes
   ORF (CP-ORF), and VPN Prefix ORF.
- **draft-akhavain-moussa-dawn-problem-statement-05** (new-draft, score 2, ignored_after_review) [none]: [Problem Statement for the Discovery of Agents, Workloads, and Named Entities (DAWN)](https://datatracker.ietf.org/doc/draft-akhavain-moussa-dawn-problem-statement/) — Interacting entities such as agents, tasks, users, workloads, data,
   compute, etc., in AI ecosystem/network are proliferating, yet there
   is no standardised way to discover what entities exist, what
   attributes such as skills, capabilities, physical characteristics,
   etc., they posses, what services they offer, or how to reach them
   across organisational boundaries.

   Discovery today relies on proprietary directories or manual
   configuration, creating fragmented ecosystems that prevent cross-
   domain collaboration.

   This document describes the problem space that motivates Discovery of
   Agents, Workloads, and Named Entities (DAWN).  It clarifies the scope
   of work within entity ecosystems, identifies why current approaches
   are insufficient, and outlines the challenges a standardised
   discovery mechanism must address.  It does not propose a specific
   solution or protocol.
- **draft-alsahati-nhp-sba-nhp-protocol-01** (new-draft, score 2, ignored_after_review) [none]: [Network Hiding Protocol (NHP) Extensions for 5G/6G Service-Based Architectures](https://datatracker.ietf.org/doc/draft-alsahati-nhp-sba-nhp-protocol/) — This document specifies a candidate implementation profile and
   extension to the evolving Network Hiding Protocol (NHP) standards,
   designed specifically for autonomous 5G/6G Service-Based
   Architectures (NHP-SBA).  It defines the payload schemas,
   cryptographic bindings, and state machine workflows necessary to
   address Policy Enforcement Point (PEP) interoperability surfaces in
   heterogeneous telecom environments.  By leveraging zero-copy
   FlatBuffers serialization and HTTP/2 Custom Frame Extensions, NHP-SBA
   enables deterministic, ultra-low-latency safety enforcement for
   agent-driven RF control loops.
- **draft-carpenter-anima-grasp-rendezvous-00** (new-draft, score 2, ignored_after_review) [none]: [Using GRASP as an Agent Rendezvous Mechanism](https://datatracker.ietf.org/doc/draft-carpenter-anima-grasp-rendezvous/) — This document describes how the GeneRic Autonomic Signaling Protocol
   (GRASP) defined by RFC 8990 may be used as a rendezvous mechanism for
   one Autonomic Service Agent to find another, and then to establish a
   generic communication channel between them.  Such a channel could be
   used for any form of agent-to-agent (A2A) communication, not limited
   to GRASP exchanges.
- **draft-cheng-dmm-srv6-6g-up-requirements-00** (new-draft, score 2, ignored_after_review) [none]: [Requirements of SRv6 for the 6G User Plane](https://datatracker.ietf.org/doc/draft-cheng-dmm-srv6-6g-up-requirements/) — This document leverages the five standardized 6G service scenarios
   defined in 3GPP TR 22.870—multi-agent collaborative communication,
   compute-network integration, integrated sensing and communication
   (ISAC), network digital twin (NDT), and wide-area deterministic
   networking—as core business baselines.  It systematically analyzes
   the multi-dimensional stringent user-plane requirements introduced by
   next-generation mobile systems.  This work further dissects inherent
   technical limitations within the 5G GTP-U point-to-point tunnel
   architecture that render it incapable of accommodating dynamic 6G
   service characteristics.  Based on the above analysis, this draft
   illustrates the inherent programmability benefits provided by SRv6,
   and accordingly establishes a suite of standardization requirements
   for SRv6 to serve as the underlay forwarding protocol of the 6G user
   plane.
- **draft-cheng-spring-srv6-for-ai-network-01** (new-draft, score 2, core_identity) [none]: [A SRv6 Traffic Engineering Application for AI Network](https://datatracker.ietf.org/doc/draft-cheng-spring-srv6-for-ai-network/) — AI applications require fast processing and responses. Traffic using
   RoCEv2 has low entropy for ECMP. At the same time, AI elephant flows
   are predictable. Traffic engineering technology for AI backend
   networks becomes a possible solution. SRv6 TE can start from the
   host side, making SRv6 source routing and traffic path control from
   the host side an optional solution.

   This document presents a AI network Traffic Engineering (TE)
   application scenario for handling link faults and traffic congestion
   issues in data centers, based on Segment Routing over IPv6 (SRv6)
   and Compressed Segment Identifier (CSID). The application scenario
   uses SRv6 CSID Network Programming to directly install all
   forwarding paths on the head-end device. When a data center
   experiences a link fault or traffic congestion, the head-end device
   switches the forwarding path to another optimal path for avoiding
   the location of link fault or traffic congestion, ensuring optimal
   AI data flow forwarding.
- **draft-dong-fann-problem-statement-00** (new-draft, score 2, ai_infrastructure) [none]: [Fast Network Notifications Problem Statement](https://datatracker.ietf.org/doc/draft-dong-fann-problem-statement/) — Many network applications, ranging from Artificial Intelligence (AI)
   /Machine Learning (ML) training/inference to cloud services, require
   networks with various combination of high bandwidth, low delay and
   low jitter and minimal packet loss in data transfer.  This requires
   that the networks must rapidly adapt to the presence of faults,
   degradation and congestion.  However, existing routing and traffic
   management mechanisms often face limitations in responsiveness,
   coverage, and operational complexity, particularly in large-scale and
   high-bandwidth network environments (e.g. data center (DC) and data
   center interconnect (DCI)).  A good and timely understanding of
   network conditions can help to enable faster response to critical
   events, so as to enable the selection of paths with reduced latency
   and improve network utilization.  This document describes the gap
   analysis and the need for fast network notification, and identifies
   the set of problems which a fast network notification solution needs
   to address.
- **draft-elkhatabi-verifiable-telemetry-ledgers-08** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Telemetry Ledgers for Resource-Constrained Environments](https://datatracker.ietf.org/doc/draft-elkhatabi-verifiable-telemetry-ledgers/) — This document profiles a verifiable-telemetry ledger for resource-
   constrained deployments.  Its interoperability boundary begins with
   exact canonical-record byte strings that an upstream system has
   already produced.  The profile fixes admission and assignment of
   those byte strings to serial-numbered segments, deterministic
   commitment-tree calculation, a Concise Binary Object Representation
   (CBOR) segment artifact, a verification manifest, three disclosure
   classes, and binding of the segment-artifact digest to external
   timestamp channels.  Transport framing, decryption, anti-replay
   processing, payload interpretation, and source-telemetry-to-record
   mapping are outside this profile.  Segment closure uses a deployment-
   configured elapsed-time interval and does not depend on source or
   gateway calendar dates.  RFC 3161 timestamp responses are the
   mandatory-to-implement interoperable timestamp channel.
   OpenTimestamps (OTS) and peer signatures are optional parallel
   channels.

   The profile enables independent recomputation and audit of disclosed
   evidence from the admitted canonical-record bytes onward.  It does
   not verify how source telemetry was authenticated, interpreted, or
   mapped to those bytes, and it does not cover device onboarding, end-
   to-end security of sensor values, or safety decisions.
- **draft-google-cfrg-libzk-02** (new-draft, score 2, ignored_after_review) [none]: [Longfellow ZK](https://datatracker.ietf.org/doc/draft-google-cfrg-libzk/) — This document defines an algorithm for generating and verifying a
   succinct non-interactive zero-knowledge argument that for a given
   input x and a circuit C, there exists a witness w, such that C(x,w)
   evaluates to 0.  The technique here combines the MPC-in-the-head
   approach for constructing ZK arguments described in Ligero [ligero]
   with a verifiable computation protocol based on sumcheck for proving
   that C(x,w)=0.
- **draft-ietf-cdni-delivery-metadata-03** (new-draft, score 2, ignored_after_review) [cdni]: [CDNI Delivery Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-delivery-metadata/) — This specification adds to the core set of configuration metadata
   defined in RFC8006, providing delivery metadata to define traffic
   types, request delegation behavior and CDN transport arrangements
   selection of a downstream CDN.
- **draft-ietf-dnsop-delext-09** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895 and 9824.
- **draft-li-dmsc-macp-06** (new-draft, score 2, ignored_after_review) [none]: [Multi-agent Collaboration Protocol Suites Architecture](https://datatracker.ietf.org/doc/draft-li-dmsc-macp/) — This document defines a protocol suite and architectural framework
   for secure and scalable multi-agent collaboration.  The proposed
   Multi-Agent Collaboration Protocol (MACP) enables trusted agent
   onboarding, capability-based query, distributed capability
   synchronization, and secure interaction among agents and external
   resources.  The architecture introduces key entities such as the
   Agent Management Center (AMC), Agent Gateway (AGW), Agents, and
   External Resource Services (ERS), along with a set of protocols that
   collectively support dynamic, capability-driven collaboration across
   administrative domains.
- **draft-mcbride-mcast4ai-p2mp-mechanism-evaluation-00** (new-draft, score 2, ignored_after_review) [none]: [AI P2MP Mechanism Evaluation](https://datatracker.ietf.org/doc/draft-mcbride-mcast4ai-p2mp-mechanism-evaluation/) — AI workloads in data centers exhibit inherently point-to-multipoint
   (P2MP) communication patterns.  During distributed training,
   collective operations such as AllReduce, AllGather and Broadcast
   require identical data delivery to many receivers.  During inference
   serving, P2MP patterns also arise from mechanisms such as KV-cache
   distribution in disaggregated serving architectures and speculative-
   decoding verifier fan-out.  Unicast replication of these flows does
   not scale to large GPU clusters.  This document evaluates two
   architectural mechanisms for addressing this problem: extending BIER
   (Bit Index Explicit Replication) to support AI P2MP requirements, or
   defining a new purpose-built protocol.  The evaluation is grounded in
   the transport-layer requirements this P2MP communication pattern
   places on a multicast solution, i.e., the requirements imposed by
   RDMA and RoCEv2 semantics rather than by the choice of network-layer
   replication mechanism, including considerations around ACK
   aggregation, congestion control, RoCE/RDMA compatibility and
   operational complexity.  This document does not define a protocol but
   is intended instead to help the mcast4ai community evaluate this
   problem space.
- **draft-praveen-fann-lq-telemetry-info-00** (new-draft, score 2, adjacent_watchlist) [none]: [A YANG Data Model for Link Quality Telemetry in CLOS Data Center Fabrics](https://datatracker.ietf.org/doc/draft-praveen-fann-lq-telemetry-info/) — This document defines a YANG data model for real-time link quality
   telemetry in multi-stage CLOS (leaf-spine) data center fabrics.  The
   data model provides a vendor-agnostic representation of link
   congestion state, enabling next-next-hop (NNH) path quality
   visibility required for adaptive routing in AI/ML training networks.
   The link quality advertisement is modeled as a YANG data structure,
   making the model directly usable with any transport.

   The data model is deliberately decoupled from any transport.  A
   lightweight UDP transport binding for disseminating the modeled data
   is specified in a companion document; additional transport bindings
   may be specified in future documents.
- **draft-singh-apex-psi-05-01** (new-draft, score 2, ignored_after_review) [none]: [PSI-05: Financial Disclosure Integrity](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/) — PSI-05 defines the royalty schedule that MAY be levied by a
   publishing foundation for commercial, litigation, regulatory, or AI-
   training reuse of PSI public ledger data above a threshold defined by
   the foundation's charter.  It establishes a flat-rate per-row fee
   schedule, exemption categories, and an audit protocol.
- **draft-wang-mcast4ai-p2mp-scaleup-00** (new-draft, score 2, ignored_after_review) [none]: [AI P2MP Multicast in Scale-UP Network](https://datatracker.ietf.org/doc/draft-wang-mcast4ai-p2mp-scaleup/) — MoE (Mixture-of-Experts) has been adopted in scale-up GPU connections
   by the mainstream Large Language Models, such as Llama4, Mixtral, and
   DeepSeekV3.  This document focuses on the AI multicast protocol
   evolution for MoE in scale-up scenarios, analyzing the challenges and
   proposing potential protocol evolutions.
- **draft-xu-idr-fare-06** (new-draft, score 2, adjacent_watchlist) [none]: [Fully Adaptive Routing Ethernet using BGP](https://datatracker.ietf.org/doc/draft-xu-idr-fare/) — Large language models (LLMs) like ChatGPT have become increasingly
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
   multiple equal-cost paths, based on network capacity and even
   congestion information along those paths.

## Ignored after review

- **draft-abraitis-idr-maximum-paths-subcode-02** (new-draft, score 0, ignored_after_review) [none]: [Maximum Number of Paths Reached Notification for BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-maximum-paths-subcode/) — This document defines a new BGP Cease NOTIFICATION message subcode,
   "Maximum Number of Paths Reached", used when a BGP speaker terminates
   a peering because the number of paths received from a neighbor, as
   permitted by BGP ADD-PATH, exceeds a locally configured upper bound.
   That bound may be applied on a per-prefix basis or as an aggregate
   limit across an address family.
- **draft-ajp-spring-srv6-mpte-01** (new-draft, score 0, ignored_after_review) [none]: [SRv6 for Multipath Traffic Engineering](https://datatracker.ietf.org/doc/draft-ajp-spring-srv6-mpte/) — A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel
   is a Traffic Engineering (TE) construct that enables weighted load
   balancing of unicast traffic across a constrained set of paths
   optimized for an objective.

   This document is informational and describes one realization approach
   for applying SRv6 semantics to MPTE, based on the Multipath Traffic
   Engineering as described in Internet-Draft (draft-kompella-teas-
   mpte).  It summarizes associated procedures, lifecycle, management,
   and forwarding behavior.

   This document applies existing SRv6 architecture and semantics to
   MPTE without defining new SRv6 Endpoint Behaviors or signaling
   protocols.  It focuses on data-plane realization using existing
   forwarding instructions.
- **draft-ali-pce-implicit-tls-profile-01** (new-draft, score 0, ignored_after_review) [none]: [A Policy-Driven Implicit TLS Transport Profile for PCEP](https://datatracker.ietf.org/doc/draft-ali-pce-implicit-tls-profile/) — RFC 8253 specifies the use of Transport Layer Security (TLS) for the
   Path Computation Element Communication Protocol (PCEP) by negotiating
   TLS using the PCEP StartTLS message exchange.  This document
   specifies a deployment profile for PCEP in which TLS is initiated
   immediately following TCP connection establishment based on local
   policy.

   This document is intended to simplify deployments where secure
   transport is mandatory.
- **draft-becker-cnsa2-smime-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Secure/Multipurpose Internet Mail Extensions (S/MIME)](https://datatracker.ietf.org/doc/draft-becker-cnsa2-smime-profile/) — This document defines a base profile of S/MIME for use with the US
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
- **draft-becker-cnsa2-ssh-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
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
- **draft-becker-cnsa2-tls-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for TLS 1.3](https://datatracker.ietf.org/doc/draft-becker-cnsa2-tls-profile/) — This document defines a base profile of TLS 1.3 which is compliant
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
- **draft-beeram-mpls-rsvp-sr-00** (new-draft, score 0, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SR-MPLS Forwarding Plane Using Adjacency Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-mpls-rsvp-sr/) — RFC 8577 introduced the concept of signaling RSVP-TE tunnels on a
   shared MPLS forwarding plane using preinstalled "TE link labels".
   Those labels are functionally equivalent to Segment Routing (SR)
   Adjacency Segment Identifiers (Adj-SIDs) but are allocated and
   distributed solely via RSVP-TE signaling.

   This document extends RFC 8577 to use SR-MPLS Adjacency SIDs that are
   advertised by the IGP as the forwarding-plane labels for RSVP-TE
   tunnels.  It restricts scope to per-link Adj-SIDs and defines the
   signaling procedures and protocol extensions required to couple the
   RSVP-TE control plane with the native SR-MPLS forwarding plane.
- **draft-bertoldi-regext-rdap-reliability-scoring-01** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Structured Reliability Assessment Metadata](https://datatracker.ietf.org/doc/draft-bertoldi-regext-rdap-reliability-scoring/) — This document proposes an extension to the Registration Data Access
   Protocol (RDAP) that enables the representation and exchange of
   structured reliability assessment metadata for registrars and domain
   names.  The extension defines a structured assessment envelope
   through which an RDAP server can expose assessment results produced
   by a registry, registrar, or third-party assessor in a common,
   machine-readable format within RDAP responses.

   The extension standardizes how assessment results are transported and
   referenced, not how they are computed.  Scoring methodologies,
   thresholds, criteria, and governance frameworks are intentionally
   left to the operational and policy layer.
- **draft-brown-epp-deleg-02** (new-draft, score 0, ignored_after_review) [none]: [Extensible Provisioning Protocol (EPP) mapping for DELEG records](https://datatracker.ietf.org/doc/draft-brown-epp-deleg/) — This document describes an extension to the Extensible Provisioning
   Protocol ([STD69]) which allows clients to provision DELEG records
   for domain names.

About this draft

   This note is to be removed before publishing as an RFC.

   The source for this draft, and an issue tracker, may can be found at
   https://github.com/gbxyz/epp-deleg-extension.
- **draft-caini-dtn-quiccl-01** (new-draft, score 0, ignored_after_review) [none]: [Delay-Tolerant Networking QUIC Convergence Layer Protocol Version 1](https://datatracker.ietf.org/doc/draft-caini-dtn-quiccl/) — This document describes a QUIC convergence layer (QUICCL) for Delay-
   Tolerant Networking (DTN).  QUICCL uses BPv7 bundles encoded by the
   Concise Binary Object Representation (CBOR) as its service data unit
   being transported and makes use of either QUIC streams (RFC 9001) or
   QUIC datagrams (RFC 9221) to transport such bundles.  QUICCL design
   is largely based on TCPCLv4 specification (RFC9174), with three
   significant differences.  First, as QUIC incorporates TLS security,
   all security related parts of TCPCLv4 were dropped.  Second, QUICCL
   provides two new transport services, notified and unreliable, in
   addition to the reliable service; Third, in the reliable service, by
   taking advantage of QUIC streams, four levels of priority are
   offered.
- **draft-cui-idr-flowspec-feedback-roadmap-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement and Roadmap for BGP FlowSpec Monitoring](https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-roadmap/) — This document describes the problem space and roadmap for monitoring
   BGP Flow Specification (FlowSpec) deployments.  It outlines the
   operational motivation for FlowSpec monitoring, identifies
   representative classes of monitoring information, and positions
   relevant work on FlowSpec, the BGP Monitoring Protocol (BMP), IP Flow
   Information Export (IPFIX), and YANG-based operational state within a
   common framework.  The resulting roadmap provides common context for
   related protocol-specific work in the relevant IETF working groups.
- **draft-cxx-ippm-ioamaggr-06** (new-draft, score 0, ignored_after_review) [none]: [Aggregation Trace Option for In-situ Operations, Administration, and Maintenance (IOAM)](https://datatracker.ietf.org/doc/draft-cxx-ippm-ioamaggr/) — The purpose of this memo is to describe a new option type for In-Situ
   Operations, Administration, and Maintenance (IOAM).  This option type
   allows to aggregate IOAM data along a network path.  Aggregates
   include functions such as the sum, average, minimum, or maximum of a
   given data parameter.
- **draft-devalk-redirect-by-00** (new-draft, score 0, ignored_after_review) [none]: [The Redirect-By HTTP Response Header Field](https://datatracker.ietf.org/doc/draft-devalk-redirect-by/) — This document defines the Redirect-By HTTP response header field.  It
   allows the software component whose decision determined an HTTP
   redirect to identify itself, so that an operator diagnosing a
   redirect can determine which component was responsible for it.  The
   field succeeds the widely deployed, non-standard X-Redirect-By
   header, which this document deprecates.
- **draft-diaz-lzip-14** (new-draft, score 0, ignored_after_review) [none]: [Lzip Compressed Format and the 'application/lzip' Media Type](https://datatracker.ietf.org/doc/draft-diaz-lzip/) — Lzip is a general-purpose lossless compressed data format.  Lzip uses
   LZMA compression and can achieve higher compression ratios than gzip.
   Lzip provides accurate and robust 3-factor integrity checking.  This
   document describes the lzip format and registers a media type, a
   content coding, and a structured syntax suffix to be used when
   transporting lzip-compressed content via MIME or HTTP.
- **draft-dkg-openpgp-external-secrets-03** (new-draft, score 0, ignored_after_review) [none]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-dkg-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
- **draft-dohmeyer-chainsync-04** (new-draft, score 0, ignored_after_review) [none]: [ChainSync: A Synchronization Protocol for Strict Sequential Execution in Linear Distributed Pipelines](https://datatracker.ietf.org/doc/draft-dohmeyer-chainsync/) — ChainSync is a lightweight application-layer protocol that runs over
   reliable TCP connections to synchronize a fixed linear chain of
   distributed processes such that they execute their local tasks in
   strict sequential order and only after every process in the chain has
   confirmed it is ready.  The protocol has four phases: 1) a forward
   "readiness" wave, 2) a backward "start" wave, 3) a forward
   "execution" wave, and 4) a backward exit wave.

   The design guarantees strict ordering even when nodes become ready at
   very different times and requires only point-to-point TCP connections
   along the chain, thus no central coordinator is needed.
- **draft-eckert-ietf-and-energy-overview-12** (new-draft, score 0, ignored_after_review) [none]: [An Overview of Energy-related Efforts within the IETF, IRTF, and IAB](https://datatracker.ietf.org/doc/draft-eckert-ietf-and-energy-overview/) — This memo provides a compilation of existing work performed by or
   proposed within the IETF, the IRTF, and the IAB that relates to
   energy and sustainability: awareness, management, control, or
   reduction of energy consumption.

   The principal goal of this document is to help IETF, IRTF, and IAB
   participants, especially newcomers and future contributors, become
   familiar with the body of work already published on energy-related
   topics, serving as the first consolidated catalog of such efforts.

   In addition, the document raises awareness of the Internet's role in
   energy efficiency and energy-related activities within the IETF,
   IRTF, and IAB more broadly.  As a reference rather than a guide, it
   may help readers identify gaps and areas where further work could be
   pursued, without this document itself directing or recommending any
   such work.  The scope of this document includes selected work from
   the IETF, IRTF, and IAB where relevant, and it is descriptive in
   nature, not proposing new work items.

   This document captures work until December 2022, when the "IAB
   workshop on Environmental Impact of Internet Applications and
   Systems" contextualized renewed community interest and discussion of
   the topic.  This memo itself does not recommend or direct future
   work.
- **draft-eggert-appeal-support-01** (new-draft, score 0, ignored_after_review) [none]: [Requiring Support for Appealing to the IESG and IAB](https://datatracker.ietf.org/doc/draft-eggert-appeal-support/) — RFC2026 describes the procedure for appealing decisions or process
   failures to the IESG and the IAB.  This document updates RFC2026 and
   requires that an appellant must first gain support for their appeal
   before an appeal may be considered by the body it is submitted to.
- **draft-farinacci-lisp-satellite-network-09** (new-draft, score 0, ignored_after_review) [none]: [LISP for Satellite Networks](https://datatracker.ietf.org/doc/draft-farinacci-lisp-satellite-network/) — This specification describes how the LISP architecture and protocols
   can be used over satellite network systems.  The LISP overlay runs on
   earth using the satellite network system in space as the underlay.
- **draft-gandhi-lsr-ber-02** (new-draft, score 0, ignored_after_review) [none]: [IS-IS, OSPF, and BGP-LS Extensions for Advertising Bit Error Rate Metric for Traffic Engineering](https://datatracker.ietf.org/doc/draft-gandhi-lsr-ber/) — Networks may experience transmission bit errors due to various
   factors, such as poor fiber quality.  This document describes
   extensions to IS-IS, OSPF, and BGP-LS to advertise the Bit Error Rate
   (BER) and Packet Error Rate (PER) metrics for the links that can be
   used for Traffic Engineering.

   Note that mechanisms for measuring bit errors or acting on that
   information, once advertised, are outside the scope of this document.
- **draft-gandhi-lsr-flex-algo-link-ber-00** (new-draft, score 0, ignored_after_review) [none]: [IGP Flexible Algorithm Utilizing Link Bit Error Rate Metric](https://datatracker.ietf.org/doc/draft-gandhi-lsr-flex-algo-link-ber/) — Networks may experience transmission bit errors due to various
   factors, such as poor fiber quality.  This document defines
   extensions to the IGP Flexible Algorithm to utilize the link Bit
   Error Rate (BER) metric as a link constraint.  It defines a mechanism
   to exclude links whose BER metric exceeds a configured threshold
   during Flex-Algorithm path computation.  The mechanism utilizes BER
   metric advertisement defined for IS-IS and OSPF in draft-gandhi-lsr-
   ber.
- **draft-gandhi-lsr-stamp-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS, OSPF, BGP-LS, and BGP Extensions for Signaling STAMP Parameters](https://datatracker.ietf.org/doc/draft-gandhi-lsr-stamp/) — The Simple Two-Way Active Measurement Protocol (STAMP), as defined in
   RFC 8762, can be utilized for active measurement without relying on a
   control channel to pre-signal session parameters.  This document
   describes the extensions to IS-IS, OSPF, BGP-LS, and BGP protocols
   for signaling STAMP reflector parameters in a network.  The STAMP
   reflector parameters can be used by the STAMP senders to set up
   appropriate performance measurement sessions for delay and packet
   loss metrics.
- **draft-gandhi-pce-pm-13** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extensions for Performance Measurement for SR-TE and MPLS-TE LSPs with Stateful PCE](https://datatracker.ietf.org/doc/draft-gandhi-pce-pm/) — In certain networks, network performance data such as packet loss,
   delay, and delay variation, as well as bandwidth utilization, are
   critical measures for Traffic Engineering (TE).  These data provide
   operators with the characteristics of their networks for the
   performance evaluation required to provide Service-Level Agreements
   (SLAs).

   Stateful Path Computation Element Communication Protocol (PCEP)
   extensions have been defined for TE LSPs for Segment Routing (SR) and
   RSVP.  This document describes the PCEP extensions for enabling and
   reporting end-to-end performance measurement and liveness detection
   for both PCE-Initiated and PCC-Initiated LSPs for SR-TE over MPLS and
   IPv6 data planes, and MPLS-TE using RSVP to an Active Stateful PCE.
- **draft-gao-opsawg-flowspec-ipfix-00** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP FlowSpec Treatment Information in IPFIX](https://datatracker.ietf.org/doc/draft-gao-opsawg-flowspec-ipfix/) — BGP Flow Specification (FlowSpec) is commonly used to distribute
   traffic filtering and traffic treatment rules.  Operational
   monitoring of FlowSpec deployments may require information from
   multiple sources, including BGP control-plane telemetry, operational
   state, and forwarding-plane observations.

   This document defines IP Flow Information Export (IPFIX) Information
   Elements that add FlowSpec context to IPFIX Flow Records.  The
   exported information enables a Collector to correlate exported Flow
   Records with a FlowSpec rule in the scope of an Observation Domain
   and to identify the treatment class reported by the Exporter.
- **draft-geng-acme-sm2dualcert-rotation-00** (new-draft, score 0, ignored_after_review) [none]: [ACME STAR Extension for SM2 Dual-Certificate Automated Key Rotation](https://datatracker.ietf.org/doc/draft-geng-acme-sm2dualcert-rotation/) — The SM2 dual-certificate system, specified in [GMT.0034-2014],
   employs a dual-certificate architecture in which each entity holds
   both a signature certificate and an encryption certificate.  The
   encryption private key is generated and escrowed by the Key
   Management Center (KMC).

   This document defines an *ACME Profile* that adapts the core protocol
   of [RFC8555] to the specific deployment scenario of SM2 dual-
   certificate management in the ShangMi (SM) ecosystem.  Building upon
   the dual-certificate foundation framework defined in [I-D.geng-acme-
   sm2dualcert-extension], this document defines a STAR extension for
   the ACME protocol that enables *synchronized short-term automatic
   renewal* of SM2 dual certificates.  The signature certificate follows
   [RFC8739] (ACME STAR) for automatic renewal with the same key pair;
   the encryption certificate achieves automated key rotation with a
   fresh key pair per epoch based on *Asynchronous Remote Key Generation
   (ARKG)* [Frymann2020].

   This extension establishes a *unified ARKG seed chain key derivation
   system*: the KMC holds a seed seed_kmc and derives all encryption
   certificate key pairs (pk_i, sk_i) for all epochs via the ARKG
   algorithm, enabling stateless, lightweight KMC operations.  On this
   basis, this extension provides *two private key delivery modes*:

   *  *Mode A (ARKG Envelope Delivery)*: delivers sk_i to the client via
      a digital envelope, fully inheriting the envelope mechanism of the
      base framework.

   *  *Mode B (ARKG Offline DH Derivation)*: the initial private key is
      obtained via envelope delivery; subsequent private keys are
      derived offline by the client, providing key insulation security
      properties.

   Both modes share the same ARKG cryptographic infrastructure,
   differing only in the final delivery mechanism of the private key.
   Deployers may choose according to their requirements, with full
   compatibility and coexistence achieved through ACME directory object
   negotiation.

   *Document Positioning*: This document is intended for the *specific
   SM ecosystem* as a practical guide and interoperability reference,
   and does not seek to become a general Internet standard.
- **draft-geng-grow-bmp-rel-enhancement-03** (new-draft, score 0, ignored_after_review) [none]: [Log More Routing Events in the BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/) — The Route Event Logging (REL) message is defined in
   [I-D.ietf-grow-bmp-rel], which enables monitored routers to report
   event-driven operational data to BMP collectors.

   This document defines additional event code points for BGP FlowSpec
   RFC8955 [RFC8956] and BGP SR Policies [I-D.ietf-idr-sr-policy-safi].
   These extensions enhance monitoring visibility for policy execution
   failures and improve network operation and troubleshooting
   capabilities.
- **draft-gerke-publication-process-reform-00** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.
- **draft-gondwana-email-header-maintenance-00** (new-draft, score 0, ignored_after_review) [none]: [Maintenance of the IANA Message Header Field Registries](https://datatracker.ietf.org/doc/draft-gondwana-email-header-maintenance/) — The IANA "Message Headers" registries record, for each registered
   header field, the protocol it belongs to, its status, whether it is a
   trace field, and the document(s) that specify it.  These registries
   were populated incrementally by many documents over more than two
   decades, and the instructions those documents gave to IANA were not
   consistent with one another.  As a result the registries no longer
   present a reliable picture of the relative status or usage of the
   fields they contain: fields of equal standing carry different status
   values, foundational fields appear less classified than minor ones,
   the "trace" property is recorded for only a fraction of the fields
   whose defining documents describe them as trace fields, and the
   reference column frequently points at a later registration document
   rather than at the document that actually defines or updates the
   field.  This reduces the value of the metadata to the point where a
   reader cannot use it to reason about a field with confidence.

   This document reviews the initial definition of, and every subsequent
   update to, each registered header field, and gives IANA a single,
   coherent set of instructions for correcting each registry entry.
   Every recommended change, and every deliberate decision to leave a
   non-obvious entry unchanged, is justified by reference to the clear
   intent of the authors of the source documents in which the field was
   defined or modified.
- **draft-gould-regext-epp-server-validation-00** (new-draft, score 0, ignored_after_review) [none]: [Server Validation Extension for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-gould-regext-epp-server-validation/) — This document describes an Extensible Provisioning Protocol (EPP)
   extension for providing the status of server validations.  Server
   validations can be done for an extensible set of types, with examples
   including validating the DNS resolution with the type "dns" and
   validating the DNSSEC with the type "dnssec".  The validations can be
   performed synchronously that will include the extension in the
   response or asynchronously that will include the validation in a poll
   message.  If validations are performed on a schedule, a change in the
   status of a typed-validation will be included in a poll message.
- **draft-gould-regext-rdap-server-validation-01** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Server Validation](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-server-validation/) — This document describes an Registration Data Access Protocol (RDAP)
   extension for providing the status of server validations.  Server
   validations can be done for an extensible set of types, with examples
   including validating DNS resolution with the type "dns" and
   validating DNSSEC with the type "dnssec".  The validations can be
   performed synchronously in the provisioning command or asynchronously
   based on a triggering command or a schedule.  The extension will
   provide the status of the validations, by type, performed by the
   server in an RDAP lookup response.
- **draft-gould-regext-rdap-status-set-01** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Status Set](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-status-set/) — This document describes an Registration Data Access Protocol (RDAP)
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
- **draft-guthrie-cnsa2-ipsec-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for IPsec](https://datatracker.ietf.org/doc/draft-guthrie-cnsa2-ipsec-profile/) — This document defines a base profile for IPsec for use with the US
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
- **draft-he-lsr-srv6-mirror-sid-igp-encoding-01** (new-draft, score 0, ignored_after_review) [none]: [IGP Encoding for SRv6 Mirror SID in Egress Protection](https://datatracker.ietf.org/doc/draft-he-lsr-srv6-mirror-sid-igp-encoding/) — This document specifies the IGP protocol extensions required to
   support SRv6 path egress protection using the Mirror SID (End.M)
   mechanism.  It reuses the existing SRv6 End SID sub-TLV defined in
   RFC 9352 (IS-IS, Section 7.2) and RFC 9513 (OSPFv3, Section 8) with
   the End.M endpoint behavior (74) to advertise the Mirror SID and the
   set of protected locators, and defines a new Protected Locators
   sub-(sub-)TLV.  enabling a backup egress node (protector) to signal
   its capability to protect a primary egress node within a single link-
   state IGP area.

   This document is a companion to
   [I-D.ietf-rtgwg-srv6-egress-protection], which specifies the overall
   SRv6 path egress protection mechanism and the End.M behavior.  The
   IGP encoding defined herein provides the signaling substrate for that
   mechanism.
- **draft-hoffman-pq-dnssec-considerations-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Selecting Post-Quantum Algorithms for DNSSEC](https://datatracker.ietf.org/doc/draft-hoffman-pq-dnssec-considerations/) — This draft lists many of the considerations that the DNS community
   needs to balance when it is deciding which post-quantum algorithms to
   standardize for DNSSEC.

   This draft is definitely not meant to become an RFC.
- **draft-hoflev-secure-smtp-01** (new-draft, score 0, ignored_after_review) [none]: [Secure SMTP](https://datatracker.ietf.org/doc/draft-hoflev-secure-smtp/) — SMTP [RFC5321] uses opportunistic TLS to optionally protect transport
   sessions.  Secure SMTP uses mandatory TLS on all connections.  It
   also provides a method for SMTP clients to locate Secure SMTP
   servers.
- **draft-housley-asn1-layman-guide-01** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.
- **draft-huitema-ccwg-c4-test-04** (new-draft, score 0, ignored_after_review) [none]: [Testing of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design was validated by
   series of simulations, and also by initial deployments in control
   networks.  We describe here these simulations and tests.
- **draft-iab-ip-geo-workshop-report-04** (new-draft, score 0, ignored_after_review) [iab]: [Report from the IAB Workshop on IP Address Geolocation](https://datatracker.ietf.org/doc/draft-iab-ip-geo-workshop-report/) — The IAB Workshop on IP Address Geolocation (IP-GEO) was held from
   December 3-5, 2025, as a three-day virtual meeting.  It covered the
   use cases and background on using IP addresses as indicators of
   geolocation, explored various problems and challenges that exist in
   that ecosystem, and discussed future directions and opportunities to
   improve or replace the current practices.

   Note that this document is a report on the proceedings of the
   workshop.  The views and positions documented in this report are
   those of the workshop participants and do not necessarily reflect IAB
   views and positions.
- **draft-iab-rfc4052bis-05** (new-draft, score 0, ignored_after_review) [iab]: [IAB Processes for Management of IETF Liaison Relationships](https://datatracker.ietf.org/doc/draft-iab-rfc4052bis/) — This document describes the procedures used by the Internet
   Architecture Board (IAB) to establish and maintain formal liaison
   relationships between the IETF and other Standards Development
   Organizations (SDOs), consortia and industry fora.  This document
   also outlines the expectations of the IAB in establishing formal
   liaison relationships and describes the responsibilities of IAB-
   appointed IETF liaison managers.
- **draft-iab-rfc4053bis-05** (new-draft, score 0, ignored_after_review) [iab]: [Procedures for Handling Liaison Statements to and from the IETF](https://datatracker.ietf.org/doc/draft-iab-rfc4053bis/) — This document describes the procedures for generating and handling
   liaison statements between the IETF and other Standards Development
   Organizations (SDOs), so that the IETF can effectively collaborate
   with other organizations in the international standards community.
- **draft-ietf-6lo-nd-gaao-11** (new-draft, score 0, ignored_after_review) [6lo]: [Generic Address Assignment Option for 6LoWPAN Neighbor Discovery](https://datatracker.ietf.org/doc/draft-ietf-6lo-nd-gaao/) — This document specifies an extension to the IPv6 Neighbor Discovery
   in Low Power and Lossy Networks (LLNs), enabling a node to request to
   be assigned an address or a prefix from neighbor routers, without
   introducing a centralized infrastructure and without relying on
   multicast messages.  Such a mechanism makes it possible to
   algorithmically assign addresses and prefixes to nodes in a 6LoWPAN
   deployment.  The proposed mechanism is more efficient in such
   specific scenario with respect to DHCPv6.
- **draft-ietf-6lo-path-aware-semantic-addressing-15** (new-draft, score 0, ignored_after_review) [6lo]: [Path-Aware Semantic Addressing (PASA) for Low power and Lossy Networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-path-aware-semantic-addressing/) — This document specifies a topological addressing scheme, Path-Aware
   Semantic Addressing (PASA), that enables stateless IP packet
   forwarding.  The forwarding decision is based solely on the
   destination address structure.  This document focuses on carrying IP
   packets across an LLN (Low power and Lossy Network), in which the
   topology is quite static, the location of the nodes is fixed for long
   period of time, and the connection between the nodes is also rather
   stable.  This document specifies the PASA architecture, along with
   the PASA address allocation, forwarding mechanism, routing header
   format, and IPv6 interconnection support.
- **draft-ietf-anima-constrained-join-proxy-21** (new-draft, score 0, ignored_after_review) [anima]: [Join Proxy for Onboarding of Constrained Network Elements](https://datatracker.ietf.org/doc/draft-ietf-anima-constrained-join-proxy/) — This document supports the constrained Bootstrapping Remote Secure
   Key Infrastructures (cBRSKI) onboarding protocol by adding a required
   network function, the Join Proxy.  This function can be implemented
   on a constrained node.  The goal of the Join Proxy is to help new
   constrained nodes ("Pledges") securely onboard into a new IP network
   using the cBRSKI protocol.  It acts as a circuit proxy for User
   Datagram Protocol (UDP) packets that carry the onboarding messages.
   The solution is extensible to support other UDP-based onboarding
   protocols as well.  The Join Proxy functionality is designed for use
   in constrained networks, including IPv6 over Low-Power Wireless
   Personal Area Networks (6LoWPAN) based networks in which the
   onboarding authority server ("Registrar") may be multiple IP hops
   away from a Pledge.  Despite this distance, the Pledge only needs to
   use link-local communication to complete cBRSKI onboarding.  Two
   modes of Join Proxy operation are defined, stateless and stateful, to
   allow different trade-offs regarding resource usage, implementation
   complexity and security.
- **draft-ietf-anima-rfc8366bis-33** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Bootstrapping Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-avtcore-hevc-webrtc-09** (new-draft, score 0, ignored_after_review) [avtcore]: [H.265 Profile for WebRTC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-hevc-webrtc/) — RFC 7742 defines WebRTC video processing and codec requirements,
   including guidance for endpoints supporting the VP8 and H.264 codecs,
   which are mandatory to implement.  This document defines a profile of
   RFC 7798 for browsers supporting the H.265 codec.
- **draft-ietf-bess-evpn-ip-mac-proxy-adv-00** (new-draft, score 0, ignored_after_review) [bess]: [Proxy MAC-IP Advertisement in EVPNs](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-ip-mac-proxy-adv/) — This document specifies procedures for EVPN PEs connected to a common
   multihomed site to generate proxy EVPN MAC-IP advertisements on
   behalf of other PEs to facilitate preservation of ARP/ND state across
   link or node failures.
- **draft-ietf-bess-evpn-umr-mobility-01** (new-draft, score 0, ignored_after_review) [bess]: [Applications and Procedures for the Unknown MAC Route in EVPN](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-umr-mobility/) — The Interconnect Solution for Ethernet VPN defines Unknown MAC (Media
   Access Control) Route (UMR) utilization for Data Center Interconnect
   (DCI) when EVPN MPLS or EVPN VXLAN is used as an overlay network for
   such interconnects.  The use of UMR has implications for EVPN MAC
   mobility procedures, for EVPN Layer 2 and IRB operations, and for
   EVPN Proxy ARP/ND operations.  This document describes additional
   enhancements required to EVPN procedures and operations when using
   UMR.  This document updates RFC9014 to clarify and extend the
   procedures for UMR usage.
- **draft-ietf-bier-frr-14** (new-draft, score 0, ignored_after_review) [bier]: [A Framework for Fast Reroute with Bit Index Explicit Replication (BIER-FRR)](https://datatracker.ietf.org/doc/draft-ietf-bier-frr/) — This document provides a framework for the development of Fast
   Reroute (FRR) mechanisms for Bit Index Explicit Replication
   forwarding (BIER-FRR).  BIER-FRR can provide protection against link
   or BFR failure by invoking locally pre-determined repair paths that
   can react in the same time-scales as (unicast) FRR for MPLS or IP
   networks - "sub 50msec", and without the creation of additional per-
   path or per-flow state coordinated across multiple routers/LSR.

   BIER-FRR can be implemed locally within a router/LSR with minimal
   interoperability requirements against other router/LSR.  It can
   therefore easily be introduced incrementally or selectively where
   needed.  BIER-FRR implementing nodes only need to understand the
   routing topology of the network for calculation of repair paths and
   know what type of unicast encapsulation can be used to send
   ("tunnel") BIER packets to remote BFR.

   This document proposes and discusses different options for BIER
   forwardng (BIFT) extensions to support BIER-FRR.  These are exemplary
   and non-normative.  This document does not specify any standards or
   experiments but aims to support such efforts.
- **draft-ietf-bmwg-savnet-sav-benchmarking-03** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-bmwg-savnet-sav-benchmarking/) — This document defines methodologies for benchmarking the performance
   of intra-domain and inter-domain source address validation (SAV)
   mechanisms.  SAV mechanisms are utilized to generate SAV rules that
   prevent source address spoofing.  The methodology treats a SAV device
   as a black box and is therefore agnostic to the specific SAV
   mechanism and implementation used by the device.  This document
   defines test setups, performance indicators, and test cases for SAV
   accuracy, control-plane and data-plane performance, and resource
   utilization.
- **draft-ietf-cbor-edn-literals-27** (new-draft, score 0, ignored_after_review) [cbor]: [Concise Diagnostic Notation (CDN)](https://datatracker.ietf.org/doc/draft-ietf-cbor-edn-literals/) — This document formalizes and consolidates the definition of the
   Concise Diagnostic Notation (CDN) of the Concise Binary Object
   Representation (CBOR), addressing implementer experience.

   Replacing CDN's previous informal descriptions, it updates RFC 8949,
   obsoleting its Section 8, and RFC 8610, obsoleting its Appendix G.

   It also specifies registry-based extension points and uses them to
   support text representations such as of epoch-based dates/times and
   of IP addresses and prefixes.


   // (This cref will be removed by the RFC editor:) This is the
   // editorial round focusing on editorial cleanup, specifically where
   // that causes moving text around.  It does not have WG input yet on
   // any renaming decisions (CDN name, b1/t1 name), ABNF cleanup, or
   // Rohan's suggestion to fix the questionable figure in 3.8.
- **draft-ietf-ccamp-fgotn-yang-00** (new-draft, score 0, ignored_after_review) [ccamp]: [YANG Data Models for fine grain Optical Transport Network](https://datatracker.ietf.org/doc/draft-ietf-ccamp-fgotn-yang/) — This document defines YANG data models to describe the topology and
   tunnel information of a fine grain Optical Transport Network.  The
   YANG data models defined in this document are designed to meet the
   requirements for efficient transmission of sub-1Gbit/s client signals
   in transport network.
- **draft-ietf-ccwg-ratelimited-increase-06** (new-draft, score 0, ignored_after_review) [ccwg]: [Increase of the Congestion Window when the Sender Is Rate-Limited](https://datatracker.ietf.org/doc/draft-ietf-ccwg-ratelimited-increase/) — This document specifies how transport protocols increase their
   congestion window when the sender is rate-limited, and updates RFC
   4341, RFC 5681, RFC 9002, RFC 9260, and RFC 9438.  Such a limitation
   can be caused by the sending application not supplying data or by
   receiver flow control.
- **draft-ietf-detnet-tcqf-01** (new-draft, score 0, ignored_after_review) [detnet]: [Deterministic Networking (DetNet) Data Plane - Tagged Cyclic Queuing and Forwarding (TCQF) for bounded latency with low jitter in large scale DetNets](https://datatracker.ietf.org/doc/draft-ietf-detnet-tcqf/) — This memo specifies a forwarding method for bounded latency and
   bounded jitter for Deterministic Networks and is a variant of the
   IEEE TSN Cyclic Queuing and Forwarding (CQF) method.  Tagged CQF
   (TCQF) supports more than 2 cycles and indicates the cycle number via
   an existing or new packet header field called the tag to replace the
   cycle mapping in CQF which is based purely on synchronized reception
   clock.

   This memo standardizes TCQF as a mechanism independent of the tagging
   method used.  It also specifies tagging via the (1) the existing MPLS
   packet Traffic Class (TC) field for MPLS packets, (2) the IP/IPv6
   DSCP field for IP/IPv6 packets, and (3) a new TCQF Option header for
   IPv6 packets.

   Target benefits of TCQF include low end-to-end jitter, ease of high-
   speed hardware implementation, optional ability to support large
   number of flow in large networks via DiffServ style aggregation by
   applying TCQF to the DetNet aggregate instead of each DetNet flow
   individually, and support of wide-area DetNet networks with arbitrary
   link latencies and latency variations as well as low accuracy clock
   synchronization.
- **draft-ietf-dkim-dkim2-dns-00** (new-draft, score 0, ignored_after_review) [dkim]: [Domain Name Specification for DKIM2](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-dns/) — The updated DomainKeys Identified Mail (DKIM2) permits an
   organization that owns the signing domain to claim some
   responsibility for a message by associating the domain with the
   message through a digital signature.  This is done by publishing to
   Domain Name Service (DNS) of the domain a public key that is then
   associated to the domain and where messages can be signed by the
   corresponding private key.  Assertion of responsibility is validated
   through a cryptographic signature and by querying the Signer’s domain
   directly to retrieve the appropriate public key.  This document
   describes DKIM2 DNS record format and how to find the record.
- **draft-ietf-dmm-tn-aware-mobility-28** (new-draft, score 0, ignored_after_review) [dmm]: [Mobility-aware Transport Network Slicing for 5G](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-dnsop-structured-dns-error-26** (new-draft, score 0, ignored_after_review) [dnsop]: [Structured Error Data for Filtered DNS](https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/) — DNS filtering is widely deployed for various reasons, including
   network security and policy enforcement.  However, filtered DNS
   responses lack structured information for end users to understand the
   reason for the filtering.  Existing mechanisms to provide explanatory
   details to end users cause harm especially if the blocked DNS
   response is for HTTPS resources.

   This document updates RFC 8914 by signaling client support for
   structuring the EXTRA-TEXT field of the Extended DNS Error to provide
   details on the DNS filtering.  Such details can be parsed by the
   client and displayed, logged, or used for other purposes.
- **draft-ietf-dtn-btpu-03** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Transfer Protocol - Unidirectional](https://datatracker.ietf.org/doc/draft-ietf-dtn-btpu/) — This document defines a protocol for the unidirectional transfer of
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
- **draft-ietf-grow-bmp-rel-06** (new-draft, score 0, ignored_after_review) [grow]: [Logging of routing events in BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/) — The BGP Monitoring Protocol (BMP) does provide for BGP session event
   logging (Peer Up, Peer Down), state synchronization (Route
   Monitoring), debugging (Route Mirroring) and Statistics messages,
   among others.  This document defines a new Route Event Logging (REL)
   message type for BMP with the aim of covering use cases with affinity
   to alerting, reporting and on-change analysis.
- **draft-ietf-grow-bmp-tlv-21** (new-draft, score 0, ignored_after_review) [grow]: [BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/) — Most of the BGP Monitoring Protocol (BMP) message types make
   provision for data in Type, Length, Value (TLV) format.  However,
   Route Monitoring messages (which provide a snapshot of the monitored
   Routing Information Base) Stats Reports (which supply periodical
   counters) and Peer Down messages (which indicate that a peering
   session was terminated) do not.  Supporting (optional) data in TLV
   format across all BMP message types provides consistent and
   extensible structures that would be useful among the various use-
   cases where conveying additional data to a monitoring station is
   required.  This document updates RFC 7854 [RFC7854] to support TLV
   data in all message types and defines some essential TLVs.

   Additionally, this document introduces support for enterprise-
   specific TLVs in the BGP Monitoring Protocol by defining an
   Enterprise Bit (E-bit) that allows usage of per-vendor Type values.
- **draft-ietf-idr-bgp-ls-bgp-only-fabric-06** (new-draft, score 0, ignored_after_review) [idr]: [BGP Link-State Extensions for BGP-only Networks](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/) — BGP is used as the only routing protocol in some networks today.  In
   such networks, it is useful to get a detailed topology view similar
   to one available when using link state routing protocols.  This
   document defines extensions to the BGP Link-state (BGP-LS) address-
   family and the procedures for advertisement of topology information
   in a BGP-only network.
- **draft-ietf-idr-bgp-ls-sr-policy-admin-flags-00** (new-draft, score 0, ignored_after_review) [idr]: [Advertisement of SR Policy Operational States using BGP Link-State](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-admin-flags/) — This document defines the extension of BGP Link-State to advertise
   the operational state of the candidate path or segment list,
   facilitating the operation and maintenance of the SR Policy.
- **draft-ietf-idr-bgpls-inter-as-topology-ext-36** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extension for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedure for distributing Border Gateway
   Protocol-Link State (BGP-LS) key parameters for inter-domain links
   between two Autonomous Systems (ASes).  It defines a new type within
   the BGP-LS Network Layer Reachability Information (NLRI) for an
   Inter-AS Link, as well as three new type-length-values (TLVs) for the
   BGP-LS Inter-AS Link descriptor.  These BGP-LS extensions enable
   Software-Defined Networking (SDN) controllers to retrieve network
   topology across Inter-AS environments.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   end-to-end network topology using information provided by the BGP-LS
   protocol.
- **draft-ietf-idr-rtc-hierarchical-rr-05** (new-draft, score 0, ignored_after_review) [idr]: [Extensions to RT-Constrain in Hierarchical Route Reflection Scenarios](https://datatracker.ietf.org/doc/draft-ietf-idr-rtc-hierarchical-rr/) — The Route Target (RT) Constrain mechanism specified in RFC 4684 is
   used to build a route distribution graph in order to restrict the
   propagation of Virtual Private Network (VPN) routes.  In network
   scenarios where hierarchical route reflection (RR) is used, the
   existing RT-Constrain mechanism cannot guarantee a correct route
   distribution graph.  This document describes the problem scenario and
   proposes a solution to address the RT-Constrain issue in hierarchical
   RR scenarios.
- **draft-ietf-idr-sr-policy-admin-flags-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP SR Policy Extensions for Administrative Flags](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-admin-flags/) — Segment Routing is a source routing paradigm that explicitly
   indicates the forwarding path for packets at the ingress node. An SR
   Policy is a set of candidate paths, each consisting of one or more
   segment lists.

   This document defines an extension to the BGP SR Policy that sets
   the administrative state of the candidate path or segment list,
   facilitating the operation and maintenance of the SR Policy.
- **draft-ietf-idr-sr-policy-nrp-13** (new-draft, score 0, ignored_after_review) [idr]: [BGP SR Policy Extensions for Network Resource Partition](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-nrp/) — Segment Routing (SR) Policy is a set of candidate paths, each
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
- **draft-ietf-idr-ts-flowspec-srv6-policy-11** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification defined in [RFC8955], [RFC8956] and [RFC9117]
   has been proposed to distribute BGP [RFC4271] FlowSpec NLRI to
   FlowSpec clients to mitigate (distributed) denial-of-service attacks,
   and to provide traffic filtering in the context of a BGP/MPLS VPN
   service.  Recently, traffic steering applications in the context of
   SR-MPLS and SRv6 using FlowSpec are being used in networks.  This
   document introduces the usage of BGP Flow Specification to steer
   packets into an SR Policy.
- **draft-ietf-intarea-multicast-application-port-08** (new-draft, score 0, ignored_after_review) [intarea]: [The Multicast Application Port](https://datatracker.ietf.org/doc/draft-ietf-intarea-multicast-application-port/) — This document discusses the drawbacks of the current practice of
   assigning a UDP port to each multicast application.  Such assignments
   are redundant because the multicast address already uniquely
   identifies the data.  The document assigns a UDP port specifically
   for use with multicast applications and lists requirements for using
   this port.  This approach provides immediate compatibility with
   existing protocol stacks, while also requiring improvements to make
   the port easier to use.
- **draft-ietf-ippm-ioam-data-integrity-20** (new-draft, score 0, ignored_after_review) [ippm]: [Integrity Protection of In Situ Operations, Administration, and Maintenance (IOAM) Data Fields](https://datatracker.ietf.org/doc/draft-ietf-ippm-ioam-data-integrity/) — In Situ Operations, Administration, and Maintenance (IOAM) records
   operational (including telemetry) information in packets while they
   traverse a path in the network.  RFC 9197 specifies data fields for
   IOAM (a.k.a IOAM-Data-Fields) and associated data types.  This
   document specifies integrity protection of IOAM-Data-Fields for
   Intra-IOAM-Domain use cases.
- **draft-ietf-ippm-stamp-cos-ecn-01** (new-draft, score 0, ignored_after_review) [ippm]: [Update of the Simple Two-way Active Measurement Protocol Class-of-Service Extension - ECN](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-cos-ecn/) — The Simple Two-Way Active Measurement Protocol (STAMP) enables one-
   way and round-trip measurement of network metrics between IP hosts,
   and has a facility for defining optional extensions.  This document
   updates the definition of the Class of Service TLV (originally
   defined in RFC 8972) to enable the measurement of manipulation of the
   value of the Explicit Congestion Notification (ECN) field of the IP
   header by middleboxes between two STAMP hosts, and to enable
   discovery and measurement of paths that provide differential
   treatment of packets depending on the value of their ECN field.
- **draft-ietf-lisp-rfc8378bis-09** (new-draft, score 0, ignored_after_review) [lisp]: [Signal-Free Locator/ID Separation Protocol (LISP) Multicast](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc8378bis/) — This document describes the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP).  The
   document specifies how LISP multicast overlays operate over a unicast
   underlay.

   When multicast sources and receivers are active at Locator/ID
   Separation Protocol (LISP) sites, the core network is required to use
   native multicast so packets can be delivered from sources to group
   members.  When multicast is not available to connect the multicast
   sites together, a signal-free mechanism can be used to allow traffic
   to flow between sites.  The mechanism within here uses unicast
   replication and encapsulation over the core network for the data
   plane and uses the LISP mapping database system so encapsulators at
   the source LISP multicast site can find decapsulators at the receiver
   LISP multicast sites.  This document when approved obsoletes RFC
   8378.
- **draft-ietf-manet-inet-gap-analysis-03** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mlcodec-opus-speech-coding-enhancement-04** (new-draft, score 0, ignored_after_review) [mlcodec]: [Integration of Speech Codec Enhancement Algorithms into the Opus Codec](https://datatracker.ietf.org/doc/draft-ietf-mlcodec-opus-speech-coding-enhancement/) — This document proposes a set of requirements for integrating a speech
   codec enhancement algorithm into the Opus codec [RFC6716].
- **draft-ietf-mls-pq-ciphersuites-06** (new-draft, score 0, ignored_after_review) [mls]: [ML-KEM and Hybrid Cipher Suites for Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-mls-pq-ciphersuites/) — This document registers new cipher suites for Messaging Layer
   Security (MLS) based on "post-quantum" algorithms, which are intended
   to be resilient to attack by quantum computers.  These cipher suites
   are constructed using the new Module-Lattice Key Encapsulation
   Mechanism (ML-KEM), optionally in combination with traditional
   elliptic curve KEMs, together with appropriate authenticated
   encryption, hash, and signature algorithms.
- **draft-ietf-moq-loc-04** (new-draft, score 0, ignored_after_review) [moq]: [Low Overhead Media Container](https://datatracker.ietf.org/doc/draft-ietf-moq-loc/) — This specification describes a Low Overhead Media Container (LOC)
   format for encoded and encrypted audio and video media data to be
   used primarily for interactive Media over QUIC Transport (MOQT).  It
   may be used in the MOQT Streaming Format (MSF) specification, which
   defines a catalog format for publishers to declare and describe their
   LOC tracks and for subscribers to consume them.  Examples are also
   provided for building media applications using LOC and MOQT.
- **draft-ietf-mpls-mna-ioam-07** (new-draft, score 0, ignored_after_review) [mpls]: [Supporting In Situ Operations, Administration, and Maintenance Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, is an on-path telemetry method to collect and record the
   operational state and telemetry information using, for example, Pre-
   allocated Trace, Proof-of-Transit, Edge-to-Edge, or Incremental Trace
   Option-Types that can be used to calculate various performance
   metrics.  RFC 9326 defines the IOAM Direct Export (IOAM-DEX) Option-
   Type in which the operational state and telemetry information are
   collected according to the specified profile and exported in a manner
   and format defined by a local policy on each node along the path.

   MPLS Network Actions (MNA) techniques are meant to indicate actions
   to be performed on any combination of Label Switched Paths, MPLS
   packets, and the node itself, and to transport data needed for these
   actions.  This document employs the MNA mechanisms to collect and
   transport the on-path operational state, and telemetry information
   using IOAM data fields as well as using direct export.
- **draft-ietf-mpls-mna-ps-hdr-10** (new-draft, score 0, ignored_after_review) [mpls]: [Post-Stack MPLS Network Action (MNA) Header Specification](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ps-hdr/) — This document specifies the Post-Stack MPLS Network Action (MNA)
   Header encoding and procedures for carrying Network Action encodings
   and Ancillary Data after the MPLS label stack, based on the MNA Sub-
   Stack including In-Stack Network Actions and Data specified in RFC
   9994.  MPLS Network Actions can be used to influence packet
   forwarding decisions, carry additional Operations, Administration,
   and Maintenance information in the MPLS packet, or perform user-
   defined operations.  This document follows the framework specified in
   RFC 9789.
- **draft-ietf-netconf-list-pagination-nc-12** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-nc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to NETCONF [RFC6241].

   This document updates [RFC6241], to augment the <get> and <get-
   config> "rpc" statements, and [RFC8526], to augment the <get-data>
   "rpc" statement, to define input parameters necessary for list
   pagination.
- **draft-ietf-netconf-list-pagination-rc-11** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-rc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to RESTCONF [RFC8040].

   This document updates RFC 8040, to declare "list" and "leaf-list" as
   valid resource targets for the RESTCONF GET operation, to define GET
   query parameters necessary for list pagination, and to define a
   media-type for XML-based lists.
- **draft-ietf-netmod-yang-semver-28** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Semantic Versioning](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-semver/) — This document specifies a YANG extension along with guidelines for
   applying an extended set of semantic versioning rules to revisions of
   YANG artifacts (e.g., modules and packages).  Additionally, this
   document defines a YANG extension for controlling module imports
   based on these modified semantic versioning rules.

   This document updates RFCs 7950, 9907, and 8525.
- **draft-ietf-netmod-yang-versioning-reqs-14** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Module Versioning Requirements](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-versioning-reqs/) — This document describes the problems that can arise because of the
   YANG language module update rules, that require all updates to YANG
   module preserve strict backwards compatibility.  It also defines the
   requirements on any solution designed to solve the stated problems.
   This document does not consider possible solutions, nor endorse any
   particular solution.
- **draft-ietf-ntp-nts-keyexchange-pool-01** (new-draft, score 0, ignored_after_review) [ntp]: [NTS extensions for enabling pools](https://datatracker.ietf.org/doc/draft-ietf-ntp-nts-keyexchange-pool/) — The aim of this document is to describe a system for NTS pools that
   are able to be used by clients without any knowledge beyond plain
   NTS.  The work here focuses purely on creating an intermediate NTS
   Key Exchange server that can be configured with the addresses of
   multiple servers and distribute load between them.  The parts of pool
   operation dealing with managing the list of servers are left out of
   scope for this work.
- **draft-ietf-quic-receive-ts-03** (new-draft, score 0, ignored_after_review) [quic]: [QUIC Extended Acknowledgement for Reporting Packet Receive Timestamps](https://datatracker.ietf.org/doc/draft-ietf-quic-receive-ts/) — This document defines an extension to the QUIC transport protocol
   which supports reporting multiple packet receive timestamps for post-
   handshake packets.
- **draft-ietf-regext-epp-same-entity-01** (new-draft, score 0, ignored_after_review) [regext]: [Same Entity Set Support for EPP](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-same-entity/) — This document defines an EPP extension allowing clients to learn
   about and manipulate a set of objects in a shared central repository
   that are necessarily tied to the same entity (typically domain
   objects whose names are equivalent in a registry-defined way and are
   tied to a single registrant).  The extension supports multiple
   registries with a shared definition of equivalence using a shared
   central repository.
- **draft-ietf-regext-rdap-versioning-06** (new-draft, score 0, ignored_after_review) [regext]: [Versioning in the Registration Data Access Protocol (RDAP)](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-versioning/) — This document describes an RDAP extension for an extensible set of
   versioning types with the features of identifying the RDAP extension
   versions supported by the server, the RDAP extension versions
   included in an RDAP response, and enabling a client to specify the
   desired RDAP extension versions to include in the RDAP query and RDAP
   response.
- **draft-ietf-roll-enrollment-priority-18** (new-draft, score 0, ignored_after_review) [roll]: [Controlling Network Enrollment in RPL networks](https://datatracker.ietf.org/doc/draft-ietf-roll-enrollment-priority/) — The Routing Protocol for Low-Power and Lossy Networks (RPL) manages
   the routing topology but lacks a mechanism to globally regulate how
   many new nodes, known as Pledges, can join a node in a 6TiSCH network
   at any given time.  Currently, Join Proxies (6LowPAN Routers) make
   local decisions about whether to facilitate a Pledge's enrollment
   based only on their immediate resources.

   This document introduces RPL extensions to ensure that enrollment
   remains orderly, prevents localized congestion at specific Join
   Proxies, and allows the network to stay within its operational
   capacity limits.
- **draft-ietf-satp-core-14** (new-draft, score 0, ignored_after_review) [satp]: [Secure Asset Transfer Protocol (SATP) Core](https://datatracker.ietf.org/doc/draft-ietf-satp-core/) — This memo describes the Secure Asset Transfer Protocol (SATP) for
   digital assets.  SATP is a protocol operating between two gateways
   that conducts the transfer of a digital asset from one gateway to
   another, each representing their corresponding digital asset
   networks.  The protocol establishes a secure channel between the
   endpoints and implements a 2-phase commit (2PC) to ensure the
   properties of transfer atomicity, consistency, isolation and
   durability.
- **draft-ietf-savnet-inter-domain-problem-statement-21** (new-draft, score 0, ignored_after_review) [savnet]: [Problem Statement, Gap Analysis, and Requirements for Inter-Domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/) — This document analyzes the problem space and provides a gap analysis
   of existing inter-domain source address validation (SAV) mechanisms.
   Based on these findings, it outlines the technical requirements for
   future improvements.
- **draft-ietf-schc-over-networks-prone-to-disruptions-05** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression and Fragmentation over networks prone to disruptions](https://datatracker.ietf.org/doc/draft-ietf-schc-over-networks-prone-to-disruptions/) — This document describes the use of SCHC over different network
   topologies and devices regardless of their capabilities and
   configurations.  The use of SCHC will bring connectivity to devices
   with disruptive connections caused by restrained use of battery and
   connectionless setups with long delays and latency.
- **draft-ietf-sidrops-rpki-erik-protocol-06** (new-draft, score 0, ignored_after_review) [sidrops]: [The Erik Synchronization Protocol for use with the Resource Public Key Infrastructure (RPKI)](https://datatracker.ietf.org/doc/draft-ietf-sidrops-rpki-erik-protocol/) — This document specifies the Erik Synchronization Protocol for use
   with the Resource Public Key Infrastructure (RPKI).  Erik
   Synchronization can be characterized as a data replication system
   using Merkle trees, a content-addressable naming scheme, concurrency
   control using monotonically increasing sequence numbers, and HTTP
   transport.  Relying Parties can combine information retrieved via
   Erik Synchronization with other RPKI transport protocols.  The
   protocol's design is intended to be efficient, fast, easy to
   implement, and robust in the face of partitions or faults in the
   network.
- **draft-ietf-spring-sr-policy-eligibility-01** (new-draft, score 0, ignored_after_review) [spring]: [Eligibility Concept in Segment Routing Policies](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-eligibility/) — Segment Routing (SR) introduces new challenges for pinning candidate
   paths on their intended paths (the path the PCE computed based on
   provided intent and may have made bandwidth reservations on).  The
   actual path through a network can change or no longer meet the
   required constraints if a SID list of an SR Policy candidate path is
   not fully expressed as a list of adjacency SIDs or when a change in
   the topology does happen.  The introduction of the new candidate path
   eligibility concept permits a path to be signaled and established as
   operationally up, but controls whether the path is eligible to carry
   traffic, thus influencing its active state.
   The eligibility concept allows a system (operator, pce, headend,
   etc.) to set eligibility as false when path deviations may have
   occurred, or path constraints are no longer met for one or more SID
   lists of a candidate path and clear it when candidate path deviations
   are removed or constraints are met again.
- **draft-ietf-spring-sr-redundancy-protection-08** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 for Redundancy Protection](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-redundancy-protection/) — Redundancy Protection is a generalized protection mechanism to
   achieve high reliability for service provided in Segment Routing
   networks.  The mechanism uses the "Live-Live" methodology, i.e.,
   multiple copies of the data packets are sent on different paths to
   provide protection.  This document introduces one new SRv6 Segment
   Endpoint Behavior to provide replication and elimination functions on
   specific network nodes by leveraging SRv6 Network Programming
   capabilities.
- **draft-ietf-spring-stamp-srpm-mpls-04** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-srv6ops-problem-summary-02** (new-draft, score 0, ignored_after_review) [srv6ops]: [SRv6 Deployment and Operation Problem Summary](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-problem-summary/) — This document aims to provide a concise overview of the common
   problems encountered during SRv6 deployment and operation, which
   provides foundations for further work, including for example of
   potential solutions and best practices to navigate deployment.
- **draft-ietf-teas-ns-ip-mpls-09** (new-draft, score 0, ignored_after_review) [teas]: [Realizing Network Slices in IP/MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-teas-ns-ip-mpls/) — Realizing network slices may require the Service Provider to have the
   ability to partition a physical network into multiple logical
   networks of varying sizes, structures, and functions so that each
   slice can be dedicated to specific services or customers.  Multiple
   network slices can be realized on the same network while ensuring
   slice elasticity in terms of network resource allocation.  This
   document describes a scalable solution to realize network slicing in
   IP/MPLS networks by supporting multiple services on top of a single
   physical network by requiring compliant domains and nodes to provide
   forwarding treatment (scheduling, drop policy, resource usage) based
   on slice identifiers.
- **draft-ietf-teas-yang-l3-te-topo-19** (new-draft, score 0, ignored_after_review) [teas]: [YANG Data Models for Layer 3 and Packet TE Topologies](https://datatracker.ietf.org/doc/draft-ietf-teas-yang-l3-te-topo/) — This document defines YANG data models for layer 3 and packet traffic
   engineering topologies.
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-25** (new-draft, score 0, ignored_after_review) [v6ops]: [Framework for Multi-domain IPv6-only Underlay Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — For the IPv6 transition, IPv6-only is considered the final stage
   where only IPv6 protocol is used for transport while maintaining
   global reachability for both IPv6 and IPv4 services.  This document
   introduces a framework for a multi-domain IPv6-only underlay network
   from the perspective of network providers.  In particular, it
   proposes stateless address mapping as the basis for enabling IPv4
   service data transmission in a multi-domain IPv6-only environment
   (i.e., IPv4-as-a-Service).  It describes the methodology of stateless
   IPv4/IPv6 mapping, illustrates the behaviors of network devices,
   analyzes the options of IPv6 mapping prefix allocation, and discusses
   the security considerations.  This framework is not intended to
   replace existing IPv6-only technologies, but rather to leverage or
   remain compatible with them.
- **draft-ihlar-poem-quic-01** (new-draft, score 0, ignored_after_review) [none]: [A Protocol for Periodic On-path Explicit Measurement](https://datatracker.ietf.org/doc/draft-ihlar-poem-quic/) — This document defines the Periodic On-path Explicit Measurement
   (POEM) protocol, which enables passive on-path measurement of packet
   loss for QUIC flows.  POEM uses periodic marker packets, coalesced
   with ordinary QUIC packets, that allow on-path network elements to
   measure upstream packet loss by counting packets between markers.
   Marker packets also carry a sender-reported loss count, enabling
   observers to distinguish upstream from downstream loss.
   Additionally, POEM defines a report mechanism through which network
   elements communicate measurement results back to endpoints.
- **draft-ihlesong-mpls-mna-signaling-04** (new-draft, score 0, ignored_after_review) [none]: [Discovering MNA Capabilities Using LSP Ping](https://datatracker.ietf.org/doc/draft-ihlesong-mpls-mna-signaling/) — This document defines a mechanism for discovering MPLS Network
   Actions (MNA) capabilities along a Label Switched Path (LSP) using
   the LSP Ping echo request/reply mechanism defined in RFC 8029.  The
   In-Stack MNA capabilities include the Readable Label Depth (RLD), the
   maximum sizes of differently scoped Network Action Sub-stacks
   (MLD_NAS), and supported In-Stack network action opcodes.  The Post-
   Stack MNA capabilities include the maximum Post-Stack MPLS Header
   size (MLD_PSMH), the Readable Label Depth including the Post-Stack
   MPLS Header (RLD_PSMH), and supported Post-Stack network action
   opcodes.  This mechanism allows the ingress Label Edge Router (LER)
   to discover MNA capabilities of each transit and egress node on the
   path, enabling correct construction of MPLS label stacks containing
   MNA network actions.
- **draft-kazuho-ptth-ptth-01** (new-draft, score 0, ignored_after_review) [none]: [Protocol for Transposed Transactions over HTTP](https://datatracker.ietf.org/doc/draft-kazuho-ptth-ptth/) — This document specifies the Protocol for Transposed Transactions over
   HTTP (PTTH), an HTTP extension that allows a backend server to
   establish an HTTP connection to a reverse proxy and transpose the
   flow of HTTP requests.  The reverse proxy then sends requests to the
   backend server over the resulting transposed channel.  This extension
   lets backend servers behind restrictive firewalls accept HTTP traffic
   through reverse proxies without changing firewall settings and with
   minimal overhead.
- **draft-koch-openpgp-webkey-service-22** (new-draft, score 0, ignored_after_review) [none]: [OpenPGP Web Key Directory](https://datatracker.ietf.org/doc/draft-koch-openpgp-webkey-service/) — This specification describes a service to locate OpenPGP and LibrePGP
   keys by mail address using a Web service and the HTTPS protocol.  It
   also provides a method for secure communication between the key owner
   and the mail provider to publish and revoke the public key.
- **draft-lee-v6ops-ipv6-satellite-networks-00** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Wireless Access in Satellite Networks (IPWASN): Problem Statement and Use Cases](https://datatracker.ietf.org/doc/draft-lee-v6ops-ipv6-satellite-networks/) — This document describes use cases and a problem statement for IPv6
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
- **draft-liao-ace-est-c509-03** (new-draft, score 0, ignored_after_review) [none]: [EST for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-ace-est-c509/) — This document defines Enrollment over Secure Transport (EST) protocol
   operations over HTTPS and secure CoAP for use with C509 certificates.
   The operations specified in this document support CA certificate
   distribution, C509 certificate enrollment, C509 certificate re-
   enrollment, and server-side key generation using C509 certificates.
   This document also defines operations for Certificate Revocation List
   (CRL) distribution.
- **draft-lin-idr-bgp-ecmp-ebgp-enhancements-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Enhancements for ECMP EBGP Scenarios](https://datatracker.ietf.org/doc/draft-lin-idr-bgp-ecmp-ebgp-enhancements/) — This document proposes extensions to BGP to apply the RFC 5004 route
   persistence algorithm across parallel EBGP sessions and to suppress
   unnecessary advertisements between EBGP peers in the same AS.

   This document updates RFC 5004.
- **draft-linkova-6man-ununra-01** (new-draft, score 0, ignored_after_review) [none]: [Unicast Unsolicited Router Advertisements for Propagating Network Configuration Updates](https://datatracker.ietf.org/doc/draft-linkova-6man-ununra/) — Multicast transmissions on Wi-Fi links are known to be unreliable,
   making the propagation of critical network configuration changes via
   multicast Router Advertisements (RAs) prone to failure or severe
   delay.  Existing approaches to improve reliability, such as sending
   multiple unsolicited multicast RAs, require fine-tuning timers and
   packet counts that may not fit all deployment scenarios.

   This document updates RFC 4861 by introducing an optimization: when a
   router detects a configuration change that must be propagated to
   hosts, it sends unicast Router Advertisements to every client
   recently observed on that interface.
- **draft-liu-fann-srv6-cc-00** (new-draft, score 0, ignored_after_review) [none]: [Congestion Control Based on SRv6 Path](https://datatracker.ietf.org/doc/draft-liu-fann-srv6-cc/) — This document describes a congestion control solution based on SRv6.
   It defines mechanisms for congestion notification and flow control
   within an SRv6-based network, optimizing congestion handling through
   hierarchical congestion control messages along SRv6 paths.
- **draft-liu-opsawg-ipfix-bgp-vpn-03** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP VPN Information in IPFIX](https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-bgp-vpn/) — This document introduces new IP Flow Information Export (IPFIX)
   information elements to carry information that can be used to
   identify the egress PE in BGP VPN scenarios.
- **draft-liu-srv6ops-sr-protection-06** (new-draft, score 0, ignored_after_review) [none]: [Operational Guidance for Protection Mechanisms in SRv6 Networks](https://datatracker.ietf.org/doc/draft-liu-srv6ops-sr-protection/) — This document describes the Operational Guidance for protection of
   Segment Routing Over IPv6 (SRv6) networks.
- **draft-mahy-oob-aad-00** (new-draft, score 0, ignored_after_review) [none]: [MLS Extension for Out-Of-Band Additional Authenticated Data](https://datatracker.ietf.org/doc/draft-mahy-oob-aad/) — This document specifies an explicit way to signal that the Additional
   Authenticated Data does include or should include data elements that
   are conveyed out-of-band (ex: are not in the MLS message).
- **draft-mankamana-pim-mofrr-failure-detection-00** (new-draft, score 0, ignored_after_review) [none]: [MoFRR Path Liveness for Network Failures](https://datatracker.ietf.org/doc/draft-mankamana-pim-mofrr-failure-detection/) — This document discusses an operational gap in Multicast-Only Fast
   Reroute when failures occur inside an upstream multicast path but do
   not cause a visible RIB or RPF change at the merge point.  The
   document motivates the need for a scalable path-liveness mechanism
   that can detect such hidden multicast delivery failures without
   requiring expensive per-flow packet monitoring.
- **draft-marenamat-grow-route-server-nh-translation-02** (new-draft, score 0, ignored_after_review) [none]: [Route Server Next Hop Translation](https://datatracker.ietf.org/doc/draft-marenamat-grow-route-server-nh-translation/) — With the advent of RFC8950, Internet Exchange Points (IXPs) are
   enabled to rely solely on IPv6 addresses for adressing in their
   peering LANs.  However, routers not supporting RFC8950 are a
   technical roadblock.

   It is easier to extend the capabilities of the IXP Route Server (RS)
   instead of those of every unsupporting router.  Thus, this document
   introduces the concept of Specific Local Address Tables (SLATs).
   SLATs translate BGP next hops between all IXP members, regardless of
   their RFC8950 support, paving the way for IPv6-only IXPs.

   This document also introduces another, more transparent variant of
   BGP next hop translation applicable in IXPs which do not employ ARP
   and ND proxying.

   This document updates RFC 7947 by specifying an allowed route
   modification at the route server.
- **draft-martin-deploying-ipv6-data-center-02** (new-draft, score 0, ignored_after_review) [none]: [Deploying IPv6 in Data Centers](https://datatracker.ietf.org/doc/draft-martin-deploying-ipv6-data-center/) — Data center operators are moving toward IPv6-only operation to
   simplify addressing, restore end-to-end connectivity, and meet
   operator and government timelines.  Much published IPv6 guidance
   targets network engineers; this document instead addresses *Site
   Reliability Engineers (SREs)* and *Software Engineers (SWEs)* who
   deploy, operate, and debug services in *operator-owned data centers*.
   It is organized in two parts after IPv6 fundamentals: a *migration
   program* (transition strategy and observability) and a *technical
   stack* (hardware, provisioning, transport, applications, and
   diagnostics).  It documents common software and infrastructure gaps
   and offers practical deployment patterns aligned with the IPv6
   Operations (v6ops) working group charter.
- **draft-martin-retry-over-ipv6-03** (new-draft, score 0, ignored_after_review) [none]: [HTTP Signaling of Planned IPv4 Unavailability](https://datatracker.ietf.org/doc/draft-martin-retry-over-ipv6/) — As operators transition services to IPv6-only, planned IPv4 outages
   help identify remaining dependencies before permanent decommission.
   Such outages must be measurable, reversible, and understandable to
   end users.  This document defines the 5NN (IPv4 Unavailable) HTTP
   response status code and associated header fields that signal an
   intentional, often time-bounded IPv4 outage, instruct aware clients
   to retry over IPv6 after closing the IPv4 connection, and allow
   clients to confirm successful IPv6 recovery via an optional
   correlation token so operators can distinguish soft failures from
   hard failures in centralized logs.  The mechanism supports staged
   enterprise rollouts, internal HTTP services, and permanent IPv6-only
   migration; coordinated public events (for example, 6/6 drills) remain
   possible with advance notice.  The primary intended deployment is
   operator-controlled environments where provider and users share
   operational responsibility.  Legacy clients that do not implement
   this specification treat an unrecognized 5NN status code as an
   internal server error and MAY use the response body for human-
   readable guidance.
- **draft-mbci-ippm-ioam-template-option-03** (new-draft, score 0, ignored_after_review) [none]: [In Situ Operations, Administration, and Maintenance (IOAM) Template Option](https://datatracker.ietf.org/doc/draft-mbci-ippm-ioam-template-option/) — In situ measurement is performed by incorporating performance related
   information into in-flight data packets.  This document specifies a
   new IOAM Option-Type that has a fixed length and can be updated by
   transit nodes along the path.  It enables lightweight monitoring
   while maintaining a constant length that is not changed in-flight and
   is not affected by the number of hops in the network.
- **draft-munizaga-quic-alternative-server-address-01** (new-draft, score 0, ignored_after_review) [none]: [QUIC Alternative Server Address Frames](https://datatracker.ietf.org/doc/draft-munizaga-quic-alternative-server-address/) — This document specifies an extension to QUIC that allows a server to
   advertise a prioritized set of alternative addresses.  This allows a
   client to migrate the connection as the availability or preference of
   server addresses changes.
- **draft-nordin-ocm-mls-federated-groups-01** (new-draft, score 0, ignored_after_review) [none]: [Federated Groups in Open Cloud Mesh using Messaging Layer Security](https://datatracker.ietf.org/doc/draft-nordin-ocm-mls-federated-groups/) — This document defines an extension to the Open Cloud Mesh (OCM)
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
- **draft-norton-sdlp-sec-arch-03** (new-draft, score 0, ignored_after_review) [none]: [SDLP Security Architecture (SDLP RFC 4)](https://datatracker.ietf.org/doc/draft-norton-sdlp-sec-arch/) — Please let me know if this can not be manually posted for some reason. Thank you for your help.
- **draft-nottingham-feed-menu-01** (new-draft, score 0, ignored_after_review) [none]: [Feed Menus](https://datatracker.ietf.org/doc/draft-nottingham-feed-menu/) — This specification defines Feed Menus, a simplified means of
   discovering the feeds (e.g., RSS or Atom) offered by a Web site.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottingham-feed-menu/.

   information can be found at https://mnot.github.io/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/feed-menu.
- **draft-nottnick-ietf-decisions-00** (new-draft, score 0, ignored_after_review) [none]: [Making Decisions in the IETF](https://datatracker.ietf.org/doc/draft-nottnick-ietf-decisions/) — This document specifies Best Current Practice for making decisions
   within the IETF process.

   It updates Section 3.3 of [RFC2418].

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottnick-ietf-decisions/.

   information can be found at https://projects.mnot.net/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/SHORT.
- **draft-pardue-httpbis-patched-digest-00** (new-draft, score 0, ignored_after_review) [none]: [HTTP Patched Digest](https://datatracker.ietf.org/doc/draft-pardue-httpbis-patched-digest/) — The PATCH method can be used to apply partial modifications to a
   resource.  This document defines the Patched-Digest request field,
   which allows a client to indicate the integrity digest of the
   modified resource once a PATCH operation is applied.  A server can
   use the integrity digest to detect an operation failure and return an
   error.  The Want-Patched-Digest response field is also defined to
   signal server integrity preferences.
- **draft-pignataro-icmp-enviro-info-02** (new-draft, score 0, ignored_after_review) [none]: [ICMP Extensions for Environmental Information](https://datatracker.ietf.org/doc/draft-pignataro-icmp-enviro-info/) — This document defines a data structure that can be appended to
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
- **draft-ramos-asdf-api-translation-03** (new-draft, score 0, ignored_after_review) [none]: [Semantic Definition Format (SDF) for API translation](https://datatracker.ietf.org/doc/draft-ramos-asdf-api-translation/) — This document defines an extension to the Semantic Definition Format
   (SDF) that enables API translation between applications and devices.
   The translation enables clarification of complex syntax for a service
   or device to utilize a different API from the one that was first
   designed to use.
- **draft-ranjbar-regext-rdap-subordinate-referrals-01** (new-draft, score 0, ignored_after_review) [none]: [Redirecting RDAP Queries to Holder-Designated Servers for Subordinate Resources](https://datatracker.ietf.org/doc/draft-ranjbar-regext-rdap-subordinate-referrals/) — Registration Data Access Protocol (RDAP) queries can be resolved from
   the IANA bootstrap registries down to the most specific object held
   by a registry operator's RDAP service.  Where the holder of a
   registered resource maintains registration data for resources
   subordinate to it, such as DNS names below a registered domain or
   more-specific networks below an address allocation, and operates a
   conformant RDAP service for that data, there is currently no
   discoverable referral from the registry's response to the holder's
   service.  This document describes an optional, holder-designated
   referral for subordinate resources, carried by a pair of directional
   RDAP link relations, "rdap-base-down" and "rdap-base-up", whose
   targets are the base URL of a downstream RDAP service and the base
   URL of the covering registry service, respectively.  The holder-
   designated subordinate referral is the primary application, but the
   same relations serve related base-URL discovery needs, including
   delegated and hybrid RPKI referrals.  It is written as input to
   draft-ietf-regext-rdap-referrals and its content may be merged into
   that document.
- **draft-rodenhaeuser-idna-transparent-resolution-00** (new-draft, score 0, ignored_after_review) [none]: [Transparent Handling of Internationalized Domain Names in Name Resolution APIs](https://datatracker.ietf.org/doc/draft-rodenhaeuser-idna-transparent-resolution/) — Applications are expected to convert internationalized domain names
   to their ASCII-Compatible Encoding (A-label) form before invoking
   name resolution APIs.  In practice this conversion is performed
   inconsistently: different applications follow different IDNA
   standards, use different libraries, and ship different versions of
   the Unicode mapping tables, so that the same input string can resolve
   to different registrable domain names depending on which software
   component performs the conversion.

   This document specifies that name resolution services accept Unicode
   host names by default and perform the conversion to A-labels
   internally, exactly once, at the point where a name is handed to a
   specific resolution protocol.  The DNS wire format is unchanged: only
   A-labels appear in queries to the public DNS.  The conversion
   procedure is Unicode IDNA Compatibility Processing (UTS #46),
   nontransitional, with a mapping-table floor of Unicode 15.1.  This
   codifies the architectural recommendation of RFC 6055 and the
   deployed practice of several major platforms.
- **draft-ruan-lsr-isis-te-extensions-for-microburst-01** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Traffic Engineering Extensions For Microburst](https://datatracker.ietf.org/doc/draft-ruan-lsr-isis-te-extensions-for-microburst/) — This document defines IS-IS and OSPF sub-TLVs and a BGP-Link State
   (BGP-LS) Link Attribute TLV for advertising aggregated measurements
   of microburst activity on a unidirectional link.  The information is
   reported for an identified traffic class and includes event, packet-
   drop, and queue-occupancy statistics.  An Anomalous (A) bit carries a
   locally determined anomaly indication.

   This document specifies the encoding and distribution of the
   information.  Microburst detection, loss attribution, threshold
   selection, and actions taken by a consumer are outside the scope of
   this document.
- **draft-sastry-spacerg-space-research-infra-typology-00** (new-draft, score 0, ignored_after_review) [none]: [A typology of Space Research Infrastructures](https://datatracker.ietf.org/doc/draft-sastry-spacerg-space-research-infra-typology/) — Space networking research increasingly relies on a heterogeneous
   ecosystem of software, datasets, experimental platforms, reference
   implementations, and operational research assets.  These resources
   have historically been developed independently by different research
   groups, agencies, and projects, making discovery, comparison,
   interoperability, and reuse difficult.  Existing registries typically
   catalogue tools individually but provide limited guidance on their
   functional role within the research lifecycle.

   This document proposes a typology for research infrastructures
   relevant to the Space Research Group (SPACERG).  Rather than
   classifying resources according to implementation technology or
   project origin, the proposed taxonomy groups resources according to
   their research function.  The typology provides a common vocabulary
   for describing software and non-software research assets, supports
   the organization of community registries, and facilitates
   interoperability, reproducibility, and long-term maintenance of
   research infrastructures.  The classification is intended to evolve
   as new classes of research resources emerge.  The typology is
   implemented by a machine-readable registry of research resources
   maintained by the research group.
- **draft-saum-nvo3-mtu-propagation-over-evpn-overlays-10** (new-draft, score 0, ignored_after_review) [none]: [MTU propagation over EVPN Overlays](https://datatracker.ietf.org/doc/draft-saum-nvo3-mtu-propagation-over-evpn-overlays/) — Path MTU Discovery between end-host-devices/Virtual-Machines/servers/
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
- **draft-saumthimma-evpn-ip-binding-sync-08** (new-draft, score 0, ignored_after_review) [none]: [Secure IP Binding Synchronization via BGP EVPN](https://datatracker.ietf.org/doc/draft-saumthimma-evpn-ip-binding-sync/) — The distribution of clients of L2 domain across extended, networks
   leveraging overlay fabric, needs to deal with synchronizing the
   Client Binding Database.  The 'Client IP Binding' indicates the IP,
   MAC and VLAN details of the clients that are learnt by security
   protocols.  Since learning 'Client IP Binding database' is last mile
   solution, this information stays local to the end point switch, to
   which clients are connected.  When networks are extended across
   geographies, that is, both layer2 and layer3, the 'Client IP Binding
   Database' in end point of switches of remote fabrics should be in
   sync.  This literature intends to align the synchronization of
   'Client IP Binding Database" through an extension to BGP control
   plane constructs and as BGP is a typical control plane protocol
   configured to communicate across network boundries.
- **draft-schinazi-httpbis-ohttp-pfs-01** (new-draft, score 0, ignored_after_review) [none]: [A Perfect Forward Secure Extension to Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-pfs/) — Oblivious HTTP (OHTTP) is a protocol for forwarding encrypted HTTP
   messages.  It does not provide Perfect Forward Secrecy (PFS).
   Chunked OHTTP expands OHTTP to be suitable for longer-lived streams,
   but still does not offer PFS.  Combined, this is leading sensitive
   traffic to de deployed at scale without PFS.  This document proposes
   a solution.
- **draft-silva-hymrpl-01** (new-draft, score 0, ignored_after_review) [none]: [HyMRPL: Per-Node Hybrid Mode of Operation and Inter-DODAG Bridge Mechanism for RPL](https://datatracker.ietf.org/doc/draft-silva-hymrpl/) — The Routing Protocol for Low-Power and Lossy Networks (RPL), defined
   in RFC 6550, enforces a single Mode of Operation (MOP) across all
   nodes within a DODAG.  This rigidity prevents heterogeneous devices
   from independently selecting their forwarding behavior and creates
   permanent isolation between DODAGs operating with different MOPs.

   This document defines HyMRPL, a Hybrid Mode of Operation (MOP=6) that
   enables per-node functional profiles within a single DODAG.  Nodes
   independently adopt Class-S (storing-like) or Class-N (non-storing-
   like) behavior without modifying RPL control message formats.
   Additionally, this document specifies an Inter-DODAG Bridge mechanism
   that uses MOP Extension (MOPex) signaling to interconnect DODAGs with
   different MOPs through cross-DODAG route injection.

   The mechanisms introduce zero additional control messages, maintain
   full backward compatibility via the J-flag in extended options, and
   have been validated with a functional implementation demonstrating
   100% packet delivery ratio across MOP boundaries.
- **draft-singh-apex-psi-02** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-02-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-02/)
- **draft-singh-apex-psi-03** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-03-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/)
- **draft-singh-apex-psi-05** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-05-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/)
- **draft-singh-apex-psi-06** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-06-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-06/)
- **draft-singh-apex-psi-07** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-07-01](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/)
- **draft-singh-apex-psi-08** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-08-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-08/)
- **draft-singh-apex-psi-09** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-09-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-09/)
- **draft-singh-psi-merkle-00** (new-draft, score 0, ignored_after_review) [none]: [PSI Merkle Tree Anchoring for Cryptographic Seals](https://datatracker.ietf.org/doc/draft-singh-psi-merkle/) — This document specifies the Merkle tree construction and anchoring
   protocol used by the Proof of Sovereign Integrity (PSI) system for
   tamper-evident content verification.  It defines tree parameters,
   leaf construction, inclusion proof generation, and root anchoring to
   public ledgers including the Bitcoin blockchain.  The protocol uses
   SHA-256 as the hash function, binary Merkle trees with height=5 (32
   leaves per epoch), and deterministic leaf ordering to enable third-
   party v
- **draft-singh-psi-post-quantum-00** (new-draft, score 0, ignored_after_review) [none]: [PSI Post-Quantum Dual-Signature Sealing](https://datatracker.ietf.org/doc/draft-singh-psi-post-quantum/) — This document specifies the post-quantum cryptographic sealing
   extension for the Proof of Sovereign Integrity (PSI) Protocol.  While
   classical Ed25519 signatures provide current security, the emergence
   of cryptographically relevant quantum computers (CRQCs) threatens all
   elliptic-curve and RSA-based signature schemes.  PSI addresses this
   through dual-signature sealing: each seal carries both an Ed25519
   signature (for immediate classical verification) and an LMS-W4-SHA256
   hash
- **draft-sipos-dtn-manifest-block-01** (new-draft, score 0, ignored_after_review) [none]: [Bundle Protocol (BP) Manifest Block](https://datatracker.ietf.org/doc/draft-sipos-dtn-manifest-block/) — This document defines an extension block type for Bundle Protocol
   version 7 to capture discretionary summary data about the state of a
   Bundle at the time the extension block is added.  This Manifest
   structure is a general purpose container for information about other
   blocks, and can be used as a piece-part of a larger security
   operation.
- **draft-skyfire-oauth-aml-methods-00** (new-draft, score 0, ignored_after_review) [none]: [Anti-Money Laundering Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-aml-methods/) — Financial regulations require application of Anti-Money Laundering
   (AML) and Countering the Financing of Terrorism (CFT) methods in many
   jurisdictions worldwide.  This specification defines a claim and
   values for declaring what AML/CFT methods were employed.
- **draft-smc-grow-bmp-route-change-stats-01** (new-draft, score 0, ignored_after_review) [none]: [BMP Route Change Statistics Based on Routing Policy](https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/) — This document defines few generic BGP Monitoring Protocol (BMP)
   statistics for monitoring route modifications or changes due to
   applying Routing Policy.  These statistics are reported per BGP peer
   using the BMP Statistics Report message.
- **draft-smith-6man-accurate-ra-router-lifetime-01** (new-draft, score 0, ignored_after_review) [none]: [More Accurately Naming IPv6 RA Router Lifetime](https://datatracker.ietf.org/doc/draft-smith-6man-accurate-ra-router-lifetime/) — IPv6 Router Advertisements (RAs) have a "Router Lifetime" field,
   which specifies how long the advertising router will act as a default
   router for the receiving hosts, unless refreshed with another
   advertisement.  The field name "Router Lifetime" is quite general,
   and could easily be misunderstood to mean the bounded lifetime of all
   of the information contained in the RA.  This memo more accurately
   renames this field "Default Router Lifetime".
- **draft-soares-sustain-green-security-00** (new-draft, score 0, ignored_after_review) [none]: [Research Directions on Energy-Aware Security Mechanisms](https://datatracker.ietf.org/doc/draft-soares-sustain-green-security/) — With the advancement of the climate emergency, all areas of human
   activity are expected to continuously assess their Greenhouse Gas
   emissions and encourage the use of clean energy as much as possible.
   The current discussion on green networking in the Network Management
   research field still needs to be expanded to the adjoined areas, such
   as Network Security.  This document outlines possible research
   directions for energy-aware security mechanisms.
- **draft-song-opsawg-ipfix-ecn-03** (new-draft, score 0, ignored_after_review) [none]: [Export of ECN Information in IPFIX](https://datatracker.ietf.org/doc/draft-song-opsawg-ipfix-ecn/) — This document defines a set of IPFIX Information Elements for
   monitoring Explicit Congestion Notification (ECN), specifically in
   the context of the Low Latency, Low Loss, and Scalable Throughput
   (L4S) service.  These Information Elements allow network operators to
   observe ECN codepoint usage within L4S deployments and evaluate the
   corresponding traffic performance.
- **draft-stone-spring-mpte-sr-03** (new-draft, score 0, ignored_after_review) [none]: [Multipath Traffic Engineering for Segment Routing](https://datatracker.ietf.org/doc/draft-stone-spring-mpte-sr/) — This document describes a mechanism to achieve Multipath Traffic
   Engineering for Segment Routing based networks.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Source Packet Routing
   in Networking Working Group mailing list (spring@ietf.org), which is
   archived at https://mailarchive.ietf.org/arch/browse/spring/.

   Source for this draft and an issue tracker can be found at
   https://github.com/astone282/draft-stone-spring-mpte-sr.
- **draft-test-psi-00** (new-draft, score 0, ignored_after_review) [none]: [Test PSI Submission](https://datatracker.ietf.org/doc/draft-test-psi/) — Test submission.
- **draft-thomson-ptth-potato-02** (new-draft, score 0, ignored_after_review) [none]: [(Potato) - HTTP, Inverted](https://datatracker.ietf.org/doc/draft-thomson-ptth-potato/) — This document defines 🥔
   (‮P̷̙̩̩̖̦̦̮̲͖͗̅͋̇̊o̷̢͚̼͎͉̙̩̻̱̊̂̽̀̅̚͟͡t̴̤̖̞͖̰̐̇̋̍̑̓̏̕͝ȁ̷̩̹͎͖̮͚͋͑̏̀̓̂͡͞ͅt̗̹̩̭͈̳̫͈͈̒͆̃̿̚͝͠o͖͓͈̩̻̤͎͐̐͐̅̂́͟‬),
   a suite of reversed versions of HTTP for origin servers.
- **draft-todo-kevinmcm-tutorial-00** (new-draft, score 0, ignored_after_review) [none]: [kevinmcm - Github tutorial](https://datatracker.ietf.org/doc/draft-todo-kevinmcm-tutorial/) — This is where the abstract should be written

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at https://kevinmcm-
   github.github.io/github-tutorial/draft-todo-kevinmcm-tutorial.html.
   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-todo-kevinmcm-tutorial/.

   Source for this draft and an issue tracker can be found at
   https://github.com/kevinmcm-github/github-tutorial.
- **draft-trammell-443-is-enough-01** (new-draft, score 0, ignored_after_review) [none]: [443 is Enough: Guidance on Port Allocation for HTTP-based Services](https://datatracker.ietf.org/doc/draft-trammell-443-is-enough/) — [RFC7605] provides guidance on the use of port numbers and the
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
- **draft-vanmook-expanse-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Extending Policy, Addressing and Numbering across Space Ecosystems (EXPANSE): Problem Statement](https://datatracker.ietf.org/doc/draft-vanmook-expanse-problem-statement/) — Ongoing IETF work on networking in non-terrestrial and deep-space
   environments treats addressing, numbering, and registry policy as a
   greenfield.  It is not.  Three decades of operational practice,
   registry governance, and routing security infrastructure exist, and
   any space-segment architecture that ignores them will recreate,
   badly, the coordination mechanisms the Internet already has.  This
   document describes the problem and motivates chartering a working
   group to address it.
- **draft-vyncke-intarea-legacy-registries-01** (new-draft, score 0, ignored_after_review) [none]: [Updates to Legacy IANA Registries](https://datatracker.ietf.org/doc/draft-vyncke-intarea-legacy-registries/) — IANA maintains several registries that were created for IPv4.  As the
   IPv4 core specification is no longer being extended and as some other
   registries do not have a defined IANA registration procedure, these
   registries need to be updated to indicate a registration procedure or
   to reflect the current practice that defining such extensions is not
   recommended.
- **draft-westerbaan-dnssec-mldsa-02** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice Digital Signature Algorithm for DNSSEC](https://datatracker.ietf.org/doc/draft-westerbaan-dnssec-mldsa/) — This document describes how to specify Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) keys and signatures in DNS Security
   (DNSSEC).  It uses the ML-DSA-44 parameter set defined in FIPS 204.
   ML-DSA-44 is believed to be secure even against adversaries in
   possession of a cryptographically relevant quantum computer.
- **draft-wu-idr-flowspec-redirect-group-02** (new-draft, score 0, ignored_after_review) [none]: [BGP Flowspec Redirect Load Balancing Group Community](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-redirect-group/) — This document defines an extension to the BGP Community Container
   Attribute, which allows flowspec redirection to multiple paths.  This
   extended community serves to redirect traffic to a load balancing
   group and supports both equal-cost multi-path (ECMP) and unequal-cost
   multi-path (UCMP) scenarios.
- **draft-zaeschke-scion-quic-multipath-01** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for QUIC Multipath over SCION](https://datatracker.ietf.org/doc/draft-zaeschke-scion-quic-multipath/) — This document provides informational guidance for using the Multipath
   Extension for QUIC with the SCION networking technology.

   SCION is an inter-domain routing protocol that supports path-aware
   multi-path networking.  The multiple paths and their associated path
   information offered by SCION provide opportunities as well as
   challenges for combining QUIC-MP with SCION.

   This document explores various aspects of this combination, such as
   algorithms for congestion control, RTT estimation, and general
   application scenarios.  In addition, it provides techniques and
   guidance to maintain the security of QUIC-MP and SCION, and to
   leverage path-aware multi-path networking with QUIC-MP.
- **draft-zedongjia-v6ops-ipv6eh-measurement-01** (new-draft, score 0, ignored_after_review) [none]: [Observations on the Reachability and Evasion of Packets with IPv6 Extension Headers on the Internet](https://datatracker.ietf.org/doc/draft-zedongjia-v6ops-ipv6eh-measurement/) — IPv6 Extension Headers (EHs) are designed to provide protocol
   flexibility and support for emerging features, while maintaining a
   concise base header and efficient processing.  In practice, their
   reachability is affected by middlebox handling along the path, and
   their flexibility also introduces security considerations.

   This document presents observations from a comprehensive, large-scale
   measurement study of IPv6 Extension Header path traversal across more
   than 23,000 autonomous systems.  Using a feedback-driven measurement
   framework called 6Travel, the reachability of 11 common IPv6
   Extension Headers is measured over ICMPv6, TCP, and UDP.  The
   measurements indicate a change relative to earlier work: contrary to
   past observations of heavy filtering, specific Extension Headers now
   achieve reachability comparable to plain traffic.  Two distinct forms
   of policy ossification are observed across industry categories,
   together with widespread potential Extension-Header-based firewall
   evasion signatures in nearly 5,000 autonomous systems, particularly
   under TCP and UDP.  These signatures appear consistent with a
   combination of implementation flaws and security misconfigurations,
   spanning both on-path and host-side firewalls.
- **draft-zhang-ippm-isft-space-flow-telemetry-00** (new-draft, score 0, ignored_after_review) [none]: [In-situ Space Flow Telemetry for IPv6 Limited Domains](https://datatracker.ietf.org/doc/draft-zhang-ippm-isft-space-flow-telemetry/) — Space networks, including satellite networks, often operate with
   constrained bandwidth, processing capacity, storage, and energy,
   while also experiencing dynamic topology and frequent link changes.
   Existing in-situ Operations, Administration, and Maintenance (IOAM)
   mechanisms provide useful per-packet telemetry, but the packet
   overhead and field selection flexibility can be costly in such
   environments.

   This document specifies In-situ Space Flow Telemetry (ISFT), a
   compact telemetry profile for IPv6 limited domains.  ISFT defines an
   8-octet telemetry option header, a small set of telemetry templates
   for delay, loss, and congestion information, and processing behavior
   for encapsulating, transit, and decapsulating nodes.  ISFT is
   intended for controlled domains such as space-network segments and
   MUST NOT be exposed as an Internet-wide protocol behavior.

## Errors / fetch failures

- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
