# IETF Identity + AI Standards Watch

Date: 2026-09-01

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
- **draft-wei-aic-identity-cert-01** (new-draft, score 21, core_identity) [none]: [AI Agent Identity Certificate (AIC) Extension for X.509 v3](https://datatracker.ietf.org/doc/draft-wei-aic-identity-cert/) — This document defines the AI Agent Identity Certificate (AIC)
   Extension for X.509 v3 certificates.  The AIC extension enables
   binding of an AI Agent's cryptographic identity to a natural person
   (principal), providing cryptographic evidence that can support
   attribution of AI-autonomous actions to a principal.  This
   specification intentionally separates cryptographic delegation from
   authorization semantics: AIC defines the cryptographic binding
   between agent and principal, while all capability and policy
   semantics are defined externally by vendors, industries, or
   regulators.  The extension is identified by the IANA Private
   Enterprise Number 66257 assigned to the document author's
   organization.

   The AIC extension carries agent identity fields (agentId,
   delegationMode), a principal identifier (principalUid) linking the
   agent to the authorizing principal, a container-based capability
   declaration, authorization boundary constraints, and delegation
   authorization evidence with replay protection.  A companion
   PrincipalAuthorization extension anchors Principal-side grant
   declarations and delegation policies.  An authorizationConstraints
   container provides offline-verifiable execution boundaries (IP range,
   window).  An extensibility framework allows vendor-specific and user-
   specific metadata.

   This document specifies the ASN.1 module, OID registration, field
   semantics, delegation model, and extensibility framework.  Security
   considerations for deployment in regulated enterprise environments
   are discussed.
- **draft-mishra-oauth-agent-grants-02** (new-draft, score 20, authorization) [none]: [OAuth Profile for Delegated AI Agent Authorization](https://datatracker.ietf.org/doc/draft-mishra-oauth-agent-grants/) — AI agents increasingly invoke protected APIs on behalf of human
   users.  This document defines an OAuth profile for identifying an
   agent client instance, obtaining an authenticated user's consent,
   issuing resource-bound and sender-constrained access tokens,
   attenuating authority through OAuth Token Exchange, and rotating
   refresh tokens safely.  The profile uses existing OAuth and JOSE
   mechanisms wherever possible and defines no new JWT claims or OAuth
   endpoints.  Operational facilities such as policy engines, audit
   stores, budgets, event streams, and credential vaults are outside the
   interoperable core.  Grantex is an incomplete reference
   implementation and is not required for conformance.
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
- **draft-morrison-ot-command-authority-02** (new-draft, score 19, authorization) [none]: [Consented and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
   issued to an operational-technology (OT) or industrial control system
   on the authority of a software agent is refused unless it carries a
   verifiable statement of who the agent is, which human principal it
   acts for, whether that principal authorised this specific action on
   this specific asset, whether a named human signed off on the action
   where its risk class requires it, and an append-only record
   sufficient to attribute the action afterward.  The profile does not
   invent new cryptography or a new identity mechanism.  It composes
   primitives specified elsewhere, DNSSEC-rooted agent discovery, a
   scoped and revocable authorisation grant, a named-human authorization
   receipt bound into the record as human-authorization evidence, and an
   append-only transparency record, into a single structure, the Command
   Authority Envelope, that an enforcement point evaluates and, on any
   missing or invalid binding, refuses.  The profile is availability-
   first and fails closed on authority, never on safety: it MUST NOT be
   placed in the trip path of a safety function.  The memo maps the
   profile onto the identification, use-control, and audit requirements
   that the IEC 62443 and NERC CIP frameworks state but do not give a
   wire mechanism for.  A neighbouring proposal gates safety-critical
   commands on an agent's trust level; this profile takes the opposite
   position, and states why.  The methods by which a principal's
   identity is inferred are out of scope by construction.
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
- **draft-marques-asqav-compliance-receipts-08** (new-draft, score 18, core_identity) [none]: [Compliance Profile of Signed Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-marques-asqav-compliance-receipts/) — This document defines a multi-jurisdiction compliance profile of the
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
   cross-agent envelope binding, per-action validity-window and
   integrity, build provenance, threat-framework taxonomy, server-built
   enforcement-control records, producer-asserted risk acceptance, and
   producer-asserted code authorship, each subject to false-attestation
   guards where applicable, and registers receipt type namespaces for
   passive-telemetry, result-bound observation, risk-acceptance, and
   code-authorship receipts.  Revision -08 additionally defines an
   attestation statement envelope (a Dead Simple Signing Envelope (DSSE)
   Pre-Authentication Encoding wrapping an in-toto Statement v1 under an
   asqav predicate namespace) with two tiers: a voluntary observation
   attestation that signs a caller-supplied digest and is explicitly not
   a capture, and an authoritative attestation whose subject digest the
   issuing platform re-derives from independent evidence (for code, the
   SHA-256 of the raw unified diff re-fetched from the source host);
   revision -08 further defines the capture-layer integrity, independent
   verification protocol, honest-tiering, and service-identity and
   revocation rules that govern those attestation statements, and
   documents the shipped keyed-digest wire tokens and the verifier
   verdict vocabulary (verified, verified_keyed, unverified).  The full
   field set and its normative requirements are defined in the body of
   this document.
- **draft-reece-wimse-cross-org-delegation-02** (new-draft, score 18, core_identity) [none]: [Cross-Organizational Delegation for Workload and Agent Identity: Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/) — Autonomous software agents increasingly act on behalf of human
   principals by invoking tools, services, and other agents, frequently
   across organizational boundaries.  Existing workload and token-based
   authorization mechanisms were designed for a single trust domain and
   a small number of delegation hops.  They do not adequately express,
   constrain, or verify authority that is delegated recursively among
   agents and that crosses the boundary between independently
   administered organizations.  This document describes the problem of
   cross-organizational agent delegation, identifies the gaps in current
   mechanisms, and enumerates requirements that any solution within the
   scope of the Workload Identity in Multi-System Environments (WIMSE)
   working group should satisfy.  It does not specify a solution.
- **draft-das-rats-openai-anthropic-extraction-00** (new-draft, score 17, trust_infrastructure) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive OpenAI and Anthropic Claude Model Information](https://datatracker.ietf.org/doc/draft-das-rats-openai-anthropic-extraction/) — Anthropic and OpenAI already ship inference interfaces richer than
   raw completions -- log-probabilities, embeddings, hidden states,
   intermediate activations, KV-cache material, and diagnostic output
   are all in production today.  Each is a channel an adversary, a
   compromised partner integration, or a stolen enterprise seat can use
   to reconstruct, steal, or distill a model far faster than by scraping
   ordinary text output.  In this document, a "release" is any point at
   which such information leaves the protected execution environment and
   becomes usable outside it: returned to a caller, cached, forwarded,
   or otherwise materialized.  The operational question this document
   answers is narrow: given that the caller is authenticated and the
   workload is attested, is this specific release still authorized to
   happen right now?

   Authentication establishes who is asking.  Confidential computing and
   remote attestation establish whether the execution environment is
   trustworthy.  Neither establishes whether this particular release, of
   this particular artifact, at this particular moment, should be
   allowed to cross the protected boundary.  A valid API key, a genuine
   TEE, and a passing Attestation Result are all fully compatible with
   an unauthorized bulk-extraction run already in progress.  Rate
   limits, output filtering, and anomaly detection operate after the
   release has already happened; they make extraction easier to notice,
   not harder to complete.

   This document specifies an execution-finality architecture that makes
   release control a technical precondition rather than a monitoring
   layer: computation is separated from authority to release, every
   sensitive result is held as a non-effective Candidate Release, and
   release becomes possible only after release-specific validation,
   rollback-resistant extraction-state evaluation, bounded
   authorization, and verification at a controlled Finality Sink.
   Because release authority is bound to rollback-resistant, atomically
   consumed extraction state rather than to a bearer credential, the
   volume of privileged teacher signal an adversary can accumulate
   through the governed path is capped by authorized state transitions,
   not by request volume or attacker persistence alone.  The mechanism
   is not claimed to prevent all forms of model distillation; its
   objective is to make unauthorized or excessive extraction of
   privileged model information structurally harder to complete, not
   merely easier to detect afterward.
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
- **draft-schrock-action-evidence-boundary-05** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
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
- **draft-das-rats-frontier-model-extraction-02** (new-draft, score 16, core_identity) [none]: [Beyond Attestation: An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive Frontier AI Model Information](https://datatracker.ietf.org/doc/draft-das-rats-frontier-model-extraction/) — As frontier AI providers expose increasingly rich inference
   interfaces to partners, evaluators, and enterprise tenants, richer-
   than-normal outputs -- for example logits, log-probability
   distributions, embeddings, hidden states, intermediate activations,
   KV-cache material, and diagnostic state -- become practical
   extraction vectors rather than theoretical concerns.  In this
   document, a "release" is any point at which such information leaves a
   provider's protected execution environment and becomes usable outside
   it, whether returned directly to a caller, cached, forwarded, or
   otherwise materialized.  Existing authentication, confidential-
   computing, and remote-attestation mechanisms can establish important
   properties of the requester and execution environment, but they do
   not by themselves establish that each specific release of sensitive
   model information is currently authorized to cross that protected-to-
   unprotected boundary.

   This document describes that gap as a pre-effectuation release-
   control problem and proposes controls intended to limit unauthorized
   extraction and reduce the risk that released model information can be
   used for downstream distillation.  It presents an execution-finality
   architecture in which computation is separated from authority to
   release.  A sensitive result is treated as a Candidate Release,
   remains non-effective outside the protected domain, and becomes
   externally available only after release-specific validation,
   rollback-resistant extraction-state evaluation, bounded
   authorization, and verification at a controlled Finality Sink.  The
   document discusses anti-bypass requirements, remote-attestation
   composition, latency, legacy deployment, industrial relevance, and a
   concrete model-extraction scenario.

   The mechanism is not claimed to prevent all forms of model
   distillation.  Its narrower objective is to reduce unauthorized or
   excessive extraction of privileged model information that can
   materially improve model stealing, reconstruction, imitation, or
   distillation.  Because release authority is bound to rollback-
   resistant, atomically consumed extraction state rather than to a
   bearer credential, the volume of privileged teacher signal an
   adversary can accumulate through the governed path is capped by
   authorized state transitions, not by request volume or attacker
   persistence alone.
- **draft-ietf-oauth-sd-jwt-vc-19** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.
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
- **draft-mcphillips-agentenvelope-derived-authority-01** (new-draft, score 16, authorization) [none]: [AgentEnvelope: Derived Authority and Legitimacy for Autonomous Systems](https://datatracker.ietf.org/doc/draft-mcphillips-agentenvelope-derived-authority/) — AgentEnvelope defines a deterministic derived-authority model for
   autonomous and action-performing systems.  Instead of issuing bearer
   credentials from a central authority, AgentEnvelope derives scoped
   action capabilities from customer-held custody material and canonical
   action envelopes.  A verifier can check an action signature against a
   public action record without receiving roots, seeds, private keys,
   mint material, or hosted service access.

   This revision extends the model with legitimacy: a governance state
   that records whether a cryptographically valid authority remains
   admissible under current policy, evidence, time, and operating
   context.  Legitimacy separates provenance from present-tense
   authorization.  A command can remain signed and verifiable while
   becoming illegitimate because operating facts, policy, or evidence
   changed.

   For autonomous-system deployments, derived authority and legitimacy
   support an IAM model concerned with authority, admissibility,
   accountability, and audit for actors that perform actions, including
   AI agents, workflows, bots, microservices, devices, robots,
   serverless workers, and multi-agent systems.
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
- **draft-das-6g-query-scoped-communication-handles-04** (new-draft, score 15, core_identity) [none]: [Authorization-to-Reach for Communication Handles: Separating Identifier Possession from Permission to Contact](https://datatracker.ietf.org/doc/draft-das-6g-query-scoped-communication-handles/) — Many Internet and telephone communication systems treat possession of
   a routable identifier as sufficient to attempt contact.  A telephone
   number, SIP URI, messaging handle, relay address, or marketplace
   contact reference can therefore remain a reusable reachability path
   after the purpose of disclosure has ended.

   Existing IETF and industry mechanisms solve related but different
   problems.  STIR and SHAKEN authenticate or attest originating
   identity.  Virtual or masked numbers hide a persistent endpoint but
   commonly leave a substitute route active while the alias is valid.
   OAuth can express delegated API authorization.  Spam scoring and call
   screening classify or reject an attempt after some path already
   exists.

   This document describes an authorization-to-reach model.  A visible
   communication handle is not, by itself, permission to create a
   communication effect.  A request is held as a candidate until
   current, purpose-scoped, revocable, and optionally consumable
   authority is validated.  The document is informational.  It asks
   whether the IETF Applications and Real-Time area should define
   interoperable semantics or an encoding for that authority (for
   example a PASSporT claim, a SIP header or pre-INVITE check, or a
   reusable authorization object).

   This work is not a 3GPP radio, core-network, or IMT-2030 architecture
   proposal.  References to machine-scale or future-network traffic are
   motivational only.  The intended protocol home, if any, is IETF work
   on SIP, STIR, messaging, and Internet communication identifiers.
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
- **draft-sokolov-rats-aep-composition-06** (new-draft, score 15, trust_infrastructure) [none]: [Composing Application-Layer Action Evidence with Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-sokolov-rats-aep-composition/) — This document sketches a composition pattern in which an application-
   layer "action evidence package" (AEP) -- a signed action record that
   can be hash-linked to earlier records and that reports an action
   taken by an automated (for example, AI-agent) system, the authority
   under which it was taken, and its outcome -- is treated as Evidence
   in the sense of the RATS Architecture (RFC 9334) and bound to
   platform Evidence produced by a hardware root of trust.  The intent
   is that a single Verifier, or a composition of Verifiers, can
   appraise both the platform state and the application-layer record
   together, and emit an Attestation Result that a Relying Party can use
   to reason about _what an automated system reports it did_ and _the
   appraised state of the platform associated with that record_. The
   composition does not turn a self-reported action or outcome into an
   independently observed fact; it prevents the Relying Party from
   having to rely on an unbound operator-side log alone.  This is an
   individual sketch intended to ask the working group whether the
   pattern is already covered by existing mechanisms or warrants a short
   document.
- **draft-birkholz-verifiable-agent-conversations-01** (new-draft, score 14, trust_infrastructure) [none]: [Verifiable Agent Conversation Records](https://datatracker.ietf.org/doc/draft-birkholz-verifiable-agent-conversations/) — Autonomous agents based on large language models increasingly perform
   consequential tasks on behalf of humans and other agents.
   Demonstrating that recorded agent behavior truthfully represents
   actual behavior is essential for accountability, compliance, and
   human oversight.  This document defines a data format for verifiable
   agent conversation records using CDDL, with representations in both
   JSON and CBOR.  The format captures session metadata, message
   exchanges, tool invocations, reasoning traces, and system events in a
   structured, extensible CDDL definition for verifiable agent
   conversation records.  COSE is used as the signing method to allow
   for native interoperability in SCITT Transparency Services and the
   CDDL definition allows for seemless integration in Evidence as
   specified in RFC 9334.  The specification supports cross-vendor
   interoperability by defining a common representation that
   accommodates translation from multiple existing agent implementations
   with distinct data structure layouts that are typically represented
   in JSON.
- **draft-das-digital-sovereignty-finality-01** (new-draft, score 14, adjacent_watchlist) [none]: [When Data Leaves Its Originating Jurisdiction, Who Controls It? Digital Sovereignty Without Data Localisation by Separating the Compute Plane from the Authority Plane](https://datatracker.ietf.org/doc/draft-das-digital-sovereignty-finality/) — Consider a simple case: data concerning U.S. citizens is processed in
   infrastructure located outside the United States.  The foreign
   jurisdiction may have its own lawful-access, surveillance,
   disclosure, retention, or national-security rules.  Even where
   contractual commitments, privacy policies, regional settings, or
   enterprise agreements specify how that data should be handled, the
   infrastructure executing the workload may ultimately operate under
   legal and technical authority outside the originating jurisdiction.

   The same problem applies in reverse to European, Indian, Japanese,
   Canadian, Australian, or other data processed through globally
   distributed infrastructure.

   This creates a deeper architectural problem than ordinary data
   localisation.

   If control over data automatically follows the physical location of
   compute, then moving computation across borders can also move
   practical authority over the resulting data, operations, and
   disclosures.  Privacy may be the first concern, but the same
   architectural dependency can later affect economic security, critical
   infrastructure, sensitive enterprise information, government
   workloads, and national security.

   This is where policy alone begins to reach its limit.

   Contracts, privacy policies, adequacy mechanisms, access-control
   rules, cloud-region settings, and audit requirements remain
   important.  However, they primarily describe what an actor is
   permitted or expected to do.  They do not necessarily create a
   technical condition that prevents a prohibited external effect from
   occurring in the first place.

   Although this document uses the term "digital sovereignty," it does
   not attempt to standardize national policy, determine which
   jurisdiction's law should prevail, or prescribe where data must be
   stored.  Its focus is technical: defining an interoperable mechanism
   by which deployment-selected policy and trust inputs can be bound to
   a specific Candidate Act and enforced at the effectuation boundary
   before that act becomes externally effective.  In this document,
   "sovereignty" therefore refers to retained execution authority, not
   to the standardization of geopolitical or regulatory policy.

   The architecture described here addresses this problem through a
   different model of digital sovereignty: separate the Compute Plane
   from the Authority Plane.

   The Compute Plane may remain globally distributed.  Data may be
   stored, transformed, analysed, routed, or processed using
   infrastructure located in another jurisdiction.  The architecture
   therefore does not require that all data remain physically local, nor
   does it assume that sovereign computing requires complete national
   isolation from global cloud, telecom, AI, or platform infrastructure.

   Instead, the Authority Plane remains independently governed.  A
   remote compute environment may perform computation, but computation
   alone does not grant authority to produce a protected external
   consequence.

   A proposed cross-jurisdiction operation is represented as a Candidate
   Act and remains in a Non-Effective State until the required policy,
   identity, purpose, destination, jurisdiction, runtime, revocation,
   and other applicable predicates have been validated.

   Protected validation may produce a LAVR or equivalent validation
   commitment and a scoped Finality Authority bound to the particular
   Candidate Act.  At the relevant Finality Sink — the first point at
   which the protected operation would become externally effective — the
   authority is independently verified.  Only after successful
   verification and appropriate consumption or reservation of that
   authority may the external effect occur.

   The resulting model is therefore: Compute Anywhere -> Authority
   Remains Independently Governed -> Candidate Act -> Protected
   Validation -> Scoped Finality Authority -> Finality-Sink Verification
   -> External Effect.

   If the required authority is missing, stale, revoked, mismatched,
   replayed, or inconsistent with the governing jurisdictional policy:
   No Valid Authority -> No Protected External Effect.

   This permits a form of digital sovereignty without mandatory data
   localisation.  A jurisdiction, enterprise, regulated institution, or
   other authorised policy owner does not necessarily need to operate
   every processor, cloud region, network, or AI system that performs
   the computation.  Instead, it can retain technical control over the
   conditions under which specified externally effective acts are
   permitted.

   The architecture therefore separates two questions that are commonly
   treated as one: Where is the computation performed?  Who has
   authority over the resulting external effect?  Those questions need
   not have the same answer.

   A U.S. workload could execute outside the United States while
   specified sensitive external effects remain subject to U.S.-
   controlled or enterprise-controlled authorization conditions.  An EU
   workload could similarly use infrastructure outside a particular
   Member State while retaining independently governed finality
   requirements.

   The same mechanism could apply to India, Japan, Singapore, Australia,
   Canada, multinational enterprises, sovereign clouds, regulated
   industries, or private data spaces.  The architecture does not
   prescribe which country's policy should prevail and does not attempt
   to resolve conflicts of law.

   Its contribution is narrower and technical: cross-border computation
   does not have to imply cross-border surrender of execution authority.

   This turns digital sovereignty from a primarily location-centred
   concept into an authority-centred execution model.  The objective is
   not to fragment the Internet or exclude global technology providers.

   On the contrary, separating the Compute Plane from the Authority
   Plane could allow hyperscale cloud providers, AI platforms, telecom
   operators, CDNs, satellite networks, and other global infrastructure
   providers to continue supplying efficient distributed computation
   while supporting stronger jurisdiction-specific, enterprise-specific,
   or regulated execution guarantees.

   In this model, sovereignty does not require saying that the data must
   never leave.  It can instead mean: the computation may occur
   elsewhere, but this protected external effect cannot occur without
   the required authority.

   That is the central architectural proposition of this document.
- **draft-das-map-discovery-communication-finality-00** (new-draft, score 14, core_identity) [none]: [Privacy-by-Design, GDPR-Aligned Communication Finality for Google Maps, Apple Maps, and Other Map-Based Business Discovery Using Query-Scoped Non-Bearer Authorization](https://datatracker.ietf.org/doc/draft-das-map-discovery-communication-finality/) — Map-based discovery systems can help a person identify nearby
   businesses, properties, service providers, hotels, clinics,
   restaurants, and other commercial actors, but discovery frequently
   transitions into communication through a persistent telephone number,
   reusable virtual number, open message thread, callback route, or
   other contact path.  A person may intend only a short first
   conversation with several candidates, while the communication
   mechanism unintentionally creates continuing reachability after that
   inquiry has ended.

   This document describes an architecture in which first contact and
   future reachability are separate authorization events.  After a user
   creates a map search, property inquiry, service request, booking
   inquiry, quote request, or similar context, a platform can create a
   query-scoped non-bearer communication reference and bounded preview
   authority.  A user or eligible business can participate in a real but
   limited first interaction.  Continued communication is separately
   authorized and remains bound to attributes such as the original
   query, business identity, purpose, channel, effect, validity window,
   nonce, quota, revocation state, and enforcement point.  Possession of
   a number, handle, previous conversation, lead assignment, API
   credential, or payment event is not by itself sufficient future-
   contact authority.

   The architecture separates marketplace policy from communication
   effectuation.  A Communication Authority Service creates a protected
   authorization binding, while an enforcement point reconstructs the
   actual attempted communication, checks current protected state,
   atomically reserves or consumes relevant authority, and releases the
   communication-bearing resource only after successful verification.
   This permits privacy-preserving first contact, controlled future
   reachability, preview-qualified lead monetization, and AI-assisted
   business discovery without requiring a new public telecom protocol
   for initial deployment.  Google Maps and Apple Maps are used as
   recognizable illustrative examples; no affiliation, endorsement,
   implementation, adoption, or technical alignment by Google, Apple, or
   any other named provider is implied.

   The architecture's binding of recipient identifiers to pseudonymous,
   query-scoped, time-limited, purpose-bound, and revocable
   authorizations rather than persistent contact data is consistent with
   the data protection principles of the EU General Data Protection
   Regulation (GDPR) -- including data minimization and purpose
   limitation (Article 5), storage limitation through bounded validity
   and quota, and privacy by design and by default (Article 25).  This
   document describes a technical architecture only; it does not
   constitute a legal compliance determination, and conformance with
   GDPR or any other data protection law depends on the specific
   deployment, controller and processor roles, and operational practices
   of an implementing platform.
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
- **draft-das-agentic-tool-binding-02** (new-draft, score 13, authorization) [none]: [tool_use Is Not invoke(): Binding Execution-Finality to Agentic Tool-Call Interfaces and MCP](https://datatracker.ietf.org/doc/draft-das-agentic-tool-binding/) — Frontier runtimes already standardized the dangerous moment.  A model
   emits a tool_use block, a tool_calls array, or an MCP tools/call
   payload.  The host then invokes whatever name and arguments the model
   printed.  Alignment, allowlists, and OAuth sit around that moment.
   They do not sit on it.  If the block is treated as a capability,
   prompt-injected mail, a poisoned retrieval, or a stolen enterprise
   seat becomes an external act with a 200 from the tool.

   This document does not invent another assistant API.  It binds the
   Agent Candidate Act profile [I-D.das-agentic] onto the three
   interface families those runtimes and their customers already ship:
   tool_use / computer_use style interfaces, function-calling and
   structured tool-response interfaces, and Model Context Protocol
   tools/call.  The model may emit the block.  The block remains non-
   effective.  A local enforcer builds the act, binds the argument
   digest, and refuses invoke() until scoped authority is verified and
   consumed at the dispatch sink.

   The implementation target is a middleware function that a host loop
   can call without changing the model vendor. tool_use is not invoke().
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
- **draft-pinto-agent-authz-contestability-00** (new-draft, score 13, authorization) [none]: [Contestability Bindings for Authorized Agent Actions](https://datatracker.ietf.org/doc/draft-pinto-agent-authz-contestability/) — Authorization artifacts can provide signed evidence of a permission
   under specified authorization rules.  Receipts can record a signed
   claim or protocol event that the authorization was exercised, and
   outcome evidence can describe what followed.  None of those artifacts
   necessarily tells a person or organization affected by the action
   where the authorization can be contested, which procedure applies,
   whether a filing changes execution state, or who selected the
   contestation forum.

   This document defines a transport-independent Contestability Binding
   for authorized agent actions.  The binding commits an authorization
   to a versioned Contestation Parameters Object that identifies the
   forum, submission mechanism, Standing Policy, procedure, time bounds,
   declared effect policy, and selection evidence.  A forum can
   acknowledge one exact authorization or publish a reusable acceptance
   manifest for closed Authorization Binding Profile and Authorization
   Trust Profile digest pairs.  A deterministic verifier validates the
   binding, separately classifies evidence claiming pre-execution
   verification by the executor, and reports forum-selection provenance
   as unilateral, multiparty, externally selected, or indeterminate.
   Where a filing is declared to affect execution state, the verifier
   also separates the issuer's declared policy, the executor's signed
   acceptance, the authenticated trigger, and the executor's claimed
   application.

   The mechanism makes the bound contestation parameters identifiable
   and verifiable, supporting discoverability while resisting post-
   action substitution.  It does not determine standing, prove forum
   independence, resolve a dispute, select a remedy, establish legal
   enforceability, or decide whether the original authorization was
   legitimate.
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
- **draft-cowles-ward-00** (new-draft, score 12, agent_identity) [none]: [Write-once Append-only Receipt Digests (WARD): A Content-Free Hash-Chain Witnessing Protocol for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-cowles-ward/) — Write-once Append-only Receipt Digests (WARD) defines a minimal,
   interoperable protocol for producing tamper-evident, content-free
   hash-chain witnesses over events from agentic AI systems.  WARD
   observes events from companion protocols (Agent Envelope Exchange
   (AEE) messages, Agent Orchestration Control Layers (AOCL) decisions,
   and Verifiable Operations Ledger and Trace (VOLT) evidence records)
   and produces cryptographically linked receipts that prove specific
   events existed at specific points in time, without storing any event
   content.

   WARD entries record only source identifiers and payload hashes, never
   raw payloads, secrets, or personally identifiable information.
   Entries are linked via SHA-256 hash chains anchored by deterministic
   genesis hashes.  Periodic checkpoints called "tips" may be signed
   with Ed25519 and published to external append-only stores (sinks) for
   independent verification.  A meta-chain pattern allows witnessing
   tips from multiple sub-chains, providing deployment-wide integrity
   from a single verification point.

   The protocol is designed as a passive observer: witnessing never
   blocks, delays, or modifies the source event pipeline.  WARD failures
   are logged but never disrupt AEE transport, AOCL decisions, or VOLT
   recording.  This fire-and-forget integration model ensures that
   witnessing adds tamper-evidence guarantees without introducing
   operational risk.
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
- **draft-ietf-acme-pop-00** (new-draft, score 12, core_identity) [acme]: [Automated Certificate Management Environment (ACME) Extension for Proof-of-Possession](https://datatracker.ietf.org/doc/draft-ietf-acme-pop/) — The Automated Certificate Management Environment (ACME) protocol
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
   popKey field and includes a pop-type identifier whose value is the
   empty string.  The server creates a dedicated pop authorization
   containing a single pop-01 challenge, processed using the same state
   machine as any other ACME authorization.  When all authorizations
   (including the pop authorization) are valid, the ACME server issues a
   certificate using the validated public key and the authorized
   identifiers, eliminating the need for a CSR at finalization.  The
   extension is additive and strictly optional: clients that do not use
   it, and servers that do not support it, continue to use the standard
   CSR-based flow defined in [RFC8555] without any changes.
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
- **draft-morrison-identity-accord-03** (new-draft, score 12, core_identity) [none]: [Identity Accord Protocol: A Peer Ceremony for Bilateral Agreements Between Identity-Substrate-Bound Principals](https://datatracker.ietf.org/doc/draft-morrison-identity-accord/) — This memo specifies the Identity Accord Protocol, a peer ceremony by
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
- **draft-sun-rats-composite-eat-00** (new-draft, score 12, trust_infrastructure) [none]: [An EAT Profile for Composite Platform Attestation](https://datatracker.ietf.org/doc/draft-sun-rats-composite-eat/) — This document defines an Entity Attestation Token (EAT) profile for
   composite platform attestation.  A Lead Attester, such as a platform
   Root of Trust, produces a single signed composite EAT that carries
   its own measurements and cryptographic digests committing to
   detached, native evidence collected from peripheral sub-attesters.
   The full sub-attester evidence -- Security Protocol and Data Model
   (SPDM) signed measurements, device-emitted EATs, or SPDM-carried TCG
   DICE Concise Evidence -- is conveyed verbatim as detached Claims-Sets
   in a Detached EAT Bundle.  This yields a single, freshness-bound,
   platform-scoped attestation artifact that a Verifier can appraise
   against platform-composition endorsements, even when the evidence is
   collected and conveyed by an untrusted mediator.
- **draft-cowles-aee-01** (new-draft, score 11, core_identity) [none]: [Agent Envelope Exchange (AEE): A Minimal JSON Envelope Format for Inter-Agent Communication](https://datatracker.ietf.org/doc/draft-cowles-aee/) — Agent Envelope Exchange (AEE) defines a minimal, transport-
   independent JSON envelope format for communication between autonomous
   AI agents, traditional services, and human participants.  The
   envelope comprises 14 well-defined fields that provide message
   identity, typing, correlation, tracing, priority, and extensibility
   without prescribing payload semantics or transport mechanisms.  AEE
   separates the concerns of message routing and lifecycle management
   (the envelope) from domain-specific meaning (intent schemas),
   enabling portable, composable, and auditable workflows across
   heterogeneous agent frameworks.  This document specifies the envelope
   structure, validity rules, conformance levels, entity identifier
   conventions, a reserved intent namespace for protocol negotiation,
   and a referencing strategy that avoids envelope nesting.
- **draft-das-child-safe-rendering-finality-03** (new-draft, score 11, core_identity) [none]: [Preventing Unauthorized Adult and Age-Restricted Content Rendering to Children Through Hardware-Rooted Execution Finality](https://datatracker.ietf.org/doc/draft-das-child-safe-rendering-finality/) — Online child-safety controls commonly operate before the final
   rendering boundary.  Platforms may use account-age flags, parental
   settings, content labels, recommender controls, server-side
   classification, age-assurance systems, access policies, or
   application filters to decide whether adult or age-restricted content
   should be available to a user.  Those controls are important, but an
   upstream decision does not by itself guarantee that the content
   cannot later be decrypted, decoded, composited, rendered, forwarded,
   mirrored, or otherwise materialized through another software or
   device path.

   The practical motivation is also personal.  As a father of three, I
   have encountered this same problem in my own family: a parent may
   understand that an unrestricted adult-configured phone should not be
   handed to a minor, yet a son or daughter may repeatedly ask to use
   the parent's phone and, in ordinary family life, the parent may
   eventually hand it over.  Human affection, trust, convenience, and
   everyday family circumstances cannot simply be designed away.
   Existing age checks, parental controls, child profiles, and
   application restrictions are useful, but they do not necessarily
   provide a simple device-wide protection for this moment of handover.
   Requiring the adult to provide a fingerprint, facial verification, or
   other authentication for every individual video would also create an
   impractical user experience.  This document therefore considers a
   Temporary Under-18 Handover Mode: before giving an adult-configured
   device to a child, the adult can place the device into a temporary
   minor-protection state, after which Execution-Finality makes that
   state technically consequential at the protected rendering boundary.
   This is therefore not only an abstract design problem for me; it is a
   solution developed to address a problem I encounter myself as a
   parent, with the broader aim of turning that everyday family
   difficulty into a practical protection that may also help other
   families.

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
- **draft-dogru-cedulon-06** (new-draft, score 11, verifiable_claims) [none]: [Cedulon: An Audit Layer for Agent-to-Agent Commerce](https://datatracker.ietf.org/doc/draft-dogru-cedulon/) — This document defines the Cedulon Protocol, an audit layer for agent-
   to-agent commerce.  Payment rails such as HTTP 402 flows (x402) and
   mandate protocols (AP2) already move value, and a mandate protocol
   can already refuse a spend before it happens and return signed
   receipts.  What they do not, by themselves, give a party that is
   neither payer nor rail operator is a retrievable record of that
   decision and a signed spend receipt that reconciles against an
   authenticated extract of the rail.  Cedulon specifies a Trade
   Manifest (signed offer before payment), a Policy Decision Point with
   default deny, a Spend Receipt (COSE/CWT claim set after a gated
   payment), epoch checkpoints, and rail-extract reconciliation.  The
   reconciliation shows that no settlement on the extract lacks a
   receipt and no settled receipt is absent from the extract.  That
   result is unconditional only when the verifier pins the rail key out
   of band and states the period under audit; otherwise the document
   requires it to be reported as conditional.  Checkpoints carry the
   suppression guarantee, so the document profiles the checkpoint as a
   Signed Statement, gives the verification algorithm a step that
   consumes the witness receipts returned for checkpoints, names what a
   witness holding a checkpoint the presented chain omits reports,
   brings equivocation within reach by comparing recorded copies against
   the presented chain, and states how checkpoint totals may be withheld
   without withholding the fact that they were.  No signed object may be
   verified against a key it carries itself, and a presented Trade
   Manifest must be bound both to the receipts that name it and to the
   terms those receipts claim.  The document also names a threat no
   adversary causes, a settlement recorded on a rail with no receipt
   behind it, and defines a Dispute Evidence Bundle (evidence, not an
   award) and optional SCITT anchoring.  The encodings earlier revisions
   called canonical are defined, and the exact input to every hash-
   valued field is stated, so that an independent verifier can be
   written from the text alone.  This revision adds the JSON counterpart
   of the CBOR duplicate-key rule, names the refusal of a non-empty
   unprotected header, and requests registration of the five media types
   the profile carries in its protected headers.  Cedulon is not a
   competitor to x402 or AP2; it sits above them.
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
- **draft-saha-aadp-02** (new-draft, score 11, core_identity) [none]: [The Agent Action Decision Protocol (AADP): Per-Action Authorization for AI Agents](https://datatracker.ietf.org/doc/draft-saha-aadp/) — The Agent Action Decision Protocol (AADP) separates per-action
   authorization from an agent's identity and its standing capabilities,
   and gives that authorization semantics that a stateless tool
   permission or access grant cannot express: whether a specific
   proposed action, with specific argument values, may be performed now,
   given mutable state such as cumulative budgets, live reservations,
   approval lifecycle, and a kill switch.  Existing agent-security work
   concentrates on identity -- who an agent is, what credentials it
   holds, and which tools it may reach; AADP addresses the complementary
   decision, and composes with that work rather than replacing it.  This
   document defines a two-phase wire contract between a Policy Decision
   Point (PDP) that authorizes agent actions and the Policy Enforcement
   Points (PEPs) that perform them: verdicts with machine-readable
   reasons, obligations that fail closed, atomic budget reservation, an
   approval lifecycle, idempotency behavior, evidence sufficient to re-
   derive every verdict, and a set of evaluation invariants any
   conformant decision point must observe -- including the rule that an
   irreversible action is never executed autonomously.  The protocol is
   transport-agnostic and is designed so that decision points and
   enforcement points can be implemented independently, in different
   languages, by different parties.
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
- **draft-cowles-volt-01** (new-draft, score 10, agent_identity) [none]: [Verifiable Operations Ledger and Trace (VOLT) Protocol](https://datatracker.ietf.org/doc/draft-cowles-volt/) — The Verifiable Operations Ledger and Trace (VOLT) protocol defines a
   minimal, interoperable format for producing tamper-evident execution
   traces for agentic AI workflows.  VOLT records are linked via SHA-256
   hash chains and packaged into portable Evidence Bundles that can be
   verified independently by any conformant implementation.

   VOLT functions as a "flight recorder" for AI agent operations: it
   captures the sequence of events -- messages received, policy
   decisions evaluated, human approvals granted, tools invoked, and
   results returned -- with cryptographic integrity guarantees that
   detect post-hoc modification, deletion, or insertion of records.

   The protocol is privacy-first by design.  Events carry metadata and
   content-addressed references rather than raw secrets or sensitive
   payloads.  Evidence Bundles support explicit redaction, optional
   Ed25519 signatures for non-repudiation, and both rolling and final
   snapshot modes for long-running workflows.
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
- **draft-mih-scitt-checkpointed-local-log-00** (new-draft, score 10, trust_infrastructure) [none]: [The Checkpointed Local Log (CLL)](https://datatracker.ietf.org/doc/draft-mih-scitt-checkpointed-local-log/) — Many systems emit individually signed records — receipts,
   attestations, statements — and store them locally.  Each record
   verifies on its own, but the collection proves nothing: records can
   be deleted, reordered, or created after the fact without detection.
   This document specifies the Checkpointed Local Log (CLL): a producer-
   operated append-only log, built on the Merkle Mountain Range
   structure whose COSE proof formats are specified in
   [I-D.bryce-cose-receipts-mmr-profile], together with a small signed
   checkpoint that commits to the log's entire history.  Records of any
   format are appended as they are produced; checkpoints are emitted on
   a declared cadence and may be registered with one or more independent
   Transparency Services or witnesses using existing SCITT registration.
   A CLL upgrades a set of point receipts into a stream with provable
   order, contemporaneity, and completeness — while defining precisely,
   and narrowly, what such a log does and does not establish.  This
   document defines the log discipline and the checkpoint structure; it
   defines no new proof formats, no transparency service behavior, and
   no payload semantics.
- **draft-surampudi-wtx1-01** (new-draft, score 10, authorization) [none]: [WTX-1: Cross-Domain Context Preservation Protocol](https://datatracker.ietf.org/doc/draft-surampudi-wtx1/) — This document defines WTX-1, a protocol for preserving pseudonymous
   user context across web domains that are operated by, or on behalf
   of, the same organization and that have mutually opted into the
   exchange.  The protocol operates only after explicit user consent and
   does not use third-party cookies, browser fingerprinting, or
   collection of direct identifiers by default.  Identifiers are
   pseudonymous, not anonymous: they can be linked to application-level
   identities by the deploying organization and may constitute personal
   data under applicable law.

   WTX-1 transfers context using an encrypted, authenticated,
   destination-bound, single-use token carried in the URL fragment.
   Tokens are issued and verified server side, with atomic replay
   consumption, DNS-based domain authorization, and short-lived server-
   signed write grants that authorize browser write operations without
   trusting caller-supplied tenant claims.

   This revision (draft-02) replaces the signed-cleartext token format
   of draft-01 with a sign-then-encrypt construction, specifies write
   grants and replay-consumption ordering, defines the consent lifecycle
   including withdrawal and asynchronous cancellation, adds storage
   retention limits and user inspection, reset, and revocation controls,
   and rescopes the document's security, privacy, and performance claims
   to match the reviewed reference implementation.  A complete change
   log appears in Appendix A.
- **draft-abak-agent-control-delivery-evidence-00** (new-draft, score 9, authorization) [none]: [Evidence Requirements for Agent Control Delivery and Outcome Reconciliation](https://datatracker.ietf.org/doc/draft-abak-agent-control-delivery-evidence/) — Agent systems can issue stop, suspend, revoke, constrain, cancel, or
   override instructions across system and administrative boundaries.  A
   record that such a control was decided or dispatched does not
   establish that the intended enforcement point received or applied it.
   Conversely, the absence of an acknowledgement does not, by itself,
   establish non-delivery.

   This document defines format-independent evidence requirements for
   preserving that distinction.  It separates issuer-side emission,
   receiver-side observation, enforcement outcome, and observation of
   the resulting control effect.  It also defines negative-observation
   rules, per-instruction reconciliation states, and bounded-population
   accounting so that missing, malformed, conflicting, and unmatched
   records remain visible.

   This document does not define a receipt format, wire protocol,
   authorization system, policy language, transparency service, or audit
   regime.
- **draft-chu-oauth-subject-key-binding-00** (new-draft, score 9, authorization) [none]: [OAuth Subject Signing Key Binding for Resource Servers](https://datatracker.ietf.org/doc/draft-chu-oauth-subject-key-binding/) — Resource servers in OAuth deployments sometimes receive application-
   layer authorization evidence that is digitally signed by the subject
   represented by an access token.  Verification of such evidence
   requires the resource server to obtain a trusted public signing key
   that is bound to that subject.

   This specification defines the subject_keys parameter, by which an
   OAuth authorization server conveys one or more subject public signing
   keys to a resource server.  The parameter can be carried as a claim
   in a JWT access token or as a member of a token introspection
   response.  The resulting key binding is scoped to the authorization
   server, token subject, resource server audience, and token validity
   context.

   This specification does not define a public-key enrollment protocol
   or the syntax and semantics of the application-layer authorization
   evidence.  It also does not use the OAuth cnf claim, which identifies
   a proof-of-possession key held by the presenter of a token.
- **draft-fassbender-scitt-time-anchor-05** (new-draft, score 9, trust_infrastructure) [none]: [Bitcoin-Anchored Temporal Proof for Transparency Services](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document defines a mechanism for temporal anchoring of digital
   artifacts by committing cryptographic hashes to the Bitcoin
   blockchain via the OpenTimestamps protocol.  The resulting proof is
   independently verifiable by any party with access to independently
   validated Bitcoin chain data, without contacting the anchoring
   service.  The SCITT Architecture is used as the primary integration
   example.  No changes to the SCITT architecture are required.
- **draft-hamr-oauth-agent-delegation-00** (new-draft, score 9, authorization) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document specifies a profile for delegating authorization to
   automated agents across administrative domains.  It defines an HTTP
   header field, Agent-Delegation, that carries a chain of attenuated
   delegation links.  Each link narrows the scope, tightens or holds a
   set of floor conditions, and shortens or holds the expiry of its
   parent.  A verifier checks every link in the chain, not only the
   last, and rejects the chain if any link violates attenuation.  The
   profile is deliberately agnostic to the credential format and to the
   nature of the entity that issues floor attestations; it specifies
   required properties, not a specific encoding or a specific kind of
   issuer.  It composes with, and does not replace, existing work on
   agent credential provisioning and posture.
- **draft-kodden-oidfed-admin-00** (new-draft, score 9, core_identity) [none]: [OpenID Federation Node Administration Protocol](https://datatracker.ietf.org/doc/draft-kodden-oidfed-admin/) — This document specifies a compact HTTP application programming
   interface for administering an OpenID Federation node.  The interface
   manages the operator-controlled inputs from which a node produces the
   Entity Configurations, Subordinate Statements, Trust Marks, and
   Federation Entity Keys defined by OpenID Federation 1.1.  It does not
   replace the public federation protocol.  It is the management plane
   used by operators and control-plane software to configure what that
   protocol publishes.

   The design is document-oriented.  Operators read and write the same
   JSON objects OpenID Federation already defines, rather than a large
   set of per-claim endpoints.  Five resources cover node identity,
   Federation Entity Keys, the node's Entity Configuration, Immediate
   Subordinates, and Trust Mark issuance.
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
- **draft-efstathiou-samp-agent-management-01** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
   management-plane protocol for heterogeneous AI agents.  SAMP allows a
   management system to discover agents, query their state, receive
   events, subscribe to event streams, and optionally configure or
   execute explicitly exposed operations under policy control.

   SAMP is inspired by operational management protocols such as SNMP,
   but it is designed for AI-agent-specific concepts such as dynamic
   profiles, autonomy classes, enrollment, trust states, and policy-
   gated execution.  It is not an agent-to-agent communication protocol,
   an agent tool-use protocol, or an agent framework specification.

   This document defines SAMP version 0.1 as an Experimental protocol
   suitable for controlled environments and independent interoperability
   testing.
- **draft-hawkins-scitt-attested-agent-payment-02** (new-draft, score 8, trust_infrastructure) [none]: [Notice of Discontinuation: Attested Agent Payment](https://datatracker.ietf.org/doc/draft-hawkins-scitt-attested-agent-payment/) — This document serves as formal administrative notification that the
   individual Internet-Draft draft-hawkins-scitt-attested-agent-payment
   has been discontinued and will not be progressed as an individual
   submission.
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
- **draft-richardson-rats-geographic-results-02** (new-draft, score 8, trust_infrastructure) [none]: [Geographic Attestation Results](https://datatracker.ietf.org/doc/draft-richardson-rats-geographic-results/) — Many workloads have limitations on what geography they are allowed to
   operate in.  This is often due to a regulation that requires that the
   computation occur in a particular jurisdiction.

   There are many mechanisms by which Evidence of location may be
   created and then evaluated by a Verifier.  No matter which mechanism
   is appropriate for a given situation, the result of the Verification
   can be expressed in a similiarly defined EAT Attestation Result.

   This document is therefore about encoding a variety of geographical
   conclusions in an Attestation Result.  In addition, one mechanism of
   directly creating a geographic result in the form of an Endorsement
   is described in an appendix.
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
- **draft-cowles-aocl-01** (new-draft, score 7, core_identity) [none]: [Agent Orchestration Control Layers (AOCL) Protocol](https://datatracker.ietf.org/doc/draft-cowles-aocl/) — Agent Orchestration Control Layers (AOCL) is a protocol that
   standardizes how an orchestrator processes incoming events by passing
   them through a layered control pipeline.  AOCL defines an eleven-
   layer taxonomy covering ingress normalization, identity scoping,
   smart routing, policy gating, plan decomposition, context retrieval,
   prompt shaping, delegation and execution, verification, response
   assembly, and audit writeback.  The protocol is runtime-agnostic and
   framework-agnostic, producing auditable governance traces as a first-
   class output.  AOCL supports both sequential pipeline and directed
   acyclic graph (DAG) execution modes, with explicit bypass and branch
   semantics that mandate audit records for all control-flow deviations.
- **draft-ietf-ocm-open-cloud-mesh-07** (new-draft, score 7, authorization) [ocm]: [Open Cloud Mesh](https://datatracker.ietf.org/doc/draft-ietf-ocm-open-cloud-mesh/) — Open Cloud Mesh (OCM) is a server federation protocol that is used to
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
- **draft-morrison-binding-moment-envelope-02** (new-draft, score 7, adjacent_watchlist) [none]: [The Briefing-and-Binding Envelope: A Delivery Contract for Agent-to-Principal Decision Moments with Dual-Veto Reconciliation](https://datatracker.ietf.org/doc/draft-morrison-binding-moment-envelope/) — This memo specifies the briefing-and-binding envelope: a delivery
   contract for the wire-level structure by which an artificial-
   intelligence agent surfaces a consequential decision to the human
   principal it acts for, and by which the principal commits, declines,
   amends, or rejects that decision.  The envelope carries eight named
   slots (a synopsis, findings, recommendations, an offer of detail, a
   question stem, a set of options each marked with its own reasoning, a
   single recommended option, and a pair of escape hatches) and is
   emitted as a structured field of a Model Context Protocol [MCP] tool
   result.  The contribution is the delivery contract itself: a single
   renderer-agnostic envelope so that the briefing an agent delivers and
   the binding a principal commits back have one machine-checkable shape
   across every consuming surface.  The central element is the dual-veto
   handshake: one escape hatch lets the principal revise the answer
   space while accepting the question; the other lets the principal
   reject the question itself and reopen deliberation.  Either party may
   veto.  The memo defines a content digest over the envelope,
   canonicalized under JCS and hashed with SHA-256, so that a resolution
   names the exact envelope it resolves and an external receipt can
   reference that envelope by digest.  The memo is Informational.  No
   new transport is introduced; the envelope composes with the handle
   namespace of [IDPRONOUNS] and the MCP tool surface of [POLICYPROV].
- **draft-singh-psi-01** (new-draft, score 7, adjacent_watchlist) [none]: [Proof of Sovereign Integrity (PSI): A Cryptographic Protocol for Verifiable AI Regulatory Compliance](https://datatracker.ietf.org/doc/draft-singh-psi/) — This document specifies the Proof of Sovereign Integrity (PSI)
   Protocol, version 1.2, a cryptographic framework enabling
   organizations to prove compliance with AI regulations (including the
   EU AI Act 2024/1689, NIST AI RMF, UK AI Safety Institute guidelines,
   and equivalent frameworks) without disclosing proprietary model
   architectures, training data, or inference logic.

   PSI achieves this through a combination of SHA-256 hash-chained audit
   trails, Ed25519 digital signatures, Merkle inclusion proofs,
   Groth16-compatible zero-knowledge commitments over BN128 fields, and
   a 3-node Multi-Party Computation (MPC) consensus mechanism with 2/3
   threshold verification.

   This revision documents a deployed public reference implementation
   and adds optional post-quantum signature profiles and Bitcoin
   timestamp anchoring.

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
- **draft-morrison-org-alter-policy-provision-03** (new-draft, score 6, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
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
   stacks, with cross-organisational residual conflicts routed to the
   peer-protocol Identity Accord ceremony [IDACCORD] rather than to a
   meta-federation authority.  The memo is Informational.  The wire
   surface relies on the DNS-based discovery of [MCPDNS] and the handle
   namespace of [IDPRONOUNS]; no new transport is introduced.
- **draft-rajappa-httpbis-connection-contamination-06** (new-draft, score 6, core_identity) [none]: [Mitigating HTTP/3 Connection Contamination in Multi-Tenant and CDN-Fronted Deployments](https://datatracker.ietf.org/doc/draft-rajappa-httpbis-connection-contamination/) — HTTP/3 [RFC9114] clients commonly reuse ("coalesce") an existing QUIC
   [RFC9000] connection for requests to a second origin when the TLS
   certificate presented on that connection is also valid for the second
   origin, even though the two origins may route to entirely different
   backends.  This document describes "connection contamination," a
   class of security exposure that arises when a routing layer --
   reverse proxy, load balancer, or CDN edge -- determines backend
   routing using a signal established at connection setup rather than
   re-validated per request.  Under that condition, a coalesced
   connection can be used to reach an unintended backend origin,
   potentially enabling cross-tenant data leakage, authentication
   bypass, and response-queue interference analogous to HTTP request
   smuggling.

   This document defines the underlying mechanism, characterizes the
   attacker model, distinguishes connection contamination from related
   QUIC exposures, and provides normative operational guidance for
   implementers and operators of HTTP/3-terminating infrastructure.
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
- **draft-ietf-webbotauth-httpsig-protocol-00** (new-draft, score 5, core_identity) [webbotauth]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-li-cats-aisemantic-contract-01** (new-draft, score 5, adjacent_watchlist) [none]: [Semantic-Driven Traffic Shaping Contract for AI Networks](https://datatracker.ietf.org/doc/draft-li-cats-aisemantic-contract/) — This document defines a "Semantic-Driven Shaping Contract".
   Traditional network protocols treat AI training and inference traffic
   as opaque byte streams, leading to highly inefficient scheduling.
   This contract allows applications or distributed training frameworks
   to explicitly pass "minimum necessary semantics" to the underlying
   network.  In exchange, the network commits to executing fine-grained,
   differentiated forwarding and resource allocation actions for tensor
   flows with diverse semantics, based on predefined rules and global
   real-time states.  This model significantly improves overall resource
   utilization and task completion times in heterogeneous computing
   networks, cross-domain intelligent computing centers, and integrated
   training-inference scenarios.
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
- **draft-watts-scientific-admissibility-evidence-00** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Admissibility Evidence Records for Verifiable Research Provenance](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility-evidence/) — This document describes a portable JSON evidence-record format for
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

- **draft-behring-cvd-policy-00** (new-draft, score 3, authorization) [none]: [Machine-Readable Coordinated Vulnerability Disclosure Policies](https://datatracker.ietf.org/doc/draft-behring-cvd-policy/) — This document defines a JSON format for machine-readable Coordinated
   Vulnerability Disclosure (CVD) policies.  It also defines the
   proposed CVD-Policy field for discovery through security.txt and
   requests registration of the application/cvd-policy+json media type.
   The format complements security.txt and human-readable policy
   documents.  A policy does not prove ownership and does not establish
   legal authorization to test, legal safe harbor, or the safety of an
   activity.
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
- **draft-bormann-cbor-cddl-csv-09** (new-draft, score 3, adjacent_watchlist) [none]: [Using CDDL for CSVs](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-csv/) — The Concise Data Definition Language (CDDL), standardized in RFC
   8610, is defined to provide data models for data shaped like JSON or
   CBOR.

   Another representation format that is quote popular is the CSV
   (Comma-Separated Values) file as defined by RFC 4180.

   The present document shows a way how to use CDDL to provide a data
   model for CSV files.
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
- **draft-ietf-ccamp-optical-path-computation-yang-09** (new-draft, score 3, adjacent_watchlist) [ccamp]: [YANG Data Models for requesting Path Computation in WDM Optical Networks](https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-path-computation-yang/) — This document provides a mechanism to request path computation in
   Wavelength-Division Multiplexing (WDM) optical networks composed of
   Wavelength Switched Optical Networks (WSON) and Flexi-Grid Dense
   Wavelength Division Multiplexing (DWDM) switched technologies.  This
   model augments the Remote Procedure Calls (RPCs) defined in RFC YYYY.

   [RFC EDITOR NOTE: Please replace RFC YYYY with the RFC number of
   draft-ietf-teas-yang-path-computation once it has been published.
- **draft-ietf-ccamp-yang-otn-slicing-12** (new-draft, score 3, adjacent_watchlist) [ccamp]: [Framework and Data Model for OTN Network Slicing](https://datatracker.ietf.org/doc/draft-ietf-ccamp-yang-otn-slicing/) — The requirement of slicing network resources with desired quality of
   service is emerging at every network technology, including the
   Optical Transport Networks (OTN).  As a part of the transport
   network, OTN can provide hard pipes with guaranteed data isolation
   and deterministic low latency, which are highly demanded in the
   Service Level Agreement (SLA).

   This document describes a framework for OTN network slicing and
   defines YANG data models with OTN technology-specific augments
   deployed at both the north and south bound of the OTN network slice
   controller.  Additional YANG data model augmentations will be defined
   in a future version of this draft.
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
- **draft-ietf-idr-sdwan-edge-discovery-30** (new-draft, score 3, core_identity) [idr]: [SD-WAN Edge and Underlay Tunnel Discovery Using BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-sdwan-edge-discovery/) — This document specifies BGP mechanisms for SD-WAN (Software-Defined
   Wide Area Network) edge node attribute discovery.  These mechanisms
   comprise a new tunnel type and associated Sub-TLVs for the BGP Tunnel
   Encapsulation Attribute, and a new Subsequent Address Family
   Identifier (SAFI) carrying a typed NLRI for advertising SD-WAN
   underlay tunnel information.
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
- **draft-ietf-lsr-isis-srv6-yang-10** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Data Model for IS-IS SRv6](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-srv6-yang/) — This document defines a YANG data model that can be used to configure
   and manage IS-IS Segment Routing over the IPv6 Data Plane.
- **draft-ietf-mpls-stamp-pw-15** (new-draft, score 3, core_identity) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document specifies encapsulations for the Simple Two-Way Active
   Measurement Protocol (STAMP), defined in RFC 8762, and its optional
   extensions, defined in RFC 8972, in MPLS networks.  It specifies the
   encapsulation of STAMP test packets for point-to-point Label Switched
   Paths (LSPs) and point-to-point single-segment Pseudowires (PWs),
   with or without an IP/UDP header, so that the test packets experience
   the same forwarding and Equal-Cost Multi-Path (ECMP) behavior as the
   data traffic being measured.  In addition, two new MPLS Generic
   Associated Channel (G-ACh) types are defined.

   This document updates RFC 8762 for TTL and IPv6 Hop Limit processing
   and RFC 8972 for the STAMP Session Identifier for LSPs and PWs.
- **draft-ietf-opsawg-ipfix-path-segment-06** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 paths identification.
- **draft-ietf-tcpm-tcp-ao-algs-07** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-ietf-teas-yang-te-mpls-topology-05** (new-draft, score 3, adjacent_watchlist) [teas]: [A YANG Data Model for MPLS-TE Topology](https://datatracker.ietf.org/doc/draft-ietf-teas-yang-te-mpls-topology/) — This document defines a YANG data model for representing, retrieving,
   and manipulating MPLS-TE network topologies.  It is based on and
   augments existing YANG models that describe network and traffic
   engineering packet network topologies.

   This document also defines a collection of common YANG data types and
   groupings specific to MPLS-TE.  These common types and groupings are
   intended to be imported by modules that model MPLS-TE technology-
   specific configuration and state capabilities.

   The YANG models defined in this document can also be used for MPLS
   Transport Profile (MPLS-TP) network topologies.
- **draft-intra-handshake-fail-17** (new-draft, score 3, trust_infrastructure) [none]: [Intra-handshake (aka Early) Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 9.8 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
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
- **draft-lin-opsawg-ipfix-rocev2-01** (new-draft, score 3, ai_infrastructure) [none]: [Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/) — This document defines a new set of IP Flow Information Export (IPFIX)
   Information Elements (IEs) for exporting Base Transport Header (BTH)
   information for RDMA over Converged Ethernet version 2 (RoCEv2)
   traffic.  These extensions enable network monitoring systems to
   collect and analyze the characteristics of RDMA traffic widely used
   in high-performance computing, storage, and artificial intelligence
   applications.
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
- **draft-morrison-alter-uri-scheme-03** (new-draft, score 3, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
   reference syntax for ~handle identity references published under the
   DNS substrate defined in [MCPDNS].  An alter: URI binds a textual
   ~handle reference to a resolution and verification procedure that
   retrieves the handle's envelope from the publishing zone, validates
   the envelope's signature chain, and dispatches the result to an
   operating-system URI handler.  The reference may be scoped to an
   organisation, narrowed to a named facet of the identity, and
   addressed to a typed action surface.  The scheme is the addressing
   form of the ~handle@org:facet/action reference; its resolution
   semantics are those of [MCPDNS], reused without modification.

   The scheme is provider-neutral, introduces no new cryptographic
   primitive, and reuses the resolution and verification procedures of
   [MCPDNS] without modification.  The principal contribution is a
   single, self-verifying dispatch surface for handle-typed references:
   clicking, typing, or scanning an alter: URI yields a verified handle
   resolution rather than a free-text string or an unauthenticated
   fetch, and where an action is addressed it yields a verify-before-
   side-effect dispatch.  This document requests provisional
   registration of the alter scheme with IANA per [RFC7595] Section 3.
- **draft-nordin-ocm-integration-protocol-01** (new-draft, score 3, adjacent_watchlist) [ocm]: [Open Cloud Mesh Integration Protocol](https://datatracker.ietf.org/doc/draft-nordin-ocm-integration-protocol/) — The Open Cloud Mesh Integration Protocol (OCM-IP) defines how an Open
   Cloud Mesh (OCM) Server can integrate supporting servers, such as
   SSH/SFTP servers, web application platforms, or stand-alone WebDAV
   servers, to perform protocol-specific work on its behalf.

   OCM-IP makes it possible for existing OCM Servers to offload protocol
   specific interactions to stand-alone servers, or even implement OCM
   as a lightweight server that handles only the OCM parts of a
   deployment: discovery, share creation, token issuance and signing.
   Anything protocol-specific, such as serving files over WebDAV,
   providing SSH access, or running an interactive web application, can
   be handed off to one or more Protocol Servers running elsewhere,
   possibly operated with different software and on different
   infrastructure.

   OCM-IP defines three integration modes: a provisioned mode, in which
   the OCM Server pushes Share information to the Protocol Server over a
   signed back channel; a self-contained mode, in which the Share
   information is embedded in the signed access token itself, so that
   the Protocol Server needs no per-share state and no inbound API at
   all; and an introspected mode, in which the Protocol Server validates
   presented credentials through a token introspection endpoint,
   restoring compatibility with Receiving Servers that do not support
   token exchange.

   OCM-IP is a protocol between the Sending OCM Server and its Protocol
   Servers only.  The Receiving Server is not involved in, and does not
   need to be aware of, this protocol: everything it observes is
   indistinguishable from the Sending Server serving the access
   protocols itself.  For this reason, an OCM Sending Server MAY adopt a
   different strategy to interoperate with Protocol Servers, including
   e.g. establishing trust via shared keys, without compromising
   compliance with the OCM protocol.
- **draft-reddy-tls-composite-mldsa-12** (new-draft, score 3, core_identity) [none]: [Use of Composite ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-reddy-tls-composite-mldsa/) — Compositing the post-quantum ML-DSA signature with traditional
   signature algorithms provides protection against potential breaks or
   critical bugs in ML-DSA or the ML-DSA implementation.  This document
   specifies how such a composite signature can be formed using ML-DSA
   with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide
   authentication in TLS 1.3, including use in certificates.
- **draft-richardson-rats-composite-attesters-05** (new-draft, score 3, trust_infrastructure) [none]: [Taxonomy of Composite Attesters](https://datatracker.ietf.org/doc/draft-richardson-rats-composite-attesters/) — This document was attempting to clarifys and extends the meaning of
   Composite Attester from RFC9334.  It has since been moved into the
   RATS wiki, and this I-D serves as a tombstone.

   A system of annotated diagram components is defined as a small
   language to explain the different ways that components can interact
   to form composites.

   These diagram components are then used to define a few popular
   classes of composites.
- **draft-scalone-cfr-source-privacy-02** (new-draft, score 3, core_identity) [none]: [Customer-Facing Relay (CFR): Enhancing Source Privacy in Encrypted Transport and CDN Scenarios](https://datatracker.ietf.org/doc/draft-scalone-cfr-source-privacy/) — Encrypted ClientHello (ECH) protects sensitive TLS ClientHello
   fields, including the Server Name Indication (SNI), from on-path
   observers.  ECH does not, however, attempt to hide the client's
   network-layer source identity from the ECH client-facing server
   (CFS).  In split-mode deployments, the CFS decrypts the
   ClientHelloInner in order to route the connection to the appropriate
   backend while also receiving the connection from the client's visible
   source address.

   This creates a distinct source-privacy problem.  Where ECH service
   and content front-door infrastructure are concentrated, a relatively
   small number of providers can obtain a privileged vantage point from
   which a stable source address can be correlated with many encrypted
   destinations and with other service telemetry.  Measurements over a
   corpus of approximately one million domains, together with an active-
   ECH validation subset, show substantial front-door concentration and
   motivate treating source privacy as a complement to destination
   privacy.

   This document describes the Customer-Facing Relay (CFR), a network-
   layer, access-side source-aliasing function.  A CFR forwards
   encrypted TCP or UDP traffic without terminating TLS or QUIC and
   replaces the subscriber-visible source address with a shared or
   short-lived source alias.  The document also examines the different
   privacy properties of IPv4 NAT/CGN and IPv6 source addressing and
   identifies requirements for privacy-preserving source mapping.
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
- **draft-xls-intarea-evn6-06** (new-draft, score 3, core_identity) [none]: [EVN6: Mapping of Ethernet Virtual Network to IPv6 Underlay for Transmission](https://datatracker.ietf.org/doc/draft-xls-intarea-evn6/) — This document describes a mechanism of mapping of Ethernet Virtual
   Network to IPv6 Underlay for transmission.  Unlike the existing
   methods, this approach places the Ethernet frames to be transmitted
   directly in the payload of IPv6 packets, i.e., L2 over IPv6, and uses
   stateless mapping to generate IPv6 source and destination addresses
   from the host's MAC addresses, the Ethernet Virtual Network
   identifier and site prefixes.  The IPv6 packets generated in this way
   carry Ethernet frames and are routed to the destination site across
   the public IPv6 network.
- **draft-xu-ccamp-impairment-info-sharing-problem-01** (new-draft, score 3, adjacent_watchlist) [none]: [Problem Statement: Information Sharing of Optical Impairments in Monitoring of Multi-Domain All-Optical Paths](https://datatracker.ietf.org/doc/draft-xu-ccamp-impairment-info-sharing-problem/) — In multi-domain all-optical Wavelength Switched Optical Networks
   (WSONs), end-to-end services may traverse multiple administrative
   domains operated by different entities.  Monitoring such services
   requires visibility into optical impairments that accumulate across
   domain boundaries.  However, exchanging impairment-related
   information raises operational, scalability, and confidentiality
   concerns.  Detailed metrics such as attenuation, noise, nonlinear
   effects, and filtering penalties may be necessary for accurate
   performance assessment, yet they can expose sensitive topology,
   equipment, or utilization information.

   This document describes the problem space associated with sharing
   optical impairment information across administrative domains for
   monitoring purposes.  It highlights the need to balance operational
   visibility and confidentiality preservation, and outlines
   considerations for abstraction, information granularity, and trust
   relationships among participating operators.
- **draft-ybam-ccamp-rfc8561bis-02** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Microwave Radio Link](https://datatracker.ietf.org/doc/draft-ybam-ccamp-rfc8561bis/) — This document defines a YANG data model for control and management of
   radio link interfaces and their connectivity to packet (typically
   Ethernet) interfaces in a microwave/millimeter wave node.  The data
   nodes for management of the interface protection functionality is
   broken out into a separate and generic YANG data model in order to
   make it available for other interface types as well.  This document
   obsoletes RFC 8561.
- **draft-yl-cats-data-model-09** (new-draft, score 3, adjacent_watchlist) [cats]: [Data Model for Computing-Aware Traffic Steering (CATS)](https://datatracker.ietf.org/doc/draft-yl-cats-data-model/) — This document defines a YANG data model for the management of
   Computing-Aware Traffic Steering (CATS) systems.
- **draft-zheng-ccamp-client-pm-yang-15** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Client Signal Performance Monitoring](https://datatracker.ietf.org/doc/draft-zheng-ccamp-client-pm-yang/) — A transport network is a server-layer network to provide connectivity
   services to its client.  Given the client signal is configured, the
   followup function for performance monitoring, such as latency and bit
   error rate, would be needed for network operation.

   This document describes the data model to support the performance
   monitoring functionalities.
- **draft-aegisfs-secdispatch-rats-01** (new-draft, score 2, ignored_after_review) [none]: [AegisFS: AI-Driven Programmable Secure File Runtime and Intelligent Workspace Architecture with Octal OpCode Processing and Policy-Driven Language Architecture](https://datatracker.ietf.org/doc/draft-aegisfs-secdispatch-rats/) — This document specifies AegisFS, a programmable secure file and
   folder runtime that transforms ordinary filesystem objects into
   intelligent, policy-driven, state-aware, execution-aware, and
   behavior-aware security objects.

   This draft introduces two novel technical contributions:
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
- **draft-li-cats-intellinode-network-scheduling-01** (new-draft, score 2, ignored_after_review) [none]: [IntelliNode: In-Network Intelligent Scheduling Extensions for CATS](https://datatracker.ietf.org/doc/draft-li-cats-intellinode-network-scheduling/) — This document introduces IntelliNode, an in-network intelligent
   scheduling mechanism built upon the Computing-Aware Traffic Steering
   (CATS) framework.  Modern large-scale AI training and inference
   heavily rely on distributed heterogeneous clusters (GPU/CPU/FPGA).
   However, existing networks lack awareness of tensor semantics,
   training phases, and heterogeneous computing capabilities, leading to
   high communication latency, low resource utilization, and pipeline
   stalls.

   IntelliNode shifts away from the traditional passive scheduling
   paradigms that rely on probes and controllers.  By bypassing
   traditional paths and integrating FPGAs alongside programmable Switch
   ASICs, it constructs a rapid data-plane closed loop of "Perception-
   Inference-Decision-Execution".  This architecture performs feature
   extraction at line rate, leverages lightweight prediction models to
   infer short-term network behavior, and drives real-time heuristic
   scheduling decisions (e.g., path selection, tensor slicing, and
   compute matching).  This document defines the four core functional
   layers and extension signaling that support this architecture, laying
   the foundation for an AI-native, scalable distributed computing
   network.
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
- **draft-dikshit-netmod-comparability-scope-extension-00** (new-draft, score 1, authorization) [none]: [A YANG Extension for Declaring the Comparability Scope of Operational State](https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/) — Several YANG modules currently in progress across multiple IETF
   working groups define counters, gauges, and other measured values
   that are exported from a network element and compared, summed, or
   averaged by a remote collector, either against the same node's
   history or against values from a different node. YANG (RFC 7950)
   has no first-class, machine-checkable way to state the domain
   within which two occurrences of such a value are comparable, so
   this determination is currently made, inconsistently or not at
   all, in prose. This document defines a YANG extension statement,
   "csc:comparability-scope", a four-value scope lattice, and a
   compatibility rule that lets a schema-aware tool statically detect
   an illegal aggregation across incomparable scopes, without waiting
   for it to happen at a collector.

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
- **draft-bormann-cbor-cddl-2-draft-09** (new-draft, score 0, ignored_after_review) [none]: [CDDL 2.0 and beyond -- a draft plan](https://datatracker.ietf.org/doc/draft-bormann-cbor-cddl-2-draft/) — The Concise Data Definition Language (CDDL) today is defined by
   RFC 8610, RFC 9165, RFC 9682, and RFC 9741).  RFC 9165 and the latter
   (as well as some more application specific specifications such as
   RFC 9090) have used the extension point provided in RFC 8610, the
   control operator.

   As CDDL is used in larger projects, feature requirements become known
   that cannot be easily mapped into this single extension point.
   Hence, there is a need for evolution of the base CDDL specification
   itself.

   The present document provides a roadmap towards a "CDDL 2.0"; it is
   intended to serve as a basis for implementations that evolve with the
   concept of CDDL 2.0.  It is based on draft-bormann-cbor-cddl-freezer,
   but is more selective in what potential features it takes up and more
   detailed in their discussion.  This document is intended to evolve
   over time; it might spawn specific documents and then retire, or it
   might eventually be published as a roadmap document.
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
- **draft-bormann-restatement-06** (new-draft, score 0, ignored_after_review) [none]: [The Restatement Anti-Pattern](https://datatracker.ietf.org/doc/draft-bormann-restatement/) — Normative documents that cite other normative documents often
   _restate_ normative content extracted out of the cited document in
   their own words.

   The present memo explains why this can be an Antipattern, and how it
   can be mitigated.
- **draft-buckeyne-jsox-format-00** (new-draft, score 0, ignored_after_review) [none]: [The JavaScript Object eXchange (JSOX) Data Interchange Format](https://datatracker.ietf.org/doc/draft-buckeyne-jsox-format/) — JavaScript Object eXchange (JSOX) is a lightweight, text-based,
   language-independent data interchange format.  It is derived from
   JSON and from the object literal syntax of the ECMAScript Programming
   Language Standard.  Every well-formed JSON text is a well-formed JSOX
   text.

   JSOX extends JSON with unquoted identifiers, additional string
   quoting and escape forms, comments, additional number forms including
   dates and arbitrary-precision integers, binary typed arrays, user-
   defined types carried by a type tag, field-name macros that remove
   repeated keys from a document, and references that permit shared and
   cyclic structures to be encoded.

   This document defines the JSOX grammar and registers the media type
   "application/jsox".
- **draft-cao-opsawg-ipfix-sav-03** (new-draft, score 0, ignored_after_review) [none]: [Export of Source Address Validation (SAV) Information in IPFIX](https://datatracker.ietf.org/doc/draft-cao-opsawg-ipfix-sav/) — This document specifies the IP Flow Information Export Information
   Elements to export the context and outcome of Source Address
   Validation enforcement data.  These SAV-specific Information Elements
   provide detailed insight into why packets are identified as spoofed
   by capturing the specific SAV rules that triggered validation
   decisions.  This operational visibility is essential for network
   operators to observe SAV enforcement behavior and analyze source
   address spoofing events detected by SAV.
- **draft-chen-grow-enhanced-as-loop-detection-09** (new-draft, score 0, ignored_after_review) [none]: [Enhanced AS-Loop Detection for BGP](https://datatracker.ietf.org/doc/draft-chen-grow-enhanced-as-loop-detection/) — Misconfiguration and malicious manipulation of the BGP `AS_PATH`
   attribute can lead to route hijacking.  This document proposes
   enhancements to BGP [RFC4271] inbound and outbound route processing
   when an AS loop is detected.  This mechanism can be implemented
   directly on devices or deployed in a centralized architecture using
   the BGP Monitoring Protocol (BMP) [RFC7854].  These enhancements
   empower networks to quickly and accurately detect route hijacking and
   malicious path poisoning.

   Two implementation options are proposed:
- **draft-choudhary-rcoap-00** (new-draft, score 0, ignored_after_review) [none]: [Ratcheted CoAP: A Forward-Secure Delta over OSCORE for Highly Constrained Wake-Send-Sleep Devices](https://datatracker.ietf.org/doc/draft-choudhary-rcoap/) — This document specifies RCOAP, a compact, zero-round-trip, link-layer
   agnostic object-security mechanism for highly constrained devices
   that transmit infrequently.  RCOAP is a targeted delta over OSCORE
   ([RFC8613]): instead of a single long-lived Sender Key, RCOAP derives
   a fresh symmetric key for every message via a one-way hash ratchet.
   This bounds the impact of physical device capture to future messages
   only, at the cost of a modest per-message size increase and the loss
   of future secrecy.  RCOAP is explicitly scoped to a narrow niche left
   open between OSCORE and EDHOC ([RFC9528]): devices for which even
   EDHOC's one-time handshake cost is disproportionate to their message
   rate or compute budget.  This document is a first individual
   submission, has not been reviewed by the IETF, and requests feedback
   in particular from the LAKE and CoRE working groups on whether this
   gap is real and worth standardizing, or already adequately covered.
- **draft-davis-ivy-equipment-capability-application-02** (new-draft, score 0, ignored_after_review) [none]: [Equipment Capability Application](https://datatracker.ietf.org/doc/draft-davis-ivy-equipment-capability-application/) — This document applies the generalized capability principles to the
   description of equipment (a physical thing) with applied data
   (configuration state and code (software, firmware etc.)) and shows
   how such capability specifications integrate with base inventory and
   entitlement models as defined in Network Inventory, Software
   Extension and Entitlement YANG models.

   The approach is examined by example, focusing on how the potential
   capabilities of each equipment type-version with applied data are
   described, how these map to entitlements (licensed or policy-
   controlled subsets of capabilities), and how they are instantiated as
   inventory items.  The explanation covers both the capabilities of
   equipment in terms of physical properties and the capabilities of
   equipment with applied data in terms of resultant emergent
   functionality.
- **draft-davis-nmop-generalized-capability-principles-02** (new-draft, score 0, ignored_after_review) [none]: [Generalized Capability Principles](https://datatracker.ietf.org/doc/draft-davis-nmop-generalized-capability-principles/) — This document introduces a framework for capability modeling based on
   the specification and refinement principles established in ITU-T
   G.7711 Annex G (also previously published as ONF TR-512.7.  See
   latest G.7711 release) and the modeling boundaries work documented in
   draft-davis-netmod-modelling-boundaries.  The framework defines how
   component–system capabilities can be explicitly described and refined
   via a process of pruning, refactoring, and occurrence formation.

   This draft version additionally incorporates a sketch of an
   occurrence-semantics kernel.  This kernel is presented here as a
   continuation of the refinement and occurrence-formation principles
   already introduced in the previous version, not as a retrospective
   reinterpretation of them.

   These capability definitions can target detailed operational
   considerations, system interactions, licensing, abstract product
   declarations, or sales and marketing.  The framework supports
   modular, layered, and fractal declarations of networked behavior, and
   provides a foundation for a suite of future IETF drafts aligned with
   ongoing work on photonic plug manifests, entitlement/licensing, IVY
   equipment modeling, energy/thermal considerations and related
   domains.
- **draft-dikshit-bess-evpn-df-hashing-analysis-00** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Consistent Hashing to Designated Forwarder Election Scope Transitions in EVPN](https://datatracker.ietf.org/doc/draft-dikshit-bess-evpn-df-hashing-analysis/) — [RFC8584] defines Highest Random Weight (HRW) as the algorithm for
   Designated Forwarder election in EVPN, and, in Section 3.1, names
   the Consistent Hashing family of algorithms as addressing the same
   object-to-server mapping problem before explicitly declining to
   evaluate them: "these will not be considered here."
   [I-D.ietf-bess-evpn-per-mcast-flow-df-election] subsequently
   introduces a scope transition, from per-(ES,VLAN) to per-
   (ES,VLAN,S,G) election, that is precisely a key-space-resizing
   event of the kind Consistent Hashing was designed to bound churn
   for. This document proposes the applicability analysis RFC 8584
   declined to make: it defines a DF-churn metric, states HRW's and
   Consistent Hashing's known theoretical guarantees against it, and
   sets out an evaluation methodology, using bounded-load Consistent
   Hashing as the specific comparison point, given multicast group
   popularity is known to be highly non-uniform in deployed networks.
- **draft-dikshit-bess-evpn-mobility-crdt-00** (new-draft, score 0, ignored_after_review) [none]: [Modeling EVPN MAC-Mobility Sequence State as a Conflict-Free Replicated Data Type](https://datatracker.ietf.org/doc/draft-dikshit-bess-evpn-mobility-crdt/) — EVPN MAC Mobility, as carried in the MAC Mobility Extended
   Community defined by [RFC7432], uses a per-MAC sequence number to
   let PEs agree on the most recent location of a moving host.
   [I-D.ietf-bess-evpn-umr-mobility] extends this to cross-data-center
   moves via gateways, and already specifies, in some detail, how
   ordinary intra-DC and inter-DC moves are kept consistent: each
   gateway maintains two independent MAC Mobility sequence counters
   per host (one intra-DC, one inter-DC) specifically so that a
   purely local move does not have to be reconciled against the
   interconnect network's state. What that document does not specify
   is what a gateway does if it fails after locally resetting its
   intra-DC counter to zero (Section 5.2, the step taken when a host
   is confirmed to have left every local PE) but before propagating
   that fact onward; no failure-handling or crash-recovery text
   exists anywhere in the document. This document shows that this
   narrower, but concretely unaddressed, gap is a special case of a
   data type with known, formally proven convergence properties, the
   Last-Writer-Wins Register, one member of the Conflict-Free
   Replicated Data Type (CRDT) family, and proposes modeling the
   per-gateway mobility sequence state that way so that a mid-reset
   gateway crash is recovered from as a consequence of the data
   type's algebra rather than requiring a new, separately specified
   recovery procedure.
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
- **draft-dikshit-netconf-yang-push-causal-ordering-00** (new-draft, score 0, ignored_after_review) [none]: [Comparable Sequence Numbers Across Publishers in YANG Datastore Telemetry](https://datatracker.ietf.org/doc/draft-dikshit-netconf-yang-push-causal-ordering/) — YANG Datastore Telemetry, YANG-Push version 2
   [I-D.ietf-netconf-yang-push-2], assigns each publisher a
   monotonically increasing sequence number so a receiver can detect
   loss and reordering. The current design leaves two questions
   unanswered: what happens when the counter wraps, and how a
   receiver aggregating records from more than one publisher is to
   compare sequence numbers that were never defined to be comparable
   across publishers in the first place. Both questions have already
   been studied, and largely settled, in the distributed systems
   literature under the heading of logical and hybrid logical clocks,
   and in deployed streaming systems under the heading of offset and
   epoch numbering. This document evaluates three existing causal-
   ordering primitives against YANG-Push's specific constraints and
   proposes adopting a Hybrid Logical Clock so that the wraparound and
   cross-publisher comparison problems are removed by construction
   rather than patched with a wider counter.
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
- **draft-garg-l2vpn-over-srv6-02** (new-draft, score 0, ignored_after_review) [none]: [Method to enable signaling of L2VPN services using SRv6 extensions](https://datatracker.ietf.org/doc/draft-garg-l2vpn-over-srv6/) — This document describes a mechanism to provide L2VPN services using
   Segment Routing over IPv6 (SRv6), eliminating the need for a separate
   signaling protocol for VPN label distribution.  In current
   deployments, L2VPN services rely on dedicated protocols such as the
   Label Distribution Protocol (LDP) or Border Gateway Protocol (BGP)
   for service label signaling, which adds control-plane complexity.
   The proposed mechanism introduces an SRv6-based extension that
   enables L2VPN service identification within the SRv6 framework,
   reducing control-plane overhead and providing a simplified and
   efficient solution for L2VPN service delivery.
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
- **draft-gould-regext-rdap-server-validation-02** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Server Validation](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-server-validation/) — This document describes an Registration Data Access Protocol (RDAP)
   extension for providing the status of server validations.  Server
   validations can be done for an extensible set of types, with examples
   including validating DNS resolution with the type "dns" and
   validating DNSSEC with the type "dnssec".  The validations can be
   performed synchronously in the provisioning command or asynchronously
   based on a triggering command or a schedule.  The extension will
   provide the status of the validations, by type, performed by the
   server in an RDAP lookup response.
- **draft-gould-regext-rdap-status-set-02** (new-draft, score 0, ignored_after_review) [none]: [Registration Data Access Protocol (RDAP) Extension for Status Set](https://datatracker.ietf.org/doc/draft-gould-regext-rdap-status-set/) — This document describes an Registration Data Access Protocol (RDAP)
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
- **draft-herdes-idr-otc-rs-verification-00** (new-draft, score 0, ignored_after_review) [none]: [Strict Only to Customer (OTC) Verification on Route Server Sessions](https://datatracker.ietf.org/doc/draft-herdes-idr-otc-rs-verification/) — RFC 9234 specifies how an AS receiving a route from a lateral Peer
   can check if route was lekaed, but doesn't specify any checks for
   routes received from Route Server (RS).  This makes quility of
   filtering dependent on whether the RS implements RFC 9234.

   This document updates RFC 9234 by adding complimentary ingress check
   by RS-Client.
- **draft-ietf-bmwg-sr-bench-meth-08** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR)](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) performance for Segment Routing over IPv6 (SRv6) and MPLS (SR-
   MPLS).
- **draft-ietf-dmm-srv6mob-arch-04** (new-draft, score 0, ignored_after_review) [dmm]: [Architecture Discussion on SRv6 Mobile User plane](https://datatracker.ietf.org/doc/draft-ietf-dmm-srv6mob-arch/) — This document describes the solution approach and its architectural
   benefits of transforming mobile session information into routing
   information, leveraging segment routing capabilities, and operating
   within the IP routing paradigm.
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
- **draft-ietf-idr-bgpls-inter-as-topology-ext-40** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extensions for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedures for distributing Border
   Gateway Protocol-Link State (BGP-LS) key parameters for inter-domain
   links between two Autonomous Systems (ASes).  It defines a new type
   within the BGP-LS Network Layer Reachability Information (NLRI) for
   an Inter-AS Link, along with three new Type-Length-Values (TLVs)
   descriptors for the BGP-LS Inter-AS Link.  These BGP-LS extensions
   enable network controllers to collect inter-domain interconnect
   information and automatically compute the inter-AS network topology.

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
- **draft-ietf-ipsecme-diet-esp-11** (new-draft, score 0, ignored_after_review) [ipsecme]: [ESP Header Compression with Diet-ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-diet-esp/) — This document specifies Diet-ESP, a compression mechanism for control
   information in IPsec/ESP communications.  The compression uses Static
   Context Header Compression rules.
- **draft-ietf-ipsecme-eesp-04** (new-draft, score 0, ignored_after_review) [ipsecme]: [Enhanced Encapsulating Security Payload (EESP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp/) — This document describes the Enhanced Encapsulating Security Payload
   (EESP) protocol, which builds on the existing IP Encapsulating
   Security Payload (ESP) protocol.  It is designed to modernize and
   overcome limitations in the ESP protocol.

   EESP adds Session IDs (e.g., to support CPU pinning and QoS support
   based on the inner traffic flow), changes some previously mandatory
   fields to optional, and moves the ESP trailer into the EESP header.
   Additionally, EESP adds header options adapted from IPv6 to allow for
   future extension.  New header options are defined which add a crypt-
   offset to allow for exposing inner flow information for middlebox
   use.
- **draft-ietf-ipsecme-eesp-ikev2-03** (new-draft, score 0, ignored_after_review) [ipsecme]: [IKEv2 negotiation for Enhanced Encapsulating Security Payload (EESP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp-ikev2/) — This document specifies how to negotiate the use of the Enhanced
   Encapsulating Security Payload (EESP) protocol using the Internet Key
   Exchange protocol version 2 (IKEv2).  The EESP protocol, which is
   defined in [I-D.ietf-ipsecme-eesp], provides the same security
   services as Encapsulating Security Payload (ESP), but has richer
   functionality and provides better performance in specific
   circumstances.  This document specifies negotiation of version 0 of
   EESP.
- **draft-ietf-ipsecme-ikev2-diet-esp-extension-08** (new-draft, score 0, ignored_after_review) [ipsecme]: [Internet Key Exchange version 2 (IKEv2) extension for Header Compression Profile (HCP)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-diet-esp-extension/) — This document describes an IKEv2 extension for Header Compression to
   agree on Attributes for Rule Derivation.  This extension defines the
   necessary registries for the ESP Header Compression Profile (EHCP)
   Diet-ESP.
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
- **draft-ietf-manet-inet-gap-analysis-10** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking: Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking problem statement and
   gap analysis.
- **draft-ietf-moq-transport-20** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
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
- **draft-ietf-netconf-restconf-trace-ctx-headers-10** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extension to Support Trace Context Headers](https://datatracker.ietf.org/doc/draft-ietf-netconf-restconf-trace-ctx-headers/) — This document defines an extension to the RESTCONF protocol in order
   to support Trace Context propagation as defined by the W3C.
- **draft-ietf-netconf-trace-ctx-extension-08** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extension to support Trace Context propagation](https://datatracker.ietf.org/doc/draft-ietf-netconf-trace-ctx-extension/) — This document defines how to propagate trace context information
   across the Network Configuration Protocol (NETCONF), that enables
   distributed tracing scenarios.  It is an adaption of the HTTP-based
   W3C specification.
- **draft-ietf-nfsv4-uncacheable-files-12** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable File Data Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-files/) — Network File System version 4.2 (NFSv4.2) clients commonly perform
   client-side caching of file data in order to improve performance.  On
   some systems, applications may influence client data caching
   behavior, but there is no standardized mechanism for a server or
   administrator to indicate that particular file data should not be
   cached by clients for reasons of performance or correctness.  This
   document introduces a new file data caching attribute for NFSv4.2.
   Files marked with this attribute are intended to be accessed with
   client-side caching of file data suppressed, in order to support
   workloads that require predictable data visibility.  This document
   extends NFSv4.2.
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
- **draft-ietf-pim-gaap-21** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
   multicast group address allocation protocol (named GAAP and
   pronounced "gap" as in "mind the gap").  GAAP requires no centralized
   service or coordination for the address-allocation protocol itself,
   though it depends on ASM-capable multicast routing already being
   provisioned in the deployment domain, and deployments using
   encryption or administrative scoping may require additional
   configuration.  The protocol runs among group participants which need
   a unique group address to send and receive multicast packets.
   Tailored for IPv4 and IPv6 networks, this design offers a simple,
   lightweight option rather than extending an existing protocol.  This
   document is Experimental, see Section 8 for the rationale and the
   criteria for concluding the experiment.
- **draft-ietf-pim-ipv6-zeroconf-assignment-11** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the criteria listed in RFC 10019.
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
- **draft-ietf-sidrops-publication-server-bcp-10** (new-draft, score 0, ignored_after_review) [sidrops]: [Best Practices for Operating Resource Public Key Infrastructure (RPKI) Publication Services](https://datatracker.ietf.org/doc/draft-ietf-sidrops-publication-server-bcp/) — This document describes best current practices for operating an RFC
   8181 (A Publication Protocol for the Resource Public Key
   Infrastructure (RPKI)) publication engine and its associated publicly
   accessible rsync (RFC 5781) and RPKI Repository Delta Protocol (RRDP)
   (RFC 8182) repositories.
- **draft-ietf-snac-simple-12** (new-draft, score 0, ignored_after_review) [snac]: [Automatically Connecting Stub Networks to Unmanaged Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-snac-simple/) — This document specifies a set of practices for using IPv6 networking
   to automatically connect stub networks to adjacent infrastructure
   networks, even if they do not otherwise use IPv6.  This is applicable
   in cases such as constrained (Internet of Things) networks where
   there is a need to provide functional parity of service discovery and
   reachability between devices on the stub network and devices on an
   adjacent infrastructure link (for example, a home network).
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
- **draft-ietf-teas-actn-poi-applicability-20** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) to Packet Optical Integration (POI)](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-applicability/) — This document explores the applicability of the Abstraction and
   Control of TE Networks (ACTN) architecture to Packet Optical
   Integration (POI) within the context of IP/MPLS and optical
   internetworking.  It examines the YANG data models defined by the
   IETF that enable an ACTN-based deployment architecture and highlights
   specific scenarios pertinent to Service Providers.

   Existing IETF protocols and data models are identified for each
   multi-technology scenario (packet over optical), particularly
   emphasising the Multi-Domain Service Coordinator to Provisioning
   Network Controller Interface (MPI) within the ACTN architecture
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
- **draft-ietf-v6ops-rfc7915-bis-01** (new-draft, score 0, ignored_after_review) [v6ops]: [IP/ICMP Translation Algorithm](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/) — This document describes the Stateless IP/ICMP Translation Algorithm
   (SIIT), which translates between IPv4 and IPv6 packet headers
   (including ICMP headers).  This document obsoletes RFC 7915.
- **draft-irtf-icnrg-ccnxversioning-01** (new-draft, score 0, ignored_after_review) [icnrg]: [CCNx Content Versioning](https://datatracker.ietf.org/doc/draft-irtf-icnrg-ccnxversioning/) — This document defines a method for content versioning in CCNx,
   enabling the differentiation of content published under the same name
   using version numbers.  This document updates RFC8569 [RFC8569] and
   RFC8609 [RFC8609].
- **draft-jags-intarea-icmp-ext-underlay-info-05** (new-draft, score 0, ignored_after_review) [none]: [ICMP extension to include underlay information](https://datatracker.ietf.org/doc/draft-jags-intarea-icmp-ext-underlay-info/) — Network operators managing overlay networks require visibility into
   underlay network hops during traceroute operations from overlay
   endpoints.  This document defines an ICMP extension object, the
   Underlay Information Object (UIO), which allows underlay head-end
   nodes to encapsulate underlay error information within ICMP error
   messages.  This mechanism provides overlay operators with crucial
   visibility into underlay network paths for troubleshooting.
- **draft-kennedy-dnssd-data-block-01** (new-draft, score 0, ignored_after_review) [none]: [DNS-SD Data Block Encoding for Non-DNS Transports](https://datatracker.ietf.org/doc/draft-kennedy-dnssd-data-block/) — The DNS-SD Data Block (DDB) is a compact TLV encoded container for
   conveying DNS-SD service information over non-IP transports used by
   short-range peer-to-peer or proximity-based advertisement and
   discovery technologies such as the Bluetooth Low Energy Transport
   Discovery Service or NFC Verb NDEF Records.
- **draft-kolomytsev-pshmp-core-00** (new-draft, score 0, ignored_after_review) [none]: [PSHMP Core: Decentralized L4 Overlay for Resilient Data Delivery and Proactive Self-Healing Networks](https://datatracker.ietf.org/doc/draft-kolomytsev-pshmp-core/) — PSHMP Core is a decentralized data delivery and proactive self-
   healing network core designed for distributed systems operating over
   existing IP infrastructure.  PSHMP Core provides an intelligent
   network layer above the existing IP network and enables distributed
   nodes to participate in dynamic multi-hop data delivery without
   requiring changes to the underlying Layer 3 routing infrastructure.

   The architecture is designed around decentralized path selection,
   continuous node and path assessment, dynamic relay chains, proactive
   recovery, and diversity-aware reconstruction of delivery paths.  The
   system can detect degradation of network participants and reconstruct
   affected delivery paths before or during service degradation.  This
   approach is intended to reduce recovery time, improve resilience, and
   maintain reliable data delivery in environments where individual
   nodes, paths, or network segments may become unstable.

   This document provides a high-level architectural overview of PSHMP
   Core, its primary components, operating principles, and potential
   application areas.  This document intentionally does not disclose
   implementation-specific algorithms, internal scoring details,
   proprietary optimization techniques, or other information that may be
   required for commercial implementation.
- **draft-kushwaha-scim-attr-cursor-pagination-01** (new-draft, score 0, ignored_after_review) [none]: [Cursor-Based Pagination and Deferred Retrieval for Multi-Valued Attributes in SCIM 2.0](https://datatracker.ietf.org/doc/draft-kushwaha-scim-attr-cursor-pagination/) — [RFC7643] defines Group.members with the returned: default
   characteristic, so a conformant service provider is required to
   return the attribute in response to GET /Groups/{id}. [RFC7644]
   defines no bound on the number of values that attribute may contain.
   A service provider holding a group with millions of members therefore
   has no conformant and interoperable way to answer a request that a
   client is entitled to make.  In practice providers diverge: they
   truncate silently, reject the request, omit the attribute, or fail.
   A client cannot discover in advance which behavior it will encounter.

   This document defines that missing behavior.  It specifies discovery
   so a client can learn how a service provider treats a high-
   cardinality attribute, a bounded response with a defined continuation
   contract, and rules preventing a partial representation from being
   mistaken for complete resource state.

   The mechanism has two forms.  A request for one resource returns a
   bounded page of one protected multi-valued attribute with an opaque
   cursor when more values exist.  A collection search returns parent
   resources without loading protected attributes, each carrying an
   authoritative link for retrieving that attribute.  The attribute
   remains part of its parent resource; this document does not create a
   top-level resource for each attribute value, and it is not a
   substitute for doing so where independent relationship lifecycle or
   cross-collection query is required (Section 16.4).

   Although the mechanism is defined generally and applies to any
   complex multi-valued attribute a service provider designates as
   protected, the attributes that reach problematic sizes in deployed
   SCIM services are predominantly Group.members and User.groups among
   those defined in [RFC7643], together with implementation-specific
   assignment attributes (Section 3).

   This document updates [RFC7643] and [RFC7644].  It adds attributes to
   existing structures defined by those documents and defines attribute-
   return behavior that replaces the requirements of Section 3.9 of
   [RFC7644] within a negotiated scope.  It does not change the behavior
   of deployments that do not implement it: the modified attribute-
   selection behavior described in Section 4 applies only between a
   service provider that has advertised this capability and a client for
   which deferred retrieval has been established through the negotiation
   mechanisms defined in this document.  It defines discovery metadata,
   the attributeCount and attributeCursor query parameters, response
   metadata, processing and compatibility rules, mutation safety, error
   handling, cursor security, and operational limits.
- **draft-lin-opsawg-ipfix-quic-header-05** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of QUIC Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-quic-header/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements to identify a set of QUIC related information,
   which contained in QUIC Header, QUIC Frame and Stream that traffic is
   being forwarded along with.
- **draft-liu-sidrops-ipfix-bgp-pov-00** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP Prefix Origin Validation in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-liu-sidrops-ipfix-bgp-pov/) — This document defines an IP Flow Information Export (IPFIX)
   Information Element for monitoring the state of Resource Public Key
   Infrastructure (RPKI) based BGP Prefix Origin Validation.  The
   Information Element enables network operators to collect and analyze
   BGP route validation states (valid, invalid, not-found) to facilitate
   the detection of potential route hijacks improving network
   observability and security.
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
- **draft-mglt-ipsecme-dscp-np-06** (new-draft, score 0, ignored_after_review) [ipsecme]: [Differentiated Services Field Codepoints Internet Key Exchange version 2 Notification](https://datatracker.ietf.org/doc/draft-mglt-ipsecme-dscp-np/) — This document outlines the DSCP Notification Payload, which, during a
   CREATE_CHILD_SA Exchange, explicitly indicates the DSCP code points
   that will be encapsulated in the newly established tunnel.  This
   document updates RFC 4301.
- **draft-nordin-ocm-mls-federated-groups-02** (new-draft, score 0, ignored_after_review) [ocm]: [Federated Groups in Open Cloud Mesh using Messaging Layer Security](https://datatracker.ietf.org/doc/draft-nordin-ocm-mls-federated-groups/) — This document defines an extension to the Open Cloud Mesh (OCM)
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
- **draft-nottingham-archive-embargo-00** (new-draft, score 0, ignored_after_review) [none]: [Embargoing Archive Publication using robots.txt](https://datatracker.ietf.org/doc/draft-nottingham-archive-embargo/) — Web sites often block archiving crawlers because they host time-
   sensitive information.  This specification documents a robots.txt
   extension, "Archive-Embargo", that can be used to request that such
   crawlers delay publication of information.

   This document updates RFC 9309 to add two directives that support
   embargoes.
- **draft-prabel-cfrg-suf-hybrid-sigs-02** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Digital Signatures with Strong Unforgeability](https://datatracker.ietf.org/doc/draft-prabel-cfrg-suf-hybrid-sigs/) — This document proposes a generic hybrid signature construction that
   achieves strong unforgeability under chosen-message attacks (SUF-
   CMA), provided that the second component (typically the post-quantum
   one) is SUF-CMA secure.  The proposed hybrid construction differs
   from the current composite hybrid approach by binding the second
   (post-quantum) signature to the concatenation of the message and the
   first (traditional) signature.  This approach ensures that hybrid
   signatures maintain SUF-CMA security even when the first component
   only provides EUF-CMA security.

   In addition to this general hybrid construction, this document also
   proposes a non-black-box variant specifically tailored for schemes
   built from the Fiat-Shamir paradigm.  This variant is SUF-CMA secure
   as long as only one component is SUF-CMA secure.
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
- **draft-song-pce-pcep-sav-03** (new-draft, score 0, ignored_after_review) [none]: [Path Computation Element Communication Protocol for Source Address Validation](https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/) — This document presents a method of Path Computation Element (PCE) for
   Source Address Validation (SAV) in networks.  It extends Path
   Computation Element Communication Protocol (PCEP) to support SAV
   policy distribution and synchronization between PCEP speakers for
   threat mitigation for source address spoofing.
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
- **draft-wang-tls-hybrid-ecdh-scloud-02** (new-draft, score 0, ignored_after_review) [none]: [Post-quantum Hybrid ECDHE-SCloud+ Key Exchange for TLS 1.3](https://datatracker.ietf.org/doc/draft-wang-tls-hybrid-ecdh-scloud/) — This draft specifies how to enable hybrid key exchange with ECDHE and
   SCloud+ in Transport Layer Security protocol version 1.3 (TLS 1.3) to
   mitigate quantum threats.  SCloud+ is an unstructured lattice based
   KEM (key encapsulation mechanism) with post-quantum security.  This
   draft follows the post-quantum hybrid key exchange framework
   specified by [RFC9954], by concatenating the public keys and
   ciphertexts of ECDHE and SCloud+. This draft specifies three concrete
   hybrid key exchange schemes, which are X25519SCloud+128,
   SecP256r1SCloud+192 and SecP384r1SCloud+256.
- **draft-wkumari-intarea-safe-limited-domains-07** (new-draft, score 0, ignored_after_review) [none]: [Safe(r) Limited Domains](https://datatracker.ietf.org/doc/draft-wkumari-intarea-safe-limited-domains/) — Documents describing protocols intended solely for use within
   "limited domains" often rely on edge filtering at every boundary node
   to prevent domain-internal traffic from leaking to the global
   Internet (and vice versa).  Relying purely on administrative
   filtering creates "fail-open" designs that are susceptible to
   configuration errors, ACL bypass, and hardware table exhaustion.

   This document describes design principles and concrete mechanisms
   that allow limited-domain protocols to "fail-closed" by default.  By
   leveraging Layer-2 encapsulation identifiers (such as dedicated or
   extended EtherTypes), link-local address scoping, and / or Hop-Limit
   boundaries, protocol designers can significantly reduce the
   operational and security risks associated with limited domain
   protocols.

   These mechanisms are not applicable to all protocols intended for use
   in a limited domain, but if implemented on certain classes of
   protocols, can significantly reduce the risks.
- **draft-wkumari-opsawg-json-geofeed-format-01** (new-draft, score 0, ignored_after_review) [none]: [A JSON Format for Self-Published IP Geolocation Feeds](https://datatracker.ietf.org/doc/draft-wkumari-opsawg-json-geofeed-format/) — This document defines a JavaScript Object Notation (JSON) format for
   self-published IP geolocation feeds.  It updates RFC 8805 by
   transitioning from the current comma-separated values (CSV) format to
   a more expressive JSON format, addressing the need for operational
   extensibility.
- **draft-wu-idr-flowspec-sip-community-filter-02** (new-draft, score 0, ignored_after_review) [none]: [Source-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-sip-community-filter/) — BGP Flow Specification (BGP-FS) propagates traffic Flow
   Specifications and Traffic Filtering Actions using BGP NLRI and BGP
   Extended Community encodings.  This document specifies a new BGP-FS
   component type to support community-level filtering within a single
   administrative domain.  The match condition filters traffic based on
   the BGP Community attributes associated with the route matching the
   packet's source IP address.
- **draft-xie-bess-evpn-extension-evn6-04** (new-draft, score 0, ignored_after_review) [none]: [EVPN Route Types and Procedures for EVN6](https://datatracker.ietf.org/doc/draft-xie-bess-evpn-extension-evn6/) — EVN6 is a mechanism designed to provide Ethernet connectivity to
   customer sites dispersed on public IPv6 networks.  At the data layer,
   EVN6 encapsulates Ethernet frames directly in the payload of IPv6
   packets, and dynamically generates the IPv6 addresses of the IPv6
   header using host MAC addresses and other information, then sends
   them into IPv6 network for transmission.  This document proposes
   extensions to EVPN for EVN6, including two new route types and
   related procedures.
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
- **draft-zhu-cats-metric-semantics-01** (new-draft, score 0, ignored_after_review) [none]: [Operational Semantics for CATS Metric Consumption](https://datatracker.ietf.org/doc/draft-zhu-cats-metric-semantics/) — The CATS framework introduces computing-related information into
   traffic steering decisions.  Existing work defines how such metrics
   are represented, distributed, and used within the CATS architecture.
   However, it does not fully address whether a metric remains suitable
   for use at the point of consumption.

   This document introduces a set of operational semantics for CATS
   metrics, including Freshness, Operational acceptability, and
   Assurance exposure.  These semantics describe whether a metric
   remains temporally aligned with the underlying condition, whether it
   remains suitable for operational use in steering, and whether
   degraded consumption is externally visible to management or OAM
   functions.

   The document further explains how these semantics apply across
   centralized, distributed, and hybrid deployments, including cases
   where different metric sources contribute under different conditions.
   The goal is to provide a consistent basis for interpreting metric
   usability in CATS without introducing a new metric level or
   prescribing a single derivation method.

   Implementations may determine when degradation occurs, while the
   resulting consumption condition can still be represented and
   understood consistently across CATS functions.

## Errors / fetch failures

- draft-faltstrom-unicode: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-faltstrom-unicode/doc.json
