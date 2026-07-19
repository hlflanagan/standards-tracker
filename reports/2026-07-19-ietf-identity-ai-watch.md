# IETF Identity + AI Standards Watch

Date: 2026-07-19

## Read now

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
- **draft-sabey-succession-receipts-sd-00** (new-draft, score 11, verifiable_claims) [none]: [Selective Disclosure for Succession Receipts](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts-sd/) — A Succession Receipt proves one completed, policy-gated transfer of
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
- **draft-singh-apex-psi-03-00** (new-draft, score 11, core_identity) [none]: [PSI-03: VPP Dispatch Conformance Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/) — PSI-03 specifies a portable, Ed25519-signed bond that anchors a
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
- **draft-singh-psi-age-assurance-00** (new-draft, score 10, core_identity) [none]: [PSI Zero-Knowledge Age Assurance Attestation](https://datatracker.ietf.org/doc/draft-singh-psi-age-assurance/) — This document specifies PSI-Age, a privacy-preserving cryptographic
   attestation for age assurance.  It enables a relying party (such as a
   social media platform or online service) to verify that a user meets
   a minimum age threshold without learning the user's identity, date of
   birth, or any other personal attribute.  PSI-Age uses zero-knowledge
   range proofs over a committed birthdate to produce a compact,
   verifiable "age credential" that proves age >= threshold without rev
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
- **draft-sabey-succession-receipts-00** (new-draft, score 8, adjacent_watchlist) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
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
   with Ed25519), and the verification algorithm, including
   bidirectional claim grounding.  Where decision receipts prove what an
   agent did, and delegation receipts prove what an agent may do,
   Succession Receipts prove that an agent legitimately became the
   holder of an authority.
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
- **draft-hwang-silp-protocol-00** (new-draft, score 7, adjacent_watchlist) [none]: [Semantic Interlingua Layer Protocol (SILP): A Payload Codec for Cross-Model Agent Communication](https://datatracker.ietf.org/doc/draft-hwang-silp-protocol/) — This document specifies the Semantic Interlingua Layer Protocol
   (SILP), a black-box, text-interface payload codec designed for cross-
   model agent-to-agent communication.  SILP defines a coarse-grained
   action-slot intermediate representation (IR) as the canonical
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

## Monitor

- **draft-ietf-nmop-message-broker-telemetry-message-05** (new-draft, score 6, trust_infrastructure) [nmop]: [Extensible YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-ietf-nmop-message-broker-telemetry-message/) — This document defines an extensible message schema in YANG to be used
   at data collection to transform Network Telemetry messages into
   external systems such as Message Brokers.  The extensible message
   schema enables data collectors to add metadata for the provenance of
   the operational network data.
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
- **draft-sabey-refusal-transparency-00** (new-draft, score 6, trust_infrastructure) [none]: [Refusal Transparency: Signed, Replay-Resistant Evidence of Refused Agent-System Transitions](https://datatracker.ietf.org/doc/draft-sabey-refusal-transparency/) — A governance system for autonomous agents is defined as much by what
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
- **draft-singh-apex-psi-08-00** (new-draft, score 5, trust_infrastructure) [none]: [PSI-08: Health Records Access Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-08/) — PSI-08 specifies a format for composing multiple Digital Gallows
   predicates into a verifiable chain.  Each link in the chain is a
   signed predicate output that serves as input to the next, enabling
   verifiable multi-step inference without a trusted intermediary.
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

## Adjacent / watchlist

- **draft-farrokhi-dnsop-ede-nta-01** (new-draft, score 3, adjacent_watchlist) [none]: [Disclosure of Negative Trust Anchors in DNS Responses](https://datatracker.ietf.org/doc/draft-farrokhi-dnsop-ede-nta/) — This document describes a mechanism for disclosing that a Negative
   Trust Anchor (NTA) was in effect at the time that a DNS response was
   generated, using an Extended DNS Error (EDE).
- **draft-huang-spring-pppoe-srv6-00** (new-draft, score 3, core_identity) [none]: [SRv6 for PPPoE Transport](https://datatracker.ietf.org/doc/draft-huang-spring-pppoe-srv6/) — This document proposes a method that employs SRv6 underlay tunnel to
   transport PPPoE session information across broadband networks.  By
   leveraging the programmability of SRv6 SIDs, the approach not only
   delivers trusted authentication and secure subscriber access, but
   also enables operators to offer differentiated services and flexibly
   instantiate network functions for broadband users.
- **draft-ietf-lsr-isis-flex-algo-yang-20** (new-draft, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for IS-IS Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-flex-algo-yang/) — This document defines a YANG data model to support IS-IS Application-
   Specific Link Attributes and Flexible Algorithm.
- **draft-ietf-lsr-ospf-flex-algo-yang-15** (new-draft, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for OSPF Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-ospf-flex-algo-yang/) — This document defines a YANG data model to support OSPF Application-
   Specific Link Attributes and Flexible Algorithm.  It also creates the
   initial version of IANA-maintained YANG modules for IGP Algorithm
   Types, IGP Metric-Types, and IGP Link Attribute Applications.

   This document updates RFCs 8665, 9350, and 9843.
- **draft-muks-dns-nta-feed-zones-00** (new-draft, score 3, adjacent_watchlist) [none]: [DNS NTA feed zones](https://datatracker.ietf.org/doc/draft-muks-dns-nta-feed-zones/) — This memo documents a method for expressing a list of DNS negative
   trust anchors [RFC7646] inside a specially constructed DNS zone, that
   validating recursive name servers and other DNSSEC validators may
   configure negative trust anchors from.
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
- **draft-singh-apex-psi-07-00** (new-draft, score 3, trust_infrastructure) [none]: [PSI-07: Organic Production Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/) — PSI-07 defines a standard signal format for regulatory events
   detected by automated monitoring systems.  The format is a signed
   JSON envelope carrying the event classification, evidence hash, and
   jurisdiction code, enabling autonomous reporting to one or more
   regulators without human intervention.
- **draft-skyfire-oauth-kyapay-token-exchange-01** (new-draft, score 3, authorization) [none]: [KYAPay Token Exchange](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token-exchange/) — This specification describes how KYAPay tokens can be exchanged for
   OAuth access tokens to dynamically grant agents access to resources
   they need to accomplish their mission.
- **draft-sullivan-cfrg-raae-02** (new-draft, score 3, core_identity) [none]: [Random-Access Authenticated Encryption](https://datatracker.ietf.org/doc/draft-sullivan-cfrg-raae/) — This document defines random-access authenticated encryption (raAE),
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
- **draft-zw-idr-bgp-orf-yang-model-01** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for BGP Outbound Route Filtering](https://datatracker.ietf.org/doc/draft-zw-idr-bgp-orf-yang-model/) — This document defines YANG data models for managing BGP Outbound
   Route Filter (ORF), including Address Prefix ORF, Covering Prefixes
   ORF (CP-ORF), and VPN Prefix ORF.
- **draft-agent-gw-02** (new-draft, score 2, ignored_after_review) [none]: [Agent Communication Gateway for Semantic Routing and Working Memory](https://datatracker.ietf.org/doc/draft-agent-gw/) — This document presents an architectural framework for an Agent
   Communication Gateway (Agent-GW), designed to support large-scale,
   heterogeneous, and dynamic multi-agent collaboration across
   administrative and protocol boundaries.

   As agents evolve from isolated entities to a collaborative digital
   workforce, the infrastructure must transition from rigid, endpoint-
   based connectivity to intent-based interaction.  This draft proposes
   Agent-GW as an infrastructure hub that provides native primitives for
   Semantic Routing (dispatching tasks by intent and capability),
   Working Memory (shared structured context across multi-step
   workflows), automated protocol adaptation (normalizing heterogeneous
   interfaces into a unified agent-facing protocol), oracle-free agent
   evaluation, and collaborative inference acceleration via a Knowledge
   Delivery Network (KDN).

   Beyond a single-gateway deployment, this document defines a
   hierarchical architecture for wide-area, multi-domain agent networks:
   three gateway tiers (access, domain, and inter-domain).  It describes
   which traffic classes traverse which tiers on both the data plane and
   the control plane, and specifies cross-domain semantic routing, name
   resolution, resilience, and operational considerations.
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
- **draft-singh-apex-psi-05-00** (new-draft, score 2, ignored_after_review) [none]: [PSI-05: Financial Disclosure Integrity](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/) — PSI-05 defines the royalty schedule that MAY be levied by a
   publishing foundation for commercial, litigation, regulatory, or AI-
   training reuse of PSI public ledger data above a threshold defined by
   the foundation's charter.  It establishes a flat-rate per-row fee
   schedule, exemption categories, and an audit protocol.
- **draft-wang-mcast4ai-p2mp-scaleup-00** (new-draft, score 2, ignored_after_review) [none]: [AI P2MP Multicast in Scale-UP Network](https://datatracker.ietf.org/doc/draft-wang-mcast4ai-p2mp-scaleup/) — MoE (Mixture-of-Experts) has been adopted in scale-up GPU connections
   by the mainstream Large Language Models, such as Llama4, Mixtral, and
   DeepSeekV3.  This document focuses on the AI multicast protocol
   evolution for MoE in scale-up scenarios, analyzing the challenges and
   proposing potential protocol evolutions.

## Ignored after review

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
- **draft-cui-idr-flowspec-feedback-roadmap-00** (new-draft, score 0, ignored_after_review) [none]: [Problem Statement and Roadmap for BGP FlowSpec Monitoring](https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-roadmap/) — This document describes the problem space and roadmap for monitoring
   BGP Flow Specification (FlowSpec) deployments.  It outlines the
   operational motivation for FlowSpec monitoring, identifies
   representative classes of monitoring information, and positions
   relevant work on FlowSpec, the BGP Monitoring Protocol (BMP), IP Flow
   Information Export (IPFIX), and YANG-based operational state within a
   common framework.  The resulting roadmap provides common context for
   related protocol-specific work in the relevant IETF working groups.
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
- **draft-geng-grow-bmp-rel-enhancement-02** (new-draft, score 0, ignored_after_review) [none]: [Log More Routing Events in the BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/) — The Route Event Logging (REL) message is defined in
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
- **draft-ietf-bmwg-sr-bench-meth-07** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR)](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) performance for Segment Routing over IPv6 (SRv6) and MPLS (SR-
   MPLS).
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
- **draft-ietf-idr-rfc4360-bis-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extended Communities Attribute](https://datatracker.ietf.org/doc/draft-ietf-idr-rfc4360-bis/) — This document describes the "Extended Communities" BGP-4 attribute.
   This attribute provides a mechanism for labeling information carried
   in BGP-4.  These labels can be used to control the distribution of
   this information, or for other applications.

   This document obsoletes RFC 4360.

   This document also updates RFC 5701 by adding an "Operational
   Considerations" section.
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
- **draft-ietf-ntp-nts-keyexchange-pool-01** (new-draft, score 0, ignored_after_review) [ntp]: [NTS extensions for enabling pools](https://datatracker.ietf.org/doc/draft-ietf-ntp-nts-keyexchange-pool/) — The aim of this document is to describe a system for NTS pools that
   are able to be used by clients without any knowledge beyond plain
   NTS.  The work here focuses purely on creating an intermediate NTS
   Key Exchange server that can be configured with the addresses of
   multiple servers and distribute load between them.  The parts of pool
   operation dealing with managing the list of servers are left out of
   scope for this work.
- **draft-ietf-regext-epp-same-entity-01** (new-draft, score 0, ignored_after_review) [regext]: [Same Entity Set Support for EPP](https://datatracker.ietf.org/doc/draft-ietf-regext-epp-same-entity/) — This document defines an EPP extension allowing clients to learn
   about and manipulate a set of objects in a shared central repository
   that are necessarily tied to the same entity (typically domain
   objects whose names are equivalent in a registry-defined way and are
   tied to a single registrant).  The extension supports multiple
   registries with a shared definition of equivalence using a shared
   central repository.
- **draft-ietf-srv6ops-problem-summary-02** (new-draft, score 0, ignored_after_review) [srv6ops]: [SRv6 Deployment and Operation Problem Summary](https://datatracker.ietf.org/doc/draft-ietf-srv6ops-problem-summary/) — This document aims to provide a concise overview of the common
   problems encountered during SRv6 deployment and operation, which
   provides foundations for further work, including for example of
   potential solutions and best practices to navigate deployment.
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
- **draft-liao-ace-est-c509-02** (new-draft, score 0, ignored_after_review) [none]: [EST for C509 Certificates](https://datatracker.ietf.org/doc/draft-liao-ace-est-c509/) — This document defines Enrollment over Secure Transport (EST) protocol
   operations over HTTPS and secure CoAP for use with C509 certificates.
   The operations specified in this document support CA certificate
   distribution, C509 certificate enrollment, C509 certificate re-
   enrollment, and server-side key generation using C509 certificates.
   This document also defines operations for Certificate Revocation List
   (CRL) distribution.
- **draft-liu-fann-srv6-cc-00** (new-draft, score 0, ignored_after_review) [none]: [Congestion Control Based on SRv6 Path](https://datatracker.ietf.org/doc/draft-liu-fann-srv6-cc/) — This document describes a congestion control solution based on SRv6.
   It defines mechanisms for congestion notification and flow control
   within an SRv6-based network, optimizing congestion handling through
   hierarchical congestion control messages along SRv6 paths.
- **draft-liu-srv6ops-sr-protection-06** (new-draft, score 0, ignored_after_review) [none]: [Operational Guidance for Protection Mechanisms in SRv6 Networks](https://datatracker.ietf.org/doc/draft-liu-srv6ops-sr-protection/) — This document describes the Operational Guidance for protection of
   Segment Routing Over IPv6 (SRv6) networks.
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
- **draft-singh-apex-psi-02** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-02-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-02/)
- **draft-singh-apex-psi-03** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-03-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/)
- **draft-singh-apex-psi-05** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-05-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/)
- **draft-singh-apex-psi-06** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-06-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-06/)
- **draft-singh-apex-psi-07** (new-draft, score 0, ignored_after_review): [draft-singh-apex-psi-07-00](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/)
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
- **draft-skyfire-oauth-aml-methods-00** (new-draft, score 0, ignored_after_review) [none]: [Anti-Money Laundering Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-aml-methods/) — Financial regulations require application of Anti-Money Laundering
   (AML) and Countering the Financing of Terrorism (CFT) methods in many
   jurisdictions worldwide.  This specification defines a claim and
   values for declaring what AML/CFT methods were employed.
- **draft-todo-kevinmcm-tutorial-00** (new-draft, score 0, ignored_after_review) [none]: [kevinmcm - Github tutorial](https://datatracker.ietf.org/doc/draft-todo-kevinmcm-tutorial/) — This is where the abstract should be written

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at https://kevinmcm-
   github.github.io/github-tutorial/draft-todo-kevinmcm-tutorial.html.
   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-todo-kevinmcm-tutorial/.

   Source for this draft and an issue tracker can be found at
   https://github.com/kevinmcm-github/github-tutorial.
- **draft-vyncke-intarea-legacy-registries-01** (new-draft, score 0, ignored_after_review) [none]: [Updates to Legacy IANA Registries](https://datatracker.ietf.org/doc/draft-vyncke-intarea-legacy-registries/) — IANA maintains several registries that were created for IPv4.  As the
   IPv4 core specification is no longer being extended and as some other
   registries do not have a defined IANA registration procedure, these
   registries need to be updated to indicate a registration procedure or
   to reflect the current practice that defining such extensions is not
   recommended.
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
