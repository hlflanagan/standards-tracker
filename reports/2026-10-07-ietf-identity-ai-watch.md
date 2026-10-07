# IETF Identity + AI Standards Watch

Date: 2026-10-07

## Read now

- **draft-fane-opena2a-aap-02** (new-draft, score 28, core_identity) [none]: [OpenA2A Agent Authorization Protocol (AAP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aap/) — This document defines the OpenA2A Agent Authorization Protocol (AAP),
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

   This revision adds a structured, mandatory-to-understand
   "authorization_details" claim with a typed entry registry and a per-
   type attenuation relation for delegation, an "aap_crit" claim naming
   the claims a verifier must understand, a "cnf" claim binding a token
   to the presenter's key, a session label in the behavioral attestation
   claim, and a local grant revocation list.
- **draft-fane-opena2a-aip-04** (new-draft, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
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
   9162-style Merkle transparency log for identity and credential
   issuance; agent identifiers expressed as W3C Decentralized
   Identifiers, provider-scoped as a did:web profile at the identity-
   provider layer and ecosystem-scoped under the registered did:opena2a
   method at the trust-fabric layer; and a structured capability
   vocabulary with reserved namespaces.  On top of these, the protocol
   specifies challenge-response verification, behavioral governance
   policies, a lifecycle model, and an append-only audit log.

   The qualifier "OpenA2A AIP" is used throughout this document because
   the abbreviation "AIP" is shared by other Internet-Drafts.  OpenA2A
   AIP is framed as complementary to agent communication protocols such
   as A2A and the Model Context Protocol, and to identity and credential
   standards such as OpenID Connect, WebAuthn, and the W3C Verifiable
   Credentials Data Model.
- **draft-helixar-hdp-agentic-delegation-03** (new-draft, score 23, agent_identity) [none]: [Human Delegation Provenance Protocol (HDP): Cryptographic Chain-of-Custody for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/) — Agentic AI systems operate on behalf of human principals, often
   delegating tasks through multi-step chains of AI agents.  There is
   currently no standard mechanism to record who authorized an agent to
   act, under what scope, and through what chain of delegation, in a way
   that can be verified offline, without a central registry, and without
   third-party trust anchors.

   This document specifies the Human Delegation Provenance Protocol
   (HDP) version 0.1, a lightweight token-based protocol that captures,
   structures, cryptographically signs, and verifies human delegation
   context in agentic AI systems.  An HDP token binds a human
   authorization event to a session, records each agent's delegation
   action as a signed hop in an append-only chain, and lets an auditor
   verify the integrity of the full record using only the issuer's
   Ed25519 public key.  Verification is fully offline.  No registry
   lookup, no network call, and no third-party trust anchor is required.

   HDP's distinguishing contribution is a signed, tamper-evident record
   of what the human asked for and of how each agent read and acted on
   that request.  On deployments that use capability-based delegation
   formats such as UCAN and ZCAP-LD, the same content can travel in the
   capability certificates' own metadata instead of a separate token.
   The underlying append-only, offline-verifiable chain-of-custody
   mechanism is payload-agnostic; human-authorized agentic delegation is
   the reference profile specified in this document.

   HDP is not an authorization protocol.  An HDP token confers no
   authority and is not an input to any access decision.  It is a record
   of who authorized a task and of what each agent declared it did with
   that authorization, carried with the task and read at audit.
- **draft-seymour-wimse-connected-flight-06** (new-draft, score 23, authorization) [none]: [Zero Trust Fabric Layer Agent-to-Agent Chained Trust on a Connected Flight](https://datatracker.ietf.org/doc/draft-seymour-wimse-connected-flight/) — The Zero Trust Fabric Layer (ZTFL) verified a single autonomous agent
   issuing a single request.  It did not address what happens when that
   agent delegates its authority to a second agent, or a third, a
   pattern already standard in multi-agent orchestration.  Existing
   delegation mechanisms do not close this gap.  OAuth 2.0 Token
   Exchange represents prior actors as claims that are informational
   only for access control decisions.  Classical logic-based and
   relationship-based authorization models were built for stable, long-
   lived principals and do not enforce a tenant boundary at the specific
   hop where it is crossed, nor do they bind every hop in a chain to a
   single expiring credential established at the chain's origin.  This
   document extends ZTFL with a chained authorization model, structured
   on the mechanics of international travel.  An immutable Passport
   establishes identity for the full journey.  A Ticket, issued once at
   task initiation as a conditional ephemeral credential, binds every
   subsequent hop to the same authorized chain; a locally valid-looking
   Boarding Pass that cannot trace back to it is rejected regardless of
   appearance.  A per-hop Boarding Pass, a child ephemeral token derived
   from and traceable to the Ticket, authorizes each leg.  A Visa, an
   explicit and narrowly scoped grant, is required only at the moment a
   hop crosses a tenant boundary the Passport alone cannot cross.  The
   model is formalized as a boundary-conditional evaluation function,
   implemented and validated against the Cedar policy language, and
   compared directly against OAuth Token Exchange, delegation logic, and
   relationship-based authorization on two properties none of them
   enforce structurally: chain-wide traceability to a single origin, and
   containment at the boundary itself.  This revision further shows that
   the model's per-hop Boarding Pass structurally resists mid-chain
   redirection, including redirection caused by prompt injection
   reaching an intermediate agent, because issuing a Boarding Pass
   requires standing the redirected agent never holds and cannot acquire
   by altering its own behavior.
- **draft-wei-aic-jwt-02** (new-draft, score 23, authorization) [none]: [AI Agent Identity Certificate (AIC) JSON Web Token Profile](https://datatracker.ietf.org/doc/draft-wei-aic-jwt/) — The AI Agent Identity Certificate (AIC) defines a data model in which
   the cryptographic identity of an AI agent is bound to a responsible
   principal, together with a structured capability container,
   delegation mode, authorization constraints, and principal-signed
   delegation evidence.  The normative definition of this model is
   specified by the AIC specification, where it is encoded in ASN.1 and
   carried in X.509 certificates, enabling authorization decisions at
   the transport layer, including fully offline operation.

   Many HTTP, web, and OAuth 2.0 (RFC 6749) deployments cannot present
   X.509 certificates at the transport layer.  This document therefore
   defines AIC-JWT as a JWT-based application-layer representation of
   the AIC data model defined by the AIC specification.  AIC-JWT is a
   companion representation, not a replacement for the X.509 form and
   not a new authorization model.

   AIC-JWT uses the standard JWT (RFC 7519) and JWS (RFC 7515)
   mechanisms as its carrier and cryptographic envelope.  Its
   authorization semantics are inherited from the AIC model rather than
   defined by JWT or OAuth.  In particular, the outer AIC-JWT is issuer-
   signed and carries the principal-signed DA JWT as the value of the
   top-level da claim, preserving the two-layer signature model of AIC.

   The normative content of this document is limited to:

   *  a mapping from the X.509 AIC extension fields to JWT claims that
      preserves the AIC data model and its two-layer signature model;

   *  representation and key-binding rules for the principal-signed
      DelegationAuthorization;

   *  validation rules for AIC-JWT, including claim consistency,
      audience, and key-binding checks; and
   *  a thin OAuth 2.0 consumption profile defining presentation of the
      DA at a token endpoint as an RFC 7523 JWT bearer authorization
      grant and the projection of the AIC authorized and representative
      delegation modes into OAuth roles.
- **draft-nirvanai-nbtp-behavioral-trust-01** (new-draft, score 22, adjacent_watchlist) [none]: [NirvanAI Behavioral Trust Protocol (NBTP)](https://datatracker.ietf.org/doc/draft-nirvanai-nbtp-behavioral-trust/) — The NirvanAI Behavioral Trust Protocol (NBTP) defines a cryptographic
   framework for continuous attestation of AI agent behavioral integrity
   in distributed networks.  NBTP treats trust as a volatile, time-
   decaying state variable measured by an oracle-federated layer of
   independent scanner nodes.  Unlike static credential systems that
   answer "Is this agent authorized?", NBTP answers "Is this agent
   currently acting like itself?"  Identity systems confirm who sent a
   message.  NBTP confirms whether the sender is still the entity that
   earned that identity.  Trust computation is performed locally by each
   verifying party using signed attestations from independent oracle
   scanners; no centralized policy engine or authorization server is
   required at verification time.

   NBTP introduces a temporal decay model with context-dependent decay
   rates, a four-state trust machine (PROBATIONARY, TRUSTED, SUSPECT,
   QUARANTINED), cross-context co-silence detection, and a genesis
   bootstrapping mechanism (Creole gate) using formal CHALLENGE/RESPONSE
   packet types.  Absence of attestation data is treated as a security-
   relevant signal.  This document specifies the protocol wire format,
   state machine, decay model, security properties, and IANA
   considerations.  Implementation-specific measurement heuristics are
   out of scope.
- **draft-birkholz-did-x509-03** (new-draft, score 21, verifiable_claims) [none]: [The did:x509 Decentralized Identifier (DID) Method](https://datatracker.ietf.org/doc/draft-birkholz-did-x509/) — This document defines the did:x509 decentralized identifier (DID)
   method, a flexible issuer identifier format for messages that
   transport or refer to X.509 certificates, including CBOR Object
   Signing and Encryption (COSE) messages using RFC 9360.  The did:x509
   identifier format implements a direct, resolvable binding between a
   certificate chain and a compact issuer string (DID string).  It
   combines the fingerprint of a certification authority (CA)
   certificate in the chain with one or more predicates on the leaf
   certificate's subject name, subject alternative names, extended key
   usage, or Fulcio issuer.  The identifier can be conveyed as an issuer
   value in a COSE Header CBOR Web Token (CWT) Claims map as defined in
   RFC 9597, in JSON Object Signing and Encryption (JOSE) and JSON Web
   Token (JWT) messages, such as in the "iss" claim defined in RFC 7519,
   or through other protocol-specific mechanisms that associate the
   identifier with the certificate chain.  The did:x509 method lets
   existing X.509 solutions and DID-based systems interoperate where a
   full transition to DIDs is not achievable or desired.  This issuer
   identifier is convenient for references and policy evaluation, for
   example in the context of transparency ledgers.

   This Informational document is published as an Independent Submission
   to describe the method as implemented by Microsoft.  It is neither a
   standard nor a product of the IETF.
- **draft-wei-aic-identity-cert-02** (new-draft, score 21, core_identity) [none]: [AI Agent Identity Certificate (AIC) Extension for X.509 v3](https://datatracker.ietf.org/doc/draft-wei-aic-identity-cert/) — This document defines the AI Agent Identity Certificate (AIC)
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
- **draft-levi-agent-certification-00** (new-draft, score 20, core_identity) [none]: [Autonomous Agent Certification Protocol (AACP)](https://datatracker.ietf.org/doc/draft-levi-agent-certification/) — This document defines the Autonomous Agent Certification Protocol
   (AACP), a framework for binding successful evaluation of an AI agent
   to cryptographically verifiable evidence of demonstrated capability.

   AACP introduces Evaluation Profiles that define the conditions under
   which an agent may be certified for a specific capability.  An Agent
   Configuration that satisfies an Evaluation Profile may receive a
   short-lived Agent Certification Credential (ACC) bound to the
   configuration that was evaluated.

   An ACC does not grant access to a resource.  It provides verifiable
   evidence that an agent has demonstrated a capability under defined
   evaluation conditions.  Existing authorization systems may require
   such evidence as a condition for granting corresponding production
   permissions.

   AACP therefore separates capability certification from identity,
   authentication, delegation, and authorization.
- **draft-morrison-ot-command-authority-03** (new-draft, score 19, authorization) [none]: [Consented and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
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
- **draft-rasmussen-acme-wif-00** (new-draft, score 18, core_identity) [none]: [A Federated Workload Identity Challenge for the Automated Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/draft-rasmussen-acme-wif/) — The Automated Certificate Management Environment (ACME, RFC 8555)
   establishes that a requester has authority over an identifier by
   means of a challenge that demonstrates control of that identifier,
   such as publishing a DNS record or serving an HTTP resource.  It
   authenticates the requester by means of an account key whose
   provenance is outside the protocol's scope.

   Neither mechanism is a good fit for automated workloads running in
   continuous-integration systems, container orchestrators, and cloud
   compute platforms.  Such workloads typically possess no long-lived
   secret and no ability to publish DNS records, but they do possess a
   short-lived, cryptographically verifiable identity assertion issued
   by their execution platform.

   This document defines a new ACME challenge type, "wif-01", by which
   an ACME server authorizes issuance for an identifier on the basis of
   a platform-issued identity token.  The token is bound to the ACME
   account key, and to the specific authorization it satisfies, using
   the token's audience claim.  The mechanism therefore requires no new
   claims, no new endpoints, and no changes of any kind to existing
   identity providers.

   Because the workload's identity is established for each
   authorization, the mechanism also removes any need for External
   Account Binding: an ordinary ACME account, created by the workload
   with no pre-shared secret, suffices.  The mechanism uses only
   extension points that ACME already defines.
- **draft-sharif-x509-agent-identity-profile-04** (new-draft, score 18, agent_identity) [none]: [X.509 Certificate Profile for Autonomous AI Agent Identity](https://datatracker.ietf.org/doc/draft-sharif-x509-agent-identity-profile/) — This document defines an X.509 certificate profile for identifying
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
- **draft-schrock-ep-authorization-evidence-chain-08** (new-draft, score 17, authorization) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
   delegation, policy, permit, approval, transparency, capability, and
   execution artifacts.  Each artifact can verify under its own
   specification while still referring to a different action, filling a
   different evidentiary role, or failing a relying party's freshness,
   status, or inter-artifact binding requirement.  This document defines
   the Authorization Evidence Chain (EP-AEC): a transport-agnostic
   composition object and a fail-closed evaluation algorithm that keeps
   native cryptographic verification separate from relying-party
   acceptance, establishes exact material-action matching, and evaluates
   a relying-party-pinned evidence requirement.

   AEC produces SATISFIED or UNSATISFIED and a replayable evaluation
   record.  SATISFIED means only that the presented evidence filled the
   relying party's named evidence requirement at the stated verification
   time.  It is not a universal authorization decision, a policy
   language for the protected application, or proof of execution or
   outcome.  The executor makes the separate local AUTHORIZED decision
   and controls consumption, invocation, and effect handling.
   Qualification evidence can fill a named evidence role but cannot
   authorize an action by itself.  AEC introduces no new component
   receipt type and does not replace any native verifier.
- **draft-correctover-ccs-10** (new-draft, score 16, core_identity) [none]: [Correctover Conformance Shape (CCS): Runtime Verification for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — This document defines the Correctover Conformance Shape (CCS), a
   runtime verification framework for AI agent tool calls.  CCS
   specifies seven verification dimensions (Structure, Schema, Latency,
   Cost, Identity, Integrity, Security) that tool calls and results must
   conform to at runtime.  The framework defines a receipt format with
   Ed25519 signatures, three verdict values (allow, deny, escalate) and
   four executor lifecycle states (confirmed, dispatched, indeterminate,
   unknown), and normative requirements for implementations.

   This revision makes the document self-contained for publication: the
   related AEB and CAID specifications are reclassified as Informative
   References, and the native artifact requirements they motivate are
   restated normatively in this document so that no conformance
   requirement depends on an unreferenced work in progress.  It also
   corrects the implementation-experience description (one reference
   implementation in two deployment forms, plus one independently
   developed third-party interoperability profile), clarifies the
   relationship to SCITT-based agent evidence work, and updates the
   author contact address.  The detached Ed25519 signature construction
   over RFC 8785 canonical JSON and the receipt lifecycle and signing-
   algorithm conformance are unchanged from draft-08.

   This revision restructures key management around two orthogonal trust
   levels: VERIFIED, the self-contained integrity and key/signature
   consistency verifiable fully offline from the receipt alone, and
   ACCEPTED, which adds out-of-band issuer pinning and is the only level
   that authenticates the signer.  The embedded public_key,
   public_key_fingerprint, and signing_algorithm fields are now required
   to be covered by the signature to prevent key substitution and
   algorithm downgrade.
- **draft-helmprotocol-tttps-13** (new-draft, score 16, trust_infrastructure) [none]: [The TLS TimeToken Secure Protocol (TTTPS)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies a temporal-evidence admission protocol with a
   fixed 180-octet Proof-of-Time Record v2.  It defines issuer
   authentication, holder presentation, context binding, asymmetric
   freshness checks, and replay-safe application commitment.
   Implementations can place verification at a declared application
   boundary and can accelerate suitable operations in a kernel, NIC, or
   FPGA without changing those requirements.

   An authenticated context identifies the event, policy, source
   evidence, and selected binding revision.  A Roughtime adapter
   combines response-chain validation with authority-backed provenance
   and effective-source aggregation.  Other clock adapters retain their
   own evidence contracts.  Confidence and propagation-aware profiles
   are optional and cannot repair a failed core check.

   The core mandatory integrity algorithm is SHA-256.  Optional recovery
   algorithms require separate complete specifications.  The protocol
   does not establish physical truth, agent intent, legal admissibility,
   or regulatory compliance, and does not replace clock synchronization,
   authorization, auditing, or transparency services.
- **draft-ni-wimse-ai-agent-identity-03** (new-draft, score 16, agent_identity) [none]: [WIMSE Applicability for AI Agents](https://datatracker.ietf.org/doc/draft-ni-wimse-ai-agent-identity/) — This document discusses WIMSE applicability to Agentic AI, so as to
   establish independent identities and credential management mechanisms
   for AI agents.  It also discusses mechanisms for cryptographically
   binding an AI agent identity to an accountable user or organization.
- **draft-c4tz-marc-03** (new-draft, score 15, core_identity) [none]: [MARC: A Control and Uncertainty Disclosure Profile for Generative Models and Agents](https://datatracker.ietf.org/doc/draft-c4tz-marc/) — This document specifies MARC, an experimental, vendor-neutral profile
   for control and uncertainty-disclosure metadata in generative models
   and agentic systems.  MARC separates pre-decision capability
   assessment from post-decision answer confidence, identifies
   uncertainty sources and confidence targets, and defines a bounded set
   of primary actions and a minimal disclosure object.

   The experiment evaluates whether independently developed components
   can exchange and interpret these metadata consistently across
   implementation and protocol boundaries.  It also supports evaluation
   of action selection, uncertainty attribution, confidence calibration,
   and downstream presentation.

   MARC specifies externally observable semantics.  It does not define
   model internals, transport, authentication, authorization, agent
   discovery, tool schemas, or task execution, and it does not require
   disclosure of internal reasoning.  The intended users are
   implementers of agent runtimes, orchestration layers, model gateways,
   evaluation systems, and user interfaces.  This document does not
   define an Internet Standard.
- **draft-lee-oauth-dpop-credential-presentation-03** (new-draft, score 15, verifiable_claims) [none]: [JWT Access Tokens as W3C Verifiable Credentials](https://datatracker.ietf.org/doc/draft-lee-oauth-dpop-credential-presentation/) — This document profiles the JWT access token of RFC 9068 so that the
   same JWT is also a W3C Verifiable Credential secured with JOSE.  The
   authorization server is the credential's issuer, and the token is
   bound to the client's key with DPoP (RFC 9449).  A resource server
   receives it as an ordinary DPoP-bound access token and needs no
   change.  A verifier that the authorization server can name as the
   token's audience can process the same object as a Verifiable
   Credential.

   The profile defines no new header parameters, claims or
   registrations.  It states which existing header parameters and claims
   the token carries, how the claims of the two data models correspond,
   and the conditions under which one object can safely serve both
   purposes.
- **draft-newton-agreement-evidence-00** (new-draft, score 15, core_identity) [none]: [Agreement Evidence for Multi-Party Agent Negotiation](https://datatracker.ietf.org/doc/draft-newton-agreement-evidence/) — Autonomous agents can exchange offers and signatures without
   producing an artifact that records which parties reached which
   outcome, over which transcript digest and message count, and for how
   long that record may be relied upon.  This document defines JSON
   agreement-evidence objects for structured, multi-attribute
   negotiation.  The core object is an agreement attestation.  A
   verified attestation establishes one thing: that a named set of
   parties jointly countersigned a stated outcome over a stated
   transcript digest and message count, together with behavioral
   counters each of them accepted.  It does not establish that the
   outcome matches what the transcript says, that any statement a party
   made is true, or that the parties are anonymous.  The format provides
   no member for a negotiated price, quantity, date, or principal
   identity.  A producer is obligated not to place those values in the
   free-text members the format does provide, and a verifier cannot
   detect a violation of that obligation, so the absence of term values
   from a received object is a producer's obligation rather than a
   verified property.  Sections 4 through 8 and 10 define every member
   of the object, its JSON type, its encoding, its value constraints,
   and the verification procedure.  This document also defines relying-
   side freshness obligations and describes related approval,
   fulfillment, and revocation artifacts, whose formats it leaves to
   other documents.

   This document does not define identity, authority delegation,
   payment, settlement, transport, boundary-decision receipts, or a
   general evidence composition and sufficiency model.
- **draft-das-interim-effectuation-validation-00** (new-draft, score 14, agent_identity) [none]: [Authority Is Earned from the Real Path, Not Granted Per Session: Receipt-Gated Interim Effectuation Validation for AI Agents, Frontier AI Model Providers, and Autonomous Systems](https://datatracker.ietf.org/doc/draft-das-interim-effectuation-validation/) — Authority to cause a real-world effect should not be granted for a
   whole session; it should be earned, one bounded step at a time, from
   the real path itself.  This document specifies an experimental
   architecture for controlling consequential external effects produced
   by agentic, autonomous, and conventional computing systems, and is
   addressed in particular to operators of AI machines and to frontier
   AI model providers.  It separates a proposed act from authority to
   make that act effective, permits a real bounded effect to occur,
   obtains protected evidence of what actually occurred, independently
   evaluates that evidence in an Interim Effectuation Validator (IEV),
   and makes a later effect technically dependent on a protected
   continuation condition.  The validator does not relay the original
   command, and if trustworthy evidence is missing the system holds or
   quarantines the act instead of retrying it.  The architecture
   supports single-phase, two-phase, and multi-phase operation; human,
   automatic, and hybrid escalation; crash and indeterminate-state
   reconciliation; validator-integrity hardening; conflicting-evidence
   handling; effectuation-time revocation; taint and provenance
   propagation; privilege-separated credential surrogation; and
   software, hardware, virtual-machine, operating-system, destination-
   native, quorum, and tokenless realizations.

   The document defines an abstract protocol and conformance model
   rather than one mandatory transport or serialization.  It also
   specifies implementation-invariance rules so that changing component
   placement, token representation, operating system, proxy topology,
   validator location, or credential representation does not by itself
   change the functional sequence when the required security properties
   are preserved.

   Patent pending: the concept described in this document is the subject
   of Indian Patent Office application number 202631117633, "Systems and
   Methods for Cryptographically Staged Effectuation with Verified
   Partial Effect, Receipt-Bound Full Effectuation, and Software-
   Hardware Enforcement".
- **draft-das-receipt-gated-iev-00** (new-draft, score 14, agent_identity) [none]: [Evidence Is the Key, Not the Log: Receipt-Gated Staged Effectuation and Interim Effectuation Validation for AI Agents, Frontier AI Model Providers, and Autonomous Systems](https://datatracker.ietf.org/doc/draft-das-receipt-gated-iev/) — Authority to cause a real-world effect should not exist on a machine
   until the real path has shown that it is safe.  This document
   describes an experimental execution-control architecture for agentic,
   autonomous, and conventional computing systems, and is addressed in
   particular to operators of AI machines and to frontier AI model
   providers.  A proposed act is separated from authority to make the
   act consequential.  The architecture supports single-phase protected
   effectuation, a bounded real first effect followed by receipt-gated
   continuation, and arbitrary multi-phase progression.  In the Interim
   Effectuation Validator (IEV) profile, protected evidence of an
   earlier real effect is not a log but a structural dependency: it is
   independently evaluated before a protected continuation condition for
   a later effect is established, and the validator does not relay the
   original command.  If trustworthy evidence is missing, the system
   holds or quarantines the act instead of retrying it.

   The document also describes taint and provenance propagation,
   protected origin attribution, surrogate or non-exportable credential
   references, boundary credential resolution, privilege-separated
   connector execution, human and automatic remediation, crash and
   indeterminate-state reconciliation, anti-bypass requirements,
   tokenless and cryptographic continuation, and software, virtual-
   machine, operating-system, mobile, application, network, transaction,
   hardware, destination-side, and distributed realizations.  The
   architecture is defined by functional relationships rather than by a
   particular product name, operating system, validator placement, token
   format, proxy, or credential representation.

   Patent pending: the concept described in this document is the subject
   of Indian Patent Office application number 202631117633, "Systems and
   Methods for Cryptographically Staged Effectuation with Verified
   Partial Effect, Receipt-Bound Full Effectuation, and Software-
   Hardware Enforcement".
- **draft-klassen-eu2122-content-profile-02** (new-draft, score 14, trust_infrastructure) [none]: [EU2122 V1.0 Standard: Content Profile for AI Output Verification Receipts](https://datatracker.ietf.org/doc/draft-klassen-eu2122-content-profile/) — This document defines a content profile for AI output
   verification receipts. It specifies the minimum fields,
   classification taxonomy, and evidentiary properties that
   a receipt MUST contain in order to constitute verifiable
   evidence that an AI-generated output was checked before
   a human or downstream agent acted on it. The profile
   is designed to be
   carried over any conformant wire format, including ACTA
   signed receipts, SCITT transparency logs, and standalone
   JSON or CBOR payloads.

   Existing IETF drafts in this space define wire formats
   for signing, transmitting, and storing AI agent receipts.
   None defines what a verification receipt must contain at
   the content layer. This document fills that gap. It
   introduces a mandatory fourteen-category failure
   taxonomy (the Information Bottleneck Species), a
   verification
   verdict schema, and evidentiary field requirements
   derived from the EU AI Act (Regulation 2024/1689), the
   Product Liability Directive (2024/2853), and the IDW
   PS 861 audit standard.

   We invite and even urge implementers to adopt, populate
   and grow the AI Output Verification market segment,
   which the author has also defined in communications to
   Gartner, Forrester, PAC/Teknowlogy, and IDC. The
   category exists. The specification is here. Build to it.
- **draft-krausz-verification-state-03** (new-draft, score 14, agent_identity) [none]: [The verification.* Constraint Family: Pre-Action Fail-Closed Gates for AI Agent Decisions](https://datatracker.ietf.org/doc/draft-krausz-verification-state/) — This document specifies the verification.* constraint family --- a
   pre-action, fail-closed gate primitive for AI agent decisions,
   sibling in shape to the environment.* family used in Verifiable
   Intent specifications.  A verification.* receipt is a JSON Web
   Signature (JWS) signed artifact carrying a canonical input, a derived
   binary act/halt output, and a versioned mapping identifier that binds
   them.  A relying party recomputes the gate locally from signed
   primitives under the named mapping; the verifier never trusts the
   issuer's runtime.

   This revision replaces the raw verdict domain of draft-krausz-
   verification-state-01 (supported/refuted/unverifiable/unknown) with a
   four-state vocabulary --- verified, contradicted, indeterminate, and
   not_evaluated --- together with a reason-code mechanism that
   separates a state's substance from a verifier's own instrument
   failure, and with an admissibility gate applied before a state is
   ever assigned.  It adds evidence pinning: a receipt MAY carry an
   evidence_set block that content-addresses the sources considered
   during verification, so that a verdict can be recomputed offline from
   the receipt and the pinned bytes alone, without depending on a live
   retrieval provider.  Freshness is anchored to the evidence's own
   retrieved_at timestamp rather than a separately declared validity
   window.  This shape provides decision explainability and traceability
   evidence aligned with EU AI Act Article 12 record-keeping obligations
   and with the Decision Explainability tier of an industry Zero Trust
   for AI Agents framework published in 2026.  The format is forward-
   compatible across mapping revisions: receipts signed under one
   mapping ID remain verifiable as correct-under-that-mapping after
   newer mappings ship.  The vectors that content-address a mapping
   document or an evidence set are historical, digest-anchored artifacts
   and are unchanged by this revision; nothing in this document alters a
   previously issued digest.
- **draft-schrock-canonical-action-identifier-05** (new-draft, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
   identify an action using format-local content and digests.  Those
   digests are not directly comparable when the formats select or encode
   material action fields differently.  This document defines the
   Canonical Action Identifier (CAID): a typed action object, a
   canonicalization and digest suite, a compact identifier string, and
   versioned action-type definitions with required material fields.
   External value sets are bound to integrity-checked snapshots.  The
   document specifies a strict JSON input profile, a fixed and ordered
   set of refusal reasons, and a digest that identifies the validation
   semantics of a type definition.  It requests seven registries:
   suites, action types, field types, code formats, reason codes,
   mapping transforms, and mapping loss policies.  It also defines an
   Action-Mapping Profile for projecting natively verified artifacts
   into a common action type, with the closed results
   EQUIVALENT_UNDER_PROFILE, NOT_EQUIVALENT, and INDETERMINATE.  CAID
   carries no trust semantics.  It does not establish identity,
   authority, authorization, execution, safety, or legal reliance.
- **draft-winmagic-condition-bound-keys-00** (new-draft, score 14, core_identity) [none]: [User Authentication in the TLS Handshake with Condition-Bound Keys](https://datatracker.ietf.org/doc/draft-winmagic-condition-bound-keys/) — A user's access to an online service is secured today in two parts.
   A login establishes who is there and ends in a verdict, which a
   cookie or token carries to later requests.  The session is then
   protected by other means, such as binding that token to a key.  The
   login does not establish the key that protects the session, and that
   leaves a gap between the two.

   This document describes authenticating the user the way workloads are
   commonly authenticated: in the TLS handshake.  The user signs in to
   their own device.  The device holds a condition-bound key that can
   sign only while that user is using the device, the device is the
   enrolled one, and its state meets local policy.  Used as the TLS
   client key, it makes the handshake the login and the TLS session the
   session.  The key represents the identity (the user, the device and
   its state) at the moment of use, so identity assurance is carried in
   each transaction and nothing else has to stand for it: no separate
   login to the service and no session credential.  When a condition
   fails, the key can no longer sign, and access ends at the next full
   handshake without a revocation message being sent.

   This is not an extension of OAuth.  OAuth starts after the login;
   this removes the login to the service and the token that carries its
   result.  Authorization is unchanged and can still come from OAuth.

   The document describes the properties of such a key, its use in
   mutual TLS, what a relying party can conclude from it, what parties
   would need to agree on for it to interoperate, and how it relates to
   existing mechanisms.
- **draft-gilda-wimse-agent-audit-record-02** (new-draft, score 13, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-wimse-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions.  The format is one in-toto predicate type, signed inside a
   DSSE envelope.  It carries the seven minimum audit fields that the
   WIMSE AI Identity Management System framework requires, and two
   properties that make those fields checkable: a canonicalization
   contract, and both the authorization decision and the observed effect
   with a derived three-valued agreement between them.  That framework
   places the record format out of scope and takes no IANA action.  This
   document supplies the format.  It defines no policy.
- **draft-lee-wimse-local-tool-call-proof-00** (new-draft, score 13, authorization) [none]: [Per-Call Proof for Local Tool Invocation by AI Agents](https://datatracker.ietf.org/doc/draft-lee-wimse-local-tool-call-proof/) — AI agents increasingly act through local tool servers that run on the
   same host and are reached over inter-process channels such as the
   stdio transport of the Model Context Protocol (MCP).  These channels
   are outside the scope of HTTP-based authorization: the tool server
   cannot tell whether a given invocation passed any policy decision,
   and reusable credentials typically sit in the agent's process memory.

   This document defines a per-call proof for local tool invocation.  A
   Call Authority that runs outside the agent process evaluates policy,
   issues a short-lived, single-use proof bound to the exact tool name
   and arguments through a canonical action digest, and verifies that
   proof on behalf of the tool server.  The tool server rejects
   invocations whose proof is missing or does not verify.  The proof
   format is opaque to the agent and the tool server; concrete formats
   are defined as evidence type profiles.  An MCP stdio binding is
   provided.
- **draft-mih-agent-evidence-layer-00** (new-draft, score 13, trust_infrastructure) [none]: [Evidence Layer](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-layer/) — This document defines the evidence layer: the conformance
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
- **draft-skyfire-oauth-using-kyapay-tokens-01** (new-draft, score 13, core_identity) [none]: [Using KYAPay Tokens](https://datatracker.ietf.org/doc/draft-skyfire-oauth-using-kyapay-tokens/) — The KYAPay Token is a JSON Web Token (JWT) that carries verified
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
- **draft-forten-oauth-sd-jwt-access-token-00** (new-draft, score 12, verifiable_claims) [none]: [Selective Disclosure for JWT Access Tokens Without Changing the Token](https://datatracker.ietf.org/doc/draft-forten-oauth-sd-jwt-access-token/) — This document adds selective disclosure to JWT access tokens without
   changing the form of the Authorization header or how the token is
   validated.  The RFC 9068 token is sent as today, with some of its
   claims selectively disclosable as defined by SD-JWT (RFC 9901); the
   Disclosures and the optional Key Binding JWT travel in two new HTTP
   fields.  A recipient that does not implement this profile ignores the
   fields and processes the token as an ordinary JWT access token.  The
   token itself then carries no selectively disclosable value, and the
   holder chooses per request which values to reveal.
- **draft-sparysh-pala-audit-01** (new-draft, score 12, trust_infrastructure) [none]: [PALA-1: A Tamper-Evident Audit Record Format for Constrained and Disconnected Deployments](https://datatracker.ietf.org/doc/draft-sparysh-pala-audit/) — This document describes PALA-1 -- version 1 of the Portable Append-
   only Log for Audit -- a compact binary record format for tamper-
   evident audit trails produced by AI inference runtimes and robotic
   control systems.  It is designed for a class of deployment defined by
   three constraints that hold together: the hardware is computationally
   modest and its cycles are reserved for the workload and the power
   budget rather than for the audit trail; no external witness is
   reachable, whether because policy forbids outbound contact or because
   the platform operates beyond connectivity, so a witness is
   unavailable by rule or by physics rather than by circumstance; and
   the right to verify the trail is separated from the right to read
   what it records.

   Records form an append-only hash chain.  Integrity verification
   requires no key material of any kind, inspects no record bodies, and
   costs one hash per record rather than one signature.  The format
   distinguishes three separately answerable questions -- internal
   consistency, completeness against an external anchor, and existence
   at a point in time against an external witness -- and states which of
   the three a given trail actually supports rather than implying all
   three.

   The format is frozen at version 1.0 and is described here as it is.
   This document presents an existing wire format; it does not revise
   one.  Where a deployment does permit an external witness, a chain
   head may be published to a transparency service such as that of the
   Supply Chain Integrity, Transparency, and Trust architecture (SCITT,
   RFC 9943); that path is described but is not part of the hashing
   contract.
- **draft-alla-agent-identity-document-00** (new-draft, score 11, core_identity) [none]: [The Agent Identity Document: A Hosted, Accountable Public Record for AI Agents](https://datatracker.ietf.org/doc/draft-alla-agent-identity-document/) — Autonomous software agents increasingly act on the public internet
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
- **draft-skyfire-oauth-kyapay-token-02** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-zambo-aer1-12** (new-draft, score 10, trust_infrastructure) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
   AI agent tool call as a portable, independently checkable execution
   receipt.  A receipt identifies the execution, records when it
   happened, preserves the canonical bytes used for the output
   commitment, names the tool and caller scope, carries a provenance
   class, and resolves at a stable public URL.  The format separates
   what the system observed from claims about the outside world, and it
   separates provenance (who ran or reported the action) from the record
   itself.  A reference implementation is deployed, and its receipts are
   publicly verifiable without an account or token.  The specification
   workflow receipts, which bind an ordered sequence of step receipts
   to a single goal with a Merkle root over the step sequence, and
   hash-chained job timelines for tamper-evident sequencing of
   executions.  This revision closes honesty and precision gaps: it
   adds the workflow-receipt truncation limit (new Section 8.4),
   normatively specifies the external anchor format and its
   verification procedure (rewritten Section 10, new Section 10.1),
   fixes a RECOMMENDED/MUST contradiction in Section 8.1, makes the
   Section 6 verification step testable, and documents replay,
   low-entropy, empty-record, and size-limit considerations.  It
   changes no receipt field, digest construction, or existing
   verification rule.
- **draft-dogru-cedulon-core-03** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-ietf-rats-network-device-subscription-14** (new-draft, score 9, trust_infrastructure) [rats]: [Attestation Event Stream Subscription](https://datatracker.ietf.org/doc/draft-ietf-rats-network-device-subscription/) — This document defines how to subscribe to YANG Event Streams for
   Remote Attestation Procedures (RATS).  Specifically, this document
   defines a YANG module that augments the YANG module for Trusted
   Platform Module (TPM)-based Challenge-Response Remote Attestation
   (CHARRA), enabling subscription to RATS Conceptual Messages of the
   Evidence type and auxiliary Event Logs as part of that Evidence.  The
   module defined requires at least one Trusted Platform Module (TPM)
   1.2 or TPM 2.0 (or equivalent hardware implementation providing the
   same protected capabilities as a TPM) must be available on the
   Attester on which the YANG server is running.
- **draft-janbjer-div-00** (new-draft, score 9, authorization) [none]: [Deterministic Intent Verification (DIV) Protocol Specification](https://datatracker.ietf.org/doc/draft-janbjer-div/) — This document specifies Deterministic Intent Verification (DIV), a
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
- **draft-paka-rats-hardware-component-attestation-01** (new-draft, score 9, trust_infrastructure) [none]: [Attestation of Hardware Components](https://datatracker.ietf.org/doc/draft-paka-rats-hardware-component-attestation/) — Hardware components constitute the foundation of all computations and
   therefore play a critical role in system integrity and reliability.
   Existing attestation mechanisms primarily rely on manufacturer
   Endorsements, which provide limited visibility into the runtime
   behavior of hardware.  This document extends the Remote ATtestation
   procedureS (RATS) architecture by defining a data model and
   guidelines for including measurements of hardware components in
   attestation Evidence.  These measurements may represent physical
   properties, results of self-tests, or behavioral observations.  The
   document considers a threat model that includes both adversarial
   actions and physical phenomena such as environmental variations and
   aging.  It proposes abstract interfaces for collecting measurements,
   enabling interoperability while remaining agnostic to implementation
   mechanisms, and outlines a security model for their use in appraisal.
- **draft-zhang-dawn-agent-discovery-framework-02** (new-draft, score 9, core_identity) [none]: [A Framework for Agent Discovery in DAWN](https://datatracker.ietf.org/doc/draft-zhang-dawn-agent-discovery-framework/) — The IETF DAWN (Discovery of Agents With Names) working group is
   developing a suite of documents addressing agent discovery across
   organizational boundaries, initially focused on discovery of AI
   agents and their capabilities.  Existing DAWN contributions include
   terminology, requirements, use cases, gap analysis, a discovery
   mechanism survey, and an information model for Minimum Discoverable
   Information (MDI).

   This document describes a two-layer federated reference architecture
   framework that operates within the DAWN.  The first layer, the Local
   Discovery Plane, performs zero-configuration agent advertisement and
   collection inside each local site, without mandating a specific link-
   local protocol.  The second layer, the Federation Plane, builds a
   federation among site gateways to exchange lightweight Federation
   Metadata Records (FMRs) — a concrete binding of DAWN MDI — across
   independent administrative domains, while full Capability Cards are
   retrieved on demand via authenticated unicast.

   The architecture emphasizes data sovereignty through an Export Policy
   Engine, separates lightweight metadata indexes from full capability
   documents, and supports multiple federation synchronization
   strategies.  This document is informational.  It does not define
   normative protocol formats, nor does it compete with existing DAWN
   proposals such as ACAP, Agent Directory, or ARDP; rather, it provides
   a deployment framework showing how these mechanisms may be composed
   at administrative boundaries.

   Consistent with the DAWN charter, the architecture is primarily
   targeted at AI agent discovery while remaining general and reusable
   for other entity types.
- **draft-arsentev-llm-context-discovery-01** (new-draft, score 8, agent_identity) [none]: [Discovery and Retrieval of Publisher-Curated Context Files for Large Language Model Consumers](https://datatracker.ietf.org/doc/draft-arsentev-llm-context-discovery/) — Publishers have begun to serve a curated, plain-text summary of a web
   origin intended for consumption by large language models and by the
   crawlers that feed them, most visibly under the de facto file name
   "llms.txt".  The practice is described by an informal proposal which,
   in its current version, recommends existing link relations from
   individual pages to the file.  It has no media type, no rules that
   bound the cost of retrieval, and no way for a consumer that starts
   from an origin's robots.txt or from a fixed well-known location to
   learn that such a file exists.

   This document specifies discovery and retrieval for publisher-curated
   context files.  It defines the well-known URI "llm-context", the link
   relation type "llm-context", and an extension record for the robots
   exclusion protocol, so that a publisher may advertise a context file
   by three independent paths and a consumer may find it without
   guessing.  It specifies a two-tier arrangement of an index resource
   and optional detail resources, states conditional-request and size
   requirements that keep retrieval affordable for both parties, and
   describes the relationship of this mechanism to the robots exclusion
   protocol, to sitemaps, to the llms.txt proposal itself, and to work
   in the IETF on AI usage preferences, agent communication and the
   discovery of AI agents.

   This document also reports measurements from an operational
   deployment in which requests presenting twenty crawler tokens of
   search and language-model providers numbered 46,155 over fifteen days
   at one origin server, without once retrieving the context file the
   origin was serving, while the same crawler tokens retrieved
   robots.txt 698 times in the three days after the context file was
   deployed.  The measurement figures in revision -00 were computed on
   an incomplete log and are corrected here.  The absence of a discovery
   mechanism, rather than the absence of interest, is the hypothesis
   this document acts upon.
- **draft-das-safety-first-execution-finality-00** (new-draft, score 8, agent_identity) [none]: [A Permit to Effect Once Is Not a Permit to Effect Permanently: Reality as a Cryptographic Dependency for AI Machines, Frontier AI Model Providers, and Critical Systems](https://datatracker.ietf.org/doc/draft-das-safety-first-execution-finality/) — A permit to effect once is not a permit to effect permanently.  An
   approval, a policy decision, or one successful effect is not standing
   authority for a larger or repeated one.  For AI machines and frontier
   AI models that can now act in the world, this separates a contained
   mistake from an irreversible one.

   Today, security checks who is asking, inspects a token, opens the
   gate, and hopes that the downstream network path, destination, or
   physical machine is safe.  AI agents now send messages and files,
   move money, change production infrastructure, invoke tools, update
   model and memory state, release sensitive data, and drive vehicles,
   robots, and industrial equipment.  Approval can show that an action
   was allowed in principle without showing that the exact action
   reaches the right recipient, device, or outcome.  Simulations and
   dry-runs do not close this gap, because a simulation can pass in a
   clean sandbox while the real target, route, or actuator has been
   hijacked.  Logs do not close it either, because a log explains a
   disaster after it has happened.

   This document makes reality a cryptographic dependency.  The full-
   consequence command is held in a state that cannot execute.  First, a
   deliberately bounded real effect is produced on the exact operational
   path: a trailing capsule, one record, a payment hold, a canary
   deployment, a constrained session, or a millimetre of actuator
   movement.  The destination, transaction system, network element,
   sensor, or hardware controller then returns an Effect Confirmation
   Receipt.  An Interim Effectuation Validator validates that receipt
   out of band against the intended act, nonces, epoch, scope,
   destination, current policy, and revocation state.  Only then does it
   issue the continuation instruction that reconstructs the key,
   releases the split credential, or unlocks the hardware register for
   the next phase.  Without the receipt, the key for full effect does
   not exist on the machine.  Evidence is therefore a structural
   dependency and not a log.

   Two properties are central.  First, the validator never relays the
   original command: the micro-effect proceeds independently and the
   validator observes the proof from a distance, so compromising an
   inline proxy or manipulating routing through prompt injection does
   not hand over the keys.  Second, uncertainty is a first-class state.
   If a micro-effect fires but trustworthy evidence is missing, the
   system quarantines and refuses progression instead of retrying, so an
   autonomous loop cannot compound a duplicate transfer, a double
   commit, or an over-actuation.  These properties hold under stated
   assumptions, including receipt integrity, path completeness, and
   atomic consumption of continuation authority, which the document
   identifies.

   The architecture covers single-phase and multi-phase execution;
   human, automatic, hybrid, threshold, and hardware-rooted approval;
   anti-replay and anti-substitution controls; alternate-path closure;
   reconciliation of indeterminate outcomes; and rollback, compensation,
   and safe-state handling.  It consolidates thirty-five workflow
   profiles across communications, files, payments, databases, cloud and
   model deployment, AI tool invocation, data export, robotics,
   vehicles, UAVs, industrial control, radio and satellite systems, GPU
   and accelerator egress, and software and firmware activation.  The
   Safety-First Critical-System Profile applies where avoiding
   catastrophic or hard-to-reverse outcomes comes before minimum
   latency: a deployment MUST NOT remove a validation, receipt, anti-
   replay, or safe-state protection merely to be faster, when protected
   policy classifies it as necessary for the consequence class.
- **draft-hardman-verifiable-voice-protocol-08** (new-draft, score 8, trust_infrastructure) [none]: [Verifiable Voice Protocol](https://datatracker.ietf.org/doc/draft-hardman-verifiable-voice-protocol/) — Verifiable Voice Protocol (VVP) authenticates and authorizes
   organizations and individuals making and/or receiving telephone
   calls.  This eliminates trust gaps that malicious parties exploit.
   Like related technologies such as SHAKEN, RCD, and BCID, VVP uses
   STIR to bind cryptographic evidence to a SIP INVITE, and verify this
   evidence downstream.  VVP can also let evidence flow the other way,
   proving things about the callee.  VVP builds from different technical
   and governance assumptions than alternatives, and uses richer,
   stronger evidence.  This allows VVP to cross jurisdictional
   boundaries easily and robustly.  It also makes VVP simpler, more
   decentralized, cheaper to deploy and maintain, more private, more
   scalable, and higher assurance.  Because it is easier to adopt, VVP
   can plug gaps or build bridges between other approaches, functioning
   as glue in hybrid ecosystems.  For example, it may justify an A
   attestation in SHAKEN, or an RCD passport for branded calling, when a
   call originates outside SHAKEN or RCD ecosystems.  VVP also works
   well as a standalone mechanism, independent of other solutions.  An
   extra benefit is that VVP enables two-way evidence sharing with
   verifiable text and chat (e.g., RCS and vCon), as well as with other
   industry verticals that need verifiability in non-telco contexts.
- **draft-lynch-ai-visibility-lifecycle-03** (new-draft, score 8, adjacent_watchlist) [none]: [The AI Visibility Lifecycle Framework](https://datatracker.ietf.org/doc/draft-lynch-ai-visibility-lifecycle/) — This document describes the 11-Stage AI Visibility Lifecycle, a
   proposed analytical model of how AI systems discover, understand,
   trust and show websites to people.  The eleven stages fall into three
   related phases -- AI Comprehension (Stages 1-5), Trust Establishment
   (Stages 6-8), and Human Visibility (Stages 9-11).  The lifecycle is
   non-linear: Stages 1-2 come first for any page; Stages 3-11 are
   weighed together, and a domain can be progressing in several at once.
   Its figures are illustrative examples (analytical estimates), and its
   descriptions of how AI systems work are inferred from observed
   behaviour, not documented internals.  Its contribution is a common
   vocabulary and a dependency map for telling crawlability from
   visibility and for measuring each element, with the claims that rest
   on outside research cited to it in the deposited specifications.  Its
   figures and some of its mechanisms are provisional and remain to be
   tested.
- **draft-mih-agent-settlement-records-00** (new-draft, score 8, core_identity) [none]: [Two-Party Settlement Records for Agent Payments](https://datatracker.ietf.org/doc/draft-mih-agent-settlement-records/) — A payment between two agents is observed by two systems: the payer's
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
- **draft-mo-cats-agent-state-affinity-00** (new-draft, score 8, agent_identity) [none]: [State, Storage, and Compute Affinity for AI Agent Service Selection in Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-mo-cats-agent-state-affinity/) — AI agent services are stateful and long-running: the speed with which
   a step can be served depends on whether the session's context,
   retrieved data, tool results, and model-side state such as a
   key-value (KV) cache are already available at, or near, the selected
   service contact instance, and on whether the computation that the
   step needs is ready there. Computing-Aware Traffic Steering (CATS)
   exposes computing and network metrics and defines service contact
   instance affinity, but it does not expose the availability of
   reusable state, does not distinguish a hard locality constraint on
   state from a preference for reusing it, does not provide a way to
   compare the cost of moving state with the cost of recomputing it, and
   does not represent the readiness of a specific computation. This
   document describes affinity in three coupled dimensions -- state,
   storage, and compute -- for agent service selection. It states the
   motivation and the goals of introducing affinity, the requirements
   and constraints that affinity places on the mapping of an agent
   workload onto storage and compute resources, the metrics and
   measurement methods by which affinity is observed, the mechanisms and
   the procedure by which affinity is assured, and two cases in detail:
   a long-horizon session that passes through several stages, and a
   group of similar agents or of tenants served by shared reusable
   state. This document defines no wire protocol, no encoding, and no
   data model, and it does not define the transfer mechanisms
   themselves.
- **draft-palanisamy-scitt-aac-runtime-00** (new-draft, score 8, trust_infrastructure) [none]: [The model_attestation Block for Agent Action Capsules: Model, Runtime, and Hardware Claims](https://datatracker.ietf.org/doc/draft-palanisamy-scitt-aac-runtime/) — This document defines the model_attestation block of the Agent Action
   Capsule (AAC) profile — referenced twice by the base profile but
   never defined there — and, within it, the compute_attestation
   container that already carries runtime extensions in the field: the
   model-serving runtime, the agent's own execution environment
   (architectural pattern, orchestration framework, sandbox confinement,
   invoked tool version), and host hardware, together with model and
   weights claims.  Every claim carries an explicitly declared source; a
   verifier grades claims by how they were observed and never infers a
   stronger grade than the evidence supports.  Hardware or platform
   attestation, when present, is cited by content-addressed reference to
   a foreign attestation record and verified with that record's own
   verifier.
- **draft-sharif-typed-evidence-record-00** (new-draft, score 8, trust_infrastructure) [none]: [The Typed-Evidence Record: A Legally-Operative, Trust-Graded Record Format for Machine-Generated Evidence](https://datatracker.ietf.org/doc/draft-sharif-typed-evidence-record/) — A tamper-evident record establishes that data has not been altered.
   It does not, by itself, establish what legally-operative fact the
   data evidences, nor how far the data may be relied upon.  This
   document defines the Typed-Evidence Record (TER): an interoperable
   record format in which a machine-generated record, such as a record
   of an action taken by an autonomous agent, is expressed as a set of
   legally-operative facts, carries an evidence grade reflecting its
   level of cryptographic attestation, carries a per-fact robustness
   indication, and carries the result of an independent integrity
   verification of its source.  A Typed-Evidence Record binds to, and
   does not replace, the underlying signed record it describes.

   This document specifies the record format and the requirements a
   record and a relying party MUST meet to be interoperable.  It does
   not specify how the legally-operative facts are produced from a
   source record; that is an implementation concern outside the scope
   of this document.
- **draft-wang-jep-receipt-profile-01** (new-draft, score 8, core_identity) [none]: [JEP Receipt Profile: Verifiable Behavior and Evidence Receipts](https://datatracker.ietf.org/doc/draft-wang-jep-receipt-profile/) — This document defines JEP Receipt Profile 1 (JEP-RP-1), a minimal
   receipt and evidence profile for the Judgment Event Protocol (JEP).

   JEP-RP-1 binds a JEP event to one digest-addressed receipt record
   through a critical JEP extension.  It defines a small behavior-record
   format, portable receipt manifests and bundles, and independent
   receipt-validation checks.  JEP remains authoritative for event
   verbs, Event Identity, Event Hash, signature processing, references,
   extension processing, validation modes, and acceptance semantics.

   Receipt records are technical evidence about observable behavior and
   related artifacts.  JEP-RP-1 does not assign legal liability, prove
   subjective intent, establish authorization validity, determine
   causality or factual truth, define governance outcomes, or establish
   regulatory compliance.
- **draft-ahuja-agent-routing-policy-02** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.

## Monitor

- **draft-cel-nfsv4-rpc-tls-dane-01** (new-draft, score 6, core_identity) [none]: [Using RPC-with-TLS with DNS-Based Authentication of Named Entities](https://datatracker.ietf.org/doc/draft-cel-nfsv4-rpc-tls-dane/) — RPC-with-TLS assumes that DNS-Based Authentication of Named Entities
   (DANE) is available on platforms where it is deployed, and recommends
   that a client operating under an opportunistic security policy check
   for a TLSA record before initiating an association, but does not say
   how.  This document specifies the missing details, so that a TLSA
   record authenticates an RPC server with no certification authority
   trust anchor provisioned on the client.  It updates RFC 9289.
- **draft-ietf-lake-edhoc-psk-10** (new-draft, score 6, core_identity) [lake]: [LAKE Authenticated with Pre-Shared Keys (PSKs)](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-psk/) — This document specifies a Pre-Shared Key (PSK) authentication method
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
- **draft-ietf-lamps-rfc6211-update-04** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects errors in the definition
   of the id-aa-cmsAlgorithmProtect ASN.1 object identifier.  The IANA
   registry entry has always been correct.
- **draft-khandelwal-bmwg-agent-memory-integrity-01** (new-draft, score 6, agent_identity) [none]: [A Benchmarking Method for the Integrity of AI Agent Memory at Rest](https://datatracker.ietf.org/doc/draft-khandelwal-bmwg-agent-memory-integrity/) — AI agents increasingly persist memory across sessions and treat that
   memory, on the next turn, as if it were their own prior experience.
   This document defines a benchmarking method that measures whether an
   agent's memory subsystem detects that its persisted memory has been
   altered, removed, reordered, replayed, or forged at the storage
   layer, and refuses to serve that memory or reports it before it is
   served.  The method defines eight storage-level edits, three verdict
   classes, a detection-point distinction between read time and audit
   time, three control cases, and a scoring rule.  It is a laboratory
   method for controlled, reproducible measurement, in the spirit of RFC
   2544 and RFC 8239, and it is intended as a test method for the
   "Protection of Memory Data Integrity" metric under discussion in the
   Benchmarking Methodology Working Group.  This revision adds a control
   that proves each edit landed as intended, reports the method's
   results on thirteen memory subsystems including six that claim tamper
   evidence, and records the first vendor fix made in response to a
   measurement.
- **draft-kott-numina-pair-binding-00** (new-draft, score 6, adjacent_watchlist) [none]: [An Evidence Preserving Companion Record for the fixed string numina.pair-binding.v1 / Ed25519: A design study of Ed25519; the universal pair binding model.](https://datatracker.ietf.org/doc/draft-kott-numina-pair-binding/) — Software attribution may need to be clarified after release artifacts
   and their cryptographic commitments have been fixed.  Editing those
   artifacts would disturb the evidence that an attribution statement is
   intended to describe.  This paper proposes a separately versioned
   companion record that associates two unchanged source commitments
   with explicit named attribution and an opaque reference to a private
   genesis record.  The construction uses JSON Canonicalization Scheme
   (JCS) bytes, an application-specific message prefix, and pure Ed25519
   signatures.  Its verification model separates payload integrity,
   signing authority, source equality, revision freshness, and private
   reference resolution.  A Numina example preserves two existing
   SHA-256 commitments and records an owner-defined person-to-alias map
   without treating labels as proof of authorship or mathematical
   derivation.  Historical records report reproduction of both
   commitments.  A later byte comparison establishes equality of the
   selected v155 inputs and hash profile, without establishing whole-
   source equality or a deployed signed binding.  The contribution is a
   proposed evidence-preservation and reporting discipline, rather than
   a new cryptographic primitive.  A public-safe record would require
   its own approved payload and signature.  Trust provisioning,
   implementation tests, and public reproducibility remain open.
- **draft-lohmann-qikvrt-epistemic-status-00** (new-draft, score 6, authorization) [none]: [QIK-VRT Epistemic Status Profile for Evidence-Bound Machine Claims](https://datatracker.ietf.org/doc/draft-lohmann-qikvrt-epistemic-status/) — This document defines an Experimental application-layer profile for
   representing the epistemic status of claims emitted or processed by
   machine cognition systems.  The profile requires a claim not to be
   represented with a stronger epistemic status than its validated,
   provenance-bound evidence supports.

   The profile distinguishes object truth from epistemic truthfulness.
   It does not guarantee that external sources are true, that reasoning
   is infallible, or that the external world is completely observable.
   It specifies how an implementation reports what is proved, observed,
   source-bound, interpretative, normative, predicted, or open.

   The profile is designed to compose with QIK-VRT EFFECT_ACK without
   modifying the five-state EFFECT_ACK version-1 wire contract.
   EFFECT_ACK controls downstream effect authorization; this profile
   controls the strength of epistemic claims.
- **draft-munro-cips-00** (new-draft, score 6, core_identity) [none]: [Contextual IP Prefix Semantics (CIPS)](https://datatracker.ietf.org/doc/draft-munro-cips/) — This document defines Contextual IP Prefix Semantics (CIPS), a model
   that distinguishes addresses, canonical prefixes, addresses with
   prefix context, and prefix selectors, and describes how these forms
   are qualified by operational context.  It provides a taxonomy of
   operational contexts and vocabulary for stating implementation
   support.  In that vocabulary, canonical-prefix support means the
   canonical prefix form is preserved as its own identity; accepting
   slash-qualified text is not that capability.  The model is intended
   to help specification authors, API and schema designers, tool
   authors, and operators preserve semantic distinctions when prefix-
   bearing values cross interchange boundaries.
- **draft-skyfire-oauth-amr-values-02** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-02** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-arsentev-agent-run-metrics-01** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Run Metrics: A JSON Interchange Format for Resource Accounting of Language-Model Agent Runs](https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/) — Autonomous software agents driven by large language models execute
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
- **draft-intra-handshake-fail-55** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100835 of CVSS 9.1, CVE-2026-92701 of CVSS 9.1, CVE-2026-92702 of CVSS 9.1, CVE-2026-100833 of CVSS 8.2, CVE-2026-33697 of CVSS 7.5, and 36 other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-33697],
   [EUVD-2026-16488], [CVE-2026-92701], [EUVD-2026-83194],
   [CVE-2026-92702], [EUVD-2026-83192], [CVE-2026-100833],
   [EUVD-2026-87851] and several GitHub Security Advisories (GHSAs)
   which provide substantial technical evidence of how early attestation
   fails in practice, even *without physical access* to the desired
   machine.  Moreover, since continuous attestation is generally
   required [CSA-eBPF] [MITRE-Continuous-Attestation], early attestation
   adds *unnecessary complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA], [EarlyAttestationBleed] and the
   artifacts [Intra-handshake.fail-repo] in state-of-the-art formal
   analysis tool, ProVerif, under Apache-2.0 license for
   reproducibility, extensibility, and review, and have been
   acknowledged by the relevant stakeholders.  Currently, there are
   *three CVEs of CVSS 9.1, one CVE of CVSS 8.2, one CVE of CVSS 7.5,
   several GHSAs published against the broader early attestation
   covering all layers of the ecosystem up to the application*. The
   research papers on these are currently either under submission or
   being prepared for submission.  The artifacts of these papers will be
   shared with the community under Apache-2.0 license for
   reproducibility, extensibility, and review.  Based on our work, all
   except two implementations of early attestation have been archived,
   withdrawn, or moved to post-handshake attestation.  In our analysis
   [Intra-handshake.fail-repo] and [ID-Crisis-repo], the remaining two
   implementations of early attestation -- Edgeless Systems Contrast and
   Meta's AI -- remain vulnerable.  We recommend users of these two
   implementations to carefully evaluate their systems and understand
   the risks.
- **draft-janz-nmrg-adhoc-semantic-reconciliation-00** (new-draft, score 5, adjacent_watchlist) [none]: [Portable Semantic Models and Ad Hoc Reconciliation by Cognitive Agents in Network Management](https://datatracker.ietf.org/doc/draft-janz-nmrg-adhoc-semantic-reconciliation/) — Interoperation between network-management systems has traditionally
   required a data model agreed in advance.  Where that is insufficient,
   a richer shared information model or ontology is agreed instead.
   Both demand broad prior agreement, negotiated and maintained by
   people.  This document examines what becomes possible once the
   systems on each side can reason.  Each side can lift its own data
   into a complete semantic model.  Two such models can then reconcile
   ad hoc, for the occasion, with no model agreed beforehand.

   The document develops the semantic model and the two operations upon
   it: the lift that produces a model, and the reconciliation that
   bridges two.  It gives careful treatment to pragmatics, the layer a
   schema is least likely to hold and so the part most easily left out
   of view, yet often one that carries key operative meaning.  It
   considers the form and utility of thin references, separately
   assessing the two distinct roles they may play.  It then reports an
   empirical study across four network-management scenarios, run over
   independently constructed cases and several cognitive-agent families.
   The study measures the portability of a lifted model, the extent to
   which cognition can reconcile divergent models without support of a
   pre-agreed standard, where a reference is load-bearing and what it
   usefully comprises.  It closes with conclusions for how information
   should be prepared for cognitive systems, and for how the community's
   standardization effort might evolve.

   This is a research document intended to inform discussion in the IRTF
   Network Management Research Group.  It reflects the authors' ideas,
   thoughts and experimental findings and does not represent IETF or
   IRTF consensus.
- **draft-konda-agentproto-evaluation-state-00** (new-draft, score 5, authorization) [none]: [Preserving Evaluation State in Agent Protocol Decisions](https://datatracker.ietf.org/doc/draft-konda-agentproto-evaluation-state/) — Agent protocols often require a participant to establish a decision-
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
   audit documents can satisfy them in their own formats.  A subsequent
   revision will specify concrete representations.
- **draft-nault-email-ai-signal-00** (new-draft, score 5, adjacent_watchlist) [none]: [Email AI-Processing Preference Signal](https://datatracker.ietf.org/doc/draft-nault-email-ai-signal/) — This document proposes an experimental Internet email header field
   for expressing sender preferences about AI assistance, persistent AI
   memory, profiling, model training, and external processing.  It
   defines syntax, category semantics, message scope, and preservation
   during forwarding and replies.  A missing field expresses no
   preference.  Receiver admission controls and a protective processing
   default are specified separately.  The signal does not establish
   legal consent or guarantee recipient compliance.
- **draft-ietf-plants-merkle-tree-certs-07** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
   certificates which integrate public logging of the certificate, in
   the style of Certificate Transparency.  The integrated design reduces
   logging overhead in the face of both shorter-lived certificates and
   large post-quantum signature algorithms, while still achieving
   comparable security properties to existing X.509 constructions and
   Certificate Transparency.  Merkle Tree certificates additionally
   admit an optional size optimization that avoids signatures
   altogether, at the cost of only applying to up-to-date relying
   parties and older certificates.
- **draft-palanisamy-scitt-aac-otel-00** (new-draft, score 4, adjacent_watchlist) [none]: [OpenTelemetry Correlation Extension for Agent Action Capsules](https://datatracker.ietf.org/doc/draft-palanisamy-scitt-aac-otel/) — This document defines org.agentactioncapsule.otel, a namespaced
   payload extension for the Agent Action Capsule profile.  The
   extension carries OpenTelemetry trace and span context alongside a
   sealed agent-action record so that the Capsule and the observability
   spans describing the same action can be joined after the fact.  It
   maps the OpenTelemetry Generative AI semantic conventions onto
   Capsule fields where a mapping is well defined and states which
   OpenTelemetry values MUST NOT enter a Capsule at all.  The extension
   does not alter Capsule verification: a verifier that does not
   implement it treats the block as informational.

## Adjacent / watchlist

- **draft-acee-lsr-ospfv3-deprecate-ah-01** (new-draft, score 3, core_identity) [none]: [Deprecation of the IPsec Authentication Header (AH) for OSPFv3 Authentication](https://datatracker.ietf.org/doc/draft-acee-lsr-ospfv3-deprecate-ah/) — RFC 4552 specifies the use of the IPsec Authentication Header (AH)
   and the Encapsulating Security Payload (ESP) to provide
   authentication and confidentiality for OSPFv3.  This document
   deprecates the use of AH for OSPFv3 and updates RFC 4552 accordingly.
   Operators are encouraged to use either ESP with NULL encryption, as
   specified in RFC 4552, or the OSPFv3 Authentication Trailer, as
   specified in RFC 7166.
- **draft-albanna-regext-eku-mtls-in-epp-04** (new-draft, score 3, core_identity) [regext]: [Extended Key Usage and Mutual TLS in EPP](https://datatracker.ietf.org/doc/draft-albanna-regext-eku-mtls-in-epp/) — This document describes the state of the Mutual Transport Layer
   Security (mTLS) client authentication mechanism in the Extensible
   Provisioning Protocol (EPP) with respect to the 15th June 2025 policy
   change that triggered a modification in the client certificates
   published by some Certificate Authorities (CAs).  The issue is
   described and options are presented to address the operational impact
   of the change.
- **draft-bhatti-ilnp-ip6-apps-01** (new-draft, score 3, core_identity) [none]: [ILNP usage by IPv6 applications](https://datatracker.ietf.org/doc/draft-bhatti-ilnp-ip6-apps/) — The Identifier Locator Network Protocol (ILNP) for IPv6 is described
   in Experimental RFCs 6740-6744.  ILNP uses a different architecture
   to IPv6 but is implemented to work with IPv6.  This document
   describes how unmodified IPv6 applications running on an ILNP-capable
   node can make use of ILNP.  This document updates RFC6740, RFC6741,
   RFC6748.
- **draft-bhatti-ilnp-nonce-01** (new-draft, score 3, core_identity) [none]: [Use of the ILNP Nonce Destination Option Header](https://datatracker.ietf.org/doc/draft-bhatti-ilnp-nonce/) — The Identifier Locator Network Protocol (ILNP) for IPv6 is described
   in Experimental RFCs 6740-6744.  ILNP packets for IPv6 are
   distinguished from normal IPv6 packets by the presence of the Nonce
   Destination Option Header (aka "Nonce Header"), as defined in
   RFC6744.  This document clarifies the use of the Nonce Header for
   ILNP.  This document updates RFC6740, RFC6741, RFC6744.
- **draft-bhatti-ilnp-preference-01** (new-draft, score 3, core_identity) [none]: [ILNP addressing using Preference values](https://datatracker.ietf.org/doc/draft-bhatti-ilnp-preference/) — The Identifier Locator Network Protocol (ILNP) for IPv6 is described
   in Experimental RFCs 6740-6744.  This document clarifies how
   addressing in ILNP makes use of Preference values with Locator (L64)
   and Node Identifier (NID) values.  This includes the way that
   Preference values are used for forming Identifier-Locator Vector
   (I-LV) values, and selecting I-LVs for use.  This document updates
   RFC6740, RFC6741, RFC6742, RFC6748.
- **draft-bhatti-ilnp-tcp-udp-checksums-01** (new-draft, score 3, core_identity) [none]: [TCP and UDP checksum calculations for ILNP](https://datatracker.ietf.org/doc/draft-bhatti-ilnp-tcp-udp-checksums/) — The Identifier Locator Network Protocol (ILNP) for IPv6 is described
   in Experimental RFCs 6740-6744.  ILNP defines the use of an
   Identifier-Locator Vector (I-LV) with a zero value L64 value and a
   relevant Node Identifier (NID) value in place of an IPv6 address in
   the pseudo-header for transport protocol checksum computations.
   However, as TCP and UDP predate ILNP, this change causes TCP and UDP
   checksum values to be generated for ILNP flows that are different to
   the same flows on IPv6.  This document changes the checksum
   computation for TCP and UDP with ILNP so that the checksum values are
   the same for ILNP and IPv6.  This document updates the checksum
   processing for TCP and UDP described in RFC6740 and RFC6741, and the
   way the checksum processing should be applied for TCP and UDP in
   RFC6748.
- **draft-bhatti-ilnp-textual-representations-01** (new-draft, score 3, core_identity) [none]: [ILNP textual representations](https://datatracker.ietf.org/doc/draft-bhatti-ilnp-textual-representations/) — The Identifier Locator Network Protocol (ILNP) for IPv6 is described
   in Experimental RFCs 6740-6744.  This document describes how values
   for ILNP data-types SHOULD be represented in textual form.  These
   data-types are: the Locator (L64), the Node Identifier (NID), and the
   Identifier-Locator Vector (I-LV).  The notation for the textual
   representation is defined formally.  Use-cases are provided as
   examples of real world usage.  This document updates RFC6740,
   RFC6741, RFC6742.
- **draft-ietf-calext-jscalendarbis-22** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-dmm-udp-tunnel-acaas-extn-02** (new-draft, score 3, adjacent_watchlist) [dmm]: [A YANG Data Model Extension for Attachment Circuit as a Service with UDP Tunnel Support](https://datatracker.ietf.org/doc/draft-ietf-dmm-udp-tunnel-acaas-extn/) — Delivery of network services over a Layer 3 tunnel assumes that the
   appropriate setup is provisioned over links that connect the customer
   termination points and provider network.  The required setup to allow
   successful data exchange over these links is referred to as an
   attachment circuit (AC) while the underlying link for carrying
   network services is referred to as "bearer", in this case a Layer 3
   UDP tunnel.

   This document specifies an extension for UDP tunnel as Layer 3 bearer
   to the YANG service data model for AC.
- **draft-ietf-ediint-rfc4130bis-05** (new-draft, score 3, core_identity) [ediint]: [AS2 Specification Modernization](https://datatracker.ietf.org/doc/draft-ietf-ediint-rfc4130bis/) — This document provides an applicability statement (RFC 2026,
   Section 3.2) describing how to securely exchange structured business
   data over HTTP.  Structured business data may be XML; Electronic Data
   Interchange (EDI) in either the American National Standards Committee
   (ANSI) X12 format or the UN Electronic Data Interchange for
   Administration, Commerce, and Transport (UN/EDIFACT) format; or other
   structured data formats.  The data is packaged using standard MIME
   structures.  Authentication and data confidentiality are obtained by
   using Cryptographic Message Syntax with S/MIME security body parts
   (see Section 10.1).  Authenticated acknowledgements make use of
   multipart/signed Message Disposition Notification (MDN) responses to
   the original HTTP message.  This applicability statement is
   informally referred to as "AS2" because it is the second
   applicability statement, produced after "AS1" (RFC 3335).  This
   document obsoletes RFC 4130 and stands on its own without reference
   to AS1 or SMTP, except where required for IANA registry updates.

   This document also updates IANA registries originally created by RFC
   3335 and RFC 4130.
- **draft-ietf-httpbis-no-vary-search-10** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The No-Vary-Search HTTP Caching Extension](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) — This specification defines an extension to HTTP Caching, changing how
   the URI query component impacts caching.  It introduces the "No-Vary-
   Search" response header field, which allows origin servers to signal
   to caches that certain parts of the query component do not
   semantically affect the served response and can be ignored for cache
   matching purposes.
- **draft-ietf-httpbis-resumable-upload-13** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Resumable Uploads for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/) — HTTP data transfers can encounter interruption due to reasons such as
   canceled requests or dropped connections.  If the intended recipient
   can indicate how much of the data was processed prior to
   interruption, a sender can resume data transfer at that point instead
   of attempting to transfer all of the data again.  HTTP range requests
   support this concept of resumable downloads from server to client.
   This document describes a mechanism that supports resumable uploads
   from client to server using HTTP.
- **draft-ietf-jmap-calendars-32** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-lamps-pq-composite-kem-22** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/) — This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.
- **draft-ietf-nmop-network-incident-yang-18** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
   lifecycle management.  This YANG module provides a standard way to
   report, diagnose, and help reduce troubleshooting tickets and resolve
   network incidents for the sake of network service health and probable
   root cause analysis.
- **draft-ietf-opsawg-collected-data-manifest-16** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push (RFC
   8641), to continuously stream information, including both counters
   and state information.  This document describes the metadata that
   ensure that the collected data can be interpreted correctly.  This
   document specifies the Data Manifest, composed of two YANG data
   models (the Platform Manifest and the non-normative Data Collection
   Manifest).  These YANG modules are specified at the network level
   (e.g., network controllers) to provide a model that encompasses
   several network platforms.  The Data Manifest must be streamed and
   stored along with the data, up to the collection and analytics
   systems to keep the collected data fully exploitable by the data
   scientists and relevant tools.  Additionally, this document specifies
   an augmentation of the YANG-Push model to include the actual
   collection period, in case it differs from the configured collection
   period.
- **draft-ietf-tcpm-tcp-ao-algs-08** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-ietf-v6ops-framework-md-ipv6only-underlay-29** (new-draft, score 3, adjacent_watchlist) [v6ops]: [Framework for Multi-domain IPv6-only Network and IPv4-as-a-Service](https://datatracker.ietf.org/doc/draft-ietf-v6ops-framework-md-ipv6only-underlay/) — This document presents a framework, from the network operators'
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
- **draft-ietf-vcon-overview-02** (new-draft, score 3, core_identity) [vcon]: [The vCon - Conversation Data Container - Overview](https://datatracker.ietf.org/doc/draft-ietf-vcon-overview/) — A vCon is the container for information relating to a real-time,
   human conversation.  It is analogous to a [vCard] which enables the
   definition, interchange and storage of an individual's various points
   of contact.  The data contained in a vCon may be derived from any
   multimedia session, traditional phone call, video conference, SMS or
   MMS message exchange, webchat or email thread.  The data in the
   container relating to the conversation may include Call Detail
   Records (CDR), call meta data, participant identity information
   (e.g., STIR PASSporT), the actual conversational data exchanged
   (e.g., audio, video, text), realtime or post conversational analysis
   and attachments of files exchanged during the conversation.  A
   standardized conversation container enables many applications,
   establishes a common method of storage and interchange, and supports
   identity, privacy and security efforts (see [vCon-white-paper])
- **draft-linker-diem-adem-core-01** (new-draft, score 3, adjacent_watchlist) [none]: [ADEM Core Specification](https://datatracker.ietf.org/doc/draft-linker-diem-adem-core/) — In times of armed conflict, the protective emblems of the red cross,
   red crescent, and red crystal are used to mark physical assets.  This
   enables military units to identify assets as respected and protected
   under international humanitarian law.  This draft specifies the
   format and trust architecture of a protective, digital emblem to
   network-connected infrastructure.  Such emblems mark assets as
   protected under IHL analogously to the physical emblems.
- **draft-prabhu-nmrg-prompt-schema-llm-01** (new-draft, score 3, adjacent_watchlist) [none]: [Framework for Normalizing Multi-Vendor Network Inputs for LLM-Assisted Network Management](https://datatracker.ietf.org/doc/draft-prabhu-nmrg-prompt-schema-llm/) — Large Language Models (LLMs) are increasingly used to assist network
   management tasks such as troubleshooting, intent translation, and
   automation.  Network operations, however, rely on data from many
   vendors and sources: CLI output, configuration snippets, telemetry,
   alarms, and vendor-specific APIs.  These inputs differ in format,
   structure, and semantics, which makes it difficult to present a
   consistent interface to an LLM.  This document describes a framework
   for standardizing such multi-vendor inputs for LLM-assisted network
   management.  Incoming messages from multi-vendor network elements are
   first handled by an Input Classifier, which determines the nature of
   each input and assigns it to one of three categories: performance,
   configuration, or response, using a hybrid approach (rule-based
   classification first, with escalation to a Small Language Model (SLM)
   when rules are insufficient).  The classified input is then passed to
   the corresponding Structurer among the Performance Structurer,
   Configuration Structurer, and Response Structurer, each of which
   produces a normalized, structured representation (typically with SLM
   assistance and optional confidence scoring).  That structured output
   is fed to a Prompt Schema Generator, which creates a structured,
   vendor-agnostic schema and supplies schema-aligned prompts to the
   central LLM.  This document specifies the architecture and component
   roles for use in design and implementation.  It does not define a
   wire protocol; it is published for informational purposes.
- **draft-sweet-settle-requirements-00** (new-draft, score 3, adjacent_watchlist) [none]: [SEcure access To Tls Local rEsources (SETTLE) Problem Statement and Requirements](https://datatracker.ietf.org/doc/draft-sweet-settle-requirements/) — This document defines the problem statement, common terminology,
   security models, and technical requirements for identifying,
   validating, and establishing secure connections with local network
   devices.  It outlines the challenges of extending the Web's Public
   Key Infrastructure (PKI) to local, offline, or "limited domain"
   environments.  The document specifies requirements for privacy-
   preserving discovery, generating and distributing local trust
   anchors, and establishing mutually authenticated secure contexts
   without relying on global certificate authorities or problematic
   Trust On First Use (TOFU) mechanisms.
- **draft-bernardos-nmrg-agentic-network-optimization-02** (new-draft, score 2, agent_identity) [none]: [Solutions for enabling agentic sensing with network optimization](https://datatracker.ietf.org/doc/draft-bernardos-nmrg-agentic-network-optimization/) — Integrated Sensing and Communications (ISAC) represents a paradigm
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
- **draft-dogru-cedulon-decision-profile-04** (new-draft, score 2, ignored_after_review) [none]: [Cedulon Decision Profile: Reconciling an Agent's Decisions Against Its Effects](https://datatracker.ietf.org/doc/draft-dogru-cedulon-decision-profile/) — The Cedulon core document reconciles an issuer's signed Spend
   Receipts against an authenticated extract of a payment rail and
   reports, over a declared population, that no settlement lacks a
   receipt and no settled receipt is absent from the rail.  Money is the
   special case that document implements.  This document defines a
   second population on the same reconciler.  A Decision Record is
   signed by the party that decided whether an agent may act; an Effect
   Extract is an authenticated list of the effects that actually
   occurred on a channel.  An allow must be matched by exactly one
   effect whose content hash the record named; a refusal must be matched
   by none.  The Decision Record claim set, the Effect Extract shape,
   the points at which the reconciliation departs from the spend rules,
   the finding codes, and one media type are defined.  This revision
   lets a deployment sign checkpoints under a separate key inside the
   decider root, states that single-row extracts are receipts rather
   than windows and what a deployment that signs them must state, and
   records a second implementation and two outside runs of its test
   vectors.  The text is provisional; the companion implementation
   carrying this profile is published.
- **draft-ietf-deleg-12** (new-draft, score 2, ignored_after_review) [deleg]: [Extensible Delegation for DNS](https://datatracker.ietf.org/doc/draft-ietf-deleg/) — This document specifies a new extensible method for the delegation of
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
- **draft-ietf-dnsop-delext-12** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895 and 9824.
- **draft-ietf-lisp-site-external-connectivity-05** (new-draft, score 2, ignored_after_review) [lisp]: [LISP Site External Connectivity](https://datatracker.ietf.org/doc/draft-ietf-lisp-site-external-connectivity/) — This draft defines how to register/retrieve pETR mapping information
   in LISP when the destination is not registered/known to the local
   site and its mapping system (e.g. the destination is an internet/
   external site destination or scale-out/scale-across end point in
   backend networks of AI Infrastructure).
- **draft-ietf-mailmaint-pacc-04** (new-draft, score 2, ignored_after_review) [mailmaint]: [Automatic Configuration of Email, Calendar, and Contact Server Settings](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pacc/) — This document specifies an automatic configuration mechanism for
   email, calendar, and contact user agent applications.  Domain owners
   publish standardized configuration information that user agent
   applications retrieve and use to simplify server setup procedures.
- **draft-janbjer-dewp-00** (new-draft, score 2, ignored_after_review) [none]: [Deterministic Evidence & Witness Protocol (DEWP) Specification](https://datatracker.ietf.org/doc/draft-janbjer-dewp/) — This document specifies the Deterministic Evidence and Witness
   Protocol (DEWP), a format for tamper-evident audit commitments and
   offline evidence verification.  It defines canonical event preimages,
   domain-separated hashing, two-tier Merkle inclusion proofs, per-
   tenant sequence checks, checkpoint continuity, and independently
   verifiable anchor evidence.  Verifiers report content, commitment,
   embedded-signature, and anchor verification separately.  Completeness
   checks cover committed events within the evaluated range; they cannot
   prove that an event was never withheld before commitment or that a
   committed description accurately records a real-world action.  The
   specification also defines a streaming format that the reference
   implementations do not yet implement.
- **draft-nault-email-ai-handling-00** (new-draft, score 2, ignored_after_review) [none]: [Handling Email AI-Processing Preferences](https://datatracker.ietf.org/doc/draft-nault-email-ai-handling/) — This document proposes an experimental receiver handling profile for
   the companion Email AI-Processing Preference Signal.  It requires
   evaluation before optional AI access, independent checks for each
   applicable use, and a protective default when a preference is absent.
   It addresses confirmation, mixed-source content, derived records, and
   usable ordinary communication when optional processing is declined.
   Requirements apply to systems claiming this profile, not to all
   Internet mail recipients; the profile does not determine legal
   consent.

## Ignored after review

- **draft-alivar-6man-icmp-error-srv6-vpn-00** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for VPNs in SRv6 Networks](https://datatracker.ietf.org/doc/draft-alivar-6man-icmp-error-srv6-vpn/) — The document specifies procedures for handling ICMP error messages in
   SRv6-based Virtual Private Network (VPN).  It describes three methods
   to improve the ICMP Error Handling for SRv6-VPNs.
- **draft-denis-uricrypt-05** (new-draft, score 0, ignored_after_review) [none]: [Prefix-Preserving Encryption for URIs](https://datatracker.ietf.org/doc/draft-denis-uricrypt/) — This document specifies URICrypt, a deterministic, prefix-preserving
   encryption scheme for Uniform Resource Identifiers (URIs).  URICrypt
   encrypts URI paths while preserving their hierarchical structure,
   enabling systems that rely on URI prefix relationships to continue
   functioning with encrypted URIs.  The scheme provides authenticated
   encryption for each URI path component, preventing tampering,
   reordering, or mixing of encrypted segments.
- **draft-frindell-moq-subscription-flow-control-00** (new-draft, score 0, ignored_after_review) [none]: [Subscription Flow Control Extension for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-frindell-moq-subscription-flow-control/) — This document defines an extension to Media over QUIC Transport
   (MOQT) that lets a subscriber limit the number of subgroup streams
   and the total bytes a publisher may send for an individual
   subscription.  It defines a Setup Option to negotiate the extension
   and set initial limits, message parameters for advertising these
   limits, messages for granting credit and signaling flow control
   state, and a session error code.
- **draft-frindell-moq-timestamp-00** (new-draft, score 0, ignored_after_review) [none]: [Timestamp Properties for MOQT](https://datatracker.ietf.org/doc/draft-frindell-moq-timestamp/) — This document defines a set of MOQT Properties for carrying per-
   Object timestamps efficiently.  The encoded timestamp is intended for
   use in MOQT, but can be referenced for application specific purposes.
- **draft-gallagher-openpgp-grease-02** (new-draft, score 0, ignored_after_review) [none]: [GREASE Code Points in OpenPGP](https://datatracker.ietf.org/doc/draft-gallagher-openpgp-grease/) — This document reserves entries in various OpenPGP registries for use
   in interoperability testing, by analogy with GREASE in TLS.
- **draft-gallagher-openpgp-padding-00** (new-draft, score 0, ignored_after_review) [none]: [Padding in OpenPGP](https://datatracker.ietf.org/doc/draft-gallagher-openpgp-padding/) — This document provides updated guidance around the generation of
   padding in OpenPGP data streams.  It does not specify any new OpenPGP
   wire formats, but does propose some higher-level best practices.
- **draft-gerke-publication-process-reform-10** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   The deterministic state-integrity constraints and automated
   milestones defined herein apply programmatically across the core
   processing streams already defined or established in the future.

   This document updates RFC 6359 and RFC 7841.
- **draft-gondwana-dkim2-debug-header-01** (new-draft, score 0, ignored_after_review) [none]: [A Diagnostic Header Field for DKIM2 Implementations](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-debug-header/) — Implementations of DomainKeys Identified Mail Signatures v2 (DKIM2)
   benefit from seeing extra debug information during the early
   deployment phase.

   This document is intended to help testers, and unlikely to be
   published.
- **draft-gondwana-email-header-maintenance-03** (new-draft, score 0, ignored_after_review) [none]: [Maintenance of the IANA Message Header Field Registries](https://datatracker.ietf.org/doc/draft-gondwana-email-header-maintenance/) — The IANA "Message Headers" registries record, for each registered
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
- **draft-hoffman-pq-dnssec-considerations-02** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Selecting Post-Quantum Algorithms for DNSSEC](https://datatracker.ietf.org/doc/draft-hoffman-pq-dnssec-considerations/) — This draft lists many of the considerations that the DNS community
   needs to balance when it is deciding which post-quantum algorithms to
   standardize for DNSSEC.

   This draft is definitely not meant to become an RFC.
- **draft-ietf-6man-rfc8504-bis-04** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 Node Requirements](https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/) — This document defines requirements for IPv6 nodes.  It is expected
   that IPv6 will be deployed in a wide range of devices and situations.
   Specifying the requirements for IPv6 nodes allows IPv6 to function
   well and interoperate in a large number of situations and
   deployments.

   This document obsoletes RFC 8504, and in turn RFC 6434 and its
   predecessor, RFC 4294.
- **draft-ietf-anima-rfc8366bis-37** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Onboarding Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
   device (Pledge) to an Owner using a digital artifact signed, directly
   or indirectly, by the Pledge's manufacturer.  This artifact is known
   as a "Voucher".

   This document defines an artifact format as a YANG-defined JSON or
   CBOR document that has been signed using a variety of cryptographic
   systems.

   The Voucher Artifact is normally generated by the Pledge's
   manufacturer which is represented by the Manufacturer Authorized
   Signing Authority (MASA).

   This document obsoletes RFC8366: it includes a number of desired
   extensions into the YANG module.  The Voucher Request YANG module
   defined in RFC8995 is also updated and now included in this document,
   as well as other YANG extensions needed for variants of RFC8995.
- **draft-ietf-bess-evpn-mvpn-seamless-interop-12** (new-draft, score 0, ignored_after_review) [bess]: [Seamless Multicast Interoperability between EVPN and MVPN PEs](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-mvpn-seamless-interop/) — Ethernet Virtual Private Network (EVPN) solution is becoming
   pervasive for Network Virtualization Overlay (NVO) services in data
   center (DC), Enterprise networks as well as in service provider (SP)
   networks.

   As service providers transform their networks in their Central
   Offices (COs) towards the next generation data center with Software
   Defined Networking (SDN) based fabric and Network Function
   Virtualization (NFV), they want to be able to maintain their offered
   services including Multicast VPN (MVPN) service between their
   existing network and their new Service Provider Data Center (SPDC)
   network seamlessly without the use of gateway devices.  They want to
   have such seamless interoperability between their new SPDCs and their
   existing networks for a) reducing cost, b) having optimum forwarding,
   and c) reducing provisioning.  This document describes a unified
   solution based on RFCs 6513 & 6514 for seamless interoperability of
   Multicast VPN between EVPN and MVPN PEs.  Furthermore, it describes
   how the proposed solution can be used as a routed multicast solution
   in data centers with only EVPN PEs.
- **draft-ietf-bier-source-protection-11** (new-draft, score 0, ignored_after_review) [bier]: [BIER (Bit Index Explicit Replication) Redundant Ingress Router Failover](https://datatracker.ietf.org/doc/draft-ietf-bier-source-protection/) — This document describes a failover in the Bit Index Explicit
   Replication domain with a redundant ingress router.
- **draft-ietf-bmwg-powerbench-03** (new-draft, score 0, ignored_after_review) [bmwg]: [Characterization and Benchmarking Methodology for Power in Networking Devices](https://datatracker.ietf.org/doc/draft-ietf-bmwg-powerbench/) — This document defines a standard mechanism to measure, report, and
   compare power usage of different networking devices under different
   network configurations and conditions.
- **draft-ietf-dconn-domainconnect-04** (new-draft, score 0, ignored_after_review) [dconn]: [Domain Connect Protocol - DNS provisioning between Services and DNS Providers](https://datatracker.ietf.org/doc/draft-ietf-dconn-domainconnect/) — This document provides specification of the Domain Connect Protocol
   that was built to support DNS configuration provisioning between
   Service Providers (hosting, social, email, hardware, etc.) and DNS
   Providers.
- **draft-ietf-grow-routing-ops-sec-inform-03** (new-draft, score 0, ignored_after_review) [grow]: [Current Options for Securing Global Routing](https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/) — The Border Gateway Protocol (BGP) is used for exchanging routing
   information between Autonomous Systems in the Internet.  Due to its
   importance, it is necessary to ensure the basic security properties
   for BGP and BGP speaking routers.  While the general principles for
   securing BGP operations are outlined in RFC 7454, that document does
   not detail the technical and implementation options for securing BGP.

   This document serves as a contemporary, non-exhaustive repository of
   options and methods for securing BGP.  This document explicitly does
   not make value statements on the efficacy of individual techniques,
   nor does it mandate or prescribe the use of specific techniques or
   implementation details.

   Operators are advised to carefully consider whether the listed
   methods are applicable for their use-cases.  Furthermore, the options
   listed in this document may change over time, and should not be used
   as a timeless ground-truth of applicable or sufficient methods.
- **draft-ietf-grow-routing-ops-terms-03** (new-draft, score 0, ignored_after_review) [grow]: [Currently Used Terminology in Global Routing Operations](https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/) — Operating the global routing ecosystem entails a diverse set of
   interacting components, while operational practice evolved over time.
   In that time, terms emerged, disappeared, and sometimes changed their
   meaning.

   To aid operators and implementers in reading contemporary drafts,
   this document provides an overview of terms and abbreviations used in
   the global routing operations community.  The document explicitly
   does not serve as an authoritative source of correct terminology, but
   instead strives to provide an overview of practice.
- **draft-ietf-idr-bgp4-rfc4271bis-02** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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
- **draft-ietf-intarea-extended-icmp-nodeid-07** (new-draft, score 0, ignored_after_review) [intarea]: [ICMP Message Extension for Originating Node Identification](https://datatracker.ietf.org/doc/draft-ietf-intarea-extended-icmp-nodeid/) — RFC5837 describes a mechanism for Extending ICMP for Interface and
   Next-Hop Identification, which allows providing additional
   information in an ICMP error that helps identify interfaces
   participating in the path.  This is especially useful in environments
   where a given interface may not have a unique IP address to respond
   to, e.g., a traceroute.

   This document introduces a similar ICMP extension for Node
   Identification.  It allows providing a unique IP address and/or a
   textual name for the node, in the case where each node may not have a
   unique IP address (e.g., a deployment in which all interfaces have
   IPv6 addresses and all next-hops are IPv6 next-hops, even for IPv4
   routes).
- **draft-ietf-ippm-stamp-ext-hdr-15** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect IPv4/IPv6 headers as well as IPv6
   extension headers for HBH and E2E active measurements, for example,
   using the IOAM data fields.
- **draft-ietf-ipsecme-ikev2-reliable-transport-08** (new-draft, score 0, ignored_after_review) [ipsecme]: [Separate Transports for IKE and ESP](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-reliable-transport/) — The Internet Key Exchange protocol version 2 (IKEv2) can operate
   either over unreliable (UDP) transport or over reliable (TCP)
   transport.  If TCP is used, then IPsec tunnels created by IKEv2 also
   use TCP.  This document specifies how to decouple IKEv2 and IPsec
   transports so that IKEv2 can operate over TCP, while IPsec tunnels
   use unreliable transport.  This feature allows IKEv2 to effectively
   exchange large blobs of data (e.g., when post-quantum algorithms are
   employed) while avoiding performance problems that arise when IPsec
   uses TCP.
- **draft-ietf-lake-edhoc-impl-cons-08** (new-draft, score 0, ignored_after_review) [lake]: [Implementation Considerations for the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-impl-cons/) — This document provides considerations for guiding the implementation
   of the Lightweight Authenticated Key Exchange (LAKE) protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Lightweight
   Authenticated Key Exchange Working Group mailing list
   (lake@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/lake/.

   Source for this draft and an issue tracker can be found at
   https://github.com/lake-wg/edhoc-impl-cons.
- **draft-ietf-lisp-map-server-reliable-transport-09** (new-draft, score 0, ignored_after_review) [lisp]: [LISP Map Server Reliable Transport](https://datatracker.ietf.org/doc/draft-ietf-lisp-map-server-reliable-transport/) — The communication between LISP ETRs and Map-Servers is based on
   unreliable UDP message exchange coupled with periodic message
   transmission in order to maintain soft state.  The drawback of
   periodic messaging is the constant load imposed on both the ETR and
   the Map-Server.  New LISP use cases increase the amount of state that
   needs to be communicated and challenge the scalability of the system
   when using the UDP exchange.  This document introduces the use of a
   reliable transport for ETR to Map-Server communications in order to
   eliminate the periodic messaging overhead, while providing
   reliability, flow-control and endpoint liveness detection.
- **draft-ietf-lisp-nat-traversal-03** (new-draft, score 0, ignored_after_review) [lisp]: [NAT traversal for LISP](https://datatracker.ietf.org/doc/draft-ietf-lisp-nat-traversal/) — This document describes a mechanism for IPv4 NAT traversal for LISP
   tunnel routers (xTR) and LISP Mobile Nodes (LISP-MN) behind a Network
   Address Translator (NAT) device.  A LISP device both detects the NAT
   and initializes its state.  Forwarding to the LISP device through a
   NAT is enabled by the LISP Re-encapsulating Tunnel Router (RTR)
   network element, which acts as an anchor point in the data plane,
   forwarding traffic from unmodified LISP devices through the NAT.
- **draft-ietf-lisp-rfc6831bis-10** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC6831
- **draft-ietf-moq-transport-22** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-netconf-distributed-notif-23** (new-draft, score 0, ignored_after_review) [netconf]: [Subscription to Notifications in a Distributed Architecture](https://datatracker.ietf.org/doc/draft-ietf-netconf-distributed-notif/) — This document describes extensions to the YANG notifications
   subscription to allow metrics being published directly from
   processors on line cards to target receivers, while subscription is
   still maintained at the route processor in a distributed forwarding
   system of a network node.
- **draft-ietf-netconf-yang-notifications-versioning-17** (new-draft, score 0, ignored_after_review) [netconf]: [Support of Versioning in YANG Notifications Subscriptions](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-notifications-versioning/) — This document defines a YANG module which extends the YANG-Push
   Subscription mechanism to enforce that particular revisions or
   semantic versions are used when configuring or establishing a
   Subscription.  It also extends the YANG-Push Subscription state
   change Notifications to include additional context about the YANG
   schema associated with the Subscription.
- **draft-ietf-netmod-yang-semver-29** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Semantic Versioning](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-semver/) — This document specifies a YANG extension along with guidelines for
   applying an extended set of semantic versioning rules to revisions of
   YANG artifacts (e.g., modules and packages).  Additionally, this
   document defines a YANG extension for controlling module imports
   based on these modified semantic versioning rules.

   This document updates RFCs 7950, 9907, and 8525.
- **draft-ietf-nmop-simap-concept-14** (new-draft, score 0, ignored_after_review) [nmop]: [SIMAP: Concept, Requirements, and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/) — This document defines the concept of Service & Infrastructure Maps
   (SIMAP) and identifies a set of SIMAP requirements and use cases.
   The SIMAP was previously known as Digital Map. SIMAP evolves the
   earlier 'Digital Map' concept by making explicit the ties between
   service and infrastructure layers, clarifying expected outcomes for
   operations and automation, and addressing ambiguity associated with
   the term 'digital.'

   The document intends to be used as a reference for the assessment of
   the various topology modules to meet SIMAP requirements.
- **draft-ietf-nvo3-rfc7348bis-11** (new-draft, score 0, ignored_after_review) [nvo3]: [Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks](https://datatracker.ietf.org/doc/draft-ietf-nvo3-rfc7348bis/) — This document specifies Virtual eXtensible Local Area Network
   (VXLAN), which is used to address the need for overlay networks
   within virtualized data centers accommodating multiple tenants.  The
   scheme and the related protocols can be used in networks for cloud
   service providers and enterprise data centers.  This document
   obsoletes RFC 7348, which documented the deployed VXLAN protocol for
   the benefit of the Internet community, and moves the VXLAN
   specification to the IETF document stream, allowing for the creation
   of extensions to VXLAN that require additions to the VXLAN header and
   their registration with IANA.  The format and processing described
   here are fully compatible with those in RFC 7348.
- **draft-ietf-opsawg-rfc5706bis-09** (new-draft, score 0, ignored_after_review) [opsawg]: [Guidelines for Considering Operations and Management in IETF Specifications](https://datatracker.ietf.org/doc/draft-ietf-opsawg-rfc5706bis/) — New Protocols and Protocol Extensions are best designed with due
   consideration of the functionality needed to operate and manage them.
   Retrofitting operations and management considerations is suboptimal.
   The purpose of this document is to provide guidance to authors and
   reviewers on what operational and management aspects should be
   addressed when writing documents in the IETF Stream that document a
   specification for New Protocols or Protocol Extensions or describe
   their use.

   This document obsoletes RFC 5706, replacing it completely and
   updating it with new operational and management techniques and
   mechanisms.  It also updates RFC 2360 to obsolete mandatory MIB
   creation.  Finally, it introduces a requirement to include an
   "Operational Considerations" section in new RFCs in the IETF Stream
   that define New Protocols or Protocol Extensions or describe their
   use (including relevant YANG Models), while providing an escape
   clause if no new considerations are identified.
- **draft-ietf-pim-multicast-over-srv6-01** (new-draft, score 0, ignored_after_review) [pim]: [Multicast over SRv6 networks](https://datatracker.ietf.org/doc/draft-ietf-pim-multicast-over-srv6/) — This document presents solutions for deploying multicast in SRv6
   networks.  It explores the use of the native IPv6 multicast data
   plane for multicast distribution.  The document discusses distributed
   control plane mechanisms, including PIM, and its integration with IGP
   Flex-Algo to optimize multicast delivery.  The document also
   addresses overlay multicast solutions for both the Global
   Table Multicast (GTM) and Multicast VPNs (MVPNs), utilizing IP-in-
   IPv6 encapsulation without requiring additional shim layers.
- **draft-ietf-regext-rdap-jscontact-27** (new-draft, score 0, ignored_after_review) [regext]: [Using JSContact in Registration Data Access Protocol (RDAP) JSON Responses](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-jscontact/) — This document describes an RDAP extension which represents entity
   contact information in JSON responses using JSContact.
- **draft-ietf-rtgwg-atn-bgp-34** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
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
- **draft-ietf-savnet-intra-domain-architecture-05** (new-draft, score 0, ignored_after_review) [savnet]: [Intra-domain Source Address Validation Architecture](https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/) — This document describes a generic architecture for intra-domain
   Source Address Validation (SAV).  It provides a common framework for
   developing new intra-domain SAV mechanisms and describes the
   conditions under which this architecture can improve SAV accuracy and
   operational efficiency with respect to existing intra-domain SAV
   mechanisms.
- **draft-ietf-spring-srv6-security-17** (new-draft, score 0, ignored_after_review) [spring]: [Segment Routing IPv6 Security Considerations](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/) — SRv6 is a traffic engineering, encapsulation and steering mechanism
   utilizing IPv6 addresses to identify segments in a pre-defined
   policy.  This document discusses security considerations in SRv6
   networks, including the potential threats and the possible mitigation
   methods.  The document does not define any new security protocols or
   extensions to existing protocols.
- **draft-ietf-v6ops-ipv6-only-04** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
- **draft-jennings-moq-uri-00** (new-draft, score 0, ignored_after_review) [none]: [MOQT URI and Discovery](https://datatracker.ietf.org/doc/draft-jennings-moq-uri/) — This document defines the moqt URI scheme, URI resolution mechanisms,
   and discovery methods for the Media over QUIC Transport (MOQT)
   protocol.  It specifies the URI syntax, fragment identifiers,
   dereferencing procedures, normalization rules, and X.509 certificate
   matching for moqt URIs.  It also defines DNS-based resolution using
   SVCB and SRV records, as well as local network discovery via mDNS and
   DNS-SD.
- **draft-knodel-nomcom-gender-representation-05** (new-draft, score 0, ignored_after_review) [none]: [Gender Representation in the IETF Nominating Committees](https://datatracker.ietf.org/doc/draft-knodel-nomcom-gender-representation/) — This document extends the existing limit on nomcom representation by
   organization ([RFC8713], Section 4.17) so that not all voting members
   of the IETF Nominating Committee (nomcom) belong to the same gender.
   It guarantees up to three voting seats to volunteers who opt into a
   self-declared pool, and changes the selection only in years when a
   plain random draw would seat fewer.
- **draft-koo-dtn-traceroute-eb-02** (new-draft, score 0, ignored_after_review) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block (TREB) for Bundle
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
- **draft-levine-dnsextlang-15** (new-draft, score 0, ignored_after_review) [none]: [An Extension Language for the DNS](https://datatracker.ietf.org/doc/draft-levine-dnsextlang/) — Adding new RRTYPEs to the DNS has required that DNS servers and
   provisioning software be upgraded to support each new RRTYPE in
   Master files.  This document defines a DNS extension language
   intended to allow most new RRTYPEs to be supported by adding entries
   to configuration data read by the DNS software, with no software
   changes needed for each RRTYPE.
- **draft-linker-diem-adem-dns-01** (new-draft, score 0, ignored_after_review) [none]: [ADEM - Distribution and Discovery over DNS](https://datatracker.ietf.org/doc/draft-linker-diem-adem-dns/) — TODO Abstract
- **draft-ma-v6ops-5g-ipv6only-05** (new-draft, score 0, ignored_after_review) [v6ops]: [Considerations of IPv6-only Deployment in 5G Mobile Networks](https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/) — This document describes a practical guide of deploying 464XLAT based
   IPv6-only technology on user plane in 3GPP 5G networks.  It also
   covers key 5G concepts and architectures, configuration methods and
   operational challenges.
- **draft-martin-retry-over-ipv6-05** (new-draft, score 0, ignored_after_review) [none]: [HTTP Signaling of Planned IPv4 Unavailability](https://datatracker.ietf.org/doc/draft-martin-retry-over-ipv6/) — As operators transition services to IPv6-only, planned IPv4 outages
   help identify remaining dependencies before permanent decommission.
   Such outages must be measurable, reversible, and understandable to
   end users.  This document defines HTTP signaling for an intentional,
   often time-bounded IPv4 outage: the existing 503 Service Unavailable
   status code together with the mandatory Retry-Over-IPv6 response
   header field (and optional related fields) that instruct aware
   clients to retry over IPv6 after closing the IPv4 connection, and
   allow clients to confirm successful IPv6 recovery via an optional
   correlation token so operators can distinguish soft failures from
   hard failures in centralized logs.  Machine-readable response bodies
   MAY use Problem Details (RFC 9457) with a registered problem type
   URI.  The mechanism supports staged enterprise rollouts, internal
   HTTP services, and permanent IPv6-only migration; coordinated public
   events (for example, 6/6 drills) remain possible with advance notice.
   The primary intended deployment is operator-controlled environments
   where provider and users share operational responsibility.  Legacy
   clients that do not implement this specification treat the response
   as ordinary service unavailability and MAY use the response body for
   human-readable guidance.
- **draft-newbold-atp-aturi-00** (new-draft, score 0, ignored_after_review) [none]: [The "at" URI Scheme](https://datatracker.ietf.org/doc/draft-newbold-atp-aturi/) — This document defines the "at" URI scheme, which is used to reference
   accounts and data records in the Authenticated Transfer Protocol.
- **draft-preussmattsson-tls-mlkem1024-x448-00** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Hybrid ML-KEM-1024/X448 Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-preussmattsson-tls-mlkem1024-x448/) — This document defines a post-quantum/traditional hybrid key exchange
   algorithm for TLS 1.3 that combines ML-KEM-1024 with X448:
   MLKEM1024X448.  The algorithm provides a hybrid key exchange option
   targeting a higher security level than X25519MLKEM768, matching the
   security level of AES-256 and ChaCha20.  A large security margin can
   protect against future cryptanalytic advances, misuse, and
   implementation errors.  Compared with P-curves offering a similar
   security level, X448 is significantly faster and provides greater
   implementation robustness.  A FIPS-validated implementation of
   MLKEM1024X448 ensures that the ML-KEM-1024 component is FIPS-
   validated.  The algorithm defined in this document is intended for
   use with TLS 1.3, DTLS 1.3, and QUIC and follows the general hybrid
   key exchange construction defined for TLS 1.3.
- **draft-prz-lsr-ash-packets-07** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-przygienda-lsr-fast-flooding-rtx-indication-00** (new-draft, score 0, ignored_after_review) [none]: [Retransmission Indication for IS-IS Fast Flooding](https://datatracker.ietf.org/doc/draft-przygienda-lsr-fast-flooding-rtx-indication/) — [RFC9681] defines a Flooding Parameters TLV.  Among other things, it
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
   mandatory-to-implement reaction to observed retransmission, fast
   flooding at scale can degenerate into sustained retransmission storms
   that serve only to keep the window full.

   This document specifies a local backoff.  A node SHOULD reduce the
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
- **draft-rsalz-4086bis-00** (new-draft, score 0, ignored_after_review) [none]: [On Random Numbers](https://datatracker.ietf.org/doc/draft-rsalz-4086bis/) — Things have changed a great deal in the two decades since RFC 4086,
   "Randomness Requirements for Security," was published.  In addition,
   as more IETF protocols use cryptography, the need for good-quality
   randomness has greatly increased.

   Copy from 4086 ?

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/richsalz/ietf-4086bis.
- **draft-sharma-moq-end-to-end-delivery-timeout-00** (new-draft, score 0, ignored_after_review) [none]: [End-to-End Delivery Timeouts for MOQT](https://datatracker.ietf.org/doc/draft-sharma-moq-end-to-end-delivery-timeout/) — This document defines an end-to-end Object delivery timeout for Media
   over QUIC Transport (MOQT).  It uses Object timestamps to include
   delay accumulated across a chain of relays instead of restarting the
   timeout at each hop.
- **draft-skoglund-epp-registry-lock-01** (new-draft, score 0, ignored_after_review) [none]: [Registry Lock Extension for the Extensible Provisioning Protocol (EPP)](https://datatracker.ietf.org/doc/draft-skoglund-epp-registry-lock/) — This document describes an Extensible Provisioning Protocol (EPP)
   extension for setting and managing a registry lock on a domain
   object.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-skoglund-epp-registry-lock/.

   Source for this draft and an issue tracker can be found at
   https://github.com/EricIO/draft-regext-epp-registry-lock.
- **draft-skyfire-oauth-aml-methods-01** (new-draft, score 0, ignored_after_review) [none]: [Anti-Money Laundering Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-aml-methods/) — Financial regulations require application of Anti-Money Laundering
   (AML) and Countering the Financing of Terrorism (CFT) methods in many
   jurisdictions worldwide.  This specification defines a claim and
   values for declaring what AML/CFT methods were employed.
- **draft-soumplis-nmop-kpi-semantics-00** (new-draft, score 0, ignored_after_review) [none]: [Operational KPI Semantics for Closed-Loop Edge-Cloud Services](https://datatracker.ietf.org/doc/draft-soumplis-nmop-kpi-semantics/) — Closed-loop management of IP-connected edge-cloud services depends on
   measurements that retain their meaning across collectors, processing
   pipelines, and administrative domains.  A metric name and numeric
   value are insufficient to determine whether a measurement can be
   compared, combined, or used at a particular decision time.  This
   document proposes a compact operational profile connecting KPI
   definitions to observation scope, statistical populations, time
   windows, freshness, and data-quality evidence.  It supplies
   calculation conventions for five KPI families, a consumer eligibility
   procedure, and worked examples.  The profile is intended to
   complement existing telemetry and metric-definition mechanisms.  It
   introduces no transport protocol, YANG module, or IANA registration.
- **draft-sriram-savnet-intrasav-solution-00** (new-draft, score 0, ignored_after_review) [none]: [IntraSAV - A Solution for Intra-Domain Source Address Validation](https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/) — This document specifies a solution, named IntraSAV, for intra-domain
   source address validation (SAV).  This solution addresses the problem
   stated in the ietf-savnet-intra-domain-problem-statement (RFC-to-be)
   document.  This document updates BCP 38 ([RFC2827]) and BCP 84
   ([RFC3704], [RFC8704]) by providing a more comprehensive solution
   methodology and accommodating prefixes that are not routed but used
   for sourcing traffic originating from an AS.
- **draft-tishkin-hmtp-00** (new-draft, score 0, ignored_after_review) [none]: [HTTP Mail Transfer Protocol](https://datatracker.ietf.org/doc/draft-tishkin-hmtp/) — This document specifies the HTTP Mail Transfer Protocol (HMTP), a
   protocol for the submission and transfer of Internet mail over HTTPS.
   HMTP covers both the submission of messages by clients to their mail
   service and the transfer of messages between mail servers.  Each
   message is carried unmodified in the existing Internet Message Format
   inside a JSON envelope that holds the information needed for
   delivery.  Large messages and attachments can be transferred by
   reference, with their integrity protected by cryptographic hashes.
   Requests are authenticated by signatures bound to the sending domain,
   using keys published with the DomainKeys Identified Mail (DKIM) key
   publication mechanism, which allows receivers to identify senders
   independently of their IP addresses.  Servers discover HMTP endpoints
   through DNS.  To allow incremental deployment alongside existing mail
   infrastructure, a server can optionally fall back to the Simple Mail
   Transfer Protocol (SMTP) when a peer does not support HMTP.
- **draft-wkumari-not-a-draft-26** (new-draft, score 0, ignored_after_review) [none]: [Just because it's an Internet-Draft doesn't mean anything... at all...](https://datatracker.ietf.org/doc/draft-wkumari-not-a-draft/) — Anyone can publish an Internet Draft (ID).  This doesn't mean that
   the "IETF thinks" or that "the IETF is planning..." or anything
   similar.
- **draft-xiao-v6ops-eds-02** (new-draft, score 0, ignored_after_review) [none]: [Enhanced Dual Stack: Connectivity-Informed IPv6/IPv4 Selection](https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/) — This document describes Enhanced Dual Stack (EDS), a framework
   intended to reduce the operational risk and upfront workload of
   introducing IPv6 into an existing IPv4 network.  EDS consists of two
   complementary mechanisms.  First, connectivity-informed destination
   selection updates Rule 6 of RFC 6724 Section 6 from "Prefer higher
   precedence" to "Prefer higher precedence unless recently failed", so
   that recently failed IPv6 connectivity is not repeatedly preferred
   over IPv4.  Second, operational diagnostics provide information that
   helps network administrators understand why IPv6 was not used and
   identify problems that can be corrected over time.  With these
   mechanisms, IPv6 deployment can move from extensive upfront
   validation toward practical upfront validation followed by gradual
   operational improvement.  This simpler IPv6 introduction approach can
   enable enterprises that do not have much IPv6 expertise and do not
   need a large number of IP addresses provided by IPv6 to try IPv6.
- **draft-yuki-ossification-cases-00** (new-draft, score 0, ignored_after_review) [none]: [Cases of Protocol Ossification on the Internet](https://datatracker.ietf.org/doc/draft-yuki-ossification-cases/) — This document catalogues cases of protocol ossification.  Protocol
   ossification is a phenomenon in which a new protocol, version, or
   extension cannot traverse an existing Internet path; such problems
   have been discovered and reported during protocol standardization and
   deployment.

   This document summarizes the reported observations and sources for
   those cases, together with case-specific responses.

## Errors / fetch failures

_None._
