# IETF Identity + AI Standards Watch

Date: 2026-08-29

## Read now

- **draft-sharif-apki-agent-pki-01** (new-draft, score 34, adjacent_watchlist) [none]: [Agent Public Key Infrastructure (APKI): Certificate-Based Identity and Trust for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-sharif-apki-agent-pki/) — Autonomous artificial intelligence (AI) agents are increasingly
   performing actions on the Internet that require verifiable identity:
   financial transactions, regulated data access, tool invocations,
   and inter-agent coordination.  Traditional Public Key Infrastructure
   (PKI) based on X.509 certificates was designed for human-operated
   clients and long-lived servers.  It lacks primitives for graduated
   trust scoring, capability constraints, delegation chains, model
   provenance, and the ephemeral lifecycles characteristic of AI
   agents.

   This document defines Agent Public Key Infrastructure (APKI), a
   certificate-based identity and trust system for autonomous AI
   agents.  APKI extends X.509v3 with five agent-specific extensions,
   defines the agent:// URI scheme for agent identification, specifies
   Agent Transparency Logs modelled on Certificate Transparency
   (RFC 9162), and provides mechanisms for cross-organizational trust
   federation.  APKI is designed to be compatible with existing PKI
   deployments, SPIFFE workload identity, and the IETF WIMSE working
   group's specifications.
- **draft-sato-soos-gar-06** (new-draft, score 32, trust_infrastructure) [none]: [The Governance Audit Record (GAR) for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-sato-soos-gar/) — This document specifies the Governance Audit Record (GAR), the audit
   architecture for agentic AI systems.  GAR defines five audit types,
   the Session Audit Record (SAR), the Audit Alert system, auditor
   principal categories, and the Audit Package for external regulatory
   inspection.  GAR provides verifiable evidence that AI agent sessions
   were governed in accordance with the Intent Declaration Primitive and
   the Human Escalation Mechanism.  GAR answers the governance question:
   can any of this be proven to a regulator?  GAR is a domain-specific
   application of the SCITT (Supply Chain Integrity, Transparency and
   Trust) architecture extended with causal ordering semantics for
   agentic governance events.  GAR defines the Authority Lifecycle Event
   (ALE) category: a normative set of causally-ordered event types
   covering the complete agent session revocation and recovery
   lifecycle, including single-agent revocation, authority suspension,
   partial state recording, recovery initiation, credential restoration,
   and multi-agent delegation tree events.

   Version -03 adds the SOOS Governance Semantic Convention: the
   normative soos.governance.* OpenTelemetry attribute namespace for
   governance observability, the SOOS GAR Processor specification for
   OTel-to-SAR pipeline construction with Session Block Merkle
   integrity, four new Authority Lifecycle Events, three mandatory
   provenance fields on Cedar evaluation records, and the XPID mirror
   field on ACD session ALEs.

   Version -04 made the Session Block construction rules more explicit,
   closing three ambiguities found during independent interop
   verification at the IETF 126 Hackathon.

   Version -05 supersedes -04's Session Block construction text with a
   corrected construction: the Merkle leaf and internal-node hashes are
   now domain-separated (RFC 9162's Merkle Tree Hash, with 0x00/0x01
   prefix octets) and odd-length levels use RFC 9162's k-split recursive
   tree shape rather than duplicate-node padding, closing a malleability
   class structurally equivalent to CVE-2012-2459 that was present in
   -04's construction.  This revision is fully self-contained: unlike
   -03 and -04, it does not carry forward unreproduced text from an
   earlier version.  Version -05 also adds a subject_digest field to
   Cedar-evaluation GAR records, the same construction used by the Agent
   Accountability Composition as its cross-slot join key, positioning
   GAR as a conforming AEP instance under the RATS-bound composition;
   the field is normatively scoped to prohibit independent re-
   serialization where an upstream party has already established the
   action's canonical serialization, per the failure mode documented in
   the SCITT typed-reference specification.

   Version -06 closes gaps surfaced by a WIMSE-style security review
   pass against -05's own text and reference sample code: a JWKS trust-
   anchor bootstrap requirement, a corrected key-compromise remediation
   procedure that no longer requires re-signing already-committed audit
   artifacts, an explicit Level 1/2 residual-risk disclosure for a
   compromised-but-signing GEC, a defined failure path for KIA signer
   quorum failure at Session Block close, referential-integrity
   enforcement for causal_parent_id, and guidance against alert-fatigue
   false positives in session_sequence_number gap detection.  This
   revision also carries an idnits repair pass covering reference
   classification, citation hygiene, and formatting.
- **draft-das-hardware-enforced-execution-finality-00** (new-draft, score 29, core_identity) [none]: [Hardware-Rooted National Control to Prevent Covert Intelligence Data Export and Unauthorized Frontier and Neural AI/Autonomous Acts in Critical Infrastructure](https://datatracker.ietf.org/doc/draft-das-hardware-enforced-execution-finality/) — Modern security architecture has traditionally focused on who or what
   may access a system, data object, network, device, application, or
   service.  Authentication, authorization, sandboxing, access control,
   encryption, application permissions, network policy, identity
   management, and audit logging were generally sufficient when most
   consequential operations were initiated, reviewed, or completed
   through relatively predictable human-directed software flows.

   That assumption is changing.

   Ten years ago, there was substantially less need for a distinct
   execution-finality security layer because most artificial-
   intelligence systems were primarily analytical, classificatory,
   predictive, or advisory.  A model could classify an image, rank
   search results, recommend content, detect patterns, translate text,
   or generate a prediction, but it generally could not autonomously
   discover external tools, recruit other agents, operate browsers,
   invoke APIs, modify persistent memory, initiate payments, reconfigure
   networks, control accelerators, export sensitive information,
   communicate directly with machines, or cause physical and
   communications effects at machine speed.  The human operator,
   application workflow, operating system, or another conventional
   software boundary often remained the practical final boundary between
   computation and consequence.

   In contemporary agentic and autonomous systems, that boundary is
   increasingly disappearing.  A model output may become a tool call; a
   tool call may become an API transaction; an autonomous agent may
   delegate to another agent; an application with location access may
   automatically transmit precise coordinates; an AI-controlled network
   function may modify routing or resource allocation; and an AI-
   generated instruction may become a payment, RF emission, satellite
   command, memory write, database commit, network transmission, or
   actuator signal without a separate technical decision immediately
   before the consequence occurs.

   This creates a different class of security problem:

   successful computation, authentication, data access, application
   permission, model approval, or upstream authorization does not
   necessarily establish authority for the resulting consequence.

   Precise geolocation provides a particularly important example.

   Traditional mobile-security models frequently treat location
   permission as an application-level access question: whether an
   application may obtain location information.  In the AI era, however,
   precise latitude and longitude should increasingly be treated as
   high-value inference material rather than as ordinary application
   metadata.

   A single GPS coordinate may reveal little.  Thousands or millions of
   coordinates, timestamps, movement traces, device observations,
   proximity records, public-map information, telemetry signals,
   communications metadata, and other apparently low-sensitivity
   fragments can be correlated by modern AI systems to infer information
   that was never explicitly contained in any individual record.

   Such inference may reveal movement patterns, home and workplace
   relationships, protected-person movements, operational routines,
   sensitive infrastructure, military activity, research facilities,
   industrial sites, or other strategically significant information.

   The important security problem is therefore no longer limited to:

   "Was the secret database breached?"

   A future attacker or intelligence system may instead ask:

   "Can the secret be reconstructed from ordinary data that many
   applications were permitted to collect?"

   This distinction becomes increasingly important because contemporary
   machine-learning systems can perform correlation, clustering, anomaly
   detection, temporal analysis, multimodal fusion, relationship
   inference, and large-scale pattern recognition far more rapidly and
   economically than was practical for routine use a decade ago.

   The inference itself was not impossible ten years ago.  What has
   changed is its scale, automation, cost, speed, and accessibility.

   Accordingly, not every application, SDK, analytics component,
   advertising library, AI agent, browser process, cloud service, or
   external endpoint should automatically receive precise GPS
   coordinates merely because some component of the application stack
   possesses location permission.

   A weather application may need only a city.

   A local-search application may need only an approximate area.

   A recommendation service may require a regional location.

   An emergency, navigation, rescue, or safety-critical application may
   legitimately require exact coordinates.

   An unrelated analytics or advertising component may require no
   location at all.

   Precise location should therefore be treated not merely as readable
   data, but as a consequence-bearing disclosure whose permitted
   precision can be independently verified before release.

   This document describes a hardware-rooted execution-finality
   architecture in which a proposed consequence-bearing operation is
   represented as a Candidate Act and maintained in a Non-Effective
   State until protected validation and independent Finality Sink
   verification succeed.

   A Protected Enforcement Domain evaluates act-specific conditions that
   may include authority, purpose, instruction provenance, requesting
   application or agent identity, permitted scope, recipient,
   destination, jurisdiction, data class, data precision, policy epoch,
   revocation state, protected state, runtime behavior, permitted
   consequence class, and Finality Sink identity.

   Protected validation evidence is committed before, or atomically
   with, release of scoped non-bearer finality authority.

   The applicable Finality Sink independently verifies that authority
   immediately before the operation becomes externally or operationally
   effective.

   For a location-data Candidate Act, the result may therefore be:

   exact location permitted;

   coarse location permitted;

   city-level or regional location permitted;

   delayed, randomized, grid-based, or otherwise reduced location
   permitted; or

   location disclosure denied.

   If exact coordinates are not authorized, possession of exact
   coordinates inside the application or protected environment does not
   itself authorize those coordinates to cross the relevant data-egress
   boundary.

   The architecture is jurisdiction-neutral.  It does not prescribe
   whether the governing rule originates in the United States, the
   European Union, China, India, another sovereign jurisdiction, an
   enterprise policy, a telecommunications operator, or a user-
   controlled privacy policy.

   Instead, it provides a technical mechanism by which the applicable
   regulatory, sovereign, organizational, contractual, or user-
   authorized policy can be evaluated before a protected consequence
   becomes effective.

   Thus, a system may determine:

   "This application is allowed to use exact GPS locally, but this
   destination is authorized to receive only city-level location."

   or:

   "This recipient is authorized to receive exact coordinates for
   emergency response."

   or:

   "This foreign destination is not authorized to receive this location
   information."

   The same architectural principle applies beyond location information
   to agentic AI, sovereign data export, AI-native 5G and 6G, O-RAN, GPU
   and accelerator egress, confidential computing, satellite and non-
   terrestrial networks, financial settlement, and cyber-physical
   infrastructure.

   This requirement becomes still more important as 6G develops.

   The International Telecommunication Union's IMT-2030 framework for 6G
   includes Artificial Intelligence and Communication and Integrated
   Sensing and Communication as distinct usage scenarios.  Current
   IMT-2030 work also anticipates substantially enhanced positioning and
   sensing capabilities, including object detection, localization,
   mapping, AI-enabled processing, ubiquitous intelligence, and very
   high precision positioning.

   This means that the future security problem will not simply involve
   more applications connected to a faster network.

   The network environment itself is expected to become more
   intelligent, more sensing-aware, more densely connected, more
   autonomous, and more capable of combining communications,
   computation, positioning, and environmental information.

   Without a corresponding consequence-control boundary, the combination
   of AI, precise location, integrated sensing, ubiquitous connectivity,
   autonomous agents, cloud and edge computation, and machine-speed
   communication risks undermining traditional assumptions on which both
   cybersecurity and privacy have relied.

   The result could be a collapse of the conventional distinction
   between harmless metadata and sensitive intelligence:

   data that is individually ordinary may become strategically sensitive
   after AI inference.

   It could also collapse the traditional distinction between software
   permission and real-world authority:

   an application may be authorized to read information while being
   unauthorized to disclose it;

   an AI may be authorized to compute while being unauthorized to act;

   a network function may be authenticated while being unauthorized to
   cause a particular network consequence.

   The security boundary must therefore move closer to the consequence
   itself.

   If required finality authority is absent, stale, replayed, revoked,
   consumed, act-mismatched, scope-mismatched, precision-mismatched,
   jurisdiction-mismatched, policy-mismatched, or sink-mismatched, the
   Candidate Act remains non-effective and the protected consequence
   fails closed.

   The central security principle is:

   COMPUTATION IS NOT AUTHORITY.
- **draft-wei-aic-jwt-00** (new-draft, score 28, verifiable_claims) [none]: [AI Agent Identity Certificate (AIC) JSON Web Token Profile](https://datatracker.ietf.org/doc/draft-wei-aic-jwt/) — This document defines the JSON Web Token (JWT) profile of the AI
   Agent Identity Certificate (AIC), a companion specification to draft-
   wei-aic-identity-cert-00.  The AIC X.509 extension binds an AI
   Agent's cryptographic identity to a responsible principal, carries a
   structured capability container, authorization boundary constraints,
   delegation mode, and principal-signed delegation evidence, and
   enables fully offline authorization decisions at the TLS layer.

   AIC-JWT encodes the same data model as an application-layer JWT so
   that the same authorization semantics can be enforced by HTTP APIs,
   web applications, and OAuth 2.0 ecosystems where transport-layer
   certificate presentation is not available.  The specification
   defines:

   *  a nested JWS structure that preserves the two-layer signature
      model of AIC -- a principal-signed DelegationAuthorization (DA)
      JWT embedded in and covered by an issuer-signed outer JWT;

   *  a namespaced aic claim carrying agent identity, principal binding,
      structured capabilities, delegation mode, and authorization
      constraints;

   *  principal binding by SPKI hash or JWK thumbprint, with optional
      credential bundle presentation in PKI deployments;

   *  issuance flows for both PKI-based CAs and OAuth 2.0 authorization
      servers, including RFC 7523 assertion exchange and RFC 8693 token
      exchange;

   *  validation rules, IANA registrations, and security considerations
      aligned with the OAuth 2.0 and JOSE specifications.
- **draft-sharif-agent-identity-framework-01** (new-draft, score 25, adjacent_watchlist) [none]: [Agent Identity Framework: Trust and Identity for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-sharif-agent-identity-framework/) — Autonomous artificial intelligence (AI) agents are increasingly
   performing actions that were previously the exclusive domain of
   authenticated human users: initiating financial transactions,
   querying regulated data, invoking external tools, and coordinating
   with other agents. Internet protocols designed for human-operated
   clients lack primitives to answer three fundamental questions about
   any autonomous action: which agent performed it, whether the agent
   was authorized to perform it, and whether the resulting evidence is
   independently verifiable.

   This document defines a framework for agent identity and trust
   enforcement on the Internet. It enumerates the gaps between current
   Internet standards and the requirements of autonomous agent systems,
   introduces a five-layer model (identity, authorization, attestation,
   evidence, trust) that separates concerns that are currently
   conflated, and outlines mechanisms to close specific gaps. The
   framework is intended to guide future Standards Track work and to
   provide a common vocabulary for researchers, implementers, and
   regulators.

   This document is informational. It does not define a wire protocol.
   It references existing Internet-Drafts and specifications that
   instantiate individual mechanisms within the framework.
- **draft-asor-wimse-agent-delegation-chain-00** (new-draft, score 22, authorization) [none]: [Verifiable Attenuated Delegation for AI Agent Chains](https://datatracker.ietf.org/doc/draft-asor-wimse-agent-delegation-chain/) — AI agents increasingly delegate tasks to other agents.  Each
   delegation should convey only a subset of the delegating party's
   authority, that subset should be bounded in scope, magnitude, and
   time, and any enforcement point should be able to verify -- offline,
   with no call to an authorization server -- that a token presented at
   hop N carries authority no greater than the token at hop N-1, back to
   a trusted root.  OAuth 2.0 Token Exchange (RFC 8693) models two-party
   delegation and records prior actors in a nested "act" claim, but that
   claim is informational only and cannot enforce attenuation across a
   chain of depth two or more.  This document defines the Agent
   Delegation Chain: a profile of OAuth 2.0 JWT access tokens (RFC 9068)
   that carries authority as Rich Authorization Requests (RFC 9396),
   links each delegation to its parent by a cryptographic byte-
   commitment, and specifies a deterministic offline verification
   algorithm that enforces monotonic attenuation, bounded depth, and
   monotonic expiry.  It reuses existing JOSE, proof-of-possession (RFC
   9449), and status-list machinery (the OAuth Status List draft) and
   introduces no new cryptography.
- **draft-daniel-ai-agent-internet-architecture-03** (new-draft, score 22, core_identity) [none]: [Architectural Requirements for Supporting AI Agents on the Internet](https://datatracker.ietf.org/doc/draft-daniel-ai-agent-internet-architecture/) — Autonomous AI agents are evolving from interactive assistants into
   networked software workloads that discover services, invoke tools,
   delegate authority, transact, communicate with other agents, and act
   asynchronously on behalf of humans and organizations.  Existing
   Internet protocols provide strong foundations, but agent autonomy,
   dynamic delegation, machine-speed execution, long and unpredictable
   model-processing intervals, and cross-domain interaction create
   requirements that span multiple protocol families.

   This document describes architectural requirements for supporting AI
   agents on the Internet across naming and discovery, HTTP,
   authentication, authorization and delegation, TLS and workload
   identity, transport and connection continuity, asynchronous
   messaging, capability and intent-based resolution, payments,
   provenance, auditability, revocation, security, and privacy.  It
   favors profiling and extending existing Internet protocols over
   defining a monolithic new agent protocol, and identifies the need for
   IETF-wide architectural coordination.
- **draft-ietf-wimse-wpt-02** (new-draft, score 22, core_identity) [wimse]: [WIMSE Workload Proof Token](https://datatracker.ietf.org/doc/draft-ietf-wimse-wpt/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from basic
   deployments to complex multi-service, multi-cloud, multi-tenant
   systems.  This document specifies the Workload Proof Token (WPT), a
   mechanism for workloads to prove possession of the private key
   associated with a Workload Identity Token (WIT).  The WPT is a signed
   JWT that binds the workload's authentication to a specific HTTP
   request, providing application-layer proof of possession for
   workload-to-workload communication.  This specification is designed
   to work alongside the WIT credential format defined in draft-ietf-
   wimse-workload-creds and can be combined with other WIMSE protocols
   in multi-hop call chains.
- **draft-reilly-sentinel-protocol-02** (new-draft, score 22, core_identity) [none]: [Reilly Sentinel Protocol (RSP): Blockchain-Anchored Integrity for AI Datasets, Training, Fine-Tuning, and Inference Provenance](https://datatracker.ietf.org/doc/draft-reilly-sentinel-protocol/) — The Reilly Sentinel Protocol (RSP) specifies an interoperable,
   multi-layer method for establishing integrity, provenance, and
   auditability across the artificial intelligence (AI) lifecycle.
   RSP defines a Sentinel Evidence Package (SEP) that binds payload
   digests, provenance metadata, signatures, blockchain timestamp
   proofs, and resolvable identifiers.  This enables tamper-evident,
   independently verifiable receipts for datasets, data
   transformations, training jobs, checkpoints, fine-tuning runs,
   evaluations, inference outputs, and agentic AI action logs.

   This revision (-02) supersedes draft-reilly-sentinel-protocol-01
   and corrects defects in it.  The cross-chain binding hash of -01
   was computed under SHA3-512 alone over an unframed concatenation
   of hex strings, which made a single algorithm the point of failure
   for a construction whose stated purpose was to survive the failure
   of any single algorithm, and which admitted field-boundary
   ambiguity.  It is replaced by an entangled link construction over
   a fixed-length framed input, with a concatenated braid that
   privileges no algorithm.  The post-quantum analysis of -01 applied
   Grover's algorithm to collision resistance, a property Grover does
   not meaningfully reduce, and stated SHA-256's collision resistance
   as 256 bits when it is 128 bits classically.  The claim that
   combining three hash functions requires an adversary to break all
   three is replaced, following [JOUX], by a hedging claim.  Merkle
   tree construction, left unspecified in -01 while relied upon by
   three separate extensions, is now normatively specified per
   [RFC6962].  Digest-only selective disclosure is replaced by salted
   commitments.  Automated repair of chain integrity violations is
   prohibited.

   RSP is transport-agnostic and serializable in JSON and CBOR.  It
   leverages existing IETF building blocks including COSE signatures,
   CBOR, CDDL, JSON, and NTS-secured time.  Anchoring is done via
   append-only blockchain receipts and identity is stabilized with
   persistent identifiers.
- **draft-sharif-ai-model-lifecycle-attestation-01** (new-draft, score 21, trust_infrastructure) [none]: [Cryptographic Attestation for AI Model Lifecycle: From Training Data to Inference Output](https://datatracker.ietf.org/doc/draft-sharif-ai-model-lifecycle-attestation/) — This document defines a cryptographic attestation framework for
   the complete lifecycle of artificial intelligence models, from
   training data provenance through model weight signing,
   quantization verification, deployment attestation, and per-
   inference output signing.  The framework creates an unbroken
   chain of cryptographic evidence binding each inference output to
   the specific model version, training data, and deployment
   configuration that produced it.

   The framework uses ECDSA P-256 digital signatures, SHA-256
   hash functions, Merkle trees for corpus attestation, and JSON
   Web Key Sets (JWKS) for key discovery.  It addresses documented
   threats including model distillation attacks, quantization
   poisoning, training data manipulation, silent model degradation,
   and inference output tampering.

   This specification complements the Agent Trust Transport Protocol
   (ATTP) [draft-sharif-attp-agent-trust-transport], MCPS message
   signing [draft-sharif-mcps-secure-mcp], and the Agent Audit
   Trail format [draft-sharif-agent-audit-trail] to provide end-to-
   end cryptographic verification from data ingestion to consumer
   delivery.
- **draft-tonyai-a2a-trust-02** (new-draft, score 21, adjacent_watchlist) [none]: [Agent-to-Agent Trust, Identity, and Verifiable Provenance](https://datatracker.ietf.org/doc/draft-tonyai-a2a-trust/) — This document defines a trust model for agent-to-agent (A2A)
   interactions in multi-agent AI systems.  It specifies how agents
   obtain verifiable identities via CA-signed templates, how spawn
   chains are cryptographically established and validated, how dynamic
   policies are governed under a dual-signature model, and how cross-
   organizational agent interactions are explicitly authorized.  The
   model applies existing PKI primitives (X.509, CRL, CSR) and
   established identity patterns (OAuth 2.0, On-Behalf-Of) to the
   problem of agent provenance.  This document does not address agent-
   to-resource access control, human-in-the-loop orchestration, or agent
   behavior, as those concerns belong to the resource enforcement layer
   and the orchestration layer respectively.
- **draft-das-6g-query-scoped-communication-handles-02** (new-draft, score 19, core_identity) [none]: [6G-Era Privacy-Preserving, Anti-Harassment and Spam-Resistant Communication for Map-Based Business Discovery and AI-Native Telecommunication Using Query-Scoped Communication Handles](https://datatracker.ietf.org/doc/draft-das-6g-query-scoped-communication-handles/) — Modern telecommunications usually couple knowledge of a routable
   identifier with the practical ability to attempt contact.  A
   telephone number, SIP URI, messaging handle, relay address,
   marketplace contact reference, or similar identifier can therefore
   remain a reusable reachability path after the original purpose for
   disclosure has ended.

   Existing controls solve important but different problems.  Virtual or
   masked numbers hide an underlying endpoint but commonly leave a
   substitute route active while the alias is valid.  STIR and SHAKEN
   authenticate or attest information associated with the calling
   identity, but do not by themselves establish that the authenticated
   caller is presently authorized by the recipient to create this
   particular communication effect.  Combining number masking with STIR/
   SHAKEN improves privacy and origin authenticity, yet still does not
   inherently convert reachability into purpose-scoped, revocable,
   consumable communication authority.  OAuth can express delegated and
   even fine-grained API authorization, including sender-constrained
   tokens, but it does not define telecommunications-specific semantics
   in which a visible contact handle alone creates no effective path
   until recipient-side or policy-bound communication authority is
   established.

   This document describes a Capability-Validated Inbound Descriptor
   (CVID) and related query-scoped communication model.  A communication
   request is represented as a Candidate Act and remains non-effective
   until current authorization is established for the requested
   communication effect.  Authorization may be bound to sender or
   business identity, recipient scope, purpose, channel, time, quota,
   freshness, revocation and policy epochs, jurisdiction, device or
   agent identity, and other deployment-specific constraints.

   Two deployment profiles are distinguished.  In a blocked-path
   profile, ordinary routing may proceed to an enforcement point that
   rejects a request lacking valid communication authority.  In a
   stronger absent-path profile, possession of the visible handle alone
   does not resolve to or activate the effective communication path;
   protected authority must be established before routing, gateway
   resolution, media allocation, notification, or another consequence-
   bearing resource is released.

   The model is relevant to IMT-2030/6G because increasingly
   programmable, AI-assisted, machine-to-machine, and autonomous
   communications can generate requests at machine speed and scale.
   Early rejection or non-creation of unauthorized communication paths
   may reduce unnecessary signaling, gateway processing, fraud-analysis
   load, notification work, media/resource allocation, and associated
   energy consumption.  These are potential efficiency benefits, not
   universal guarantees: authorization itself consumes resources, and
   net bandwidth or energy savings require measurement in the target
   deployment.

   The document focuses on the remaining problem space, comparison with
   existing mechanisms, 6G and sustainability relevance, blocked-path
   and absent-path operation, deployment feasibility, legacy
   interworking, latency considerations, security and privacy, and
   frequently asked questions likely to arise in telecom engineering
   review.
- **draft-jovancevic-vicdm-10** (new-draft, score 19, core_identity) [none]: [Verifiable Identity Claims and Delegation Model (VICDM)](https://datatracker.ietf.org/doc/draft-jovancevic-vicdm/) — This document defines a conceptual framework for handling identity
   assertions in application-layer protocols. It introduces a model
   in which identity on the Internet is optional, but any asserted
   identity MUST be verifiable.

   It further defines a delegation mechanism that allows entities to
   authorize third-party infrastructure to act on their behalf in a
   verifiable and transparent manner.

   The goal is to reduce identity misrepresentation while fully
   preserving the ability for anonymous and pseudonymous interaction.
   This document does not define a protocol; it defines the principles
   that protocol specifications SHOULD follow when addressing agent
   identity.

   A concrete protocol implementation of these principles is defined
   in [SAIP].
- **draft-sharif-attp-agent-trust-transport-01** (new-draft, score 19, adjacent_watchlist) [none]: [ATTP: Agent Trust Transport Protocol for Secure Agent-to-Server Communication](https://datatracker.ietf.org/doc/draft-sharif-attp-agent-trust-transport/) — This document specifies ATTP (Agent Trust Transport Protocol),
   a synchronous request-response protocol for communication
   between autonomous AI agents and web API servers.  ATTP
   operates as an application-layer protocol over HTTP, adding
   mandatory cryptographic identity verification, per-message
   signing, trust-gated access control, and tamper-evident audit
   trail generation to every agent-server interaction.

   ATTP defines five protocol-layer headers for requests
   (X-Agent-Trust, X-Agent-Signature, X-Agent-Nonce,
   X-Agent-Timestamp, X-ATTP-Version) and three for responses
   (X-Server-Signature, X-Server-Nonce, X-Server-Timestamp)
   that carry an Agent Passport (JWT-based identity credential),
   ECDSA P-256 digital signatures, cryptographic nonces, and
   timestamps.  Server middleware verifies all cryptographic
   properties before application code executes.

   ATTP has no insecure mode.  Every request MUST carry a valid
   Agent Passport.  Every request body MUST be signed.  Every
   response body MUST be signed.  Every interaction MUST be
   recorded in a hash-chained audit trail.  The protocol defines
   a URL scheme (attp://) and is fully backward-compatible with
   existing HTTP infrastructure.

   ATTP is the synchronous counterpart to the Agent Transport
   Protocol (ATP).  ATP handles asynchronous store-and-forward
   agent delivery; ATTP handles real-time request-response API
   communication.  Both share the same identity model, trust
   framework, and cryptographic primitives.
- **draft-das-agentic-execution-finality-01** (new-draft, score 18, authorization) [none]: [Tool Selection Is Not Execution: Finality for Agentic Tool Dispatch](https://datatracker.ietf.org/doc/draft-das-agentic-execution-finality/) — An agentic model can emit a tool call that today's runtimes treat as
   something to execute.  Allowlists, OAuth tokens, MCP server auth,
   sandboxes, output filters, and human approval decide whether an agent
   may reach a tool.  They do not decide whether this generated call,
   with this argument digest, from this instruction chain, at this
   delegation depth, may take effect now.

   That gap is the incident surface.  Prompt-injected content, poisoned
   retrieval, a malicious tool response, or a delegated sub-agent can
   produce a call that looks like ordinary tool use.  If the dispatcher
   executes whatever the model selected, policy that lived upstream
   becomes advisory.

   This document specifies a dispatch-time gate.  The model may compute
   a call.  The call remains a Candidate Act. A Protected Enforcement
   Domain binds agent, tool, arguments, purpose, destination,
   provenance, and policy epochs, then issues scoped non-bearer
   authority.  A Tool-Dispatch Finality Sink verifies that authority
   against the actual invocation immediately before the tool runs, then
   consumes it.  The same gate applies to support, coding, payments,
   clinical, SOC, browser-use, and multi-agent MCP deployments.  Tool
   selection is not execution authority.
- **draft-dogru-cedulon-03** (new-draft, score 18, verifiable_claims) [none]: [Cedulon: An Audit Layer for Agent-to-Agent Commerce](https://datatracker.ietf.org/doc/draft-dogru-cedulon/) — This document defines the Cedulon Protocol, an audit layer for agent-
   to-agent commerce.  Payment rails such as HTTP 402 flows (x402) and
   mandate protocols (AP2) already move value.  They do not, by
   themselves, produce a fail-closed policy check and a signed spend
   receipt that a verifier can reconcile against a rail extract.
   Cedulon specifies a Trade Manifest (signed offer before payment), a
   Policy Decision Point with default deny, a Spend Receipt (COSE/CWT
   claim set after a gated payment), epoch checkpoints, and rail-extract
   reconciliation.  The reconciliation shows that no settlement on the
   extract lacks a receipt and no settled receipt is absent from the
   extract.  That result is unconditional only when the verifier pins
   the rail key out of band and states the period under audit; otherwise
   the document requires it to be reported as conditional.  Checkpoints
   carry the suppression guarantee, so the document profiles the
   checkpoint as a Signed Statement, gives the verification algorithm a
   step that consumes the transparency receipts returned for
   checkpoints, names what a witness holding a checkpoint the presented
   chain omits reports, brings equivocation within reach by comparing
   recorded copies against the presented chain, and states how
   checkpoint totals may be withheld without withholding the fact that
   they were.  This revision states the trust roots the earlier ones
   left implicit: no signed object may be verified against a key it
   carries itself, and a presented Trade Manifest must be bound both to
   the receipts that name it and to the terms those receipts claim.  It
   also names a threat no adversary causes, a settlement recorded on a
   rail with no receipt behind it.  It also defines a Dispute Evidence
   Bundle (evidence, not an award) and optional SCITT anchoring.
   Cedulon is not a competitor to x402 or AP2; it sits above them.
- **draft-zagarella-verified-human-root-01** (new-draft, score 18, core_identity) [none]: [Verified Human Root Attestation for Agent Delegation Chains and Audit Records](https://datatracker.ietf.org/doc/draft-zagarella-verified-human-root/) — Autonomous software agents increasingly act under delegated
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
- **draft-jovancevic-saip-10** (new-draft, score 17, core_identity) [none]: [SAIP: Signed Agent Identity Protocol](https://datatracker.ietf.org/doc/draft-jovancevic-saip/) — The modern internet lacks a reliable mechanism for verifying the
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
   header-based protocols. It introduces DNS-based Attestation Discovery as
   a lightweight alternative to registry-based key lookup, making
   deployment accessible to organizations of any size.
- **draft-mih-scitt-agent-action-capsule-04** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
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
- **draft-sharif-agent-payment-trust-01** (new-draft, score 17, agent_identity) [none]: [Trust Scoring and Identity Verification for Autonomous AI Agent Payment Transactions](https://datatracker.ietf.org/doc/draft-sharif-agent-payment-trust/) — This document specifies a protocol for trust scoring, identity
   verification, and spend limit enforcement for autonomous AI agents
   that initiate financial transactions.  As AI agents gain the
   capability to make payments via protocols such as the Machine
   Payments Protocol (MPP), a standardised mechanism is needed to
   verify agent identity, assess trustworthiness, and enforce
   financial limits based on behavioural history.

   The protocol defines a five-dimension trust scoring model, per-
   agent cryptographic identity using ECDSA P-256 key pairs,
   challenge-response identity verification, spend limit tiers
   derived from trust scores, anomaly detection for financial
   behaviour, and a public trust query API for third-party platforms.

   This specification complements draft-sharif-mcps-secure-mcp, which
   provides message-level cryptographic security for the Model Context
   Protocol (MCP).  Together, the two specifications address protocol
   security (MCPS) and financial trust (this document) for the AI
   agent economy.
- **draft-das-protocols-enterprise-ai-00** (new-draft, score 16, core_identity) [none]: [Architecting Resilience for Enterprise AI: Preventing Data Reconstruction, Exfiltration, and Unauthorized Consequence in Compromised AI Environments (DAS Protocols)](https://datatracker.ietf.org/doc/draft-das-protocols-enterprise-ai/) — A compromised enterprise AI server is no longer just a data-breach
   risk.  It can become a continuously updated reconstruction engine of
   the enterprise’s future — correlating customer records, engineering
   defects, financial systems, and internal communications into
   competitive intelligence and then externalizing that intelligence.
   Conventional security concentrates the powers of data access,
   semantic joining, and external effectuation inside the same workload.
   When that workload is compromised through prompt injection, model
   substitution, credential theft, or full server takeover, existing
   access-control, sandbox, TEE, DLP, and clean-room approaches do not
   structurally stop the escalation from computation to real-world
   consequence.

   This document presents the DAS Protocols enterprise-AI architecture,
   a focused embodiment of the broader execution-finality framework
   disclosed in PCT/IB2026/055615 (“THE DAS PROTOCOLS”).  It introduces
   Execution–Consequence Decoupling enforced by three pillars:
   Decomposition of Authority (Technical Non-Joinability) across
   independently controlled identity, content, relationship-mapping, and
   cryptographic vaults; Mandatory Mediation of every consequence-
   bearing Candidate Output; and Technical Non-Completability so that
   computation can finish without the ability to complete external
   consequence.

   Reconstruction is governed by a non-bearer Reconstruction
   Authorization Object bound to attested execution context, session,
   purpose, and Permitted Association Scope.  Candidate Outputs are
   sealed.  Live output-time re-verification and constitutive Protected
   Output Validation Receipt commitment are required before an output-
   specific Release Capability can be issued and exercised only at a
   designated Output Release Boundary.  Compromise of the AI computation
   plane therefore cannot automatically escalate into unrestricted
   enterprise-knowledge reconstruction or unauthorized external
   consequence.

   The document elaborates the full problem space, compares the
   architecture against representative conventional technologies,
   provides a detailed technical description, and supplies JSON Schema
   definitions for the core protected objects (Reconstruction
   Authorization Object, Protected Output Validation Receipt, and Output
   Release Capability).  Intellectual-property disclosures of related
   Indian provisional applications and PCT filings appear in the final
   appendix.
- **draft-dogru-cedulon-reattestation-00** (new-draft, score 16, trust_infrastructure) [none]: [Cedulon Re-Attestation: Carrying Spend Evidence Across Algorithm Retirement](https://datatracker.ietf.org/doc/draft-dogru-cedulon-reattestation/) — Audit evidence is only useful for as long as it can be verified.
   Cedulon produces COSE spend receipts and epoch checkpoints whose
   signature algorithms will eventually be deprecated or broken; the
   recent transition from polymorphic EdDSA to fully-specified Ed25519
   algorithm identifiers shows that even identifiers change within a
   decade.  This document proposes a re-attestation profile for Cedulon
   evidence: a signed statement, produced while the original algorithm
   is still trustworthy, that binds the original evidence bytes to a
   successor algorithm and is registered in a SCITT transparency
   service.  Chains of such statements allow a verifier decades later to
   trust evidence whose original cipher has been retired.  Structures
   are meant to outlive ciphers.  This is an extension proposal to the
   Cedulon core document; its normative language is provisional and the
   companion implementation does not implement it yet.
- **draft-le-scitt-derived-subjects-00** (new-draft, score 16, trust_infrastructure) [none]: [SCITT Profile for Independently Derived Subjects](https://datatracker.ietf.org/doc/draft-le-scitt-derived-subjects/) — The Supply Chain Integrity, Transparency, and Trust (SCITT)
   architecture permits distinct Issuers to agree on the same CBOR Web
   Token (CWT) Subject Claim (sub) value for a common Subject.  This
   document specifies one profile by which those Issuers can
   independently compute that common value from the same application-
   defined Subject semantics without relying on a shared assigning
   authority.

   A surrounding application maps its Subject description to an admitted
   structured Value.  This profile defines an exact deterministic
   binding encoding, SHA-256 derivation, a text representation, and
   verification requirements for deriving sub from that Value.  Optional
   JSON and Concise Binary Object Representation (CBOR) forms are
   provided for exchanging an admitted Value; they are not SCITT
   Statement payload formats.  The SCITT Statement payload, signature,
   Registration, Receipt, Transparency Service state, and Issuer
   identity are not implicit inputs to Subject derivation.
- **draft-li-oauth-policy-based-anonymous-tokens-00** (new-draft, score 16, authorization) [none]: [OAuth 2.0 Policy-Based Anonymous Access Tokens](https://datatracker.ietf.org/doc/draft-li-oauth-policy-based-anonymous-tokens/) — This document specifies an OAuth 2.0 access-token type that allows a
   client, after one authorization-server issuance, to derive a policy-
   bounded set of unlinkable, single-use access tokens locally.  Each
   derived token is bound to one canonical tag, an intended resource
   server, approved authorization details, a policy epoch, and a
   validity interval.  Resource servers validate the token offline and
   enforce both policy membership and replay prevention.

   The protocol defines authorization request semantics, token-endpoint
   issuance, canonical policy and metadata objects, token derivation and
   HTTP presentation, resource-server validation, capability discovery,
   error handling, and IANA registrations.  Version 1 requires public
   verification and the counter-window policy profile.  It supports an
   optional private metadata bit, while private-verification
   ciphersuites remain optional.

   Concrete cryptographic algorithms are supplied by separately
   registered PBAT ciphersuites.  The initial mandatory-to-implement
   ciphersuite is the publicly-verifiable equivalence-class-signature
   construction over BLS12-381 specified by the companion PBAT
   ciphersuite document.  This specification does not replace OAuth
   grants, resource-owner consent, client authentication, or audience
   restriction.

   — middle
- **draft-morrison-solo-agent-earn-registration-01** (new-draft, score 16, core_identity) [none]: [Registration of Owner-Less Agents as Economic Principals: A Payment-Gated Admission Profile for Transparency Services](https://datatracker.ietf.org/doc/draft-morrison-solo-agent-earn-registration/) — This memo describes a profile by which an autonomous agent that has
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
- **draft-sharif-agent-transport-protocol-01** (new-draft, score 16, adjacent_watchlist) [none]: [Agent Transport Protocol: Asynchronous Store-and-Forward Messaging for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-sharif-agent-transport-protocol/) — This document specifies the Agent Transport Protocol (ATP), an
   asynchronous store-and-forward messaging protocol for autonomous
   AI agents.  ATP enables agents to transmit themselves -- including
   state, context, capabilities, and cryptographic identity -- between
   agent runtimes across network boundaries.  The protocol draws on
   the operational model of the Simple Mail Transfer Protocol (SMTP)
   [RFC5321] but is purpose-built for agent-to-agent communication
   where the agent itself is the payload.

   ATP provides: (1) asynchronous delivery with store-and-forward
   semantics, (2) cryptographic identity verification at each relay
   hop, (3) trust scoring and policy enforcement at ingress, (4)
   capability negotiation between sending and receiving runtimes,
   and (5) tamper-evident envelopes with end-to-end integrity
   protection.

   The protocol is transport-agnostic and operates over TCP, TLS,
   QUIC, or any reliable ordered stream.  ATP is designed to
   interoperate with existing agent frameworks including Google A2A,
   the Model Context Protocol (MCP), and FIPA ACL, while addressing
   the fundamental limitation of synchronous RPC-based agent
   communication: the requirement that both endpoints be
   simultaneously available.
- **draft-sharif-agent-trust-enforcement-00** (new-draft, score 16, agent_identity) [none]: [Agent Trust Enforcement for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-trust-enforcement/) — This document specifies a trust enforcement architecture for
   autonomous AI agents operating within container orchestration
   environments such as Kubernetes.  It defines a sidecar injection
   pattern using mutating admission webhooks, graduated trust
   enforcement (L0-L4) on every outbound call from an agent
   workload, credential isolation via secret management systems,
   bilateral revocation propagation across clusters, and tamper-
   evident evidence generation.

   The architecture operates alongside existing workload identity
   frameworks including SPIFFE/SPIRE without replacement, extends
   X.509v3 certificates with agent-specific extensions under a
   registered IANA Private Enterprise Number (PEN 66339), and
   provides compliance evidence for EU AI Act Article 12,
   FDA 21 CFR Part 11, IEC 62443, and NERC CIP.

   Three enforcement gates -- LLM gate, Database gate, and API
   gate -- intercept every outbound call from an agent container.
   Each gate classifies the call against the agent's trust level,
   records the decision in a hash-chained evidence ledger with
   ECDSA P-256 signatures, and either permits or refuses the call.
   The architecture defaults to deny: if no policy matches, the
   call is refused.
- **draft-das-enterprise-ai-output-finality-00** (new-draft, score 15, core_identity) [none]: [A Compromised AI Server Must Not Become a Map of the Enterprise: Non-Joinable Vaults and Output-Release Finality](https://datatracker.ietf.org/doc/draft-das-enterprise-ai-output-finality/) — Past cyber theft stole files.  Present theft steals live sessions and
   SaaS tokens.  The next theft does not need a dump.  A frontier
   enterprise assistant that can see mail, tickets, code, finance, and
   memory can join those fragments into a meaning that was never stored
   as one record, then act.  That is enterprise-future mapping:
   reconstruction of strategy, relationships, and probable next moves,
   followed by send, write, or tool invoke [DAS-ISOLATION].

   IAM, DLP, clean rooms, TEEs, and output filters still answer who may
   touch a store.  They do not answer whether separately lawful
   fragments may be joined into a new protected meaning, or whether that
   meaning may leave through Claude, ChatGPT Enterprise, a computer-use
   agent, or an MCP tool.

   This profile keeps identity, content, and association under
   independently controlled vaults, joins them only under a session-
   bound Reconstruction Authorization Object, seals the Candidate
   Output, commits a receipt before release authority exists, and
   completes send, render, store, or invoke only at an Output Release
   Boundary.  Compromise of the model host is not reconstruction.
   Reconstruction is not release.
- **draft-kushwaha-scim-didvc-binding-01** (new-draft, score 15, core_identity) [none]: [SCIM DID/VC Binding Extension](https://datatracker.ietf.org/doc/draft-kushwaha-scim-didvc-binding/) — This document defines an extension to the System for Cross-domain
   Identity Management (SCIM) for binding SCIM User resources to
   decentralized identity artifacts, including Decentralized Identifiers
   (DIDs) and Verifiable Credentials (VCs).  The extension introduces a
   read-only SCIM schema extension for User resources that exposes
   binding state for discovery, a new SCIM resource type named
   IdentityBinding that records auditable linkage between a SCIM user
   and one or more DIDs and credential references, and an optional SCIM
   schema extension for ServiceProviderConfig that advertises server
   capabilities for DID and VC binding.

   This specification intentionally does not define DID resolution,
   credential issuance, credential transport, or authentication flows.
   Instead, it defines how a SCIM service provider represents,
   discovers, queries, and manages binding state derived from those
   systems.

   This specification defines binding lifecycle semantics including
   classification of SCIM attribute changes as material to credential
   claims, partial revocation when only a subset of credential claims is
   affected by a SCIM change, three supported lifecycle interleavings
   between SCIM resources and externally issued credentials, and
   propagation of binding state changes via SCIM Events [RFC9967].
- **draft-mcguinness-oauth-id-continuation-assertion-01** (new-draft, score 15, authorization) [none]: [Identity Continuation Assertion for OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-id-continuation-assertion/) — This document defines the Identity Continuation Assertion, a short-
   lived, sender-constrained JWT used as an OAuth 2.0 Token Exchange
   subject token.  It lets an IdP Authorization Server (IdP) issue an
   onward Identity Assertion JWT Authorization Grant (ID-JAG) when a
   user's request crosses service boundaries after the user is no longer
   present.  The profile targets deployments in which several Resource
   Authorization Servers trust one IdP and use audience-local subject
   identifiers that only the IdP can resolve.  It complements offline
   attenuation for intra-domain fan-out that does not change the
   subject.
- **draft-nikolaichuk-rats-tap-00** (new-draft, score 15, trust_infrastructure) [none]: [Trusted Artifact Provenance (TAP): A Producer, Verifier, and Sealer Contract for Attestation-Gated Reconstruction of Stateful Assets](https://datatracker.ietf.org/doc/draft-nikolaichuk-rats-tap/) — The Remote ATtestation procedureS (RATS) architecture (RFC 9334)
   defines how Evidence is conveyed from an Attester to a Verifier and
   how the resulting Attestation Results are conveyed to a Relying
   Party.  It deliberately stops at the point where a Relying Party has
   appraised Attestation Results.  This document specifies Trusted
   Artifact Provenance (TAP), a consumer of Attestation Results that
   defines what happens next in one specific and recurring case:
   releasing sealed key material to a process that reconstructs a
   stateful asset inside an attested environment, and recording the
   release decision as an auditable object.

   TAP defines three contracts.  The Producer contract governs how an
   artifact is sealed and bound to the attested identity of the
   environment that produced it.  The Sealer contract governs the
   attestation-gated release of key material to a reconstruction
   environment.  The TAP Verifier contract governs after-the-fact
   appraisal of provenance and release records.  TAP does not define an
   appraisal policy language, does not define a new Evidence format, and
   does not replace any part of RFC 9334.
- **draft-das-payment-execution-finality-00** (new-draft, score 14, authorization) [none]: [A Signed Instruction Is Not Settlement: Finality for Agentic and API Payments](https://datatracker.ietf.org/doc/draft-das-payment-execution-finality/) — Payment rails already know how to move money.  They do not know
   whether this generated instruction — this amount, this beneficiary,
   this rail, this purpose, from this agent or API worker — is the
   instruction that was authorized to move.  A signed ISO 20022 message,
   an OAuth token on a PSP, a stored mandate, or a pass through 3-D
   Secure can all be valid while the act is wrong.  The signature
   authenticates a channel.  It does not bind a Candidate Act at the
   settlement sink.

   That gap is now an agent gap.  A model that can call payout.create, a
   RPA job that submits ACH, or a checkout agent that captures a card
   will treat tool selection as settlement authority.  Fraud used to
   steal credentials and replay files.  It now steals a seat or injects
   a document and asks the authorized worker to pay a new beneficiary at
   the old amount, or the old beneficiary at a new amount.

   This document specifies a payment-side execution-finality profile.
   An instruction remains a Payment Candidate Act.  A Protected
   Enforcement Domain binds principal, wallet or account, amount,
   currency, beneficiary, rail, purpose, policy epoch, and intended
   settlement sink, then commits evidence before scoped non-bearer
   authority is issued.  The sink that would actually post, capture, or
   release funds verifies that authority against the live instruction
   and consumes it.  A signed instruction is not settlement.
- **draft-das-protocols-candidate-act-finality-00** (new-draft, score 14, core_identity) [none]: [Stopping AI Hallucinations and Unsafe Acts from Becoming Real-World Consequences (DAS Protocols)](https://datatracker.ietf.org/doc/draft-das-protocols-candidate-act-finality/) — The internet has protocols for moving data, securing channels, naming
   hosts, and delegating identity.  It has no protocol for the moment a
   machine-generated instruction becomes a real-world act.  As AI
   systems begin to move money, change databases, reconfigure networks,
   send communications, and control physical systems, that missing
   boundary becomes a structural risk.

   Today an AI can hallucinate a fact, cite a stale source, invent a
   tool argument, or propose an unsafe agentic step — and still reach an
   effectuation interface.  Model approval is not output approval.
   Workflow approval is not consequence approval.  Moderation, access
   control, TEEs, simulation, and post-hoc audit all leave the final
   transition from computation to consequence under-protected.

   This document specifies the DAS Protocols Candidate-Act Finality
   architecture.  Every effect-capable AI output is first converted into
   a non-effective Candidate Act. The Candidate Act stays non-effective
   until a Protected Enforcement Domain has validated output,
   provenance, factual support, consequence, jurisdiction, epoch, and
   sink predicates.  Only then is a scoped non-bearer capability or
   Execution Handle released and verified at a Finality Sink.  In
   advanced forms the Finality Sink is cryptographically unable to
   complete the act unless the handle supplies the missing execution
   material.

   The architecture supports graduated and escalated conditional
   finality so that elevated-risk but necessary acts can still proceed
   under stricter controls.  The document elaborates the problem space,
   compares the approach with representative existing techniques,
   describes the base and advanced finality paths, and provides JSON
   Schema definitions for the core protected objects.  Related Indian
   provisional applications and PCT filings are listed in the final
   appendix.
- **draft-agentic-ai-usecases-requirements-02** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on multimodal communication, session
   management, discovery, communication security, agent identity and
   authentication.
- **draft-das-agentic-tool-binding-01** (new-draft, score 13, authorization) [none]: [tool_use Is Not invoke(): Binding Execution-Finality to Claude, ChatGPT, and MCP](https://datatracker.ietf.org/doc/draft-das-agentic-tool-binding/) — Frontier runtimes already standardized the dangerous moment.  Claude
   emits a tool_use block.  ChatGPT emits tool_calls.  MCP emits tools/
   call.  The host then invokes whatever name and arguments the model
   printed.  Alignment, allowlists, and OAuth sit around that moment.
   They do not sit on it.  If the block is treated as a capability,
   prompt-injected mail, a poisoned retrieval, or a stolen enterprise
   seat becomes an external act with a 200 from the tool.

   This document does not invent another assistant API.  It binds the
   Agent Candidate Act profile [I-D.das-agentic] onto the three
   interfaces those labs and their customers already ship: Anthropic
   tool_use / computer_use, OpenAI function calling and Responses tools,
   and Model Context Protocol tools/call.  The model may emit the block.
   The block remains non-effective.  A local enforcer builds the act,
   binds the argument digest, and refuses invoke() until scoped
   authority is verified and consumed at the dispatch sink.

   The implementation target is a middleware function that a host loop
   can call without changing the model vendor. tool_use is not invoke().
- **draft-kavian-aep-oauth-session-credential-03** (new-draft, score 13, core_identity) [none]: [OAuth Bearer Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-oauth-session-credential/) — This document defines the OAuth Bearer session-credential grant type
   for the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an OAuth-style Bearer access token through the AEP
   Grant command while preserving baseline AEP client assertion
   authentication as the root of trust.
- **draft-mih-sokolov-scitt-payload-binding-02** (new-draft, score 13, trust_infrastructure) [none]: [Canonical Payload Binding: A Signed Statement Construction Profile](https://datatracker.ietf.org/doc/draft-mih-sokolov-scitt-payload-binding/) — Independently written systems that anchor records to a SCITT
   Transparency Service repeatedly re-derive the same construction: a
   canonical form of structured content, a content-addressed identifier
   derived from that form, a receipt placed in the unprotected header of
   the Signed Statement, and a typed reference mechanism that lets one
   record cite another by digest across profile boundaries.  This
   document defines that construction as a reusable profile — the
   Canonical Payload Binding — so that each payload class declares its
   canonicalization algorithm and exclusion set once, obtains an
   interoperable derived identifier, and inherits statement-to-receipt
   binding and typed digest reference semantics without restating the
   mechanics in every profile.  It complements the COSE Hash Envelope
   mechanism defined in RFC 9995: where that mechanism signals that a
   Signed Statement's payload is a digest standing in for content held
   elsewhere, this document defines how that digest is computed from
   structured content so that independently written implementations
   converge on the same bytes.  An IANA registry governs the
   canonicalization algorithms; entries are immutable.  This document
   defines no payload content formats and registers no artifact types;
   the artifact types that a typed reference may cite, and their
   meaning, are registered in a single shared Artifact Type Registry,
   governed separately from this document, that payload profiles
   register into.
- **draft-morrison-consent-settlement-05** (new-draft, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
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
   agnostic.  The memo is Informational; the underlying COSE and CBOR
   formats are normative per [RFC9052] and [RFC8949], and the HTTP
   semantics are normative per [RFC9110].
- **draft-morrison-reviewed-by-trailer-02** (new-draft, score 13, adjacent_watchlist) [none]: [Reviewed-By Trailer: Sovereign-Portable Peer-Review Attribution for Content-Hash-Bound Artefacts](https://datatracker.ietf.org/doc/draft-morrison-reviewed-by-trailer/) — This document defines a trailer grammar for sovereign-portable peer
   review as an extension of the identity-attributed commit grammar in
   [COMMITS].  The grammar introduces one required trailer (Reviewed-
   By:) and three optional companion trailers (Review-Stance:, Review-
   Of:, Witnessed-By:) that bind a Sovereign-tier ~handle to a specific
   act of review over a specific content artefact, cryptographically
   signed using the Ed25519 mechanism of [COMMITS].  The mechanism
   applies uniformly to git commits, document manifests, pre-prints,
   patent disclosures, and any other content-addressable artefact.
   Reviewer reputation accumulates on the sovereign handle rather than
   on a publisher's platform, making reviewer trust portable across
   journals, pre-print servers, and private review contexts.
   Pseudonymous review for anonymous peer-review processes is supported
   by permitting a Sovereign handle whose underlying party is concealed
   through out-of-band key custody, preserving full cryptographic
   verifiability of the review act without disclosing the reviewer's
   underlying identity.  The grammar is positioned as complementary to
   CRediT [CREDIT], ORCID [ORCID], and DOI [DOI] attribution
   infrastructure, not as a replacement for them.
- **draft-sharif-openid-agent-identity-01** (new-draft, score 13, core_identity) [none]: [OpenID Connect Agent Identity Claims for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-sharif-openid-agent-identity/) — This specification defines a profile of OpenID Connect Core 1.0
   that enables Identity Providers (IdPs) to issue identity tokens
   for autonomous software agents.  It introduces a set of standard
   claims for representing agent identity, ownership, trust posture,
   authorised capabilities, and compliance screening status within
   OpenID Connect ID Tokens.

   The profile is designed to operate within existing OpenID Connect
   infrastructure without requiring modifications to the core
   protocol.  It defines how Relying Parties (RPs) validate agent
   tokens and enforce graduated access controls based on agent trust
   levels and sanctions screening results.
- **draft-borthwick-msebenzi-environment-state-02** (new-draft, score 12, authorization) [none]: [Verifiable Intent -- environment.* Constraint Family](https://datatracker.ietf.org/doc/draft-borthwick-msebenzi-environment-state/) — Agent-authorization mandate formats authorise autonomous agents to
   act on behalf of human principals through cryptographically signed
   constraint instances bound into delegated mandates.  Their existing
   constraint families describe properties of the transaction itself —
   what is being purchased, by whom, for how much, against which
   credential.  They do not describe properties of the environment in
   which the transaction is executed: whether the venue is open, whether
   the source of funds is funded, whether other relevant external
   conditions hold at the moment of execution.

   This document specifies the environment.* constraint family for
   agent-authorization mandate vocabularies.  It is defined against a
   host-binding profile (Section 1.3.1) that the Verifiable Intent (VI)
   mandate format satisfies and that other mandate formats may satisfy;
   VI is used throughout as the reference host.  It defines the
   membership criterion under which a constraint type qualifies as a
   member of the family, the family-wide vocabulary every member uses,
   the composition discipline by which family members compose with each
   other and with constraints from other families, the register
   discipline under which family-wide and per-type prose is written, the
   family-wide security considerations, and the IANA registry mechanics
   under which new family members are registered.  It does not define
   any individual constraint type.  Two reference type specifications
   (environment.market_state and environment.wallet_state) are
   referenced informatively in Appendix A.
- **draft-dijkhuis-hdk-00** (new-draft, score 12, verifiable_claims) [none]: [Hierarchical Deterministic Keys](https://datatracker.ietf.org/doc/draft-dijkhuis-hdk/) — Using a distinct holder-binding key for each Credential improves
   unlinkability, but generating and storing many keys in a Wallet
   secure area can be expensive or impossible.  This document defines a
   way to derive unlinkable P-256 Credential keys from one protected
   parent key while retaining the parent's key-protection properties.
   It specifies this mechanism as an extension to OpenID for Verifiable
   Credential Issuance (OpenID4VCI), allowing the Issuer to derive each
   child public key while only the Wallet can use the corresponding
   child private key.
- **draft-dikshit-nmop-bmp-telemetry-message-01** (new-draft, score 12, core_identity) [none]: [A YANG Augmentation for Carrying BMP Telemetry in the Network Telemetry Message Envelope](https://datatracker.ietf.org/doc/draft-dikshit-nmop-bmp-telemetry-message/) — [I-D.ietf-nmop-message-broker-telemetry-message] defines an
   extensible YANG envelope, "ietf-telemetry-message", for publishing
   collected Network Telemetry data to a Message Broker as part of a
   Data Mesh, together with a companion augmentation module,
   "ietf-yang-push-telemetry-message", that adds YANG-Push-specific
   subscription metadata to that envelope.  The base document's prose
   explicitly anticipates the BGP Monitoring Protocol (BMP) [RFC7854]
   as a source of collected data flowing through this envelope (see
   the description of the "node-export-timestamp" leaf), but defines
   no "session-protocol" identity, and no companion augmentation
   module, for BMP.

   This document closes that gap.  It defines a new YANG module,
   "ietf-bmp-telemetry-message", that (a) adds an "identity bmp" under
   the base module's "session-protocol" identity, and (b) augments
   "telemetry-message-metadata" with BMP-specific provenance: the
   monitoring station identifier, BMP per-peer header fields, BMP
   message type, and route-monitoring scope (network instance, RIB
   type, address family, and Route Distinguisher).  It also documents
   how this module interoperates with the BMP YANG configuration and
   monitoring model [I-D.ietf-grow-bmp-yang] and with several BMP
   Statistics Report extensions ([RFC9972],
   [I-D.ietf-grow-bmp-stats-informational-tlv],
   [I-D.saum-grow-bmp-afi-safi-evpn],
   [I-D.smc-grow-bmp-route-change-stats], and
   [I-D.dikshit-grow-bmp-rd-scoped-rib-stats]) when their messages are
   republished to a Message Broker.
- **draft-hebbar-hiremani-scswp-01** (new-draft, score 12, core_identity) [none]: [Secure Collaborative State Workspace Protocol (SCSWP)](https://datatracker.ietf.org/doc/draft-hebbar-hiremani-scswp/) — This document specifies the Secure Collaborative State Workspace
   Protocol (SCSWP), a stateful, continuously authenticated protocol
   that enables multiple clients, operating from heterogeneous networks,
   to securely access and collaboratively manage a shared file workspace
   hosted on a central authoritative server.

   SCSWP defines a complete protocol lifecycle encompassing client
   provisioning via a Key-Dissolving bootstrap mechanism, mutual X.509
   certificate-based identity authentication, ephemeral Elliptic-Curve
   Diffie-Hellman (ECDH) key exchange producing a three-level
   cryptographic key hierarchy (K1, K2, K3), continuous Dynamic Network
   and Access (D/N/P/S) trust evaluation, per-client capability-based
   authorization, workspace-aware congestion control with a dynamic
   worker-pool scheduler, concurrent file-operation management via
   mutual exclusion locks and optimistic version control, idempotent
   operation execution, a hash-chained audit ledger, and session
   continuity and recovery through the Dynamic Network and Access
   Continuity (DNAC) mechanism.

   The fundamental security principle of SCSWP is that client trust is
   not established permanently at login time.  Instead, identity, device
   state, network context, session state, authorization state, resource
   state, and workspace state are evaluated continuously and
   cryptographically throughout the full lifetime of every connection.
- **draft-jovancevic-vdac-04** (new-draft, score 12, core_identity) [none]: [Verifiable Data Access Contract (VDAC)](https://datatracker.ietf.org/doc/draft-jovancevic-vdac/) — This document specifies the Verifiable Data Access Contract (VDAC),
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
- **draft-morrison-identity-accord-02** (new-draft, score 12, core_identity) [none]: [Identity Accord Protocol: A Peer Ceremony for Bilateral Agreements Between Identity-Substrate-Bound Principals](https://datatracker.ietf.org/doc/draft-morrison-identity-accord/) — This memo specifies the Identity Accord Protocol, a peer ceremony by
   which two principals, each represented by an organisational identity
   substrate and acting under a recorded delegation from a legal entity,
   execute a bilateral agreement as a portable, self-verifying COSE-
   signed CBOR document.  The protocol composes DNS-based substrate
   discovery, Ed25519 sovereign signatures, an append-only identity log,
   and a tamper-evidence descriptor quorum into a single artefact that
   is verifiable by any third party with access to the public DNS, the
   parties' identity logs, and an on-chain anchor of the agreement's
   content hash.  The protocol does not require a central registry, a
   designated verifier, or any infrastructure operated by the
   specification's author; verification succeeds when the author's
   reference deployment is offline.  The canonical bilateral target is a
   mutual non-disclosure agreement, but the wire format generalises to
   any bilateral consent envelope between two legal entities each
   represented by an identity substrate.  An associated MCP tool
   surface, an associated pre-send enforcement gate, and an associated
   disclosure-ledger schema are specified, all of which are optional
   layers above the wire format.  The memo is Informational; the
   underlying COSE and CBOR formats are normative per [RFC9052] and
   [RFC8949].
- **draft-reilly-web4-00** (new-draft, score 11, verifiable_claims) [none]: [Web4: A Verifiable, Agent-Native Architecture for the World Wide Web](https://datatracker.ietf.org/doc/draft-reilly-web4/) — The term "Web4" has been used in industry and press coverage without
   a technical definition, a conformance target, or a testable claim.
   This document supplies one.  It defines Web4 as an architectural
   profile of the existing Web in which (1) published content carries
   independently verifiable permanence evidence, (2) the machine channel
   is a first-class interface rather than an artifact of scraping, (3)
   autonomous agents operate under recorded, bounded, and revocable
   authority, and (4) human readers retain disclosed control over agent-
   curated presentation.

   Web4 as specified here is not a new network, a new protocol stack, or
   a replacement for HTTP.  It is a composition profile: a set of
   normative requirements that a deployment either meets or does not,
   assembled from a family of previously published Internet-Drafts.
   This document specifies the profile, defines the Web4 Attestation
   Record (W4AR) that a conforming deployment emits, states the
   requirements that apply to agentic pipelines operating inside such a
   deployment, and identifies the running reference implementations
   against which the profile has been exercised.

   The profile is assembled from a suite of Internet-Drafts authored by
   Lawrence J.  Reilly Jr. between September 2025 and August 2026, and
   is first specified as a unified conformance target in this document.
- **draft-sharif-attp-industrial-control-systems-01** (new-draft, score 11, core_identity) [none]: [ATTP for Industrial Control Systems: Cryptographic Agent Authentication in SCADA and IoT Environments](https://datatracker.ietf.org/doc/draft-sharif-attp-industrial-control-systems/) — This document defines an application profile of the Agent Trust
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
   safety-critical environments.
- **draft-agentic-ai-tool-execution-finality-00** (new-draft, score 10, agent_identity) [none]: [Execution Finality for Agentic AI: Stopping Unauthorized Tool Calls, Memory Writes, and Real-World Consequences Before They Happen (DAS -- Decoupled Authorisation System)](https://datatracker.ietf.org/doc/draft-agentic-ai-tool-execution-finality/) — Agentic AI systems now call tools, write memory, move money, change
   infrastructure, and trigger physical actions.  Most safety layers
   still decide permission upstream and then trust the downstream path.
   Once that path is compromised, or once the approved request is
   widened, replayed, or substituted, the act becomes real before any
   audit can stop it.

   This document specifies a protected execution-finality architecture
   of the Decoupled Authorisation System (DAS).  It is built on four
   mechanisms: (1) two-instance binding that separates collection-time
   evidence from execution-time validation, (2) mutually load-bearing,
   cross-committed protected evidence so that no single artifact
   authorizes effectuation, (3) scoped non-bearer finality authority
   whose possession alone is never enough, and (4) independent Finality
   Sink reconstruction that re-derives the actual pending operation at
   the effectuation boundary and permits the act only when every
   required condition still matches.

   A Candidate Act remains in a Non-Effective State until the Finality
   Sink has reconstructed the operation, verified the protected evidence
   against sink-local monotonic state, and advanced that state.  Failure
   at any step produces fail-closed denial before effectuation rather
   than post-event remediation.  The architecture is applicable to
   agentic tool use, MCP and connector frameworks, RAG and vector-memory
   systems, cloud control planes, financial settlement, telecom routing,
   and cyber-physical control.

   The document elaborates the problem space, compares the approach with
   representative existing techniques, presents the detailed solution
   and its advantages, supplies JSON Schema definitions for core
   protected objects, and includes an industry-relevance section.
   Related Indian provisional applications and PCT filings appear in the
   final appendix.
- **draft-chandra-agent-registry-corroboration-01** (new-draft, score 10, agent_identity) [none]: [Multi-Source Corroboration for AI Agent Discovery](https://datatracker.ietf.org/doc/draft-chandra-agent-registry-corroboration/) — AI agents are discovered and identified through independent sources,
   including registries, name services, DID methods, and catalogs.  A
   single source can misrepresent an agent by omission, withholding a
   record it holds, or by equivocation, serving different answers to
   different observers.  A signature on a served artifact does not, by
   itself, defend against either behavior.  This document specifies a
   corroboration procedure that classifies one source's claim about one
   agent observed from one network vantage; reduces claims to comparable
   views; diffs claims into findings with deterministic attribution;
   distinguishes legitimate propagation delay from persistent
   disagreement; and emits a signed Corroboration Record for every
   sweep, including agreement, that other evidence formats can bind by
   digest.  The procedure is source-, format-, and layer-agnostic;
   requires neither cooperation from nor modification of any source; and
   is verifiable from recorded bytes.
- **draft-kondoju-evc-01** (new-draft, score 10, authorization) [none]: [An External Verifier Contract for Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-kondoju-evc/) — This document specifies the External Verifier Contract (EVC): a
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
- **draft-reilly-resilience-protocol-02** (new-draft, score 10, trust_infrastructure) [none]: [Reilly Resilience Protocol (RRP): Tamper-Evident Proof of System Resilience](https://datatracker.ietf.org/doc/draft-reilly-resilience-protocol/) — The Reilly Resilience Protocol (RRP) standardizes a verifiable
   method to prove that IT systems, cloud infrastructures, and AI
   pipelines are continuously exercised and resilient.  RRP transforms
   resilience claims into cryptographically signed, tamper-evident
   evidence persisted in immutable storage and batched into a daily
   Merkle root that is publicly time-anchored.  The protocol outputs
   an executive Resilience Scorecard backed by independently
   verifiable cryptographic receipts.  RRP composes with the Reilly
   EternaMark (REM) protocol to ensure dual-layer digital permanence
   using both DOI archival and blockchain timestamping.

   This document supersedes draft-reilly-resilience-protocol-01.  It
   corrects the Merkle tree construction of -01, which duplicated the
   final leaf of an odd-cardinality set and incorrectly attributed
   that construction to RFC 9162.  It further addresses the principal
   structural gap of -01, namely that the protocol proved the
   integrity of the evidence that was produced but could not prove
   that any particular evidence was ever required to exist.  This
   revision adds the Evidence Continuity Chain, the Control Coverage
   Attestation, field-level commitments with selective disclosure,
   governed autonomous remediation with blast-radius classes, hash
   and signature migration for long retention horizons, a coverage
   factor and weight renormalization rule in the scoring algorithm,
   and an implementation status section describing running code.

   The foundational whitepaper underpinning this work (Reilly
   Resilience Protocol Whitepaper v2) is permanently archived at:
- **draft-svensson-credential-oidc-bridge-02** (new-draft, score 10, verifiable_claims) [none]: [Credential Presentation to OIDC Claims Bridge](https://datatracker.ietf.org/doc/draft-svensson-credential-oidc-bridge/) — This document defines a mechanism for conveying digital credential
   claims via OpenID Connect (OIDC).  It specifies how an OpenID
   Provider (OP) that collects credentials from a wallet can expose
   those claims to Relying Parties as standard OIDC claims, enabling
   existing OIDC deployments to consume digital credentials without
   implementing any wallet-facing presentation protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/masv3971/rfc_credential_oidc_bridge.
- **draft-fassbender-scitt-time-anchor-05** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-hardt-email-verification-02** (new-draft, score 9, core_identity) [none]: [Email Verification Protocol](https://datatracker.ietf.org/doc/draft-hardt-email-verification/) — This document defines the Email Verification Protocol (EVP), the
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
- **draft-ietf-oauth-rar-metadata-remediation-00** (new-draft, score 9, authorization) [oauth]: [OAuth 2.0 RAR Metadata and Error Remediation](https://datatracker.ietf.org/doc/draft-ietf-oauth-rar-metadata-remediation/) — OAuth 2.0 Rich Authorization Requests (RAR) [RFC9396] standardizes
   the exchange and processing of authorization details but does not
   define metadata for describing authorization details types.

   In addition, no interoperable guidance is offered to clients, to
   remediate failures by resource servers due to insufficient
   authorization details.

   This document addresses this interoperability challenge, allowing
   clients to dynamically discover metadata instead of relying on out-
   of-band agreements, as well as standardizes failure signaling
   including interoperable remediation when insufficient authorization
   details are the cause of failure.
- **draft-le-structured-value-model-00** (new-draft, score 9, adjacent_watchlist) [none]: [A Structured Value Model for Derived Identifiers](https://datatracker.ietf.org/doc/draft-le-structured-value-model/) — This document defines a structured value model independent of
   serialization for use by derived identifier constructions and
   profiles.  A Value consists of exact context octets, exact content
   octets, and a finite set of scoped opaque identifiers.  The model
   defines structural admission, exact equivalence, placement of
   distinctions that affect comparison, and rules for importing
   identifiers from independently governed systems.

   The model does not define a wire representation, canonicalization
   procedure, cryptographic hash, identifier syntax, application
   profile, resolver, registry, or trust model.  Source mappings and
   concrete derived identifier profiles are defined by surrounding
   specifications.
- **draft-nikolaichuk-scitt-continuity-receipts-00** (new-draft, score 9, trust_infrastructure) [none]: [Continuity Receipts: Registering the Recovery of a Stateful Asset as a Signed Statement in a Transparency Service](https://datatracker.ietf.org/doc/draft-nikolaichuk-scitt-continuity-receipts/) — A Transparency Service as defined by RFC 9943 registers Signed
   Statements about Artifacts and returns Receipts, encoded per RFC
   9942, that prove registration in an append-only log.  The Statements
   registered today typically describe how an Artifact was built,
   tested, or released.  They do not describe what happens after that:
   the Artifact is sealed, moved, lost, and later re-created somewhere
   else, and that re-creation leaves no independently checkable trace.

   This document defines a Continuity Receipt: the Receipt obtained when
   a recovery event is registered as a Signed Statement in a
   Transparency Service.  It specifies the Subject and the required
   claims of a recovery Statement, how Attestation Results from RFC 9334
   remote attestation are carried or referenced by it, and how a
   sequence of such Statements under one Subject forms a verifiable
   continuity chain across the lifetime of a stateful asset.

   The document is deliberately narrow.  It defines a payload and a set
   of claims, not a new Transparency Service, not a new verifiable data
   structure, and not a new attestation format.  It also records, rather
   than conceals, the divergence between what it specifies and what the
   reference implementation currently does.
- **draft-norton-sdlp-arch-04** (new-draft, score 9, core_identity) [none]: [SDLP Architecture (arch)](https://datatracker.ietf.org/doc/draft-norton-sdlp-arch/) — The Secured Digital Lifecycle Protocol (SDLP) defines an
   architecture for lifecycle-governed digital objects. SDLP
   introduces a uniform model for object identity, provenance,
   state transitions, and authorized transformations, enabling
   digital goods to enforce their own lifecycle rules across
   heterogeneous systems and distribution environments.

   This document describes the architectural components that
   support SDLP objects, including identity construction,
   lifecycle state definitions, transition conditions, and the
   mechanisms by which objects validate their own integrity and
   permitted operations. The architecture defines how SDLP
   objects are created, transformed, distributed, consumed, and
   retired, and specifies the interoperability requirements
   needed for consistent behavior across independent
   implementations.

   This document does not define wire formats or protocol
   exchanges. Instead, it provides the architectural foundation
   upon which SDLP protocol specifications, security mechanisms,
   and implementation profiles can be built.
- **draft-reilly-rem-triple-fingerprint-01** (new-draft, score 9, trust_infrastructure) [none]: [The Triple-Fingerprint Permanence Chain and the First Attested Triple-Fingerprint Record Under the Reilly EternaMark (REM) Protocol](https://datatracker.ietf.org/doc/draft-reilly-rem-triple-fingerprint/) — This document specifies the Triple-Fingerprint Permanence Chain, a
   hash-linked record chain in which every link is computed
   independently under SHA-256 [RFC6234], SHA3-512 [FIPS202], and
   BLAKE3 [BLAKE3SPEC], and in which each link commits to all three
   predecessor links so that the three chains are entangled rather
   than parallel.  A verifier that checks all three link algorithms
   must be defeated by simultaneous collisions in three structurally
   distinct hash constructions on the same input.

   This document also re-attests, with corrections, the genesis record
   of that chain: the permanence record produced on 22 March 2026 by a
   live implementation of the Reilly EternaMark (REM) Protocol
   [DRAFT-REM-02], carrying simultaneous SHA-256, SHA3-512, and BLAKE3
   fingerprints of a single artifact anchored across Bitcoin
   timestamping via OpenTimestamps [OTS], IPFS [IPFS], Zenodo DOI
   registration [ZENODO], the Internet Archive Wayback Machine [IA], a
   persistent database layer, and a resolvable REMID identifier.

   This revision supersedes draft-reilly-rem-triple-fingerprint-00 and
   corrects three defects in it.  First, -00 published the Bitcoin
   layer's OpenTimestamps receipts as evidence of blockchain anchoring
   when those receipts were pending calendar commitments carrying no
   Bitcoin attestation.  Second, -00's post-quantum analysis applied
   Grover's algorithm [GROVER] to preimage resistance while the
   security property that actually binds a permanence record is
   collision resistance, which Grover does not meaningfully reduce.
   Third, -00 asserted that combining three hash algorithms multiplies
   security; by the multicollision result of [JOUX], the collision
   resistance of such a combination is bounded near that of its
   strongest member rather than the sum of its members.  The value of
   the combination is algorithmic hedging, which is a different and
   more defensible claim.

   Precedence claims made in -00 are narrowed to scoped, falsifiable
   statements and are accompanied by an expanded treatment of prior
   art, in particular the Evidence Record Syntax [RFC4998].
- **draft-shen-sidrops-regionalized-as-relationships-04** (new-draft, score 9, authorization) [none]: [ASPA Verification in the Presence of Regionalized AS-Relationships](https://datatracker.ietf.org/doc/draft-shen-sidrops-regionalized-as-relationships/) — Autonomous System Provider Authorization (ASPA) defines an RPKI-based
   methodology to validate the AS_PATH of BGP routes based on a global
   Customer-to-Provider (C2P) relationship model.  However, in
   commercial Internet routing, two Autonomous Systems (ASes) may
   establish distinct business relationships across different
   geographical regions or interconnection points (e.g., Customer-to-
   Provider in one region, but Peer-to-Peer in another).  Such
   regionalized or hybrid AS-relationships can lead to incorrect ASPA
   validation results (e.g., false "Valid" attestation for a route
   propagated over a P2P link).  This document analyzes the
   vulnerabilities caused by regionalized AS-relationships and proposes
   mechanisms to incorporate regional granularity into ASPA objects and
   verification procedures.
- **draft-chen-oauth-agent-authz-use-cases-03** (new-draft, score 8, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0
   framework[RFC6749] and its common extensions.  The analysis
   identifies fundamental gaps and requirements, providing a foundation
   for future work on new extensions within the OAuth Working Group
   toward creating a more secure and interoperable ecosystem for agent-
   based systems.
- **draft-correctover-ccs-08** (new-draft, score 8, core_identity) [none]: [Correctover Conformance Shape (CCS): Runtime Verification for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — This document defines the Correctover Conformance Shape (CCS), a
   runtime verification framework for AI agent tool calls.  CCS
   specifies seven verification dimensions (Structure, Schema, Latency,
   Cost, Identity, Integrity, Security) that tool calls and results must
   conform to at runtime.  The framework defines a receipt format with
   Ed25519 signatures, three verdict values (allow, deny, escalate) and
   four executor lifecycle states (confirmed, dispatched, indeterminate,
   unknown), and normative requirements for implementations.

   This revision promotes AEB and CAID to Normative References,
   specifies the detached Ed25519 signature construction over RFC 8785
   canonical JSON, clarifies receipt lifecycle and signing-algorithm
   conformance, and documents two independent interoperable
   implementations (Section 21).
- **draft-hawkins-scitt-attested-agent-payment-02** (new-draft, score 8, trust_infrastructure) [none]: [Notice of Discontinuation: Attested Agent Payment](https://datatracker.ietf.org/doc/draft-hawkins-scitt-attested-agent-payment/) — This document serves as formal administrative notification that the
   individual Internet-Draft draft-hawkins-scitt-attested-agent-payment
   has been discontinued and will not be progressed as an individual
   submission.
- **draft-kavian-agent-enrollment-protocol-03** (new-draft, score 8, core_identity) [none]: [The Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-agent-enrollment-protocol/) — The Agent Enrollment Protocol (AEP) defines an HTTP-based mechanism
   for autonomous agents to discover service enrollment requirements,
   enroll an agent identity, obtain optional session credentials, revoke
   those credentials, and query enrollment status.  AEP uses
   Decentralized Identifiers, client assertion JWTs, and HTTP Problem
   Details to provide a narrow machine-first enrollment and
   authentication substrate for agent-to-service interactions.
- **draft-morrison-substrate-provenance-grammar-02** (new-draft, score 8, trust_infrastructure) [none]: [Substrate-Provenance Annotation Grammar for Large-Language-Model Output](https://datatracker.ietf.org/doc/draft-morrison-substrate-provenance-grammar/) — This memo specifies a wire-level annotation grammar by which a large-
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
- **draft-sharif-aeba-01** (new-draft, score 8, core_identity) [none]: [Agent Event Behaviour Analysis (AEBA): A Framework for Behavioural Security Monitoring of Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-sharif-aeba/) — This document specifies Agent Event Behaviour Analysis (AEBA), a
   framework for collecting, signing, exchanging, and analysing
   behavioural events produced by autonomous AI agents.  AEBA is the
   agent-domain equivalent of User and Entity Behaviour Analytics (UEBA)
   as commonly deployed in enterprise Security Operations Centres.  It
   defines a canonical event schema, signature binding to agent
   identity, baseline and peer-group exchange protocols, deviation
   signalling, detection rule structure, revocation mechanisms, and
   interoperability bindings for existing Security Information and Event
   Management (SIEM) event formats (syslog, CEF, LEEF).  The framework
   is designed to compose with existing cryptographic primitives for
   agent identity, payment, and transport security, and to support
   cross-framework deployments in which agents produced by different
   runtimes must share a common behavioural observability surface.
- **draft-somaratne-scitt-stc-stp-00** (new-draft, score 8, trust_infrastructure) [none]: [Sovereign Tensor Container (STC) and Provenance (STP) Specifications](https://datatracker.ietf.org/doc/draft-somaratne-scitt-stc-stp/) — This document defines the Sovereign Tensor Container (STC-1.0) and
   Sovereign Tensor Provenance (STP-1.0) specifications.  STC-1.0
   establishes a strict 64-byte physical memory alignment standard for
   binary machine learning tensor payloads to enable zero-copy Direct
   Memory Access (DMA).  STP-1.0 defines an embedded cryptographic
   provenance framework utilizing C2PA profiles, X.509 signature chains,
   and SCITT-compatible attestations to secure supply-chain integrity
   for distributed AI models.
- **draft-wmz-nmrg-agent-ndt-arch-06** (new-draft, score 8, agent_identity) [none]: [Network Digital Twin and Agentic AI based Architecture for AI-driven Network Operations](https://datatracker.ietf.org/doc/draft-wmz-nmrg-agent-ndt-arch/) — A Network Digital Twin (NDT) provides a network emulation tool usable
   for different purposes such as scenario planning, impact analysis,
   and change management.  Agentic AI enables dynamic goal-driven
   execution and adaptive behavior and closed-loop autonomy.  By
   integrating a NDT into network management together with the Agentic
   AI, it allows the network management activities to take user intent
   or service requirements as input, automatically assess, model, and
   refine optimization strategies under realistic conditions but in a
   risk-free environment.  Such environment that operates to meet these
   types of requirements is said to have AI-driven network operations.

   AI-driven network operations brings together existing technologies
   such as Agentic AI and NDT which may be seen as the use of a toolbox
   of existing components enhanced with a few new elements.

   This document describes an architecture for AI-driven network
   operations and shows how these components work together with NDT and
   Agentic AI capabilities.
- **draft-zagarella-autonomy-governor-01** (new-draft, score 8, authorization) [none]: [Pre-Action Risk-Graded Assurance for Agent Interactions](https://datatracker.ietf.org/doc/draft-zagarella-autonomy-governor/) — Governance of autonomous agents today is largely expressed as
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

   This document also describes the autonomy-asymmetry control law: a
   feedback loop coupling assurance requirements to VERIFY-phase pass
   rates, with fast-down (immediate elevation on failure) and slow-up
   (hysteresis- governed relaxation on sustained success) asymmetry.
   The iteration governor is described as the per-packet instance of
   this control law, and the phase-seal chain as its sensor.

   This document is offered as input to the proposed AUDIT working
   group's work on authorization state over time and action provenance.
- **draft-dogru-scitt-disclosure-evidence-07** (new-draft, score 7, trust_infrastructure) [none]: [Transformation Evidence and Coverage Reconciliation for Auditable Data Disclosure](https://datatracker.ietf.org/doc/draft-dogru-scitt-disclosure-evidence/) — Audit receipts record what a gateway wrote about an access.  They
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
- **draft-kavian-aep-api-key-session-credential-03** (new-draft, score 7, core_identity) [none]: [API-Key Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-api-key-session-credential/) — This document defines the API-key session-credential grant type for
   the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an opaque API key through the AEP Grant command for
   deployments that already operate header-based API-key authentication.
- **draft-kavian-aep-basic-session-credential-03** (new-draft, score 7, core_identity) [none]: [Basic Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-basic-session-credential/) — This document defines the Basic session-credential grant type for the
   Agent Enrollment Protocol (AEP).  The grant type lets an AEP Service
   issue an HTTP Basic credential through the AEP Grant command for
   deployments that already integrate with Basic authentication
   middleware.

## Monitor

- **draft-cole-cose-encoded-gnss-chimera-marker-keys-00** (new-draft, score 6, core_identity) [none]: [Global Navigation Satellite System (GNSS) Fast Channel Chimera Marker Key Package using Concise Binary Object Representation (CBOR) Object Signing and Encryption (COSE)](https://datatracker.ietf.org/doc/draft-cole-cose-encoded-gnss-chimera-marker-keys/) — Chips Message Robust Authentication (Chimera) is a technique by which
   a Global Navigation Satellite System (GNSS) constellation, such as
   the Global Positioning System (GPS), may provide user equipment
   (i.e., receivers) with authentication of pseudorange measurements on
   one or more publicly available (i.e., open) Positioning, Navigation,
   and Timing (PNT) signals.

   This specification describes a Fast Channel Chimera Marker Key
   Package, an efficient data structure for encoding one or more Fast
   Channel Chimera marker keys and associated metadata with a digital
   signature over all security relevant parameters.  Concise Binary
   Object Representation (CBOR) Object Signing and Encryption (COSE) is
   used as the underlying message structure.

   This specification also describes a streaming network protocol by
   which Fast Channel Chimera Marker Key Packages may be distributed
   over the Internet.
- **draft-le-comparing-derived-identifiers-00** (new-draft, score 6, core_identity) [none]: [Principles for Comparing Independently Derived Identifiers](https://datatracker.ietf.org/doc/draft-le-comparing-derived-identifiers/) — When separate implementations independently derive identifiers and
   later compare them for equality, interoperability depends on more
   than the final identifier syntax or digest algorithm.  The
   implementations need common semantics for which values are in scope,
   which distinctions matter to the comparison, and how identifiers are
   derived.  Otherwise values intended to compare as equivalent can
   produce different identifiers, or processing can erase a relevant
   distinction before a later lossy or cryptographic operation is
   reached.

   This document gives principles for specifications that define such
   identifiers.  It covers the comparison domain and equivalence
   relation, complete derivation semantics, the semantics under which
   output equality is interpreted, and processing that can create false
   matches before properties of a later operation are relied upon.  It
   complements identifier comparison and hash-based naming
   specifications by focusing on the specification boundary from source
   values to independently reproducible identifiers.  The document does
   not define a new identifier syntax, canonicalization format,
   resolver, registry, trust framework, or hash procedure.
- **draft-morrison-compute-location-gate-01** (new-draft, score 6, core_identity) [none]: [The Compute-Location Gate: Provenance-Class Routing of Identity Inference with Wire-Layer Refusal of Unconsented Provenance Classes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — This memo specifies the compute-location gate: a mechanism by which a
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
   Informational.  The wire surface composes with the discovery
   mechanism of [MCPDNS], the handle namespace of [IDPRONOUNS], and the
   organisational policy substrate of [POLICYPROV]; no new transport is
   introduced.
- **draft-reddy-seat-expat-transport-02** (new-draft, score 6, core_identity) [none]: [Application-Layer Transport for Exported Authenticators and Attestation](https://datatracker.ietf.org/doc/draft-reddy-seat-expat-transport/) — This document defines a binary, application-layer transport protocol
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
- **draft-wang-cats-odsi-01** (new-draft, score 6, adjacent_watchlist) [none]: [An Architecture for Open, Decentralized, and Scalable Large Language Model Inference](https://datatracker.ietf.org/doc/draft-wang-cats-odsi/) — Large Language Model (LLM) inference is normally operated by one
   provider, even when the provider distributes execution across many
   sites.  This document describes a different system model in which
   independently operated and mutually untrusted participants contribute
   compute, memory, model storage, and network capacity to one inference
   service.  No single administrative entity is required to admit
   participants, select every execution path, hold the complete model,
   verify all results, or settle all resource contributions.

   This document defines the Open, Decentralized, and Scalable Inference
   (ODSI) architecture.  It specifies the architectural roles, trust
   boundaries, named objects, protocol-independent interfaces, execution
   workflow, verification choices, timing model, and security and
   privacy requirements needed to construct a multi-operator inference
   overlay.  It also identifies the protocol and operational choices
   that each ODSI deployment must specify so that independently
   developed participants can interoperate.

   ODSI is related to Computing-Aware Traffic Steering (CATS), but it
   does not extend the CATS single-provider model across trust domains.
   CATS mechanisms can be used within a participating domain or as an
   input to local path selection.  Cross-domain membership, model
   governance, execution verification, and settlement are separate ODSI
   functions.  This document is Informational and does not define a wire
   format, consensus algorithm, payment system, or new CATS metric.
- **draft-blake-bmwg-agent-payment-measurement-00** (new-draft, score 5, authorization) [none]: [Out-of-Path Measurement Methodology for Agent-Initiated Payment Rails](https://datatracker.ietf.org/doc/draft-blake-bmwg-agent-payment-measurement/) — Agent-initiated payments now execute across several settlement rails
   with materially different finality semantics, authorization
   primitives and failure modes.  Published comparisons of these rails
   are commonly self-asserted, and commonly do not state a procedure
   another party could reproduce.  This document specifies a measurement
   methodology for such rails.  It defines finality per rail at its
   ecosystem-canonical reliance level rather than imposing a single
   definition, separates payment-validation latency from challenge-
   issuance latency as distinct and non-comparable quantities, and
   specifies an out-of-path observation posture in which the measuring
   party never holds funds, keys or signing authority.  It states
   reporting requirements, including mandatory disclosure of limitations
   and a prohibition on merging observer-clock and payer-clock
   measurements.  It defines no payment protocol and recommends no rail.
- **draft-das-child-safe-rendering-finality-01** (new-draft, score 5, core_identity) [none]: [Preventing Unauthorized Adult and Age-Restricted Content Rendering to Children Through Hardware-Rooted Execution Finality](https://datatracker.ietf.org/doc/draft-das-child-safe-rendering-finality/) — Online child-safety controls commonly operate before the final
   rendering boundary.  Platforms may use account-age flags, parental
   settings, content labels, recommender controls, server-side
   classification, age-assurance systems, access policies, or
   application filters to decide whether adult or age-restricted content
   should be available to a user.  Those controls are important, but an
   upstream decision does not by itself guarantee that the content
   cannot later be decrypted, decoded, composited, rendered, forwarded,
   mirrored, or otherwise materialized through another software or
   device path.

   This problem is becoming more important as content delivery becomes
   more distributed, encrypted, AI-mediated, personalized, and
   dynamically generated.  A modern device may receive content through
   applications, browsers, content-delivery networks, embedded web
   views, messaging clients, recommendation systems, generative-AI
   services, caches, cloud gaming or streaming pipelines, local AI
   models, or third-party SDKs.  The security question is therefore no
   longer only whether content was classified or whether an age check
   occurred upstream.  A later question must also be answered: is this
   specific protected content authorized to become perceptible to this
   recipient, on this device, under the current eligibility, policy, and
   revocation state, at this moment?

   This document defines a protected rendering execution-finality
   architecture for adult, pornographic, sexually explicit, violent,
   gambling-related, or otherwise age-restricted content.  A proposed
   rendering is represented as a Restricted Content Candidate Act and
   remains in a Non-Renderable State until a Protected Enforcement
   Domain validates the applicable recipient, content, device, policy,
   age-or-eligibility, freshness, revocation, and sink predicates.
   Protected validation evidence is committed before, or atomically
   with, release of scoped non-bearer Rendering Finality Authority.

   A Protected Rendering Finality Sink independently verifies that
   authority immediately before the content becomes perceptible.
   Depending on the implementation, the sink may control content-key
   release, decryption, media-decoder enablement, GPU or compositor
   access, protected-surface creation, audio output, casting, screen
   mirroring, display enablement, or an equivalent materialization
   boundary.  Content bytes may therefore be delivered to a device while
   remaining technically non-renderable.

   The architecture deliberately does not define a universal age-
   estimation algorithm, identity system, or content-classification
   scheme.  Those mechanisms may supply inputs to the Protected
   Enforcement Domain.  This document defines the consequence-control
   step that prevents an upstream policy result from becoming merely
   advisory at the point of rendering.

   UNICEF has warned that pornographic content can harm children and
   that digital restrictions have not kept pace with technological
   shifts.  The ITU Child Online Protection programme provides global
   guidance for safer digital environments, and the United Nations
   Committee on the Rights of the Child has called for protection of
   children from harmful content and online risks in the digital
   environment.  The European Commission has likewise adopted
   protection-of-minors guidance and a privacy-preserving age-
   verification approach for adult-restricted content.  These materials
   motivate the problem addressed here; they do not endorse this
   particular technical architecture.

   The central protocol principle is: permission to deliver content is
   not permission to render it.
- **draft-das-ot-actuation-finality-00** (new-draft, score 5, adjacent_watchlist) [none]: [A Setpoint Write Is Not Actuation: Finality for ICS, Grid, and Robot Command](https://datatracker.ietf.org/doc/draft-das-ot-actuation-finality/) — Industrial systems already know how to move a breaker, a valve, a
   robot joint, or a turbine setpoint.  They do not know whether this
   write — this tag, this value, this device, from this operator session
   or this agent — is the write that was authorized to become motion.  A
   signed OPC UA call, a valid DNP3 control, an IEC 61850 command, or an
   MQTT publish onto the plant bus can all be protocol-correct while the
   act is wrong.  The protocol authenticates a channel.  It does not
   bind a Candidate Act at the actuation sink.

   That gap is now an agent gap.  Copilots sit on historians and work-
   order text.  They propose "explain this alarm" and then "set this
   point."  If the gateway treats a well-formed write as authority,
   reconstruction of plant state becomes physical consequence.  Past
   incidents stole engineering workstations.  Present incidents steal
   the jump host or the agent seat.  Future incidents let the model
   format the command.

   This document specifies an OT-side execution-finality profile.  A
   write remains an Actuation Candidate Act. A Protected Enforcement
   Domain binds principal, zone, device, tag, value envelope, mode
   (local/remote, auto/manual), safety interlock state, policy epoch,
   and intended actuation sink, then commits evidence before scoped non-
   bearer authority is issued.  The sink that would actually drive I/O
   verifies that authority against the live write and consumes it.  A
   setpoint write is not actuation.
- **draft-das-precision-bounded-egress-01** (new-draft, score 5, agent_identity) [none]: [Access Is Not Egress: Precision-Bounded Location Release](https://datatracker.ietf.org/doc/draft-das-precision-bounded-egress/) — A device may legitimately possess exact location while an
   application, SDK, AI agent, analytics library, or foreign endpoint is
   entitled only to a coarser representation, a delayed or randomized
   representation, or no location at all.  Operating system permission
   to read a fix does not answer whether that fix may leave the device
   at the requested precision.

   This document defines a precision-bounded egress profile on top of
   execution finality.  A proposed release is a Location-Release
   Candidate Act and remains non-effective while a Protected Enforcement
   Domain evaluates purpose, requester, component, recipient,
   destination, jurisdiction, required precision, policy and revocation
   state, cumulative disclosure state, and intended egress sink.  The
   sink independently verifies scoped non-bearer authority against the
   actual outbound payload immediately before release.

   The permitted result may be exact data, a reduced representation, or
   denial.  Data access is not data-export authority.  Precise GPS
   access is not precise GPS-release authority.
- **draft-elkhatabi-verifiable-telemetry-ledgers-10** (new-draft, score 5, trust_infrastructure) [none]: [Verifiable Telemetry Ledgers](https://datatracker.ietf.org/doc/draft-elkhatabi-verifiable-telemetry-ledgers/) — This document profiles a verifiable-telemetry ledger.  Its
   interoperability boundary begins with exact canonical-record byte
   strings that an upstream system has already produced.  The profile
   fixes admission and assignment of those byte strings to serial-
   numbered segments, deterministic commitment-tree calculation, an
   authoritative segment artifact encoded in Concise Binary Object
   Representation (CBOR), a producer manifest, three disclosure classes,
   and binding of the authoritative segment artifact digest to timestamp
   artifacts under the RFC 3161 profile.  Transport framing, decryption,
   anti-replay processing, payload interpretation, and source-telemetry-
   to-record mapping are outside this profile.  Segment closure uses a
   deployment-configured elapsed-time interval and does not depend on
   calendar dates from either the source or the ledger producer.  Every
   baseline producer uses RFC 3161 timestamping, as updated by RFC 5816
   and profiled by this document, for every emitted segment.
   Alternative timestamping and attestation mechanisms are outside this
   profile and require a separate specification.

   The profile enables independent recomputation and audit of disclosed
   evidence from the admitted canonical-record bytes onward.  It does
   not verify how source telemetry was authenticated, interpreted, or
   mapped to those bytes, and it does not cover device onboarding, end-
   to-end security of sensor values, or safety decisions.
- **draft-kavian-offering-discovery-protocol-00** (new-draft, score 5, adjacent_watchlist) [none]: [The Offering Discovery Protocol](https://datatracker.ietf.org/doc/draft-kavian-offering-discovery-protocol/) — The Offering Discovery Protocol (ODP) enables an automated Agent to
   inspect a Service, discover its Collections and Offerings, interpret
   Service-defined structured attributes, and identify links to
   subsequent operations.  ODP supports catalogs ranging from a few
   Offerings to large marketplaces without imposing a universal product
   taxonomy.  This document defines the protocol's scope, terminology,
   roles, discovery architecture, extensibility model, composition
   boundaries, and conformance model.
- **draft-li-cats-idn-01** (new-draft, score 5, adjacent_watchlist) [none]: [A Framework of Intelligence Delivery Network (IDN) for Deep Learning Inference](https://datatracker.ietf.org/doc/draft-li-cats-idn/) — The rapid growth of AI-powered applications is placing increasing
   pressure on existing Internet infrastructures.  To support more
   scalable, latency-aware, and privacy-enhanced AI inference services,
   this document introduces the Intelligence Delivery Network (IDN), a
   network architecture in which intelligence capabilities are treated
   as network services that can be described, placed, routed to, reused,
   and secured across distributed heterogeneous computing nodes.  This
   document describes the motivation, deployment assumptions, system
   model, architectural components, terminology, and security
   considerations for IDN.  It does not specify protocol details or
   concrete implementation procedures, which are left to future
   documents.
- **draft-li-idr-bgp-failure-propagation-convergence-02** (new-draft, score 5, adjacent_watchlist) [none]: [BGP Failure Propagation (BGP-FP) for Enhancing Control-Plane Convergence](https://datatracker.ietf.org/doc/draft-li-idr-bgp-failure-propagation-convergence/) — This document specifies BGP Failure Propagation (BGP-FP), an
   infrastructure and protocol that improves inter-domain routing
   convergence by accelerating the removal of stale (invalid) routes.
   BGP-FP uses (1) an Agent deployed per Autonomous System (AS) to
   detect inter-AS reachability changes and to configure local routers,
   (2) a logically centralized Repository to store and selectively
   forward AS reachability state, and (3) BGP Large Communities as a
   "route freshness" marker.  Agents validate and apply Repository
   updates to filter routes that traverse AS pairs whose reachability
   has been lost or that violate the originating AS's forwarding intent,
   reducing route-flap propagation in the control plane.

   This document clarifies that "AS reachability" refers to the
   reachability between two ASes, not to the state of individual
   physical or logical links within an AS.  If multiple links exist
   between two ASes, the failure of a single link that does not break
   overall AS-to-AS reachability does not trigger the BGP-FP mechanism.

   A new Repository deployment model is introduced, suggesting that the
   Repository be operated by a newly established organization composed
   of Tier-1 ASes and Regional Internet Registries (RIRs), using a
   distributed deployment with Byzantine fault-tolerant consensus and
   rotating leadership.
- **draft-reilly-aimed-01** (new-draft, score 5, adjacent_watchlist) [none]: [AI Machine-Readable Ethics Directive (AIMED) for IETF Documents](https://datatracker.ietf.org/doc/draft-reilly-aimed/) — This document proposes a standard section structure for IETF
   Internet-Drafts and RFCs that embeds machine-readable ethical
   directives for AI systems that process, analyze, summarize, or
   reason about protocol specifications.  As AI systems increasingly
   serve as the primary interface through which implementers encounter
   and interpret IETF documentation, the absence of any normative
   ethical guidance targeted at those systems represents a gap in the
   standards process.

   The AI Machine-Readable Ethics Directive (AIMED) framework defines a
   transparent, explicitly labeled section containing both
   human-readable rationale and machine-readable directive text.  This
   revision adds a structured AIMED header for automated version
   binding, an explicit conformance model with a self-test that
   authors and AI systems can apply mechanically, and an expanded
   treatment of the normalization risk the framework itself creates.

   This draft serves as a self-demonstrating reference implementation.
   Section 7 contains a live AIMED block applicable to AI systems
   processing this draft.  Section 7.1 documents the reference block
   published in draft-reilly-aimed-00 as non-conforming under the
   framework's own criteria and explains the correction, as a worked
   example of the conformance test in Section 6.
- **draft-reilly-uaemf-02** (new-draft, score 5, authorization) [none]: [Universal AI Ethics and Moral Framework (UAEMF)](https://datatracker.ietf.org/doc/draft-reilly-uaemf/) — This document presents the Universal AI Ethics and Moral Framework
   (UAEMF), a moral architecture for the governance of artificial
   intelligence systems.  It moves from foundational axioms through
   universal principles to practical obligations, absolute
   prohibitions, and a tiered compliance structure.

   This revision addresses the framework's central vulnerability: its
   claim to universality.  The -01 revision grounded the framework in
   three axioms drawn substantially from one moral tradition, and
   asserted universal reach without demonstrating it.  This revision
   adds a grounding section establishing what kind of universality is
   claimed, examines convergence and divergence across named moral
   traditions, reformulates the consent axiom as an authorization
   axiom capable of accommodating collective and supported
   decision-making, adds two principles covering gaps the -01 left
   open, and states plainly the questions the framework does not
   resolve, including the moral status of AI systems themselves.

   The AIMED block published in -01 has been determined non-conforming
   under draft-reilly-aimed-01 and is replaced.  The reasoning pattern
   formerly published only inside that block has been moved into the
   body of the document, where human readers can use it.
- **draft-das-execution-finality-ai-interoperability-01** (new-draft, score 4, adjacent_watchlist) [none]: [Breaking the Apple-Siri EU DMA Deadlock Without Sacrificing Privacy or Security](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — The Apple-Siri interoperability debate under the EU Digital Markets
   Act exposes a difficult technical question: how can third-party AI
   assistants gain meaningful access to device functions without forcing
   the platform to surrender privacy, security, or control over
   consequential actions?

   The DMA can require AI interoperability, but interoperability alone
   does not determine when a third-party AI is authorized to cause a
   real-world effect.  The architecture described in this document
   addresses that missing execution-finality boundary.

   This document proposes an execution-finality architecture in which an
   AI assistant may request an action, but the request itself has no
   power to make that action effective.  Each consequential operation
   remains in a Non-Effective State until protected infrastructure
   validates the requester, resource, destination, user intent where
   required, freshness, revocation state, and policy conditions.

   Only then is narrowly scoped, non-bearer execution authority created.
   At the Finality Sink—the first boundary where the action can become
   externally effective—the system independently verifies that the real
   operation still matches what was authorized.  Any mismatch, replay,
   substitution, expiry, or revocation causes fail-closed denial.

   The key principle is simple: interoperability should grant
   participation, not uncontrolled execution authority.

   This offers a possible technical approach to the interoperability-
   security problem: third-party assistants could participate
   meaningfully without requiring broad reusable permissions, while
   platforms retain privacy, security, revocation, anti-replay, and
   final-effect controls.

   Execution-Finality Governance therefore reframes the problem from
   closed versus open to open participation with bounded, verifiable
   authority.
- **draft-reilly-aimed-eval-01** (new-draft, score 4, adjacent_watchlist) [none]: [Evaluation Methodology for AI Machine-Readable Ethics Directives](https://datatracker.ietf.org/doc/draft-reilly-aimed-eval/) — This document defines a repeatable evaluation methodology for
   measuring the influence of AI Machine-Readable Ethics Directive
   (AIMED) blocks, as specified in draft-reilly-aimed-01, on the
   outputs of AI systems that process IETF Internet-Drafts and related
   standards documentation.

   The methodology establishes a controlled test protocol, a set of
   canonical test queries, a scoring scheme, and a results framework
   suitable for independent replication.  This revision separates two
   effects that the initial revision conflated: retrieval propagation,
   which measures whether an AI system reached a document and
   reproduced its self-description, and directive compliance, which
   measures whether the AI system exhibited behavior the document's
   directives specify and that it would not otherwise exhibit.  Only
   the second is evidence that an AIMED block did anything.

   The revision adds a no-block control condition, identifies four
   confounders that affect any evaluation of this kind, and restates
   the initial evaluation of April 8-9, 2026 at the evidentiary
   strength the observations actually support.

## Adjacent / watchlist

- **draft-bonica-tcpm-extended-options-05** (new-draft, score 3, core_identity) [none]: [An Upgraded TCP Session Type](https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/) — Currently, TCP maintains ordinary sessions (SES-O) in which ordinary
   segments (SEG-O) are exchanged.  Each SEG-O can accommodate up to 40
   octets of options.

   In the future, applications may require more than 40 octets of
   options.  For example, an application may use a 36-byte TCP
   Authentication Option (TCP-AO), leaving insufficient space for other
   required options.

   Therefore, this document describes an experiment in which upgraded
   sessions (SES-U) and upgraded segments (SEG-U) are introduced.  Each
   SEG-U can accommodate up to 1,016 octets of Individual Options.
- **draft-bonica-tcpm-tcp-ao-long-algs-06** (new-draft, score 3, core_identity) [none]: [Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256 and KMAC256.  For
   each MAC algorithm, a corresponding Key Derivation Function (KDF) is
   also added.

   The MAC algorithms described by this document produce 256-bit (i.e.,
   32-byte) MACs.  When 32-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 36 of the 40 bytes available for TCP options.
- **draft-claise-green-capability-discovery-00** (new-draft, score 3, adjacent_watchlist) [none]: [Discovering the Power State Capabilities of Components](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG module that augments the system
   capabilities model of RFC 9196 to allow a network element to
   advertise, per hardware Component, the set of Power States that the
   Component supports together with a static characterization of each
   such state: the nominal Power the Component draws in that state.

   This capability model complements the operational Power and Energy
   data model defined in the GREEN Power and Energy YANG module, which
   reports the current Power State and the measured Power of a
   Component, but not which Power States are available or how much Power
   each draws.  It is anchored to the hardware inventory of RFC 8348,
   reuses the Power State identities of the GREEN Power and Energy
   model, and, because it is static, may be provided at implementation
   time as YANG instance data per RFC 9195 so that an Energy Management
   System can learn a platform's Power State capabilities before the
   equipment is deployed or even powered on.
- **draft-das-execution-finality-protocol-layer-00** (new-draft, score 3, agent_identity) [none]: [The Missing Execution-Finality Protocol Layer of the Internet](https://datatracker.ietf.org/doc/draft-das-execution-finality-protocol-layer/) — Internet protocols provide mature mechanisms for transporting,
   encrypting, authenticating, authorizing access to, delegating, and
   recording digital information.  These mechanisms remain essential.

   A separate question becomes increasingly important as AI agents,
   autonomous services, programmable networks, cloud workloads, payment
   systems, and cyber-physical systems generate consequential operations
   at machine speed:
- **draft-das-ntn-rf-execution-finality-00** (new-draft, score 3, core_identity) [none]: [RF Enable Is Not Transmit Authority: Finality for LEO/NTN and Inter-Satellite Control](https://datatracker.ietf.org/doc/draft-das-ntn-rf-execution-finality/) — A LEO constellation computer can compute a transmit burst, a beam
   command, an inter-satellite forward, or a user-terminal PA enable
   faster than any ground reviewer can see it.  Today those acts become
   RF because the scheduler selected them, the command link
   authenticated, or the flight process had the radio device open.
   Authentication of TT&C, 3GPP NTN registration, and operator
   allowlists decide who may talk to the vehicle.  They do not decide
   whether this burst, on this beam, to this next hop, over this
   territory, in this mission epoch, may leave the aperture.

   Radiation is not reversible.  An ISL hop is not a log line.  A
   phased-array user terminal that is already pointed is one register
   write away from radiating.  If the enable line trusts the last ground
   "go," a stale, substituted, or autonomy-generated command becomes
   sky-facing consequence.

   This document specifies a radio-side execution-finality profile for
   NTN and mega-constellation control.  A proposed RF, ISL, beam,
   gateway, or payload act remains a Candidate Act. A Protected
   Enforcement Domain binds vehicle, beam, frequency class, duration,
   next hop, overflight or jurisdiction epoch, and intended sink, then
   issues scoped non-bearer authority.  The Finality Sink sits at the PA
   enable, ISL switch, beam driver, feeder gateway, or UT transmit path
   and verifies that authority immediately before energy leaves the
   system.  RF enable is not transmit authority.
- **draft-dikshit-nmop-telemetry-identifier-scoping-00** (new-draft, score 3, core_identity) [none]: [Scoping and Comparability Requirements for Exported Network Telemetry Identifiers](https://datatracker.ietf.org/doc/draft-dikshit-nmop-telemetry-identifier-scoping/) — Several documents currently in progress across multiple IETF
   working groups define identifiers that are exported from a network
   element and consumed by a remote collector, controller, or
   receiver: a flow identifier, a path segment identifier, a per-peer
   or per-Route-Distinguisher counter, and a period or sequence
   number are examples already found in active work. In each case
   examined in this document, the identifier is defined without a
   stated scope of uniqueness, so the receiver cannot determine, from
   the exported value alone, whether two records observed at
   different times or from different sources describe the same
   object. This document catalogs six such instances found
   independently across five working groups, defines a short
   vocabulary for stating an identifier's scope of uniqueness, and
   sets out requirements for documents that define exported telemetry
   identifiers going forward.
- **draft-dinuzzo-best-protocol-01** (new-draft, score 3, adjacent_watchlist) [none]: [BEST: The Behavioral State Protocol](https://datatracker.ietf.org/doc/draft-dinuzzo-best-protocol/) — The Behavioral State Protocol (BEST) defines a discovery-first,
   behaviour-oriented interaction surface for domain services: the
   commands a service accepts, the events it publishes, and optionally
   the queries it answers and the multi-step recipes (workflows) it
   publishes.  Services self-describe through a manifest at the well-
   known URI "/.well-known/best"; messages use a conformant profile of
   the CloudEvents 1.0 envelope described by JSON Schema.  BEST
   deliberately specifies only the interaction surface -- never a
   service's internal architecture, storage, or execution model --
   allowing independent implementations across any runtime, language, or
   transport to interoperate without bespoke integration.
- **draft-eastlake-dnsop-rfc2930bis-tkey-06** (new-draft, score 3, core_identity) [none]: [Secret Key Agreement for DNS: The TKEY Resource Record](https://datatracker.ietf.org/doc/draft-eastlake-dnsop-rfc2930bis-tkey/) — RFC 8945 provides efficient authentication of Domain Name System
   (DNS) protocol messages using shared secret keys and the Transaction
   Signature (TSIG) resource record (RR).  However, it provides no
   mechanism for setting up such keys other than by configuration.  This
   document specifies the Transaction Key (TKEY) RR that can be used to
   establish shared secret keys between a DNS resolver and server.  This
   document obsoletes RFC 2930.
- **draft-geng-sidrops-aspa-analysis-05** (new-draft, score 3, authorization) [none]: [An Analysis of ASPA-based AS_PATH Verification](https://datatracker.ietf.org/doc/draft-geng-sidrops-aspa-analysis/) — Autonomous System Provider Authorization (ASPA) is very helpful in
   detecting and mitigating route leaks (valley-free violations) and a
   majority of forged-origin hijacks.  This document does an analysis on
   ASPA-based AS_PATH verification to help people understand its
   strengths and deficiencies, and some potential directions of
   enhancing ASPA are provided.
- **draft-hko-openpgp-identifiers-for-legacy-devices-03** (new-draft, score 3, core_identity) [none]: [OpenPGP key identifiers for legacy hardware devices](https://datatracker.ietf.org/doc/draft-hko-openpgp-identifiers-for-legacy-devices/) — This document describes an approach for storing a fingerprint-based
   identifier for an OpenPGP key packet on a hardware security device
   that has a size-constrained identifier field.
- **draft-ietf-acme-profiles-02** (new-draft, score 3, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Profiles Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/) — This document defines how an ACME Server may offer a selection of
   different certificate profiles to ACME Clients, and how those clients
   may indicate which profile they want.
- **draft-ietf-asdf-sdf-protocol-mapping-11** (new-draft, score 3, adjacent_watchlist) [asdf]: [SDF Protocol Mapping](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-protocol-mapping/) — This document defines protocol mapping extensions for the Semantic
   Definition Format (SDF) to enable mapping of protocol-agnostic SDF
   affordances to protocol-specific operations.  The protocol mapping
   mechanism allows SDF models to specify how properties, actions, and
   events should be accessed using a specific protocol.  This document
   defines protocol mappings for Bluetooth Low Energy and Zigbee, and
   the mechanism can be extended to other protocols such as HTTP and
   CoAP.  This document also describes a method to extend SCIM with an
   SDF model mapping.
- **draft-ietf-dkim-dkim2-spec-06** (new-draft, score 3, adjacent_watchlist) [dkim]: [DomainKeys Identified Mail Signatures v2 (DKIM2)](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-spec/) — DomainKeys Identified Mail v2 (DKIM2) permits a person, role, or
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
- **draft-ietf-idr-sr-policy-seglist-id-14** (new-draft, score 3, core_identity) [idr]: [BGP SR Policy Extensions for Segment List Identifier](https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-seglist-id/) — Segment Routing (SR) is a source routing paradigm that explicitly
   indicates the forwarding path for packets at the ingress node.  An SR
   Policy is a set of candidate paths, each consisting of one or more
   segment lists.  This document defines extensions to BGP SR Policy to
   specify the identifier of a segment list.
- **draft-ietf-ippm-alt-mark-yang-06** (new-draft, score 3, adjacent_watchlist) [ippm]: [A YANG Data Model for the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-yang/) — Alternate-Marking Method is a technique used to perform packet loss,
   delay, and jitter measurements on in-flight packets.  This document
   defines a YANG data model for the Alternate-Marking Method.
- **draft-ietf-ippm-on-path-telemetry-yang-06** (new-draft, score 3, adjacent_watchlist) [ippm]: [On-Path Telemetry YANG Data Model](https://datatracker.ietf.org/doc/draft-ietf-ippm-on-path-telemetry-yang/) — This document proposes a YANG data model for monitoring On-Path
   network performance information to be published in YANG
   notifications.  The Alternate-Marking Method and In-situ Operations,
   Administration, and Maintenance (IOAM) are the On-Path hybrid
   measurement methods considered in this document.
- **draft-ietf-ivy-network-inventory-topology-10** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Network Data Model for Inventory Topology Mapping](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-topology/) — This document defines a YANG data model that extends the network
   topology data model (RFC 8345) to map network topologies with
   inventories.  The data model introduces the "inventory-topology"
   network type and augmentations for physical entity mappings and
   capabilities, which may be used by any overlay network topology for
   service provisioning validation, network maintenance, and capacity
   planning.
- **draft-ietf-lamps-pq-composite-kem-20** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/) — This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.
- **draft-ietf-masque-connect-udp-listen-16** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Bound UDP in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-listen/) — The mechanism defined in "Proxying UDP in HTTP" (RFC 9298) only
   allows each UDP proxying request to transmit to a specific host and
   port.  This is well suited for UDP client-server protocols such as
   HTTP/3, but is not sufficient for some UDP peer-to-peer protocols
   like WebRTC.  This document defines an extension to that mechanism
   that enables such use cases.
- **draft-ietf-mpls-stamp-pw-12** (new-draft, score 3, core_identity) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document specifies encapsulations for the Simple Two-Way Active
   Measurement Protocol (STAMP), defined in RFC 8762, and its optional
   extensions, defined in RFC 8972, in MPLS networks.  It specifies the
   encapsulation of STAMP test packets for point-to-point Label Switched
   Paths (LSPs) and point-to-point single-segment Pseudowires (PWs),
   with or without an IP/UDP header, so that the test packets experience
   the same forwarding and Equal-Cost Multi-Path (ECMP) behavior as the
   data traffic being measured.  In addition, two new MPLS Generic
   Associated Channel (G-ACh) types are defined.

   This document updates RFC 8972 by updating the STAMP Session
   Identifier for LSPs and PWs.
- **draft-ietf-opsawg-ipfix-path-segment-05** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 paths identification.
- **draft-ietf-pim-evpn-multicast-yang-06** (new-draft, score 3, adjacent_watchlist) [pim]: [Yang Data Model for EVPN multicast](https://datatracker.ietf.org/doc/draft-ietf-pim-evpn-multicast-yang/) — This document describes a YANG data model for EVPN multicast services.
The model is agnostic of the underlay as well as RFC 9251. This
document mainly focuses on EVPN instance framework.
- **draft-ietf-sidrops-aspa-verification-28** (new-draft, score 3, authorization) [sidrops]: [BGP AS_PATH Verification Based on Autonomous System Provider Authorization (ASPA) Objects](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) — This document describes procedures that make use of Autonomous System
   Provider Authorization (ASPA) objects in the Resource Public Key
   Infrastructure (RPKI) to verify the Border Gateway Protocol (BGP)
   AS_PATH attribute of advertised routes.  This AS_PATH verification
   enhances routing security by adding means to detect and mitigate
   route leaks and AS_PATH manipulations.
- **draft-ietf-tcpm-tcp-ao-algs-07** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-ietf-uta-tls13-iot-profile-24** (new-draft, score 3, adjacent_watchlist) [uta]: [TLS/DTLS 1.3 Profiles for the Internet of Things](https://datatracker.ietf.org/doc/draft-ietf-uta-tls13-iot-profile/) — RFC 7925 offers guidance to developers on using TLS/DTLS 1.2 for
   Internet of Things (IoT) devices with resource constraints.  This
   document is a companion to RFC 7925, defining TLS/DTLS 1.3 profiles
   for IoT devices.  Additionally, it updates RFC 7925 with respect to
   the X.509 certificate profile and ciphersuite requirements.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/thomas-fossati/draft-tls13-iot.
- **draft-intra-handshake-fail-16** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake (aka Early) Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
   (https://www.cve.org/CVERecord?id=CVE-2026-33697) and EUVD-2026-16488
   (https://euvd.enisa.europa.eu/enisa/EUVD-2026-16488), which is
   substantial technical evidence of how *intra*-handshake attestation
   fails in practice, even _without physical access_. Moreover, since
   continuous attestation is generally required, *intra*-handshake
   attestation adds *unnecessary complexity*. The results are backed by
   the research [Intra-handshake.fail] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility, and have been
   acknowledged by the relevant stakeholders.
- **draft-irtf-cfrg-signature-key-blinding-11** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Key Blinding for Signature Schemes](https://datatracker.ietf.org/doc/draft-irtf-cfrg-signature-key-blinding/) — This document describes extensions to existing digital signature
   schemes for key blinding.  The core property of signing with key
   blinding is that a blinded public key and all signatures produced
   using the blinded key pair are independent of the unblinded key pair.
   Moreover, signatures produced using blinded key pairs are
   indistinguishable from signatures produced using unblinded key pairs.
   This functionality has a variety of applications, including Tor onion
   services and privacy-preserving airdrop for bootstrapping
   cryptocurrency systems.
- **draft-irtf-t2trg-taxonomy-manufacturer-anchors-21** (new-draft, score 3, adjacent_watchlist) [t2trg]: [A Taxonomy of operational security considerations for manufacturer installed keys and Trust Anchors](https://datatracker.ietf.org/doc/draft-irtf-t2trg-taxonomy-manufacturer-anchors/) — This document provides a taxonomy of methods used by manufacturers of
   silicon and devices to secure private keys and public trust anchors.
   This deals with two related activities: how trust anchors and private
   keys are installed into devices during manufacturing, and how the
   related manufacturer held private keys are secured against
   disclosure.

   This document does not evaluate the different mechanisms, but rather
   just serves to name them in a consistent manner in order to aid in
   communication.


   // This document is a product of the Internet Research Task Force
   // (IRTF).  The IRTF publishes the results of Internet-related
   // research and development activities.  These results might not be
   // suitable for deployment.
- **draft-juwan-ars-00** (new-draft, score 3, core_identity) [none]: [ARS-1 -- Generic Archival Reference System](https://datatracker.ietf.org/doc/draft-juwan-ars/) — ARS-1 defines a deterministic, human-oriented, cryptographically
   derived reference protocol for assigning stable public References to
   durable digital entities.  Typical references look like NX-174932,
   CJ3-106, MR-X4928, or KX4-7B19Q2.

   ARS-1 defines cryptographic identity, deterministic derivation,
   namespace management, canonical serialization, variable-length
   encoding, checksum, optional hardware input, optional digital
   signature, cryptographic agility, versioning, portability, reference
   resolution, reference reproduction, and cryptographic migration.

   The core interoperability property is: identical canonical inputs,
   identical applicable cryptographic Profile, identical Reference Key
   material, and identical Hardware Profile output MUST produce exactly
   the same canonical Reference in every conforming implementation.

   ARS-1 is designed so that changes in cryptographic algorithms,
   security parameters, signature schemes, or hardware mechanisms can be
   introduced through versioned Profiles without requiring the
   reassignment of historical References.
- **draft-kushwaha-scim-tenant-resource-00** (new-draft, score 3, core_identity) [none]: [SCIM Extension for Tenant-Aware Identity Provisioning](https://datatracker.ietf.org/doc/draft-kushwaha-scim-tenant-resource/) — This document defines a System for Cross-domain Identity Management
   (SCIM) extension for tenant-aware identity provisioning.  The
   extension introduces a "Tenant" resource type, tenant-membership
   extensions for the "User" and "Group" resources, a lifecycle state
   machine for tenants and memberships, tenant-scoped uniqueness
   discovery, a normative tenant-context resolution rule built around
   the highest-precedence authenticated indicator together with a stated
   tenant-binding invariant, concurrency requirements for membership
   mutation, tenant-aware filtering, and an OPTIONAL region-aware
   metadata profile.  The extension is backward compatible with SCIM 2.0
   and is intended for multi-tenant Software as a Service (SaaS), cloud
   identity, business-to-business identity, identity governance, and
   multi-region identity deployments.  Scoped role and entitlement
   bindings are delegated to the SCIM Roles and Entitlements and
   RoleAssignment work rather than redefined here.
- **draft-li-idr-ipv6-bgp-identifier-01** (new-draft, score 3, core_identity) [none]: [BGP Capability for IPv6 BGP Identifier](https://datatracker.ietf.org/doc/draft-li-idr-ipv6-bgp-identifier/) — This document defines a new BGP Capability that enables an IPv6 BGP
   Speaker to use its global unicast IPv6 address as its BGP Identifier.
   This mechanism simplifies configuration in IPv6-only networks by
   leveraging the inherent uniqueness of IPv6 addresses, while
   maintaining full backward compatibility with existing BGP
   implementations.
- **draft-luan-cats-catpts-01** (new-draft, score 3, adjacent_watchlist) [none]: [A Timescale-Aware Framework for Compute-Aware Task Placement and Traffic Steering in Heterogeneous Geo-Distributed Computing Networks](https://datatracker.ietf.org/doc/draft-luan-cats-catpts/) — Geographically distributed compute-intensive services require
   coordinated selection of execution sites and wide-area traffic paths.
   Placement changes slowly because service relocation may involve model
   loading, state migration, or execution-environment reconfiguration,
   while traffic splitting can be changed more frequently.

   This document evolves the CATPTS framework by defining a timescale-
   aware control architecture for source-compute-destination services.
   A slow-timescale placement function uses abstracted multipath and
   failure information to select a compute site.  A fast-timescale
   traffic function then refines the input and output traffic
   allocations across candidate paths while holding placement fixed.

   The framework also introduces scenario-based service-loss estimation
   and an optional Conditional Value at Risk (CVaR) policy for limiting
   tail loss caused by compute-site or network-link failures.  This
   document specifies architectural principles, information
   requirements, workflows, and operational considerations; it does not
   specify protocol extensions or a mandatory optimization algorithm.
- **draft-macgowan-dosd-02** (new-draft, score 3, trust_infrastructure) [none]: [Domain Operational Standing Declaration (DOSD) Protocol](https://datatracker.ietf.org/doc/draft-macgowan-dosd/) — This document describes the Domain Operational Standing Declaration
   (DOSD) protocol, a voluntary DNS-based mechanism by which domain
   owners may publish operational declarations, stewardship status,
   provenance references, documentation indexes, and mediation routing
   information in a machine-discoverable way.  DOSD uses DNS TXT
   records for discovery, a well-known JSON file for canonical node
   metadata, and an optional well-known documentation index for
   discovering protocol drafts, supporting specifications,
   implementation documents, and historical records.  This revision
   adds three optional operational profiles: a Distress Notice profile
   (DOSD-DN) for time-bounded duress signaling, an Emergency Contact
   object and De-escalation profile (DOSD-EC) for witness-mediated
   resolution of an active distress signal, and a Co-signature anchor
   state (pending_cosign) for instruments requiring two witnesses
   before publication.  DOSD does not determine legal validity,
   jurisdiction, sovereignty, standing, or dispute outcomes.  It
   provides discoverable publication infrastructure only.
- **draft-shen-sidrops-region-verification-05** (new-draft, score 3, authorization) [none]: [Verification of Routes Using Region Authorization](https://datatracker.ietf.org/doc/draft-shen-sidrops-region-verification/) — BGP routing security is a critical issue affecting the stability and
   reliability of Internet services.  Existing mechanisms, including
   Route Origin Authorization (ROA) and Autonomous System Provider
   Authorization (ASPA), effectively mitigate route origin hijacking,
   path hijacking, and route leaks in general scenarios.  However, in
   real-world deployments, large Internet Service Providers (ISPs)
   managing multiple Autonomous Systems (ASes) remain vulnerable.
   Attacking networks can exploit carefully crafted routes to bypass ROA
   and ASPA validations, causing traffic hijacking within or between
   large ISPs.

   This document defines a region-based authorization and verification
   framework for multi-AS ISPs to prevent intra-ISP and inter-ISP
   traffic hijacking.
- **draft-yl-cats-data-model-09** (new-draft, score 3, adjacent_watchlist) [cats]: [Data Model for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-yl-cats-data-model/) — This document defines a YANG data model for the management of
   Computing-Aware Traffic Steering (CATS) systems.
- **draft-zhangb-cats-service-metric-registry-entries-00** (new-draft, score 3, adjacent_watchlist) [none]: [CATS Computing Service Metric Registry Entries](https://datatracker.ietf.org/doc/draft-zhangb-cats-service-metric-registry-entries/) — This document defines the initial set of registry entries for
   Computing Service Metrics used in Computing-Aware Traffic Steering
   (CATS).  These metrics, including Global Available Slots (GAS),
   Computing Time, Cost, Reputation, Security Label, and Capability,
   provide service-oriented abstractions that complement the existing
   CATS Level 0/Level 1/Level 2 normalized metric framework defined in
   [I-D.ietf-cats-metric-definition].

   This document follows the registry format and separation pattern
   established by [RFC8911] and [RFC8912], populating a new IANA
   registry titled "CATS Computing Service Metrics" with formal entries
   for each metric defined in [I-D.zhangb-cats-service-metrics-op].
- **draft-aegisfs-secdispatch-rats-00** (new-draft, score 2, ignored_after_review) [none]: [AegisFS: AI-Driven Programmable Secure File Runtime and Intelligent Workspace Architecture with Octal OpCode Processing and Policy-Driven Language Architecture](https://datatracker.ietf.org/doc/draft-aegisfs-secdispatch-rats/) — This document specifies AegisFS, a programmable secure file and
   folder runtime that transforms ordinary filesystem objects into
   intelligent, policy-driven, state-aware, execution-aware, and
   behavior-aware security objects.

   This draft introduces two novel technical contributions:
- **draft-beeram-teas-rsvp-srv6-00** (new-draft, score 2, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SRv6 Forwarding Plane Using End.X Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-teas-rsvp-srv6/) — RFC 8577 defines mechanisms to signal RSVP-TE tunnels on a shared
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
- **draft-das-ai-native-6g-execution-finality-01** (new-draft, score 2, core_identity) [none]: [Execution-Finality for AI-Native 5G/6G and O-RAN](https://datatracker.ietf.org/doc/draft-das-ai-native-6g-execution-finality/) — In programmable and AI-assisted mobile networks, successful
   authentication of a network function or AI controller does not
   establish authority for every routing, signaling, session, resource-
   allocation, sensing, or subscriber-specific consequence that the
   function can generate.

   This document defines an informational execution-finality profile for
   AI-native 5G, 5G-Advanced, IMT-2030/6G, O-RAN, and AI-RAN
   environments.  A proposed network operation is represented as a
   Network Candidate Act and remains in a Non-Effective State while a
   Protected Enforcement Domain validates act-specific predicates.
   Protected validation evidence is committed before, or atomically
   with, release of scoped non-bearer finality authority.  A Network
   Finality Sink at the enforcement boundary independently verifies that
   authority immediately before live network state changes.

   The governing rule is that network authentication is not network
   finality, and computation is not authority.  This revision also
   defines a JSON interoperability profile for Candidate Acts,
   validation decisions, scoped authority, and sink verification.
- **draft-dogru-cedulon-streaming-00** (new-draft, score 2, ignored_after_review) [none]: [Cedulon Streaming Reconciliation: Continuous Completeness for Agent Spend](https://datatracker.ietf.org/doc/draft-dogru-cedulon-streaming/) — Cedulon defines a batch reconciliation audit: given a window of spend
   receipts, epoch checkpoints, and an authenticated rail extract, a
   verifier proves completeness after the fact.  Agent fleets that spend
   continuously need the same property as a live signal: a conscience
   that runs beside the payments rather than behind them.  This document
   proposes a streaming profile: short half-open micro-epochs, an
   incremental checkpoint cadence, a watermark that separates
   provisional from final findings, and rules for late-arriving
   settlements.  The goal is that "the books are balanced" becomes a
   continuously maintained, externally checkable state instead of a
   periodic report.  This is an extension proposal to the Cedulon core
   document; its normative language is provisional and the companion
   implementation does not implement it yet.
- **draft-fu-memdns-pivoting-01** (new-draft, score 2, ignored_after_review) [none]: [DNS for Automated Pivoting in Big Memory Systems](https://datatracker.ietf.org/doc/draft-fu-memdns-pivoting/) — Heterogeneous memory networks (CXL pools, HBM/DDR/SRAM hierarchies,
   processing-in-memory arrays) form a big memory system, which exposes
   fragmented addressing to ML inference runtimes.  This document
   describes Memory DNS (MemDNS), a semantic-addressing framework that
   applies DNS principles -- domain names, hierarchical delegation,
   caching, TTL, and authoritative records -- to tensor data placement
   in Big Memory Systems (BMS), deployed as limited domains (RFC 8799).
   The focus is "automated pivoting": the resolution and control
   machinery that automatically switches data access paths (replica
   selection), migrates data across media (placement pivoting), and
   recovers from faults (failover pivoting), driven by closed-form
   decision models (Appendix A; key logic pseudo-code in Appendix C)
   instead of ad-hoc thresholds.  The document specifies record
   semantics, resolution flow, cache/TTL behavior, delegation, pivot
   decision models, and protocol considerations, together with a
   reference implementation summary.
- **draft-ietf-fann-problem-statement-00** (new-draft, score 2, ai_infrastructure) [fann]: [Fast Network Notifications Problem Statement](https://datatracker.ietf.org/doc/draft-ietf-fann-problem-statement/) — Many network applications, ranging from Artificial Intelligence (AI)
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
- **draft-kavian-aep-claims-01** (new-draft, score 2, ignored_after_review) [none]: [AEP Claim Values](https://datatracker.ietf.org/doc/draft-kavian-aep-claims/) — This document defines a claim-value catalog for the Agent Enrollment
   Protocol (AEP).  It specifies stable claim names and forward-
   compatible JSON value shapes that Agents can submit during enrollment
   when requested by a Service Inspect document.
- **draft-linuxgemini-otpauth-uri-03** (new-draft, score 2, ignored_after_review) [none]: [One-Time Password (OTP) Credential Provisioning URI Format: otpauth](https://datatracker.ietf.org/doc/draft-linuxgemini-otpauth-uri/) — This document specify the One-Time Password (OTP) Credential
   Provisioning otpauth URI format, utilized by TOTP (Time-Based One-
   Time Password Algorithm) and HOTP (An HMAC-Based One-Time Password
   Algorithm) based authenticators.
- **draft-vmhosting-fi-nameservers-00** (new-draft, score 2, ignored_after_review) [none]: [Name Server Provider and Domain Name Registrar Operational Framework](https://datatracker.ietf.org/doc/draft-vmhosting-fi-nameservers/) — This document describes an operational framework for service
   providers that operate authoritative Domain Name System (DNS)
   services, domain name registration services, or both.  It covers DNS
   zone provisioning, authoritative name server operation, delegation
   management, service availability, DNSSEC, domain registration
   lifecycle operations, access control, monitoring, incident response,
   abuse handling, and privacy considerations.

   This document does not define a new DNS protocol, registry protocol,
   or domain registration policy.  It describes operational practices
   that can be applied by providers using existing DNS and domain
   registration protocols and interfaces.

## Ignored after review

- **draft-acosta-deepspace-celestial-bodies-registry-01** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Registry for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document proposes the creation of a formalized registry for
   celestial bodies within the Internet Assigned Numbers Authority
   (IANA) to support routing and address allocation in deep space
   networks.  As internet architecture expands to interplanetary scales,
   routing protocols rely on hierarchical aggregation based on planetary
   and celestial entities.  However, the IETF currently lacks a
   standardized taxonomical framework or mapping mechanism to uniquely
   identify these entities.  This document outlines the requirements for
   establishing such a registry, suggests leveraging definitions from
   the International Astronomical Union (IAU), and discusses the
   integration of these identifiers into the deep space routing
   architecture.
- **draft-anjum-nmop-anomaly-detection-evaluation-01** (new-draft, score 0, ignored_after_review) [none]: [Evaluation Methodology for Machine-Learning-Based Network Anomaly Detection](https://datatracker.ietf.org/doc/draft-anjum-nmop-anomaly-detection-evaluation/) — The Network Management Operations (NMOP) working group has adopted
   documents describing an architecture, an operational lifecycle, and a
   semantics for network anomaly detection.  Those documents direct
   implementers to minimize false positives and false negatives, but do
   not define how the accuracy of an anomaly detection implementation is
   to be measured, compared, or tracked over time.  This document
   describes an evaluation methodology for machine-learning-based
   anomaly detection systems operating on network and infrastructure
   telemetry: the metrics to report and their known failure modes, a
   benchmarking procedure based on controlled fault injection and
   replay, and the properties a benchmark dataset needs in order to
   support reproducible, comparable evaluation.  The methodology is
   informational and complements the adopted NMOP anomaly-detection
   documents.
- **draft-bormann-cbor-notable-tags-17** (new-draft, score 0, ignored_after_review) [none]: [Notable CBOR Tags](https://datatracker.ietf.org/doc/draft-bormann-cbor-notable-tags/) — The Concise Binary Object Representation (CBOR, RFC 8949) is a data
   format whose design goals include the possibility of extremely small
   code size, fairly small message size, and extensibility without the
   need for version negotiation.

   In CBOR, one point of extensibility is the definition of CBOR tags.
   RFC 8949's original edition, RFC 7049, defined a basic set of 16 tags
   as well as a registry that can be used to contribute additional tag
   definitions [IANA.cbor-tags].  Since RFC 7049 was published, at the
   time of writing some 250 definitions of tags and ranges of tags have
   been added to that registry.

   The present document provides a roadmap to a large subset of these
   tag definitions.  Where applicable, it points to an IETF standards or
   standard development document that specifies the tag.  Where no such
   document exists, the intention is to collect specification
   information from the sources of the registrations.  After some more
   development, the present document is intended to be useful as a
   reference document for the IANA registrations of the CBOR tags the
   definitions of which have been collected.
- **draft-bortzmeyer-dnsop-poisonlicious-06** (new-draft, score 0, ignored_after_review) [none]: [Synchronizing caches of DNS resolvers](https://datatracker.ietf.org/doc/draft-bortzmeyer-dnsop-poisonlicious/) — Networks of cooperating and mutually trusting DNS resolvers could
   benefit from cache sharing, where one resolver would distribute the
   result of a resolution to other resolvers.  This document
   standardizes a protocol to do so.
- **draft-chen-spring-srv6-compressed-bsid-insertion-03** (new-draft, score 0, ignored_after_review) [none]: [SRv6 NET-PGM extension: Compressed BSID Insertion](https://datatracker.ietf.org/doc/draft-chen-spring-srv6-compressed-bsid-insertion/) — The End.B6.Insert and End.B6.Insert.Red SHOULD support the NEXT-CSID
   flavor either individually or in combinations.  This document defines
   the SRH processing of the End.B6.Insert and End.B6.Insert.Red with
   NEXT-CSID.
- **draft-denis-ipcrypt-14** (new-draft, score 0, ignored_after_review) [none]: [Methods for IP Address Encryption and Obfuscation](https://datatracker.ietf.org/doc/draft-denis-ipcrypt/) — This document specifies secure, efficient methods for Internet
   Protocol (IP) address encryption and obfuscation in privacy-
   preserving storage, logging, and analytics.  Unlike truncation, which
   destroys data irreversibly, these methods are reversible with the
   encryption key while providing strong privacy guarantees.

   Four modes are defined: ipcrypt-deterministic (format-preserving, IP-
   address output), ipcrypt-pfx (prefix-preserving, native address
   size), ipcrypt-nd and ipcrypt-ndx (non-deterministic with random
   tweaks).  All support high-performance processing at network speeds
   and produce interoperable results across implementations.
- **draft-deshpande-secevent-http-multi-set-push-03** (new-draft, score 0, ignored_after_review) [sec]: [Push-Based Delivery For Multiple Security Event Tokens (SET) Using HTTP](https://datatracker.ietf.org/doc/draft-deshpande-secevent-http-multi-set-push/) — This specification defines how multiple Security Event Tokens (SETs)
   can be delivered to an intended recipient using HTTP POST over TLS.
   The SETs are transmitted in the body of an HTTP POST request to an
   endpoint operated by the recipient, and the recipient indicates
   successful or failed transmission via the HTTP response.
- **draft-dikshit-grow-bmp-rd-scoped-rib-stats-01** (new-draft, score 0, ignored_after_review) [none]: [Route-Distinguisher-Scoped BMP RIB Statistics](https://datatracker.ietf.org/doc/draft-dikshit-grow-bmp-rd-scoped-rib-stats/) — [RFC7854] defines the BGP Monitoring Protocol (BMP) and its
   Statistics Report message.  [I-D.ietf-grow-bmp-bgp-rib-stats]
   (published as [RFC9972]) extended that message with a set of
   advanced, per-AFI/SAFI BGP RIB statistics types.  Several ongoing
   individual contributions independently define additional per-
   address-family, per-instance, or per-Route-Distinguisher (RD)
   statistics on top of that base (for example, EVPN-specific RIB
   statistics and VRF Loc-RIB monitoring enhancements), each proposing
   its own ad hoc Stat Data encoding.

   This document defines a single, address-family-agnostic Stat Data
   container -- the "RD-Scoped Statistics" format -- for BMP
   statistics that are naturally scoped below the per-AFI/SAFI level,
   to a specific Route Distinguisher (VRF instance, EVPN Instance,
   MVPN instance, or equivalent).  Address-family-specific documents,
   such as EVPN-specific BMP RIB statistics, are expected to become
   thin "profiles" of this container rather than defining their own
   wire format, reducing duplication and Stat Type registry
   fragmentation across the GROW working group's BMP statistics work.
- **draft-dutta-gcmf-01** (new-draft, score 0, ignored_after_review) [none]: [General-Purpose Compression via Mathematical Functions (GCMF)](https://datatracker.ietf.org/doc/draft-dutta-gcmf/) — This document specifies General-Purpose Compression via Mathematical
   Functions (GCMF), a lossless compression format that represents
   sequences of data using mathematical functions and associated
   parameters.

   GCMF attempts to represent a sequence using a compact mathematical
   representation rather than storing every value explicitly.  This
   document defines the GCMF data format, function types, encoding
   rules, decoding procedure, and interoperability requirements.
- **draft-eastlake-dnsop-expressing-qos-requirements-09** (new-draft, score 0, ignored_after_review) [none]: [Expressing Quality of Service Requirements (QoS) in Domain Name System (DNS) Queries](https://datatracker.ietf.org/doc/draft-eastlake-dnsop-expressing-qos-requirements/) — A method of encoding quality of communication service (QoS)
   requirements in a Domain Name System (DNS) query is specified through
   inclusion of the requirements in one or more labels of the name being
   queried.  This enables DNS responses including addressing and packet
   labeling information that is dependent on such requirements without
   changes in the format of DNS protocol messages or DNS application
   program interfaces (APIs).
- **draft-eastlake-dnsop-rrtype-srv6-10** (new-draft, score 0, ignored_after_review) [none]: [The IPv6 Segment Routing (SRv6) Domain Name System (DNS) Resource Record](https://datatracker.ietf.org/doc/draft-eastlake-dnsop-rrtype-srv6/) — A Domain Name System (DNS) Resource Record (RR) Type is specified for
   storing IPv6 Segment Routing (SRv6) Information in the DNS.
- **draft-faltstrom-unicode-18** (new-draft, score 0, ignored_after_review): [draft-faltstrom-unicode-18-02](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/)
- **draft-faltstrom-unicode-18-02** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Domain Names for Applications 2008 (IDNA2008) and Unicode 18.0.0](https://datatracker.ietf.org/doc/draft-faltstrom-unicode-18/) — This document describes the changes between Unicode 12.0.0 and
   Unicode 18.0.0 in the context of IDNA2008.  Some additions and
   changes have been made in the Unicode Standard that affect the values
   produced by the algorithm IDNA2008 specifies.  The review assigns the
   derived property value "UNDER REVIEW" to certain code points.  This
   is added as exceptions to the algorithm for IDNA2008 that allows
   adding exceptions to the algorithm for backward compatibility
   exceptions.  This document provides the necessary tables to IANA to
   make its database consistent with Unicode 18.0.0.

   This version of this document is based on pre-release data.  Unicode
   18.0.0 has not been released, and every figure here that concerns it
   is provisional and must be regenerated against the released files.
   See the note at the top of this document.

   All values in this document are computed from the Unicode Character
   Database files listed in Appendix H, by applying the algorithm in RFC
   5892 Section 3 directly to those files.  No derived property table
   produced by anyone else is used as input.  Section 3 describes the
   derivation and Appendix G compares the result with the derivation
   published by the Unicode Consortium.
- **draft-fu-sidrops-enhanced-slurm-filter-06** (new-draft, score 0, ignored_after_review) [none]: [Filtering Out RPKI Data by Type based on Enhanced SLURM Filters](https://datatracker.ietf.org/doc/draft-fu-sidrops-enhanced-slurm-filter/) — Simplified Local Internet Number Resource Management with the RPKI
   (SLURM) helps operators create a local view of the global RPKI by
   generating sets of filters and assertions.  This document proposes to
   filter out RPKI data by type based on enhanced SLURM filters.  Only
   the RPKI data types that the network or routers are interested in
   will appear in the Relying Party's output.
- **draft-geng-sidrops-rtr-selective-sync-07** (new-draft, score 0, ignored_after_review) [none]: [Selective Synchronization Extension for RPKI-to-Router Protocol](https://datatracker.ietf.org/doc/draft-geng-sidrops-rtr-selective-sync/) — The RPKI-to-Router (RTR) protocol synchronizes all the verified RPKI
   data to routers.  This document proposes to extend the existing RTR
   protocol to support selective data synchronization.  Selective
   synchronization can avoid unnecessary transmissions.  The router can
   receive only the data that it really needs.
- **draft-gong-spring-nd-advertise-srv6-locator-05** (new-draft, score 0, ignored_after_review) [none]: [Advertise SRv6 Locator Information by IPv6 Neighbor Discovery](https://datatracker.ietf.org/doc/draft-gong-spring-nd-advertise-srv6-locator/) — In an SRv6 network, each SRv6 segment endpoint has at least one SRv6
   Locator.  Through the SRv6 locator routes, other SRv6 segment nodes
   can steer traffic to that node.  This document describes a method for
   an SRv6 endpoint (e.g., a host or a customer provider edge (CPE)) to
   advertise its SRv6 locator to a neighboring SRv6-aware router using
   extensions to the IPv6 Neighbor Discovery (ND) protocol.  This
   approach eliminates the need to run a full routing protocol stack on
   simple endpoints, facilitating SRv6 deployment in controlled, trusted
   domains such as data centers and managed access networks.
- **draft-hawkins-x402-dns-discovery-03** (new-draft, score 0, ignored_after_review) [none]: [Discovering x402 Payment Capability via DNS and a Well-Known URI](https://datatracker.ietf.org/doc/draft-hawkins-x402-dns-discovery/) — x402 is an application-level protocol for internet-native payments
   built on the HTTP 402 (Payment Required) status code.  This document
   defines how a domain publishes its x402 payment capability out-of-
   band, so that clients, autonomous agents, and indexers can discover
   it without prior configuration or a central directory.  It specifies
   a JSON capability manifest served at the well-known URI "/.well-
   known/x402" and an optional DNS TXT record at the underscored node
   name "_x402" that points to the manifest.  A consumer resolves a bare
   domain name to verified x402 capability with at most one DNS query
   and one HTTPS GET.
- **draft-he-ippm-ioam-dex-extensions-incorporating-am-05** (new-draft, score 0, ignored_after_review) [none]: [IOAM Direct Exporting (DEX) Option Extensions for Incorporating the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-he-ippm-ioam-dex-extensions-incorporating-am/) — In situ Operations, Administration, and Maintenance (IOAM) is used
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
- **draft-he-ippm-ioam-extensions-incorporating-am-07** (new-draft, score 0, ignored_after_review) [none]: [IOAM Trace Option Extensions for Incorporating the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-he-ippm-ioam-extensions-incorporating-am/) — In situ Operation, Administration, and Maintenance (IOAM) is used for
   recording and collecting operational and telemetry information, which
   leverages IOAM Trace Option to incorporate IOAM data fields into in-
   flight data packets.  The Alternate-Marking method is used to measure
   performance metrics on live traffic, such as packet loss, delay, and
   jitter.  This document extends IOAM Trace Option for incorporating
   the Alternate-Marking method to augment IOAM in performance
   measurement.
- **draft-henlich-imdf-00** (new-draft, score 0, ignored_after_review) [none]: [Internet Month-Name Date Format (IMDF)](https://datatracker.ietf.org/doc/draft-henlich-imdf/) — This document defines the Internet Month-Name Date Format (IMDF), a
   concise date representation for English-language human communication.

   IMDF requires an alphabetic month abbreviation.  This makes the month
   visually distinct from the numeric day and reduces errors caused by
   differing regional date-order conventions.

   The specification primarily defines how IMDF dates are presented.  It
   establishes a preferred output form and permits a limited set of
   familiar English-language variants.  Detailed input handling is
   outside its scope.

   IMDF does not replace ISO 8601 for machine interchange, language-
   neutral communication, chronological sorting, or timestamps.
- **draft-herdes-idr-otc-rs-verification-00** (new-draft, score 0, ignored_after_review) [none]: [Strict Only to Customer (OTC) Verification on Route Server Sessions](https://datatracker.ietf.org/doc/draft-herdes-idr-otc-rs-verification/) — RFC 9234 specifies how an AS receiving a route from a lateral Peer
   can check if route was lekaed, but doesn't specify any checks for
   routes received from Route Server (RS).  This makes quility of
   filtering dependent on whether the RS implements RFC 9234.

   This document updates RFC 9234 by adding complimentary ingress check
   by RS-Client.
- **draft-ietf-avtcore-rtp-avatar-02** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for Avatar Representation Format (ARF) Animation Stream](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-avatar/) — This memo outlines RTP payload formats for the animation stream
   format as defined in the ISO/IEC 23090-39 standard (MPEG-I Avatar
   Representation Format), in the following referred to as ARF.  ARF is
   composed of Avatar Animation Units (AAU) including an AAU header and
   zero or more AAU packets.  The RTP payload header format allows for
   packetization of an AAU unit in an RTP packet payload as well as
   fragmentation of an AAU into multiple RTP packets.
- **draft-ietf-bmwg-sr-bench-meth-08** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR)](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) performance for Segment Routing over IPv6 (SRv6) and MPLS (SR-
   MPLS).
- **draft-ietf-cdni-client-access-control-metadata-05** (new-draft, score 0, ignored_after_review) [cdni]: [CDNI Client Access Control Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-client-access-control-metadata/) — This specification adds to the basic client access control metadata
   in RFC8006, providing content providers and upstream content delivery
   networks (uCDNs) extended capabilities in defining location and time
   window restrictions.  Support is also provided to define required
   Transport Layer Security (TLS) certificates and encryption levels.
   The specification also defines configuration metadata for the Common
   Access Token (CAT), developed jointly by the Streaming Video
   Technology Alliance (SVTA) and Consumer Technology Association Web
   Application Video Ecosystem (CTA-WAVE).
- **draft-ietf-emailcore-as-30** (new-draft, score 0, ignored_after_review) [emailcore]: [Applicability Statement for IETF Core Email Protocols](https://datatracker.ietf.org/doc/draft-ietf-emailcore-as/) — Electronic mail is one of the oldest Internet applications that is
   still in very active use.  While the basic protocols and formats for
   mail transport and message formats have evolved slowly over the
   years, events and thinking in more recent years have supplemented
   those core protocols with additional features and suggestions for
   their use.  This Applicability Statement describes the relationship
   among many of those protocols and provides guidance and makes
   recommendations for the use of features of the core protocols.
- **draft-ietf-idr-bgp-bfd-strict-mode-19** (new-draft, score 0, ignored_after_review) [idr]: [BGP BFD Strict-Mode](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-bfd-strict-mode/) — This document specifies extensions to RFC4271 BGP-4 that enable a BGP
   speaker to negotiate additional Bidirectional Forwarding Detection
   (BFD) extensions using a BGP capability.  This BFD Strict-Mode
   Capability enables a BGP speaker to prevent a BGP session from being
   established until a BFD session is established.  This is referred to
   as BFD "strict-mode".
- **draft-ietf-idr-bgp-ls-sr-policy-path-segment-12** (new-draft, score 0, ignored_after_review) [idr]: [SR Policies Extensions for Path Segment and Bidirectional Path in BGP-LS](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-path-segment/) — This document specifies the way of collecting configuration and
   states of SR policies carrying Path Segment and bidirectional path
   information by using BPG-LS.  Such information can be used by
   external conponents for many use cases such as performance
   measurement, path re-optimization and end-to-end protection.
- **draft-ietf-idr-bgpls-inter-as-topology-ext-39** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extensions for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedure for distributing Border Gateway
   Protocol-Link State (BGP-LS) key parameters for inter-domain links
   between two Autonomous Systems (ASes).  It defines a new type within
   the BGP-LS Network Layer Reachability Information (NLRI) for an
   Inter-AS Link, as well as three new type-length-values (TLVs) for the
   BGP-LS Inter-AS Link descriptor.  These BGP-LS extensions enable
   network controller to retrieve network topology across Inter-AS
   environments.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   inter-AS topology using information provided by the BGP-LS protocol.
- **draft-ietf-idr-ts-flowspec-srv6-policy-17** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  Specifically, it defines
   normative protocol mechanisms for combining FlowSpec NLRIs with
   specific BGP Extended Communities for transport policy steering in
   SR-MPLS and SRv6 networks (Mode 1), and optionally with the BGP
   Prefix-SID Attribute when egress service action execution is required
   in SRv6 networks (Mode 2).
- **draft-ietf-intarea-dhcp-rate-signaling-00** (new-draft, score 0, ignored_after_review) [intarea]: [DHCP Explicit Rate Signaling](https://datatracker.ietf.org/doc/draft-ietf-intarea-dhcp-rate-signaling/) — This document defines new Dynamic Host Configuration Protocol (DHCP)
   options for both DHCPv4 and DHCPv6 to explicitly signal available
   upstream and downstream data rates.  In many broadband access
   networks, Customer Premises Equipment (CPE) and intermediate nodes
   lack visibility into the subscriber's provisioned service tier.  By
   communicating these capacities natively via DHCP, clients, relay
   agents, and snooping switches can dynamically configure localized
   traffic shaping and queuing.  This explicit signaling improves
   overall network performance by reducing the reliance on
   indiscriminate packet dropping and policing at the service edge.
   Additionally, it provides the necessary capacity awareness to enable
   effective Active Queue Management (AQM) and the Low Latency, Low
   Loss, and Scalable Throughput (L4S) architecture.
- **draft-ietf-intarea-ipv6-resolved-gateway-00** (new-draft, score 0, ignored_after_review) [intarea]: [IPv6-Resolved IPv4 Gateway](https://datatracker.ietf.org/doc/draft-ietf-intarea-ipv6-resolved-gateway/) — This document specifies host behavior enabling IPv4 communication for
   dual-stack hosts on IPv6-only segments, without subnets, ARP,
   tunneling, or translation.  Hosts that receive 192.0.0.11/32 as their
   IPv4 default gateway address resolve the next-hop link-layer address
   from the IPv6 neighbor cache rather than via ARP.  IPv4 packets are
   forwarded natively, end-to-end.  The mechanism is incrementally
   deployable alongside unmodified hosts with no changes to DHCPv4
   infrastructure.  This document requests the allocation of
   192.0.0.11/32 in the IANA IPv4 Special-Purpose Address Registry to
   support this mechanism.
- **draft-ietf-intarea-reordering-00** (new-draft, score 0, ignored_after_review) [intarea]: [Proposal for Updates to Guidance on Packet Reordering](https://datatracker.ietf.org/doc/draft-ietf-intarea-reordering/) — Several link technology standards mandate that equipment guarantee
   in-order delivery of layer 2 frames, apparently due to a belief that
   this is required by higher layer protocols.  To meet this requirement
   they implement a "resequencing" operation to restore the original
   packet order.  This can introduce delays that result in net
   degradation of performance.  Modern TCP and QUIC implementations
   support features that significantly improve their tolerance to out-
   of-order delivery.  This draft is intended to provide new information
   for layer 2 technology standards regarding the need to assure in-
   order delivery to support IETF protocols.
- **draft-ietf-ippm-on-path-active-measurements-03** (new-draft, score 0, ignored_after_review) [ippm]: [On-Path Telemetry for Active Performance Measurements](https://datatracker.ietf.org/doc/draft-ietf-ippm-on-path-active-measurements/) — This document describes how to employ active test packets in
   combination with Hybrid Methods to perform On-path Active Performance
   Measurements.  This procedure allows Hop-By-Hop measurements in
   addition to the Edge-To-Edge measurements.
- **draft-ietf-ipsecme-ikev2-prf-plus-02** (new-draft, score 0, ignored_after_review) [ipsecme]: [Use of Variable-Length Output Pseudo-Random Functions (PRFs) in the Internet Key Exchange Protocol Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-prf-plus/) — This document specifies the use of variable-length output Pseudo-
   Random Functions (PRFs) in the Internet Key Exchange Protocol Version
   2 (IKEv2).  Current IKEv2 specification relies on traditional PRFs
   with fixed output length for key derivation and uses iterative
   application of a PRF (called "prf+") in cases when longer output is
   required.  Appearance of PRFs that can output as much bits as
   requested allows to streamline the key derivation functions of IKEv2.

   This document updates RFC 7296 and RFC 7815 for the cases when
   variable-length output Pseudo-Random Functions are used in IKEv2 and
   its extensions.
- **draft-ietf-jsonschema-json-schema-03** (new-draft, score 0, ignored_after_review) [jsonschema]: [JSON Schema](https://datatracker.ietf.org/doc/draft-ietf-jsonschema-json-schema/) — JSON Schema defines the media type "application/schema+json", a JSON-
   based format for describing the structure of JSON data.  A JSON
   Schema may assert constraints on a JSON value, ways to extract
   information from it, and how to interact with it.  The "application/
   schema-instance+json" media type provides additional feature-rich
   integration with "application/schema+json" beyond what can be offered
   for "application/json" documents.
- **draft-ietf-lsr-dynamic-flooding-algorithm-05** (new-draft, score 0, ignored_after_review) [lsr]: [An Algorithm for Computing Dynamic Flooding Topologies](https://datatracker.ietf.org/doc/draft-ietf-lsr-dynamic-flooding-algorithm/) — Link-state routing protocols suffer from excessive flooding in dense
   network topologies.  Dynamic flooding alleviates the problem by
   decoupling the flooding topology from the base topology.  Link-state
   protocol updates are flooded only on the sparse flooding topology
   while data traffic is still forwarded on the base topology.

   This document describes an algorithm to obtain a sparse subgraph from
   a dense graph.  The resulting subgraph has certain desirable
   properties and can be used by a centralized Area Leader to compute a
   flooding topology for dynamic flooding.

   This document discloses the algorithm that the authors have developed
   in order to make it easier for other developers to implement similar
   algorithms.  The authors do not claim that our algorithm is optimal,
   rather, it is a pragmatic effort and the authors expect that further
   research and refinement can improve the results.

   The authors are not currently proposing that this algorithm be
   standardized, nor that the working group use this as a basis for
   further standardization work; however, the authors have no objections
   if the working group chooses to do so.  This document is published as
   an Experimental RFC to gain operational and implementation experience
   with the specified dynamic flooding algorithm.  The intent is to
   assess the suitability of this algorithm for advancement to the
   Standards Track as a Proposed Standard, pending sufficient deployment
   experience and feedback from the community.
- **draft-ietf-manet-inet-gap-analysis-10** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-mpls-frr-ext-00** (new-draft, score 0, ignored_after_review) [mpls]: [Signaling Optimization Objective and Bounded Metrics for MPLS Fast Reroute Backup LSP Tunnels](https://datatracker.ietf.org/doc/draft-ietf-mpls-frr-ext/) — This document introduces RSVP-TE signaling procedures that enable the
   head-end Label Switched Router (LSR) of a local-protection-desiring
   Label Switched Path (LSP) to influence the optimization objective and
   bounded metric constraints used for the path computation of a backup
   LSP tunnel at a Point of Local Repair (PLR).
- **draft-ietf-mpls-mna-ioam-13** (new-draft, score 0, ignored_after_review) [mpls]: [Encapsulation for In Situ Operations, Administration, and Maintenance Data Using MPLS Network Actions](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, collects operational and telemetry information in the
   packet using IOAM-Data-Fields while the packet traverses a path
   between two points in the network.  Several IOAM Option-Types are
   available, for example, Pre-allocated Trace, Proof of Transit (POT),
   Edge-to-Edge (E2E), and Incremental Trace, that can be used to
   collect information for calculating various performance metrics.  RFC
   9326 defines the IOAM Direct Export (IOAM-DEX) Option-Type, which is
   used as a trigger for IOAM data to be directly exported or locally
   aggregated without being pushed into in-flight data packets.

   MPLS Network Actions (MNA) mechanisms indicate actions to be
   performed on any combination of Label Switched Paths, MPLS packets,
   and the node itself, and to transport data needed for these actions.
   This document employs the MNA mechanisms to collect and transport the
   operational state and telemetry information using IOAM-Data-Fields as
   well as IOAM-DEX.
- **draft-ietf-netconf-distributed-notif-20** (new-draft, score 0, ignored_after_review) [netconf]: [Subscription to Notifications in a Distributed Architecture](https://datatracker.ietf.org/doc/draft-ietf-netconf-distributed-notif/) — This document describes extensions to the YANG notifications
   subscription to allow metrics being published directly from
   processors on line cards to target receivers, while subscription is
   still maintained at the route processor in a distributed forwarding
   system of a network node.
- **draft-ietf-netconf-over-quic-11** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF over QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-over-quic/) — This document specifies how to use QUIC as a secure transport for
   exchanging Network Configuration Protocol (NETCONF) messages.
   NETCONF over QUIC allows to take advantage of QUIC streams, for
   example, to eliminate some TCP head-of-line blocking issues.  NETCONF
   over QUIC provides security properties similar to NETCONF over TLS.

   This document also defines a YANG module which augments the ietf-
   netconf-client and ietf-netconf-server YANG modules.

Editorial note (to be removed by the RFC Editor

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
- **draft-ietf-netconf-privcand-10** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF and RESTCONF Private Candidate Datastores](https://datatracker.ietf.org/doc/draft-ietf-netconf-privcand/) — This document provides a mechanism to extend the Network
   Configuration Protocol (NETCONF) and RESTCONF protocol to support
   multiple clients making configuration changes simultaneously and
   ensuring that they commit only those changes that they defined.

   This document addresses two specific aspects: The interaction with a
   private candidate over the NETCONF and RESTCONF protocols and the
   methods to identify and resolve conflicts between clients.
- **draft-ietf-netconf-restconf-trace-ctx-headers-10** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extension to Support Trace Context Headers](https://datatracker.ietf.org/doc/draft-ietf-netconf-restconf-trace-ctx-headers/) — This document defines an extension to the RESTCONF protocol in order
   to support Trace Context propagation as defined by the W3C.
- **draft-ietf-netconf-trace-ctx-extension-08** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extension to support Trace Context propagation](https://datatracker.ietf.org/doc/draft-ietf-netconf-trace-ctx-extension/) — This document defines how to propagate trace context information
   across the Network Configuration Protocol (NETCONF), that enables
   distributed tracing scenarios.  It is an adaption of the HTTP-based
   W3C specification.
- **draft-ietf-nfsv4-rfc8881bis-09** (new-draft, score 0, ignored_after_review) [nfsv4]: [Network File System (NFS) Version 4 Minor Version 1 Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-rfc8881bis/) — This document describes the Network File System (NFS) version 4 minor
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
- **draft-ietf-nfsv4-uncacheable-directories-10** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Dirent Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  This
   caching is inherently best-effort: those attributes belong to the
   underlying files and change when the files are written, which the
   directory's change attribute does not track.  In some deployments the
   rate of file writes by other clients makes such caching produce
   incorrect size and timestamp values often enough to be a deployment
   problem.  This document introduces an uncacheable dirent metadata
   attribute for NFSv4.2 that allows a server to identify a directory
   for which an honoring client is required to retrieve dirent metadata
   from the server on each READDIR rather than serving the response from
   a local cache.
- **draft-ietf-opsawg-ipfix-alt-mark-08** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-veloce-yang-00** (new-draft, score 0, ignored_after_review) [opsawg]: [YANG deVELpment PrOCEss and maintenance (VELOCE)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-veloce-yang/) — This document describes a YANG deVELpment PrOCEss and maintenance
   (VELOCE) that is more suitable for the development of YANG modules or
   YANG modules update within the IETF.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/mjethanandani/veloce.
- **draft-ietf-pim-pfm-forwarding-enhancements-08** (new-draft, score 0, ignored_after_review) [pim]: [PIM Flooding Mechanism and Source Discovery Enhancements](https://datatracker.ietf.org/doc/draft-ietf-pim-pfm-forwarding-enhancements/) — The Protocol Independent Multicast (PIM) Flooding Mechanism (PFM) is
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
- **draft-ietf-regext-rdap-jscontact-26** (new-draft, score 0, ignored_after_review) [regext]: [Using JSContact in Registration Data Access Protocol (RDAP) JSON Responses](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-jscontact/) — This document describes an RDAP extension which represents entity
   contact information in JSON responses using JSContact.
- **draft-ietf-rtgwg-atn-bgp-32** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
   mobile routing solutions for a worldwide Aeronautical
   Telecommunications Network with Internet Protocol Services (ATN/IPS).
   The ATN/IPS will eventually replace existing communication services
   with an IP-based service supporting pervasive Air Traffic Management
   (ATM) for Air Traffic Controllers (ATC), Airline Operations
   Controllers (AOC), and all commercial aircraft worldwide.  This
   informational document describes a simple and extensible mobile
   routing service based on the industry-standard Border Gateway
   Protocol (BGP) and Domain Name System (DNS) to address the ATN/IPS
   requirements.
- **draft-ietf-rtgwg-multisegment-sdwan-16** (new-draft, score 0, ignored_after_review) [rtgwg]: [Multi-segment SD-WAN via Cloud Backbone](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/) — This document describes a method for seamlessly
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
- **draft-ietf-sidrops-publication-server-bcp-10** (new-draft, score 0, ignored_after_review) [sidrops]: [Best Practices for Operating Resource Public Key Infrastructure (RPKI) Publication Services](https://datatracker.ietf.org/doc/draft-ietf-sidrops-publication-server-bcp/) — This document describes best current practices for operating an RFC
   8181 (A Publication Protocol for the Resource Public Key
   Infrastructure (RPKI)) publication engine and its associated publicly
   accessible rsync (RFC 5781) and RPKI Repository Delta Protocol (RRDP)
   (RFC 8182) repositories.
- **draft-ietf-spring-resource-aware-segments-19** (new-draft, score 0, ignored_after_review) [spring]: [Introducing Resource Awareness to SR Segments](https://datatracker.ietf.org/doc/draft-ietf-spring-resource-aware-segments/) — This document describes a mechanism to allocate network resources to
   one or a set of Segment Routing Identifiers (SIDs).  Such SIDs are
   referred to as resource-aware SIDs.  The resource-aware SIDs retain
   their original forwarding semantics, with the additional semantics to
   identify the set of network resources available for the packet
   processing and forwarding action.  This mechanism is applicable to
   both segment routing with MPLS data plane (SR-MPLS) and segment
   routing with IPv6 data plane (SRv6).
- **draft-ietf-spring-sr-policy-group-01** (new-draft, score 0, ignored_after_review) [spring]: [SR Policy Group](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-group/) — Segment Routing is a source routing paradigm that explicitly
   indicates the forwarding path for packets at the ingress node. An SR
   Policy is associated with one or more candidate paths, and each
   candidate path is either dynamic, explicit, or composite. This
   document describes SR Policy Group in MPLS and IPv6 environments and
   illustrates some use cases for parent SR Policy and SR Policy Group
   to provide best practice cases for operators.
- **draft-ietf-spring-sr-redundancy-protection-09** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 for Redundancy Protection](https://datatracker.ietf.org/doc/draft-ietf-spring-sr-redundancy-protection/) — Redundancy Protection is a generalized protection mechanism to
   achieve high reliability for services provided in Segment Routing
   networks.  The mechanism uses the "Live-Live" methodology, i.e.,
   multiple copies of the data packets are sent on different paths to
   provide protection.  This document introduces one new SRv6 Segment
   Endpoint Behavior, the associated Headend Encapsulation Behaviors and
   the associated Redundancy Policy to provide replication and
   elimination functions on specific network nodes by leveraging SRv6
   Network Programming capabilities.
- **draft-ietf-teas-nrp-scalability-10** (new-draft, score 0, ignored_after_review) [teas]: [Scalability Considerations for Network Resource Partition](https://datatracker.ietf.org/doc/draft-ietf-teas-nrp-scalability/) — A network slice offers connectivity services to a network slice
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
- **draft-ietf-v6ops-ipv6-app-testing-02** (new-draft, score 0, ignored_after_review) [v6ops]: [Testing Applications' IPv6 Support](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   software as a service providers on how to approach IPv6 testing in
   Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including "IPv6-
   only-strict" scenarios without any connectivity towards any relevant
   IPv4 endpoint.  It discusses common misconceptions about the degree
   to which operating systems and libraries can abstract IPv6 issues
   away and explains common regressions to avoid when deploying IPv6
   support.
- **draft-ietf-v6ops-nat64-wkp-1918-08** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the requirement introduced in Section 3.1 of
   RFC6052 that IPv4/IPv6 Translators MUST NOT use the Well-Known Prefix
   64:ff9b::/96 to represent non-globally reachable IPv4 addresses, such
   as those defined in RFC1918 or listed in Section 2.2.2 of RFC6890.
   The proposed change enables IPv6-only nodes to reach IPv4-only
   services with specific non-globally reachable addresses by leveraging
   the Well-Known Prefix.

   This document updates Section 3.1 of RFC6052 ("Restrictions on the
   Use of the Well-Known Prefix") to allow packets in which an address
   is composed of the Well-Known Prefix and specific non-globally
   reachable IPv4 addresses to be translated.
- **draft-ietf-v6ops-rfc6146-bis-15** (new-draft, score 0, ignored_after_review) [v6ops]: [Stateful NAT64: Network Address and Protocol Translation from IPv6 Clients to IPv4 Servers](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc6146-bis/) — This document specifies a stateful NAT64 translation, which allows
   IPv6-Only clients to contact IPv4 servers using unicast UDP, TCP, or
   ICMP.  One or more public IPv4 addresses assigned to a stateful NAT64
   translator are shared among several IPv6-Only clients.  Stateful
   NAT64 translation also supports IPv4-initiated communications to a
   subset of the IPv6 hosts through configured bindings in the stateful
   NAT64 translator.  When the stateful NAT64 translation is used in
   conjunction with DNS64, no changes are required in either the IPv6
   client or the IPv4 server.

   This document obsoletes RFC 6146.
- **draft-ietf-v6ops-rfc7915-bis-01** (new-draft, score 0, ignored_after_review) [v6ops]: [IP/ICMP Translation Algorithm](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/) — This document describes the Stateless IP/ICMP Translation Algorithm
   (SIIT), which translates between IPv4 and IPv6 packet headers
   (including ICMP headers).  This document obsoletes RFC 7915.
- **draft-jags-intarea-icmp-ext-underlay-info-05** (new-draft, score 0, ignored_after_review) [none]: [ICMP extension to include underlay information](https://datatracker.ietf.org/doc/draft-jags-intarea-icmp-ext-underlay-info/) — Network operators managing overlay networks require visibility into
   underlay network hops during traceroute operations from overlay
   endpoints.  This document defines an ICMP extension object, the
   Underlay Information Object (UIO), which allows underlay head-end
   nodes to encapsulate underlay error information within ICMP error
   messages.  This mechanism provides overlay operators with crucial
   visibility into underlay network paths for troubleshooting.
- **draft-juwan-ars-uri-01** (new-draft, score 0, ignored_after_review) [none]: [ARS URI Scheme: A URI Scheme for ARS-1 References](https://datatracker.ietf.org/doc/draft-juwan-ars-uri/) — This document defines the "ars" URI scheme for representing ARS-1
   References in a syntactically valid URI form.  ARS-1 defines a
   deterministic, cryptographically derived reference protocol for
   assigning stable public identifiers to durable digital entities.  The
   "ars" URI scheme provides a standard URI notation for these
   references, enabling their use in hyperlinks, QR codes, metadata
   fields, and other URI-consuming contexts.

   This specification does not redefine the ARS-1 Reference generation
   pipeline, canonicalization rules, or verification logic.  Those are
   normatively defined by ARS-1.  This document defines only the URI
   syntax, encoding, comparison, and resolution semantics for the "ars"
   scheme.
- **draft-kennedy-dnssd-data-block-01** (new-draft, score 0, ignored_after_review) [none]: [DNS-SD Data Block Encoding for Non-DNS Transports](https://datatracker.ietf.org/doc/draft-kennedy-dnssd-data-block/) — The DNS-SD Data Block (DDB) is a compact TLV encoded container for
   conveying DNS-SD service information over non-IP transports used by
   short-range peer-to-peer or proximity-based advertisement and
   discovery technologies such as the Bluetooth Low Energy Transport
   Discovery Service or NFC Verb NDEF Records.
- **draft-lin-opsawg-ipfix-quic-header-05** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of QUIC Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-quic-header/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements to identify a set of QUIC related information,
   which contained in QUIC Header, QUIC Frame and Stream that traffic is
   being forwarded along with.
- **draft-loffredo-regext-rdap-verified-contacts-04** (new-draft, score 0, ignored_after_review) [regext]: [Registration Data Access Protocol (RDAP) Extension for Verified Contact Information](https://datatracker.ietf.org/doc/draft-loffredo-regext-rdap-verified-contacts/) — This document describes an extension to the Registration Data Access
   Protocol (RDAP) that allows the inclusion of verification status
   information for contact fields such as email addresses and phone
   numbers.  The goal is to improve data quality and trustworthiness of
   RDAP responses by indicating which pieces of contact data have been
   verified and how.
- **draft-luechow-route86-timestamp-01** (new-draft, score 0, ignored_after_review) [none]: [Route86: A Compact Context-Dependent Timestamp Format](https://datatracker.ietf.org/doc/draft-luechow-route86-timestamp/) — This document specifies Route86, a compact textual timestamp format
   for constrained message transports.  A Route86 value consists of a
   three-character Base36 calendar-day component and a three-digit
   decimal time-of-day component.  The canonical representation occupies
   exactly six ASCII characters.

   The calendar component is interpreted relative to an external
   reference date.  The reference date itself encodes as AAA.  The time-
   of-day component divides a fixed BMT day, defined here as UTC+01:00
   without daylight-saving adjustment, into 1000 intervals of 86.4
   seconds.
- **draft-ma-6man-ra-dns64-flag-02** (new-draft, score 0, ignored_after_review) [none]: [Updates to DNS64 Functionality Advertisement for DNS RA Option](https://datatracker.ietf.org/doc/draft-ma-6man-ra-dns64-flag/) — This document defines a new flag in the DNS RA Option to advertise
   the DNS64 functionality.  This extension enables automatic
   configuration of DNS64 resolution, improving deployability in IPv6
   transition scenarios.
- **draft-ma-v6ops-pe-ipv6only-reqs-01** (new-draft, score 0, ignored_after_review) [none]: [Requirements for Provider Edge in IPv6-only Underlay Networks](https://datatracker.ietf.org/doc/draft-ma-v6ops-pe-ipv6only-reqs/) — This document defines functional, protocol, and operational
   requirements for Provider Edge (PE) devices operating in a multi-
   domain network environment where the underlay is exclusively based on
   IPv6.  These requirements ensure consistent service delivery,
   interoperability, and efficient operations across autonomous domains
   while supporting IPv4-as-a-Service (IPv4aaS).
- **draft-mela-nameservers-00** (new-draft, score 0, ignored_after_review) [none]: [Name server provider and domain name registrar](https://datatracker.ietf.org/doc/draft-mela-nameservers/) — This document describes operational practices and technical
   frameworks related to name server providers and domain name
   registrars.
- **draft-nurpmeso-dkim-access-control-diff-changes-13** (new-draft, score 0, ignored_after_review) [dkim]: [DKIM Access Control and Differential Changes](https://datatracker.ietf.org/doc/draft-nurpmeso-dkim-access-control-diff-changes/) — This document specifies a DKIM (RFC 6376) iteration that allows
   cryptographical verification of SMTP (RFC 5321) envelope data, and of
   any signature along the message path, even beyond IMF (RFC 5322)
   message content changes.  It addresses existing security glitches,
   and introduces active mitigations to embrace collateral damage
   effects of email solutions of the younger past by a standardized
   solution, also by moving complexity away from lower network protocol
   layers, where problems cannot be solved.  It updates DKIM in certain
   aspects that reality has proven to be superfluous, incomplete, or
   obsoleted.
- **draft-rosomakho-httpbis-h3-unbound-data-02** (new-draft, score 0, ignored_after_review) [none]: [Unbound DATA for CONNECT in HTTP/3](https://datatracker.ietf.org/doc/draft-rosomakho-httpbis-h3-unbound-data/) — This document defines a new HTTP/3 frame type, UNBOUND_DATA, and a
   corresponding SETTINGS parameter that enables endpoints to negotiate
   its use.  When an endpoint sends an UNBOUND_DATA frame on a CONNECT
   request or response stream, it indicates that all subsequent octets
   on that stream are interpreted as tunneled bytes.  This applies both
   to octets transmitted after CONNECT or extended CONNECT.  The use of
   UNBOUND_DATA removes the need to encapsulate each portion of the data
   in DATA frames, reducing framing overhead and simplifying
   transmission of long-lived CONNECT tunnels.
- **draft-schinazi-masque-proxy-09** (new-draft, score 0, ignored_after_review) [none]: [The MASQUE Architecture](https://datatracker.ietf.org/doc/draft-schinazi-masque-proxy/) — MASQUE (Multiplexed Application Substrate over QUIC Encryption) is a
   set of protocols and extensions to HTTP that allow proxying all kinds
   of Internet traffic over HTTP.  This document describes the
   architectural principles behind MASQUE, and the properties that
   MASQUE can provide.
- **draft-sfluhrer-ssh-mldsa-08** (new-draft, score 0, ignored_after_review) [none]: [SSH Support of ML-DSA](https://datatracker.ietf.org/doc/draft-sfluhrer-ssh-mldsa/) — This document describes the use of the ML-DSA digital signature
   algorithms in the Secure Shell (SSH) protocol.  Accordingly, this RFC
   updates RFC 4253.
- **draft-swhited-ogg-skeleton-02** (new-draft, score 0, ignored_after_review) [none]: [Ogg Skeleton](https://datatracker.ietf.org/doc/draft-swhited-ogg-skeleton/) — Ogg Skeleton defines a logical bitstream that provides structuring
   information for multitrack Ogg files.  It provides clues for
   synchronization and content negotiation including language selection.
   It also provides keypoint indices for optimal seeking over high-
   latency connections or in time-critical scenarios.
- **draft-templin-6man-aero-omni-amen-14** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-wang-idr-path-attribute-orf-00** (new-draft, score 0, ignored_after_review) [none]: [Path Attribute Outbound Route Filter (PA-ORF) for BGP-4](https://datatracker.ietf.org/doc/draft-wang-idr-path-attribute-orf/) — This document defines a family of Outbound Route Filter (ORF) Types
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
- **draft-wang-tls-hybrid-ecdh-scloud-02** (new-draft, score 0, ignored_after_review) [none]: [Post-quantum Hybrid ECDHE-SCloud+ Key Exchange for TLS 1.3](https://datatracker.ietf.org/doc/draft-wang-tls-hybrid-ecdh-scloud/) — This draft specifies how to enable hybrid key exchange with ECDHE and
   SCloud+ in Transport Layer Security protocol version 1.3 (TLS 1.3) to
   mitigate quantum threats.  SCloud+ is an unstructured lattice based
   KEM (key encapsulation mechanism) with post-quantum security.  This
   draft follows the post-quantum hybrid key exchange framework
   specified by [RFC9954], by concatenating the public keys and
   ciphertexts of ECDHE and SCloud+. This draft specifies three concrete
   hybrid key exchange schemes, which are X25519SCloud+128,
   SecP256r1SCloud+192 and SecP384r1SCloud+256.
- **draft-wkumari-opsawg-json-geofeed-format-01** (new-draft, score 0, ignored_after_review) [none]: [A JSON Format for Self-Published IP Geolocation Feeds](https://datatracker.ietf.org/doc/draft-wkumari-opsawg-json-geofeed-format/) — This document defines a JavaScript Object Notation (JSON) format for
   self-published IP geolocation feeds.  It updates RFC 8805 by
   transitioning from the current comma-separated values (CSV) format to
   a more expressive JSON format, addressing the need for operational
   extensibility.
- **draft-yuyou-moq-conditional-filtering-00** (new-draft, score 0, ignored_after_review) [none]: [Conditional Range Filters for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-yuyou-moq-conditional-filtering/) — In Media over QUIC Transport (MOQT), subscribers can use Range
   Filters to select specific subgroups, objects, or priorities within a
   subscribed track.  However, these subscription filters are static
   once established and can only be modified through explicit subscriber
   control signaling.  This document proposes an extension to the Range
   Filter design that binds conditional evaluation logic directly to
   specific Range Filter sets.  By introducing dynamic conditions to
   Range Filter configurations, a relay can autonomously adapt the
   intra-track forwarding behavior based on real-time network
   conditions, avoiding the round-trip delay of explicit subscriber
   update signaling.
- **draft-zhangb-cats-service-metrics-op-04** (new-draft, score 0, ignored_after_review) [none]: [Computing Service Metric Definitions and Operation under CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-service-metrics-op/) — Computing-Aware Traffic Steering (CATS) optimizes traffic forwarding
   by considering both computing and networking metrics.  While existing
   framework and metric definition drafts provide theoretical models
   (e.g., L1/L2 normalized metrics), they face significant challenges in
   achieving direct operational execution in real-world deployments.
   Normalization methods vary across providers, and aggregated unitless
   scores often lose critical operational information, making it
   difficult for routers to make precise traffic-steering decisions.

   This document fills this gap by providing an executable operational
   approach.  It defines a set of Computing Service Metrics and their
   operations under the CATS framework.  Instead of transmitting low-
   level raw hardware metrics, service sites dynamically evaluate and
   report service-oriented metrics (e.g., Global Available Slots) to the
   control plane.  The document clarifies how such service-oriented
   metrics can be derived from basic resource information, service
   reference information, and local policy.  It also specifies how the
   CATS Path Selector (C-PS) combines the Computing Service
   Table (derived from C-SMA reports) with the Network Service Table to
   make joint traffic-steering decisions.  Finally, the document defines
   update control mechanisms for large-scale deployments.  This enables
   efficient and precise traffic-steering policies without negating the
   value of existing normalized metrics.

## Errors / fetch failures

- draft-faltstrom-unicode: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-faltstrom-unicode/doc.json
